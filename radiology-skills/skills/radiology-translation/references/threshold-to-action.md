# Threshold-to-action mapping & net benefit

An operating point only means something when it triggers an action with a known cost. Tie them
together and quantify with decision-curve analysis.

## Map each threshold to an action

```
Threshold → predicted positive → action (e.g. biopsy, recall, escalate, treat)
          → predicted negative → action (e.g. routine follow-up, discharge)
```

- Prespecify or select the threshold within the authorized development/internal-validation route,
  then freeze it before the final evaluation set. If a separate calibration/adaptation set is used,
  name it and do not relabel it as untouched external testing.
- Choose threshold consequences from the use scenario. “Rule-out favours sensitivity” and “rule-in
  favours specificity” are heuristics, not substitutes for prevalence, calibration, downstream
  actions, harms, resource limits and stakeholder values.

## Consequences table

| | Action taken | Consequence |
|---|---|---|
| True positive | [action] | benefit |
| False positive | [action] | cost (over-treatment, anxiety, resource) |
| True negative | [action] | benefit (avoided harm) |
| False negative | [action] | cost (missed disease) |

Fill this in for the specific scenario — it justifies the threshold.

## Net benefit / decision-curve analysis (DCA)

- DCA plots net benefit across **threshold probabilities**, comparing the model to
  treat-all / treat-none.
- It estimates model-based net benefit relative to named alternatives under explicit threshold,
  exchange-rate and action assumptions. It does not directly observe whether patient benefit exceeds
  harm, establish cost-effectiveness or replace a clinical-impact study.
- Report net benefit over the range of thresholds a clinician might use, not a single point.
- Computation → `radiology-stats`; plot → `radiology-figure`.

## Calibration is a prerequisite

- A miscalibrated risk model makes threshold-based decisions wrong even with good discrimination.
- Report calibration (slope/intercept, plot) before using probabilities for actions.

## Reporting sentence

*"At the predefined operating point (sensitivity 0.92), a positive result triggered [action];
decision-curve analysis showed positive net benefit across threshold probabilities of 5–30%
relative to treat-all and treat-none, with the model well-calibrated (calibration slope 0.97)."*
