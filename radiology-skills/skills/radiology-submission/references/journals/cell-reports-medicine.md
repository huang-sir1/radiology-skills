# Cell Reports Medicine — submission profile

Snapshot checked: 2026-08-22. Scope: `Research article`. Current web pages show no visible update
date. A later independent request returned HTTP 403; future final audits must reacquire a current
official page/asset or keep decisive items incomplete. The linked 2021 final-files DOCX conflicts
with current pages and is not authoritative where it is stale.

## Authoritative routes

- `CRM-TYPES`: [Article types](https://www.cell.com/cell-reports-medicine/information-for-authors/article-types)
- `CRM-INITIAL`: [Initial submission](https://www.cell.com/cell-reports-medicine/information-for-authors/submit-manuscript)
- `CRM-REVISE`: [Revision](https://www.cell.com/cell-reports-medicine/information-for-authors/revise-manuscript)
- `CRM-FINAL`: [Final submission](https://www.cell.com/cell-reports-medicine/information-for-authors/final-submission)
- `CRM-POLICY`: [Journal policies](https://www.cell.com/cell-reports-medicine/information-for-authors/journal-policies)
- `CELL-STAR`: [STAR Methods guide](https://www.cell.com/pb-assets/journals/research/cell/methods/Methods_Guide_general-1776088412237.pdf)
- `CELL-TRIAL`: [Clinical trials submission checklist](https://www.cell.com/pb-assets/journals/ifa-assets/clinical-trials-submission-checklist-for-authors-1701981584220.pdf)
- `CELL-AFTER`: [After you submit](https://www.cell.com/information-for-authors/after-you-submit)

## Route facts

- Single-anonymized, free-format initial submission: one PDF or Word plus separate files; LaTeX as
  compiled PDF; initial total at most 20 MB. Initial package requires manuscript, cover letter and
  Declaration of Interests form. Clinical trials also provide protocol including amendments and SAP
  for review.
- Research article is below 7,000 words including figure legends but excluding STAR Methods,
  supplementary legends and references; figures plus tables are capped at seven.
- Revision/final title is at most 145 characters; Summary at most 150 words. Resource availability,
  Author Contributions, DOI, STAR Methods and KRT follow current pages/forms. The Discussion must
  contain a `Limitations of the study` subsection—this is a journal-specific requirement and must not
  be projected onto Cancer Cell.
- Final tables, figures, graphical abstract, Highlights/eTOC and editable source follow the current
  Cell Reports Medicine pages. Main tables are Word table or LaTeX tabular, not Excel/PDF; figures are
  preferably TIFF/PDF with stated alternatives, each at most 20 MB. Graphical abstract is
  1200×1200 px/300 dpi in TIFF/PDF/JPG. Highlights/eTOC are one Word file.
- Final editable source uses one complete alternative: editable Word, or the LaTeX source set plus a
  checked PDF. The `.tex` row binds the PDF with `latex_checked_pdf_sha256`; the PDF row binds the
  source with `latex_source_tex_sha256`. Both repeat matching `latex_source_set_sha256`,
  `latex_dependency_manifest_sha256`, `latex_compile_receipt_sha256`,
  `latex_dependency_manifest_locator` and `latex_compile_receipt_locator`. These fields establish only
  machine-checked internal consistency. A human must inspect all dependencies, reproduce an isolated
  compile and visually compare the PDFs; the auditor does not parse the complete TeX graph or replace
  those checks, and a lone `.tex` cannot pass. CDX is listed for figures but is structurally
  `UNAVAILABLE` until a format-aware ChemDraw adapter and visual render close it.
- The old final-files DOCX says a 150-character title and omits Resource Availability; current web
  pages say 145 characters and require Resource Availability. Use current pages/decision letter and
  record the conflict; do not let the stale form override.

## Stage material matrix

| Stage | Material | Class | Publicly verified format/status |
|---|---|---|---|
| initial | free-format manuscript | required | one PDF or Word plus files; LaTeX compiled PDF; total ≤20 MB |
| initial | cover letter | required | exact extension/portal designation live-check |
| initial | Declaration of Interests | required | official PDF |
| initial | protocol, amendments and SAP | conditional | clinical-trial branch |
| revision/final-files | STAR Methods | required | embedded-content locator in current guide/template route |
| revision/final-files | Key Resources Table | conditional by content | embedded-content locator in current STAR Methods/template route |
| revision/final-files | Limitations of the study | required | embedded Discussion-subsection locator |
| final-files | editable source | required | Word, or complete LaTeX source set + checked PDF + cross-linked hash/dependency/compile receipts and human isolated-compile/visual QA |
| final-files | separate main figures | conditional when figures exist | TIFF/PDF preferred; EPS/JPEG/CDX also listed; each ≤20 MB; CDX structural adapter required |
| final-files | main tables | conditional | Word table or LaTeX tabular; no Excel/PDF |
| final-files | graphical abstract | required | TIFF/PDF/JPG, 1200×1200 px, 300 dpi |
| final-files | Highlights and eTOC | required | one Word file |
| revision | point-by-point response | required | included in `CRM-REV-PACKAGE`; exact extension remains portal-specific |

## Unverified current/portal gates

- Complete live upload labels and metadata; numeric reference cap; local cover extension. Treat the
  2021 checklist as stale where it conflicts with current web guidance.

## Published exemplars — advisory only

- [Clinical, IHC, metabolomic, pathomic, transcriptomic and genomic risk stratification](https://www.sciencedirect.com/science/article/pii/S2666379124006955) (2025).
- [Spatial transcriptomic and multiplex-IF study of primary immunotherapy resistance](https://www.sciencedirect.com/science/article/pii/S2666379125000072) (2025).
