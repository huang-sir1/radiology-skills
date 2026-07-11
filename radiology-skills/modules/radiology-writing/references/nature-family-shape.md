# Nature-family manuscript shape (Nature Medicine / Nature Biomedical Engineering / Nature Communications / npj Digital Medicine / Cell Reports Medicine, etc.)

Use this file instead of `structured-abstract.md`/`article-architecture.md` when the target is a
**Nature-portfolio-family** venue rather than _Radiology_. The argument-first discipline, the
claim–evidence map, and the integrity rules in the main `SKILL.md` are unchanged — only the
**shape** changes. Route by target venue before drafting; if the venue is undecided, draft the
_Radiology_ shape first (it is stricter) and ask which venue before finalising the abstract, since
rebuilding a structured abstract into an unstructured one is easy but not the reverse.

## Core shape differences (know these before drafting a word)

| Element | _Radiology_ shape (default, see structured-abstract.md) | Nature-family shape |
|---|---|---|
| Abstract | **Structured**: Background/Purpose/Materials and Methods/Results/Conclusion headings | **Unstructured**: one flowing paragraph, no headings |
| Abstract length | Verify current limit | Short and hard-capped — **Nature Medicine: ≤150 words**, unreferenced (verified current; other venues differ — verify live before finalising, e.g. Nature Communications/npj Digital Medicine/Nature Biomedical Engineering each set their own limit) |
| References in abstract | Not used | **Not permitted** |
| Abbreviations in abstract | Defined at first use | Avoid entirely except universally recognised ones (DNA, RNA, MRI); spell out the rest |
| Summary statement (1 sentence) | **Required** | Does not exist as a named element — fold the equivalent single-sentence claim into the last sentence of the abstract instead |
| Key Results box (≤3, ≤75 words) | **Required** | Does not exist — some venues instead want a separate one-line **significance/teaser** for internal editorial use; ask the user for it only if the target venue requires one, don't invent the box |
| Title | Concrete, modality + finding | Often shorter and more declarative/punchy; still no "novel"/"first" without a live literature check (→ radiology-frontier/radiology-search) |
| Main-text word limit | Verify current limit | Typically tighter than _Radiology_ and **excludes** Methods (see below) — verify live per venue |
| Methods placement | Inline, ordered section (see methods.md) | Frequently placed **after References**, online-only, not counted in the main word limit — still needs the same content (design, cohort, technique, model/statistics) and the same reporting-guideline coverage; check the specific venue's current instructions for placement |
| Display items in main text | Figures/tables within journal limits | A **small number of main display items** (figures/tables); everything else goes to **Extended Data** (peer-reviewed, published) or **Supplementary Information** (not typeset) — verify the current cap live; hand off figure-count planning to `radiology-figure`/`nature-figure-spec.md` and `radiology-data` |
| Reference style | Author–year or numbered per _Radiology_ house style | Numbered, in order of first citation (Vancouver-style superscripts) — hand off to `radiology-citation`/`export-formats.md` |
| Statistics disclosure | Reported in Methods/Results prose | Prose **plus** a separate **Reporting Summary** for life-sciences submissions (→ `radiology-reporting/nature-reporting-summary.md`) |

## Abstract (unstructured, one paragraph)

Write it as a single paragraph that still does the same four jobs as the structured version, in
order, without headings — the reader should be able to find each job but not see a label:

1. **Context + gap** — one to two sentences on the clinical/scientific stakes and what's missing.
2. **What was done** — design, cohort (n, brief), technique/model in one clause each.
3. **What was found** — the primary result **with the effect size**; a CI can be tight/omitted only
   if the word budget truly forces it, but never omit the point estimate.
4. **What it means** — one bounded closing sentence carrying the claim (this is the sentence that
   does the job of the _Radiology_ Summary statement — it must stand alone if quoted).

No sentence should require the reader to have read a heading to know what job it's doing — each
sentence's own wording should make its role obvious.

### Template
> [Context/gap in 1 sentence]. Here we [what was done: design, n, technique/model], and show that
> [primary result with effect size]. [Bounded closing sentence carrying the claim, e.g. generalisation
> across an external cohort, or the boundary of the claim].

### Worked example (illustrative — not real data; same underlying study as the structured-abstract.md worked example)
> Preoperative identification of IDH mutation status in glioma informs management, but tissue
> sampling is invasive and may miss tumour heterogeneity. Here we developed an MRI radiomic model
> in 314 patients with newly diagnosed glioma and validated it in an independent external cohort of
> 96 patients, achieving an area under the curve of 0.85 with good calibration. These results show
> that a noninvasive, externally validated imaging signature can stratify IDH status and support
> molecular risk assessment before tissue is available.

Keep the word count against the **specific target venue's current limit** — do not assume 150
words applies beyond Nature Medicine without checking (→ radiology-search / the venue's current
author instructions).

## Introduction / Discussion pacing

- **Introduction** can open one step further back — broader scientific or clinical significance
  before narrowing to the specific gap — but must still reach a precise, falsifiable objective by
  the end; it should not stay broad throughout. Length is typically shorter than a _Radiology_
  Introduction because the significance work is partly done by the unstructured abstract.
- **Discussion** keeps the same discipline as `discussion.md` (key finding first, no new results,
  honest limitations, bounded conclusion) — Nature-family venues do **not** relax the limitations
  requirement; if anything, external/prospective evidence and fairness/subgroup performance are
  scrutinised harder (→ `radiology-deep-learning/interpretability-uncertainty.md` for AI-specific
  claims, `radiology-translation` for clinical-utility claims).
- Avoid the _Radiology_-specific labels ("Summary statement", "Key Results") anywhere in the prose
  itself — an editor will read past them, but they signal the wrong house style at a glance.

## Methods (content unchanged, placement and framing differ)

The content requirements are identical to `methods.md` — design/ethics, participants, technique,
reference standard/readers, model/feature pipeline, statistical analysis — reporting-guideline
coverage (CLAIM/TRIPOD+AI/CLEAR/STARD, → `radiology-reporting`) does not relax because Methods runs
online-only. Write it with clear subheadings (Nature-family Methods sections are typically broken
into short, labelled subsections rather than one continuous block) and keep it reproducible enough
to stand alone from the main text.

## Output format (adapts the main SKILL.md contract for this shape)

1. **`Draft`** — the unstructured abstract + requested sections, Nature-family shape.
2. **`Word budget`** — running count against the target venue's limit (flag if over; verify the
   limit live if not already confirmed for this venue).
3. **`Claim–evidence map`** — unchanged from the main workflow.
4. **`Display-item plan`** — which results go to main figures/tables vs Extended Data/Supplementary
   Information (→ `radiology-figure/nature-figure-spec.md`, `radiology-data`).
5. **`Reporting check`** — checklist items **plus** whether a Reporting Summary is required for this
   venue (→ `radiology-reporting/nature-reporting-summary.md`).

## Handoffs
- Figure sizing, panel-letter case, Extended Data figure limits → `radiology-figure` /
  `references/nature-figure-spec.md`.
- Source Data, Extended Data vs Supplementary Information, data/code as a condition of publication
  → `radiology-data`.
- Reporting Summary / Editorial Policy Checklist → `radiology-reporting` /
  `references/nature-reporting-summary.md`.
- Numbered reference style, export format → `radiology-citation`.
- Venue fit and current word/figure limits (verify live) → `radiology-journal`.
