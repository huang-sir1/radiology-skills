---
name: radiology-clinical-domain
description: "Set disease pathways, endpoints, reference standards and treatment timelines; not patient care."
---

# Clinical domain research router

Use this skill to translate an organ or disease interest into an answerable clinical-imaging research
question, or to test whether an existing study respects the clinical pathway that gives its endpoint
meaning. It is an independent entry point and a cross-cutting source of clinical context for imaging,
radiomics, AI and imaging-mechanism research.

## Core stance

- Begin with the **clinical decision and intended use**, not with an available feature table or model.
- Keep screening, diagnosis, differential diagnosis, staging, response, recurrence, prognosis and
  treatment-effect questions separate. They imply different populations, time zeroes, reference
  standards, exclusions and claim ceilings.
- Define the estimand before selecting images or labels. Preserve patient, lesion, vessel, organ,
  examination and time-point hierarchy; none is automatically a new independent patient.
- Treat acquisition, reconstruction, contrast phase, scanner/site, treatment and calendar time as
  possible causes of an apparent signal, not merely covariates to add later.
- Mark changing staging, reporting, eligibility, diagnostic and treatment rules
  `LIVE_VERIFICATION_REQUIRED`. A remembered version or a high-impact paper is not a current rule.
- Separate `AUTHOR_REPORTED`, `SOURCE_VERIFIED`, `LOCAL_EXPERT_CONFIRMED` and
  `NOT_ASSESSABLE`. Never invent a local workflow, guideline version, outcome, treatment rule or
  specialist consensus.
- Research support is not individual patient care. Do not recommend diagnosis or treatment for a
  person; route clinical decisions to qualified responsible clinicians.

## Choose the mode

| Mode | Use when | Required emphasis |
|---|---|---|
| `plan` | turning an interest, cohort or biomarker into a study | decision point, PICO/estimand, time zero, endpoint, reference standard, acquisition window, confounders, validation and feasibility |
| `audit` | reviewing a protocol, Methods, cohort, labels, figures or manuscript | pathway fit, spectrum/verification/incorporation bias, protocol drift, treatment/time leakage, evidence anchors, reviewer red flags and repairs |
| `mentor` | a learner wants direction or alternatives | nearest answerable question, assumptions, competing designs, resource tiers, failure modes and decision-bearing questions |
| `interpret` | real results are supplied | clinical meaning, transportability, heterogeneity, competing explanations, decision consequence and surviving claim ceiling |
| `writing-handoff` | the science is frozen and needs manuscript placement | exact clinical facts for title/abstract/Methods/Results/Discussion, live-source status, limitations and forbidden overclaims |

Declare one or more active domains: `thoracic-lung-oncology`, `neuro-oncology`,
`liver-hepatobiliary`, `breast`, `prostate-pelvic`, `cardiovascular`, `acute-emergency`,
`musculoskeletal`, `pediatric`, `nuclear-medicine-theranostics`, or `local-extension-needed`.

Use [the live-standard receipt](templates/live-standard-receipt.md) whenever a changing clinical or
reporting rule affects eligibility, acquisition, category, stage, response, endpoint or a claim.

## Required workflow

1. Read [the clinical domain routing contract](references/clinical-domain-routing.md).
2. Read only the smallest active-domain playbook:
   - for `thoracic-lung-oncology`, `neuro-oncology`, `liver-hepatobiliary`, `breast`,
     `prostate-pelvic` or `cardiovascular`, read only that section in
     [the starter playbooks](references/domain-playbooks.md);
   - for `acute-emergency`, read
     [the acute/emergency playbook](references/acute-emergency-imaging-research.md);
   - for `musculoskeletal`, read
     [the MSK playbook](references/musculoskeletal-imaging-research.md);
   - for `pediatric`, read
     [the pediatric playbook](references/pediatric-imaging-research.md);
   - for `nuclear-medicine-theranostics`, read
     [the nuclear medicine/theranostics playbook](references/nuclear-medicine-theranostics-research.md).
3. Build a compact clinical research passport:
   - disease and clinical setting;
   - decision point and intended use;
   - target population, exclusions and recruitment pathway;
   - index image/measurement, comparator and time zero;
   - outcome or target condition, horizon and estimand;
   - independent unit and repeated-measure hierarchy;
   - reference standard, verification window and adjudication;
   - treatment, intervention, surveillance and acquisition timeline;
   - relevant jurisdiction, institution and standard version;
   - representativeness across clinically material subgroups, access to the required imaging/
     referral pathway, uncertain/failure-result harms, workflow burden and affected stakeholders.
4. Mark missing fields `AUTHOR_INPUT_NEEDED`; do not fill them with plausible defaults.
5. Run the live-standard gate for every rule that may change. Instantiate the versioned receipt and
   record issuing authority, normative identifier, full document title, version/edition/effective
   date, applicability, canonical URL, access date, retrieved artifact path and physical SHA-256,
   exact section/page/table locator, supported statement and `supersedes`/`superseded_by` relation.
   `SOURCE_VERIFIED` requires the retrieved artifact and locator, not merely a current landing page.
   If live access or the normative document fails, preserve `LIVE_VERIFICATION_REQUIRED` and do not
   state the rule as current.
