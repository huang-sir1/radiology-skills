# Starter clinical-domain playbooks

Read only the active domain section. These playbooks guide research framing and review; they do not
provide individual diagnosis or treatment. Every version-sensitive entry is
`LIVE_VERIFICATION_REQUIRED` at the time of use, even when an official source was verified on the
date recorded below.

## Source-entry convention

- `last checked` records link availability and page content checked on that date, not perpetual
  currency or applicability to a historical cohort.
- `official entry` is preferred for current version discovery; a primary consensus paper can anchor
  a stable scientific statement.
- Never copy a management recommendation into a study plan until population, jurisdiction, version
  and study period are confirmed by a responsible domain expert.

---

## 1. Thoracic and lung oncology

### Clinical question and PICO/estimand

- Route separately: screening nodule triage; symptomatic diagnostic work-up; histology/molecular
  prediction; clinical stage/extent; treatment response; recurrence; prognosis; or treatment-effect
  heterogeneity.
- Define whether the population is screening-detected, incidentally detected, symptomatic,
  biopsy-proven, resectable, advanced, post-treatment or under surveillance. Do not transport
  prevalence or thresholds silently across these pathways.
- Fix the index CT/PET-MRI date, lesion-versus-patient unit, target condition or event, horizon,
  competing risks, and intended role (triage, add-on, staging, monitoring or explanation).
- For a treatment-selection claim, specify the treatment comparator and biomarker-by-treatment
  interaction; one treated cohort supports at most prognosis under that care pathway.

### Imaging protocol and common artifacts

- Record low-dose screening versus diagnostic CT, contrast phase, slice thickness, reconstruction
  kernel/algorithm, field of view, breath hold, PET uptake interval and scanner/site changes.
- Check respiratory/cardiac motion, partial volume, beam hardening, truncation, metal, atelectasis,
  mucus, infection/inflammation, pleural effusion and adjacent-vessel or chest-wall interfaces.
- Segmentation and feature stability can change with subsolid components, cavitation, necrosis,
  multifocal disease and post-obstructive change. Preserve which lesion determines a patient label.

### Reference standard

- Distinguish resection pathology, core/fine-needle biopsy, nodal sampling, liquid/molecular testing,
  clinical-radiological follow-up and multidisciplinary adjudication.
- Record biopsy target and adequacy, stage source (clinical versus pathological), interval and
  treatment between image and verification, and whether hard-to-biopsy/indeterminate nodules were
  excluded.
- A reporting category or radiologist impression is not automatically histology or stage ground
  truth.

### Treatment and time-line confounding

- Map surgery, radiotherapy, systemic therapy, immunotherapy, targeted therapy, biopsy and infection
  relative to every image and tissue sample. Do not hard-code a treatment recommendation.
- Postoperative change, radiation injury, immune-related inflammatory change, tumour cavitation and
  variable follow-up can mimic response or progression. Calendar-era treatment changes can confound
  apparent model transportability.

### Mechanism hypotheses

- Candidate measured explanations may include cellularity, necrosis, fibrosis/desmoplasia,
  perfusion, hypoxia, stromal composition and immune-cell state.
- Competing biological explanations include inflammation, infection, collapse/atelectasis and
  treatment injury; technical alternatives include reconstruction, motion and segmentation.
- A radiomic texture or deep embedding does not identify any of these without object-matched
  evidence.

### Validation ladder

1. acquisition/segmentation robustness and locked-pipeline internal validation;
2. temporal/site validation with pathway and protocol shift described;
3. reader or workflow comparison at the intended decision point;
4. patient-lesion-image-tissue mapping with pathology/molecular concordance;
5. longitudinal or orthogonal assays that distinguish alternatives;
6. perturbation/target-engagement/rescue evidence for any bounded causal claim.

### Claim ceiling

- Screening data support screening-pathway claims only; pathology-enriched case-control data do not
  establish population screening utility.
- Molecular association in sampled tumours supports a measured cohort link, not non-invasive
  replacement, whole-tumour biology or treatment benefit.
- Response prediction without a valid comparator remains prognostic.

### Writing points and review red flags

- Methods must state clinical pathway, index date, lesion selection, TNM/reporting version used,
  acquisition/reconstruction, label source and treatment window.
- Results must show patient and lesion flow, unverified/indeterminate cases, stage/treatment mix,
  site/time performance and uncertainty.
