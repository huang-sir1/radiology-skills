# Radiogenomics scientific-review state intake

Interface version: `1.0`

Use this finding-level adapter together with the global three-state prereview contract in
[prereview-response-state-crosswalk.md](prereview-response-state-crosswalk.md). The global scientific
prereview state, item-level source review state and response closure state are three separate axes.

The upstream scientific-review state and this Skill's response-closure state are separate fields.
Consume the upstream `finding_id`, affected Claim IDs, criterion, artifact ID/SHA-256, evidence
locator and `source_review_state`; never replace them with a rhetorically convenient closure state.

| Upstream `source_review_state` | Maximum automatic response intake state |
|---|---|
| `VERIFIED` | `VERIFIED` only after the same criterion is rechecked on the same artifact digest; otherwise `NOT_VERIFIED` |
| `PARTIAL` | `PARTIAL` with closed and open subcriteria retained |
| `NOT ADDRESSED` | `NOT_VERIFIED` |
| `MADE WORSE` | `MADE_WORSE` |
| `NOT VERIFIABLE` | `NOT_VERIFIED` |

`NOT_APPLICABLE` has no automatic upstream equivalent. It requires a criterion-linked rationale and
accountable adjudication; `NOT ADDRESSED` and `NOT VERIFIABLE` must never be converted to N/A. Keep
`source_review_state` and `response_closure_state` side by side in the response audit packet. Digest,
criterion or Claim-ID drift returns the item to scientific review.
