# Availability statements, dataset citations, FAIR

## Data Availability statement — templates
- **Public:** *"The imaging data are available in The Cancer Imaging Archive
  (https://doi.org/XX.XXXX/tcia.XXXX). Radiomic feature values and analysis code are
  available at Zenodo (DOI: 10.5281/zenodo.XXXX). RNA-seq data are in GEO (GSEXXXXXX)."*
- **Mixed/controlled:** *"Derived radiomic features and code are publicly available (Zenodo
  DOI …). Raw DICOM images cannot be shared publicly because consent did not cover open
  release; de-identified images are available to qualified researchers from [steward] under a
  data-use agreement, subject to [IRB/committee] approval. Germline sequencing data are under
  controlled access in dbGaP (phsXXXXXX)."*
- **Restriction (last resort):** name the controller, the reason, and the access process —
  avoid bare "available on reasonable request."

## Code/Model Availability — template
*"Code to reproduce the analyses is available at https://github.com/…, archived at Zenodo
(DOI …). Trained model weights are available at [repository] under [license] for non-commercial
research; the model is provided for research use and is not a medical device."*

## Dataset citations (DataCite style)
`Creator(s). (Year). Title [Data set]. Repository. https://doi.org/…` — cite public datasets
(TCIA/TCGA/GEO) you used in the reference list, not just inline.

## FAIR quick check
- **Findable** — persistent identifier (DOI/accession) + rich metadata.
- **Accessible** — clear access route (open or documented controlled access).
- **Interoperable** — standard formats (DICOM, NIfTI/BIDS, FASTQ, standard feature schemas)
  + vocabularies; IBSI parameter file for features.
- **Reusable** — license, README/data dictionary, provenance, version, processing parameters.

## Chinese-author alignment（中文对齐）
- "可根据合理要求获得" → if used, must name controller + conditions; prefer a concrete
  repository.
- "原始数据" (raw) vs "衍生数据/特征" (derived) — separate their access routes.
- "受限数据/伦理限制" → state reason + steward + process + timeline.
- Output English statement + **中文待确认清单**: 仓库账号？accession？许可协议？伦理/DUA 条款？
  是否可公开原图？
