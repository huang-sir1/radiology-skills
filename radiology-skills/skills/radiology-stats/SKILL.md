---
name: radiology-stats
description: "Plan/compute/audit inference on defined data/effect rows: CI, AUC, MRMC, survival, meta-analysis and power. CN: 统计、样本量、AUC比较、校准"
---

# Imaging Biostatistics for _Radiology_

Use this skill to choose the right test, run it correctly, and **report it the way
_Radiology_ wants** — estimates with 95% CIs, exact p-values, named tests, and multiplicity
handled. It covers the statistics that imaging-AI, radiomics, and reader studies live or die
on.

## Core stance

- **Estimate + uncertainty, not just p.** Every primary result gets a 95% CI. Report exact
  p-values (e.g. `P = .03`, not `P < .05`); use `P < .001` only below that floor.
- **The test must match the design.** Paired data → paired test (same patients/cases read by
  both methods); clustered data (multiple lesions per patient) → account for clustering;
  multiple readers → MRMC, not a naive average.
- **Match performance measures to use.** A probabilistic diagnostic/prognostic model generally
  needs discrimination and calibration. Evaluate decision-analytic utility only when an intended
  decision, threshold range, consequences and comparator strategies are defined; do not require a
  decision curve for every exploratory classifier.
- **Control multiplicity honestly.** Thousands of radiomic/omic features ⇒ FDR or stronger;
  pre-specify primary vs exploratory.
- **No fishing, no fabrication.** Pre-specify the primary analysis; never invent a number,
  a CI, or a p-value. If data are insufficient, say what is needed.
- **Reproducible.** Always return an executable statistical brief. Return runnable code and computed
  results only when the required data/schema, estimand, hierarchy, environment and execution authority
  are available; record software/version and the exact uncertainty method.
- **Evidence state is explicit.** Use `PLAN_ONLY`, `DATA_READY`, `COMPUTED`, `AUTHOR_REPORTED`,
  `PARTLY_VERIFIED`, `NOT_ASSESSABLE`, or `BIOSTATISTICIAN_REQUIRED`. A proposed model is not a run.
- **No universal sample-size threshold.** Power and precision depend on the estimand, endpoint
  distribution, effect worth detecting, allocation unit, clustering/repeated structure, multiplicity,
  attrition and acceptable uncertainty. Do not substitute an EPV, event-count or replicate rule of
  thumb for those inputs.

## Choose the route

| Route | Use when | Required contract |
|---|---|---|
| `single-study-inference` | estimating or comparing outcomes within one imaging/omics cohort or reader study | endpoint, estimand, true unit, pairing/clustering, missingness, model/test, uncertainty and multiplicity |
| `meta-analysis-inference` | compatible study/effect rows need a synthesis model, audit or result interpretation | study-family/effect IDs, effect scale/direction, unit and dependence, model family, heterogeneity, sensitivity and small-study boundary |
| `experimental-inference-power` | a tissue, cell, organoid or animal experiment needs inferential design, model or power/precision planning | assigned unit, endpoint distribution, estimand, cluster/repeat hierarchy, effect worth detecting, nuisance inputs, attrition and feasible design |
| `quantitative-measurement` | repeatability, reproducibility, bias, change detection or scanner/site comparability of a quantitative image measure | measurand, repeat/reproduce conditions, bias reference, variance components, wCV/repeatability coefficient/LoA or smallest detectable change and claim boundary |
| `causal-clinical-impact` | estimating workflow/intervention effects from randomized, pragmatic or observational deployment data | target trial/contrast, assignment/exposure time, confounding, interference, missingness and sensitivity plan |
| `longitudinal-multistate` | repeated imaging, landmark/dynamic prediction, interval-censored transitions or competing events | time zero, visit process, time-varying exposure/measurement, state definition, estimand and dependence model |

Declare one mode:

| Mode | Output boundary |
|---|---|
| `plan` | executable brief and missing-input ledger; no computed result |
| `audit` | artifact-anchored design/model/inference findings, repairs and stop gate |
| `compute` | authorized code/run record and verified outputs from sufficient inputs |
| `interpret` | effect/uncertainty/heterogeneity/power meaning and bounded claim from real outputs |
| `mentor` | minimum defensible, standard publishable and stronger route with why, prerequisites, resource cost, failure signal, fallback, closure evidence and surviving claim |
| `writing-handoff` | fixed Methods/Results/table/figure/statistical-reporting fields without evidence upgrade |

