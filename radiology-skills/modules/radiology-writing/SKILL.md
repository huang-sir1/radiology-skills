---
name: radiology-writing
description: "Draft or rebuild imaging-AI / radiomics / radiogenomics manuscript sections for Radiology (RSNA), Nature-portfolio/npj, European Radiology, NEJM, Science, or Lancet-family style from author-provided results, figures, notes, or Chinese drafts. Enforces the target venue's manuscript shape: Radiology Summary/Key Results, Nature-style broad scientific narrative, European Radiology key points/clinical relevance, NEJM four-part clinical abstract and SAP rigor, Science compact display-item story, or Lancet-series Research in context and AI/data transparency using The Lancet Digital Health guide as the default proxy. Use when the user wants to write or restructure imaging-research prose, not just polish it. Never invents data, metrics, or citations."
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
| [references/nature-family-shape.md](references/nature-family-shape.md) | Target is Nature Medicine / Nature Biomedical Engineering / Nature Communications / npj Digital Medicine / Cell Reports Medicine etc. — unstructured abstract, no Summary statement/Key Results box, different Methods placement |
| [references/argument-spine-and-stage-gates.md](references/argument-spine-and-stage-gates.md) | Full manuscript rebuild, rejected-paper rescue, unclear contribution, high-impact submission, or a draft whose story/figures/results do not yet lock together |
| [references/journal-family-writing-style.md](references/journal-family-writing-style.md) | Target journal family is known, or the user supplied author-guide PDFs/classic papers and wants the manuscript to carry that venue's writing style |

## Intake (identify before drafting)

- **Target venue/shape**: _Radiology_-family (structured abstract, Summary statement, Key
  Results — default) or Nature-family (unstructured abstract, no Summary statement/Key Results
  → `references/nature-family-shape.md`). If undecided, draft the _Radiology_ shape first and
  confirm venue before finalising the abstract (→ `radiology-journal`).
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

0. **For full manuscripts or high-impact rebuilds**, open
   `argument-spine-and-stage-gates.md` and establish the project context, contribution-first
   gate, and results-as-validation map before drafting long prose.
0. **For target-venue writing taste**, open `journal-family-writing-style.md` after confirming
   the venue family; use it to adjust article shape, title/abstract rhythm, key points, and
   clinical relevance language.
1. **One-sentence argument**: *"In [population/modality], we show [advance] using [approach],
   supported by [key result with CI], with [boundary]."*
2. **Pick the architecture** (article-architecture.md) by study type.
3. **Map each paragraph to one job**: context / gap / objective / design / cohort / technique
   / analysis / result / comparison / validation / interpretation / limitation.
4. **For full sections**, draft the topic-sentence chain first. If the claims do not flow,
   revise the chain before writing full paragraphs.
5. **Draft from evidence outward** — keep claims next to the numbers that support them.
6. **Calibrate verbs** to evidence; remove unsupported novelty/"first" claims.
7. **Fit the _Radiology_ shape** — abstract headings, Summary statement, Key Results,
   structured Discussion.
8. **Self-review** against the relevant reporting checklist; flag unmet items.

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
3. **`Topic-sentence chain`** — for full sections or major rewrites, the claim sequence before
   paragraph expansion.
4. **`Claim–evidence map`** — `Claim | Evidence (with CI) | Status: supported / needs input`.
5. **`Stage gates`** — for full manuscripts: contribution gate, results-as-validation gate,
   citation/figure/reporting gates that are passed or still open.
6. **`Venue style check`** — if the target family is known: abstract shape, title/key-points
   logic, clinical relevance language, and any guide-derived limits or `VERIFY FROM GUIDE`.
7. **`Assumptions / missing inputs`** — only material gaps.
8. **`Reporting check`** — checklist items this draft does/doesn't satisfy (→ radiology-reporting).

For Chinese notes: polished English first, then brief Chinese notes on structural choices.

## Handoffs
- Sentence-level polish / house style → `radiology-polishing`.
- Statistics/CIs/tests behind the numbers → `radiology-stats`.
- Checklist compliance → `radiology-reporting`.
- Figures/legends → `radiology-figure`.
- Finding/verifying citations to support a claim in Introduction/Discussion → `radiology-citation`.
- Draft is complete and ready for a harsh read before submission → `radiology-prereview`.
