---
name: radiology-acquisition-qc
description: "Audit imaging acquisition, reconstruction, series eligibility, quantitative transforms and protocol drift; not model training."
---

# Imaging Acquisition, Reconstruction, and Measurement QC Router

Own the validity of the image as a measurement before annotation, feature extraction, model
training, biological interpretation, or clinical deployment. Route to the smallest relevant
modality playbook, freeze what was actually acquired and reconstructed, and return the strongest
claim the verified measurement chain permits.

## When to use

- "Can these acquisition/reconstruction parameters support a quantitative study?" /
  "这批影像的采集重建参数能不能支撑定量研究？" Series/phase/sequence selection and exclusion.
- "Can multi-center, multi-scanner, multi-protocol data be analysed together?" /
  "多中心、多扫描仪、多协议的数据能不能合并分析？"
- "How do I interpret artifacts, dose, phantom or test-retest results?" / "伪影、剂量、重复扫描结果怎么解释？"
- Freeze the measurement passport and claim ceiling before annotation, radiomics or model training.

## Ownership

This skill owns:

- acquisition, reconstruction and post-processing provenance;
- intended series/phase/sequence/view/tracer selection and exclusion rules;
- modality-specific artifacts, physical confounders and quantitative-unit validity;
- phantom, test-retest and reconstruction-perturbation design;
- protocol/site/scanner/software shift and the acquisition-side harmonisation boundary;
- an `Imaging measurement passport` and `PASS / CONDITIONAL / STOP` measurement claim ceiling.

It does not own disease eligibility or treatment rules, de-identification, ROI annotation,
radiomics/DL execution, statistical inference, clinical reader studies, mechanism interpretation,
or individual-patient care.

## Modes

| Mode | Use when | Output emphasis |
|---|---|---|
| `plan` | Designing acquisition/QC for a proposed study | minimum defensible protocol, stronger option, repeatability and shift plan |
| `audit` | Images, DICOM exports, protocols, Methods or QC artifacts exist | provenance gaps, series-selection bias, artifacts, sensitivity and claim repair |
| `mentor` | A learner has a clear acquisition/measurement question | decision ladder, physical rationale, falsifier, teach-back or transfer prompt |
| `interpret` | Real QC, phantom, test-retest or protocol-shift results are supplied | magnitude, uncertainty, failure boundary and surviving measurement claim |
| `writing-handoff` | Acquisition science is frozen | exact Methods/Results/Supplement fields, evidence state and prohibited upgrade |

Advisory and tutoring work is read-only. Create or update a passport only when the user requests a
durable artifact.

## Progressive routing

Resolve the active modality and measurement decision before opening references. Load only the
matching file or files:

| Active object | Load |
|---|---|
| CT, dual-energy/spectral CT, photon-counting CT, CT perfusion or CT-derived quantitative measurement | [references/ct-acquisition-reconstruction.md](references/ct-acquisition-reconstruction.md) |
| Structural/contrast-weighted MRI, DWI/ADC, DCE/DSC/ASL, quantitative mapping or MR reconstruction | [references/mr-acquisition-reconstruction.md](references/mr-acquisition-reconstruction.md) |
| MRS or MRSI, including metabolite ratios, fitted peaks or concentration estimates | MR core plus [references/mr-spectroscopy.md](references/mr-spectroscopy.md) |
| Task or resting-state BOLD fMRI, activation, connectivity or network measurement | MR core plus [references/functional-mri.md](references/functional-mri.md) |
| DTI, DKI, NODDI, fixel analysis, tractometry or tractography | MR core plus [references/diffusion-tensor-tractography.md](references/diffusion-tensor-tractography.md) |
| PET, PET/CT, PET/MR, SPECT, SPECT/CT, SUV, kinetic or count-based measurement | [references/pet-spect-acquisition-quantification.md](references/pet-spect-acquisition-quantification.md) |
| Ultrasound, Doppler, CEUS, strain or shear-wave elastography | [references/ultrasound-ceus-elastography.md](references/ultrasound-ceus-elastography.md) |
| Projection radiography, mobile radiography, mammography, DBT or synthetic 2D mammography | [references/projection-radiography-mammo-dbt.md](references/projection-radiography-mammo-dbt.md) |
| Phantom, test-retest, longitudinal change, multicentre protocol shift, harmonisation or reconstruction sensitivity | [references/phantom-test-retest-protocol-shift.md](references/phantom-test-retest-protocol-shift.md) |
| Fluoroscopy, DSA/angiography, cone-beam CT, image-guided or interventional imaging | `LOCAL_EXTENSION_REQUIRED`; do not substitute the CT or projection-radiography playbook |

For PET/CT load PET/SPECT plus CT; for PET/MR load PET/SPECT plus MR. For multimodal studies, load
only each modality that contributes to the requested measurement claim. Add the common
phantom/shift playbook when repeatability, longitudinal, cross-scanner, cross-site or absolute
quantitative equivalence is material.

Fluoroscopy, DSA/angiography, cone-beam CT and interventional imaging have time-dependent dose,
device, subtraction, geometry, procedural and safety contracts not represented here. Mark the route
`LOCAL_EXTENSION_REQUIRED` and stop acquisition-specific assurance until a dedicated, locally
verified playbook and responsible radiologist/physicist/procedural owner are supplied. Ordinary CT
or projection-radiography rules cannot be borrowed as a substitute.

