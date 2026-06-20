# From trend to an executable, submittable research question

A theme becomes a study only when it is a **specific question** with an endpoint, a comparator,
and a defensible increment. This file converts frontier directions into that form.

## The conversion template

```
Trend:                [e.g. foundation-model transfer]
Clinical question:    [the decision it informs]
Population / modality:[who, what imaging]
Specific increment:   [the one-sentence advance over the best current approach]
Primary endpoint:     [estimand + metric]
Comparator:           [radiologist / clinical model / prior biomarker / SOTA]
Minimum evidence to compete: [validation type, calibration/DCA, reader/external, etc.]
Target venue tier:    [→ radiology-journal]
Open-gap check:       [confirm still open — → radiology-search]
```

## Writing the "specific increment" (the hardest line)

A competitive increment is concrete and falsifiable. Compare:

- ✗ "We apply a novel deep-learning model to predict outcome." (no increment)
- ✓ "We test whether a foundation-model encoder fine-tuned on 3 centers transports to an unseen
  4th center better than a task-trained CNN, with calibration maintained."

If you cannot state the increment in one sentence naming the baseline it beats and the condition
under which it beats it, the idea is not yet a question.

## Novelty framing (defensible, not superlative)

- Frame novelty as a **specific gap** ("no prior study validates X across vendors with
  calibration"), not "first/novel" — superlatives invite the reviewer to find a counterexample.
- A gap claim is only safe **after** a live check that it is still open (→ radiology-search).
- Increment can be in **question, data, method, validation, or mechanism** — be explicit which.

## Rank the shortlist

Score each candidate question on:

1. **Fit** — data can carry it (prerequisites met).
2. **Gap** — still open and worth answering (verified live).
3. **Reachable bar** — the user can produce the minimum evidence to compete at the target tier.
4. **Increment clarity** — the one-sentence advance exists.

Promote 2–4 questions that score well on all four; park the rest with the reason.

## Handoff

- Full design of the chosen question → `radiology-design`.
- Venue tiering of the question → `radiology-journal`.
- Live confirmation of gap + seed papers → `radiology-search` → `radiology-citation`.
