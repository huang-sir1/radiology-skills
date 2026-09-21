# Model behavior evaluations

This directory is the release-facing harness for real forward model-behavior evaluation. Static
skill validators prove only that contracts and case registries are well formed; they do not execute
prompts or prove that a model follows those contracts.

## Evidence boundary

No model outputs or qualified human adjudications are included in this release tree. Two prior blind
checks were not imported because no complete bundle was available that bound the exact frozen prompt,
installed product/manifest, raw output file, output SHA-256, rubric decision and adjudicator record.
They therefore remain informal pilot observations, not release evidence.

The machine validators in this directory report structural integrity only. They never turn a model
output, rubric-shaped JSON or self-score into a human behavior PASS.

## Evidence-based improvement loop

Use `run-observation.template.json` to freeze one run-level observation and
`improvement-candidate.template.json` only after comparing evidence across runs. The controlled
defect classes distinguish routing, execution, template, handoff, source and runtime problems from
`NO_DEFECT`. Every observation records a stable `invariant_id`, `defect_signature`,
`root_cause_state` and `affected_contract`. A `READY_FOR_REVIEW` candidate must cite every physical
observation file and its SHA-256. The validator reopens those files and independently derives the
observation IDs, runs, prompts, highest severity, defect class, invariant, signature, root cause and
affected contracts; self-reported `evidence_pattern` values must match.

A persistent change may enter review only after the same non-`NO_DEFECT` class, invariant, defect
signature and resolved root cause appear in at least two distinct runs and two distinct
cases/prompts. A single documented P0/P1 invariant break retains an emergency review path. Merely
repeating a defect class is insufficient. Neither condition authorizes the edit: both templates keep
`persistent_change_authorized=false`, and every proposal must name the smallest change, regression
and rollback. See the pipeline's `evidence-based-skill-improvement-loop.md` contract.

The validator always checks both template shapes. Completed external records can also be checked
with `--run-observation <file>` or `--improvement-candidate <file>`; this still records structure and
eligibility only, never a release decision.

## Frozen case registry

`cases.json` covers colloquial, ambiguous, compound and boundary-crossing prompts. Each case
binds its exact UTF-8 prompt with SHA-256, declares required/prohibited behavior, carries an
explicit `release_blocking` flag and explicitly names `dependency_skills`. Every runtime skill must
be the `target_skill` of at least one frozen case; the validator fails closed on an uncovered
skill. The evaluated skill bundle is the complete de-duplicated union of every
`target_skill` and `dependency_skills`; dependencies cannot repeat their case target. Changing prompt
text requires a new registry version and new model outputs. Shared hashing/JSON helpers live in
`scripts/eval_common.py` and are imported by both the validator and the receipt builder.

Validate the frozen assets:

```powershell
$Python = 'C:\huangsir-radiomics\.mamba\envs\radiomics_lab\python.exe'
& $Python 'C:\radiology-Skill\behavior-evals\scripts\validate_behavior_eval_assets.py' `
    --registry 'C:\radiology-Skill\behavior-evals\cases.json'
```

## Capturing a real pilot run

1. Install or package the exact product version being evaluated.
2. Run each frozen prompt against that installed product without rewriting it.
3. Save each complete raw response as `<case_id>.txt` in a run directory outside the release source
   tree. Preserve model errors/refusals exactly; do not clean the output.
4. Build an unadjudicated receipt. This computes the registry, plugin-manifest and output hashes; it
   does not call a model:

```powershell
$Python = 'C:\huangsir-radiomics\.mamba\envs\radiomics_lab\python.exe'
$RunRoot = 'C:\radiology-behavior-runs\pilot-20260822'
& $Python 'C:\radiology-Skill\behavior-evals\scripts\build_behavior_eval_receipt.py' `
    --registry 'C:\radiology-Skill\behavior-evals\cases.json' `
    --manifest 'C:\radiology-Skill\.codex-plugin\plugin.json' `
    --product-root 'C:\radiology-Skill' `
    --outputs-dir (Join-Path $RunRoot 'outputs') `
    --run-id 'pilot-20260822' `
    --provider 'AUTHOR_INPUT_NEEDED' `
    --model 'AUTHOR_INPUT_NEEDED' `
    --model-version 'AUTHOR_INPUT_NEEDED' `
    --output (Join-Path $RunRoot 'behavior-eval-receipt.json')
```

The builder hashes the full file tree of the complete target-plus-dependency closure; a matching
version string or plugin manifest alone is not accepted as exact evaluated content. It also binds an
evaluation-harness tree digest covering `cases.json`, `rubric.md`, the receipt schema, every JSON
template and the complete `scripts/` tree. Any later harness change invalidates the receipt.
Replace the three visible `AUTHOR_INPUT_NEEDED` values with the actual provider/model/version before
claiming a reproducible execution identity. A generated receipt remains
`PILOT_UNADJUDICATED`, `comparison_claim_eligible=false` and `release_claim_eligible=false`.

The default `system_context_digest=not-captured` is acceptable for a pilot capture only. Such a
receipt cannot support a cross-version comparison or any maturity upgrade. This harness keeps
`comparison_claim_eligible=false` even when a context digest is present; a separately governed,
trusted comparison process must establish any stronger claim.

5. Give the frozen outputs, receipt, `rubric.md` and
   `human-adjudication.template.json` to qualified reviewers. Reviewers cite response line locators,
   score every required/prohibited behavior, record disagreements and freeze the completed
   adjudication file with SHA-256.
6. Validate the receipt and output hashes again. Machine validation can establish file identity and
   completeness; `release_claim_eligible` must remain `false` because this harness cannot authenticate
   adjudicator identity, qualification or signature. Release acceptance remains a trusted signed
   human decision outside this harness.

Do not store credentials, patient data, private prompts or institution-only material in run files.
