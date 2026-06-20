# radiology-figure

**Publication-quality figures to _Radiology_ (RSNA) standard** — the statistical charts
imaging-AI reviewers expect, plus de-identified annotated imaging panels. Primary output is
editable vector (`.svg`/`.pdf`) with a ≥ 300 dpi raster.

## What it does
- **Statistical charts**: ROC (+ DeLong annotation), calibration, decision-curve analysis,
  forest/SROC, Kaplan-Meier with numbers-at-risk, Bland-Altman, box/violin, heatmaps.
- **Radiogenomics**: MOFA/factor plots, deconvolution stacked bars, habitat maps, correlation
  heatmaps.
- **Imaging panels**: montages with windowing labels, arrows, insets, scale bars, panel
  labels — de-identified.
- **Flow diagrams**: CONSORT / STARD / PRISMA.

## Reference files
```
references/
├── radiology-figure-guidelines.md  format, resolution, size, fonts, color, de-identification
├── chart-types.md                  pick + parameterise the right chart
├── api.md                          rcParams preamble, palette, ROC/calibration/forest/KM helpers
├── imaging-panels.md               montages, windowing, arrows, scale bars, anonymisation
└── design-theory.md                typography, layout, color-blind-safe palettes, anti-redundancy
```

## Conventions enforced
- Vector-first; text stays text (`svg.fonttype='none'`); ≥ 300 dpi raster companion.
- Sans-serif (Arial/Helvetica); single-column ~85 mm / double ~170 mm; ≥ ~7 pt at print size.
- Color-blind-safe palette; never red/green alone; CI bands + n shown; honest axes.
- Every image panel de-identified; windowing (WL/WW) + scale bar where size matters.

## Example prompts
- "Plot ROC for these two models on the same cases and annotate the DeLong p."
- "Calibration plot + decision curve for my prediction model."
- "Kaplan-Meier by radiomic-risk group with numbers-at-risk."
- "Forest + SROC for my DTA meta-analysis."
- "Lay out a 2×3 MRI montage with arrows and a scale bar, de-identified."

## Integrity
Plots only supplied/loaded data; flags example data; hands the underlying statistic to
`radiology-stats` and checklist-fit to `radiology-reporting`.
