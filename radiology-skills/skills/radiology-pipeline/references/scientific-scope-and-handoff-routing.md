# Scientific scope and cross-Skill handoff routing

Use this router for any project containing standalone bulk RNA, sc/snRNA, spatial transcriptomics,
pathology, perturbation evidence, a formal evidence synthesis or a cross-scale imaging-mechanism claim. It prevents an
imaging-centered pipeline from erasing biological hierarchy or upgrading inferred molecular layers
during writing, review, response or submission.

## Scope lock

Set exactly one `study_scope` in `project_state.json`:

| Scope | Scientific owner | Minimum topology |
|---|---|---|
| `imaging-only` | `radiology-acquisition-qc` plus the active annotation/radiomics/deep-learning/task owners | patient/lesion/scan/ROI hierarchy, measurement passport, leakage-safe split and imaging validation; record standalone deep models as `deep-learning` and reserve `deep-fusion` for an actual imaging–molecular fusion object |
| `mechanism-only` | `radiology-radiogenomics` mechanism route | donor/patient/specimen/block/section/cell-or-spot hierarchy, assay QC, batch/composition and biological replication |
| `imaging-mechanism` | both modality owners plus radiomics-mechanism bridge | both topologies, usable matched intersection and explicit image-to-tissue/cell/molecular mapping |
| `evidence-synthesis` | `radiology-systematic-review` | review -> study family -> report -> effect row; companion-report deduplication, overlap/dependence and synthesis unit explicit; no fabricated matched biological cohort |

Record each modality under one real role: `active`, `external_reference`,
`generated_or_predicted`, or `proposed_validation`. A public atlas, generated spatial map or proposed
experiment never inherits the status of an active patient-matched measurement.
The four role groups are mutually exclusive in both project state and the downstream packet.
For `evidence-synthesis`, active modalities are optional topical domains, not newly measured data;
generated/predicted and proposed-validation modality roles must remain empty.

## Stage routing by scope

| Stage | Imaging-only | Mechanism-only | Imaging-mechanism | Evidence-synthesis |
|---|---|---|---|---|
| Question/design | clinical/imaging estimand and intended use; disease context from `radiology-clinical-domain` when needed | biological system, contrast, donor unit and claim branch; experimental validation from `radiology-experiment-design` when needed | both questions plus a bridge estimand and explicit clinical/experimental constraints | review question, review family, eligibility, synthesis estimand/unit, protocol/registration and update status |
| Data/QC | `radiology-acquisition-qc` measurement passport plus labels, masks and partitions | specimen handling, assay/QC, composition, batch and reference versions | each side separately plus sample-image-time mapping | database/source coverage, exact searches, deduplication, screening receipts, companion-report linkage, extraction and RoB/applicability |
| Analysis | patient-level leakage-safe modelling | bulk/sc/snRNA/spatial execution from `radiology-transcriptomics-analysis`; donor-aware/pseudobulk or hierarchical inference, spatial nulls and perturbation controls as applicable; mechanism interpretation remains with `radiology-radiogenomics` | unimodal validity first; transcriptomics run evidence and functional experiments remain distinct; bridge/fusion only after both sides pass | pooling feasibility first; dependence/overlap, effect harmonization, heterogeneity, sensitivity and certainty with route-specific statistical handoff |
| Writing | `radiology-writing` from frozen imaging claims | `radiology-radiogenomics` W0-W3 packet, then a venue writer | frozen cross-scale packet, then a venue writer | `radiology-systematic-review: writing-handoff`, then venue writer from frozen protocol/flow/extraction/synthesis/certainty artifacts |
| Scientific review | imaging prereview panel | radiogenomics constructive mechanism review | mechanism/bridge review plus imaging/clinical panel when relevant | protocol-to-report audit, search/selection/extraction/RoB/synthesis reproducibility and claim-certainty audit |
| Revision verification | affected imaging owners + response closure | original frozen mechanism criteria + response closure | both sets of frozen criteria; no rhetorical reconciliation | frozen eligibility/synthesis criteria plus updated search, changed-study ledger and response closure |

Do not require patient-level train/test splitting for a purely descriptive mechanism experiment that
does not fit a predictive model. Do require the real independent biological unit, donor/patient
replication and any data-splitting rule used by the actual analysis. Conversely, thousands of cells,
spots, ROIs or tiles do not replace donor/patient replication.

