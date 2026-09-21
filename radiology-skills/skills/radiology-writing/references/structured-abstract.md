# Structured abstract + Summary statement + Key Results

## Structured abstract (headings)
- **Background** — 1–2 sentences: the clinical/scientific gap (not a textbook intro).
- **Purpose** — the specific objective ("To evaluate whether …").
- **Materials and Methods** — design (retro/prospective), dates, setting; participants (n,
  inclusion); reference standard; key technique; **primary analysis**; ethics/registration.
- **Results** — cohort (n, key demographics with a measure of spread); the **primary
  outcome with effect size + 95% CI + p**; key comparison/validation. Numbers, not adjectives.
- **Conclusion** — one or two sentences, bounded to the evidence; no new data; no hype.

Report past tense; include CIs; avoid undefined abbreviations. (Leading-zero style is venue
house style — the _Radiology_ family drops the leading zero for statistics bounded by 1
(.88, not 0.88); `radiology-polishing/stat-reporting.md` enforces it at polish stage.)

### Template
> **Background:** [gap]. **Purpose:** To [objective]. **Materials and Methods:** In this
> [design] study ([dates]), [n] [participants] ([selection]) were [analysed] with [technique];
> [reference standard]; [primary analysis]. **Results:** Among [n] ([demographics]), [primary
> result: estimate, 95% CI, P]; [comparison/validation result]. **Conclusion:** [bounded
> conclusion].

## Summary statement (one sentence)
A single declarative sentence capturing the main finding — concrete and bounded.
> *A deep-learning model detected [finding] on [modality] with sensitivity 0.91 and
> specificity 0.84, comparable to subspecialist radiologists in an external test cohort.*

## Key Results (≤ 3 items, ≤ 75 words total)
- Up to three results/conclusions **with summary data**; declarative; no abbreviations; no
  vague language ("good," "promising"); do **not** repeat the Summary statement. (These feed
  the visual abstract.)
- Include **study type, n, disease/condition, and modality**; report percentages, ratios,
  and P values as summary data. The RSNA *Scientific Style Guide* presents Key Results
  **without 95% CIs** (CIs belong to the abstract Results and the body); the author
  instructions say only "including summary data" — when the two sources pull apart, follow
  the Style Guide and keep CIs out of Key Results.
> - In [n] patients with [disease] on [modality], the model's AUC was .88 (P = .01 vs readers).
> - Performance held in external validation (AUC .85).
> - The model exceeded readers in sensitivity (91% vs 82%; P = .01).

## Common abstract failures
Vague Purpose; no CIs; conclusion broader than the data; abbreviations in Key Results;
prevalence omitted so PPV/NPV are uninterpretable; "first" claims; reader-comparison stated
without the statistic.

For shape only, see the [fully synthetic worked example](examples/abstract-example.md). Its cohort,
numbers and findings are invented teaching placeholders and must never be transferred into a real
manuscript or treated as evidence.
