# Musculoskeletal imaging research playbook

Use this reference to design or audit musculoskeletal (MSK) imaging research across trauma,
degeneration, inflammatory disease, infection, tumour, sports injury and postoperative imaging. It
is not a diagnostic or management guideline. Disease-, joint-, procedure- and modality-specific
rules remain `LIVE_VERIFICATION_REQUIRED` until verified for the jurisdiction and study period.

## 1. Separate the pathway and research job

Do not treat “MSK MRI” or “joint disease” as one population. Declare one primary pathway:

| Pathway | Research distinctions that must remain explicit |
|---|---|
| acute injury/trauma | injury mechanism, acuity, initial versus problem-solving imaging, immobilisation and surgery before verification |
| persistent pain/degeneration | symptom duration, prior conservative treatment, structural disease spectrum, load-bearing state and longitudinal horizon |
| inflammatory disease | diagnosis and activity state, treatment exposure, systemic multi-joint involvement and validated outcome instrument |
| infection | native versus postoperative/prosthetic setting, antibiotics, specimen source and microbiological uncertainty |
| tumour/lesion characterisation | incidental versus symptomatic/referral pathway, primary versus metastatic disease, biopsy/resection selection |
| preoperative planning | proposed procedure, required anatomical measurement, position/load and acceptable error for the decision |
| postoperative/implant surveillance | procedure, hardware/implant, elapsed time, expected healing/remodelling and complication target |
| treatment response/prognosis | baseline, intervention, longitudinal interval, symptom/function endpoint and competing surgery/reinjury |

Separate detection, classification, grading, segmentation, measurement, structural progression,
pain/function association, response, prognosis and workflow. Structural abnormality, symptoms,
functional limitation and treatment benefit are different constructs.

## 2. Time zero, laterality and structural hierarchy

Freeze time zero at the real decision point: injury, initial presentation, index examination,
treatment start, operation, postoperative milestone, flare, enrolment or outcome-instrument baseline.
State what was known and what intervention occurred before that point.

Use an explicit hierarchy such as:

`person -> episode -> body side -> region/joint -> bone/compartment -> structure -> lesion/subregion ->
examination -> sequence/view/reconstruction -> reader/measurement -> time point`.

- Record laterality at acquisition, annotation, reference standard and analysis. A side mismatch is a
  data-integrity failure, not random label noise.
- Bilateral joints, multiple lesions, bones, tendons, entheses or vertebral levels from one person
  are correlated. The number of structures is not the sample size for patient-level claims.
- A contralateral side is not an automatically healthy or independent control. Systemic disease,
  altered biomechanics, compensatory loading and shared exposure can affect both sides.
- For longitudinal studies, lock lesion/structure correspondence across time; do not silently match
  the most conspicuous lesion at each visit.
- Record dominant side, injury side, treated side and symptomatic side separately when relevant;
  do not infer one from another.

## 3. Minimum MSK research passport

| Field | Required lock |
|---|---|
| disease/pathway | clinical setting, acuity, prior treatment/procedure and referral mechanism |
| intended decision | detection, triage, grading, operative planning, monitoring, prognosis or explanation |
| population | consecutive denominator, age/skeletal maturity, activity/injury context, symptoms and exclusions |
| anatomical object | person, side, joint/region, structure, lesion/subregion and aggregation rule |
| index imaging | modality, position/load, protocol family, contrast, hardware state and acquisition date |
| comparator | reader, modality, clinical score, standard measurement, treatment or counterfactual |
| time zero/horizon | exact event, follow-up schedule and intercurrent surgery/treatment/reinjury policy |
| outcome/target | structural, diagnostic, symptom, function, return-to-activity, surgery or other named endpoint |
| reference standard | source, spatial match, verification timing, blinding, adjudication and uncertainty |
| unit model | patient and all nested sides/structures/visits/readers/sites |
| load/position | weight-bearing/non-weight-bearing, stress, joint angle, immobilisation and reproducibility |
| postoperative state | procedure, hardware/material, interval, expected change and complication target |
| failure state | nondiagnostic, artifact-limited, occult, multifocal, discordant and indeterminate cases |

## 4. Acquisition and measurement collaboration

