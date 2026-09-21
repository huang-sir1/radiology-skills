# Spatial transcriptomics research guidance

Use this playbook when a task requires design, audit, interpretation, repair, or manuscript
reporting for spatial transcriptomics. It turns the 33 eligible studies in
`spatial-transcriptomics-literature-map-2024-2026.tsv` into decision gates. Read only the blocks
needed for the user's question, but never bypass the provenance, inferential-unit, measured-versus-
inferred, or registration gates.

The evidence map was locked on 2026-08-21. Every included article has a formal publication date
from 2024-08-21 through 2026-08-21 and a journal JIF of at least 10 under the final audit. Evidence
IDs `ST01`–`ST33` below point to the corresponding TSV rows. They support decisions; they do not
make a platform, model, or biological conclusion universally valid.

## Non-negotiable interpretation language

- The biological sample or patient is the inferential unit for patient-level claims. Cells, bins,
  spots, molecules, fields of view, serial sections, and virtual sections are nested observations,
  not independent patients.
- Record the shared primary state (`measured`, `derived`, `estimated`, `associated`, `predicted`, or
  `perturbed`), the spatial subtype (`segmented`, `assigned`, `deconvolved`, `mapped`, `imputed`,
  `interpolated`, or other declared operation), and the claim link (`direct`, `inferred`, or
  `proposed`) in separate fields. Do not collapse them in a table, figure, caption, or narrative.
- `missing` means that evidence or metadata do not exist. It is never a primary evidence state.
  These three axes are labels, not a single progression from measurement to causality.
- Advertised resolution is not effective biological resolution. Report capture area, transcript
  diffusion, panel sensitivity, cell segmentation, molecule assignment, tissue morphology, and
  the unit actually analysed.
- A spatial domain, topic, embedding, neighbourhood, communication edge, velocity arrow, clone,
  virtual slice, or histology-predicted expression value is a model output until independently
  supported. It is not a direct observation merely because it is displayed on tissue.
- Spatial proximity is not signaling; an inferred trajectory is not lineage; an RNA-derived CNA is
  not a measured genome; H&E-predicted expression is not spatial transcriptomics.
- For every spatial study, preserve the assay/tissue coordinate chain:
  `patient -> specimen/lesion -> block -> section -> field/tile -> molecule -> cell/spot/bin -> pathology region`.
  Record transformations and uncertainty at every arrow. Only when
  `study_scope == imaging-mechanism`, extend this chain from the pathology region to a registered
  radiology habitat; mechanism-only work must not be asked for that extension.
- Keep discovery, threshold selection, registration tuning, model fitting, and validation separate.
  Patient or tissue leakage through adjacent sections, reference atlases, tissue tiles, or pretrained
  corpora is still leakage.

## Route the request before analysis

| Route | Typical request | Primary estimand | Mandatory blocks |
|---|---|---|---|
| Feasibility | Can these samples answer the spatial question? | identifiable contrast at a declared spatial unit | 1–5 |
| Platform or protocol choice | Which assay should we use? | expected information under tissue and panel constraints | 1–3 |
| Domain or gradient analysis | Where is a program enriched? | domain, continuous gradient, SVG, or subcellular localization | 1–6 |
| Cell composition or mapping | Which cells are where? | cell fraction, cell assignment, or mapped state | 1–7 |
| Niche or communication | Which cells co-occur or may signal? | enrichment or directed interaction under a spatial null | 1–8 |
| Histology-to-expression | Can morphology predict molecular state? | held-out prediction error and calibration | 1–5, 9 |
| Multi-sample, 3D, or time | How does architecture vary across patients, sections, or time? | sample-aware spatial effect, reconstruction error, or transition | 1–7, 10 |
| Perturbation or lineage | Does a perturbation or clone change a spatial program? | guide/barcode-by-context effect | 1–5, 8, 11 |
| Spatial tumour evolution | Where are tumour clones and CNAs? | allelic event or clone-by-niche association | 1–5, 12 |
| Radiology linkage, only when `study_scope == imaging-mechanism` | Does a radiology habitat map to a molecular niche? | patient- or lesion-level registered association | 1–8, 13 |
| Manuscript/reviewer audit | Are the claims defensible? | branch-specific verdicts and repair actions | relevant blocks plus reviewer checklist |

For a composite request, open the **union** of all mandatory blocks from every applicable route.
Only when `study_scope == imaging-mechanism`, imaging-habitat-to-niche work requires both the
radiology-linkage block and
the niche/neighbourhood/spatial-null block. A later biological label must not cause an earlier QC,
registration, mapping or inferential-unit block to be skipped.

## Input contract

Do not choose a method until the available inputs and the intended claim are explicit.

### Scientific question and spatial estimand

Capture:

`population | biological condition | contrast | endpoint | spatial unit | target region | distance/gradient/neighbourhood definition | time | intended claim | validation target`

Examples of distinct estimands that must not be mixed:

- patient-level difference in the fraction or area of a pathology-defined domain;
- within-cell-type expression gradient as distance from an invasive front increases;
- enrichment of sender and receiver cell types relative to a tissue-aware spatial null;
- held-out error when H&E predicts a measured gene program;
- clone-by-neighbourhood interaction for a DNA-supported clone;
- only when `study_scope == imaging-mechanism`, association between a registered radiology habitat
  and a measured spatial niche.

### Specimen and replication passport

Require:

- patient, lesion, block, section, side, orientation, thickness, order, anatomical region, and date;
- biological replicates, technical replicates, serial or adjacent sections, fields of view, and the
  rule linking them;
- preservation, fixation, ischemia, decalcification, storage, section damage, tumour content,
  necrosis, folds, tears, edge and background regions;
- treatment timing, longitudinal relation, site, operator, reagent lot, run, slide, batch, and panel;
- whether a sample used for model selection also appears in validation, a single-cell reference,
  a pathology foundation-model corpus, or an adjacent-section comparator.

### Platform and feature passport

Record:

`vendor/platform | chemistry/version | sequencing- or microscopy-based assay | fresh-frozen/FFPE | whole-transcriptome/targeted | panel version and genes | advertised resolution | effective unit | assay-native microscopy/histology channels | segmentation version | transcript-assignment rule | negative controls | positive controls | software versions`

For targeted assays, include probe design, isoform coverage, negative-control probes, blank codewords,
per-gene sensitivity and specificity, panel dropouts, and whether the biological program can be
identified using the assayed genes. For sequencing assays, include capture area, binning, sequencing
depth, unique molecules, mapping, tissue coverage, diffusion or spillover checks, and effective
cellular mixture.

### Coordinate, tissue, and registration passport

Require original and transformed coordinates, assay-native microscopy or histology resolution,
pixel size, orientation, fiducials, landmarks, masks, interpolation method, transformation matrices,
registration residuals, blinded landmark checks, and the mapping from molecular locations to
pathology regions. Only when `study_scope == imaging-mechanism`, append the transform to radiology
regions/habitats and its uncertainty.

If only processed matrices remain, state which operations cannot be audited: raw molecule assignment,
segmentation, tissue masking, coordinate transforms, microscopy/histology normalization, or
registration tuning.

### Reference and generated-layer passport

For every scRNA reference, atlas, pretrained model, imputation model, histology model, spatial
integration, or 3D reconstruction, record:

- source patients, tissues, conditions, platforms, panels and preprocessing;
- feature overlap, label hierarchy, missing or novel states, tumour-state representation, and
  reference-to-query shift;
- training, tuning and test partitions, patient overlap, adjacent-section overlap and corpus overlap;
- measured inputs and generated outputs; uncertainty, calibration and held-out validation;
- whether the layer will be used only for visualization or for formal testing.

### Required artifacts for an audit

Ask for the sample manifest, raw or molecule-level inputs when available, assay-native microscopy/
histology and segmentation
files, coordinate transforms, QC tables and maps, code and environment lock, random seeds, panel
manifest, scRNA reference, model checkpoints or versions, intermediate assignment/deconvolution
objects, statistical design, multiplicity plan, final figures with source tables, and independent
validation evidence.

## Verdict language

Use one verdict per decision block and one global verdict.

