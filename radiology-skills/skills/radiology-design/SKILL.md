---
name: radiology-design
description: "Lock study feasibility, population, estimand, imaging task and validation; not novelty scanning or execution. CN: 可行性、课题设计、样本量、外部验证"
---

# Imaging Study Design & Feasibility

Use this skill at the **front of the research chain**: someone has imaging data (and maybe
clinical/pathology/molecular labels) but no settled study. It (1) triages **scientific
feasibility**, (2) keeps governance and data-access readiness as a separate verified state,
and (3) converts a feasible idea into a claim-matched design: clinical question, population,
endpoint, methods (minimum viable → stronger), and validation appropriate to the intended use.

## Core stance

- **Clinical question first, model second.** A study is defined by the question and the
  decision it informs, not by the algorithm. "Build a model" is not a study.
- **Match data to task, honestly.** The same images support very different ceilings. Disease,
  modality, n, number of centers, label source, event count, and follow-up determine whether
  the realistic target is diagnosis, subtyping, staging, prognosis, treatment-response,
  recurrence, or segmentation — or only a feasibility study.
- **Validation follows the claim and intended use.** State the validation type explicitly and
  design it **before** modelling. Internal resampling may be sufficient for bounded feasibility
  or model-development claims; transport, temporal, geographic, or external claims require the
  corresponding untouched evaluation population.
- **Surface the binding constraint.** Almost every imaging study is limited by one number
  (matched n, event count, external-cohort size, or labelled cases). Name it up front; the
  design must respect it.
- **Separate confirmation from exploration.** Lock confirmatory endpoints, analyses, and split
  rules before inspecting their results. Exploratory analyses may generate hypotheses, but must
  be labelled, multiplicity-aware, and independently confirmed before confirmatory wording.
- **Registration routes are not interchangeable.** Trial registration, preregistration, protocol
  publication and Registered Reports answer different questions. Verify the target journal before
  claiming a Stage 1/IPA route.
- **Design with affected people, not just data about them.** Distinguish PPI from participation and
  engagement; record who shaped the question, burden, harms, thresholds and dissemination, and how
  their input changed the protocol. Do not invent involvement.
- **Integrity.** Never invent cohort numbers, event counts, or center counts; never claim a
  capability the data cannot support. If the honest answer is "not yet — do X first," say so.

## When to use

- "I have [N] cases of [disease] [modality] — what can I actually study?" / "这批数据能不能做研究？"
- "Turn my data into a complete, submittable project." / "帮我把现有数据设计成一个完整课题。"
- "Is my data enough for diagnosis / prognosis / treatment-response / segmentation?"
- "Design a multi-center / external-validation / temporal-validation plan." / "多中心外部验证怎么设计？"
- "How do I show generalisability across scanners/hospitals?" / center, scanner, batch effects.
- Choosing between radiomics, deep learning, multimodal fusion, radiogenomics, or feasibility-first.
- "Can this be submitted as a Registered Report?" / "How should patients, technologists and
  radiologists shape this imaging study and its equity estimands?"

## When to open extra files

