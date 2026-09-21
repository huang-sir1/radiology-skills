# radiology-data

面向 _Radiology_ 级别投稿的数据与代码可用性、DICOM 去标识化、数据仓库选择和 FAIR 检查工作流。它解决的是“文章方法看起来完整，但数据能不能共享、代码能不能复现、隐私风险有没有处理清楚”这一类审稿人与编辑非常关注的问题。

## 它能做什么

- 起草投稿可用的 **Data Availability** 与 **Code / Model Availability** statements。
- 规划 **DICOM de-identification**：header tags、burned-in pixel PHI、面部重建风险、brain MRI defacing。
- 选择合适仓库：TCIA / Zenodo / GitHub / GEO / dbGaP / EGA 等，并说明公开、受控访问或不可共享的边界。
- 生成 DataCite 风格 dataset citation，检查 FAIR 与可复现材料。
- 让数据共享表述与伦理、知情同意、DUA 和机构限制保持一致。

## 典型触发

- “帮我写 Data Availability，图像放 TCIA，代码放 Zenodo，RNA-seq 放 GEO。”
- “公开脑 MRI 前如何去标识化和 defacing？”
- “我们有 dbGaP 受控访问数据，availability statement 应该怎么诚实表述？”

## 参考文件

```text
references/
├── cohort-assembly-and-id-reconciliation.md  三表 ID 对齐审计、错位根因、协议异质筛除与纳排计数
├── data-dictionary-spec.md                   字段级数据字典模板：变量/类型/编码/缺失码/出处
├── chinese-clinical-text-abstraction.md      中文病历变量提取：人工摘录表、正则起步、LLM 预填纪律
├── outcome-and-followup-data.md              结局与随访字段规范、随访采集 SOP、删失与缺失值策略
├── dicom-deidentification.md                 DICOM tags、pixel PHI、defacing、标准与工具
├── repositories.md                           图像、特征、代码、模型、组学数据放哪里
├── availability-and-fair.md                  statement 模板、dataset citation、FAIR、中文对齐
└── ai-radiogenomics-public-resources.md      公共数据集角色规划：pretraining/开发/测试/外部验证，TCIA/GDC/PhysioNet/GEO/dbGaP/EGA
```

## 边界

不会夸大数据开放程度，也不会编造 accession。该 skill 提供科研与投稿文本支持，不替代机构 IRB、DUA 或法律审查。
