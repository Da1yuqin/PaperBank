# Rebuttal · 规则与模板

方括号填写真实材料；模拟反馈供作者内部使用。

<a id="prepare"></a>
## 2. 整理问题与证据

先读完整 review，再写回答。不要只盯着 Questions：具体关切也可能出现在 Weaknesses、建议和评分理由里。

- 【铁律】Weaknesses、Questions、建议和评分理由里的具体关切都要回答；保留原意，一句话有多问就拆开。
- 逐题记录：原问题 → 回应类型 → 现有依据及位置 → 缺口。
- 定义不清给定义，流程不清给案例，效果存疑给对照，实际错误就修正。
- 优先整理已有实验；确实缺证据时，提出能区分争议解释的最小检验，交作者决定。
- 【铁律】向工具提供材料前，确认当轮保密与 AI 规则允许；不上传密钥、个人数据或无权使用的材料。

<a id="prepare-template-1"></a>
### 问题清单

```markdown
| ID | 原问题 | 需要回答什么 | 已有证据与位置 | 缺口 |
| :--- | :--- | :--- | :--- | :--- |
| Q1.1 | 【审稿原话】 | 【具体结论】 | 【节、表、记录】 | 【仍缺什么；没有则写无】 |
| Q1.2a | 【子问题：定义】 | 【对象与判定方式】 | 【定义所在位置】 | 【歧义在哪里】 |
| Q1.2b | 【子问题：有效性】 | 【必要对照】 | 【已有比较】 | 【不能由现有结果回答的部分】 |
```

这张表供作者整理问题；正式回复按下一节的 Q&A 交付。

<a id="response-format"></a>
## 3. 逐题回复格式

一题一个答案：结论 → 证据 → 解释 → 位置。首句把问题答了，后面才有必要读。

- 【铁律】默认交付：每位审稿人单独一个 Markdown 代码块；提交时按平台要求粘贴正文。
- 【铁律】问题标题固定为 > **Q1.1: [问题标题]**：引用、加粗、编号、冒号都保留。
- 【铁律】一个大问题有多问，拆成 Q1.1a、Q1.1b，标题忠于原意。
- 【铁律】第一句直接回答：是否题先给结论，证据不足就说明不能判断；原因题给原因，流程题给操作，数值题给具体值。
- 【铁律】回答之后给必要设置、证据、解释与表号、节号或行号；不先感谢，不先讲背景。
- 【铁律】可比较数据用表格，写全条件、单位、指标方向和统计口径；表后解释结论，不逐格复述。
- 【铁律】一个小点一段；问题之间空一行。感谢具体、克制，放在相关解释后或文末，第一句仍先回答问题。
- 【铁律】修改给真实位置；只有实际改过稿件，才能写成已修改。
- 【铁律】同一实验跨 Q 引用，首次定义简短名称，后续统一使用；每个 Q 仍要独立读懂。

<a id="response-format-template-1"></a>
### 一位审稿人的完整回复

```markdown
> **Q1.1: How does [method] differ from [closest prior work]?**

The main difference is [specific mechanism or evaluation target]. [Prior work] uses [input or operation] to produce [output], whereas [our method] uses [corresponding input or operation] to produce [corresponding output]. This difference addresses [precise limitation] under [stated scope]. The description and comparison are in Section [X] and Table [Y].

> **Q1.2: Does [component] improve [metric]?**

Under [tested setting], [component] [improves / does not improve] [metric] relative to [control] by [absolute difference and unit]. We hold [necessary conditions] fixed and change only [tested component].

| Configuration | [Metric and direction] | [Sample size or number of runs] |
| :--- | :---: | :---: |
| [Control] | [Verified value] | [Verified count] |
| [With component] | [Verified value] | [Verified count] |

The observed [finding] addresses [the reviewer’s concern] because [explanation of the result], supporting [the corresponding contribution]. The results and protocol are in [table or record] and Section [X].
```

方括号全部换成已核实材料；增删表格列取决于比较需要，不能删掉影响公平性或解释结果的条件。若 Q1.2 同时问定义与效果，拆为 Q1.2a、Q1.2b，分别首句回答。

<a id="response-format-example-1"></a>

### 一段回复怎样读

教学模板：把方括号换成自己的真实证据。

**English 教学改写**

Under [tested setting], [component] improves [metric] relative to [control] by [absolute difference and unit]. We hold [confounding factors] fixed and compare [configurations] on [same test set]. The observed [finding] addresses [the reviewer’s concern] because [explanation of the result], supporting [the corresponding contribution]. The protocol and results are in Section [X] and Table [Y].


**高亮与旁批**

1. **Under [tested setting], [component] improves [metric] relative to [control] by [absolute difference and unit].**：【铁律】先答问题。首句给答案：条件、比较对象、指标与差异都在。仅在相应结果支持时使用。
2. **We hold [confounding factors] fixed and compare [configurations] on [same test set].**：【铁律】交代对照。交代怎样得到答案；对照要对应审稿人的质疑。
3. **The observed [finding] addresses [the reviewer’s concern] because [explanation of the result], supporting [the corresponding contribution].**：分析实验。实验后解释现象，回应审稿人的疑虑，并落到论文的创新点和贡献。
4. **The protocol and results are in Section [X] and Table [Y].**：【铁律】给出位置。给位置，便于核查。

StrongResponse · 原创教学模板

原创教学模板，不是真实审稿回复。

本指南原创内容采用 CC BY 4.0；转载请附作者、原文链接与许可，改写注明改动。

<a id="answer-types"></a>
## 4. 四类回答模板

按问题选证据，不强行把每个问题都变成补实验。澄清用定义和流程，效果用比较，机制用能区分解释的检验。

- 【铁律】解释性答复：先定义具体对象，再给输入、操作、输出；必要时用一条样例走完整个流程。
- 【铁律】实证答复：报告真实绝对值、比较对象、指标方向与必要条件。平均值涉及波动时给相应不确定性。
- 【铁律】合理不同意见：指出争议前提和证据，只讨论论文；确有错误就修正，不评价审稿人的能力或动机。
- 【铁律】承诺不是证据。阶段性结果写实际范围；没有直接证据就说明缺口、缩小主张，不能把计划写成已完成。
- 【铁律】表格保留影响判断的设置差异和负结果；删列是为了省阅读时间，不能为了改变结论。

<a id="answer-types-template-1"></a>
### 4.1 定义与流程

```markdown
> **Q1.2a: What does [term] mean, and how is it used?**

[Term] denotes [concrete object and decision rule]. For input [x], [module] performs [operation] and returns [y] to [next module]. This interface is specified in Section [X]; [example or algorithm] shows [the disputed step].
```

术语先落到对象；举例要解释被问到的环节，不重讲整篇方法。

<a id="answer-types-template-2"></a>
### 4.2 实验与对照

```markdown
> **Q1.2b: Could [alternative explanation] account for [result]?**

Under [matched setting], the result [persists / does not persist] when [confounding factor] is controlled. We compare [A] and [B] with identical [necessary conditions]; [metric] is [verified A] versus [verified B] ([direction]; Table [R]). This comparison [supports / does not support] [bounded conclusion]. [Remaining uncertainty] is not resolved by this test.
```

对照必须能检验替代解释；同一批数据换个表头，不等于排除了混淆。

<a id="answer-types-template-3"></a>
### 4.3 有依据的不同意见

```markdown
> **Q2.1: Does [specific concern] invalidate [claim]?**

[Specific concern] does not invalidate [bounded claim] under [stated setting], because [verified fact]. The concern assumes [premise], whereas [paper location or verified record] specifies [relevant fact]. This supports [limited conclusion]. We agree that [valid part of the concern], and [verified clarification or correction, if applicable] is documented in [location].
```

只有证据支持时才使用“不推翻主张”的首句；依据不够就说明不能判断。不同意见也要承认成立的部分。

<a id="answer-types-template-4"></a>
### 4.4 目前不能回答

```markdown
> **Q2.2: Does [claim] hold under [untested condition]?**

We do not have direct evidence for [claim] under [untested condition]. The available result in [location] covers [tested scope] only. We therefore limit our conclusion to [supported claim]. Establishing [broader claim] would require [specific comparison or measurement].
```

没有依据就把边界写清楚；只有稿件确已修订时，才能追加具体修改与位置。

<a id="follow-up"></a>
## 6. 追问与 AC letter

追问用 Rebuttal skill 只补新增信息。完成回复后，再用独立的 AC letter skill 总结审稿人的评价、改分与核心回应。

- 【铁律】保留原 Q 编号和问题关系；新子问可续为 Q1.2c，编号仍以平台要求为准。
- 【铁律】先回答追问，再定位新增证据；已经讲清的背景用位置引用。

<a id="follow-up-template-1"></a>
### 6.1 追问回复模板

```markdown
> **Q1.2c: [Faithful title of the follow-up question]**

[Direct answer to the new question, with the necessary scope].

**New evidence**: Compared with Q1.2, we now provide [verified result or clarification]. Under [necessary setting], [comparison or reasoning] shows [specific finding] ([table / section / lines]). This supports [bounded conclusion] because [link between the evidence and the question].

**Revision**: Section [X], lines [Y–Z], now states: “[Exact wording of the completed revision].”

**Remaining issue**: The evidence covers [tested scope]; it does not establish [unresolved claim]. [Specific evidence still needed, if any].
```

保留原 Q 编号，追问新子项续编。填真实证据与位置；无新结果就给已有依据和明确边界。未改稿删 Revision，没有剩余疑问删 Remaining issue；可比较数据改用紧凑表格。

---

Da1yuqin / [StrongResponse](https://da1yuqin.github.io/StarPaper/StrongResponse/)，[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)。转载请保留署名、出处及许可，改写注明改动。
