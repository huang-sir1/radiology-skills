---
name: radiology-writing
description: "Draft or rebuild Radiology (RSNA) manuscript sections from author-provided results, figures, notes, or Chinese drafts — the structured abstract, the one-sentence Summary statement, the Key Results box (up to 3 results, up to 75 words), Introduction, Materials and Methods, Results, and a structured Discussion. Use when the user wants to write or restructure imaging-research prose (not just polish it), especially for AI/radiomics/radiogenomics studies. Builds the argument from the evidence, enforces the Radiology manuscript shape and word/figure limits, and never invents data, metrics, or citations."
---

# Radiology-Style Manuscript Writing

Use this skill to **construct** imaging-research prose — argument first, then sentences —
in the exact shape _Radiology_ requires. It is for drafting and restructuring, not only
polishing (for sentence-level polish use `radiology-polishing`).

## Core stance

- **Author evidence first.** Never invent results, metrics, p-values, cohort numbers,
  citations, mechanisms, or limitations. Missing input → explicit placeholder or a question.
- **Write the argument before the sentences.** One-sentence claim → section architecture →
  paragraph jobs → prose.
- **Match the _Radiology_ shape.** Structured abstract, **Summary statement** (one sentence),
  **Key Results** (≤ 3, ≤ 75 words), structured Discussion, tight word/figure limits.
- **Bound the claim.** Ambitious but evidence-bounded; calibrate verbs to evidence
  (demonstrate → suggest → may reflect).
- **Reporting-aware.** Every Methods/Results element should satisfy the relevant checklist
  item (CLAIM/TRIPOD+AI/CLEAR/STARD) — cross-check with `radiology-reporting`.

## When to use

- Draft/rebuild any section: title, structured abstract, Summary statement, Key Results,
  Introduction, Materials and Methods, Results, Discussion.
- Turn Chinese lab notes / mixed drafts into submission-ready English.
- Restructure a rejected draft to the _Radiology_ argument shape.

## When to open extra files

| File | Open when |
|---|---|
| [references/article-architecture.md](references/article-architecture.md) | Section order, argument flow, and the _Radiology_ manuscript skeleton |
| [references/structured-abstract.md](references/structured-abstract.md) | Writing the structured abstract + Summary statement + Key Results box |
| [references/methods.md](references/methods.md) | Materials and Methods for imaging/AI/radiomics studies (what must appear, in order) |
| [references/results.md](references/results.md) | Results narrative: flow, performance with CIs, comparisons, validation |
| [references/discussion.md](references/discussion.md) | Structured Discussion (key-finding first → context → limitations → conclusion) |
| [references/chinese-author-workflow.md](references/chinese-author-workflow.md) | Notes are Chinese / mixed / lab-note style; translate intent and argument, not clause order |

## Intake (identify before drafting)

- **Section(s)** requested.
- **Study type**: diagnostic-accuracy, prediction model, radiomics, radiogenomics, reader
  study, observational, trial.
- **Core claim**: what the study actually shows.
- **Evidence**: cohorts (n, source, dates), metrics with CIs, comparisons, validation.
- **Boundary**: where the claim stops (single-centre? retrospective? prevalence?).
- **Limits**: target word/figure counts (verify against current author instructions).

If core claim, evidence, or boundary is missing, surface the gap and offer a scaffold with
placeholders rather than inventing content.

## Writing workflow

1. **One-sentence argument**: *"In [population/modality], we show [advance] using [approach],
   supported by [key result with CI], with [boundary]."*
2. **Pick the architecture** (article-architecture.md) by study type.
3. **Map each paragraph to one job**: context / gap / objective / design / cohort / technique
   / analysis / result / comparison / validation / interpretation / limitation.
4. **Draft from evidence outward** — keep claims next to the numbers that support them.
5. **Calibrate verbs** to evidence; remove unsupported novelty/"first" claims.
6. **Fit the _Radiology_ shape** — abstract headings, Summary statement, Key Results,
   structured Discussion.
7. **Self-review** against the relevant reporting checklist; flag unmet items.

## Section defaults

- **Title** — concrete: population/condition + modality/method + finding/role. State AI/
  radiomics if central. Avoid slogans and "novel."
- **Structured abstract** — Background → Purpose → Materials and Methods → Results →
  Conclusion; report design, cohort sizes/dates, primary metric(s) **with CIs**, a bounded
  conclusion. (structured-abstract.md)
- **Summary statement** — a single declarative sentence of the main finding.
- **Key Results** — up to **3** results/conclusions, **≤ 75 words**, with summary data; don't
  repeat the Summary statement; avoid vague language and abbreviations.
- **Introduction** — field/clinical stakes → specific gap → objective/hypothesis. Short; no
  results dump.
- **Materials and Methods** — design + ethics/registration → participants/flow → imaging
  technique → image analysis/reference standard/readers → model/feature pipeline →
  statistical analysis. (methods.md)
- **Results** — patient flow + characteristics → primary performance with CIs → comparisons →
  validation/subgroups. Past tense, quantitative. (results.md)
- **Discussion** — **first paragraph = concise summary of key findings**, then relation to
  prior work, then **limitations**, then a bounded conclusion. (discussion.md)

## Output format

1. **`Draft`** — the requested prose in _Radiology_ shape.
2. **`Section outline`** — 3–7 compact bullets (for a full section).
3. **`Claim–evidence map`** — `Claim | Evidence (with CI) | Status: supported / needs input`.
4. **`Assumptions / missing inputs`** — only material gaps.
5. **`Reporting check`** — checklist items this draft does/doesn't satisfy (→ radiology-reporting).

For Chinese notes: polished English first, then brief Chinese notes on structural choices.

## Handoffs
- Sentence-level polish / house style → `radiology-polishing`.
- Statistics/CIs/tests behind the numbers → `radiology-stats`.
- Checklist compliance → `radiology-reporting`.
- Figures/legends → `radiology-figure`.
