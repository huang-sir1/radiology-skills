# Stage gates and handoffs

Use this map to enter, resume, or audit a project. A stage is complete only when its required
artifact exists and its gate has evidence.

## Pipeline map

| Stage | Owner skills | Required artifact | Hard gate |
|---|---|---|---|
| 0 Intake | `radiology-pipeline` | project passport + material inventory | provenance and scope known |
| 1 Question and novelty | `radiology-frontier`, `radiology-search`, `radiology-citation`; formal evidence-synthesis projects: `radiology-systematic-review` | question, gap matrix, verified seed set; or registered/frozen review protocol | contribution is specific and gap is not fabricated; review eligibility/synthesis plan is prespecified |
| 2 Protocol and design | `radiology-design`, `radiology-clinical-domain`, `radiology-acquisition-qc`, `radiology-stats`, `radiology-reporting`; review protocol: `radiology-systematic-review` | protocol/SAP, disease-context lock, task contract, acquisition/reconstruction/QC plan, endpoint, split, sample-size rationale; or review eligibility/extraction/RoB plan | estimand, validation and image-measurement claim locked before modelling; disease/reference/treatment-time assumptions explicit; review protocol precedes screening/synthesis |
| 3 Image measurement, data and ground truth | imaging: `radiology-acquisition-qc`, `radiology-data`, `radiology-annotation`, `radiology-ethics`; mechanism: `radiology-radiogenomics` modality playbooks; evidence synthesis: `radiology-search` + `radiology-systematic-review` | accepted-series/measurement passport, acquisition-QC deviations, cohort/specimen flow, data dictionary, ground-truth/annotation or assay QC, governance; or exact search, deduplication, screening, companion-report and extraction trail | image formation/quantitative transforms/protocol shifts, IDs/labels/masks/specimens/assays/access and biological hierarchy are valid and traceable; review study-family identity and selection are reproducible |
| 4 Analysis and method evaluation | domain execution: `radiology-radiomics`, `radiology-deep-learning`, `radiology-transcriptomics-analysis`; biological/bridge interpretation: `radiology-radiogenomics`; functional validation: `radiology-experiment-design`; evidence synthesis: `radiology-systematic-review`; evaluation: `radiology-method-evaluation`; inference: `radiology-stats` | run/source manifest, results, diagnostics, deviations, experiment/control matrix or extraction/RoB/synthesis record, and parameter/method-evaluation matrix when a configuration, superiority, ablation or robustness claim is material | real independent-unit, protected-test, leakage/batch/composition/spatial/perturbation, control/target-engagement, pooling-feasibility, fair-comparator, freeze and sensitivity gates applicable to the declared analysis pass |
| 5 Evidence displays | `radiology-figure`, `radiology-table` | figure/table set + source-data crosswalk | final-size render and value reconciliation pass |
| 5F Funding branch (when requested) | `radiology-grant` with frozen inputs from question/design/domain/statistics/ethics/data owners | live call and eligibility passport, proposal/aim-evidence contract, criterion findings or mock-panel synthesis, revision-closure ledger | current call applicability is verified; administrative acceptability is distinct from scientific merit; every finding has an evidence anchor and closure condition; no score, preliminary result, eligibility or funding probability is invented |
| 5P Scientific-communication branch (when requested) | `radiology-paper2ppt` with the frozen scientific owner plus `radiology-reader`, `radiology-figure`, `radiology-table` or `radiology-stats` as needed | deck brief, slide map, source/transformation ledger, speaker notes, presentation artifact when requested, and separate scientific/privacy/accessibility/render/rehearsal QA receipts | audience/decision and evidence maturity are explicit; slide claims resolve to frozen or labelled planned evidence; imaging display and PHI gates pass; artifact creation and rehearsal status are reported honestly |
| 5T Clinical-translation/deployment branch (optional, non-linear T0-T6) | `radiology-translation`; economic route `radiology-health-economics`; qualitative determinants `radiology-qualitative-mixed-methods`; site delivery `radiology-research-ops`; replay `radiology-reproducibility` | seven-axis evidence-state card; intended-use/release lock; technical/clinical validation; ethics/regulatory/IT/safety state; site acceptance/silent receipt; active-impact/implementation evidence; HTA/economic brief; production monitoring/change/rollback/retirement contract as applicable | technical performance, clinical validation, utility, regulatory, economic, implementation and monitoring states remain independent; silent deployment cannot prove human interaction; local activation/rollback/retirement require authorized owners |
| 5D Dissemination branch (when requested) | `radiology-dissemination` with scientific owner; decks remain `radiology-paper2ppt` | audience/channel passport, claim-source map, derivative/version/accessibility/privacy review and release/withdrawal plan | every public claim resolves to frozen evidence; uncertainty, authorship, confidentiality, channel limits and derivative staleness stay visible; reach is not impact |
| 5B Bibliometrics and research-impact assessment (when requested) | `radiology-bibliometrics` with identifier/citation support from `radiology-citation` | identity-resolved corpus, source/query/date snapshot, normalized indicator matrix, uncertainty/gaming and responsible-interpretation statement | field/time/document-type and database coverage are explicit; author/institution disambiguation passes; metrics do not become quality, causality or individual evaluation by themselves |
| 5I Innovation and transfer branch (when requested) | `radiology-innovation-transfer` with `radiology-translation`, `radiology-research-integrity`, data/legal/institutional owners | disclosure/state passport, prior-art/search handoff, inventorship/evidence boundary, IP/data/software rights map and non-confidential transfer brief | public disclosure, contributor versus inventor, ownership/licensing, confidentiality, clinical/regulatory and institutional-authority questions remain separated; the skill never gives a legal clearance opinion |
| 6 Manuscript | mechanism truth: `radiology-radiogenomics`; evidence synthesis: `radiology-systematic-review: writing-handoff`; parameter/method evidence: `radiology-method-evaluation`; venue prose: `radiology-writing`; then `radiology-polishing`/`radiology-citation` | mechanism-bearing scope: validated scientific handoff packet; imaging-only: frozen claim register or compatible packet; evidence synthesis: frozen protocol/search/flow/extraction/RoB/synthesis/certainty packet; plus applicable evaluation-placement map, manuscript and Claim-ID drift ledger | contribution/results/citations, evaluation evidence states and immutable claim ceiling remain aligned |
| 7 Compliance and review | reporting plus scope route: imaging `radiology-prereview`; mechanism `radiology-radiogenomics: manuscript-review`; combined uses both; evidence synthesis uses `radiology-systematic-review` route audit before whole-manuscript prereview; focused parameter/method findings retain `radiology-method-evaluation` criteria | filled checklists + canonical scientific-prereview receipt containing digest-bound findings/closure criteria | no required open finding, unresolved P0/P1, unsupported submission or method claim, failed mechanism/bridge gate, or unreproducible review selection/synthesis |
| 8 Venue and submission | `radiology-journal`, `radiology-submission` | verified venue profile + upload manifest | current guide and package audit pass |
| 9 Revision | `radiology-response` plus affected owners | source prereview receipt + response ledger + revised artifacts + post-revision prereview receipt + canonical response receipt | every promised change is independently traceable and no `NOT_VERIFIED` item is hidden by response prose |
| 10 Research closeout and knowledge reuse | `radiology-pipeline`, `radiology-reproducibility`, `radiology-data` plus domain owners | replay-level/closeout packet, final decision log, negative/failure index, versioned artifact manifest and reuse memo | another authorized team can identify what ran and what failed; any replay level is evidenced; future users distinguish reusable method knowledge from cohort-specific findings; access and claim boundaries remain explicit |
| 11 Published-output lifecycle | `radiology-pipeline` routes unique owners: `radiology-submission`, `radiology-data`, `radiology-research-ops`, `radiology-research-integrity`, `radiology-systematic-review`, `radiology-consensus-guideline`, `radiology-dissemination`, `radiology-bibliometrics`, `radiology-translation` | version/identifier and deposit receipt, request/correspondence ledger, correction/retraction/update state, derivative-impact snapshots, deployment linkage and retirement record | version and status are current; known errors/staleness trigger authorized action; public-access, metric or deployment signals never substitute for scientific validity; superseded derivatives are updated or withdrawn |

