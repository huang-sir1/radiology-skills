# Acute and emergency imaging research playbook

Use this reference to design or audit acute-care imaging research. It is a research-design playbook,
not an emergency imaging protocol, triage rule, clinical-practice guideline, or patient-care tool.
Any condition-specific imaging or treatment window must be verified against the governing authority,
jurisdiction, institution, and study period and marked `LIVE_VERIFICATION_REQUIRED` until that
verification is complete.

## 1. Lock the pathway before selecting images

Name one acute pathway and one decision that imaging could change. Do not pool pathways merely
because they use the same modality.

| Pathway | Required distinction for research |
|---|---|
| prehospital or transfer triage | origin, transport/transfer decision, receiving capability, information available before arrival |
| emergency-department work-up | walk-in versus ambulance/transfer, triage state, acute syndrome, initial versus delayed imaging |
| trauma activation | activation level, primary survey state, direct-to-scanner pathway, transfer imaging and repeat imaging |
| hyperacute neurologic pathway | suspected syndrome, last-known-well/onset evidence, transfer status, baseline deficit and treatment availability |
| acute chest/abdominal/vascular pathway | presenting syndrome, physiological stability, prior testing and intended rule-in/rule-out action |
| inpatient deterioration | ward/ICU location, trigger, baseline illness, competing urgent work and different ordering workflow |
| post-procedure or postoperative emergency | procedure, elapsed time, expected postoperative findings and responsible service |

Separate diagnostic accuracy, triage prioritisation, report acceleration, communication, treatment
selection, transfer, resource use and patient outcome. A faster report is not automatically a faster
or better action.

## 2. Define the clocks and time zero

Acute imaging has several valid clocks. Freeze the one aligned with the estimand and retain the rest
as process variables:

`symptom/onset or injury -> first medical contact -> arrival -> triage/activation -> order -> protocol
decision -> transport to scanner -> acquisition start/end -> image availability -> preliminary/final
interpretation -> critical-result communication -> acknowledgement -> clinical action -> disposition`.

- State whether time zero is onset, arrival, activation, order, acquisition completion, alert, or
  randomisation. Do not switch clocks after seeing results.
- Define `time-to-action` as a named action with a timestamp source and an accountable actor. Report
  turnaround time, communication time and action time separately.
- Reconcile PACS, modality, EHR, paging, transfer and research-system clocks. Record timezone,
  daylight-saving changes, back-entered events, batch signing and missing/implausible sequences.
- If the index test or alert changes queue position, later patients' times are interference outcomes;
  they are not independent background observations.
- For transfer cohorts, retain both referring-site and receiving-site clocks and identify duplicated
  imaging, unavailable images and transport delay.

## 3. Minimum acute-care research passport

| Field | Required lock |
|---|---|
| syndrome/pathway | presenting syndrome, setting, entry route, urgency state and governing period |
| intended use | detection, rule-out, prioritisation, add-on interpretation, communication, transfer or action support |
| population | consecutive denominator, age range, severity, transfer status, prior imaging/treatment and exclusions |
| index examination/tool | modality, body region, protocol family, reader/tool availability and exact workflow insertion point |
| comparator | usual workflow, alternative modality, reader condition, queue policy or contemporaneous control |
| time zero and horizon | exact event, timestamp source, time window and handling of delayed entry |
| primary estimand | patient- or episode-level contrast, endpoint, horizon, intercurrent-event strategy and analysis set |
| unit hierarchy | patient, encounter, acute episode, examination, finding, reader, shift, site and calendar period |
| reference standard | source, verification window, blinding, adjudication and discordant/indeterminate handling |
| action endpoint | action, actor, timestamp, prerequisite findings and whether the action was clinically possible |
| workflow state | staffing, queue volume, scanner availability, downtime, diversion/crowding and local escalation policy |
| failure policy | nondiagnostic, unavailable, late, false alert, discordant and no-action states |

Use `AUTHOR_INPUT_NEEDED` for missing local workflow or timestamp facts. Do not infer them from a
paper, a vendor description, or a generic acute-care pathway.

## 4. Cohort, denominator and independent unit

- Prefer a pathway-defined denominator: all eligible presentations, activations, orders or acquired
  examinations during prespecified periods. A positive-case archive cannot estimate operational
  benefit, alert burden or false-priority harm.
- Preserve repeated visits, transfers, multiple examinations, multiphasic studies, addenda and
  repeated alerts. One patient can contribute several correlated acute episodes, but the independence
  assumption must match the estimand.
- Record patients who die, transfer, receive treatment, leave, or undergo surgery before complete
  verification. Their absence can create survivorship or informative-verification bias.
- Do not use the contralateral organ, an earlier examination, or a later report as an independent
  control without modelling within-patient dependence and temporal change.
- Describe site capability: emergency radiology coverage, overnight staffing, modality access,
  stroke/trauma/other specialty services, transfer network and escalation channels. Capability is
  part of transportability, not a nuisance label.

## 5. Imaging and operations collaboration

