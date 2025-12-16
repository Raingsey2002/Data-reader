import { NextRequest, NextResponse } from "next/server";
import { getLoadedData } from "@/lib/data-loader";
import { applyFilters, summarize } from "@/lib/data-service";
import { Kind, Level, Row } from "@/lib/types";
import { monthNameToNum, UP } from "@/lib/utils";

export async function GET(req: NextRequest) {
  try {
    const STATE = await getLoadedData();

    const { searchParams } = new URL(req.url);
    const mode = searchParams.get("mode") || "summary";
    const typeParam = searchParams.get("type");
    const type: Kind | null = typeParam === "Report" || typeParam === "Query" ? typeParam : null;

    const getMulti = (key: string) => {
      const all = searchParams.getAll(key).flatMap((v) =>
        String(v)
          .split(",")
          .map((s) => s.trim())
          .filter(Boolean)
      );
      return Array.from(new Set(all));
    };
    const levels = getMulti("level") as Level[];
    const entityFilterRaw = getMulti("entity");
    const months = getMulti("month")
      .map((v) => (Number.isNaN(parseInt(v)) ? monthNameToNum(v) : parseInt(v)))
      .filter((n) => Number.isFinite(n) && n >= 1 && n <= 12) as number[];
    const years = getMulti("year").map((v) => Number(v)).filter((n) => Number.isFinite(n)) as number[];
    const codes = getMulti("code");


    if (mode === "masters") {
      return NextResponse.json({
        entities: STATE.masterEntities,
        levels: Object.keys(STATE.masterByLevel),
        error: STATE.loadingError || null,
      })
    }

    const filtered = applyFilters(STATE.rows, {
      levels: levels.length ? levels : undefined,
      entities: entityFilterRaw.length ? entityFilterRaw : undefined,
      months: months.length ? months : undefined,
      years: years.length ? years : undefined,
      codes: codes.length ? codes : undefined,
      type: (type ?? "") as Kind | "",
    });

    if (mode === "summary") {
      const s = summarize(filtered);

      // --- FLEXIBLE UNIVERSE (respects Levels) ---
      const byLevel = STATE.masterByLevel;
      const selectedLevels: Level[] = levels.length ? (levels as Level[]) : (["National Level", "Sub-National Level", "APE"] as Level[]);

      // union of masters for selected levels
      const masterUniverse = Array.from(new Set(selectedLevels.flatMap((l) => byLevel[l] || []).map(e => e.code)));

      // ===== Scoped “inactive” logic =====
      const selectedEntitiesUniverseCodes = entityFilterRaw.length ? Array.from(new Set(entityFilterRaw.map(UP))).sort() : masterUniverse;

      const entitiesAll = STATE.masterEntities.filter(e => selectedEntitiesUniverseCodes.includes(e.code));
      const activeEntities = s.activeEntities.map(code => entitiesAll.find(e => e.code === code)).filter(Boolean);
      const inactiveEntities = entitiesAll.filter(e => !s.activeEntities.includes(e.code));

      const masterCodes =
        type === "Report"
          ? STATE.masterReports
          : type === "Query"
          ? STATE.masterQueries
          : Array.from(new Set([...STATE.masterReports, ...STATE.masterQueries])).sort();

      // Codes selection scoping (if user selected types/codes)
      const upCodes = codes.map(UP);
      const selectedReportUniverse = upCodes.length ? STATE.masterReports.filter((c) => upCodes.includes(c)) : STATE.masterReports;
      const selectedQueryUniverse = upCodes.length ? STATE.masterQueries.filter((c) => upCodes.includes(c)) : STATE.masterQueries;

      const inactiveReportTypes = selectedReportUniverse.filter((c) => !s.activeReportCodes.includes(c));
      const inactiveQueryTypes = selectedQueryUniverse.filter((c) => !s.activeQueryCodes.includes(c));

      return NextResponse.json(
        {
          ...s,
          activeEntities,
          inactiveEntities,
          entitiesAll,
          inactiveReportTypes,
          inactiveQueryTypes,
          yearsAll: STATE.yearsAll,
          coverage: { text: STATE.coverage.text },
          masterCodes,
        },
        { headers: { "Cache-Control": "no-store" } }
      );
    }

    // -------- rows mode with FREE-TEXT SEARCH (q) BEFORE pagination --------
    const q = (searchParams.get("q") || "").trim().toLowerCase();
    const hay = (x: unknown) => String(x ?? "").toLowerCase();
    const contains = (r: Row) =>
      hay(r.code).includes(q) ||
      hay(r.name).includes(q) ||
      hay(r.desc).includes(q) ||
      hay(r.user).includes(q) ||
      hay(r.entity).includes(q);

    const filteredWithQ = q ? filtered.filter(contains) : filtered;

    const offset = Math.max(0, Number(searchParams.get("offset") || 0));
    const limit = Math.min(Math.max(1, Number(searchParams.get("limit") || 500)), 2000);
    const slice = filteredWithQ.slice(offset, offset + limit);
    const hasMore = offset + limit < filteredWithQ.length;

    return NextResponse.json({ rows: slice, total: filteredWithQ.length, hasMore }, { headers: { "Cache-Control": "no-store" } });
  } catch (e) {
    return NextResponse.json({ error: e instanceof Error ? e.message : "Unknown error" }, { status: 500 });
  }
}
