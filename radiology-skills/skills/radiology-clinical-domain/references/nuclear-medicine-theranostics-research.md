# Nuclear medicine and theranostics imaging research playbook

Use this reference to design or audit clinical research involving PET, SPECT, hybrid imaging,
radiopharmaceutical biodistribution, theranostic pairs, targeted radionuclide/radiopharmaceutical
therapy, dosimetry or imaging response. It is not a procedure standard, treatment-eligibility rule,
prescribing guide, radiation-safety authorisation or patient-care tool. Tracer-, disease-, therapy-,
response- and jurisdiction-specific rules remain `LIVE_VERIFICATION_REQUIRED`.

## 1. Separate the pathway and research job

Declare one primary pathway and one decision. Do not pool radiopharmaceuticals because they use the
same scanner or molecular target name.

| Pathway | Research distinction |
|---|---|
| diagnostic detection/staging | tracer-specific target condition, clinical work-up, pathology/follow-up and intended add-on/replacement role |
| target-expression or eligibility imaging | exact target/ligand, positivity construct, treatment option, unavailable/discordant imaging and selection mechanism |
| biodistribution/first-in-human | molecule/radionuclide, mass/activity, sampling schedule, organ/lesion definition, safety and uncertainty |
| theranostic-pair development | diagnostic and therapeutic agents, shared target/ligand relation, evidence that one predicts distribution or effect of the other |
| targeted radionuclide therapy course | eligibility, administered product/activity, cycle schedule, co-therapy, post-therapy imaging, toxicity and outcome |
| patient-specific dosimetry | imaging/sampling schedule, activity quantification, time integration, dose model, target/organs at risk and uncertainty |
| response assessment | baseline tracer/exam, treatment, follow-up interval, response construct, outcome and target-expression change |
| prognosis/clinical impact | index examination, observed treatment pathway, horizon, competing events and causal/decision claim |

Keep these claims separate: tracer uptake, target availability, treatment eligibility, administered
activity, absorbed-dose estimate, biological effect, imaging response, clinical response and patient
benefit. None automatically proves the next.

## 2. Tracer and theranostic-pair identity lock

Create a pair passport before cohort or model design:

| Field | Diagnostic member | Therapeutic member |
|---|---|---|
| radionuclide | exact isotope and physical form | exact isotope and physical form |
| radiopharmaceutical | full nonproprietary/product name | full nonproprietary/product name |
| vector/ligand/target | molecule and target construct | molecule and target construct |
| pair relation | identical, chemically related, same target only, or empirical companion | identical, chemically related, same target only, or empirical companion |
| product/batch | manufacturer/site, synthesis and release source | manufacturer/site, synthesis and release source |
| administered quantity | assayed activity, time, residual/extravasation; mass/molar activity when relevant | assayed activity, time, residual/extravasation; mass/molar activity when relevant |
| patient preparation | preparation, medications/interventions and physiology | preparation, medications/interventions and physiology |
| acquisition/sampling | uptake/frame times and modality | post-therapy imaging/sampling schedule and modality |
| measurement | visual rule, uptake/kinetic quantity and unit | activity/time-integrated activity/dose quantity and unit |
| clinical use | detection, staging, eligibility, baseline or response | treatment, cycle planning, dosimetry or response |

- Same target does not guarantee identical affinity, pharmacokinetics, biodistribution, tumour
  penetration or normal-organ exposure.
- A diagnostic image can support a bounded selection construct only for the verified agent, disease,
  timing and rule. It does not measure delivered therapeutic absorbed dose by itself.
- Record competing/discordant imaging, heterogeneous target expression, tumour phenotype change and
  prior target-directed therapy.
- Do not infer tracer identity, radionuclide, activity, timing or unit from pixel appearance or a
  generic DICOM series description.

## 3. Time zero and complete theranostic timeline

Freeze a timeline with distinct clocks:

`disease/reference state -> diagnostic tracer administration -> diagnostic acquisition ->
eligibility decision -> treatment assignment -> therapy administration/cycle 1 -> post-therapy
imaging/sampling -> later cycles -> response examination -> toxicity assessment -> clinical outcome`.

- State whether time zero is diagnostic imaging, eligibility, therapy assignment, first
  administration, each cycle, landmark response or outcome follow-up.
- For survival or response analyses, avoid guarantee/immortal time created by requiring completion of
  multiple cycles, post-therapy imaging or dosimetry.
- Treat each cycle as a repeated exposure with changing disease, organ function, target expression,
  co-medication and administered activity.
