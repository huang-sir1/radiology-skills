# Clinical live-standard receipt

Use one row per decision-bearing normative statement. Do not mark `SOURCE_VERIFIED` from a landing
page, memory or secondary summary. Hash the exact retrieved PDF/HTML/XML artifact that was reviewed.

## Receipt identity

| Field | Value |
|---|---|
| Receipt ID | [AUTHOR_INPUT_NEEDED] |
| Receipt version / date | [AUTHOR_INPUT_NEEDED] |
| Project / claim IDs | [AUTHOR_INPUT_NEEDED] |
| Active clinical domain | [AUTHOR_INPUT_NEEDED] |
| Verifier role / verified on | [AUTHOR_INPUT_NEEDED] |

## Normative-source ledger

| Rule ID | Issuing authority | Normative identifier | Full document title | Edition/version/effective date | Applicability: disease/population/modality/jurisdiction/study period | Canonical URL | Accessed date | Retrieved artifact path / format | Retrieved artifact SHA-256 | Exact section and page/table/figure/paragraph locator | Paraphrased supported statement | Supersedes ID/version | Superseded by ID/version | Verification state |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| STD-001 |  |  |  |  |  |  |  |  |  |  |  |  |  | LIVE_VERIFICATION_REQUIRED |

Allowed states are `SOURCE_VERIFIED`, `LIVE_VERIFICATION_REQUIRED`, `SUPERSEDED`, and
`NOT_APPLICABLE`. `SOURCE_VERIFIED` requires a nonzero physical SHA-256 and an exact locator.
For `SUPERSEDED`, retain the historically applicable source and identify the successor when the
issuing authority provides it. If no superseded relation is discoverable, record the exact search
boundary and `none known as of <accessed date>`; do not infer that no successor exists.

## Claim handoff

| Claim ID | Rule ID | Allowed wording | Forbidden stronger/current wording | Historical-versus-current use | Residual limitation |
|---|---|---|---|---|---|
|  |  |  |  |  |  |

## Re-verification triggers

- protocol freeze:
- analysis freeze:
- manuscript submission:
- major revision:
- authority update or superseded notice:
