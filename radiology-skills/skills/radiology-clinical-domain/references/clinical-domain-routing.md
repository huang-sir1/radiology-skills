# Clinical domain routing contract

Use this reference for every request routed to the clinical-domain module. It determines which
playbook and output depth are needed; it does not replace the disease playbook.

## 1. First classify the clinical job

| Clinical job | Defining question | Frequent route error |
|---|---|---|
| screening | who in an asymptomatic at-risk population should undergo further work-up? | importing symptomatic prevalence or a diagnostic reference standard |
| detection/diagnosis | does the index examination identify a target condition in the intended work-up pathway? | case-control spectrum, partial verification, incorporation bias |
| differential/classification | which clinically confusable states can be separated? | easy controls, post hoc class definitions, category leakage |
| staging/extent | what anatomical or biological extent is present at the declared time? | mixing clinical and pathological stage or using future information |
| response | what change follows a defined intervention and baseline? | variable baseline, pseudo-response/progression, immortal time |
| recurrence/surveillance | who has recurrent disease, and by what horizon? | surveillance intensity and informative follow-up |
| prognosis | what future outcome occurs under the observed care pathway? | calling prognostic association a treatment-selection marker |
| treatment-effect heterogeneity | for whom does treatment effect differ versus a valid comparator? | one-arm outcome prediction without interaction estimand |
| workflow/utility | does use of the tool improve a clinical process or outcome? | equating discrimination with net benefit or implementation value |
| mechanism bridge | what measured biology could explain an imaging phenotype? | association or atlas lookup presented as patient-specific causality |

If one study contains several jobs, give each a separate estimand, analysis set and claim ID.

## 2. Domain selection

| Domain route | Supported scope | Escalate to `local-extension-needed` when |
|---|---|---|
| `thoracic-lung-oncology` | lung screening, thoracic tumour diagnosis/staging, response and recurrence | non-lung thoracic disease needs a different pathway or standard |
| `neuro-oncology` | adult brain-tumour MRI, tissue mapping and response | paediatric, spinal, metastatic or non-glioma criteria differ materially |
| `liver-hepatobiliary` | focal liver lesion/HCC-risk imaging, staging and treatment response | biliary, pancreatic or non-risk-population questions need dedicated rules |
| `breast` | screening/diagnostic imaging, lesion characterization and neoadjuvant response | hereditary, implant, pregnancy or uncommon treatment pathway changes estimand |
| `prostate-pelvic` | prostate MRI detection, localization, staging and surveillance | bladder, rectal, gynaecologic or other pelvic disease is the primary target |
| `cardiovascular` | coronary CT/plaque and ischemia-oriented imaging research | structural, congenital, inflammatory or cardiomyopathy questions dominate |
| `acute-emergency` | acute/ED, trauma, transfer, hyperacute neurologic and time-to-action imaging pathways | a condition-specific care rule or intervention window is needed beyond the verified pathway contract |
| `musculoskeletal` | trauma, degeneration, inflammation, infection, tumour, sports and postoperative/implant imaging | a joint-, disease-, procedure- or modality-specific rule is needed beyond the verified MSK construct |
| `pediatric` | developmental state, body size, dose, sedation, rare disease, family dependence and cross-age validation | a disease/organ pathway is primary; compose with that route rather than borrowing adult rules |
| `nuclear-medicine-theranostics` | tracer-defined PET/SPECT, dosimetry, response and diagnostic–therapy pair research | the agent, radionuclide, disease, dosimetry method or treatment pathway lacks a verified dedicated contract |
| `local-extension-needed` | another organ, disease, pathway or local practice not covered above | always build and verify a local extension before disease-specific conclusions |

The supported scope is a routing boundary, not an assertion that excluded questions are unimportant.
`liver-hepatobiliary` and `prostate-pelvic` are retained as stable route IDs, but they require a
mandatory subtype gate before any playbook content is used: the current starter content covers
focal liver/HCC-risk questions and prostate MRI respectively. Biliary/pancreatic disease and
non-prostate pelvic organs route to `local-extension-needed`; the broad ID never licenses borrowing
the starter standard.

`pediatric` is a cross-cutting developmental route and may be composed with one organ/pathway route;
do not average children into an adult protocol or split related siblings across partitions. For
`nuclear-medicine-theranostics`, this module owns the clinical pathway, tracer/therapy intent,
reference standard and endpoint; PET/SPECT acquisition, reconstruction, corrections, calibration,
quantitative validity and technical dosimetry receipts route to `radiology-acquisition-qc`.

## 3. PICO and estimand gate

Record each field explicitly:

| Field | Required decision |
|---|---|
| Population | entry pathway, symptoms/risk, disease state, prior treatment, site and exclusions |
| Index/exposure | examination, sequence/phase, feature/model, acquisition time and availability |
| Comparator | standard model, reader, modality, treatment or counterfactual appropriate to the claim |
| Outcome/target | event or target condition, definition, adjudicator, time horizon and competing event |
| Time zero | moment eligibility, predictors and treatment strategy are aligned |
| Estimand | population-level quantity, unit, contrast, horizon and intercurrent-event policy |
| Intended use | triage, replacement, add-on, rule-out, rule-in, staging, monitoring or explanation |
| Representativeness | clinically material subgroup coverage, missing pathway populations and denominator |
| Equity/access | availability of scanner/protocol/expertise/referral and who is excluded by access |
| Harm/consequence | false, indeterminate or failed-output consequences, workflow burden and affected stakeholders |

Do not accept “predict prognosis” or “differentiate benign and malignant” as a complete estimand.

## 4. Reference-standard gate

Describe:

- source: whole-specimen pathology, biopsy, clinical consensus, serial imaging, laboratory/functional
  measure, outcome registry, or composite;
