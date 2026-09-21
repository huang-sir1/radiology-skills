# Evidence-based skill improvement loop

Use this contract after a real skill run, failed handoff, source refresh or human adjudication reveals
possible friction. It improves the package without turning one anecdote, one model lapse or a
self-score into a permanent rule.

## 1. Reflect on one run

Freeze one `behavior-evals/run-observation.template.json` record outside the release tree. Bind the
exact prompt or frozen case, installed product/version and manifest digest, execution identity, raw
output or artifact hashes, exact evidence locators, expected behavior and observed behavior.

Classify the observation as exactly one of:

- `ROUTING_ERROR`: the wrong primary owner was selected or a required clarification was skipped;
- `EXECUTION_LAPSE`: the right contract existed but the run did not follow it;
- `TEMPLATE_FRICTION`: required work was duplicated, unclear or disproportionate;
- `HANDOFF_GAP`: a receiver could not consume the producer's artifact without reconstructing facts;
- `SOURCE_DRIFT`: a version, URL, status or dynamic requirement changed;
- `RUNTIME_LIMITATION`: the client/model/tool could not execute an otherwise valid contract; or
- `NO_DEFECT`: the observed behavior is consistent with the frozen contract.

Keep `persistent_change_authorized=false`. A reflection is evidence, not a diagnosis of the whole
skill and not permission to edit it.

## 2. Separate defect classes before proposing a change

Compare the observation with the exact installed skill version. Do not repair skill text when the
cause is an execution lapse, missing user authority, unavailable tool, unsupported client feature or
stale external source that already carries `LIVE_VERIFICATION_REQUIRED`. Conversely, do not dismiss a
missing receiver field or unsafe invariant as mere model variance.

Record the smallest reproducible unit: prompt, expected behavior, actual output lines, affected
artifact, workaround and residual boundary. Preserve negative and `NO_DEFECT` observations so that a
convenient story is not built only from failures.

## 3. Promote only an evidence pattern

Create an `improvement-candidate.template.json` record only after comparing observations. A candidate
may become `READY_FOR_REVIEW` when either:

1. the same non-`NO_DEFECT` class is reproduced in at least two distinct run IDs and two distinct
   frozen cases or prompt hashes; or
2. one P0/P1 invariant break creates a credible privacy, patient-safety, scientific-validity or
   record-integrity risk.

These are review-entry conditions, not proof that the proposed repair is correct. Repeated outputs
from the same run or paraphrases of one prompt do not count as independent replication.

## 4. Require a reversible, testable proposal

Every candidate names the target file, smallest proposed change, affected routes, source-freshness
impact, scientific owner, independent reviewer, regression to add and rollback. Prefer tightening an
existing boundary or handoff over adding a new template or skill. Reject a proposal that cannot state
what new test would fail before the change and pass after it.

No machine validator, model self-score or completed candidate may set
`persistent_change_authorized=true`. A qualified release owner reviews the evidence, checks for route
collisions and template burden, applies the smallest accepted patch, runs targeted and full release
validation, and records the external release decision separately.

## 5. Close the loop without erasing history

After release, retain the source observations, candidate decision, changed file hashes, regression
result and rollback route. A rejected candidate remains useful evidence. Re-open the issue only with
new evidence; do not silently rewrite prior observations to fit the later decision.

