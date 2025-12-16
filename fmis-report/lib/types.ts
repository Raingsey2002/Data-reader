export type Level = "National Level" | "Sub-National Level" | "APE";
export type Kind = "Report" | "Query";

export type Row = {
  rq: string;
  name: string;
  desc: string;
  count: number;
  user: string;
  level: Level;
  entity: string;
  office: string;
  ou: string;
  year: number;
  month: number;
  day: number;
  type: Kind;
  code: string;
};

export type MastersJSON = {
  entities: Array<{ code: string; level: Level; desc: string }>;
  reportTypes: string[];
  queryTypes: string[];
};

export type Summary = {
  totals: { reports: number; queries: number };
  levelDistribution: Array<{ name: Row["level"]; reports: number; queries: number; total: number }>;
  entityPerformance: Array<{ entity: string; reports: number; queries: number; total: number }>;
  monthlyTrends: Array<{ month: string; reports: number; queries: number }>;
  yearlyTotals: Array<{ year: number; reports: number; queries: number }>;
  monthlyComparison: Array<{ year: number; reports: number[]; queries: number[] }>;
  codes: string[];
  entities: Array<{ code: string; label: string }>;
  entitiesAll: Array<{ code: string; label: string }>;
  reportTypeDistribution: Array<{ name: string; value: number }>;
  queryTypeDistribution: Array<{ name: string; value: number }>;
  activeEntities: Array<{ code: string; label: string }>;
  inactiveEntities: Array<{ code: string; label: string }>;
  inactiveReportTypes: string[];
  inactiveQueryTypes: string[];
  yearsAll?: number[];
  coverage?: { text?: string };
  masterCodes?: string[];
};
