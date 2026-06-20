# Survival & prognostic modelling

Use when the endpoint is **time-to-event** (OS, PFS, recurrence). Common in radiogenomics
(imaging/omics signature → prognosis).

## Core toolkit
- **Kaplan-Meier** curves + **log-rank** test for group comparison. Report median survival
  with 95% CI and numbers-at-risk under the x-axis (a _Radiology_ figure expectation).
- **Cox proportional-hazards** for covariate effects → hazard ratios with 95% CI.
- **C-index** (Harrell's) for discrimination; **time-dependent AUC** for discrimination at a
  horizon; **calibration** at fixed time points (e.g. 1/3/5-yr) — discrimination alone is
  not enough, same as for binary models.

```python
from lifelines import KaplanMeierFitter, CoxPHFitter
from lifelines.statistics import logrank_test
cph = CoxPHFitter().fit(df, duration_col="time", event_col="event")
cph.print_summary()              # HRs + CIs
cph.check_assumptions(df)        # proportional hazards (Schoenfeld)
print(cph.concordance_index_)
```

## Assumptions & pitfalls
- **Proportional hazards** — test with Schoenfeld residuals; if violated, use
  time-varying coefficients, stratification, or restricted mean survival time (RMST).
- **Dichotomising a continuous score** at an "optimal" cutpoint inflates significance and is
  often a reviewer flag (cut-point on the same data). Pre-specify or keep continuous; if a
  cut-point is clinical, validate it.
- **EPV** for Cox = events per variable (aim ≥ 10–15, or use Riley); imaging/omics signatures
  must avoid overfitting (build signature, then fit Cox on the signature, not 800 raw
  features).
- **Competing risks** — if non-event deaths compete, use cumulative incidence (Aalen-Johansen)
  and **Fine-Gray** subdistribution hazards, not naive KM.
- **Immortal-time / lead-time bias** — define time-zero and exposure carefully.
- **Independent validation** of a prognostic signature is expected.

## Reporting sentence
*"The radiomic signature was associated with overall survival (HR 2.1; 95% CI: 1.4, 3.2;
P = .001, Cox), with a C-index of 0.71 (95% CI: 0.65, 0.77) and acceptable 3-year
calibration. Proportional hazards held (Schoenfeld P = .34)."*

## Reviewer hot-spots
Optimal cut-point on the same cohort; PH not tested; competing risks ignored; HR reported
without CI; signature overfit (Cox on raw high-dimensional features); no external validation.