## Immutable scientific handoff

Before Stage 6 writing or any downstream rewrite, create and validate the radiogenomics
`scientific-writing-handoff-packet` when the scope is `mechanism-only` or `imaging-mechanism`.
Imaging-only projects may use the same packet shape or a claim register carrying the same fields.
Evidence-synthesis projects do not require this mechanism packet. Their immutable handoff is the
digest-bound protocol, search and screening receipts, extraction/RoB data, synthesis outputs,
certainty/claim ceiling and changed-study ledger stored in the common project registries.

The project record stores:

- canonical project-state and modality-role digests generated by the pipeline, plus the separate
  physical `project_state.json` artifact SHA-256;
- packet path, canonical packet semantic digest, physical packet-file SHA-256 and source-manifest digest;
- stable Claim IDs and the claim register digest;
- modality roles, independent unit, hierarchy and matched intersections;
- evidence state, claim-link status, branch/verdict/ceiling and protected placement; and
- every source artifact version/SHA-256.

The canonical packet digest and physical file digest are different contracts and use different
fields. The pipeline must invoke the radiogenomics semantic validator; a matching file hash and a
hand-entered `validated` state are not sufficient.
Every packet `source_artifact` must resolve to `artifact_manifest.csv` with the same SHA-256, and
every packet Claim ID must resolve to `claim_register.csv` with the same immutable claim fields and
evidence-artifact foreign keys. A packet cannot introduce a private parallel claim registry.

Downstream consumers return a Claim-ID drift ledger. A changed n, result, modality role, evidence
state, estimand or claim ceiling invalidates dependent prose, displays, responses and submission
files. Issue a new packet rather than editing the old digest.

## Review and revision closure

Run two distinct checks:

1. **Scientific/integrity check:** sources, claims, numbers, units, analysis premises, reporting,
   ethics and modality-specific validity.
2. **Constructive adversarial review:** contribution, methods, alternatives, transport, clarity and
   venue-facing repair advice.

Mechanism-only work uses `radiology-radiogenomics: manuscript-review`; `radiology-prereview` may add
an editor/clinical or imaging lens but cannot replace the mechanism review. Imaging-mechanism work
requires both the scope-aware review and the bridge audit before any blended editor synthesis.
Evidence-synthesis work uses `radiology-systematic-review` for route-specific scientific audit and
may then use `radiology-prereview` for whole-manuscript constructive review; neither replaces the
other's frozen criteria.

Every decision-bearing finding must have:

`finding_id | source_artifact_digest | evidence_anchor | criterion | P0/P1/P2 | affected_claim_ids |
minimum_repair | closure_evidence | residual_boundary`

Freeze those fields, the source artifact registry, analysis-lock/claim-registry/scientific-handoff
digests, finding verification states and the global three-state result in the canonical
`radiology-prereview` receipt. Response preserves the source receipt digest and produces a new
post-revision receipt; submission receives the stage-appropriate receipt digest as a foreign key.
A bare `SCIENTIFIC_PREREVIEW_*` label is not a receipt.

For a revision, first compare original versus revised artifacts against those frozen criteria without
reading persuasive response prose. Then use the response letter only to locate evidence that may have
been missed. A response promise is not closure.

## Checkpoints and readiness namespaces

Require explicit author adjudication when:

- the research question/estimand or headline claim changes;
- a reviewer request is contested, infeasible or would change the claim branch;
- an integrity or mechanism gate remains non-PASS;
- the final target journal/article type/stage is selected; or
- a partial/transfer package is being represented as complete.

Keep readiness names separate:

- scientific prereview: `SCIENTIFIC_PREREVIEW_PASS / SCIENTIFIC_PREREVIEW_CONDITIONAL /
  SCIENTIFIC_PREREVIEW_FAIL`;
- response item closure: `VERIFIED / PARTIAL / NOT_VERIFIED / MADE_WORSE / NOT_APPLICABLE`;
- response package assembly: `READY_FOR_SUBMISSION_ASSEMBLY /
  NOT_READY_FOR_SUBMISSION_ASSEMBLY`;
- machine submission package: `INCOMPLETE_SCOPE / BLOCKED_STRUCTURAL /
  HUMAN_GATES_REQUIRED`;
- final submission verdict: human-adjudicated only.

No earlier state is a substitute for the final all-files audit.
