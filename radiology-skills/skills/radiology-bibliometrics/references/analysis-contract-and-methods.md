# Bibliometric analysis contract and methods

## Corpus construction

Record the database and platform separately because hosted implementations, index selections and
export fields may differ. Freeze the verbatim query, dates searched, time zone, filters, result count,
export batches, API parameters/version, and immutable IDs. Report which document and cited-reference
types are unavailable or incomplete.

Deduplicate in layers:

1. normalize valid DOI strings and merge exact DOI matches;
2. resolve corrections, retractions, versions, preprint-to-version-of-record and conference-to-article
   relationships according to the declared work-family policy;
3. for records without DOI, use title, authors, year, venue, volume/pages or other identifiers with
   review of ambiguous matches;
4. never discard conflicts silently; retain the chosen representative and linked source records.

## Identity resolution

- Prefer authenticated ORCID iDs for people and ROR IDs for organizations, while recording assertion
  provenance; an identifier field copied from untrusted metadata is not equivalent to authentication.
- Use name variants, affiliation history, coauthors, topics, email/domain and dates as supporting
  evidence. Do not merge solely on transliteration or initials.
- Split university systems, hospitals, departments and affiliated centers only according to the
  stated unit of assessment. Preserve mergers, renamings and temporal affiliation changes.
- Report ambiguous clusters and sensitivity with/without them. Manual adjudication must be logged.

## Counting and normalization

Declare whether publication/citation/collaboration counts use:

- full counting;
- author-level, address-level, institution-level or country-level fractional counting;
- sequence/contribution weighting, if defensible and prespecified;
- consortium/group-author handling and multi-affiliation rules.

For impact comparison specify field classification, document type, publication year, citation
source, census date/window and self-citation policy. Prefer distributions, percentiles and stability
intervals over a single mean. Normalized metrics remain dependent on their reference set.

## Network specification

For each network record:

- nodes and entity version; edge relation and directed/undirected status;
- binary or weighted edges, counting method and self-loop policy;
- feature minimum occurrence, edge threshold, component/pruning rule;
- normalization such as association strength and why it is appropriate;
- layout algorithm/parameters separately from analytical distances;
- clustering algorithm, resolution, random seed/runs and label method;
- centrality definition and whether calculated on full, thresholded or largest-component graph;
- sensitivity across thresholds, counting, normalization, resolution and plausible identity decisions.

Assess community agreement with a stated stability measure or at minimum a reproducible membership
comparison. A visually separated cluster without stability evidence is exploratory.

## Temporal analyses

Freeze windows and explain whether citations accrue to publication year, citing year or census date.
Control for database backfill, index expansion, early-access dates and truncation. Changing keywords,
classification systems and organization identities can create artificial topic change.

