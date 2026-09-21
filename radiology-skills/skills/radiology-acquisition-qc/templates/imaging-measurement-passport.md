# Imaging measurement passport

Use this artifact only for a requested persistent record or full audit. Keep unknown facts as
`AUTHOR_INPUT_NEEDED`. A plausible scanner default is not evidence.

## Identity and evidence

| Field | Value |
|---|---|
| Passport ID / version / date | [AUTHOR_INPUT_NEEDED] |
| Study / cohort / site | [AUTHOR_INPUT_NEEDED] |
| Producer / verifier role | [AUTHOR_INPUT_NEEDED] |
| Mode | [plan / audit / mentor / interpret / writing-handoff] |
| Evidence state | [AUTHOR_REPORTED / ARTIFACT_VERIFIED / COMPUTED / NOT_ASSESSABLE] |
| Source artifacts and immutable locators | [AUTHOR_INPUT_NEEDED] |

## Measurement claim

| Field | Value |
|---|---|
| Clinical/research question handoff | [AUTHOR_INPUT_NEEDED] |
| Modality and subtype | [CT / MRI / PET / SPECT / US / CEUS / elastography / radiography / mammography / DBT / hybrid] |
| Measurement object | [AUTHOR_INPUT_NEEDED] |
| Intended claim | [visual adequacy / relative signal / absolute quantity / longitudinal change / cross-site comparability / reconstruction gain / downstream input fitness] |
| Unit and scale | [AUTHOR_INPUT_NEEDED] |
| Intended population, setting and time point | [AUTHOR_INPUT_NEEDED] |
| Maximum wording requested | [AUTHOR_INPUT_NEEDED] |

## Hierarchy and object lock

`patient -> examination/time point -> series/acquisition -> reconstruction/derived object ->
view/frame/slice/voxel/measurement`

| Object | Stable ID/hash | Role | Included? | Reason fixed before result review? | Evidence |
|---|---|---|---|---|---|
| [AUTHOR_INPUT_NEEDED] | | [primary / sensitivity / excluded] | | | |

Record multi-lesion, repeated-scan, paired-view, multi-sequence, hybrid and longitudinal nesting.

## Coverage and disposition denominators

Use one explicit flow at each declared grain:

`eligible -> acquired -> exported/received -> QC assessed -> accepted | nondiagnostic | excluded | unresolved`

Acquired and exported/received are flow stages, not final mutually exclusive outcomes. The final
disposition categories must reconcile to the QC-assessed denominator. Never report only accepted
objects or silently drop failed, missing or nondiagnostic acquisitions.

| Stage/disposition | Grain (patient/exam/series/object) | Count | Reason categories and counts | Evidence/query locator |
|---|---|---:|---|---|
| Eligible | [AUTHOR_INPUT_NEEDED] | [AUTHOR_INPUT_NEEDED] | eligibility window and source population | [AUTHOR_INPUT_NEEDED] |
| Acquired | [AUTHOR_INPUT_NEEDED] | [AUTHOR_INPUT_NEEDED] | not acquired: refusal / cancellation / contraindication / technical or other prespecified reason | [AUTHOR_INPUT_NEEDED] |
| Exported/received | [AUTHOR_INPUT_NEEDED] | [AUTHOR_INPUT_NEEDED] | not exported/received: transfer, archive, format or availability failure | [AUTHOR_INPUT_NEEDED] |
| QC assessed | [AUTHOR_INPUT_NEEDED] | [AUTHOR_INPUT_NEEDED] | not assessable: corrupt, incomplete or missing decisive provenance | [AUTHOR_INPUT_NEEDED] |
| Accepted | [AUTHOR_INPUT_NEEDED] | [AUTHOR_INPUT_NEEDED] | meets prespecified input/QC rule | [AUTHOR_INPUT_NEEDED] |
| Nondiagnostic | [AUTHOR_INPUT_NEEDED] | [AUTHOR_INPUT_NEEDED] | artifact/coverage/contrast/count/signal or modality-specific reason | [AUTHOR_INPUT_NEEDED] |
| Excluded | [AUTHOR_INPUT_NEEDED] | [AUTHOR_INPUT_NEEDED] | prespecified scientific or technical exclusion reason | [AUTHOR_INPUT_NEEDED] |
| Unresolved | [AUTHOR_INPUT_NEEDED] | [AUTHOR_INPUT_NEEDED] | pending adjudication or missing evidence | [AUTHOR_INPUT_NEEDED] |