| Verdict | Meaning | Allowed action |
|---|---|---|
| **PASS** | Inputs, design, uncertainty and validation support the requested inference. | Proceed and state the bounded claim. |
| **CONDITIONAL** | The analysis is informative but one or more limitations lower the claim or require sensitivity analysis. | Proceed only with named repairs, downgraded language and unresolved uncertainty. |
| **STOP** | The requested estimand is not identifiable, provenance is broken, leakage exists, or the result is being represented as a stronger evidence type than it is. | Do not make the claim; request data, redesign, or relabel the output. |

`CONDITIONAL` is not a softer synonym for PASS. Name the condition, the analysis and claim branch it
affects, the repair, and the permitted wording after repair.

## End-to-end stage gates

| Gate | Question | PASS artifact | Typical CONDITIONAL | STOP trigger |
|---|---|---|---|---|
| G0 — estimand | Is the biological contrast defined at a spatial and sample unit? | locked estimand and claim target | exploratory estimand with explicit scope | cells/spots treated as patient replicates or no definable contrast |
| G1 — assay contract | Can the platform, panel and tissue resolve the target? | platform/resolution passport and benchmark match | partial panel or mixed effective resolution | target program not observable or platform/version unknown |
| G2 — QC and provenance | Are tissue, molecules, cells and coordinates auditable? | QC maps, provenance chain and attrition table | processed-only audit with named blind spots | broken sample identity, irrecoverable registration, severe unbounded artifact |
| G3 — representation | Are segmentation, domains, labels or factors stable enough? | alternative-boundary and representation sensitivity | one defensible model with unresolved assignment error | downstream result dominated by segmentation or unsupported recovered cells |
| G4 — spatial inference | Does the test match the SVG, gradient, niche or CCC estimand and sample structure? | sample-aware effect, null, uncertainty and multiplicity | exploratory local pattern without external validation | invalid null, pseudoreplication, or causal claim from proximity alone |
| G5 — generated layers | Are mapped, imputed, predicted or virtual layers validated on measured data? | held-out measured validation and calibration | visualization-only generated layer | generated value presented as direct measurement or used unvalidated for a biomarker |
| G6 — multi-sample/dynamic | Are integration, 3D, time, clone or perturbation assumptions testable? | condition-preservation, holdout or experimental controls | stable association with incomplete mechanism | virtual time called lineage, RNA CNA called genome, or guide/barcode identity unreliable |
| G7 — radiology linkage, only when `study_scope == imaging-mechanism` | Does molecular evidence refer to the same patient, lesion, region and time as radiology imaging? | locked mapping, independent cohort and calibrated claim | patient-level association with weak local registration | local co-localization claimed from unmatched or coarse data |

Do not advance to a later gate to compensate for failure at an earlier gate. A compelling heatmap or
large cell count cannot repair an unidentifiable estimand, mismatched patient, unsuitable panel, or
broken coordinate chain.

## Decision block 1 — question, spatial estimand, and inferential unit

### Expand

Translate the scientific question into one primary estimand and a limited set of secondary
estimands. Specify:

- the biological unit: patient, specimen/lesion, block, section, field, cell, spot, bin, molecule,
  clone, or pathology region; add a radiology region only when
  `study_scope == imaging-mechanism`;
- the spatial object: categorical domain, continuous gradient, point process, contact graph,
  neighbourhood, distance to a boundary, subcellular compartment, 3D volume, or time-indexed state;
- the contrast: condition, treatment, outcome, genotype, clone, pathology region, or time; add a
  radiology imaging habitat only when `study_scope == imaging-mechanism`;
- the effect: abundance/area, expression, composition, co-occurrence, signaling score, transition,
  prediction error, or association;
- the replication and correlation structure, including serial sections and multiple fields from one
  patient;
- the intended claim branch or branches and each validation route.

If the user asks to “find spatial biomarkers,” separate a patient-level domain burden, a within-
domain gene program, a morphology–molecular association and a predictive signature for unseen
patients. When `study_scope == imaging-mechanism`, add registered radiology–molecular association as
a separate target. These need different models and evidence.

### Review

Audit whether the design contains independent biological samples for the requested claim. Check
whether regions were chosen before viewing the outcome, whether a distance or neighbourhood radius
was tuned on the same patients used for testing, whether many sections from one patient were treated
as replicates, and whether the contrast is confounded by site, batch, tissue quality, or platform.

For spatial hypotheses, inspect the support of the estimand: enough cells on both sides of a boundary,
enough patients with each condition, sufficient panel genes, observable rare populations, overlapping
distance ranges, and adequate tissue area after QC.

### Interpret and decide

A descriptive map can establish where measured or estimated features appear in the assayed section.
It cannot establish population prevalence, treatment prediction, temporal transition, or mechanism
without the corresponding replication, comparator and validation. A large number of cells increases
within-section precision but does not create more independent patients.

### PASS / CONDITIONAL / STOP

- **PASS:** one estimand is written in terms of population, contrast, spatial unit, effect and
  inferential unit; biological replication and validation match the intended claim.
- **CONDITIONAL:** the map is valid for descriptive discovery but sample size, region selection or
  panel support restricts population-level inference. Return effect estimates as exploratory and cap
  the claim at the assayed tissue.
- **STOP:** the contrast cannot be reconstructed, cells/spots are the only “replicates,” outcome-
  informed regions are tested without separation, or the target is absent from the assay.

### Repair or help

Create a sample-by-section manifest, collapse or model nested observations at the patient level,
lock region and distance definitions, identify a confirmatory cohort or held-out tissue, and reduce
the question to the highest identifiable estimand. If power is limited, return detectable-effect or
uncertainty analysis rather than a significance promise.

### Hard constraints

- Never calculate a patient-level p value by treating cells, spots, tiles, or sections as independent
  patients.
- Never replace an absent counterfactual or time point with a spatial gradient and call it response.
- Do not let post-outcome region selection enter confirmatory inference.

### Writing four-part contract

- **Methods:** state the primary estimand, spatial unit, inferential unit, nesting, contrast,
  prespecified region/distance, covariates, validation split and multiplicity family.
- **Results:** report patient-level effect size, interval, donor consistency, tissue support and
  attrition; keep descriptive and confirmatory results separate.
- **Figure legend:** identify patient and section counts, spatial unit, measured or inferred status,
  denominator, summary statistic, test and multiplicity correction.
- **Discussion:** bound the conclusion to sampled tissue, effective resolution and cohort; name the
  shortest unmet requirement in every claim branch invoked.

**Evidence:** ST01–ST04, ST15, ST25, ST29, ST32–ST33.

## Decision block 2 — platform, resolution, panel, and reproducibility

### Expand

Choose an assay by the information needed, not prestige or nominal resolution. Compare:

- sequencing versus in situ microscopy-based chemistry;
- whole-transcriptome capture versus targeted panel;
- fresh-frozen versus FFPE compatibility and tissue consumption;
- spot/bin, single-cell, and subcellular effective resolution;
- sensitivity, specificity, diffusion/spillover, dynamic range and false discovery;
- assay-native nuclear and membrane channels, segmentation support, transcript assignment and morphology;
- field size, throughput, multi-section design, cost, failure rate, batch/site reproducibility and
  compatibility with downstream pathology registration; only when
  `study_scope == imaging-mechanism`, also check radiology registration compatibility.

For targeted platforms, perform a panel sufficiency test before procurement: marker redundancy,
cell-state separability, ligand and receptor pairing, tumour and stromal coverage, housekeeping and
negative controls, isoform ambiguity, and whether the planned model was trained on the same panel.

### Review

Use matched, tissue-relevant benchmarks where possible. Audit platform and chemistry version, probe
design, serial-section allocation, tissue microarray versus whole-section sampling, reference assays,
manual pathology review, software version and metric definitions. Do not accept a single composite
rank that hides opposing sensitivity, specificity, segmentation and morphology trade-offs.

Reproducibility review must include within-run, between-run and between-site controls; standardized
positive and negative samples; panel lot; section order; site/operator; and a plan for comparing new
data with a touchstone distribution.

### Interpret and decide

Platform performance is multidimensional and context specific. Higher transcript counts may coexist
with different specificity or segmentation errors. A platform that is optimal for broad discovery
may be unsuitable for an FFPE validation panel, subcellular localization, clone inference, or whole-
lesion morphology.

### PASS / CONDITIONAL / STOP

- **PASS:** tissue format, panel, effective resolution and all decision-critical metrics are matched
  to the estimand; versions and controls are recorded; cross-site or replicate performance is
  acceptable.
