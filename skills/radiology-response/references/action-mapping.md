# Comment classification → action → location

## Classify each comment
- **Severity**: major (affects validity/conclusions) vs minor (clarity/presentation).
- **Type**: analysis/method · result/interpretation · claim/overreach · reference ·
  presentation/figure · reproducibility/reporting.
- **Feasibility**: doable now · needs new data/analysis · needs author decision · reasonable
  to push back.

## Action codes
| Code | Use when | Response shape |
|---|---|---|
| `ACCEPT_TEXT` | wording/clarification fix | "We have revised … (p X, lines …)." |
| `ACCEPT_ANALYSIS` | added/changed an analysis | state method + result + location (route to radiology-stats) |
| `NEW_EXPERIMENT` | new data/validation requested | describe plan/result; if pending → AUTHOR_INPUT_NEEDED |
| `ADD_RESULT` | report an existing-but-unshown result | add to Results/supplement + cite location |
| `SOFTEN_CLAIM` | overclaim flagged | calibrate wording (radiology-polishing) + cite change |
| `CLARIFY` | misunderstanding | clarify; point to existing/added text |
| `DISAGREE_WITH_REASON` | reviewer is mistaken/out of scope | respectfully, with evidence/citation; offer a compromise edit |
| `AUTHOR_INPUT_NEEDED` | only author can answer/do | flag for the author; don't fabricate |

## Traceability rule
Every "we changed X" must cite **where** (section/page/line/figure/table/supplement) or show
a visible placeholder. No untraceable "revised accordingly."

## Cross-reviewer consistency
When reviewers conflict, reconcile explicitly: acknowledge both, choose a defensible path
with reasons, and make a single consistent manuscript change (note it to both).
