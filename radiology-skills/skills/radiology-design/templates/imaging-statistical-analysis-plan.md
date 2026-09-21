# Imaging statistical analysis plan — fillable template

This SAP specifies inference before confirmatory outcome inspection or protected-test access. It does
not authorize data access or execution. Use `AUTHOR_INPUT_NEEDED`, `NOT_VERIFIED`, `NOT_APPLICABLE`,
`STOP_FOR_REPAIR` or `BIOSTATISTICIAN_REQUIRED`; never invent nuisance inputs or results.

## 1. Document and freeze control

| Field | Value |
|---|---|
| Study/protocol ID and version | [AUTHOR_INPUT_NEEDED] |
| SAP ID / version / date | [AUTHOR_INPUT_NEEDED] |
| Protocol/registration locator | NOT_VERIFIED |
| Data snapshot / cohort manifest digest | [AUTHOR_INPUT_NEEDED] |
| Split manifest / test-access ledger | [AUTHOR_INPUT_NEEDED] |
| Software/environment target | [AUTHOR_INPUT_NEEDED] |
| SAP freeze date/digest/approver roles | [AUTHOR_INPUT_NEEDED] |
| Outcome/test information seen before freeze | [AUTHOR_INPUT_NEEDED] |
| Amendments/deviations locator | [AUTHOR_INPUT_NEEDED] |

## 2. Primary question and estimand

| Field | Frozen specification |
|---|---|
| Population / analysis setting | [AUTHOR_INPUT_NEEDED] |
| Index test/exposure/intervention | [AUTHOR_INPUT_NEEDED] |
| Comparator | [AUTHOR_INPUT_NEEDED] |
| Outcome/target/measurement | [AUTHOR_INPUT_NEEDED] |
| Time zero / horizon / visit | [AUTHOR_INPUT_NEEDED] |
| Independent unit and hierarchy | [AUTHOR_INPUT_NEEDED] |
| Estimand / treatment or prediction target | [AUTHOR_INPUT_NEEDED] |
| Effect/performance measure | [AUTHOR_INPUT_NEEDED] |
| Threshold/margin and derivation source | [AUTHOR_INPUT_NEEDED] |
| Primary hypothesis / CI / success criterion | [AUTHOR_INPUT_NEEDED] |
| Allowed claim if passed | [AUTHOR_INPUT_NEEDED] |

## 3. Data structure and analysis populations

- Participant/patient, examination, series, lesion, ROI, reader, site and timepoint keys:
- Biological versus technical units and nesting:
- Source tables/files and immutable snapshot:
- Derivation/development population:
- Full-analysis/intention-to-treat-like population, if applicable:
- Per-protocol/evaluable population and role:
- Safety/failure population:
- External/prospective population:
- Inclusion/exclusion/non-evaluable flow reconciliation:
- Duplicate/overlap/public-data contamination checks:

No slice, tile, lesion, reader score, fold, seed or technical replicate becomes a patient-level n.

## 4. Variables and provenance

| Variable/feature family | Role | Unit/time | Definition/source | Missingness | Learned/frozen where? |
|---|---|---|---|---|---|
| Primary outcome | outcome |  |  |  | frozen protocol |
| Index score/exposure | predictor/exposure |  |  |  |  |
| Comparator | comparator |  |  |  |  |
| Covariate | confounder / precision / nuisance / mediator / subgroup |  |  |  |  |

- Imaging acquisition/reconstruction and protocol variables:
- Annotation/reference-standard variables and uncertainty states:
- Treatment/intercurrent-event/visit variables:
- Variables unavailable at intended prediction/action time:

## 5. Preprocessing and leakage boundary

For each step specify `FIXED_PRE_SPLIT`, `FIT_IN_TRAINING_ONLY`, `APPLIED_FROZEN`, or
`EXTERNAL_ADAPTATION`:

| Step | State | Fit data/unit | Parameters/version | Application to validation/test | Failure/deviation rule |
|---|---|---|---|---|---|
| series/ROI selection |  |  |  |  |  |
| registration/resampling |  |  |  |  |  |
| intensity/feature processing |  |  |  |  |  |
| imputation/scaling/harmonisation |  |  |  |  |  |
| feature selection/dimensionality reduction |  |  |  |  |  |
| model/hyperparameter/threshold/calibration |  |  |  |  |  |

Define the exact consequence of protected-test access. Report frozen results before adaptation/updating.

## 6. Missing, indeterminate and excluded observations

- Missingness description by variable, population, site and outcome:
- Structural versus intermittent versus dropout/terminal missingness:
- Primary handling and assumptions:
- Auxiliary variables and imputation model, number of imputations and pooling rule if applicable:
- Indeterminate/non-evaluable/abstention handling in numerator and denominator:
- Exclusion rule and blinded implementation:
- Sensitivities for plausible assumption violations:

Complete-case analysis is not a default. Attrition inflation does not correct attrition bias.

## 7. Primary analysis specification

```text
analysis population -> independent unit/hierarchy -> estimand -> model/test -> link/distribution or
performance estimator -> covariates/functional forms/interactions -> effect/performance measure ->
uncertainty method -> alpha/CI -> threshold/margin -> success criterion -> allowed claim
```

- Model formula or executable pseudocode:
- Variance/cluster/bootstrap unit:
- Assumption diagnostics and decision rules:
- Model convergence/failure and fallback:
- Effect estimate, CI and absolute quantities to report:

## 8. Task-specific endpoint addendum

Complete the applicable row(s), one primary route only:

| Task | Required frozen details |
|---|---|
| Diagnostic/triage | sampling/reference standard, threshold, sensitivity/specificity/PPV/NPV, verification/indeterminate handling, paired/clustered comparison |
| Detection/localization | case versus lesion level, candidate matching, FROC operating points, false positives/exam, patient-clustered uncertainty |
| Segmentation/quantification | classes/empty cases, overlap + surface tolerance, measurement bias/repeatability, multiple lesions/readers |
| Prognosis/risk | index time/horizon, censoring/competing risks, calibration, discrimination, Brier/net benefit and external validation |
| Response/longitudinal | time zero/visits, intercurrent events, repeated covariance, landmark/joint/multi-state route and informative missingness |
| Reconstruction/enhancement | paired reference, physical/task metric, quantitative bias, margin, reader/case variance and failure cases |
| Report/VLM | clinical error taxonomy, human reference/adjudication, model/prompt snapshot, paired reader effect and critical-error denominator |

## 9. Model development and evaluation

- Candidate parameters/complexity and shrinkage/regularization:
- Resampling/tuning design, nesting and repeat policy:
- Simple, clinical and technical comparator models:
- Internal optimism correction:
- Frozen external/temporal/geographic evaluation:
- Calibration and threshold policy:
- Updating/adaptation plan and required further test:
- Site/scanner/protocol and OOD/failure analyses:

Do not treat resampling folds/seeds as independent samples or use protected-test performance for model
selection.

## 10. Multiplicity, secondary and subgroup analyses

| Family | Confirmatory/exploratory | Number/scope | Error-control method | Reporting rule |
|---|---|---|---|---|
| Primary | confirmatory |  |  |  |
| Secondary outcomes |  |  |  |  |
| Models/metrics/horizons |  |  |  |  |
| Subgroups/interactions |  |  |  |  |
| Features/omics |  |  |  |  |

- Prespecified subgroup definitions and interaction/heterogeneity test:
- Minimum information/precision below which results remain descriptive:
- Complete-result table/archive location:

Separate subgroup estimates do not prove a difference; use a prespecified contrast/interaction.

## 11. Specialized inference addenda

### Quantitative measurement

- measurand, units, repeatability/reproducibility conditions and allowable change:
- bias/limits/repeatability coefficient and heteroscedasticity handling:
- subject, reader, scanner/site and repeat variance components:

### Reader/MRMC or clinical impact

- reader/case/site/period allocation and crossing:
- endpoint, paired contrast, variance method and missing reads:
- workflow clock, contamination, secular trend and safety endpoint:

### Causal treatment/impact

- target trial/strategy, assignment, time zero, follow-up and causal contrast:
- exchangeability, positivity, consistency/interference and measurement assumptions:
- confounder/censoring/adherence/switching model and diagnostics:
- negative controls and unmeasured-confounding sensitivity:

### Longitudinal/multi-state

- observation times, state/transition definitions and interval censoring:
- time-varying covariates, joint/landmark/mixed/multi-state estimand:
- dropout/death/competing-event strategy and dynamic validation:

## 12. Sensitivity, falsification and failure analyses

| Analysis | Threat addressed | Expected diagnostic | Failure threshold | Consequence/claim ceiling |
|---|---|---|---|---|
|  |  |  |  |  |

Include, where applicable: alternative reference/outcome definitions, missing-data assumptions, site/
protocol/raw-scale analysis, segmentation/registration perturbation, threshold/margin stability,
negative controls, label/time permutation, influential observations and model/specification alternatives.

## 13. Sample size / precision / power

- Objective and primary model:
- Effect worth detecting, margin or precision target and rationale:
- Prevalence/events/transitions/variance/correlation/censoring inputs and sources:
- Reader/case/site/cluster/repeat structure:
- Model complexity/anticipated fit or calibration precision:
- Missing/non-evaluable/attrition assumptions:
- Calculation/simulation method, software/version and scenario range:
- Required versus feasible independent units:
- Unresolved inputs: [AUTHOR_INPUT_NEEDED / BIOSTATISTICIAN_REQUIRED]

## 14. Outputs and reporting

- Primary table/figure and denominator source:
- Effect/performance estimates and CIs to report regardless of significance:
- Calibration, failure/non-evaluable and subgroup displays:
- Source-result artifact and manuscript handoff fields:
- Reporting-guideline/version verification owner/date:
- Prohibited result transformations or selective displays:

## 15. Software and reproducibility

| Component | Package/software | Version/commit | Config/seed | Command/notebook | Verification/test |
|---|---|---|---|---|---|
|  |  |  |  |  |  |

- Environment/container and hardware:
- Input/output schemas and checksums:
- Randomness/repeat-run policy:
- Code/data/model availability and licenses/access boundary:
- Independent rerun/review receipt:

## 16. Amendments and deviations

| ID | Date | SAP field | Old | New | Reason | Result-aware? | Affected outputs | Disclosure |
|---|---|---|---|---|---|---|---|---|
| S-001 |  |  |  |  |  | yes / no / unknown |  |  |

Any result-aware addition is exploratory unless an independently protected confirmation exists.
