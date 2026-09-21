# Mechanism-only submission and rebuttal package

Use this module for bulk RNA, single-cell or single-nucleus assays, spatial transcriptomics,
pathology, other omics and perturbation studies that do not include an imaging claim. Do not request
scanner tables, segmentation reproducibility, radiomics parameter files or sample-to-image mapping.

## Scientific readiness

- State the biological question, system, condition, comparator, primary endpoint and claim ceiling.
- Show donor, patient, specimen, region, cell and technical-observation counts separately.
- Report inclusion, exclusion, attrition, failed assays and missingness at the correct unit.
- Describe specimen acquisition, timing, treatment exposure, preanalytics and batch allocation.
- Provide assay-specific QC, normalization, filtering, annotation and software/reference versions.
- Preserve donor- or patient-level inference; cells, spots, fields and reads do not inflate biological n.
- Report multiplicity family, effect sizes, uncertainty, sensitivity analyses and independent or
  orthogonal validation.
- Distinguish measured, derived, estimated, associated, predicted and perturbed evidence.
- Bound descriptive, association, localization, mechanistic and causal wording to the demonstrated
  links.

## Modality-specific supplement

Include only the modules actually used:

- **Bulk RNA:** library and sequencing QC, normalization, batch/covariate design, full differential
  results, gene-set source/version and deconvolution uncertainty.
- **Single-cell or single-nucleus:** donor balance, cell/nucleus QC, doublet and ambient-RNA handling,
  annotation evidence, integration sensitivity and pseudobulk or hierarchical inference.
- **Spatial:** tissue and region sampling, registration within the tissue workflow, spot/cell QC,
  spatial dependence, neighborhood definition and representativeness.
- **Pathology:** fixation and section handling, marker or panel validation, staining batch, blinded
  scoring, scanner/algorithm QC where WSI is used, and patient-aware nested statistics.
- **Other omics:** platform-specific QC, normalization, missingness, batch and feature identifiers.
- **Perturbation:** assignment, efficiency, off-target assessment, dose-time design, target engagement,
  controls, biological replication and rescue or orthogonal confirmation.

## Data, code and provenance

- Give the appropriate accession or controlled-access route for the measured assay; never imply open
  access when consent, regulation or a data-use agreement prohibits it.
- Archive code, environments, reference resources, annotation dictionaries and key parameters.
- Supply complete result tables and analysis-ready metadata when ethically and legally permitted.
- Identify public-reference atlases separately from measured cohort data, and generated or predicted
  layers separately from observed assays.

## Rebuttal constraints

For every reviewer point, use a frozen finding ID and report: concern, action, evidence location,
residual limitation and revised claim. Do not add imaging terminology or promise radiology validation
to satisfy a generic “multi-modal” request. Recommend the minimum assay, control, reanalysis or claim
reduction that resolves the actual evidence gap.

Before upload verify: author approval, accession and repository status, resolved placeholders, exact
line/figure/table references, consistent sample counts, complete supplement, versioned code and a
claim-evidence ledger consistent across abstract, Results, Discussion, captions and cover letter.
