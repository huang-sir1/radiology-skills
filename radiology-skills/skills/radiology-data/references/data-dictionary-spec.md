# Data dictionary specification

One dictionary per project, one row per `table_id + variable_name`. It is the shared foundation three consumers
depend on: the stage-3 data-dictionary artifact (`radiology-pipeline/stage-gates-and-handoffs.md`),
FAIR "Reusable" archiving (`availability-and-fair.md`), and feature-ID mapping
(`radiology-radiomics/feature-extraction.md`). Build it **before** abstraction or extraction.

## Rules

- `patient_id` is the patient-level grouping/split key, **not a universal join key**. Each table
  needs a table passport with row grain, full primary/composite key, foreign keys and expected join
  cardinality (`cohort-assembly-and-id-reconciliation.md`). Repeated patients are legitimate in
  encounter, exam, lesion, timepoint and abstraction tables; uniqueness is checked at the declared
  grain. Preserve those keys in the dictionary and do not collapse rows merely to make patient IDs
  unique.
- Define variables before collecting them. Never silently redefine a variable mid-project —
  add a new variable name and log the change (decision log, `radiology-pipeline`).
- One missing code: `NA`. Never encode missing as 0, blank, or a real-looking value; never mix
  missing codes within one column.
- Coding and allowed values are exhaustive and fixed; units stated once and kept.
- Keep the `source` column verbatim — Chinese source field names and report snippets are
  allowed and encouraged for traceability.
- Version the dictionary (`v0.1`, `v1.0`, ...); archive it with the dataset and reference it in
  the availability statement.

## Column template

| Column | Content | Example |
|---|---|---|
| `table_id` | table with declared grain, complete key and join-cardinality passport | `clinical_baseline` |
| `variable_name` | stable snake_case ID | `os_event` |
| `label` | human-readable (Chinese OK) | 总生存事件 |
| `type` | continuous / ordinal / nominal / date / text | nominal |
| `unit` | stated unit; empty if none | months |
| `coding` | value → meaning | `1=死亡; 0=删失` |
| `allowed_values` | range or enumerated set | `{0;1}` |
| `missing_code` | always `NA` | `NA` |
| `source` | table / field / document location | 出院小结·出院诊断 |
| `derived` | derivation rule, if any | `event_date - surgery_date` |
| `owner` | who maintains the variable | A. Wang |
| `dict_version` | dictionary version | v1.0 |

## Example — radiomics project excerpt

```text
table_id,variable_name,label,type,unit,coding,allowed_values,missing_code,source,derived,owner,dict_version
clinical_baseline,patient_id,患者编号,nominal,,,,,脱敏映射表,,A. Wang,v1.0
clinical_baseline,center,中心,nominal,,01=本院;02=协作中心,{01;02},NA,伦理批件机构清单,,A. Wang,v1.0
clinical_baseline,age,年龄,continuous,years,,18–100,NA,住院首页,,A. Wang,v1.0
clinical_baseline,sex,性别,nominal,,M=男;F=女,{M;F},NA,住院首页,,A. Wang,v1.0
clinical_baseline,t_stage,原发灶分期,ordinal,,T1<T2<T3<T4,{T1;T2;T3;T4},NA,病理报告·pTNM,,A. Wang,v1.0
clinical_baseline,time_origin,时间原点,date,,,,,手术记录·手术日期,see outcome-and-followup-data.md,A. Wang,v1.0
clinical_baseline,os_event,总生存事件,nominal,,1=死亡;0=删失,{0;1},NA,随访记录,see outcome-and-followup-data.md,A. Wang,v1.0
clinical_baseline,os_time,总生存时间,continuous,months,,>0,NA,,last_contact_or_event - time_origin,A. Wang,v1.0
```

This example is a prespecified one-row-per-patient baseline/OS snapshot, not a schema for repeated
exams or endpoints. Its passport declares `patient_id` unique; repeated source records retain their
own keys and the snapshot selection/aggregation rule.

Outcome and follow-up fields follow `outcome-and-followup-data.md`; text-sourced variables
follow `chinese-clinical-text-abstraction.md`.

## Pre-handoff checks

1. Every delivered table has a grain/key/cardinality passport. Every column has a dictionary row; every row maps to a
   delivered column or is marked `not_yet_collected`.
2. Missing-code discipline verified programmatically (scan coded fields for 0/blank/Unknown
   used as missing).
3. Codings match what the analysis script actually consumes (spot-check parsing, encoding,
   factor levels).
4. Dictionary version recorded in `research_record/`; downstream stages refuse a table with no
   dictionary version (handoff rule, `radiology-pipeline/stage-gates-and-handoffs.md`).
