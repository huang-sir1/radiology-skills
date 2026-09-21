# Experiment-lineage DAG contract

Use this optional contract when an analysis contains material branching, configuration search,
checkpoint selection, reruns or protected-test access. A simple prespecified one-pass analysis does
not need a DAG.

The DAG records **iteration lineage only**: an edge means that a later experiment used a parent's
result or feedback. It is not a causal graph, does not prove a mechanism or treatment effect, and
does not upgrade exploratory evidence. A checkpoint chosen after repeated access to a test set is
not independent or external confirmation.

## Required record

Copy `../assets/experiment-lineage.template.json` and replace every empty or
`AUTHOR_INPUT_NEEDED` value. Validate it with:

```powershell
python scripts/validate_experiment_lineage.py path\to\experiment-lineage.json
```

The root binds a stable lineage/study ID, creation time, the fixed non-causal boundary, one
checkpoint-selection policy, experiment nodes and any selection events.

Each experiment node binds:

- `experiment_id` and de-duplicated `parent_ids`;
- creation time, hypothesis, decision, branch reason and lifecycle state;
- `analysis_intent`: `PRE_SPECIFIED_CONFIRMATORY` or `EXPLORATORY`, plus the intent-lock time and
  artifact hash when confirmatory;
- data manifest identity, split manifest identity and the split role;
- protected-test identity, whether it was accessed, its lineage-wide access counter and access time;
- configuration, code and environment SHA-256 values;
- result state, time, metric, result artifact and feedback artifact;
- selection-family identity, claim status, and a reason whenever superseded or abandoned.

`parent_ids` are iteration dependencies, not evidence that changing a parent caused a child's
result. Configuration and artifact hashes establish identity only; they do not establish scientific
validity.

## Hard invariants

1. Experiment IDs are unique. Every parent exists, no node is its own parent, and the graph is
   acyclic.
2. `CONFIRMATORY` and `EXTERNAL_CONFIRMATORY` nodes must be locked before the first access to their
   named test, execute exactly one access with counter `1`, and use the matching confirmatory split
   role. An exploratory node cannot later be relabelled confirmatory.
3. The same confirmatory-test identity may be accessed by at most one experiment node. Reuse turns
   the affected work into exploratory development; do not preserve an external-confirmation claim.
4. A checkpoint selection names its selected experiment, complete selection family, all attempts,
   selection basis and selection time. The validator requires `all_attempt_experiment_ids` to equal
   every recorded node in that family. Multiple attempts require an immutable attempts artifact.
5. An applicable selection rule is locked before candidate results. Selecting among configurations
   that already accessed confirmatory tests is prohibited.
6. Every executed result and feedback resolves to a nonzero SHA-256 also present in the node's
   artifact list. Superseded and abandoned nodes remain in the DAG with a reason; they are never
   deleted merely because performance was unfavourable.

## Claim boundary

Allowed claim states are `NON_CLAIM_BEARING`, `EXPLORATORY`, `INTERNAL_VALIDATION`, `CONFIRMATORY`
and `EXTERNAL_CONFIRMATORY`. The validator checks structural lineage and test-use discipline only.
It cannot prove causal identification, biological mechanism, clinical utility, transportability or
that two datasets contain independent patients. Those claims remain with their scientific owners
and require their own evidence.

## Design provenance

Microsoft's [RD-Agent](https://github.com/microsoft/RD-Agent) and its
[Trace API](https://rdagent.readthedocs.io/en/latest/api_reference.html) were used as an open-source
comparison for hypothesis -> experiment -> feedback ancestry. This contract adds protected-test and
claim-ceiling gates for research use; it neither depends on RD-Agent nor treats lineage ancestry as
causal structure.
