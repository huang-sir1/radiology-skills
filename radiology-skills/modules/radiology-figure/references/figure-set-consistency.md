# Figure-set consistency & number cross-validation

Two figures can each be fine and the *set* still fail review: clashing palettes, drifting fonts,
or a survival % in Figure 3 that doesn't match Table 2. Treat the whole figure set + manuscript
tables + underlying data as one object that must agree.

## Visual unification (lock these once, apply to every figure)

| Element | Rule |
|---|---|
| Palette | One system, semantic roles (`color-systems.md`); identical hex per role across all panels |
| Font | One sans-serif (Arial / Liberation Sans); **one size ladder** reused everywhere |
| Font sizes | At final print size, nothing below ~7 pt; titles/labels/ticks/legend in fixed steps. Small text reads as "unfinished" — size up until legible at column width |
| Axes | Same spine weight (e.g. 0.8–1.0 pt print; thicker for on-screen teaching decks); top/right spines off; ticks outward |
| Panel letters | Same size/weight/position (e.g. bold, top-left) in every figure |
| CI bands / line weights | Same alpha and lw conventions across panels |
| Whitespace | Don't crowd: consistent inter-panel `wspace/hspace`; if elements collide (title vs legend), move them apart rather than shrink |

A practical workflow: keep a tiny shared style module (`rcParams` + `C` palette dict + helper
fns) and `import` it in every figure script, so a single edit re-themes the whole paper.

> On-screen teaching decks vs print: a print figure uses ~7–9 pt; a slide/teaching figure can use
> a larger ladder (and thicker axes). Pick one ladder per deliverable and keep it uniform.

## Number cross-validation (do this before every export)

Every number a figure shows — AUC, HR, P, n, %, group counts, at-risk — must be **recomputed from
the data at render time** and must **match the manuscript tables and the data file**. The common
failure: hardcoded values in the manuscript drift after the data/analysis is regenerated.

Checklist:
- Figure annotations are computed in the plotting script from the **same** dataframe the tables
  use — not pasted in. (If a number must be typed into prose, re-derive and diff it.)
- Group **n** in a KM legend = group n in the Sankey blocks = group n in the data = the t=0
  numbers-at-risk.
- Survival % on the curve = the table's k-year survival = `km_at(t)` on the data.
- AUC/C-index/HR/P in the figure = the values reported in text/tables (same estimator, same
  cohort mask).
- Cross-tab sanity: e.g. for a 2×2-derived 3-group scheme, confirm the "impossible" cell is 0
  (a low-risk patient never lands in the concordant-high group) and that group sizes sum.
- After any data regeneration, re-run the whole figure + table build; **don't** hand-patch one
  number.

## Honesty for simulated / teaching / example data

- If any values are simulated or de-identified surrogates, **say so on the figure and in the
  legend/footer**, and keep the *real* outcomes/labels where the story depends on them.
- Keep simulated quantities internally consistent (e.g. sub-volumes that must sum to a total
  actually sum to it; fractions in [0,1]); state the generative convention.
- Never present simulated numbers as real measured ones.

## Pre-export audit (run on the whole set)
- [ ] One palette, one font, one size ladder across **all** figures.
- [ ] Every figure number re-derived from data and equal to the table/text.
- [ ] KM curve ↔ numbers-at-risk ↔ censoring convention all consistent (`survival-figures.md`).
- [ ] Group counts reconcile across KM / bar / Sankey / data.
- [ ] Grayscale + color-blind check passed.
- [ ] Vector (`.svg`, text-as-text) + ≥300 dpi raster; legible at final width.
- [ ] Simulated/example data flagged; de-identification confirmed for imaging panels.

→ Palettes → `color-systems.md`. The statistics themselves → `radiology-stats`. Whether a figure
satisfies a reporting checklist → `radiology-reporting`.
