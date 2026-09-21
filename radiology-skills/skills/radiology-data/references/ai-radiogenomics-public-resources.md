# Public resources for radiology AI and radiogenomics

Use this reference when selecting public datasets, planning external validation, building foundation-model pretraining, or writing dataset citations for radiology AI/radiogenomics. Verify access rules, licenses, and current dataset status before use.

## Dataset selection logic

| Need | Resource type |
|---|---|
| Chest radiograph classification, SSL, VLM, report supervision | CheXpert, MIMIC-CXR, PadChest and comparable CXR repositories |
| Lung CT detection/radiomics/radiogenomics | LIDC-IDRI, NSCLC Radiogenomics, other TCIA lung collections |
| General CT lesion detection and weak supervision | DeepLesion-style lesion resources |
| MRI reconstruction / acceleration | fastMRI and related k-space datasets |
| Brain tumor segmentation and molecular prediction | BraTS, TCGA-GBM/LGG imaging, UPenn-GBM, UCSF-PDGM |
| Breast radiogenomics | TCGA-BRCA / TCGA-Breast-Radiogenomics and institutional MRI/pathology cohorts |
| Omics linkage | GDC, GEO, SRA, cBioPortal, dbGaP/EGA when controlled access is needed |

## Resource checklist

For each dataset, record:

```text
Dataset:
Modality:
Disease/task:
Approximate scale:
Labels/reference standard:
Access route:
License/DUA:
Patient overlap risk:
Can be used for pretraining? yes/no/verify
Can be used for external validation? yes/no/verify
Citation/accession:
```

## Known high-value resource families

| Resource family | Best use | Key caution |
|---|---|---|
| CheXpert / MIMIC-CXR | CXR classification, report supervision, VLM/SSL | report-derived labels are weak; avoid label leakage |
| LIDC-IDRI | lung nodule detection, segmentation, reader variability | nodule-level labels and readers require careful aggregation |
| DeepLesion | CT lesion detection and weak supervision | bookmark lesions are not full segmentation labels |
| fastMRI | reconstruction and acceleration | not a diagnostic-label dataset |
| BraTS | glioma MRI segmentation and selected molecular tasks | challenge splits and preprocessing rules must be respected |
| NSCLC Radiogenomics | CT + mutation linkage | matched n is small; claims must be bounded |
| TCGA-GBM/LGG + TCIA | brain tumor imaging-genomics | mapping, timing, and GDC/TCIA linkage must be explicit |
| UPenn-GBM / UCSF-PDGM | glioma MRI + clinical/molecular validation | check access/version and overlap with other cohorts |
| TCGA-BRCA radiogenomics | breast MRI + molecular labels | imaging subset is much smaller than GDC molecular cohort |

## External validation caution

A public dataset is not automatically external if:

- it was used in pretraining
- cases overlap with training data
- preprocessing or labels were tuned after seeing test results
- it shares the same acquisition institution or challenge leakage route

State whether the dataset is used for pretraining, method development, internal testing, or external validation. Do not reuse one dataset for several roles without clear separation.

## Radiogenomics matched-n rule

For imaging-omics studies, the meaningful n is:

```text
usable imaging intersect usable omics intersect usable clinical endpoint intersect usable validation status
```

Report that intersection before modeling. If the matched cohort is small, use public imaging data for pretraining and treat molecular prediction claims conservatively.