- Discussion must separate diagnostic, prognostic and predictive meaning and explain protocol,
  verification and treatment-era transportability.
- Red flags: screening and symptomatic cohorts merged; future stage/treatment leaks; biopsy-only
  labels treated as whole-tumour truth; multiple nodules counted as independent patients; post-
  treatment images interpreted as untreated biology.

### Learner prompts

- At what point in the lung-cancer pathway would the model be available, and what action could it
  change?
- Which indeterminate or unverified nodules disappeared from the dataset?
- Could reconstruction, inflammation or treatment timing explain the same phenotype?
- What paired tissue or temporal evidence would disprove the preferred mechanism?

### Current-standard entry points

| Use | Authority/source | Official or primary URL | Last checked | State |
|---|---|---|---|---|
| screening CT categories/version discovery | American College of Radiology, Lung-RADS | https://www.acr.org/clinical-resources/clinical-tools-and-reference/reporting-and-data-systems/lung-rads | 2026-08-22 | official page available; `LIVE_VERIFICATION_REQUIRED` at use |
| thoracic tumour staging/version discovery | International Association for the Study of Lung Cancer, Staging Project | https://www.iaslc.org/science-research/scientific-projects/iaslc-staging-project-lung-cancer-thymic-tumors-and | 2026-08-22 | official page identifies ninth-edition resources; `LIVE_VERIFICATION_REQUIRED` at use |

---

## 2. Neuro-oncology

### Clinical question and PICO/estimand

- Separate preoperative diagnosis/grade or molecular association, segmentation/extent, surgical
  planning, early postoperative residual, treatment response, progression versus treatment effect,
  recurrence, prognosis and treatment-effect questions.
- State adult versus paediatric, primary versus metastatic, newly diagnosed versus recurrent,
  enhancing versus non-enhancing disease, surgery/radiotherapy status and corticosteroid context.
- Fix the baseline definition, index MRI, response-assessment window, patient/lesion unit, event
  definition, confirmation rule and horizon.

### Imaging protocol and common artifacts

- Record field strength, coil, pre/post-contrast T1, T2/FLAIR, DWI/ADC, susceptibility, perfusion,
  spectroscopy/PET if used, contrast dose/timing, geometric registration and slice/voxel geometry.
- Check motion, susceptibility, distortion, hemorrhage, postoperative blood/products, resection
  cavity, steroid effect, anti-angiogenic pseudo-response, pseudoprogression, radiation injury and
  scanner/protocol drift.
- Spatial mapping must distinguish enhancing core, non-enhancing abnormality, edema, necrosis,
  resection margin and sampled coordinates.

### Reference standard

- Record integrated pathological/molecular diagnosis version, resection versus stereotactic biopsy,
  sampled region, tissue quality, tumour purity and interval from MRI to tissue.
- For progression/response, state the exact criteria/version, baseline, confirmatory imaging,
  clinical status and adjudication. Pathology at reoperation can also be heterogeneous and mixed
  with treatment effect.

### Treatment and time-line confounding

- Map surgery, radiation, systemic/anti-angiogenic/immunotherapy, steroids and seizure-related or
  other acute changes relative to imaging, tissue and outcome.
- Baseline choice and early post-treatment windows can change the response label. Treatment is not
  a nuisance variable when it causes the imaging appearance under study.

### Mechanism hypotheses

- Candidate explanations include cellularity, blood-brain barrier disruption, angiogenesis,
  necrosis, edema, infiltration and immune/stromal state.
- Alternatives include seizure/inflammation, ischemia, hemorrhage, steroid effect, treatment injury,
  motion and registration/segmentation error.
- A regional image-tissue claim requires coordinate-aware sampling; one block cannot represent an
  entire heterogeneous tumour by assertion.

### Validation ladder

1. sequence/protocol harmonisation, registration and segmentation robustness;
2. locked temporal/site validation with baseline and criteria held explicit;
3. longitudinal confirmation and progression-versus-treatment-effect adjudication;
4. image-guided multi-region tissue mapping with molecular/pathology concordance;
5. orthogonal cellular/spatial evidence and within-patient discordance analysis;
6. perturbation evidence in an appropriate model for causal contribution.

### Claim ceiling

- Imaging-only discrimination cannot establish molecular state or infiltrative mechanism.
- Resection-selected, tissue-rich cohorts may not transport to biopsy-only or non-surgical patients.
- Response association under one regimen is not a treatment-selection biomarker.

