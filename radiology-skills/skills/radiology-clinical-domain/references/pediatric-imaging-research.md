# Pediatric imaging research playbook

Use this reference to design or audit imaging research involving fetuses, neonates, infants,
children, adolescents or young adults when development, body size, dose, cooperation, sedation,
rare disease or transition to adult care changes the estimand. It is a research-design playbook, not
a pediatric imaging, sedation or treatment guideline. Local clinical, ethics and safety decisions
belong to qualified teams and remain `LIVE_VERIFICATION_REQUIRED` when version-sensitive.

## 1. Define the pediatric pathway and developmental state

Do not use “pediatric” as a single subgroup. Name the pathway and the developmental construct that
matters to the question.

| Pathway | Required research distinction |
|---|---|
| prenatal/perinatal | fetal versus maternal unit, gestational age source, delivery timing and prenatal-to-postnatal correspondence |
| neonatal intensive care | gestational and corrected age, prematurity, critical illness, bedside versus transported imaging and survival/transfer |
| acute/emergency | injury/illness pathway, caregiver-provided history, cooperation, dose/sedation and time-to-action |
| congenital/developmental | developmental stage, changing normal anatomy, syndrome definition and repeated longitudinal assessment |
| chronic disease/surveillance | treatment, growth, cumulative visits, transition of care and age-dependent outcome definitions |
| oncology/rare disease | disease subtype, natural-history stage, referral centre, therapy, family structure and multicentre ascertainment |
| screening or population cohort | age-specific prevalence, eligibility, school/community versus tertiary pathway and follow-up completeness |
| transition to adult care | pediatric/adult protocol boundary, site/service change, phenotype evolution and recalibration need |

Record chronological age at each index examination. Add gestational age, corrected age, pubertal or
skeletal maturity, developmental stage, height, weight or body-size measure only when scientifically
relevant and actually available; do not infer them from appearance. A newborn, toddler and
adolescent cannot be made exchangeable by adding age as one linear covariate.

## 2. Time zero and cross-age estimand

Choose a time zero aligned with the decision: birth, corrected-age milestone, symptom onset,
referral, index image, treatment start, procedure, disease diagnosis, surveillance visit or planned
developmental assessment.

- Use age-at-event and calendar time separately. Longitudinal change may reflect maturation,
  disease, treatment, scanner/protocol change or their interaction.
- Define the target population over an age/development interval. “All children” is not an estimand
  unless the design represents and models the material stages.
- For growth/development questions, specify whether the estimand is status at age, within-child
  change, deviation from a reference trajectory, time to milestone, or association with a later
  outcome.
- For treatment or surveillance, align baseline with treatment and distinguish maturation from
  treatment response.
- For cross-age transport, prespecify whether the goal is interpolation within represented ages,
  transport to an unseen developmental stage, transfer from adults to children, or transition from
  pediatric to adult services. These require different evidence.

## 3. Minimum pediatric research passport

| Field | Required lock |
|---|---|
| condition/pathway | disease/syndrome, acute/chronic state, referral setting and care service |
| age/development target | chronological range plus relevant gestational/corrected age, maturity or developmental construct |
| intended decision | detection, diagnosis, severity, growth, response, prognosis, procedure planning or workflow |
| population/denominator | recruitment source, tertiary/referral enrichment, family structure, prior treatment and exclusions |
| index imaging | modality, protocol family, body region, indication, acquisition date and cooperation/sedation state |
| body-size/dose context | weight/height or task-appropriate size metric, protocol stratum, recorded dose quantities and repeat exposure scope |
| time zero/horizon | exact event, developmental timescale and intercurrent treatment/transition policy |
| outcome/target | age-appropriate definition, adjudication, horizon and patient/caregiver-relevant meaning |
| reference standard | source, age validity, spatial/temporal match, verification and uncertainty |
| unit hierarchy | child, pregnancy/family/sibling, visit, exam, organ/lesion, reader, site and time point |
| rare-disease state | subtype/genotype where supplied, natural-history stage, family/site clusters and registry ascertainment |
| failure state | incomplete/nondiagnostic exam, motion, sedation failure/adverse event, dose missingness and uncertain diagnosis |

Human-subjects, assent/consent/permission, privacy, family linkage, secondary use and return-of-result
questions route to `radiology-ethics: human-subjects`. Mark them `AUTHOR_INPUT_NEEDED` until the
responsible authority confirms them.

## 4. Unit hierarchy, family structure and repeated development

Use an explicit hierarchy:

`pregnancy/family -> child -> episode/visit -> examination -> organ/side/lesion -> sequence/view ->
reader/measurement -> developmental time point`.

- Multiple images, organs, lesions, slices or follow-up visits are not independent children.
- Twins, siblings and related participants may share genetics, environment, referral and scanner
  pathways. Split and analyse at the family level when leakage or dependence is plausible.
