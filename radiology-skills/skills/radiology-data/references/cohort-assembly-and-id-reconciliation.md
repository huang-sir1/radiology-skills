# Cohort assembly & ID reconciliation

Local imaging, clinical, and annotation tables rarely arrive keyed the same way. Assemble the
cohort by auditing the joins **before** any modelling; every unmatched or duplicated patient is
resolved or excluded with a written record. The outputs feed the stage-3 gate and the
cohort-flow figure (`radiology-pipeline/stage-gates-and-handoffs.md`).

## Identity, grain and key discipline

- Assign a de-identified `patient_id` — one person, one ID (e.g. `PAT-0001`). Store the
  real-identity mapping table separately and secured, per IRB (linkage key:
  `dicom-deidentification.md`).
- `patient_id` is the patient-level split/grouping key, **not a universal join key**. Every table
  must declare its row grain, primary/composite key and expected cardinality before any join.
- Use the narrowest de-identified key that identifies the row's real object. Typical grains are:

  | Table grain | Minimum key or controlled link |
  |---|---|
  | one row per patient | `patient_id` |
  | one row per encounter/episode | `patient_id + encounter_id` |
  | one row per imaging examination/study | `patient_id + exam_id` or an authorised, consistently replaced Study UID |
  | one row per series | `patient_id + exam_id + series_id` or the corresponding replaced UID graph |
  | one row per lesion | `patient_id + lesion_id`, with a versioned exam/timepoint linkage table |
  | one row per mask/target/reader/version in a single reference series | `patient_id + exam_id + series_id + reference_space_id + lesion_id + mask_id + reader_id + annotation_version` |
  | one row per repeated outcome/measurement | `patient_id + endpoint_id + timepoint_id` or a prespecified encounter/time-window link |

- Join equal-grain tables on their complete key. Join different grains only through an explicit,
  versioned link table or a declared one-to-many/many-to-one relationship. A many-to-many join is
  `STOP_JOIN_CARDINALITY_UNRESOLVED` until the intended pairing or aggregation is specified.
- Mask identity includes the source image-space, not just patient, lesion, reader and version.
  Two masks of the same lesion on T2 and DWI in one examination remain different objects even if
  their reader/version labels match. Bind each `mask_id` to its source series/object(s), reference
  image/geometry or registered space, target/label and transformation/version manifest. For a
  multi-series segmentation, use a controlled mask-to-source-object link table instead of forcing
  one `series_id`; an immutable mask key is acceptable only when that complete binding is preserved.
- Before and after each join, assert uniqueness at the declared grain, expected cardinality, row
  counts, unmatched keys and row-multiplication factor. An unexplained multiplication factor above
  1 is a failed gate, not additional sample size.
- Never join on names, accession numbers, or medical-record numbers directly — they identify
  studies and admissions, not persons.
- One patient → many studies/lesions/observations is expected. Preserve those nested grains while
  keeping all rows from one patient in the same development/validation partition (leakage rule:
  `radiology-pipeline` SKILL).

## Grain-aware reconciliation audit

1. Build the **patient registry** at patient grain and freeze the de-identified identity crosswalk.
2. Build the **imaging inventory** at examination and series grains with patient key, de-identified
   exam/series keys, acquisition time state, modality and protocol parameters.
3. Build the **mask/label inventory** at its declared observation grain with patient, exam, series,
   lesion/region, reader, version and reference-standard keys (`radiology-annotation`).
4. Reconcile in staged joins: patient registry → encounter/clinical records → examination/series
   inventory → lesion/label/mask observations → outcome/follow-up. Use the complete composite key or
   a prespecified temporal/linkage rule at each transition; do **not** full-outer-join mixed-grain
   tables on `patient_id` alone.
5. For every transition, produce a join-audit row:

   `left grain/key | right grain/key | expected cardinality | pre-join rows/unique keys |
   post-join rows/unique keys | unmatched left/right | duplicated keys | row multiplication factor |
   time-window/link rule | disposition`.

6. Produce three exception lists:
   - **unmatched** — present in one table, absent in another (image without clinical row,
     clinical row without image, mask without image);
   - **duplicate/cardinality violation** — duplicate key at the declared grain, one person under
     two IDs, or an unplanned many-to-many expansion;
   - **orphan/misaligned** — masks/images/outcomes outside the study window, wrong modality, wrong
     side/lesion/exam, or without a resolvable parent object.
