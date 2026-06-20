# radiology-search

**Multi-source search for imaging literature *and* datasets**, with deduplication and
identifier verification. PubMed + arXiv + Crossref for papers; TCIA/GEO/cBioPortal/OpenNeuro/
Grand Challenge/MSD for data.

## What it does
- Routes queries to the right source (PubMed + MeSH for recall; arXiv for imaging-AI methods;
  Crossref for DOIs).
- Finds public **datasets** (imaging + omics) for a task/organ/modality.
- Deduplicates across sources; verifies DOI/PMID/arXiv; logs the strategy for systematic
  searches (PRISMA-DTA).

## Reference files
```
references/
├── source-tiers.md      source routing, fallback order, MeSH, recall/precision, dedup keys
└── dataset-sources.md   imaging + omics dataset registries and how to search them
```

## Example prompts
- "Systematic PubMed search (with MeSH) for CT radiomics in lung cancer diagnosis."
- "Find a public prostate MRI dataset with PI-RADS labels."
- "Verify and dedup these 30 hits from two databases."

## Modes
Prompt mode (built-in search, following the rules) or an academic-search MCP
(`search_papers`/`get_paper_by_id`/`get_citation`/`lookup_mesh`). Hands export to
`radiology-citation`. Never fabricates metadata or accessions; never bypasses blocked domains.
