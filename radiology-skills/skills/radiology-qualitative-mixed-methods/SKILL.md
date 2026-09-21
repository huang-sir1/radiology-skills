---
name: radiology-qualitative-mixed-methods
description: "Design/audit qualitative and mixed-methods sampling, reflexivity, integration and claim limits."
---

# Radiology Qualitative and Mixed Methods

Use this skill when the research question requires accounts, meanings, behaviours, interactions or
work practices to be studied through interviews, focus groups, observation, workflow ethnography,
think-aloud or an explicit qualitative-quantitative integration design. Its unique responsibility is
the qualitative strand and the logic by which qualitative and quantitative strands are integrated.

## Non-negotiable boundaries

- A usability interview, debrief or collection of free-text comments is not automatically a complete
  qualitative study. Without a declared question, sampling logic, analysable records, analytic method,
  reflexivity and audit trail, label it `FORMATIVE_FEEDBACK_ONLY`.
- Purposeful sampling supports information-rich variation, not statistical representativeness.
  Do not justify a fixed sample with folklore or claim saturation without a method-specific stopping
  rule and contemporaneous evidence.
- Participant quotations and field observations are source evidence; codes, themes and explanations
  are analytic interpretations. A mixed-methods meta-inference is a further interpretive step.
- Member checking, multiple coders, inter-coder agreement and software use are not universal proof of
  qualitative validity. Select rigor procedures that fit the analytic tradition and record what each
  procedure can and cannot establish.
- Parallel qualitative and quantitative work is not mixed-methods integration unless the strands
  meet at a prespecified design, sampling, analysis or interpretation point.
- This skill does not own quantitative power calculations, survey psychometrics, clinical workflow
  deployment, ethics approval, individual patient decisions or manuscript copy-editing.

## Route by mode

| Need | Mode | Read |
|---|---|---|
| define a qualitative question, design, sample and fieldwork plan | `scope-plan` | [methods-and-rigor.md](references/methods-and-rigor.md) |
| build an interview, focus-group, observation, ethnography or think-aloud protocol | `fieldwork-protocol` | [methods-and-rigor.md](references/methods-and-rigor.md) |
| audit coding, themes, negative cases, reflexivity or an existing qualitative report | `analysis-audit` | [methods-and-rigor.md](references/methods-and-rigor.md) |
| plan or interpret convergent, explanatory-sequential or exploratory-sequential research | `mixed-methods-integration` | [mixed-methods-integration.md](references/mixed-methods-integration.md) |
| freeze methods/results fields for a protocol, grant or manuscript | `reporting-handoff` | the applicable method reference and [source-registry.md](references/source-registry.md) |

Do not load every reference for a narrow request. Use
[qualitative-mixed-methods-passport.md](templates/qualitative-mixed-methods-passport.md) for a
persistent study record and
[joint-display-and-discordance-ledger.md](templates/joint-display-and-discordance-ledger.md) when
the strands are integrated.

## Input passport

Before giving a claim-bearing recommendation, record:

1. decision context, research question, stage and intended claim;
2. qualitative tradition or mixed-methods rationale, priority and timing; use
   `AUTHOR_INPUT_NEEDED` rather than inventing an epistemological position;
3. participant/stakeholder roles, setting, unit of analysis, eligibility, sampling frame and
   purposeful sampling dimensions;
4. data source, topic/observation guide, interviewer or observer relationship, recording,
   transcription/translation and privacy state;
5. analysis approach, unit of coding, inductive/deductive balance, coder roles, software and
   versioned codebook or reflexive memo process;
6. for mixed methods, strand-specific artifact versions, integration point/level, sampling
   relationship and planned joint display or traceable narrative integration; require a linking key
   only for participant/case-level linkage;
7. supplied raw artifacts and their evidence state.

Missing fields remain visible. Do not infer consent, transcript completeness, participant identity,
site context, data quality or analytic decisions from filenames or polished prose.

## Required workflow

1. **Lock the phenomenon and claim.** State whether the study seeks description, interpretation,
   explanation, theory development, implementation insight or instrument development.
2. **Match design to the question.** Select interviews, focus groups, observation, workflow
   ethnography or think-aloud because of the evidence they can produce, not because they are
   convenient. In radiology, freeze the imaging task, role, site, shift, PACS/RIS/EHR context,
   displayed image/report/AI-output version and scenario fidelity.
3. **Make sampling auditable.** Specify purposeful criteria and desired variation. Use information
   power or a method-specific saturation construct, state its dimensions, review it during
   collection and keep a stopping log. Do not convert it into a post hoc claim that “no new themes”
   appeared.
