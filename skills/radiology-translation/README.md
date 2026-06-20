# radiology-translation

**Stage 5 — Submission & Translation.** Move a validated model from retrospective performance
toward clinical use — the step that earns a clinical-utility claim.

## What it does

- **Use scenario** — pathway position (screening/triage/diagnosis/staging/prognosis/response/
  surveillance/MDT), output type, decision-maker, and the cost of false positives/negatives.
- **Reader (MRMC) study** — radiologist alone vs +AI, washout, randomisation, reader experience,
  time/confidence outcomes, the right statistic.
- **Threshold-to-action map** — operating points tied to clinical actions; net-benefit /
  decision-curve framing; calibration as prerequisite.
- **Prospective / real-world plan** — temporal/prospective/RWE design, PACS/RIS integration,
  drift monitoring.
- **Claim ladder** — what each evidence level licenses, with the honest current claim marked.

## Trigger examples

- "帮我设计读者研究、医生+AI 增益、前瞻性验证。"
- "What does it take to claim clinical utility / move toward deployment?"
- "Map my model's threshold to a clinical action and net benefit."

## Reference files

| File | Use |
|---|---|
| `references/use-scenario.md` | Pathway position, output, error costs |
| `references/reader-study.md` | MRMC design: readers, washout, arms, outcomes |
| `references/threshold-to-action.md` | Operating point → action; net benefit / DCA |
| `references/prospective-deployment.md` | Prospective/RWE design, PACS/RIS, drift |

## Handoffs

`radiology-stats` (MRMC, net benefit, DCA) · `radiology-reporting` (DECIDE-AI/CONSORT-AI) ·
`radiology-design` (validation cohort) · `radiology-figure` (net-benefit/reader plots).

Plans research and evaluation only — no individual-patient clinical or diagnostic advice.
