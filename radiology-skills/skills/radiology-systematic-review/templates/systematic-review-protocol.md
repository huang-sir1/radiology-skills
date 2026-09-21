# Systematic review protocol

Use `AUTHOR_INPUT_NEEDED` rather than guessing. Preserve dated versions and amendments.

## 1. Protocol identity

| Field | Value |
|---|---|
| Review title / Protocol ID | [AUTHOR_INPUT_NEEDED] |
| Version and date | [AUTHOR_INPUT_NEEDED] |
| Review team and roles | [AUTHOR_INPUT_NEEDED] |
| Mode and primary route | [AUTHOR_INPUT_NEEDED] |
| Registration platform / ID / link | [AUTHOR_INPUT_NEEDED] |
| Registration status | PROSPECTIVELY_REGISTERED / RETROSPECTIVELY_REGISTERED / UNREGISTERED / REGISTRATION_NOT_APPLICABLE / NOT_VERIFIED |
| Review lifecycle | STATIC / LIVING / RETIRED |
| Lifecycle owner / last status confirmation | [AUTHOR_INPUT_NEEDED] |
| Funding / conflicts | [AUTHOR_INPUT_NEEDED] |
| Current evidence state | PLANNED / AUTHOR_REPORTED / PARTLY_VERIFIED / VERIFIED / NOT_ASSESSABLE |

## 2. Rationale, objective and question lock

- Rationale and decision this review should inform:
- Primary objective:
- Secondary objectives:
- Question framework: PICO / PIRD / PECO / PICOS / prediction domains / population-concept-context / other:
- Population/context:
- Index test / exposure / intervention / model:
- Comparator / reference standard:
- Outcome / target condition / estimand:
- Time horizon / threshold / intended use:
- Primary independent unit: study / patient / donor / lesion / other:
- Preliminary claim ceiling:

## 3. Eligibility criteria

| Dimension | Include | Exclude | Rationale |
|---|---|---|---|
| Population/context |  |  |  |
| Index/exposure/intervention/model |  |  |  |
| Comparator/reference standard |  |  |  |
| Outcomes/target condition/horizon |  |  |  |
| Study designs |  |  |  |
| Report/publication status |  |  |  |
| Language/date/geography |  |  |  |
| Minimum data for synthesis |  |  |  |
| Overlapping cohorts/multiple reports |  |  |  |

## 4. Search handoff to `radiology-search`

| Field | Specification |
|---|---|
| Concept blocks and synonyms | [AUTHOR_INPUT_NEEDED] |
| Controlled-vocabulary concepts | [AUTHOR_INPUT_NEEDED] |
| Databases/platforms/source types | [AUTHOR_INPUT_NEEDED] |
| Coverage dates / language | [AUTHOR_INPUT_NEEDED] |
| Grey literature / trial registries / preprints | [AUTHOR_INPUT_NEEDED] |
| Citation chasing / related-record policy | [AUTHOR_INPUT_NEEDED] |
| Exact strategy capture requirement | yes |
| Deduplication hierarchy | identifier then normalized bibliographic match; verify locally |
| Last-search date / update trigger | [AUTHOR_INPUT_NEEDED] |
| Retrieval/acquisition boundary | [AUTHOR_INPUT_NEEDED] |

Returned evidence required: source/platform, exact query, run date, raw count, deduplicated corpus,
unresolved duplicates, search limitations and lawful acquisition state.

### Search-strategy peer-review receipt

Do not infer peer review from team composition or acknowledgement text. Attach the actual receipt or
mark it `NOT_REVIEWED`.

| Field | Receipt |
|---|---|
| Status | NOT_REVIEWED / REVIEWED_OPEN / REVIEWED_CLOSED / NOT_APPLICABLE |
| Strategy ID / version / date reviewed | [AUTHOR_INPUT_NEEDED] |
| Reviewer role / independence / conflicts | [AUTHOR_INPUT_NEEDED] |
| Stated criterion or framework / version | [AUTHOR_INPUT_NEEDED] |
| Review date | [AUTHOR_INPUT_NEEDED] |
| Comments / marked strategy locator | [AUTHOR_INPUT_NEEDED] |
| Resolution and amended-strategy locator | [AUTHOR_INPUT_NEEDED] |
| Unresolved issues and consequence | [AUTHOR_INPUT_NEEDED] |
| Material amendment requiring re-review? | [yes / no / AUTHOR_INPUT_NEEDED] |
| Closure owner / date | [AUTHOR_INPUT_NEEDED] |

### Lifecycle and update plan

| Lifecycle | Required record |
|---|---|
| STATIC | final search date, currency justification at publication/submission, and conditions that would require an update |
| LIVING | monitored sources, trigger/cadence, responsible owner, last completed update, next checkpoint, update decision log and public/versioned output |
| RETIRED | retirement date/reason, final search date, successor or archive locator, and wording preventing use as current evidence |

- Current lifecycle state and rationale:
- Last completed search/update and evidence locator:
- Next trigger/checkpoint, if `LIVING`:
- Retirement reason/successor/archive, if `RETIRED`:
- Lifecycle status verification date/owner:

## 5. Selection and PRISMA flow

- Title/abstract reviewers and independence:
- Full-text reviewers and independence:
- Pilot/calibration:
- Conflict resolution:
- Automation/priority screening receipt (complete even when `NOT_USED`):

