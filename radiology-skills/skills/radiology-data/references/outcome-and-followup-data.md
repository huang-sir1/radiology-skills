# Outcome & follow-up data

The data-side half of survival analysis: how outcome fields are defined, how follow-up is
acquired, when follow-up is too short, and which missing-data strategy the design can defend.
Model-side choices (Cox assumptions, imputation pooling) route to `radiology-stats`; estimand
locks route to `radiology-design`.

## Endpoint field spec

| Field | Rule |
|---|---|
| `patient_id` | patient grouping/split key, **not a universal join key**; declare the endpoint/observation row grain and full key (`cohort-assembly-and-id-reconciliation.md`) |
| `endpoint_id` / `outcome_record_id` | distinguish endpoints, repeated/recurrent observations and record versions; add timepoint/episode keys when required and audit join cardinality |
| `time_origin` | exactly one per endpoint — diagnosis, surgery, or treatment start; state which and why; never mix origins within an endpoint |
| `event_type` / `event` | preserve target event, each competing event and censoring separately; derive a binary analysis indicator only under the locked estimand/model; coding fixed in the dictionary (`data-dictionary-spec.md`) |
| `event_date` / `last_contact_date` / `last_known_event_free_date` | record sources and endpoint-specific ascertainment; being contacted/alive does not prove absence of progression or recurrence; keep interval bounds when event time is interval censored |
| `censor_reason` | administrative end / loss to follow-up / withdrawal or other prespecified reason; a competing event keeps its own type/date even if a cause-specific model subsequently censors at that event |
| `time` | derive from the prespecified event or endpoint-appropriate censoring date minus `time_origin`, with administrative limits and units fixed; do not substitute a later contact for the last confirmed event-free assessment; preserve interval bounds when applicable |
| `horizon` | administrative censoring date and time-horizon (e.g. 3-year) pre-specified |

The censoring definition is locked per endpoint **before** the first Kaplan–Meier curve;
changing it after seeing curves is a protocol deviation (decision log, `radiology-pipeline`).

## Follow-up acquisition SOP

Channel ladder, cheapest reliable first; record every contact attempt.

1. **Clinic / outpatient records** (门诊复查) — scheduled imaging and clinic notes.
2. **Telephone follow-up** (电话随访) — scripted; two attempts on different days before marking
   a patient unreachable; who called and when is logged.
3. **Medical records office** (病案室) — re-admissions and in-hospital deaths.
4. **Death registry** (死因登记) — where institutional access exists; confirm the access route
   with your institution (verify live; governance: `radiology-ethics`).

```text
followup_log.csv:
contact_id,patient_id,endpoint_id,outcome_record_id,channel,contact_date,status,event_info,last_known_event_free_date,next_due,operator
```

Set a follow-up cadence per endpoint (example: every 3–6 months for the first 2 years —
justify per disease course) and a closing date after which all remaining patients are
administratively censored.

## Completeness — quantify, don't assert

Report all three, in Methods/Results:

- **Median potential follow-up by reverse Kaplan–Meier** using all eligible patients with usable
  event/censoring times: original events are censored and original right-censorings become events
  for this follow-up estimator. Do not restrict the calculation to censored patients. State the
  endpoint, population and handling of delayed entry/competing events; if the median is not reached,
  report that rather than substituting the median of observed times.
- **Percent reaching the horizon** (or event) per cohort.
- **Loss-to-follow-up rate**, with reasons from `censor_reason`.

Pre-specify minimums in the protocol; a cohort below its follow-up floor is a design problem
(see `radiology-pipeline/underpowered-fallback.md`), not a footnote. These three numbers are
consistency keys reconciled before submission (`radiology-pipeline/cross-artifact-consistency.md`).

## Follow-up too short — preserve the time-zero population

| Route | What it means | Cost | When defensible |
|---|---|---|---|
| **Include and censor** | retain eligible patients and all observed target/competing events; censor event-free observations at the last endpoint-appropriate ascertainment | less information and wider CIs | censoring assumptions and completeness are defensible; use sensitivity for informative loss |
| **Administrative entry cutoff** | restrict enrollment dates so sufficient potential follow-up exists before a fixed data close | smaller eligible recruitment period | freeze calendar eligibility without requiring actual future survival or follow-up; retain early events among eligible patients |
| **Landmark question** | define a new population alive/event-free and observable at a prespecified landmark, with follow-up and prediction starting there | answers a different conditional question | declare eligibility, exclusions and new time zero; do not generalize to the original baseline population |

Do not exclude early deaths or other early events because observed follow-up is below a minimum.
Prespecification or an included-versus-excluded baseline table does not remove the resulting
survivor-selection/immortal-time problem. Whether death is a target or competing event follows the
endpoint definition. Escalate unresolved landmark, delayed-entry or censoring choices to
`radiology-stats` and `radiology-design` before filtering.

## Missing data — strategy by mechanism

| Assumed mechanism | Complete case | Multiple imputation | Also required |
|---|---|---|---|
| **MCAR** (missing unrelated to any data) | may be valid but loses precision; state the population and assumptions | candidate when compatible with the estimand/model | report missingness and efficiency; a baseline comparison cannot prove MCAR |
| **MAR** (missing explained by observed variables) | validity depends on the estimand and selection/model structure; not universally biased or valid | use a justified compatible MI/model/weighting method; select variables under the analysis context below | report assumptions, variables, number of imputations, diagnostics and software |
| **MNAR** (missing depends on unobserved values after conditioning) | generally needs additional identifying assumptions | standard MAR-based MI does not resolve MNAR | use explicit sensitivity/selection/pattern-mixture assumptions where defensible |

- **Association/effect estimation:** include observed outcomes and suitable auxiliary variables in a
  compatible imputation model when justified for the inferential estimand; account for survival
  outcome/censoring structure rather than treating follow-up as an ordinary complete variable.
- **Prediction development and validation:** fit the imputation procedure within development folds
  and reproduce the intended deployment procedure during validation. Do not use protected
  validation/test outcomes to impute predictors. Development use of outcomes in MI needs an explicit,
  validated strategy for new patients whose outcomes are unavailable; it is not an instruction to
  feed future outcomes into inference-time preprocessing. Full-cohort fitting before splitting is
  leakage (`radiology-pipeline` SKILL, stage-4 rule).
- Missing outcome ascertainment, censoring and competing events require their own estimand-aware
  treatment; a routine covariate imputer cannot silently manufacture event-free follow-up.
- Report: assumed mechanism, method, number of imputations, imputation-model variables, and the
  sensitivity of the headline result to the choice. Pooling rules and diagnostics →
  `radiology-stats`.
- For high-missingness variables, pre-specify a drop line rather than imputing noise.

## Methodological sources

- Schemper M, Smith TL. [A note on quantifying follow-up in studies of failure time](https://pubmed.ncbi.nlm.nih.gov/8889347/).
- [REMARK explanation and elaboration: follow-up reporting](https://pmc.ncbi.nlm.nih.gov/articles/PMC3362748/).
- Lévesque LE, et al. [Problem of immortal time bias in cohort studies](https://www.bmj.com/content/340/bmj.b5087).
- [Imputation and missing indicators in development and deployment of clinical prediction models: simulation study](https://pmc.ncbi.nlm.nih.gov/articles/PMC10515473/).

Checked 2026-09-04; route numerical implementation and estimator-specific assumptions to
`radiology-stats`.
