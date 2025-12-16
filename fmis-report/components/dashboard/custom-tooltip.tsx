type TooltipEntry = {
  value?: number;
  name?: string;
  color?: string;
  dataKey?: string;
  stroke?: string;
};

type CustomTooltipProps = {
  active?: boolean;
  payload?: TooltipEntry[];
  label?: string;
  isOverview?: boolean;
};

type YearData = {
  reports?: number;
  queries?: number;
  color: string;
};

export const CustomTooltip = ({ active, payload, label, isOverview }: CustomTooltipProps) => {
  if (active && payload && payload.length) {
    const total = payload.reduce((a, p) => a + (Number(p.value) || 0), 0);

    if (isOverview) {
      const byYear: Record<string, YearData> = payload.reduce((acc, p) => {
        const year = p.name?.split(" ")[1];
        if (year) {
          if (!acc[year]) acc[year] = { color: p.stroke || "" };
          if (p.name?.startsWith("Reports")) acc[year].reports = p.value;
          if (p.name?.startsWith("Queries")) acc[year].queries = p.value;
        }
        return acc;
      }, {} as Record<string, YearData>);

      return (
        <div className="bg-card border border-border rounded-lg shadow-lg p-3 min-w-[400px]">
          <p className="font-semibold text-foreground text-lg mb-2">{label}</p>
          <div className="space-y-1">
            {Object.entries(byYear).map(([year, data]) => (
              <div key={year} className="flex justify-between items-center" style={{ color: data.color }}>
                <span className="text-base font-medium">{year}:</span>
                <div className="flex items-center space-x-4">
                  <span>Reports: <span className="font-bold text-lg">{(data.reports ?? 0).toLocaleString()}</span></span>
                  <span>Queries: <span className="font-bold text-lg">{(data.queries ?? 0).toLocaleString()}</span></span>
                </div>
              </div>
            ))}
          </div>
          {payload.length > 1 && (
            <div className="border-t border-border mt-2 pt-2 flex justify-between items-center">
              <span className="text-base font-semibold">Total:</span>
              <span className="text-lg font-bold">{total.toLocaleString()}</span>
            </div>
          )}
        </div>
      );
    }

    return (
      <div className="bg-card border border-border rounded-lg shadow-lg p-4 min-w-[240px]">
        <p className="font-semibold text-foreground text-lg mb-2">{label}</p>
        {payload.map((entry: TooltipEntry, index: number) => (
          <p key={index} className="text-base font-medium" style={{ color: entry.color }}>
            {entry.name}: <span className="font-bold text-xl">{(entry.value ?? 0).toLocaleString()}</span>
          </p>
        ))}
        {payload.length > 1 && (
          <p className="mt-2 text-base font-semibold">
            Total: <span className="text-xl">{total.toLocaleString()}</span>
          </p>
        )}
      </div>
    );
  }
  return null;
};