4. **Preserve fieldwork context.** Record who collected the data, prior relationships, power
   differences, prompts, non-participation, group composition, observation role and field changes.
   Think-aloud reveals verbalised reasoning under reactivity; it does not reproduce an unobserved
   natural workflow.
5. **Run the declared analysis.** Keep raw segment -> code -> category/theme -> interpretation
   traceability. Search for negative or deviant cases and document decisions. Use member checking
   only for a defined purpose, such as correcting factual accounts or discussing interpretation.
6. **Integrate deliberately.** For mixed methods, connect, build, merge or embed the strands at the
   declared participant, site, construct, design or interpretation level. A joint display or traceable
   narrative can document the bridge; different samples do not require invented person-level keys.
   Classify convergence, complementarity, expansion and discordance; derive a bounded meta-inference.
   Never infer individual relationships from aggregate integration or let the larger strand win.
7. **Separate statement classes.** Label `SOURCE_EVIDENCE`, `PARTICIPANT_ACCOUNT`,
   `FIELD_OBSERVATION`, `ANALYTIC_INTERPRETATION`, `META_INFERENCE`,
   `RECOMMENDATION` and `AUTHOR_INPUT_NEEDED`.
8. **Apply the claim ceiling and hand off.** Qualitative transferability depends on documented
   context and analytic reasoning; it is not prevalence. Mixed-methods integration does not repair
   a weak constituent strand.

## STOP gates

Return the exact stop state and the smallest next action:

- `STOP_ETHICS_OR_PRIVACY`: consent, confidentiality, recording, image/report exposure or
  re-identification authority is unresolved;
- `STOP_NO_ANALYSABLE_RECORD`: conclusions rely only on memory, unverified AI summaries or
  inaccessible recordings without an authorised analytic record;
- `STOP_DESIGN_METHOD_MISMATCH`: the named method cannot answer the question or its required
  sampling/data/analysis elements are absent;
- `STOP_UNSUPPORTED_ADEQUACY`: information power or saturation is asserted without defined,
  reviewable evidence;
- `STOP_NO_INTEGRATION`: a mixed-methods claim is requested but no defensible integration point,
  strand-to-inference bridge or discordance handling exists; missing participant keys block only
  an inference that requires participant-level linkage, not construct-level or sequential integration.

A STOP blocks the affected claim, not all useful work. A bounded design repair or artifact inventory
may still be returned.

## Radiology-specific evidence limits

- Interview patients, radiologists, technologists, physicists, referrers and operational staff as
  distinct roles; one role cannot silently stand for the whole pathway.
- Account for reporting-room interruptions, worklists, hanging protocols, prior examinations,
  display calibration, voice recognition, handoffs, alert timing and local escalation rules.
- Observation can reveal work-as-done but does not prove why it occurs; interviews can explain
  experience but do not directly measure actual behaviour.
- Think-aloud and simulated cases may alter speed, search and confidence. Preserve case selection,
  image presentation, AI version and observer presence as transfer boundaries.
- Qualitative acceptance of an imaging or AI tool does not establish diagnostic accuracy, safety,
  effectiveness, cost-effectiveness or implementation success.

## Output contract

Return only the sections needed for the selected mode:

1. `Route and passport status` — mode, supplied artifacts, missing inputs and stop state.
2. `Question-design-claim map` — phenomenon, design rationale, unit and claim ceiling.
3. `Sampling adequacy plan/read` — purposeful dimensions, information-power or saturation logic,
   stopping evidence and exclusions.
4. `Fieldwork and reflexivity` — guide, setting, relationships, recording and positionality.
5. `Analysis audit trail` — analytic approach, segment-to-interpretation trace, negative cases and
   conditional credibility procedures.
6. `Integration and discordance` — design, joint display or integrated narrative, convergence/complementarity/discordance
   and bounded meta-inferences when applicable.
7. `Evidence-inference-recommendation ledger` — no category laundering.
8. `Limitations and handoff` — unresolved risks and unique receiving owner.

## Handoffs and non-ownership

- Quantitative design, power, psychometrics and numerical inference -> `radiology-stats` or
  `radiology-design`; acquisition claims -> `radiology-acquisition-qc`.
- Human-factors deployment, prospective workflow evaluation and routine usability testing ->
  `radiology-translation`. Return here only when a genuine qualitative or mixed-methods inference
  is requested.
- Data governance/de-identification -> `radiology-data`; consent and participant governance ->
  `radiology-ethics`.
- Reporting-guideline selection -> `radiology-reporting`; prose production ->
  `radiology-writing`; project receipts -> `radiology-pipeline`.
- Individual patient imaging, diagnosis or treatment decisions remain with the responsible clinical
  team. This skill does not confer ethics approval or certify methodological validity.
