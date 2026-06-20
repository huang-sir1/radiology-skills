# radiology-radiomics

**Stage 3 — Modeling & Analysis.** Design or audit a hand-crafted radiomics study end-to-end to
CLEAR / IBSI standard — reproducible and leakage-free.

## What it does

- **Pipeline spec** — preprocessing → extraction → selection → modelling → validation, each step
  with parameters and the leakage control marked.
- **IBSI-compliant parameters** — resampling, intensity normalisation, gray-level discretisation
  (bin width vs count), filters, feature families, software + version (PyRadiomics parameter
  file).
- **Leakage-safe selection & modelling** — ICC/variance/correlation/LASSO/mRMR inside training
  folds, EPV-aware models, radiomics signature/score and nomogram.
- **Leakage audit** — the patient-level / fit-on-training / tuning / reproducibility / evaluation
  checklist reviewers enforce.
- **Methods paragraph** — CLEAR/IBSI-aligned prose.

## Trigger examples

- "帮我设计/审查影像组学流程（PyRadiomics、IBSI）。"
- "Bin width or bin count? what resampling and filters?"
- "How do I do LASSO feature selection without leakage?"

## Reference files

| File | Use |
|---|---|
| `references/preprocessing-ibsi.md` | Resampling, normalisation, discretisation, filters, IBSI reporting |
| `references/feature-extraction.md` | Feature families, PyRadiomics settings, parameter file |
| `references/selection-modelling.md` | Leakage-safe selection, modelling, signature/score, EPV |
| `references/leakage-audit.md` | The radiomics leakage checklist |

## Handoffs

`radiology-annotation` (masks, stability) · `radiology-reporting` (IBSI/CLEAR/METRICS/RQS) ·
`radiology-stats` (CV, calibration, DCA, multiplicity, sample size) ·
`radiology-deep-learning` (deep-feature comparison) · `radiology-radiogenomics` (biology) ·
`radiology-figure` (ROC, calibration, nomogram).
