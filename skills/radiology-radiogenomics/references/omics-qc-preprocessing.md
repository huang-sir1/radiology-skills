# Omics QC and preprocessing for radiogenomics

Radiogenomic associations are only as credible as the molecular matrix. Treat omics QC as a
pre-specified pipeline, not a post-hoc cleaning step.

## Intake inventory
Record one row per molecular layer:

`Layer | Assay/platform | Tissue source | Sample ID | Patient ID | Date | Processing center | Batch/library | Raw repository/accession | Usable for primary analysis? | Exclusion reason`

The patient ID must map to the imaging subject ID through a documented crosswalk. Keep the
crosswalk private when it contains identifiers; share a de-identified sample map when allowed.

## Bulk RNA-seq / expression
- Confirm tissue type, tumour content/purity if available, RNA quality, library strategy,
  read depth, strandedness, and batch/library preparation.
- Filter low-expression genes before testing. Pre-specify the filter.
- Normalize appropriately for the assay: counts-based methods for RNA-seq; platform-aware
  normalization for microarrays. Use log-scale or variance-stabilized values for association.
- Adjust for relevant covariates when justified: age, sex, stage, treatment, tumour purity,
  batch, center, sequencing platform, and molecular subtype when it is not the endpoint.
- Avoid using all samples, including validation, to choose genes, thresholds, or signatures.

## Mutation / WES / WGS
- State variant caller, reference genome, target regions, tumor-normal status, depth/coverage,
  filtering thresholds, annotation tool, and version.
- Define mutation endpoints before modelling: single driver mutation, pathway-level alteration,
  TMB/MSI/HRD/CNV burden, or subtype class.
- For rare mutations, avoid unstable models. Merge biologically justified classes or use pathway
  alterations when counts are too small.

## Methylation, CNV, proteomics, metabolomics
- State platform, probe/feature filtering, missingness rules, normalization, and batch correction.
- For methylation arrays, document probe filtering and cell-composition/tumour-purity concerns.
- For proteomics/metabolomics, report missingness mechanism, imputation rule, scaling, and batch.

## Batch correction and harmonisation
- Identify batch variables before correction: sequencing center, library kit, platform, run date,
  plate, scanner/site, acquisition protocol.
- Use ComBat/ComBat-seq/Harmony/limma or another justified method for the layer; preserve the
  biological covariate being tested. Never remove the signal of interest as a batch covariate.
- Fit correction on training/discovery data only when the corrected matrix enters a prediction
  model. Apply the learned transformation or a validation-safe strategy to held-out data.
- Show sensitivity: association before/after correction, batch-only model, and covariate-adjusted
  model where feasible.

## Missing data
- Report missingness per layer and whether missingness is related to outcome, site, or batch.
- Define whether the primary cohort requires complete cases for all layers or allows method-level
  missing views, such as MOFA+.
- Imputation must be fit inside training folds for predictive work.

## Minimal reporting table
`Layer | Initial samples | QC exclusions | Matched with imaging | Features before filtering | Features after filtering | Batch variables | Normalization | Availability/accession`

## Reviewer-facing Methods sentence
"Molecular matrices were processed by assay-specific, pre-specified QC pipelines. Low-abundance
features and samples failing platform-level quality criteria were removed before association
analysis; normalization and batch adjustment were performed within the discovery set, preserving
the biological covariate of interest. All filtering thresholds, software versions, and accessions
are provided in the Supplement."