# Nature-portfolio figure specification

Use this file instead of (not in addition to conflicting rules in)
`radiology-figure-guidelines.md` when the target is a Nature-portfolio venue (Nature Medicine,
Nature Biomedical Engineering, Nature Communications, npj Digital Medicine, Nature Machine
Intelligence, etc.). The design-theory principles (honest graphics, color-blind-safe palette,
one-figure-one-message, anti-redundancy) are venue-independent and still apply — only the
**mechanical spec** below changes. Verify exact current numbers against the specific journal's
figure guide before final submission; this file records durable, recently-verified conventions.

## Panel labelling — the one rule most likely to be gotten backwards

> **Nature-portfolio default: lowercase, bold, upright a, b, c** (not italic), ~8 pt, top-left of
> each panel. This is the opposite convention from the _Radiology_-family default (uppercase
> **A, B, C**) used elsewhere in this skill. Set the case explicitly — see `api.md`'s
> `panel_letter()` helper, which takes `case="lower"` for Nature-family output instead of the
> `case="upper"` _Radiology_ default. Do not mix cases within one figure set.

- Multi-panel figures must be assembled as **one single image file** per figure (all sub-panels
  combined) — do not upload panels individually.
- Figure legends: begin with a short title for the whole figure, then a short description per
  panel and every symbol used; the parsed Nature Partner Journals guide uses **≤ 250 words**
  as the figure-legend ceiling. Some venue-specific instructions differ — verify before final
  submission.

## Size

| Element | Spec |
|---|---|
| Single column | **89 mm** wide |
| Column-and-a-half | 120–136 mm wide |
| Double column (full width) | **183 mm** wide |
| Maximum figure height | **170 mm** (leaves room for the legend beneath; full page depth is 247 mm) |

Build the figure at final size (not scaled down later) so font sizes hold — same discipline as
the _Radiology_ workflow, different numbers. Update `SINGLE, DOUBLE` in `api.md` for a
Nature-family run (89/25.4, 183/25.4 inches) rather than reusing the 85/170 mm _Radiology_
constants.

## Typography & color

- Sans-serif throughout (Helvetica/Arial), one family for **every** figure in the paper — same
  rule as `design-theory.md`.
- Lettering (axis labels etc.): lower-case type with the first letter capitalised, no full stop.
- Color mode: **RGB** for online/digital submission (not CMYK).
- White background; avoid excessive boxing, unnecessary color, decorative effects, 3D
  histograms, and axis truncation that exaggerates differences.
- Use scale bars rather than magnification factors for images; define scale-bar length in the
  legend.
- Color-blind-safe palette and semantic color→meaning mapping rules are unchanged — reuse
  `color-systems.md`/Okabe-Ito or the NPG palette (NPG already approximates a "Nature-journal"
  look and is a reasonable default here, see `color-systems.md`).

## Display-item budget (main text vs Extended Data vs Source Data)

Nature-family venues cap the **main-text** display items tightly (verify the current number for
the specific venue — it is small, commonly single digits) and route the rest to:

- **Extended Data** — additional figures/tables that are peer-reviewed and published with the
  article (up to a per-venue cap, commonly cited as up to ~10 items — verify live). Use for
  supporting analyses a methods-literate reader would want but that don't carry the headline
  claim.
- **Supplementary Information** — not separately peer-reviewed in the same way, not typeset;
  use for bulk material (full statistical tables, extended cohort tables, code listings).
- **Source Data** — the raw numbers behind **every** graph, as a structured file (commonly one
  tab/sheet per figure panel), linked explicitly to the figure it supports. This is a Nature
  Portfolio publication requirement, not optional supplementary material — plan for it from the
  first figure script, the same way `figure-set-consistency.md` already insists every plotted
  number is re-derived from the data file rather than hand-typed. In practice: export the exact
  dataframe/array used to draw each panel alongside the figure at generation time.

Decide the main vs Extended Data split **before** finalising the figure count; hand off the
plan to `radiology-writing`/`nature-family-shape.md` (display-item plan) and to `radiology-data`
(Source Data + Extended Data availability wording).

## Imaging panels, statistical charts, de-identification

All content rules in `imaging-panels.md`, `chart-types.md`, and `radiology-figure-guidelines.md`
(windowing, scale bars, arrows, de-identification, ROC/KM/calibration construction, honest axes,
uncertainty shown) are **venue-independent** and carry over unchanged. Only panel-letter case,
column widths, legend word limit, RGB mode, and the Extended Data/Source Data split are
Nature-specific.

## QA checklist (Nature-family, run in addition to the shared checklist)

- [ ] Panel letters lowercase, bold, upright (`case="lower"`), not uppercase.
- [ ] Figure built at 89 mm / 120–136 mm / 183 mm width, ≤170 mm height.
- [ ] Multi-panel figure exported as one assembled image file, not separate panel files.
- [ ] Legend follows the target venue cap (≤250 words for the parsed Nature Partner guide;
      verify if the target journal specifies a different limit) and begins with a whole-figure
      title.
- [ ] RGB color mode.
- [ ] Source Data file prepared per figure (values match the plotting script's dataframe, per
      `figure-set-consistency.md`).
- [ ] Main vs Extended Data split decided and consistent with the manuscript's display-item plan.

## Handoffs
- Figure content rules (chart choice, imaging panels, de-identification) → `radiology-figure`
  main workflow (venue-independent).
- Manuscript display-item plan, abstract/word budget → `radiology-writing/nature-family-shape.md`.
- Source Data / Extended Data availability wording, "condition of publication" language →
  `radiology-data`.
- Reporting Summary cross-check for any figure that reports a statistic → `radiology-reporting`.
