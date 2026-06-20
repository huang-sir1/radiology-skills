# radiology-annotation

**Stage 2 — Data & Annotation.** Make the ROI/VOI/mask behind a radiomics, segmentation, or
radiogenomics study defensible — and write the Methods paragraph.

## What it does

- **Annotation SOP** — lesion-selection strategy (2D/2.5D/3D, whole-tumour/largest-slice/
  peritumoral/habitat, multi-lesion rule), justified by endpoint and biology.
- **Reader protocol** — number, seniority, blinding, independent-vs-consensus, third-party
  adjudication, segmentation-training phase.
- **Reproducibility & QC** — repeat-annotation design, ICC/Dice/Hausdorff, feature-stability
  filtering (applied before selection, training-only), sensitivity analysis.
- **Geometry integrity** — spacing/origin/direction/slice-order checks across DICOM, NIfTI,
  DICOM-SEG, RTSTRUCT; conversion pitfalls and a programmatic QC check.
- **Methods paragraph** — submission-ready prose with placeholders for values to be measured.

## Trigger examples

- "帮我写 ROI 标注 SOP 和 Methods（勾画规范、一致性）。"
- "Two radiologists contoured the tumours — how do I report agreement and keep stable features?"
- "My masks don't align with the images after DICOM→NIfTI conversion."

## Reference files

| File | Use |
|---|---|
| `references/lesion-selection.md` | 2D/3D, region, peritumoral, habitat, multi-lesion rule |
| `references/reader-protocol.md` | Readers, blinding, consensus/adjudication, training |
| `references/reproducibility-qc.md` | ICC/Dice/HD, feature-stability filtering, sensitivity |
| `references/mask-geometry.md` | Spacing/origin/direction/slice-order; format conversions |

## Handoffs

`radiology-radiomics` (feature extraction) · `radiology-reporting` (IBSI/CLEAR) ·
`radiology-stats` (ICC model, Bland-Altman) · `radiology-radiogenomics` (habitats) ·
`radiology-data` / `radiology-ethics` (de-identifying shared masks).

Specifies and reports annotation; does not perform clinical contouring.