- In prenatal-to-postnatal studies, define whether the unit is fetus, pregnancy, liveborn child or
  paired fetal-child trajectory and account for pregnancy loss and non-livebirth outcomes without
  survivorship erasure.
- Children who age into a new protocol, service or scanner stratum create a time-varying exposure;
  do not attribute the resulting image change solely to development.
- Repeated surveillance intensity can be informative: sicker children may be imaged more often,
  sedated differently and verified more completely.

## 5. Acquisition, body size and dose collaboration

The clinical-domain owner freezes the pediatric pathway, developmental target, decision, reference,
outcome and claim ceiling. `radiology-acquisition-qc` owns modality-specific acquisition,
reconstruction, dose/quantitative-image validity, artifacts, protocol strata, phantom/test-retest
and protocol drift. Do not duplicate or override that technical owner.

For ionising imaging, preserve the actual recorded quantities and their semantics, such as scanner
output/dose indicators, administered activity, fluoroscopy metrics or radiography exposure data.
Do not convert an unavailable metric into a guessed effective dose, and do not call a scanner output
quantity an individual biological risk.

At minimum record:

- age, task-relevant size/body-region measure, indication and protocol stratum;
- equipment/model/software, acquisition/reconstruction, field of view, phases/views, repeat series
  and image-quality outcome;
- dose/exposure metadata source, missingness and whether values are measured, reported or estimated;
- motion, immobilisation, caregiver presence, feed-and-wrap/behavioural technique if used, sedation/
  anaesthesia state and failed or abbreviated examinations;
- body-size, age or indication changes that trigger different modality/protocol choices;
- cumulative research exposure scope without implying that heterogeneous dose quantities can simply
  be added.

Optimisation is a joint image-quality and exposure question. A lower recorded dose is not a success
if the target becomes non-evaluable or repeat imaging increases; higher image quality is not a
licence to ignore exposure.

## 6. Sedation, anaesthesia, cooperation and transport

Sedation or anaesthesia is part of the pathway and selection mechanism, not a disposable nuisance
variable. Create a timeline:

`referral -> preparation/fasting decision -> attempted nonsedated acquisition -> sedation or
anaesthesia decision -> administration -> acquisition -> recovery -> diagnostic result -> follow-up`.

- Record intended and achieved sedation depth only from governed source data; responsible personnel,
  monitoring and adverse events remain local clinical/ethics facts.
- Distinguish no sedation, behavioural/immobilisation support, failed nonsedated attempt, sedation,
  general anaesthesia and unknown. Do not collapse unknown into no sedation.
- Sedation can affect physiology, motion, timing, recruitment, cost and access. It can also select
  younger, developmentally different or sicker children.
- Report cancellations, incomplete exams, repeat acquisition, recovery delay and adverse-event
  ascertainment. A study of completed sedated scans excludes the failure pathway.
- For transport from NICU/ICU or low-resource sites, measure transport eligibility, instability,
  escort/equipment needs and patients not transported. Bedside and fixed-scanner cohorts may differ
  clinically and technically.
- Never turn this playbook or a publication into patient-specific sedation advice.

## 7. Reference standards and developmental truth

| Target | Candidate reference | Pediatric qualification |
|---|---|---|
| congenital/developmental anatomy | expert consensus, surgery/pathology, genetic testing, longitudinal phenotype | age-dependent normal variation, incomplete penetrance and changing phenotype |
| acute diagnosis | surgery/pathology, laboratory/physiologic evidence, serial imaging or adjudicated composite | selective verification, treatment before reference and caregiver/history uncertainty |
| tumour/rare disease | pathology/genotype, specialist consensus, registry/natural history and follow-up | small samples, subtype heterogeneity, sampled tissue and referral enrichment |
| growth/maturation | validated age-/sex-/population-specific reference or longitudinal measurement | reference population, version, measurement error and transport across ancestry/setting |
| treatment response | disease-specific criteria, biological/clinical outcome or adjudication | developmental change, treatment timing, confirmatory interval and competing progression/death |
| functional/developmental outcome | age-appropriate validated instrument, clinician assessment or caregiver/patient report | instrument version/language, floor/ceiling effects and respondent |

- An adult reference range, adult-trained model or adult disease definition is not automatically
  valid in children.
- Pathology may be unavailable or ethically inappropriate for many pediatric conditions. A composite
  or longitudinal reference must expose its components, uncertainty and index-test incorporation.
- Developmental norms are population- and method-dependent. Verify the reference, age/maturity
  coverage and measurement protocol; do not label deviation as disease by default.
- Preserve indeterminate, evolving and not-yet-verifiable diagnoses. Later diagnosis can be a valid
  reference only with a declared horizon and leakage-safe time zero.

## 8. Rare disease and small-population design

