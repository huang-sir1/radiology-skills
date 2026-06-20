---
name: radiology-search
description: "Multi-source literature and dataset search for imaging research, with deduplication, identifier verification, and reference management. Searches PubMed (biomedical), arXiv (imaging-AI methods/preprints), and Crossref (DOI/cross-disciplinary), and routes to imaging dataset registries (TCIA, GEO, cBioPortal, OpenNeuro, Grand Challenge, Medical Segmentation Decathlon). Use when the user wants to find papers or datasets, run a systematic/recall-oriented search, verify a DOI/PMID/arXiv ID, look up MeSH terms, or merge results across sources. Verifies identifiers and exposes incomplete metadata; never fabricates bibliographic fields."
---

# Multi-Source Search (imaging literature + datasets)

Find and verify imaging-research papers **and** datasets across the right sources, merge
without double-counting, and hand clean candidates to citation/export.

## Core stance
- **Right source first.** PubMed for biomedical recall (+ MeSH); arXiv for imaging-AI methods
  and preprints; Crossref for DOI/cross-disciplinary metadata. Dataset registries for data.
- **Verify identifiers** (DOI/PMID/arXiv) before citing; expose failed/missing metadata.
- **Deduplicate** by DOI → PMID → arXiv ID → normalized title; don't count duplicates as
  independent evidence.
- **Recall vs precision** — for systematic/DTA reviews use MeSH + structured strategy and log
  it (PRISMA-DTA reproducibility); for quick lookups, precision.
- **No fabrication** — never invent volume/issue/pages/DOI/dataset accession.

## When to use
- "Find recent papers on [imaging-AI topic]." / "Systematic search for a DTA meta-analysis."
- "Is there a public dataset for [task/organ/modality]?"
- "Verify these DOIs/PMIDs." / "Expand my query with MeSH terms."

## When to open extra files
| File | Open when |
|---|---|
| [references/source-tiers.md](references/source-tiers.md) | Which source to query first; fallback order; MeSH; recall vs precision; dedup keys |
| [references/dataset-sources.md](references/dataset-sources.md) | Finding imaging + omics datasets (TCIA, GEO, cBioPortal, OpenNeuro, Grand Challenge, MSD) |

## Workflow
1. **Classify the need** — papers vs datasets; quick lookup vs systematic recall.
2. **Build the query** — concepts (translate Chinese → English scientific terms); for PubMed
   add MeSH; record the strategy for systematic searches.
3. **Search the right sources** (source-tiers.md), per-source limits; for data use
   dataset-sources.md.
4. **Merge & dedup** across sources by identifier/title.
5. **Verify** key identifiers; flag unresolved.
6. **Return** a ranked, deduplicated candidate list (+ a logged strategy for systematic
   searches). Hand export to `radiology-citation`.

## MCP/tooling note
Works in prompt mode (built-in search tools, following these rules) or with an academic-search
MCP exposing `search_papers` / `get_paper_by_id` / `get_citation` / `lookup_mesh`. Set a
contact email for PubMed E-utilities; optionally `NCBI_API_KEY` for higher rate limits.
(Restricted/blocked domains: do not attempt to bypass — report inaccessibility.)

## Output contract
1. **`Strategy`** — sources queried, query strings/MeSH, limits, dates (full log for
   systematic searches).
2. **`Candidates`** — deduplicated: `Title | Authors | Year | Venue | DOI/PMID/arXiv |
   Verified?`.
3. **`Datasets`** (if requested) — `Name | Source | Modality/omics | n | Access | Accession`.
4. **`Unresolved/Incomplete`** — failed lookups and missing metadata.

## Handoffs
Citation grading/export → `radiology-citation`; dataset access/governance & availability
statements → `radiology-data`; systematic-review reporting → `radiology-reporting` (PRISMA-DTA).
