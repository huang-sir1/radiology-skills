# Results — narrative

Past tense, quantitative, claim-first. Build an evidence ladder, not a lab diary.

## Order
1. **Patient flow & characteristics** — final n and how it was reached (mirror the flow
   diagram); Table 1 (demographics, prevalence, key clinical variables, by split/group).
2. **Primary result** — the main performance/effect **with 95% CI** (and p where a test
   applies); state the operating threshold and where it came from.
3. **Comparisons** — model vs readers / vs standard of care / vs prior method, **paired**
   where the same cases were used; report the difference + CI + test (DeLong/McNemar).
4. **Calibration & clinical utility** (prediction models) — slope/intercept, Brier;
   decision-curve net benefit.
5. **Validation** — internal (resampling) and, crucially, **external/independent**
   performance.
6. **Method evaluation when claimed** — fair benchmark, component/modality ablation and parameter
   sensitivity with matched conditions, effect/uncertainty and whether the conclusion changed.
7. **Robustness / OOD / efficiency / failure analysis** — pre-specified; report negative settings,
   failure cases and hardware/implementation conditions for any efficiency claim; don't fish.
8. **Subgroups** — pre-specified and interaction-aware; don't infer differences from separate p values.

## Rules
- Numbers carry the message: estimate + CI + n; don't say "significantly higher" without the
  value and test.
- Don't interpret here (save meaning for Discussion); don't introduce methods here.
- Match every Results number to a table/figure or the text — no orphan numbers; no number in
  text that contradicts a table.
- Report exact p (`P = .03`); reserve `P < .001`.
- Distinguish `PLANNED`, `AUTHOR_REPORTED`, `PARTLY_VERIFIED`, `VERIFIED` and `NOT_ASSESSABLE`; no prose may imply an
  ablation, sensitivity analysis or benchmark was run when only a plan or Methods statement exists.
- “Robust” requires the tested values/range, independent unit, estimate/uncertainty, artifact
  location and claim consequence. Put reconstructive configuration detail in Supplement, but keep a
  conclusion-changing failure visible in the main Results.

## Reporting sentence patterns
- *"Of 412 eligible patients, 98 were excluded ([reasons]), leaving 314 ([demographics])."*
- *"The model achieved an AUC of 0.88 (95% CI: 0.84, 0.92) on the internal test set and 0.85
  (95% CI: 0.79, 0.90) on the external cohort."*
- *"Sensitivity exceeded that of the radiologists (0.91 vs 0.82; difference 0.09; P = .01,
  McNemar)."*

## Common failures
Interpretation creep; missing CIs; unpaired test on paired data; per-lesion stats treated as
independent; subgroup fishing; numbers that don't match tables.
