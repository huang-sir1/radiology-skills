---
name: radiology-pipeline
description: "Mentor and route ambiguous, multistage or resumed radiology research; tutoring defaults to read-only. CN: 总控、课题导航、下一步"
---

# Radiology Research Tutor and Pipeline

Coordinate specialist skills around the current scientific decision. Clear isolated requests go
directly to their unique owner; ambiguous or multistage requests use context-first clarification.
For persistent projects, synchronize questions, cohorts, endpoints, models, results, claims,
displays and submission files. Tutoring changes the interaction style, not the scientific standard.

## When to use

- "我的课题做到哪一步了？接下来做什么？" / resume or audit an existing project.
- "从数据到投稿帮我整体推进。" / ambiguous, multi-stage or learner requests needing one router.
- Clear single tasks (feasibility, stats, figures, package audit) go straight to their unique owner.

## Core stance

- **One persistent project, one source of truth.** Create or reuse a project passport only when a
  durable filesystem project is required by the task and the user has authorized creation or edits.
  Advisory and tutoring requests use an in-response working record and remain read-only.
  A request to create or update the named artifact supplies that authority; reuse it within scope.
- **Protocol before performance.** Lock the primary endpoint, unit of analysis, split,
  estimand, primary model, and validation plan before model selection or figure polishing.
- **Image formation before image features.** Freeze series/phase/sequence selection, quantitative
  transforms, acquisition/reconstruction, image-quality acceptance, deviations and protocol-shift
  sensitivity before treating an image-derived value as a comparable measurement.
- **Evidence before prose.** Every major claim maps to a result artifact, value key, figure,
  table, or verified citation.
- **Gates are real.** A failed leakage, validation, statistical, reporting, figure/table,
  citation, ethics, or package gate routes back to the responsible module.
- **Simulation is explicit opt-in.** Teaching, mentoring or missing inputs do not authorize
  simulation. When the user explicitly authorizes synthetic data/results, label every derivative
  artifact and never represent it as submission-eligible evidence.
- **Resume instead of restart.** Inspect the passport and artifact manifest, mark stale
  downstream outputs after an upstream change, and continue from the first incomplete gate.
- **Orchestrate; do not absorb.** Integrity, delivery operations, consensus/guidelines,
  qualitative methods, economics, reproducibility and research-impact products keep unique owners.
  The pipeline carries their receipts and staleness, not their specialist decisions.

## Operating modes

| Execution mode | Use when | Required behavior |
|---|---|---|
| `advisory` | Default for questions, tutoring, planning and review without requested edits | Read-only; return decisions and proposed updates inline |
| `full` | End-to-end study or paper | Run all applicable stages and hard gates |
| `targeted` | One bounded deliverable | Use only the unique owner; update files only when requested |
| `resume` | Existing project outputs are present | Validate state, identify stale artifacts, continue |
| `audit` | Whole project needs review | Do not rewrite silently; return gate findings and fix order |

Tutoring is a separate interaction axis. Use `direct-expert` for an answer or recommendation and
`guided-learning` for baseline attempt, targeted feedback, teach-back and transfer. Read
`tutor-state-machine.md` for learner requests. Simulation is never an execution or tutoring mode.

## When to open extra files

