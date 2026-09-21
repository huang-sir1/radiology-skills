# Public-data overlap check — local cohort vs TCIA/TCGA and other public sets

Using a public cohort (TCIA/TCGA, CPTAC, IvyGap, UPENN-GBM, NLST …) as the **external
validation** set is valid only if no patient appears on both sides. Overlap turns "external"
into silent internal validation: the model has effectively seen those patients (or their
near-duplicates), performance is inflated, and the generalisability claim collapses — a
defect reviewers can check from accession IDs.

## How overlap happens

- Institutional data later **uploaded to TCIA** (your hospital contributed the collection).
- A public cohort used in **pretraining** or feature development, then "validated" on itself.
- The same patient present under **different IDs or collections** (rescan, follow-up study,
  re-hosted series, multi-collection archives).
- A foundation model whose **pretraining corpus swallowed the public test set** — the same
  audit applies (→ `radiology-deep-learning/foundation-models-trustworthy-ai.md`).

## Operational steps

1. **Obtain manifests.** Download the public collection's subject-ID list (e.g. TCGA
   barcodes, TCIA collection subject IDs) and, where available, DICOM PatientID /
   StudyInstanceUID / SeriesInstanceUID metadata. Record the collection, manifest version,
   and download date (collections change — verify live).
2. **Normalise IDs.** Harmonise case and prefixes (e.g. `TCGA-XX-XXXX` forms), strip
   site-specific de-identification wrappers, and map local pseudonymised IDs back to source
   IDs through the honest broker / de-identification log (→ `radiology-data`).
3. **Compute the intersection.**
   - Exact subject-ID match.
   - UID match (Study/SeriesInstanceUID) where DICOM metadata exists on both sides.
   - Where IDs cannot be matched, **fuzzy screen** on (sex, age, study date ± tolerance,
     modality, laterality) and hand-review every candidate.
4. **Resolve and log.** Exclude overlapping patients from **one** side (usually the external
   set), record cohort counts before and after, and re-run validation on the cleaned cohort.
5. **Residual-risk statement.** List what could not be checked (missing UIDs, irreversibly
   pseudonymised IDs, pretraining corpora) and bound the claim accordingly.

## Checklist

```text
[ ] Public manifest downloaded (collection, version, access date recorded)
[ ] Local IDs traceable to source IDs (honest-broker mapping documented)
[ ] Exact-ID intersection computed: [N] overlaps found and removed
[ ] UID-level intersection computed, or marked not feasible with reason
[ ] Fuzzy screen done where IDs unmatched; candidates hand-reviewed
[ ] Pretraining corpora of any pretrained/foundation component audited
[ ] Post-cleaning cohort sizes updated everywhere (flow diagram, Tables, Methods)
[ ] Residual-risk sentence included in Methods/Limitations
```

## Proof wording (Methods template)

Clean check:

*"We verified the independence of the development and external cohorts by cross-checking
subject identifiers and, where available, DICOM Study/Series UIDs between the institutional
dataset and the [collection, version, access date] manifest; [N] overlapping subjects were
identified and excluded from the external cohort before analysis. No development-cohort
patient remained in the external set after cleaning."*

Partial check:

*"Because source identifiers for [subset] were irreversibly pseudonymised, overlap could be
excluded only at the [ID level checked]; residual undetected overlap cannot be ruled out and
is noted as a limitation."*

## Reviewer hot-spots

An "external" public cohort with no overlap statement; an institutional collection that also
exists on TCIA and was not cross-checked; a foundation-model pretraining corpus containing
the test collection; overlaps removed without updating the flow diagram and cohort counts.