### Writing points and review red flags

- Report baseline definition, criteria/version, steroid and treatment windows, all sequences,
  registration, enhancing/non-enhancing compartments and tissue coordinates.
- Show exclusions for non-measurable disease, missing sequences, early death or no confirmation and
  explain the estimand consequence.
- Red flags: postoperative and pretreatment scans mixed; progression criteria unnamed; pathology
  block assigned to whole tumour; cells/voxels treated as independent patients; pseudo-response or
  pseudoprogression ignored.

### Learner prompts

- Which MRI is time zero, and would every input be available then?
- Is the target treatment response, progression, or pathology, and how is ambiguity adjudicated?
- Which tumour compartment supplied the tissue and which generated the image feature?
- What observation would distinguish tumour biology from treatment injury?

### Current-standard entry points

| Use | Authority/source | Official or primary URL | Last checked | State |
|---|---|---|---|---|
| adult high-/low-grade glioma response research | RANO 2.0 primary consensus publication, Journal of Clinical Oncology | https://ascopubs.org/doi/10.1200/JCO.23.01059 | 2026-08-22 | primary article available; scope/version remain `LIVE_VERIFICATION_REQUIRED` at use |
| RANO family version discovery | Response Assessment in Neuro-Oncology group | https://rano.group/publications | 2026-08-22 | group publication portal available; disease-specific route remains `LIVE_VERIFICATION_REQUIRED` |

---

## 3. Liver and hepatobiliary imaging

### Clinical question and PICO/estimand

- Separate surveillance in an at-risk population, focal-lesion diagnosis, HCC versus non-HCC
  malignancy, staging/extent, treatment response, recurrence and prognosis.
- State liver-disease risk population, cirrhosis/etiology, prior HCC or treatment, transplant or
  surgical pathway, modality and whether the question falls inside the declared reporting system's
  target population.
- Fix observation-versus-patient unit, index phase/examination, target condition, reference window,
  competing events such as transplantation/death, and horizon.

### Imaging protocol and common artifacts

- Record CT/MRI/US/CEUS route, contrast agent, injection and bolus timing, arterial/portal/delayed or
  hepatobiliary phases, sequence parameters, breath hold, fat/iron assessment and reconstruction.
- Check arterial mistiming, transient motion, subtraction misregistration, fat/iron effects,
  perfusion alteration, arterioportal shunt, confluent fibrosis, regenerative/dysplastic nodules,
  biliary obstruction and post-treatment change.
- A lesion visible in one phase may not have a reliable cross-phase or pathology match.

### Reference standard

- Distinguish explant/resection pathology, biopsy, accepted imaging criteria, interval growth,
  treatment response and multidisciplinary composite diagnosis.
- Record which observations receive pathology, biopsy target and adequacy, transplant/surgery
  selection, interval/treatment, and category changes over follow-up.
- Do not use a reporting category as histology or continuous tumour biology without justification.

### Treatment and time-line confounding

- Map ablation, embolic/locoregional therapy, radiation, systemic therapy, surgery and transplant
  relative to imaging and tissue. Do not supply patient management instructions.
- Perfusion changes, hemorrhage, necrosis and inflammatory rim after therapy can affect both image
  phenotype and response labels; use the response framework appropriate to treatment and study era.

### Mechanism hypotheses

- Candidate explanations include arterialisation, portal supply loss, extracellular space,
  cellularity, fat/iron, fibrosis, necrosis, hypoxia and immune/stromal organisation.
- Alternatives include benign perfusion phenomena, cirrhosis severity, etiology, inflammation,
  treatment effect, phase timing and motion/misregistration.

### Validation ladder

1. phase/sequence quality, lesion matching and segmentation robustness;
2. patient-level temporal/site validation within the intended risk population;
3. reference-standard and verification-bias analysis including indeterminate observations;
4. observation-to-block/region tissue mapping and orthogonal assays;
5. longitudinal category/biology change with treatment and timing modelled;
6. perturbation evidence for any causal biological explanation.

### Claim ceiling

- Results inside an at-risk HCC population do not automatically generalize to incidental lesions in
  a non-risk population or other hepatobiliary cancers.
- Imaging-category prediction is not equivalent to pathology prediction, clinical utility or
  treatment response.

### Writing points and review red flags

