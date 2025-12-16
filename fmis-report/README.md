# FMIS Report Dashboard

A dashboard for exploring FMIS report/query activity from an Excel file. It provides KPIs, charts, inactive-lists, and a detailed table with fast filters (Level, Entity, Month, Type) for both **Reports** and **Queries**. Data is loaded from `public/main_data.xlsx` at runtime via a server API route.

## Features

* Three tabs: **Overview**, **Reports**, and **Queries** with independent filters.
* KPIs:

  * Total Generated (Reports + Queries)
  * Totals for Reports and Queries
  * Top Entity, Active/Inactive Entities
* Charts:

  * Distribution by Level (tab-aware, scrollable bar chart)
  * Monthly Trends (line chart; shows one line on tabs, two on Overview)
  * Top 10 Entities Performance (tab-aware vertical bar chart)
  * Type Distributions (scrollable; tab-specific and combined in Overview)
* **Inactive lists**:

  * Inactive Entities (by selected Level/Entity scope)
  * Inactive Report/Query Types (computed against master lists, respects current filters)
* Paginated **All Records / Report Records / Query Records** tables with:

  * Free-text search (server-side, applied before pagination — fixes mismatch issues)
  * Clear & Apply filter controls
  * Previous/Next pagination with coverage info
* Coverage banner showing data range (`Jan YYYY – Jul YYYY`).

## Tech Stack

* Next.js 15 (App Router)
* TypeScript
* Recharts (charts)
* shadcn/ui (cards, table, selects, dialogs)
* Lucide-react (icons)
* XLSX (Excel parsing) on the server API route
* `next/image` for optimized images (logo)
* Tailwind CSS for styling

## Project Structure (relevant)

```
/app/api/data/route.tsx          # API: loads Excel, filtering, master universes, summary/rows mode
/components/report-dashboard.tsx # UI: tabs, filters, KPIs, charts, inactive lists, table
/public/main_data.xlsx            # Source data (first sheet is read)
/public/masters.json              # Master lists for entities & report and query codes
/public/KantumruyPro-Medium.ttf   # Khmer font file
```

## Data Source & Column Mapping

The API reads `public/main_data.xlsx` (first sheet) and maps common header variants to internal fields. Expected columns (case/spacing tolerant):

* **Report/Query** → `rq`
* **Name of Report and Query** → `name` (also used as `code`)
* **Description** → `desc`
* **Count** → `count`
* **User ID** → `user`
* **Level** → `level` (`National Level` | `Sub-National Level` | `APE`)
* **Entity** → `entity`
* **Office** → `office`
* **Operating Unit** → `ou`
* **Year** → `year`
* **Month** → `month` (accepts names like “Jan”, “February” or numbers 1–12)

The API also derives:

* **type** → `"Report"` or `"Query"`
* **code** → normalized display/selection code
* **coverage** → min–max month/year range in the dataset
* **yearsAll** → all years available for filtering

Master universes used for inactivity & dropdowns:

* Entities (partitioned by Level)
* Report codes (`R01, R02, …`)
* Query codes (`Q01, Q02, …`)
  – loaded from `masters.json` if present, else inferred from data.

## Getting Started

1. **Install**

   ```bash
   npm i
   ```

2. **Place your data**

   * Put `main_data.xlsx` into `public/`.

   * (Optional) Place `masters.json` into `public/` to override master lists.

3. **Dev**

   ```bash
   npm run dev
   ```

4. **Build**

   ```bash
   npm run build
   npm start
   ```

5. **Run Sync data to Supabase**
   ```bash
   node scripts/sync-data.mjs  
   ```


## API

### `GET /api/data`

Two modes: `summary` (default) and `rows`.

#### Common query params

* `type`: `Report` | `Query` (tab context)
* `level`: `National Level` | `Sub-National Level` | `APE`
* `entity`: entity code(s)
* `month`: `1..12` or names (`Jan`, `February`)
* `year`: year(s)
* `code`: report/query code(s)
* `q`: free-text search (applies to `code`, `name`, `desc`, `user`, `entity` — rows mode only)

#### `mode=summary` response

* `totals: { reports, queries }`
* `levelDistribution`, `entityPerformance`, `monthlyTrends`
* `reportTypeDistribution`, `queryTypeDistribution`
* `codes`, `entities`, `entitiesAll`
* `activeEntities`, `inactiveEntities`
* `inactiveReportTypes`, `inactiveQueryTypes`
* `activeReportCodes`, `activeQueryCodes`
* `yearsAll`
* `coverage: { text }` (e.g., `"Jan 2021 – Jul 2025"`)

#### `mode=rows` response

* `rows`: filtered, searched, and paginated rows
* `total`: total count matching filters/search
* `hasMore`: whether another page exists
* Use `offset` & `limit` to paginate (UI uses 200/page)

## UI Behavior

* Changing **Level/Entity/Month/Type/Tab** refetches summary and resets table pagination.
* The **search box** now delegates to API `q` param — so results are accurate across all pages.
* **Inactive lists** respect current scope (Level, Entity, Type filters).
* Overview tab aggregates both Reports and Queries; Reports/Queries tabs show type-specific KPIs, charts, and tables.

## Troubleshooting

* **No results in All Records after search**
  Ensure you’re on the latest version — the free-text search (`q`) now runs server-side before pagination.
* **Empty charts / zero counts**
  Check your Excel headers match expected logical fields.
* **Missing masters.json**
  The app falls back to inferring codes/entities from the dataset.
* **Khmer text not displaying correctly**
  The project now includes a local font file `KantumruyPro-Medium.ttf` to ensure proper rendering of Khmer text. If you are still having issues, please ensure your browser is not blocking local font loading.