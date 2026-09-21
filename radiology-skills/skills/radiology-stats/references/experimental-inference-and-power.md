# Experimental inference and power contract

Use this reference after the biological claim, experimental system, intervention/comparator and
primary readouts are defined. It turns that design into an estimand, analysis model and input-driven
power/precision brief. It does not choose a mechanism, prescribe a laboratory condition, invent local
variance, or replace ethics/biosafety and specialist statistical review.

## 1. Intake and route state

Declare one state: `PLAN_ONLY`, `DATA_READY`, `COMPUTED`, `AUTHOR_REPORTED`,
`PARTLY_VERIFIED`, `NOT_ASSESSABLE`, or `BIOSTATISTICIAN_REQUIRED`.

Record:

- Claim ID, hypothesis, system and primary intervention/comparator;
- primary endpoint, measurement time and endpoint family: continuous, binary, count/rate, or other;
- effect worth detecting or precision target and its scientific/clinical rationale;
- unit independently assigned to intervention and unit independently sampled from the target
  population;
- donor, litter, cage, animal, organoid line, culture, well, field, cell, section and time hierarchy;
- allocation/blocking/factorial structure, pairing, crossover or repeated measures;
- endpoint variance, baseline event probability, count rate/exposure, overdispersion, cluster ICC,
  cluster-size distribution and repeated-measure correlation when known;
- primary type-I error/multiplicity policy and desired power or precision criterion supplied by the
  protocol/author;
- expected non-evaluable samples, attrition, assay failure and missingness, with evidence source;
- feasible units, batches, calendar, cost and ethical/welfare constraints;
- pilot/external information source, uncertainty and transportability.

Never infer wells, fields, cells or time points as independent biological units from a table shape.

## 2. Define the estimand before the model

Write:

`population/system -> intervention strategy -> comparator -> endpoint/time -> analysis population ->
summary contrast -> handling of attrition/intercurrent events`.

Examples of contrast families without numeric defaults:

- mean difference or ratio at a prespecified time;
- baseline-adjusted difference;
- group-by-time contrast or trajectory feature;
- risk/risk-ratio/odds-ratio for a binary endpoint;
- count/rate ratio with exposure offset;
- factorial main effect or interaction;
- donor/animal-level response summary.

Do not power one estimand and report another because it becomes favourable.

## 3. Independent allocation and hierarchy

Inference follows the unit receiving independent assignment or exposure:

| Design feature | Required decision | Common invalid shortcut |
|---|---|---|
| donor-derived samples | whether donors, derived lines or separately randomized cultures receive intervention | cells/wells from one donor counted as donor replication |
| litter/cage/animal | whether treatment is assigned by litter, cage or animal and whether litter/cage induces clustering | every animal treated as independently randomized when exposure is cage-level |
| repeated wells/fields/cells | aggregation or hierarchical measurement model | technical/subsample count used as biological `n` |
| repeated time points | subject/unit random effect and time covariance/contrast | independent test at each time with no multiplicity or interaction |
| batch/plate/section | blocking/bridge and fixed/random representation | correcting batch after outcome inspection or ignoring complete confounding |
| paired/matched design | pair ID, within-pair contrast and broken-pair handling | unpaired analysis that discards matching |

If assignment and analysis units cannot be reconciled, return `BIOSTATISTICIAN_REQUIRED` before
power or inferential recommendations.

## 4. Endpoint/model routes

### 4.1 Continuous endpoint

Candidate models include linear models, baseline-adjusted models and linear mixed/hierarchical models.
Specify:

- raw or transformed estimand and scale;
- residual distribution/variance structure and whether heteroscedasticity is expected;
- fixed effects, interactions, blocking factors and random effects;
- aggregation from fields/cells/wells to the valid unit;
- robust or permutation/bootstrap alternative when justified;
- effect estimate, interval and diagnostics—not only a group-wise p-value.

Rank-based tests do not automatically estimate a mean or median difference, and repeated technical
measurements do not repair few independent units.

### 4.2 Binary endpoint

Candidate models include binomial regression, logistic mixed models, GEE or design-matched exact/
penalized approaches. Specify:

- risk, risk ratio, odds ratio or risk difference estimand;
- event definition/time, denominator and repeated/cluster structure;
- baseline event probability and treatment contrast used for planning;
- separation/sparse-event diagnostics and fallback;
- marginal versus conditional interpretation.

Do not translate an odds ratio into a risk ratio or absolute benefit without required baseline-risk
information.

### 4.3 Count or rate endpoint

Candidate models include Poisson, negative-binomial or mixed/GEE count models. Specify:

- count versus rate estimand and exposure/observation-time offset;
- mean-variance relation, overdispersion and clustering;
- recurrent-event/within-unit structure;
- zero process and whether zero inflation/hurdle structure has a scientific basis;
- incidence-rate ratio or mean-count contrast with interval.

Do not choose a zero-inflated model merely because it improves fit after viewing the preferred
contrast.