- **CONDITIONAL:** the platform can support a coarser or narrower claim, but panel gaps, mixture,
  sensitivity or version mismatch limits cell state, CCC, or subcellular inference.
- **STOP:** the biological target is unmeasured, negative controls fail, sample format is unsupported,
  resolution is claimed from marketing rather than data, or platform identity/version is unknown.

### Repair or help

Run a pilot on representative tissue, add orthogonal protein or RNA markers, redesign the panel,
increase marker redundancy, include matched serial sections and standardized controls, or lower the
estimand from cell/subcellular to spot/domain level. Preserve tissue for an independent validation
assay before exhausting the block.

### Hard constraints

- Do not call a platform universally best from one tissue, panel or vendor version.
- Do not compare platforms on different gene universes without a matched-gene analysis.
- Serial sections are matched specimens, not same-cell ground truth.
- Technical metric PASS does not establish biological interpretation PASS.

### Writing four-part contract

- **Methods:** report tissue handling, section allocation, platform/chemistry/software version,
  panel/probe design, effective unit, depth/exposure, controls and replicate/site design.
- **Results:** present metric-specific sensitivity, specificity, SNR, FDR, diffusion, segmentation,
  annotation and reproducibility with uncertainty; explain the chosen trade-off.
- **Figure legend:** name platform, version, tissue, section, panel and whether genes/regions are
  matched across comparisons.
- **Discussion:** limit transfer to tested tissues and versions; state which intended analyses remain
  underpowered or panel limited.

**Evidence:** ST01–ST04, ST09, ST20.

## Decision block 3 — spatial QC and tissue integrity

### Expand

Create separate QC layers for specimen, assay-native microscopy/histology, molecule, spot/bin, cell,
gene, field, section, run
and site. At minimum assess:

- tissue folds, tears, detachment, compression, decalcification, necrosis, hemorrhage, edge and dry
  artifacts, background and off-tissue signal;
- library size or transcript count, detected features, blank probes/codewords, negative-control
  signal, sensitivity, specificity, SNR, mapping, duplicate/UMI behaviour and panel dropout;
- local and regional spatial outliers, barcode effects, hangnails, dryspots, diffusion/spillover and
  section-to-section discontinuity;
- segmentation and transcript-assignment quality, tissue mask, morphology, cell size, nuclear/cell
  ratio, molecules per cell and unassigned molecules;
- sample, run, site, lot and platform-version effects without forcing biological regions to mix.

Keep global QC distributions and maps. A value that is extreme globally may be expected in a true
necrotic, fibrotic, adipose, immune-dense or highly transcriptional spatial region.

### Review

Overlay every QC flag on raw morphology and pathology annotation. Review removed and retained areas,
the number and fraction of molecules/spots/cells affected per patient, and whether artifact burden is
associated with outcome, condition, site or morphology stratum. When
`study_scope == imaging-mechanism`, also audit association with the radiology habitat. Verify that
thresholds were not tuned to maximize a desired spatial pattern.

For multisite microscopy-based assays, compare samples to standardized metric distributions and review cross-
site dynamic range, SNR, FDR and annotation congruence. For targeted panels, inspect each critical
gene rather than accepting only an aggregate panel score.

### Interpret and decide

QC is a measurement model, not cosmetic filtering. Spatial artifacts can produce coherent domains,
gradients or apparent interaction zones. Conversely, indiscriminate global filtering can erase real
local biology. A result is interpretable only when it is stable to defensible QC choices and not
explained by tissue damage or assay geometry.

### PASS / CONDITIONAL / STOP

- **PASS:** specimen and spatial artifacts are mapped, thresholds are prespecified or justified,
  attrition is sample balanced, controls pass, and key findings survive defensible QC sensitivity.
- **CONDITIONAL:** processed data support limited interpretation, but raw molecule/microscopy audit or one
  artifact class is unavailable; downgrade the affected claims and preserve sensitivity analyses.
- **STOP:** sample identity is uncertain, control probes fail broadly, artifact overlaps the entire
  target region, condition is confounded with run/site damage, or filtering creates the finding.

### Repair or help

Recover raw microscopy/histology or molecules, re-mask tissue with pathology review, use spatially aware local and
regional outlier detection, repeat key analyses across threshold grids, include artifact covariates,
drop irreparable sections at the patient-analysis level, and acquire replacement sections when the
target is not observable.

### Hard constraints

- Never copy scRNA-seq mitochondrial or library-size thresholds without tissue-aware justification.
- Never remove a spatial region solely because it is locally unusual.
- Always report section- and patient-level attrition; hidden cell/spot loss can bias composition.
- QC performed after seeing the clinical outcome belongs to discovery unless independently locked.

### Writing four-part contract

- **Methods:** define QC metrics at every layer, thresholds, local neighbourhood, artifact rules,
  pathology review, controls, attrition and sensitivity analyses.
- **Results:** report control performance, artifact maps, patient-wise attrition and stability of
  major conclusions before and after QC.
- **Figure legend:** show raw/filtered status, QC variable and threshold, tissue mask and number of
  patients/sections represented.
- **Discussion:** state residual blind spots, possible removal of true spatial biology and any
  outcome-associated missingness.

**Evidence:** ST01–ST04, ST06, ST08.

## Decision block 4 — segmentation, transcript assignment, and cell identity

### Expand

Decide whether the estimand requires cells at all. Available routes include microscopy-defined cells,
transcript-defined cells, multimodal boundaries, probabilistic boundaries, fixed bins, spots, and
segmentation-free factors. For cell-level analysis, record microscopy channels, nuclear/cell markers,
algorithm and version, parameters, size/shape priors, overlapping or multinucleated cells,
unassigned molecules and the treatment of boundary molecules.

Plan uncertainty propagation before choosing downstream analyses. At minimum compare an alternative
segmentation or assignment rule, quantify changed molecules and cells, and repeat priority cell-state,
DE, neighbourhood and CCC results. Where boundaries are not credible, use factors or regional
estimands rather than inventing cells.

### Review

Inspect raw molecules over boundaries in multiple tissue types and difficult regions. Review cell
size, molecules per cell, within-cell expression coherence, expected marker combinations, apparent
doublets, zero-molecule cells, fragmented or merged cells and spatially structured unassigned signal.
Compare morphology-only, transcript-only, multimodal or segmentation-free results where defensible.

Do not judge segmentation only by visual plausibility. Review downstream stability because subtle
misassignment can dominate differential expression, neighbour effects and ligand-receptor analysis.

### Interpret and decide

Cell boundaries and identities are estimates. Better segmentation may uncover difficult immune cells,
but a model-inferred boundary is not ground truth. Segmentation-free factors preserve fine spatial
structure but are not cells. Cell assignment and annotation uncertainty should be carried into the
claim, not discarded after creating a count matrix.

### PASS / CONDITIONAL / STOP

- **PASS:** boundaries or factors are appropriate to the estimand; assignment diagnostics pass;
  alternative-boundary results are stable; uncertain cells remain labelled or excluded transparently.
- **CONDITIONAL:** one defensible segmentation exists but rare cells, tumour borders or subcellular
  claims are unstable. Restrict interpretation to robust domains or coarse cell classes.
- **STOP:** boundary errors dominate the target result, recovered cells are called observed, or no
  credible representation supports the requested cell-level inference.

### Repair or help

Re-segment with additional membrane channels or multimodal/transcript information, apply a correction
for local molecular admixture, compare Proseg-like and platform-default boundaries, use a
segmentation-free factor analysis, merge unstable subtypes, or lower the claim to spot/bin/domain
resolution. Store a molecule-to-cell reassignment table.

### Hard constraints

- A segmentation algorithm output is never a direct cell truth.
- Any cell-level DE, neighbourhood or CCC claim must report segmentation sensitivity.
- Segmentation-free factors, reconstructed cells and assigned cell types require distinct labels.
- Correction cannot recover the true origin of every lost or misassigned molecule.

### Writing four-part contract

- **Methods:** state microscopy channels, algorithm/version, parameters, boundary/assignment rules,
  unassigned molecules, alternatives, correction and stability analyses.
- **Results:** report assignment yield, boundary diagnostics, affected molecules/cells and downstream
  stability; separate robust and segmentation-sensitive conclusions.
