# 公库

Use this file when the user asks about public datasets, TCIA, TCGA, GEO, CPTAC,
IDC, public imaging cohorts, public transcriptomics, public single-cell or spatial
transcriptomics datasets, external validation, or public-data-based mechanism analysis.

## Core goal

公库模块的目标是帮助作者把公共数据用在正确位置：外部验证、机制注释、背景支持或方法比较。必须区分
“配对数据验证”和“非配对数据解释”。

## First questions

- 想用公库做什么：外部验证、机制解释、补充文献证据、训练预训练模型，还是复现对照？
- 目标疾病、模态、治疗场景、终点和样本量是什么？
- 公共数据是否有原始影像、mask、临床终点、病理/分子标签、随访？
- 影像和组学是否来自同一患者、同一病灶、同一时间点？
- 数据许可证、引用要求、访问限制和下载日期是否能记录？
- 是否需要当前联网核验数据集可用性、版本和访问政策？

## Common public resources

Use current source checking before final recommendations, because dataset availability,
versions, and access rules can change.

| Resource type | Examples | Typical use |
|---|---|---|
| public imaging | TCIA, Imaging Data Commons | imaging validation, segmentation, radiogenomics |
| cancer genomics | TCGA, CPTAC | molecular annotation, paired radiogenomics when matched |
| transcriptomics | GEO, ArrayExpress, SRA | pathway validation, expression signatures |
| single-cell | GEO, Single Cell Portal, cellxgene | cell type annotation and mechanism support |
| spatial transcriptomics | GEO, HuBMAP, institutional public data | spatial niche support |
| challenge data | BraTS, KiTS, LIDC-IDRI, LiTS, MSD | segmentation/detection benchmarking |

Do not list a public dataset as available for the user's exact task without checking its
cohort, labels, modality, and access status when the advice is submission-critical.

## Public-data use levels

### Level 1: direct external validation

Requirements:

- same disease and clinically comparable population
- same or compatible modality/protocol
- same endpoint or mappable label
- enough sample size/events
- independent from training data
- locked model applied without retuning

### Level 2: paired radiogenomics validation

Requirements:

- same patient-level imaging and omics pairing
- clear sample ID mapping
- consistent time point or treatment context
- outcome or biology endpoint available
- transparent exclusions

### Level 3: mechanism support

Use when:

- public omics data are not paired to the user's images
- data can support pathway, cell type, or immune microenvironment interpretation
- claims are phrased as external annotation/support, not direct validation

### Level 4: background evidence

Use when:

- dataset is too different for validation
- it only supports literature context or hypothesis generation

## Search and screening plan

For public datasets, return:

1. disease and modality keywords
2. candidate databases
3. inclusion criteria
4. required fields
5. exclusion reasons
6. matching strategy
7. data-use and citation requirements
8. risk of domain mismatch

## Reporting public data

Methods should state:

- database name
- dataset/accession identifier
- access date
- inclusion/exclusion criteria
- downloaded files
- preprocessing and matching rules
- endpoint mapping
- whether data were used for validation, mechanism annotation, or background only

## Output format

```text
公库定位
- 使用目的：
- 目标疾病/模态：
- 是否需要配对数据：

候选公库
| 数据库 | 可能用途 | 必须核验 | 风险 |

使用路线
- 外部验证：
- 机制解释：
- 背景支持：

写作和引用
- 方法描述：
- 数据可用性：
- 引用/访问日期：
```

## Red lines

- Do not present unpaired public data as direct validation of the user's model.
- Do not invent dataset IDs, sample sizes, endpoints, access dates, or availability.
- Do not ignore data licenses, citation requirements, controlled access, or privacy rules.
- Do not mix public data into training and then call it independent external validation.
- Do not use public data with incompatible endpoints without explicitly stating limitations.
