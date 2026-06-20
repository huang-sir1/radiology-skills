# Threshold-to-action mapping & net benefit

An operating point only means something when it triggers an action with a known cost. Tie them
together and quantify with decision-curve analysis.

## Map each threshold to an action

```
Threshold → predicted positive → action (e.g. biopsy, recall, escalate, treat)
          → predicted negative → action (e.g. routine follow-up, discharge)
```

- Choose the threshold on **derivation/training** data, never the test set.
- Rule-out tools favour sensitivity; rule-in tools favour specificity (set by the use scenario).

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
- It answers "does using the model at clinically plausible thresholds do more good than harm?" —
  the question AUC cannot.
- Report net benefit over the range of thresholds a clinician might use, not a single point.
- Computation → `radiology-stats`; plot → `radiology-figure`.

## Calibration is a prerequisite

- A miscalibrated risk model makes threshold-based decisions wrong even with good discrimination.
- Report calibration (slope/intercept, plot) before using probabilities for actions.

## Reporting sentence

*"At the predefined operating point (sensitivity 0.92), a positive result triggered [action];
decision-curve analysis showed positive net benefit across threshold probabilities of 5–30%
relative to treat-all and treat-none, with the model well-calibrated (calibration slope 0.97)."*