- **Figure legend:** identify boundary source, whether cells/factors are observed or inferred, and
  which segmentation generated each panel.
- **Discussion:** name tissues and cell types with weak boundaries and limit cell-level, CCC and
  subcellular conclusions accordingly.

**Evidence:** ST05, ST07–ST09, ST20–ST23.

## Decision block 5 — coordinates, tissue registration, and spatial provenance

### Expand

Construct the coordinate chain before testing a local association. Distinguish molecule coordinates,
segmentation coordinates, spot/bin centres, tissue pixels, pathology regions, serial-section space,
and 3D reconstruction space. Only when `study_scope == imaging-mechanism`, append radiology voxels.
For each applicable transformation record source and target space, units, orientation, scaling,
cropping, mirroring, fiducials/landmarks, rigid or deformable model, interpolation,
software/version, operator input and uncertainty.

Define the spatial support of the estimand. A cell-to-cell contact, distance to an invasive front
and pathology-region burden have different tolerable registration errors. When
`study_scope == imaging-mechanism`, also define the radiology-habitat scale and use patient-level
association when that mapping cannot support local co-localization.

### Review

Trace several blinded landmarks end to end. Inspect overlays at tissue boundaries, folds, necrosis,
small vessels, glands and tumour–stroma interfaces. Report landmark residuals and local deformation,
not only a global correlation or attractive overlay. Check whether registration was tuned after
viewing molecular or clinical outcomes and whether adjacent sections contain the same anatomy.

For multi-slice or 3D work, review section order, thickness, spacing, missing sections, tissue loss,
z-axis scaling and whether interpolated slices influenced alignment. For tissue/pathology linkage,
verify specimen, section, orientation and sampling trajectory. Only when
`study_scope == imaging-mechanism`, also verify patient, lesion, radiology acquisition, treatment
interval and biopsy trajectory.

### Interpret and decide

Registration uncertainty sets the maximum spatial claim. Accurate specimen/section matching can
support a tissue-region association even when cellular co-localization is impossible. Only when
`study_scope == imaging-mechanism`, accurate patient/lesion matching may support a sample-level
molecular–imaging association despite coarse local registration; high-resolution molecular data do
not rescue coarse, deformed or unmatched radiology imaging.

### PASS / CONDITIONAL / STOP

- **PASS:** the full coordinate transform is reproducible; blinded landmark error is small relative
  to the spatial effect; uncertainty is propagated into region/distance sensitivity.
- **CONDITIONAL:** patient and lesion match, but local registration is coarse or adjacent-section
  deformation is substantial. Restrict to patient-, lesion- or broad-region association.
- **STOP:** patient/lesion identity is uncertain, orientation cannot be recovered, transformations
  are unavailable, or a local effect is smaller than unbounded registration error.

### Repair or help

Recover original images and transforms, add fiducial or anatomy landmarks, use pathology-guided
registration blinded to outcome, quantify error with held-out landmarks, dilate/erode regions over a
plausible error range, aggregate to larger habitats, or reframe the claim at patient level.

### Hard constraints

- “Alignment-free integration” is not physical registration.
- Adjacent or serial sections are not the same cells and may not contain identical microanatomy.
- Do not report micron-scale co-localization when registration error is unmeasured or coarser.
- Never tune a tissue registration to maximize the tested molecular association in the same cohort.
  When `study_scope == imaging-mechanism`, this prohibition also covers molecular–radiology
  association.

### Writing four-part contract

- **Methods:** provide coordinate spaces, transformation sequence, units, landmarks, model,
  interpolation, software, blinding, residual metric and sensitivity range.
- **Results:** report landmark error distribution, failed/removed sections and association stability
  across region perturbations or aggregation scales.
- **Figure legend:** name coordinate space, section relation, registration method, scale bar and
  whether the overlay is measured, transformed or interpolated.
- **Discussion:** state the finest supportable spatial scale and how mismatch or deformation could
  explain the finding.

**Evidence:** ST01–ST03, ST10–ST11, ST16, ST24, ST27, ST32–ST33.

## Decision block 6 — domains, gradients, SVGs, and subcellular expression

### Expand

Route the target before selecting a method:

1. **Domain:** a categorical or probabilistic tissue compartment.
2. **Continuous gradient:** expression or composition as a function of a prespecified spatial axis,
   boundary or distance.
3. **Overall SVG:** any spatial variation in a gene across the assayed tissue.
4. **Cell-type-specific SVG:** spatial expression variation within a declared cell type.
5. **Spatial-domain-marker SVG:** a feature distinguishing a spatial domain.
6. **Subcellular localization:** transcript point pattern within a cell coordinate system.

Declare the feature universe, spatial unit, distance/adjacency, covariates, sample structure, null,
effect size and multiplicity family. Preserve continuous topic/gradient scores even when a categorical
summary is needed. For subcellular analysis, include cell shape, polarity, compartment, cell cycle,
segmentation and localization error.

### Review

Audit domain number and stability across seeds, resolutions, patients, section orientation and
segmentation. Compare spatial and non-spatial baselines. Verify that histological gradients were
prespecified, span comparable ranges across samples and are not proxies for library size, tissue
edge, necrosis or batch.

For SVGs, check whether the method targets the requested category and whether cell composition was
mistaken for within-cell-type expression. Inspect type I error evidence, spatial permutation/null,
multiple testing and patient consistency. For subcellular claims, inspect raw molecule locations,
boundary uncertainty and results after shape/cycle stratification.

### Interpret and decide

A domain is a useful representation, not an anatomical truth. A topic is not a cell type. An SVG
may reflect cell composition, technical geometry or a true within-cell program depending on the
estimand. Subcellular enrichment locates RNA but does not establish transport, translation or
retention mechanism.

### PASS / CONDITIONAL / STOP

- **PASS:** estimand category, null and multiplicity are explicit; patterns replicate across patients
  or held-out sections; morphology/markers support interpretation; segmentation and QC sensitivity
  are acceptable.
- **CONDITIONAL:** a reproducible exploratory pattern exists but category, patient replication,
  domain resolution or boundary uncertainty restricts the claim.
- **STOP:** a method tests the wrong SVG category, one section supplies all inference, spatial
  artifact explains the pattern, or subcellular localization rests on unreliable segmentation.

### Repair or help

Rewrite the estimand, switch to a category-appropriate model, add sample-level random/fixed effects,
use tissue-aware permutations, repeat domain resolution and seed grids, model a continuous gradient,
  adjust or stratify composition, validate with pathology, RNA-FISH or another in situ assay, and
  merge unsupported domains.

### Hard constraints

- Do not use the generic phrase “spatially variable” without naming the SVG category and unit.
- Do not infer ct-SVG from spot data without composition uncertainty.
- Do not convert a topic/factor/domain into a new biological entity solely from marker enrichment.
- Subcellular association does not prove an RNA localization mechanism.

### Writing four-part contract

- **Methods:** define domain/gradient/SVG/localization estimand, coordinates, unit, null, covariates,
  patient model, parameters, stability, feature universe and multiplicity.
- **Results:** report effect surfaces or scores, intervals, patient consistency, stability and
  orthogonal support rather than only a coloured map.
- **Figure legend:** state categorical versus continuous, all three evidence axes, spatial unit,
  colour scale, sample count, test and correction.
- **Discussion:** separate tissue organization, composition and within-cell explanations; state
  unresolved domain and mechanism ambiguity.

**Evidence:** ST05, ST10, ST13, ST18–ST20, ST24.

## Decision block 7 — deconvolution, cell reconstruction, and scRNA-to-space mapping

### Expand

Separate four tasks:

- **spot deconvolution:** estimates cell-type fractions per spot;
- **cell-type-specific expression recovery:** estimates expression attributable to a type;
- **cell reconstruction/assignment:** infers cells or assigns molecules to cells using histology or
  other evidence;
- **scRNA-to-space mapping/imputation:** maps dissociated states or unmeasured genes into space.

For each task record the reference, label hierarchy, marker genes, count scale, feature overlap,
normalization, transcriptome-size correction, unknown-state policy, tumour and rare-state coverage,
  spatial prior, histology/morphology use and uncertainty. Decide whether output is for visualization
  or formal testing.

### Review

