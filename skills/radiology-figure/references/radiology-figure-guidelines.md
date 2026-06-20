# Radiology (RSNA) figure requirements

> Verify exact numbers against the **current** _Radiology_ author instructions before
> submission — specs change. This file captures durable conventions.

## File format & resolution
- **Vector** for charts/diagrams: `.svg`/`.pdf`/`.eps` (editable; text as text). This skill
  produces `.svg` as primary.
- **Raster** for images/photographs: **TIFF/PNG**, **≥ 300 dpi** (line art / combination art
  often **600–1200 dpi**). Export a raster companion of every chart too.
- Do not upscale a low-res raster; do not save charts only as low-dpi PNG.

## Size & layout
- Design to column width: **single ~85 mm**, **double ~170 mm**. Build at final size so fonts
  are correct.
- Multi-panel: label **A, B, C** (bold, consistent corner). Align panels on a grid; equal
  gutters.

## Typography
- **Sans-serif** (Arial/Helvetica). Minimum ~**7 pt** at final print size; axis titles a bit
  larger. Consistent sizes across panels.
- Avoid tiny tick labels, overlapping text, and 3-D effects.

## Color
- **Color-blind-safe**; never encode meaning by **red/green alone**. Use palette in
  `design-theory.md`. Keep enough contrast for grayscale printing.
- Use color to encode data, not decoration. Grayscale for anatomical images unless color
  carries information (e.g. overlays, parametric maps with a labelled colorbar).

## Imaging panels — de-identification (mandatory)
- **No PHI** in pixels: scrub patient name/MRN/dates from DICOM overlays and corners; remove
  burned-in annotations; no identifiable faces (defacing for 3-D/face MRI).
- Report **windowing** (window level/width) and modality/sequence.
- Add a **scale bar** or state field-of-view when lesion size matters.
- Use arrows/arrowheads/asterisks to point to findings; define them in the legend.

## Statistical graphics honesty
- Show **uncertainty** (CI bands, error bars — define whether SD/SE/CI) and **n**.
- Don't truncate axes to exaggerate; if truncated for clarity, make it obvious.
- ROC: plot to (0,0)–(1,1), square aspect, diagonal reference; annotate AUC + CI.
- Kaplan-Meier: include a **numbers-at-risk** table beneath the x-axis; mark censoring.

## Legends/captions
- Self-contained: define abbreviations, arrows, error bars, n, statistical test, and
  windowing. (Prose → `radiology-writing`.)

## Final QA
`vector + 300dpi raster? · text-as-text? · column width? · fonts legible at size? ·
color-blind-safe? · CI + n shown? · panels A/B/C? · images de-identified + windowing +
scale bar? · no invented data?`