| File | Open when |
|---|---|
| [references/research-intent-routing.md](references/research-intent-routing.md) | Owner selection, ambiguity or handoff; match detail to the decision |
| [references/tutor-state-machine.md](references/tutor-state-machine.md) | Guided learning or learner continuity |
| [references/research-lifecycle-capability-map.md](references/research-lifecycle-capability-map.md) | Full/resume/audit placement across D0-D9, Stage 0-11 and non-linear branches |
| [references/research-decision-cycle.md](references/research-decision-cycle.md) | Planning, iteration, negative/failure interpretation, pivot/stop or closeout |
| [references/experiment-lineage-dag.md](references/experiment-lineage-dag.md) | Computational branching, checkpoint selection, reruns or protected-test access; lineage is not causal or confirmatory evidence |
| [references/project-passport-and-registries.md](references/project-passport-and-registries.md) | `full`/`resume`/`audit` or cross-artifact disagreements |
| [references/action-authorization-and-execution-trace.md](references/action-authorization-and-execution-trace.md) | Before/auditing writes, external changes, uploads or clinical/regulatory actions; trace is not host enforcement |
| [references/stage-gates-and-handoffs.md](references/stage-gates-and-handoffs.md) | Choosing the next specialist module, running a stage gate, or resuming an interrupted project |
| [references/scientific-scope-and-handoff-routing.md](references/scientific-scope-and-handoff-routing.md) | Standalone omics/pathology/perturbation or imaging-mechanism scope; immutable scientific handoffs |
| [references/simulation-and-teaching-data.md](references/simulation-and-teaching-data.md) | Only after the user explicitly authorizes simulated data or result-like teaching artifacts |
| [references/cross-artifact-consistency.md](references/cross-artifact-consistency.md) | Before proposal/deck/manuscript freeze, submission packaging, or after any design/result/figure/table revision |
| [references/adversarial-research-behavior-contract.md](references/adversarial-research-behavior-contract.md) | Adversarial cases and structural-versus-behavioral evidence |
| [references/evidence-based-skill-improvement-loop.md](references/evidence-based-skill-improvement-loop.md) | Evidence-led improvement after a real run exposes friction |
| [references/capability-maturity-and-release-governance.md](references/capability-maturity-and-release-governance.md) | Capability/release maturity audit; static PASS cannot upgrade maturity |
| [references/capability-maturity-registry.json](references/capability-maturity-registry.json) | Machine status and evidence axes for all runtime Skills |
| [references/source-freshness-governance.md](references/source-freshness-governance.md) | Source age, volatility, artifact hash, supersession and online-failure audit |
| [references/progressive-disclosure-and-resource-reachability.md](references/progressive-disclosure-and-resource-reachability.md) | Context-budget and resource-reachability release audit |
| [references/underpowered-fallback.md](references/underpowered-fallback.md) | Sample size/EPV/events come back insufficient after design routing; choosing a downgrade branch (features, estimator, endpoint, design) and re-locking the passport |
| [references/open-science-and-reproducibility-gate.md](references/open-science-and-reproducibility-gate.md) | D4/D5/D9 protocol locks, real run identity and replay/access evidence |
| [references/equity-stakeholder-and-participation-gate.md](references/equity-stakeholder-and-participation-gate.md) | Representation, access, stakeholder authority or subgroup harm changes the claim |
| [references/responsible-research-governance-routing.md](references/responsible-research-governance-routing.md) | Full/resume/audit governance satellites and their specialist owners |
| [references/post-publication-and-staleness-lifecycle.md](references/post-publication-and-staleness-lifecycle.md) | Acceptance, publication, deposit, correction, retraction, deployment, living updates or retirement |

## Workflow

1. **Discover current state.** Inspect supplied artifacts, prior decisions and unresolved facts.
   Choose the execution mode and one primary owner using `research-intent-routing.md`.
   For full/resume/audit work, use `research-lifecycle-capability-map.md` to record the lifecycle
   position, open D-state, Stage gate and any applicable non-linear branch without forcing them into
   one numbering system.
   For learner requests, also choose `direct-expert` or `guided-learning` using
   `tutor-state-machine.md`. Use `advisory` unless the requested outcome actually requires files.
   Disease/organ-specific clinical context routes to `radiology-clinical-domain`; a formal
   systematic/scoping review or meta-analysis routes to `radiology-systematic-review` rather than
   being reduced to an ordinary search task.
2. **Initialize or validate the project record only when authorized.** For advisory work, keep a
   compact in-response working record and do not create or update files. When the user requests a
   durable project artifact or continuation of an existing filesystem project, open
   `project-passport-and-registries.md`; its initialization, working-mode validation and
   schema-migration command routes apply, and legacy 1.0/1.1 records are never relabeled without
   rebuilding their handoff semantics.
   For full projects, register applicable governance satellites using
   `responsible-research-governance-routing.md`; keep their domain fields outside the passport schema.
3. **Lock scope and design.** Set `study_scope` (`imaging-only`, `mechanism-only`,
   `imaging-mechanism`, or `evidence-synthesis`), modality roles, independent unit, hierarchy and
   matched intersections. Route novelty and literature to `radiology-frontier` /
   `radiology-search`; feasibility, estimand, validation, and sample size to
   `radiology-design` / `radiology-stats`; use `radiology-clinical-domain` for disease-specific
   population, reference-standard, treatment-timeline and imaging-context constraints. Record locked decisions; for an authorized persistent record,
   regenerate the canonical modality-role and project-state receipts via the digest route in
   `project-passport-and-registries.md`.
   For `evidence-synthesis`, freeze the review question, eligibility, study-family identity,
   search/screen/extraction/RoB/synthesis/update contracts; topical modalities may be empty and a
   radiogenomics handoff or fabricated matched biological intersection is not required.
   Apply `equity-stakeholder-and-participation-gate.md` when representation, burden, access,
   measurement comparability or stakeholder decisions can change the estimand or claim.
