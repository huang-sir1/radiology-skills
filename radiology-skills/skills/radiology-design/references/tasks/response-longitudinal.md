# Response and longitudinal-imaging study contract

Use this contract for repeated imaging, treatment response, progression, growth, delta-radiomics or
time-varying imaging biomarkers. First decide whether the study estimates **change**, predicts a future
outcome from a landmark, compares treatment strategies or evaluates effect modification. These are not
interchangeable.

## 1. Freeze the longitudinal estimand

| Field | Required specification |
|---|---|
| Population/treatment context | eligibility, disease state, line/regimen and care setting |
| Time zero | treatment start, diagnosis, surgery or another reproducible origin |
| Imaging schedule | windows, modality/series, allowed deviations and reason for unscheduled imaging |
| Target/measurement | lesion/organ/burden, criteria/version, reader/algorithm and quantitative units |
| Response endpoint | continuous change, categorical response, progression, time-to-event or transition |
| Intercurrent events | treatment switch/stop, surgery, death, new lesion, missing scan and rescue therapy strategy |
| Primary unit | patient; define lesion/timepoint nesting and target-lesion selection |
| Estimand class | measurement change, treatment-contextual prognosis, ATE, effect modification or dynamic prediction |
| Primary contrast/horizon | exact visits/strategies/states compared and effect measure |
| Claim ceiling | descriptive, prognostic, causal treatment, predictive biomarker or utility |

State whether a post-baseline scan is required to enter the analysis. Conditioning on surviving or
remaining progression-free until that scan changes the target population and can create guarantee-time
bias.

## 2. Acquisition, registration and measurement

- Freeze sequence/phase, reconstruction, contrast timing, scanner/protocol ranges, quality rules and
  acceptable visit windows. Record deviations per timepoint rather than averaging them away.
- For delta features, define spatial registration, resampling, interpolation, contour propagation,
  manual correction and failure criteria. Quantify registration/segmentation sensitivity.
- Identify lesions across time with a stable patient-exam-lesion identifier and explicit split/merge,
  disappearance, new-lesion and non-target-lesion rules.
- Report technical repeatability and biologic change separately. A change smaller than measurement
  error cannot be treated as proven biology or response.
- Name and version disease-specific criteria (e.g. RECIST/iRECIST when applicable), but verify live
  applicability with the clinical-domain owner; no generic rule replaces specialist judgment.

## 3. Missingness and observation process

Repeated imaging is usually informative: sicker patients may scan earlier, miss visits, switch therapy
or die. Record why each scheduled scan is absent and who remains observable.

- Predefine the analysis population and strategies for death, progression before scan, treatment
  switching, off-window imaging and non-evaluable scans.
- Distinguish intermittent missing measurements from dropout/terminal events.
- Consider inverse-probability methods, joint models or sensitivity analyses only when their assumptions
  and nuisance inputs are supportable; mixed models do not automatically fix informative dropout.
- An unscheduled scan triggered by symptoms is not exchangeable with a scheduled scan without an
  explicit observation-process model or claim boundary.

## 4. Analysis routes

| Estimand | Candidate analysis | Critical safeguards |
|---|---|---|
| Mean/trajectory change | paired contrast, mixed model or GEE | time form, covariance, patient clustering, informative missingness |
| Response category | patient-level binary/ordinal model | criteria version, confirmation rule and non-evaluable state |
| Time to progression/death | survival/competing-risk or multi-state model | time zero, interval censoring, competing event and transition definitions |
| Dynamic risk using updated imaging | landmark or joint longitudinal-event model | predictors available at landmark, validation by time and no future leakage |
| Treatment contrast | randomized or defensible causal design | aligned eligibility/time zero, exchangeability, positivity, switching/adherence |
| Effect modification | treatment-by-imaging-marker contrast | prespecified scale, adequate overlap, multiplicity and independent confirmation |

Specify whether inference is subject-specific or population-average. For multiple lesions, choose a
patient-level rule or hierarchical model; analyzing each lesion as an independent patient is invalid.

## 5. Validation and robustness

- Freeze measurement and prediction definitions before test access; keep all patient timepoints in one
  partition.
- Validate the longitudinal pipeline across site/scanner/protocol and realistic visit-window drift.
- Report calibration and time-dependent discrimination for dynamic prediction, not only association.
- Predefine sensitivities to visit window, baseline/landmark choice, target-lesion rule, criteria
  version, registration/segmentation, missingness, treatment switching and competing risks.
- Use negative/control analyses where possible, such as non-target anatomy, implausible future-to-past
  prediction or label/time permutation, to detect leakage and protocol signal.

## 6. Sample size and stop gates

Plan using independent patients, number/timing of repeated observations, event/transition counts,
within-patient covariance, dropout/competing events, treatment allocation/overlap and model complexity.
Extra scans do not substitute for patients. Use simulation/scenario analysis for complex joint,
multi-state or informative-observation designs.

Return `STOP_FOR_REPAIR` for undefined time zero, future information entering baseline prediction,
untraceable lesion linkage, post-result visit-window/response redefinition, patient overlap or a causal
treatment claim without identification. Return `BIOSTATISTICIAN_REQUIRED` for unresolved joint/multi-
state/interval-censored or time-varying-confounding inference.

## 7. Claim boundary and handoff

Observed change may reflect biology, treatment, acquisition, registration and measurement error.
Prognosis under one regimen is not treatment effect; association of change with outcome is not proof
that changing the biomarker changes outcome.

Return: `longitudinal estimand card -> visit/acquisition manifest -> lesion-linkage and measurement
protocol -> intercurrent-event/missingness table -> analysis and sample-size brief -> validation/
sensitivity plan -> claim ceiling -> deviations`.

## Primary and official sources

- Eisenhauer EA, et al. [RECIST 1.1](https://doi.org/10.1016/j.ejca.2008.10.026).
- Seymour L, et al. [iRECIST](https://doi.org/10.1016/S1470-2045(17)30074-8).
- ICH. [E9(R1) Estimands and Sensitivity Analysis](https://database.ich.org/sites/default/files/E9-R1_Step4_Guideline_2019_1203.pdf).
- Collins GS, et al. [TRIPOD+AI](https://doi.org/10.1136/bmj-2023-078378).
