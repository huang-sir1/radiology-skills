# Comment classification → action → location

## Decompose before classifying

Preserve the reviewer's original order and wording. Assign the compound comment a parent ID, then
split every independently verifiable request into child commitments (`R1-2a`, `R1-2b`). Repeated
requests may cross-reference one canonical commitment, but no item may disappear through deduplication.

## Classify each commitment

- **Request class**: manuscript-grounded defect · clarification-needed · optional strengthening ·
  reviewer preference · scope-contested/infeasible. Use
  `non-actionable-summary-or-praise (N/A—NON_ACTIONABLE)` only when there is no request or
  decision-bearing concern; this operational intake class is not part of corpus request-frequency
  statistics. Reviewer tone and the words “must” or “should” do not establish scientific necessity.
  `N/A—AUDIT_CONTROL` is reserved for regression fixtures and package-level failures such as stale
  manifests or unresolved placeholders; it is never assigned to a reviewer request or counted in the
  transparent-review corpus.
- **Editorial obligation**: `MUST_FIX` · `SHOULD_FIX` · `CONSIDER` · `UNKNOWN`. A non-`UNKNOWN`
  value requires a bounded quote and locator from the decision/editor letter. Never infer it from
  reviewer tone, request class, severity, reviewer count or eventual publication. Obligation controls
  whether the item must be explicitly answered or escalated to the editor; it does not make the
  reviewer's preferred experiment scientifically necessary.
- **Scientific consequence**: affects validity/claim ceiling · affects interpretation/transport ·
  affects reproducibility/reporting · presentation only.
- **Type**: design/cohort/unit · analysis/method · result/interpretation · claim/overreach · validation ·
  reference · presentation/figure · reproducibility/reporting.
- **Author decision**: accept · partially accept · contest · cannot address. Do not infer this decision.
- **Feasibility**: doable from current material · needs reanalysis · needs new data/experiment · needs
  author input · scientifically reasonable to push back.

## Action codes
| Code | Use when | Response shape |
|---|---|---|
| `ACCEPT_TEXT` | wording/clarification fix | "We have revised … (p X, lines …)." |
| `ACCEPT_ANALYSIS` | added/changed an analysis | state method + result + location (route to radiology-stats) |
| `NEW_EXPERIMENT` | new data/validation requested | describe plan/result; if pending → AUTHOR_INPUT_NEEDED |
| `ADD_RESULT` | report an existing-but-unshown result | add to Results/supplement + cite location |
| `SOFTEN_CLAIM` | overclaim flagged | calibrate wording (radiology-polishing) + cite change |
| `CLARIFY` | misunderstanding | clarify; point to existing/added text |
| `DISAGREE_WITH_REASON` | reviewer is mistaken/out of scope | respectfully state the governing reason and existing evidence; add an edit or sensitivity only if it reduces a real ambiguity |
| `AUTHOR_INPUT_NEEDED` | only author can answer/do | flag for the author; don't fabricate |
| `REPORT_EXISTING` | result/evidence exists but is not visible | state the result and add it to the correct manuscript/display location |
| `REANALYZE` | current analysis does not satisfy the criterion | run the corrected analysis, report changed or unchanged results, and propagate consequences |
| `VALIDATE` | an independent/orthogonal validation is required for the retained claim | freeze the object, dataset/assay, metric/readout and pass/fail criterion before execution |
| `BOUND_SCOPE` | request is infeasible or unnecessary for the declared claim | state the boundary, disclose the limitation and narrow the claim if needed |
| `ACKNOWLEDGE_ONLY` | praise, summary or a non-actionable observation | brief acknowledgement; no invented commitment, method, result or change |
| `ANSWER_FROM_EXISTING_RECORD` | the answer is already established and need not be newly reported | answer from a versioned artifact and give its source locator; manuscript change may be `N/A—NO_MANUSCRIPT_CHANGE_JUSTIFIED` |
| `CROSS_REFERENCE_ONLY` | another stable response fully answers the repeated item | cite the canonical issue/response ID and state which child obligation it closes |
| `NO_CHANGE_JUSTIFIED` | the current claim and reporting already satisfy the governing criterion | give the criterion-linked rationale and existing evidence locator; do not fabricate a compromise analysis or edit |
| `EDITOR_CLARIFICATION_REQUESTED` | decision/editor instructions are ambiguous or conflict materially | ask the editor a narrow process/scientific question; force `NOT_VERIFIED`, pending, and `NOT_READY_FOR_SUBMISSION_ASSEMBLY` until a versioned answer is received |

## Traceability rule
Every final response involving new work or a manuscript change must provide:

`position/rationale -> action and method -> result/evidence -> exact revised location -> residual
limitation or claim boundary -> internal artifact-fulfillment state`.

For `ACKNOWLEDGE_ONLY`, `CROSS_REFERENCE_ONLY`, `ANSWER_FROM_EXISTING_RECORD` or
`NO_CHANGE_JUSTIFIED`, do not force a fake method/result/location. Record the applicable existing
evidence or canonical response locator and use `N/A—NO_NEW_WORK` or
`N/A—NO_MANUSCRIPT_CHANGE_JUSTIFIED` explicitly. The internal fulfillment audit still verifies that
the no-change rationale answers the exact commitment.

Every "we changed X" must cite **where** (section/page/line/figure/table/supplement) or show a visible
placeholder in a planning draft. No final letter may use an untraceable "revised accordingly." “We
performed” without the resulting estimate/direction/finding is not fulfilled.

## Cross-reviewer consistency
When reviewers conflict, reconcile explicitly: acknowledge both, choose a defensible path
with reasons, and make a single consistent manuscript change (note it to both).
