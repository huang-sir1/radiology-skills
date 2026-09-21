# Revision Trace Matrix

Use this matrix for reviewer comments, internal audit findings, or protocol corrections. Freeze the
original criteria before inspecting the revised artifact. First compare the original and revised
manuscript/data/code against those criteria without relying on the response narrative. Then read the
response letter to locate additional evidence that may have been missed. A revision may satisfy,
partially satisfy, fail, or worsen a criterion; persuasive response language is not evidence that
the manuscript changed.

## 1. Revision contract

| Field | Entry |
|---|---|
| Project/manuscript identifier | [AUTHOR_INPUT_NEEDED: identifier] |
| Original artifact and version | [AUTHOR_INPUT_NEEDED: filename/version/date] |
| Revised artifact and version | [AUTHOR_INPUT_NEEDED: filename/version/date] |
| Review source | [AUTHOR_INPUT_NEEDED: external reviewer, editor, internal audit, or protocol gate] |
| Review/decision letter version | [AUTHOR_INPUT_NEEDED: filename/version/date] |
| Review target or venue | [AUTHOR_INPUT_NEEDED: target or state unknown] |
| Study scope | [AUTHOR_INPUT_NEEDED: imaging-only / mechanism-only / imaging-mechanism] |
| Primary inferential unit | [AUTHOR_INPUT_NEEDED: unit] |
| Primary matched n | [AUTHOR_INPUT_NEEDED: n and intersection rule] |
| Revision coverage | [AUTHOR_INPUT_NEEDED: comments/findings included and excluded] |

## 2. Frozen yardstick

Record these criteria from the original review before evaluating the revision. Do not tighten,
weaken, or replace them after seeing the author's response. New concerns belong in Section 6.

| Criterion ID | Original finding ID/comment | Frozen criterion | Required evidence type | Required closure evidence | Original severity | Original obligation | Original claim ceiling | Original confidence/scope limit |
|---|---|---|---|---|---|---|---|---|
| [AUTHOR_INPUT_NEEDED: stable ID] | [AUTHOR_INPUT_NEEDED: source ID or exact comment locator] | [AUTHOR_INPUT_NEEDED: criterion] | [AUTHOR_INPUT_NEEDED: text / table / figure / dataset / code / experiment] | [AUTHOR_INPUT_NEEDED: observable closure evidence] | [AUTHOR_INPUT_NEEDED: P0 / P1 / P2] | [AUTHOR_INPUT_NEEDED: must-fix / should-fix / consider] | [AUTHOR_INPUT_NEEDED: ceiling] | [AUTHOR_INPUT_NEEDED: confidence/basis/limit] |

## 3. Author adjudication record

Do not infer an author's decision from an edited file. Record explicit decisions or mark them as
requiring author input.

Split a compound reviewer comment into separately verifiable commitments while retaining the parent
criterion ID.

| Criterion ID / commitment ID | Request class | Author decision | Rationale | Intended action | Required evidence type | Author-confirmed scope |
|---|---|---|---|---|---|---|
| [AUTHOR_INPUT_NEEDED: criterion/commitment ID] | [AUTHOR_INPUT_NEEDED: manuscript-grounded defect / clarification / optional strengthening / reviewer preference / scope-contested] | [AUTHOR_INPUT_NEEDED: accept / partially accept / contest / cannot address] | [AUTHOR_INPUT_NEEDED: rationale] | [AUTHOR_INPUT_NEEDED: action] | [AUTHOR_INPUT_NEEDED: evidence type] | [AUTHOR_INPUT_NEEDED: scope] |

## 4. Revision verification matrix

Allowed verification states: `VERIFIED`, `PARTIAL`, `NOT ADDRESSED`, `MADE WORSE`,
`NOT VERIFIABLE`.

