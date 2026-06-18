# 入口

Use this file first when the user gives an incomplete, mixed, or high-level radiology
AI request.

## Task modes

| Mode | Use when | Default next module |
|---|---|---|
| `frontier` | User wants new research directions, hotspots, or innovation points | 前沿 |
| `literature` | User wants recent papers, evidence maps, or search terms | 文献 |
| `public-datasets` | User asks about TCIA, TCGA, GEO, CPTAC, IDC, public imaging/omics datasets, or public validation cohorts | 公库 |
| `radiomics` | User describes handcrafted features or Pyradiomics-style workflow | 组学 |
| `deep-learning` | User describes CNN, transformer, segmentation, classification, foundation models, or multimodal AI | 深度 |
| `mechanism` | User asks how radiomics/deep learning model scores relate to genomics, transcriptomics, single-cell, spatial transcriptomics, pathways, immune microenvironment, or biological mechanisms | 机制 |
| `study-design` | User gives data and asks what project can be done | 设计 |
| `grant-writing` | User asks to write, polish, revise, or structure NSFC/national or provincial natural science foundation proposals | 基金 |
| `annotation` | User asks about ROI, VOI, mask, lesion selection, segmentation annotation, reader agreement, or ICC/Dice | 标注 |
| `statistics` | User asks about statistical analysis, sample size, feature selection, LASSO, Cox, C-index, calibration, DCA, confidence intervals, or survival analysis | 统计 |
| `validation` | User asks whether the model or result is reliable | 验证 |
| `multicenter` | User asks about multicenter data, external validation by center, scanner/vendor/protocol differences, center effects, harmonization, or domain shift | 多中心 |
| `checklist` | User asks about CLAIM, CLEAR, RQS, IBSI, TRIPOD+AI, PROBAST+AI, STARD-AI, METRICS | 规范 |
| `data` | User asks about DICOM, NIfTI, masks, labels, privacy, repository, or sharing | 数据 |
| `ethics` | User asks about ethics approval, IRB, consent waiver, privacy, de-identification, or data-use limits | 伦理 |
| `reproducibility` | User asks about code, model weights, feature tables, random seeds, environment, supplementary files, or reproducibility | 复现 |
| `writing` | User asks for Methods, Results, Discussion, abstract, title, or translation | 写作 |
| `figures` | User asks about figures, tables, graphical abstracts, figure legends, workflows, ROC/calibration/DCA/KM plots, or mechanism diagrams | 图表 |
| `pre-submission` | User asks for pre-submission audit, simulated reviewer critique, manuscript risk review, or top-journal readiness | 预审 |
| `journal-selection` | User has a draft/manuscript and asks where to submit, whether a journal fits, or how to choose target journals | 选刊 |
| `clinical-translation` | User asks about clinical utility, reader study, prospective validation, workflow integration, PACS/RIS, deployment, or real-world evaluation | 转化 |
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
annotation_strategy:
readers:
reader_agreement:
clinical_variables:
omics_data:
paired_omics:
omics_sample_size:
omics_platform:
split_plan:
external_validation:
center_distribution:
scanner_protocols:
statistics_plan:
main_metrics:
calibration_dca:
figure_needs:
public_dataset_plan:
ethics_approval:
consent_status:
data_sharing_limits:
code_availability:
clinical_use_case:
reader_study_plan:
model_type:
target_journal_or_output:
candidate_journals:
publication_goal:
funding_scheme:
proposal_section:
grant_deadline_or_year:
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
- "影像组学模型做完了，想结合转录组和单细胞解释机制" -> 机制 + 组学 + 文献 + 验证
- "帮我润色国自然立项依据" -> 基金 + 前沿 + 设计 + 写作
- "ROI 是两位医生勾画的，Methods 怎么写" -> 标注 + 组学 + 规范
- "LASSO、Cox、DCA、C-index 这部分统计对不对" -> 统计 + 验证
- "帮我看 Methods 是否符合 CLAIM" -> 规范 + 深度 + 验证
- "帮我规划论文图表和 figure legend" -> 图表 + 写作 + 规范
- "投稿前帮我模拟审稿人预审" -> 预审 + 验证 + 规范 + 图表
- "代码、特征表和模型参数怎么放补充材料" -> 复现 + 数据 + 伦理
- "4 家医院数据怎么做外部验证和中心差异分析" -> 多中心 + 验证 + 统计
- "想用 TCIA/TCGA/GEO 做验证或机制解释" -> 公库 + 文献 + 机制 + 数据
- "伦理、知情同意豁免和数据共享怎么写" -> 伦理 + 数据 + 复现
- "这个模型怎么做读者研究和临床转化" -> 转化 + 验证 + 统计
- "文章写好了，帮我选刊" -> 选刊 + 文献 + 规范 + 验证
- "审稿人说没有外部验证怎么回复" -> 回复 + 验证