- Keep calendar time and regulatory/product/protocol version. Radiopharmaceutical availability,
  reconstruction, eligibility and therapy pathways can drift.
- Align diagnostic and therapeutic agents closely enough for the claimed biological relation, or
  explicitly model the intervening treatment and phenotype change.

## 4. Minimum nuclear-medicine research passport

| Field | Required lock |
|---|---|
| disease/pathway | diagnosis/stage, prior therapies, referral source, treatment line and study period |
| intended use | detection, staging, eligibility, biodistribution, dosimetry, response, prognosis or workflow |
| tracer/pair | full diagnostic and therapeutic identity plus the claimed pair relation |
| population/denominator | all referred, all imaged, tracer-positive, treated, dosimetry-complete or another explicit stage |
| time zero/horizon | exact event, cycle/landmark, response window and competing-event policy |
| index measurement | visual/ordinal, SUV, kinetic, activity concentration, time-integrated activity, absorbed dose or other named quantity |
| unit and hierarchy | patient, therapy course, cycle, administration, scan, time frame, organ, lesion/voxel, reader, site and batch |
| comparator | pathology/standard imaging, alternative tracer, treatment, dose strategy, reader or clinical model |
| reference standard | source, mapping, timing, blinding, adjudication and uncertainty |
| response/outcome | tracer- and disease-appropriate construct, patient outcome, toxicity and horizon |
| dosimetry method | input data, software/version, segmentation, curve/model, mass/geometry and uncertainty |
| technical passport | calibration, acquisition, correction, reconstruction, QC and quantitative validity owner record |
| failure state | nondiagnostic/discordant imaging, extravasation, missing time point, nonquantifiable lesion/organ and incomplete therapy |

## 5. Unit hierarchy and denominator transitions

Use an explicit hierarchy:

`patient -> therapy course -> cycle/administration -> imaging/sampling visit -> organ/lesion -> voxel/
region -> frame/time point/reconstruction -> reader/measurement -> site/batch`.

- Lesions, organs, voxels, time frames and cycles are not independent patients. Dose-response and
  toxicity models must preserve their nesting and competing within-patient risks.
- Show denominators at referral, diagnostic imaging, evaluable imaging, eligibility, treatment,
  dosimetry completion, response imaging and outcome follow-up. Each transition can be selective.
- A tracer-positive treated cohort cannot estimate diagnostic utility or treatment effect in all
  referred patients without the appropriate comparator and selection model.
- Multiple lesions may receive different absorbed doses and responses. Patient-level benefit cannot
  be inferred by multiplying lesion observations.
- Record lesion emergence, coalescence, splitting and organ/lesion correspondence across diagnostic,
  post-therapy and response images.

## 6. PET/SPECT technical owner boundary

The clinical-domain owner defines disease pathway, intended use, pair hypothesis, population,
eligibility/response construct, reference standard, clinical endpoint and claim ceiling.

`radiology-acquisition-qc` owns the PET/SPECT measurement chain, including:

- radionuclide/radiopharmaceutical administration timestamps, assayed/administered activity,
  residual/extravasation evidence and clock alignment;
- patient preparation and uptake/acquisition timing as measurement conditions;
- scanner/gamma-camera, collimator, acquisition, corrections, attenuation map, reconstruction,
  calibration/cross-calibration, software and QC;
- SUV/normalisation, kinetic or count/activity-concentration quantity, unit, partial-volume and
  quantitative SPECT/PET validity;
- PET/CT, PET/MR and SPECT/CT component roles, registration/artifacts, repeatability and protocol
  drift.

For hybrid imaging, CT/MR validity stays with the corresponding acquisition playbook. The clinical
domain cannot certify quantitative PET/SPECT or dosimetry inputs, and acquisition QC cannot define
clinical eligibility, response or treatment benefit.

Dosimetry is a joint research interface: a qualified nuclear-medicine/medical-physics team owns the
local method and safety/regulatory implementation; acquisition QC establishes quantitative input
validity; this playbook fixes the clinical estimand, organs/lesions, cycles, outcomes and claim.
No skill output is a dosimetry prescription or therapy authorisation.

## 7. Reference standards and target truth

