# Weak-result pivot — what to do when the headline number is small

The study is done and the result is modest (AUC 0.68, C-index 0.65, no significant
association). This is the most common crisis in imaging research — and it has defensible
exits. Pick **one** primary exit; stacking pivots reads as fishing.

## Step 0 — verify the weakness is real, not a fixable defect

Before pivoting, audit for defects that can suppress performance and are legitimately
fixable **once**, without re-mining:

- Leakage-free but **underpowered**? (event count / EPV → `radiology-stats/sample-size.md`)
- Noisy reference standard or inconsistent endpoint ascertainment?
- Model too complex for the cohort (variance, not bias)?
- Preprocessing/harmonisation error (e.g. ComBat removing the biology)?
- A threshold/calibration problem rather than a discrimination problem?

If a defect is found, fix it once, pre-specify the corrected analysis, and record the change
in the deviation log (`radiology-stats/analysis-hierarchy-and-missingness.md`). If the
weakness survives an honest pipeline, choose an exit below.

## The five exits

| # | Exit | Enough evidence | Claim shape |
|---|---|---|---|
| 1 | **Methodology / reproducibility contribution** | A documented, rerunnable pipeline with fair baselines and shared artifacts (parameter file, splits, code); the contribution is the method + honest evaluation, not the AUC | "We present a reproducible pipeline/benchmark; performance was modest and is reported transparently as a reference baseline." |
| 2 | **Generalisation failure as the finding** | Multi-center data with per-center performance, a shift diagnosis (population vs protocol — `validation-strategy.md`), and a harmonisation sensitivity analysis | "Performance did not transport across centers; we characterise where and why, and quantify the harmonisation effect." |
| 3 | **Pre-specified subgroup** | The subgroup was declared before unblinding, has a biological rationale, and the **interaction test** is significant — "significant in one subgroup only" does not qualify (→ `radiology-stats` subgroup discipline) | "A pre-specified interaction suggested differential performance in [subgroup]; hypothesis-generating." |
| 4 | **Incremental-value reframe** | The imaging score alone is weak but adds to the clinical model, shown with the full nested-comparison package (ΔAUC/LRT, calibration, DCA ± auxiliary NRI/IDI) → `radiology-stats/incremental-value.md` | "Alone the score discriminated modestly, but it improved risk stratification over the clinical model (net-benefit gain across thresholds …)." |
| 5 | **Honest negative / feasibility downgrade** | A clean, leakage-free, adequately powered attempt at a question the field cares about | "In this adequately powered cohort, [features/model] did not predict [endpoint]; this bounds the expected value of [approach]." |

## Rules that keep the exit honest

- **One primary exit.** Everything else is secondary and labelled so.
- **No re-mining.** Cycling through endpoints, subgroups, thresholds, or feature sets until
  something turns significant — then presenting it as the primary analysis — is HARKing, and
  it is what PROBAST / TRIPOD+AI reviewers are trained to catch.
- **Downgrade the claim, not the evidence.** A feasibility-level claim on solid data beats a
  strong claim on tortured data (verdict wording → `feasibility-triage.md`).
- A negative result still gets the full honest report: discrimination, calibration, CIs, and
  the deviation log. A null result reported well is citable and protects the field from
  publication bias.

## Statement templates (fill from real output)

- Methodology: *"We developed an IBSI-compliant, openly documented pipeline and report its
  performance transparently; discrimination was modest (AUC 0.6x; 95% CI: …) and we release
  the pipeline, splits, and parameter file as a reusable benchmark."*
- Generalisation failure: *"The model performed well internally (AUC 0.8x) but did not
  transport to center B (AUC 0.6x); calibration drift and scanner-protocol strata identified
  [cause] as the dominant shift."*
- Subgroup: *"A pre-specified treatment-by-subgroup interaction was significant (P = .0x);
  the subgroup effect is hypothesis-generating and requires independent confirmation."*
- Incremental value: *"Although the imaging score alone discriminated modestly (AUC 0.6x),
  adding it to the clinical model improved calibration and net benefit across threshold
  probabilities of 0.1x–0.3x (full package in Table [x])."*
- Honest negative: *"Despite adequate power ([N] events), neither hand-crafted nor deep
  imaging features predicted [endpoint] beyond clinical variables; we report the null result
  with full calibration and confidence intervals."*

## Output pattern

```text
Weakness verified as real: [yes/no — defect found and fixed once: …]
Chosen exit: [1–5, one only]
Evidence assembled: [per the table]
Downgraded claim: [the exact sentence]
Secondary/exploratory labels: [what is not primary]
Deviation log updated: [yes]
```