| Criterion / commitment ID | Pre-response evidence state | Author response claim | Action/method actually used | Result or evidence produced | Manuscript/data/code change | Exact location | Spatial/time/unit compatibility | Matched n | Final verification state | Adjustment from pre-response state and basis | Residual issue | Revised claim ceiling | Required next action |
|---|---|---|---|---|---|---|---|---:|---|---|---|---|---|
| [AUTHOR_INPUT_NEEDED: criterion/commitment ID] | [AUTHOR_INPUT_NEEDED: VERIFIED / PARTIAL / NOT ADDRESSED / MADE WORSE / NOT VERIFIABLE from blind comparison] | [AUTHOR_INPUT_NEEDED: response claim] | [AUTHOR_INPUT_NEEDED: analysis/experiment/text/boundary action and method] | [AUTHOR_INPUT_NEEDED: estimate/direction/benchmark/negative result or evidence pointer] | [AUTHOR_INPUT_NEEDED: actual change] | [AUTHOR_INPUT_NEEDED: section, line, figure, table, file, or commit] | [AUTHOR_INPUT_NEEDED: compatibility] | [AUTHOR_INPUT_NEEDED: n] | [AUTHOR_INPUT_NEEDED: final state] | [AUTHOR_INPUT_NEEDED: unchanged or exact evidence that changed the state] | [AUTHOR_INPUT_NEEDED: residual] | [AUTHOR_INPUT_NEEDED: ceiling] | [AUTHOR_INPUT_NEEDED: action] |

## 5. Claim-strength conservation

| Claim ID | Original wording | Revised wording | Evidence added or removed | Primary evidence state | Modality subtype | Claim-link status | Stronger, same, or weaker | Justified? | Action |
|---|---|---|---|---|---|---|---|---|---|
| [AUTHOR_INPUT_NEEDED: claim ID] | [AUTHOR_INPUT_NEEDED: wording] | [AUTHOR_INPUT_NEEDED: wording] | [AUTHOR_INPUT_NEEDED: evidence change] | [AUTHOR_INPUT_NEEDED: measured / derived / estimated / associated / predicted / perturbed; use missing only as an absence marker] | [AUTHOR_INPUT_NEEDED: assay or operation subtype] | [AUTHOR_INPUT_NEEDED: direct / inferred / proposed] | [AUTHOR_INPUT_NEEDED: direction] | [AUTHOR_INPUT_NEEDED: yes / no / uncertain with reason] | [AUTHOR_INPUT_NEEDED: retain / weaken / remove / verify] |

## 6. Newly discovered issues

New issues must not retroactively change whether an original criterion was satisfied. Evaluate them
separately and state whether they affect the current decision.

| New issue ID | Source class | Evidence pointer | Finding | Severity | Claim affected | Decision impact | Repair |
|---|---|---|---|---|---|---|---|
| [AUTHOR_INPUT_NEEDED: stable ID] | [AUTHOR_INPUT_NEEDED: revision regression / previously missed / indeterminate] | [AUTHOR_INPUT_NEEDED: pointer] | [AUTHOR_INPUT_NEEDED: finding] | [AUTHOR_INPUT_NEEDED: P0 / P1 / P2] | [AUTHOR_INPUT_NEEDED: claim] | [AUTHOR_INPUT_NEEDED: impact] | [AUTHOR_INPUT_NEEDED: repair] |

## 7. Fresh integrity re-check

Run this check from the revised artifact and its current evidence, not from the first review's
conclusions.