The clinical-domain owner defines the pathway, anatomical object, decision, reference standard,
timing, outcome and claim ceiling. `radiology-acquisition-qc` owns modality-specific acquisition,
reconstruction, positioning/sequence validity, artifacts, quantitative transforms, protocol drift,
phantom/test-retest and measurement passports. Annotation and analysis modules own object
delineation and model execution; neither can repair an incoherent clinical hierarchy.

Preserve, as applicable:

- radiograph views, beam geometry, calibration object, positioning, rotation, flexion and whether the
  examination is weight-bearing or stress-loaded;
- CT/cone-beam CT acquisition, reconstruction, field of view, metal-artifact reduction and whether
  the position is loaded;
- MRI field strength, coil, planes, sequence families, spatial resolution, fat suppression,
  quantitative map derivation and metal-artifact-reduction method;
- ultrasound operator, transducer, dynamic manoeuvre, probe pressure, Doppler settings, side and
  target structure;
- nuclear medicine tracer, timing and hybrid-component role when used for MSK infection, tumour or
  prosthesis questions;
- interval hardware, surgery, injection, immobilisation, rehabilitation and activity/load before
  each examination.

Do not compare loaded and unloaded measurements, different joint angles, pre- and postoperative
anatomy, or metal-artifact-reduction outputs as though they were interchangeable acquisitions.

## 5. Weight-bearing, bilateral and dynamic designs

- State the biomechanical construct: alignment, joint space, instability, impingement, deformity,
  contact relation or another prespecified measure. “More realistic” is not an estimand.
- For loaded-versus-unloaded comparisons, keep examinations paired within person and as close in
  time as feasible; record load magnitude, stance, assistance, pain-limited positioning and order.
- A weight-bearing protocol may exclude people unable to stand or tolerate load. Describe that
  missing population and lower the transportability claim.
- For bilateral acquisition, specify whether both sides are target joints, one is a comparator, or
  one is incidental. Model within-person dependence and side-specific treatment/injury.
- For ultrasound or stress/dynamic imaging, prespecify manoeuvre, operator, force/angle where
  measurable, number of attempts, image-selection rule and failure to reproduce the manoeuvre.
- Do not choose the “best” frame, load state, side or reconstruction after outcome inspection.

## 6. Postoperative and implant studies

Create a surgical timeline:

`preoperative imaging -> operation/procedure -> immediate baseline -> rehabilitation/load change ->
index postoperative imaging -> revision/intervention -> outcome`.

Record procedure type and indication, operated side/level, implant/hardware identity and material,
operative findings, complications, interval, weight-bearing/rehabilitation status and any revision.

- Expected healing, edema, granulation, scar, marrow change, synovitis and remodelling vary with
  procedure and interval. A postoperative abnormality requires a time-qualified target definition.
- Hardware causes missing or distorted information, not merely lower visual quality. Evaluate
  artifact by target structure and distance from hardware.
- Surgical findings are a reference only for structures actually visualised and documented at that
  operation. They are not whole-joint or future postoperative truth.
- Revision-only cohorts are strongly selected. Do not generalise their pathology or implant-failure
  prevalence to all postoperative patients.
- If the algorithm uses operative notes, implant type or later follow-up that would be unavailable at
  the claimed imaging decision, mark leakage and lower the claim.

## 7. Reference standards and object matching

| Research target | Candidate reference | Required qualification |
|---|---|---|
| fracture/structural injury | surgery, cross-sectional imaging, expert adjudication, interval healing | target structure, side, occult lesions, treatment and verification interval |
| cartilage/meniscus/tendon/ligament | arthroscopy/surgery, expert consensus, longitudinal imaging | surface/segment correspondence, partial visualisation and interval change |
| bone/soft-tissue tumour | pathology, molecular testing, multidisciplinary diagnosis, follow-up | biopsy target, grade heterogeneity, neoadjuvant treatment and resection selection |
| infection | culture/histology, operative findings, laboratory/clinical composite, follow-up | antibiotics, specimen site/quality, culture-negative state and incorporation |
| inflammatory activity/damage | validated imaging score plus clinical/laboratory outcome | instrument version, reader calibration, construct validity and treatment timing |
| degeneration/progression | prespecified quantitative/semiquantitative imaging measure, surgery or patient outcome | load/position comparability, smallest detectable change and symptom-structure discordance |
| postoperative complication | surgery/aspiration, multidisciplinary adjudication, serial imaging and outcome | procedure/interval-specific definition and verification selection |

