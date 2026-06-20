# Reference export — RIS / ENW / BibTeX

Export only **verified** records; preserve fields exactly; never fabricate.

## Field mapping (essentials)
| Field | RIS tag | BibTeX | Notes |
|---|---|---|---|
| Type | TY | @article/@inproceedings | journal vs conference (MICCAI etc.) |
| Author | AU (one per line) | author = {A and B} | preserve order, full names if available |
| Year | PY/Y1 | year | |
| Title | TI | title | preserve capitalisation; protect {} in BibTeX |
| Journal | JO/T2 | journal | full name; abbrev only if required |
| Volume/Issue | VL/IS | volume/number | |
| Pages | SP/EP | pages | start/end |
| DOI | DO | doi | verified |
| PMID | (custom) | | keep for biomedical |
| URL | UR | url | |

## Integrity rules
- A record missing DOI **and** PMID is flagged "metadata-only — verify manually."
- Don't auto-fill volume/issue/pages by guessing; leave blank + flag.
- Protect title casing in BibTeX with braces for proper nouns/gene names ({IDH}, {MRI}).
- One export file per request; report counts (verified / flagged / dropped).
