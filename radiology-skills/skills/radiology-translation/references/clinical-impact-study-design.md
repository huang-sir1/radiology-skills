# Clinical-impact study design for imaging and AI

Use this reference when the question is whether an imaging test, model, reconstruction or workflow
changes reader decisions, timeliness, safety, resource use or patient outcomes. Retrospective accuracy,
external validation and decision-curve analysis are prerequisites or decision analyses—not observed
clinical impact.

## 1. Freeze the intervention and causal estimand

| Field | Required specification |
|---|---|
| Population/pathway | eligibility, setting, prevalence/spectrum and access constraints |
| Intervention | exact model/test/UI/workflow/version, threshold, availability and fallback |
| Comparator | current standard workflow, not an obsolete or artificial control |
| Assignment unit | patient/exam, reader, shift, team, site or time period |
| Time zero | when eligibility, assignment and follow-up begin |
| Primary endpoint | decision, time, safety, resource or patient outcome with scale/horizon |
| Estimand | policy/ITT, per-protocol/adherence, mean/risk/time contrast or effect modification |
| Contamination | how users/cases can cross arms or learning persists |
| Claim ceiling | simulated reader effect, live process effect, safety, resource or patient benefit |

Describe the complete intervention: inputs, UI placement, alert/abstention, human authority, operating
point, response to failure, training and support. “AI-assisted” is not a reproducible intervention.

## 2. Evidence ladder and design router

| Question | Suitable design | What it can establish |
|---|---|---|
| Does output change readers on a fixed case set? | randomized/counterbalanced MRMC, sequential or parallel reader study | controlled reader effect only |
| Can the frozen system run in the intended environment? | prospective silent/shadow deployment | technical availability, drift and counterfactual performance without influencing care |
| Does showing output change live workflow/decisions? | active prospective randomized/pragmatic or credible quasi-experimental design | process/decision impact under that implementation |
| Is individual randomization feasible without spillover? | patient/exam-level randomized trial | causal policy effect if contamination and analysis are handled |
| Is the intervention delivered to a worklist/team/site? | cluster randomized trial | cluster-level policy effect with enough clusters |
| Must rollout be staged? | justified stepped-wedge cluster design | effect separated from time only with adequate periods/clusters and secular-trend model |
| Was there a system-wide implementation date? | controlled interrupted time series when randomization was infeasible | level/slope effect under trend/concurrent-change assumptions |
| Does impact persist and remain safe? | prospective monitoring/RWE with a prespecified causal or surveillance objective | performance/safety in observed practice; not automatically causal |

A simple before–after comparison cannot separate intervention from secular trend, staffing, case mix or
concurrent policy change.

## 3. Controlled reader studies

- Choose fully crossed, partially crossed, sequential, parallel or another design deliberately; match
  analysis and power to reader/case assignment.
- Randomize/counterbalance case/arm order; manage washout, carryover, learning and memory. Sequential
  reading estimates a different workflow than independent paired reads.
- Report reader experience, training, interface, clinical information, prevalence/enrichment and
  reference standard.
- Primary endpoint should match intended use: paired accuracy/sensitivity/specificity, critical-error
  rate or another decision measure. Reading time, confidence and agreement are usually secondary unless
  the claim is explicitly workflow efficiency.
- Capture automation-induced errors: correct unaided -> incorrect aided, wrong high-confidence acceptance,
  failure to override and time lost to false alerts.
- Use MRMC inference for crossed reader/case performance and retain patient/reader denominators.

Reader studies do not establish live queue effects, patient outcomes or deployment safety.

## 4. Silent prospective study

Freeze model, threshold, pipeline and intended workflow before enrollment. Record:

- consecutive eligibility and real prevalence/spectrum;
- technical uptime, latency, missing inputs, OOD/abstention and output delivery success;
- frozen prospective accuracy/calibration and site/scanner/protocol strata;
- simulated counterfactual decision/worklist outcomes labelled as simulation;
- drift and failure triggers, without allowing output to influence care.

Silent deployment is valuable feasibility evidence but cannot measure how clinicians react to visible
output.

## 5. Active prospective/pragmatic study