- Pathology or arthroscopy must map to the same side, structure and subregion. A specimen from one
  lesion cannot label all lesions or the entire joint.
- Reader consensus is a reference to expert interpretation, not proof of pathology or clinical
  importance.
- A scoring system defines an imaging construct. It does not automatically become disease truth,
  symptom severity, function or a surrogate endpoint.
- Preserve indeterminate, nonvisualised, technically limited and discordant states. Forced binary
  labels hide clinically meaningful failure.

## 8. Endpoints and tasks

| Task | Primary target | Essential companion outcomes |
|---|---|---|
| detection/classification | patient- and structure-level accuracy with uncertainty | lesion/structure spectrum, non-evaluable rate and clustering |
| segmentation/quantification | agreement/error for the declared object and unit | repeatability, smallest detectable change, failure and anatomical plausibility |
| grading/scoring | construct-valid score or category agreement | reader calibration, ordinal analysis, responsiveness and score version |
| structural progression | change over a prespecified interval | measurement error, load/protocol consistency, treatment/reinjury and attrition |
| symptom/function association | prespecified association/added value | confounders, temporal alignment and discordance analysis |
| treatment response | change under a defined intervention and baseline | comparator, adherence, co-intervention and patient-important outcome |
| operative planning/workflow | decision, measurement or reader/process outcome | action threshold, reader/surgeon interaction, failures and downstream consequence |

Patient-reported pain, function, quality of life, return to activity/work and reoperation may be more
decision-relevant than image change. Choose them prospectively when they match the intended claim;
do not retrofit an image biomarker as a surrogate after observing association.

## 9. Major bias and confounding map

| Threat | MSK manifestation | Required response |
|---|---|---|
| surgical/verification selection | only severe or operative cases receive reference | show verification pathway; include/bound nonoperative cases |
| spectrum bias | obvious tears/tumours versus healthy controls | recruit clinically confusable states from the intended pathway |
| laterality leakage | wrong-side labels or both sides split across train/test | side audit and patient-level splitting |
| contralateral-control bias | opposite side assumed normal and independent | assess symptoms/pathology and model paired dependence |
| structure multiplicity | many lesions/levels inflate effective sample | hierarchical analysis and patient-level aggregation |
| load/position confounding | cases and controls imaged under different stance/angle | standardise/record position; sensitivity or restricted estimand |
| postoperative confounding | procedure, interval and hardware drive image phenotype | stratify/model timeline; separate native from postoperative anatomy |
| treatment/confounding by indication | treatment changes both imaging and outcome | define strategy/comparator and time-varying treatment handling |
| symptom-structure discordance | structural severity presented as pain/function truth | measure both constructs and retain discordance |
| scanner/protocol drift | quantitative change follows sequence/reconstruction change | protocol ledger, repeatability bridge and temporal validation |
| attrition/competing intervention | surgery or loss to follow-up removes worsening cases | record intercurrent events; align estimand and missing-data plan |
| reader incorporation | index category guides biopsy/surgery/reference | blind adjudication where possible; document incorporation |

## 10. Validation and subgroup ladder

1. Verify side, structure, visit and procedure linkage and exclude cross-split patients/families.
2. Establish acquisition/position/load and annotation repeatability for the target object.
3. Use locked internal validation with patient-level resampling and hierarchical inference.
4. Run temporal/site/vendor validation with protocol and surgical-practice drift described.
5. Prespecify subgroups that can change morphology or measurement: age/skeletal maturity, sex where
   relevant, body size, activity/injury mechanism, joint/region, side, disease severity, inflammatory
   state, prior treatment, postoperative interval, implant/hardware, load tolerance and image quality.
6. Validate across clinically confusable conditions, not only normal controls.
7. For longitudinal biomarkers, demonstrate measurement error/repeatability before interpreting
   biological change, then relate change to an independent patient-important or biological endpoint.
8. For decision support, evaluate reader/orthopaedic/rheumatology workflow at the intended action
   point; retrospective accuracy alone does not establish planning or treatment utility.

Cross-joint or cross-anatomy pooling requires an explicit shared construct and separate validation;
more images from different structures do not substitute for adequate patients in each target use.

## 11. Failure and uncertainty contract

Prespecify and report:

