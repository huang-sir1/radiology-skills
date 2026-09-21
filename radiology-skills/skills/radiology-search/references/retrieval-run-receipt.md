# Retrieval-run receipt and corpus/index identity

Use this contract after a real literature/dataset query, API harvest, corpus refresh or local index
build. A planned query is not an executed search, a provider result count is not a deduplicated
corpus, and an index is not current merely because it opens.

## Freeze the retrieval

For every source, record the exact endpoint/source ID, verbatim query, filters, sort, date window,
requested limits, pagination/cursor state, request count, raw result count, outcome and response
artifact SHA-256. Preserve these outcomes separately: `SUCCESS`, `EMPTY_VERIFIED`,
`RATE_LIMITED`, `AUTH_REQUIRED`, `NETWORK_FAILED`, `SOURCE_ERROR` and `NOT_RUN`.

`EMPTY_VERIFIED` means the exact query completed and returned zero records; it is not a transport
failure. `RATE_LIMITED`, `AUTH_REQUIRED` and `NETWORK_FAILED` do not establish zero evidence or an
invalid source. A complete-coverage claim is allowed only for the declared sources/limits when every
source completed and pagination was exhausted.

## Bind configuration and corpus

- Hash the complete retrieval configuration: parser/tool version, deduplication order,
  normalization rules, language/date/type filters and caps.
- Build a corpus manifest with one stable record ID per candidate and hash the physical manifest.
  Keep source IDs, query membership, identifier aliases, access level and retrieval state.
- The index identity binds `corpus_manifest_sha256 + retrieval_config_sha256 + index_sha256`.
  A changed query, parser, filter, dedup rule, corpus row or document requires `STALE` until rebuilt.
- Do not infer DOI/title/author metadata when the source is unresolved. Store conflicts and failed
  lookups rather than silently choosing a convenient value.

## Evidence-to-claim boundary

An evidence context records the corpus record ID, evidence level (`FULL_TEXT`, `ABSTRACT`,
`METADATA_ONLY`), exact page/section/record locator, content SHA-256 and downstream Claim IDs. It
does not certify that the source supports the claim; claim-level verification remains with
`radiology-citation`, and eligibility/bias/synthesis remain with `radiology-systematic-review`.

Do not embed copyrighted full text in a public receipt. Hash lawful local response/content artifacts
and expose only permitted locators/metadata. Provider terms, access controls and controlled data
remain binding.

## Machine gate

Start from [the receipt template](../templates/retrieval-run-receipt.template.json) and validate a
populated record with:

```text
python scripts/validate_retrieval_run_receipt.py RECEIPT.json
```

The gate checks structural identity, physical artifact hashes, configuration/corpus/index linkage,
pagination/coverage consistency and the final receipt digest. It does not run the query, establish
source authority or grade scientific support.

## Required return

`question/protocol digest -> execution identity -> per-source exact query/outcome/pagination ->
retrieval-config digest -> response artifacts -> corpus manifest digest -> evidence locators ->
index state -> failures -> update triggers -> coverage claim -> receipt digest`.

## Official API documentation

- NCBI. [E-utilities usage guidelines](https://www.ncbi.nlm.nih.gov/books/NBK25497/).
- Crossref. [REST API documentation](https://www.crossref.org/documentation/retrieve-metadata/rest-api/).
- Future-House. [PaperQA2](https://github.com/Future-House/paper-qa), used here only as an
  open-source design comparison for corpus/settings identity and evidence-context retention.

The documentation describes interfaces and responsible use; it does not guarantee completeness of a
particular query or metadata field.
