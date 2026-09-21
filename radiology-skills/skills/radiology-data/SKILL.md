---
name: radiology-data
description: "Plan/audit imaging provenance, DICOM de-identification, sharing, repositories and retention; not ethics approval."
---

# Imaging Data Lifecycle, Availability & De-identification

Build or audit a living data-lifecycle/DMP record, prepare submission-ready **Data Availability**
and **Code/Model Availability** statements, plan **DICOM de-identification**, choose repositories,
and check FAIR — for imaging and imaging+omics studies.

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
- **A DMP is a living operational artifact.** Freeze a funder/institution policy passport, then
  version data objects, controls, sharing, preservation, retention/destruction, costs, owners and
  amendments. A publication availability paragraph is not a lifecycle plan.
- **FAIR is not automatically public.** Protected imaging/genomic data can use a controlled access
  route; privacy, consent, DUA and community/institutional governance remain binding.

## When to use
- "Write the Data Availability / Code Availability statement."
- "How do I de-identify these DICOMs for TCIA / a public release?"
- "Which repository for my images / radiomic features / RNA-seq?"
- "Write dataset citations / check FAIR."
- "We have controlled genomics (dbGaP/EGA) — how do I word availability?"
- "What goes in Extended Data vs Supplementary Information vs Source Data?" (Nature-portfolio)
- "Write/update the funder DMP/DMS plan, retention schedule or data-access workflow."
- "A collaborator requested post-publication images/data — what evidence and approval are needed?"

## When to open extra files
| File | Open when |
|---|---|
| [references/cohort-assembly-and-id-reconciliation.md](references/cohort-assembly-and-id-reconciliation.md) | Local imaging/clinical/annotation tables do not line up by patient ID; protocol-heterogeneity screening and inclusion/exclusion counts for the cohort flow |
| [references/data-dictionary-spec.md](references/data-dictionary-spec.md) | Building or auditing the field-level data dictionary (variables, coding, missing codes, provenance) |
| [references/chinese-clinical-text-abstraction.md](references/chinese-clinical-text-abstraction.md) | Extracting variables from Chinese discharge summaries / pathology / radiology reports (manual abstraction, regex, LLM-assisted prefill) |
| [references/outcome-and-followup-data.md](references/outcome-and-followup-data.md) | Defining event/censor/time-origin fields, follow-up acquisition and completeness, too-short follow-up, missing-data strategy |
| [references/dicom-deidentification.md](references/dicom-deidentification.md) | De-identifying imaging: DICOM tags, pixel PHI, defacing, standards/tools |
| [references/repositories.md](references/repositories.md) | Choosing a repository for images, features, code/models, and omics (open vs controlled) |
| [references/availability-and-fair.md](references/availability-and-fair.md) | Statement templates, dataset citations, FAIR checklist, Chinese-author alignment |
| [references/data-lifecycle-management-plan.md](references/data-lifecycle-management-plan.md) | Building or updating a funder/institution policy passport, living DMP/DMS plan, preservation/retention/destruction schedule or post-publication access-request route |
| [references/ai-radiogenomics-public-resources.md](references/ai-radiogenomics-public-resources.md) | Selecting public datasets for radiology AI/radiogenomics, planning external validation or pretraining, or checking TCIA/GDC/PhysioNet/GEO/dbGaP/EGA-style resource roles |
| [templates/data-lifecycle-plan.md](templates/data-lifecycle-plan.md) | A durable object/lifecycle inventory, imaging release gate and amendment log is requested |

## Workflow
1. **Freeze the applicable policy passport** when a DMP/DMS, retention or access decision is in
   scope. Use `VERIFIED_CURRENT / VERIFY_FROM_CURRENT_POLICY / NOT_APPLICABLE /
   STOP_POLICY_UNRESOLVED`; never copy one funder's current format into another regime.
2. **Inventory** result-supporting data: imaging, radiomic feature tables, clinical data,
   omics (bulk/scRNA/spatial), code, trained models.
3. **For lifecycle planning**, open `data-lifecycle-management-plan.md`; bind raw and derived
   imaging/clinical/omics/code/model objects to storage, access, metadata/QC, sharing, preservation,
   retention/destruction, cost, owner and amendment controls.
4. **For public-resource planning**, open `ai-radiogenomics-public-resources.md` and mark each
   dataset as pretraining, development, internal test, external validation, or citation-only.
5. **Classify each** as public / depositable / restricted (privacy, consent, DUA, commercial).
6. **De-identify** imaging (dicom-deidentification.md); freeze a closed object/payload/package
   manifest and apply profile-appropriate checks to attributes, descriptors, structured content,
   graphics, pixels/faces, encapsulated documents, video/waveform/private payloads and package
   artifacts. Unknown or unsupported payloads fail closed. Reconcile the released archive to the
   manifest, resolve every flag and record coverage/exclusions/residual risk. Do not claim absolute
   absence of PHI from a partial or unaudited check.
7. **Pick repositories** (repositories.md): images → TCIA/Zenodo; features/code → Zenodo/
   GitHub (+ DOI); expression → GEO; controlled genomics → dbGaP/EGA.
8. **Draft statements** (availability-and-fair.md) with accessions/placeholders; write dataset
   citations; run the FAIR check.
9. **Flag restrictions** honestly: reason, controller, review route, conditions. For retention,
   destruction or post-publication requests, require the authorized steward and a versioned receipt.

## Output contract
1. **`Policy passport and lifecycle state`** — when applicable: exact authority/source/date,
   object inventory, controls, preservation/retention/destruction, costs, owner and amendment log.
2. **`Data inventory`** — item → sensitivity → access route → repository → accession/placeholder.
3. **`Data Availability statement`** and **`Code/Model Availability statement`** (submission-ready).
4. **`Dataset citations`** (DataCite-style) for any public data used.
5. **`Public-resource role map`** — dataset → role (pretraining/development/test/external
   validation) → overlap/leakage/access risks.
6. **`De-identification plan and closed release-surface manifest`** (if imaging is shared) — every
   object/payload/package artifact, SOP Class or media type, disposition, hash, QA coverage,
   exception and residual-risk state.
7. **`FAIR/issues`** — gaps and fixes; restricted-data wording.
8. **`Extended Data / Source Data plan`** (Nature-portfolio only) — which items are main-text,
   Extended Data, Supplementary Information, and confirmation that Source Data will be exported
   per figure.
9. **`Access-request/closeout state`** — when applicable: request authority, release manifest,
   retention/destruction hold and unresolved steward action.
10. **`待确认（中文）`** for Chinese authors — items needing author confirmation.

## Handoffs
Series/phase/sequence acceptance, acquisition/reconstruction, quantitative transforms, artifacts,
dose, phantom/test-retest and protocol drift → `radiology-acquisition-qc`; this skill retains
inventory, provenance, de-identification, access and sharing ownership. Reporting-guideline
availability items, Reporting Summary → `radiology-reporting`; dataset
discovery → `radiology-search`; controlled-cohort design → `radiology-radiogenomics`; figure-level
Source Data / Extended Data figure count → `radiology-figure/nature-figure-spec.md`; display-item
and table-level source-data crosswalk → `radiology-table`; display-item plan in the manuscript →
`radiology-writing`; package manifest → `radiology-submission`; project provenance →
`radiology-pipeline`; replay level and executable reproduction package →
`radiology-reproducibility`; delivery owners/cadence → `radiology-research-ops`. Not legal advice — confirm consent/DUA/IRB terms
with your institution.
