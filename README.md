# Radiology Skills

Codex skill for radiomics, medical imaging deep learning, imaging AI frontiers,
study design, validation audit, reporting checklists, manuscript writing, and
reviewer response.

## What It Covers

- 入口: route user requests and build a study card
- 前沿: identify recent research frontiers and match them to user data
- 文献: organize high-impact radiomics and imaging deep learning literature
- 组学: audit traditional radiomics workflows
- 深度: design and audit medical imaging deep learning studies
- 设计: turn datasets into feasible research projects
- 验证: detect leakage, weak validation, and metric/reporting gaps
- 规范: choose CLAIM, CLEAR, RQS, IBSI, TRIPOD+AI, PROBAST+AI, STARD-AI, and related frameworks
- 数据: handle imaging data, masks, privacy, and availability statements
- 写作: draft Methods, Results, Discussion, titles, and abstracts
- 回复: prepare reviewer responses
- 中文: support Chinese author notes and terminology
- 依据: source and guideline provenance

## Install

Clone this repository and copy the skill folder into your Codex skills directory:

```powershell
git clone https://github.com/huang-sir1/radiology-skills.git
cd radiology-skills
New-Item -ItemType Directory -Force "$env:USERPROFILE\.codex\skills" | Out-Null
Copy-Item -Recurse -Force .\radiology-skills "$env:USERPROFILE\.codex\skills\"
```

On macOS or Linux:

```bash
git clone https://github.com/huang-sir1/radiology-skills.git
cd radiology-skills
mkdir -p ~/.codex/skills
cp -R radiology-skills ~/.codex/skills/
```

Restart Codex or reload skills if needed.

## Use

Ask Codex with:

```text
Use $radiology-skills to design, audit, or write a radiomics or medical imaging deep learning study.
```

Typical requests:

- Find recent radiology AI frontiers for my dataset.
- Audit my radiomics Methods section for leakage and reporting gaps.
- Design a validation plan for a CT/MRI/PET deep learning model.
- Draft Methods, Results, Discussion, or reviewer responses for imaging AI manuscripts.

## Notes

This skill helps plan and audit research. It does not provide clinical diagnosis,
treatment advice, or patient-specific medical interpretation.
