# Assay and control matrix

Use this matrix to bind every assay or system to its scientific job, control, unit, failure signal
and claim ceiling. It is not a reagent recipe. Exact antibodies, clones, guide sequences, doses,
incubations, instruments and thresholds require source-backed local validation.

## Universal control taxonomy

| Control class | Question answered | Common misuse |
|---|---|---|
| baseline/untreated | what changes without the active intervention? | confused with vehicle when handling differs |
| vehicle/vector/mock/sham | is delivery or procedure responsible? | omitted because vehicle appears "inert" |
| negative assay | is signal non-specific or background? | treated as biological negative without validation |
| positive assay | can the assay detect an expected state? | used as evidence that the experimental sample engaged the target |
| batch/bridge sample | can runs, plates, blocks or sections be compared? | batch corrected after outcome inspection without bridge evidence |
| viability/toxicity/stress | is phenotype a non-specific consequence? | measured at an irrelevant time or with the same readout as phenotype |
| independent perturbation | is effect specific to target/process? | two reagents with the same off-target profile called orthogonal |
| rescue/reversal | does restoring/bypassing the target reverse the effect? | rescue itself changes baseline or exposure and is not controlled |
| model/donor replication | does the effect persist across context? | wells/passages from one source called independent donors |

## System-specific design matrix

| System/assay | Scientific job | Required design checks | Core controls | Independent unit | Failure signal / interpretation |
|---|---|---|---|---|---|
| IHC | localize or quantify marker in tissue | antigen/assay validity, pre-analytics, ROI sampling, scoring rule, saturation, reader blinding, block/section hierarchy | positive/negative tissue, isotype or validated negative where applicable, batch/bridge control | usually patient/specimen for human claims | signal tracks batch/necrosis or disappears under validated negative control -> technical/composition alternative remains |
| multiplex IF | test spatial/cellular colocalization or phenotype | panel interference, bleed-through, autofluorescence, segmentation/phenotyping, registration, cell/ROI-to-patient aggregation | single-stain controls, no-primary/negative, bridge tissue, segmentation QC | patient/donor, not cells | colocalization without spatial null or patient aggregation -> association only |
| RNA/protein tissue assay | measure abundance or activation state | tissue provenance/purity, pre-analytics, reference/normalization, dynamic range, non-detects, composition | reference/control material, batch bridge, negative/positive assay controls | patient/donor/specimen as designed | bulk change may reflect composition; activation cannot be inferred from abundance alone |
| cell line | tractable perturbation-response | identity, contamination status, passage/context, target presence, culture/batch, model diversity | untreated, vehicle/vector/mock, non-targeting, viability, positive assay | independently treated culture/experiment, depending allocation | effect confined to one model/batch -> context-limited, not general mechanism |
| organoid/ex vivo | donor-context perturbation | derivation success, selection bias, passage, cellular composition, matched donor, culture state | matched untreated/vehicle, viability, derivation/batch bridge, donor replication | donor-derived line/organoid unit as allocated, not organoids by default | differential establishment/attrition correlated with condition -> selection threat |
| animal model | systemic/temporal mechanism | model relevance, allocation, cage/litter/sex/age, randomization, blinding, welfare endpoint, attrition | sham/vehicle, positive where justified, toxicity/welfare, batch/cohort | animal or cluster actually randomized | differential attrition or unblinded endpoint -> causal estimate compromised |
| genetic loss/gain | necessity or sufficiency in model | target expression, guide/construct validity, delivery, editing/knockdown at RNA/protein/function, off-target | non-targeting/empty vector, multiple independent constructs, delivery, viability | independently assigned culture/animal/donor model | phenotype without engagement or with one construct only -> target attribution unsupported |
| pharmacological modulation | exposure-dependent target/pathway test | exposure/selectivity rationale, solubility/delivery, target engagement, dose-time, toxicity | vehicle, exposure control, viability, orthogonal compound or genetic route | independently assigned culture/animal/model | phenotype only near toxicity or without engagement -> non-specific explanation |
| rescue/reversal | strengthen specificity/mediation | rescue expression/exposure, timing, baseline effect, compatibility with perturbation, blinded comparison | perturbation alone, rescue alone, vector/vehicle, wild-type/appropriate mutant if justified | same valid allocation unit | rescue changes baseline or fails engagement -> rescue is not interpretable |
| imaging-linked assay | reconnect laboratory result to imaging claim | patient/lesion/region/block/section mapping, time/treatment alignment, feature freeze, sampling discordance | mapping QC, negative region/control tissue, sensitivity to aggregation | patient or prespecified matched unit | unmatched or post-selected ROI -> cannot validate imaging-mechanism bridge |

## Replicate and repeat rules

- A **biological replicate** reflects independently arising biological material or an independently
  repeated intervention at the level justified by the design. Define it; do not infer it from labels.
- A **technical replicate** evaluates measurement precision. Average or model its structure; do not
  count it as a new independent unit.
- An **independent repeat** should start early enough in the process to re-expose the relevant sources
  of variation. Re-reading the same plate or re-imaging the same section is not an independent repeat.
- Multiple fields, cells, regions, spots or sections can improve measurement of a biological unit but
  do not automatically increase biological degrees of freedom.
- Donors, animals or batches excluded after outcome inspection require explicit provenance and
  sensitivity analysis; hidden exclusions are unacceptable.

## Randomization, blocking and blinding

Randomize at the unit receiving the intervention. Block only on prespecified factors needed for
balance or logistics, and preserve block in analysis. When full randomization is impossible, document
allocation, reason, likely confounding and a repair/limitation.

Blind intervention labels during endpoint acquisition, image selection, ROI definition, scoring and
primary analysis wherever feasible. If blinding is impossible, use objective acquisition/selection
rules, independent verification and explicit limitation language.

## Target engagement and phenotype are separate

| Layer | Example job | Requirement |
|---|---|---|
| delivery/exposure | construct/reagent reached the system | evidence at the relevant compartment/time |
| molecular engagement | target abundance/activity changed | readout distinct from the desired phenotype where possible |
| pathway engagement | downstream mediator changed as predicted | temporal and directional coherence; alternatives considered |
| phenotype | functional/cellular/tissue consequence | prespecified endpoint at the valid unit |
| specificity | effect tracks target rather than artifact | independent perturbation, rescue or orthogonal evidence |

A phenotype without engagement cannot be attributed to the intended target. Engagement without a
phenotype is evidence about intervention biology, not a successful phenotypic mechanism.

## Assay performance checks

For any quantitative assay, document:

- analyte/object definition and intended measurement range;
- sample handling and pre-analytic conditions;
- specificity, sensitivity/detection limit and saturation where relevant;
- calibration/reference/normalization and between-run bridging;
- repeatability and reproducibility at the intended decision threshold;
- missing/non-detect handling and QC failure criteria;
- operator, software/algorithm, version and locked scoring/segmentation rule;
- raw data and source-image retention.

Hand detailed assay-performance and alternative-method evaluation to
`radiology-method-evaluation`; hand inferential calculations to `radiology-stats`.

## Constructive audit output

For each finding, return:

`evidence anchor -> threatened explanation -> criterion -> severity -> minimum repair -> stronger
route and cost -> closure evidence -> surviving claim`.

Do not request every conceivable control. Prioritize controls that could reverse the conclusion or
are needed to distinguish the proposed mechanism from a plausible alternative.
