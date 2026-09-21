# Lesion-selection strategy

Pre-specify the rule; apply it uniformly; justify it by the endpoint and biology.

## Dimension: 2D vs 3D

| Choice | Use when | Trade-off |
|---|---|---|
| **2D (single slice)** | Largest cross-section convention; fast; thick slices | Misses volumetric heterogeneity; slice-choice variability |
| **2.5D (few slices)** | Compromise; some volumetric context | Still ROI-placement dependent |
| **3D (whole volume)** | Volumetric features, heterogeneity, habitats | Costlier; more sensitive to segmentation error and slice thickness |

State slice thickness and whether features are slice-thickness robust.

## Region of interest

- **Whole tumour** — default for most radiomics; captures global heterogeneity.
- **Largest slice** — common, reproducible-ish, but discards volume; justify if used.
- **Sub-regions** — enhancing core, necrosis, edema; biologically meaningful, but each needs its
  own reproducibility.
- **Peritumoral ring** — fixed-distance dilation (state mm) capturing micro-environment/invasion;
  report how the ring is constructed and that it stays within anatomy.
- **Habitats** — voxel clustering into sub-regions by multi-parametric signature; align with
  spatial/regional omics (→ radiology-radiogenomics).

## Multi-lesion handling (decide explicitly)

- **Index lesion only** (define the rule: largest / most FDG-avid / target lesion).
- **All lesions** with patient-level aggregation (mean / largest / worst) — define the rule.
- **Per-lesion analysis** with clustering accounted for in statistics (→ radiology-stats).
- Never let lesions from one patient cross train/test splits (patient-level partition).

## Justification checklist

- Does the region match the **endpoint** (e.g. peritumoral for invasion; habitats for spatial
  biology)?
- Is the rule **uniform** across all cases and centers?
- Is the dimension consistent with slice thickness and the feature set?
- Is the multi-lesion rule defined and leakage-safe?

## Reporting sentence

*"For each patient the index lesion (largest by long-axis diameter) was segmented volumetrically
on contrast-enhanced T1 across all slices; a 3-mm peritumoral ring was added by morphological
dilation constrained to soft tissue. Sub-region habitats were defined by voxel-wise k-means on
co-registered T1c/T2/ADC."*
