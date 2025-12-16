"use client"

import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"
import {
  BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer, Legend, LabelList,
} from "recharts"
import { CustomTooltip } from "./custom-tooltip"

type YearlyComparisonProps = {
  data: Array<{ year: number; reports: number; queries: number }>;
  mode?: "both" | "reports" | "queries";
};

type LegendPayload = {
  value?: string;
  type?: string;
  id?: string;
  color?: string;
}

const renderLegend = (props: { payload?: readonly LegendPayload[] }) => {
  const { payload } = props;
  return (
    <div className="flex items-center justify-center gap-4 mt-4">
      <div className="p-2 flex items-center gap-4">
        {payload?.map((entry: LegendPayload, index: number) => (
          <div key={`item-${index}`} className="flex items-center gap-2">
            <div style={{ width: 6, height: 6, backgroundColor: entry.color, borderRadius: '2px' }} />
            <span className="text-base text-muted-foreground">{entry.value}</span>
          </div>
        ))}
      </div>
    </div>
  );
};

export function YearlyComparisonBar({ data, mode = "both" }: YearlyComparisonProps) {
  const showReports = mode !== "queries";
  const showQueries = mode !== "reports";

  const subtitle =
    mode === "reports" ? "Total reports by year" :
      mode === "queries" ? "Total queries by year" :
        "Total reports & queries by year";

  const minWidth = Math.max((data.length || 0) * 120, 800)

  return (
    <Card>
      <CardHeader>
        <CardTitle>Yearly Comparison</CardTitle>
        <CardDescription>{subtitle}</CardDescription>
      </CardHeader>
      <CardContent>
        <div className="overflow-x-auto">
          <div style={{ width: minWidth }}>
            <ResponsiveContainer width="100%" height={320}>
              <BarChart data={data} margin={{ left: 15, bottom: 5, top: 40 }}>
                <CartesianGrid strokeDasharray="3 3" stroke="hsl(var(--border))" />
                <XAxis dataKey="year" stroke="hsl(var(--muted-foreground))" />
                <YAxis stroke="hsl(var(--muted-foreground))" />
                <Tooltip content={<CustomTooltip />} />
                <Legend content={renderLegend} />
                {showReports && (
                  <Bar dataKey="reports" fill="#10b891" name="Reports" radius={[6, 6, 0, 0]}>
                    <LabelList dataKey="reports" position="top" offset={4} formatter={(label) => (Number(label) || 0).toLocaleString()} />
                  </Bar>
                )}
                {showQueries && (
                  <Bar dataKey="queries" fill="#3b82f6" name="Queries" radius={[6, 6, 0, 0]}>
                    <LabelList dataKey="queries" position="top" offset={4} formatter={(label) => (Number(label) || 0).toLocaleString()} />
                  </Bar>
                )}
              </BarChart>
            </ResponsiveContainer>
          </div>
        </div>
      </CardContent>
    </Card>
  );
}
