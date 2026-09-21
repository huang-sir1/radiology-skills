# Label ontology and reference-standard contract

Use this reference for labels beyond segmentation masks: case/lesion findings, diagnosis, severity,
ordinal categories, measurements, outcomes and composite labels. Replace the phrase “ground truth”
with **reference standard** unless the measurement is demonstrably traceable and effectively error-
free for the intended construct.

## 1. Define the construct before the code

Record one row per label:

| Field | Required specification |
|---|---|
| Construct | what biological/clinical state the label represents—and what it does not |
| Intended use | training, eligibility, endpoint, stratification, evaluation or monitoring |
| Unit | patient, encounter, examination, series, side, organ, lesion, region, report or timepoint |
| Time | index/reference windows and treatment/event relationship |
| Value set | allowed categories/range/units, hierarchy and mutually exclusive versus multilabel |
| Uncertainty | uncertain/indeterminate/equivocal/non-evaluable/not-assessed states |
| Reference process | source(s), readers/tests, adjudication and version |
| Provenance | source locator, extraction/transformation, author, date and confidence/state |
| Claim boundary | construct validity and known misclassification/verification limits |

Do not collapse `absent`, `not mentioned`, `not assessed`, `indeterminate`, `technically inadequate`
and `missing` into one negative value.

## 2. Ontology and coding rules

- Use a versioned controlled terminology where it fits the construct (e.g. RadLex, SNOMED CT or a
  disease-specific system); preserve the original text/value alongside the mapped code.
- Define parent/child and synonym rules, laterality, anatomy, temporality, negation, uncertainty and
  multiplicity. State whether a parent may be inferred from a child and whether categories overlap.
- Record code-system version, local extensions and deprecated/remapped codes. Never silently map a
  local category to a broader clinical construct.
- For numeric labels, specify units, device/assay, rounding, transform, plausible range and whether the
  value is measured, derived, estimated or predicted.
- For ordinal clinical categories, preserve order and version; do not treat them as interval-scaled
  without justification.

Minimum machine-readable fields:

```text
label_id | construct_id | unit_type | patient_id | exam_id | series_id | side | lesion_id | timepoint |
raw_value | normalized_value | code_system | code | version | uncertainty_state | source_type |
source_locator | reader/test_id | adjudication_state | created_at | transformation_id
```

## 3. Choose and document the reference standard

Possible sources include pathology, microbiology/laboratory tests, surgery, longitudinal follow-up,
expert image review, validated clinical criteria or a prespecified composite. Choose by the target
construct, not convenience.

For every source specify:

- timing relative to index imaging and any intervening treatment/disease change;
- who/what produced it, qualifications, calibration and technical quality;
- information available and blinding to index model/test and competing references;
- whether all participants receive the same standard and why missing verification occurs;
- independence: whether the index test/model output is incorporated into the reference;
- disagreement, uncertainty and adjudication process;
- criterion/version and known sensitivity/specificity or applicability limitations.

A composite standard needs an explicit deterministic or adjudicated rule. “Clinical diagnosis” without
its evidence/time window is not reproducible.

## 4. Bias safeguards

| Threat | Required safeguard or boundary |
|---|---|
| Partial verification | verify all or a prespecified unbiased sample; characterize unverified cases and consider correction/sensitivity |
| Differential verification | justify and model/stratify different standards; do not pool them as identical truth |
| Incorporation bias | keep index/model output out of reference where possible; otherwise disclose and test an independent source |
| Review bias | blind reference assessors to index result/hypothesis where feasible; record information seen |
| Spectrum bias | label a pathway-representative cohort or bound an enriched/case-control sample |
| Temporal misclassification | align reference window and account for disease/treatment change |
| Consensus concealment | preserve individual reads and disagreement before consensus |

If the reference process differs across sites/time, treat `reference_standard_version/site` as part of
the measurement process and analyze heterogeneity.

## 5. Reader/adjudication protocol

- Define reader count, expertise, training/calibration set and minimum information.
- Use independent primary reads when reproducibility or consensus bias matters.
- Specify majority, consensus, third-reader or evidence-panel adjudication; adjudication is a new
  measurement process, not proof the final label is error-free.
- Capture individual labels, confidence/uncertainty, reason codes and timestamps before adjudication.
- Keep evaluation readers independent of model development and, where possible, index-model output.
- Predefine re-read sampling and inter-/intra-reader agreement using a statistic matched to scale/unit.

## 6. Quality-control and release gate

Before labels enter development/evaluation:

1. validate ID/unit/time joins and one-to-many expectations;
2. check allowed codes, hierarchy, units, laterality and impossible combinations;
3. audit a stratified sample against primary source locations;
4. reconcile duplicates, conflicts, missing and non-evaluable states without deleting history;
5. quantify source/reader/site/version-specific disagreement;
6. freeze ontology, extraction/adjudication code and label snapshot digest;
7. publish a label/data card with known error and applicability boundaries.

Return `STOP_FOR_REPAIR` when the construct/unit/time is undefined, reference timing is incompatible,
model output circularly defines the evaluation reference without disclosure, source locators cannot be
audited or missing/unverified cases disappear from the cohort flow.

## 7. Claim boundary and output

Reference agreement supports performance relative to that process. It does not prove biological truth,
clinical benefit or transport to a different reference process. Report:

`construct/ontology card -> reference-standard hierarchy -> reader/adjudication protocol -> bias and
verification audit -> label schema/snapshot -> agreement/error profile -> exclusions/non-evaluable
flow -> claim ceiling -> deviations`.

## Primary and official sources

- Tejani AS, et al. [CLAIM 2024 Update](https://doi.org/10.1148/ryai.240300) (uses “reference standard”).
- Bossuyt PM, et al. [STARD 2015](https://doi.org/10.1136/bmj.h5527).
- FDA–NIH. [BEST Resource](https://www.ncbi.nlm.nih.gov/books/NBK326791/).
- RSNA. [RadLex](https://radlex.org/).
- DICOM Standards Committee. [Current DICOM Standard](https://www.dicomstandard.org/current/).

Terminology and clinical criteria are versioned; verify live applicability with the clinical-domain and
reporting owners.
