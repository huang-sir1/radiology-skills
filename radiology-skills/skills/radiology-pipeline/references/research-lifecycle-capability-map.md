# Authoritative research-lifecycle capability map

Use this map to place a request in the research lifecycle before selecting a specialist. It is the
authoritative topology for the suite. It does not replace the unique-owner decisions in
`research-intent-routing.md`, the evidence requirements in `stage-gates-and-handoffs.md`, or the
scientific decision logic in `research-decision-cycle.md`.

Three structures coexist for different purposes:

- **Lifecycle position** says where the project or output currently sits.
- **D0-D9 decision state** says which scientific decision is open.
- **Stage 0-11 gate** says which durable artifact and acceptance evidence are required.

They are related but are not interchangeable. A revision, deployment or published-output event can
reopen an earlier scientific decision without moving the project backwards administratively.

## 1. Main lifecycle

| Lifecycle position | Decision or deliverable | Primary capabilities | Exit or handoff |
|---|---|---|---|
| Intake and current-state discovery | identify the requested decision, supplied artifacts, authority and earliest stale dependency | `radiology-pipeline` | one current owner, bounded scope and known evidence state |
| Question and evidence formation | define the clinical/scientific question, novelty, evidence gap, review question or data-bound opportunity | `radiology-frontier`, `radiology-search`, `radiology-citation`, `radiology-design`, `radiology-clinical-domain`; formal evidence synthesis uses `radiology-systematic-review` | question/estimand, evidence boundary and feasibility decision |
| Protocol, registration and funding | lock population/system, endpoint, estimand, measurement, validation, SAP, registration route, governance and funder contract | `radiology-design`, `radiology-acquisition-qc`, `radiology-stats`, `radiology-data`, `radiology-ethics`, `radiology-grant`; operational startup uses `radiology-research-ops` | protocol/registration/funding artifacts with unresolved institutional actions visible |
| Startup, acquisition, data and ground truth | qualify sites and roles; acquire/accept images; build cohort/data identity; establish labels, annotations, specimens and access | `radiology-research-ops`, `radiology-acquisition-qc`, `radiology-data`, `radiology-annotation`, `radiology-ethics` | accepted measurement/data/ground-truth artifacts and traceable deviations |
| Execution, analysis and evaluation | run the declared imaging, modelling, transcriptomics or experimental route and evaluate inference, parameters, comparison and reproducibility | `radiology-radiomics`, `radiology-deep-learning`, `radiology-transcriptomics-analysis`, `radiology-experiment-design`, `radiology-radiogenomics`, `radiology-method-evaluation`, `radiology-stats`, `radiology-reproducibility` | versioned run/results/diagnostics and an evidence-bounded interpretation |
| Evidence freeze and research decision | reconcile values, claims, alternatives, negative/failure evidence, figures and tables; decide proceed/refine/replicate/pivot/stop | scientific owner with `radiology-method-evaluation`, `radiology-stats`, `radiology-figure`, `radiology-table`, coordinated by `radiology-pipeline` when multistage | frozen claim/evidence/display package and decision receipt |
| Manuscript and scientific review | draft from frozen evidence, polish without scientific drift, verify citations/reporting and close scientific findings | `radiology-writing`, `radiology-polishing`, `radiology-citation`, `radiology-reporting`, scope-aware `radiology-prereview` or `radiology-radiogenomics` review | reviewed manuscript package with traceable open/closed findings |
| Venue, submission and revision | select a verified venue, audit the complete package, adjudicate decisions and verify revised artifacts | `radiology-journal`, `radiology-submission`, `radiology-response` plus affected scientific owners | human-facing submission state and revision-closure receipts; no machine claim of external submission |
| Publication, maintenance, closeout and reuse | preserve authoritative versions, deposits/access, correspondence, corrections, living updates, deployed derivatives, retirement and reusable knowledge | `radiology-pipeline` routes `radiology-submission`, `radiology-data`, `radiology-research-ops`, `radiology-research-integrity`, `radiology-systematic-review`, `radiology-consensus-guideline`, `radiology-dissemination`, `radiology-bibliometrics`, `radiology-translation`, `radiology-innovation-transfer`, `radiology-reproducibility` as applicable | current version/status, accountable owner, next surveillance date and governed closeout/reuse record |

## 2. Cross-lifecycle assurance planes

These capabilities apply wherever their decision becomes material. They are not chronological stages
and must not be postponed merely because they appear below the main lifecycle.

| Assurance plane | Unique decision owners | What the pipeline carries |
|---|---|---|
| clinical context and intended use | `radiology-clinical-domain`; deployment/use evidence: `radiology-translation` | versioned context and use-state handoff |
| image measurement and ground truth | `radiology-acquisition-qc`, `radiology-annotation` | measurement/annotation receipt and deviations |
| data identity, access and lifecycle | `radiology-data`; authorization: `radiology-ethics` | data/access/retention state without inferring approval |
| inference, method defensibility and claim ceiling | `radiology-stats`, `radiology-method-evaluation`, active scientific owner | estimand, unit, comparison/evaluation and claim-state receipts |
| integrity, authorship and disclosure | `radiology-research-integrity` | allegation-neutral evidence and authorized escalation state |
| delivery, roles, resources and change control | `radiology-research-ops` | RACI, readiness, risk/change/deviation and closeout state |
| replay and computational provenance | `radiology-reproducibility`; data authority remains `radiology-data` | replay level, exact bundle and residual boundary |
| PPI, stakeholder participation and equity | study-question/protocol decisions: `radiology-design`; ethics, data, statistics, qualitative, translation, operations, reporting and dissemination retain their bounded decisions | represented groups, authority, protocol impact, equity estimand, unresolved harm/access and next owner |
| reporting and cross-artifact consistency | `radiology-reporting`; source artifact owners retain scientific truth | checklist locations, affected artifacts and unresolved findings |

