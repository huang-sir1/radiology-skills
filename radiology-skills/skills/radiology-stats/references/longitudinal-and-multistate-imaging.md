# Longitudinal and multi-state imaging inference

Use this reference when repeated imaging measurements, dynamic prediction, disease-state transitions,
recurrent events, competing risks or informative observation/dropout are central. A repeated-measures
model is not chosen merely because multiple scans exist; start from the longitudinal estimand.

## 1. Freeze time, state and estimand

| Field | Required specification |
|---|---|
| Time origin | diagnosis, treatment start, surgery, baseline imaging or another reproducible event |
| Observation schedule | planned windows, actual times, unscheduled triggers and maximum follow-up |
| Unit/hierarchy | patient, lesion, organ, reader, scanner/site and repeated measurement nesting |
| Longitudinal measure/state | definition, units/criteria/version and measurement-error process |
| Event/transition | origin/destination states, absorbing/recurrent/competing events and adjudication |
| Intercurrent events | death, treatment switch/stop, surgery, rescue, missing scan and strategy |
| Estimand | mean trajectory/change, state occupancy/transition, cumulative incidence, recurrent burden or dynamic risk |
| Conditioning | baseline, landmark/event-free status and variables known at that time |
| Claim | descriptive, prognostic/dynamic prediction, treatment effect or effect modification |

Requiring a post-baseline scan conditions on being observable/alive/event-free until that scan. Name the
landmark population and do not generalize it to all baseline patients.

## 2. Data and observation-process audit

- Preserve actual timestamps, visit windows, treatment states, scan reason and nonattendance/failure
  reason. Visit labels alone are insufficient.
- Keep all patient timepoints in one partition and model lesion/reader/site dependence explicitly.
- Separate scheduled from symptom-triggered scans; their observation process may depend on latent
  disease severity.
- Distinguish intermittent missing values, informative visit timing, dropout, terminal events and
  administrative censoring.
- Validate lesion/exam linkage, criteria/version, registration and measurement repeatability before
  interpreting change.
- Record delayed entry, left truncation, interval-censored events and competing events when applicable.

## 3. Route by estimand

### Repeated continuous/ordinal measurement

- Paired analysis is limited to fixed two-timepoint complete pairs.
- Mixed models estimate subject-specific/random-effect trajectories conditional on model assumptions;
  GEE targets population-average contrasts with a working correlation and adequate clusters.
- Predefine time form (categorical, spline, nonlinear), baseline handling, covariance/random effects and
  treatment/time interactions. Do not select the curve after viewing significance.
- Mixed-model likelihood under missing-at-random assumptions does not solve informative dropout or
  symptom-driven visit timing; add explicit sensitivity/joint/weighted approaches when justified.

### Landmark and dynamic prediction

- At each landmark include only information available then and define the event-free/observable target
  population and prediction horizon.
- Fit/tune within development patients and evaluate calibration, discrimination and error dynamically
  on untouched patients/sites/time.
- Repeated landmark estimates are dependent; do not report them as independent confirmations.

### Joint longitudinal–event models

- Specify longitudinal submodel, event submodel and association structure (current value, slope,
  cumulative or another prespecified function).
- Joint modeling can address association and informative dropout under its shared-process assumptions;
  it does not establish causality or automatically fix misspecification.
- Validate dynamic predictions and inspect sensitivity to random-effects/association/time forms.

### Multi-state and competing-risk models

- Draw allowed transitions and define time scale, origin, absorbing states and whether transitions are
  interval censored.
- Choose cause-specific hazards, subdistribution/cumulative-incidence or transition-probability/state-
  occupancy estimands from the question. Hazard estimands and absolute risk answer different questions.
- Treat death or other competing events explicitly. Kaplan–Meier with competing events censored can
  overstate event probability.
- For recurrent events, define event ordering, terminal event and whether the estimand is rate, mean
  cumulative count, gap time or another quantity.

### Time-varying treatment/confounding

If imaging both predicts later treatment and is affected by prior treatment, ordinary covariate
adjustment can block mediation or induce bias. Define the treatment strategy and causal estimand, then
use a justified longitudinal g-method/target-trial route under `causal-and-clinical-impact-inference.md`.

## 4. Measurement error and multiple lesions

- Change combines biological trajectory and acquisition/registration/annotation error. Use repeatability
  evidence and sensitivity to measurement procedure.
- Decide whether patient burden, selected target, worst lesion or a hierarchical lesion model defines
  the endpoint. Lesion disappearance/new/split/merge rules must be frozen.
- Tiles, lesions and scans increase within-patient resolution, not independent patient n.
- If an estimated imaging trajectory is entered into a survival model as if observed without error,
  quantify the consequence or use a joint/error-aware approach.

## 5. Model checks and sensitivity

Predefine checks for residual/time functional form, random-effects/covariance structure, proportional
hazards where used, transition sparsity, Markov/semi-Markov assumption, influential patients/sites,
competing-event definition, visit-window/landmark choice, interval censoring, missing-not-at-random
scenarios and measurement error.

Report absolute risk/state occupancy/trajectory with CIs, denominators/risk sets and event/transition
counts. A p value for time is not an adequate longitudinal result.

## 6. Sample size and validation

Plan from independent patients, number/timing of observations, within-patient covariance, event/
transition counts, censoring/competing events, dropout/visit process, site clustering and model
complexity. Use simulation for joint, multi-state, sparse-transition or irregular-visit designs. More
scans cannot replace patients or events.

Externally validate dynamic prediction in the intended site/time/protocol with the full measurement and
landmark pipeline frozen. Model updating consumes the evaluation cohort's independence.

Return `BIOSTATISTICIAN_REQUIRED` for unsupported joint/multi-state/interval-censored, recurrent/terminal,
informative-observation or time-varying-confounding models.

## 7. Stop gates and reporting contract

Return `STOP_FOR_REPAIR` for undefined time zero/state/transition, future leakage, impossible chronology,
untraceable lesion linkage, death treated as ordinary missingness against the estimand, patient timepoints
crossing partitions or causal treatment language without identification.

Return:

`time/state/estimand card -> observation/missingness process -> data hierarchy/linkage -> selected model
and assumptions -> event/transition and risk-set counts -> effect/trajectory/risk with CI -> dynamic
validation -> sensitivity -> claim ceiling -> deviations`.

## Primary and official sources

- ICH. [E9(R1) Estimands and Sensitivity Analysis](https://database.ich.org/sites/default/files/E9-R1_Step4_Guideline_2019_1203.pdf).
- Fine JP, Gray RJ. [Competing-risks subdistribution model](https://doi.org/10.1080/01621459.1999.10474144).
- Putter H, et al. [Competing risks and multi-state models](https://doi.org/10.1002/sim.2712).
- Wulfsohn MS, Tsiatis AA. [Joint model for survival and longitudinal data](https://doi.org/10.2307/2533558).
- Collins GS, et al. [TRIPOD+AI](https://doi.org/10.1136/bmj-2023-078378).
