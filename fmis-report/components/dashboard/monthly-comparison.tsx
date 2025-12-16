"use client"

import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"
import {
  LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer, Legend
} from "recharts"
import { CustomTooltip } from "./custom-tooltip"

interface MonthData {
  month: string;
  [key: string]: string | number; // For dynamic year-specific report/query data
}

/* Monthly Trends – one line on tabs, two on overview + dynamic subtitle */
const COLORS = ["#f97ed8ff", "#b01018ff", "#0028f1ff", "#ff7300", "#387908", "#ff0000"];

export function MonthlyComparison({
  monthlyComparison,
  mode = "both",
  isOverview = false,
}: {
  monthlyComparison: Array<{ year: number; reports: number[]; queries: number[] }>;
  mode?: "both" | "reports" | "queries";
  isOverview?: boolean;
}) {
  const showReports = mode !== "queries";
  const showQueries = mode !== "reports";
  const subtitle =
    mode === "reports"
      ? "Reports generation over time"
      : mode === "queries"
      ? "Queries generation over time"
      : "Reports & queries over time";

  const data: MonthData[] = Array.from({ length: 12 }).map((_, i) => {
    const monthData: MonthData = {
      month: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"][i],
    };
    monthlyComparison.forEach((d) => {
      if (showReports) monthData[`reports-${d.year}`] = d.reports[i];
      if (showQueries) monthData[`queries-${d.year}`] = d.queries[i];
    });
    return monthData;
  });

  return (
    <Card>
      <CardHeader>
        <CardTitle>Monthly Comparison</CardTitle>
        <CardDescription>{subtitle}</CardDescription>
      </CardHeader>
      <CardContent>
        <ResponsiveContainer width="100%" height={320}>
          <LineChart data={data}>
            <CartesianGrid strokeDasharray="3 3" stroke="hsl(var(--border))" />
            <XAxis dataKey="month" stroke="hsl(var(--muted-foreground))" />
            <YAxis stroke="hsl(var(--muted-foreground))" />
            <Tooltip content={<CustomTooltip isOverview={isOverview} />} />
            <Legend />
            {monthlyComparison.map((d, i) =>
              showReports ? (
                <Line
                  key={`reports-${d.year}`}
                  type="monotone"
                  dataKey={`reports-${d.year}`}
                  stroke={COLORS[i % COLORS.length]}
                  strokeWidth={2}
                  name={`Reports ${d.year}`}
                  dot
                />
              ) : null
            )}
            {monthlyComparison.map((d, i) =>
              showQueries ? (
                <Line
                  key={`queries-${d.year}`}
                  type="monotone"
                  dataKey={`queries-${d.year}`}
                  stroke={COLORS[i % COLORS.length]}
                  strokeDasharray="5 5"
                  strokeWidth={2}
                  name={`Queries ${d.year}`}
                  dot
                />
              ) : null
            )}
          </LineChart>
        </ResponsiveContainer>
      </CardContent>
    </Card>
  );
}