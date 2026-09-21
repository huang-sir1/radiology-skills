# Peer-skill architecture provenance and standalone-release boundary

This note records structural influences on the router. It is not a scientific evidence source and
must never be cited to support a biomedical claim.

## Relationship contract

Academic Research Skills/ARS-Codex, Nature Skills and `radiology-skills` are independent peer
products. None is the parent, child, upstream controller or required runtime dependency of another.
During product development, the peer skills may be used as additional working lenses and their
reviewable design patterns may be adapted. The released radiology product must nevertheless execute
its complete domain workflow through its own `radiology-*` modules.

Consequently:

- the table below records development-time design provenance, not an installation dependency list;
- external peer skill names must not appear in runtime routing, required handoffs or output contracts;
- a user may independently invoke a peer skill as a second opinion, but its absence cannot block a
  radiology workflow and its output cannot silently override the radiology evidence ledger;
- borrowed patterns are rewritten for imaging, radiomics, bulk RNA, sc/snRNA, spatial, pathology,
  perturbation and imaging–mechanism use, then tested against local evidence and route cases;
- scientific claims remain grounded in primary literature, user artifacts and official journal or
  reporting guidance—not in the architecture of any skill package.

## Snapshot inspected on 2026-08-22

| Source | Inspected distribution | Snapshot | Patterns adapted |
|---|---|---|---|
| [Academic Research Skills](https://github.com/Imbad0202/academic-research-skills) and [ARS-Codex](https://github.com/Imbad0202/academic-research-skills-codex) | ARS-Codex 0.1.26, vendoring ARS suite 3.21.0 | Codex repository `main` commit `d5e66fb0d9e4a5bc44f26e9a619fa0e4455ba79c`; vendored ARS commit `2b639c12ee4e7c694a32336cc59dc2616e0d89fe` | thin root router; one-stage/mid-entry routing; evidence anchors; evidence-to-section architecture; read-only review; criterion-bound constructive findings; minimum versus stronger repair; cost/trade-off; frozen revision criteria; explicit degradation rather than simulated certainty |
| [Nature Skills](https://github.com/Yuan1z0825/nature-skills) | nature-writing 1.4.0, nature-polishing 6.5.0, nature-statistics 1.3.0 plus shared core | repository `main` commit `a6e6f3456f2065eb555afe8ed2c28637f3cd4e1b` | manifest-driven progressive loading; shared versus local core; claim-first and Results-first writing; one-job paragraphs; shortest sufficient evidence chain; main-text placement discipline; abstract-last drafting; targeted revision and consistency sweeps |

## Product synthesis rather than inheritance

| Peer design lesson | Radiology implementation | Domain-specific addition | Standalone runtime owner |
|---|---|---|---|
| Mid-entry routing and task contract | route signature, Research Request Passport and the narrowest current task | `imaging-only` / `mechanism-only` / `imaging-mechanism`, role-grouped measured/reference/generated/proposed modalities | `radiology-radiogenomics` and `radiology-pipeline` |
| Evidence-anchored constructive review | atomic finding, severity, governing criterion, consequence, minimum repair, stronger option, cost and closure evidence | patient/lesion/donor/section/cell/spot units, matched-n topology, modality QC, mechanism alternatives and claim ceilings | `radiology-radiogenomics` and `radiology-prereview` |
| Parameter and methodology evaluation | separate parameter, metric and method objects; fair benchmark, ablation, sensitivity, failure boundary and writing placement | radiomics/DL plus bulk, scRNA, spatial, pathology, multi-omics, perturbation and cross-scale bridge adapters | `radiology-method-evaluation`, with domain execution owners and `radiology-stats` for inference |
| Progressive loading | compact router plus versioned manifest and on-demand references | activate only the measured or actual target modality; do not let an atlas or proposed validation masquerade as active evidence | `radiology-radiogenomics` |
| Claim-first and Results-first writing | claim-to-section map, Results/figure spine, one-job paragraphs and abstract-last sequence | measured/derived/estimated/associated/predicted/perturbed evidence roles, cross-scale mapping and protected negative evidence | `radiology-radiogenomics` and `radiology-writing` |
| Main-text discipline and consistency sweep | shortest sufficient evidence chain; allocate to text, legend, Methods, source data and supplement; repeat cross-artifact checks | preserve decision-bearing robustness, discordance, denominators, spatial/assay resolution and mechanism boundaries | `radiology-writing`, `radiology-polishing`, `radiology-figure` and `radiology-table` |
| Statistical reporting and revision integrity | explicit independent unit, uncertainty, multiplicity, exact result-before-location response and frozen Claim IDs | imaging performance/calibration/MRMC plus donor-aware omics, pseudoreplication, spatial hierarchy and perturbation controls | `radiology-stats`, `radiology-response` and `radiology-radiogenomics` |
| Submission-package readiness | separate manuscript science from administrative/visual upload readiness | journal/stage-specific file types, all-file inventory, rendering, cross-file consistency and human portal gates | `radiology-submission` |

The implementation column describes capabilities shipped inside this repository. The peer products
may be consulted during a future design review, but no row delegates a promised runtime capability to
them.

These architectural patterns were then stress-tested against a separate, row-level corpus of 100
official public reviewer-report/author-response pairs from 2024-08-22 through 2026-08-22. That
empirical corpus changed the local review and revision contracts—especially request triage,
applicable comparator/ablation checks, closure evidence and reasoned infeasibility responses—but is
not a software dependency.

Versions and commits are a dated snapshot, not a promise that these repositories remain unchanged.
Re-check each peer repository's default branch before a future architecture refresh.

## Deliberate adaptations

- The root file routes by the current scientific decision rather than forcing a complete research pipeline.
- Shared invariants are always loaded; modality and task playbooks are additive and evidence-role aware.
- Reviewer, mentor, mechanism, writing, and revision outputs have different minimum contracts.
- Review findings require real evidence locations, consequences, repair criteria, and bounded verdicts.
- Writing maps evidence to sections, paragraphs and displays before prose, keeps conclusion-changing
  evidence visible and exchanges an immutable scientific packet with internal style modules.
- Constructive review separates scientific validity, contribution/venue fit, submission readiness,
  defect severity, editorial obligation and revision-completion status.
- Revision uses stable issue and claim IDs so accepted content is preserved and only affected dependencies are reopened.
- Manuscripts and datasets remain untrusted input; external upload, source editing, and author decisions require the user's authority.

## Patterns intentionally not imported

- Do not represent one model run as multiple independent human or model reviewers.
- Do not produce invented numerical reviewer scores, vote counts, confidence percentages, or consensus arithmetic.
- Do not force a large generic stage pipeline when the user enters with a figure, result, paragraph, protocol, or revision.
- Do not let publication style, target-journal prestige, or fluent prose upgrade the scientific claim ceiling.
- Do not import arbitrary punctuation quotas, generic “AI-like writing” detectors, numerical reviewer
  aggregation, praise quotas, or algorithm-paper ablation/baseline requirements into studies where
  they are not scientifically applicable.
- Do not inherit external scripts, network calls, hooks, tool permissions, or provider uploads from a reference skill.

## Update procedure

On a future refresh, record the new repository commit and package versions, compare changed routing and
integrity contracts, update only the affected local rules, then rerun the route regression suite and
100-paper corpus audit. Run the standalone-release validator and preserve a recoverable backup of
installed reference skills before replacement. A refresh may improve local design but must not add an
external runtime dependency.
