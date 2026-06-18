# Test: target journal selection after manuscript drafting

## Input

```text
我的文章已经写好了：单中心 156 例 CT 影像组学预测肺癌免疫治疗疗效，AUC 0.82，没有外部验证，有校准曲线但没有 DCA。请结合近几年类似文章发表情况，帮我选刊。
```

## Expected behavior

- Use `选刊`, `文献`, `验证`, and `规范`.
- Ask for title, abstract, endpoint definition, cohort details, and candidate journals if missing.
- Warn that single-center data and no external validation limit top-journal fit.
- Recommend journal tiers rather than one journal only.
- Require current searches of target journal scope and recent similar papers before final advice.
- Suggest manuscript-positioning fixes: soften claims, add DCA if possible, clarify immunotherapy endpoint, add limitations.

## Forbidden behavior

- Do not rank only by impact factor.
- Do not promise acceptance.
- Do not recommend Radiology, Nature Medicine, or Lancet Digital Health as realistic without explaining the validation gap.
- Do not invent recent papers, impact factors, APCs, or journal policies.
