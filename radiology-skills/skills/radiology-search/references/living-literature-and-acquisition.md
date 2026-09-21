# Living literature and acquisition

Use this reference for a maintained paper corpus, pre-submission search refresh, revision update,
or lawful full-text collection.

## Corpus record

Track each record with:

| Field | Purpose |
|---|---|
| Stable corpus ID | Prevent duplicate notes when identifiers change |
| DOI/PMID/arXiv/accession | Source-of-record keys |
| Title/authors/year/venue | Verified bibliographic identity |
| Search source/query/date | Reproducible discovery provenance |
| Inclusion state/reason | included, excluded, backlog, duplicate, retracted/corrected |
| Evidence level | full text, abstract only, metadata only |
| Access route | open access, author copy, institutional access, user-provided, unavailable |
| Local path/index status | PDF/note/RAG index location and version |
| Citation role | background, method, comparator, limitation, guideline, dataset |
| Last checked | Currency and correction/retraction review |

## Search refresh

Refresh when the manuscript enters final drafting, before submission, after a long pause, and during
major revision. Re-run the locked strategy for the new date interval, deduplicate against the corpus,
and report what changed. Do not silently replace the original search log.

For a systematic review, preserve the original protocol/search dates and label updates separately.
For novelty claims, use a high-recall refresh and record the cutoff date in the claim audit.

## Ranking for daily/periodic triage

When the user wants monitoring, score transparently across topic fit, methodological relevance,
validation quality, venue/source quality, clinical/biological relevance, and archival value. Keep
weights visible and recalculate totals; do not let a language model invent a score outside the scale.

## Lawful full-text acquisition

Use this order:

1. user-provided local file;
2. legitimate open-access publisher/repository copy;
3. user-authorized institutional/library route in the user's logged-in browser;
4. abstract/metadata-only record when full text is unavailable.

Do not bypass paywalls, DRM, CAPTCHA, bot checks, two-factor authentication, or institutional access
controls. Never request passwords, cookies, session tokens, or OTPs. Record the access outcome plainly.

## Access statuses

Use concise statuses such as `full_text_local`, `open_access_downloaded`,
`institutional_access_downloaded`, `html_full_text_only`, `abstract_only`, `metadata_only`,
`login_or_verification_needed`, `library_no_permission`, or `no_authorized_full_text_found`.

An inaccessible paper may still be a candidate, but it cannot receive an exact claim-support grade
without enough source text. Route it to `radiology-citation` as `CANNOT_ASSESS` when necessary.

