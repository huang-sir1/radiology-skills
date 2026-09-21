# Meta-analysis statistical inference contract

Use this reference after a review has defined compatible synthesis groups and supplied traceable
study-family/effect rows. It owns statistical specification, computation when inputs are sufficient,
diagnostics and bounded interpretation. It does not repair eligibility, invent covariance, decide
which studies are clinically compatible, or certify a search as complete.

## 1. Intake and evidence state

Record the source artifact and one state: `PLAN_ONLY`, `DATA_READY`, `COMPUTED`,
`AUTHOR_REPORTED`, `PARTLY_VERIFIED`, `NOT_ASSESSABLE`, or `BIOSTATISTICIAN_REQUIRED`.

Minimum intake per candidate synthesis group:

- review/protocol ID, route, estimand and compatibility decision;
- `Study-family ID`, `Effect ID`, report/source locator and overlap resolution;
- population, design, endpoint/target, horizon or measurement period;
- exact effect definition, scale/transformation, direction convention and adjustment class;
- estimate plus standard error/CI or reconstructable raw numerator/denominator/person-time/2 x 2;
- independent unit, clusters/nesting, repeated effects, thresholds, readers/devices and shared
  comparators;
- within-study covariance/correlation when available, or evidence that effects are independent;
- risk-of-bias/applicability state and primary/sensitivity role;
- prespecified subgroup/meta-regression hypotheses, multiplicity family and software environment.

Unknown dependence is not zero dependence. Mark the field `AUTHOR_INPUT_NEEDED` and preserve the
claim boundary.

## 2. Freeze the statistical estimand

Write:

`target population of studies -> study-level quantity -> effect scale -> synthesis quantity ->
heterogeneity interpretation -> claim ceiling`.

Keep distinct:

- conditional common-effect inference versus a distribution of effects;
- average effect versus prediction for a new setting;
- adjusted versus unadjusted effects;
- development, internal validation and external validation performance;
- patient versus lesion/reader/cell/spot effects;
- different thresholds, horizons, measurement periods or intervention contrasts.

A random-effects label does not make incompatible estimands commensurate.

## 3. Dependence strategy

Choose and justify one strategy before fitting:

| Dependence source | Candidate strategy | Required evidence |
|---|---|---|
| one eligible effect per independent study family | univariate fixed/common or random-effects model as justified | effect/SE and verified study-family uniqueness |
| multiple outcomes, horizons, thresholds, subgroups or models per study | prespecified effect selection, multilevel/multivariate meta-analysis, or robust-variance approach | nesting labels, covariance or sensitivity range, adequate model identifiability |
| shared comparator or multi-arm study | multivariate/shared-control covariance model or an explicit non-duplicating contrast strategy | arm sizes and shared-control structure |
| multiple readers/lesions/centres within study | study-level cluster-aware estimate or hierarchical model preserving reader/case/centre levels | lower-level hierarchy and valid within-study uncertainty |
| overlapping cohorts/reports | one study-family representation or modelled overlap | overlap map and primary-report/effect rule |

Do not split a shared comparator, duplicate a cohort, or treat thresholds/readers as new studies to
increase precision. If dependence is decision-bearing but unrecoverable, stop with
`BIOSTATISTICIAN_REQUIRED` or use a protocol-authorized single-effect/narrative route.

## 4. Model-family routes

### 4.1 Generic effects and random-effects synthesis

For mean differences, standardized effects, correlations or other compatible continuous effects,
declare:

- effect construction and direction;
- sampling-variance formula;
- fixed/common versus random-effects estimand;
- between-study variance estimator and interval method;
- dependence strategy;
- influence/outlier diagnostics and prespecified sensitivity alternatives.

Random effects require an interpretable distribution of effects. Record the estimate and interval,
between-study variance, and a prediction interval only when its assumptions and information support
one. Do not use a random-effects model as permission to pool different questions.

### 4.2 Diagnostic accuracy: bivariate or HSROC

Use paired sensitivity/specificity evidence from compatible 2 x 2 data or equivalent likelihood
inputs. Preserve threshold, disease spectrum, reference standard, uninterpretable tests, patient/
lesion unit and study flow.

- Use a bivariate model when joint average sensitivity/specificity and their correlation are the
  target under represented thresholds.
- Use an HSROC parameterization when threshold/accuracy structure or an SROC summary is the target.
- Model sensitivity and specificity jointly; do not run unrelated univariate pools when their
  threshold relationship is decision-bearing.
- Comparative test accuracy needs within-study test pairing and design indicators; indirect
  between-study comparison is not a paired test.
- Sparse cells, perfect classification, few studies or complex random effects may prevent stable
  fitting. Preserve failures and route to the stop gate rather than silently changing models.

### 4.3 Prevalence and incidence

Keep point/period/lifetime prevalence, cumulative incidence and incidence rates separate.

- Prevalence/cumulative risk requires numerator, eligible/analyzed denominator, sampling frame,
  state/event definition and period.
- Incidence rate requires events, person-time/exposure, recurrent-event policy and time scale.
- Choose a binomial/count likelihood, generalized linear mixed model, or justified transformation
  from the data and estimand. Record zero-event handling and back-transformation.
- Run sensitivity to defensible likelihood/transformation choices when they materially change the
  conclusion; do not choose the one that gives the narrowest interval.
- A pooled proportion from selected studies is not population incidence or individual risk.

