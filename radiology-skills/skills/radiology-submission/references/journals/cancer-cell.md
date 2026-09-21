# Cancer Cell — submission profile

Snapshot checked: 2026-08-22. Scope: `Article/Research Article`. Journal pages show no visible update
date; final-file PDF asset metadata is 2026-08-03. A later independent request returned HTTP 403, so
future final audits must reacquire an official current page/asset or keep decisive items incomplete;
a decision letter remains human-adjudicated under the shared source boundary.

## Authoritative routes

- `CC-TYPES`: [Article types](https://www.cell.com/cancer-cell/information-for-authors/article-types)
- `CC-INITIAL`: [Initial submission](https://www.cell.com/cancer-cell/information-for-authors/submit-manuscript)
- `CC-REVISE`: [Revision](https://www.cell.com/cancer-cell/information-for-authors/revise-manuscript)
- `CC-FINAL`: [Final submission](https://www.cell.com/cancer-cell/information-for-authors/final-submission)
- `CC-POLICY`: [Journal policies](https://www.cell.com/cancer-cell/information-for-authors/journal-policies)
- `CC-FFC`: [Current final-files checklist](https://www.cell.com/pb-assets/journals/EM/MasterFFCs/CCELLFFC-1785771261693.pdf)
- `CELL-STAR`: [STAR Methods guide](https://www.cell.com/pb-assets/journals/research/cell/methods/Methods_Guide_general-1776088412237.pdf)
- `CELL-AFTER`: [After you submit](https://www.cell.com/information-for-authors/after-you-submit)

## Route facts

- Single-anonymized review. Initial submission is free-format and may be one PDF containing all
  material or Word plus separate files; LaTeX authors submit a PDF. Initial total is at most 20 MB.
- Initial hard inventory is deliberately small: complete manuscript, cover letter and completed
  Declaration of Interests PDF. STAR Methods, Key Resources Table, graphical abstract, Highlights and
  eTOC are revision/final-stage routes, not universal initial blockers.
- The cover letter explains current knowledge, conceptual advance, significance/potential impact and
  consortium status, and discloses related manuscripts, timing/competition and editor contacts. It may
  suggest or exclude reviewers and is editor-only.
- Article main text is at most 7,000 words including main-figure legends but excluding STAR Methods,
  supplementary legends and references; figures plus tables are capped at eight.
- At revision/final: title at most 145 characters (normally about 10–12 words); one-paragraph Summary
  at most 150 words; Resource availability has lead contact, materials availability and data/code
  availability; Author Contributions and DOI are present; STAR Methods and KRT follow current forms.
- Main table must be a Word table or LaTeX tabular, not Excel/PDF. Final figures are separate
  high-resolution TIFF/PDF preferably, with EPS/JPEG/CDX also accepted, each at most 20 MB.
- Final editable source uses one of two complete alternatives: an editable Word source, or the LaTeX
  source set plus a checked PDF. For LaTeX, the `.tex` row must bind the PDF with
  `latex_checked_pdf_sha256`, and the PDF row must bind the source with
  `latex_source_tex_sha256`. Both repeat matching `latex_source_set_sha256`,
  `latex_dependency_manifest_sha256`, `latex_compile_receipt_sha256`,
  `latex_dependency_manifest_locator` and `latex_compile_receipt_locator`. These fields prove only
  machine-checked internal consistency; a human must inspect all dependencies, reproduce an isolated
  compile and visually compare the PDFs. The auditor does not parse the complete TeX graph or replace
  those checks, and a lone `.tex` cannot pass. CDX is an accepted figure extension but the bundled
  auditor has no CDX parser, so it needs a format-aware ChemDraw integrity check plus visual render
  before readiness.
- Final graphical abstract is required for Cancer Cell: 1200×1200 px, 300 dpi, TIFF/PDF/JPG. Highlights
  and eTOC are in one separate Word file: up to four Highlights of at most 85 characters each; eTOC at
  most 50 words/two sentences.
- Final revision package contains a new cover letter and point-by-point response, editable source and
  separate final figures. Retain unprocessed data for integrity checks.

## Stage material matrix

| Stage | Material | Class | Publicly verified format/status |
|---|---|---|---|
| initial | free-format manuscript | required | one PDF or Word plus separate files; LaTeX as PDF; total initial package ≤20 MB |
| initial | cover letter | required | editor-only; extension/portal designation live-check |
| initial | Declaration of Interests | required | completed official PDF |
| revision/final-files | STAR Methods | required | embedded-content locator in current guide/template route |
| revision/final-files | Key Resources Table | conditional by content | embedded-content locator in current STAR Methods/template route |
| final-files | editable manuscript source | required | Word, or complete LaTeX source set + checked PDF + cross-linked hash/dependency/compile receipts and human isolated-compile/visual QA |
| final-files | separate main figures | conditional when figures exist | TIFF/PDF preferred; EPS/JPEG/CDX also listed; each ≤20 MB; CDX structural adapter required |
| final-files | main tables | conditional | Word table or LaTeX tabular; no Excel/PDF |
| final-files | graphical abstract | required | TIFF/PDF/JPG, 1200×1200 px, 300 dpi |
| final-files | Highlights and eTOC | required | one separate Word file |
| revision | point-by-point response | required | included in `CC-REV-PACKAGE`; exact extension remains portal-specific |

## Unverified current/portal gates

- Complete live upload labels and metadata; a numeric Research Article reference cap; exact local cover
  extension. Portal capture refines, but does not silently generalize, the profile.

## Published exemplars — advisory only

- [Single-cell and spatial multi-omics analysis of CAFs across cancers](https://www.sciencedirect.com/science/article/pii/S1535610825000832) (2025).
- [Imaging mass cytometry and multi-omics breast-cancer spatial architecture](https://www.sciencedirect.com/science/article/pii/S1535610825002697) (2025).
