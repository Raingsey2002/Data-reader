"use client"

import * as React from "react"
import * as CheckboxPrimitive from "@radix-ui/react-checkbox"
import { Check } from "lucide-react"
import { cn } from "@/lib/utils"

type OnChange = (checked: boolean) => void

function Checkbox({
  className,
  onCheckedChange,
  checked,
  ...props
}: Omit<React.ComponentProps<typeof CheckboxPrimitive.Root>, "onCheckedChange" | "checked"> & {
  checked?: boolean
  onCheckedChange?: OnChange
}) {
  return (
    <CheckboxPrimitive.Root
      data-slot="checkbox"
      className={cn(
        "border-input peer h-4 w-4 shrink-0 rounded-sm border bg-transparent shadow-none outline-none",
        "focus-visible:border-ring focus-visible:ring-ring/50 focus-visible:ring-[3px]",
        "data-[state=checked]:bg-primary data-[state=checked]:text-primary-foreground",
        "disabled:cursor-not-allowed disabled:opacity-50",
        className
      )}
      checked={checked}
      onCheckedChange={(state) => onCheckedChange?.(state === true)}
      {...props}
    >
      <CheckboxPrimitive.Indicator className="flex items-center justify-center text-current">
        <Check className="h-3.5 w-3.5" />
      </CheckboxPrimitive.Indicator>
    </CheckboxPrimitive.Root>
  )
}

export { Checkbox }
