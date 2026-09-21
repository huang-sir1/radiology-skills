# Reframing to a scientific question + forging the innovation point

The most common fatal flaw in imaging-AI grants: an engineering goal dressed as science. Fix the
framing first, then make the innovation specific.

## Engineering goal → scientific question

| Paper/engineering framing (weak) | Grant scientific framing (fundable) |
|---|---|
| "Build a CNN to classify X" | "What imaging phenotype reflects [biological process] in X, and can it be learned to stratify [outcome]?" |
| "Improve AUC for Y" | "Which [features/mechanism] drive predictability of Y, and do they generalise across centers?" |
| "Apply a foundation model to Z" | "Does a transferable representation capture [generalisable principle] of Z better than task-specific features, and why?" |
| "Combine imaging + genomics" | "What molecular programs underlie [imaging phenotype], and can imaging serve as their non-invasive surrogate?" |

The test: does the project leave behind **knowledge, a defensible measurement, a decision-relevant
estimate or a generalisable principle**, not just a model? Do not force every engineering project
into a biological mechanism claim: a rigorous measurement, transportability or human–AI decision
question can be scientific when the design supports it.

## The key scientific question (关键科学问题)

- Usually one central question, sharp and answerable within the period; follow a call that explicitly
  requires another architecture.
- All aims serve it; if an aim doesn't, cut or refold it.
- Phrase as a question about a mechanism, relationship, or generalisable principle — not a
  deliverable.

## Forging the innovation point (创新点)

Classify the innovation explicitly (one or more):

- **Question innovation** — a question not previously posed.
- **Data innovation** — a uniquely matched/scaled/multimodal cohort.
- **Method innovation** — a genuinely new technical contribution (be precise).
- **Validation innovation** — a stronger generalisability/clinical-utility design.
- **Mechanism innovation** — linking imaging phenotype to biology (→ radiology-radiogenomics).

Rules:
- Be **specific**: "first to validate X across N vendors with calibration" beats "novel deep
  model."
- Tie each innovation to the **gap** in 立项依据.
- A gap/"first" claim needs a reproducible live literature check (→ radiology-frontier /
  radiology-search), including contradictory and near-neighbour work — never assert it from memory.
- Avoid 领先/国际首创 unless genuinely supportable; reviewers punish hollow superlatives.
- Keep the evidence state visible. `No paper found in a bounded search` is not proof that no work
  exists, and technical novelty is not automatically scientific importance.
- Calibrate to the funder: under NIH's current simplified framework, innovation influences
  Importance but a non-novel project may still be important; under NSFC, preserve innovation as a
  named review dimension without inventing a numeric weight.

## Output

```
Scientific question (one):
Hypothesis:
Innovation point(s) [classified + specific + tied to gap]:
Gap-check to verify live: [→ radiology-search]
Evidence state and search boundary:
Strongest claim licensed by the proposed design:
Stronger claims explicitly not licensed:
```

This reframing is funder-independent — the same forged question and innovation point feed an
NSFC 立项依据/创新点 section, an NIH Specific Aims/Significance/Innovation, or an ERC Part I
"excellence of the research project" narrative alike. Only the packaging differs
(→ `international-grants.md`); redo this step once, not per funder.
