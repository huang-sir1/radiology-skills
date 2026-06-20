# Feature selection, modelling & the signature/score

The single rule: **every data-dependent step is fit inside training only.** Selection on the
whole cohort is the most common radiomics leak.

## Selection pipeline (all inside CV / training folds)

1. **Reproducibility filter** — drop low-ICC features (from radiology-annotation), threshold
   pre-specified.
2. **Unsupervised pruning** — near-zero variance; collapse highly correlated features
   (e.g. |r| > 0.9 keep one).
3. **Supervised selection** — univariate screen (with multiplicity awareness), or embedded
   methods: **LASSO**, elastic net, **mRMR**, Boruta/RF importance.
4. **Dimensionality** — keep the final feature:event ratio sane (EPV → radiology-stats).

> Wrong: rank features by association on the full dataset, then cross-validate the chosen set.
> Right: re-run selection inside each training fold; report selection stability.

## Modelling

- Match the model to n/EPV: penalised regression for small n; tree ensembles/SVM when justified;
  avoid heavy models on tiny cohorts.
- Tune hyperparameters with **nested CV** (inner loop) — never on the test set.
- Pre-specify the **primary** model; others are exploratory.

## Building a radiomics signature / score

- Combine selected features into a single score (e.g. LASSO linear predictor → "Rad-score").
- Optionally a **nomogram** combining Rad-score with clinical variables — report both the
  combined and component models.
- Report the formula/coefficients (supplement) for reproducibility.

## Validation & reporting (hand computation to radiology-stats)

- Internal: nested CV or bootstrap optimism correction.
- External/temporal/geographic: pipeline frozen.
- Metrics: discrimination (AUC/C-index + CI), **calibration** (slope/intercept, Brier),
  **decision-curve** — not AUC alone.
- Report selection stability and per-center performance where relevant.

## Reporting sentence

*"Within each training fold, features were filtered (ICC > 0.80, variance, correlation |r| < 0.9)
and selected by LASSO; the linear predictor defined a radiomics score. The primary model (Rad-
score + clinical) was validated externally with the pipeline frozen; discrimination,
calibration, and decision-curve analysis are reported with 95% CIs."*
