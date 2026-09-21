# Project passport and registries

Use one project record to keep every specialist module synchronized when the user has requested or
authorized a durable filesystem project. The record is lightweight: one JSON passport plus five CSV
registries. Store it under a project-owned `research_record/` directory unless the user chooses
another location. For advisory, audit-only or tutoring work without requested edits, keep a proposed
passport update in the response and do not initialize, migrate or update files.

## Required files

| File | Purpose | Stable IDs |
|---|---|---|
| `project_state.json` | Study identity, design locks, provenance, stages, gate status | study ID, stage names |
| `reported_values.csv` | Canonical numerical facts reused in prose, figures, and tables | `VAL-###` |
| `claim_register.csv` | Claim to evidence/citation/value/location map | `CLM-###` |
| `display_register.csv` | Figure/table/panel to claim/value/source-data map | `FIG-##`, `TAB-##`, `SUP-##` |
| `artifact_manifest.csv` | Versioned files and their producer/input lineage | `ART-###` |
| `decision_log.csv` | Pre-specified and later decisions, with rationale and affected artifacts | `DEC-###` |

Stage-applicable research-decision artifacts—question/estimand card, assumption register,
experiment/analysis plan, iteration/test-access log, parameter/method-evaluation matrix,
negative/failure register and reproducibility/knowledge-reuse closeout—are registered in
`artifact_manifest.csv`. Use the
[research-decision packet template](../assets/research-decision-packet.template.md) when one durable packet
is preferable. They are not required for a one-off bounded request, but a full project cannot claim
the corresponding D0-D9 decision state without the artifact and evidence gate.

Full projects also register applicable governance satellites rather than expanding the core passport
into a god schema: team charter/RACI, authorship/CRediT ledger, AI-use ledger, integrity evidence
manifest, DMP/DMS and amendments, PPI/stakeholder/equity ledger, operations/readiness/risk logs,
reproducibility/replay receipt, dissemination receipt, bibliometric corpus/analysis passport and
innovation-transfer handoff. Each remains owned by its specialist and carries version, digest,
authority/evidence state, affected decisions/Claim IDs and staleness. See
`responsible-research-governance-routing.md`.

When present, also register grant artifacts (call/eligibility passport, proposal, criterion findings,
mock-panel synthesis and revision ledger) and scientific-presentation artifacts (deck brief, slide
map, source/transformation ledger, speaker notes, deck file and distinct QA receipts). A `.pptx`
file or polished proposal is not self-validating evidence.

For `evidence-synthesis`, the same manifest must also bind the frozen protocol/registration and
amendments, exact searches and dates, screening/conflict log, study-family/companion-report map,
effect-row ledger, risk-of-bias/applicability judgments, statistical brief and verified synthesis
code/results, certainty assessment and review claim ledger. A protocol, planned model or
author-reported forest plot is not a verified synthesis artifact.

The explicit template index is:

- core state and provenance: [project state](../assets/project_state.template.json),
  [reported values](../assets/reported_values.template.csv),
  [claim register](../assets/claim_register.template.csv),
  [display register](../assets/display_register.template.csv),
  [artifact manifest](../assets/artifact_manifest.template.csv) and
  [decision log](../assets/decision_log.template.csv);
- applicable governance satellites: [AI-use ledger](../assets/ai_use_ledger.template.csv),
  [stakeholder decision ledger](../assets/stakeholder_decision_ledger.template.csv) and
  [team charter](../assets/team_charter.template.md); and
- the optional [research-decision packet](../assets/research-decision-packet.template.md).

Initialize core project files with `../scripts/init_research_project.py` only when a filesystem
project is requested and file creation is authorized. Governance satellites are activated only when
applicable; blank templates do not prove that governance work occurred.
After any intentional scope, modality-role, analysis-lock, stage, handoff or other project-state
change, regenerate and verify all canonical receipts with
`../scripts/compute_project_state_digests.py project_state.json --write`. When an adjacent
`artifact_manifest.csv` exists, the command must find exactly one row bound to that project-state
path and updates its physical file SHA-256 in the same operation; a missing or ambiguous binding
fails closed before the state write. A stale top-level or manifest digest is an error, not a second
source of truth.

