# Prognosis and risk-prediction study contract

Use this contract when imaging available at a defined prediction time estimates a future outcome or
risk. Keep these questions distinct:

- prognosis under the observed care context;
- diagnostic classification of a condition already present;
- treatment effect or differential treatment benefit.

A single-treatment cohort can support treatment-contextual prognosis, not a causal comparison between
treatments or a predictive-biomarker claim.

## 1. Freeze PICOTS and the estimand

| Field | Required specification |
|---|---|
| Population | eligibility, care setting, recruitment pathway and target deployment population |
| Index time | exact time at which prediction is made and predictors must be available |
| Predictors | imaging/clinical variables, acquisition timing and any prior/follow-up information |
| Outcome | definition, ascertainment, competing events and blinded adjudication where applicable |
| Horizon | fixed risk horizon(s) or time-to-event target; one primary horizon |
| Independent unit | patient unless a different biological unit and its clustering are explicitly justified |
| Treatment context | therapy available/received and whether treatment occurs before or after index time |
| Estimand | absolute risk, survival probability, hazard-related quantity or another defined prediction target |
| Intended use/action | counselling, surveillance, escalation, eligibility or research-only |
| Comparator | established clinical score/model and imaging-only/clinical-only simple baselines |
| Claim | development, internal performance, external evaluation, updating or prospective utility |

Align eligibility, index time, predictor window and start of follow-up. Excluding early events or
requiring a future scan can create immortal-time/guarantee-time bias.

## 2. Cohort and outcome contract

- Use patient-level recruitment and preserve center/calendar-time structure. Report exclusions,
  follow-up, event counts, competing events and censoring by partition.
- Define outcome ascertainment uniformly and before modelling. Record adjudicators, data sources,
  blinding, intervals, loss to follow-up and changes in criteria/version.
- Distinguish administrative censoring, loss to follow-up and competing events. Treating a competing
  event as ordinary non-informative censoring changes the estimand.
- Specify whether repeat lesions/examinations are aggregated, selected or modeled hierarchically.
  Lesions and slices do not increase patient-level outcome information.
- For treatment response/progression, route longitudinal measurement and time-dependent information to
  `response-longitudinal.md`; predictors observed after index time cannot enter a baseline model.

## 3. Development and leakage boundary

- Split by patient and, for transport claims, by site/time as intended. Freeze an untouched external
  evaluation cohort before tuning.
- Fit imputation, scaling, harmonisation, feature selection, representation learning, hyperparameters,
  calibration and risk thresholds within development data/folds only.
- A feature from follow-up, treatment response, outcome-related report text or an acquisition selected
  using future knowledge is leakage unless the estimand explicitly conditions on that landmark.
- Avoid univariable p-value screening and arbitrary dichotomization. Preserve continuous information
  with justified functional forms and regularization.
- Document candidate-parameter complexity, missingness, event information, model version and complete
  executable predictor definition.

## 4. Performance and clinical-value contract

Report all three performance dimensions:

1. **Calibration:** calibration-in-the-large/intercept, slope and a calibration plot at the primary
   horizon; appropriate observed-risk estimator under censoring/competing risks.
2. **Discrimination:** C-index and/or time-dependent AUC with definition and CI.
3. **Overall/decision performance:** Brier or other proper score and decision-curve/net benefit when a
   real action and threshold range are defined.

Also report risk distribution, event/nonevent counts, missingness, non-evaluable predictions and
clinically relevant site/subgroup estimates with uncertainty. A high AUC/C-index does not compensate
for poor calibration or establish utility.

Use bootstrap/nested resampling for internal optimism correction; report apparent and corrected values
clearly. External testing applies the complete frozen model first. Recalibration/updating on the
external cohort is a new model state and needs further independent evaluation.

## 5. Treatment, subgroup and causal boundaries

- Prognosis among treated patients means risk **under that observed treatment context**.
- A treatment-benefit claim requires a defined treatment contrast and causal identification plan.
- Effect modification requires a prespecified treatment-by-marker contrast on a stated scale; one arm
  significant and the other nonsignificant is not evidence of interaction.
- Subgroup performance audits fairness/transport only when the subgroup and estimand are defined. They
  do not establish different biological mechanisms or optimal treatment.

## 6. Sample size and sensitivity

Use an input-driven prediction-model framework: outcome incidence/event probability, follow-up and
censoring, candidate complexity, anticipated fit/shrinkage, calibration/discrimination precision,
validation design, clustering and missingness. A universal events-per-variable cutoff is not a design.

Predefine sensitivities for missing data, alternative outcome definitions/horizons, competing-risk
handling, influential observations, functional forms, site/protocol shift, treatment context and
complete-case versus imputed analyses where defensible.

Return `BIOSTATISTICIAN_REQUIRED` when event/censoring inputs, competing-risk estimand, hierarchical
structure or model-development/validation sample-size assumptions are unresolved.

## 7. Stop gates and claim ladder

Return `STOP_FOR_REPAIR` for undefined index time, predictors measured after prediction, outcome/test
leakage, patient overlap, test-set threshold/model selection, unreconciled event denominators or a
treatment-benefit claim without a treatment contrast.

- Development/internal resampling -> model-development performance only.
- Untouched temporal/geographic evaluation -> transport to that named setting/time.
- Updated-model evaluation on the update data -> adaptation, not external validation.
- Prospective impact study -> utility only for its prespecified workflow and outcomes.

Return: `PICOTS/estimand card -> cohort/event flow -> predictor/outcome definitions -> split/test-
access manifest -> model and sample-size brief -> calibration/discrimination/utility plan -> validation
and sensitivity matrix -> claim ceiling -> deviations`.

## Primary sources

- Collins GS, et al. [TRIPOD+AI](https://doi.org/10.1136/bmj-2023-078378).
- Moons KGM, et al. [PROBAST+AI](https://doi.org/10.1136/bmj-2024-082505).
- Riley RD, et al. [Minimum sample size for prediction-model development](https://doi.org/10.1136/bmj.m441).

Verify the current reporting/risk-of-bias versions through `radiology-reporting` at protocol freeze.
