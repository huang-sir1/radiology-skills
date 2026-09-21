# Versioning and anonymization

## Version freeze

Before package assembly, record:

- analysis lock/run identifier;
- canonical value-registry version;
- manuscript version;
- figure-set and table-set versions;
- supplement, checklist, source-data, and response versions;
- date/time and person/skill performing the freeze.
- SHA-256 for every actual upload file after the freeze; a changed hash invalidates that row's prior
  render and cross-file evidence until rechecked.

If any primary value, cohort definition, endpoint, model, figure, or table changes after freeze,
mark dependent artifacts stale and freeze again after reconciliation.

## File naming

Use stable, sortable names without author identity in blinded packages. Keep a manifest mapping
working names to upload names. Avoid `final`, `final2`, and `really_final`; use explicit versions.

Example pattern:

```text
study-shortname_v1.3_manuscript_blinded.docx
study-shortname_v1.3_title-page.docx
study-shortname_v1.3_figure-01.tiff
study-shortname_v1.3_table-01.docx
study-shortname_v1.3_supplement.pdf
```

Adapt filenames to portal rules after verifying them.

## Blind audit

When double-blind review applies, inspect:

- author names, affiliations, corresponding-author details, acknowledgments, grants, ethics sites,
  registrations, repository links, self-citation phrasing, and institution-specific equipment text;
- document properties, comments, tracked changes, headers/footers, hidden text, alt text, and filenames;
- figures/tables/screenshots for site names, patient IDs, logos, paths, or metadata;
- supplement, reporting checklists, source-data files, and code links, not just the main manuscript.

Do not remove scientifically necessary site information blindly. Follow the guide's masking rule and
use consistent placeholders where required.

For identified or single-anonymized journals, metadata is still audited for accidental stale authors,
reviewer comments and wrong versions; `single-anonymized` is not permission to ship hidden edits.

At `final-files`, `review_model` records the historical review workflow but no longer requires a
blinded production package. Final editable sources normally restore the complete author/title-page
identity required by the journal. Contracts therefore mark final manuscript sources unblinded, while
metadata and cross-file identity are still audited for correctness. Never carry anonymous
placeholders into production merely because the paper previously used double-anonymized review.

## Revision traceability

Every response item records:

| Comment ID | Promised action | Artifact/version | Exact location | Verification status |
|---|---|---|---|---|

The response writer's claim is not proof. Re-open the revised file and independently confirm the
change, value, and location before marking it fulfilled.
