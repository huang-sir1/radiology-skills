# Experimental inference and power executable brief

Use `AUTHOR_INPUT_NEEDED` for unknown values. Do not insert a universal replicate, event, donor,
animal, litter, cage, cluster or power threshold.

## 1. Scope and state

- Brief ID/version/date:
- Experiment/protocol/Claim IDs:
- Route: `experimental-inference-power`
- System/intervention/comparator:
- Evidence/execution state: `PLAN_ONLY / DATA_READY / COMPUTED / AUTHOR_REPORTED / PARTLY_VERIFIED / NOT_ASSESSABLE / BIOSTATISTICIAN_REQUIRED`
- Supplied design/data/code/output locators:
- Local feasibility/ethics owner and constraints:

## 2. Estimand

| Field | Specification |
|---|---|
| target population/system | [AUTHOR_INPUT_NEEDED] |
| intervention strategy and comparator | [AUTHOR_INPUT_NEEDED] |
| endpoint family and measurement time | continuous / binary / count-rate / other |
| primary analysis population | [AUTHOR_INPUT_NEEDED] |
| summary contrast/effect scale | [AUTHOR_INPUT_NEEDED] |
| attrition/intercurrent/missing-data handling | [AUTHOR_INPUT_NEEDED] |
| effect worth detecting or precision target and rationale | [AUTHOR_INPUT_NEEDED] |
| supported claim and prohibited upgrade | [AUTHOR_INPUT_NEEDED] |

## 3. Assignment, unit and hierarchy

| Level | Identifier/count | Role | Assigned independently? | Nesting/crossing/repeats | Analysis handling |
|---|---|---|---|---|---|
| donor |  | sampled unit / cluster / other |  |  |  |
| litter |  | allocation/cluster/block/other |  |  |  |
| cage |  | allocation/cluster/block/other |  |  |  |
| animal/model/organoid line/culture |  |  |  |  |  |
| well/section/field/cell/time point |  | technical/subsample/repeat | no unless justified |  | aggregate/model |

- Allocation ratio/randomization/blocking/factorial structure:
- Pairing/crossover/repeated-measure structure:
- Batch/plate/time confounding check:

## 4. Analysis-model specification

- Endpoint/model family: linear / logistic-binomial / Poisson-negative-binomial / mixed / GEE / other
- Model formula in words or code:
- Fixed effects/interactions/contrasts:
- Random effects/correlation/covariance:
- Exposure offset or baseline adjustment:
- Aggregation from technical/subsample observations:
- Estimation/interval/df method:
- Multiplicity family and adjustment:
- Missingness/attrition model or sensitivity:
- Assumptions/diagnostics/convergence checks:
- Software/package/version to verify:

## 5. Power/precision input ledger

| Input ID | Parameter | Primary value | Plausible range/scenarios | Unit/scale | Evidence source/state | Why decision-bearing | `AUTHOR_INPUT_NEEDED` consequence |
|---|---|---|---|---|---|---|---|
| P-01 | effect worth detecting or precision target |  |  |  |  |  |  |
| P-02 | endpoint variance / baseline event probability / count rate and exposure |  |  |  |  |  |  |
| P-03 | allocation ratio |  |  |  |  |  |  |
| P-04 | cluster number/size distribution and ICC |  |  |  |  |  |  |
| P-05 | repeated-measure timing/correlation/covariance |  |  |  |  |  |  |
| P-06 | type-I error/multiplicity allocation |  |  |  |  |  |  |
| P-07 | target power or interval precision |  |  |  |  |  |  |
| P-08 | attrition/non-evaluable/assay-failure mechanism and rate |  |  |  |  |  |  |
| P-09 | feasible independent units/batches/cost/time |  |  |  |  |  |  |

## 6. Calculation or simulation plan

- Approach: closed-form / cluster design / mixed-GLM simulation / assurance-scenario / feasibility precision
- Formula/model matched to planned analysis:
- Simulation data-generating process, if applicable:
- Seeds/iterations/convergence and failure handling, if applicable:
- Success criterion counted in power/precision:
- Scenario grid:
- Expected output schema/plot/table:
- Code/config/environment/output locator:
- Plan versus computed state:

## 7. Attrition and analysis population

| Loss type | Level | Expected scenario/source | Differential? | Estimand consequence | Inflation/calculation handling | Bias sensitivity | Reporting denominator |
|---|---|---|---|---|---|---|---|
| pre-assignment ineligible |  |  |  |  |  |  |  |
| post-assignment attrition/welfare removal |  |  |  |  |  |  |  |
| assay/non-evaluable endpoint |  |  |  |  |  |  |  |
| entire cluster loss |  |  |  |  |  |  |  |

## 8. Design scenarios and feasibility

| Scenario | Independent units/allocation | Assumption changes | Estimated power/precision state | Cost/time/welfare consequence | Claim ceiling | Decision |
|---|---|---|---|---|---|---|
| primary |  |  | PLAN_ONLY / COMPUTED / NOT_ASSESSABLE |  |  |  |
| plausible-input sensitivity |  |  |  |  |  |  |
| resource-constrained |  |  |  |  |  |  |
| design repair/pilot |  |  |  |  |  |  |

## 9. Stop gate

| Decision | Verdict `PASS/CONDITIONAL/BIOSTATISTICIAN_REQUIRED` | Evidence | Exact blocker | Minimum pilot/source/specialist decision | Allowed fallback | Surviving claim |
|---|---|---|---|---|---|---|
| primary estimand/assigned unit |  |  |  |  |  |  |
| cluster/repeated dependence |  |  |  |  |  |  |
| effect/variance/base-rate inputs |  |  |  |  |  |  |
| attrition/estimability/model stability |  |  |  |  |  |  |
| specialist/high-stakes sign-off |  |  |  |  |  |  |

## 10. Writing and experiment handoff

- Statistical Methods fields:
- Results/figure/legend unit and denominator fields:
- Power/precision statement with evidence state:
- Attrition/deviation/sensitivity wording:
- Exact data/code artifacts required after execution:
- Single next decision-bearing action:
- `AUTHOR_INPUT_NEEDED`:
