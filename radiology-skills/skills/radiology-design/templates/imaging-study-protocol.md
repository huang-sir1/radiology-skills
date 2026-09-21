# Imaging study protocol — fillable template

Use `AUTHOR_INPUT_NEEDED`, `NOT_VERIFIED`, `NOT_APPLICABLE` or `STOP_FOR_REPAIR`; never fill a field
from assumption. Freeze this document before outcome-aware modelling/protected-test access and preserve
all later versions.

## 1. Document control

| Field | Value |
|---|---|
| Protocol title / short title | [AUTHOR_INPUT_NEEDED] |
| Protocol ID / version / date | [AUTHOR_INPUT_NEEDED] |
| Study owner / sponsor / sites | [AUTHOR_INPUT_NEEDED] |
| Study family / task contract(s) | [AUTHOR_INPUT_NEEDED] |
| Registration platform / ID / public link | NOT_VERIFIED |
| Registration status | PROSPECTIVE / RETROSPECTIVE / UNREGISTERED / NOT_APPLICABLE / NOT_VERIFIED |
| Ethics/consent/waiver ID and state | NOT_VERIFIED |
| Data-use/access authority | NOT_VERIFIED |
| SAP locator / version / date | [AUTHOR_INPUT_NEEDED] |
| Protocol freeze date / digest / approver roles | [AUTHOR_INPUT_NEEDED] |
| Outcome/test-access state at freeze | [AUTHOR_INPUT_NEEDED] |
| Reporting/registry requirements verified on | [AUTHOR_INPUT_NEEDED] |

## 2. Rationale and decision

- Clinical/scientific problem and current pathway:
- Evidence gap and why this study can resolve it:
- Decision the result should inform:
- Intended users and moment of use:
- Minimum defensible claim:
- Explicitly forbidden stronger claim:

## 3. Question–estimand card

| Field | Frozen specification |
|---|---|
| Population / setting / pathway | [AUTHOR_INPUT_NEEDED] |
| Index test / exposure / intervention | [AUTHOR_INPUT_NEEDED] |
| Comparator | [AUTHOR_INPUT_NEEDED] |
| Outcome / target condition / measurement | [AUTHOR_INPUT_NEEDED] |
| Time zero / predictor time / horizon | [AUTHOR_INPUT_NEEDED] |
| Primary independent unit and hierarchy | [AUTHOR_INPUT_NEEDED] |
| Primary estimand / contrast | [AUTHOR_INPUT_NEEDED] |
| Intended action / threshold / margin | [AUTHOR_INPUT_NEEDED] |
| Primary hypothesis and success criterion | [AUTHOR_INPUT_NEEDED] |
| Claim branch / ceiling | [AUTHOR_INPUT_NEEDED] |

Attached task contract(s) and version:

## 4. Study design and setting

- Prospective/retrospective; observational/interventional:
- Exact design: cohort / cross-sectional / case-control / reader / randomized / cluster / ITS / other:
- Sites, care levels, geography and calendar period:
- Recruitment/export pathway and sampling method:
- Study start, expected end and analysis-freeze milestones:
- Concurrent workflow/policy/technology changes to track:

## 5. Participants, cohort and information flow

### Eligibility

| Dimension | Include | Exclude | Rationale / observable before outcome? |
|---|---|---|---|
| Patient/pathway |  |  |  |
| Index examination/time |  |  |  |
| Modality/series/protocol |  |  |  |
| Reference/outcome availability |  |  |  |
| Prior treatment/intervention |  |  |  |
| Technical quality |  |  |  |

- Sampling frame and target-population relationship:
- Expected prevalence/events/transitions and provenance:
- Patient–exam–series–lesion–report–timepoint ID scheme:
- Duplicate/overlap/public-dataset contamination audit:
- Screening/exclusion/non-evaluable flow source:
- Development, test and analysis populations:

## 6. Imaging acquisition, reconstruction and technical QC

| Field | Frozen specification / evidence locator |
|---|---|
| Modality, anatomy and views/sequences/phases | [AUTHOR_INPUT_NEEDED] |
| Series-selection rule | [AUTHOR_INPUT_NEEDED] |
| Scanner/vendor/site/protocol ranges | [AUTHOR_INPUT_NEEDED] |
| Acquisition/reconstruction/contrast/dose/count details | [AUTHOR_INPUT_NEEDED] |
| Raw and derived format/provenance | [AUTHOR_INPUT_NEEDED] |
| Image-quality acceptance and failure rule | [AUTHOR_INPUT_NEEDED] |
| Registration/resampling/interpolation | [AUTHOR_INPUT_NEEDED] |
| Protocol-deviation manifest | [AUTHOR_INPUT_NEEDED] |
| Physics/technical conformance review | NOT_VERIFIED |

## 7. Reference standard, annotation and longitudinal linkage

