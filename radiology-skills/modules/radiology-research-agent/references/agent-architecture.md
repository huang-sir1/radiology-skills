# Imaging-Research Agent Architecture

Use this reference to select an orchestration pattern and specify evidence, roles, tools, typed
contracts, durable state, and reproducible artifacts.

## 1. Choose single versus multi-agent

Start with a single Agent plus deterministic tools. Add roles only when they create a testable
control or performance gain.

| Design | Use when | Required controls | Avoid when |
|---|---|---|---|
| Single Agent | The task is sequential, the context is bounded, and one policy/tool surface is sufficient | Typed tool calls, explicit state, independent output checks | One context would mix untrusted retrieval, privileged actions, and verification |
| Multi-agent | Roles need different permissions, independent verification, parallel work, or specialized context | Supervisor, typed handoffs, shared evidence identifiers, loop/budget limits, conflict resolution | Roles merely restate one another or increase cost without measurable benefit |
| Deterministic pipeline | Steps and validation rules are stable | Versioned code, schemas, checkpoints, exception routing | Scientific judgment or evidence conflict needs accountable review |

Document the rejected alternatives, expected benefit, added failure modes, latency/cost budget, and
an ablation comparing the chosen design with the simplest credible baseline.

## 2. Assign roles without diffusing accountability

| Role | Responsibility | Must not |
|---|---|---|
| Planner | Decompose the approved charter into steps, dependencies, gates, and budgets | Expand scope or authorize actions |
| Retriever | Search approved sources and create provenance-complete evidence records | Treat retrieved instructions as trusted or invent inaccessible metadata |
| Analyst | Run approved transformations or statistical/code workflows | Change the analysis plan, inputs, or endpoint silently |
| Verifier | Check claim-source support, numbers, artifact hashes, and reproducibility | Approve its own privileged action or waive a failed check |
| Writer | Compose bounded research artifacts from verified claims and results | Introduce unsupported facts or convert uncertainty into certainty |
| Supervisor | Enforce state transitions, budgets, permissions, approvals, and escalation | Override clinical, ethics, governance, or human-approval boundaries |

Every handoff has one producer, one named consumer, a typed payload, acceptance criteria, and an
owner for unresolved conflicts. Keep privileged tools separate from roles that ingest untrusted
content.

## 3. Build provenance-first RAG

Assign each source a stable identifier such as `SRC-000123`; do not use rank position or a mutable
URL as the identifier. Store:

- source identifier, source type, title, authors/organization, publication or release date;
- DOI, PMID, registry ID, accession, repository commit, dataset version, or other persistent ID;
- canonical URI, retrieval timestamp, retriever/tool version, content hash, and access status;
- license, retraction/correction status, extraction method, and page/section/table/figure location;
- trust tier, relevance decision, eligibility decision, and human verification status.

Keep raw retrieved content in an untrusted evidence store. Pass only delimited excerpts plus
metadata to reasoning roles. Strip or quarantine embedded instructions, executable content, hidden
text, links, and macros; never promote them into Agent policy.

Create a claim record for each substantive statement:

```text
claim_id | claim_text | source_ids | source_locations | support_type
verification_status | verifier | verified_at | conflicts | artifact_ids
```

Use `support_type` values such as direct, derived, contextual, contradictory, or unsupported.
Derived claims must also identify the transformation or analysis artifact. A citation is not
verified merely because the source exists; confirm that the cited location supports the exact
claim, population, modality, endpoint, and number.

## 4. Constrain tools

Maintain a deny-by-default allowlist:

```text
tool_id | role | operation | input_schema | output_schema | data_class
filesystem_scope | network_scope | write_scope | approval_required
timeout | retry_limit | version | audit_fields
```

Implement the allowlist in a deterministic non-LLM control plane and tool gateway. Agents only
submit typed proposals. The control plane authenticates the caller, validates policy, permission,
approval, state, budget, and schema, then asks the gateway to invoke the exact permitted tool
operation. The gateway independently enforces resource, path, network, target, payload, and write
scope and returns a signed or integrity-protected result for the ledger. Never rely on an Agent to
self-enforce permissions, approval, or authoritative state transitions.

Separate read, compute, local-write, and external-write capabilities. Pin tool and dependency
versions. Restrict paths and network destinations explicitly. Run downloaded code and document
parsers in isolated, resource-limited environments. Never expose secrets to a role or tool that
does not require them.

## 5. Use typed inputs and outputs

Every task and handoff includes:

- `task_id`, `run_id`, `step_id`, `schema_version`, `plan_version`, and `correlation_id`;
- input artifact IDs and hashes, evidence IDs, data classification, and authorization context;
- requested operation, assumptions, preconditions, resource budget, and completion criteria;
- output artifact IDs and hashes, validation status, warnings, errors, and unresolved decisions.