## Passport minimum

`project_state.json` should identify:

- `study_id`, project title, project owner, and schema version.
- data provenance: `real`, `simulated`, or `mixed`; and `teaching_only`.
- `study_scope` (`imaging-only`, `mechanism-only`, `imaging-mechanism`, or `evidence-synthesis`) plus
  active, external, generated/predicted and proposed-validation modality roles. An
  `evidence-synthesis` project may leave active modalities empty for a cross-domain review, or use
  them only to name included evidence domains; generated/proposed roles are not review evidence.
- independent unit, evidence/biological hierarchy and every usable matched intersection needed by
  a claim; cells, spots, sections, ROIs and repeated measures remain nested under the real
  biological unit. For `evidence-synthesis`, use study family/report/effect-row hierarchy, deduplicate
  companion reports and record dependence/overlap instead of inventing a matched biological cohort.
- target journal family and the exact guide source/version/date last verified.
- disease/population, modality, endpoint/estimand, unit of analysis, cohort roles, centers,
  dates, event counts where relevant, primary model, validation design, and reporting stack.
- current stage, stage status, unresolved author facts, and hard-gate outcomes.
- software/runtime and analysis lock information sufficient to identify the run, plus the canonical
  `analysis_lock_digest` generated from the complete `analysis_lock` object.
- canonical `modality_role_digest` generated from schema version, study ID, study scope and the four
  sorted modality-role lists; and canonical `project_state_digest` generated from the entire project
  state after removing only `project_state_digest` itself.
- for mechanism-only/imaging-mechanism work, the validated scientific-handoff packet path, separate
  canonical semantic digest and physical-file SHA-256, source-manifest digest and claim-register
  digest before writing, review, response or submission release; imaging-only may instead remain on
  its frozen project claim register unless it deliberately uses the compatible packet contract.
  Evidence-synthesis projects instead freeze protocol, searches, eligibility decisions, extraction,
  risk-of-bias/applicability, synthesis code/results and certainty/claim records under the project
  artifact and claim registries; they do not require a radiogenomics handoff unless a separate
  mechanism-bearing primary-data scope is actually added.

Unknown facts stay `null`, empty, or in `unresolved_items`; never fill them from memory.

Schema `1.3` is the first state schema that produces all three canonical receipts. Schemas 1.0-1.2
remain inspectable in working mode but are migration-blocked in submission mode.
For a structurally compatible 1.2 passport, migrate explicitly and atomically with
`compute_project_state_digests.py project_state.json --write --migrate-to-current`; the command
changes the schema to 1.3 before computing receipts. It refuses an implicit 1.2 write. Schemas 1.0
and 1.1 require manual migration because their scientific-handoff digest fields do not have the
same canonical-versus-physical meaning; rebuild and validate that handoff before selecting 1.3.

## Canonical value registry

Every submission-facing number gets one value key. A value row should include:

| Field | Meaning |
|---|---|
| `value_id` | Stable key such as `VAL-017` |
| `metric` | `development_n`, `external_auc`, `cox_hr_age`, `events_3y`, etc. |
| `value`, `unit`, `precision` | Exact stored representation and display precision |
| `cohort`, `endpoint`, `timepoint` | Context that prevents cross-cohort copying |
| `ci_lower`, `ci_upper`, `p_value` | When applicable; do not detach CI from estimate |
| `source_artifact`, `source_location` | File/table/object and exact location |
| `verified_status` | `verified`, `pending`, `superseded`, or `simulated` |

Do not duplicate the same statistic with different rounding. Keep exact source precision in the
registry and define display precision at export.

## Claim register

Each major claim records:

- claim type: background, novelty, methods, primary result, secondary result, comparison,
  clinical utility, biological interpretation, limitation, or conclusion.
