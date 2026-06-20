# radiology-writing

**Construct _Radiology_ (RSNA) manuscript prose — argument first, then sentences — in the
exact shape the journal requires.** For drafting and restructuring (sentence-level polish is
`radiology-polishing`).

## What it does
- Drafts/rebuilds every section: title, **structured abstract**, **Summary statement**,
  **Key Results** box, Introduction, Materials and Methods, Results, structured Discussion.
- Turns Chinese lab notes / mixed drafts into submission-ready English (intent, not clause
  order).
- Enforces the _Radiology_ manuscript shape, verb calibration, and reporting-checklist
  awareness.

## The _Radiology_ shape (what differs from a generic paper)
- **Summary statement** — one declarative sentence of the main finding.
- **Key Results** — ≤ 3 results/conclusions, ≤ 75 words, with summary data; no abbreviations
  or vague language (feeds the visual abstract).
- **Structured abstract** — Background, Purpose, Materials and Methods, Results, Conclusion.
- **Structured Discussion** — first paragraph summarises key findings; limitations explicit;
  bounded conclusion.

## Reference files
```
references/
├── article-architecture.md     section order + argument flow + manuscript skeleton
├── structured-abstract.md      abstract + Summary statement + Key Results templates
├── methods.md                  Materials and Methods order for imaging/AI/radiomics
├── results.md                  Results narrative (flow, CIs, comparisons, validation)
├── discussion.md               structured Discussion pattern
├── chinese-author-workflow.md  中文/混排笔记 → submission-ready English
└── examples/                   worked section examples
```

## Example prompts
- "Draft the structured abstract + Summary statement + Key Results from these results."
- "Write Materials and Methods for this CT radiomics study (here are the parameters)."
- "My Discussion is a results re-cap — restructure it the way _Radiology_ wants."
- "把这段中文实验记录写成 Methods。"

## Integrity
Never invents data, metrics, CIs, or citations. Surfaces missing inputs and offers
placeholder scaffolds. Cross-checks sections against `radiology-reporting`.
