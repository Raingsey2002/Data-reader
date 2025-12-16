"use client"

import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"
import { FileSpreadsheet, Users, Building2 } from "lucide-react"

export function OverviewKpis({
  totalReports,
  totalQueries,
  entityPerformance,
  activeEntities,
  entitiesAll,
}: {
  totalReports: number
  totalQueries: number
  entityPerformance: Array<{ entity: string; reports: number; queries: number; total: number }>
  activeEntities: Array<{ code: string; label: string }>;
  entitiesAll: Array<{ code: string; label: string }>;
}) {
  const topEntity = (entityPerformance?.[0]?.entity) ?? "—"
  const totalGenerated = (totalReports + totalQueries)

  return (
    <div className="grid grid-cols-1 md:grid-cols-5 gap-4 sm:gap-6 mb-2 sm:mb-6">
      {/* NEW: Total Generated */}
      <Card>
        <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
          <CardTitle className="text-lg font-medium">Total Generated</CardTitle>
          <FileSpreadsheet className="h-4 w-4 text-primary" />
        </CardHeader>
        <CardContent>
          <div className="text-3xl font-bold text-primary">{totalGenerated.toLocaleString()}</div>
          <p className="text-sm text-muted-foreground">reports + queries</p>
        </CardContent>
      </Card>

      <Card>
        <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
          <CardTitle className="text-lg font-medium">Total Reports</CardTitle>
          <FileSpreadsheet className="h-4 w-4 text-muted-foreground" />
        </CardHeader>
        <CardContent>
          <div className="text-3xl font-bold text-primary">{totalReports.toLocaleString()}</div>
          <p className="text-sm text-muted-foreground">reports generated</p>
        </CardContent>
      </Card>

      <Card>
        <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
          <CardTitle className="text-lg font-medium">Total Queries</CardTitle>
          <FileSpreadsheet className="h-4 w-4 text-muted-foreground" />
        </CardHeader>
        <CardContent>
          <div className="text-3xl font-bold text-primary">{totalQueries.toLocaleString()}</div>
          <p className="text-sm text-muted-foreground">queries generated</p>
        </CardContent>
      </Card>

      <Card>
        <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
          <CardTitle className="text-lg font-medium">Top Entity</CardTitle>
          <Building2 className="h-4 w-4 text-primary" />
        </CardHeader>
        <CardContent>
          <div className="text-2xl font-bold text-primary">{topEntity}</div>
          <p className="text-sm text-muted-foreground">Most active entity</p>
        </CardContent>
      </Card>

      <Card>
        <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
          <CardTitle className="text-lg font-medium">Active Entities</CardTitle>
          <Users className="h-4 w-4 text-emerald-500" />
        </CardHeader>
        <CardContent>
          <div className="text-2xl font-bold text-emerald-600">{activeEntities.length}</div>
          <p className="text-sm text-muted-foreground">of {entitiesAll.length} total</p>
        </CardContent>
      </Card>
    </div>
  )
}