If the request crosses routes, keep separate estimands and briefs. Open only the active specialized
reference: [meta-analysis](references/meta-analysis-inference.md),
[experimental inference/power](references/experimental-inference-and-power.md),
[quantitative measurement](references/quantitative-imaging-measurement-science.md),
[causal clinical impact](references/causal-and-clinical-impact-inference.md), or
[longitudinal/multistate imaging](references/longitudinal-and-multistate-imaging.md). Persist the
meta-analysis or experimental specification with the
[meta-analysis brief](templates/meta-analysis-statistical-brief.md) or
[experimental inference/power brief](templates/experimental-inference-power-brief.md).

## When to use

- Diagnostic accuracy: sensitivity/specificity/PPV/NPV/accuracy/likelihood ratios + CIs.
- Comparing models/readers/tests: **DeLong** or bootstrap for AUCs; McNemar for paired
  sensitivity/specificity.
- Reader studies: **kappa / weighted kappa / Fleiss / ICC / Bland-Altman**; **MRMC** analysis and
  sample sizing (clinical reader-study design stays with `radiology-translation`).
- Prediction models: ROC, **calibration** (slope/intercept, Brier), **decision-curve
  analysis**, threshold selection.
- Radiomics/omics: feature reproducibility (ICC), **multiple-testing** correction,
  cross-validation/nested CV, bootstrap optimism.
- Statistical inference for already-defined configuration, method, ablation or sensitivity
  comparisons: paired deltas, cluster bootstrap, run variability and multiplicity. The scientific
  comparison design itself remains with `radiology-method-evaluation`.
- Survival/prognosis: Kaplan-Meier + log-rank, **Cox**, **C-index**, time-dependent ROC,
  competing risks.
- Quantitative imaging measurement: bias, repeatability/reproducibility, wCV, repeatability
  coefficient, limits of agreement, smallest detectable change and scanner/site variance.
- Causal/clinical impact: randomized/pragmatic, cluster/stepped-wedge, ITS/DiD or target-trial
  analyses with explicit identification assumptions and interference/time-varying confounding.
- Longitudinal imaging: mixed/joint/landmark/multistate models, interval censoring, informative
  visit/dropout processes and competing events.
- Planning: **sample size/power/precision** for accuracy, AUC, prediction models and experiments,
  using input-driven methods rather than universal EPV, event-count or replicate cutoffs.
- 中文高频说法：“样本量/统计功效怎么算？”“两个 AUC 怎么比较（DeLong 还是 bootstrap）？”
  “校准曲线/决策曲线怎么做？”“多阅片者一致性（kappa/ICC/MRMC）怎么报？”“meta 分析怎么合并？”

## When to open extra files

