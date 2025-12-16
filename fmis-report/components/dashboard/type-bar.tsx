"use client"

import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"
import {
  BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer,
  LabelList
} from "recharts"
import { CustomTooltip } from "./custom-tooltip"

/* Type bars (scrollable) */
export function TypeBar({ title, data, barColor }: { title: string; data: Array<{ name: string; value: number }>, barColor: string }) {
  const contentWidth = Math.max((data?.length || 0) * 80, 900)
  return (
    <Card>
      <CardHeader>
        <CardTitle>{title}</CardTitle>
        <CardDescription>Most frequently used types</CardDescription>
      </CardHeader>
      <CardContent>
        <div className="overflow-x-auto">
          <div style={{ width: contentWidth }}>
            <ResponsiveContainer width="100%" height={380}>
              <BarChart data={data} margin={{ left: 10,bottom: 5, top: 30 }}>
                <CartesianGrid strokeDasharray="3 3" stroke="hsl(var(--border))" />
                <XAxis dataKey="name" stroke="hsl(var(--muted-foreground))" interval={0} angle={360} height={60} />
                <YAxis stroke="hsl(var(--muted-foreground))" />
                <Tooltip content={<CustomTooltip />} />
                <Bar dataKey="value" fill={barColor} radius={[6, 6, 0, 0]}>
                  {/* eslint-disable-next-line @typescript-eslint/no-explicit-any */}
                  <LabelList dataKey="value" position="top" formatter={(label: any) => {
                    const num = Number(label);
                    return !isNaN(num) ? new Intl.NumberFormat('en-US').format(num) : label;
                  }} />
                </Bar>
              </BarChart>
            </ResponsiveContainer>
          </div>
        </div>
      </CardContent>
    </Card>
  )
}