"use client"

import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"
import { Input } from "@/components/ui/input"
import { Button } from "@/components/ui/button"
import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from "@/components/ui/table"
import { Search } from "lucide-react"
import { Row } from "@/lib/types"

export function ListTable(props: {
  rows: Row[]
  page: number
  pageSize: number
  total: number
  hasMore: boolean
  loadingRows: boolean
  onPrev: () => void
  onNext: () => void
  totalPages: number
  searchTerm: string
  onSearch: (v: string) => void
  tab: "Report" | "Query" | "All"
}) {
  const { rows, page, pageSize, total, loadingRows, onPrev, onNext, totalPages, searchTerm, onSearch, tab } = props
  return (
    <Card>
      <CardHeader>
        <CardTitle className="text-xl">{tab === "Report" ? "Report Records" : tab === "Query" ? "Query Records" : "All Records"}</CardTitle>
        <CardDescription>Detailed view</CardDescription>
      </CardHeader>
      <CardContent>
        <div className="flex items-center justify-between mb-4">
          <div className="flex items-center gap-2">
            <Search className="h-4 w-4 text-muted-foreground" />
            <Input placeholder={`Search ${tab.toLowerCase()}...`} value={searchTerm} onChange={(e) => onSearch(e.target.value)} className="w-72" />
          </div>
        </div>

        <div className="rounded-md border max-h-96 overflow-auto">
          <Table>
            <TableHeader>
              <TableRow>
                <TableHead>N°</TableHead>
                <TableHead>Type</TableHead>
                <TableHead>Code</TableHead>
                <TableHead>Description</TableHead>
                <TableHead>User</TableHead>
                <TableHead>Level</TableHead>
                <TableHead>Entity</TableHead>
                <TableHead>Office</TableHead>
                <TableHead>Operating Unit</TableHead>
                <TableHead>Month</TableHead>
                <TableHead>Year</TableHead>
              </TableRow>
            </TableHeader>
            <TableBody>
              {rows.map((r, i) => (
                <TableRow key={`${r.user}-${r.name}-${page * pageSize + i}`}>
                  <TableCell>{page * pageSize + i + 1}</TableCell>
                  <TableCell>{r.rq}</TableCell>
                  <TableCell>{r.name}</TableCell>
                  <TableCell className="max-w-xs truncate font-kantumruy">{r.desc}</TableCell>
                  <TableCell>{r.user}</TableCell>
                  <TableCell>{r.level}</TableCell>
                  <TableCell>{r.entity}</TableCell>
                  <TableCell>{r.office}</TableCell>
                  <TableCell>{r.ou}</TableCell>
                  <TableCell>{r.month}</TableCell>
                  <TableCell>{r.year}</TableCell>
                </TableRow>
              ))}
            </TableBody>
          </Table>
        </div>

        <div className="flex items-center justify-between mt-4">
          <p className="text-sm text-muted-foreground">
            Showing {rows.length ? page * pageSize + 1 : 0}–{Math.min((page + 1) * pageSize, total)} of {total} {tab.toLowerCase()} records
          </p>
          <div className="flex items-center gap-2">
            <Button variant="outline" size="sm" onClick={onPrev} disabled={page === 0 || loadingRows}>Previous</Button>
            <span className="text-sm text-muted-foreground">Page {total ? page + 1 : 0} of {totalPages}</span>
            <Button variant="outline" size="sm" onClick={onNext} disabled={page + 1 >= totalPages || loadingRows}>Next</Button>
          </div>
        </div>
      </CardContent>
    </Card>
  )
}
