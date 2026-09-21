# Causal and clinical-impact inference

Use this reference when the claim says an imaging test, AI system, workflow or treatment strategy
**changes** decisions, time, resource use, harms or patient outcomes. Prediction, association, external
accuracy and decision-curve net benefit do not themselves identify a causal impact.

## 1. Write the target trial or intervention contrast

Before selecting a method, specify:

| Component | Required specification |
|---|---|
| Eligible population | observable criteria at a common decision time |
| Strategies | deploy/use versus comparator; thresholds, fallback, adherence and allowed cointerventions |
| Assignment | randomization or observational assignment mechanism |
| Time zero | eligibility, strategy assignment and follow-up start aligned |
| Follow-up | horizon, censoring, switching and contamination |
| Outcome | patient, workflow, safety or resource endpoint and ascertainment |
| Causal estimand | ITT/policy, per-protocol/adherence, ATE/ATT, risk/mean/time contrast or effect modification |
| Analysis | estimator, adjustment, uncertainty, clustering and sensitivity |

For imaging biomarkers, distinguish treatment-contextual prognosis from a comparison of treatment
strategies. Effect modification additionally requires a biomarker-by-treatment contrast on a defined
scale.

## 2. Identification assumptions

State and defend:

- **consistency/well-defined strategies:** what “AI used” or “standard care” actually means;
- **exchangeability:** measured variables sufficient for the intended observational contrast;
- **positivity/overlap:** each relevant patient/site/time can receive each strategy;
- **no relevant interference:** one patient's assignment or a shared worklist/model does not alter
  another's outcome, or interference is modeled at cluster level;
- **measurement and missingness:** assignment, confounders, outcome and censoring measured comparably;
- **time alignment:** no immortal-time or future-information eligibility/assignment.

Use a causal diagram plus domain knowledge to classify confounders, precision variables, mediators and
colliders. Do not select adjustment variables by univariable p value or model feature importance.

If a key confounder is unmeasured, condition is perfectly confounded with site/time, or overlap is
absent, no adjustment algorithm repairs identification; narrow the estimand or return `STOP`.

## 3. Choose a design before an estimator

| Design | Best use | Critical requirements |
|---|---|---|
| Individual randomized trial | participant-level diagnostic/decision intervention | allocation concealment, adherence/contamination, outcome blinding and ITT estimand |
| Cluster/pragmatic trial | worklist/site/team intervention where spillover is expected | enough clusters, cluster-level allocation/time, ICC and implementation fidelity |
| Stepped wedge | staged rollout when justified | secular-time model, transition/learning period, cluster dependence; rollout convenience is not justification |
| Interrupted time series | system-wide intervention at a known time | sufficient pre/post observations, level/slope estimand, autocorrelation/seasonality and concurrent-change audit |
| Difference-in-differences | exposed versus comparison trend | defensible parallel-trends/carryover assumptions and no differential concurrent shock |
| Regression discontinuity | treatment assigned by threshold | no manipulation, local continuity and bandwidth/sensitivity plan |
| Observational target-trial emulation | treatment/workflow variation with rich confounding data | explicit time zero/strategies, overlap, exchangeability and censoring/adherence plan |

A before–after comparison without a counterfactual mainly estimates change over time, not intervention
effect.

## 4. Estimator contract

Potential estimators include standardized outcome regression, propensity-score weighting/matching,
g-computation, augmented/doubly robust estimators and, for time-varying treatment/confounding,
marginal structural or longitudinal g-methods. Choose from the estimand/design and record:

- nuisance-model variables, forms/interactions and fitting partition;
- target population and weight/match definition;
- overlap/balance diagnostics before outcome interpretation;
- extreme-weight/trimming policy and the estimand it changes;
- cluster/site/time correlation and finite-cluster uncertainty;
- censoring/adherence/switching model;
- robust/bootstrapped variance at the independent assignment unit.

Propensity-score matching does not control unmeasured confounding; good balance on recorded variables is
necessary, not proof of exchangeability. “Doubly robust” does not rescue violations of positivity,
consistency or both nuisance models being seriously misspecified.

## 5. Imaging-AI impact endpoints

Predefine a small hierarchy:

- decision accuracy or error type at a clinically fixed action/threshold;
- time to review/action, including queue start/stop, off-hours and censored/failed cases;
- downstream tests, referrals, treatment or resource use;
- safety: missed/delayed critical findings, automation-related errors and overrides;
- patient outcomes and patient-reported/access/equity outcomes when the design supports them;
- implementation fidelity, availability and clinician uptake as process variables, not substitutes for
  patient benefit.

Algorithm performance is a mediator/process measure in an impact study. Report implementation fidelity
and failures, but do not equate them with the causal clinical endpoint.

## 6. Effect modification and fairness

- Prespecify subgroup/marker, scale and treatment-by-marker interaction or stratum-specific absolute
  causal effects.
- Ensure overlap within subgroup and control multiplicity; independent confirmation is usually needed.
- A significant effect in one subgroup and nonsignificant effect in another is not interaction.
- Fairness gaps may arise from access, workflow, missingness and treatment differences; model-performance
  parity alone does not establish equal benefit.

## 7. Falsification and sensitivity

Predefine negative-control outcomes/exposures where credible, placebo intervention dates, pre-trend
checks, alternative time windows/specifications, unmeasured-confounding sensitivity, weight/overlap
scenarios, cluster/site leave-out and missing/censoring assumptions. Report the frozen primary result
before robustness-selected alternatives.

## 8. Sample size and stop gates

Power/precision uses the independent assignment unit, effect worth detecting, baseline rate/variance,
cluster ICC/autocorrelation, number/size of clusters or periods, adherence/contamination, overlap,
censoring and multiplicity. Patient count cannot compensate for too few randomized sites or time points.

Return `BIOSTATISTICIAN_REQUIRED` for cluster/stepped-wedge/ITS/DiD, time-varying confounding, complex
interference or unsupported causal sample-size inputs. Return `STOP_FOR_REPAIR` for misaligned time zero,
post-treatment confounder adjustment without a longitudinal method, absent overlap, result-selected
intervention date/model, or causal wording from a prediction/association-only design.

## 9. Reporting contract

Return:

`target-trial/intervention protocol -> DAG/assumption register -> design/counterfactual -> analysis
population/estimand -> estimator/nuisance plan -> balance/overlap/fidelity diagnostics -> effect and CI
-> safety/process outcomes -> falsification/sensitivity -> transport/claim ceiling -> deviations`.

## Primary and official sources

- Hernán MA, Robins JM. [Causal Inference: What If](https://www.hsph.harvard.edu/miguel-hernan/causal-inference-book/).
- Hernán MA, Robins JM. [Using big data to emulate a target trial](https://doi.org/10.1093/aje/kwv254).
- Bernal JL, et al. [Interrupted time-series tutorial](https://doi.org/10.1093/ije/dyw098).
- ICH. [E9(R1) Estimands and Sensitivity Analysis](https://database.ich.org/sites/default/files/E9-R1_Step4_Guideline_2019_1203.pdf).
- SPIRIT–CONSORT Group. [Published 2025 statements](https://www.consort-spirit.org/published-statements).
- Vasey B, et al. [DECIDE-AI](https://doi.org/10.1038/s41591-022-01772-9).

Apply CONSORT/SPIRIT/DECIDE-AI only to the relevant design and verify current reporting/regulatory
requirements live.
