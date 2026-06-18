# Example: pre-submission audit with annotation, statistics, figures, and reproducibility

## User request

```text
我的肺结节 CT 影像组学文章已经写好了。ROI 是两位医生手工勾画，模型用了 LASSO 和 logistic 回归，内部测试集 AUC 0.84，没有外部验证。图里有 ROC 和 nomogram，但没有校准曲线和 DCA。请帮我投稿前预审，并告诉我补充材料怎么整理。
```

## Expected module route

- `标注`
- `统计`
- `图表`
- `预审`
- `复现`
- `组学`
- `验证`
- `规范`

## Expected output shape

```text
任务定位
- 主模块：预审
- 相关模块：标注、统计、图表、复现、组学、验证、规范
- 当前最大风险：单中心无外部验证、特征筛选流程可能泄漏、图表缺少校准和临床实用性

分模块建议
| 模块 | 关键判断 | 必须补充 | 建议动作 |

可直接使用内容
[Methods/Discussion/Data Availability text only after facts are supplied]

需要作者确认
- 训练/验证/测试划分方式
- 两位医生年资、盲法、分歧处理、ICC/Dice
- LASSO 是否只在训练集完成
- 阈值选择方法
- 伦理和代码/数据共享限制
```