| File | Open when |
|---|---|
| [references/feasibility-triage.md](references/feasibility-triage.md) | Deciding if the data can support a study at all; what's the realistic task ceiling; what's missing |
| [references/study-blueprints.md](references/study-blueprints.md) | Picking a design template (diagnostic accuracy, prediction/prognosis, treatment-response, segmentation, radiogenomics, reader study) and its minimum-viable vs stronger version |
| [references/validation-strategy.md](references/validation-strategy.md) | Designing internal/temporal/geographic/external/multi-center/federated validation; center & scanner effects; what counts as "external" |
| [references/endpoints-and-estimands.md](references/endpoints-and-estimands.md) | Choosing the clinical question, target population, endpoint, comparator, and clinical-use scenario |
| [references/task-contract-router.md](references/task-contract-router.md) | Freezing a task-specific contract for detection/localization, segmentation/quantification, diagnosis/triage, prognosis, longitudinal response, reconstruction/enhancement, synthetic imaging or report/VLM studies |
| [references/primary-imaging-study-protocol-and-preregistration.md](references/primary-imaging-study-protocol-and-preregistration.md) | Building the primary-study protocol, SAP, preregistration/deviation and open-science lock before outcome or protected-test access |
| [templates/imaging-study-protocol.md](templates/imaging-study-protocol.md) | A durable primary imaging-study protocol artifact is authorized |
| [templates/imaging-statistical-analysis-plan.md](templates/imaging-statistical-analysis-plan.md) | A durable imaging SAP artifact is authorized after estimand/unit/outcome locks are known |
| [references/registered-reports-ppi-and-equity.md](references/registered-reports-ppi-and-equity.md) | Distinguishing trial registration/preregistration/Registered Reports, verifying a Stage 1 route, or recording patient/public/stakeholder impact and equity/access decisions |
| [templates/ppi-equity-decision-ledger.md](templates/ppi-equity-decision-ledger.md) | A durable PPI/stakeholder/equity decision artifact is requested |
| [references/modeling-route-decision.md](references/modeling-route-decision.md) | Choosing the modelling route (hand-crafted radiomics vs deep features vs end-to-end DL vs foundation adaptation) from n, events, annotation cost, compute, and timeline |
| [references/weak-result-pivot.md](references/weak-result-pivot.md) | The headline result is weak (e.g. AUC ~0.7) or the study "has no story" — picking one defensible exit |
| [references/ai-radiogenomics-12-24-roadmap.md](references/ai-radiogenomics-12-24-roadmap.md) | The user wants a 12-24 month plan for radiology AI/deep radiomics/radiogenomics, or asks how to turn data into a staged publication and translation program |

## Workflow

1. **Inventory the data and authority state.** Disease, modality(ies), n (patients and lesions),
   centers/scanners, label source and quality, masks, clinical variables, follow-up/events,
   pathology/molecular labels and time span. Separately record applicable ethics/consent or waiver,
   secondary-use authority, data/tissue access and sharing constraints. Mark every unknown; do not
   infer approval or access from the existence of data.
2. **Define the provisional question** (endpoints-and-estimands.md). Clinical question → target population →
   primary endpoint/estimand → comparator → intended clinical-use scenario.
   When organ/disease pathway, reference-standard, treatment-timeline, response/staging framework or
   acquisition-artifact context can change that definition, obtain a versioned clinical-context
   packet from `radiology-clinical-domain` **before** grading label quality or feasibility.
3. **Run the participation/equity design gate when applicable.** Open
   `registered-reports-ppi-and-equity.md`; separate involvement, participation and engagement, then
   record representation, decision authority, imaging burden/harms, access, equity estimands and
   protocol changes. Lack of PPI is reported honestly, not reconstructed after the fact.
4. **Feasibility triage** (feasibility-triage.md). Judge the reference standard against that
   specific target construct, then decide the realistic task ceiling and flag scientific
   showstoppers (unfit reference standard, inadequate events, leakage-prone structure, or validation
   that cannot support the proposed claim). Report two axes:
   `SCIENTIFICALLY_FEASIBLE / FEASIBLE_WITH_CHANGES / FEASIBILITY_ONLY / NOT_SCIENTIFICALLY_FEASIBLE`
   and `GOVERNANCE_VERIFIED / GOVERNANCE_PENDING / GOVERNANCE_BLOCKED`. A scientifically feasible
   project is not `submittable` while governance or access remains pending.
5. **Freeze the task contract** (task-contract-router.md), including target object, independent
   unit, reference standard, sampling, primary metric/CI, matching/aggregation, failure handling,
   workflow consequence, transport shift and claim ceiling.
6. **Pick the blueprint** (study-blueprints.md). Choose the design template and give a
   **minimum-viable** version (what's publishable now) and a **stronger** version (what would
   reach a higher tier), with the extra cost of each.
7. **For program-level AI/radiogenomics planning**, open `ai-radiogenomics-12-24-roadmap.md`
   and place the project on the staged route from cohort lock to baselines, fusion, external
   validation, and silent/reader/prospective evidence.
8. **Design the validation** (validation-strategy.md). Specify the split (patient-level),
   internal scheme, and the external/temporal/geographic/multi-center plan. State what is held
   out and what "external" honestly means here.
9. **Define falsification and controls** — counter-hypothesis, negative/control analysis,
   expected failure signal, and the sensitivity analysis that distinguishes artifact from signal.
