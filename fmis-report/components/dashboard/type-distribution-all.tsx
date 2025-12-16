"use client"

import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"
import {
  BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer,
  LabelList
} from "recharts"
import { CustomTooltip } from "./custom-tooltip"

/** ===== Overview-only split Type Distribution (scrollable) ===== */
export function TypeDistributionAll({ reportData, queryData }:{
  reportData: Array<{ name: string; value: number }>
  queryData:  Array<{ name: string; value: number }>
}) {
  const widthReports = Math.max((reportData?.length || 0) * 80, 900)
  const widthQueries = Math.max((queryData?.length  || 0) * 80, 900)
  return (
    <Card>
      <CardHeader>
        <CardTitle>Type Distribution (Report and Query)</CardTitle>
        <CardDescription>Most frequently used types</CardDescription>
      </CardHeader>
      <CardContent>
        <div className="space-y-8">
          <div className="rounded-lg bg-emerald-50/60 p-4">
            <p className="text-lg font-semibold text-emerald-800 mb-2">Report Types</p>
            <div className="overflow-x-auto">
              <div style={{ width: widthReports }}>
                <ResponsiveContainer width="100%" height={320}>
                  <BarChart data={reportData} margin={{ bottom: 5, top: 30 }}>
                    <CartesianGrid strokeDasharray="3 3" stroke="hsl(var(--border))" />
                    <XAxis dataKey="name" interval={0} angle={360} height={48} stroke="hsl(var(--muted-foreground))" />
                    <YAxis stroke="hsl(var(--muted-foreground))" />
                    <Tooltip content={<CustomTooltip />} />
                    <Bar dataKey="value" fill="#10b981" radius={[6, 6, 0, 0]}>
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
          </div>

          <div className="rounded-lg bg-emerald-50/40 p-4">
            <p className="text-lg font-semibold text-emerald-800 mb-2">Query Types</p>
            <div className="overflow-x-auto">
              <div style={{ width: widthQueries }}>
                <ResponsiveContainer width="100%" height={300}>
                  <BarChart data={queryData} margin={{ bottom: 5, top: 30 }}>
                    <CartesianGrid strokeDasharray="3 3" stroke="hsl(var(--border))" />
                    <XAxis dataKey="name" interval={0} angle={360} height={48} stroke="hsl(var(--muted-foreground))" />
                    <YAxis stroke="hsl(var(--muted-foreground))" />
                    <Tooltip content={<CustomTooltip />} />
                    <Bar dataKey="value" fill="#3b82f6" radius={[6, 6, 0, 0]}>
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
          </div>
        </div>
      </CardContent>
    </Card>
  )
}