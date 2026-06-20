---
name: radiology-annotation
description: "Design and document ROI/VOI/mask annotation that survives Radiology (RSNA) review — lesion-selection strategy (2D vs 3D, whole-tumour vs largest-slice vs peritumoral vs habitat vs multi-lesion), reader protocol (number, seniority, blinding, independent vs consensus, third-party adjudication), reproducibility (repeat annotation, ICC, Dice, Hausdorff, feature-stability filtering), and geometric integrity of masks against DICOM/NIfTI/DICOM-SEG/RTSTRUCT (spacing, origin, direction, slice order). Use when the user mentions ROI, VOI, mask, segmentation protocol, contouring, \"标注\", \"勾画\", \"分割规范\", inter-/intra-observer agreement, or needs the Methods paragraph for annotation. Produces an annotation SOP, a QC plan, and submission-ready Methods text. Never invents agreement values or reader details."
---

# ROI / VOI / Mask Annotation SOP

Use this skill to make the **annotation** behind a radiomics/segmentation/radiogenomics study
defensible. Reviewers reject papers when the segmentation is a black box: unknown readers,
no reproducibility, masks that don't align with the images, or feature instability never tested.
This skill specifies the lesion-selection strategy, the reader protocol, the reproducibility
plan, and the geometric checks — and writes the Methods text.

## Core stance

- **Segmentation is a measurement, so characterise its error.** Report inter-/intra-observer
  reproducibility and propagate it (drop unstable features) — don't treat masks as ground truth.
- **Pre-specify the lesion-selection rule.** 2D vs 3D, whole-tumour vs largest-slice vs
  peritumoral ring vs sub-regional habitat vs multi-lesion handling — decided up front, applied
  uniformly, and justified by the biology and the endpoint.
- **Readers are part of the method.** Number, seniority, blinding to outcome, independent vs
  consensus, and the adjudication rule for disagreement all belong in Methods.
- **Geometry must be exact.** Mask and image must share spacing, origin, direction, and slice
  order; a one-voxel or flipped-axis mismatch silently corrupts every feature.
- **Reproducibility before modelling.** Filter to reproducible features (e.g. ICC threshold)
  **before** selection/modelling, on training data only — leakage hides here too.
- **Integrity.** Never invent ICC/Dice values, reader counts, or QC results; mark what must be
  measured.

## When to use

- "Design an ROI/mask annotation SOP / 帮我写标注 SOP（勾画规范）。"
- "Two radiologists contoured the lesions — how do I report agreement and select stable features?"
- "Whole-tumour or largest-slice? 2D or 3D? peritumoral? habitat?"
- "My masks don't line up with the images / DICOM-SEG/RTSTRUCT conversion issues."
- "Write the segmentation + reproducibility paragraph for Methods."

## When to open extra files

| File | Open when |
|---|---|
| [references/lesion-selection.md](references/lesion-selection.md) | Choosing 2D/3D, whole-tumour/largest-slice/peritumoral/habitat/multi-lesion; what the endpoint and biology imply |
| [references/reader-protocol.md](references/reader-protocol.md) | Reader number/seniority, blinding, independent vs consensus, adjudication, training set |
| [references/reproducibility-qc.md](references/reproducibility-qc.md) | Repeat-annotation design, ICC/Dice/Hausdorff, feature-stability filtering, sensitivity analysis |
| [references/mask-geometry.md](references/mask-geometry.md) | DICOM/NIfTI/DICOM-SEG/RTSTRUCT spacing/origin/direction/slice-order checks, conversion pitfalls |

## Workflow

1. **Fix the target.** What is segmented (whole tumour, core, necrosis, edema, node, organ),
   in which modality/sequence/phase, and why that target serves the endpoint.
2. **Choose the selection strategy** (lesion-selection.md) — dimension, region, peritumoral
   extent, habitats, and the multi-lesion rule. Justify it.
3. **Specify the reader protocol** (reader-protocol.md) — who, how many, blinded to what,
   independent vs consensus, adjudication, and any segmentation-training phase.
4. **Plan reproducibility** (reproducibility-qc.md) — repeat-annotation subset, ICC/Dice/HD,
   the feature-stability filter and threshold, and a sensitivity analysis.
5. **Verify geometry** (mask-geometry.md) — confirm image↔mask spacing/origin/direction/slice
   order; document the conversion path (DICOM-SEG/RTSTRUCT/NIfTI) and QC.
6. **Write Methods** — the annotation paragraph: target, software+version, readers, blinding,
   reproducibility, stability filtering — in _Radiology_ style.

## Output contract

1. **`Annotation SOP`** — target, selection strategy, software/version, step-by-step procedure.
2. **`Reader protocol`** — number/seniority/blinding/independent-or-consensus/adjudication.
3. **`Reproducibility & QC plan`** — repeat design, metrics (ICC/Dice/HD), stability filter +
   threshold, sensitivity analysis — with placeholders for values to be measured.
4. **`Geometry checklist`** — the alignment/conversion checks and their pass/fail.
5. **`Methods paragraph`** — submission-ready prose (+ 待确认 list for Chinese authors).

## Quality bar

A good annotation spec lets an independent group reproduce the masks and the feature set, tells
the reviewer exactly how segmentation error was measured and controlled, and never reports an
agreement value that was not computed.

## Handoffs

- IBSI feature reproducibility / CLEAR-METRICS audit → `radiology-reporting`.
- Hand-crafted feature extraction pipeline → `radiology-radiomics`.
- ICC model choice, Dice/Bland-Altman statistics → `radiology-stats`.
- Habitat masks for imaging×omics → `radiology-radiogenomics`.
- De-identifying shared masks/images → `radiology-data` / `radiology-ethics`.
- This skill specifies and reports annotation; it does not perform clinical contouring.
