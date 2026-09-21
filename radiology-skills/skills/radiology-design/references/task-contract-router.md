# Imaging task-contract router

Open exactly one primary task contract after the clinical question and before choosing an algorithm.
A study may have secondary tasks, but each confirmatory claim gets its own target, unit, reference,
metric and failure policy. Do not merge task endpoints into a generic "model performance" claim.

## Route by the decision the output supports

| Primary task | Open | Distinguishing lock |
|---|---|---|
| find and localize one or more findings | [tasks/detection-localization.md](tasks/detection-localization.md) | lesion matching, missed/unmarked truth, false positives per case and patient-level aggregation |
| delineate or quantify a structure | [tasks/segmentation-quantification.md](tasks/segmentation-quantification.md) | empty masks, boundary/volume error, topology and downstream measurement consequence |
| classify, diagnose or prioritize work | [tasks/diagnosis-triage.md](tasks/diagnosis-triage.md) | pathway prevalence, threshold/action, indeterminate/abstention and time-to-attention |
| estimate future risk or time-to-event | [tasks/prognosis-risk.md](tasks/prognosis-risk.md) | time zero, horizon, censoring/competing events, calibration and clinical decision |
| measure change or treatment response | [tasks/response-longitudinal.md](tasks/response-longitudinal.md) | baseline/landmark, registration, scan interval, treatment changes and change beyond measurement error |
| reconstruct, denoise, accelerate or enhance images | [tasks/reconstruction-enhancement.md](tasks/reconstruction-enhancement.md) | reference availability, data fidelity, hallucination risk, task preservation and dose/time trade-off |
| generate synthetic images, paired modalities, lesion insertions or synthetic cohorts | [tasks/synthetic-imaging-generation.md](tasks/synthetic-imaging-generation.md) | source-patient lineage, no synthetic clinical-n inflation, matched real-only baseline, untouched-real evaluation and privacy/memorisation threat model |
| generate, structure or align reports with images | [tasks/report-generation-vlm.md](tasks/report-generation-vlm.md) | finding-level truth, prior comparison, critical omission/hallucination and human editing/workflow effect |

## Contract shared by every task

Freeze, in order:

`target object -> intended decision -> independent unit/hierarchy -> reference standard and timing ->
sampling/enrichment -> primary metric and uncertainty -> matching/aggregation -> threshold/action ->
indeterminate/abstention/failure handling -> workflow consequence -> transport shift -> claim ceiling`.

Then bind the task contract to:

1. the `radiology-clinical-domain` clinical-context lock;
2. the `radiology-acquisition-qc` measurement passport;
3. the annotation/ground-truth passport;
4. the validation split and protected-test policy; and
5. the statistical brief for clustering, uncertainty, multiplicity and missingness.

If the output changes the clinical decision, independent unit, reference standard, matching rule or
primary metric, issue a new task contract rather than calling it a routine model variant.
