# Radiogenomics submission package

Use this before journal selection, pre-review, and upload. The goal is to make the paper easy for
an editor, methods reviewer, genomics reviewer, and imaging reviewer to verify.

## Main manuscript must contain
- Clear title and objective naming modality, cancer/disease, imaging phenotype, and molecular
  layer or endpoint.
- Matched-cohort flow: patients with imaging, patients with omics, intersection, exclusions, and
  validation cohort.
- Imaging acquisition and preprocessing enough for reproducibility; scanner/protocol variation.
- Segmentation/annotation protocol and reproducibility.
- Feature extraction/deep feature pipeline with software versions and parameter files.
- Omics QC, normalization, batch variables, accession/source, and feature definitions.
- Sample-to-image mapping: timing, lesion/region relationship, and treatment interval.
- Statistical analysis: primary hypothesis, FDR plan, covariates, validation, sensitivity.
- Results with effect sizes, CIs, FDR/q-values, validation direction/effect size, not p-values alone.
- Bounded biological interpretation and limitations.

## Supplement files reviewers expect
- Patient flow diagram and matched-cohort table.
- Imaging protocol/scanner table by site.
- Segmentation/reader reproducibility table.
- Radiomics parameter YAML or deep-feature extraction specification.
- Feature list after filtering, ideally feature matrix if allowed.
- Omics QC table and batch/covariate table.
- Sample-to-image mapping table, de-identified.
- Full association results table, including all tested families and FDR values.
- Model formula, coefficients, thresholds, calibration details, and validation outputs if predictive.
- Sensitivity analyses: batch adjustment, tumour volume, site/scanner, treatment interval.
- Completed reporting checklist: CLEAR/IBSI for imaging; TRIPOD+AI if prediction; STARD if
  diagnostic accuracy; STROBE/REMARK/omics standards as appropriate.

## Data and code availability
Coordinate with `radiology-data`.
- Imaging: TCIA or controlled/institutional route when shareable; otherwise honest restriction.
- Omics: GEO/SRA/ArrayExpress/GDC/cBioPortal/dbGaP/EGA as applicable.
- Features and trained models: Zenodo/Figshare/Open Science Framework or institutional repository.
- Code: GitHub/GitLab plus archived DOI release when possible.
- Controlled genomic data require DUA and access committee wording. Never imply open access when
  consent or regulation forbids it.

## Cover letter angle
Use one central claim:

`Clinical problem -> matched imaging-omics design -> biological insight or validated prediction -> why this journal's readers need it -> integrity/reproducibility package`

Avoid selling a correlation as mechanism. Highlight independent validation, spatially matched
sampling, prospective design, reader/clinical utility, or unusually strong open science if present.

## Suggested reviewers
Suggest people who can evaluate:
- Imaging/radiomics reproducibility.
- Genomics/bioinformatics QC and batch correction.
- Biostatistics/high-dimensional modelling.
- Disease-specific clinical relevance.

Avoid conflicted collaborators, same institution, recent coauthors, direct competitors with known
conflicts, or anyone who cannot fairly evaluate both imaging and molecular sides.

## Upload readiness checklist
`Frontmatter valid? | matched n explicit? | accession placeholders resolved? | no invented line numbers? | checklist attached? | data/code statement specific? | cover letter bounded? | figures de-identified? | supplement tables complete? | author approvals confirmed?`