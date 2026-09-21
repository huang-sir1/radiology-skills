# Radiology–pathology mechanism validation: review and advisory playbook

Use this reference when a radiomic feature, deep imaging embedding, imaging habitat, longitudinal
imaging change, or radiology model is connected to **H&E, FFPE tissue, IHC, multiplex
immunofluorescence (mIF), digital pathology/whole-slide imaging (WSI), or targeted tissue and cell
validation**. It is a bridge playbook: it audits whether pathology supports an imaging mechanism and
helps a learner design the smallest informative tissue study.

Also use [radiomics-mechanism-bridge.md](radiomics-mechanism-bridge.md) for the full
image-to-mechanism chain and
[sample-to-image-mapping.md](sample-to-image-mapping.md) for specimen provenance. When RNA data
are involved, add the relevant bulk, single-cell, or spatial transcriptomics route. This reference
does not replace a pathologist's diagnostic review, a pathology laboratory's assay validation, or
clinical regulatory requirements.

## Scope and routing

Route here when the unresolved link is any of the following:

- whether an imaging phenotype corresponds to viable tumour, necrosis, fibrosis, oedema, vessels,
  stroma, inflammation, immune aggregates, invasive margin, or another tissue architecture;
- whether an image-defined group or habitat differs in a prespecified protein, cell population,
  cell state surrogate, tissue compartment, or spatial neighbourhood;
- whether H&E or WSI can localise the tissue structure that plausibly contributes to an imaging
  contrast;
- whether targeted IHC/mIF provides orthogonal support for a molecular or cellular interpretation;
- whether digital pathology-derived densities, fractions, morphologies, or neighbourhoods are
  technically and statistically credible;
- how to design, analyse, explain, or write a small FFPE validation substudy.

Do **not** use this route alone to answer:

- a clinical diagnosis, grade, stage, margin status, or treatment recommendation;
- whether an antibody or panel is fit for clinical deployment without laboratory validation;
- whether one sampled block represents an entire heterogeneous lesion;
- whether one marker proves a cell identity, activation state, pathway, or causal mechanism;
- whether cross-sectional morphology establishes temporal order, biological function, or causality;
- whether a pathology association makes an imaging model an actionable biomarker;
- whether response under one observed treatment predicts comparative treatment benefit.

When the requested conclusion exceeds the assay, preserve the useful observation and state the
nearest supportable question.

## Two duties: audit and teach

| Mode | Starting material | Required work | Required output |
|---|---|---|---|
| **Review** | Protocol, block list, stained slides, WSI pipeline, tables, figures, or manuscript | Reconstruct provenance, selection, assay, reader/algorithm, inference, and claim; find the first broken link | Severity-ranked findings, `PASS / CONDITIONAL / STOP`, claim ceiling, and exact repairs |
| **Advise** | Imaging result, biological idea, available FFPE, or a learner's question | Generate competing tissue explanations; identify the observation that separates them; compare feasible assays and designs | Mechanism question tree, conservative/standard/ambitious plans, controls, and next executable step |
| **Combined** | Incomplete study needing interpretation and rescue | Audit existing evidence before proposing new work | Preserved findings, blocked claims, repair plan, and revised wording |

For every criticism or recommendation, give:

1. **Principle** — why the issue matters.
2. **Consequence** — which estimate or claim is affected.
3. **Options** — at least two routes when a real trade-off exists.
4. **Next action** — the smallest useful action the learner can take now.

Do not merely say “add pathology” or “validate by IHC.” Name the target tissue feature, sampling
frame, assay, controls, independent unit, analysis, and claim it could support.

## Evidence-language contract

Keep observation, measurement, computation, and inference distinct in every table, figure, and
sentence.

| Evidence layer | Defensible wording | Prohibited upgrade |
|---|---|---|
| H&E | morphology or tissue architecture was **observed/annotated** on the examined section | a protein, pathway, molecular state, or whole-lesion property was measured |
| IHC/mIF signal | assay signal for a declared marker was **measured/detected** under stated controls | the marker alone proves a cell state, pathway activity, interaction, or function |
| Pathologist score | a prespecified feature was **scored/graded** with declared readers and agreement | an unblinded score is automatically ground truth |
| Digital pathology | tissue, cells, phenotypes, or neighbourhoods were **segmented/classified/estimated** by a validated algorithm | algorithmic output is a direct biological measurement or universally correct label |
| Cross-modal comparison | an imaging phenotype was **associated/concordant** with a pathology endpoint | pathology caused the imaging feature or established mechanism |
| Intervention/orthogonal evidence | a defined experiment **supported** a directional mechanistic link in the tested system | universal causality across patients, lesions, platforms, or treatments |