10. **Write the protocol/SAP lock** (primary-imaging-study-protocol-and-preregistration.md), then
   name the binding constraint and sample-size/power/precision question (hand the numbers to
   `radiology-stats`).
11. **Select the registration/publication route.** Distinguish trial registration, preregistration,
    protocol publication and Registered Reports. For a Registered Report, verify current venue
    support and freeze Stage 1/IPA commitments before outcome/protected-test access.
12. **Return** the blueprint + feasibility verdict + validation plan + the prioritised list of
   what to secure next.

## Output contract

1. **`Feasibility verdict`** — separate scientific-feasibility and governance-readiness states,
   each with its evidence or unresolved input.
2. **`Data read`** — the inventory, with the binding constraint surfaced and unknowns listed.
3. **`Study blueprint`** — clinical question, population, primary endpoint/estimand, comparator,
   clinical-use scenario; design type.
4. **`Task contract`** — target object, unit/hierarchy, reference standard, sampling, metric/CI,
   matching/aggregation, failure handling, workflow consequence, transport shift and claim ceiling.
5. **`Method options`** — minimum-viable vs stronger, with the trade-off and which reporting
   guideline each will be judged against (→ `radiology-reporting`).
6. **`Validation plan`** — split scheme, internal + external/temporal/geographic/multi-center
   design, and the honest definition of "external" for this data.
7. **`Falsification/controls`** — counter-hypothesis, negative/control analysis, failure signal,
   and sensitivity plan.
8. **`Protocol/SAP/preregistration lock`** — primary endpoint/estimand, analysis population,
   acquisition/accepted-image gate, reference standard, split/test access, primary model/comparator,
   missingness, multiplicity, sensitivity analyses, deviations and open-science plan.
9. **`Registration/Registered Report state`** — route distinctions, verified venue policy/status,
   Stage 1/IPA commitments, deviations and exact claim boundary.
10. **`PPI/stakeholder/equity ledger`** — represented groups, decision authority, input/impact,
    imaging burden/harms, access estimands, residual disagreement and reporting state.
11. **`Roadmap`** — when relevant: staged 0-3, 3-6, 6-9, 9-12, 12-18, and 18-24 month milestones.
12. **`Governance/access state`** — the verified ethics, consent/waiver, secondary-use and access
   evidence, or an explicit `GOVERNANCE_PENDING/BLOCKED` handoff to `radiology-ethics`.
13. **`Next actions`** — what to collect, label, or confirm before/while running it, in priority
   order. Questions only the author can answer go here.

## Quality bar

A good design read sounds like a senior imaging-AI mentor who has reviewed for _Radiology_:
it tells the author honestly whether the data can carry the ambition, designs the validation
that will survive review, and surfaces the one constraint everything hinges on — without
inflating a single-center retrospective dataset into a claim it cannot support.

## Handoffs

- Frontier framing / is this direction novel & publishable → `radiology-frontier`.
- Disease/organ-specific pathway, reference standard, treatment timeline, imaging artifacts and
  live clinical-standard context → `radiology-clinical-domain`.
- Series/phase/sequence qualification, acquisition/reconstruction, quantitative transforms,
  artifacts, dose, phantom/test-retest and protocol drift → `radiology-acquisition-qc`.
- Sample size, EPV, power, Riley minimum sample size → `radiology-stats`.
- Hand-crafted radiomics pipeline design → `radiology-radiomics`.
- Deep-learning architecture & training design → `radiology-deep-learning`.
- Imaging × omics mechanism design → `radiology-radiogenomics`.
- ROI/mask annotation SOP → `radiology-annotation`.
- Which checklist the design must satisfy → `radiology-reporting`.
- Document-verified ethics/consent or waiver, secondary-use authority, tissue/data access and
  sharing constraints → `radiology-ethics`; unresolved authorization keeps governance pending or
  blocked regardless of scientific feasibility or target venue.
- Clinical-use scenario, reader study, prospective plan → `radiology-translation`.
- Turning this design into a funding proposal instead of / alongside a paper → `radiology-grant`.
- Selective-reporting/deviation or authorship-integrity audit → `radiology-research-integrity`;
  delivery RACI/site readiness → `radiology-research-ops`.
- Full-project state, decision lock, and downstream staleness → `radiology-pipeline`.
- This skill plans research; it does not provide clinical or diagnostic recommendations.
