# StrongResponse · 规则与模板

以下均为原创教学模板，不是真实审稿记录；方括号填写已核实材料。

<a id="prepare"></a>
## 1. 整理问题与证据

先读完整 review，再写回答。不要只盯着 Questions：具体关切也可能出现在 Weaknesses、建议和评分理由里。

- 保留原问题和顺序；一句话问了定义、对照和成本，就拆成三问。
- 逐题记录：原问题 → 回应类型 → 现有依据及位置 → 缺口。
- 定义不清给定义，流程不清给案例，效果存疑给对照，实际错误就修正。
- 优先整理已有实验；确实缺证据时，提出能区分争议解释的最小检验，交作者决定。
- 向工具提供材料前，确认当轮保密与 AI 规则允许；不上传密钥、个人数据或无权使用的材料。

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
## 2. 逐题回复格式

一题一个答案：结论 → 证据 → 解释 → 位置。首句把问题答了，后面才有必要读。

- 默认交付：每位审稿人单独一个 Markdown 代码块；提交时按平台要求粘贴正文。
- 问题标题固定为 > **Q1.1: [问题标题]**：引用、加粗、编号、冒号都保留。
- 一个大问题有多问，拆成 Q1.1a、Q1.1b，标题忠于原意。
- 第一句直接回答：是否题先给结论，证据不足就说明不能判断；原因题给原因，流程题给操作，数值题给具体值。
- 回答之后给必要设置、证据、解释与表号、节号或行号；不先感谢，不先讲背景。
- 列点用 **Evidence**: 等短标签；适合比较的数据用表格，注明条件、单位与指标方向。
- 一个小点一段；问题之间空一行，不堆分隔线，简短致谢放最后。
- 修改给真实位置；只有实际改过稿件，才能写成已修改。

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

This comparison supports [bounded conclusion]; it does not establish [untested mechanism or generalization]. The results and protocol are in [table or record] and Section [X].
```

方括号全部换成已核实材料；增删表格列取决于比较需要，不能删掉影响公平性或解释结果的条件。若 Q1.2 同时问定义与效果，拆为 Q1.2a、Q1.2b，分别首句回答。

<a id="response-format-example-1"></a>

### 一段回复怎样读

教学模板：把方括号换成自己的真实证据。

**English 教学改写**

Under [tested setting], [component] improves [metric] relative to [control] by [absolute difference and unit]. We hold [confounding factors] fixed and compare [configurations] on [same test set]. The result supports [bounded conclusion], but does not establish [untested mechanism]. The protocol and results are in Section [X] and Table [Y].


**高亮与旁批**

1. **Under [tested setting], [component] improves [metric] relative to [control] by [absolute difference and unit].**：先答问题。首句给答案：条件、比较对象、指标与差异都在。仅在相应结果支持时使用。
2. **We hold [confounding factors] fixed and compare [configurations] on [same test set].**：交代对照。交代怎样得到答案；对照要对应审稿人的质疑。
3. **The result supports [bounded conclusion], but does not establish [untested mechanism].**：限定结论。说明证据支持到哪里，避免把相关性写成因果。
4. **The protocol and results are in Section [X] and Table [Y].**：给出位置。给位置，便于核查。

StrongResponse · 原创教学模板

原创教学模板，不是真实审稿回复。

本指南原创内容采用 CC BY 4.0；转载请附作者、原文链接与许可，改写注明改动。

<a id="answer-types"></a>
## 3. 四类回答模板

按问题选证据，不强行把每个问题都变成补实验。澄清用定义和流程，效果用比较，机制用能区分解释的检验。

- 解释性答复：先定义具体对象，再给输入、操作、输出；必要时用一条样例走完整个流程。
- 实证答复：报告真实绝对值、比较对象、指标方向与必要条件。平均值涉及波动时给相应不确定性。
- 合理不同意见：指出争议前提和证据，只讨论论文；确有错误就修正，不评价审稿人的能力或动机。
- 没有直接证据：明确能回答什么、不能回答什么，缩小主张。计划不是结果，空口承诺也不是证据。
- 表格保留影响判断的设置差异和负结果；删列是为了省阅读时间，不能为了改变结论。

<a id="answer-types-template-1"></a>
### 3.1 定义与流程

```markdown
> **Q1.2a: What does [term] mean, and how is it used?**

[Term] denotes [concrete object and decision rule]. For input [x], [module] performs [operation] and returns [y] to [next module]. This interface is specified in Section [X]; [example or algorithm] shows [the disputed step].
```

术语先落到对象；举例要解释被问到的环节，不重讲整篇方法。

<a id="answer-types-template-2"></a>
### 3.2 实验与对照

```markdown
> **Q1.2b: Could [alternative explanation] account for [result]?**

