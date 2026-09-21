# Survival and model tables

## Cox regression table

Minimum columns:

| Variable / level | Unit or contrast | Univariable HR (95% CI) | P value | Multivariable HR (95% CI) | P value |
|---|---|---|---|---|---|

Add or footnote:

- endpoint, time origin, censoring rule, n and event count;
- reference level for every categorical variable;
- scaling for continuous variables (per unit, SD, 10 units, log transform);
- covariate-selection strategy and full adjustment set;
- missing-data method;
- proportional-hazards assessment and action if violated;
- penalization/shrinkage and bootstrap/nested-CV use where applicable;
- multiplicity status for exploratory features.

Do not report a dichotomized risk score without the cut-point source and whether it was fixed in training.

## Prognostic model performance

Use separate rows by cohort and time horizon:

| Cohort | Model | C-index (95% CI) | AUC at t (95% CI) | Brier at t | Calibration slope/intercept | DCA range | n/events |
|---|---|---|---|---|---|---|---|

State whether estimates are apparent, optimism-corrected, cross-validated, temporal, geographic, or
external. Do not call internal resampling external validation.

## Incremental-value table

For clinical, radiomics, and combined models, report the same cohort, horizon, and evaluation method.
Include effect on discrimination and calibration; add likelihood-ratio, NRI/IDI, or net benefit only when
pre-specified and statistically defensible. Never let a small AUC increase stand alone as clinical utility.

## Nomogram coefficient table

A nomogram is a display of a fitted model, not a separate analysis. Preserve:

- original coefficient, variable transformation, reference level, and scaling;
- points mapping and total-score-to-risk transformation;
- baseline survival or intercept needed to reproduce absolute risk;
- target time horizon and cohort used to fit the model.

Any rounded points table must remain traceable to full-precision coefficients.

## Radiomics feature audit table

Recommended rows:

| Stage | Rule fitted on | Input features | Retained features | Threshold/tuning | Output artifact |
|---|---|---:|---:|---|---|
| extraction | all images by fixed parameter file | ... | ... | IBSI/PyRadiomics config | feature matrix |
| stability | training/retest subset | ... | ... | ICC model + threshold | stable set |
| redundancy | training only | ... | ... | correlation rule | de-correlated set |
| selection | training folds only | ... | ... | LASSO/mRMR/etc. | selected set |
| final model | locked training pipeline | ... | ... | penalty/tuning | model object |

Counts must reconcile from stage to stage. Record feature-family and transformed names in a supplementary
dictionary so figures, equations, and tables use the same labels.