> Stage-3 image-measurement specs live in `radiology-acquisition-qc`; data specs live in radiology-data: data dictionary → `radiology-data/data-dictionary-spec.md`; cohort-flow counts / ID reconciliation → `radiology-data/cohort-assembly-and-id-reconciliation.md`; outcome & follow-up fields → `radiology-data/outcome-and-followup-data.md`. Underpowered designs at stage 2 → `underpowered-fallback.md`.

For mechanism-only and imaging-mechanism routing, load
`scientific-scope-and-handoff-routing.md`. Validate the immutable packet with
`radiology-radiogenomics/scripts/validate_scientific_handoff.py --require-ready` before Stage 6.
The pipeline validator repeats that semantic validation and separately checks
`canonical_packet_sha256` and `packet_file_sha256`; neither digest substitutes for the other.
It also requires every packet source artifact and Claim ID to resolve to the project artifact and
claim registries with the same digests and immutable fields. A packet-internal registry cannot
replace those project foreign keys.
For `evidence-synthesis`, the same project passport is valid without a mechanism packet or matched
biological intersection. Record `study family` as the independent synthesis unit, the review ->
study family -> report -> effect-row hierarchy, and freeze protocol/search/screening/extraction/
RoB/synthesis/certainty artifacts in the common manifest and claim registry.

