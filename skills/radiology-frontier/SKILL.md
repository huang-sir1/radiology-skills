---
name: radiology-frontier
description: "Find publishable frontier directions and innovation points for imaging-AI / radiomics / radiogenomics research, grounded in the publication patterns of high-impact journals (Radiology, Radiology: AI, Lancet Digital Health, Lancet Oncology, Nature Medicine, Nature Communications, npj Digital Medicine, npj Precision Oncology, eClinicalMedicine, Cell Reports Medicine). Use when the user asks for frontier directions, innovation points, hot vs suitable topics, \"近三年前沿方向\", \"创新点\", \"what's novel in imaging AI\", or wants to know the evidence/publication-pattern basis behind a recommendation (\"有什么文献依据\", \"证据\"). Translates trends (foundation models, self-supervised, vision-language, multimodal fusion, longitudinal, weak/federated learning, radiogenomics) into executable research questions matched to the user's actual data. Encodes publication-pattern heuristics, not a fabricated citation list — routes live verification to radiology-search and never invents PMIDs/DOIs."
---

# Frontier Directions & Evidence Layer

Use this skill to turn "what's hot in imaging AI" into **a publishable question matched to the
user's data** — and to expose the **publication-pattern evidence** behind each recommendation.
It is the strategic front of the chain: before designing (→ radiology-design), decide *what is
worth doing and likely to be accepted at a high-impact venue*.

## Core stance

- **Frontier ≠ feasible for you.** A direction is only useful if the user's data can actually
  carry it. Always test a trend against their disease, modality, n, centers, labels, and omics.
- **Evidence over vibes.** Recommendations are grounded in *how top journals actually publish*
  — design patterns, validation expectations, and what each venue rewards — not in slogans.
- **Patterns are durable; specific papers are not.** This skill encodes **publication-pattern
  heuristics** (the kinds of studies that get into each journal and the methodological bar
  they meet). It does **not** ship a fixed citation list. Concrete recent papers must be
  retrieved and verified **live** (→ radiology-search); never cite a PMID/DOI from memory.
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

## Workflow

1. **Read the data** — disease, modality, n, centers, labels, follow-up, omics availability
   (reuse the inventory from `radiology-design` if present).
2. **Scan themes** (frontier-themes.md) and **filter by fit** — for each candidate direction,
   state the data prerequisites and whether the user meets them. Reject poor fits explicitly.
3. **Ground in evidence** (evidence-layer.md) — for each surviving direction, state the
   publication pattern (what kind of study, what validation, which venues) and the
   methodological bar it must clear. Flag every concrete claim that needs **live verification**.
4. **Convert to questions** (idea-to-question.md) — turn the best 2–4 directions into specific
   research questions with endpoint, comparator, and the minimum evidence to be competitive.
5. **Trigger live search** — hand the chosen direction to `radiology-search` to retrieve and
   verify current seed papers (PMID/DOI) and confirm the gap is still open.
6. **Return** a ranked shortlist: direction → fit → evidence pattern → executable question →
   target-venue tier → what to verify now.

## Output contract

1. **`Data-fit summary`** — the inventory and the binding constraint, reused or restated.
2. **`Frontier shortlist`** — ranked directions, each with: fit (yes/conditional/no + reason),
   the publication-pattern evidence, and the methodological bar.
3. **`Executable questions`** — 2–4 concrete questions (endpoint, comparator, minimum evidence),
   each mapped to a candidate venue tier (→ radiology-journal).
4. **`Hot-but-unsuitable`** — trendy directions to avoid for this data, with the reason.
5. **`Verify now`** — the explicit list of claims/papers to confirm via live search today
   (handed to `radiology-search`); nothing here is presented as already-verified.

## Quality bar

A good frontier read sounds like a mentor who reviews for these journals: it knows what each
venue keeps publishing and why, matches the trend to the user's real data, names the directions
that are fashionable but wrong for them, and never invents a citation to sound current.

## Handoffs

- Turn the chosen direction into a full design → `radiology-design`.
- Retrieve & verify current seed literature / confirm the gap → `radiology-search`.
- Which journal tier the question targets → `radiology-journal`.
- Method-specific feasibility → `radiology-radiomics` / `radiology-deep-learning` /
  `radiology-radiogenomics`.
- Citation export of verified seeds → `radiology-citation`.
- This skill advises on research strategy; specific recent claims must be verified live.
