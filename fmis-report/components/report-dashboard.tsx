"use client"

import { useCallback, useEffect, useMemo, useState } from "react"
import Image from "next/image"
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs"
import { Button } from "@/components/ui/button"
import { Filter as FilterIcon, XCircle, CalendarDays } from "lucide-react"

import { Row, Summary } from "@/lib/types";



import { MultiSelect } from "@/components/dashboard/multi-select"
import { OverviewKpis } from "@/components/dashboard/overview-kpis"
import { LevelBar } from "@/components/dashboard/level-bar"
import { MonthlyComparison } from "@/components/dashboard/monthly-comparison"
import { MonthlyTrends } from "@/components/dashboard/monthly-trends"
import { EntityBar } from "@/components/dashboard/entity-bar"
import { TypeDistributionAll } from "@/components/dashboard/type-distribution-all"
import { InactiveListTableSimple } from "@/components/dashboard/inactive-list-table-simple"
import { InactiveListTable } from "@/components/dashboard/inactive-list-table"
import { ListTable } from "@/components/dashboard/list-table"
import { KpisBlock } from "@/components/dashboard/kpis-block"
import { TypeBar } from "@/components/dashboard/type-bar"
import { YearlyComparisonBar } from "@/components/dashboard/yearly-comparison-bar"

const MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
const PAGE_SIZE = 200

