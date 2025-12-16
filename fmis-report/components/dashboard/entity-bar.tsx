"use client"

import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"
import {
  BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer,
  LabelList
} from "recharts"
import { CustomTooltip } from "./custom-tooltip"

/* Top 10 Entities – tab-aware series & labels */
export function EntityBar({
  entityPerformance,
  mode = "both",
}:{
  entityPerformance: Array<{ entity: string; reports: number; queries: number; total: number }>
  mode?: "both" | "reports" | "queries"
}) {
  const data = (entityPerformance ?? []).slice(0, 10)
  const showReports = mode !== "queries"
  const showQueries = mode !== "reports"
  const labelKey    = mode === "reports" ? "reports" : mode === "queries" ? "queries" : "total"
  // Increase the per-bar width from 120 to 200 for bigger bars
  const contentWidth = Math.max((data.length || 0) * 100 + 360, 1200)

  return (
    <Card>
      <CardHeader>
        <CardTitle>Top 10 Entities Performance</CardTitle>
        <CardDescription>
          {mode === "reports" ? "Reports by entity" :
           mode === "queries" ? "Queries by entity" :
           "Activity by entity"}
        </CardDescription>
      </CardHeader>
      <CardContent>
        <div className="overflow-x-auto">
          <div style={{ width: contentWidth }}>
            <ResponsiveContainer width="100%" height={520}>
              <BarChart data={data} layout="vertical" margin={{ left: 0, right: 90, top: 8, bottom: 8 }}>
                <CartesianGrid strokeDasharray="3 3" stroke="hsl(var(--border))" />
                <XAxis type="number" stroke="hsl(var(--muted-foreground))" />
                <YAxis dataKey="entity" type="category" stroke="hsl(var(--muted-foreground))" width={100} />
                <Tooltip content={<CustomTooltip />} cursor={{ fill: "rgba(0,0,0,0.03)" }} />

                {showReports && (
                  <Bar dataKey="reports" stackId="a" fill="#10b981" name="Reports" radius={[0, 6, 6, 0]}>
                    {!showQueries && (
                      <LabelList
                        dataKey={labelKey}
                        position="right"
                        formatter={(label) => (Number(label) || 0).toLocaleString()}
                      />
                    )}
                  </Bar>
                )}

                {showQueries && (
                  <Bar dataKey="queries" stackId="a" fill="#3b82f6" name="Queries" radius={[0, 6, 6, 0]}>
                    <LabelList
                      dataKey={labelKey}
                      position="right"
                      formatter={(label) => (Number(label) || 0).toLocaleString()}
                    />
                  </Bar>
                )}
              </BarChart>
            </ResponsiveContainer>
          </div>
        </div>
      </CardContent>
    </Card>
  )
}