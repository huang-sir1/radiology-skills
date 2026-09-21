# Prospective / real-world validation & workflow integration

Plan the design, workflow position and monitoring, then bound the claim to what that specific design
can identify. Prospective, retrospective, controlled-reader, pragmatic and routine-monitoring
evidence answer different questions; there is no universal strength ranking across them.

## Design-to-claim map

1. Retrospective internal — development/internal performance under the sampled setting; no patient-benefit claim.
2. Retrospective external/temporal — transport/performance under the specified external contrast; still not observed utility.
3. **Controlled reader study** — reader decision/performance under the tested case, interface and information conditions.
4. **Silent prospective validation** — technical and predictive behaviour on future eligible cases without influencing care.
5. **Active observational or quasi-experimental RWE** — observed routine-practice processes/outcomes under stated confounding and trend assumptions.
6. **Randomized/pragmatic trial** — causal policy effect for its assignment unit, implementation and estimand when trial assumptions hold (→ radiology-reporting).

Record all applicable evidence types and their assumptions. Do not treat them as automatically
cumulative: a randomized impact study may have weak transport evidence, while strong external
performance does not establish workflow or patient benefit.

## Prospective design essentials

- Pre-register the protocol and primary endpoint.
- Define the enrolment population (unselected vs criteria) and prevalence.
- Freeze the model; lock the pipeline and threshold before enrolment.
- Define outcome ascertainment uniform across the cohort.

## PACS/RIS workflow integration

- Where the output appears (PACS overlay, RIS field, worklist priority, structured report).
- Latency, failure modes, and the fallback when the model abstains or errors.
- Human-in-the-loop: how the radiologist sees, accepts, or overrides the output.
- Automation bias and deskilling risks — and how the design mitigates them.

For a real site, open `deployment-interoperability-and-site-acceptance.md`. A DICOM conformance
statement, vendor demonstration or successful research export does not prove patient/exam identity,
worklist orchestration, SR/SEG/results display, latency, fallback, audit/security or end-to-end local
interoperability.

## Monitoring & drift (post-deployment)

- Track performance and **calibration drift** over time and across scanners/sites.
- Define triggers for recalibration/retraining and who is responsible.
- Log failures and out-of-distribution inputs.
- This section is the deployment-lifecycle half of the **FUTURE-AI** framework (Fairness,
  Universality, Traceability, Usability, Robustness, Explainability —
  → `radiology-deep-learning/interpretability-uncertainty.md` for the pre-deployment
  Robustness/Explainability evidence, and `radiology-reporting/guideline-router.md` for how the
  two connect). Monitoring here operationalises Universality/Robustness in production; it does
  not substitute for the pre-deployment interpretability and uncertainty evidence.

For active production, open `production-monitoring-and-change-control.md` and specify eligible-case
capture, input completeness, output delivery, uptime/latency/failure/abstention; scanner/vendor/
protocol/software/sequence/population/spectrum/workflow drift; output/calibration/performance; label
delay/missingness/verification bias; subgroup harm; exposure/adoption/override/automation bias;
safety/resources/cost; and for every monitor its denominator, baseline, window, cadence, threshold,
owner, action, CAPA, rollback, revalidation and escalation. When labels are unavailable, declare a
`PERFORMANCE_BLIND_INTERVAL`; no alert is not proof of stable performance.

The intervention release is model + preprocessing + threshold + output schema + UI + training +
integration + fallback + monitoring configuration. A material change can stale prior human-impact and
site-acceptance evidence even when model discrimination is unchanged.

## Evidence-to-claim output

```
Evidence obtained:   [design, setting, release and observed axis]
Licensed claim:      [what can honestly be said]
Not yet supported:   [claims requiring a different or stronger identifying design]
Next decision:       [smallest study/artifact that resolves the current uncertainty]
```

This map describes study evidence only. Record regulatory, economic, implementation and production
states separately using `evidence-state-and-translation-lifecycle.md`.

## Reporting sentence

*"The frozen model was validated prospectively on consecutively enrolled patients (n=…) under the
intended PACS workflow; performance and calibration were monitored across sites. The evidence
supports [assistive use under radiologist oversight]; autonomous use is not claimed."*
