---
name: radiology-data
description: "Prepare and audit Data/Code Availability statements, DICOM de-identification plans, repository selection, dataset citations, and FAIR/sharing checks for Radiology (RSNA) and Nature-portfolio imaging+omics submissions. Use when the user needs a data availability statement, must de-identify DICOM imaging, choose a repository (TCIA, Zenodo, GEO, dbGaP, EGA), share code/models, write dataset citations, check FAIR compliance, or needs Extended Data / Supplementary Information / Source Data planning for a Nature-family journal — including controlled-access genomics for radiogenomics. Bilingual-aware (中文作者备注 → submission-ready English). Never overstates availability or invents accessions."
---

# Data & Code Availability + De-identification

Prepare submission-ready **Data Availability** and **Code/Model Availability** statements,
plan **DICOM de-identification**, choose repositories, and check FAIR — for imaging and
imaging+omics (radiogenomics) studies.

## Core stance
- **Every result-supporting dataset maps to a concrete access route** — public repository +
  accession, controlled access + steward, or a justified restriction. Avoid bare "available
  on reasonable request" (editors increasingly reject it; if used, name the controller and
  conditions). At Nature-portfolio venues this is stated as **a condition of publication**,
  not a recommendation — treat it accordingly.
- **De-identify before sharing** any imaging — DICOM headers **and** burned-in pixel PHI;
  defacing for head imaging.
- **Cite datasets** like literature (DataCite-style: creator, title, repository, year,
  identifier).
- **Share code/models** for reproducibility (CLAIM/TRIPOD+AI open-science items).
- **Don't overstate or fabricate** — no invented accessions; controlled data described
  honestly with the access process.

## When to use
- "Write the Data Availability / Code Availability statement."
- "How do I de-identify these DICOMs for TCIA / a public release?"
- "Which repository for my images / radiomic features / RNA-seq?"
- "Write dataset citations / check FAIR."
- "We have controlled genomics (dbGaP/EGA) — how do I word availability?"
- "What goes in Extended Data vs Supplementary Information vs Source Data?" (Nature-portfolio)

## When to open extra files
| File | Open when |
|---|---|
| [references/dicom-deidentification.md](references/dicom-deidentification.md) | De-identifying imaging: DICOM tags, pixel PHI, defacing, standards/tools |
| [references/repositories.md](references/repositories.md) | Choosing a repository for images, features, code/models, and omics (open vs controlled) |
| [references/availability-and-fair.md](references/availability-and-fair.md) | Statement templates, dataset citations, FAIR checklist, Chinese-author alignment |
| [references/ai-radiogenomics-public-resources.md](references/ai-radiogenomics-public-resources.md) | Selecting public datasets for radiology AI/radiogenomics, planning external validation or pretraining, or checking TCIA/GDC/PhysioNet/GEO/dbGaP/EGA-style resource roles |

## Workflow
1. **Inventory** result-supporting data: imaging, radiomic feature tables, clinical data,
   omics (bulk/scRNA/spatial), code, trained models.
2. **For public-resource planning**, open `ai-radiogenomics-public-resources.md` and mark each
   dataset as pretraining, development, internal test, external validation, or citation-only.
3. **Classify each** as public / depositable / restricted (privacy, consent, DUA, commercial).
4. **De-identify** imaging (dicom-deidentification.md); confirm no pixel PHI; deface head MRI/CT.
5. **Pick repositories** (repositories.md): images → TCIA/Zenodo; features/code → Zenodo/
   GitHub (+ DOI); expression → GEO; controlled genomics → dbGaP/EGA.
6. **Draft statements** (availability-and-fair.md) with accessions/placeholders; write dataset
   citations; run the FAIR check.
7. **Flag restrictions** honestly: reason, controller, review route, conditions.

## Output contract
1. **`Data inventory`** — item → sensitivity → access route → repository → accession/placeholder.
2. **`Data Availability statement`** and **`Code/Model Availability statement`** (submission-ready).
3. **`Dataset citations`** (DataCite-style) for any public data used.
4. **`Public-resource role map`** — dataset → role (pretraining/development/test/external
   validation) → overlap/leakage/access risks.
5. **`De-identification plan`** (if imaging is shared).
6. **`FAIR/issues`** — gaps and fixes; restricted-data wording.
7. **`Extended Data / Source Data plan`** (Nature-portfolio only) — which items are main-text,
   Extended Data, Supplementary Information, and confirmation that Source Data will be exported
   per figure.
8. **`待确认（中文）`** for Chinese authors — items needing author confirmation.

## Handoffs
Reporting-guideline availability items, Reporting Summary → `radiology-reporting`; dataset
discovery → `radiology-search`; controlled-cohort design → `radiology-radiogenomics`; figure-level
Source Data / Extended Data figure count → `radiology-figure/nature-figure-spec.md`; display-item
plan in the manuscript → `radiology-writing`. Not legal advice — confirm consent/DUA/IRB terms
with your institution.