Check reference-to-query tissue, condition, patient, platform and panel shift. Review absent and novel
states, marker specificity, malignant-state diversity, rare-population detectability, compositional
identifiability and sensitivity to reference/marker perturbation. Compare coarse and fine labels,
reference-free or simple marker baselines, and any matched single-cell-resolution or in situ truth.

For reconstructed cells, review nuclear gaps, multi-/non-nucleated cells and histology-expression
alignment. For mapped or imputed genes, hold out measured genes and samples and assess calibration,
not only correlation.

### Interpret and decide

Fractions, recovered cells, mapped labels and imputed expression are different estimates. Mapping a
scRNA state to a location does not observe that cell. Good average concordance can hide failure for
rare or malignant states. Formal testing must propagate or at least stress-test reference and
composition uncertainty.

### PASS / CONDITIONAL / STOP

- **PASS:** reference and feature support are adequate; unknown states are handled; held-out or
  orthogonal validation passes; key effects are stable across reference/marker choices.
- **CONDITIONAL:** coarse composition is supported but subtype, cell-level or imputed-gene inference
  is uncertain. Limit claims to robust classes or visualization.
- **STOP:** key state is absent from reference/panel, reconstructed cells are represented as observed,
  imputed-only features drive a biomarker without measured validation, or reference leakage invalidates
  the test.

### Repair or help

Build a tissue/condition-matched reference, add an unknown state, collapse labels, correct count-scale
and transcriptome-size mismatch, perturb markers and reference donors, compare multiple methods,
validate with in situ markers, or return spot/domain-level results. Keep separate matrices and
metadata for measured and inferred layers.

### Hard constraints

- Never describe deconvolved fractions, recovered cells, mapped labels or imputed genes as observed.
- Do not use the same patient/adjacent section as both tuning data and an “independent” validation.
- Rare-state claims require detectability and orthogonal validation, not only a high posterior score.
- ct-SVG or CCC based on deconvolution inherits its uncertainty.

### Writing four-part contract

- **Methods:** report reference patients/tissue/platform, labels, feature overlap, normalization,
  model/version, priors, unknown-state policy, uncertainty and validation.
- **Results:** give reconstruction/deconvolution accuracy, reference sensitivity, rare-state
  performance and patient-wise effects; label all generated values.
- **Figure legend:** distinguish observed spots/cells from fractions, mapped cells, reconstructed
  cells and imputed genes; state reference and resolution.
- **Discussion:** state reference shift, identifiability, rare-state and non-observation limits.

**Evidence:** ST09, ST12, ST16–ST17, ST19.

## Decision block 8 — niches, neighbourhoods, co-localization, and cell-cell communication

### Expand

Define the graph and the null before calculating enrichment. Specify cell/spot unit, segmentation,
distance metric, radius or k, contact versus diffusion, tissue mask, barriers, edge correction,
cell-density/composition conditioning, patient aggregation and multiple testing.

Separate the following outputs:

- cell-type co-occurrence or avoidance;
- neighbourhood/community abundance or architecture;
- distance-to-boundary or sender analysis;
- ligand–receptor compatibility;
- multiple-sender effects or information flow;
- putative relay network;
- functionally corroborated signaling, with any direct intervention recorded as `perturbed`.

For CCC, record ligand-receptor database/version, expression threshold, complex handling, direction,
spatial kernel, negative controls, segmentation sensitivity and any proximity or perturbation assay.

### Review

Inspect whether a finding survives tissue-aware nulls that preserve morphology, density and cell-type
abundance. Compare radii and boundary definitions without cherry-picking. Review patient consistency,
section effects, segmentation/cell assignment, rare-population counts and whether one large tissue
dominates. For directed or relay models, compare simpler proximity and LR baselines and alternative
network orders.

### Interpret and decide

Co-localization means the observed arrangement differs from a declared null. Ligand and receptor
expression plus proximity supports compatibility, not signaling. Modelled sender effects, dynamics
or relay paths remain hypotheses until a proximity assay, perturbation, receptor blockade, rescue or
equivalent functional experiment supports them.

### PASS / CONDITIONAL / STOP

- **PASS:** graph and spatial null are appropriate; effects replicate at the patient level; results
  are stable to radius/segmentation; priority signaling has orthogonal or perturbational support.
- **CONDITIONAL:** robust co-occurrence or modelled CCC exists without functional validation. Use
  “associated,” “compatible,” “putative,” or “prioritized.”
- **STOP:** independence is assumed for neighbouring cells, no spatial null is used, one section
  supplies the p value, or proximity/attention is called causal signaling.

### Repair or help

Use conditional randomization or toroidal/label permutations appropriate to tissue geometry, model
patient-level niche burden, vary radius and segmentation, include negative-control pairs, perform
proximity ligation/multiplex microscopy, perturb sender/receiver or pathway, and reduce the claim from
signaling to spatial compatibility when functional work is unavailable.

### Hard constraints

- A neighbourhood enrichment test requires a declared tissue-aware spatial null.
- Patient-level conclusions require patient-level replication.
- Attention weights and inferred temporal LR dynamics are not mechanisms.
- Deconvolution, imputation and segmentation uncertainty must be named in CCC conclusions.

### Writing four-part contract

- **Methods:** define graph, radius, barriers, null/permutation, database, direction, sample model,
  multiplicity, sensitivity and validation assay.
- **Results:** report effect sizes, intervals, donor consistency, radius/segmentation stability,
  negative controls and functionally corroborated subset, with the primary evidence state explicit.
- **Figure legend:** state graph, unit, radius, null, whether edges are inferred or validated and the
  patient/section denominator.
- **Discussion:** distinguish co-location, compatibility, predicted communication and functionally
  corroborated signaling; list alternative density/composition explanations.

**Evidence:** ST08, ST21–ST23, ST29–ST31.

## Decision block 9 — histology-to-expression, imputation, and super-resolution

### Expand

Classify the task as registration, retrieval, annotation, cell decomposition, measured-gene
imputation, unmeasured-gene imputation, expression prediction from histology, spatial
super-resolution, cell reconstruction, or virtual slicing. Declare which measured data supervise the
model and which outputs will be used for inference.

Require a baseline ladder: morphology-only linear or nearest-neighbour baseline, simple gene/spot
interpolation or mapping, task-specific model, and foundation/deep model. Split by patient and block;
adjacent patches or sections from one patient must not cross training and test. Audit pretrained-corpus
overlap and staining/scanner/domain shift.

### Review

Evaluate held-out measured genes, regions, sections, patients, tissues and platforms as appropriate.
Report calibration and spatial residuals, not only Pearson correlation. Inspect boundary, rare-state,
low-expression and OOD performance. Determine whether downstream SVG, domain, DE or CCC gains persist
when restricted to measured genes and whether the model merely learns tissue morphology.

### Interpret and decide

Histology can predict or prioritize molecular programs but cannot substitute for measured spatial
expression. Imputation increases apparent completeness, not information certainty. Super-resolved
spots, virtual cells and slices are generated layers whose resolution is bounded by training data,
assumptions and measured validation.

### PASS / CONDITIONAL / STOP

- **PASS:** patient-level held-out measured validation passes against simple baselines; calibration
  and OOD error are reported; generated layers remain explicit and do not leak into validation.
- **CONDITIONAL:** the model supports visualization, retrieval or hypothesis prioritization but lacks
  external tissue/platform validation or fails for rare/boundary regions.
- **STOP:** patch leakage exists, predictions are presented as measurements, imputed-only genes drive
  a clinical claim without measured validation, or no meaningful baseline/holdout is available.

### Repair or help

Re-split by patient/block, audit corpus overlap, reserve measured genes/sections, add simple baselines,
calibrate uncertainty, map spatial error, validate in an external tissue/platform, restrict downstream
testing to measured features, or relabel the output as exploratory prediction.

### Hard constraints

- Never call H&E-predicted expression spatial transcriptomics data.
- No random tile split when tiles from the same patient or section can leak.
- Virtual resolution cannot be reported as experimental resolution.
- Generated layers require separate storage, metadata, plotting and writing labels.

### Writing four-part contract

- **Methods:** report measured inputs, target, model/pretraining, patient-level splits, overlap audit,
  baselines, calibration, OOD tests and generated-layer use.
- **Results:** give baseline-relative held-out metrics, spatial residuals, calibration and failures;
  separate measured-only and generated-layer downstream analyses.