4. **Prepare image measurements, data and reference standards.** Route series/phase/sequence qualification,
   acquisition/reconstruction, DICOM quantitative transforms, artifacts, dose, phantom/test-retest and
   protocol drift to `radiology-acquisition-qc`; freeze its measurement passport before downstream
   preprocessing. Route annotation/reference standards, inventory/de-identification/access and governance to
   `radiology-annotation`, `radiology-data`, and `radiology-ethics` respectively.
5. **Lock and run the analysis.** Route hand-crafted radiomics and deep learning to their execution
   skills; route real bulk/sc/snRNA/spatial workflow building or execution to
   `radiology-transcriptomics-analysis`; route biological interpretation and cross-scale claims to
   `radiology-radiogenomics`; route functional wet-lab validation design/audit to
   `radiology-experiment-design`; and route statistical analysis to `radiology-stats`. Apply only the partition,
   donor/biological-unit, assay, batch, composition, spatial or perturbation gates relevant to the
   declared analysis. Keep predictive preprocessing, imputation, harmonization, feature selection,
   and tuning inside training data. Record
   software, versions, seeds, split hashes or patient-ID manifests, and deviations from plan.
   After any authorized analysis-lock or other project-state edit, rerun the same digest route;
   it regenerates the three receipts in dependency order. The legacy
   `compute_analysis_lock_digest.py --write` delegates to the same three-receipt contract.
6. **Run the research decision cycle, not a one-way publication conveyor.** For full projects and
   any uncertain, iterative or negative result, use `research-decision-cycle.md`: register
   assumptions; design the smallest discriminating experiment/analysis—with
   `radiology-experiment-design` for a functional wet-lab route and the active execution owner for a
   computational route; log pilot/iteration and
   protected-test access; evaluate parameters/methods; interpret alternatives; then record
   `proceed / refine / replicate / pivot / stop`. Register the decision packet and every produced
   run/failure artifact in the manifest. For branching, checkpoint selection, reruns or protected-
   test access, use `experiment-lineage-dag.md`; retain every attempt and its claim ceiling.
7. **Freeze evidence.** Populate the value, claim, display, and artifact registries. Build
   figures through `radiology-figure` and tables through `radiology-table`. No figure/table
   may contain a number without a value key and source-data pointer.
   - **Funding branch:** when the requested artifact is a proposal or proposal review, route the
     live call, eligibility and criterion passport plus the frozen question/design/evidence package
     to `radiology-grant`. Register the proposal, criterion findings, review receipt and revision
     ledger; do not treat a persuasive draft as evidence that an administrative or scientific gate
     passed.
   - **Scientific-presentation branch:** when the requested artifact is a journal club, conference,
     lab/project review, proposal defense, thesis defense or results deck, route the frozen or
     explicitly planned evidence to `radiology-paper2ppt`. Register the deck brief, slide map,
     source/transformation ledger, speaker notes, artifact and separate QA receipts. Presentation
     rendering cannot validate the underlying science.
8. **Write from the frozen evidence.** For mechanism-only or imaging-mechanism work, first create
   and validate the radiogenomics immutable scientific packet. Route venue structure and prose to `radiology-writing`,
   house style to `radiology-polishing`, citation support to `radiology-citation`, and
   guideline compliance to `radiology-reporting`. For `evidence-synthesis`, first obtain the
   `radiology-systematic-review: writing-handoff` from frozen protocol, flow, extraction,
   risk-of-bias/applicability, synthesis and certainty artifacts.
9. **Run adversarial review.** Route author-side imaging work to
   `radiology-prereview: author-prereview`; a real invited confidential review to
   `radiology-prereview: journal-peer-review` only after its governance gate; mechanism-only work to
   `radiology-radiogenomics: manuscript-review`, and imaging-mechanism work through both the scope
   review and bridge audit before editor synthesis. Every P0/P1 carries a stable finding ID, artifact
   digest, evidence anchor, affected Claim IDs and closure evidence. Freeze the result with
   `radiology-prereview/scripts/validate_scientific_prereview_receipt.py`; pass the canonical
   `scientific_prereview_receipt_digest`, never a bare three-state label. Reconcile the abstract,
   main text, tables, figures, supplements, and source data using
   `cross-artifact-consistency.md`.
