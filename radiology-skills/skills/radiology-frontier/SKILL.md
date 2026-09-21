---
name: radiology-frontier
description: "Identify evidence-grounded imaging frontiers and gaps; not design lock or journal choice."
---

# Frontier Directions & Evidence Layer

Use this skill to turn "what's hot in imaging AI" into **a publishable question matched to the
user's data** — and to expose the **publication-pattern evidence** behind each recommendation.
It is the strategic front of the chain: before designing (→ radiology-design), decide *what is
worth doing and likely to be accepted at a high-impact venue*.

## Core stance

- **Frontier ≠ feasible for you.** A direction is only useful if the user's data can actually
  carry it. Always test a trend against their disease, modality, n, centers, labels, and omics.
- **Scientific value before venue fit.** Rank the importance and answerability of the question,
  including independent validation, failure boundaries and informative negative results. A new
  architecture or a result that beats a baseline is not required for a valuable question.
- **Heuristics are hypotheses to check.** Venue patterns orient a search; they are not current
  editorial requirements or evidence that a topic remains open. Retrieve current scope and relevant
  papers before making a current frontier, novelty or venue-fit recommendation. Record source/date,
  task and study type; if retrieval fails, return a `PROVISIONAL_SHORTLIST` with unresolved claims.
- **Separate hot from suitable.** Name directions that are trendy but a poor fit for the data,
  and say why — steering away from a wrong direction is as valuable as suggesting a right one.
- **Bound novelty claims.** "First/novel" is a liability without a literature check. Frame
  innovation as a specific, defensible gap, not a superlative.
- **Integrity.** Never fabricate references, effect sizes, or "recent studies show…" claims.
  Mark anything that needs same-day verification.

## When to use

- "Give me frontier directions for [disease/modality] I can publish in the next 1–2 years."
- "找近三年的前沿方向和创新点" / "结合我的数据找创新点。"
- "Is [foundation models / self-supervised / VLM / multimodal / federated] right for my data?"
- "What's the evidence/publication-pattern basis for this recommendation?" / "有什么文献依据？"
- "Which top journals publish this kind of study, and what do they demand?"

## When to open extra files

| File | Open when |
|---|---|
| [references/frontier-themes.md](references/frontier-themes.md) | Surveying current themes (foundation models, SSL, VLM, multimodal fusion, longitudinal, weak/semi-supervision, domain adaptation, federated, generative, radiogenomics) and their data prerequisites |
| [references/evidence-layer.md](references/evidence-layer.md) | Explaining the publication-pattern evidence: what each high-impact journal rewards, the methodological bar, and how to verify with live search |
| [references/idea-to-question.md](references/idea-to-question.md) | Converting a trend into a concrete, executable, submittable research question; novelty framing |
| [references/ai-radiogenomics-frontier-map.md](references/ai-radiogenomics-frontier-map.md) | The user asks for radiology AI/radiogenomics directions over the next 12-24 months, or needs to choose among foundation models, SSL, VLM, multimodal fusion, federated learning, UQ/XAI, and radiogenomics |

## Workflow

1. **Read the data** — disease, modality, n, centers, labels, follow-up, omics availability
   (reuse the inventory from `radiology-design` if present).
2. **Scan themes** (frontier-themes.md) and **filter by fit** — for each candidate direction,
   state the data prerequisites and whether the user meets them. Reject poor fits explicitly.
3. **For AI/radiogenomics strategy**, open `ai-radiogenomics-frontier-map.md` and judge the
   idea against generalisability, supervision cost, multimodal fusion, trustworthy inference,
   external validation, and clinical-value evidence.
4. **Ground in current evidence** (evidence-layer.md) — retrieve relevant current primary literature
   and any material venue rules, then assess the gap and task-specific evidence needs. Separate
   verified findings from search hypotheses; do not require DCA or every reporting framework for
   every task. A failed search leaves the ranking provisional.
5. **Convert to questions** (idea-to-question.md) — turn the best 2–4 directions into specific
   research questions with endpoint, comparator, and the minimum evidence to be competitive.
6. **Add a falsification test** — for each leading idea, state the counter-hypothesis, the
   negative/control result that would weaken it, and the data needed to distinguish them.
7. **Close the search handoff** — use `radiology-search` when needed and carry its verified seed
   records and remaining coverage limits back into the recommendation. A referral alone does not
   establish that a gap or current venue preference was checked.
8. **Return** a ranked shortlist: direction → fit → evidence pattern → executable question →
   target-venue tier → what to verify now.

## Output contract

1. **`Data-fit summary`** — the inventory and the binding constraint, reused or restated.
2. **`Frontier shortlist`** — ranked directions, each with: fit (yes/conditional/no + reason),
   the publication-pattern evidence, and the methodological bar.
3. **`Executable questions`** — 2–4 concrete questions (endpoint, comparator, minimum evidence),
   each mapped to a candidate venue tier (→ radiology-journal).
4. **`Hot-but-unsuitable`** — trendy directions to avoid for this data, with the reason.
5. **`Counter-hypothesis/falsification`** — what alternative explanation or negative result
   would defeat each leading idea and how the study would test it.
6. **`Source status and verify now`** — current verified sources with locators/dates, unresolved
   claims and search coverage limits. Use `PROVISIONAL_SHORTLIST` when current evidence is absent;
   do not present a search handoff as a completed verification.

## Quality bar

A good frontier read sounds like a mentor who reviews for these journals: it knows what each
venue keeps publishing and why, matches the trend to the user's real data, names the directions
that are fashionable but wrong for them, and never invents a citation to sound current.

## Handoffs

- Turn the chosen direction into a full design → `radiology-design`.
- Retrieve & verify current seed literature / confirm the gap → `radiology-search`.
- Which journal tier the question targets → `radiology-journal`.
- Method-specific feasibility → `radiology-radiomics` / `radiology-deep-learning` /
  `radiology-radiogenomics`; these inform but do not replace `radiology-design`'s feasibility verdict.
- Citation export of verified seeds → `radiology-citation`.
- The direction fits a funding proposal better than (or in addition to) a paper right now →
  `radiology-grant`.
- This skill advises on research strategy; specific recent claims must be verified live.