### Assignment and concealment

- Align eligibility, assignment and intervention start. Predefine allocation/concealment, cluster/
  period boundaries and handling of crossover/contamination.
- Analyze at the independent assignment level; patient count does not compensate for too few sites,
  readers or periods.
- Preserve policy/ITT effect as primary where appropriate; define adherence/per-protocol analysis and
  its additional assumptions.

### Workflow clocks

For time endpoints freeze start, stop, pauses, censoring and competing events. Record acquisition,
availability, alert, opening, interpretation, communication and action timestamps separately. Include
off-hours, downtime, queued cases, transfers and failed/abstained examinations.

### Endpoint hierarchy

1. safety-critical patient/decision endpoint where feasible;
2. diagnostic/management decision quality;
3. time/resource endpoint with clinical consequence;
4. implementation fidelity, availability, uptake/override and user experience;
5. algorithm accuracy/calibration as process evidence.

Process success is not patient benefit. Define harms and adverse-event adjudication, including delayed
critical cases, unnecessary downstream testing and inequitable access/impact.

## 6. Implementation, fidelity and context

Measure who was exposed, whether output arrived in time, whether it was opened, acted on or overridden,
why, and what fallback occurred. Track staffing, training, workload, scanner/site, pathway, software,
threshold and policy changes. Distinguish:

- intervention unavailable;
- intervention available but not used;
- intervention used contrary to protocol;
- clinician override;
- technical/model failure;
- downstream action unavailable.

These states support mechanism/fidelity interpretation; they must not be selectively removed from the
primary policy-effect denominator.

## 7. Analysis and sample size

Route causal inference to `radiology-stats/references/causal-and-clinical-impact-inference.md`. Predefine
effect measure and CI, cluster/site/reader/time correlation, secular trends/autocorrelation, baseline
adjustment, missing outcomes, contamination, subgroup interactions and multiplicity.

Power/precision uses effect worth detecting, baseline rate/variance, allocation, ICC/autocorrelation,
number/size of clusters or readers/cases/periods, adherence, downtime, contamination and attrition. Use
simulation for MRMC, cluster, stepped-wedge and complex time designs; no universal reader/site count.

Return `BIOSTATISTICIAN_REQUIRED` for unresolved MRMC, cluster/stepped-wedge/ITS, contamination or
causal estimand/sample-size inputs.

## 8. Monitoring and change control

Predefine performance/calibration, availability/latency, subgroup, OOD, override and harm monitoring;
alert thresholds; responsible owner; investigation; rollback; and evidence required before model,
threshold, UI or workflow modification. A changed intervention is a new version and may require a new
protocol/authorization and evaluation.

For regulated products, verify current jurisdiction-specific requirements. A predetermined change
control plan documents planned changes and validation/impact controls; it is not permission for
unbounded self-updating.

## 9. Stop gates and output

Return `STOP_FOR_REPAIR` for an undefined comparator/intervention/version, outcome-selected operating
point, misaligned assignment/time zero, untracked concurrent changes, too few independent assignment
units for the claimed design, or patient-benefit language from retrospective/silent evidence.

Return:

`impact-use card -> intervention/comparator manifest -> design/assignment/time-zero -> endpoint/safety
hierarchy -> human-factors/fidelity plan -> statistical/sample-size brief -> monitoring/change control
-> claim ceiling -> deviations`.

## Primary and official sources

- Vasey B, et al. [DECIDE-AI](https://doi.org/10.1038/s41591-022-01772-9).
- SPIRIT–CONSORT Group. [Published SPIRIT 2025 and CONSORT 2025 statements](https://www.consort-spirit.org/published-statements).
- Liu X, et al. [CONSORT-AI](https://doi.org/10.1038/s41591-020-1034-x).
- Rivera SC, et al. [SPIRIT-AI](https://doi.org/10.1038/s41591-020-1037-7).
- FDA. [Predetermined Change Control Plan guidance for AI-enabled device software functions](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/marketing-submission-recommendations-predetermined-change-control-plan-artificial-intelligence).

Reporting and regulatory applicability are live facts; verify them at protocol freeze, deployment and
major change.
