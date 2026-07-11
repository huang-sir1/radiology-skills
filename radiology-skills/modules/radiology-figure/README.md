# radiology-figure

面向高水平影像期刊投稿的统计图、影像图版和流程图制作 skill。它的目标是把“能看懂的图”提升为“审稿人能核查、排版能使用、统计表达站得住”的 publication-quality figure。

## 它能做什么

- 生成 **statistical charts**：ROC、DeLong 标注、calibration、decision-curve analysis、forest / SROC、Kaplan-Meier with numbers-at-risk、Bland-Altman、box / violin、heatmap。
- 生成 **radiogenomics figures**：MOFA / factor plots、deconvolution stacked bars、habitat maps、correlation heatmaps。
- 设计 **imaging panels**：windowing label、arrow、inset、scale bar、panel label、去标识化。
- 输出 **flow diagrams**：CONSORT、STARD、PRISMA 等流程图。
- 优先输出可编辑 vector（`.svg` / `.pdf`）和 300 dpi 以上 raster。

## 参考文件

```text
references/
├── radiology-figure-guidelines.md  格式、分辨率、尺寸、字体、色彩、去标识化
├── chart-types.md                  选择并参数化正确图型
├── api.md                          rcParams、palette、ROC/calibration/forest/KM helpers
├── imaging-panels.md               montage、windowing、arrow、scale bar、匿名化
└── design-theory.md                typography、layout、color-blind-safe palette、去冗余
```

## 默认规范

- Vector-first；文字保持为可编辑文本；配套导出 300 dpi 以上 raster。
- 采用 Arial / Helvetica 等 sans-serif；单栏约 85 mm，双栏约 170 mm；印刷尺寸下约 7 pt 以上。
- 使用 color-blind-safe palette，不单独依赖红/绿；显示 CI bands、n 和诚实坐标轴。
- 所有影像图版必须去标识化；必要时标注 WL / WW 与 scale bar。

## 典型触发

- “把两个模型的 ROC 画在同一批病例上，并标注 DeLong p 值。”
- “给预测模型画 calibration plot 和 decision curve。”
- “按 radiomic-risk group 画 Kaplan-Meier，并带 numbers-at-risk。”
- “做一个 2×3 MRI montage，加箭头、scale bar，并去标识化。”

## 边界

只绘制用户提供或已加载的数据；示例数据会明确标记。底层统计交给 `radiology-stats`，报告规范适配交给 `radiology-reporting`。