Use “pathology ground truth” only for a narrowly defined endpoint supported by an appropriate
reference standard, blinded expert annotation or consensus, and documented uncertainty. H&E is not
ground truth for an unobserved pathway; IHC positivity is not ground truth for a complex cell state.

## Input contract

Build this contract before judging results. Mark each item `known`, `derived`,
`missing-but-noncritical`, or `blocking`; do not infer it from filenames or representative images.

| Domain | Required fields | Blocking or claim-limiting examples |
|---|---|---|
| Question | imaging phenotype, biological alternative hypotheses, contrast, endpoint, intended claim, discovery versus validation | “explain texture” with no defined feature, ROI, or competing explanation |
| Biological hierarchy | patient, lesion, procedure, specimen, block, section, ROI/field, cell; paired/repeated status | fields or cells cannot be linked to patients; lesions pooled without patient clustering |
| Imaging | modality/sequence/tracer, scan date, acquisition/reconstruction, ROI, feature/embedding/habitat definition, stability | phenotype cannot be reproduced or is dominated by scanner/site |
| Tissue provenance | biopsy/resection, anatomical site, orientation/grossing map, block ID, section depth, tumour content, image-to-block mapping | wrong lesion, unverifiable specimen, or no mapping for a regional claim |
| Time/treatment | scan, biopsy/resection and staining dates; interval; intervening systemic therapy, radiation, steroids, surgery or sampling | treatment or long interval makes contemporaneous biology uninterpretable |
| Preanalytics | cold/warm ischaemia, fixation delay/type/duration, decalcification, processing, block age/storage, section thickness/age/storage, staining batch | condition perfectly confounded with fixation, block age, or staining batch |
| Assay | H&E/IHC/mIF platform, marker target, clone, lot, dilution, retrieval, detection, controls, panel/phenotype rule | marker identity or controls unavailable; batch-specific threshold defines the result |
| Reader | pathologist role, number, training/calibration, region definition, blinding, repeat reads, disagreement resolution | reader knows imaging/outcome group while defining or scoring the primary endpoint |
| WSI pipeline | scanner, magnification/resolution, file format, QC, colour handling, tissue/cell segmentation, phenotype model, version, thresholds | unreviewed segmentation or outcome-tuned model produces the endpoint |
| Analysis | estimand, patient-level sample size, nesting, covariates, missingness, multiplicity, uncertainty, sensitivity analyses | cells/fields counted as independent patients; result-dependent ROI selection |
| Validation | discovery/held-out status, cohort overlap, locked assay/model/cutoff, independent site/cohort, orthogonal/functional evidence | same exploratory subset relabelled as external validation |

## Specimen, block, and section selection

### Define the sampling frame before seeing the result

Specify the eligible patients, lesions, procedures, blocks, and tissue-quality criteria before
examining the image–pathology association. Selection may be based on prespecified clinical and
technical eligibility, not on which slide best supports the desired mechanism.

A defensible selection record includes:

- all eligible patients and the reason each was included or excluded;
- whether tissue availability depends on outcome, treatment, tumour size, resectability, site, or
  image phenotype;
- whether a biopsy or resection was used and what lesion fraction it plausibly samples;
- all available blocks per lesion and the rule used to select blocks;
- whether tumour centre, invasive margin, peritumoural tissue, necrotic area, or image habitat was
  targeted;
- section level, serial-section distance, recut history, thickness, tissue loss, folds, and usable
  area;
- whether the primary ROI was fixed before marker results and whether any regions were replaced.

Prefer systematic, random, or explicitly stratified block/ROI sampling over choosing a visually
interesting or strongly stained field. Image-guided sampling is acceptable when it is the declared
design, but it must include a traceable coordinate chain, a prespecified matching rule, and a
neutral/comparator region when the question requires a contrast.

### Avoid result-dependent selection

`STOP` the confirmatory claim when blocks, fields, positivity thresholds, or representative images
were selected after viewing both the imaging phenotype and marker result, unless an untouched
validation set repeats the locked procedure. If selection cannot be reconstructed, downgrade the
work to illustrative or hypothesis-generating evidence.

Do not hide the following substitutions:

- using the block with the most tumour after the prespecified block was inadequate;
- excluding low-staining slides only from one imaging group;
- replacing a discordant ROI with a more visually concordant field;
- showing a representative image chosen from the strongest responder without a declared rule;
- using adjacent sections as though the same cells were measured.

### Same block is not the same tissue

Serial H&E, IHC, and mIF sections are related but not identical. Record section order and distance;
explain tissue disappearance, folding, and compartment shifts. A same-block comparison supports
approximate regional concordance, not exact single-cell colocalisation, unless the assay and
registration genuinely preserve that relation.

## FFPE and preanalytical audit

Create a specimen ledger at patient–lesion–block–section level. At minimum review:

| Stage | Record and inspect | Why it matters |
|---|---|---|
| Collection | specimen type, anatomical source, collection time, warm/cold ischaemia, handling, transport | morphology, antigenicity, nucleic acids, and cell integrity can change before fixation |
| Fixation | fixative, concentration/pH if available, delay, duration, temperature, specimen thickness | under/overfixation and group-specific handling alter staining and molecular recovery |
| Processing | grossing, decalcification, dehydration, embedding, orientation, laboratory/site | decalcification and processing can selectively affect targets and morphology |
| Archive | block age, storage conditions, prior sampling/recuts | older or exhausted blocks may differ in available tissue and antigenicity |
| Section | cut date, thickness, depth/order, charged slide, storage duration/conditions | section age and depth affect signal and cross-section correspondence |
| Staining | date, platform, run/batch, reagent lot, retrieval, detection, control tissue | batch and lot effects can mimic a biological group difference |
| Scanning | scanner, objective/effective resolution, calibration, compression, scan date | colour, focus, and spatial measurements depend on acquisition |

Check balance of every preanalytical variable across imaging groups and sites. If a variable is
partly imbalanced, require adjustment or a stratified/batch sensitivity analysis. If biological
condition is completely confounded with fixation, staining batch, scanner, or block age, the
corresponding biological comparison is `STOP` unless independent data break the confounding.

Missing historical fixation metadata does not become “standard fixation.” Label it unknown,
inspect available batch/quality proxies, run sensitivity analyses where possible, and lower the
claim.

## Choose the assay by the unresolved link

| Unresolved question | Most direct feasible route | What it can add | Boundary |
|---|---|---|---|
| What tissue architecture corresponds to the image phenotype? | Blinded H&E annotation/quantification across prespecified compartments | viable tumour, necrosis, fibrosis, vessels, stroma, inflammation, morphology and distribution | does not directly measure a molecular pathway or cell function |
| Is a prespecified protein/cell population enriched? | Validated targeted IHC with morphology-aware scoring | marker signal, positive-cell/tissue fraction, density, intensity, compartment | one marker is rarely sufficient for cell state or pathway activity |
| Are markers co-expressed and cells spatially organised? | mIF with single-stain controls, spectral unmixing, locked phenotype rules and neighbourhood analysis | multiplex phenotype estimates and spatial proximity patterns | proximity is not physical signalling or causal interaction |
| Is a WSI-scale tissue pattern reproducible? | Digital pathology with held-out annotation and patient-level analysis | scalable morphology, tissue/cell estimates and distribution | algorithm error, stain/site shift, and selection remain part of uncertainty |
| Is a transcriptomic interpretation located in tissue? | Region-matched H&E/IHC/mIF or spatial assay, depending on target | orthogonal localisation of selected tissue/cell/protein features | targeted confirmation cannot validate the whole discovery transcriptome |
| Is the mechanism functional or causal? | Perturbation, rescue, longitudinal or functional assay plus tissue evidence | directional support in the tested system | cross-sectional FFPE alone cannot supply this rung |

Assay choice should remove the main ambiguity, not maximise technology. If H&E can distinguish
necrosis from viable tumour, it may be more informative than a broad marker panel. If the ambiguity
is immune-cell composition, targeted mIF may be more efficient than another bulk analysis. If the
claim is exact habitat localisation, patient-matched but unregistered IHC is insufficient even if
the marker is biologically plausible.

## Antibody and marker-panel contract

For each antibody/marker record target, clone, vendor, catalogue number, lot, host/species,
conjugate where relevant, dilution/concentration, incubation, antigen retrieval, platform,
detection chemistry, positivity rule, expected tissue/cellular localisation, and known limitations.

Require controls appropriate to the assay:

- known positive tissue and an interpretable negative tissue or compartment;
- reagent/no-primary or isotype controls when scientifically appropriate, without treating either
  as a universal substitute for biological specificity;
- single-stain controls for multiplex panel development, compensation/spectral-unmixing checks,
  autofluorescence assessment, and spillover review;
- within-run controls and a stable bridging control across staining batches/lots;
- repeat or orthogonal confirmation for an unexpected localisation or critical weak signal;
- predeclared handling of edge artefact, necrosis, pigment, non-specific background and exhausted
  tissue.

Do not infer a complex state from a convenient single marker. A marker may be compatible with
several cell types, activation contexts, subcellular localisations, or technical artefacts. Define
a phenotype with a justified combination of markers, morphology, compartment, intensity/locality,
and an `unclassified/ambiguous` option. Validate the rule against blinded expert review on held-out
fields representing all sites, batches, disease states, and difficult artefacts.

Examples of prohibited shortcuts:

- one immune marker = immune activation;
- one checkpoint marker = pathway activation or treatment sensitivity;
- one proliferation marker = tumour aggressiveness or causal growth driver;
- one stromal marker = a unique fibroblast state;
- marker-positive proximity = ligand–receptor signalling;
- a percentage-positive cutoff optimised on outcome = validated biomarker threshold.

When a pathway or cell state is the target, specify the minimum convergent evidence: multiple
compatible markers, morphology/compartment, an orthogonal RNA or protein readout, or functional
evidence as appropriate. Report what remains unresolved.

## Pathologist review, blinding, and region definitions

Define the pathologist's role before analysis: eligibility confirmation, tumour/compartment
annotation, endpoint scoring, adjudication, algorithm-training annotation, or QC. State whether the
reader was blinded to imaging phenotype, molecular result, outcome, treatment, and algorithm
output. If full blinding is impossible, state what was visible and use an independent blinded read
or sensitivity analysis for the primary endpoint.

Prespecify regions in operational terms. “Tumour,” “margin,” “peritumoural,” “stroma,” “immune
hotspot,” and “necrosis” require boundaries, exclusion rules, minimum area/cell counts, and how
mixed regions are handled. A region name must not acquire the biological meaning being tested.

For subjective or ordinal endpoints:

- train/calibrate readers on examples separate from the primary test set;
- use at least two readers or a justified repeat-read subset when reliability matters;
- report the agreement metric with uncertainty and prevalence context;
- define adjudication without revealing the imaging/outcome group;
- retain disagreement as uncertainty rather than silently replacing it with consensus;
- separate algorithm-training annotations from locked evaluation annotations.

## Digital pathology and WSI pipeline

### Slide and scan QC

Inventory slides before algorithmic analysis. Review tissue completeness, folds, chatter, tears,
bubbles, pen/ink, coverslip artefact, debris, edge effects, staining saturation, uneven illumination,
out-of-focus regions, stitching errors, compression, and missing scan levels. Record whether QC was
manual, automated, or both; keep an exclusion ledger by patient and group.

Scanner/site, magnification, effective pixel size, focus policy, colour profile and file conversion
must be traceable. Do not pool pixel distances or neighbourhood radii across resolutions without
conversion to physical units.

### Colour and batch handling

Measure stain/scanner variation before normalisation. Fit colour normalisation or harmonisation on
training material only, freeze it before validation, and verify that it preserves diagnostically
relevant morphology and marker intensity. Show results with and without normalisation when the
headline depends on colour. Do not allow site or outcome labels to determine the reference slide.

### Tissue and cell segmentation

Validate tissue, compartment, nucleus/cell, and instance segmentation separately when each affects
the endpoint. Include held-out annotations across sites, staining batches, tumour phenotypes,
artefacts, sparse/dense regions, and tissue boundaries. Report task-appropriate performance,
failure modes, and downstream sensitivity to segmentation perturbation; a high average overlap
score can conceal errors at invasive fronts or in crowded cells.

Do not delete difficult cells or regions solely because confidence is low. Use an uncertain class,
manual review rule, or sensitivity bounds. Carry segmentation and classification uncertainty into
cell densities, phenotype fractions, and neighbourhood analyses.

### Phenotypes, density, and neighbourhoods

Lock marker thresholds and phenotype hierarchy before the held-out comparison. Report the tissue
area denominator and compartment; percentages without a defined denominator are uninterpretable.
For spatial analyses, declare coordinate units, search radius or graph rule, edge correction,
minimum cell counts, tissue masks, and the spatial null model.

Neighbourhood and proximity scores depend on density, tissue geometry, segmentation, and the
chosen radius. Compare against within-patient/within-compartment permutations or another justified
spatial null, preserve patient labels, and correct the family of tested cell pairs, radii, and
regions. Describe a compatible spatial organisation, not “cell communication,” unless direct
functional evidence exists.

## Imaging–pathology mapping contract

Build an explicit chain:

```text
patient -> lesion -> imaging time and ROI/habitat -> procedure and orientation
-> gross specimen/block -> section and pathology ROI -> tissue/cell endpoint
```

For each link, record the identifier, method, uncertainty, and exclusions. The claim ceiling follows
the weakest link.

| Available match | Highest usual localisation claim |
|---|---|
| Patient only | patient-level association; not lesion- or region-specific |
| Patient + lesion, no spatial coordinates | lesion/tumour-level concordance; not habitat localisation |
| Lesion + mapped block, approximate orientation | regional support with explicit sampling/registration uncertainty |
| Registered image–gross specimen–slide chain | regional association at declared resolution, after registration sensitivity |
| Same/serial section across assays | section-level colocalisation; serial sections are not identical cells |

Always report the scan-to-tissue interval and intervening treatment. A post-treatment resection
cannot automatically explain a pretreatment imaging phenotype. Biopsy tracks, collapse, resection
deformation, tissue shrinkage, sectioning and registration error must be considered.