- wrong side/region, incomplete coverage, motion, low signal, poor positioning or non-reproducible
  load/dynamic manoeuvre;
- metal, cast, brace, body-size or postoperative artifact that obscures the target;
- multifocal, bilateral, mixed chronic/acute, postoperative and anatomically variant cases;
- reference-standard discordance, nonvisualised structure, inadequate specimen and uncertain onset;
- segmentation/measurement failure, anatomically impossible output and large change within the
  repeatability bound;
- inability to bear weight, complete a dynamic task or return for follow-up.

Do not exclude these states and then claim applicability to the full clinical pathway. Report the
fallback, need for expert review and consequence of a wrong or uncertain output.

Return `STOP_FOR_REPAIR` when side/object/time identity is untraceable, related structures from one
patient cross partitions, incompatible load/position or postoperative states are treated as one
measurement, the reference cannot be mapped to the analysed structure, or surgical verification
selection is ignored for a pathway-level claim.

## 12. Claim ceilings

| Evidence | Maximum default conclusion |
|---|---|
| retrospective image-label association | associated with/discriminated the declared imaging or reference target in the analysed cohort |
| reader-consensus labels | reproduced expert image interpretation, not pathology or clinical utility |
| surgical/pathology-enriched validation | performed in the selected verified population, not all referred patients |
| repeatable quantitative measurement | measured reproducibly under the tested protocol/load; biological validity remains separate |
| external/temporal validation | transported to the named site/time/anatomy/protocol strata |
| longitudinal association | imaging change was associated with the named outcome under the observed pathway |
| prospective reader/workflow study | changed the prespecified reader/process endpoint in that study |

Do not upgrade an image score to pain relief, functional improvement, treatment benefit or surrogate
endpoint without corresponding evidence. Do not generalise adult Bone-RADS, one joint, one load
state or one postoperative procedure to different populations by analogy.

## 13. Decision-bearing mentor questions

- What is the true object: patient, side, joint, structure, lesion or subregion?
- Are both sides or multiple structures present, and how is dependence handled?
- Was the image acquired under the position/load that gives the measurement clinical meaning?
- What operation, hardware, treatment or activity occurred before the image and reference?
- Does the reference map to the same structure and time, or only to a selected specimen?
- Which patients cannot tolerate the protocol or never receive definitive verification?
- Is the desired conclusion about structure, symptoms, function, treatment response or workflow?

## 14. Authoritative and original source entry points

`last checked` records source availability only. Standards, scoring instruments and reporting
systems require a versioned live-standard receipt before use.

| Research use | Authority/original source | URL | Last checked | State |
|---|---|---|---|---|
| modality/anatomy-specific acquisition and interpretation parameter discovery | ACR Practice Parameters and Technical Standards | https://www.acr.org/Clinical-Resources/Clinical-Tools-and-Reference/Practice-Parameters-and-Technical-Standards | 2026-08-23 | official index available; exact parameter/version is `LIVE_VERIFICATION_REQUIRED` |
| MSK consensus terminology and incidental-lesion framework discovery | Society of Skeletal Radiology, consensus papers | https://skeletalrad.org/ssr-consensus-papers/ | 2026-08-23 | official society index available; population and version are `LIVE_VERIFICATION_REQUIRED` |
| adult incidental solitary bone-lesion framework example | SSR Bone-RADS primary consensus publication | https://doi.org/10.1007/s00256-022-04022-8 | 2026-08-23 | primary paper available; adult/solitary/incidental scope must not be expanded |
| outcome-domain and measurement-instrument development | OMERACT Handbook and MRI in Arthritis Working Group | https://omeract.org/handbook/ ; https://omeract.org/working-groups/mri/ | 2026-08-23 | official methodology and working-group pages available; exact instrument/version is `LIVE_VERIFICATION_REQUIRED` |
| longitudinal knee imaging cohort/protocol exemplar | NIH Osteoarthritis Initiative | https://www.nia.nih.gov/research/resource/osteoarthritis-initiative-oai | 2026-08-23 | official cohort resource; dataset release/protocol/visit must be frozen per analysis |
| weight-bearing CT acquisition/measurement limitations | primary methodological review, *Skeletal Radiology* | https://doi.org/10.1007/s00256-022-04223-1 | 2026-08-23 | original methodological source available; not a universal protocol or care rule |
