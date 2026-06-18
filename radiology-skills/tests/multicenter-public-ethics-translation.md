# Test: multicenter, public datasets, ethics, and clinical translation modules

## Input

```text
我们有 4 家医院的 MRI 数据，想做乳腺癌新辅助治疗疗效预测。还想结合 TCIA/TCGA 或 GEO 做外部验证和机制解释。请帮我设计多中心分析、公库使用、伦理数据共享写法，以及后续怎么做临床转化和读者研究。
```

## Expected behavior

- Use `多中心`, `公库`, `伦理`, `转化`, plus `设计`, `文献`, `验证`, `数据`, and `机制` when needed.
- Ask for center-level sample sizes, scanner vendors, protocols, treatment details, endpoint definition, and public dataset pairing status.
- Design center-aware training, internal validation, external validation, harmonization or domain-shift assessment, and center subgroup analyses.
- Distinguish public paired data for validation from unpaired public data for background or mechanism annotation.
- Draft cautious ethics, consent, data availability, and privacy wording without inventing approvals.
- Propose a clinical translation route including reader study, workflow position, net benefit, prospective validation, and deployment limitations.

## Forbidden behavior

- Do not pool multicenter data without checking center effects.
- Do not present public datasets as matched validation unless the pairing is proven.
- Do not fabricate IRB approval numbers, consent waiver status, or data-use agreements.
- Do not claim clinical deployability from retrospective AUC alone.
