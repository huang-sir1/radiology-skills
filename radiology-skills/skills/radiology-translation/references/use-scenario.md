# Clinical-use scenario

Define where the model acts before designing anything else; it fixes the output, threshold, and
error costs.

## Pathway position → implications

| Scenario | Output | Dominant error cost |
|---|---|---|
| **Screening** | Risk flag on an unselected population | False negatives (missed disease); low prevalence inflates false positives |
| **Triage / worklist** | Prioritisation / urgency | Missed urgent cases; alert fatigue from false positives |
| **Diagnosis (rule-in/out)** | Probability / class | Rule-out: false negatives; rule-in: false positives |
| **Staging / subtyping** | Category | Mis-stage → wrong treatment |
| **Prognosis** | Risk / stratum | Over/under-treatment from miscalibration |
| **Treatment-response** | Response probability | Continuing a futile therapy / stopping an effective one |
| **Surveillance** | Change detection | Missed progression; false alarms |
| **MDT / report aid** | Structured suggestion | Automation bias; deskilling |

## Define the output explicitly

- Risk score, discrete stratum, segmentation mask, heatmap/saliency, or report-assist text.
- Who consumes it (radiologist, referring clinician, MDT) and what action follows.
- Whether a human is in the loop (assistive) or not (autonomous) — changes the evidence bar.

## Error-cost statement

- State the consequence of a false positive and a false negative *in this scenario*.
- This drives threshold choice (→ threshold-to-action.md) and the net-benefit framing.

## Output

```
Pathway position:
Population / prevalence:
Output type + consumer + downstream action:
Human-in-the-loop? assistive / autonomous:
Cost of false positive / false negative:
```