The clinical-domain owner freezes the pathway, decision, population, time zero, reference standard,
action and claim ceiling. Send acquisition/reconstruction, series qualification, dose, artifacts,
protocol drift and quantitative-image validity to `radiology-acquisition-qc`. Send live reader,
queue, alert, human-factors and prospective workflow design to `radiology-translation`.

At minimum, preserve:

- scanner/site, protocol family, contrast use/phase, acquisition duration and repeat series;
- portable versus fixed equipment, transfer images, outside priors and image-availability failures;
- motion, incomplete coverage, poor opacification, metal, postoperative change and other reasons an
  examination is nondiagnostic for the declared acute task;
- preliminary versus final reader, specialty, location, workload, concurrent cases and access to
  clinical history/prior imaging;
- protocol, software, prioritisation, staffing, paging and EHR/PACS changes by calendar period.

An apparently stable model can sit inside a drifting workflow. Freeze or model changes in ordering,
scanner allocation, preliminary-read policy, communication, staffing, crowding and downstream
treatment availability.

## 6. Reference standards and action truth

Match the reference to the research job:

| Job | Possible reference | Main limitation to record |
|---|---|---|
| acute target-condition detection | surgery/pathology, laboratory/physiologic evidence, expert adjudication, serial imaging or composite follow-up | verification depends on severity or index result; treatment changes later evidence |
| extent/severity | operative findings, specialist consensus, quantitative/clinical measurement or outcome | different spatial unit or post-treatment timing |
| report/alert accuracy | blinded expert reread with prespecified definitions | adjudicators may see the original report or outcome |
| communication | message and acknowledgement logs plus chart audit | sent, received, acknowledged and understood are different states |
| time-to-action | timestamped named intervention, transfer, consultation or disposition | action may be unavailable, contraindicated, declined or delayed for non-imaging reasons |
| patient/process outcome | prespecified clinical outcome, harm, resource or workflow measure | confounding by severity, staffing, treatment and calendar period |

- Do not use the final clinical report as an independent truth if the index AI, preliminary read or
  alert influenced that report.
- Do not force indeterminate or nondiagnostic examinations into negative labels. Preserve an explicit
  non-evaluable state and its downstream consequence.
- For composites, publish the component hierarchy, adjudication rules and what happens when
  components disagree.
- Clinical action is not proof that the imaging finding was correct; absence of action is not proof
  that it was unimportant.

## 7. Endpoints and study tasks

Choose one primary endpoint family and place others in a hierarchy.

| Task | Suitable primary quantity | Required companion evidence |
|---|---|---|
| diagnostic accuracy | sensitivity/specificity or calibrated risk at the declared threshold and denominator | spectrum, nondiagnostic rate, verification flow and patient-level aggregation |
| prioritisation/triage | time-to-action or time-to-verified communication under the real queue | false-priority burden, displaced-case delay, alert exposure and availability |
| reader assistance | paired/clustered reader accuracy, time and failure outcomes | reader mix, case order, washout/carryover, arbitration and learning |
| workflow intervention | prespecified process contrast across comparable periods/clusters | volume, acuity, staffing, downtime, secular trend and contamination |
| transfer/resource strategy | transfer, repeat imaging, disposition, length-of-stay or resource contrast | site capability, transport constraints and case-mix adjustment |
| clinical impact | prespecified patient/process outcome under the intended-use strategy | prospective assignment or defensible causal design, adherence and harms |

For time endpoints, report the full distribution, censoring, competing events and tail delays rather
than only a mean or median. A threshold-specific proportion can complement, not replace, the time
distribution. Avoid post hoc selection of the interval that makes the intervention look fastest.

## 8. Major bias and leakage map

| Threat | Typical acute-imaging failure | Required design response |
|---|---|---|
| spectrum/selection | only scanned, admitted, operated or severe patients retained | reconstruct the pathway denominator and exclusions |
| partial/differential verification | positives receive definitive testing; negatives receive variable follow-up | show verification route by index result and bound missing truth |
| incorporation | index result enters report, adjudication or action reference | independent adjudication or explicit incorporation analysis |
| treatment paradox | early action changes the later reference or outcome | define the treatment-policy estimand and timing |
| immortal/survivor bias | inclusion requires later imaging, action or complete follow-up | align eligibility and time zero; retain early competing events |
| before-after confounding | staffing, volume, protocol or care changes with the intervention | concurrent/clustered design where feasible; measure secular changes |
| contamination | clinicians see alerts in the control arm or learn during crossover | record exposure, carryover and protocol deviations |
| queue interference | reprioritising one case delays others | measure displaced-case and system-level outcomes |
| timestamp bias | signed reports or charted actions are batch-entered | validate event semantics and clock synchronisation |
| workflow drift | ordering, scanner, software, staffing or action threshold changes | calendar-version ledger and temporal validation |
| availability bias | action cannot occur overnight or at a low-resource site | distinguish recognition from executable action |
| label leakage | downstream treatment, final diagnosis or later scans enter an earlier model | availability audit at the declared decision point |

## 9. Validation and subgroup ladder

