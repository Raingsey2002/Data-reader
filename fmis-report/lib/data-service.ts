import { Row, Level, Kind } from "./types";
import { UP } from "./utils";

export function applyFilters(
  rows: Row[],
  f: {
    levels?: string[];
    entities?: string[];
    months?: number[];
    years?: number[];
    codes?: string[];
    type?: Kind | "";
  }
) {
  let data = rows;
  if (f.type) data = data.filter((r) => r.type === f.type);
  if (f.levels && f.levels.length) {
    const set = new Set(f.levels);
    data = data.filter((r) => set.has(r.level));
  }
  if (f.entities && f.entities.length) {
    const set = new Set(f.entities.map(UP));
    // strict Entity filter (no office/OU fallback)
    data = data.filter((r) => set.has(UP(r.entity)));
  }
  if (f.months && f.months.length) {
    const set = new Set(f.months);
    data = data.filter((r) => set.has(r.month));
  }
  if (f.years && f.years.length) {
    const set = new Set(f.years);
    data = data.filter((r) => set.has(r.year));
  }
  if (f.codes && f.codes.length) {
    const set = new Set(f.codes.map(UP));
    data = data.filter((r) => set.has(r.code));
  }
  return data;
}

export function summarize(rows: Row[]) {
  let reports = 0,
    queries = 0;

  // per-level split
  const levelAgg = new Map<Level, { reports: number; queries: number; total: number }>();
  // per-entity split
  const entityAgg = new Map<string, { reports: number; queries: number; total: number }>();

  const monthCounts = Array.from({ length: 12 }, (_, i) => ({ m: i + 1, reports: 0, queries: 0 }));
  const userCounts = new Map<string, { reports: number; queries: number; total: number }>();
  const perCodeReport = new Map<string, number>();
  const perCodeQuery = new Map<string, number>();
  const activeReportCodes = new Set<string>();
  const activeQueryCodes = new Set<string>();
  const activeEntitiesSet = new Set<string>();
  const yearlyAgg = new Map<number, { reports: number; queries: number }>();

  rows.forEach((r) => {
    const isReport = r.type === "Report";
    if (isReport) {
      reports++;
      activeReportCodes.add(r.code);
    } else {
      queries++;
      activeQueryCodes.add(r.code);
    }

    // level split
    const lv = levelAgg.get(r.level) || { reports: 0, queries: 0, total: 0 };
    if (isReport) lv.reports++;
    else lv.queries++;
    lv.total++;
    levelAgg.set(r.level, lv);

    // entity split
    const ent = UP(r.entity);
    if (ent) {
      const ea = entityAgg.get(ent) || { reports: 0, queries: 0, total: 0 };
      if (isReport) ea.reports++;
      else ea.queries++;
      ea.total++;
      entityAgg.set(ent, ea);
      activeEntitiesSet.add(ent);
    }

    // months
    if (r.month >= 1 && r.month <= 12) {
      const mc = monthCounts[r.month - 1];
      if (isReport) mc.reports++;
      else mc.queries++;
    }

    // users
    const u = userCounts.get(r.user) || { reports: 0, queries: 0, total: 0 };
    if (isReport) u.reports++;
    else u.queries++;
    u.total++;
    userCounts.set(r.user, u);

    // type distributions
    if (isReport) perCodeReport.set(r.code, (perCodeReport.get(r.code) || 0) + 1);
    else perCodeQuery.set(r.code, (perCodeQuery.get(r.code) || 0) + 1);

    // yearly aggregation
    if (r.year) {
      const yearData = yearlyAgg.get(r.year) || { reports: 0, queries: 0 };
      if (isReport) yearData.reports++;
      else yearData.queries++;
      yearlyAgg.set(r.year, yearData);
    }
  });

  const monthlyComparison = new Map<number, { reports: number[]; queries: number[] }>();

  rows.forEach((r) => {
    if (r.year && r.month) {
      if (!monthlyComparison.has(r.year)) {
        monthlyComparison.set(r.year, {
          reports: Array(12).fill(0),
          queries: Array(12).fill(0),
        });
      }
      const yearData = monthlyComparison.get(r.year)!;
      if (r.type === "Report") {
        yearData.reports[r.month - 1]++;
      } else {
        yearData.queries[r.month - 1]++;
      }
    }
  });
  
  const levelDistribution = (["National Level", "Sub-National Level", "APE"] as Level[]).map((l) => {
    const agg = levelAgg.get(l as Level) || { reports: 0, queries: 0, total: 0 };
    return { name: l, reports: agg.reports, queries: agg.queries, total: agg.total };
  });

  const entityPerformance = [...entityAgg.entries()]
    .map(([entity, v]) => ({ entity, reports: v.reports, queries: v.queries, total: v.total }))
    .filter((e) => e.entity)
    .sort((a, b) => b.total - a.total)

  const monthlyTrends = monthCounts.map((m, i) => ({
    month: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"][i],
    reports: m.reports,
    queries: m.queries,
  }));

  const activeEntities = Array.from(activeEntitiesSet).sort();
  const codesAllPresent = [...new Set(rows.map((r) => r.code))].filter(Boolean).sort();

  const reportTypeDistribution = [...perCodeReport.entries()]
    .map(([name, value]) => ({ name, value }))
    .sort((a, b) => b.value - a.value)
    .slice(0, 50);

  const queryTypeDistribution = [...perCodeQuery.entries()]
    .map(([name, value]) => ({ name, value }))
    .sort((a, b) => b.value - a.value)
    .slice(0, 50);

  const yearlyTotals = Array.from(yearlyAgg.entries())
    .map(([year, data]) => ({ year, ...data }))
    .sort((a, b) => a.year - b.year);

  const monthlyComparisonData = Array.from(monthlyComparison.entries())
    .map(([year, data]) => ({ year, ...data }))
    .sort((a, b) => a.year - b.year);

  return {
    totals: { reports, queries },
    levelDistribution,
    entityPerformance,
    monthlyTrends,
    yearlyTotals,
    monthlyComparison: monthlyComparisonData,
    topUsers: [...userCounts.entries()]
      .map(([userId, v]) => ({ userId, ...v }))
      .sort((a, b) => b.total - a.total)
      .slice(0, 20),
    codes: codesAllPresent,
    entities: activeEntities,
    reportTypeDistribution,
    queryTypeDistribution,
    activeEntities,
    inactiveEntities: [],
    inactiveReportTypes: [],
    inactiveQueryTypes: [],
    entitiesAll: [],
    activeReportCodes: [...activeReportCodes].sort(),
    activeQueryCodes: [...activeQueryCodes].sort(),
  };
}