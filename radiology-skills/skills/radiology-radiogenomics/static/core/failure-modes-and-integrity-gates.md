# Failure modes and integrity gates

Diagnose scientific structure before recommending models or polishing prose. A fluent narrative cannot
repair broken identity, leakage, pseudoreplication, or a non-identifiable mechanism.

## Orthogonal scientific labels

**Severity describes the defect:**

- `P0` — could invalidate a central result or make the requested claim non-identifiable; must fix.
- `P1` — claim may survive, but an important design, validation, or reporting weakness remains.
- `P2` — clarity, completeness, or reproducibility improvement unlikely to reverse the main conclusion.

**Verdict describes a specific claim or decision gate:**

- `PASS` — inspected evidence supports the bounded inference and planned use.
- `CONDITIONAL` — informative only after named repair, sensitivity analysis, or explicit claim downgrade.
- `STOP` — do not make the requested claim because a required identity, design, evidence, or validation
  condition is absent or contradicted.

Do not translate `P0/P1/P2` into `PASS/CONDITIONAL/STOP` mechanically. A P1 reporting problem can accompany
a PASS-quality bounded association; one P0 identity failure can STOP a mechanistic headline.

Other workflow fields remain separate: `must-fix / should-fix / consider` is an editorial obligation;
`W-LEDGER-READY / W-REVISE / W-HANDOFF-READY / W-POLISH-READY / W-RETURN-TO-LEDGER` is a writing-workflow state; and
`VERIFIED / PARTIAL / NOT ADDRESSED / MADE WORSE / NOT VERIFIABLE` is revision completion. None is a
fourth scientific verdict or a numerical score.

## Diagnostic order

Audit in this order and stop downstream storytelling when an upstream gate fails:

1. **Question and estimand:** population, contrast, endpoint, time, inferential unit, claim and decision.
2. **Identity and provenance:** patient, lesion, sample, block/section, region, time and treatment chain.
3. **Measurement validity:** imaging stability, assay capability, QC, preanalytics and attrition.
4. **Independence and design:** biological versus technical replication, nesting, pairing and repeated measures.
5. **Leakage and confounding:** train/test separation, batch/site/scanner, volume, subtype, treatment and selection.
6. **Analysis integrity:** model compatibility, multiplicity, uncertainty, baselines, calibration and sensitivity.
7. **Cross-scale bridge:** physical image source, tissue architecture, cell source, molecular program and time scale.
8. **Discrimination and validation:** competing explanations, negative controls, independent/orthogonal evidence,
   transportability and out-of-distribution behavior.
9. **Claim and writing:** evidence grade, maximum wording, denominator, limitations and reproducible reporting.

## Immediate STOP conditions

- Broken or unverifiable patient/lesion/sample/coordinate identity for the claimed linkage.
- Cells, spots, tiles, sections, images, reads, or technical replicates treated as independent patients.
- Outcome, feature, batch, or adjacent-sample leakage into selection, harmonisation, tuning, or validation.
- Exposure/condition is perfectly confounded with site, batch, treatment, or acquisition, with no identifying data.
- Generated, imputed, deconvolved, mapped, or predicted values presented as direct measurement.
- Regional co-localization claimed at a scale finer than tissue sampling or registration uncertainty permits.
- Mechanism or causality claimed from association, enrichment, proximity, saliency, attention, trajectory, or
  communication scores without evidence that distinguishes alternatives.
- A treatment effect claimed from a one-arm responder comparison without a valid treatment contrast.
- Differential treatment benefit or effect modification claimed without a prespecified
  biomarker-by-treatment interaction and absolute effects by biomarker level.
- Validation cohort overlaps development data or the supposedly locked model was refit to validation outcomes.

## Finding and repair contract

For every material finding report:

`finding ID | lens | severity | obligation | typed evidence anchor | problem | governing criterion |
scientific consequence | claim/gate verdict | claim if unresolved | minimum feasible repair | optional
stronger route | cost/trade-off | observable closure evidence | confidence/scope limit`

Keep genuine strengths in a separate evidence-anchored list without weakness severity. A missing item
uses an `absence` anchor that names where it should appear and which surfaces were checked. Scientific
relevance, target-venue relevance and submission readiness are separate judgements.

When a claim receives `STOP`, do not end at rejection. Return:

`blocked question -> blocking reason -> nearest answerable question -> minimum new evidence needed to restore
the original question -> wording currently allowed -> smallest executable next step`

Preserve valid analyses explicitly. A repair must name its required input and completion criterion; “add more
validation,” “use spatial,” or “try a better model” is not an executable repair.
