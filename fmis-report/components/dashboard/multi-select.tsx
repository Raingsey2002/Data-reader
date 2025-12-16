"use client";

import { useEffect, useMemo, useState } from "react";
import { Button } from "@/components/ui/button";
import { Checkbox } from "@/components/ui/checkbox";
import { Dialog, DialogContent, DialogFooter, DialogHeader, DialogTitle } from "@/components/ui/dialog";
import { Input } from "@/components/ui/input";
import { ChevronDown } from "lucide-react";

export function MultiSelect({
  label, options, selected, onChange,
}: { label: string; options: Array<{ value: string; label: string }>; selected: string[]; onChange: (next: string[]) => void }) {
  const allOptionValues = useMemo(() => options.map(o => o.value), [options]);
  const isAllSelected = selected.length === 0;

  const [open, setOpen] = useState(false)
  const [temp, setTemp] = useState<string[]>(isAllSelected ? allOptionValues : selected)
  const [q, setQ] = useState("")

  useEffect(() => {
    if (open) {
      const newValues = selected.length === 0 ? allOptionValues : selected;
      setTemp(newValues);
    }
  }, [open, selected, allOptionValues]);

  useEffect(() => { setQ("") }, [open])

  const visibleOptions = useMemo(() => {
    const t = q.trim().toLowerCase()
    return t ? options.filter(o => o.label.toLowerCase().includes(t)) : options
  }, [q, options])

  const allSelectedVisible = visibleOptions.length > 0 && visibleOptions.every(v => temp.includes(v.value))
  const toggle = (v: { value: string; label: string }) => setTemp(p => p.includes(v.value) ? p.filter(x => x !== v.value) : [...p, v.value])

  const toggleAll = (checked: boolean | "indeterminate") => {
    if (checked) {
      const add = visibleOptions.filter(v => !temp.includes(v.value)).map(v => v.value)
      setTemp(p => [...p, ...add])
    } else {
      setTemp(p => p.filter(x => !visibleOptions.map(v => v.value).includes(x)))
    }
  }

  const apply = () => {
    const isTempAllSelected = options.length > 0 && temp.length === options.length;
    onChange(isTempAllSelected ? [] : temp);
    setOpen(false)
  }
  const cancel = () => {
    setTemp(isAllSelected ? allOptionValues : selected);
    setOpen(false)
  }

  const display =
    isAllSelected
      ? "All options"
      : `${selected.length} selected`

  return (
    <div className="space-y-2">
      <label className="text-base font-semibold text-emerald-800">{label}</label>
      <Button
        variant="outline"
        className="w-full h-11 justify-between border-2 border-emerald-200 hover:border-emerald-300"
        onClick={() => setOpen(true)}
      >
        <span className="text-base truncate">{display}</span>
        <ChevronDown className="h-4 w-4 opacity-40" />
      </Button>

      <Dialog open={open} onOpenChange={setOpen}>
        <DialogContent className="max-w-md max-h-[85vh] flex flex-col top-[10%] left-auto right-[10%] translate-x-0 translate-y-0">
          <DialogHeader>
            <DialogTitle className="text-xl">Select {label}</DialogTitle>
          </DialogHeader>

          <div className="mb-2">
            <Input
              value={q}
              onChange={(e) => setQ(e.target.value)}
              placeholder={`Search ${label.toLowerCase()}...`}
            />
          </div>

          <div className="flex items-center justify-between mb-3 pb-2 border-b">
            <div className="flex items-center gap-2">
              <Checkbox id={`all-${label}`} checked={allSelectedVisible} onCheckedChange={toggleAll} />
              <label htmlFor={`all-${label}`} className="text-base font-medium">
                Select All (filtered)
              </label>
            </div>
            <span className="text-sm text-muted-foreground">
              {temp.length} of {options.length} selected{q ? ` — showing ${visibleOptions.length}` : ""}
            </span>
          </div>

          <div className="overflow-y-auto space-y-1 pr-1 max-h-60">
            {visibleOptions.map((opt) => (
              <div key={opt.value} className="flex items-center gap-2 p-2 hover:bg-accent rounded-md">
                <Checkbox id={`${label}-${opt.value}`} checked={temp.includes(opt.value)} onCheckedChange={() => toggle(opt)} />
                <label htmlFor={`${label}-${opt.value}`} className="text-base flex-1 cursor-pointer font-kantumruy">{opt.label}</label>
              </div>
            ))}
            {visibleOptions.length === 0 && (
              <div className="text-base text-muted-foreground py-6 text-center">No results</div>
            )}
          </div>

          <DialogFooter className="border-t pt-3 gap-2">
            <Button variant="outline" onClick={cancel}>Cancel</Button>
            <Button onClick={apply} className="bg-emerald-600 text-white hover:bg-emerald-700">Done</Button>
          </DialogFooter>
        </DialogContent>
      </Dialog>
    </div>
  )
}