7. No row enters modelling while a required link or cardinality violation is unresolved.
   Exclusions and aggregation/link decisions stay in the log permanently.

## Mismatch root-cause table

| Symptom | Likely cause | Fix |
|---|---|---|
| Clinical row has no image | accession no. / medical-record no. / inpatient no. mixed as key | re-derive the key from the hospital master patient index; log the mapping |
| One patient, two clinical rows | multiple admissions or timepoints at a finer grain | preserve encounter/timepoint grain; select or aggregate only by a prespecified rule and retain the source rows |
| Extra imaging studies | repeat/follow-up scans inside the export | apply the protocol window + sequence rule; keep the index study |
| Rows multiply after adding masks/outcomes | incomplete join key or an unplanned many-to-many relation | stop; restore exam/lesion/timepoint/reader keys or create an explicit linkage/aggregation table |
| Two IDs, same person | pinyin variants / ID re-issue / anonymisation applied twice | merge under one `patient_id`; log both source IDs |
| IDs look shifted or mangled | leading zeros lost, padding, Excel auto-format | re-import as text; never let Excel own IDs |
| Dates inconsistent | date-of-birth or admission-date swapped in transcription | verify against the source document; log the correction |

## reconciliation_log.csv

```text
patient_id,object_grain,object_key,source_table,issue_type,expected_cardinality,row_multiplier,link_or_time_rule,action,resolved_by,date,notes
PAT-0042,encounter,ENC-02,clinical,unmatched_no_exam,one-to-many,1.0,index exam within 30 days,excluded,A. Wang,2026-01-15,no eligible exam in window
PAT-0117,patient,PAT-0117,identity,duplicate_id,one-to-one,1.0,verified identity crosswalk,merged,B. Li,2026-01-16,two de-identified source IDs confirmed as one person
```

Store the log in `research_record/` (`radiology-pipeline/project-passport-and-registries.md`).
Its counts are the **only** source for the flow diagram — never re-type them by hand.

## Protocol-heterogeneity screening

Multi-scanner/multi-protocol data: decide per parameter whether to **hard-exclude**,
**keep-and-stratify**, or **harmonise**. The lines below are *examples* — set and justify your
own with a reproducibility analysis (`radiology-annotation/reproducibility-qc.md`).

| Parameter | Hard-exclude (example line) | Keep-and-stratify | Harmonise |
|---|---|---|---|
| Slice thickness | >5 mm for volumetric texture | analyse thick/thin strata separately | resample image + nearest-neighbour mask (`radiology-annotation/mask-geometry.md`) |
| kVp / mAs (CT) | non-diagnostic dose | record as covariate or stratify | — |
| Field strength (MRI) | 1.5T/3.0T pooled without check | stratify by field strength | ComBat or another justified method; first distinguish represented vs unseen batch levels |
| Reconstruction kernel | sharp and smooth mixed silently | record kernel; stratify | — |
| Contrast phase | wrong or absent phase for the target | — | re-derive phase from headers; exclude if indeterminate |
| Missing sequence | required sequence absent | — | exclude the case |

- Any data-dependent harmonisation must avoid test/outcome leakage. For validation samples from
  batch levels represented in training, use frozen training parameters only if the implementation
  supports that transform. Ordinary/transductive ComBat cannot be assumed to transform a wholly
  unseen site because its batch parameters were never estimated. Keep an unseen-site evaluation on
  the raw scale, use a pre-specified method validated for unseen batches, or label external-data
  parameter estimation as adaptation rather than untouched external validation. Fitting on the full
  cohort and calling the result untouched validation is invalid (`radiology-pipeline`, stage 4).
- Record every screened parameter and its disposition in the screening log; "no difference"
  claims need a check, not an assumption.

## Inclusion/exclusion counts (cohort-flow source)

```text
Screened (imaging export):                n = [N]
  Excluded — unmatched ID:                n = [N]   (from reconciliation_log)
  Excluded — protocol hard line:          n = [N]   (per parameter, from screening log)
  Excluded — missing clinical variables:  n = [N]
  Excluded — missing outcome/follow-up:   n = [N]
  Excluded — image quality / artefact:    n = [N]
Final cohort:                             n = [N]   (per center if multi-center)
```

- Fill counts only from the reconciliation and screening logs.
- These numbers are the cohort-flow figure data (`radiology-figure`), the stage-3 gate
  evidence, and the denominators reconciled before submission
  (`radiology-pipeline/cross-artifact-consistency.md`).
