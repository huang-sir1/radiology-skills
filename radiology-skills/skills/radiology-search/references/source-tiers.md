# Source tiers, MeSH, dedup

## Tier 1 (structured, API-backed) — start here
- **PubMed (E-utilities)** — biomedical recall; **MeSH** controlled vocabulary; best for
  clinical/diagnostic imaging and systematic searches.
- **Crossref** — DOI resolution + cross-disciplinary metadata; good for verifying and for
  non-PubMed venues (engineering/ML).
- **arXiv** — imaging-AI methods and preprints (cs.CV, eess.IV); pair with the published
  version when it exists.
- **medRxiv / bioRxiv** — main preprint venues for clinical imaging AI; when citing a
  preprint, check whether a peer-reviewed version has since appeared and cite that instead.
- **ClinicalTrials.gov / WHO ICTRP** — trial registries (free, structured); required for
  systematic reviews to surface unpublished/ongoing trials and check outcome switching.

## Tier 2 — supplementary
- **Embase**, **Cochrane CENTRAL**, **Scopus / Web of Science** — subscription databases;
  the standard systematic-review complement to MEDLINE (see "Systematic-review minimum").
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

## Systematic-review minimum
- PRISMA / PRISMA-DTA reviewers expect at minimum **MEDLINE (PubMed) + Embase**, usually
  plus **Cochrane CENTRAL** for trials, plus **trial registries** (ClinicalTrials.gov,
  WHO ICTRP). PubMed alone is not defensible as a systematic search.
- Without an institutional subscription: CENTRAL is searchable free via the Cochrane
  Library; trial registries are free. Embase/Scopus/WoS have no free systematic-search
  equivalent — do not pretend otherwise.
- If subscription databases were inaccessible, say so in the limitations: name the
  databases not searched and state that recall is reduced (single-database searches miss
  a material fraction of eligible records, especially non-US and conference literature).

## Deduplication keys (in order)
DOI → PMID → arXiv ID → normalized title (lowercased, punctuation-stripped, author+year
tie-break). Merge multi-source hits into one record; never count duplicates as independent
evidence.

## Verification
Resolve DOI/PMID/arXiv before citing; on failure, flag "unverified" rather than guessing
fields. Respect blocked/restricted domains — report inaccessibility, do not bypass.