- Target construct, ontology and label unit:
- Reference source, timing and rationale:
- Reader/annotator number, expertise and training/calibration:
- Blinding and information available:
- Independent reads, consensus/adjudication and disagreement preservation:
- Uncertain, indeterminate, absent and non-evaluable states:
- Model-assisted/report-derived/weak-label provenance and clean-reference evaluation:
- Mask geometry and DICOM frame-of-reference receipt:
- Longitudinal lesion/exam linking and split/merge/new-lesion rules:
- Inter-/intra-reader repeatability/reproducibility plan:

## 8. Index test, model/intervention and comparators

- Exact algorithm/test/intervention and version:
- Inputs available at the intended moment:
- Output, threshold, abstention/failure and fallback:
- Architecture/modeling route and simple baseline:
- Clinical/technical comparator and version:
- Training/tuning/stopping rule:
- Model/prompt/retrieval/checkpoint/configuration manifest:
- Allowed adaptation/update and change-control rule:

## 9. Partition and protected-access plan

| Partition | Unit/grouping | Site/time role | Intended use | Who may access labels/results | Frozen locator/digest |
|---|---|---|---|---|---|
| Development |  |  | train/tune/internal resampling |  |  |
| Validation |  |  | threshold/model selection |  |  |
| Protected test |  |  | one frozen evaluation |  |  |
| External/prospective |  |  | transport/impact |  |  |

- Patient/family/repeat/lesion/timepoint grouping:
- Split-generation code/seed and overlap tests:
- Data-dependent steps fitted inside development only:
- Test-access event log and permitted diagnostics:
- Consequence of test access or adaptation:

## 10. Outcomes and analysis intent

| Role | Outcome/estimand | Unit | Horizon/threshold/margin | Measure + CI | Success criterion |
|---|---|---|---|---|---|
| Primary | [AUTHOR_INPUT_NEEDED] |  |  |  |  |
| Secondary |  |  |  |  |  |
| Exploratory |  |  |  |  | hypothesis-generating only |
| Safety/failure |  |  |  |  |  |

- Clustering/repeated-measure/reader-case structure:
- Missing, indeterminate, non-evaluable and exclusion strategy:
- Multiplicity and subgroup/fairness family:
- Calibration/decision utility where applicable:
- Sensitivity, negative-control and falsification plan:
- SAP locator and unresolved biostatistics gate:

## 11. Sample size / information size

- Design objective: power / precision / model-development stability / feasibility:
- Primary estimand and planned analysis:
- Effect worth detecting, margin or interval target and rationale:
- Prevalence/event rate/variance/correlation/censoring inputs and sources:
- Site/reader/cluster/repeated-measure structure:
- Missing/non-evaluable/attrition allowance:
- Scenario range and required versus feasible independent units:
- Calculation/simulation method, software/version and reviewer:
- Unresolved inputs: [AUTHOR_INPUT_NEEDED / BIOSTATISTICIAN_REQUIRED]

## 12. Bias, validation and failure controls

| Threat | Prevention/diagnostic | Failure signal | Prespecified response | Surviving claim |
|---|---|---|---|---|
| selection/spectrum |  |  |  |  |
| verification/reference |  |  |  |  |
| patient/test leakage |  |  |  |  |
| site/scanner/protocol shift |  |  |  |  |
| missing/non-evaluable data |  |  |  |  |
| measurement/annotation error |  |  |  |  |
| multiplicity/overfitting |  |  |  |  |
| workflow/human-factor failure |  |  |  |  |

## 13. Ethics, safety, privacy and governance

- Ethics/IRB and consent/waiver evidence:
- Secondary use, data/model-provider transfer and agreements:
- De-identification/linkage-key and re-identification risk:
- Incidental findings/critical results/adverse event process:
- Clinical override, abstention and fallback:
- Participant/reader burden and compensation:
- Security/access roles, retention and destruction/archive policy:
- Funding, conflicts, sponsor/model-provider role:
- Patient/public involvement and accessibility/equity plan:

## 14. Reproducibility, dissemination and reporting

- Repository, commit and license:
- Environment/container, hardware, config, commands and seeds:
- Input/output schema, cohort/split manifest and tests/CI:
- Data/model card, weights and access boundary:
- Negative/failure/deviation preservation:
- Reporting-guideline stack and live verification date:
- Publication, protocol/SAP, code/data/results and negative-result plan:
- Long-term owner and archive/replay check:

## 15. Amendments and deviations

| ID | Date | Protocol field | Old | New | Reason | Result-aware? | Affected estimand/output | Disclosure |
|---|---|---|---|---|---|---|---|---|
| A-001 |  |  |  |  |  | yes / no / unknown |  |  |

## 16. Decisions and unresolved inputs

| ID | Question/input | Options/tradeoff | State | Evidence/owner | Due before | Consequence if unresolved |
|---|---|---|---|---|---|---|
| D-001 |  |  | [AUTHOR_INPUT_NEEDED] |  | freeze / execute / test / report |  |