| Check | Applicability | Result | Evidence pointer | Consequence |
|---|---|---|---|---|
| Cohort counts and matched n are internally consistent | [AUTHOR_INPUT_NEEDED: APPLICABLE / NOT APPLICABLE / NOT ASSESSED] | [AUTHOR_INPUT_NEEDED: PASS / CONDITIONAL / STOP when applicable] | [AUTHOR_INPUT_NEEDED: pointer] | [AUTHOR_INPUT_NEEDED: consequence] |
| Inferential unit and repeated observations remain correct | [AUTHOR_INPUT_NEEDED: applicability] | [AUTHOR_INPUT_NEEDED: verdict] | [AUTHOR_INPUT_NEEDED: pointer] | [AUTHOR_INPUT_NEEDED: consequence] |
| Numerical results agree across text, tables, figures, and supplement | [AUTHOR_INPUT_NEEDED: applicability] | [AUTHOR_INPUT_NEEDED: verdict] | [AUTHOR_INPUT_NEEDED: pointer] | [AUTHOR_INPUT_NEEDED: consequence] |
| Citations exist and support the attached claims | [AUTHOR_INPUT_NEEDED: applicability] | [AUTHOR_INPUT_NEEDED: verdict] | [AUTHOR_INPUT_NEEDED: pointer] | [AUTHOR_INPUT_NEEDED: consequence] |
| Evidence-state and claim-link distinctions remain correct, including mechanism links when applicable | [AUTHOR_INPUT_NEEDED: applicability] | [AUTHOR_INPUT_NEEDED: verdict] | [AUTHOR_INPUT_NEEDED: pointer] | [AUTHOR_INPUT_NEEDED: consequence] |
| Competing explanations and limitations remain visible | [AUTHOR_INPUT_NEEDED: applicability] | [AUTHOR_INPUT_NEEDED: verdict] | [AUTHOR_INPUT_NEEDED: pointer] | [AUTHOR_INPUT_NEEDED: consequence] |
| No new causal or treatment-benefit overclaim was introduced | [AUTHOR_INPUT_NEEDED: applicability] | [AUTHOR_INPUT_NEEDED: verdict] | [AUTHOR_INPUT_NEEDED: pointer] | [AUTHOR_INPUT_NEEDED: consequence] |
| Data/code/accession/ethics statements match the current artifact | [AUTHOR_INPUT_NEEDED: applicability] | [AUTHOR_INPUT_NEEDED: verdict] | [AUTHOR_INPUT_NEEDED: pointer] | [AUTHOR_INPUT_NEEDED: consequence] |

## 8. Revision decision

| Field | Entry |
|---|---|
| Original criteria verified | [AUTHOR_INPUT_NEEDED: count verified / total, with PARTIAL, MADE WORSE and NOT VERIFIABLE visible] |
| P0 unresolved criteria | [AUTHOR_INPUT_NEEDED: IDs or state none] |
| P1 unresolved criteria | [AUTHOR_INPUT_NEEDED: IDs or state none] |
| Newly discovered decision-bearing issues | [AUTHOR_INPUT_NEEDED: IDs or state none] |
| Final verdict | [AUTHOR_INPUT_NEEDED: PASS / CONDITIONAL / STOP] |
| Final claim ceiling | [AUTHOR_INPUT_NEEDED: strongest defensible wording] |
| Claim-changing stop condition | [AUTHOR_INPUT_NEEDED: condition] |
| Author decision still required | [AUTHOR_INPUT_NEEDED: decision or state none] |

## 9. STOP rescue, if required

| Rescue element | Entry |
|---|---|
| Blocked revision claim | [AUTHOR_INPUT_NEEDED: claim] |
| Unmet frozen criterion | [AUTHOR_INPUT_NEEDED: criterion ID and reason] |
| Nearest acceptable revision | [AUTHOR_INPUT_NEEDED: bounded change] |
| Minimum new evidence needed | [AUTHOR_INPUT_NEEDED: evidence] |
| Wording currently allowed | [AUTHOR_INPUT_NEEDED: wording] |

## 10. Response-letter completion record

| Criterion ID / commitment ID | Response text status | Exact revised location stated | Evidence accurately described | Residual limitation disclosed |
|---|---|---|---|---|
| [AUTHOR_INPUT_NEEDED: criterion/commitment ID] | [AUTHOR_INPUT_NEEDED: complete / incomplete / requires author input] | [AUTHOR_INPUT_NEEDED: yes / no and location] | [AUTHOR_INPUT_NEEDED: yes / no and correction] | [AUTHOR_INPUT_NEEDED: yes / no and wording] |

A parent criterion is `VERIFIED` only when every required commitment is `VERIFIED`; one completed
subcommitment cannot hide an unaddressed sibling.