Match scales deliberately. A radiology voxel or habitat averages a much larger and different volume
than a cell, field, section, or core. Define how pathology endpoints are aggregated to the imaging
scale, include tissue area/composition, and test plausible registration/aggregation choices. Small
focal pathology cannot be claimed as the source of a whole-lesion feature without a sampling model.

## Statistical contract: the patient remains the inferential unit

Write the hierarchy explicitly:

```text
cells/objects nested in fields or ROIs
-> ROIs nested in sections and blocks
-> blocks nested in lesions
-> lesions nested in patients
```

Cells, tiles, fields, ROIs, serial sections, and technical repeat stains increase measurement
information; they do not create independent patients. The primary analysis should use patient-level
aggregates or a hierarchical/mixed model that preserves patient clustering and the estimand. When
several lesions per patient are included, justify lesion-level inference and cluster or model by
patient.

The analysis contract must specify:

- primary pathology endpoint, direction, compartment, aggregation rule, and denominator;
- image predictor and whether it was selected or trained in the same patients;
- patient-level sample size and matched counts, not only cell/ROI totals;
- covariates chosen from the causal/design question, including relevant site, specimen type,
  treatment, tumour size/stage, and preanalytical batch—not significance screening alone;
- handling of repeated lesions, multiple blocks, missing tissue, failed stains, and below-threshold
  cell counts;
- effect estimate, confidence interval, donor/patient consistency, and influence analysis;
- multiplicity across markers, compartments, cell types, neighbourhoods, radii, imaging features,
  and subgroups;
- train/tuning/test separation for digital pathology models, thresholds, and signatures;
- sensitivity analyses for block/ROI sampling, segmentation/phenotyping, batch, registration,
  tissue area, tumour purity/composition, and influential patients.

Do not call a result robust because thousands of cells yield a small p value. Show patient-level
paired/scatter plots and leave-one-patient-out or influence diagnostics when the cohort is small.
Avoid relying on asymptotic precision with very few clusters; use exact/permutation or cluster-aware
bootstrap procedures only when their assumptions and limited resolution are acknowledged.

### The ten-case FFPE rule

Ten patients with many blocks, ROIs, fields, or cells are still ten independent patients. A
well-controlled 10-case FFPE substudy can provide:

- orthogonal tissue-level concordance;
- feasibility evidence for staining, mapping, or a digital endpoint;
- illustrative localisation;
- an exploratory mechanistic hypothesis and an effect-size estimate with wide uncertainty.

It is **not independent external validation** merely because pathology uses another assay or
because many cells were measured. If the ten cases were selected from the imaging discovery cohort,
describe them as an exploratory or orthogonal subset. Independent external validation requires
non-overlapping patients from an appropriate target population, a locked selection/assay/endpoint/
cutoff/analysis, and no tuning on that cohort. Even when the ten patients are separate, their size
usually supports preliminary replication rather than a stable clinical validation claim.

## Stage-gated decision workflow

Every gate ends in `PASS`, `CONDITIONAL`, or `STOP`. The headline inherits the most restrictive
claim-determining gate; preserve valid subsidiary observations separately.

| Gate | Core question | PASS | CONDITIONAL | STOP examples | Help after verdict |
|---|---|---|---|---|---|
| RP0 — question | What imaging phenotype and tissue mechanism are being tested? | phenotype, alternatives, endpoint, unit, and claim are explicit | exploratory question is bounded | undefined feature or post-hoc single story | build mechanism question tree and falsifiers |
| RP1 — provenance | Is every pathology result linked to patient, lesion, block, section, and time? | complete traceable chain with acceptable interval | patient/lesion match supports only tumour-level claim | wrong/unknown patient or lesion; treatment invalidates contemporaneous claim | mapping table and lower-resolution question |
| RP2 — selection | Were patients, blocks, sections, and ROIs selected independently of the result? | prespecified representative/stratified rule and full ledger | availability sampling is transparent and bias assessed | concordant regions or slides chosen after results | reanalyse all eligible material or label illustrative |
| RP3 — specimen/assay | Are preanalytics, antibody/panel, controls, and batches adequate? | balanced/controlled variables and validated assay | residual batch or archival uncertainty is sensitivity-tested | condition completely confounded with fixation/stain batch; failed controls | batch-balanced repeat, bridging controls, or restricted claim |
| RP4 — reader/algorithm | Are regions and endpoints reproducibly obtained without leakage? | blinded reader or locked held-out algorithm with uncertainty | partial blinding/validation supports bounded use | outcome-informed annotation, test-set tuning, gross segmentation failure | blinded reread, locked evaluation, error/sensitivity audit |
| RP5 — inference | Does analysis respect nesting, selection, confounding, and multiplicity? | patient-aware model, effect/CI, prespecified primary endpoint | small/power-limited but identifiable exploratory estimate | cells/fields as independent n; unrecoverable selective reporting | patient aggregation/hierarchical reanalysis and multiplicity plan |
| RP6 — cross-scale bridge | Do image and tissue refer to compatible region, time, and scale? | mapped evidence and registration/aggregation sensitivity | lesion/patient-level concordance only | unmatched lesion or regional claim from patient-only match | downgrade localisation or obtain mapped tissue |
| RP7 — mechanism/validation | What evidence level is actually reached? | convergent orthogonal/functional evidence supports declared rung | targeted FFPE supports plausibility/concordance | one marker or cross-sectional association claimed causal/external | add orthogonal marker/panel, functional test, or independent locked cohort |
| RP8 — writing/release | Does prose preserve observation, measurement, estimate, and inference? | all sections match provenance and verdict | wording repair is sufficient | predicted/estimated endpoint reported as measured; ten cases called external validation | exact replacement text and claim-evidence table |

