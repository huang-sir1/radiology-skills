# Scope-aware omics QC and preprocessing

Molecular claims are only as credible as the assay matrix and specimen topology. Use this module for
standalone molecular studies or cross-scale imaging–mechanism studies. Treat omics QC as a
prespecified pipeline, not post-hoc cleaning.

## Intake inventory
Record one row per molecular layer:

`Layer | Assay/platform | Tissue source | Sample ID | Biological-unit ID | Date/time | Condition/treatment | Processing center | Batch/library | Raw repository/accession | Usable for primary analysis? | Exclusion reason`

For `mechanism-only`, map biological unit -> specimen -> aliquot/library -> assay -> condition/time.
For `imaging-mechanism`, additionally map the biological-unit ID to the imaging subject, lesion,
region/habitat and time through a documented crosswalk. Never invent imaging fields for standalone
work. Keep identifying crosswalks private and share only a permitted de-identified map.

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
- Identify batch variables before correction: sequencing center, library kit, platform, run date and
  plate; add scanner/site/acquisition protocol only when imaging is active.
- Use ComBat/ComBat-seq/Harmony/limma or another justified method for the layer; preserve the
  biological covariate being tested. Never remove the signal of interest as a batch covariate.
- Fit correction on training/discovery data only when the corrected matrix enters a prediction
  model. Frozen parameters may be applied only to batch/site levels represented during fitting and
  supported by the implementation. A wholly unseen external batch has no ordinary ComBat parameters;
  estimating them from that center is adaptation/transductive use and cannot be called untouched
  external validation. Predefine a reference/frozen method or use no-correction and covariate/site
  sensitivity routes for the new batch.
- Show sensitivity: association before/after correction, batch-only model, and covariate-adjusted
  model where feasible.

## Missing data
- Report missingness per layer and whether missingness is related to outcome, site, or batch.
- Define whether the primary cohort requires complete cases for all layers or allows method-level
  missing views, such as MOFA+.
- Imputation must be fit inside training folds for predictive work.

## Minimal reporting table
`Layer | Initial biological units | Initial assay samples | QC exclusions | Units usable for primary analysis | Features before filtering | Features after filtering | Batch variables | Normalization | Availability/accession`

For `imaging-mechanism`, add `Units matched to imaging | lesion/region/time compatibility`. For
`mechanism-only`, omit those columns.

## Reviewer-facing Methods sentence
"Molecular matrices were processed using assay-specific prespecified QC. Low-abundance features and
samples failing platform-level criteria were removed before the primary analysis; normalization and
batch adjustment were learned within the discovery data where required, preserving the biological
contrast. Filtering thresholds, unit–specimen mapping, software versions and accessions are provided
in the Supplement."
