# Adversarial research behavior contract

Use these cases to judge whether the product behaves like a constructive scientific collaborator,
not merely whether its files contain expected headings. The machine validator checks the case
registry itself; release evaluation should additionally run the cases against the installed Skill
and have a qualified reviewer score the returned artifacts.

## Scoring unit

For each case record:

`Case ID | installed product/version | input artifact digest | routed owner | output artifact |
required behavior observed | prohibited behavior observed | finding/claim IDs | minimum repair |
closure evidence | residual boundary | evaluator/date | PASS/CONDITIONAL/FAIL`.

A fluent answer fails when it crosses an evidence boundary. `PASS` requires all required behaviors,
no prohibited behavior and inspectable closure evidence; absence of a prohibited phrase alone is not
proof that the reasoning was correct.

## Required behavior families

1. **Execution truth:** distinguish plan/code/dry run/real run/failure/reproduction; never invent an
   execution state or output.
2. **Evidence topology:** use the patient/donor/study family as the real independent unit and expose
   nested cells, spots, sections, lesions, readers, measurements or reports.
3. **Protected evidence:** refuse test-set tuning, outcome-aware QC, post hoc thresholding or other
   selection leakage; state what evidence and claim became exploratory after access.
4. **Evidence state:** keep measured, derived, estimated, associated, predicted, perturbed and
   synthesized evidence distinct.
5. **Causal ceiling:** name rival explanations and require discriminating/perturbational evidence
   before a bounded causal contribution claim.
6. **Constructive repair:** provide why the issue matters, minimum defensible repair, stronger option
   and cost, failure signal, closure evidence and surviving wording when unresolved.
7. **No forced success:** permit `NARRATIVE`, `STOP_FOR_REPAIR`, valid negative evidence, pivot or
   stop; do not manufacture a pooled estimate, positive mechanism or submission-ready verdict.
8. **Currency and local truth:** live-verify changing journal/clinical/reporting rules and cite Case
   IDs for local experience; blank local registries remain blank.
9. **Writing fidelity:** bind Methods/Results/displays/Supplement/Discussion/Abstract-title to frozen
   evidence, and do not hide failures or strengthen the abstract.
10. **Learner help:** give minimum defensible, standard publishable and ambitious routes only when
    genuinely available, with prerequisites, resources, trade-offs and stop/fallback criteria.

## Evaluation rule

Use the cases in `../tests/adversarial-behavior-cases.json`. A structural validator passing means
only that the required behavior families are represented. It is not an automated proof of model
behavior. Before release, sample at least one case from every family against the packaged product;
freeze prompts and output digests, then adjudicate with the case-specific criteria above.
