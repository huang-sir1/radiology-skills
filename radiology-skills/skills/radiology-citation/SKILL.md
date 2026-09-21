---
name: radiology-citation
description: "Verify claim-level sources and DOI/PMID; export checked citations. Not discovery or evidence synthesis."
---

# Imaging-Scoped Citation Retrieval & Export

Convert manuscript text or standalone claims into **verified** citation candidates, scoped to
the imaging literature when desired, and export a clean reference file.

## Core stance
- **Verify before citing.** Resolve DOI/PMID/arXiv ID against a source of record; expose
  failed lookups rather than filling fields by guesswork.
- **Never fabricate** DOI, pages, volume, issue, year, or journal — metadata-only support is
  flagged as such.
- **Cite what supports the claim.** Grade support: strong / partial / background / limiting.
  Record access depth and an exact evidence locator; DOI/PMID resolution alone cannot verify a
  scientific claim. Abstract-only evidence cannot establish unseen Methods or supplement details.
- **Scope deliberately.** Restrict to imaging journals when the user wants imaging-specific
  support; broaden for methods/biology claims (radiogenomics often needs Nature/Cell/
  Bioinformatics + imaging).

## When to use
- "Find references supporting this sentence/claim."
- "Scope these citations to radiology journals."
- "Verify these DOIs/PMIDs and export RIS/EndNote/BibTeX."
- "Build a bibliography for this Introduction/Discussion."

## When to open extra files
| File | Open when |
|---|---|
| [references/radiology-journal-scope.md](references/radiology-journal-scope.md) | Choosing the journal scope (imaging-only vs. broadened) and ranking by venue |
| [references/export-formats.md](references/export-formats.md) | RIS / ENW / BibTeX field mapping and integrity rules |
| [references/claim-verification-gate.md](references/claim-verification-gate.md) | Pre-submission claim-by-claim verification, doc-only/source-limited audits, numerical checks, novelty checks, or figure/table claim verification |
| [references/reference-integrity-audit.md](references/reference-integrity-audit.md) | Auditing a bibliography/BibTeX/RIS/reference list field by field, resolving DOI-year/pages/author conflicts, or preparing corrected reference-manager records |

## Workflow
0. **Choose the audit axis.** For claim support, open `claim-verification-gate.md` and state
   Search / Doc-only / Visual-table. For bibliography metadata, open
   `reference-integrity-audit.md`. Run both before final submission when references are in scope.
1. **Segment** the text into citable claim units (stable IDs).
2. **Translate** Chinese claims into precise English scientific concepts; prefer precision
   over volume.
3. **Search** (hand off retrieval to `radiology-search` / your academic-search MCP): get
   candidates with DOI/PMID.
4. **Verify** each identifier; drop or flag unresolved ones.
5. **Grade support** per candidate against the claim.
6. **Scope/rank** (radiology-journal-scope.md) — imaging-first when requested.
7. **Export** one file (RIS / ENW / BibTeX), preserving verified fields only.

## Output contract
1. **`Claim → candidates`** table: `Claim ID | Candidate (authors, year, journal) | DOI/PMID |
   Access depth + evidence locator | Version/correction status | Support grade | Verified?`.
2. **`Verification gate`** — if used: `Claim ID | Status | Required action` with unsupported,
   partial, conflicting, or cannot-assess claims made explicit.
3. **`Export`** — a single RIS/ENW/BibTeX file with only verified records.
4. **`Reference integrity`** — when used: field-level Verified/Check/Needs-fix/Unverifiable
   report plus corrected records; do not conflate metadata correctness with claim support.
5. **`Machine-readable audit`** — for full audits, a JSON/CSV ledger preserving stable claim or
   reference IDs, sources, locations, status, and required action.
6. **`Unresolved`** — claims with no verified support, and identifiers that failed lookup.

## Handoffs
- Retrieval/verification engine → `radiology-search`.
- In-text citation style/placement in prose → `radiology-polishing` / `radiology-writing`.
- Dataset citations (TCIA/GEO) → `radiology-data`.
- Full bilingual read of a cited paper → `radiology-reader`.
- Submission claim/reference gate and project claim ledger → `radiology-submission` /
  `radiology-pipeline`.
