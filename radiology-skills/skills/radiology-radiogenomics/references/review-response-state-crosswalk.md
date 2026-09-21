# Scientific review to response-state crosswalk

Version: `1.0`

Scientific verification and response-package closure are different axes. Preserve the original
`source_review_state`, criterion, artifact digest and evidence locator when handing a finding to the
response workflow; write the response result separately as `response_closure_state`. Never overwrite
one with the other merely to obtain a cleaner status table.

| Scientific review state | Conservative response intake state | Required rule |
|---|---|---|
| `VERIFIED` | `VERIFIED` only when the same criterion is rechecked on the same frozen artifact/digest; otherwise `NOT_VERIFIED` | carry finding ID, criterion, digest, locator and reviewer evidence |
| `PARTIAL` | `PARTIAL` | enumerate the closed and open subcriteria; prose cannot collapse them |
| `NOT ADDRESSED` | `NOT_VERIFIED` | absence of a change is not N/A and remains blocking |
| `MADE WORSE` | `MADE_WORSE` | preserve the regression evidence and block release |
| `NOT VERIFIABLE` | `NOT_VERIFIED` | obtain the missing artifact/evidence or keep the gate open |

`NOT_APPLICABLE` exists only on the response-closure axis. It requires a criterion-linked rationale,
author/reviewer accountability and evidence that the criterion truly does not apply. It has no
automatic source-review equivalent. In particular, never convert `NOT ADDRESSED` or
`NOT VERIFIABLE` to `NOT_APPLICABLE`.

Required handoff fields:

`finding_id | affected_claim_ids | criterion | source_review_state | source_artifact_id |
source_artifact_sha256 | evidence_locator | response_item_id | response_closure_state |
closure_evidence_locator | adjudicator | adjudicated_on`

If the artifact digest, criterion or Claim IDs drift, return to the scientific review/claim ledger
instead of asserting response closure. An editor clarification request remains `NOT_VERIFIED` until
a versioned answer is received.
