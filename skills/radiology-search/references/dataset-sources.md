# Imaging + omics dataset sources

## Imaging archives
- **TCIA (The Cancer Imaging Archive)** — DICOM collections, often linked to TCGA molecular
  data (radiogenomics). Check series completeness, modality, pre/post-contrast, annotations.
- **OpenNeuro** — neuroimaging (MRI/EEG/MEG), BIDS-formatted.
- **Grand Challenge (grand-challenge.org)** — curated challenge datasets + leaderboards
  (segmentation/detection/classification).
- **Medical Segmentation Decathlon (MSD)**, **MICCAI challenge** datasets (BraTS, LiTS, KiTS,
  PROMISE12, etc.).
- **UK Biobank imaging**, **ADNI** (neurodegeneration), **NLST/LIDC-IDRI** (lung CT),
  **fastMRI** (raw MRI), **PI-CAI** (prostate) — application/registration often required.
- **NIH ChestX-ray / MIMIC-CXR / CheXpert** — chest radiographs (DUAs apply).

## Omics & matched molecular data (for radiogenomics)
- **GDC / TCGA**, **cBioPortal**, **GEO/ArrayExpress** (expression incl. single-cell),
  **dbGaP / EGA** (controlled-access raw genomics — DUA), **ICGC/PCAWG**, **HCA / Tabula
  Sapiens** (scRNA-seq references), **Single Cell Portal**, **10x datasets** (spatial).

## How to search
- Query by organ/disease + modality + label type ("prostate MRI PI-RADS segmentation").
- Record: name, source, modality/omics, **n**, label/annotation availability, **access type**
  (open / registration / controlled), license, and **accession/DOI**.
- For matched radiogenomics, confirm the **imaging↔molecular intersection** exists and its
  size (cross-ref radiology-radiogenomics/cohort-design.md).

## Governance
Note license and access conditions; controlled-access (dbGaP/EGA) needs approvals/DUA.
Capture accessions for the data-availability statement (→ radiology-data). Verify a dataset's
current availability before citing it.