## 3. Non-linear branches

| Branch | When it can enter | Primary owner and boundary | Return to the main lifecycle |
|---|---|---|---|
| `5F` funding | from question/design through revision, or when an awarded project changes | `radiology-grant` owns live-call, proposal and funder-package decisions; institutional submission and award authority remain human | approved/frozen proposal terms hand to `radiology-research-ops`; scientific changes return to their original owners |
| `5P` scientific presentation and education | from a supplied paper, proposal or any frozen evidence state | `radiology-paper2ppt` owns decks; `radiology-reader` owns source-grounded bilingual reading artifacts; `radiology-figure`/`radiology-table` own standalone evidence carriers | scientific changes return upstream; rendering never validates science |
| evidence-synthesis/guideline | may begin at question formation and continue as a living product | `radiology-systematic-review` owns formal review science; `radiology-consensus-guideline` owns evidence-to-recommendation and consensus process | frozen synthesis/recommendations feed writing, dissemination and living-update routes |
| `5T` clinical translation and deployment | can begin during intended-use design and continues after publication | `radiology-translation`; determinants: `radiology-qualitative-mixed-methods`; economics: `radiology-health-economics`; delivery: `radiology-research-ops` | evidence or workflow changes reopen the applicable design/measurement/analysis decision |
| `5D` dissemination | after a claim-source base is frozen; planning may begin earlier | `radiology-dissemination`; decks and standalone figures retain their owners | derivatives inherit source staleness and update/withdrawal duties |
| `5B` bibliometrics and research-impact assessment | from a frozen corpus, usually during field mapping or after publication | `radiology-bibliometrics`; it does not convert attention metrics into quality or causal impact | dated corpus/metric snapshot returns to strategy or published-lifecycle surveillance |
| `5I` innovation and transfer | before public disclosure and throughout evidence maturation | `radiology-innovation-transfer`; legal, regulatory, ownership and institutional decisions remain external | scientific, deployment, rights or disclosure changes return to their qualified owners |

## 4. D0-D9 to Stage 0-11 crosswalk

The table names the **usual** relationship, not a forced one-to-one sequence. Record both identifiers
when a durable project is in use.

| Stage gate | Usual D-state relationship | Crosswalk rule |
|---|---|---|
| Stage 0 Intake | opens D0-D1 or resumes any D-state | inventory first; do not infer the current decision from a folder name or prior prose |
| Stage 1 Question and novelty | D0 Question, D1 Feasibility and early D2 Assumptions | novelty evidence cannot substitute for an estimand or feasible independent unit |
| Stage 2 Protocol and design | D1-D4, ending in D4 Lock | registration, SAP, validation and measurement decisions are locked before protected outcome/test access |
| Stage 3 Image measurement, data and ground truth | D2-D5 | D2/D3 define validity checks; D4 freezes acceptance rules; D5 records what was actually acquired/accepted |
| Stage 4 Analysis and method evaluation | D3-D7 and may iterate through D8 | execution is D5, evaluation is D6 and scientific interpretation is D7; a D8 refine/pivot can reopen D2-D4 |
| Stage 5 Evidence displays | primarily D7, using locked D5-D6 outputs | display creation exposes evidence; it does not create a new scientific result or gate pass |
| Branch 5F Funding | usually D0-D4; review/resubmission may invoke D8 | proposal claims remain planned unless backed by real evidence; award terms do not replace scientific locks |
| Branch 5P Scientific communication | usually D7-D9; proposal/teaching decks may carry explicitly planned D0-D4 content | audience adaptation cannot upgrade evidence maturity; changes to scientific content return upstream |
| Branch 5T Translation/deployment | can repeat D0-D9 within each bounded use/deployment question | preserve separate technical, clinical, utility, regulatory, economic, implementation and monitoring states |
| Branch 5D Dissemination | usually D7-D9 | every derivative binds a frozen claim/source and inherits staleness |
| Branch 5B Bibliometrics | may inform D0-D2; a completed analysis follows D5-D9 on a frozen corpus | attention/network outputs are new descriptive evidence, not proof of scientific quality or impact |
| Branch 5I Innovation/transfer | may enter D0-D4 before disclosure and D5-D9 as evidence matures | confidentiality/rights/readiness states remain independent of scientific validity |
| Stage 6 Manuscript | D7 from frozen D0-D6 decisions | writing communicates the claim ceiling; it does not silently reopen or repair science |
| Stage 7 Compliance and review | D6-D8 | findings can force evaluate, reinterpret, refine, replicate, pivot or stop; record the reopened D-state |
| Stage 8 Venue and submission | D7-D9 with current venue/package evidence | package completeness is distinct from scientific validity and external human submission |
| Stage 9 Revision | D8 plus any affected D2-D7 state | reopen only the decisions affected by a comment/change, then re-freeze downstream artifacts |
| Stage 10 Research closeout and knowledge reuse | D8-D9 | preserve negative/failure evidence, access constraints, replay status and reusable boundary |
| Stage 11 Published-output lifecycle | repeated D7-D9; material new evidence may reopen D0-D8 | current version/status and authorized correction/update/retirement actions propagate to every derivative |

## 5. Routing rule

1. Locate the request in the lifecycle and identify any applicable assurance plane or branch.
2. Name the open D-state when a scientific decision is required and the Stage gate when a durable
   artifact must be accepted.
3. Select exactly one primary owner through `research-intent-routing.md`.
4. Use collaborators only for separable artifacts; never turn the lifecycle map into a multi-owner
   answer or a mandatory linear conveyor.
5. If an event changes an upstream decision or source version, mark dependents stale and resume from
   the earliest affected D-state/Stage gate.
