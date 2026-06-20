---
name: radiology-figure
description: "Produce publication-quality figures to Radiology (RSNA) standard with Python (matplotlib) — ROC curves, calibration plots, decision-curve analysis, forest/SROC plots, Kaplan-Meier curves with numbers-at-risk, Bland-Altman, confusion/heatmaps, radiogenomics factor/deconvolution plots, and annotated imaging panels (montages with windowing, arrows, scale bars, panel labels). Use when the user wants a figure, plot, ROC/calibration/forest/KM/decision curve, an imaging figure panel, a CONSORT/STARD flow diagram, or asks how to format a figure for Radiology. Output is editable vector (.svg/.pdf) plus a 300+ dpi raster. Enforces de-identification and journal typography; never invents data points."
---

# Radiology Publication Figures

Use this skill to build figures that pass _Radiology_'s technical and editorial bar: correct
file format and resolution, legible typography, color-blind-safe palettes, honest axes, and
the specific chart types imaging-AI reviewers expect (ROC, calibration, decision-curve,
forest/SROC, Kaplan-Meier, Bland-Altman), plus **de-identified** annotated imaging panels.

## Core stance

- **Vector first.** Primary output is editable **`.svg`** (or `.pdf`); secondary is a
  **≥ 300 dpi** raster (TIFF/PNG). Keep text as text (`svg.fonttype='none'`), not outlines,
  so editors can re-typeset.
- **One figure, one message.** Each panel answers one question; no two panels duplicate it.
  Panels are labelled A, B, C.
- **Honest graphics.** Axes start where the data demand (don't truncate to exaggerate);
  show uncertainty (CI bands, error bars); state n.
- **De-identify every image.** No PHI burned into pixels, no faces/identifiers; scrub DICOM
  overlays; report windowing (WL/WW) and add a scale bar where size matters.
- **Match the journal.** Sans-serif (Arial/Helvetica), figure width to column (single ~85 mm
  / double ~170 mm), adequate font size at final print size (≈ 7–9 pt min).
- **Never fabricate data.** Plot only supplied/loaded values; mark simulated/example data
  clearly.

## When to use

- Statistical figures: ROC (+ DeLong annotation), calibration, decision-curve, forest, SROC,
  Kaplan-Meier (with numbers-at-risk), Bland-Altman, box/violin, heatmaps/clustermaps.
- Radiogenomics: MOFA/factor plots, deconvolution stacked bars, habitat maps, correlation
  heatmaps.
- Imaging panels: multi-row montages, before/after, arrows/insets, windowing labels, scale
  bars.
- Flow diagrams: CONSORT / STARD / PRISMA patient-selection diagrams.

## When to open extra files

| File | Open when |
|---|---|
| [references/radiology-figure-guidelines.md](references/radiology-figure-guidelines.md) | File format, resolution, size, fonts, color, panel labelling, de-identification rules |
| [references/chart-types.md](references/chart-types.md) | Choosing/parameterising the right statistical chart (ROC, calibration, DCA, forest, KM, Bland-Altman, heatmap) |
| [references/imaging-panels.md](references/imaging-panels.md) | Building montages: windowing, arrows, insets, scale bars, anonymisation, panel layout |
| [references/api.md](references/api.md) | The matplotlib rcParams preamble, color palette, and reusable helper functions (ROC/calibration/forest/KM) |
| [references/design-theory.md](references/design-theory.md) | Typography, layout grid, color-blind-safe palettes, anti-redundancy, accessibility |

## Workflow

1. **Pick the chart for the message** (chart-types.md). Discrimination → ROC; reliability →
   calibration; clinical value → decision-curve; agreement → Bland-Altman; time-to-event →
   Kaplan-Meier; meta-analysis → forest/SROC.
2. **Start the script with the rcParams preamble and palette** from api.md.
3. **Build the panel(s)** with helper functions; add CI bands, n, and clear axis labels with
   units; label panels A/B/C.
4. **For imaging panels**, confirm de-identification, add windowing labels + scale bar +
   arrows; keep grayscale unless color encodes data.
5. **Export** `.svg` (text-as-text) **and** a 300–600 dpi raster; check legibility at final
   print width.
6. **QA** (see contract) and return the script + both files.

## Output contract

1. **`Figure plan`** — what each panel shows and why; the chart type chosen.
2. **`Script`** — a single runnable `.py` starting with the rcParams preamble; data inputs
   clearly marked (real vs example).
3. **`Files`** — `figure.svg` (primary) + `figure.png`/`.tiff` at ≥ 300 dpi.
4. **`QA notes`** — fonts embedded as text, color-blind check, axis honesty, n shown,
   de-identification confirmed for any image panel.

## QA checklist (run before returning)

- rcParams preamble present; output is `.svg` with `svg.fonttype='none'` **and** a ≥ 300 dpi
  raster.
- Every axis labelled with units; legend present; panels labelled A/B/C.
- Uncertainty shown (CI band/error bars) and n stated.
- Color-blind-safe; not reliant on red/green alone; sufficient contrast.
- Imaging panels de-identified; windowing + scale bar present where relevant.
- No invented data points; example data flagged.

## Handoffs
- The statistic behind the plot (AUC CI, DeLong, ICC, calibration metrics, net benefit) →
  `radiology-stats`.
- Whether the figure satisfies a checklist item (flow diagram for STARD/CONSORT) →
  `radiology-reporting`.
- Figure legends/captions prose → `radiology-writing`.