| Research target | Candidate reference | Critical qualification |
|---|---|---|
| lesion/disease detection | pathology, standard imaging, laboratory/clinical composite, longitudinal adjudication | verification selection, tracer incorporation and lesion matching |
| molecular target expression | spatially matched tissue assay, validated orthogonal assay or paired agent data | sampling, heterogeneity, interval, treatment and assay construct |
| treatment eligibility | prespecified verified clinical/tracer rule plus accountable multidisciplinary decision | rule/version, unavailable options, discordance and access |
| biodistribution | quantitative imaging and/or biological sampling under validated measurement chain | timing, calibration, metabolite/specimen semantics and model dependence |
| absorbed dose | traceable activity/time data and specified dose model | estimated quantity, geometry/mass assumptions, software/version and uncertainty |
| imaging response | tracer-/disease-/therapy-specific criteria with baseline and follow-up | target-expression versus burden change, timing and new-lesion rule |
| clinical response/outcome | prespecified clinical, laboratory, patient-reported, toxicity or survival endpoint | adjudication, competing events, treatment and follow-up |

- Tissue target expression from one biopsy does not represent all lesions or the later therapy state.
- Imaging uptake is influenced by delivery, perfusion, binding, metabolism, clearance, lesion size,
  partial volume and treatment, not target expression alone.
- An eligibility threshold is a decision rule, not continuous biological truth.
- Absorbed dose is model-derived; label it with method and uncertainty rather than “measured dose”
  unless the exact quantity is directly measured and defined.
- Reference criteria that include the index tracer require explicit incorporation-bias handling.

## 8. Dosimetry research contract

Freeze the quantity before analysis:

| Quantity | Do not confuse it with |
|---|---|
| assayed/administered activity (Bq and multiples) | activity concentration, uptake or absorbed dose |
| count rate/image intensity | calibrated activity concentration |
| activity concentration | time-integrated activity or absorbed dose |
| time-integrated activity | absorbed dose or biological effect |
| absorbed dose (Gy) | administered activity, equivalent/effective dose or treatment benefit |
| biologically effective/equivalent dose model | directly observed tissue injury or efficacy |

Record radionuclide data source, acquisition/sampling time points, calibration, quantitative imaging
method, registration, segmentation, organ/lesion mass or geometry, time-activity-curve model,
integration/extrapolation, S-values/voxel kernel/Monte Carlo or other dose engine, software/version,
cycle summation and uncertainty propagation.

- Prespecify target organs/lesions and the dose-response or dose-toxicity estimand. Searching all
  organs, lesions, time points and curve models after outcome inspection creates multiplicity and
  analytic flexibility.
- Sparse time-point methods require validation against a fuller schedule in the relevant tracer,
  organ, patient and workflow range.
- Missing late imaging, organ overlap, motion/registration, segmentation and partial-volume effects
  can be informative and lesion-size dependent.
- Dose estimates across methods, software versions, mass definitions or radionuclides are not
  interchangeable without a bridge.
- A dose-outcome association under selected treatment does not by itself prove that changing activity
  to target that dose will improve benefit or safety.

## 9. Response and target-expression change

Before calling response, lock:

- tracer/radiopharmaceutical, acquisition and quantitative method at baseline and follow-up;
- treatment start/cycles, co-treatment, response time point and confirmatory rule;
- lesion/organ/patient aggregation and handling of new, disappearing and nonevaluable lesions;
- disease- and tracer-specific response framework/version, outcome and reader blinding;
- repeatability boundary and minimum interpretable change under the tested protocol.

FDG PERCIST, PSMA-specific RECIP, Deauville-type systems and other response frameworks are not
interchangeable. Use each only in its verified disease, tracer, treatment and version scope.

- Falling uptake may reflect response, altered target expression, perfusion/delivery change,
  treatment timing or technical variation.
- Rising uptake may reflect progression, flare/inflammation, target upregulation, changed clearance
  or protocol drift.
- Disappearance on target-specific imaging does not establish eradication if dedifferentiated or
  target-negative disease remains possible.
- Imaging response is not automatically a validated surrogate for survival, symptoms, toxicity or
  quality of life.

## 10. Endpoints and study tasks

| Task | Primary target | Required companion evidence |
|---|---|---|
| diagnostic accuracy | patient- and lesion-level accuracy/calibration | verification flow, nonevaluable scans and clustering |
| eligibility/selection biomarker | treatment-strategy contrast or validated selection construct | comparator, threshold lock, discordance, access and interaction evidence |
| biodistribution/kinetics | prespecified organ/lesion quantity-time profile | measurement validity, sampling schedule, uncertainty and safety |
| dosimetry feasibility | successful traceable dose estimate and uncertainty under a workflow | missing time points, burden, repeatability and method comparison |
| dose-response/toxicity | prespecified dose-outcome relationship | organ/lesion hierarchy, confounding, cycle selection and multiplicity |
| imaging response | criterion-defined change at fixed time | repeatability, new-lesion handling, clinical/laboratory outcome |
| treatment effect | patient-important contrast versus valid comparator | assignment/confounding, adherence, co-treatment, toxicity and competing events |
| workflow/access | completion, time, burden, capacity or equity endpoint | unavailable tracer/scanner/therapy, travel, failures and stakeholder effects |

