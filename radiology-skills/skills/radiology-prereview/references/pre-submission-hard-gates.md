# Pre-submission hard gates

Use this reference for a final submission audit, rejected-paper rescue, or any manuscript meant for a high-level imaging/Nature-family venue. The purpose is to prevent the team from polishing around a fatal weakness.

## Gate logic

Each ordinary scientific/reporting gate is `PASS`, `CONDITIONAL`, or `FAIL`. The human-subjects
authorization gate additionally uses `STOP`; it is an absolute stop state, not a more severe synonym
for `CONDITIONAL`.

- `PASS`: evidence is present and manuscript text/figures report it clearly.
- `CONDITIONAL`: acceptable only if the limitation is explicitly bounded and unlikely to decide the editorial outcome.
- `FAIL`: for a non-authorization scientific/reporting gate, do not submit until fixed unless the
  author intentionally chooses a lower-scope venue, the remaining claim is supportable and the risk
  is explicit. This lower-scope exception never applies to human-subjects authorization.
- `STOP`: for applicable human-subjects authorization, the only readiness verdict is `Not ready`.
  It cannot be converted to `PASS`, `CONDITIONAL` or ordinary `FAIL` by venue choice, claim
  downgrading, author risk acceptance, retrospective wording or editorial preference.

## Hard gates

| Gate | What to check | Route if failed |
|---|---|---|
| Contribution map | The paper has a specific clinical/methodological contribution, not just "we built a model" | `radiology-writing`, `radiology-design` |
| Data integrity | Patient-level split, no leakage, correct labels/reference standard, exclusions documented | `radiology-radiomics`, `radiology-deep-learning`, `radiology-data` |
| Validation | Internal/temporal/external/multicenter/prospective validation matches the claim level | `radiology-design`, `radiology-stats` |
| Results-as-validation | Every major claim maps to a result/figure/table and does not exceed evidence | `radiology-writing`, `radiology-stats` |
| Statistical completeness | CIs, calibration, DCA/clinical utility when relevant, multiplicity, survival assumptions, sample-size/event limits | `radiology-stats` |
| Reporting stack | Study-type-appropriate EQUATOR-family checklists selected via radiology-reporting (CLAIM/TRIPOD+AI/CLEAR/STARD) and the Nature Reporting Summary are materially satisfied; IBSI/RQS are reproducibility/quality standards, checked separately | `radiology-reporting` |
| Figure/data crosswalk | Figures match data and manuscript claims; no render/overlap defects | `radiology-figure` |
| Citation verification | Key background, novelty, comparison, and guideline claims are supported by a fixed two-pass claim audit | `radiology-citation` |
| Human-subjects authorization | For every applicable activity, a versioned `radiology-ethics: human-subjects` receipt binds the reviewed document by path and SHA-256 and marks approval, consent/waiver and data-use authorization `DOCUMENT_VERIFIED` for the same population, sites, dates, data/tissue and activities | `radiology-ethics: human-subjects`; `STOP` until document-verified closure |
| Data/code sharing | Data and Code Availability promises match the verified consent/DUA/access restrictions, actual repository/access route and artifacts; this gate is assessed separately from authorization | `radiology-data`, with `radiology-ethics` only for consent/DUA consistency |
| Reviewer objection register | Likely objections are anticipated with evidence or bounded language | relevant skill |

## Absolute human-subjects STOP

For a final-readiness verdict, consume
`../templates/prereview-governance-gates.template.json` and validate it with
`../scripts/validate_prereview_governance_gates.py`. Apply `STOP` when an applicable approval,
consent/waiver or data-use authorization is missing, only author-reported, expired, conflicting,
out of scope, or not bound to the supplied `radiology-ethics` artifact and its physical SHA-256.
Only a current local-owner document can establish non-applicability. Manuscript wording, a published
cohort, de-identification, or a data-sharing restriction cannot convert this STOP to CONDITIONAL.

Run the sharing gate independently. Restricted or unavailable sharing may be honestly described and
handled according to venue policy; it never substitutes for permission to perform the research.

**Readiness override prohibition:** if any applicable human-subjects authorization row is `STOP`,
return `Not ready` and withhold submission-ready assurance. Do not return `Ready`, `Ready with
declared risk`, or `Major revision before submission`, and do not offer a lower-scope venue as a way
around the STOP. Safe gap documentation and institutional escalation may continue.

## Two-pass claim audit gate

Before final submission, run or request `radiology-citation/references/claim-verification-gate.md` for the abstract, Key Results, figure legends, tables, Discussion comparison claims, novelty claims, and graphical abstract text.

| Pass | Requirement | Failure mode |
|---|---|---|
| Extraction | Fixed list of claims with IDs and locations | hidden unchecked claims |
| Verification | Each claim has source/manuscript-data support status | unsupported or numerically wrong claims |

Do not declare a paper ready if an abstract or figure/table claim is unsupported, even when the prose sounds polished.

## Reviewer objection register

Create this table before submission:

| Likely reviewer objection | Evidence already in manuscript | Current weakness | Preventive fix | Severity |
|---|---|---|---|---|
| No external validation | Temporal validation only | claim says generalizable | soften claim / add external cohort | Blocker/Major |
| Calibration absent | none | risk model reports only AUC | add calibration plot/Brier or remove risk claim | Major |

This register turns pre-review into an action plan, not just criticism.

## Readiness verdict

Use one of these:

- **Ready**: all hard gates pass, the applicable human-subjects gate is document-verified, and only
  minor polish remains.
- **Ready with declared risk**: one or more conditional non-authorization gates, with bounded claims
  and target venue adjusted; unavailable when human-subjects authorization is `STOP`.
- **Major revision before submission**: one or more non-authorization major gates fail but are
  fixable; unavailable when human-subjects authorization is `STOP`.
- **Not ready**: fatal design/data/reporting gap cannot be fixed without new analysis/data.

`Not ready` is also mandatory whenever applicable human-subjects authorization is `STOP`, regardless
of whether the missing or conflicting authorization might later be repairable.

## Output table

| Gate | Status | Evidence/location | Risk if ignored | Required fix |
|---|---|---|---|---|
| Validation | FAIL | no external/temporal validation | major revision or rejection | revise claim or add validation |

Do not let good language, attractive figures, or a strong topic compensate for a failed hard gate.
