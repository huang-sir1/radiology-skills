# Radiogenomics pitfalls — the reviewer's hit-list

Most radiogenomics rejections come from a short list of avoidable errors.

## 1. Data leakage / double-dipping
- Feature selection, harmonisation (ComBat), normalisation, or thresholding done on **all**
  data (incl. validation) → optimistic everything. Fit on **training only**; nest selection
  inside CV.
- "Cluster then test the clustering variable" (double-dipping) inflates significance.
- Patient-level splits; never split by slice/region within the same patient.

## 2. Batch / scanner / sequencing confounding
- Imaging: scanner, vendor, protocol, field strength. Omics: sequencing batch, platform,
  centre. If cases and controls differ by batch, your "signal" may be batch.
- Mitigate: harmonise (ComBat / ComBat_seq, biology preserved), adjust for site, and **test
  that the association survives**; show a batch-only model does not explain it.

## 3. Small-n optimism & overfitting
- Matched cohorts are tiny; thousands of features → spurious "AUC 0.95." Limit candidate
  features, use penalisation/stability, report optimism-corrected metrics, and validate
  externally.

## 4. Spatial mismatch (imaging vs sampled tissue)
- Bulk omics from one fragment vs whole-tumour radiomics; micron-scale spatial omics vs
  mm-scale imaging. Quantify registration/co-localisation uncertainty; prefer **habitat-** or
  **biopsy-localised** matching; bound claims accordingly.

## 5. Multiplicity not controlled
- Feature×gene grids generate millions of tests. No correction → false discoveries. Always
  FDR (or stronger) and pre-specify the primary hypothesis.

## 6. Reproducibility gaps
- Non-IBSI features, unstated discretisation, no segmentation ICC, unshared feature matrices,
  unversioned omics pipelines. These block replication (CLEAR/IBSI).

## 7. Over-interpretation
- Mechanistic claims from correlation; ignoring that bulk expression mixes cell types
  (deconvolve!); generalising from one tumour type or one scanner.

## Pre-submission self-check
`Matched n stated? · validation cohort present? · all data-dependent steps train-only? ·
batch tested + harmonised? · FDR applied + primary pre-specified? · IBSI/CLEAR met? ·
spatial matching + registration uncertainty stated? · claims bounded to association?`
