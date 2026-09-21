# Longitudinal lesion and examination linkage contract

Use this reference to connect examinations and lesions across time without leaking outcome information
or hiding ambiguous identity. Longitudinal linkage is a measurement process: it needs rules, provenance,
reader agreement and failure states.

## 1. Identity hierarchy

Maintain stable, de-identified keys:

```text
patient_id -> clinical_episode_id -> exam_id -> series_id -> lesion_track_id -> observation_id
```

- `exam_id` represents one acquisition episode with date/time, modality and protocol.
- `lesion_track_id` represents a hypothesized same lesion through time; it is not an image-coordinate ID.
- `observation_id` is one lesion assessment on one exam/series by one reader/algorithm/version.
- Keep side, organ/segment, anatomic landmarks and frame of reference as attributes; never join only by
  row order, lesion number or free-text name.

All timepoints for one patient remain in one development/test partition.

## 2. Freeze the clinical and temporal frame

Record:

| Field | Required specification |
|---|---|
| Episode/time zero | diagnosis, treatment start, surgery or other event with evidence locator |
| Visit labels/windows | baseline, on-treatment, follow-up and allowed deviation |
| Eligible exams | modality/series/phase/protocol and quality rules |
| Lesion universe | target, non-target, new, resolved and incidental lesions |
| Criteria/version | disease-specific rule and live verification owner |
| Information available | prior scans, reports, treatment/outcome and model output visible to linker |
| Linkage output | same/new/split/merge/resolved/indeterminate/non-evaluable with confidence/reason |

Chronological position alone is not a clinical timepoint. Store actual timestamps/windows and treatment/
intervention changes.

## 3. Linkage procedure

1. Select eligible exams/series without outcome/model-error knowledge.
2. Register or co-display images using a prespecified method; record failures and manual corrections.
3. Identify candidate correspondence from anatomy, side/segment, morphology and spatial relationship.
4. Assign a linkage state and reason; do not force ambiguous lesions into a track.
5. Independently review a prespecified subset or all decision-critical tracks.
6. Adjudicate disagreements under a frozen rule while preserving original reads.
7. Freeze the linkage snapshot/version before downstream delta/response analysis.

If a model proposes links, record model/version, inputs and confidence; final human acceptance is a new
annotation state, not independence from the proposal.

## 4. Split, merge, disappearance and new lesions

Predefine:

- one lesion splitting into several observations and several merging into one;
- lesions below visibility, obscured by treatment/artifact or outside coverage;
- complete response/disappearance versus non-evaluable absence;
- newly appearing lesions versus retrospectively recognized baseline lesions;
- target-lesion replacement and handling of resection/ablation;
- whether aggregate burden, selected targets or all lesions define the patient endpoint.

Never renumber lesions after outcome review without retaining the old-to-new mapping and result-aware
deviation. A “new lesion” may carry specific clinical meaning under a criterion; verify it with the
clinical-domain owner rather than inferring from geometry alone.

## 5. Registration and measurement boundary

- Record rigid/deformable method, fixed/moving image, transforms, resampling/interpolation and software
  version. Save transform and QC artifacts.
- Assess gross anatomic plausibility and target-region alignment; a high global similarity score may
  conceal local failure.
- Separate linkage uncertainty from segmentation/measurement uncertainty. Propagated masks require
  human QC and an edit/failure record.
- Delta smaller than technical repeatability/registration/annotation error cannot be interpreted as
  established biological change.

## 6. Linkage manifest

Minimum row fields:

```text
patient_id | episode_id | exam_id | acquisition_datetime | visit_label | series_id | lesion_track_id |
observation_id | side/anatomy | linkage_state | parent_track_ids | registration_id | reader/model_id |
confidence_state | reason_code | adjudication_state | criteria_version | treatment_state |
source_locator | annotation_version | created_at
```

Preserve a separate exam-level manifest for missing/off-window/non-evaluable scans and reasons.

## 7. Quality, agreement and sensitivity

- Audit missing exams, duplicate IDs, impossible chronology, side/anatomy changes and orphan masks.
- Quantify linkage agreement on patient/track decisions with uncertainty; raw percent agreement plus a
  scale-appropriate statistic may be useful, but prevalence-sensitive measures need context.
- Stratify failures by lesion size/morphology, modality/protocol, interval and treatment state.
- Repeat downstream analysis under plausible alternative ambiguous links, target-lesion rules and visit
  windows when they could change the conclusion.
- Keep the linker blinded to outcome/model prediction when feasible; otherwise record information seen
  and perform an independent sensitivity audit.

## 8. Stop gates and claim boundary

Return `STOP_FOR_REPAIR` for unresolvable patient/exam identity, incompatible frame of reference,
untraceable manual relinking, outcome-guided linkage without disclosure, silent missing timepoints or
patient timepoints split across partitions.

Linkage supports correspondence under the stated criteria; it does not prove clonal identity, causal
evolution or response. Return:

`episode/visit contract -> exam/series manifest -> linkage SOP -> registration QC -> lesion-track
manifest -> ambiguity/agreement report -> downstream sensitivity -> claim ceiling -> deviations`.

## Primary and official sources

- Eisenhauer EA, et al. [RECIST 1.1](https://doi.org/10.1016/j.ejca.2008.10.026).
- Seymour L, et al. [iRECIST](https://doi.org/10.1016/S1470-2045(17)30074-8).
- DICOM Standards Committee. [Current DICOM Standard](https://www.dicomstandard.org/current/).

RECIST/iRECIST are oncology examples, not universal lesion-linkage standards; confirm the applicable
disease-specific criteria and version live.