- State the eligible population, liver disease/etiology, reporting/version route, contrast agent and
  phases, observation selection, reference hierarchy and treatment window.
- Report observation and patient flow separately, indeterminate categories, verification route and
  transplant/surgical selection.
- Red flags: non-applicable populations pooled; phase timing absent; observations counted as
  independent patients; treated and untreated lesions mixed; explant-only truth generalized to all.

### Learner prompts

- Does the reporting system apply to every enrolled patient and every target lesion?
- Could arterial timing or cirrhosis etiology create the phenotype?
- Which observations never received definitive verification, and why?
- Can the available tissue be mapped to the exact observation and phase-derived feature?

### Current-standard entry points

| Use | Authority/source | Official or primary URL | Last checked | State |
|---|---|---|---|---|
| liver surveillance/diagnosis/treatment-response version discovery | American College of Radiology, LI-RADS | https://www.acr.org/Clinical-Resources/Clinical-Tools-and-Reference/Reporting-and-Data-Systems/LI-RADS | 2026-08-22 | official page lists route-specific releases; choose route/version with `LIVE_VERIFICATION_REQUIRED` |

---

## 4. Breast imaging

### Clinical question and PICO/estimand

- Separate population screening, diagnostic work-up, lesion characterization, extent, neoadjuvant
  response, recurrence and prognosis.
- State symptoms/risk, screening round, prior cancer/surgery, density, modality, lesion type and
  whether the intended use is recall/triage, add-on diagnosis, biopsy reduction, extent or monitoring.
- Fix patient/breast/lesion/examination unit, index date, target condition, reference window and
  interval-cancer horizon.

### Imaging protocol and common artifacts

- Record mammography/DBT views and dose, ultrasound acquisition/operator and lesion targeting,
  MRI field strength/sequences/contrast timing, or contrast-enhanced mammography protocol.
- Check positioning and tissue inclusion, compression, motion, overlapping tissue, implants,
  postsurgical change, biopsy clip/hematoma, background parenchymal enhancement, hormonal timing,
  fat suppression and registration.
- Preserve laterality, breast, lesion and biopsy-target mapping; contralateral or multifocal lesions
  are not interchangeable labels.

### Reference standard

- Distinguish core/vacuum biopsy, excision/surgery, image follow-up, interval cancer and expert
  adjudication. Record imaging-pathology concordance and upgrades at surgery.
- Verify which negative or probably benign findings receive follow-up and whether follow-up length is
  sufficient for the stated target.

### Treatment and time-line confounding

- Map biopsy, surgery, systemic/neoadjuvant therapy and radiation relative to all images and tissue.
  Treatment can change enhancement, cellularity and lesion conspicuity.
- Screening round, prior images, reader access and surveillance intensity can create label and
  workflow differences.

### Mechanism hypotheses

- Candidate explanations include cellularity, vascular permeability, desmoplasia, necrosis,
  calcification, stromal density and immune state.
- Alternatives include benign proliferative change, inflammation, hormonal/background enhancement,
  biopsy/surgical change, density, positioning and acquisition differences.

### Validation ladder

1. acquisition/reader/segmentation reproducibility by modality;
2. temporal/site validation with screening versus diagnostic pathway preserved;
3. pathology-concordance and interval-cancer/negative follow-up analysis;
4. lesion-to-tissue mapping with subtype and treatment timing;
5. prospective reader/workflow or biopsy-reduction evaluation;
6. controlled biological validation for mechanism claims.

### Claim ceiling

- A pathology-enriched diagnostic set does not establish screening recall reduction or safety.
- Subtype association in resected lesions does not imply non-invasive replacement or treatment
  selection in the unsampled population.

### Writing points and review red flags

- State screening versus diagnostic pathway, edition/version, modality/protocol, prior-image access,
  lesion mapping, pathology concordance and follow-up rule.
- Report density, symptoms/risk, lesion spectrum, interval cancers, verification routes and patient-
  level clustering.
- Red flags: breasts or lesions treated as independent patients; negative cases with inadequate
  follow-up; post-biopsy MRI used as pretreatment biology; pathology-enriched spectrum presented as
  screening performance; category labels treated as pathology.

### Learner prompts

- Is the intended decision recall, biopsy, extent assessment or treatment monitoring?
- Which negative cases have adequate follow-up for the target horizon?
- Could density, background enhancement or biopsy timing explain the result?
- Would the model still help when prior examinations and clinical history are available to readers?