Report toxicity and patient-reported outcomes alongside tumour response when the research question is
therapeutic. Do not reduce the benefit-risk problem to uptake or tumour dose alone.

## 11. Major bias and leakage map

| Threat | Nuclear-medicine manifestation | Required response |
|---|---|---|
| tracer-positive selection | only eligible/treated positive patients analysed | show full referral/imaging denominator; define selected-population claim |
| verification bias | pathology/follow-up differs by uptake | verification-route analysis and bounded missing truth |
| incorporation bias | tracer result enters diagnosis, eligibility or response reference | independent components/adjudication or explicit incorporation |
| guarantee/immortal time | cohort requires later cycle, dosimetry or response scan | align time zero; landmark/time-dependent analysis where appropriate |
| informative cycle continuation | responders/tolerant patients receive later cycles/imaging | cycle-specific risk sets and intercurrent-event strategy |
| treatment confounding | prior/co-therapy changes uptake and outcome | treatment timeline and valid comparator/adjustment |
| target-expression drift | diagnostic and therapeutic states separated by therapy/time | paired timing and discordance/sensitivity analysis |
| calibration/protocol drift | apparent uptake/dose/response follows technical change | measurement passport, bridges and temporal validation |
| lesion multiplicity | lesion count inflates sample and significance | hierarchical inference and patient-level aggregation |
| organ/lesion mapping error | regions change across time/modalities | registered correspondence with uncertainty |
| postbaseline leakage | dose/response information enters baseline selection model | availability audit at the intended decision point |
| access/referral bias | specialised centres receive selected, travel-capable patients | source-pathway description and external/resource validation |

## 12. Validation and subgroup ladder

1. Verify product/tracer identity, timestamps, activity units, patient/course/cycle and lesion/organ
   linkage before splitting data.
2. Establish PET/SPECT analytical validity, calibration, repeatability and quantitative uncertainty
   through the acquisition-QC owner.
3. Use patient-level locked internal validation with nested lesions/organs/cycles.
4. Run temporal validation across product batch, scanner/software, reconstruction, eligibility,
   treatment and response-protocol changes.
5. Run external validation across site, vendor, radiopharmacy, referral and therapy capability.
6. Prespecify clinically material groups: disease subtype/stage, tumour burden and heterogeneity,
   target-expression pattern, prior/co-treatment, renal/hepatic or marrow function when supplied,
   age/sex where relevant, body size, lesion size/site, tracer/product, cycle, image quality and
   nonevaluable/discordant status.
7. Validate theranostic pairing directly with paired biodistribution/dosimetry/outcomes; shared target
   or visual similarity is insufficient.
8. For selection or dose-guided strategies, progress to a prospective comparison capable of testing
   the strategy, not merely the biomarker association.

No single phantom, SUV agreement study, internal dose-response curve or tracer-positive cohort proves
clinical benefit, generalisability or individualised-treatment utility.

## 13. Failure and uncertainty contract

Prespecify and report:

- wrong/unknown radiopharmaceutical or activity record, residual/extravasation, timing error and
  clock mismatch;
- motion, attenuation-map/hybrid misregistration, truncation/metal, low counts, detector/collimator
  mismatch and calibration/QC failure;
- missing dynamic/dosimetry time point, nonquantifiable organ/lesion, segmentation/registration
  failure and software/version failure;
- discordant diagnostic/therapeutic pair, heterogeneous or absent target uptake and nonevaluable
  eligibility/response;
- delayed/unavailable radiopharmaceutical, scanner, therapy, qualified staff or follow-up;
- incomplete therapy, dose modification, competing treatment, toxicity, early death and loss before
  response imaging;
- false eligibility/exclusion, missed target-negative disease, unnecessary treatment/escalation and
  inequitable access/travel burden.

Return uncertainty in the reported quantity and a defined fallback/adjudication route. Do not remove
failed or discordant cases and then claim performance for the full theranostic pathway.

Return `STOP_FOR_REPAIR` when radiopharmaceutical/activity/time identity is not recoverable,
calibration or quantitative/dosimetry units are undefined, diagnostic and therapeutic targets are
treated as interchangeable without evidence, required cycles/time points are selectively missing
without an estimand policy, or technical failure is removed from the intended-pathway denominator.