- who received which verification and why;
- interval from index image to verification and intervening treatment;
- spatial correspondence among lesion, image region, biopsy, resection and molecular specimen;
- blinding and whether the index test entered the reference decision;
- indeterminate, discordant, missing and changed diagnoses;
- uncertainty or adjudication, rather than forced certainty.

A reference standard or outcome may legitimately be ascertained after the index image. Later
pathology or follow-up is not itself leakage: document the interval, intervening treatment, disease
evolution, verification selection and whether the label still represents the declared target.

Flag `STOP` for the affected inference when future reference/outcome information is used as an input
claimed available at the earlier decision point, the label incorporates the index test without
acknowledgment, or the reference cannot be mapped to the analysed object. A post-treatment label
cannot silently stand for pretreatment disease; either establish the target bridge or reframe the
estimand. Outcome-based retrospective sampling is a design/spectrum issue requiring the declared
sampling and claim boundary, not automatically predictor leakage.

[STARD 2015 explanation and elaboration](https://pmc.ncbi.nlm.nih.gov/articles/PMC5128957/)
(accessed 2026-09-04), item 22, requires reporting the interval and interventions between the index
test and reference standard; it does not require the reference result to exist at prediction time.

## 5. Treatment and time-line gate

Create a line with dates or relative windows for:

`eligibility -> index image -> tissue/assay -> intervention -> early response image -> confirmatory
image -> outcome ascertainment`.

Then identify:

- treatment before imaging or tissue that could alter the phenotype;
- treatment selection influenced by the image or model;
- variable scan frequency, delayed entry, immortal time and landmark choices;
- surgery, radiation, systemic therapy, steroids or other disease-specific modifiers;
- protocol/version changes across calendar time;
- data that would not be available at the stated decision point.

## 6. Live-standard verification protocol

Use live web or supplied source access for any changing rule. Prefer the issuing professional body,
regulator, trial group or primary consensus publication. Record this ledger:

| Field | Value |
|---|---|
| receipt ID / version | stable ID and receipt version/date |
| authority | issuing organisation(s) |
| normative identifier | guideline/standard/reporting-system identifier assigned by the authority |
| exact document | full title, edition/version/effective date |
| use in this study | eligibility, acquisition, category, stage, response, endpoint or reporting |
| applicability | disease, population, modality, jurisdiction and study period |
| canonical URL | direct official or primary-publication URL |
| accessed | ISO date |
| retrieved artifact | immutable local/controlled artifact path and retrieval format |
| retrieved artifact SHA-256 | physical lowercase SHA-256 of the exact PDF/HTML/XML artifact reviewed |
| exact locator | document section plus page/table/figure/paragraph locator |
| superseded relation | `supersedes` ID/version and `superseded_by` ID/version, or document-verified `none known as of accessed date` |
| verification state | `SOURCE_VERIFIED`, `LIVE_VERIFICATION_REQUIRED`, `SUPERSEDED`, `NOT_APPLICABLE` |
| exact supported statement | paraphrased rule supported at the exact locator; no unsupported extrapolation |
| verifier / verified on | responsible reviewer role and ISO date |

Re-run this gate at protocol freeze, analysis freeze, manuscript submission and major revision.
An accessible current landing page does not prove that a historical cohort used that version, and a
URL without the retrieved artifact SHA-256 and section/page locator is not a completed receipt.
Retain superseded documents when they govern the historical study period, but do not cite them as the
current rule; link both sides of the superseded relation when the authority supplies them.

## 7. Constructive review and mentoring

For each issue, return:

`evidence anchor -> governing clinical criterion -> affected estimand/claim -> severity -> minimum
repair -> stronger option and cost -> closure evidence -> wording if unresolved`.

For a learner, also ask one decision-bearing question from each relevant family:

1. What real clinical decision changes if the result is true?
2. Which patients are hardest and most likely to be missing from the cohort?
3. What information existed at time zero?
4. What could create the same imaging signal without the proposed disease mechanism?
5. What is the weakest evidence that would falsify the preferred explanation?
6. Which validation tier is feasible with current patients, tissue, time and expertise?
7. Who cannot access the protocol or follow-up assumed by the design, and how could a failed or
   uncertain output affect patients, readers, technologists or the clinical workflow?

## 8. Claim ceilings

| Available evidence | Maximum default wording |
|---|---|
| internal retrospective association | associated with / discriminated within the analysed cohort |
| temporally or geographically independent validation | validated performance in the named external setting |
| prospective silent evaluation | prospective performance under the declared workflow |
| reader or workflow impact study | changed the measured reader/process outcome in that study |
| clinical utility trial | improved the prespecified clinical/process outcome under the evaluated use |
| cross-sectional molecular concordance | consistent with / linked to the measured biological feature |
| longitudinal or orthogonal validation | supports the named explanation, with alternatives retained |
| controlled perturbation with target engagement and rescue | supports a bounded causal contribution in that system |

Any mismatch in population, timing, protocol, reference standard or unit may lower the ceiling.

## 9. Writing handoff packet

Freeze these items before prose drafting:

- clinical decision, intended use and one-sentence contribution;
- PICO/estimand, time zero, horizon and independent unit;
- cohort flow and clinically meaningful exclusions;
- acquisition/reconstruction and reference-standard facts;
- treatment/time-line map;
- primary and subgroup claims with evidence state;
- current-standard citations and unresolved live-verification flags;
- allowable clinical implication and explicit non-implication;
- subgroup representativeness, access/workflow burden and plausible downstream harms;
- limitations that materially change transportability or meaning.

If any immutable field changes during writing, return to this router rather than repairing it with
stronger prose.