### Immediate STOP rules for the mechanistic headline

Stop or downgrade when any remains unresolved:

- tissue cannot be traced to the imaged patient and lesion;
- block, ROI, field, marker, threshold, or representative image was selected to maximise the result;
- imaging group is completely confounded with fixation, staining batch, scanner, or specimen type;
- reader annotation or WSI model uses outcome/group information for the held-out endpoint;
- cells, tiles, fields, or sections are analysed as independent patients;
- one marker is treated as definitive cell state/pathway/function;
- patient-only tissue is used for a habitat-level localisation claim;
- H&E/IHC association is described as causal mechanism;
- same-cohort or overlapping FFPE cases are called independent external validation.

## Advisory workflow: turn an image result into testable tissue hypotheses

### Build a pathology mechanism question tree

Start with the exact imaging phenotype and its physical contrast. Generate at least:

- **architecture hypothesis:** viable tumour, necrosis, fibrosis, oedema, vessels, stroma,
  inflammation, boundary morphology, or another tissue arrangement could alter the contrast;
- **composition/state hypothesis:** a prespecified cell population or multi-marker state could
  contribute to that architecture or physiology;
- **technical/sampling hypothesis:** acquisition, reconstruction, segmentation, tumour volume,
  biopsy location, fixation, stain batch, or field selection could explain the association;
- **falsifier for each hypothesis:** an observation that would weaken it;
- **discriminating endpoint:** the smallest pathology measurement that separates the leading
  alternatives.

Do not map texture to “heterogeneity,” low ADC to “cellularity,” enhancement to “angiogenesis,” or
peritumoural signal to “invasion” by name alone. Ask what tissue distribution, cell density,
microstructure, perfusion/permeability, or artefact would generate the image signal and what else
would generate the same pattern.

### Choose the next step by information gain

Rank candidate actions by:

`ability to distinguish hypotheses | mapping quality | assay validity | patient-level information |
feasibility | cost/tissue use | remaining claim ceiling`.

When tissue is scarce, do not spend the block on a broad panel before confirming tissue content,
mapping, and the most discriminating markers. Reserve sections for controls and repeat/orthogonal
work; document section allocation before staining.

## Imaging plus limited FFPE: three useful plans

Use these as design templates, not automatic prescriptions.

### Conservative plan — credible orthogonal exploration

Best when approximately 10 matched FFPE cases are available.

- Predefine one imaging phenotype and one or two competing tissue hypotheses.
- Create a patient–lesion–block–section map and report the scan-to-tissue interval/treatment.
- Select blocks/regions by a written representative or stratified rule independent of marker
  intensity; retain all eligible-case and exclusion records.
- Obtain blinded H&E annotation for one primary tissue endpoint and, only if needed, one small
  validated IHC panel with positive/negative and batch controls.
- Use patient-level paired summaries or a patient-aware model; show every patient, effect and CI.
- Run block/ROI, batch, threshold, and influential-patient sensitivity analyses.
- Write the result as exploratory orthogonal concordance or tissue-level support, not independent
  validation, pathway confirmation, or causality.

This plan is often better than an underpowered broad mIF panel because it answers one clear tissue
question honestly.

### Standard plan — locked tissue validation study

- Enrol or identify a larger non-overlapping matched cohort with a prespecified target population.
- Lock imaging phenotype, patient/block/ROI selection, primary pathology endpoint, marker panel,
  reader protocol, WSI pipeline, cutoffs, covariates, and multiplicity before evaluation.
- Sample multiple prespecified blocks/regions when whole-lesion heterogeneity matters.
- Use blinded pathology, batch-bridging controls, held-out algorithm validation, and patient-aware
  statistics.
- Quantify registration and temporal uncertainty; test external site/scanner/stain robustness.
- Reserve secondary markers and neighbourhoods for labelled exploratory analyses.

