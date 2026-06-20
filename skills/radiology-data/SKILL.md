---
name: radiology-data
description: "Prepare and audit Data/Code Availability statements, DICOM de-identification plans, repository selection, dataset citations, and FAIR/sharing checks for Radiology (RSNA) and imaging+omics submissions. Use when the user needs a data availability statement, must de-identify DICOM imaging, choose a repository (TCIA, Zenodo, GEO, dbGaP, EGA), share code/models, write dataset citations, or check FAIR compliance — including controlled-access genomics for radiogenomics. Bilingual-aware (中文作者备注 → submission-ready English). Never overstates availability or invents accessions."
---

# Data & Code Availability + De-identification

Prepare submission-ready **Data Availability** and **Code/Model Availability** statements,
plan **DICOM de-identification**, choose repositories, and check FAIR — for imaging and
imaging+omics (radiogenomics) studies.

## Core stance
- **Every result-supporting dataset maps to a concrete access route** — public repository +
  accession, controlled access + steward, or a justified restriction. Avoid bare "available
  on reasonable request" (editors increasingly reject it; if used, name the controller and
  conditions).
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

## When to open extra files
| File | Open when |
|---|---|
| [references/dicom-deidentification.md](references/dicom-deidentification.md) | De-identifying imaging: DICOM tags, pixel PHI, defacing, standards/tools |
| [references/repositories.md](references/repositories.md) | Choosing a repository for images, features, code/models, and omics (open vs controlled) |
| [references/availability-and-fair.md](references/availability-and-fair.md) | Statement templates, dataset citations, FAIR checklist, Chinese-author alignment |

## Workflow
1. **Inventory** result-supporting data: imaging, radiomic feature tables, clinical data,
   omics (bulk/scRNA/spatial), code, trained models.
2. **Classify each** as public / depositable / restricted (privacy, consent, DUA, commercial).
3. **De-identify** imaging (dicom-deidentification.md); confirm no pixel PHI; deface head MRI/CT.
4. **Pick repositories** (repositories.md): images → TCIA/Zenodo; features/code → Zenodo/
   GitHub (+ DOI); expression → GEO; controlled genomics → dbGaP/EGA.
5. **Draft statements** (availability-and-fair.md) with accessions/placeholders; write dataset
   citations; run the FAIR check.
6. **Flag restrictions** honestly: reason, controller, review route, conditions.

## Output contract
1. **`Data inventory`** — item → sensitivity → access route → repository → accession/placeholder.
2. **`Data Availability statement`** and **`Code/Model Availability statement`** (submission-ready).
3. **`Dataset citations`** (DataCite-style) for any public data used.
4. **`De-identification plan`** (if imaging is shared).
5. **`FAIR/issues`** — gaps and fixes; restricted-data wording.
6. **`待确认（中文）`** for Chinese authors — items needing author confirmation.

## Handoffs
Reporting-guideline availability items → `radiology-reporting`; dataset discovery →
`radiology-search`; controlled-cohort design → `radiology-radiogenomics`. Not legal advice —
confirm consent/DUA/IRB terms with your institution.
