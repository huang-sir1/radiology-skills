# Materials and Methods — order and content (imaging/AI/radiomics)

Write M&M so a reader can reproduce and a reviewer can tick the checklist. Order:

## 1. Study design & ethics
- Retrospective/prospective; single/multi-centre; dates of data collection.
- IRB/ethics approval + consent (or waiver rationale); HIPAA/GDPR; trial/registry ID if
  applicable. Reporting guideline named ("reported following CLAIM/TRIPOD+AI/STARD").

## 2. Participants
- Eligibility (inclusion/exclusion) at patient level; consecutive vs selected; source
  population; **flow** (→ a flow diagram with counts). Prevalence/spectrum described.

## 3. Imaging technique
- Modality; **scanner vendor/model**, field strength; key acquisition parameters (kVp/mAs,
  TR/TE, slice thickness, contrast agent/dose/timing); reconstruction. Multi-scanner/protocol
  variation reported (supplement table if many).

## 4. Image analysis / reference standard / readers
- Reference standard and rationale (histology, follow-up, expert consensus) + its accuracy.
- Segmentation/measurement method + software; number, experience, and **blinding** of
  readers/annotators; adjudication; **inter-/intra-observer reproducibility (ICC/kappa)**.

## 5. Model / feature pipeline (AI, radiomics, radiogenomics)
- **Data partition** and its **unit (patient-level)**; train/validation/test definition; that
  the test set was untouched.
- Preprocessing (registration, resampling, normalisation) — **fit on training only**.
- Radiomics: IBSI-compliant extraction (resampling, **discretisation**, filters, software +
  version), feature reproducibility filtering, harmonisation method/fitting data and whether
  validation batch levels were represented; distinguish a frozen supported transform from
  unseen-site adaptation (ComBat is not automatically inductive). (→
  radiology-reporting/ibsi-features.md)
- Model: architecture/algorithm, hyperparameter tuning (on validation), training details,
  seed, hardware; code/model availability.
- Radiogenomics: omics source/processing, batch correction, integration/association method.

### Parameter and method-evaluation reporting

For each decision-bearing acquisition, preprocessing, QC, representation, model, threshold or
integration setting, report the value/range and unit; role; scientific/source rationale; when and on
which data it was fixed, derived or tuned; search space/budget/objective and stopping rule when
applicable; software/version; freeze point; deviations; and prespecified sensitivity or failure
boundary. For method comparisons, state the matched cases/splits/preprocessing, comparator/control,
tuning/compute conditions, ablation logic and negative controls. Put the complete parameter register,
configurations and seeds in Supplement/config/code with an exact main-text pointer. Use
`radiology-method-evaluation` to decide what needs evaluation; do not present a package default as
scientific rationale or test-set selection as validation.

## 6. Statistical analysis
- Primary endpoint and analysis; metrics (with the **CI method**); comparison tests (e.g.
  **DeLong**); **calibration** and **decision-curve** for prediction models; **multiplicity**
  control; software + version; significance threshold. (→ radiology-stats)

## Tense & style
Past tense; specific not vague ("3-T MRI" not "high-field"); name versions; one method, one
place (don't scatter the same detail). Hand wording to `radiology-polishing`.

## Self-check
`design+ethics? · eligibility+flow? · scanner+protocol? · reference standard+reader blinding+
ICC? · patient-level split+leakage controls? · IBSI/harmonisation fit data+unseen-batch support? · stats with CI
method+multiplicity? · decision-bearing parameters/rationale/selection data/freeze/sensitivity? ·
fair comparator/ablation conditions? · availability?`