export function ReportDashboard() {
  const [activeTab, setActiveTab] = useState<"overview" | "reports" | "queries">("overview")
  const [levels, setLevels] = useState<string[]>([])
  const [entities, setEntities] = useState<string[]>([])
  const [months, setMonths] = useState<string[]>([])
  const [years, setYears] = useState<string[]>([])
  const [codes, setCodes] = useState<string[]>([])

  const [summary, setSummary] = useState<Summary | null>(null)
  const [rows, setRows] = useState<Row[]>([])
  const [totalRows, setTotalRows] = useState(0)
  const [hasMore, setHasMore] = useState(false)
  const [page, setPage] = useState(0)

  const [loadingSummary, setLoadingSummary] = useState(false)
  const [loadingRows, setLoadingRows] = useState(false)
  const [error, setError] = useState<string | null>(null)
  const [searchTerm, setSearchTerm] = useState("")

  const clearAll = () => {
    setLevels([]); setEntities([]); setMonths([]); setYears([]); setCodes([]); setSearchTerm("")
  }

  // buildParams (rows + summary)
  const buildParams = useCallback((mode: "summary" | "rows", opts?: { offset?: number; limit?: number }) => {
    const params = new URLSearchParams()
    params.set("mode", mode)
    if (activeTab === "reports") params.set("type", "Report")
    else if (activeTab === "queries") params.set("type", "Query")

    const appendArr = (key: string, arr: string[]) => arr.forEach(v => params.append(key, v))
    if (levels.length) appendArr("level", levels)
    if (entities.length) appendArr("entity", entities)
    if (months.length) appendArr("month", months)
    if (years.length) years.map(y => String(y)).forEach(y => params.append("year", y))
    if (codes.length) appendArr("code", codes)

    if (mode === "rows") {
      params.set("offset", String(opts?.offset ?? 0))
      params.set("limit", String(opts?.limit ?? PAGE_SIZE))
      // free-text search BEFORE pagination
      if (searchTerm.trim()) params.set("q", searchTerm.trim())
    }

    return params
  }, [activeTab, levels, entities, months, years, codes, searchTerm])

  useEffect(() => { setRows([]); setPage(0) }, [activeTab, levels, entities, months, years, codes, searchTerm])

  // load summary
  useEffect(() => {
    const load = async () => {
      try {
        setLoadingSummary(true)
        const res = await fetch(`/api/data?${buildParams("summary").toString()}`, { cache: "no-store" })
        const json = await res.json()
        if (!res.ok) throw new Error((json as { error?: string })?.error || "Failed to load summary")
        setSummary(json as Summary)
      } catch (e) {
        setError(e instanceof Error ? e.message : "Failed to load summary")
      } finally {
        setLoadingSummary(false)
      }
    }
    load()
  }, [buildParams])

  useEffect(() => { setPage(0) }, [searchTerm])

  const fetchRows = useCallback(async (targetPage: number) => {
    try {
      setLoadingRows(true)
      const offset = targetPage * PAGE_SIZE
      const res = await fetch(`/api/data?${buildParams("rows", { offset, limit: PAGE_SIZE }).toString()}`, { cache: "no-store" })
      const json = await res.json() as { rows: Row[]; total: number; hasMore?: boolean }
      if (!res.ok) throw new Error((json as { error?: string })?.error || "Failed to load rows")

      const filtered = json.rows.filter(r => {
        if (!searchTerm) return true
        const t = searchTerm.toLowerCase()
        return (
          r.code.toLowerCase().includes(t) ||
          r.name.toLowerCase().includes(t) ||
          r.desc.toLowerCase().includes(t) ||
          r.user.toLowerCase().includes(t) ||
          r.entity.toLowerCase().includes(t)
        )
      })

      setRows(filtered)
      setTotalRows(json.total)
      setPage(targetPage)
      const computedHasMore = (targetPage * PAGE_SIZE) + json.rows.length < json.total
      setHasMore(typeof json.hasMore === "boolean" ? json.hasMore : computedHasMore)
    } catch (e) {
      setError(e instanceof Error ? e.message : "Failed to load rows")
    } finally {
      setLoadingRows(false)
    }
  }, [buildParams, searchTerm])

  useEffect(() => { fetchRows(0) }, [fetchRows])

  // --------- Derived data ----------
  const levelDistribution = summary?.levelDistribution ?? []
  const entityPerformance = summary?.entityPerformance ?? []
  const monthlyTrends = summary?.monthlyTrends ?? []
  const yearlyTotals = summary?.yearlyTotals ?? []
  const monthlyComparison = summary?.monthlyComparison ?? []
  const activeEntities = summary?.activeEntities ?? []
  const inactiveEntities = summary?.inactiveEntities ?? []
  const entitiesAll = summary?.entitiesAll ?? []
  const totalReports = summary?.totals.reports ?? 0
  const totalQueries = summary?.totals.queries ?? 0

  const reportTypeDistribution = summary?.reportTypeDistribution ?? []
  const queryTypeDistribution = summary?.queryTypeDistribution ?? []
  const inactiveReportTypes = summary?.inactiveReportTypes ?? []
  const inactiveQueryTypes = summary?.inactiveQueryTypes ?? []

  const yearsAll = (summary?.yearsAll ?? []).map(String)
  const coverageText = summary?.coverage?.text ?? "—"

  const [masterEntities, setMasterEntities] = useState<Array<{ code: string; label: string }>>([])
  useEffect(() => {
    const getMasters = async () => {
      const res = await fetch(`/api/data?mode=masters`, { cache: "force-cache" })
      if (!res.ok) return
      const json = await res.json()
      if (json.error) {
        setError(`Failed to load master data: ${json.error}`)
        return
      }
      setMasterEntities(json.entities ?? [])
    }
    getMasters()
  }, [])

  // Options
  const levelOptions = ["National Level", "Sub-National Level", "APE"]
  const entityOptions = masterEntities

  /** ⬇️ FIX: Build type options from backend master lists, sliced by tab.
   *  - Overview: combined (R* and Q*)
   *  - Reports : only R*
   *  - Queries : only Q*
   */
  const typeOptions = useMemo(() => {
    const master = summary?.masterCodes ?? []
    if (activeTab === "reports") return master.filter(c => c.startsWith("R"))
    if (activeTab === "queries") return master.filter(c => c.startsWith("Q"))
    return master // overview = combined
  }, [summary, activeTab])

  const typeLabel =
    activeTab === "reports" ? "Report Types"
      : activeTab === "queries" ? "Query Types"
        : "Report/Query Types"

  const monthOptions = MONTHS

  if (error) return <div className="p-6 text-red-500 text-lg">{error}</div>

  // dynamic subtitle for Level distribution
  const levelSubtitle =
    activeTab === "reports" ? "Reports by organizational level" :
      activeTab === "queries" ? "Queries by organizational level" :
        "Reports & queries by organizational level"

  const totalPages = Math.max(1, Math.ceil((totalRows || 0) / PAGE_SIZE))

  return (
    <div className="min-h-screen bg-background font-sans text-[16px]">
      <div className="container mx-auto px-4 sm:px-6 pt-4 sm:pt-6">
        {/* Header */}
        <div className="flex flex-col sm:flex-row items-start sm:items-center justify-between gap-2">
          <div className="w-full flex flex-col sm:flex-row items-center sm:items-start gap-2 sm:gap-4">
            <div className="text-center sm:text-left">
              <h1 className="text-2xl sm:text-3xl font-bold leading-tight tracking-tight text-emerald-900">
                📘 Report &amp; Query Analytics Dashboard
              </h1>
              <p className="text-base sm:text-lg text-emerald-800 mt-1">
                Report performance based on National, Sub-National, and APE levels.
              </p>
            </div>
          </div>

          {/* Coverage badge */}
          <div className="w-full sm:w-auto mt-4 sm:mt-0 flex flex-col sm:flex-row items-stretch sm:items-center gap-3">
            <div className="inline-flex items-center justify-center sm:justify-start gap-2 whitespace-nowrap rounded-lg bg-emerald-700 text-white px-4 py-3 text-lg md:text-lg font-semibold shadow">
              <CalendarDays className="h-4 w-4" />
              <span>Coverage:&nbsp;{coverageText}</span>
            </div>
          </div>
        </div>

        {/* Filters */}
        <div className="mt-4 sm:mt-6 rounded-xl border-2 border-emerald-200 bg-white shadow-sm">
          <div className="p-4 sm:p-6">
            <div className="flex items-center justify-between gap-2 flex-wrap mb-4">
              <h3 className="text-xl sm:text-2xl font-semibold text-emerald-800 m-0">Filters</h3>
              <div className="flex items-center gap-2">
                <Button size="sm" className="bg-emerald-600 hover:bg-emerald-600 text-white">
                  <FilterIcon className="h-4 w-4 mr-1" /> Apply Filters
                </Button>
                <Button size="sm" onClick={clearAll} variant="outline" className="border-emerald-400 text-emerald-600 hover:bg-emerald-50">
                  <XCircle className="h-4 w-4 mr-1" /> Clear All
                </Button>
              </div>
            </div>

            <div className="grid grid-cols-2 lg:grid-cols-5 gap-4 sm:gap-6">
              <MultiSelect label="Levels" options={levelOptions.map(o => ({ value: o, label: o }))} selected={levels} onChange={setLevels} />
              <MultiSelect label="Entities" options={entityOptions.map(e => ({ value: e.code, label: e.label }))} selected={entities} onChange={setEntities} />
              <MultiSelect
                label={typeLabel}
                options={typeOptions.map(o => ({ value: o, label: o }))}
                selected={codes}
                onChange={setCodes}
              />
              <MultiSelect label="Months" options={monthOptions.map(o => ({ value: o, label: o }))} selected={months} onChange={setMonths} />
              <MultiSelect label="Years" options={yearsAll.map(o => ({ value: o, label: o }))} selected={years} onChange={setYears} />
            </div>
          </div>
        </div>

        {loadingSummary && (<div className="text-base text-muted-foreground mt-3">Loading…</div>)}
      </div>

      <div className="container mx-auto px-4 sm:px-6 py-4 sm:py-6">
        <Tabs value={activeTab} onValueChange={(v) => setActiveTab(v as "overview" | "reports" | "queries")} className="w-full">
          <TabsList className="grid w-full grid-cols-3 mb-4 sm:mb-6">
            <TabsTrigger value="overview">Overview</TabsTrigger>
            <TabsTrigger value="reports">Reports</TabsTrigger>
            <TabsTrigger value="queries">Queries</TabsTrigger>
          </TabsList>

          {/* OVERVIEW */}
          <TabsContent value="overview" className="space-y-6">
            <OverviewKpis
              totalReports={totalReports}
              totalQueries={totalQueries}
              entityPerformance={entityPerformance}
              activeEntities={activeEntities}
              entitiesAll={entitiesAll}
            />

            <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
              <LevelBar title="Distribution by Level" subtitle={levelSubtitle} data={levelDistribution} mode="both" />
              <MonthlyTrends monthlyTrends={monthlyTrends} mode="both" />
            </div>

            <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
              <MonthlyComparison monthlyComparison={monthlyComparison} mode="both" isOverview={true} />
              <YearlyComparisonBar data={yearlyTotals} mode="both" />
            </div>

            <EntityBar entityPerformance={entityPerformance} mode="both" />

            <TypeDistributionAll
              reportData={reportTypeDistribution}
              queryData={queryTypeDistribution}
            />

            <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
              <InactiveListTableSimple title="Inactive Report Types" subtitle="Report types with no activity in current filters" items={inactiveReportTypes} itemHeader="Report Code" />
              <InactiveListTableSimple title="Inactive Query Types" subtitle="Query types with no activity in current filters" items={inactiveQueryTypes} itemHeader="Query Code" />
              <InactiveListTable title="Inactive Entities" subtitle="Entities with no activity in current filters" items={inactiveEntities} itemHeader="Entity Code" />
            </div>

            <ListTable
              rows={rows}
              page={page}
              pageSize={PAGE_SIZE}
              total={totalRows}
              hasMore={hasMore}
              loadingRows={loadingRows}
              onPrev={() => { if (page > 0 && !loadingRows) fetchRows(page - 1) }}
              onNext={() => { if (page + 1 < totalPages && !loadingRows) fetchRows(page + 1) }}
              totalPages={totalPages}
              searchTerm={searchTerm}
              onSearch={setSearchTerm}
              tab="All"
            />
          </TabsContent>

          {/* REPORTS */}
          <TabsContent value="reports" className="space-y-6">
            <KpisBlock
              title="Reports"
              totalPrimary={totalReports}
              entityPerformance={entityPerformance}
              activeEntities={activeEntities}
              entitiesAll={entitiesAll}
            />

            <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
              <LevelBar title="Distribution by Level" subtitle={levelSubtitle} data={levelDistribution} mode="reports" />
              <MonthlyTrends monthlyTrends={monthlyTrends} mode="reports" />
            </div>

            <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
              <MonthlyComparison monthlyComparison={monthlyComparison} mode="reports" />
              <YearlyComparisonBar data={yearlyTotals} mode="reports" />
            </div>

            <EntityBar entityPerformance={entityPerformance} mode="reports" />

            <TypeBar title="Report Type Distribution" data={reportTypeDistribution} barColor="#10b981" />

            <div className="grid grid-cols-1 xl:grid-cols-2 gap-6">
              <InactiveListTableSimple title="Inactive Report Types" subtitle="Report types with no activity in current filters" items={inactiveReportTypes} itemHeader="Report Code" />
              <InactiveListTable title="Inactive Entities" subtitle="Entities with no reports in current filters" items={inactiveEntities} itemHeader="Entity Code" />
            </div>

            <ListTable
              rows={rows}
              page={page}
              pageSize={PAGE_SIZE}
              total={totalRows}
              hasMore={hasMore}
              loadingRows={loadingRows}
              onPrev={() => { if (page > 0 && !loadingRows) fetchRows(page - 1) }}
              onNext={() => { if (page + 1 < totalPages && !loadingRows) fetchRows(page + 1) }}
              totalPages={totalPages}
              searchTerm={searchTerm}
              onSearch={setSearchTerm}
              tab="Report"
            />
          </TabsContent>

          {/* QUERIES */}
          <TabsContent value="queries" className="space-y-6">
            <KpisBlock
              title="Queries"
              totalPrimary={totalQueries}
              entityPerformance={entityPerformance}
              activeEntities={activeEntities}
              entitiesAll={entitiesAll}
            />

            <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
              <LevelBar title="Distribution by Level" subtitle={levelSubtitle} data={levelDistribution} mode="queries" />
              <MonthlyTrends monthlyTrends={monthlyTrends} mode="queries" />
            </div>

            <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
              <MonthlyComparison monthlyComparison={monthlyComparison} mode="queries" />
              <YearlyComparisonBar data={yearlyTotals} mode="queries" />
            </div>

            <EntityBar entityPerformance={entityPerformance} mode="queries" />

            <TypeBar title="Query Type Distribution" data={queryTypeDistribution} barColor="#3b82f6" />

            <div className="grid grid-cols-1 xl:grid-cols-2 gap-6">
              <InactiveListTableSimple title="Inactive Query Types" subtitle="Query types with no activity in current filters" items={inactiveQueryTypes} itemHeader="Query Code" />
              <InactiveListTable title="Inactive Entities" subtitle="Entities with no queries in current filters" items={inactiveEntities} itemHeader="Entity Code" />
            </div>

            <ListTable
              rows={rows}
              page={page}
              pageSize={PAGE_SIZE}
              total={totalRows}
              hasMore={hasMore}
              loadingRows={loadingRows}
              onPrev={() => { if (page > 0 && !loadingRows) fetchRows(page - 1) }}
              onNext={() => { if (page + 1 < totalPages && !loadingRows) fetchRows(page + 1) }}
              totalPages={totalPages}
              searchTerm={searchTerm}
              onSearch={setSearchTerm}
              tab="Query"
            />
          </TabsContent>
        </Tabs>
      </div>
    </div>
  )
}









