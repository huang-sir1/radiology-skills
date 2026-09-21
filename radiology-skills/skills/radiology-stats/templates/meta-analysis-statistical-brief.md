# Meta-analysis executable statistical brief

Use `AUTHOR_INPUT_NEEDED` rather than guessing. A completed brief is a specification, not evidence
that computation ran.

## 1. Scope and state

- Brief ID/version/date:
- Review/protocol/synthesis-group ID:
- Route: `meta-analysis-inference`
- Review question/Claim IDs:
- Compatibility decision supplied by review owner: `POOL / STRATIFY / NARRATIVE / STOP_FOR_REPAIR`
- Evidence/execution state: `PLAN_ONLY / DATA_READY / COMPUTED / AUTHOR_REPORTED / PARTLY_VERIFIED / NOT_ASSESSABLE / BIOSTATISTICIAN_REQUIRED`
- Supplied effect table/code/output locators:
- Execution authority/environment/output root:

## 2. Estimand and effect contract

| Field | Specification |
|---|---|
| target population of studies/settings | [AUTHOR_INPUT_NEEDED] |
| study-level quantity and independent study-family unit | [AUTHOR_INPUT_NEEDED] |
| synthesis quantity: common/average/distribution/prediction | [AUTHOR_INPUT_NEEDED] |
| endpoint/target, horizon/period and threshold | [AUTHOR_INPUT_NEEDED] |
| exact effect measure/metric definition/model/form | [AUTHOR_INPUT_NEEDED] |
| scale/transformation and direction convention | [AUTHOR_INPUT_NEEDED] |
| adjusted/unadjusted or validation class | [AUTHOR_INPUT_NEEDED] |
| supported claim and prohibited upgrade | [AUTHOR_INPUT_NEEDED] |

## 3. Effect rows and input schema

| Effect ID | Study-family ID | Source anchor | Estimate/raw data | SE/CI | Numerator/denominator/person-time/2 x 2 | Unit | Threshold/horizon/period | Adjustment/validation class | RoB/applicability | Include role |
|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  |  | primary / subgroup / sensitivity / exclude |

- Required columns and types:
- Missing/conflicting rows:
- Transformations/reconstruction rules and verification owner:

## 4. Dependence and overlap

| Source | Affected IDs | Evidence/covariance | Planned strategy | Sensitivity or stop condition |
|---|---|---|---|---|
| multiple effects/outcomes/horizons/thresholds |  |  | select / multilevel / multivariate / robust variance / other |  |
| shared comparator/multi-arm |  |  |  |  |
| readers/lesions/centres/clusters |  |  |  |  |
| overlapping cohorts/reports |  |  |  |  |

## 5. Model specification

- Model family/parameterization: generic common/random / multilevel-dependent / bivariate DTA / HSROC / prevalence-incidence / log HR-OR-RR / reliability-agreement / prediction-performance / other
- Formula/likelihood in words or code:
- Between-study variance estimator, if applicable:
- Interval/df method:
- Zero-event/sparse/separation handling:
- Weighting and covariance assumptions:
- Software/package/version to verify:
- Expected convergence/identifiability checks:

## 6. Heterogeneity and diagnostics

- Between-study variance output and uncertainty:
- I-squared or route-specific heterogeneity output and interpretation boundary:
- Prediction interval condition/output:
- Influence/outlier diagnostics:
- Clinical/methodological heterogeneity fields to return to review owner:
- Few-study/weak-information limitation:

## 7. Sensitivity, subgroup and reporting-bias plan

| Analysis ID | Prespecified question | Effect IDs/assumption changed | Method | Decision consequence | Multiplicity/claim state |
|---|---|---|---|---|---|
|  |  |  |  |  | primary / sensitivity / exploratory |

- Funnel/asymmetry/selection analysis conditions:
- Registry/selective-reporting evidence required:
- Forbidden interpretation of publication-bias output:

## 8. Execution and artifact contract

- Exact command/entry point:
- Working directory/environment/seed policy:
- Output table schema:
- Required figures/data handoff:
- Log/convergence/warning artifacts:
- Success assertions:
- Failure assertions and fallback:
- Run status/output locators, if executed:

## 9. Stop gate

| Decision | Verdict `PASS/CONDITIONAL/BIOSTATISTICIAN_REQUIRED` | Evidence | Exact blocker/assumption | Minimum evidence or specialist decision | Allowed fallback | Surviving claim |
|---|---|---|---|---|---|---|
| estimand/effect compatibility |  |  |  |  |  |  |
| independent study family/dependence |  |  |  |  |  |  |
| data/uncertainty/metric definition |  |  |  |  |  |  |
| model identifiability/convergence |  |  |  |  |  |  |
| high-stakes/specialist sign-off |  |  |  |  |  |  |

## 10. Writing/table handoff

- Methods specification:
- Results fields with evidence state:
- Table/forest/HSROC/calibration display keys:
- Sensitivity and heterogeneity wording:
- Discussion/Abstract/title ceiling:
- `AUTHOR_INPUT_NEEDED`:
