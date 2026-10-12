# 局限性与结论边界：按需参考

以下为通用规则与教学模板，不是真实论文原文、研究事实或实测。

#### Limitations：单段两点

先承认有据工作，再说明与任务相关的具体边界；两点合成一个自然段。

两句写在同一个自然段；although 不再搭配 but。复数边界用 warrant，单数用 warrants。

教学模板；方括号填有据工作与具体边界，不是研究事实。

- 【铁律】本套 CS 写作约定：Limitations 全节只写一个自然段，用 First, 和 Second, 引出两点，不另起段、列条目或加小标题。官方格式与当前用户要求优先。
- 【铁律】每点先用 although 简短说明已完成的有据工作，再给具体的特殊或长期边界；已有措施不能写成解决了尚未验证的问题。
- 【铁律】真实有效性限制与全文结论一致；若限制动摇核心结论，先缩小或修正结论，不用让步句掩盖。

本套 CS 写作约定；官方格式与当前用户要求优先

First, although we have [verified work addressing the main difficulty], [specific special condition] still warrants further study.

首先，尽管我们已完成[针对主要难点的有据工作]，[具体特殊情况]仍值得进一步研究。

**第 1 句：**First 引出第一点；although 后交代已处理什么，主句落在具体边界。已有工作必须可核验。

Second, although we have [another verified contribution], [specific longer-term condition] still warrants further study.

其次，尽管我们已完成[另一项有据工作]，[具体长期情况]仍值得进一步研究。

**第 2 句：**Second 引出另一项独立边界，与前句在同一自然段。说明研究对象，不堆贡献和防御措施。

**完整 LaTeX 结构模板**

```latex
First, although we have [verified work addressing the main difficulty], [specific special condition] still warrants further study. Second, although we have [another verified contribution], [specific longer-term condition] still warrants further study.
```

---

Da1yuqin / [StarPaper](https://da1yuqin.github.io/StarPaper/)，[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)。转载保留署名、出处与许可，改编注明改动。
