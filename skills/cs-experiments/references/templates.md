# 实验、评价与诊断：按需参考

以下为通用规则与教学模板，不是真实论文原文、研究事实或实测。

#### Experiments：承接方法，概述发现

先列 Intro 主张与检验标准；成稿章首承接方法，概述被测对象和主发现，再进入实际分析。

教学模板；【】填真实材料。

- RQ 可用于组织，不必每表一个编号；标题写 Main Results、Ablation Studies 或具体目的。
- 按论文贡献选实验，不照搬另一类研究的实验清单。
- 章首先概述已有证据支持的主发现，再用 Specifically 展开分析；没有实际结果时，不用模板编造发现。

通用要求；推荐结构模板

After constructing [method or benchmark], we evaluate [actual target] on [scope].

构建[方法或基准]后，我们在[范围]内评价[实际对象]。

**第 1 句：**承接前章产物，交代实际被测对象与范围。

Our results show [supported main finding] under [tested conditions].

结果显示，在[已测试条件]下，[有证据支持的主发现]。

**第 2 句：**先让读者知道发现什么，范围与正文实测一致。

Specifically, we examine whether [design] addresses [Intro limitation] using [actual comparison].

具体而言，我们用[实际比较]检验[设计]是否处理了[引言局限]。

**第 3 句：**展开上一句的发现与检验依据；设计、局限和比较必须真实对应。

We further analyze [actual additional question] through [existing evidence or control].

我们进一步通过[已有证据或对照]分析[实际的补充问题]。

**第 4 句：**只引出实际存在的分析，不自动要求消融或虚构串行依赖。

#### Experimental Setup：比较设置

集中定义指标、方向、分母、简称与实验设置，新增指标说明用途与贡献。

教学模板；【】填真实材料。

- Metrics：一个紧凑自然段，先总述指标类别，再编号并加粗各指标名；各项给定义、方向、单位、分母、汇总和无效输出处理。Models 或 Baselines 独立介绍。
- Baselines：按路线分类，给引用和可影响结果的共享条件。简介讲它做什么，结果差异留给分析。
- Implementation Details：Method 出现的参数给实际值与选择依据；完整参数表可放附录。训练、推理、硬件、重复次数和成本口径说全。
- 人工或模型 judge：谁判什么、按什么判、核验多少。设置是为了让人判断比较是否成立，不是报设备清单。

通用要求；Metrics/Baselines 为推荐组织

We evaluate [unit] from [dataset version], using [split or selection rule].

我们从[数据版本]中按[划分或选择规则]评价[样本单位]。

**第 1 句：**先定义比较对象与分母，不根据结果更换统计范围。

Metrics. We evaluate [target properties]. 1) [Metric 1] measures [definition, unit, direction, and denominator]. 2) [Metric 2] measures [definition, unit, direction, and denominator].

指标。我们评价[目标属性]。1) [指标一]衡量[定义、单位、方向与分母]。2) [指标二]衡量[定义、单位、方向与分母]。

**第 2 句：**保持一个紧凑自然段，编号定义各指标；正式 LaTeX 中只用 textbf 加粗指标名，完整格式见下方模板。

We compute [per-unit statistic] and aggregate by [rule]. [Invalid-output policy].

先计算[单位统计量]，再按[规则]汇总；[无效输出处理规则]。

**第 3 句：**宏平均、微平均与条件子集不能混用。

Baselines. We compare [method] with [routes and citations] using [shared conditions].

基线。我们在[共享条件]下，将[方法]与[基线路线及引用]比较。

**第 4 句：**把可影响结果的条件说明白，不只报模型名字。

Implementation Details. We select [parameters] on [development data] and fix them before [final evaluation].

实现细节。我们在[开发数据]上选择[参数]，并在[最终评价]前固定这些选择。

**第 5 句：**明确选择边界；具体值与来源按真实记录填。

**完整 LaTeX 结构模板**

```latex
\noindent\textbf{Metrics.}
We evaluate [target properties] using [verified metrics and assessment units].
1) \textbf{[Metric 1]} measures [definition, unit, direction, and denominator].
2) \textbf{[Metric 2]} measures [definition, unit, direction, and denominator].
We aggregate [per-unit results] by [actual rule] and handle [invalid or not-applicable outputs] according to [actual protocol].
```

#### Main Results：先写发现

解释主要差异、可能原因及对应设计，不逐行重复表格数值。

教学模板；【】填真实材料。

