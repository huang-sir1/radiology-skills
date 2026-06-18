# 复现

Use this file when the user asks about reproducibility, code sharing, feature tables,
model coefficients, random seeds, environments, supplementary materials, or data/code
availability for radiomics and medical imaging AI studies.

## Core goal

复现模块的目标是让别人能理解、审查，并在合理条件下复现研究流程。医学影像数据往往不能完全开放，
但方法、参数、代码、特征表和限制必须透明。

## First questions

- 能否共享原始影像、脱敏影像、mask、特征表、模型权重或代码？
- 伦理和数据使用协议允许什么级别的共享？
- radiomics 特征提取工具、版本、参数是否完整？
- 深度学习训练代码、模型结构、权重、随机种子、硬件和包版本是否可记录？
- 是否有数据字典、变量定义、缺失值规则、排除病例清单？
- 目标期刊的数据/代码政策是什么？是否需要当前核验？

## Reproducibility package

### Data dictionary

Include:

- patient_id surrogate definition
- center_id
- scan_id / study_id / series_id
- lesion_id
- time_point
- modality and sequence
- label and endpoint definitions
- clinical variables and coding
- missing-value codes
- split assignment
- public/private data source

Do not include direct identifiers, accession numbers, names, dates, or raw DICOM metadata that can identify patients.

### Radiomics reproducibility

Report:

- software and version, such as Pyradiomics version
- image preprocessing: resampling, interpolation, normalization
- gray-level discretization: bin width or bin count
- filters: wavelet, LoG, square, square root, logarithm, exponential
- feature classes
- mask strategy
- feature stability filtering
- feature selection and model coefficients
- random seeds and resampling design

### Deep learning reproducibility

Report:

- framework and version
- model architecture and initialization
- input size, channels, windowing, normalization
- train/validation/test split files or deterministic rules
- data augmentation
- loss function and optimizer
- learning rate schedule
- batch size, epochs, early stopping
- hardware
- random seeds
- checkpoint selection rule
- inference threshold
- model weights availability or restriction

### Statistical reproducibility

Report:

- software packages and versions
- imputation/scaling/feature-selection pipeline
- resampling folds
- CI method, bootstrap count if used
- threshold selection
- subgroup definitions
- code for tables and figures if shareable

## Availability statements

### Code availability skeleton

```text
The analysis code used to reproduce the main preprocessing, feature-selection,
modeling, and evaluation steps is available at [repository] under [license]. Code
requiring institutional data access is provided as documented scripts with example
inputs and a data dictionary.
```

If code cannot be shared:

```text
The full clinical analysis code cannot be publicly released because it contains
institution-specific data access paths and protected processing logic. Key parameter
settings, model specifications, and feature definitions are provided in the Supplementary
Materials, and reasonable requests for additional methodological details may be directed
to the corresponding author subject to institutional approval.
```

### Data availability skeleton

Use `references/data.md` and `references/ethics.md` together when privacy wording matters.

## Supplementary materials checklist

- ST1: cohort and variable dictionary
- ST2: image acquisition parameters
- ST3: segmentation protocol
- ST4: radiomics extraction parameters
- ST5: selected features and coefficients
- ST6: hyperparameters and training settings
- ST7: split assignment summary
- ST8: full performance with CI
- ST9: sensitivity/subgroup analyses
- ST10: checklist compliance

## Output format

```text
复现定位
- 可共享内容：
- 受限内容：
- 目标期刊要求：

复现包
- 数据字典：
- 代码/环境：
- radiomics 参数：
- 深度学习参数：
- 统计脚本：

补充材料建议
- [tables and files]

Availability 文本
[only when sharing limits are known]
```

## Red lines

- Do not recommend public sharing of identifiable images or protected metadata.
- Do not invent GitHub, Zenodo, OSF, Figshare, or institutional repository links.
- Do not claim full reproducibility if core data, code, model weights, or parameters are missing.
- Do not expose patient IDs, accession numbers, dates, or DICOM identifiers.
- Do not omit restrictions when data-use agreements or ethics approvals limit sharing.
