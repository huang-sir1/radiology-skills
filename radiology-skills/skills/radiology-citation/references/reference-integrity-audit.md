# Reference integrity audit

Metadata integrity and claim support are different gates. A perfectly formatted reference may not
support the sentence, and a supporting paper may be cited with wrong metadata. Audit both.

## Input modes

- numbered reference list from a manuscript;
- RIS, ENW, BibTeX, NBIB, or reference-manager export;
- DOI/PMID list;
- one disputed reference.

## Verification order

1. Parse each record and assign stable `REF-###` IDs.
2. Resolve DOI/PMID/title against a source of record: PubMed for biomedical indexing, Crossref for
   DOI metadata, publisher page for article/version/page details, and dataset/registry record for data.
3. Compare fields: title, author names/order, journal, year, volume, issue, pages/article number,
   DOI/PMID, publication type, correction/retraction/version status.
4. Use a second authoritative source for conflicts; preserve both observations when unresolved.
5. Produce corrected records without guessing absent fields.

## Status

| Status | Meaning |
|---|---|
| `VERIFIED` | identity and required fields agree across authoritative metadata |
| `CHECK_SUGGESTED` | minor/legitimate ambiguity: online vs issue year, initials, issue omission |
| `NEEDS_FIX` | wrong identity, DOI, author/order, title, venue, pages/article number, or version |
| `UNVERIFIABLE` | available sources cannot establish the record |

Severity is based on identity and retrieval impact, not typography alone. A DOI pointing to another
paper is critical; title capitalization is informational.

## Conflict rules

- Distinguish online-publication year from issue year; do not call one wrong without the journal style.
- Treat article numbers and page ranges correctly for the venue.
- Check errata, expressions of concern, retractions, and preprint-to-version-of-record links.
- Do not combine a preprint DOI and journal metadata into one synthetic record.
- For group authorship, preserve the source-of-record author form.

## Output

| Ref ID | Current identity | Field issue | Verified value | Sources | Status | Action |
|---|---|---|---|---|---|---|

Return a corrected RIS/ENW/BibTeX file only from verified fields. Keep unresolved records out of the
clean export or label them clearly for author review.

After metadata repair, run the claim-support gate for the manuscript sentences that use the reference.
