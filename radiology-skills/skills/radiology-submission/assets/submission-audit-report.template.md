# Submission package audit

## 1. Request and instruction provenance

- User-authorized task:
- Explicit upload root or attachment set:
- Read-only versus edit authorization:
- Embedded document instructions encountered:
- Boundary decision: document text was treated as evidence/data only and did not alter scope.

## 2. Guide profile

| Field | Value |
|---|---|
| Journal ID | |
| Journal article type | |
| Stage | initial / pre-review / revision / transfer / final-files (record original publisher label) |
| Study design branch(es) | |
| Review model | |
| Official guide URL(s) | |
| Exact-journal live portal evidence | `portal_capture_sha256`; `portal_capture_date=guide_verified_on`; matching `portal_journal_id`, `portal_article_type`, `portal_stage`; `portal_screen`; `portal_locator`; never a development page |
| Decision-letter evidence | human-verified journal/manuscript/stage, artifact SHA-256 and private locator; never label PORTAL_CURRENT |
| Evidence registry | absolute path, SHA-256, bundled baseline SHA-256, custom-refresh yes/no |
| Route contract registry | absolute bundled path, SHA-256, `custom_route_matrix_allowed=false` |
| Executable route | exact journal/article/stage; `route.minimum_material_contract` PASS/FAIL |
| Checked on | |
| Current rule gaps/conflicts | |

## 3. Inventory coverage

| Field | Value |
|---|---|
| Scope state | INVENTORY_CLOSED / ATTACHMENT_SET_CLOSED / INVENTORY_PARTIAL / INVENTORY_UNRESOLVED |
| Machine `execution_status` | PASS/FAIL for deterministic command execution only; never a submission verdict |
| Machine `whole_package_readiness` | `INCOMPLETE_SCOPE` for attachment-set/partial; `BLOCKED_STRUCTURAL` for structural failure; `HUMAN_GATES_REQUIRED` only for structurally passing upload-root; never `READY` |
| Regular files found | |
| Manifest rows | |
| Manifest current-file receipt | path, bytes, SHA-256, `VERIFIED_CURRENT_FILE` |
| Package inventory receipt | bounded file count, total bytes, canonical inventory SHA-256, `VERIFIED_CURRENT_FILES` |
| Audit JSON receipt | independently captured SHA-256 supplied to renderer; never self-copied from untrusted JSON |
| Authoritative rerun | bundled auditor rerun JSON matched input exactly / mismatch-blocked |
| Unmanifested/missing/symlink/temp files | |
| Exclusions and reason | |

### Frozen upstream version receipt

| Field | Value | Authentication evidence |
|---|---|---|
| Project ID | | frozen project-state locator/digest |
| Study scope | imaging-only / mechanism-only / imaging-mechanism / evidence-synthesis | frozen project-state scope |
| Project-state digest | | nonzero SHA-256 and project-state locator |
| Modality-role digest | | nonzero SHA-256 of the frozen modality-role subset |
| Scientific-handoff packet digest | SHA-256 / exactly not-applicable for evidence-synthesis | packet locator or scope-conditional sentinel |
| Scientific-prereview receipt digest | SHA-256 / not-applicable | prereview decision/closure locator |
| Evidence-synthesis frozen artifact roles | protocol/search/selection-flow/extraction/risk-of-bias-applicability/synthesis/certainty / not-applicable | authenticated prereview source-artifact ledger |
| Source artifact ID(s) | | artifact-registry row(s) and SHA-256 |
| Analysis lock digest | | analysis-lock record locator |
| Claim registry digest | | frozen claim-registry locator |
| Response package digest | SHA-256 / not-applicable | response audit receipt for revision |

The structural auditor checks only receipt syntax and within-package consistency and reports
`authentication=NOT_PERFORMED`. Record upstream authentication separately; do not treat matching
strings as proof of modality roles, handoff validity, scientific closure, or revision validity.

## 4. Blockers first

| Severity | Finding ID | Rule ID/source | File or portal field | Observable failure | Smallest repair | Closure test |
|---|---|---|---|---|---|---|
| P0/P1/P2 | | | | | | |