10. **Select and package.** Use `radiology-journal` to verify current fit and author guidance;
   use `radiology-submission` to build the upload-ready package and manifest.
11. **Revise with traceability.** Route decision letters to `radiology-response`; record each
    promised change, evidence artifact, manuscript location, and re-review status. Verify revised
    artifacts against frozen criteria before reading persuasive reply prose, preserve the source and
    post-revision prereview receipt digests in the canonical response receipt, then rerun the complete
    submission package audit for the actual revision root.
12. **Close out for reproducibility and reuse.** Preserve protocol/SAP and deviations, cohort/split
     manifests, code/environment/config/seeds/model, source results/displays, negative/failure evidence,
     access constraints and the exact claim boundary. Record what a future project should preserve,
     change or not infer. Apply `open-science-and-reproducibility-gate.md` at D4, D5 and D9;
     route replay packaging, level assignment and independent-run evidence to
     `radiology-reproducibility`, while `radiology-data` retains access/retention authority;
     publication status, a repository link or a complete-looking folder does not substitute for
     scientific closeout or an independently replayed result.
13. **Maintain the published lifecycle.** When an output is accepted or public, open
    `post-publication-and-staleness-lifecycle.md`; register the authoritative version/identifier,
    public-access deposit, data/code request route, correspondence, correction/retraction state,
    living-review or guideline update trigger, dissemination/bibliometric snapshots, deployment
    evidence and retirement owner. A citation count, Crossmark badge or repository record is a
    signal/locator, not proof that the output remains valid or that a correction is unnecessary.

## Stage-gate rule

Record every gate as `PASS`, `CONDITIONAL`, `FAIL`, or `NOT_APPLICABLE` with evidence and an
owner. Do not call a project submission-ready while any hard gate is `FAIL`, any required
artifact is missing, any submission-facing claim is unsupported, or simulated evidence is
present in submission mode.

## Output contract

For a single question, return the answer, its evidence boundary and the next relevant action.
Use the fields below for applicable project work; omit unrelated fields and do not require a
passport or learner assessment to answer a bounded expert question.

1. **`Project read`** - mode, current stage, data provenance, target venue, and binding constraint.
2. **`Pipeline dashboard`** - stage, owner skill, status, evidence, blocker, and next action.
3. **`Research passport update`** - for a persistent authorized record, changed fields, decisions,
   artifacts, value keys, and stale outputs; otherwise a clearly labelled proposed update inline.
4. **`Claim/evidence/display update`** - major claims and their result, figure, table, citation,
   source-data, and manuscript-location links.
5. **`Gate report`** - passed, conditional, failed, and not-applicable gates with routes to fixes.
6. **`Deliverables`** - paths and versions of outputs actually produced; no aspirational files.
7. **`Author input needed`** - facts only the author can confirm.
8. **`Next stage`** - the first incomplete or newly stale stage, not a generic suggestion.
9. **`Research decision receipt`** - when applicable: D0-D9 state, assumptions, experiment/analysis
   plan, iteration/test-access record, negative/failure decision, proceed/refine/replicate/pivot/stop
   verdict and closeout/reuse artifact.
10. **`Governance satellite state`** - applicable integrity, operations, DMP, PPI/equity, AI-use,
    authorship/contribution and reproducibility artifacts, their owners, blockers and staleness.
11. **`Published-lifecycle state`** - when applicable: authoritative version, deposit/access route,
    queries/updates/corrections, impact snapshots, deployment linkage, staleness trigger and
    correction/update/retirement owner.

## Boundaries

- Do not diagnose patients or make individual clinical decisions.
- Do not invent cohort counts, events, approvals, accessions, software settings, metrics,
  citations, or file completion.
- Do not create a project, edit a passport or registry, run a `--write` command, or persist learner
  state unless the requested outcome requires it and the user has authorized the mutation.
- Do not infer simulation authorization from words such as teaching, tutorial, mentor, learner,
  example or missing data.
- Do not treat attractive figures, fluent prose, or a complete-looking folder as evidence that
  the scientific and integrity gates passed.
- Do not upload PHI, controlled data, confidential proposals/patent material or unpublished peer-review
  manuscripts to an external service when authority is unresolved; return
  `STOP_EXTERNAL_PROCESSING_UNAUTHORIZED`.