- **Figure legend:** label predicted, imputed, reconstructed, super-resolved or virtual panels and
  identify the measured validation source.
- **Discussion:** state non-measurement, domain shift, leakage safeguards and prospective validation
  required before biomarker or mechanism claims.

**Evidence:** ST11–ST12, ST16, ST24, ST27.

## Decision block 10 — multi-sample integration, 3D reconstruction, and spatiotemporal inference

### Expand

Name the integration objective: comparable visualization, shared-domain discovery, condition-
specific domain testing, cross-platform transfer, 3D physical reconstruction, time-series
trajectory, or spatial velocity. Do not use one integrated embedding for every objective.

For multi-sample analysis, preserve patient, condition, section, site, platform, panel and batch.
Define shared and condition-specific signals before integration. For 3D, record section order,
thickness, spacing, orientation, missing tissue and measured versus virtual slices. For time, separate
measured longitudinal or destructive time points, pseudospatial order, optimal-transport trajectory,
RNA/spatial velocity and true lineage tracing.

### Review

Audit biological conservation and batch removal together. Review unintegrated and integrated data,
condition separability, sample mixing, rare-state preservation, leave-one-patient/platform-out
transfer, domain/topic stability and whether the model was trained on overlapping tissues.

For 3D, validate on measured held-out sections and map error by distance from measured tissue. For
trajectories, inspect time coverage, transport-cost sensitivity, population growth/death assumptions,
kinetic fit and direction stability. Compare non-spatial and simple alignment/trajectory baselines.

### Interpret and decide

Good integration removes unwanted variation while retaining biological contrasts; batch mixing alone
is insufficient. A 3D atlas can combine measured and interpolated anatomy, but virtual sections remain
predictions. Spatial trajectory or velocity suggests a transition compatible with the data and model;
it does not observe ancestry, migration or time.

### PASS / CONDITIONAL / STOP

- **PASS:** integration preserves declared biology and generalizes to held-out samples; 3D or temporal
  outputs pass measured holdouts and sensitivity analyses; measured and generated layers are distinct.
- **CONDITIONAL:** shared architecture is stable, but condition-specific, fine 3D, rare-state or
  directional conclusions lack enough samples or validation.
- **STOP:** integration erases the target contrast, patient/condition is confounded with platform,
  virtual slices are treated as samples, or pseudotime/velocity is called lineage or migration.

### Repair or help

Use a simpler sample-aware representation, integrate only for visualization, test on unintegrated
pseudobulk/domain summaries, add condition-preserving objectives, hold out patients/platforms, reserve
measured slices, increase section density, collect real time points, or seek lineage/perturbation data.

### Hard constraints

- Do not evaluate integration by batch mixing alone.
- Do not include virtual slices as independent biological replicates.
- A cross-sectional spatial gradient is not a time series.
- Velocity arrows and optimal-transport paths are not observed lineage or migration.

### Writing four-part contract

- **Methods:** state integration objective, covariates, model/version, patient splits, preservation
  metrics, section geometry, holdouts, temporal model and assumptions.
- **Results:** report batch removal and biological preservation, leave-one-sample-out stability,
  measured-section reconstruction error and trajectory/velocity diagnostics.
- **Figure legend:** identify sample/platform/time, integrated status, measured or virtual section,
  inferred direction and patient denominator.
- **Discussion:** state overcorrection, missing-tissue, interpolation, destructive-time and kinetic
  assumptions; separate architecture from lineage.

**Evidence:** ST13–ST15, ST24–ST27, ST32–ST33.

## Decision block 11 — spatial perturbation and lineage tracing

### Expand

Classify the evidence:

1. observed genetic or pharmacologic perturbation with spatial transcriptomic readout;
2. pooled spatial CRISPR screen with in situ guide assignment;
3. observed clone/barcode plus spatial expression;
4. transcriptomic similarity used as a lineage proxy;
5. model-predicted perturbation or virtual knockout.

For observed perturbations, define guide/drug, target, assignment confidence, efficiency, off-target
assessment, non-targeting/positive controls, density and neighbourhood, time, functional readout,
biological replicate and guide-by-context estimand. For lineage, define barcode design, diversity,
collision, dropout, assignment, clone size, fitness effects and relation to spatial location.

### Review

Inspect guide/barcode calls at the molecule and cell level, multiple guides, low-confidence cells,
perturbation efficiency, target engagement, off-target or stress programs, replicate consistency and
whether spatial density or clone size confounds effects. Compare perturbation effects with conventional
Perturb-seq or other measured readouts where available.

For clone/environment separation, fit clone and location jointly and test clone-by-neighbourhood
effects. Do not infer clone identity from expression similarity when a barcode or mutation is absent.

### Interpret and decide

Spatial perturbation can support causal effects within the experimental model when assignment,
controls and target engagement are sound. It does not automatically establish human tissue relevance.
A measured barcode supports shared ancestry within collision/dropout limits; a transcriptional
trajectory or similar state does not.

### PASS / CONDITIONAL / STOP

- **PASS:** guide/barcode identity, controls, target engagement and biological replication pass;
  context effects are prespecified or validated; causal language is bounded to the model.
- **CONDITIONAL:** perturbation or clone association is real but guide efficiency, barcode recovery,
  model transfer or mechanism is incomplete. Use association or model-specific causal language.
- **STOP:** predicted knockout is presented as an experiment, guide/barcode identity is unreliable,
  no valid controls exist, or expression similarity is called lineage.

### Repair or help

Add independent guides, non-targeting and positive controls, target-engagement assays, off-target
analysis, replicate models, barcode-collision estimation, clone-size adjustment, functional readouts,
receptor/pathway blockade or rescue, and human/orthogonal tissue validation. Relabel virtual knockout
as a prediction and compare it with measured perturbations.

### Hard constraints

- Predicted perturbation is never an observed spatial perturbation.
- Causal claims require intervention, assignment, controls and a bounded experimental context.
- Barcode dropout or collision must be quantified before clone comparisons.
- Transcriptional similarity, velocity or proximity cannot substitute for lineage identity.

### Writing four-part contract

- **Methods:** report guide/barcode library, assignment thresholds, controls, efficiency, off-targets,
  replicates, spatial model, clone collision/dropout and functional validation.
- **Results:** report target engagement, guide-level concordance, context interaction, clone recovery,
  uncertainty and validated mechanism; separate predicted analyses.
- **Figure legend:** label perturbation or barcode status, assignment confidence, model, replicate,
  spatial context and whether an effect is observed or predicted.
- **Discussion:** restrict causality to the tested system; state guide/barcode, density, clone-size,
  temporal and human-transfer limits.

**Evidence:** ST25, ST29–ST31.

## Decision block 12 — RNA-derived CNA, clones, and tumour phylogeography

### Expand

Decide whether the data support total-copy pattern, allele-specific CNA, copy-neutral LOH, mutation-
defined clone, barcode-defined clone, spatial clone assignment, or a phylogeographic tree. Record
tumour and normal regions, purity, allele counts, informative SNPs, reference normal, expression
bias, coverage, section geometry and available DNA, mutation, FISH or lineage validation.

For a clone-by-niche question, prespecify clone identity independently of the neighbourhood where
possible. Distinguish clone prevalence, spatial segregation, neighbourhood association and evidence
that a niche changes clone fitness or neoplastic outcome.

### Review

Inspect allelic depth, reference bias, normal admixture, subclonal sensitivity, segmentation and
deconvolution effects, consistency across adjacent sections and plausible tree alternatives. Compare
total-copy baselines and assess how purity or breakpoint choices change clones. Verify key events and
clone identity with DNA sequencing, mutation assays, FISH or lineage tracing.

### Interpret and decide

RNA provides indirect evidence about genomic state. Allele-specific modelling can prioritize CNAs,
LOH and spatial clones, but the output remains RNA-inferred until orthogonally measured. Spatially
associated clones and niches suggest selection hypotheses; they do not prove evolutionary causality
without temporal, lineage or perturbational evidence.

### PASS / CONDITIONAL / STOP

- **PASS:** allelic support, purity sensitivity and spatial consistency pass; priority CNA/clone is
  validated by DNA/mutation/FISH/barcode; the phylogeographic claim matches the evidence.
- **CONDITIONAL:** broad tumour/normal or major clone structure is stable but fine subclones, tree
  order or niche selection lacks orthogonal support.