This plan can support independent replication of a locked association. It does not by itself prove
causality or clinical utility.

### Ambitious plan — mapped, multi-scale mechanism programme

- Prospectively coordinate radiology, surgery/grossing, pathology and molecular sampling.
- Use image-guided, orientation-preserving multi-region blocks plus neutral/comparator regions.
- Register radiology to gross specimen, block, WSI and spatial/molecular coordinates with error
  estimates.
- Combine H&E architecture, validated mIF/cell neighbourhoods, spatial transcriptomics or another
  orthogonal assay chosen for the question.
- Add longitudinal, perturbation, organoid/ex vivo, or functional evidence when a directional
  mechanism is claimed.
- Validate the locked imaging–tissue relationship in an independent cohort and assess clinical
  performance only if the intended use requires it.

The ambitious plan increases mechanistic resolution but also registration, multiplicity, batch,
and selection risks; each added layer must answer a prespecified link rather than decorate the
story.

## Repair patterns after common findings

| Finding | Preserve | Block/downgrade | Smallest useful repair |
|---|---|---|---|
| Ten same-cohort FFPE cases agree with imaging | illustrative patient-level concordance | independent/external validation and clinical generalisation | show all patients, effect/CI, blind scoring, label exploratory; seek locked non-overlapping cohort |
| One IHC marker differs by imaging group | marker-specific tissue association | cell-state, pathway, function, or causality | add justified panel/morphology/compartment and orthogonal evidence |
| Many cells but few patients | descriptive cellular distribution | cell-level p value as patient inference | aggregate or fit patient-clustered model; report patient n |
| Only patient/lesion match, no coordinates | tumour-level concordance | habitat or voxel localisation | obtain block map/registration or lower spatial claim |
| WSI endpoint changes after colour normalisation | conditional association | platform-invariant biology | test raw/normalised, site/batch, locked reference and external slides |
| Segmentation fails near boundary | unaffected central-region result if prespecified | invasive-front/neighbourhood headline | annotate held-out boundary fields and propagate error/sensitivity |
| Pathologist knew imaging group | descriptive annotations | confirmatory primary endpoint | blinded reread or independent reader; disclose and downgrade |
| Marker panel/threshold tuned on all cases | exploratory score | held-out validation | freeze panel/rules and test untouched patients |

## Writing contract

### Methods must report

- study role: discovery, exploratory orthogonal substudy, internal replication, or independent
  external validation;
- patient and matched patient–lesion–block–section counts at each stage, with eligibility and
  exclusions;
- scan/tissue dates, intervening treatment, specimen type, grossing/orientation, mapping and
  registration uncertainty;
- block/section/ROI selection rules and whether fixed before pathology/image-group results;
- fixation, processing, block/section age, thickness, staining platform/batch, scanner and QC;
- antibody clone/vendor/catalogue/lot, dilution, retrieval, detection, controls, panel and phenotype
  rules;
- pathologist roles, region definitions, training, blinding, repeat reads, agreement and
  adjudication;
- WSI version, training/tuning/test split, colour handling, segmentation/classification validation,
  thresholds, spatial parameters and failure handling;
- primary endpoint/denominator, patient-level inferential unit, nesting model, covariates,
  multiplicity, missingness and sensitivity analyses.

### Results must report

- eligible, stained, QC-passing, matched, and analysed patient counts before cell/ROI counts;
- balance or confounding of specimen, fixation, block age, staining batch, scanner and tissue area;
- effect size and confidence interval, patient-level distribution/consistency, and exact adjusted
  multiplicity result;
- reader/algorithm performance and important failure modes on held-out material;
- sensitivity to block/ROI choice, marker threshold, segmentation, batch, registration, tissue
  composition and influential patients;
- concordant and discordant cases, not only representative concordance;
- whether the result is morphology observed, marker signal measured, algorithm endpoint estimated,
  or mechanism inferred.

### Figure legends must report

- number of patients, lesions, blocks, sections, ROIs/fields and cells separately;
- stain/marker, compartment, scale bar, scanner/resolution and image-processing status;
- whether images are representative and the prespecified selection rule;
- annotation/segmentation/phenotype definitions, threshold, denominator and aggregation level;
- what points, boxes, bars, lines and error intervals represent;
- statistical model, independent unit, sidedness, multiplicity correction and exact p value where
  appropriate;
- whether displayed serial sections are adjacent rather than the same cells.

### Discussion must report

- the highest supported claim and the evidence rung reached;
- alternative tissue, cellular, technical and sampling explanations;
- limitation from FFPE/preanalytics, marker specificity, WSI error, tissue coverage, nesting,
  temporal mismatch and registration/scale;
- whether pathology is an exploratory orthogonal subset, internal replication, or independent
  validation;
