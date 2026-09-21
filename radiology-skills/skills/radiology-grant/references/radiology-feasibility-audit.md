# Radiology-specific grant feasibility audit

Run this for a full imaging proposal or whenever the central claim depends on image formation,
quantification, interpretation or image-derived prediction.

First expose the proposal's bridge:

`clinical phenomenon/bottleneck → knowledge gap → image physics/contrast source → reproducible
quantitative phenotype → biological/clinical proposition → matched validation or intervention →
bounded value`.

If a link is unsupported, lower the mechanism/causal/clinical claim. A model, database, platform or
heat map cannot substitute for the scientific proposition.

## Audit sequence

### 1. Intended use, task and independent unit

- Define the clinical/research decision, target population, setting, user and moment in the pathway.
- Freeze the task: detection/localization, segmentation/quantification, diagnosis/triage,
  prognosis/risk, longitudinal response, reconstruction/enhancement or report/VLM generation.
- Distinguish patient, examination, series, reconstruction, lesion, image/slice, reader and site.
  State which level is independent for splitting, sample size and inference.
- Name the comparator: standard of care, clinician unaided/aided, conventional model, acquisition or
  reconstruction alternative, or no-action baseline.

`STOP_AND_REFRAME` if the primary endpoint or unit changes between aims, cohort counts and analysis.

### 2. Image-formation and measurement chain

For each modality/aim record:

- acquisition timing, phase/sequence/view/tracer, device/vendor/field strength and key parameters;
- reconstruction algorithm/kernel/iterations/version, corrections and post-processing;
- series-selection rule fixed before outcomes/model performance are seen;
- raw, derived, display and analysis objects; units and quantitative definitions;
- DICOM/source metadata completeness, artifacts, nondiagnostic/failed acquisitions and QC;
- phantom/test–retest or repeatability evidence where the claim is quantitative;
- protocol/site/vendor drift, represented versus wholly unseen levels and adaptation policy.

Do not let harmonisation substitute for missing metadata or erase site–outcome confounding. If
external data are used to tune harmonisation, recalibration or thresholds, retain an untouched
evaluation or label the result as adaptation rather than wholly independent validation.

### 3. Cohort and availability arithmetic

Reconcile, per center and time window:

`eligible patients → examinations → usable target series → linked reference standard → analyzable
primary outcome → events/classes → development/validation allocation`.

Require reasons for exclusions and expected acquisition/QC failure. Distinguish existing accessible
data, data requiring approval/linkage, and prospective accrual. “Our PACS has N scans” is not a
matched, analyzable cohort.

For imaging–clinical–pathology–omics work, effective `n` is the successfully linked intersection at
the same patient/lesion/region/time window, not the sum of modality-specific counts. Report loss,
missingness mechanism and event/class counts at every join.

### 4. Reference standard and annotation

- Define the construct, reference standard, timing and permissible verification window.
- Specify pathology/follow-up/consensus/report-derived/weak labels and their limitations.
- Specify reader number/expertise, blinding, SOP, training, repeat reads, disagreement and
  adjudication.
- Quantify reliability/uncertainty at the correct level and plan sensitivity analysis for imperfect
  or differential verification.
- Audit index-test blindness, partial/differential verification and incorporation bias. A label
  derived from the same image or report is not automatically an independent reference standard.
- For longitudinal work, freeze lesion/exam linkage, new/resolved lesions and interval rules.

A more experienced annotator does not eliminate construct ambiguity or reference-standard bias.

### 5. Leakage, analysis and uncertainty

- Split at the highest dependent unit and preserve sites/time as the design requires.
- Keep preprocessing, feature selection, harmonisation, imputation and tuning inside training folds.
- Audit dataset aliases, repeated/near-duplicate examinations, the same patient across sites,
  pretraining corpora, foundation-model weights, prompt/RAG data and hosted-API retention. If a model
  may have seen the test source during pretraining, do not call the evaluation wholly independent.
- Justify sample/event/reader/site/cluster counts for the primary estimand; do not count slices as
  patients.
- Prespecify primary metric/estimand, uncertainty, calibration where relevant, multiplicity,
  missing data, subgroup/interaction and sensitivity analyses.
- Use paired/clustered/MRMC methods for reader or method comparisons as appropriate.
- Compare against meaningful baselines and report failure/nondiagnostic cases.

The budget and timeline must include statistical design/finalization before outcome-aware tuning.

Create an aim-level sample-size memo containing the primary estimand, independent unit, design
inputs and sources, plausible scenarios, non-evaluable/loss allowance, development/tuning/test
allocation, method/software/version, required `n` and accessible `n`. Do not impose a universal
10-events-per-variable rule or arbitrary AUC, Dice or ICC threshold.

### 6. Transport and prospective execution

- Name the intended transport claim: new time, site, scanner/vendor, protocol, population or pathway.
- Make validation units independent of development and document all external-data access.
- Separate frozen evaluation from recalibration/domain adaptation/fine-tuning.
- Record independence as a vector across patient, site, time, protocol, vendor, geography/population
  and pretraining lineage. External data used for harmonisation, recalibration, threshold selection,
  fine-tuning or prompt selection are adaptation data; reserve an untouched test or lower the
  transport claim.