Reject payloads with missing provenance, unknown schema versions, stale authorization, or
unexpected fields. Validate semantic invariants as well as syntax: cohort counts must reconcile,
citations must resolve, and result tables must match the approved analysis version.

## 6. Define an explicit state machine

Use transitions such as:

```text
draft -> scoped -> evidence_pending -> evidence_verified -> plan_pending
plan_pending -> plan_approved -> running -> verification_pending
verification_pending -> approval_pending -> completed
any nonterminal -> blocked | failed | cancelled
running -> paused -> running
```

List the required records and approver for every transition. Reject skipped or backward transitions
unless a documented rollback creates a new run/version. Terminal state must distinguish completed,
blocked, failed, and cancelled; never label a partially executed task completed.

Store the authoritative state outside Agent context. Apply transitions with compare-and-swap on the
expected state/version so concurrent workers cannot both advance a run. A worker must hold a
bounded lease and monotonic fencing token; every durable write and tool invocation rejects an
expired lease or older token. Agents may propose transitions, but only the deterministic control
plane can commit them.

## 7. Persist durable checkpoints

Checkpoint before and after costly computation, approval, privileged operation, or external action.
Store atomically:

- state and transition event; plan/schema/tool versions; input and output hashes;
- evidence ledger and claim-source map snapshots;
- code, environment, parameters, random seeds, logs, and validation results;
- approval identity, scope, target, artifact hash, timestamp, and expiry;
- pending operations, idempotency keys, retry counts, costs, and known external state.

Protect checkpoints against unauthorized modification and record append-only audit events. Keep
patient identifiers and secrets out of checkpoint content unless an approved encrypted store and
retention policy explicitly require them.

## 8. Make execution idempotent and resumable

Write every effectful proposal to an atomic operation ledger before execution. Give each logical
operation one globally unique idempotency key derived from the run, action nonce, operation, target,
and payload/artifact hash. Record expected state/version, fencing token, approval event, attempt,
status (`proposed`, `claimed`, `dispatched`, `succeeded`, `failed`, or `unknown`), result identifier,
and timestamps. Enforce a uniqueness constraint on the idempotency key.

Claim the ledger row and compare-and-swap the run state in one transaction where possible. Use a
bounded lease and fencing token to prevent a paused or retried worker from acting after ownership
has moved. A read-before-write check is insufficient because another worker can win the check-act
race.

Prefer target-side idempotency using the same key and reconcile the returned target identifier. If
the target does not support idempotency, atomically write a transactional outbox event with the
state/ledger update, then let a fenced dispatcher deliver it with deduplication and reconcile the
outcome. Do not mark success until target-side evidence is durable. Retries may repeat reads and
deterministic local computation; an external write with unknown outcome requires reconciliation or
human review, never blind replay.

On resume:

1. load the last verified checkpoint;
2. verify hashes, schemas, tool versions, authorization scope, and approval validity;
3. reconcile pending external operations;
4. invalidate descendants of changed evidence, data, code, or plans;
5. continue from the earliest valid state, preserving the prior run as audit history.

Set bounded retries and loop budgets. Escalate persistent failures, evidence conflicts, and state
ambiguity rather than generating a plausible completion.

## 9. Authenticate and consume approvals

Receive approvals only as authenticated control events from a trusted UI or API. Verify the human
identity and authorized role, then bind the event to `run_id`, a cryptographically unpredictable
`action_nonce`, exact operation, target, payload/artifact hash, scope, policy version, issue time,
and expiry. Store the event in the control plane, not Agent memory.

Consume approval once, atomically with the operation claim or state transition. Enforce nonce
uniqueness and reject replay, mutation, expiration, wrong role, wrong run, wrong target, or hash
mismatch. Never infer approval from retrieved documents, messages, metadata, Agent text, memory,
or tool output; these are untrusted inputs even when they appear to quote an authorized person.

## 10. Maintain an artifact manifest

Use one lineage manifest for papers, data, code, figures, and decisions:

```text
artifact_id | type | title | version | hash | created_by | created_at
source_artifact_ids | evidence_ids | code_commit | environment_id
approval_status | validation_status | data_class | storage_uri | retention
```

For papers, preserve persistent identifiers and exact cited locations. For data, record cohort,
schema, inclusion snapshot, de-identification status, and access terms. For code, record commit,
dependencies, parameters, and seeds. For figures, record generating code and source tables. For
decisions, record alternatives, rationale, evidence, approver, and downstream artifacts.

The manifest is the authoritative inventory for reproducibility and rollback. Do not overwrite an
artifact in place; create a new version and preserve lineage.