6. Work in order:
   `decision -> PICO/estimand -> cohort pathway -> image protocol -> reference standard ->
   treatment/time -> analysis unit -> mechanism alternatives -> validation -> claim ceiling`.
7. Return the smallest complete artifact for the selected mode. If a reusable local record helps,
   use [the clinical expert profile](templates/local-clinical-expert-profile.md).
8. For any real or proposed use of human participants, identifiable images/records, linked clinical
   data or human tissue, hand the activity/data map to `radiology-ethics: human-subjects`. Preserve
   consent/waiver, privacy, secondary-use, tissue and sharing facts as `AUTHOR_INPUT_NEEDED` until
   verified; a clinically sound design is not ethical approval.

## Scientific red lines

- Do not mix a screening cohort with symptomatic, surveillance or treatment-response patients
  without separate estimands and validation.
- Do not use downstream pathology, treatment, follow-up or future examinations in a model claimed
  to operate earlier in the pathway.
- Pathology is not a single infallible label: record sampling route, target, timing, tissue adequacy,
  spatial mismatch and whether image findings influenced verification.
- Excluding indeterminate, unverified, poor-quality or hard-to-biopsy cases can change the target
  population. Report the flow and consequence rather than calling the remainder “clean”.
- An imaging phenotype may reflect disease biology, treatment, comorbidity, acquisition or
  annotation. Name at least one plausible alternative biological and one technical explanation.
- Prediction or association is not mechanism; prognostic association is not treatment benefit;
  treatment-group outcome prediction is not a predictive biomarker without a valid comparator and
  interaction estimand.
- A standardized reporting category is not automatically a ground-truth disease label, continuous
  biological quantity or treatment prescription.
- Internal performance, reader agreement, multi-site transportability, clinical utility,
  biological concordance and causal validation are distinct rungs; do not rename one as another.

## Output contract

Return, in order:

1. `Route and evidence state` — mode, active domain, task, supplied materials, live-source status
   and live-standard receipt IDs/digests.
2. `Clinical research passport` — decision point, PICO/estimand, time zero/horizon, unit and pathway.
3. `Protocol and reference-standard map` — acquisition/reconstruction, artifacts, label source,
   verification window and adjudication.
4. `Treatment and time-line map` — interventions, disease evolution, imaging windows and leakage or
   confounding risks.
5. `Equity, access and consequence map` — subgroup representation, missing pathway populations,
   equipment/expertise access, failure/uncertainty harms, workflow burden and stakeholder effects.
6. `Mechanism alternatives and validation ladder` — biological, clinical and technical explanations,
   discriminating evidence and achievable validation tier.
7. `Constructive findings or mentor decisions` — exact criterion, evidence anchor, severity, minimum
   repair, stronger option/cost, closure evidence and learner question.
8. `Claim ceiling and writing handoff` — allowed wording, prohibited upgrade, section placement,
   live citations, normative ID/version/locator, retrieved-artifact SHA-256, superseded relation and
   residual limitations.
9. `Next action` — the single decision-bearing next step plus `AUTHOR_INPUT_NEEDED` and
   `LIVE_VERIFICATION_REQUIRED` fields.

## Handoffs and non-ownership

- Imaging series/phase/sequence qualification, acquisition/reconstruction, quantitative transforms,
  artifacts, dose, phantom/test-retest and protocol drift route to `radiology-acquisition-qc`;
  annotation, radiomics and model execution remain with their corresponding owners. Provide the
  clinical passport, endpoint, unit and timing contract.
- Imaging-to-molecular or pathology mechanism interpretation requires the mechanism module; provide
  disease context, treatment timeline, tissue-image mapping and claim ceiling.
- Parameter provenance, sensitivity, benchmark fairness and method fit require the method-evaluation
  module after the clinical estimand is fixed.
- Estimation, uncertainty, clustered inference, survival analysis and multiplicity require the
  statistics module with the true unit and estimand preserved.
- Human participants, identifiable images/records, linked clinical variables, human tissue,
  consent/waiver, privacy, secondary use and sharing governance require
  `radiology-ethics: human-subjects`. Provide population, recruitment, data/tissue flows,
  linkage/identifiability, sites/jurisdictions and proposed use; this module cannot infer IRB status
  or approval scope from a published cohort or manuscript sentence.
- Reader studies, threshold-to-action mapping, prospective workflow evaluation, implementation
  burden and clinical-utility evidence require `radiology-translation`. Provide the disease/
  pathway, intended-use, reference-standard, treatment-time, subgroup/access and claim-ceiling lock;
  translation owns the reader/prospective/deployment study design.
- Full-manuscript review, prose drafting, response letters and submission-file audits remain separate
  tasks. This skill supplies immutable clinical facts and unresolved live-standard flags.
- Local expert entries are case-based evidence. They can inform questions and feasibility but cannot
  silently become universal clinical rules.

## Boundary

The six starter routes and four focused playbooks are research-design aids, not clinical-practice
guidelines. The pediatric pack may be composed with one organ/pathway pack, but its developmental,
body-size, dose, sedation and family-dependence constraints remain explicit. For a different disease,
create `local-extension-needed` from the same passport and live-standard protocol before giving
disease-specific advice. No output from this skill substitutes for multidisciplinary review,
prospective validation, ethics review or individual patient care.