- 把有依据的结论写在段首或小标题。一段优先围着一个实验、一个图表、一个结论讲，不混三件事。
- 先说明关键关系，再给决定判断的数字与范围；全面胜出、显著、稳定需要对应证据。
- 观察之后解释原因，消融才能帮助归因；有利、不利指标与代价都照实解释。

通用要求；加粗发现为 StarPaper 偏好

[Design] improves [specific ability] under [tested condition].

在[实测条件]下，[设计]改善了[具体能力]。

**第 1 句：**作为加粗结论；无提升就写真实差异或未支持的主张。

Table [ref] shows [qualitative contrast] relative to [comparison].

表[真实编号]显示，相比[对照]，[关键关系]。

**第 2 句：**只讲决定结论的对照，不逐行复述数字。

This contrast supports [Intro contribution], while [observed trade-off] limits [scope].

这一对照支持[引言贡献]，但[已观察代价]限制了[适用范围]。

**第 3 句：**解释结果意味着什么，同时保留真实取舍。

#### 消融实验：每个模块先 Setting，再 Results

每个模块各写设置与结果。先让读者知道两行差在哪，再解释这个差异说明什么。

填空模板；【】换成真实材料，不包含论文实测数字。

- Setting：目的、完整变体名称、删掉或替换的因素、保留的因素、会影响结果的共享条件。训练型模块按实际协议重新训练。
- Results：先给真实发现，再指向表中刚定义的两行，说明对应指标的变化、范围和必要代价。没有结果，不填写结论。
- 【铁律】多项同时变化，只能评价整套改动；条件性的增量作用不能冒称单独作用或交互效应。
- 所有变体在 Setting 和表中同名。同一变体不能在文中叫 No Reward，在表中却叫 Baseline 2。
- 先讲整体共同设置也可以；随后每个模块仍交代其独有改动，Results 紧接对应设置。

组织参考 EviNoteRAG §4.6；具体控制条件按实际实验填写。

**完整 LaTeX 结构模板**

```latex
\subsection{Ablation Study}
\label{sec:ablation}

\paragraph{Effect of [Module A].}
\textbf{Setting.}
To examine [Module A's role], we compare [control variant] with [Module A variant].
Both retain [shared modules] and use [matched training data, model, evaluation set, decoding settings, and budget].
Only [the specified factor] changes.
[Remaining differences and their location].

\textbf{Results.} \textbf{[Verified finding under these conditions].}
Table~\ref{tab:ablation} compares [the two rows] on [relevant metric and scope].
[Observed change and measured uncertainty].
This supports [the bounded component role].
[Observed exception or limitation].

\paragraph{Effect of [Module B].}
\textbf{Setting.}
We compare [variant retaining Module A] with [the same variant using Module B].
We keep [Module A and other shared conditions] fixed and change only [Module B or specified replacement].
[Actual retraining, repetitions, and settings location].

\textbf{Results.} \textbf{[Verified finding with Module A fixed].}
Table~\ref{tab:ablation} shows [actual difference] between [the matched rows].
This tests [Module B's incremental role in this configuration].
[Observed trade-off or exception].
```

#### 扩展实验：稳定性、效率、迁移

按主张选择稳健性、效率或迁移分析。保留失败记录，报告有助于判断贡献的负结果。

教学模板；【】填真实材料。

- 效率比较给端到端成本、资源和质量取舍；计入生成与审核。
- 每组先说为什么测、改什么、固定什么，再说发现和范围。
- 哪些条件有效、哪条路走不通，都是有信息的结果；不能只挑最好一次，或把失败全藏起来。

按贡献选择必要分析

To test [stability or transfer claim], we vary [factor] while holding [controls] fixed.

为检验[稳定或迁移主张]，我们改变[因素]，保持[控制项]不变。

**第 1 句：**问题与实际变化必须匹配。

We report [variation or outcome] across [repeat unit or new setting].

我们报告跨[重复单位或新设置]的[变化或结果]。

**第 2 句：**说清独立运行、样本和重复层级，不靠最好一次说明稳定。

These comparisons support [scope-limited finding], but do not establish [broader claim].

这些比较支持[有限范围的发现]，尚不能说明[更广主张]成立。

**第 3 句：**范围边界具体写；不是在每段末尾机械加免责声明。

#### Case Study：展示方法的运行过程

选一个能看懂核心设计的案例，沿输入、中间产物、输出走一遍。重点解释方法在哪里发挥作用，不重复报排行榜。

填空模板；不预填任何真实论文的输入、输出或实验结论。

