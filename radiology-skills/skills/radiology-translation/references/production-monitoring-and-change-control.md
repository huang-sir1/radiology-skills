# Production monitoring, change control and retirement

Use this reference after or during bounded active deployment. Monitoring is a prespecified decision
system, not a dashboard of convenient metrics.

## 1. Monitor the complete intervention

Bind the release bundle: model/weights, preprocessing, threshold, output schema, UI, training,
integration, intended use, fallback and monitoring configuration. Give each monitor:

`metric/event | eligible denominator | exclusions/missingness | baseline/reference | window | cadence |
strata | threshold/decision rule | label delay/verification plan | owner | investigation | immediate
containment | CAPA | rollback/revalidation/regulatory escalation | closure evidence`.

## 2. Required monitor families

| Family | Imaging examples |
|---|---|
| capture/delivery | eligible case capture, input completeness, execution/output delivery, uptime, latency, failure, abstention |
| input/context drift | scanner/vendor/protocol/software, sequence/phase, dose, population/disease spectrum, referral and workflow |
| output/performance | output distribution, errors, discrimination/accuracy, calibration and clinically material operating-point performance |
| label integrity | outcome availability/delay, selective verification, reference-standard change, adjudication and missingness |
| subgroup/equity harm | access/exposure, errors/calibration, downstream action and burden across prespecified intersectional groups |
| human interaction | output opened, adoption/ignore/override, correct-to-incorrect changes, alert fatigue, automation bias, workload/training decay |
| safety/resources/economics | incidents/near misses, unnecessary/delayed care, resource displacement, cost and capacity drift |
| change/system | release mismatch, configuration/UI/training changes, integration failures, unauthorized adaptation and cybersecurity events |

When labels are delayed, missing or selectively verified, report a `PERFORMANCE_BLIND_INTERVAL` and
use process/input proxies only as proxies. Absence of an alarm cannot establish stable performance.

## 3. Event and CAPA lifecycle

`signal -> triage/severity -> preserve release/input/output/log evidence -> immediate containment ->
root-cause hypotheses and analysis -> corrective/preventive action -> validation/retest -> authorized
release/rollback -> effectiveness check -> closure/residual risk`.

Keep `OBSERVATION`, safety/performance `SIGNAL`, confirmed technical event and formal regulatory/
institutional finding distinct. Route research-integrity concerns to
`radiology-research-integrity`; do not infer intent or misconduct from a production anomaly.

## 4. Change, stop and retirement

Classify changes to data pipeline, model/weights, threshold, intended population/use, output,
UI/training, integration/fallback, monitoring and security. For each record affected evidence,
risk, required technical/clinical/human/site/economic revalidation, live jurisdictional decision and
rollback. A PCCP describes bounded planned modifications and controls; it is not permission for
unbounded self-updating.

Predefine pause/rollback/retire criteria for safety harm, critical identity/delivery failure,
performance/calibration/equity breach, unavailable labels beyond the safety tolerance, unauthorized
change, expired support/security, unsustainable workload/cost or superior replacement. Retirement
includes communication, worklist/integration disablement, archival, data/log retention, open-incident
handoff and prevention of stale output reuse.

Return `release manifest -> monitoring specification -> current blind intervals/signals -> event/CAPA
ledger -> change/revalidation decision -> pause/rollback/retire state -> owner and claim ceiling`.

## Official sources

- FDA. [Methods and tools for effective postmarket AI monitoring](https://www.fda.gov/medical-devices/medical-device-regulatory-science-research-programs-conducted-osel/methods-and-tools-effective-postmarket-monitoring-artificial-intelligence-ai-enabled-medical-devices)
  (official regulatory-science program checked 2026-08-23; not itself an authorization).
- FDA. [PCCP final guidance](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/marketing-submission-recommendations-predetermined-change-control-plan-artificial-intelligence)
  (final August 2025, checked 2026-08-23).
- FDA. [QMSR](https://www.fda.gov/medical-devices/postmarket-requirements-devices/quality-management-system-regulation-qmsr)
  (official page states effective 2026-02-02; checked 2026-08-23).

Qualified local manufacturer, quality, regulatory, safety, IT and clinical owners control formal
CAPA, reportability, release, rollback and retirement decisions.
