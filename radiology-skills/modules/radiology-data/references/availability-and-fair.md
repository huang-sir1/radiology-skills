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

## Extended Data, Supplementary Information, and Source Data (Nature-portfolio)

Three different containers, often confused. Decide which each item belongs in **before**
finalising the manuscript, and coordinate with `radiology-figure/nature-figure-spec.md` (which
plans the figure-level split) and `radiology-writing/nature-family-shape.md` (display-item plan):

| Container | What goes there | Peer-reviewed? | Published with article? |
|---|---|---|---|
| **Main text figures/tables** | The small number of display items carrying the headline claim | Yes | Yes |
| **Extended Data** | Additional figures/tables a methods-literate reader would want but that don't carry the headline claim (commonly capped in the single digits to ~10 items — verify live per venue) | Yes | Yes |
| **Supplementary Information** | Bulk material: full statistical tables, extended cohort tables, code listings, extended methods | Not in the same formal sense | Yes, as a separate file |
| **Source Data** | The raw numbers behind **every** individual graph/plot, one file (commonly one sheet/tab per panel), explicitly linked to the figure it supports | N/A — a data requirement, not a display item | Yes, alongside the article |

Source Data is a **publication requirement** for figures showing quantitative data at
Nature-portfolio journals, not optional supplementary material — plan for it at figure-generation
time (the same values the plotting script uses, exported alongside the figure; see
`radiology-figure/figure-set-consistency.md`, which already requires every plotted number to be
re-derived from the data file rather than hand-typed).

## Data/code availability as a condition of publication (Nature-portfolio)

_Radiology_-style guidance above ("avoid bare 'on request'") is a strong recommendation.
Nature Portfolio states it more strongly: making materials, data, code, and associated protocols
**promptly available to readers, without undue qualifications, is a condition of publication** —
not a best-practice suggestion. When drafting for a Nature-portfolio venue:
- Treat any residual restriction as something that must be **justified and bounded** (consent,
  privacy, DUA, commercial), never left vague.
- Confirm the code/model repository is archived with a persistent identifier (Zenodo release DOI,
  not a bare GitHub URL) **before** submission, since availability is checked as part of
  acceptance, not fixed later.
- Cross-check that this statement, the Ethics/consent statement (`radiology-ethics`), and the
  Reporting Summary (`radiology-reporting/nature-reporting-summary.md`) all say the same thing.

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
