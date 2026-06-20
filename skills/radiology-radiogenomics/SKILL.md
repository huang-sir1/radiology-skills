---
name: radiology-radiogenomics
description: "Design, analyse, report, and submit imaging-multi-omics radiogenomics studies that link radiomic/deep imaging phenotypes to genomic, transcriptomic, single-cell, and spatial-omics data. Use when the user mentions radiogenomics, imaging genomics, imaging-transcriptomics, TCIA/TCGA, GEO, dbGaP, EGA, cBioPortal, multi-omics integration, MOFA, iCluster, SNF, DIABLO, scRNA-seq deconvolution, CIBERSORTx, BayesPrism, spatial transcriptomics, Visium, Xenium, imaging habitats, gene expression, mutations, pathways, biological validation, omics QC, sample-to-image mapping, radiogenomics submission packages, or reviewer comments about batch/leakage/spatial mismatch. Covers the full chain from matched-cohort feasibility and protocol/SAP to omics QC, imaging pipeline, integration, validation, reporting, submission, and rebuttal support. Never fabricates associations, cohort counts, accessions, approvals, metrics, or reviewer actions."
---

# Radiogenomics and Imaging-Multi-Omics

Use this skill to plan, analyse, report, submit, and revise studies that connect **imaging
phenotypes** (radiomics, deep features, or spatial habitats) to **molecular data**: bulk genomics
or transcriptomics, single-cell RNA-seq, deconvolution, and spatial omics. This is one of the
highest-difficulty corners of imaging research because the analysable cohort is the matched
intersection of imaging and omics, both data spaces are high-dimensional, and scanner/site and
sequencing batch effects can masquerade as biology.

## Core stance

- **Match first, then mine.** State the patients with both usable imaging and usable omics first;
  that matched n drives design, power, claims, and journal tier.
- **Map tissue to image.** A molecular sample is not automatically the whole tumour. Record timing,
  lesion, region, treatment interval, and whether the analysis is patient-, lesion-, habitat-, or
  section-level.
- **Separate confirmation from discovery.** Pre-specify the primary hypothesis and analysis plan;
  FDR-control discovery scans and validate independently whenever possible.
- **Batch can look like biology.** Scanner/site/protocol and sequencing batch/platform/center must
  be recorded, adjusted or harmonised appropriately, and tested in sensitivity analyses.
- **Reproducible imaging and omics.** Radiomics must be IBSI/CLEAR-aligned; omics QC, filtering,
  normalization, batch correction, accessions, and software versions must be explicit.
- **Interpret as association unless proven otherwise.** Pathways, cell types, and spatial evidence
  strengthen biological interpretation but usually do not prove mechanism.
- **Submission-ready integrity.** Never invent cohort counts, accessions, p values, effect sizes,
  approvals, validation results, or reviewer-response locations.

## When to use

- Designing a TCIA-TCGA, GEO, dbGaP/EGA, cBioPortal, in-house, or multi-center radiogenomics study.
- Linking radiomic/deep features with mutations, gene expression, methylation, CNV, proteomics,
  molecular subtypes, pathway activity, immune/cell-type composition, or prognosis.
- Integrating imaging with multi-omics using MOFA/MOFA+, iCluster, SNF, DIABLO/mixOmics, sparse CCA,
  multi-block PLS, NMF, or related methods.
- Connecting imaging habitats to scRNA-seq deconvolution or spatial transcriptomics.
- Drafting a protocol, statistical analysis plan, Methods, Results, Discussion, supplement, or
  submission package for a radiogenomics manuscript.
- Auditing a manuscript or reviewer comments for leakage, batch confounding, small-n optimism,
  tissue-image mismatch, overclaiming, and incomplete data/code availability.

## When to open extra files

| File | Open when |
|---|---|
| [references/cohort-design.md](references/cohort-design.md) | Choosing data sources, matching imaging to omics, estimating matched n, planning validation and ethics |
| [references/sample-to-image-mapping.md](references/sample-to-image-mapping.md) | Determining whether tissue, biopsy, histology, spatial omics, or lesion sampling actually matches the imaging ROI/habitat |
| [references/radiomics-pipeline.md](references/radiomics-pipeline.md) | Building the imaging side: segmentation, IBSI features, deep features, habitats, registration, harmonisation |
| [references/omics-qc-preprocessing.md](references/omics-qc-preprocessing.md) | Preparing RNA-seq, mutation, methylation, CNV, proteomics, or other molecular matrices with QC, normalization, batch handling |
| [references/analysis-plan-sap.md](references/analysis-plan-sap.md) | Writing a protocol/SAP, defining primary versus discovery analyses, covariates, FDR, validation, sensitivity analyses |
| [references/multi-omics-integration.md](references/multi-omics-integration.md) | Choosing integration strategy and methods: MOFA+, iCluster, SNF, DIABLO/mixOmics, sparse CCA, fusion strategies |
| [references/single-cell-spatial.md](references/single-cell-spatial.md) | scRNA-seq deconvolution, pseudobulk, spatial transcriptomics, and habitat linkage |
| [references/association-validation.md](references/association-validation.md) | Feature-gene/pathway association, GSEA/ssGSEA, multiple testing, radiogenomic signatures, validation |
| [references/biological-validation.md](references/biological-validation.md) | Calibrating biological claims and adding pathway, IHC, spatial, single-cell, or orthogonal validation support |
| [references/pitfalls.md](references/pitfalls.md) | Auditing leakage, batch effects, double-dipping, small-n optimism, spatial mismatch, overclaiming |
| [references/radiogenomics-submission-package.md](references/radiogenomics-submission-package.md) | Preparing the manuscript, supplement, checklists, data/code availability, cover-letter angle, reviewer suggestions |
| [references/reviewer-playbook.md](references/reviewer-playbook.md) | Simulating radiogenomics reviewer concerns or drafting rebuttal logic for batch, validation, mapping, and mechanism critiques |

