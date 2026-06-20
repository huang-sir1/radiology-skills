# Cohort design for radiogenomics

## The binding constraint: the matched intersection
A radiogenomics cohort = patients with **both** usable imaging **and** the molecular layer(s).
This intersection is almost always far smaller than either alone. **Compute and report it
first**, e.g. "TCGA-GBM has N with RNA-seq; the matched TCIA imaging archive has M with
pre-treatment MRI of adequate quality; the analysable intersection is K." K drives power.

## Public data sources
| Source | Holds | Notes |
|---|---|---|
| **TCIA** (The Cancer Imaging Archive) | DICOM imaging, often matched to TCGA | The canonical imaging side; check series completeness, pre-/post-contrast, slice thickness |
| **TCGA** (via **GDC**) | bulk RNA-seq, WES/WGS, methylation, CNV, clinical | Barcodes link to TCIA patient IDs |
| **cBioPortal** | curated TCGA + many studies | Fast querying of mutations/expression/subtypes |
| **GEO / ArrayExpress** | expression (bulk + single-cell) | Public; variable metadata quality |
| **dbGaP / EGA** | controlled-access genomics (germline, raw) | **Data-use agreement** required (cross-ref radiology-data) |
| **ICGC / PCAWG** | international cancer genomes | Pan-cancer |
| **HCA / Human Cell Atlas, Tabula Sapiens** | scRNA-seq references | For deconvolution references |
| **IvyGAP, UPENN-GBM, REMBRANDT** | glioma imaging+molecular | Useful independent validation cohorts |

## Matching imaging to the molecular sample (a subtle trap)
- **What was sequenced?** Bulk omics from a *resection* or *biopsy* fragment may not
  correspond to the imaged region. State the spatial relationship.
- **Region vs whole-tumour.** If omics is from one block, consider matching it to an imaging
  **habitat/sub-region** rather than the whole-tumour radiomics (see radiomics-pipeline.md,
  single-cell-spatial.md).
- **Timing.** Imaging should precede the tissue event (pre-treatment, pre-resection) — guard
  against treatment effects between scan and sample.
- **One sample per patient** for the primary analysis (avoid pseudo-replication).

## Design choices
- **Discovery vs. prediction.** Discovery = which genes/pathways associate with a phenotype
  (FDR-controlled, hypothesis-generating). Prediction = a signature predicting a molecular
  label from imaging (needs TRIPOD+AI, calibration, external validation).
- **Endpoint.** Mutation/subtype (classification), continuous expression/signature
  (regression/correlation), pathway activity (GSEA), or prognosis (survival).
- **Validation cohort planned up front** — an independent dataset, site, or time period.
  Single-cohort radiogenomics is rarely publishable in _Radiology_ without it.

## Size & power
- For a *primary* association or a predictive signature, power that specific comparison
  (radiology-stats/sample-size.md). Treat the genome-wide scan as FDR-controlled discovery.
- Small K (often < 100) means: limit candidate features, use penalised/stability methods,
  and lean on validation rather than complex models.

## Ethics & governance
- Public TCIA/TCGA are generally open; **dbGaP/EGA** raw germline data need approved access
  and a DUA. Document approvals and any controlled-access constraints in the data-availability
  statement (radiology-data).

## Reporting sentence
*"Of 162 TCGA-LGG patients with RNA-seq, 98 had pre-operative TCIA MRI meeting quality
criteria; this matched cohort (n = 98) formed the discovery set, with the UCSF-PDGM cohort
(n = 71) reserved for independent validation."*
