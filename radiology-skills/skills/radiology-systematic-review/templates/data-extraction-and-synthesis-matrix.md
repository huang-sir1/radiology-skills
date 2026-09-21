# Data extraction and synthesis matrix

Keep report-level metadata, study-family identity and effect-level rows separate. One paper may
contain several eligible effects; several papers may describe one study. Never treat either as
automatic independent evidence.

## A. Report and study-family index

| Report ID | Study-family ID | Citation/identifier verification state | Report type | Cohort/site/dates | Overlap evidence | Primary report? | Source location | Extractor/verifier | Query status |
|---|---|---|---|---|---|---|---|---|---|
| R-001 | S-001 | NOT_VERIFIED |  |  |  | yes / no / unclear |  |  | open / resolved |

## B. Study, population and design

| Study-family ID | Design | Country/setting | Inclusion/exclusion | N enrolled/analyzed | Events/target-positive | Age/sex and key spectrum | Treatment/time context | Recruitment | Follow-up | Funding/conflicts |
|---|---|---|---|---|---|---|---|---|---|---|
| S-001 |  |  |  |  |  |  |  | consecutive / random / convenience / unclear |  |  |

## C. Imaging, AI, radiomics, DTA and prediction fields

| Study-family ID | Modality/protocol | Intended use/task | Index/model/version | Development or validation type | Split and test isolation | Reference standard/outcome/horizon | Threshold | Patient/lesion/reader unit | Discrimination | Calibration | Clinical utility | Leakage/applicability note |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| S-001 |  |  |  |  |  |  |  |  |  |  |  |  |

For DTA, also capture the 2 × 2 counts or reconstructability, paired sensitivity/specificity,
prevalence/spectrum, uninterpretable tests, reference-standard blinding, flow/timing and threshold
status. For model evidence, keep development, internal validation and external validation distinct.

## D. Intervention and prognosis fields

| Study-family ID | Exposure/intervention and comparator | Assignment/confounding | Contrast/scale | Outcome and horizon | Adjusted? and covariates | Censoring/competing events | Adherence/crossover | Cluster/multi-arm structure | Harms |
|---|---|---|---|---|---|---|---|---|---|
| S-001 |  |  |  |  |  |  |  |  |  |

## E. Prevalence, incidence and observational-association fields

| Study-family ID | Quantity: prevalence/incidence/association | Population/sampling frame and period | Condition/event/exposure/outcome definitions | Numerator and analyzed/eligible denominator or person-time | Exposure contrast / time order | Sampling/recruitment/non-response | Effect estimate and exact scale | Adjusted? and covariates | Unit/clustering/repeats | Missing/zero-event handling | Precision/source |
|---|---|---|---|---|---|---|---|---|---|---|---|
| S-001 |  |  |  |  |  |  |  |  |  |  |  |

Keep point/period/lifetime prevalence, cumulative incidence, incidence rate and observational
association separate. Never reconstruct person-time, denominators, contrasts or adjustment from an
unverified assumption.

## F. Reliability, agreement and method-comparison fields

| Study-family ID | Construct/question | Object/subjects and sampling | Methods/devices/readers/raters | Repeats/conditions/interval/blinding | Independent unit and hierarchy | Exact metric definition/model/type/form/weighting | Threshold/range | Estimate and uncertainty | Direction convention | Missing/uninterpretable/exclusions | Shared subjects/readers/multiple metrics dependence | Applicability |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| S-001 | repeatability / reproducibility / reliability / categorical agreement / quantitative agreement / segmentation overlap / method difference |  |  |  |  |  |  |  |  |  |  |  |

Correlation is not agreement. Record the exact ICC model/type/form, kappa weighting, overlap-metric
variant, repeatability formulation, or bias/limits-of-agreement definition instead of extracting an
unspecified headline value. Classification against a target-condition reference belongs in the DTA
branch.

## G. Omics, spatial and mechanism fields

| Study-family ID | Tissue/disease/treatment/time | Assay/platform | Measured or inferred | Patient/donor/sample/cell/spot n | Matched across modalities? | Preprocessing/batch/composition | Contrast/readout | Multiplicity | Spatial/temporal scale | Perturbation/target engagement/rescue | External biological validation |
|---|---|---|---|---|---|---|---|---|---|---|---|
| S-001 |  |  | measured / inferred / generated |  |  |  |  |  |  |  |  |

## H. Effect-level rows for synthesis handoff

| Effect ID | Study-family ID | Report/source anchor | Synthesis group | Endpoint/target and horizon/period | Population/contrast | Effect estimate | Scale/transformation or exact metric definition/model/form | SE/CI/raw data | Numerator/denominator/person-time if relevant | Direction convention | Adjusted class | Independent unit | Reader/device/repeat/cluster/dependence/shared comparator | Threshold | RoB/applicability state | Include in primary? |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| E-001 | S-001 |  |  |  |  |  |  |  |  |  |  | patient / donor / lesion / object / other |  |  |  | yes / subgroup / sensitivity / no |

## I. Pooling-feasibility matrix

| Candidate group | Common estimand? | Population/setting | Design/validation type | Index/exposure/intervention/model/method | Comparator/reference | Outcome/horizon/period | Effect/threshold/exact metric form | Unit/reader/device/repeat/dependence | Overlap resolved? | RoB pattern | Decision and rationale |
|---|---|---|---|---|---|---|---|---|---|---|---|
| G-001 | yes / no / unclear | compatible? | compatible? | compatible? | compatible? | compatible? | compatible? | compatible? | yes / no |  | POOL / STRATIFY / NARRATIVE / STOP_FOR_REPAIR |

## J. Narrative/convergence synthesis

| Synthesis group | Study-family IDs | Effect direction | Magnitude/precision pattern | Bias/applicability pattern | Concordance | Discordance explanation | Measured/inferred and matchedness | Supported claim | Claim ceiling |
|---|---|---|---|---|---|---|---|---|---|
| N-001 |  |  |  |  |  |  |  |  |  |

## K. Missingness and data-query ledger

| Query ID | Study/Effect ID | Missing or conflicting field | Why decision-bearing | Source checked | Author contact/status | Resolution | Synthesis consequence |
|---|---|---|---|---|---|---|---|
| Q-001 |  |  |  |  |  | OPEN |  |

## L. Statistical handoff receipt

- Eligible Effect IDs:
- Excluded/held-out Effect IDs and reasons:
- Independent unit and dependence/covariance:
- Numerator/denominator/person-time or reader/device/repeat structure, if relevant:
- Direction and transformations:
- Exact reliability/agreement metric definition/model/type/form/weighting, if relevant:
- Prespecified model candidate:
- Heterogeneity outputs required:
- Subgroup/meta-regression hypotheses and multiplicity family:
- Sensitivity/influence analyses:
- Small-study/reporting-bias assessment conditions:
- Evidence-state boundary: PLANNED / AUTHOR_REPORTED / PARTLY_VERIFIED / VERIFIED / NOT_ASSESSABLE