### Current-standard entry points

| Use | Authority/source | Official or primary URL | Last checked | State |
|---|---|---|---|---|
| breast terminology/categories/audit version discovery | American College of Radiology, BI-RADS | https://www.acr.org/Clinical-Resources/Clinical-Tools-and-Reference/Reporting-and-Data-Systems/BI-RADS | 2026-08-22 | official page identifies BI-RADS v2025; exact modality/application remains `LIVE_VERIFICATION_REQUIRED` |

---

## 5. Prostate and pelvic imaging

### Clinical question and PICO/estimand

- Starter scope: prostate MRI detection/localization, clinically significant disease definition,
  local staging, active-surveillance change and post-treatment assessment. Other pelvic organs route
  to `local-extension-needed`.
- State biopsy-naive/prior-negative/active-surveillance/staging/recurrence pathway, PSA/clinical risk
  context, prior treatment and whether MRI guides biopsy.
- Define “clinically significant” from the actual reference and study period rather than assuming a
  universal threshold. Fix patient/lesion/sector unit, index MRI, biopsy/surgery interval and horizon.

### Imaging protocol and common artifacts

- Record field strength, coil, T2 planes, DWI b-values, ADC derivation, DCE timing, spatial
  resolution, antiperistaltic preparation if used and scanner/site.
- Check motion, rectal gas susceptibility/distortion, hemorrhage after biopsy, prostatitis, benign
  hyperplasia nodules, calcification, partial volume, hip hardware and post-treatment fibrosis.
- Preserve peripheral/transitional zone, sector, lesion and biopsy-core mapping.

### Reference standard

- Distinguish targeted and systematic biopsy, template mapping, prostatectomy whole mount,
  follow-up/repeat biopsy and composite adjudication.
- Record biopsy route, targeting method, core-to-lesion mapping, grade reclassification at surgery,
  time interval and MRI-informed verification.
- Prostatectomy truth is detailed but selected; biopsy truth is sampled and may miss or under-grade.

### Treatment and time-line confounding

- Map biopsy, androgen-directed/systemic therapy, radiation, focal therapy and surgery relative to
  imaging and tissue. Do not prescribe a treatment.
- Post-biopsy hemorrhage, treatment-related gland change and surveillance-triggered repeat testing
  can change phenotype and verification probability.

### Mechanism hypotheses

- Candidate explanations include glandular architecture loss, cellularity, diffusion restriction,
  perfusion, stromal composition, hypoxia and immune state.
- Alternatives include prostatitis, hyperplasia, hemorrhage, fibrosis, distortion, zone and scanner
  differences.

### Validation ladder

1. protocol/quality and reader/segmentation reproducibility;
2. temporal/site validation stratified by diagnostic pathway and zone;
3. targeted-plus-systematic or whole-mount concordance with verification-bias analysis;
4. lesion/sector-to-tissue molecular or pathology mapping;
5. longitudinal surveillance or treatment-response validation;
6. perturbational evidence for any bounded causal mechanism.

### Claim ceiling

- Prostatectomy cohorts do not represent all men undergoing MRI or biopsy.
- Lesion-level accuracy without patient-level aggregation and missed-lesion accounting does not
  establish patient-level biopsy triage.
- Imaging-pathology association does not establish treatment benefit.

### Writing points and review red flags

- State diagnostic pathway, standard/version, image-quality assessment, sequences/b-values,
  clinically significant definition, biopsy route, reader access and MRI-to-tissue interval.
- Report patient and lesion flow, zones, MRI-negative patients, biopsy/prostatectomy verification and
  clustering.
- Red flags: lesion cores as independent patients; prostatectomy-only verification generalized;
  post-biopsy hemorrhage ignored; target definition changes across cohorts; PI-RADS category used as
  pathology truth.

### Learner prompts

- Is the intended use biopsy avoidance, target selection, staging or surveillance?
- What is the reference definition of clinically significant disease, and is it stable across sites?
- Which MRI-negative patients received systematic verification?
- Could zone, inflammation, hemorrhage or distortion explain the signal?

### Current-standard entry points

| Use | Authority/source | Official or primary URL | Last checked | State |
|---|---|---|---|---|
| prostate MRI acquisition/interpretation version discovery | American College of Radiology with ESUR and AdMeTech, PI-RADS | https://www.acr.org/Clinical-Resources/Clinical-Tools-and-Reference/Reporting-and-Data-Systems/PI-RADS | 2026-08-22 | official page provides PI-RADS v2.1 resources; `LIVE_VERIFICATION_REQUIRED` at use |

