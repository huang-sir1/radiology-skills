# radiology-frontier

**Stage 1 — Scope & Design.** Find publishable frontier directions and innovation points,
grounded in how high-impact journals actually publish — and matched to the user's real data.

## What it does

- **Frontier shortlist** — surveys current themes (foundation models, self-supervised learning,
  vision-language, multimodal fusion, longitudinal/delta, weak/semi-supervision, domain
  adaptation, federated learning, generative, uncertainty/safety, radiogenomics, AI+reader) and
  filters each by whether the user's data can carry it.
- **Evidence layer** — explains the *publication-pattern* basis behind each recommendation: what
  Radiology, Radiology: AI, Lancet Digital Health/Oncology, Nature Medicine, Nature
  Communications, npj Digital Medicine/Precision Oncology, eClinicalMedicine reward, and the
  methodological bar each enforces.
- **Executable questions** — converts the best 2–4 directions into concrete questions (endpoint,
  comparator, minimum evidence, target-venue tier).
- **Hot-but-unsuitable** — flags trendy directions that are a poor fit for the data, with reasons.

## Integrity

Encodes **durable publication patterns, not a fixed citation list**. Specific recent papers
(PMID/DOI) are retrieved and verified **live** via `radiology-search` — never cited from memory.
Every concrete claim ships with a *Verify-now* item.

## Trigger examples

- "找近三年的前沿方向和创新点，结合我的数据。"
- "Is a foundation model right for my single-center CT cohort?"
- "What's the evidence basis for recommending external validation here? / 有什么文献依据？"

## Reference files

| File | Use |
|---|---|
| `references/frontier-themes.md` | Themes + data prerequisites + fit test |
| `references/evidence-layer.md` | Journal publication-pattern heuristics; verify-live discipline |
| `references/idea-to-question.md` | Trend → executable question; novelty framing |

## Handoffs

`radiology-design` (full design) · `radiology-search` (verify gap + seeds) ·
`radiology-journal` (venue tier) · `radiology-radiomics` / `radiology-deep-learning` /
`radiology-radiogenomics` (method fit) · `radiology-citation` (export verified seeds).
