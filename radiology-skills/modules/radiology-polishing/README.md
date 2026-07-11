# radiology-polishing

面向已经写好的影像科研英文段落的 _Radiology_ house style 润色 skill。它不是重写研究内容，而是在不改变数字、结论和证据边界的前提下，让语言更精确、统计表达更规范、语气更符合高水平影像期刊。

## 它能做什么

- 压缩冗余句子，让每句话只承载一个清晰论点。
- 规范 **statistical reporting**：estimate + 95% CI、exact p-values、单位、百分比、样本量、test names。
- 应用 American English、缩写规则、时态和 Radiology 风格表达。
- 识别 **overclaiming**：过度因果、过强临床效用、单中心研究外推、未验证机制，并给出有边界的改写。

## 参考文件

```text
references/
├── radiology-house-style.md  voice、tense、American spelling、abbreviations、units
├── stat-reporting.md         p-values、CIs、decimals、%、n、ranges、test names
└── style-guardrails.md       overclaim / causation 检测、hedging、禁用表达
```

## 典型触发

- “把这段 Results 按 Radiology 风格润色，并修正统计格式。”
- “改成 American English 和期刊风格。”
- “单中心回顾性研究这样写 conclusion 会不会 overclaim？”

## 边界

不会修改已报告的数值、CI、p 值或引用；怀疑错误时会标记。需要新写内容时交给 `radiology-writing`，缺失统计量交给 `radiology-stats`。