- why association/localisation does not establish function or causality and which experiment would;
- target population and platform/site generalisability.

### Title, abstract, and conclusion language

Do not allow stronger wording in the title or abstract than in the Results. Prefer:

- “was associated with” over “was driven by”;
- “showed concordance with” over “validated the mechanism”;
- “marker-positive cell density” over “activated cell state” when that is what was measured;
- “algorithm-estimated phenotype” over “pathological measurement” when segmentation/classification
  created the endpoint;
- “exploratory orthogonal FFPE subset” over “external validation cohort” for nested cases;
- “supports a candidate tissue explanation” over “reveals the biological basis” when alternatives
  remain.

## Reviewer checklist

Classify findings as `BLOCKER`, `MAJOR`, `MINOR`, or `CLARIFICATION` and cite the exact table,
figure, paragraph, code/output, or missing record.

### Design and provenance

- Is the imaging phenotype exactly defined and technically stable?
- Are patient, lesion, time, treatment, block, section and region links traceable?
- Were tissue availability and exclusions compared across groups?
- Were blocks/ROIs/images selected without viewing the result?
- Does tissue coverage support the claimed spatial scale?

### Assay and pathology

- Are preanalytical variables recorded and balanced?
- Are antibody/panel identities, controls, batches and phenotype rules reproducible?
- Is a single marker overinterpreted as state, pathway or function?
- Are pathologist roles, blinding, region definitions and agreement clear?
- Are serial sections described honestly?

### Digital pathology

- Are scanner, stain variation, QC exclusions and colour handling auditable?
- Were segmentation/classification models locked and validated on held-out representative fields?
- Are artefacts, uncertainty and failure modes propagated to the endpoint?
- Are density, denominator, spatial radius/null, boundary handling and multiplicity explicit?

### Statistics and claims

- Is patient the independent unit and nesting preserved?
- Are matched patient counts distinguished from cell/ROI counts?
- Are effect sizes, CIs, patient-level plots and influential-case analyses shown?
- Were primary endpoints and multiplicity defined before testing?
- Is same-cohort FFPE correctly labelled orthogonal/exploratory rather than external validation?
- Are H&E observation, IHC measurement, algorithm estimate and mechanism inference kept separate?
- Does the proposed validation actually test the unresolved bridge?

## Standard output

Return the following sections for a substantive review/advice request:

1. **Task and claim target** — imaging phenotype, tissue question, unit, time and intended evidence
   level.
2. **Provenance map** — patient–lesion–image–block–section–ROI chain with missing links.
3. **Evidence-layer ledger** — H&E observations, IHC/mIF measurements, algorithm estimates and
   mechanistic inferences in separate rows.
4. **Gate table** — RP0–RP8 verdict, evidence, consequence and repair.
5. **Competing hypotheses** — at least two biological and one technical/sampling explanation,
   discriminating endpoint and falsifier.
6. **Assay and control plan** — block/section selection, panel, controls, reader/WSI QC and tissue
   budget.
7. **Analysis plan** — primary patient-level endpoint, nesting, covariates, multiplicity,
   uncertainty and sensitivities.
8. **Plan ladder** — conservative, standard and ambitious routes with claim ceilings and trade-offs.
9. **Writing repair** — Methods omissions, Results/legend corrections and exact bounded conclusion.
10. **Next executable action** — one action that most reduces the current uncertainty.

If the user supplies only prose or a figure, distinguish verified evidence from reconstructed or
missing assumptions. If a gate is `STOP`, do not end with rejection alone: offer the nearest valid
question and the shortest feasible repair.

## Internal cross-checks

Before returning, confirm alignment with:

- [radiomics-mechanism-bridge.md](radiomics-mechanism-bridge.md) for imaging physics, competing
  mechanisms, cross-modal triangulation and claim grade;
- [sample-to-image-mapping.md](sample-to-image-mapping.md) for patient/lesion/region/time mapping;
- [association-validation.md](association-validation.md) for patient-level association and
  replication;
- [biological-validation.md](biological-validation.md) for orthogonal and functional validation;
- [research-mentoring-and-idea-development.md](research-mentoring-and-idea-development.md) for
  learner-calibrated, executable advice;
- [reviewer-playbook.md](reviewer-playbook.md) for severity-ranked manuscript review.

Final self-check:

- Did the answer separate H&E observation, IHC/mIF measurement, algorithm estimate, and mechanism
  inference?
- Did it preserve patient as the independent unit despite many cells/fields?
- Did it audit specimen selection, FFPE preanalytics, controls, blinding, WSI QC and mapping?
- Did it prevent a nested 10-case FFPE subset from being called independent external validation?
- Did it state `PASS / CONDITIONAL / STOP` and the claim ceiling?
- Did it give the learner alternatives, trade-offs, falsifiers, writing language and a next action?