- **STOP:** RNA-derived CNA is called a measured mutation/genome, purity/reference is unavailable,
  clones are defined by the same neighbourhood used to test association, or the tree is non-identifiable.

### Repair or help

Add matched normal and DNA data, increase allelic coverage, use mutation or FISH validation, perturb
purity and breakpoints, merge unstable clones, compare alternative trees, repeat across sections and
patients, and downgrade phylogeny to a spatial clonal hypothesis when ordering is unresolved.

### Hard constraints

- RNA-derived CNA and clone labels must remain explicitly inferred until orthogonally verified.
- Total expression shifts alone cannot establish allele-specific CNA or LOH.
- Spatial separation does not establish clone ancestry or direction of evolution.
- A niche–clone association is not a selection mechanism without additional evidence.

### Writing four-part contract

- **Methods:** report allelic/mutation inputs, reference, purity, coverage, model/version, breakpoint
  and tree assumptions, section relation, sensitivity and orthogonal validation.
- **Results:** provide event/clone uncertainty, purity stability, section/patient consistency,
  alternative trees and validated subset.
- **Figure legend:** label RNA-inferred versus DNA/barcode-observed clones, section geometry and tree
  uncertainty.
- **Discussion:** bound claims about LOH, ancestry, evolution and niche selection; identify the DNA,
  temporal or perturbational experiment still needed.

**Evidence:** ST28–ST31.

## Decision block 13 — optional radiology linkage

Use this block only when `study_scope == imaging-mechanism`. Skip it for mechanism-only spatial
transcriptomics; assay-native microscopy, histology, pathology regions and tissue registration remain
covered by blocks 2–5 and do not require radiology data.

### Expand

Use a staged linkage rather than jumping from a molecular heatmap to an imaging biomarker:

1. establish a sample-level measured molecular program;
2. localize its cellular source using measured or clearly estimated cell evidence;
3. localize its tissue niche with spatial/pathology evidence;
4. register that niche to an imaging habitat at a justified spatial scale;
5. test the association at the patient/lesion level;
6. lock the feature, mapping and threshold and validate in unseen patients.

Record patient, lesion, block, section, biopsy trajectory, orientation, anatomical region, acquisition
date, treatment interval, radiology sequence, pathology stain, feature extraction, habitat definition,
registration and whether imaging covers the entire lesion while molecular data sample only a section.

### Review

Audit same-patient, same-lesion, same-region and same-time linkage; tissue sampling geometry; tumour
heterogeneity; image preprocessing and feature stability; outcome and registration leakage; patient-
level splits; lesion multiplicity; covariates; and whether the molecular signature was locked before
clinical testing. Compare patient-level and local registration analyses.

Check whether an H&E-predicted or imputed spatial layer has silently become the molecular target. For
local claims, compare registration error with habitat and niche scale. For prediction, require
calibration, comparator, external cohort and clinical endpoint definition.

### Interpret and decide

Matched patient-level data can support a molecular–imaging association even when local registration is
weak. Local co-localization requires finer evidence. A radiologic signature may be prognostic because
of tumour burden, anatomy or treatment rather than the proposed niche. Predictive treatment claims
require an explicit biomarker-by-treatment interaction and unseen-patient validation.

### PASS / CONDITIONAL / STOP

- **PASS:** patient/lesion/time mapping is traceable; local error fits the claim scale; the molecular
  layer is measured or properly qualified; patient-level association is validated independently.
- **CONDITIONAL:** patient-level association is supported but section sampling or registration blocks
  local co-localization. Use lesion-level or broad-region language.
- **STOP:** imaging and molecular data are unmatched, local claims exceed registration precision,
  generated expression is treated as measured, patient leakage exists, or prediction lacks an unseen
  cohort.

### Repair or help

Recover the sample-to-image manifest, involve pathology/radiology review, map biopsy trajectory,
aggregate to defensible habitats, quantify registration and sampling uncertainty, repeat analyses at
coarser scales, lock features and thresholds, use patient-level nested validation, acquire multi-region
tissue, and validate in an independent matched cohort.

### Hard constraints

- Same patient is necessary but not sufficient for same-region co-localization.
- One tissue section cannot represent whole-lesion heterogeneity without a sampling model.
- Image-to-expression predictions cannot serve as independent molecular validation of the same image.
- Treatment prediction requires a treatment interaction, not separate prognostic significance.

### Writing four-part contract

- **Methods:** report full sample-to-image mapping, dates, regions, sampling, registration, molecular
  layer, image features, patient split, model, covariates, endpoint, comparator and calibration.
- **Results:** report matched/failed cases, registration error, patient-level effect and interval,
  local-scale sensitivity, calibration, comparator and external validation.
- **Figure legend:** identify patient/lesion/section, imaging sequence, molecular layer, registration,
  scale, region/habitat definition and whether the overlay is measured or predicted.
- **Discussion:** separate local co-localization, patient association, prognosis, treatment prediction
  and mechanism; state sampling, registration and external-validity limits.

**Evidence:** ST01, ST03–ST04, ST10–ST11, ST24, ST27, ST29, ST32–ST33.

## Standard output contract

Return only the components relevant to the user's route, but preserve their labels and evidence
status.

1. **Scientific question and estimand** — population, contrast, spatial object, effect, inferential
   unit, claim target and validation.
2. **Sample/platform passport** — patients, lesions, sections, batches, platform/version, panel,
   tissue format, effective resolution and controls.
3. **Three-axis layer map** — every matrix, label, domain, cell, gene, edge, slice, clone and
   assay-native tissue feature with primary evidence state, modality subtype, claim-link status,
   generation method and uncertainty. Only when `study_scope == imaging-mechanism`, append radiology
   image features.
4. **Spatial QC and attrition report** — patient/section QC maps, controls, artifact burden, removed
   tissue/cells/spots/molecules and sensitivity.
5. **Coordinate and registration statement** — spaces, transforms, residuals, error range and maximum
   supportable spatial scale.
6. **Representation dictionary** — cells, factors, domains, gradients, topics and labels with
   segmentation/assignment/stability evidence.
7. **Spatial finding table** —
   `finding | estimand | unit | primary evidence state | modality subtype | claim-link status | effect | interval | patient consistency | null/test | multiplicity | sensitivity | evidence ID | claim branch | branch verdict`.
8. **Niche/CCC table** — graph, radius, null, database, effect, segmentation and radius sensitivity,
   validated subset and causal boundary.
9. **Generated-layer validation table** — target, baseline, patient split, overlap audit, held-out
   error, calibration, OOD performance and allowed use.
10. **Multi-sample/3D/time/clone table** — biological preservation, holdout, measured/virtual status,
    trajectory or clone evidence and unresolved assumptions.
11. **Radiology triangulation, only when `study_scope == imaging-mechanism`** — molecular source,
    niche, registered habitat, discordance, sampling/registration uncertainty and independent
    validation.
12. **Verdict and repair plan** — PASS/CONDITIONAL/STOP per block, global verdict, exact repair,
    author input needed and allowed wording for each selected claim branch.
13. **Reproducibility artifacts** — manifests, parameters, code/environment, seeds, transforms,
    intermediate objects, source tables and provenance hashes where available.

## Three-axis evidence record and spatial claim requirements

The evidence axes are independent; none is a rung toward another.

| Axis | Allowed values | Spatial use |
|---|---|---|
| Primary evidence state | `measured`, `derived`, `estimated`, `associated`, `predicted`, `perturbed` | molecules are measured; normalized counts or region summaries are derived; labels/domains/deconvolution/trajectories are estimated; valid sample-aware spatial effects are associated; locked held-out outputs are predicted; observed assigned spatial perturbation results are perturbed |
| Modality subtype | declared operation such as `molecule-count`, `segmentation`, `assignment`, `domain`, `SVG`, `deconvolution`, `scRNA-mapping`, `niche`, `ligand-receptor-score`, `histology-predicted-expression`, `3D-interpolation`, `RNA-CNA`, `perturbation-response` | identifies the spatial operation without promoting its evidence state |
| Claim-link status | `direct`, `inferred`, `proposed` | records how directly the result supports the sentence under review |

`missing` means that evidence is absent and belongs in the gap register, never in the primary-state
column.

