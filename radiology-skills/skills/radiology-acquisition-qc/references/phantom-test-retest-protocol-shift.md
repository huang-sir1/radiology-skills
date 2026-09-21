# Phantom, Test-Retest, and Protocol-Shift Evidence

Use this common playbook whenever the claim involves repeatability, longitudinal change,
cross-scanner/site comparability, reconstruction sensitivity, harmonisation or absolute
quantification. Load it in addition to the active modality playbook.

This module owns acquisition-side study design, measurement-state classification and the transport
claim ceiling. `radiology-stats` owns final numerical inference; `radiology-method-evaluation` owns
comparative method claims; `radiology-translation` owns prospective workflow utility.

## Separate the metrology questions

Do not use these terms as synonyms:

| Question | Evidence target |
|---|---|
| accuracy/trueness | closeness or systematic difference relative to a justified reference value |
| precision | dispersion under stated conditions |
| repeatability | precision under deliberately specified near-same conditions |
| reproducibility | precision when named conditions change, such as site, system, operator or protocol |
| agreement | magnitude and pattern of differences between methods/occasions |
| reliability | discrimination among subjects relative to total variability; depends on sample heterogeneity |
| clinical validity/utility | association with clinical truth or improvement in a clinical decision/workflow |

High reliability can coexist with poor agreement or large bias. Phantom precision does not prove
clinical validity, patient-level repeatability or utility.

## Measurement-claim ladder

Evaluate the exact rung requested; evidence does not automatically climb upward:

1. `visual adequacy` — the intended anatomy/signal can be reviewed for a stated use.
2. `within-protocol relative measurement` — ordering or relative differences are defensible inside
   a fixed acquisition/reconstruction chain.
3. `within-site quantitative measurement` — units and repeatability are supported for a bounded
   system/protocol.
4. `longitudinal change` — repeatability and technical-change evidence allow observed change to be
   separated from measurement error for the target interval/use case.
5. `cross-site/platform absolute comparability` — calibration, reproducibility and untouched
   transport evidence support the stated systems/sites/population.

When a higher rung fails, preserve the strongest lower rung that remains supported and state the
prohibited upgrade.

## Design a task-matched phantom study

### Prespecify

- exact measurement object, unit, intended clinical range and allowable claim;
- phantom identity/version, material/reference values and traceability or justification;
- acquisition protocol, scanner/system, software, reconstruction/post-processing and analysis
  algorithm/version;
- number/timing of repeated acquisitions, full repositioning/re-setup rule, sites/operators and
  service/software states;
- primary metric, uncertainty interval and acceptance criterion before results;
- retained raw/source data, all reconstructions, failure/repeat log and environmental variables.

### Match the threat

| Threat being tested | Minimum perturbation |
|---|---|
| short-term precision | independent repeat acquisitions, not repeated clicks on one image |
| positioning sensitivity | complete phantom removal/repositioning and reacquisition |
| reconstruction sensitivity | multiple prespecified reconstructions from the same source/raw data |
| scanner/protocol reproducibility | crossed or clearly nested scanner/protocol/site design |
| drift | repeated QC over calendar time with service/software events logged |
| absolute bias | justified reference values spanning the task-relevant range |

Same-raw-data reconstruction perturbation is valuable because biology is fixed, but it estimates
reconstruction dependence—not independent acquisition repeatability or external generalization.
Phantom findings should be bridged to patient data when anatomy, motion, physiology, tracer/contrast
kinetics or disease heterogeneity materially affect the measurement.

## Design a human test-retest study

1. Justify that biology should be sufficiently stable over the interval for the intended estimand.
2. Record treatment, intervention, contrast/tracer, preparation and physiologic events between
   scans; do not label treatment-spanning scans “test-retest.”
3. Repeat the full acquisition with repositioning and the intended operator workflow. Repeating ROI
   placement on one acquisition estimates reader/analysis repeatability only.
4. Preserve paired patient identity and all nested lesions/series/frames. Split, resample and analyze
   at the correct independent level.
5. Prespecify valid/failed/nondiagnostic rules and report the failure rate, not only valid pairs.
6. Justify scan burden, radiation/contrast exposure, consent and local ethics/governance; route
   authorization decisions to `radiology-ethics` and the responsible clinical team.
7. Sample the measurement range and population in which the repeatability claim will be used.

## Statistical specification to hand off

State the estimand and conditions, then send calculations to `radiology-stats`. Useful outputs may
include:

- within-subject standard deviation and coefficient of variation with uncertainty;
- repeatability coefficient/limits under explicit distribution and homoscedasticity assumptions;
- absolute and proportional bias with Bland-Altman-style limits, using a repeated-measures or
  clustered method when needed;
- concordance correlation where both precision and bias matter;
- ICC with model, effects, unit (single/average) and consistency versus absolute-agreement choice
  fully named;
- smallest detectable change or profile-specific repeatability boundary with uncertainty;
- failure/nondiagnostic rate and missing-pair analysis.

