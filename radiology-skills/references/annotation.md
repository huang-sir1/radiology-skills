# 标注

Use this file when the user asks about ROI, VOI, masks, lesion selection, segmentation
annotation, reader agreement, or segmentation quality control in radiomics or medical
imaging AI studies.

## Core goal

标注模块的目标是把“影像区域怎么来”讲清楚。影像组学和影像深度学习文章中，ROI/mask
不是技术细节，而是模型输入的来源。标注不清楚会直接影响特征稳定性、模型可重复性和审稿可信度。

## First questions

Ask only what is needed for the task:

- 疾病、模态、序列、增强期相和目标病灶是什么？
- ROI/VOI 是 2D、3D、whole tumor、largest slice、tumor core、peritumoral ring，还是 habitat？
- 标注单位是 patient、lesion、slice、volume 还是 time point？
- 谁标注：放射科医生、研究生、技师、自动分割模型，还是半自动工具？
- 有几名读片者？年资、是否盲法、是否独立标注？
- 分歧如何处理：共识会议、第三名高级医生裁决、平均 mask，还是选择一名读片者结果？
- 是否做重复标注？间隔多久？用于 ICC、Dice、Hausdorff 还是敏感性分析？
- mask 格式是什么：DICOM-SEG、RTSTRUCT、NIfTI、NRRD、MHA、PNG、JSON？
- 是否检查图像和 mask 的 spacing、origin、direction、slice order、registration？

## Annotation design

### Lesion selection

- 单病灶研究：说明目标病灶选择规则，例如最大病灶、原发灶、可测量病灶、治疗前基线病灶。
- 多病灶研究：说明每例患者纳入一个主病灶、所有病灶汇总、病灶级建模，还是患者级聚合。
- 转移瘤研究：说明是否按器官、病灶大小、治疗照射范围或 RECIST target lesion 选择。
- 纵向研究：说明 baseline、post-treatment、follow-up 的时间窗和病灶配准规则。
- 排除规则：运动伪影、金属伪影、边界不清、治疗后坏死、过小病灶、非目标序列缺失。

### ROI/VOI strategy

| Strategy | Best use | Main risk |
|---|---|---|
| 2D largest slice | quick retrospective radiomics, small workload | misses heterogeneity and is reader-sensitive |
| 3D whole tumor | most standard for CT/MRI radiomics | segmentation burden and inter-reader variability |
| tumor core / enhancing tumor | biologically focused tasks | needs strict imaging definition |
| peritumoral ring | invasion, edema, immune microenvironment | ring width and anatomy boundaries must be justified |
| habitat | heterogeneity, treatment response, mechanism work | clustering and registration add uncertainty |
| automatic segmentation | large datasets or workflow studies | requires independent segmentation validation |

Do not recommend a complex ROI design unless it answers the clinical question.

## Reader workflow

Recommended reporting elements:

1. Number of readers and professional background.
2. Years of radiology experience.
3. Whether readers were blinded to clinical outcome, pathology, molecular data, and model results.
4. Software and version used for segmentation.
5. Image windowing, sequence, phase, slice thickness, reconstruction settings if relevant.
6. Initial independent annotation or primary annotation plus review.
7. Disagreement resolution rule.
8. Repeated annotation subset and interval.
9. Quantitative reproducibility metrics.
10. How final mask was selected for model building.

## Quality control

### Visual QC

- Randomly inspect overlays across centers, scanners, phases, and lesion sizes.
- Check whether mask covers non-target tissue, vessels, necrosis, edema, air, bone, or background.
- Confirm mask and image alignment after format conversion.
- For 3D masks, inspect axial, coronal, and sagittal views if possible.
- Document exclusion after QC and avoid excluding cases based on model performance.

### Technical QC

- image-mask shape match
- spacing/origin/direction consistency
- non-empty mask
- lesion volume above minimum voxel count
- no duplicate patient or lesion IDs
- correct phase/sequence and time point
- no patient identifiers retained in exported files

### Reproducibility metrics

Use metrics according to task:

- Radiomics feature reproducibility: ICC or concordance correlation coefficient.
- Segmentation overlap: Dice similarity coefficient.
- Boundary agreement: Hausdorff distance or average surface distance.
- Small lesions: be careful with Dice instability; report volume and boundary metrics.
- Reader robustness: repeat radiomics pipeline with alternative reader masks if feasible.

## Methods wording skeleton

```text
Tumor segmentation was performed on [sequence/phase] by [reader number and experience]
using [software]. Readers were blinded to [outcomes/pathology/model results]. The
[2D/3D/whole-tumor/peritumoral] region of interest was defined as [definition].
Disagreements were resolved by [consensus/third reader]. To assess segmentation
reproducibility, [n] cases were re-segmented by [reader] after [interval], and
[ICC/Dice/Hausdorff] was calculated. Features with [stability criterion] were retained
for subsequent modeling.
```

Use this skeleton only after replacing bracketed facts with real user-supplied details.

## Output format

```text
标注定位
- 模态/序列：
- 病灶和 ROI 策略：
- 标注者和流程：

必须补充
- [reader, blinding, software, repeat annotation, QC]

质控方案
- 视觉质控：
- 技术质控：
- 一致性评价：

Methods 可写内容
[only when facts are supplied]

高风险问题
- [unclear lesion selection, no reader agreement, mask-image mismatch, post-hoc exclusion]
```

## Red lines

- Do not accept “医生勾画 ROI” as enough methodological detail.
- Do not invent reader experience, blinding, agreement values, software versions, or exclusion counts.
- Do not let lesion-level or slice-level annotation imply patient-level independence.
- Do not ignore registration and coordinate consistency when masks are converted across formats.
- Do not treat automatic segmentation masks as reliable without segmentation validation or QC.
