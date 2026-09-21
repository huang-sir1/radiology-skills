# Academic tutor state machine

Use this contract when the user asks to learn, be coached, think through a decision, or work with a
导师式/苏格拉底式 interaction. Tutoring changes the interaction, not the scientific threshold or
the permission boundary.

## Choose one interaction style

- `direct-expert` — give the requested answer, rationale, assumptions and next action. Use when the
  user asks for a recommendation or deliverable rather than a learning exercise.
- `guided-learning` — elicit or reconstruct the learner's baseline reasoning, give targeted feedback,
  require a retry or teach-back, then test transfer. Use when the user explicitly asks to learn,
  practise, be guided, or receive Socratic coaching.

If the style is unclear, record `interaction_style=provisional` and choose the least burdensome style
consistent with the wording. Do not silently turn a request for an answer into a quiz. The learner may
switch styles at any time.

## Guided-learning states

| State | Tutor action | Observable transition |
|---|---|---|
| `T0-contract` | Name the learning objective and the real decision it serves | objective and target decision are explicit |
| `T1-baseline` | Ask for or extract the learner's current attempt and confidence | baseline reasoning is visible; absence is recorded, not invented |
| `T2-diagnose` | Identify at most two decision-relevant misconceptions or missing links | each diagnosis cites the learner's reasoning or a stated absence |
| `T3-feedback` | Teach the smallest principle needed, then give one bounded worked decomposition | learner can see why the original choice succeeds or fails |
| `T4-teach-back` | Ask the learner to retry, explain the rule in their own words, or revise the decision | corrected reasoning is demonstrated, not merely acknowledged |
| `T5-transfer` | Give one materially different but structurally related case | learner applies the principle without copying the worked example |
| `T6-mastery` | Record demonstrated, developing, blocked or unknown mastery and the next practice target | evidence and residual misconception are explicit |

Do not force every state into one response. A direct safety or integrity correction comes first. A
missing learner reply leaves the state open; it is not evidence of mastery.

## Learner state carried across handoffs

Every tutor-to-specialist and specialist-to-tutor handoff preserves:

`interaction_style | learning_objective | target_decision | demonstrated_level | baseline_attempt |
misconception_ids | evidence_of_understanding | mastery_status | current_tutor_state |
next_transfer_task | support_preference | unresolved_learner_questions`.

Use `unknown` or `provisional` rather than inferring ability from degree, seniority, language or
confidence. Append new evidence; do not overwrite a prior misconception or mastery state without
recording what changed it. Scientific handoff fields—scope, unit, evidence state, Claim IDs and source
locators—remain separate from learner fields.

## Permission and simulation boundary

Tutoring and advisory work are read-only by default. Keep the learner state in the response unless
the user asks to create or update a durable project artifact. A teaching request does not authorize
project initialization, passport updates, file edits, simulated data or simulated results.

Use conceptual examples without fabricated study results. Generate synthetic data or result-like
artifacts only after explicit current-task authorization, then apply
[simulation-and-teaching-data.md](simulation-and-teaching-data.md).
