# Modality execution workflows

Open only the active modality section. Every step records inputs, outputs, decision, alternatives,
assumptions, unit, evidence state, code/config locator and failure action.

## Shared T0-T8 state machine

| State | Required decision | Exit evidence |
|---|---|---|
| T0 question | exact contrast/endpoint and intended inference | question, Claim IDs, primary modality |
| T1 identity | donor-sample-specimen-section-library map | unique IDs, hierarchy, mismatch report |
| T2 intake QC | file/object compatibility and raw evidence preservation | dimensions, schema, provenance, blockers |
| T3 analysis lock | steps, parameters, alternatives, independent unit, protected-test rule | signed/frozen plan |
| T4 build | executable code/config and assertions | dry check, expected-output contract |
| T5 run | authorized command and monitored output root | exit status, log, deviations |
| T6 QC/result | exclusion ledger and real result artifacts | retained units, result schemas, checksums |
| T7 evaluation | sensitivity/method/inference questions separated | handoff packets and claim consequence |
| T8 archive | reproducible package and limitations | manifest, environment, code, logs, outputs |

Do not advance T5 to T6 merely because a process ended. Required artifacts must exist, be readable,
match the expected schema, and be attributable to the recorded run.

## Optional raw-read-to-matrix front end

Activate this front end when FASTQ files are supplied or the requested run starts before an
analysis-ready matrix. If a matrix/object is supplied instead, mark every upstream item
`UPSTREAM_AUTHOR_REPORTED`, `UPSTREAM_PARTLY_VERIFIED`, or `UPSTREAM_VERIFIED` with its producer,
reference and QC evidence; never pretend this skill reran an upstream step.

### Shared raw-read intake and provenance

1. Freeze the FASTQ manifest, checksums, read layout, sample/library/index map, lane/run identity,
   organism, assay/library chemistry and expected feature types. If BCL-to-FASTQ demultiplexing is
   outside the supplied material, record the sample-sheet/demultiplexing evidence rather than
   reconstructing it. If BCL is supplied, demultiplex only with explicit authority and a preserved
   sample sheet/run manifest.
2. Inspect read-quality profiles, adapter/polymer/low-complexity signals, read-length/UMI/barcode
   structure, contamination indicators and cross-sample identity evidence. Trimming or correction
   is a recorded decision, not an automatic ritual; retain pre/post evidence and read counts.
3. Freeze the genome/transcriptome/feature reference bundle, annotation release, contig policy,
   decoy/spike-in policy, index builder and checksums. A reference name without the exact bundle and
   index provenance is insufficient.
4. Record exact tool/workflow versions, command/config, environment, compute class, logs, temporary
   and final output roots, restart points and success assertions. Preserve upstream intermediate
   metrics needed to diagnose a matrix even if only the matrix enters downstream analysis.
5. Reconcile produced library/sample IDs and features with the frozen manifest before T3. Stop on
   index collision, unexpected feature types, incompatible chemistry/read structure, reference
   mismatch, unexplained sample loss or output overwrite risk.

### Bulk FASTQ to counts

- Establish strandedness/read layout and choose alignment, pseudoalignment or other quantification
  deliberately for the locked gene/transcript estimand; record multimapping, duplicate/UMI and
  transcript-to-gene aggregation policies.
- Export per-library assignment/mapping and coverage/strand evidence, transcript and/or gene matrix,
  feature annotation, sample sheet, unassigned/failed-read summary and reference/config receipts.
- A quantifier's abundance estimate is not automatically a raw integer count suitable for every
  downstream likelihood. Record the exact assay/slot consumed by the gene-level model.

### sc/snRNA FASTQ to feature-barcode matrices

- Use chemistry-aware barcode/UMI and feature-library parsing; record whitelist/correction policy,
  intronic/exonic counting for cells versus nuclei, multi-library linkage and feature-barcode types.
- Preserve raw droplets and the initially filtered/called matrix, cell-calling rule/tool evidence,
  per-library sequencing/mapping/saturation/feature metrics and barcode-to-library map. Ambient and
  independent cell-calling analyses need the raw droplet universe.
- Do not merge libraries or discard barcode namespaces before donor/specimen assignment is proven.
  A filtered matrix supplied by another pipeline remains an upstream artifact, not a verified cell
  population merely because it loads successfully.

### Spatial raw input branches

- **Spot/bin capture assays:** bind FASTQ libraries to slide, capture area, spot/barcode whitelist,
  tissue image, coordinate table and scale factors. Record reference/index, read-to-feature/spot
  quantification, tissue/calling rule and the exact matrix-coordinate-image bundle produced.
- **Imaging-based spatial assays:** there may be no conventional FASTQ-to-matrix path. Freeze raw
  image rounds/channels/fields, codebook/probe reference, registration/decoding/segmentation and
  molecule-to-cell assignment provenance. Never force this branch through a sequencing workflow.
- Stop if slide/area/barcode/image identities, image scale/orientation or matrix coordinates cannot
  be reconciled. Visual alignment by appearance is not provenance.

## Bulk RNA route

### Matrix/object intake

- Identify count type: raw integer gene counts, transcript abundance, normalized matrix or summary.
- Record organism, gene identifier namespace/version, strandedness, library preparation, alignment/
  quantification source and whether technical replicates exist.
- Reconcile samples against donor, tissue, time, condition, batch and clinical covariates.

### Core workflow

1. **Identity/QC**: library size, detected features, mapping/assignment metrics when available,
   sample correlation/PCA, sex/known markers where ethically and scientifically appropriate.
