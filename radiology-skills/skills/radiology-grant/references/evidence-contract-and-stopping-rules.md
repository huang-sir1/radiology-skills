# Evidence contracts, claim boundaries and stopping rules

## Evidence states

Assign a state before using any assertion in a proposal or review:

| State | Meaning | Permitted use |
|---|---|---|
| `VERIFIED_CURRENT` | checked against a current, applicable primary/official source | compliance or factual premise, with citation and retrieval date |
| `OFFICIAL_CYCLE_SNAPSHOT` | official for a named cycle/mechanism but not rechecked against the live call | orientation only; must be reverified before submission advice |
| `VERIFIED_RESEARCH_ARTIFACT` | traceable team result with dataset/code/output/version | preliminary evidence, within its measured scope |
| `USER_ATTESTED` | supplied by the user/team but not independently verified | attributed feasibility input, never silently promoted to verified |
| `CALCULATED` | derived from visible inputs with a reproducible calculation | planning/feasibility, with assumptions |
| `HYPOTHESIS` | proposition to be tested | rationale and aim; never preliminary evidence |
| `PLANNED` | future action/resource/analysis | approach only |
| `INFERRED` | reviewer interpretation beyond direct evidence | explicitly labelled reasoning |
| `MISSING` / `STALE` / `CONFLICTING` | absent, outdated or inconsistent evidence | finding and repair request; not a positive claim |

Forbidden promotions include `PLANNED → VERIFIED_RESEARCH_ARTIFACT`, `USER_ATTESTED →
VERIFIED_CURRENT`, and `model association → mechanism/causality/utility` without new evidence.

## Research canon

Before drafting or full audit, build one evidence ledger:

| Claim/need | Exact evidence anchor | State | Applicability | Limitation | Proposal location/aim |
|---|---|---|---|---|---|

Every premise, innovation, feasibility and preliminary-data statement should map to an anchor or be
labelled as a hypothesis/unknown. A citation count is not a premise audit; check whether each source
actually supports the span claimed.

## Aim evidence contract

| Field | Requirement |
|---|---|
| Purpose | testable sub-question serving the central question |
| Inputs | cohort, images, metadata, labels, approvals, people, compute and preliminary artifacts |
| Independent unit | patient/exam/lesion/image/reader/site hierarchy; no denominator ambiguity |
| Measurement chain | acquisition, reconstruction, post-processing and QC assumptions |
| Allowed claims | inference successful completion would support |
| Forbidden claims | mechanism, causality, transport or utility not licensed by the design |
| Comparator/analysis | prespecified comparison, estimand/metric and uncertainty |
| Success criterion | evidence-based decision criterion; not an invented “good” number |
| Failure signal | observation that weakens the hypothesis or feasibility premise |
| Fallback | scientifically meaningful alternative, labelled if exploratory |
| Dependency | upstream evidence/resource that must exist and failure propagation |
| Milestone/owner/time | inspectable completion and decision point |
| Budget link | quantity and cost visibly derived from this work |

Use `templates/aim-milestone-risk-register.md` for multiple aims.

## Claim ceiling

Classify each aim's maximum inference:

1. technical performance / measurement repeatability;
2. association or discrimination;
3. calibrated prediction / transport to a defined setting;
4. diagnostic or prognostic accuracy against a valid reference standard;
5. changed clinician decision or workflow performance;
6. improved patient/process outcome;
7. causal or mechanistic explanation.

Do not cross levels by wording alone. External validation does not establish clinical utility;
biological correlation does not prove mechanism; retrospective treatment/outcome associations do
not prove causal benefit.

## Stopping rules

Return `STOP_AND_REFRAME` when any unresolved condition invalidates the proposed programme:

- target call, eligibility or submission route is unresolved and the user requests readiness;
- a live NSFC workflow would rely on directly generated application text contrary to the current
  call's AI-use rule;
- no aim answers the stated central question;
- required images, metadata, reference standard, events, independent sites or approvals do not
  exist and no credible acquisition route is documented;
- sample/event/cluster count cannot support planned complexity;
- outcome leakage, site-outcome confounding or measurement shift makes the primary inference
  non-identifiable;
- aims depend circularly on one another;
- preliminary evidence contradicts the premise and no honest reformulation remains;
- the budget/timeline cannot execute the minimum valid design;
- the requested claim exceeds the strongest available design with no plan to add the needed
  evidence.

Record the triggering evidence, affected aims and smallest scientifically valid re-scope. Do not
polish an infeasible project into apparent feasibility.
