# radiology-annotation

面向放射组学、分割模型和影像基因组学研究的 **ROI / VOI / mask 标注规范工作流**。它解决的是高水平期刊最常追问的问题：病灶如何选择，谁来勾画，是否盲法，是否独立标注，如何达成 consensus，重复标注和一致性评价是否足以支撑后续特征、模型或机制结论。

## 它能做什么

- 设计 **Annotation SOP**：2D / 2.5D / 3D、whole-tumour、largest-slice、peritumoral、habitat、多病灶规则，并与 endpoint 和生物学假设对齐。
- 明确 **reader protocol**：读者数量、资历、盲法、独立 vs consensus、第三方裁决、标注训练阶段。
- 规划 **reproducibility & QC**：重复标注、ICC / Dice / Hausdorff、feature-stability filtering、敏感性分析。
- 检查 **mask geometry integrity**：DICOM、NIfTI、DICOM-SEG、RTSTRUCT 之间的 spacing / origin / direction / slice order 风险。
- 输出可放入稿件的 Methods 段落，并保留需要作者确认的占位项。

## 典型触发

- “帮我写 ROI 标注 SOP 和 Methods，包括勾画规范和一致性评价。”
- “两个放射科医生勾画肿瘤，ICC / Dice 应该怎么设计和报告？”
- “DICOM 转 NIfTI 后 mask 对不上图像，怎么做几何一致性 QC？”

## 参考文件

| File | 用途 |
|---|---|
| `references/lesion-selection.md` | 2D/3D、区域选择、瘤周、habitat、多病灶规则 |
| `references/reader-protocol.md` | 读者、盲法、consensus / adjudication、训练流程 |
| `references/reproducibility-qc.md` | ICC、Dice、Hausdorff、feature stability、敏感性分析 |
| `references/mask-geometry.md` | spacing / origin / direction / slice order 与格式转换风险 |

## 下游衔接

`radiology-radiomics`（特征提取）· `radiology-reporting`（IBSI / CLEAR）· `radiology-stats`（ICC 模型、Bland-Altman）· `radiology-radiogenomics`（habitat）· `radiology-data` / `radiology-ethics`（共享 mask 的去标识化和伦理）。

## 边界

该 skill 用于规范和报告科研标注流程，不替代临床诊断性勾画或个体患者决策。