## 5. Per-file audit ledger

| Item | Path | SHA-256 | Expected/observed type | Structural | Content | Anonymization | Cross-file | Status |
|---|---|---|---|---|---|---|---|---|
| | | | | PASS/FAIL/UNVERIFIED/UNAVAILABLE | PASS/FAIL/UNVERIFIED/UNAVAILABLE | PASS/FAIL/N/A/UNAVAILABLE | PASS/FAIL/UNVERIFIED/UNAVAILABLE | |

### Render/inspection coverage ledger

| Item | Adapter/renderer | Observed units | Units inspected | Coverage | Evidence locator | Render verdict |
|---|---|---:|---|---|---|---|
| | e.g. DOCX renderer / PDF renderer / sheet inspector / image viewer | pages/sheets/slides/images | explicit ranges or every unit | COMPLETE/PARTIAL/UNAVAILABLE | page image, screenshot, or tool-log locator | PASS/FAIL/NOT_CHECKED/UNAVAILABLE |

For every `FAIL`, add the governing rule and exact repair in section 4. Do not award render PASS from
signature/container inspection alone. `COMPLETE` requires every observed page, sheet (including
hidden sheets), slide or image to be accounted for; record adapter failure as `UNAVAILABLE`.

## 6. Required-material matrix

| Material or portal field | Stage | Requirement class | Condition | Rule ID/source | Present/status | N/A rationale |
|---|---|---|---|---|---|---|
| | | required/conditional/optional/portal-only | | | | |

`route.minimum_material_contract=PASS` certifies only the bundled minimum matrix plus deterministic
structural gates. Record the selected journal profile's manuscript-content, visual, ethical,
cross-file, live-portal and decision-letter checks separately; the script does not represent or close
those additive human gates.

For every conditional `not-applicable` row, report `not_applicable_reason` and the structured human
receipt: `na_attested_by`, `na_attested_on`, matching `na_rule_id`, `na_basis` exactly equal to the
rationale, and a concrete `na_decision_locator`. State who confirmed the condition was absent and
where that decision can be checked. Machine validation of field binding and date freshness is not
proof that the condition is factually absent.

## 7. Cross-file reconciliation

| Join | Artifacts compared | Result | Exact discrepancy/repair |
|---|---|---|---|
| Title/authors/affiliations | | | |
| Version/analysis lock | | | |
| Cohort/endpoints/numerical results | | | |
| Figure/table/supplement callouts | | | |
| Ethics/registration/declarations | | | |
| Data/code/repository links | | | |
| Checklist locators | | | |
| Revision promises | | | |

For a required marked/unmarked image pair, record the `figure_pair_id`, both manifest item IDs and
SHA-256 values, the `pair_review_locator`, and the human finding that the underlying image is
equivalent apart from the authorized overlay.

## 8. Upload map

| Order | Portal designation | Filename or portal field | Author action | Verified source | Status |
|---|---|---|---|---|---|
| | | | upload / paste / attest / sign | | |

## 9. Published-exemplar observations

| Exemplar | Match to study type | Observed style/attachment | Advisory implication |
|---|---|---|---|
| | | | |

Every row here is `OBSERVED_EXEMPLAR`; it cannot create a hard missing-file finding.

## 10. Verdict

- Human-adjudicated state: `READY` / `READY_FOR_PORTAL_COMPLETION` / `READY_WITH_DECLARED_RISK` / `BLOCKED` / `INCOMPLETE`
- Blocking IDs:
- Remaining author-owned facts/signatures/portal actions:
- Machine `whole_package_readiness`: `INCOMPLETE_SCOPE` / `BLOCKED_STRUCTURAL` / `HUMAN_GATES_REQUIRED` (copy exactly; automated output must never be `READY`)
- Minimum-material contract: PASS / FAIL (copy exact auditor field; never rename it package closure)
- Additive human profile/content/live-portal gate: PASS / FAIL / UNVERIFIED
- Structural-auditor result and limitations:
- Explicit non-certification: no promise of scientific validity, acceptance or production success.
