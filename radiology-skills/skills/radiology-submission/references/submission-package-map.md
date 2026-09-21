# Submission package map

Verify every item against the current guide and portal. The matrix below is a routing inventory,
not a claim that every venue requires every file. Start from the selected profile in
`journal-router.md`; do not flatten initial, revision and production materials into one checklist.

## Core inventory

| Material | Typical content | Owner skill | Manifest class |
|---|---|---|---|
| Main manuscript | blinded/unblinded text, references, callouts | writing/polishing | required or guide-dependent |
| Title page | title, authors, affiliations, corresponding author, word counts | submission | usually separate |
| Cover letter | contribution, fit, originality, declarations, related submissions | writing/submission | guide-dependent |
| Summary/highlights | Summary statement, Key Results, Key Points, Highlights, Research in context | writing | venue-dependent |
| Figures | separate final files, legends, graphical abstract if required | figure | guide-dependent |
| Tables | editable tables, embedded or separate as instructed | table | guide-dependent |
| Supplement | methods, figures, tables, appendices, video/data descriptions | all owners | study-dependent |
| Reporting checklists | CLAIM/TRIPOD+AI/CLEAR/STARD/PRISMA/etc. with locations | reporting | study-dependent |
| Nature policy package | Reporting Summary, source data, Extended Data mapping | reporting/data | Nature-family |
| Data/code statements | repository/accession/access process and code/model availability | data | usually required text/form |
| Ethics/consent | approval, waiver/consent, registration, privacy | ethics | required text/form |
| Declarations | funding, conflicts, author contributions, acknowledgments, AI-use disclosure | submission | guide/portal dependent |
| Author identity & contribution forms | ORCID iD (RSNA: submitting author linked at submission, all authors at acceptance; Nature/Lancet: corresponding author required), CRediT role assignment, ICMJE COI disclosure form | submission | guide/portal dependent |
| Suggested reviewers | names, rationale, conflicts, verified current details | journal/submission | portal dependent |
| Revision files | response, clean manuscript, marked/redline manuscript, change summary | response | revision only |

## Initial submission versus revision

For a revision, preserve stable reviewer IDs and add:

- editor-instruction ledger;
- point-by-point response;
- clean revised manuscript;
- marked/redline manuscript in the required convention;
- revised figures/tables/supplement and source data;
- checklist updates with new page/line locations;
- commitment verification: every promised action exists in the revised artifact.

## Manifest schema 2.5

Use `../assets/submission-manifest.template.csv`. One row represents an actual file, a missing
requirement, a conditional item adjudicated not applicable, or a portal-only action. The decisive
fields are:

`project_id | study_scope | project_state_digest | modality_role_digest |
scientific_handoff_packet_digest | scientific_prereview_receipt_digest | source_artifact_id |
analysis_lock_digest | claim_registry_digest | response_package_digest | journal_id | article_type |
submission_stage | study_design | review_model |
material | requirement_class | condition | rule_id |
authority_class | source_url | guide_verified_on | path | expected_extensions | version | sha256 |
blinded | tracked_changes_policy | revision_variant | status | technical_qa | render_qa | content_gate |
anonymization_qa | crossfile_qa`

The nine package-level provenance values bind the upload ledger to one frozen scientific version.
Repeat the same `project_id`, `study_scope`, project-state, modality-role, scientific-handoff,
scientific-prereview, analysis-lock, claim-registry, and response-package receipts on every row.
`study_scope` is `imaging-only`, `mechanism-only`, `imaging-mechanism`, or
`evidence-synthesis`. Project-state and modality-role receipts must be nonzero lowercase SHA-256
values. The first three scopes also require a nonzero scientific-handoff receipt and may use
`not-applicable` for scientific prereview. Evidence synthesis instead requires
`scientific_handoff_packet_digest=not-applicable`, a nonzero
`scientific_prereview_receipt_digest`, and `study_design=systematic-review-meta-analysis`; the
prereview receipt binds the frozen protocol/search/selection-flow/extraction/RoB/synthesis/certainty
chain. Revision requires a response-package SHA-256; other stages may use `not-applicable`. Each
physical file needs a real `source_artifact_id`; path-free field/portal rows may use
`not-applicable`.

The machine validates exact schema order, syntax and same-package consistency only. Its report keeps
`upstream_provenance.authentication=NOT_PERFORMED`; a human must authenticate every value against
the upstream project state, scientific handoff, prereview, artifact, analysis, claim and response
registries.

Allowed requirement classes are `required`, `conditional`, `optional`, and `portal-only`. A
conditional `not-applicable` row needs both the triggering condition and a concrete rationale. A
published exemplar cannot supply a hard-rule row.

`study_design` is the same semicolon-delimited controlled set on every row: `randomized-trial`,
`nonrandomized-intervention`, `observational`, `diagnostic-accuracy`, `prognostic-prediction`,
`medical-ai`, `systematic-review-meta-analysis`, `qualitative-mixed-methods`, `oncology-biomarker`,
`animal-preclinical`, `software-methods`, or `other`. Use every applicable token; it activates
study-design reporting branches and prevents a triggered checklist from being declared N/A.
`other` cannot be the sole token in submission mode: maintain a new controlled route or keep the
conditional-material review human and `INCOMPLETE`.
`review_model` is one selected value (`single-anonymized`, `double-anonymized`, or `not-confirmed`),
not the journal capability label `optional-double-anonymized`. `not-confirmed` is an intake state and
is a structural blocker, not a third peer-review workflow.

`tracked_changes_policy` is an explicit controlled value: `prohibited`,
`allowed-marked-revision`, or `not-applicable`. Never infer it from a material filename or prose label.
`revision_variant` is `not-applicable`, `clean`, `marked`, `response`, `cover`, or `other-revision`.
Only a revision-stage `marked` row may use `allowed-marked-revision`, and the selected journal route
or an exact target-journal live-portal receipt must explicitly authorize that marked file.

## Manifest statuses

- `ready`: file exists, current version, guide rule confirmed, technical QA passed.
- `pending-author`: needs signature, declaration, approval number, reviewer details, or portal entry.
- `pending-guide`: exact requirement/format must be verified from current instructions.
- `blocked-upstream`: scientific/reporting/citation/figure/table/ethics gate failed.
- `not-applicable`: reason recorded.
- `portal-entry`: exact file-neutral action is mapped for author completion in the live portal;
  `ready` means that captured portal item has actually been completed.

Never mark an item `not-applicable` merely because it is inconvenient to prepare.

In submission mode, required and triggered conditional files need a current rule receipt, allowed
extension, version, SHA-256, structural PASS, and closed render/content/anonymization/cross-file gates.
The structural script does not generate render PASS; a human or format-aware renderer must do that.
`expected_extensions` must be a subset of the extensions established by that rule. If the official
guide does not state an accepted extension, use a dated genuine `PORTAL_CURRENT` receipt with an
evidence locator; do not populate the field from memory or a sibling journal.
