# Reviewer response audit gate

Use this reference after drafting a point-by-point response, before sending the revision to the journal, or when reviewer comments are numerous, conflicting, or analysis-heavy.

## Response ledger

Every reviewer/editor comment receives a row:

| ID | Comment summary | Category | Action | Manuscript location | Evidence artifact | Status |
|---|---|---|---|---|---|---|
| R1-1 | External validation concern | validation | SOFTEN_CLAIM / ADD_ANALYSIS | Abstract, Discussion | new Table S2 | resolved / pending |
| R2-3 | Calibration requested | statistics/figure | ADD_RESULT | Results, Fig 3 | calibration script/output | pending author input |

Status options:

- `RESOLVED`: action is completed and location is known.
- `PARTIAL`: action is partly completed; limitation is disclosed.
- `PENDING_AUTHOR_INPUT`: cannot answer without author data/decision.
- `SCIENTIFIC_DISAGREEMENT`: respectful disagreement with evidence and scope reasoning.
- `NOT_FEASIBLE`: request cannot be done; reason and mitigation are explicit.

## Factuality lock

Before finalizing each response, verify:

- The claimed analysis/experiment was actually performed.
- Reported numbers match the revised manuscript, tables, and figures.
- Page/line/figure/table locations exist or are marked as placeholders.
- Added citations are verified.
- No response says "we revised accordingly" without describing what changed.
- A limitation is not presented as solved unless it truly is solved.

## Tone rules

- Start with appreciation only when it is natural; do not over-apologize.
- State the action first, then the evidence/location.
- If disagreeing, acknowledge the concern, define the scope, and cite data/guidance.
- Do not make reviewer-facing promises that the manuscript does not fulfill.

## Conflict handling

When reviewers ask for incompatible changes:

| Conflict | Resolution |
|---|---|
| One reviewer asks to shorten; another asks for detail | Put key text in manuscript, full detail in supplement |
| One asks for stronger claim; another flags overclaim | Keep bounded claim and explain evidence boundary |
| New analysis requested but data unavailable | Explain infeasibility, add limitation, provide sensitivity/negative control if possible |

## Final audit output

| Audit item | Pass? | Notes |
|---|---|---|
| Every comment has a stable ID | yes/no | ... |
| Every response has action + location | yes/no | ... |
| All claimed new analyses verified | yes/no | ... |
| Numbers match revised manuscript | yes/no | ... |
| Unresolved items are explicit | yes/no | ... |
| Tone is cooperative and evidence-forward | yes/no | ... |

If any audit item fails, return the response letter with a fix list rather than calling it final.