1. Validate timestamp semantics, protocol/version lineage and patient/episode linkage before outcome
   modelling.
2. Use locked internal validation that respects patient, episode, reader, shift and calendar
   clustering.
3. Run temporal validation across workload, staffing, protocol and software changes.
4. Run site/transfer-network validation with different capability and disease prevalence.
5. Evaluate prespecified clinically material subgroups: age, sex where relevant, pregnancy status
   where supplied and governed, language/communication access, disability, severity, transfer,
   time-of-day/day-of-week, crowding, scanner/protocol, reader experience and nondiagnostic status.
6. For workflow tools, progress from retrospective replay to prospective silent evaluation, then to
   an appropriately assigned reader/workflow study; keep each rung's claim distinct.
7. For clinical impact, measure adherence, override, alert fatigue, displaced workload, treatment
   availability, adverse consequences and downstream resource use.

Small subgroup counts are uncertainty, not proof of equivalence. Report denominators and intervals;
do not declare fairness or transportability from nonsignificant interaction tests.

## 10. Failure, uncertainty and safety outcomes

Prespecify at least these states:

- no image, incomplete/nondiagnostic image, corrupted transfer or unavailable prior;
- model/tool unavailable, delayed result, duplicate/conflicting alert or threshold indeterminacy;
- reader disagreement, changed diagnosis, communication not acknowledged and action not possible;
- false-negative delay, false-positive escalation, priority inversion, downstream unnecessary
  testing, staff burden and delay imposed on non-alerted patients;
- clinical deterioration, transfer or treatment before verification.

Report the fallback workflow and which events are observed versus not measured. Do not describe a
system as safe because no harm was documented in a dataset that did not collect harm or displaced
workload.

Return `STOP_FOR_REPAIR` when the pathway denominator or time zero cannot be reconstructed,
timestamp semantics are not auditable, index output is incorporated into the reference without a
bias boundary, queue interference is ignored for a timing/impact claim, or safety is claimed without
ascertaining relevant failure and displaced-workload outcomes.

## 11. Claim ceilings

| Evidence | Maximum default conclusion |
|---|---|
| retrospective enriched image set | discriminated the target condition in the analysed set |
| consecutive retrospective pathway cohort | estimated accuracy/process association in that pathway and period |
| retrospective queue simulation | estimated reprioritisation or timing under stated simulation assumptions |
| prospective silent evaluation | prospective technical/clinical performance without acting on output |
| assigned reader/workflow study | changed the measured reader or process endpoint in the evaluated workflow |
| impact study with action and harm ascertainment | changed the prespecified process/patient outcome under that implementation |

Do not upgrade reduced report turnaround time to reduced time-to-action, improved outcome, safety or
generalisability. Do not call a retrospective replay a deployed workflow evaluation.

## 12. Decision-bearing mentor questions

- Which exact action should occur sooner or more accurately, and which timestamp proves it?
- Which patients never reached imaging or definitive verification?
- What changed in staffing, volume, protocol, software or downstream capacity during the study?
- Who is delayed when an examination is moved forward in the queue?
- What happens when the image, alert, reader or recommended action is unavailable or uncertain?
- What is the narrowest claim that survives a different site, shift and transfer pathway?

## 13. Authoritative and original source entry points

`last checked` confirms that the entry was reachable on that date. It does not establish that a
version applies to a study or remains current. Retrieve the governing document, locator and artifact
digest before using a rule.

| Research use | Authority/original source | URL | Last checked | State |
|---|---|---|---|---|
| condition-specific acute imaging pathway/version discovery | American College of Radiology, Appropriateness Criteria | https://www.acr.org/clinical-resources/clinical-tools-and-reference/appropriateness-criteria | 2026-08-23 | official index available; exact topic/variant/version is `LIVE_VERIFICATION_REQUIRED` |
| trauma imaging pathway and performance-indicator discovery | American College of Surgeons Trauma Quality Programs, Best Practices Guidelines | https://www.facs.org/quality-programs/trauma/quality/best-practices-guidelines/ | 2026-08-23 | official index available; current imaging document and local applicability are `LIVE_VERIFICATION_REQUIRED` |
| hyperacute stroke pathway/version discovery | American Heart Association/American Stroke Association, 2026 acute ischemic stroke guideline hub | https://professional.heart.org/en/guidelines-statements/2026-guideline-for-the-early-management-of-patients-with-acute-ischemic-strokestr0000000000000513 | 2026-08-23 | official hub available; exact recommendation and study-period applicability are `LIVE_VERIFICATION_REQUIRED` |
| emergency diagnostic-imaging research priorities | Academic Emergency Medicine 2015 consensus conference research agenda | https://pubmed.ncbi.nlm.nih.gov/27234978/ | 2026-08-23 | primary consensus publication; use as research framing, not a current care rule |
| early live evaluation of AI decision support and workflow/human factors | DECIDE-AI consensus statement | https://doi.org/10.1038/s41591-022-01772-9 | 2026-08-23 | primary reporting/design source available; check current extensions at use |
