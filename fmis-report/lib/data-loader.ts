import { Client } from "pg";
import path from "node:path";
import fs from "node:fs";
import { Row, Level, MastersJSON } from "./types";
import { UP, MONTHS } from "./utils";

type State = {
  ready: boolean;
  rows: Row[];
  masterByLevel: Record<Level, Array<{ code: string; label: string }>>;
  masterReports: string[];
  masterQueries: string[];
  masterEntities: Array<{ code: string; label: string }>;
  coverage: {
    minYM?: { d: number; y: number; m: number };
    maxYM?: { d: number; y: number; m: number };
    text?: string;
  };
  yearsAll: number[];
  loadingError?: string | null;
};

const STATE: State = {
  ready: false,
  rows: [],
  masterByLevel: {
    "National Level": [],
    "Sub-National Level": [],
    APE: [],
  },
  masterReports: [],
  masterQueries: [],
  masterEntities: [],
  coverage: {},
  yearsAll: [],
  loadingError: null,
};

let loadingPromise: Promise<void> | null = null;

function tryReadJSONMasters(): MastersJSON | null {
  try {
    const p = path.join(process.cwd(), "public", "masters.json");
    const raw = fs.readFileSync(p, "utf8");
    const parsed = JSON.parse(raw) as MastersJSON;
    if (!parsed || !Array.isArray(parsed.entities)) {
      STATE.loadingError = "masters.json was read but is either not a valid JSON object or is missing the 'entities' array.";
      console.error(STATE.loadingError);
      return null;
    }
    return parsed;
  } catch (error) {
    const errorMessage = error instanceof Error ? error.message : String(error);
    STATE.loadingError = `Failed to read or parse masters.json: ${errorMessage}`;
    console.error(STATE.loadingError);
    return null;
  }
}

async function _doLoad(): Promise<void> {
  const connectionString = process.env.DATABASE_URL;
  if (!connectionString) {
    console.error("DATABASE_URL environment variable is not set.");
    throw new Error("DATABASE_URL environment variable is not set.");
  }

  let ssl: { rejectUnauthorized: boolean; ca?: string } = { rejectUnauthorized: false };
  if (process.env.POSTGRES_CA_CERT) {
    const ca = process.env.POSTGRES_CA_CERT.replace(/\\n/g, "\n").trim();
    ssl = {
      ca,
      rejectUnauthorized: true,
    };
    console.log("Using custom Postgres CA certificate from POSTGRES_CA_CERT.");
  } else {
    console.log("POSTGRES_CA_CERT not set, using insecure SSL.");
  }

  const client = new Client({
    connectionString,
    ssl,
  });

  try {
    await client.connect();
    console.log("Connected to the database for data loading.");
    await client.query("SET statement_timeout = 600000");

    const res = await client.query<Row>(
      'SELECT rq, name, "desc", count, "user", level, entity, office, ou, year, month, day, type, code FROM rows'
    );
    STATE.rows = res.rows;
    console.log(`Total rows loaded from database: ${STATE.rows.length}`);

    if (STATE.rows.length > 0) {
      const dym = STATE.rows
        .filter((r) => r.year && r.month && r.day)
        .map((r) => ({ y: r.year, m: r.month, d: r.day }))
        .sort((a, b) => {
          if (a.y !== b.y) return a.y - b.y;
          if (a.m !== b.m) return a.m - b.m;
          return a.d - b.d;
        });

      if (dym.length > 0) {
        STATE.coverage.minYM = dym[0];
        STATE.coverage.maxYM = dym[dym.length - 1];
        const minDay = String(STATE.coverage.minYM.d).padStart(2, "0");
        const maxDay = String(STATE.coverage.maxYM.d).padStart(2, "0");
        const minMonth = MONTHS[(STATE.coverage.minYM.m || 1) - 1];
        const maxMonth = MONTHS[(STATE.coverage.maxYM.m || 1) - 1];
        STATE.coverage.text = `${minDay} ${minMonth} ${STATE.coverage.minYM.y} – ${maxDay} ${maxMonth} ${STATE.coverage.maxYM.y}`;
      }
    }

    STATE.yearsAll = Array.from(
      new Set(STATE.rows.map((r) => r.year).filter(Boolean))
    ).sort((a, b) => a - b);

    const masters = tryReadJSONMasters();
    if (masters) {
      const byLevel: Record<Level, Array<{ code: string; label: string }>> = {
        "National Level": [],
        "Sub-National Level": [],
        APE: [],
      };
      const allEntities: Array<{ code: string; label: string }> = [];

      for (const e of masters.entities) {
        const lvl = e.level as Level;
        const code = UP(e.code);
        const label = `${code} - ${e.desc}`;
        if (byLevel[lvl] && code) byLevel[lvl].push({ code, label });
        allEntities.push({ code, label });
      }

      (Object.keys(byLevel) as Level[]).forEach((l) => {
        byLevel[l] = byLevel[l].sort((a, b) => a.code.localeCompare(b.code));
      });

      STATE.masterByLevel = byLevel;
      STATE.masterEntities = allEntities.sort((a, b) =>
        a.code.localeCompare(b.code)
      );

      STATE.masterReports = (masters.reportTypes || []).map(UP).sort();
      STATE.masterQueries = (masters.queryTypes || []).map(UP).sort();
    } else {
      STATE.masterReports = Array.from(
        new Set(
          STATE.rows
            .filter((r) => r.type === "Report")
            .map((r) => UP(r.code))
        )
      ).sort();

      STATE.masterQueries = Array.from(
        new Set(
          STATE.rows
            .filter((r) => r.type === "Query")
            .map((r) => UP(r.code))
        )
      ).sort();

      STATE.masterEntities = Array.from(
        new Set(STATE.rows.map((r) => r.entity).filter(Boolean))
      )
        .map(e => ({ code: e, label: e }))
        .sort((a, b) => a.code.localeCompare(b.code));
    }

    STATE.ready = true;
  } catch (error) {
    console.error("Error in data loading process from database:", error);
    throw error;
  } finally {
    await client.end();
    console.log("Database connection closed (data loader).");
  }
}

function ensureLoaded(): Promise<void> {
  if (STATE.ready) {
    return Promise.resolve();
  }
  if (loadingPromise) {
    return loadingPromise;
  }
  loadingPromise = _doLoad().catch((err) => {
    loadingPromise = null;
    return Promise.reject(err);
  });
  return loadingPromise;
}

export async function getLoadedData() {
  await ensureLoaded();
  return STATE;
}