### 4.4 HR, OR, RR and other association/effect measures

- Harmonize direction and analyse ratio measures on the log scale with valid uncertainty.
- Do not treat HR, OR, RR, incidence-rate ratio or standardized mean difference as interchangeable.
- Preserve exposure/intervention contrast, endpoint definition, horizon, censoring/competing-risk
  estimand and adjusted class.
- Do not pool adjusted and unadjusted estimates unless the protocol defines separate branches.
- A pooled observational association remains association; it is not a treatment effect or mechanism.

### 4.5 ICC, kappa, reliability, agreement and method comparison

The exact construct comes before the number:

- ICC requires model, type, form/unit and measurement design;
- kappa requires categories, weighting and marginal/prevalence context;
- overlap metrics require the exact variant, object and aggregation unit;
- repeatability/reproducibility requires measurement conditions and variance definition;
- Bland-Altman evidence requires bias, limits-of-agreement construction, range/proportional-bias
  assessment and subject/repeat structure.

Correlation is not agreement. Pool only compatible definitions and apply a justified
transformation/variance model. Do not average limits of agreement, ICC variants, weighted and
unweighted kappa or Dice variants as if they were one metric. If uncertainty is absent or the metric
definition cannot be reconstructed, return `STOP_FOR_REPAIR` or `BIOSTATISTICIAN_REQUIRED`.

### 4.6 Prediction performance and calibration

Keep model identity/version, endpoint/horizon, population and validation type fixed.

- Discrimination: specify c-statistic/AUC definition, uncertainty and transformation candidate.
- Calibration: prefer compatible calibration slope, calibration-in-the-large/intercept and
  observed-to-expected information with uncertainty; do not infer calibration from AUC.
- Overall accuracy: define Brier or other score and its outcome/prevalence context.
- Clinical utility: net benefit depends on threshold and setting; do not pool decision curves into a
  single number without a justified common threshold/strategy estimand.
- Development/apparent, internal-validation and external-validation estimates remain separate.
  Different model versions are not repeated validations of one frozen model.

When multiple performance measures or validations arise from one study, preserve their dependence.

## 5. Heterogeneity, few-study and subgroup discipline

Report heterogeneity as information, not a pass/fail ritual:

- between-study variance on the model scale and its uncertainty when available;
- I-squared only with its scale and imprecision understood;
- prediction interval only when the effect distribution and information make it interpretable;
- forest/influence diagnostics, clinical sources and risk-of-bias patterns;
- subgroup/meta-regression contrasts as interaction questions, not separate significance tests.

There is no universal study-count threshold that makes heterogeneity, meta-regression or small-study
tests valid. Judge identifiability, degrees of freedom, event/cell information, estimator behaviour
and interval stability for the proposed model. With weak information, simplify the prespecified model,
report broad uncertainty, use structured narrative synthesis, or return `BIOSTATISTICIAN_REQUIRED`.

## 6. Sensitivity and reporting-bias boundary

Prespecify decision-bearing sensitivity analyses from applicable rows:

- risk-of-bias/applicability restrictions;
- overlapping-study resolution and alternative eligible effect choice;
- fixed/common versus random-effects target, heterogeneity estimator or interval method;
- dependence/covariance assumptions and multilevel/robust alternatives;
- adjusted versus unadjusted branch, threshold/horizon/period and metric transformation;
- zero-event/sparse-data handling;
- external-validation-only or frozen-model-only performance;
- influential study and leave-one-study-family diagnostics.

Funnel plots, asymmetry tests and selection models address different assumptions. They may be
uninformative with limited studies, dependence, severe heterogeneity or outcome/threshold selection.
Asymmetry is not proof of publication bias; symmetry is not proof of its absence. Integrate registries,
protocols, selective outcome/model reporting and unavailable uncertainty into the interpretation.

## 7. Executable brief and stop gate

Complete `templates/meta-analysis-statistical-brief.md`. It must name the input columns/effect IDs,
effect construction, model and parameterization, dependence, uncertainty, heterogeneity, diagnostics,
sensitivity, software/version to verify, expected outputs and failure assertions.

Return `BIOSTATISTICIAN_REQUIRED` and stop a final model/result when any of these is decision-bearing:

- the estimand/effect direction or independent study-family unit is unresolved;
- incompatible effect measures, horizons, thresholds, validation types or adjustment classes remain
  in one requested pool;
- dependent effects/shared comparators/overlap cannot be represented or safely selected;
- required 2 x 2, numerator/denominator/person-time, estimate uncertainty or metric definition is
  missing and cannot be reconstructed;
- sparse/separated data, singularity/non-convergence or model complexity prevents stable estimation;
- a bespoke multivariate, adaptive, regulatory or confirmatory analysis needs accountable specialist
  sign-off.

The gate records the exact blocker, minimum evidence needed, allowed fallback and surviving claim. It
does not label the whole review invalid and never fabricates a replacement analysis.

## 8. Writing handoff

Methods receive the estimand, effect construction, model/parameterization, dependence, heterogeneity,
uncertainty, multiplicity, software/version and deviations. Results receive only computed or
inspectably author-reported estimates with state labels, intervals, heterogeneity and sensitivity.
Discussion receives transportability, residual heterogeneity, few-study and reporting-bias limits.
Abstract/title cannot exceed the weakest compatibility, dependence and evidence-state link.
