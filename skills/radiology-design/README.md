# radiology-design

**Stage 1 — Scope & Design.** Feasibility triage + full study design + validation strategy for
imaging research. The front of the chain: someone has data but no settled study.

## What it does

- **Feasibility verdict** — can this CT/MRI/PET/US/mammography/multimodal data support a
  credible study, and what is the realistic task ceiling? Returns one of: *Feasible as designed*,
  *Feasible with changes*, *Feasibility study only*, *Not yet — collect X first*.
- **Study blueprint** — clinical question → population → endpoint/estimand → comparator →
  clinical-use scenario, with a **minimum-viable** version (publishable now) and a **stronger**
  version (higher tier), plus the design template (diagnostic accuracy, prediction/prognosis,
  treatment-response, segmentation, radiomics, radiogenomics, reader study).
- **Validation plan** — internal CV/bootstrap, temporal, geographic/center-held-out, fully
  external, multi-center, federated; what honestly counts as "external"; center/scanner/batch
  effects and harmonisation.
- **Binding constraint** — names the single number (matched n, event count, external-cohort
  size, labelled cases) the whole study hinges on.

## Trigger examples

- "我有 300 例多中心肝癌 MRI，这批数据能做什么课题？"
- "Turn my data into a complete, submittable project."
- "Design a multi-center external-validation plan / 多中心外部验证怎么设计？"
- "Is my data enough for a prognosis model, or only a pilot?"

## Reference files

| File | Use |
|---|---|
| `references/feasibility-triage.md` | Task ceiling, showstoppers, the four-verdict format |
| `references/study-blueprints.md` | Seven design templates, MVP vs stronger |
| `references/validation-strategy.md` | The validation ladder, multi-center design, center effects |
| `references/endpoints-and-estimands.md` | Clinical question, endpoint, comparator, threshold logic |

## Handoffs

`radiology-frontier` (is it novel/publishable) · `radiology-stats` (sample size, EPV, power) ·
`radiology-radiomics` / `radiology-deep-learning` / `radiology-radiogenomics` (method design) ·
`radiology-annotation` (mask SOP) · `radiology-reporting` (which checklist) ·
`radiology-ethics` (consent/sharing feasibility) · `radiology-translation` (reader/prospective).

Plans research only — no clinical or diagnostic recommendations.
