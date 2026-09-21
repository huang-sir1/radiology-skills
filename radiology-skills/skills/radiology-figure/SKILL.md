---
name: radiology-figure
description: "Create/audit publication plots, visual abstracts and imaging panels with render QA; not tables or decks. CN: 统计图、ROC、森林图、影像图版"
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
  Panels are labelled A, B, C (_Radiology_-family) or a, b, c (Nature-family — the case is
  venue-dependent, never mixed within one manuscript; see "When to open extra files").
- **Honest graphics.** Axes start where the data demand (don't truncate to exaggerate);
  show uncertainty (CI bands, error bars); state n.
- **De-identify every image.** No PHI burned into pixels, no faces/identifiers; scrub DICOM
  overlays; report windowing (WL/WW) and add a scale bar where size matters.
- **Match the journal.** Sans-serif (Arial/Helvetica), figure width to column — _Radiology_-family
  single ~85 mm / double ~170 mm, **or** Nature-family single 89 mm / double 183 mm (max height
  170 mm) — adequate font size at final print size (≈ 7–9 pt min). Confirm the target venue
  before sizing the first figure.
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
| [references/color-systems.md](references/color-systems.md) | Picking ONE palette (Okabe-Ito / NPG / Morandi) and mapping color→meaning so every figure matches |
| [references/survival-figures.md](references/survival-figures.md) | Kaplan-Meier integrity (curve ↔ numbers-at-risk ↔ censoring), numbers-at-risk done right, time-dependent (IPCW) ROC/calibration/DCA, incremental-value framing |
| [references/figure-set-consistency.md](references/figure-set-consistency.md) | Unifying palette/fonts/axes across all figures, and cross-validating every figure number against the manuscript tables and data before export |
| [references/nature-figure-spec.md](references/nature-figure-spec.md) | Target is a Nature-portfolio venue instead of _Radiology_ — column widths (89/183 mm), lowercase panel letters, RGB, legend word cap, Extended Data/Source Data display-item split |
| [references/figure-intent-and-render-qa.md](references/figure-intent-and-render-qa.md) | Full figure set planning, crowded/colliding labels, DCA/KM/heatmap layout problems, final-size render review, source-data crosswalk, or premium academic visual polish |
| [references/journal-family-visual-style.md](references/journal-family-visual-style.md) | Target journal family is known, the user supplied author-guide PDFs/classic articles, or the figure set needs Nature/npj or European Radiology visual taste |
| [references/backend-and-geometry-qa.md](references/backend-and-geometry-qa.md) | Choosing Python vs R, using survival/nomogram/ComplexHeatmap conventions, or auditing white background, excessive whitespace, edge clipping, and export geometry |

## Workflow

Choose the requested scope first: `advisory` explains/designs a figure, `audit` inspects existing
figures and reports findings, and `create-edit` produces or changes artifacts. Audit may render a
temporary preview for inspection; it does not authorize rewriting originals. Generate scripts and
exports only for `create-edit` or an explicitly requested artifact. Use only applicable QA items:
conceptual diagrams and flowcharts need not have numerical axes, confidence intervals or sample n.

0. **Confirm the target venue** (_Radiology_-family default, or Nature-family →
   nature-figure-spec.md) before sizing the first figure — column widths and panel-letter case
   differ and are painful to change after the set is built.
1. **For venue-specific visual taste**, open `journal-family-visual-style.md` and apply the
   target family's panel lettering, legend density, graphical abstract, table, and source-data
   conventions.
2. **For full figure sets or layout-sensitive figures**, open
   `figure-intent-and-render-qa.md` and create the figure intent table plus source-data
   crosswalk before drawing.
3. **Pick the chart for the message** (chart-types.md). Discrimination → ROC; reliability →
   calibration; net benefit at justified risk thresholds linked to a clinical action → decision-curve;
   agreement → Bland-Altman; time-to-event →
   Kaplan-Meier; meta-analysis → forest/SROC; whole-study summary → graphical abstract.
4. **Resolve the backend** with `backend-and-geometry-qa.md`: reuse the project's existing
   Python/R stack; otherwise default to Python for general imaging panels and consider R for
   survival/nomogram/ComplexHeatmap workflows where it is the established project route.
5. **Start the script with the backend theme and palette** from api.md (Python) or
   `backend-and-geometry-qa.md` (R).
6. **Build the panel(s)** with helper functions; add CI bands, n, and clear axis labels with
   units; label panels via `panel_letter()`/`add_panel_letter()` (api.md) with the case set for
   the confirmed venue — never hardcode `chr(65+i)` per script.
7. **For imaging panels**, confirm de-identification, add windowing labels + scale bar +
   arrows; keep grayscale unless color encodes data.
8. **Export** `.svg`/`.pdf` (editable text where possible) **and** a 300–600 dpi raster on an
   explicit opaque white canvas; check legibility at final print width.
9. **QA** (see contract): run `scripts/audit_figure_export.py` on raster exports, then visually
   inspect the final render for text/number/legend overlap and semantic errors before returning.

## Output contract

For advisory/audit scope, return only the requested plan or evidence-linked findings and applicable
QA status. The script and file requirements below apply to artifact creation/editing. A diagnostic
render is not proof that statistical, de-identification or submission checks passed.

1. **`Figure plan`** — what each panel shows and why; the chart type chosen.
2. **`Figure intent / source-data crosswalk`** — for full figure sets or submission figures,
   show what claim each panel supports and where the data came from.
3. **`Script`** — a single runnable `.py` or `.R` using the selected backend theme; data inputs
   clearly marked (real vs example).
4. **`Files`** — editable `figure.svg`/`figure.pdf` + `figure.png`/`.tiff` at ≥ 300 dpi.
5. **`QA notes`** — fonts embedded as text, color-blind check, axis honesty, n shown,
   de-identification confirmed for any image panel, final-size render checked for no
   overlap/clipping, and venue-family visual style checked when applicable.

## QA checklist (run before returning)

- Selected backend theme/preamble is present; output is editable `.svg`/`.pdf` with text retained
  where possible **and** a ≥ 300 dpi raster on an opaque white canvas.
- Every axis labelled with units; legend present; panels labelled A/B/C or a/b/c per the
  confirmed venue, consistently across the whole figure set.
- Uncertainty shown (CI band/error bars) and n stated.
- Color-blind-safe; not reliant on red/green alone; sufficient contrast.
- Imaging panels de-identified; windowing + scale bar present where relevant.
- No invented data points; example data flagged.
- Final exported render inspected at target size; no label/tick/legend/number overlap,
  clipping, or text crossing plot elements.
- Venue-family rules satisfied when applicable (panel-letter case, background, legend length,
  graphical abstract blocks, Source Data/table expectations).
- Raster geometry audit recorded (white canvas, DPI metadata when available, occupied area,
  edge-ink/clipping risk); visual inspection still required for actual text collisions.

## Handoffs
- The statistic behind the plot (AUC CI, DeLong, ICC, calibration metrics, net benefit) →
  `radiology-stats`.
- Whether the figure satisfies a checklist item (flow diagram for STARD/CONSORT), or the
  Reporting Summary/Nature Portfolio checklist → `radiology-reporting`.
- Figure legends/captions prose, display-item plan (main vs Extended Data) →
  `radiology-writing`.
- Source Data files, Extended Data vs Supplementary Information wording → `radiology-data`.
- Reuse or adapt a frozen figure inside an audience-specific scientific deck →
  `radiology-paper2ppt` with the editable asset, source locator and transformation limits.
- Full figure set finished and ready for a harsh read before submission → `radiology-prereview`.
- Figure/table value reconciliation and project state → `radiology-table` /
  `radiology-pipeline`; upload package → `radiology-submission`.