- 先写选择理由：典型困难、失败边界或关键设计。不要只挑最好看的成功例子。
- 输入交代问题、可用证据和必要条件；关键步骤展示实际可核查产物，如证据笔记、检索片段或约束标记。
- 输出紧接中间产物，指出哪条证据支持或否定哪个判断。有对照时先交代共同与不同条件，再并排比较。
- 【铁律】实测材料保留原始输入、输出与标签；构造案例明示。没有记录的中间步骤不编造，隐藏推理不能改画成已观察过程。
- 【铁律】个例说明方法运行或具体失败，不能替代所声称效果需要的实验、证明整体有效或推断总体比例。
- 时间紧时，可优先整理已有真实案例并深入分析，补充方法说明；主要结论仍需对应验证。分析充分的 Case Study 能让读者看清设计的价值。
- 【铁律】同一案例在论文中完整展示一次；其他章节交叉引用，避免换图、换语言后重复讲同一个故事。
- 图的颜色按语义分组，图形和纹理提供第二种区分。局部圈出关键证据并编号，旁注解释这一步如何改变输出；保留白底，不整块涂色。

组织参考 EviNoteRAG §4.8 / Figure 4（PDF 第 8 页）；案例与统计作用不同。

**完整 LaTeX 结构模板**

```latex
\subsection{Case Study}
\label{sec:case-study}
\textbf{[Concrete behavior illustrated by this case].}
We select [recorded case or explicitly constructed example] because [selection reason tied to an Introduction challenge].
Figure~\ref{fig:case-study} shows [the actual question and relevant evidence], which requires [specific behavior].
[Named method stage] transforms [input] into [recorded intermediate artifact].
In this artifact, [concrete marked evidence or retained uncertainty] supports [the next operation].
The final output [meets or violates the requirement] based on [verifiable evidence].
[Comparable baseline output, if available, and the exact contrast].
This case illustrates [the observed operation or failure], while [the quantitative evaluation or the untested boundary] determines the broader claim.
```

#### 结果表：名称、对照、口径对应

先定行列再填结果。表头按“数据集—指标”分两级，表体每行就是 Setting 定义的一种变体。

可复制 LaTeX 表格模板；需 booktabs 与 multirow。

- 【铁律】完整名称、引用、数值与误差在同一单元格内保持单行。优先调整列宽，必要时用通栏表，不用缩写、折行或整体缩放掩盖拥挤。
- 共同的数据集、指标、方向、单位与精度固定。读者应能横向查同一变体，纵向比同一指标。
- 路线很多时用分组行；消融表则将完整方法与匹配变体邻近摆放。表内变体名与 Setting 一致。
- 【铁律】均值与不确定性必须基于真实观测和明确方法；说明统计或重采样单位、实际数量及 SD、SE 或 CI。单次运行不能冒称跨运行稳定性，不套用示例论文的重复次数。
- 最优与次优只在可比组内逐列标记，按指标方向判断，并列共用标记。不能给整行自动加粗或声称每列都胜出。
- Caption 写范围、单位、汇总、误差含义和标记规则；未测量写未测量，N/A 说明不适用原因，二者不能填零。
- 最终 PDF 核查最长名称、误差上标、两级表头、列距和页边距。booktabs、multirow 在导言区加载；模板占位值逐格替换。

组织参考 EviNoteRAG Table 1（PDF 第 6 页）与 Table 2（第 7 页）；单行要求来自最新绘图 skill。

**完整 LaTeX 结构模板**

```latex
\begin{table*}[!t]
\centering
\caption{Ablation results on [evaluation scope and split].
Scores use [unit and aggregation rule]; arrows show the preferred direction.
[Single-run results, or actual repeat count and defined uncertainty type].
Bold marks the best and underline the second-best distinct value among comparable variants; ties share the same mark.}
\label{tab:ablation}
\begin{tabular*}{\textwidth}{@{\extracolsep{\fill}} l cccc @{}}
\toprule
\multirow{2}{*}{Variant} & \multicolumn{2}{c}{[Dataset A]} & \multicolumn{2}{c}{[Dataset B]} \\
\cmidrule(lr){2-3}\cmidrule(lr){4-5}
 & EM $\uparrow$ & F1 $\uparrow$ & EM $\uparrow$ & F1 $\uparrow$ \\
\midrule
{[Control variant full name]} & [value] & [value] & [value] & [value] \\
{[Module A variant full name]} & [value] & [value] & [value] & [value] \\
{[Module B variant full name]} & [value] & [value] & [value] & [value] \\
\bottomrule
\end{tabular*}
\end{table*}
```

---

Da1yuqin / [StarPaper](https://da1yuqin.github.io/StarPaper/)，[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)。转载保留署名、出处与许可，改编注明改动。