2. **Filtering**: define feature/sample rule before outcome inspection; record tested gene universe.
3. **Normalization/exploration**: choose a method compatible with count source and model; do not feed
   an already normalized matrix into a count model that expects raw counts.
4. **Design/contrast**: encode condition, paired/repeated structure, batch and justified covariates;
   check rank/aliasing and estimability.
5. **Gene-level model**: preserve effect direction, magnitude, uncertainty, raw P and adjusted P;
   define multiplicity family.
6. **Pathway/score**: state database/version, universe, ranking statistic, direction and redundancy
   handling. Distinguish discovery from validation.
7. **Export**: sample QC, normalized/exploratory object, design/contrast, full result table, pathway
   table, plots, session/environment and decision log.

### Frequent stops

- condition perfectly confounded with batch/site/library;
- donor IDs missing or technical replicates treated as biological replicates;
- non-integer/unknown matrix used with an incompatible count likelihood;
- contrast not estimable, or filtering/universe reconstructed only after seeing hits;
- cell-composition change described as cell-intrinsic expression without supporting analysis.

## sc/snRNA route

### Matrix/object intake

- Record count-matrix origin and whether cell calling already occurred; preserve raw droplets if
  ambient correction or independent calling may be needed.
- Reconcile cell barcode -> library -> specimen -> donor/patient -> condition/time/site.
- Record chemistry/reference/feature type and nuclei-specific limitations when applicable.

### Core workflow

1. **Calling/ambient/RBC**: distinguish empty/background droplets, ambient contamination and real
   low-RNA populations; log correction method and pre/post evidence.
2. **QC**: inspect library/sample distributions before setting thresholds; preserve per-library
   rules and avoid removing the biological state of interest solely because it is extreme.
3. **Doublets/multiplets**: report method, expected rate basis, sample-wise application, flagged vs
   removed counts and sensitivity.
4. **Normalization/HVG**: state layer/assay used at every downstream step; prevent corrected or
   integrated values from being used in an incompatible count test.
5. **Reduction/integration**: justify PCs/latent dimension, neighbor graph and batch correction;
   evaluate batch mixing together with preservation of known biology.
6. **Clustering/annotation**: log resolution and stability; use marker/reference evidence,
   contradictions, unknown/ambiguous labels and donor distribution.
7. **Donor-aware testing**: for group comparisons use pseudobulk or justified mixed/hierarchical
   methods; test abundance/composition separately from cell-state expression.
8. **Optional analyses**: subclustering, trajectory, communication, GRN or perturbation response
   each gets its own assumptions, unit, null/control and claim ceiling.
9. **Export**: raw/clean object locators, per-cell and per-sample QC, exclusions, annotations,
   marker tables, donor-aware results, optional outputs, code/environment and manifest.

### Frequent stops

- donor/sample identity cannot be reconstructed;
- all donors of one group occur in one batch;
- clusters are supported by one desired marker while conflicting markers are ignored;
- cells are used as independent biological replicates for a donor-level claim;
- integrated coordinates are treated as measured expression or as proof that batches vanished;
- trajectory, communication or GRN output is narrated as causal biology.

## Spatial transcriptomics route

### Matrix/object and geometry intake

- Inventory histology images, count/feature matrix, barcodes, coordinates, scale factors, masks,
  registration transforms, section orientation and tissue metadata.
- Define whether the unit is spot, bin, segmented cell, region, section, specimen or patient and
  how repeated sections/regions will be aggregated.
- Record platform/assay, nominal resolution and whether cell-type values are measured, mapped,
  transferred or deconvolved.

### Core workflow

1. **Geometry QC**: coordinate/image correspondence, scale/orientation, tissue mask, registration,
   segmentation and edge artifacts.
2. **Molecular QC/normalization**: per section and region; preserve section effects and zero/
   sparsity structure relevant to the chosen model.
3. **Cell-type mapping/deconvolution**: state reference source, overlap, granularity, identifiability,
   compositional constraints and uncertainty; label estimates as estimates.
4. **Domains/features**: record input representation, neighborhood graph, latent dimension,
   resolution/seed and stability across defensible alternatives.
5. **Spatial statistic/neighborhood**: declare coordinate system, scale, radius/kernel/k, weights,
   edge handling, spatial null/permutation unit and multiple testing.
6. **Patient aggregation**: prevent spot/section pseudo-replication; use patient-aware summaries or
   hierarchical models for clinical inference.
7. **Optional bridge**: register region/section to imaging or pathology with explicit mapping error,
   matched N, discordance and missingness.
8. **Export**: geometry QC, processed object, estimates with uncertainty, domain/neighborhood
   tables, patient-level summaries, sensitivity results, images, transforms and run manifest.

### Frequent stops

- coordinates, images and matrix barcodes do not reconcile;
- scale/orientation/registration is assumed from appearance alone;
- deconvolved proportions are called measured cells;
- spots or sections are counted as independent patients;
- the chosen spatial null destroys or preserves structure in a way incompatible with the question;
- a result disappears under nearby plausible radius/resolution/segmentation choices but the claim
  remains unchanged.

## Interpretation packet

For each downstream result include:

`Result ID | question/contrast | modality | donor/patient hierarchy | producing run ID | object/table
and exact locator | method/layer | effect/readout | uncertainty/multiplicity state | QC/exclusion
state | sensitivity state | alternative explanations | evidence status | allowed claim | prohibited
upgrade | requested receiver decision`.
