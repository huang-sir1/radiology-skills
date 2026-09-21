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

## Venue reference styles (Vancouver/ICMJE)
- Core ICMJE/"Vancouver" pattern: references numbered in order of first citation; in-text
  marker style (parenthesized, bracketed, superscript) follows the venue.
- **RSNA family** (Radiology, RadioGraphics, Radiology: AI, …) — AMA/Vancouver, numbered
  by order of appearance:
  - Authors: list all when ≤6; with ≥7 list the first 3 + "et al."
  - Journal names in NLM Catalog abbreviation (Radiology, Eur Radiol, Am J Roentgenol).
  - Layout: Author AA, Author BB. Title. J Abbrev Year;volume(issue):pages. DOI when
    available/required by the journal.
- **European Radiology** — similar numbered style: ≥7 authors → first 3 + "et al.";
  DOI required for every reference.
- **Nature family** (Nat Med, Nat Biomed Eng, …) — numbered superscript citations; the
  reference-list format differs (titles included, different punctuation/order) — follow
  the nature.com author guide for the specific journal.
- Venue details change between style editions — confirm against the current Instructions
  for Authors before submission (verify live).
