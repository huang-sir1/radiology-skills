# Final technical audit

Run after content freeze and before portal upload.

## File integrity

- every manifest path exists and opens;
- file extensions match actual content;
- filenames follow current portal rules and are unique case-insensitively;
- no zero-byte, temporary, lock, duplicate, or stale files are included;
- editable masters are preserved outside the upload folder;
- required metadata and accessibility fields are present without breaking anonymization.

## Document render

Render the manuscript, title page, supplement, response, and redline. Inspect every page for:

- missing/overflowing text, orphan headings, broken cross-references, unresolved citations;
- table clipping, split rows, unreadable footnotes, figure-caption separation;
- page/line numbering required for review;
- tracked changes/comments that should be accepted or intentionally retained;
- correct section order, word counts, and references.

## Figure and graphical-abstract render

- white academic background unless the guide requires otherwise;
- final-size legibility, no text/number overlap or clipping;
- correct panel-letter case, dimensions, resolution, color mode, and file format;
- de-identification and source-data crosswalk pass;
- simulated teaching content is never present in a submission package.

## Table render

- editable format as requested; no cropped columns or microscopic type;
- repeated headers and coherent page breaks;
- denominators, estimates, CIs, p values, reference levels, missingness, and footnotes reconcile;
- table titles/callouts match manuscript and supplement.

## Content/package reconciliation

| Check | Pass condition |
|---|---|
| Cohort and values | abstract, flow, tables, figures, Results, supplement match registry |
| Callouts | every figure/table/supplement is cited and every callout exists |
| Checklists | page/line locations point to the frozen manuscript |
| Declarations | title page, manuscript, forms, and portal fields agree |
| Revision | every response promise exists in clean and marked manuscripts |
| Guide currency | guide source and access date recorded; no provisional limit remains |

Use `../scripts/audit_submission_package.py PACKAGE_ROOT --submission-mode --scope upload-root` only
for an author-confirmed complete upload folder. Use `--scope attachment-set` or `--scope partial` when
that is all the user supplied. The script
compares the manifest with the actual root in both directions, validates signatures and hashes, and
flags placeholders and selected DOCX revision/metadata surfaces. Then perform visual inspection; no
automated scan can prove that a page or figure is aesthetically and scientifically correct.

Archive the report with both `evidence_registry.sha256` and `route_contract_registry.sha256`. Copy
`whole_package_readiness` literally: scoped input remains `INCOMPLETE_SCOPE`, structural failure is
`BLOCKED_STRUCTURAL`, and a passing upload-root is only `HUMAN_GATES_REQUIRED`.

Do not call structural PASS `READY` until render, content, anonymization, cross-file, current-guide and
live-portal gates are independently closed. Preserve the script's stated limitations in the report.