### 4.4 Repeated measurements and longitudinal contrasts

Specify the primary time contrast before fitting:

- endpoint at a fixed time adjusted for baseline;
- group-by-time interaction or prespecified contrast vector;
- area/trajectory summary when scientifically meaningful;
- correlation/covariance structure and random effects;
- unequal timing, dropout and missingness assumptions.

Do not replace the longitudinal estimand with separate tests at every time point. If treatment,
time and batch are aliased, the intended effect may be unestimable.

## 5. Power and precision inputs

Power is a design calculation, not a universal replicate count. Complete every applicable input:

1. primary estimand/model/test and sidedness/error definition from the protocol;
2. effect worth detecting or desired interval precision, with scientific rationale;
3. endpoint variance, baseline event probability, rate/exposure or other nuisance parameter;
4. allocation ratio, number/size distribution of clusters and cluster ICC;
5. within-unit repeated-measure correlation/covariance and number/timing of measurements;
6. blocking, pairing, factorial interactions or multiple primary contrasts;
7. multiplicity/error allocation and target power/precision;
8. expected attrition, assay failure, non-evaluable outcome and differential-loss scenarios;
9. feasible independent units, batches, cages/litters/donors, cost/time and ethical constraints;
10. source/evidence state and plausible range for every numerical input.

The effect worth detecting should reflect a decision-bearing biological difference, not merely a
large pilot point estimate. Pilot variance/ICC estimates can be unstable; carry their plausible range
into scenarios. Do not report observed post hoc power as evidence for a completed result.

## 6. Calculation approach

Choose the approach that matches the planned analysis:

- closed-form precision/power when the design and estimand genuinely match the formula;
- cluster/design-effect calculation only with defensible cluster size/ICC assumptions and the same
  allocation level as the experiment;
- mixed-model or generalized-model simulation when repeated, hierarchical, count, binary, attrition
  or complex covariance structure makes a simple formula misleading;
- assurance or scenario grids when nuisance parameters are uncertain;
- feasibility-constrained precision reporting when available independent units cannot meet a chosen
  power/precision objective.

Record code/configuration, seeds, number of simulations if used, convergence/failure handling,
software/version and the exact criterion counted as success. There is no universal minimum sample,
event, donor, litter, cage, animal or replicate threshold.

## 7. Attrition and missingness

Separate:

- pre-randomization/non-eligible loss;
- post-assignment attrition, death/welfare removal or culture/assay failure;
- missing endpoint/measurement;
- entire cluster loss versus within-cluster missingness;
- differential loss by intervention and loss related to outcome.

Inflation for attrition requires a source-backed scenario and does not correct attrition bias.
Prespecify the analysis population, reasons/denominators, missing-data assumptions and sensitivity
analyses. If dropout is outcome-related or treatment-related, a simple complete-case analysis may not
estimate the intended effect.

## 8. Sensitivity and feasibility routes

Return at least the routes that are decision-bearing:

- **primary design:** protocol-preferred estimand and best-supported nuisance inputs;
- **plausible-input sensitivity:** effect, variance/base rate, ICC/correlation, cluster-size and
  attrition ranges justified by evidence;
- **resource-constrained design:** fixed feasible independent units with attainable precision/power
  and reduced claim ceiling;
- **design repair:** alternative allocation, repeated measurement, blocking, endpoint or pilot that
  resolves an unidentifiable input without outcome shopping.

Do not reduce valid comparators or independent units merely to keep more secondary endpoints.

## 9. Executable brief and stop gate

Complete `templates/experimental-inference-power-brief.md`. It must specify input schema, estimand,
allocation/hierarchy, model formula in words or code, power inputs and ranges, calculation/simulation
plan, diagnostics, attrition, sensitivity, expected artifacts and failure assertions.

Return `BIOSTATISTICIAN_REQUIRED` and stop a final model/sample-size recommendation when:

- the assigned/randomized unit or primary estimand is unresolved;
- treatment is completely confounded with batch, donor, litter, cage or time;
- no defensible effect-worth-detecting/precision target or endpoint nuisance inputs/ranges exist;
- cluster/repeated dependence is material but ICC/correlation/covariance cannot be bounded;
- separation, singularity, sparse information or anticipated attrition makes the proposed model
  unidentified or unstable;
- adaptive/sequential, multi-stage, regulatory, confirmatory or welfare-critical decisions require
  accountable specialist sign-off.

Return the exact blocker, minimum pilot/source input, permissible fallback and surviving claim.

## 10. Writing handoff

Methods receive the allocation unit, hierarchy, estimand, model, effect/variance assumptions, power or
precision criterion, multiplicity, attrition, software/version and deviations. Results receive actual
unit counts, analyzed denominators, effect/interval, diagnostics, attrition and all prespecified
primary contrasts. Figures/legends distinguish biological/experimental units from wells/fields/cells.
Discussion preserves model, feasibility, missingness and translation limits. A planned calculation
cannot be written as achieved power or verified adequacy.
