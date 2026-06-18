# 入口

Use this file first when the user gives an incomplete, mixed, or high-level radiology
AI request.

## Task modes

| Mode | Use when | Default next module |
|---|---|---|
| `frontier` | User wants new research directions, hotspots, or innovation points | 前沿 |
| `literature` | User wants recent papers, evidence maps, or search terms | 文献 |
| `radiomics` | User describes handcrafted features or Pyradiomics-style workflow | 组学 |
| `deep-learning` | User describes CNN, transformer, segmentation, classification, foundation models, or multimodal AI | 深度 |
| `study-design` | User gives data and asks what project can be done | 设计 |
| `validation` | User asks whether the model or result is reliable | 验证 |
| `checklist` | User asks about CLAIM, CLEAR, RQS, IBSI, TRIPOD+AI, PROBAST+AI, STARD-AI, METRICS | 规范 |
| `data` | User asks about DICOM, NIfTI, masks, labels, privacy, repository, or sharing | 数据 |
| `writing` | User asks for Methods, Results, Discussion, abstract, title, or translation | 写作 |
| `journal-selection` | User has a draft/manuscript and asks where to submit, whether a journal fits, or how to choose target journals | 选刊 |
| `response` | User gives reviewer comments or revision notes | 回复 |

## Study card

Collect these fields when available:

```yaml
disease:
clinical_question:
modality:
data_format:
n_patients:
n_images_or_lesions:
centers:
time_span:
labels:
endpoint:
follow_up:
segmentation:
clinical_variables:
split_plan:
external_validation:
model_type:
target_journal_or_output:
candidate_journals:
publication_goal:
main_constraint:
```

## Clarifying question rule

Proceed with explicit assumptions when the user wants brainstorming or a rough plan.
Ask before final wording when missing facts would otherwise fabricate:

- sample size or patient/lesion/image unit
- endpoint or label source
- segmentation source and reader agreement
- train/validation/test split unit
- external validation status
- reported performance values
- ethics, consent, code, or data availability

## Fast routing examples

- "我有 200 例 CT 想做预后模型" -> 设计 + 组学 or 深度 + 验证
- "近三年影像 AI 前沿有哪些" -> 前沿 + 文献
- "帮我看 Methods 是否符合 CLAIM" -> 规范 + 深度 + 验证
- "文章写好了，帮我选刊" -> 选刊 + 文献 + 规范 + 验证
- "审稿人说没有外部验证怎么回复" -> 回复 + 验证