Reconcile counts without mixing grains. If one patient contributes multiple examinations or series,
report both the patient denominator and the lower-level object denominator. Preserve every exclusion
reason and whether it arose before acquisition, during transfer, at QC or after the series rule was
applied; do not convert a measurement failure into an eligibility exclusion.

## Acquisition

| Field | Value / evidence locator |
|---|---|
| Vendor, model, hardware and software version | [AUTHOR_INPUT_NEEDED] |
| Protocol/preset name and version | [AUTHOR_INPUT_NEEDED] |
| Modality-specific acquisition settings | [AUTHOR_INPUT_NEEDED] |
| Contrast/tracer/exposure and timing | [AUTHOR_INPUT_NEEDED / NOT_APPLICABLE] |
| Positioning, motion control and operator factors | [AUTHOR_INPUT_NEEDED] |
| Acquisition deviations and service/upgrades | [AUTHOR_INPUT_NEEDED] |

## Reconstruction and post-processing

| Field | Value / evidence locator |
|---|---|
| Reconstruction family/version and parameters | [AUTHOR_INPUT_NEEDED] |
| Geometry, spacing/thickness/increment/view/frame handling | [AUTHOR_INPUT_NEEDED] |
| Corrections, filters, normalization or derived-map algorithm | [AUTHOR_INPUT_NEEDED] |
| Quantitative scaling, units and reference | [AUTHOR_INPUT_NEEDED] |
| Display-only versus analysis pixels | [AUTHOR_INPUT_NEEDED] |
| Alternative reconstructions and selection rule | [AUTHOR_INPUT_NEEDED] |

## QC, artifacts, and disposition

| QC/artifact ID | Object/level | Expected measurement effect | Detection evidence | Disposition | Residual risk |
|---|---|---|---|---|---|
| [AUTHOR_INPUT_NEEDED] | | | | [retain / exclude / stratify / sensitivity / reacquire-not-authorized] | |

## Repeatability and protocol shift

| Field | Value |
|---|---|
| Claim needs phantom/test-retest evidence? | [yes / no + rationale] |
| Phantom/reference object and traceability | [AUTHOR_INPUT_NEEDED / NOT_APPLICABLE] |
| Test-retest interval, repositioning and stability argument | [AUTHOR_INPUT_NEEDED / NOT_APPLICABLE] |
| Repeatability statistic, uncertainty and prespecified criterion | [AUTHOR_INPUT_NEEDED / NOT_COMPUTED] |
| Site/vendor/model/software/protocol shift ledger | [AUTHOR_INPUT_NEEDED] |
| Represented versus wholly unseen levels | [AUTHOR_INPUT_NEEDED] |
| Raw/frozen primary evaluation | [AUTHOR_INPUT_NEEDED] |
| Harmonisation/adaptation fit scope and external-data access | [AUTHOR_INPUT_NEEDED / NOT_APPLICABLE] |

## Standards and source ledger

| Source ID | Authority | Exact title/version/date | Applicability | Canonical URL | Retrieved artifact/hash/locator | State |
|---|---|---|---|---|---|---|
| [AUTHOR_INPUT_NEEDED] | | | | | | [SOURCE_VERIFIED / LIVE_VERIFICATION_REQUIRED / NOT_APPLICABLE] |

Do not claim profile/standard conformance from a landing page alone. Verify the exact version,
applicable claim and required conformance evidence.

## Verdict and handoff

| Field | Value |
|---|---|
| Measurement verdict | [PASS / CONDITIONAL / STOP] |
| Allowed wording | [AUTHOR_INPUT_NEEDED] |
| Prohibited upgrade | [AUTHOR_INPUT_NEEDED] |
| Smallest decision-bearing next action | [AUTHOR_INPUT_NEEDED] |
| Receiving owner and artifact | [AUTHOR_INPUT_NEEDED] |
| Unresolved assumptions | [AUTHOR_INPUT_NEEDED] |
| Learner fields, if applicable | [learning objective / baseline attempt / misconception / evidence of understanding / next transfer task] |