- Define the exact disease/subtype and natural-history stage; do not merge rare disorders because
  they share an organ or imaging appearance without a shared construct.
- Prefer multicentre/registry or natural-history collaboration when feasible, but preserve site,
  referral, genotype, family, treatment and protocol differences.
- Deduplicate participants across registries, publications, family cohorts and repeated releases.
  A rare-disease “external” set may contain the same child or family.
- Split at child and family level; when a site uniquely represents a subtype, report that subtype-site
  confounding rather than claiming site-independent validation.
- Use uncertainty and shrinkage appropriate to small samples. Do not manufacture balance with
  synthetic images and then describe the target population as represented.
- Report case ascertainment, diagnostic delay, survival to referral, unavailable imaging and who
  could not travel to a specialty centre.
- A leave-one-site/family/subtype analysis can probe fragility but does not by itself prove broad
  transportability. Preserve descriptive natural-history value when prediction is not supportable.

## 9. Endpoints and tasks

| Task | Primary target | Pediatric companion evidence |
|---|---|---|
| detection/diagnosis | age/pathway-specific accuracy and calibrated probability | developmental spectrum, non-evaluable exams, verification and body-size/protocol strata |
| segmentation/measurement | error/agreement for age-appropriate anatomy | size dependence, repeatability, anatomical plausibility and failure |
| developmental trajectory | within-child change or deviation from a verified reference trajectory | measurement error, treatment, maturation and attrition |
| dose/image-quality optimisation | task-based image quality at recorded exposure strata | repeat/failure rate, body size, indication and downstream adequacy |
| treatment response/prognosis | prespecified outcome/horizon under the observed care pathway | growth, treatment timing, competing events and age-appropriate outcome |
| workflow/access | completion, sedation/transport burden, time, equity or resource endpoint | children not referred/completed, caregiver burden and site capability |
| AI/decision support | clinical task performance at the intended age/workflow | age-stage transport, failures, human factors and prospective evaluation |

Patient- and caregiver-relevant outcomes may include comfort/distress, completion without repeat,
time away from school/work, travel, sedation/transport burden and downstream testing. Collect them
only with an appropriate protocol; do not infer them from image quality.

## 10. Major bias and leakage map

| Threat | Pediatric manifestation | Required response |
|---|---|---|
| age/development confounding | disease groups occupy different developmental stages | design overlap/stratification; model nonlinearity; report unsupported ages |
| body-size/protocol confounding | size-driven dose/reconstruction mimics disease signal | protocol/size ledger and technical validation |
| sedation selection | completed sedated scans exclude failed or nonsedated pathways | retain intended/attempted/completed states and selection model |
| tertiary-referral spectrum | severe/rare/treated cases dominate specialty centres | describe source denominator and external pathway validation |
| survivor/transport bias | unstable or deceased children never reach scanner/follow-up | include competing outcomes and non-transported denominator |
| family leakage | siblings/twins appear across splits | family-level split and clustered inference |
| rare-disease site confounding | site identifies subtype, genotype or protocol | stratified/leave-site analyses and bounded claim |
| adult-to-child leakage | adult norms, labels or pretrained output used as pediatric truth | pediatric reference and stage-specific validation |
| longitudinal leakage | later diagnosis, treatment or future images enter earlier prediction | availability audit at time zero |
| changing normal anatomy | maturation labelled progression or error | developmental reference and within-child design |
| dose missingness | dose metadata absent non-randomly by device/site/era | report source/missingness; do not impute uncritically |
| informative follow-up | sicker children receive more surveillance and verification | model visit process; prespecify horizon and attrition handling |

## 11. Cross-age and multisite validation ladder

1. Verify child/family identity, age units, gestational/corrected-age semantics, side/organ and visit
   linkage before splitting data.
2. Establish task-based acquisition, size/dose metadata and annotation/measurement validity.
3. Use patient- and family-level locked internal validation with age-stage performance and failure.
4. Perform temporal validation across growth, protocol, scanner/software and care-era changes.
5. Perform external validation in a site with different referral intensity, pediatric expertise,
   equipment and sedation/transport pathway.
6. Prespecify material groups: neonatal/prematurity state, developmental stage, body size, sex where
   relevant, disease subtype/severity, disability/cooperation, sedation, site/resource level,
   inpatient/outpatient/emergency pathway, image quality and device/protocol.
7. Test cross-age transport explicitly: adult-to-pediatric, older-to-younger, stage-to-stage and
   pediatric-to-adult-service transitions. Label wholly unseen stages as unsupported until evaluated.
8. For deployed tools, progress through prospective silent and then live workflow evaluation with
   failure, override, burden and safety outcomes.

Do not claim equivalence from overlapping confidence intervals or nonsignificant subgroup tests.
Sparse strata require uncertainty and a lower claim ceiling.