Do not adopt a universal ICC/CV/change threshold. A threshold must come from the prespecified use,
measurement scale, consequence and applicable validated profile. Compare longitudinal biological
change to measurement error; a statistically nonzero mean change alone is insufficient.

## Build the protocol-shift ledger

Create one row per patient/examination/time point and retain:

- site, scanner/system, manufacturer/model, hardware, software, service/upgrade state and date;
- acquisition protocol and all modality-critical parameters;
- contrast/tracer/agent, preparation, operator and timing/physiology where applicable;
- reconstruction, correction, post-processing and derived-map algorithm/version;
- calendar period, referral/clinical setting and outcome prevalence;
- whether each factor is represented during development, represented only in evaluation, or wholly
  unseen;
- any recalibration, normalization, harmonisation, threshold change or manual review using
  evaluation-site data.

Site, calendar period, device and outcome can be confounded. A domain classifier or successful site
removal does not prove biological signal preservation or causal correction.

## Transport and harmonisation decision grid

| Evaluation state | Label | Allowed claim |
|---|---|---|
| same represented sites/protocols in a patient-independent held-out set | internal held-out | performance within represented acquisition levels |
| a held-out site/protocol whose data never influence fitting, preprocessing, feature selection, calibration or thresholds | untouched external/transport evaluation | transport to that specific unseen setting, bounded by sample and shift |
| evaluation-site images used without labels to learn normalization/harmonisation | unsupervised adaptation or transductive evaluation | adapted performance, not untouched external validation |
| evaluation labels/outcomes used for any choice or calibration | supervised adaptation/redevelopment | adapted/retrained performance with a new protected test required |
| only phantom or same-raw reconstructions tested | technical sensitivity | no clinical external-generalization claim |

Executable rules:

- fit normalization, harmonisation, feature selection and thresholds on development data only for an
  untouched evaluation;
- retain the native/raw primary analysis; label harmonised or corrected results as prespecified
  secondary/sensitivity unless the deployment path includes that frozen transform;
- validate that harmonisation preserves the target measurement and biological ordering, not only
  that site separability falls;
- stratify or cross scanner/protocol effects when the data support it; expose sparse or missing
  combinations rather than assuming exchangeability;
- never claim that harmonisation repairs absent metadata, invalid units, failed acquisition QC,
  missing anatomy or an outcome-confounded site;
- after any evaluation-set adaptation, require a further untouched dataset for a new external-
  validation claim.

## Gate and claim ceiling

- `PASS` for the exact rung only when the task-matched design, independent unit, protocol/shift
  ledger, QC, uncertainty and protected evaluation state support it.
- `CONDITIONAL` when evidence supports a narrower within-protocol/site/range claim or a
  sensitivity-bounded result.
- `STOP` for the higher claim when no full-acquisition repeats exist, technical/biological change is
  inseparable, site/outcome confounding is dominant, evaluation data influenced fitting without
  disclosure, or missing/invalid acquisition information determines the measurement.

Required output:

1. claim rung and estimand;
2. represented versus wholly unseen levels;
3. perturbations and independent unit;
4. native primary and all adaptation states;
5. uncertainty/failure evidence;
6. `PASS / CONDITIONAL / STOP` plus allowed wording, prohibited upgrade and smallest next action.

## Handoff

- modality fields and physical failure return to the active modality playbook;
- data inventory/splits and de-identification go to `radiology-data`;
- numerical estimation and uncertainty go to `radiology-stats`;
- method comparison/ablation goes to `radiology-method-evaluation`;
- downstream feature/model execution goes to `radiology-radiomics` or
  `radiology-deep-learning`;
- prospective thresholds, reader workflow and clinical utility go to `radiology-translation`;
- disease endpoint/reference-standard meaning goes to `radiology-clinical-domain`.

The receiving owner must preserve the measurement verdict and adaptation label.

## Authoritative source ledger

- DICOM Standard Committee. [Current DICOM Standard](https://www.dicomstandard.org/current/).
- RSNA QIBA. [Profiles index](https://qibawiki.rsna.org/index.php/Profiles). Select the exact
  modality/use-case profile and verify its stage, actors, procedures and conformance conditions.
- RSNA QIBA. [CT Small Lung Nodule Volume Profile
  2023](https://doi.org/10.1148/QIBA/20231219).
- RSNA QIBA. [Diffusion-Weighted MRI and ADC Profile
  2022](https://doi.org/10.1148/QIBA/20221215).
- RSNA QIBA. [FDG-PET/CT Response Profile
  2023](https://doi.org/10.1148/QIBA/20230615).
- RSNA QIBA. [Ultrasound Shear Wave Speed Profile
  2024](https://doi.org/10.1148/QIBA/20240115).
- American College of Radiology. [Practice Parameters and Technical
  Standards](https://www.acr.org/Clinical-Resources/Clinical-Tools-and-Reference/Practice-Parameters-and-Technical-Standards).

Profiles and standards are versioned and scoped. Verify the current authoritative artifact and
local applicability; the citation itself is not evidence that a study, site or device conforms.
