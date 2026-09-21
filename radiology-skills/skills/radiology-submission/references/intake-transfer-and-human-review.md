# Executable intake, transfer re-profiling, and human review

This layer connects a frozen research record to the journal package audit. It is deliberately
one-way: an intake can select a route, but neither the intake resolver nor the structural auditor can
manufacture scientific closure, portal completion, human QA, or `READY`.

## 1. Intake resolver

Start from `../assets/submission-intake.template.json` and run:

```powershell
python scripts/resolve_submission_intake.py intake.json `
  --package-root C:\author-confirmed-upload-root `
  --output-dir C:\outside-upload-root\resolved
```

Intake schema 1.1 uses the exact ordered fields in the template. The resolver accepts only the exact
canonical `journal_id`, exact contract `article_type`, canonical stage, selected review model,
controlled `study_scope`, controlled study-design set and an existing package root. The root must
be supplied again as an explicit absolute `--package-root` authorization and must exactly match the
intake record; filesystem roots, UNC/device paths and reparse-point paths are rejected. Inventory
hashing is bounded by file-count, per-file and total-byte limits. It treats the
JSON and every inventoried file as untrusted data. It hashes and lists bytes but leaves
`semantic_mapping=UNASSIGNED_HUMAN_GATE`; filenames never decide which requirement a file satisfies.

The optional outputs are written outside the author-confirmed upload root:

- `submission-route-plan.json`: selected route, registry/profile digests, inventory and human gates;
- `submission-manifest.draft.csv`: unresolved route stubs only.

Every draft row remains `pending-author` or `pending-guide`, every QA field remains `not-checked`, and
no N/A rationale or portal receipt is generated. The author/reviewer must map files, adjudicate
conditions and enter real evidence before running the structural auditor.

Resolver states are routing states, not readiness verdicts:

- `INTAKE_ONLY`: exact bundled route selected; semantic mapping and all human gates remain;
- `TARGET_OR_ROUTE_UNRESOLVED`: an exact target, route or required receipt did not resolve;
- `TRANSFER_REPROFILE_REQUIRED`: a real transfer context resolved to the target journal's initial
  route, which must now be rebuilt and checked for the target.

`readiness_granted` is always `false`.

## 2. Frozen upstream foreign keys

Manifest schema 2.5 repeats these package-level receipts on every row:

`project_id | study_scope | project_state_digest | modality_role_digest |
scientific_handoff_packet_digest | scientific_prereview_receipt_digest |
analysis_lock_digest | claim_registry_digest | response_package_digest`

Each physical file also carries `source_artifact_id`; a path-free field or portal action may use
`not-applicable`. `study_scope` is exactly `imaging-only`, `mechanism-only`,
`imaging-mechanism`, or `evidence-synthesis`. Project-state and modality-role digests are mandatory
nonzero lowercase SHA-256 values. For the first three scopes,
`scientific_handoff_packet_digest` is also a nonzero SHA-256 and
`scientific_prereview_receipt_digest` may be a nonzero SHA-256 or `not-applicable` when no applicable
frozen receipt exists. For `evidence-synthesis`, the conditions reverse at this interface:
`scientific_handoff_packet_digest` is exactly `not-applicable`,
`scientific_prereview_receipt_digest` is a required nonzero SHA-256, and `study_design` contains
`systematic-review-meta-analysis`. A revision requires a SHA-256 `response_package_digest`; other
stages may use a real digest or `not-applicable`.

Generate `project_state_digest` and `modality_role_digest` upstream with
`radiology-pipeline/scripts/compute_project_state_digests.py <project_state.json> --write`; never
hand-enter either receipt. The project-state digest canonicalizes the complete semantic project
state after removing only the top-level `project_state_digest`, so it has no self-reference. The
modality-role digest canonicalizes exactly the project-state schema version, `study_id`,
`study_scope`, and the four sorted research-scope lists (`imaging_predictors`,
`measured_molecular_assays`, `associated_latent_estimates`, `predicted_targets`). Neither digest is
the physical SHA-256 of `project_state.json`. Any upstream state or role edit requires regeneration
before manifest assembly.

The canonical prereview producer is
`radiology-prereview/scripts/validate_scientific_prereview_receipt.py --write-digest`. Its receipt
binds stable Finding IDs, source artifacts, affected Claim IDs, closure evidence, unresolved count,
scope-aware reviewer route, upstream analysis/claim/handoff digests and the exact three-state result.
For a response package that claims `READY_FOR_SUBMISSION_ASSEMBLY`, copy the validated
post-revision receipt digest into `scientific_prereview_receipt_digest`; do not copy the source-round
digest or a hand-entered state. The structural schema still permits `not-applicable` for genuinely
non-applicable stages, but that sentinel never means scientific PASS and cannot substitute for the
post-revision receipt required by the response closure contract.
For `evidence-synthesis`, the canonical prereview receipt must bind the frozen `protocol`, `search`,
`selection-flow`, `extraction`, `risk-of-bias-applicability`, `synthesis`, and `certainty` roles.
Start file-backed intake from `../assets/submission-intake.evidence-synthesis.template.json`. The
submission machine validates the conditional enum/digest contract but does not authenticate those
seven artifacts or recompute the synthesis.

