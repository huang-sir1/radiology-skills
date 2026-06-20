# Reproducibility & QC of annotation and features

Quantify segmentation error and remove the features it corrupts — **before** selection/modelling,
on training data only.

## Metrics

| Metric | Measures | Notes |
|---|---|---|
| **ICC** | Agreement of continuous features / volumes across readers | State the ICC model (two-way random, absolute agreement, single vs average); → radiology-stats |
| **Dice (DSC)** | Volumetric overlap of masks | Sensitive to small structures; report per-region |
| **Jaccard (IoU)** | Overlap (stricter than Dice) | Alternative to Dice |
| **Hausdorff (HD95)** | Boundary distance | Use 95th percentile to limit outlier sensitivity |
| **Volume difference / Bland-Altman** | Systematic vs random volume bias | Pairs with ICC |

## Repeat-annotation design

- Define the **subset** (all cases, or a random sample with a stated size and rationale).
- **Inter-observer:** ≥2 independent readers on the subset.
- **Intra-observer:** one reader, re-segment after a washout (e.g. ≥2 weeks).
- Pre-specify when (before feature extraction) and on which split (training subset).

## Feature-stability filtering (the step reviewers look for)

1. Extract features from each reader's masks on the reproducibility subset.
2. Compute per-feature ICC across readers (and intra-reader).
3. **Retain** features above a pre-specified threshold (commonly ICC > 0.75–0.90; state it).
4. Apply the filter **before** feature selection/modelling, fit on **training only** — never
   choose the threshold to maximise downstream performance.
5. Report how many features entered and survived.

## Sensitivity analysis

- Show the main result is stable to reader choice (e.g. repeat with reader B's masks) or to the
  ICC threshold. A result that flips with the segmenter is not robust.

## Leakage warnings specific to annotation

- Computing stability or selecting features using the **whole** cohort (including test) — leak.
- Choosing the ICC threshold to maximise AUC — circular.
- Letting one patient's repeat-segmentations inform both train and test — patient-level only.

## Reporting sentence

*"Of 1218 extracted features, 842 with inter-observer ICC > 0.80 (two-way random-effects,
absolute agreement) were retained prior to selection, which was performed within the training
folds only; results were stable when repeated with the second reader's segmentations."*
