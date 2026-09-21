---
name: radiology-bibliometrics
description: "Build reproducible radiology bibliometrics with corpus identity, disambiguation and sensitivity; not reviews."
---

# Radiology Bibliometrics

Use this skill to describe and map a frozen scholarly corpus: publication/citation patterns,
collaboration, topical structure and network change. It owns the bibliometric analysis contract and
responsible interpretation. It does not determine whether an intervention works, whether evidence is
trustworthy, or whether a topic is scientifically innovative.

## Non-negotiable boundaries

- **Corpus before metrics.** Consume a versioned `corpus passport` containing database/index
  coverage, exact query, filters, document types, languages, retrieval date, export/API route and
  deduplication state. `radiology-search` supplies or freezes the scientific corpus.
- **Coverage is part of the result.** Web of Science, Scopus, PubMed, OpenAlex, Crossref and regional
  indexes cover different works, references and document types. Counts from one source are not a
  census of scholarship and should not be silently merged with another.
- **Identity is evidence, not a name string.** Use authenticated/persistent identifiers where
  available, then affiliation, coauthor, topic and time evidence. Preserve unresolved author and
  institution clusters; name-only matching is insufficient.
- **Counting choices change claims.** Declare full or fractional counting, the fractional unit,
  denominator, treatment of multi-affiliation and hyperauthorship, and sensitivity to alternatives.
- **Normalize before comparison.** Citation comparisons require an explicit field/classification,
  document type, publication year and citation window. Recent work is right-censored.
- **Networks are model outputs.** Edge definition, normalization, thresholds, pruning, clustering
  algorithm, resolution, seed and label rules must be recorded. A colored community is not a natural
  scientific truth; test threshold and community stability.
- **Metrics are not merit.** Citation, centrality, journal metrics and altmetrics indicate forms of
  attention or network position; they do not establish quality, causal impact, clinical benefit or
  innovation. Quantitative indicators support, not replace, expert and qualitative judgment.
- **No evidence-synthesis laundering.** Co-citation, keyword frequency or publication volume cannot
  answer a diagnostic, prognostic or treatment-effect question.

## Input passport and STOP gates

Start with [corpus-passport.md](templates/corpus-passport.md). Required fields include:

- purpose, unit of assessment, date range and intended comparison;
- database/platform, indexes, coverage limits, query and retrieval timestamp;
- export fields, cited-reference availability, API/snapshot/version and access/license constraints;
- inclusion/exclusion, document types, preprints/proceedings, language and correction/retraction rules;
- DOI and non-DOI deduplication; work/version/family policy;
- author/institution identifiers, disambiguation evidence and unresolved cases;
- metric definitions, counting method, normalization, citation window and network specification.

Return a STOP state when:

- `STOP_CORPUS`: query, database coverage, retrieval date or inclusion logic is missing;
- `STOP_IDENTITY`: unresolved author/institution identity materially changes ranks or networks;
- `STOP_METRIC`: a requested indicator lacks a denominator, window or reproducible definition;
- `STOP_NETWORK`: the network is dominated by arbitrary thresholds, disconnected fragments or
  unstable communities without sensitivity analysis;
- `STOP_INTERPRETATION`: the requested conclusion equates metrics with quality, clinical impact or
  innovation;
- `STOP_ACCESS`: data reuse, API terms or export rights do not support the proposed analysis.

A STOP may still permit a diagnostic audit and repair plan; it blocks definitive comparative claims.

## Route by mode

| Need | Mode | Main contract |
|---|---|---|
| Check search/export fitness | `corpus-audit` | coverage, query, retrieval, fields, DOI/version dedup and missingness |
| Describe output and attention | `descriptive-impact` | time series, document/citation distributions and normalized indicators |
| Map coauthorship or institutions | `collaboration-network` | identity resolution, full/fractional counting, edge and consortium policy |
| Co-word, co-citation or coupling map | `science-mapping` | feature construction, normalization, thresholds, clustering and labels |
| Compare authors/institutions/countries | `benchmarking` | fair comparison set, counting, normalization, uncertainty and responsible metrics |
| Examine longitudinal topic/network change | `temporal-evolution` | fixed/moving windows, database drift, label continuity and stability |
| Reproduce or challenge a prior map | `audit-reanalysis` | frozen inputs, method replay, sensitivity matrix and claim-drift ledger |

For methods read [analysis-contract-and-methods.md](references/analysis-contract-and-methods.md).
For claim limits read [responsible-interpretation.md](references/responsible-interpretation.md).
Use the [source registry](references/source-registry.md) for source/version status.

## Radiology-specific controls

- Search across radiology, nuclear medicine, medical physics, imaging informatics, engineering and
  computer-science venues when the question crosses them; report conference/preprint asymmetry.
- Preserve modality, anatomy, task, clinical purpose, reference-standard and development/validation/
  deployment state. Keyword presence alone cannot reliably assign clinical maturity.
- Disambiguate hospitals, university systems, cancer centers and consortia; report whether networks
  count authors, addresses, organizations or countries.
- Treat multi-center imaging consortia and hyperauthored AI papers explicitly; a consortium edge can
  dominate maps without representing ordinary collaboration.
- Vendor names, scanner families and software ecosystems may be affiliation/technology entities, not
  scholarly authors; do not mix entity types.
- High publication volume in imaging AI does not prove clinical uptake, regulatory authorization or
  improved patient outcomes.

## Workflow and output contract

1. Freeze the corpus passport and an immutable record-ID/DOI list with exclusions and reasons.
2. Resolve work versions and identities; keep a disambiguation ledger and manual-review queue.
3. Define every metric, denominator, count, normalization and time window before computing it.
4. Define networks completely, run threshold/resolution/seed and counting sensitivities, and assess
   community/centrality stability rather than presenting a single attractive map.
5. Build [bibliometric-analysis-and-claim-ledger.md](templates/bibliometric-analysis-and-claim-ledger.md).
6. Return: `Corpus flow`, `Coverage and missingness`, `Identity ledger`, `Metric dictionary`,
   `Network specification`, `Sensitivity/stability results`, `Claim-source ledger`, `Limitations`,
   and `Reproducibility manifest`.

Label conclusions as `DESCRIPTIVE`, `COMPARATIVE`, `NETWORK_STRUCTURAL`, `HYPOTHESIS_GENERATING` or
`NOT_SUPPORTED`. Never promote them to evidence-effect, quality or innovation conclusions.

## Handoffs and non-ownership

- Corpus retrieval/search reproducibility → `radiology-search`.
- Novel question and qualitative opportunity assessment → `radiology-frontier`.
- Intervention/diagnostic/prognostic evidence conclusions and risk-of-bias appraisal →
  `radiology-systematic-review`.
- Verification of an individual citation or reference metadata → `radiology-citation`.
- Statistical uncertainty methods beyond the bibliometric contract → `radiology-stats`.
- Figures and tables for publication → `radiology-figure` / `radiology-table`.
- This skill does not rank people for hiring/funding, infer research quality from journal metrics,
  or make causal claims about collaboration, policy or clinical impact.