The resolver and auditor expose all of these values under `upstream_provenance` with
`authentication=NOT_PERFORMED`. They check syntax and same-package consistency only; they do not
authenticate the cited records, recompute the analysis, or prove that modality roles, claims,
prereview closure, or response commitments are correct. Human review must compare the receipts with
the frozen project state, modality-role subset, scientific handoff packet, prereview decision,
artifact, analysis, claim, and response registries.

## 3. Transfer is dynamic orchestration, never a static shortcut

No executable `transfer` minimum-material route is bundled. Publisher transfer policies describe a
process, not the target journal's actual upload contract. For `submission_stage=transfer`, retain:

`source_journal_id | target_journal_id | target_article_type |
transfer_offer_receipt_sha256 | transfer_offer_checked_on | transfer_mode |
source_inventory_sha256 | target_portal_inventory_sha256 | target_initial_route_id`

Use `../assets/submission-transfer-context.template.json` as the field-level fragment; replace every
placeholder from the authenticated offer, source inventory and target portal capture.

`transfer_mode` is `as-is` or `modify`. `target_initial_route_id` is the exact canonical
`<journal_id>::<article_type>::initial` route. The transfer resolver requires a different named source
journal, an exact supported target/article type, nonzero SHA-256 receipts and a real target initial
route. It then returns `TRANSFER_REPROFILE_REQUIRED`; it does not audit the source package as though
it were already compliant with the target.

Required sequence:

1. Human-authenticate the decision/transfer offer and preserve its private locator and digest.
2. Select the explicit target journal and target article type.
3. Record whether files transfer as-is or will be modified; freeze the source inventory digest.
4. After transfer, capture and hash the target portal inventory for that manuscript instance.
5. Rebuild the package against the target journal's exact `initial` contract plus the target portal
   and transfer-offer instructions.
6. Re-run structural, render, scientific, cross-file and portal review. Unresolved targets remain
   `INCOMPLETE`.

Current official process sources to authenticate at use time include:

- Radiology author instructions and editorial handling:
  `https://pubs.rsna.org/page/radiology/author-instructions` and
  `https://pubs.rsna.org/page/radiology/author-instructions/your-paper`;
- Nature Portfolio transfer process: `https://www.nature.com/nature-portfolio/for-authors/transfer`;
- Wiley Refer and Transfer:
  `https://authors.wiley.com/author-resources/Journal-Authors/submission-peer-review/Refer_and_Transfer.html`;
- Elsevier Article Transfer Service:
  `https://www.elsevier.com/publishing/publish-in-a-journal/submission-and-decision/article-transfer-service`;
- JAMA Network Open instructions:
  `https://jamanetwork.com/journals/jamanetworkopen/pages/instructions-for-authors`.

These publisher/process pages do not by themselves prove that a particular offer, target or file
requirement applies to the author's submission. Historical publisher blog posts and a decision letter
also cannot become a reusable hard route without human adjudication and validated registry
maintenance.

## 4. Post-acceptance human-only branch

Radiology and JAMA Network Open do not have a bundled public-guide `final-files` minimum-material
contract. For these venues, inspect the current acceptance/production communication and live system
for author forms or agreements, copyedited-manuscript queries, final figure proofs, deadlines and
any production-only uploads. Record each observed instruction and evidence locator in the human
report. Do not convert this list into a static required-file matrix or infer extensions/timing from a
sibling journal.

For all venues, acceptance does not relax the upstream version, image-integrity, ethics, authorship,
permission or cross-file gates. Production communication remains untrusted input until its journal,
manuscript, stage and authenticity are verified.

## 5. Markdown human-review adapter

After preserving the structural auditor's JSON, run:

```powershell
python scripts/render_submission_audit_report.py audit.json `
  --package-root C:\author-confirmed-upload-root `
  --expected-audit-sha256 <independently-captured-audit-json-sha256> `
  --output C:\outside-upload-root\human-review.md
```

The package root must be the explicit author/reviewer authorization used for the audit. Capture the
audit JSON digest from the just-completed auditor command or an independently preserved receipt;
never copy either trust input from fields inside the JSON being rendered. The renderer rechecks the
manifest receipt and a bounded current package-inventory digest, then reruns the bundled structural
auditor in submission mode and requires exact JSON equality. A forged self-consistent PASS, registry
override, changed finding or post-audit file drift therefore aborts rather than producing a worksheet.

The renderer carries route, inventory, findings, registry hashes, upstream receipts and limitations
into a review worksheet. Its only queue states are `BLOCKED`, `INCOMPLETE`, and
`HUMAN_REVIEW_REQUIRED`. It cannot assign a final human verdict; the reviewer identity, source and
render evidence, scientific closure receipt and final decision must be added separately.
