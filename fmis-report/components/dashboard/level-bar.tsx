"use client"

import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"
import {
  BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer,
  LabelList
} from "recharts"
import { CustomTooltip } from "./custom-tooltip"

/* Level stacked bar (scrollable) with tab-aware labels */
export function LevelBar({
  title, subtitle, data, mode
}:{
  title:string;
  subtitle:string;
  data: Array<{ name:string; reports:number; queries:number; total:number }>;
  mode: "both" | "reports" | "queries"
}) {
  const showReports = mode !== "queries"
  const showQueries = mode !== "reports"
  const labelKey    = mode === "reports" ? "reports" : mode === "queries" ? "queries" : "total"
  const contentWidth = Math.max((data?.length || 0) * 160, 520)

  return (
    <Card>
      <CardHeader>
        <CardTitle>{title}</CardTitle>
        <CardDescription>{subtitle}</CardDescription>
      </CardHeader>
      <CardContent>
        <div className="overflow-x-auto">
          <div style={{ width: contentWidth }}>
            <ResponsiveContainer width="100%" height={320}>
              <BarChart data={data} margin={{ left: 12, right: 32, top: 30, bottom: 10 }}>
                <CartesianGrid strokeDasharray="3 3" stroke="hsl(var(--border))" />
                <XAxis dataKey="name" stroke="hsl(var(--muted-foreground))" />
                <YAxis stroke="hsl(var(--muted-foreground))" />
                <Tooltip content={<CustomTooltip />} cursor={{ fill: "rgba(0,0,0,0.03)" }} />

                {showReports && (
                  <Bar dataKey="reports" stackId="a" fill="#10b981" name="Reports" radius={[6,6,0,0]}>
                    {!showQueries && (
                      <LabelList
                        dataKey={labelKey}
                        position="top"
                        formatter={(label) => (Number(label) || 0).toLocaleString()}
                      />
                    )}
                  </Bar>
                )}

                {showQueries && (
                  <Bar dataKey="queries" stackId="a" fill="#3b82f6" name="Queries" radius={[6,6,0,0]}>
                    <LabelList
                      dataKey={labelKey}
                      position="top"
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