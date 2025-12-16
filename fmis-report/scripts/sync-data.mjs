import { Client } from "pg";
import * as XLSX from "xlsx";
import { fileURLToPath } from "url";
import { dirname } from "path";
import dotenv from "dotenv";

dotenv.config({ path: ".env.local" });

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

// helpers
import {
  norm,
  UP,
  keyFor,
  toNumber,
  monthNameToNum,
} from "../lib/utils.ts";

export async function syncData() {
  console.log("Starting data sync process...");

  process.env.NODE_TLS_REJECT_UNAUTHORIZED = "0";

  const connectionString = process.env.DATABASE_URL;
  if (!connectionString) {
    console.error("DATABASE_URL environment variable is not set.");
    process.exit(1);
  }

  console.log(
    "TLS verification disabled for sync-data (NODE_TLS_REJECT_UNAUTHORIZED=0, rejectUnauthorized=false)."
  );

  const client = new Client({
    connectionString,
    ssl: { rejectUnauthorized: false },
  });

  try {
    await client.connect();
    console.log("Connected to the database for data sync.");

    console.log('Clearing existing data from the rows table...');
    await client.query('TRUNCATE TABLE "rows" RESTART IDENTITY;');
    console.log('Existing data cleared.');

    const urls = [
      process.env.GOOGLE_SHEET_URL_2025,
      process.env.GOOGLE_SHEET_URL_2024,
      process.env.GOOGLE_SHEET_URL_2023,
      process.env.GOOGLE_SHEET_URL_2022,
      process.env.GOOGLE_SHEET_URL_2021,
    ].filter(Boolean);

    console.log(`Found ${urls.length} Google Sheet URLs to process.`);

    if (!urls.length) {
      console.log("No Google Sheet URLs found. Exiting sync.");
      return;
    }

    const allRows = [];

    for (const url of urls) {
      console.log("Fetching data from:", url);
      const response = await fetch(url);
      if (!response.ok) {
        console.error(
          `Failed to fetch Excel file from ${url}: ${response.status} ${response.statusText}`
        );
        continue;
      }

      const buf = await response.arrayBuffer();
      const wb = XLSX.read(buf, { type: "array" });
      const sheetName = wb.SheetNames[0];
      const ws = wb.Sheets[sheetName];
      const rowsA = XLSX.utils.sheet_to_json(ws, { header: 1 });

      console.log(`Loaded ${rowsA.length} rows from sheet "${sheetName}".`);

      if (!rowsA.length) continue;

      const [header, ...body] = rowsA;
      if (!header) continue;

      const idx = {};
      header.forEach((h, i) => {
        const k = keyFor(String(h));
        if (k && idx[k] == null) idx[k] = i;
      });

      // Force "count" to match real Excel column
      const headerLower = header.map((h) => String(h).trim().toLowerCase());
      const countIndex = headerLower.findIndex((h) => h === "count");
      if (countIndex !== -1) {
        idx["count"] = countIndex;
      }

      const needed = [
        "rq",
        "name",
        "desc",
        "count",
        "user",
        "level",
        "entity",
        "office",
        "ou",
        "year",
        "month",
        "day",
      ];

      const missing = needed.filter((k) => idx[k] == null);
      if (missing.length) {
        console.error(
          `Missing required columns in sheet "${sheetName}" from ${url}: ${missing.join(", ")}`
        );
        continue;
      }

      for (let i = 0; i < body.length; i++) {
        const r = body[i];
        if (!r || !r.length) continue;

        const get = (k) => r[idx[k]] ?? "";

        const rq = norm(get("rq"));
        const name = norm(get("name"));
        const desc = norm(get("desc"));
        const user = UP(get("user"));
        const level = norm(get("level"));
        const entity = UP(get("entity"));
        const office = UP(get("office"));
        const ou = UP(get("ou"));

        const year = toNumber(get("year")) ?? 0;
        const month = monthNameToNum(get("month")) ?? 0;
        const day = toNumber(get("day")) ?? 0;

        // ✔ KEEP COUNT EXACTLY AS RAW FROM GOOGLE SHEET
        const count = get("count");

        // Determine type
        const rqU = rq.toUpperCase();
        let type;
        if (rqU.includes("REPORT")) type = "Report";
        else if (rqU.includes("QUERY")) type = "Query";
        else if (name.toUpperCase().startsWith("Q")) type = "Query";
        else type = "Report";

        let rawCode = "";
        if (idx["code"] != null) {
          rawCode = norm(r[idx["code"]]);
        }

        const code = UP(rawCode || name || `${type}-${i + 1}`);

        allRows.push({
          rq,
          name,
          desc,
          count,
          user,
          level,
          entity,
          office,
          ou,
          year,
          month,
          day,
          type,
          code,
        });
      }
    }

    console.log(`Total parsed rows: ${allRows.length}`);

    if (!allRows.length) {
      console.log("No rows to insert.");
      return;
    }

    const esc = (s) => (s ?? "").toString().replace(/'/g, "''");
    const num = (n) => {
      const x = Number(n);
      return Number.isFinite(x) ? x : 0;
    };

    const chunkSize = 5000;

    for (let i = 0; i < allRows.length; i += chunkSize) {
      const chunk = allRows.slice(i, i + chunkSize);

      const values = chunk.map((r) => {
        return `(
          '${esc(r.rq)}',
          '${esc(r.name)}',
          '${esc(r.desc)}',
          '${esc(r.count)}',     -- RAW COUNT INSERTED
          '${esc(r.user)}',
          '${esc(r.level)}',
          '${esc(r.entity)}',
          '${esc(r.office)}',
          '${esc(r.ou)}',
          ${num(r.year)},
          ${num(r.month)},
          ${num(r.day)},
          '${esc(r.type)}',
          '${esc(r.code)}'
        )`;
      });

      const sql = `
        INSERT INTO "rows" (
          rq, name, "desc", count, "user", level, entity, office, ou,
          year, month, day, type, code
        )
        VALUES ${values.join(", ")};
      `;

      await client.query(sql);

      console.log(
        `Inserted ${chunk.length} rows (up to ${i + chunk.length}/${allRows.length}).`
      );
    }

    console.log("All rows inserted into rows table.");
    console.log("Data sync completed successfully.");
  } catch (err) {
    console.error("Error during data sync:", err);
    throw err;
  } finally {
    await client.end();
    console.log("Database connection closed (sync-data).");
  }
}

if (process.argv[1] === __filename) {
  syncData()
    .then(() => {
      console.log("Sync completed.");
      process.exit(0);
    })
    .catch((err) => {
      console.error("Sync failed:", err);
      process.exit(1);
    });
}
