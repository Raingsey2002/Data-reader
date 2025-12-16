"use client"

import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"
import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from "@/components/ui/table"

export function InactiveListTable({
  title, subtitle, items, itemHeader
}:{
  title: string; subtitle: string; items: Array<{code: string, label: string}>; itemHeader: string
}) {
  return (
    <Card>
      <CardHeader>
        <CardTitle>{title}</CardTitle>
        <CardDescription>{subtitle}</CardDescription>
      </CardHeader>
      <CardContent>
        <div className="rounded-md border max-h-72 overflow-auto">
          <Table>
            <TableHeader>
              <TableRow>
                <TableHead>N°</TableHead>
                <TableHead>{itemHeader}</TableHead>
                <TableHead>Description</TableHead>
              </TableRow>
            </TableHeader>
            <TableBody>
              {items.length === 0 ? (
                <TableRow>
                  <TableCell colSpan={3} className="text-center text-muted-foreground py-6">None</TableCell>
                </TableRow>
              ) : (
                items.map((it, idx) => (
                  <TableRow key={it.code}>
                    <TableCell>{idx + 1}</TableCell>
                    <TableCell>{it.code}</TableCell>
                    <TableCell className="font-kantumruy">{typeof it.label === 'string' ? it.label.split(" - ")[1] : ''}</TableCell>
                  </TableRow>
                ))
              )}
            </TableBody>
          </Table>
        </div>
      </CardContent>
    </Card>
  )
}
