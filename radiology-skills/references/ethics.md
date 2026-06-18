# 伦理

Use this file when the user asks about ethics approval, consent waiver, retrospective
clinical imaging research, privacy, de-identification, data sharing restrictions,
multi-center data use agreements, or manuscript ethics statements.

## Core goal

伦理模块的目标是帮助作者准确表达已有审批和限制。它不能替代 IRB/伦理委员会意见，也不能创造不存在的审批。

## First questions

- 研究是回顾性、前瞻性、注册研究，还是多中心数据回顾分析？
- 是否已有伦理审批？审批机构、编号、日期、适用中心是什么？
- 是否豁免知情同意？豁免依据由谁批准？
- 是否涉及影像、临床、病理、基因组、转录组、单细胞或空间组学数据？
- 是否涉及跨机构数据传输、云端训练、模型部署或公共共享？
- 数据是否已去标识化？有哪些字段不能共享？
- 目标期刊是否要求特定 Ethics/Consent/Data Availability 格式？

## Ethics statement elements

Include only true facts:

- approving ethics committee or IRB
- approval number
- study design
- consent status or waiver
- data de-identification
- compliance with institutional rules
- multi-center approval or local approvals when applicable
- controlled-access restrictions if data cannot be public

## Retrospective study skeleton

```text
This retrospective study was approved by [ethics committee/institutional review board]
of [institution] (approval No. [number]), and the requirement for written informed
consent was waived due to the retrospective nature of the study. All imaging and
clinical data were de-identified before analysis.
```

Use only if the user confirms approval and waiver. If not confirmed, ask for the facts.

## Multicenter wording

```text
Each participating center obtained local ethics approval or was covered by the
central approval according to institutional requirements. Data were transferred and
analyzed under approved data-use agreements after de-identification.
```

Use only when true. If centers have different approvals, list them in supplement or
state that center-specific approvals were obtained.

## Consent and privacy

Check:

- direct identifiers removed
- dates shifted or generalized where needed
- DICOM metadata scrubbed
- accession numbers removed
- rare disease and small-cell privacy risk
- genetic and omics data re-identification risk
- data-use agreement restrictions
- cloud or third-party processing approval

## Data sharing ethics

Possible positions:

- public open sharing: only when allowed and de-identified
- controlled access: common for clinical imaging and omics data
- no public sharing: acceptable when justified by consent, law, or institutional policy
- derived data sharing: feature tables, aggregate statistics, trained weights, or code

Use `references/data.md` and `references/reproducibility.md` together for availability wording.

## Output format

```text
伦理定位
- 研究类型：
- 审批状态：
- 数据类型和隐私风险：

需要作者确认
- [IRB, approval number, consent waiver, data-use agreement, sharing limits]

伦理/知情同意文本
[only after facts are supplied]

数据共享限制
- 可共享：
- 受控访问：
- 不可共享：

投稿前风险
- [missing approval, unclear waiver, identifiable metadata, omics privacy]
```

## Red lines

- Do not invent ethics approval, waiver, approval numbers, committee names, or dates.
- Do not provide legal advice; recommend checking institutional IRB and journal requirements.
- Do not recommend sharing identifiable DICOM, genetic, or clinical data.
- Do not imply consent waiver unless confirmed.
- Do not ignore multi-center approval and data-use agreement differences.
