# Shared scientific-state interoperability contract

Use this contract when radiomics, bulk RNA, sc/snRNA, spatial, pathology, perturbation or
imaging-mechanism state is exchanged between `radiology-*` tasks for writing, polishing, prereview,
response or submission work. The packet preserves scientific meaning and exact source identity;
it is not a prose outline, a publication-readiness certificate or a claim that one skill owns truth.

The module that creates a packet and the module that receives it have temporary task roles, not a
parent–child relationship. A packet is required when a prior task's frozen state is being consumed.
It is not a prerequisite for direct standalone entry: a module may build a bounded local state from
the supplied artifacts, expose missing evidence and proceed wherever the requested claims are
traceable.

## Packet-origin gate

Create the packet from
`../templates/scientific-writing-handoff-packet.template.json`. A packet may carry
`W-RETURN-TO-LEDGER` or `W-REVISE` while work is incomplete. Set
`writing_handoff_status=W-HANDOFF-READY` only after W0-W3 have closed and every material claim has:

- a stable Claim ID and source artifact pointer;
- source artifact version and SHA-256 plus the source-manifest digest;
- the canonical analysis-lock digest and the frozen claim-register file SHA-256;
- the real study scope and modality roles (`active`, `external_reference`,
  `generated_or_predicted`, `proposed_validation`);
- independent unit, biological hierarchy and usable matched intersection;
- primary evidence state, modality subtype and claim-link status;
- claim branch, `PASS / CONDITIONAL / STOP`, maximum wording and residual boundary; and
- protected manuscript/display placement for decision-bearing evidence and limitations.

Unknown facts remain in `author_input_needed`; a ready packet cannot contain unresolved author
facts. Generated, transferred, deconvolved, imputed or virtually perturbed layers remain labelled as
such. Their presence does not convert them into patient-matched or experimentally measured evidence.

For tutoring handoffs, include the optional `learner_state` object from the template. Preserve
`interaction_style`, learning objective, target decision, demonstrated level, baseline attempt,
misconception IDs, evidence of understanding, mastery status, current tutor state, next transfer
task, support preference and unresolved learner questions. A non-tutoring packet may omit the
object. `mastery_status=demonstrated` requires recorded evidence of understanding; a receiving
module appends new evidence instead of silently overwriting the prior state.

## Digest and identity

`packet_sha256` is the lowercase **canonical semantic digest** of UTF-8 JSON after removing only the top-level
`packet_sha256` field. Canonical JSON uses sorted keys, compact separators and rejects non-finite
numbers. It is not the SHA-256 of the packet file bytes. `source_manifest_digest` is the frozen
source-manifest file SHA-256; `analysis_lock_digest` binds the canonical analysis-lock object; and
`claim_register_sha256` binds the exact claim-register file. Every listed source artifact also
carries its own SHA-256.

Modality role groups are mutually exclusive. Every claim evidence pointer uses
`<registered artifact_id>:<locator>`, and the claim's independent unit and matched n must match a
topology intersection linked to at least one of those evidence artifacts. A canonical digest locks
bad content just as effectively as good content, so semantic cross-references must pass before
`W-HANDOFF-READY`.

As a minimum anti-overclaim invariant, a `mechanistic` or `causal` branch cannot receive `PASS` when
its primary evidence is `derived`, `estimated`, `associated` or `predicted`, or when the claim link is
`inferred`/`proposed`. Such a PASS needs at least measured or perturbed primary evidence and a direct
claim link; this compatibility check is necessary but never sufficient for causal validity. The
branch-specific scientific review must still inspect alternatives, identification, controls,
temporal order, target engagement and transport as applicable.

Before consuming a ready packet, run:

```text
python scripts/validate_scientific_handoff.py <packet.json> --require-ready
```

A valid digest proves internal byte binding, not that an analysis or experiment occurred or that a
claim is scientifically correct.

## Receiving-module contract

Writing, polishing, review and response modules may change paragraph order, transitions, syntax,
compression and venue-appropriate presentation. They may not silently change:

`study_scope | modality roles | independent unit | matched n | evidence state | modality subtype |
claim-link status | claim branch | branch verdict | maximum wording | protected placement`

When present, learner-state fields are also immutable historical state except through an appended
evidence-backed tutor update. Editorial modules may not infer learner mastery or erase a recorded
misconception.

Each receiving module returns a Claim-ID drift ledger:

`claim_id | preserved_fields | proposed_change | reason | source_evidence | disposition`

Allowed dispositions are:

- `PRESERVED` — no immutable field changed;
- `EDITORIAL_ONLY` — wording/placement changed within the packet ceiling;
- `RETURN_TO_LEDGER` — a requested edit conflicts with the packet or needs new evidence;
- `SUPERSEDED_BY_NEW_PACKET` — the originating task issued a new validated packet after a verified
  source, analysis or author-decision change.

Do not use `EDITORIAL_ONLY` to conceal claim strengthening or removal of a protected negative result.
If source bytes, n, estimand, modality role, result or claim ceiling changes, reopen affected
artifacts and issue a new packet/digest.

## Scope routing

- `imaging-only`: route scientific imaging writing/review through the imaging chain; do not request
  absent molecular evidence.
- `mechanism-only`: keep donor/specimen/cell/spot hierarchy and assay-specific evidence under the
  radiogenomics mechanism playbooks. A generic Radiology-shaped writer or imaging-only prereviewer
  cannot replace this scientific review.
- `imaging-mechanism`: both modality pipelines and the cross-scale bridge must pass separately. A
  later venue/style pass cannot repair a failed tissue-image mapping or mechanism claim.

The final all-files submission audit independently verifies the actual upload root and target-journal
rules. When a shared-state packet is used, it must validate before another module relies on it; that
validation helps preserve source-bound state but does not certify truth or imply that the package is
structurally or visually ready.