| Claim branch | Minimum spatial support | Spatial STOP example |
|---|---|---|
| Descriptive | assay/QC PASS, traceable molecule/spot/cell and coordinate definition, correct nested denominator and uncertainty | generated cell, domain or slice called measured |
| Association | sample-aware effect, tissue-aware null where applicable, effect/CI, multiplicity, representation sensitivity and independent samples | spots/cells treated as patient replicates or invalid spatial null |
| Localization | direct spatial measurement or validated mapping; complete coordinate/region provenance; effective resolution and registration error compatible with the stated scale; independent/orthogonal confirmation | locality asserted below segmentation, diffusion, section or registration precision |
| Prediction | locked target/mapping/model, patient-level split, simple baseline, unseen measured-data evaluation, calibration and OOD/section/site transport | adjacent-section or tile leakage, or generated target used as its own validation |
| Treatment effect or effect modification | treatment comparator, explicit treatment-by-biomarker interaction or identified causal contrast, time zero, allocation/confounding strategy, spatial effect/CI and independent confirmation | one-arm spatial response relabelled as treatment benefit |
| Mechanistic | competing hypotheses, directional cell/context chain, temporal compatibility, target engagement, mediator/pathway and phenotype readouts, spatially indexed perturbation or strong orthogonal triangulation, alternative-mechanism tests | proximity, ligand-receptor, attention, velocity or clone association alone called mechanism |
| Causal | explicit causal estimand; randomized perturbation or defended exchangeability/positivity/consistency; reliable guide/barcode/exposure assignment; temporal order; interference/context model; negative controls/sensitivity and rescue where applicable | observational co-localization, inferred lineage or predicted counterfactual alone |

Report `PASS / CONDITIONAL / STOP` for every invoked branch and the shortest unmet requirement in
that branch. Prediction, treatment effect, localization, mechanism and causality are distinct routes;
there is no single highest spatial grade.

## Reviewer checklist

### Question and samples

- Is the spatial estimand explicit and distinct from a descriptive map?
- Are patients, lesions, blocks, sections and fields distinguished?
- Are cells/spots/sections incorrectly used as independent patient replicates?
- Were regions, radii, thresholds and models selected without outcome leakage?

### Platform and QC

- Are platform, chemistry, panel, software and segmentation versions reported?
- Is effective rather than advertised resolution used in claims?
- Are negative/positive controls, sensitivity, specificity, diffusion and panel gaps reported?
- Are local and regional artifacts overlaid on histology and is attrition patient specific?
- Is the result stable to defensible QC thresholds?

### Segmentation, coordinates, and registration

- Are boundaries or segmentation-free factors appropriate and clearly labelled?
- Is segmentation uncertainty propagated into DE, neighbourhood and CCC analyses?
- Are coordinate transforms, units, landmarks and residual errors reproducible?
- Does the claimed co-localization scale exceed registration or section mismatch?

### Spatial inference

- Is SVG category, domain, gradient or subcellular estimand named?
- Is the spatial null appropriate to tissue geometry and composition?
- Are patient-level effects, intervals and multiplicity reported?
- Are domains/topics interpreted with markers, morphology and stability rather than naming alone?

### Mapping and generated layers

- Are deconvolution, reconstruction, mapping, imputation and prediction distinguished?
- Is reference shift, unknown-state handling and rare-state performance audited?
- Are patient-level holdouts, simple baselines, calibration and OOD tests reported?
- Are virtual cells/slices and predicted expression prevented from becoming observations?

### Dynamics, perturbation, clones, and communication

- Are time series, velocity, transport trajectories and lineage kept distinct?
- Are guide/barcode assignment, controls, efficiency, collision and dropout reported?
- Are RNA-derived CNAs/clones validated with DNA, mutation, FISH or lineage evidence?
- Are proximity, LR scores, attention and relay networks kept below causal language without
  functional validation?

### Writing, plus optional radiology review

- When `study_scope == imaging-mechanism`, do radiology and molecular data match patient, lesion,
  region and time?
- When `study_scope == imaging-mechanism`, is registration error reported relative to
  habitat/niche size?
- Is clinical validation patient level, leakage safe, calibrated and independent?
- Do Methods reconstruct the work, Results report effects/uncertainty, legends state denominators and
  inferred status, and Discussion bound mechanism and transfer?

## Wording boundaries and repairs

| Avoid | Use when supported | Repair needed for stronger wording |
|---|---|---|
| “single-cell map” for deconvolved spots | “estimated cell-type fractions/cells at spot resolution” | matched single-cell-resolution or in situ validation |
| “observed expression” for H&E prediction or imputation | “predicted/imputed expression” | measured spatial assay in held-out tissue |
| “new cell type” from a topic/domain | “inferred spatial state/domain with marker support” | orthogonal markers, morphology and reproducible cell identity |
| “spatially variable gene” without target | “overall/ct-/domain-marker SVG” | explicit estimand, null, error control and replication |
| “cells communicate” from proximity/LR | “spatially compatible or putative interaction” | functional perturbation, blockade, rescue or proximity evidence |
| “cell trajectory/lineage” from pseudotime or velocity | “inferred transition/velocity compatible with…” | measured time and lineage/barcode evidence |
| “3D measured atlas” containing virtual slices | “3D reconstruction with measured and interpolated sections” | dense experimental sampling or held-out-section validation |
| “tumour clone/CNA” from RNA alone | “RNA-inferred clone/CNA” | DNA, mutation, FISH or barcode confirmation |
| “causal niche” from clone association | “clone-associated neighbourhood” | temporal/lineage plus intervention or validated selection mechanism |
| When `study_scope == imaging-mechanism`: “molecular imaging habitat” from coarse matching | “patient/lesion-level imaging–molecular association” | local registration error below the claimed scale |
| “predictive biomarker” from the discovery cohort | “candidate association/signature” | locked model, unseen cohort, calibration and comparator |

## Global hard stops

- Broken patient, lesion, section or coordinate identity.
- Cells, spots, bins, molecules, fields, sections or virtual slices treated as independent patients.
- Platform/panel cannot observe the target estimand.
- Severe artifact or segmentation uncertainty explains or dominates the target finding.
- Generated or inferred layers presented as direct measurement.
- Outcome leakage through regions, adjacent sections, tiles, references, registration or pretraining.
- No tissue-aware spatial null for neighbourhood/CCC inference.
- Velocity, proximity, attention, RNA CNA or histology-based prediction used as causal/measured evidence.
- When `study_scope == imaging-mechanism`, local radiology–molecular co-localization claimed without
  compatible registration precision.
- Predictive or treatment claims without locked unseen-patient validation and, for treatment,
  a biomarker-by-treatment interaction.

## Evidence-to-block index

| Block | Evidence IDs |
|---|---|
| 1. Question/estimand | ST01–ST04, ST15, ST25, ST29, ST32–ST33 |
| 2. Platform/reproducibility | ST01–ST04, ST09, ST20 |
| 3. Spatial QC | ST01–ST04, ST06, ST08 |
| 4. Segmentation/cell assignment | ST05, ST07–ST09, ST20–ST23 |
| 5. Coordinates/registration | ST01–ST03, ST10–ST11, ST16, ST24, ST27, ST32–ST33 |
| 6. SVG/domain/gradient/subcellular | ST05, ST10, ST13, ST18–ST20, ST24 |
| 7. Deconvolution/mapping | ST09, ST12, ST16–ST17, ST19 |
| 8. Niche/neighbourhood/CCC | ST08, ST21–ST23, ST29–ST31 |
| 9. Histology/super-resolution | ST11–ST12, ST16, ST24, ST27 |
| 10. Multi-sample/3D/time | ST13–ST15, ST24–ST27, ST32–ST33 |
| 11. Perturbation/lineage | ST25, ST29–ST31 |
| 12. CNA/clones/phylogeography | ST28–ST31 |
| 13. Optional radiology linkage (`study_scope == imaging-mechanism`) | ST01, ST03–ST04, ST10–ST11, ST24, ST27, ST29, ST32–ST33 |

Explicit corpus coverage for deterministic audits:
`ST01, ST02, ST03, ST04, ST05, ST06, ST07, ST08, ST09, ST10, ST11, ST12, ST13, ST14, ST15, ST16, ST17, ST18, ST19, ST20, ST21, ST22, ST23, ST24, ST25, ST26, ST27, ST28, ST29, ST30, ST31, ST32, ST33`.