Under [matched setting], the result [persists / does not persist] when [confounding factor] is controlled. We compare [A] and [B] with identical [necessary conditions]; [metric] is [verified A] versus [verified B] ([direction]; Table [R]). This comparison [supports / does not support] [bounded conclusion]. [Remaining uncertainty] is not resolved by this test.
```

对照必须能检验替代解释；同一批数据换个表头，不等于排除了混淆。

<a id="answer-types-template-3"></a>
### 3.3 有依据的不同意见

```markdown
> **Q2.1: Does [specific concern] invalidate [claim]?**

[Specific concern] does not invalidate [bounded claim] under [stated setting], because [verified fact]. The concern assumes [premise], whereas [paper location or verified record] specifies [relevant fact]. This supports [limited conclusion]. We agree that [valid part of the concern], and [verified clarification or correction, if applicable] is documented in [location].
```

只有证据支持时才使用“不推翻主张”的首句；依据不够就说明不能判断。不同意见也要承认成立的部分。

<a id="answer-types-template-4"></a>
### 3.4 目前不能回答

```markdown
> **Q2.2: Does [claim] hold under [untested condition]?**

We do not have direct evidence for [claim] under [untested condition]. The available result in [location] covers [tested scope] only. We therefore limit our conclusion to [supported claim]. Establishing [broader claim] would require [specific comparison or measurement].
```

没有依据就把边界写清楚；只有稿件确已修订时，才能追加具体修改与位置。

<a id="revise-loop"></a>
## 4. Revise loop

回到原 review，逐题查漏答、证据与逻辑。先修内容，再缩文字；一篇流畅的答非所问，还是答非所问。

- 按原问题清单检查，逐项定位具体 Q、段落或表格；不能因为别处提过就算回答。
- 先只读题目与首句：是否答了原问题？再读证据：能否支撑这句结论、区分争议解释？
- 核对数字、引用、范围、必要条件和位置；表格要能独立说明比较了什么。
- 只改未通过项，改后重查同一张清单；新证据引出新问题时补入清单。
- 覆盖完整、证据对应、逻辑成立、篇幅合规后停止，交作者定稿。缺实验时列出需要作者决定的事项，不预测提分或录用。

<a id="revise-loop-template-1"></a>
### 让 Codex 逐题检查

```markdown
运行 revise loop。输入为论文【】、原 review【】、回复【】、真实证据【】、当轮规则【】。

按 review 原顺序逐题检查：
1. 原问题是否有明确对应的 Q？
2. 首句是否直接回答，而非重复问题？
3. 证据是否支持结论、区分争议解释，且保留必要条件与范围？
4. 图表、引用和修改位置是否真实？

对未通过项输出：Q 编号｜原问题｜回复位置｜具体缺口｜最小改法｜还缺的证据。只修改获授权的回复文件，不自动跑实验或改稿。修改后重查同一清单；最终交付每位审稿人的独立 Markdown，把检查记录与证据缺口单独给作者。
```

检查记录不粘进正式回复；它帮助作者决定如何修改，不代替作者判断。

<a id="follow-up"></a>
## 5. 追问与 AC 总结

追问只补新增信息。给 AC 的总结写问题、回应、证据和剩余分歧，不重贴整份 rebuttal。

- 保留原 Q 编号和问题关系；新子问可续为 Q1.2c，编号仍以平台要求为准。
- 先回答追问，再定位新增证据；已经讲清的背景用位置引用。
- AC 指 Area Chair。总结按重要关切组织，写清哪些已澄清、哪些仍未解决；引用评价须与原文一致。
- 不猜未回复审稿人的态度，不请求提分或接收，把判断交给审稿方。

<a id="follow-up-template-1"></a>
### 5.1 第二轮追问

```markdown
> **Q1.2c: Follow-up on [specific unresolved point]**

[Direct answer to the new question]. Compared with our response to Q1.2, the new information is [verified evidence or clarification], located in [location]. This [addresses / leaves unresolved] [specific point]; [remaining limitation] remains outside the tested scope.
```

只写新增信息；若问题仍未解决，直说证据缺口。

<a id="follow-up-template-2"></a>
### 5.2 给 AC 的简要总结

```markdown
The main remaining issue concerns [precise issue]. Our response provides [verified evidence and location], supporting [bounded conclusion].

**Reviewer [ID], Q[X.X].** The concern was [faithful summary]. We answered it with [comparison or clarification]; [verified result or revised wording] is in [location]. [Remaining disagreement or limitation, if any].

**Reviewer [ID], Q[Y.Y].** The concern was [faithful summary]. The response distinguishes [explanation A] from [explanation B] using [evidence and location]. [What the evidence establishes and leaves unresolved].
```

没有实质分歧就改为关键问题总结。内容与篇幅服从当轮规则；不列推测态度、身份或提分诉求。

---

Da1yuqin / [StrongResponse](https://da1yuqin.github.io/PaperBank/StrongResponse/)，[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)。转载请保留署名、出处及许可，改写注明改动。