- evidence artifacts and value keys.
- verified citation IDs for external claims.
- status: `supported`, `partial`, `unsupported`, `pending`, or `simulated`.
- primary evidence state, modality subtype, claim-link status, independent unit/matched n,
  effect/uncertainty, claim branch, branch verdict, maximum wording, protected placement and residual
  boundary. Keep these separate from the generic registry status.
- manuscript locations and submission eligibility.

A major result or conclusion claim without evidence/value keys is a blocker. A novelty claim
without a high-recall literature check remains `pending` or `partial`.

### Evidence-synthesis claim and hierarchy contract

For `study_scope=evidence-synthesis`:

- use `primary_evidence_state=synthesized` for a review-level conclusion produced from the frozen
  eligible corpus and synthesis route. Do not relabel it `measured`, and do not use `synthesized`
  for a protocol, search result, author-reported analysis or an unverified forest plot;
- set `independent_unit=study family`. Use `matched_n=not-applicable` unless the claim truly concerns
  a matched primary-data cohort. Store included study-family, report and effect-row counts as
  canonical value keys rather than as matched patient/sample n;
- set `modality_subtype` to the declared review route. Use `claim_link_status=direct` only when the
  claim resolves to frozen eligible effect/narrative rows and a verified synthesis artifact;
- bind `evidence_artifacts` to the protocol/search/selection/extraction/RoB/synthesis/certainty
  chain. `effect_uncertainty` records the compatible effect estimate and interval plus material
  heterogeneity/certainty, or the bounded narrative range and why pooling was not defensible;
- never count companion publications, arms, outcomes, time points, subgroups or effect rows as
  independent studies. Any unresolved overlap or dependence lowers the branch verdict or stops
  pooling.

The **study-family ledger** is a versioned artifact with at least:

`study_family_id | report_id | companion_relation | cohort/setting/time | population/design |
overlap_group | eligibility_status/reason | source_locator | verification_state`.

The **effect-row ledger** is a versioned artifact with at least:

`effect_row_id | study_family_id | report_id | outcome/estimand | horizon | contrast |
effect_measure | estimate/SE-or-CI | analysis_population | adjustment | dependence_cluster |
RoB/applicability | source_locator | verification_state | synthesis_eligibility/exclusion_reason`.

Every effect row resolves to exactly one study family and source report. Multiple rows from one
family retain a dependence cluster and cannot silently increase the synthesis n. Narrative rows use
the same identifiers and evidence anchors even when no numeric effect is available.

## Display register

Every figure, panel, and table records:

- the claim IDs it supports;
- value keys shown or summarized;
- source-data path and transformation;
- output file(s), caption/footnote status, main/supplement role, and render QA status.

If a panel supports no claim, remove it, combine it, or move it to exploratory/supplementary
material. If a main claim has no display or text evidence, flag it.

## Staleness rule

Any change to the active call/criteria, cohort membership, endpoint definition, split,
preprocessing, model, statistical method, canonical value, claim ceiling or frozen design makes
dependent grant proposals/review receipts, scientific deck briefs/maps/decks/notes/source ledgers,
figures, tables, prose, citations, and submission files potentially stale. Mark those artifacts
`stale` in `artifact_manifest.csv` and re-run the responsible gate. Do not rely on file modification
time alone; record the decision explicitly.

The same applies to a material change in authorship/contribution, sponsor/COI, AI-use authorization,
data-sharing/retention authority, stakeholder/equity decision, implementation context, regulatory or
economic policy snapshot, publication correction/retraction status, dissemination claim or IP/public-
disclosure boundary. Re-run only the affected specialist gates, then propagate the new receipts.

Each artifact row carries its SHA-256 plus source-input hashes or a source-manifest digest. The
validator reports a detached fingerprint for all six registry files; the artifact manifest does not
self-certify its own hash.

## Handoff update

After each specialist module returns, append a compact update:

```text
Producer skill:
Inputs consumed (artifact IDs/versions):
Artifacts produced or changed:
Values added/superseded:
Claims affected:
Displays affected:
Decisions locked or changed:
Open issues:
Receiving owner:
Recommended next gate:
Claim boundary / prohibited upgrade:
```
