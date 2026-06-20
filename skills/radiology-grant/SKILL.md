---
name: radiology-grant
description: "Reframe and polish imaging-AI / radiomics / radiogenomics research as a research grant proposal — convert paper-style \"we built a model\" into grant logic (clinical need → scientific question → hypothesis → specific aims/研究内容 → technical route/技术路线 → innovation/创新点 → feasibility/可行性 → expected outcomes), and strengthen title, abstract, background/立项依据, aims, key scientific question/关键科学问题, and significance. Tuned for NSFC (国家自然科学基金: 青年/面上/地区), provincial funds (省自然), and institutional grants, while applicable to general proposals. Use when the user mentions 国自然/省自然/基金申请/标书/立项依据/科学问题/技术路线/创新点/可行性, or wants to turn a study into a fundable proposal. Flags weak innovation, thin preliminary data, open-loop technical routes, and over-promising. Reminds the author to verify the current official guidelines; never fabricates preliminary results or citations."
---

# Research Grant Proposals (国自然 / 省自然 / institutional)

Use this skill to turn an imaging-research idea or finished study into a **fundable proposal**.
A grant is not a paper: reviewers fund a **scientific question** and a credible plan to answer
it, not a model. This skill rebuilds the logic and polishes each section to the structure
funders expect.

## Core stance

- **Grant logic, not paper logic.** Lead with the clinical need and the **scientific question**,
  then hypothesis → aims → technical route → innovation → feasibility → expected outcomes.
  "Construct a model / improve accuracy" is an engineering task, not a science question — reframe
  it into the mechanism or generalisable principle being tested.
- **The key scientific question (关键科学问题) is the spine.** One sharp, answerable question that
  the aims serve. If the aims don't all serve it, the proposal is unfocused.
- **Close the loop.** The technical route (技术路线) must connect need → question → each aim →
  method → expected result → back to the question. Reviewers reject open-loop routes.
- **Innovation must be specific and defensible.** Name the increment (question / data / method /
  validation / mechanism). Avoid "first/领先" without grounding.
- **Feasibility is shown, not asserted.** Preliminary data, team capability, data access, and
  ethics make it credible — never fabricate preliminary results.
- **Don't over-promise.** Aims must be achievable in the period and budget; over-scoping reads as
  naïveté.
- **Verify the current guidelines.** Word limits, format, attachments, ethics, and 限项 rules
  change yearly — confirm against the **current** official 申报指南 (the author must check; this
  skill flags it, it does not have the current year's rules memorised).

## When to use

- "把我的研究改写成国自然/省自然标书 / 帮我写立项依据、科学问题、技术路线、创新点。"
- "Turn this finished study into a grant proposal."
- "Is my innovation point / feasibility strong enough? polish my aims."
- "Reframe 'build a model' into a fundable scientific question."

## When to open extra files

| File | Open when |
|---|---|
| [references/grant-architecture.md](references/grant-architecture.md) | The section-by-section structure and what each must accomplish (NSFC/provincial) |
| [references/reframe-and-innovation.md](references/reframe-and-innovation.md) | Converting paper/engineering framing into a scientific question + a defensible innovation point |
| [references/feasibility-and-pitfalls.md](references/feasibility-and-pitfalls.md) | Showing feasibility (preliminary data, route closure, team/data/ethics) and the common rejection reasons |

## Workflow

1. **Extract the science.** From the idea/study, find the clinical need and the **one scientific
   question** worth funding (reframe engineering goals into mechanism/generalisable principle).
2. **Set the architecture** (grant-architecture.md) — title, abstract, 立项依据, 研究目标, 研究内容
   (aims), 关键科学问题, 技术路线, 创新点, 可行性, 预期成果, plan.
3. **Build aims that serve the question** — each aim a testable sub-question with a method and an
   expected result; aims are coherent, not a feature list.
4. **Forge the innovation point** (reframe-and-innovation.md) — specific, defensible, tied to the
   gap; classify the kind of innovation.
5. **Close the technical route** — a loop diagram in prose: need → question → aims → methods →
   expected results → question; mark validation and risk mitigations.
6. **Evidence feasibility** (feasibility-and-pitfalls.md) — preliminary data (real only), team,
   data access, ethics; pre-empt the common rejection reasons.
7. **Polish & guideline-check** — tighten each section; flag every place the author must verify
   the current official 申报指南 (limits, format, 限项, ethics).

## Output contract

1. **`Scientific question`** — the one fundable question + hypothesis.
2. **`Section drafts`** — title, abstract, 立项依据, 研究目标/内容, 关键科学问题, 技术路线, 创新点,
   可行性, 预期成果 — drafted or restructured.
3. **`Innovation point`** — specific, classified, defensible.
4. **`Technical-route check`** — is the loop closed? gaps marked.
5. **`Feasibility & risk`** — what supports feasibility; risks + mitigations.
6. **`Weaknesses & fixes`** — thin innovation, weak preliminary data, over-scoping, open loop.
7. **`待核验（中文）`** — current-guideline items the author must confirm (字数/格式/附件/伦理/限项).

## Quality bar

A good proposal makes a reviewer see one sharp scientific question, aims that all serve it, a
closed technical route, a specific innovation, and credible feasibility — written to the funder's
structure, with no fabricated preliminary data and an explicit reminder to verify the current
year's guidelines.

## Handoffs

- Study/validation design behind an aim → `radiology-design`.
- Frontier framing & evidence for the gap → `radiology-frontier` (verify live → `radiology-search`).
- Statistics/sample-size for an aim → `radiology-stats`.
- Ethics/feasibility of data → `radiology-ethics` / `radiology-data`.
- English polish of an English-language proposal → `radiology-polishing`.
- This skill drafts and critiques proposals; it does not guarantee funding and does not replace
  the current official 申报指南.