## Required routing workflow

1. Name the requested measurement object and claim: visual adequacy, relative signal, absolute
   quantity, longitudinal change, cross-site comparability, reconstruction gain, or downstream
   input fitness.
2. Identify the independent hierarchy: patient -> examination/time point -> series/acquisition ->
   reconstruction/derived object -> frame/slice/voxel/measurement. Do not treat reconstructions,
   views, frames or repeated scans as independent patients.
3. Load the modality playbook and reconstruct the acquisition-to-measurement chain from supplied
   artifacts. Mark unsupported fields `AUTHOR_INPUT_NEEDED`; do not infer settings from a series
   description or filename.
4. Freeze the series/phase/sequence/view/tracer and reconstruction inclusion rule before outcome,
   model-performance or mechanism results are used to select inputs.
5. Add the common playbook when a repeatability or transport claim is intended. Distinguish a
   represented protocol/scanner level from a wholly unseen level and untouched evaluation from
   adaptation.
6. Assign `PASS`, `CONDITIONAL` or `STOP` to the exact measurement claim, then hand off the
   passport without upgrading its evidence state.

Use [templates/imaging-measurement-passport.md](templates/imaging-measurement-passport.md) for a
requested persistent/full audit artifact.

## Claim ceiling

- `PASS`: the acquisition, reconstruction, series rule, QC, units and applicable repeatability/
  transport evidence are traceable and fit the stated claim.
- `CONDITIONAL`: the measurement remains usable for a narrower population, protocol, relative
  comparison or sensitivity-bounded claim, with the unresolved source named.
- `STOP`: the central measurement is not identifiable or reproducible because the wrong/unknown
  series, invalid units, result-dependent input selection, dominant unbroken acquisition
  confounding, failed QC, or an unsupported quantitative transform determines the claim.

A standardized protocol is not proof of cross-platform equivalence. Phantom repeatability is not
clinical validity. Harmonisation is not a substitute for missing acquisition metadata, invalid
quantification or an outcome-confounded site. A derived map or model output is not a direct
physical measurement merely because it is stored as an image.

## Handoffs

| Requested decision | Unique owner | Send from this skill |
|---|---|---|
| disease pathway, endpoint, reference standard, treatment timeline or current clinical rule | `radiology-clinical-domain` | measurement passport, protocol limits, artifacts and claim ceiling |
| cohort inventory, DICOM de-identification, release or repository plan | `radiology-data`; governance to `radiology-ethics` | series/object inventory and sensitive-data flags without asserting authorization |
| ROI/VOI or reader annotation procedure | `radiology-annotation` | eligible series, geometry, resolution and artifact constraints |
| radiomics preprocessing/extraction | `radiology-radiomics` | accepted input series, units, reconstruction/shift and repeatability fields |
| imaging model/reconstruction network training | `radiology-deep-learning` | measurement target, input provenance, paired reference and protected evaluation rule |
| parameter comparison, ablation or method-fit judgement | `radiology-method-evaluation` | frozen parameter ledger and acquisition claim; numerical inference to `radiology-stats` |
| radiologist reader study, threshold-to-action or prospective workflow | `radiology-translation` | intended image presentation, failure/nondiagnostic states and measurement ceiling |
| imaging-to-pathology/omics mechanism | `radiology-radiogenomics` | physical contrast candidates, measurement state and technical alternatives |

## Output contract

Return only the parts needed for the selected mode:

1. `Route and evidence state` — mode, modality/subtype, requested measurement and supplied artifacts.
2. `Measurement chain` — acquisition -> reconstruction -> post-processing -> selected object -> value.
3. `Series and hierarchy lock` — included/excluded objects, unit and repeated-measure structure.
4. `Coverage and disposition denominators` — eligible, acquired, exported/received, QC-assessed,
   accepted, nondiagnostic and excluded counts at the declared grain, with reconciled reasons.
5. `QC and physical-confounder map` — artifact, likely effect, evidence, test and disposition.
6. `Repeatability/shift read` — when applicable, represented/unseen levels, raw primary analysis,
   adaptation status and sensitivity.
7. `Claim verdict` — `PASS / CONDITIONAL / STOP`, allowed wording, prohibited upgrade and smallest
   next action.
8. `Handoff` — exact fields and unresolved assumptions for the unique receiving owner.

## Boundaries

- Do not infer a scanner setting, dose, contrast/tracer exposure, sequence, reconstruction, QC pass
  or quantitative unit from convention.
- Do not prescribe or alter an individual patient's examination, contrast, radiation, diagnosis or
  treatment. Local protocol approval, radiation safety and equipment acceptance remain with
  qualified radiologists, technologists, medical physicists and institutional governance.
- Do not run a reconstruction, modify source images, or persist a passport unless the requested
  outcome authorizes that action.
- Exact standards, profiles and practice parameters are versioned and jurisdiction-dependent.
  Verify the current authoritative artifact and applicability before asserting conformance.
- Fluoroscopy, DSA/angiography, cone-beam CT and interventional imaging are
  `LOCAL_EXTENSION_REQUIRED`; this skill has no dedicated contract for them and must not upgrade a
  generic CT or X-ray review into modality- or procedure-specific assurance.
