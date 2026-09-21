# Scientific prereview → response closure crosswalk

Interface version: `1.0`

This is the formal three-state crosswalk for the global scientific prereview result. It does not
collapse finding-level verification, response closure, or submission readiness into one status.

| Frozen scientific prereview state | Response intake consequence | Maximum assembly state before fresh re-review |
|---|---|---|
| `SCIENTIFIC_PREREVIEW_PASS` | Open each actual editor/reviewer item against its frozen criterion; PASS does not auto-close a later response | `NOT_READY_FOR_SUBMISSION_ASSEMBLY` until item-level verification and final receipt validation finish |
| `SCIENTIFIC_PREREVIEW_CONDITIONAL` | Convert every named condition into a stable required response/re-review item | `NOT_READY_FOR_SUBMISSION_ASSEMBLY`; may advance only after post-revision scientific state is PASS |
| `SCIENTIFIC_PREREVIEW_FAIL` | Preserve every blocking finding and return affected claims to the scientific owner | `NOT_READY_FOR_SUBMISSION_ASSEMBLY`; rhetoric, author attestation or package completeness cannot override it |

The response receipt stores both `source_scientific_prereview_state` and
`post_revision_scientific_prereview_state` plus the canonical receipt digest for each result. Never
copy a bare state without its validated receipt. The validator must load both actual receipts and
crosscheck their digests, states, upstream foreign keys, stable Finding/Claim IDs, immutable
criteria/source states and post-revision closure evidence. A final response package can be
`READY_FOR_SUBMISSION_ASSEMBLY` only when the latter is `SCIENTIFIC_PREREVIEW_PASS`, all required
item closures are independently `VERIFIED` or justified `NOT_APPLICABLE`, and no placeholder remains.

## Finding-level crosswalk

Keep these axes side by side:

| Frozen `source_review_state` | Initial response closure state | Upgrade rule |
|---|---|---|
| `VERIFIED` | `NOT_VERIFIED` unless the exact criterion is rechecked on the same/current bound artifact | same criterion + current artifact digest + closure evidence |
| `PARTIAL` | `PARTIAL` | enumerate closed/open subcriteria; all required children must close |
| `NOT ADDRESSED` | `NOT_VERIFIED` | actual new evidence and a version-bound change are required |
| `MADE WORSE` | `MADE_WORSE` | preserve regression evidence and block release |
| `NOT VERIFIABLE` | `NOT_VERIFIED` | obtain the missing artifact/evidence or keep the item open |
| `NOT_VERIFIED` from a canonical prereview receipt | `NOT_VERIFIED` | only a new version-bound closure check with state-change evidence may upgrade it |

Every item carries:

`finding_id | affected_claim_ids | criterion | source_review_state | source_artifact_id |
source_artifact_sha256 | evidence_locator | response_item_id | response_closure_state |
closure_evidence_locator | state_change_evidence | required_for_release`

`NOT_APPLICABLE` exists only on the response-closure axis and requires a criterion-linked rationale.
Neither a global PASS nor a reviewer acknowledgement is a scientific-validity certificate.

## Assembly and submission boundary

`READY_FOR_SUBMISSION_ASSEMBLY` is a response-package state only. The next Skill must copy the
validated canonical `response_package_digest` and the
`post_revision_scientific_prereview_receipt_digest` as the stage-appropriate prereview foreign key;
it still performs current-guide, file, render,
anonymization, cross-file and portal review and may block the upload package.