---

## 6. Cardiovascular imaging

### Clinical question and PICO/estimand

- Starter scope: coronary CT angiography, stenosis/plaque characterization, optional CT-derived
  physiology, event prognosis and workflow. Structural, congenital, inflammatory and cardiomyopathy
  studies require a local extension.
- Separate stable versus acute symptoms, asymptomatic risk assessment, known versus suspected CAD,
  prior revascularization, per-patient disease category, lesion ischemia and future-event prognosis.
- Fix index examination, vessel/segment/lesion/patient unit, comparator (reader, invasive angiography,
  invasive physiology or outcome), horizon and intended role.

### Imaging protocol and common artifacts

- Record scanner, detector/reconstruction, prospective/retrospective gating, heart rate/rhythm,
  rate-control/vasodilator use if applicable, contrast timing, tube settings, slice thickness and
  calcium/plaque method.
- Check cardiac/respiratory motion, stair-step or misregistration, blooming from calcium/stent,
  beam hardening, poor opacification, small vessels, noise and segmentation/centerline error.
- A segment- or lesion-level result must be aggregated for a patient-level decision without treating
  correlated vessels as independent people.

### Reference standard

- Distinguish expert CCTA consensus, quantitative/invasive angiography, invasive functional
  measurement, downstream testing, adjudicated clinical events and composite labels.
- Record verification pathway and time, whether CCTA influenced invasive referral, lesion matching,
  blinding, indeterminate studies and revascularization before outcome ascertainment.

### Treatment and time-line confounding

- Map preventive/anti-anginal therapy, revascularization and other interventions after the index
  examination. Image-driven treatment can mediate observed outcomes.
- Event definitions, surveillance, competing death and treatment changes affect prognostic
  estimands. Do not turn a reporting-system management suggestion into a patient directive.

### Mechanism hypotheses

- Candidate explanations include plaque burden/composition, remodelling, stenosis, lesion physiology,
  inflammation and myocardial consequence.
- Alternatives include calcium blooming, motion/noise, vessel size, reconstruction, heart rate,
  treatment and comorbidity.
- CT-derived physiology or imaging biomarkers are estimates; do not call them invasive measurements
  or causal mechanisms.

### Validation ladder

1. scan quality, vessel/segment annotation and repeatability;
2. site/vendor/rhythm/calcium-stratified external validation;
3. lesion-matched anatomical or functional reference validation;
4. patient-level outcome validation with post-index treatment handled in the estimand;
5. prospective reader/workflow or clinical-utility evaluation;
6. orthogonal biological or perturbational evidence for a mechanism claim.

### Claim ceiling

- Agreement with expert CCTA labels supports automated classification, not invasive physiology or
  patient outcome benefit.
- Event association after image-driven treatment is not untreated natural history or treatment
  effect.
- Per-vessel performance does not establish patient-level triage without correct aggregation.

### Writing points and review red flags

- State clinical presentation, prior CAD/revascularization, acquisition and medication protocol,
  quality/exclusions, unit, reference standard, lesion matching and post-index treatment handling.
- Report indeterminate/nondiagnostic scans, calcium/rhythm strata, patient-level uncertainty and
  outcome adjudication.
- Red flags: segments treated as independent patients; invasive verification only in positive cases;
  post-index revascularization ignored; expert category called physiological truth; acute and stable
  pathways pooled without separate estimands.

### Learner prompts

- Is the decision anatomical classification, ischemia assessment, prognosis or workflow triage?
- Who underwent invasive verification, and was that decision influenced by CCTA?
- How will calcium, rhythm, stents and nondiagnostic scans affect transportability?
- Is post-index treatment a confounder, mediator or part of the intended strategy estimand?

### Current-standard entry points

| Use | Authority/source | Official or primary URL | Last checked | State |
|---|---|---|---|---|
| standardized coronary CT reporting/version anchor | SCCT/ACC/ACR/NASCI, CAD-RADS 2.0 primary consensus | https://www.jacc.org/doi/10.1016/j.jcmg.2022.07.002 | 2026-08-22 | primary consensus available; current version/applicability remain `LIVE_VERIFICATION_REQUIRED` at use |