## Workflow

1. **Define the linkage question**: imaging phenotype, molecular layer, endpoint, disease context,
   discovery versus prediction, and whether the intended claim is association, prediction, or biology.
2. **Assemble the matched cohort**: sources, eligibility, the imaging-omics intersection, exclusions,
   and a validation cohort before modelling.
3. **Map sample to image**: tissue source, lesion/region/habitat, time interval, treatment exposure,
   and mapping level. Bound claims when mapping is weak.
4. **Write the protocol/SAP**: primary hypothesis, covariates, multiplicity, validation criterion,
   missing-data handling, sensitivity analyses, and leakage controls.
5. **Build the imaging side**: segmentation/annotation, IBSI radiomics or deep features, registration,
   habitat definitions, stability filtering, and scanner/site harmonisation.
6. **Prepare omics**: assay-specific QC, filtering, normalization, batch correction, feature definitions,
   accessions, software versions, and controlled-access constraints.
7. **Integrate or associate**: choose association, pathway analysis, supervised prediction, or formal
   multi-omics integration. Keep all data-dependent operations inside training or discovery only.
8. **Validate and interpret**: replicate direction/effect size, add biological corroboration where
   available, and keep mechanistic language bounded.
9. **Report and submit**: map to CLEAR/IBSI and the appropriate prediction/diagnostic/observational
   guidelines, prepare supplement and data/code statements, then run pre-review and journal selection.
10. **Revise with traceability**: classify reviewer comments, perform feasible analyses, soften unsupported
    claims, and cite exact manuscript/supplement locations.

## Output contract

For design or audit tasks, return as many of these as the task requires:

1. **`Linkage design`**: phenotype, omics layer, endpoint, claim type, integration strategy.
2. **`Matched cohort`**: sources, intersection n, exclusion logic, validation cohort, limiting count.
3. **`Sample-to-image map`**: timing, lesion/region/habitat, tissue source, mapping level, uncertainty.
4. **`Protocol/SAP`**: primary hypothesis, covariates, FDR/test family, validation rule, sensitivity analyses.
5. **`Pipeline`**: imaging pipeline and omics QC/preprocessing with leakage-prone steps marked train-only.
6. **`Analysis`**: association/integration/prediction method, multiplicity control, validation, code/tool route.
7. **`Biological interpretation`**: claim level, pathway/cell/spatial evidence, alternative explanations.
8. **`Reporting map`**: CLEAR/IBSI plus TRIPOD+AI/STARD/STROBE/REMARK/omics standards as applicable.
9. **`Submission package`**: main-manuscript requirements, supplement tables, checklists, data/code/accessions.
10. **`Reviewer risk list`**: likely radiogenomics critiques and concrete fixes or response strategy.
11. **`Author input needed`**: any missing counts, accessions, approvals, line numbers, software versions, or results.

## Handoffs

- Study feasibility, validation strategy, and cohort architecture -> `radiology-design`.
- Dataset/literature search and accession verification -> `radiology-search` / `radiology-citation`.
- Segmentation SOP and reproducibility -> `radiology-annotation`.
- IBSI/CLEAR/METRICS/RQS, TRIPOD+AI, STARD, STROBE routing -> `radiology-reporting`.
- ROC, calibration, DCA, survival, DeLong, MRMC, sample size, multiplicity -> `radiology-stats`.
- Figures: habitats, MOFA factors, heatmaps, deconvolution bars, KM, flow diagrams -> `radiology-figure`.
- Data/code availability, DICOM de-identification, GEO/dbGaP/EGA/Zenodo/GitHub wording -> `radiology-data`.
- Ethics, consent, DUA, HIPAA/GDPR/PIPL, genomic re-identification risk -> `radiology-ethics`.
- Manuscript drafting and claim calibration -> `radiology-writing` / `radiology-polishing`.
- Pre-submission mock review -> `radiology-prereview`; journal ladder -> `radiology-journal`; rebuttal -> `radiology-response`.

This skill guides design, analysis logic, reporting, and submission readiness. It does not replace
a genomics/bioinformatics collaborator for production pipelines or institutional legal/ethics review.