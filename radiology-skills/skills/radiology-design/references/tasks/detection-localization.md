# Detection and localization study contract

Use this contract when the output says **whether** a target is present and/or **where** it is by
point, box, heatmap, candidate list or region proposal. A detector is not a segmenter, a diagnostic
classifier or a triage intervention unless those additional claims are separately designed and tested.

## 1. Freeze the task and intended use

Record before modelling:

| Field | Required specification |
|---|---|
| Population and pathway | screening, diagnostic work-up, surveillance, emergency or other setting; prevalence/spectrum |
| Modality and input | exact series/phases/views, prior examinations and clinical information available at inference |
| Target | finding/lesion/anatomy, minimum clinically relevant size or visibility boundary, single versus multiple targets |
| Output | case score, candidate score, point, box, heatmap or another frozen representation |
| Independent unit | normally patient/examination; state lesion and series nesting explicitly |
| Intended action | second read, concurrent aid, worklist prioritisation, rule-out, candidate prompting or research-only |
| Primary estimand | e.g. case sensitivity at frozen specificity, or lesion sensitivity at a frozen false-positive rate per examination |
| Comparator | standard workflow, unaided reader, prior algorithm or simple image/clinical baseline |
| Claim ceiling | feasibility, internal test, external test, reader effect or live-workflow impact |

Do not optimize a detection metric until the intended action fixes which misses and false alarms matter.

## 2. Cohort, acquisition and reference standard

- Assemble through the real pathway or state enrichment explicitly. A lesion-enriched case-control set
  can estimate bounded discrimination but not workflow prevalence, predictive values or workload.
- Freeze eligible modalities, series-selection rules, reconstruction/protocol ranges, image-quality
  exclusions and handling of incomplete examinations. Route technical acceptance to the acquisition
  owner and preserve a DICOM/series manifest.
- Define the reference standard per target: pathology, longitudinal imaging, expert panel, multimodal
  consensus or another justified composite. Record blinding, information available, adjudication,
  uncertainty and verification timing.
- For multiple lesions, specify which lesions count, whether occult/incidental targets count, how
  duplicates are merged and how candidates are matched to references. Matching radius/IoU and one-to-
  one versus many-to-one assignment are analysis decisions, not plotting details.
- Keep indeterminate, non-evaluable and unverified examinations visible. Do not silently relabel them
  negative.

## 3. Partition and leakage contract

- Split by patient; keep all examinations, lesions, slices, crops and derived views from one patient
  together. Account for families, bilateral organs or repeat acquisitions when they create dependence.
- A geographic/temporal claim requires the corresponding untouched site/period. Randomly mixing sites
  and holding out cases is not external testing.
- Fit preprocessing, candidate generation, hard-negative mining, threshold selection, calibration and
  post-processing using development data only. Test-set error review cannot feed another reported test
  result without a new independent set.
- Audit report-derived labels, acquisition metadata, overlays and burned-in annotations for target
  leakage. Pretrained models require a documented source/overlap audit where feasible.

## 4. Endpoint and analysis contract

Choose a primary level and preserve the hierarchy:

| Question | Suitable primary analysis | Mandatory context |
|---|---|---|
| Is any target present in the examination? | sensitivity/specificity or ROC/PR measure at case level, with CI | prevalence/spectrum and frozen threshold |
| How many true lesions are found at an acceptable alarm burden? | FROC sensitivity at prespecified false positives per examination | candidate-matching rule and patient-clustered uncertainty |
| Is the target localized closely enough for the action? | localization success at prespecified distance/IoU/tolerance | clinical justification for tolerance and size strata |
| Does prompting improve readers? | paired MRMC change in accuracy/sensitivity and reading time | reader/case variance, order, washout and automation-related errors |

- Average precision/mAP is allowed only with the IoU convention, averaging rule and clinical meaning
  stated; it does not replace clinically interpretable operating points.
- Report false positives **per examination**, not only per image/slice, when the user experiences an
  examination-level alarm burden.
- Estimate uncertainty at the highest independent unit using cluster-aware bootstrap/model methods.
  Do not treat lesions, candidates, slices or folds as independent patients.
- Report performance by lesion size/visibility, site, scanner/protocol and clinically relevant subgroup
  when adequately supported. Small subgroups yield uncertainty, not proof of equivalence.
- Lock operating points on development/validation data. Report the frozen threshold result first; any
  test-set recalibration is model updating and consumes independence.

## 5. Baselines, stress tests and failure evidence

Minimum comparators: a no-skill/prevalence or simple image baseline, an established detector if
available, and the actual clinical comparator implied by the claim. Predefine:

- small/subtle, multiple, overlapping and edge-of-field lesions;
- normal examinations and common mimics;
- motion, implants, altered anatomy, missing series and protocol shift;
- duplicate candidates, wrong-side/wrong-organ localization and high-confidence false positives;
- center/time-held-out performance and raw-scale performance before any adaptation.

Keep a false-positive/false-negative atlas tied to stable case IDs and adjudication state. Examples are
diagnostic evidence, not a substitute for denominator-based estimates.

## 6. Sample-size and stop gates

Plan from the primary estimand, target-positive and target-negative cases, lesion multiplicity,
precision/power target, paired design, reader/case variance and non-evaluable rate. No universal case,
lesion or reader count is defensible.

Return `STOP_FOR_REPAIR` when the target/matching rule changes after test access, reference-standard
verification depends on the model output without a correction plan, patient overlap crosses partitions,
or the primary unit/denominator cannot be reconstructed. Return `BIOSTATISTICIAN_REQUIRED` for unresolved
clustered FROC/MRMC inference or sample-size inputs.

## 7. Allowed claim ladder

- Internal held-out performance -> bounded performance in the sampled cohort.
- Untouched site/time testing -> transport to the named domain only.
- Controlled reader study -> effect on readers under that reading design.
- Prospective live-workflow study -> effect on the prespecified workflow endpoints.

Detection/localization performance alone does not establish diagnosis, patient benefit, workload
reduction, safety or deployment readiness.

## 8. Required handoff

Return: `task card -> cohort/acquisition manifest -> reference-standard and candidate-matching contract
-> split/test-access manifest -> primary endpoint/threshold -> analysis and sample-size brief -> baseline
and stress-test matrix -> failure atlas -> claim ceiling -> unresolved inputs/deviations`.

## Primary and official sources

- Tejani AS, et al. [CLAIM 2024 Update](https://doi.org/10.1148/ryai.240300).
- Bossuyt PM, et al. [STARD 2015](https://doi.org/10.1136/bmj.h5527).
- Sounderajah V, et al. [STARD-AI](https://doi.org/10.1038/s41591-025-03953-8).

Reporting-guideline versions are live facts; verify them through `radiology-reporting` at protocol
freeze and submission.