The 5T branch coordinates decisions rather than imposing one regulatory sequence. T0 intended-use,
T1 validation/transport, T2 governance readiness, T3 site acceptance/silent, T4 bounded active impact,
T5 HTA/procurement/scale and T6 monitoring/change/retirement may partly overlap. Every handoff still
preserves the seven independent evidence axes and qualified local authority.

## Resume logic

1. Read `project_state.json` and `artifact_manifest.csv`.
2. Confirm that the stated stage matches actual artifacts.
3. Find upstream artifacts changed since their dependent outputs were verified.
4. Mark affected downstream artifacts `stale`, including proposal/review artifacts and scientific
   presentation maps/decks/notes/ledgers, dissemination derivatives, bibliometric snapshots,
   innovation-transfer briefs, deployment contracts and published-version records when their call,
   design, evidence, status or canonical values changed.
5. Resume from the earliest failed, incomplete, or stale gate.

Do not restart a valid project merely because the current conversation lacks prior context.

After every state-changing checkpoint, run
`compute_project_state_digests.py project_state.json --write`. `analysis_lock_digest` binds only the
analysis-lock object; `modality_role_digest` binds schema/study/scope and the four role groups; and
`project_state_digest` binds the full semantic state while excluding only itself. None is the
physical JSON file SHA-256, and none substitutes for another.
Schema 1.2 must use the explicit
`compute_project_state_digests.py project_state.json --write --migrate-to-current` route. Do not
change only the version string or ask the legacy analysis-lock command to infer a migration.

## Gate record

For each gate record:

| Field | Requirement |
|---|---|
| Gate ID and stage | Stable name |
| Status | `PASS`, `CONDITIONAL`, `FAIL`, `NOT_APPLICABLE` |
| Evidence | Artifact ID/path and exact location |
| Checked by | Responsible skill or human reviewer |
| Checked on | Date/time and relevant version |
| Residual risk | What remains true even after pass |
| Next action | Concrete fix and owner if not pass |

`CONDITIONAL` never means "probably fine." State the condition, claim boundary, and venue risk.

## Handoff acceptance

A downstream stage may reject a handoff when:

- required fields or source artifacts are absent;
- the artifact uses a different cohort, endpoint, timepoint, or model name;
- data provenance is unclear;
- a result is reported without uncertainty or source location;
- the upstream artifact changed after verification;
- simulated and real evidence are mixed without explicit separation.

Return `HANDOFF_INCOMPLETE` with missing fields and the responsible upstream owner. Do not repair
scientific facts by guessing downstream.

## Journal-guide currency gate

Before final formatting or submission, record the exact author-guide source, article type,
version/update date if shown, and date accessed. Values remembered from prior submissions are
working defaults only. Mark unverified limits `VERIFY_FROM_CURRENT_GUIDE` and block final package
approval until resolved.