## 12. Failure and uncertainty contract

Prespecify and report:

- motion, incomplete coverage, poor cooperation, failed preparation/sedation, aborted or repeated
  examination and unavailable pediatric protocol;
- non-diagnostic image, dose metadata failure, body-size outside the protocol/model range and
  anatomically implausible output;
- evolving/indeterminate diagnosis, absent pathology, rare subtype, developmental variant and
  discordant specialist opinions;
- transport ineligibility, missed visit, transition-of-care loss and family withdrawal;
- adult-trained or older-child model output outside supported ages;
- false reassurance, unnecessary escalation/repeat exposure, delayed diagnosis, sedation/transport
  burden and inequitable access.

State the fallback and accountable specialist. “No adverse event observed” is not a safety claim if
adverse events, repeats, distress or downstream exposure were not systematically measured.

Return `STOP_FOR_REPAIR` when age units or developmental state are irrecoverable, body-size/protocol
or sedation selection materially confounds the target without a defensible boundary, related
children cross partitions, adult evidence is used as pediatric truth without direct validation, or
unsupported ages are included in the claim.

## 13. Claim ceilings

| Evidence | Maximum default conclusion |
|---|---|
| retrospective selected pediatric images | associated with/discriminated the target in the represented ages and pathway |
| adult-trained model tested in one pediatric cohort | observed performance in that named cohort, not pediatric validation generally |
| age-stratified internal validation | internal performance across represented strata; unseen stages remain unsupported |
| temporal/site external validation | transported to the named age, protocol, referral and resource setting |
| dose/image-quality study | compared task-based adequacy and recorded exposure under tested protocols, not lifetime risk |
| longitudinal association | imaging trajectory was associated with the named developmental/clinical outcome |
| prospective workflow study | changed the measured completion/reader/process outcome in that pediatric workflow |

Do not upgrade imaging prediction to developmental prognosis, individual radiation risk, sedation
safety, treatment benefit or cross-age generalisability without direct evidence.

## 14. Decision-bearing mentor questions

- Which developmental stage and clinical decision define the target population?
- Could age, body size, protocol or sedation create the apparent disease signal?
- Which children, families or rare subtypes never reach the specialist scanner or reference standard?
- Are related children or repeated visits separated across development and validation sets?
- What happens when the child cannot complete the intended protocol?
- Is the reference valid for this age and measured at the same developmental time?
- Which age stages are wholly unseen, and what wording will keep them out of the claim?

## 15. Authoritative and original source entry points

`last checked` records availability only. Retrieve and version the governing document before using a
clinical, dose or sedation rule.

| Research use | Authority/original source | URL | Last checked | State |
|---|---|---|---|---|
| pediatric protocol/dose rationale and body-size framing | US Food and Drug Administration, Pediatric X-ray Imaging | https://www.fda.gov/radiation-emitting-products/medical-imaging/pediatric-x-ray-imaging | 2026-08-23 | official page available; device, jurisdiction and current guidance are `LIVE_VERIFICATION_REQUIRED` |
| pediatric radiological-protection principles | International Commission on Radiological Protection, Publication 121 | https://www.icrp.org/publication.asp?id=ICRP+Publication+121 | 2026-08-23 | official publication record available; use as protection framework, not individual risk estimate |
| pediatric CT optimisation resources | Alliance for Radiation Safety in Pediatric Imaging, Image Gently | https://imagegently.org/Procedures/Computed-Tomography | 2026-08-23 | official campaign resource available; exact protocol remains local and `LIVE_VERIFICATION_REQUIRED` |
| sedation pathway/safety-source discovery | AAP/AAPD pediatric sedation clinical report, doi:10.1542/peds.2019-1000 | https://doi.org/10.1542/peds.2019-1000 | 2026-08-23 | primary report page states reaffirmed with reference updates in 2025; local applicability remains `LIVE_VERIFICATION_REQUIRED` |
| rare-disease multicentre, registry and natural-history collaboration | NIH-funded Rare Diseases Clinical Research Network | https://www.rarediseasesnetwork.org/ | 2026-08-23 | official network entry available; exact consortium/protocol/data release must be frozen |
| pediatric AI development/implementation and cross-age safety concerns | ACR/ESPR/SPR/SLARP/AOSPR/SPIN multisociety statement | https://doi.org/10.1007/s00247-025-06386-0 | 2026-08-23 | primary multisociety publication available; use as research/implementation source, not a performance certificate |
| pediatric and modality-specific practice-parameter discovery | American College of Radiology, Practice Parameters and Technical Standards | https://www.acr.org/Clinical-Resources/Clinical-Tools-and-Reference/Practice-Parameters-and-Technical-Standards | 2026-08-23 | official index available; exact document/version is `LIVE_VERIFICATION_REQUIRED` |