| File | Open when |
|---|---|
| [references/diagnostic-accuracy.md](references/diagnostic-accuracy.md) | Sensitivity/specificity/PPV/NPV/LR, the right CI method, paired comparison (McNemar) |
| [references/model-evaluation.md](references/model-evaluation.md) | ROC/AUC, DeLong vs bootstrap, thresholds, calibration, Brier, decision-curve analysis |
| [references/incremental-value.md](references/incremental-value.md) | Added information versus validated predictive gain: distinguish development LRT, independent binary ROC and censored survival comparison; condition DCA and optional NRI/IDI on their decision and inference assumptions |
| [references/agreement-mrmc.md](references/agreement-mrmc.md) | Cohen/weighted/Fleiss kappa, ICC model choice, Bland-Altman, MRMC (Obuchowski-Rockette / DBM) |
| [references/high-dimensional-omics.md](references/high-dimensional-omics.md) | Multiple testing (Bonferroni/Holm/BH-FDR/q-values), CV/nested CV, leakage, optimism, harmonisation stats |
| [references/survival-prognostic.md](references/survival-prognostic.md) | Kaplan-Meier, Cox PH (+ assumptions), C-index, time-dependent AUC, competing risks |
| [references/sample-size.md](references/sample-size.md) | Input-driven sample-size/power/precision for sensitivity/specificity, AUC, prediction validation, MRMC and clustered designs without universal cutoffs |
| [references/analysis-hierarchy-and-missingness.md](references/analysis-hierarchy-and-missingness.md) | Multiple lesions/slices/timepoints/readers, nested or repeated data, biological vs technical replication, missing data, exclusions, and analysis-plan deviations |
| [references/method-comparison-and-sensitivity.md](references/method-comparison-and-sensitivity.md) | Real benchmark, ablation or parameter-sensitivity outputs need paired deltas, patient/donor-level uncertainty, run variability and multiplicity without treating folds/seeds as subjects |
| [references/meta-analysis-inference.md](references/meta-analysis-inference.md) | Generic/dependent random-effects synthesis, bivariate/HSROC DTA, prevalence/incidence, HR/OR/RR, ICC/kappa/agreement, prediction performance/calibration, heterogeneity, few-study and reporting-bias boundaries |
| [references/experimental-inference-and-power.md](references/experimental-inference-and-power.md) | Continuous/binary/count experimental endpoints, donor/litter/cage/cluster assignment, repeated measures/mixed models, attrition and input-driven power/precision planning |
| [references/quantitative-imaging-measurement-science.md](references/quantitative-imaging-measurement-science.md) | Bias, repeatability/reproducibility conditions, variance components, wCV, repeatability coefficient, Bland–Altman limits, smallest detectable change and cross-site quantitative claims |
| [references/causal-and-clinical-impact-inference.md](references/causal-and-clinical-impact-inference.md) | Target-trial framing, randomized/pragmatic/cluster/stepped-wedge/ITS/DiD routes, confounding, interference and causal claim ceilings |
| [references/longitudinal-and-multistate-imaging.md](references/longitudinal-and-multistate-imaging.md) | Repeated imaging, time-varying/landmark/joint/multistate models, interval censoring, visit-process bias and competing events |

## Workflow

1. **Declare route, evidence and execution state.** Inventory the supplied protocol, effect rows,
   raw/summary data, code/output and authority. Never turn a brief or author-reported result into
   `COMPUTED`.
2. **Restate the design and hierarchy** — independent experimental unit, patient/lesion/slice/
   timepoint nesting, paired vs unpaired, repeated measures, readers, prevalence, primary vs
   secondary endpoints. Open `analysis-hierarchy-and-missingness.md` when clustering or missingness
   exists; do not count images/cells/model runs as independent patients.
3. **Pick the estimand and model/test** using the route reference. Name the population quantity,
   contrast, endpoint, time/measurement period and intercurrent/missing-data handling explicitly.
4. **Choose the uncertainty method** (e.g. Wilson/Clopper-Pearson for single-study proportions; DeLong or
   bootstrap for AUC; bootstrap for derived metrics).
5. **Handle dependence, missingness, exclusions, attrition and deviations** before looking at significance;
   define the analysis population and sensitivity analyses.
6. **Handle multiplicity** — declare the primary analysis; correct the rest (method + family).
7. **Run the stop gate.** If an estimand, independent/allocation unit, dependence structure, effect
   definition or required power input cannot be made defensible, return `BIOSTATISTICIAN_REQUIRED`
   with the exact blocking decision and do not present a final model or sample size.
8. **Specify, then run only when ready.** Complete the route template. Provide code/configuration and
   compute estimate + interval (+ p where applicable) only from sufficient verified inputs.
9. **Write the result** — a _Radiology_-style sentence (estimate, CI, p, n) plus a Methods
   sentence (test, software/version, CI method, multiplicity).
10. **Sanity-check** — does the interval width align with information size? is the model paired,
   cluster/dependence-aware if needed? is
   calibration reported for a clinical model? are subgroups pre-specified?
   Subgroup discipline:
   - A subgroup claim needs an **interaction test** (treatment × subgroup P) — "significant in
     one subgroup, not the other" is not evidence that the effect differs.
   - Multiplicity compounds: #subgroups × #outcomes is the family-wise risk. Pre-specify a
     small number of subgroups; label everything else exploratory.
   - Show subgroup results as a **forest plot including the interaction P** → hand off to
     `radiology-figure`.
   - For prediction models, prespecify clinically material subgroup/fairness evaluations when the
     intended population, plausible harms and available sample sizes make them relevant. Report
     what was and was not assessable; do not manufacture underpowered subgroup claims merely to
     populate a checklist.
