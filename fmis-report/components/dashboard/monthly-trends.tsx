"use client"

import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"
import {
  LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer,
} from "recharts"
import { CustomTooltip } from "./custom-tooltip"


/* Monthly Trends – one line on tabs, two on overview + dynamic subtitle */
export function MonthlyTrends({
  monthlyTrends,
  mode = "both"
}:{ monthlyTrends: Array<{ month: string; reports: number; queries: number }>; mode?: "both" | "reports" | "queries" }) {
  const showReports = mode !== "queries"
  const showQueries = mode !== "reports"
  const subtitle =
    mode === "reports" ? "Reports generation over time" :
    mode === "queries" ? "Queries generation over time" :
    "Reports & queries over time"

  return (
    <Card>
      <CardHeader>
        <CardTitle>Monthly Trends</CardTitle>
        <CardDescription>{subtitle}</CardDescription>
      </CardHeader>
      <CardContent>
        <ResponsiveContainer width="100%" height={320}>
          <LineChart data={monthlyTrends ?? []}>
            <CartesianGrid strokeDasharray="3 3" stroke="hsl(var(--border))" />
            <XAxis dataKey="month" stroke="hsl(var(--muted-foreground))" />
            <YAxis stroke="hsl(var(--muted-foreground))" />
            <Tooltip content={<CustomTooltip />} />
            {showReports && <Line type="monotone" dataKey="reports" stroke="#10b981" strokeWidth={3} name="Reports" dot />}
            {showQueries && <Line type="monotone" dataKey="queries" stroke="#3b82f6" strokeWidth={3} name="Queries" dot />}
          </LineChart>
        </ResponsiveContainer>
      </CardContent>
    </Card>
  )
}