| Field | Frozen specification / evidence |
|---|---|
| Status | NOT_USED / PILOT / ACTIVE / SUSPENDED |
| Automation ID | [AUTHOR_INPUT_NEEDED] |
| Tool/provider and software version | [AUTHOR_INPUT_NEEDED] |
| Model ID and model/version snapshot | [AUTHOR_INPUT_NEEDED] |
| Prompt/instructions version and exact locator | [AUTHOR_INPUT_NEEDED] |
| Code/config version | [AUTHOR_INPUT_NEEDED] |
| Input-corpus digest | [AUTHOR_INPUT_NEEDED] |
| Pilot/calibration sample, sampling rule and reference human decisions | [AUTHOR_INPUT_NEEDED] |
| Calibration result and error classes | [AUTHOR_INPUT_NEEDED] |
| Ranking/exclusion threshold, frozen date and owner | [AUTHOR_INPUT_NEEDED] |
| Low-priority exclusion audit sampling rule and n | [AUTHOR_INPUT_NEEDED] |
| Recall safeguard, minimum acceptable value and breach action | [AUTHOR_INPUT_NEEDED] |
| Human override rule and immutable override-log locator | [AUTHOR_INPUT_NEEDED] |
| Final inclusion/exclusion responsibility | [named human role; AUTHOR_INPUT_NEEDED] |
| Score/recommendation/decision artifact locator and SHA-256 | [AUTHOR_INPUT_NEEDED] |

No low-priority record may be excluded solely by model rank unless the prespecified audit and recall
safeguard pass. A breach suspends automated exclusion and routes the affected set to human screening;
it does not license a post hoc threshold change.
- Full-text exclusion taxonomy:
- Study-family linking rule:
- PRISMA count reconciliation owner:

## 6. Extraction and data-query plan

- Extraction form/version:
- Extractor/verifier model:
- Source locations to capture:
- Study-family and Effect ID rule:
- Multiple thresholds/time points/outcomes/effects policy:
- Adjusted versus unadjusted policy:
- Missing/unclear data and author-contact policy:
- Transformations/calculations permitted before statistics handoff:

## 7. Risk of bias and applicability

| Evidence branch | Tool/domain family and version to verify | Reviewers/conflict | Overall-judgment logic | Applicability domains |
|---|---|---|---|---|
| Primary branch | [AUTHOR_INPUT_NEEDED] | [AUTHOR_INPUT_NEEDED] | follow verified tool | [AUTHOR_INPUT_NEEDED] |

## 8. Pooling-feasibility rules

Before seeing results, define which differences require `STRATIFY`, `NARRATIVE`, or
`STOP_FOR_REPAIR`:

- population/setting:
- design/validation type:
- index/exposure/intervention/model:
- comparator/reference standard:
- outcome/target condition/time horizon:
- prevalence/incidence quantity, denominator/person-time and measurement period, if applicable:
- observational exposure contrast, temporal order and adjustment class, if applicable:
- reliability/agreement construct, exact metric/model/form and reader/device/repeat hierarchy, if applicable:
- threshold/effect scale/contrast:
- patient/lesion/donor/cell/spot unit and dependence:
- overlapping cohorts/reports:
- risk-of-bias exclusions/sensitivities:

## 9. Quantitative synthesis specification

| Branch | Effect measure / direction | Eligible estimate class | Model candidate | Dependence | Heterogeneity | Subgroup/meta-regression | Sensitivity | Small-study assessment |
|---|---|---|---|---|---|---|---|---|
| Primary | [AUTHOR_INPUT_NEEDED] | [AUTHOR_INPUT_NEEDED] | [AUTHOR_INPUT_NEEDED] | [AUTHOR_INPUT_NEEDED] | [AUTHOR_INPUT_NEEDED] | [AUTHOR_INPUT_NEEDED] | [AUTHOR_INPUT_NEEDED] | [AUTHOR_INPUT_NEEDED] |

Implementation and computation handoff: `radiology-stats`.

## 10. Structured synthesis without meta-analysis

- Prespecified grouping dimensions:
- Effect direction/magnitude/precision display:
- Risk-of-bias/applicability integration:
- Discordance/heterogeneity explanation:
- Rule against p-value vote counting:
- Mechanism convergence/discordance fields, if applicable:

## 11. Certainty, reporting and writing

- Certainty/confidence framework and version to verify:
- Review lifecycle state at writing handoff and search-currency statement:
- Search-strategy peer-review receipt/limitations for Methods or Supplement:
- Domain judgment process:
- Guideline/reporting audit handoff: `radiology-reporting`.
- Planned tables/figures/supplement:
- Supported conclusion class:
- Forbidden stronger claim:
- Writing handoff owner: `radiology-writing`.

## 12. Deviations and amendments

| Amendment ID | Date | Protocol field | Old decision | New decision | Reason | Result-aware? | Affected outputs | Disclosure location |
|---|---|---|---|---|---|---|---|---|
| A-001 |  |  |  |  |  | yes / no / unknown |  |  |

## 13. Decision and unresolved-input ledger

| Decision/Input ID | Question | Options/tradeoff | Chosen state | Evidence/owner | Due before | Consequence if unresolved |
|---|---|---|---|---|---|---|
| D-001 |  |  | [AUTHOR_INPUT_NEEDED] |  | search / screen / extract / synthesize / write |  |
