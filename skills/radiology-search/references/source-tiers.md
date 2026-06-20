# Source tiers, MeSH, dedup

## Tier 1 (structured, API-backed) — start here
- **PubMed (E-utilities)** — biomedical recall; **MeSH** controlled vocabulary; best for
  clinical/diagnostic imaging and systematic searches.
- **Crossref** — DOI resolution + cross-disciplinary metadata; good for verifying and for
  non-PubMed venues (engineering/ML).
- **arXiv** — imaging-AI methods and preprints (cs.CV, eess.IV); pair with the published
  version when it exists.

## Tier 2 — supplementary
- Semantic Scholar / OpenAlex (citation graph, broad coverage), Google Scholar (recall, but
  unstructured — verify everything), conference proceedings (MICCAI, IPMI, SPIE, RSNA
  abstracts).

## MeSH strategy (PubMed, recall-oriented)
- Map concepts to MeSH descriptors + subheadings; combine with free-text in title/abstract.
- Use explosion for broad concepts; restrict with study-type filters for DTA reviews.
- Log the full Boolean strategy + dates + filters (PRISMA-DTA reproducibility).

## Recall vs precision
- Systematic/DTA review → recall: MeSH + synonyms + free-text, multiple databases, documented.
- Quick lookup/support → precision: tight phrases, recent, high-relevance.

## Deduplication keys (in order)
DOI → PMID → arXiv ID → normalized title (lowercased, punctuation-stripped, author+year
tie-break). Merge multi-source hits into one record; never count duplicates as independent
evidence.

## Verification
Resolve DOI/PMID/arXiv before citing; on failure, flag "unverified" rather than guessing
fields. Respect blocked/restricted domains — report inaccessibility, do not bypass.