## 14. Claim ceilings

| Evidence | Maximum default conclusion |
|---|---|
| retrospective uptake association | uptake/measurement was associated with the named target/outcome in the analysed cohort |
| pathology concordance | concordant with sampled target expression at the mapped site/time, not whole-body biology |
| quantitative PET/SPECT validation | measurement was valid/repeatable under the tested chain, not clinically useful by itself |
| patient-specific dose estimate | estimated absorbed dose using the named method and uncertainty, not delivered biological effect |
| dose-response association | dose estimate was associated with the named response/toxicity under that treatment pathway |
| imaging response association | criterion-defined imaging change was associated with the named clinical outcome |
| external tracer/pair validation | transported to the named disease, tracer, product, site and protocol |
| comparative prospective strategy study | changed the prespecified outcome under the tested selection/dose/response strategy |

Do not call uptake a direct target assay, diagnostic eligibility a therapeutic dose, absorbed dose a
measured biological response, response association a surrogate endpoint, or a one-arm treated cohort
a predictive treatment-selection biomarker.

## 15. Decision-bearing mentor questions

- What exact tracer and quantity supports which decision in the pathway?
- Are the diagnostic and therapeutic agents truly paired, or only aimed at a nominally shared target?
- Which referred or tracer-negative patients disappear before treatment and outcome analysis?
- Does tissue/reference evidence map to the same lesion, time and treatment state?
- Which part of the dosimetry chain is measured, modelled or assumed, and where is uncertainty lost?
- Could technical drift, target-expression change or treatment timing mimic response?
- What is the fallback when tracer, scanner, post-therapy imaging, dosimetry or therapy is unavailable?

## 16. Authoritative and original source entry points

`last checked` records availability only. Retrieve the exact guideline/profile/publication, version,
locator and artifact digest before applying any tracer, therapy, dose or response rule.

| Research use | Authority/original source | URL | Last checked | State |
|---|---|---|---|---|
| nuclear-medicine guideline and tracer/application version discovery | European Association of Nuclear Medicine, guidelines overview | https://eanm.org/publications/guidelines/overview/ | 2026-08-23 | official index available; exact guideline/version is `LIVE_VERIFICATION_REQUIRED` |
| current dosimetry-method source discovery | EANM Dosimetry guideline index | https://eanm.org/publications/guidelines/overview/dosimetry/ | 2026-08-23 | official index available; tracer/method/version is `LIVE_VERIFICATION_REQUIRED` |
| radiopharmaceutical-therapy dosimetry framework | International Atomic Energy Agency, *Dosimetry for Radiopharmaceutical Therapy* (2024) | https://doi.org/10.61092/iaea.xlzb-6h67 | 2026-08-23 | official monograph/DOI available; not a local prescription or authorisation |
| MIRD schema, pamphlet and software provenance discovery | SNMMI Committee on Medical Internal Radiation Dose | https://snmmi.org/Web/About/About-SNMMI/Committees/Committee-on-Medical-Internal-Radiation-Dose/Default.aspx | 2026-08-23 | official committee index available; exact pamphlet/software/version must be frozen |
| tracer-specific theranostic guideline example | joint EANM/SNMMI 177Lu-PSMA radioligand-therapy guideline | https://doi.org/10.1007/s00259-023-06255-8 | 2026-08-23 | primary guideline available; disease/agent/jurisdiction scope is `LIVE_VERIFICATION_REQUIRED` |
| patient-specific 177Lu ligand dosimetry example | EANM Dosimetry Committee recommendations | https://doi.org/10.1007/s00259-022-05727-7 | 2026-08-23 | primary recommendations available; do not extrapolate across radionuclides/agents |
| quantitative FDG-PET response measurement profile | RSNA QIBA FDG-PET/CT Profile v1.14 (2023) | https://doi.org/10.1148/QIBA/20230615 | 2026-08-23 | official profile available; conformance and current status are `LIVE_VERIFICATION_REQUIRED` |
| FDG-PET response-framework origin | PERCIST 1.0 primary publication | https://doi.org/10.2967/jnumed.108.057307 | 2026-08-23 | primary source available; tracer/disease/protocol scope must be verified |
| PSMA-PET response-framework example | RECIP 1.0 international multicentre primary study | https://doi.org/10.2967/jnumed.121.263072 | 2026-08-23 | primary study available; do not generalise beyond validated population/tracer/therapy |
