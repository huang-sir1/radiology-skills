# Prospective / real-world validation & workflow integration

The strongest evidence short of a trial. Plan the design, the workflow position, and ongoing
monitoring — and bound the claim to the evidence actually obtained.

## Validation strength ladder (restate the honest claim)

1. Retrospective internal — weakest; no clinical claim.
2. Retrospective external/temporal — generalisability, still not utility.
3. **Reader study** — radiologist impact under controlled conditions.
4. **Prospective validation** — applied to a future cohort under the intended workflow.
5. **Real-world evidence (RWE)** — performance in routine practice, unselected population.
6. **Prospective randomised (trial)** — highest; CONSORT-AI / SPIRIT-AI (→ radiology-reporting).

Mark which level the study reaches; the claim cannot exceed it.

## Prospective design essentials

- Pre-register the protocol and primary endpoint.
- Define the enrolment population (unselected vs criteria) and prevalence.
- Freeze the model; lock the pipeline and threshold before enrolment.
- Define outcome ascertainment uniform across the cohort.

## PACS/RIS workflow integration

- Where the output appears (PACS overlay, RIS field, worklist priority, structured report).
- Latency, failure modes, and the fallback when the model abstains or errors.
- Human-in-the-loop: how the radiologist sees, accepts, or overrides the output.
- Automation bias and deskilling risks — and how the design mitigates them.

## Monitoring & drift (post-deployment)

- Track performance and **calibration drift** over time and across scanners/sites.
- Define triggers for recalibration/retraining and who is responsible.
- Log failures and out-of-distribution inputs.

## Claim ladder output

```
Evidence obtained:   [level on the ladder]
Licensed claim:      [what can honestly be said]
Not yet supported:   [claims requiring a higher level]
Next step to climb:  [reader study / prospective / RWE / trial]
```

## Reporting sentence

*"The frozen model was validated prospectively on consecutively enrolled patients (n=…) under the
intended PACS workflow; performance and calibration were monitored across sites. The evidence
supports [assistive use under radiologist oversight]; autonomous use is not claimed."*
