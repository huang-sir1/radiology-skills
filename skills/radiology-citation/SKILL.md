---
name: radiology-citation
description: "Turn manuscript text or claims into verified, imaging-journal-scoped citation candidates and export one reference-manager-ready file (RIS, EndNote ENW, or BibTeX). Use when the user needs references for an imaging paper, wants to find supporting citations for a claim, scope citations to radiology/imaging journals (Radiology, Radiology: AI, RadioGraphics, AJR, European Radiology, JACR, etc.), verify a DOI/PMID, or export a bibliography. Verifies identifiers before formatting and never fabricates DOIs, pages, volumes, or journal metadata."
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

## Workflow
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
   Support grade | Verified?`.
2. **`Export`** — a single RIS/ENW/BibTeX file with only verified records.
3. **`Unresolved`** — claims with no verified support, and identifiers that failed lookup.

## Handoffs
- Retrieval/verification engine → `radiology-search`.
- In-text citation style/placement in prose → `radiology-polishing` / `radiology-writing`.
- Dataset citations (TCIA/GEO) → `radiology-data`.