- For prospective or clinical-impact work, specify workflow integration, eligible-patient capture,
  override/failure handling, monitoring, operator training and adoption/human-factors endpoints.
- Reader improvement does not establish patient benefit; workflow speed does not establish safety.

### 7. Data, software, compute, security and ethics

- Inventory image bytes, DICOM metadata, labels, clinical/pathology/outcome joins and identifiers.
- Define de-identification, burned-in-pixel checks, linkage keys, access controls, retention/sharing
  and cross-border/cloud restrictions.
- Lock code/model/container/dependency versions, compute/storage/egress estimates, backup and run
  receipts.
- Record ethics/privacy/security status as approved, pending, not submitted or not applicable; never
  predict approval.

For a China/NSFC route, pure clinical/imaging/protein/metabolite data are excluded from the current
human-genetic-resource implementation rule's definition of HGR information, but they remain
sensitive health information subject to ethics, privacy and security controls. Imaging linked to
biospecimens, genes/genomes or linkable HGR data may trigger HGR review. Treat the 2026 HGR revision
consultation draft as `DRAFT_NONCONTROLLING`. Audit multicentre, cloud, cross-border and hosted-model
data flows separately.

### 8. Team, milestones, risk and budget

Map actual people and effort to radiology acquisition/QC, clinical domain, annotation, statistics,
data engineering, ML/radiomics, ethics and implementation. A collaborator's name without role,
availability or dependency does not close a capability gap.

Use `task → required expertise → named person → effort → inspectable deliverable → data/equipment
permission or collaboration evidence → backup owner`. Prioritize preliminary evidence that closes
the highest execution risk: access, accrual, measurement repeatability, label reliability,
multimodal matching or a critical experiment—not only the best AUC.

For each aim define:

- inspectable milestone and date;
- evidence-based go/modify/stop decision rule;
- leading indicators (access/accrual/QC/annotation) rather than only final performance;
- risk trigger, impact, mitigation, fallback and affected claim ceiling;
- budget quantities for acquisition, contrast/tracer/assays, annotation/adjudication, readers, core
  facilities, external sites, compute/storage/software, governance and dissemination.

Do not invent universal AUC, Dice, ICC or accrual thresholds. Justify project-specific criteria from
clinical relevance, measurement error, prior evidence, minimum viable inference and available
resources.

### 9. Mechanism evidence ladder

When the proposal claims a biological mechanism or causality, map its evidence to:

`association → independent replication → orthogonal pathology/molecular evidence → spatial or
temporal matching → targeted perturbation → rescue/counterfactual validation`.

Enrichment, significant correlation, SHAP, attention or saliency maps alone do not establish
mechanism. Pure metrology or transport studies do not need an artificial animal experiment; require
higher-rung evidence only when the claim needs it.

## Radiology gate output

| Domain | Verdict | Proposal evidence | Key gap | Repair/owner | Claim impact |
|---|---|---|---|---|---|
| Intended use/task/unit |  |  |  |  |  |
| Phenotype–mechanism/clinical bridge |  |  |  |  |  |
| Acquisition/reconstruction/QC |  |  |  |  |  |
| Cohort/multimodal intersection |  |  |  |  |  |
| Reference standard/annotation |  |  |  |  |  |
| Data/model-lineage leakage and statistics |  |  |  |  |  |
| Aim-level sample size |  |  |  |  |  |
| External-independence/prospective transport |  |  |  |  |  |
| Mechanism evidence / claim ceiling |  |  |  |  |  |
| Data/compute/security/ethics |  |  |  |  |  |
| Team/milestones/risk/budget |  |  |  |  |  |

Use `PASS / CONDITIONAL / FAIL / NOT_ASSESSABLE`. Passing this gate means the written plan exposes
the necessary measurement and execution controls; it does not prove the future study will succeed.

## Primary frameworks used to derive the gate

Select study-specific frameworks with `imaging-methodology-router.md`; do not route every imaging
proposal to CLAIM or treat checklist completion as validity.

- CLAIM 2024 update for AI in medical imaging:
  https://doi.org/10.1148/ryai.240300
- STARD-AI for AI-centered diagnostic-accuracy studies:
  https://doi.org/10.1038/s41591-025-03953-8
- DECIDE-AI for early-stage clinical evaluation of AI decision support:
  https://doi.org/10.1038/s41591-022-01772-9
- Quantitative imaging biomarker metrology framework:
  https://doi.org/10.1148/radiol.2015142202
- DICOM current standard:
  https://www.dicomstandard.org/current/
- RSNA QIBA profiles for acquisition-to-measurement claims:
  https://qibawiki.rsna.org/index.php/Profiles

These reporting/metrology frameworks inform design completeness; compliance with a checklist does
not itself establish validity, feasibility or fundability.
