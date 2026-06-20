# radiology-radiogenomics

**Build radiogenomics studies from matched-cohort feasibility to submission and rebuttal.** This
skill links imaging phenotypes to molecular biology while protecting against the failure modes that
reviewers target: small matched cohorts, batch/scanner confounding, high-dimensional multiplicity,
spatial tissue-image mismatch, and over-interpreted biology.

## What it does

- **Cohort feasibility** across TCIA/TCGA, GEO, dbGaP, EGA, cBioPortal, ICGC, HCA, institutional
  data, and validation cohorts, with the matched imaging-omics intersection surfaced first.
- **Sample-to-image mapping** for patient-, lesion-, habitat-, biopsy-, histology-, and spatial-
  omics-level claims.
- **Imaging pipeline** for IBSI radiomics, deep features, scanner/site harmonisation, registration,
  and imaging habitats.
- **Omics QC/preprocessing** for RNA-seq, mutations, methylation, CNV, proteomics, batch variables,
  normalization, missing data, and accessions.
- **Analysis planning** with primary hypothesis, discovery scan, FDR, train-only preprocessing,
  nested CV where needed, validation, sensitivity analyses, and negative controls.
- **Multi-omics integration** using MOFA/MOFA+, iCluster, SNF, DIABLO/mixOmics, sparse CCA,
  multi-block PLS, and early/intermediate/late fusion strategies.
- **Single-cell and spatial linkage** via deconvolution, pseudobulk, spatial transcriptomics,
  and imaging habitats.
- **Submission readiness**: supplement tables, checklists, data/code availability, cover-letter
  angle, suggested reviewers, and radiogenomics-specific rebuttal playbook.

## Reference files

```text
references/
├── cohort-design.md                    data sources, matching, matched n, validation, ethics
├── sample-to-image-mapping.md           tissue/biopsy/spatial sample ↔ imaging ROI/habitat
├── radiomics-pipeline.md                segmentation, IBSI/deep features, habitats, harmonisation
├── omics-qc-preprocessing.md            RNA/mutation/methylation/proteomics QC and batch handling
├── analysis-plan-sap.md                 protocol/SAP, primary vs discovery, FDR, validation
├── multi-omics-integration.md           MOFA+, iCluster, SNF, DIABLO, sparse CCA, fusion
├── single-cell-spatial.md               deconvolution, pseudobulk, spatial omics ↔ habitats
├── association-validation.md            feature-gene/pathway association, signatures, validation
├── biological-validation.md             pathway/cell/spatial/IHC corroboration and claim ladder
├── pitfalls.md                          leakage, batch, double-dipping, small-n, spatial mismatch
├── radiogenomics-submission-package.md  manuscript/supplement/checklist/data-code upload package
└── reviewer-playbook.md                 pre-review and rebuttal patterns for radiogenomics critiques
```

## Example prompts

- "Design a TCIA-TCGA radiogenomics study linking MRI habitats to hypoxia pathway activity."
- "Make the sample-to-image mapping table for these biopsy locations and MRI ROIs."
- "Draft a radiogenomics statistical analysis plan with primary hypothesis, FDR, and validation."
- "Audit my RNA-seq preprocessing and ComBat plan for leakage and batch confounding."
- "Integrate MRI radiomics with RNA-seq and methylation; should I use MOFA or DIABLO?"
- "Prepare the radiogenomics submission package and likely reviewer objections."
- "Help answer reviewers who say the feature-gene association is batch-driven and overclaimed."

## Integrity

Never invent associations, cohort counts, accessions, approvals, p values, effect sizes, validation
results, line numbers, or completed reviewer actions. Treat feature-gene correlations as bounded
hypotheses unless independent and biological validation supports a stronger claim. Route statistics,
reporting, data sharing, ethics, writing, journal selection, and rebuttal work to the linked
radiology skills when those specialised steps are needed.