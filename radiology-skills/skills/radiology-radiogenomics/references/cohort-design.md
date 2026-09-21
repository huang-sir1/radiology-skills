# Cohort, specimen, and matched-unit design

Use this module for feasibility and protocol work in all three study scopes. Begin from the declared
`study_scope`; do not demand an imaging–omics intersection from a mechanism-only study or an omics
assay from an imaging-only study.

## 1. The binding quantity is the usable independent-unit intersection

Report counts as a flow, not as one headline number:

`identified -> eligible -> modality-specific QC pass -> mapping/QC intersection -> analysable -> validation`

The last biologically independent unit governs power. Cells, spots, tiles, ROIs, repeated lesions,
sections and technical replicates do not increase patient- or donor-level n unless the estimand and
model explicitly treat them as independent experimental units.

| Scope | Required intersection | Typical independent unit | Scope-specific mapping |
|---|---|---|---|
| `imaging-only` | eligible subjects/lesions with usable imaging, labels and endpoint | patient, or lesion when the estimand and clustering justify it | patient–lesion–series–ROI–time |
| `mechanism-only` | eligible biological units with the active assay, metadata, condition and endpoint | donor/patient, animal, organoid, culture replicate or randomized experimental unit | donor–specimen–assay–condition–time; add block/section/cell/spot hierarchy as applicable |
| `imaging-mechanism` | the same biological units with usable imaging **and** the molecular/pathology layer required by the claim | usually patient or donor; sometimes lesion with justified within-patient modeling | patient–lesion–scan–ROI/habitat–biopsy/resection–block–section–assay–time |

Never substitute the largest upstream database count for the analysis intersection. Keep discovery,
internal resampling, orthogonal validation and independent external validation counts separate.

## 2. Unit and provenance contract

Before proposing a model, record:

- population, disease/context, setting, treatment state and sampling frame;
- biological independent unit and every nested level;
- inclusion/exclusion rules and whether they were defined before outcome inspection;
- specimen source, preservation, assay platform, batch, processing time and QC status;
- exposure/perturbation assignment, dose, duration, target engagement and controls when relevant;
- endpoint definition, observation window, censoring and competing events;
- missingness by variable and by stage of the cohort flow;
- discovery/validation independence, including institution, time, participants and preprocessing;
- permissions, consent, data-use agreements and re-identification/overlap risks.

For `imaging-mechanism`, additionally record whether the assayed tissue came from the imaged lesion,
region/habitat and time window. A resection-wide bulk sample cannot silently validate a local imaging
habitat. For `mechanism-only`, stop at the real specimen/assay chain; do not invent scan or ROI fields.

## 3. Modality-specific feasibility questions

### Imaging-only

- Are acquisition, reconstruction, contrast phase, field strength, scanner/site and segmentation
  sufficiently represented and separable from outcome?
- Are labels and endpoints assigned at the same patient/lesion/time level as the model output?
- Can all data-dependent preprocessing be learned inside training data?

### Bulk RNA or other bulk molecular assays

- Is the independent biological replicate a donor/patient rather than a library or aliquot?
- Are tissue composition, purity, preservation, library strategy and batch recoverable?
- Are treatment/condition and batch distinguishable, and are paired samples modeled as paired?

### Single-cell or single-nucleus assays

- How many donors and conditions remain after donor-level QC, not how many cells?
- Are dissociation/nucleus protocol, viability, ambient RNA, doublets and donor/condition batches
  separable from the biological contrast?
- Can confirmatory inference be performed at donor/pseudobulk or another defensible replicate level?

### Spatial transcriptomics or pathology

- How many independent patients/specimens, blocks and sections exist?
- What resolution is directly measured and what is segmented, deconvolved, transferred or inferred?
- Does region selection create spectrum bias, and can within-specimen observations be modeled as nested?

### Perturbation

- Is assignment randomized or otherwise identifiable, and can efficiency, multiplicity and off-target
  effects be measured?
- Are non-targeting, positive, vehicle/sham and rescue/orthogonal controls available as appropriate?
- Are biological replicates independent, with dose and time sufficient to separate primary response
  from toxicity, stress and downstream adaptation?

## 4. Public and institutional data sources

Use sources only when they match the requested scope and claim. Examples include TCIA for imaging;
TCGA/GDC, cBioPortal, GEO/BioStudies, ICGC/PCAWG and controlled dbGaP/EGA studies for molecular data;
HCA and disease atlases for external cell references; and institutional archives for matched imaging,
specimens or experimental validation. An external atlas is contextual reference evidence unless its
participants and specimens are truly part of the analysis cohort.

For a claimed external validation set, check participant/sample/UID overlap, collection provenance,
label independence, preprocessing independence and whether model/threshold choices were frozen before
evaluation. Public origin alone does not make a cohort independent.

## 5. Power and complexity

- Power the prespecified primary estimand at the real independent-unit level.
- Treat high-dimensional scans as multiplicity-controlled discovery, not as powered confirmatory work.
- Limit degrees of freedom when usable n is small; prefilter only by outcome-blind rules.
- For clustered or repeated data, account for intra-unit correlation, imbalance and attrition.
- For prediction, estimate the effective sample available to each training/tuning/validation stage.
- For perturbation, power biological replicates for the assigned intervention and primary phenotype;
  cell count cannot repair a one-replicate experiment.

Do not promise a mechanistic or externally validated study merely because a complex model can be fit.

## 6. Feasibility verdict and rescue

| Verdict | Minimum interpretation |
|---|---|
| `PASS` | unit identity, required intersection, key provenance, primary estimand and validation route are credible |
| `CONDITIONAL` | the question remains answerable after named metadata recovery, scope reduction or bounded sensitivity analysis |
| `STOP` | unit identity is broken, essential modalities/conditions do not overlap, condition is inseparable from batch, or the requested claim requires evidence the design cannot produce |

For `STOP`, return:

`blocked claim -> exact design failure -> nearest answerable question -> minimum new data/metadata -> wording allowed now -> smallest next action`.

## 7. Mentor options

- **Conservative:** one primary contrast at the real independent-unit level, limited features/programs,
  rigorous QC and honest descriptive/association wording.
- **Standard:** prespecified primary analysis plus one orthogonal or independent validation route and
  targeted sensitivity analyses.
- **Advanced:** spatial/temporal sampling, multi-system replication, perturbation/rescue or prospective
  validation only when identity, resources and analysis capacity are credible.

Compare options by required n, metadata, assay cost, failure risk, claim ceiling and fallback value.

## 8. Writing contract

Methods must state the cohort flow, independent unit, nesting, timing, exclusions, QC, missingness,
batch/site structure and discovery/validation separation. Results must begin with the analysable count
for the primary estimand and explain every denominator change. Limitations must name spatial, temporal,
sampling and transportability boundaries.

Scope-aware sentence skeletons:

- `imaging-only`: “Of [N] eligible participants, [K] with protocol-compliant imaging and complete
  endpoint data formed the analysis cohort; [V] independent participants were reserved for validation.”
- `mechanism-only`: “Of [N] eligible biological units, [K] independent [donors/animals/cultures]
  passed prespecified specimen and assay QC for the primary [condition/perturbation] contrast.”
- `imaging-mechanism`: “Of [N] molecularly profiled participants and [M] with usable imaging, [K]
  had lesion-, region- and time-compatible data for the primary cross-scale analysis.”
