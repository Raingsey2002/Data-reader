import { type ClassValue, clsx } from "clsx"
import { twMerge } from "tailwind-merge"

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs))
}

export const norm = (s: unknown) =>
  String(s ?? "")
    .replace(/[\u200B-\u200D\uFEFF]/g, "")
    .normalize("NFKD")
    .replace(/[\u0300-\u036f]/g, "")
    .replace(/\s+/g, " ")
    .trim()

export const low = (s: unknown) => norm(s).toLowerCase()
export const UP  = (s: unknown) => norm(s).toUpperCase()

const alias: Record<string, string> = {
  "report/query":"rq","report / query":"rq","report- query":"rq","report - query":"rq","reportquery":"rq",
  "name of report and query":"name","name":"name","report/query name":"name",
  "description":"desc","count":"count",
  "user id":"user","userid":"user","user":"user",
  "level":"level","entity":"entity","office":"office",
  "operating unit":"ou","operatingunit":"ou","ou":"ou",
  "year":"year","month":"month","day":"day",
}
export const keyFor = (h: string) => alias[low(h)] ?? ""

export const toNumber = (v: unknown) => {
  const n = Number(String(v ?? "").replace(/[, ]+/g, ""))
  return Number.isFinite(n) ? n : undefined
}
export const monthNameToNum = (v: unknown) => {
  if (typeof v === "number") return v
  const m: Record<string, number> = { jan:1,feb:2,mar:3,apr:4,may:5,jun:6,jul:7,aug:8,sep:9,oct:10,nov:11,dec:12 }
  const k = low(v).slice(0,3)
  return m[k] ?? (Number.isFinite(Number(v)) ? Number(v) : undefined)
}
export const MONTHS = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
export function ymToLabel(y:number,m:number){ return `${MONTHS[m-1]} ${y}` }