11. **In mentor mode**, do not prescribe a larger model or sample by fashion. Separate:
    - minimum defensible: the narrowest estimand/model/precision that current inputs can support;
    - standard publishable: the comparator, dependence handling, diagnostics and sensitivity needed
      for the intended claim;
    - stronger/discriminating: additional design or information that resolves the named ambiguity.
    For each, state why, prerequisites, resource/time burden, expected failure signal, fallback,
    closure evidence and allowed wording. If key nuisance or allocation inputs remain unknown, the
    learner route still ends at `BIOSTATISTICIAN_REQUIRED`, not a guessed sample size.

## Reporting templates (fill from real output — never fabricate)

- Accuracy: *"Sensitivity was 0.87 (95% CI: 0.81, 0.92; 130/149) and specificity 0.79 (95%
  CI: 0.73, 0.84; 158/200)."*
- Independent binary-model AUC comparison: *"On the same independent cases, the frozen model's AUC
  (0.88; 95% CI: 0.84, 0.92) exceeded the frozen comparator model's (0.81; 95% CI: 0.76, 0.86;
  difference 0.07; P = .004, paired DeLong)."* Reader-population contrasts require the applicable
  MRMC analysis rather than this two-model template.
- Agreement: *"Inter-reader agreement was substantial (ICC, 0.82; 95% CI: 0.75, 0.87;
  two-way random-effects, absolute agreement, single rater)."*
- Multiplicity: *"Of [N] features, [K] differed after Benjamini-Hochberg control at FDR <
  0.05."*

## Output contract

1. **`Route and evidence state`** — route, scope, supplied artifacts, execution authority and one of
   the declared states.
2. **`Design/estimand read`** — population quantity, contrast, endpoint/period, independent or
   allocation unit, pairing/readers/clusters and claim boundary.
3. **`Hierarchy/missingness read`** — nested/repeated/dependent structure, analysis
   population, exclusions, missing-data mechanism/handling, and sensitivity analyses.
4. **`Executable statistical brief`** — input schema/effect rows, model/test, dependence strategy,
   uncertainty, heterogeneity or power inputs, multiplicity, diagnostics, sensitivity and success/
   failure assertions. Use the active route template.
5. **`Code/run record`** — when authorized and ready, runnable Python/R plus versions, command,
   logs and output locators; otherwise `NOT_RUN` with blockers.
6. **`Results sentence`** — _Radiology_-style, with placeholders only where the user must
   supply data.
7. **`Methods sentence`** — for the statistical-analysis paragraph.
8. **`Table handoff`** — canonical estimates/value keys and the table shell needed by
   `radiology-table` when a publication table is requested.
9. **`Stop gate and caveats`** — `PASS`, `CONDITIONAL`, or `BIOSTATISTICIAN_REQUIRED`, exact
   assumptions/blocker, minimum missing input, sensitivity boundary and reviewer risk.
10. **`Learner route receipt`** — in `mentor`: minimum defensible / standard publishable /
    stronger-discriminating options, prerequisites, cost, failure signal, fallback, closure evidence
    and the claim that survives if the stronger route is infeasible.

## Integrity & handoffs

- Never invent numbers, CIs, or p-values; compute from supplied data or mark as needed.
- Never invent covariance, person-time, within-study pairing, cluster ICC, repeated-measure
  correlation, baseline event rate, variance, effect worth detecting, attrition or power inputs.
- `BIOSTATISTICIAN_REQUIRED` stops a final model/sample-size recommendation; it does not authorize
  guessing or relabel an unresolved plan as completed analysis.
- Reporting-guideline alignment of the statistics → `radiology-reporting`.
- Plotting the result (ROC, calibration, DCA, forest, KM) → `radiology-figure`.
- Publication tables (Table 1, Cox/logistic, model performance, MRMC) → `radiology-table`.
- High-dimensional study design (leakage, batch effects in radiogenomics) →
  `radiology-radiogenomics`.
- Decide which parameters/methods/comparators need evaluation and whether the evidence supports the
  methodological claim → `radiology-method-evaluation`; return here only for statistical inference.
- Sample-size numbers feeding a grant's feasibility section → `radiology-grant`.
- Analysis plan is locked and results are in; want a harsh pre-submission read → `radiology-prereview`.
- Project value registry, analysis lock, and cross-artifact state → `radiology-pipeline`.
- This skill is statistical guidance, not a substitute for a qualified biostatistician on
  high-stakes or regulatory work.
