# Survival figures — KM integrity, numbers-at-risk, time-dependent discrimination

_Radiology_ reviewers read Kaplan-Meier panels closely. The two failure modes are (a) a
numbers-at-risk table that doesn't reconcile with the curve, and (b) "improved" discrimination
shown with a plain binary ROC when the endpoint is time-to-event. This file fixes both.

## KM internal consistency (the rule that ties the figure together)

A KM figure has three coupled elements that **must** agree:

1. **The curve** steps **down only at events**.
2. **Censoring tick marks** show where patients leave follow-up *without* an event.
3. **Numbers-at-risk** decrease because of **events *and* censoring**.

So if the curve is nearly flat (few events) but numbers-at-risk fall steeply, that drop is
*censoring* — and the **censoring ticks are the only on-curve cue that explains it**. Therefore:

> **Do not silently delete censoring ticks.** Removing every tick makes a flat curve sit above a
> plummeting at-risk row with nothing to explain the gap — it looks self-contradictory.

If ticks are too dense (large cohorts), **thin them, don't delete them**: cap the number drawn
per curve (e.g. ≤ 12–15, evenly/randomly sampled) so they still indicate censoring throughout.
This is purely cosmetic — KM estimate, P, HR, numbers-at-risk are always computed from **all**
patients.

### If a clean teaching figure truly needs no ticks
Some non-inferential/teaching figures want zero ticks. The only way to stay internally consistent
is the **complete-follow-up convention**: show numbers-at-risk as `N_group − cumulative events`
(declines by events only, matching the curve). Label it honestly ("assuming complete follow-up")
and keep the inferential statistics (log-rank, HR, C-index) on the **real, censoring-aware** data.
Accept a small (≤ ~3%) gap between the censoring-aware curve and at-risk/N. For a real submission,
prefer the standard: real numbers-at-risk **with** (thinned) censoring ticks.

## Numbers-at-risk table (do it like a top journal)

- A **separate sub-axes** under the plot (not text crammed into the curve), x-axis aligned to the
  KM time ticks.
- Header "**Number at risk**"; one row per group, row colour = curve colour.
- Print strata labels **once** on the far left (leftmost panel only when faceting cohorts).
- First column at t=0 equals the group n; values are **monotonically non-increasing** (assert it).

## Truncation & extension

- **Truncate the x-axis to the analysis horizon** (e.g. 5 years) — don't show a long sparse tail
  where few remain at risk and CIs explode.
- **Extend each curve flat to the last follow-up** (not just the last *event*). A group whose last
  event is at 3.5 y but who are followed to 5 y must show a flat line to 5 y, or the curve looks
  "cut short". (Standard estimators do this; verify your helper does too.)

## Per-panel annotations
Log-rank P; HR (95% CI) vs a stated reference (or per-group 5-yr survival % if a reference group is
near-zero events and the HR/CI is unstable → show survival % instead of an exploding HR);
faceting by cohort (training / internal test / external) with panel letters matching the case used
across the rest of the figure set (`api.md` `panel_letter()` — uppercase A/B/C for _Radiology_-family,
lowercase a/b/c for Nature-family, see `nature-figure-spec.md`; never mix the two). Put the stats in
a light semi-transparent box so they read over CI bands.

## Time-dependent (survival) discrimination, calibration, utility

For a time-to-event endpoint, do **not** use plain `sklearn` ROC/calibration on a binary label.

- **Time-dependent ROC / AUC (IPCW, cumulative/dynamic)** at fixed horizons (e.g. 3 & 5 y):
  cases = events by *t*, controls = event-free at *t*, weighted by inverse probability of
  censoring (KM of the censoring distribution). Report AUC(t) and the ROC at each horizon.
- **Survival calibration** at *t*: predicted risk `1 − Ŝ(t|x)` (Cox baseline via Breslow) vs
  observed `1 − KM(t)` within risk bins; plot against the diagonal.
- **Decision-curve analysis** at *t*: net benefit using `1 − Ŝ(t|x)` as predicted risk and KM for
  the observed event rate in the flagged subset; clip the y-axis to the decision-relevant region
  (the "treat-all" curve dives very negative and otherwise compresses the interesting part).

Helper code for all three (IPCW td-AUC/ROC, Breslow baseline survival, survival DCA) is in
`api.md`.

## Incremental-value framing (clinical + a new marker)

The standard imaging-AI survival story is *"does the new marker add to an existing clinical
model?"* Show it consistently:
- ROC/AUC at 3 & 5 y: **clinical** vs **clinical + marker** (same two colours everywhere).
- Calibration: both models near the diagonal.
- DCA: augmented model ≥ clinical across the threshold range.
- Curve/percentages must match the manuscript's C-index / NRI / IDI (computed in
  `radiology-stats`) — cross-check before export (`figure-set-consistency.md`).

## QA (survival panels)
- Curve flat-extended to last follow-up; x truncated to horizon.
- Censoring ticks present (thinned if dense) **or** complete-follow-up at-risk used and labelled.
- Numbers-at-risk: separate axes, monotone, t=0 = n, aligned to time ticks.
- Time-to-event discrimination uses **time-dependent** AUC/ROC, not binary.
- Same palette/roles as the rest of the figure set.

→ Effect sizes, IPCW formulas, NRI/IDI, C-index → `radiology-stats`. Cross-figure number checks →
`figure-set-consistency.md`.
