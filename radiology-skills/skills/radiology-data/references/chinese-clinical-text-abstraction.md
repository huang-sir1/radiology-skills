# Chinese clinical text abstraction

Variables for retrospective imaging studies usually live in Chinese free text: discharge
summaries (出院小结), operative notes, pathology and radiology reports. Default to structured
manual abstraction; add rules or LLM prefill only where they beat manual work on measured
agreement.

## Three-tier strategy

| Tier | Use when | Discipline |
|---|---|---|
| **Manual abstraction** (default) | any variable; small-to-moderate n | dual-abstract a pre-specified subset; adjudicate; measure agreement |
| **Rule / regex** | stable-phrasing fields (诊断, 手术日期, 分期) at larger n | validate against a manual sample first; log every pattern version |
| **LLM-assisted prefill** | large n, well-defined variables | prefill only — a human verifies **every** value against the source quote; de-identify text before any external service (governance: `radiology-ethics`) |

Regex or LLM output never enters the dataset unverified. Record tool + version + date for
either tier.

## Red lines (all three, always)

1. **Definitions before abstraction** — every variable already exists in the data dictionary
   (`data-dictionary-spec.md`) with coding fixed before anyone opens a chart.
2. **Source quote retained** — every abstracted value keeps the verbatim source snippet and
   its location (report type + date), so any value can be re-checked without reopening the HIS.
3. **Grain-aware keys** — `patient_id` groups the person but is **not a universal join key**.
   Preserve an `abstraction_id` plus the relevant encounter/exam/lesion/timepoint, variable,
   source-document and review-version keys. A patient can have multiple variables, reports and
   timepoints. Join to analysis tables using the complete key or a frozen temporal/aggregation
   rule; unresolved many-to-many pairing returns `STOP_JOIN_CARDINALITY_UNRESOLVED`
   (`cohort-assembly-and-id-reconciliation.md`, `outcome-and-followup-data.md`).

## Manual abstraction form

```text
abstraction_id,patient_id,encounter_id,source_document_id,observation_time,variable_name,value,coding_applied,source_quote,source_location,abstractor,date,review_version,status
ABS-0007-01,PAT-0007,ENC-02,DOC-008,2025-11-02,t_stage,T3,pT3,病理回报：胃窦腺癌，浸润至浆膜下层（pT3）,病理报告,A. Wang,2026-01-10,v1,verified
```

- Two abstractors independently code a pre-specified proportion (state it, e.g. the first [N]
  cases); a third senior person adjudicates disagreements.
- Keep a disagreement log (variable, both values, ruling) — it trains the next abstractors and
  feeds the Methods sentence.
- Report the agreement measured on the double-coded subset in Methods; never invent the value.

## Regex starter patterns (validate before trusting)

```python
import re
text = open("discharge.txt", encoding="utf-8").read()

# 手术日期：优先“手术日期：YYYY年M月D日”，退化匹配“于YYYY年M月D日行…术”
m = re.search(r"手术日期[:：]\s*(\d{4})\s*年\s*(\d{1,2})\s*月\s*(\d{1,2})\s*日", text)
m = m or re.search(r"于\s*(\d{4})\s*年\s*(\d{1,2})\s*月\s*(\d{1,2})\s*日\s*行", text)

# TNM 分期：pT?N?M? 或 cT?N?M?
m = re.search(r"[pc]T([0-4is]+)\s*N([0-3X]+)\s*M([01X]+)", text)

# 出院诊断：取“出院诊断”后的文本，到下一标题为止
m = re.search(r"出院诊断[:：]\s*(.+?)(?:\n\s*\n|出院情况|出院医嘱)", text, re.S)
```

- Chinese punctuation variants (：/:, full/half width, line breaks) break naive patterns —
  normalise the text first.
- Run every pattern against a manual sample; record hit-rate and error modes, then decide the
  tier **per variable**.

## LLM-assisted prefill workflow

1. De-identify the text (name / ID / date scrub) before any external model; prefer an
   institutional or local deployment for clinical text.
2. Prompt for **variable + verbatim supporting quote**, never just the value.
3. A human accepts or rejects each prefilled value against the quote; rejections go to the
   disagreement log with a reason.
4. Record model, version, prompt version, and date in the abstraction log.

## Handoff

- Deliver: filled abstraction forms, disagreement log, agreement result, tool/version record,
  and the dictionary version used.
- The modelling side rejects tables without source-quote coverage for key variables (handoff
  rule, `radiology-pipeline/stage-gates-and-handoffs.md`).
