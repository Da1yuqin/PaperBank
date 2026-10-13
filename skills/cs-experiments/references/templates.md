# 实验、评价与诊断：按需参考

以下为通用规则与教学模板，不是真实论文原文、研究事实或实测。

<a id="annotated-experiments-overview"></a>

#### 实验概述

承接方法输出，先概述发现，再交代接下来如何检验贡献。

**English 填空模板**

After constructing [method, dataset, or benchmark], we evaluate [target systems or behaviors] on [evaluation scope]. The results show [verified main finding that answers the Introduction question]. Specifically, we compare [method or systems] with [comparison group] to examine [primary claim]. We then analyze [component role or remaining question] through [actual ablation, diagnosis, or further test].


**高亮与旁批**

1. **After constructing [method, dataset, or benchmark]**：接回前章产物。开头承接已经介绍的方法或数据，让读者知道下面测试什么。
2. **The results show [verified main finding that answers the Introduction question].**：先概述主发现。填实验最重要的结论，与摘要和引言保持一致；不从模型名单起笔。
3. **to examine [primary claim]**：主实验回答核心主张。每项主要贡献都要能在后文找到对应证据；RQ 可以显式编号，也可以直接写进句子。
4. **through [actual ablation, diagnosis, or further test]**：预告后续分析。只预告实际存在的分析；诊断、消融、效率实验分别回答不同问题。

<a id="annotated-experiments-datasets"></a>

#### 数据与划分

这一段定义实验总体、样本单位与数据使用边界。

**English 填空模板**

**Datasets.** We evaluate on [dataset names, versions, and citations], which contain [sample unit and task-relevant coverage]. We use [training, development, and test split or official evaluation protocol]. [Parameters or model choices] are selected using [development data], while [test split] is reserved for final evaluation. [Inclusion rules and resulting sample counts] define the evaluated population. [Additional preprocessing details] are provided in Appendix [data].


**高亮与旁批**

1. **[dataset names, versions, and citations]**：标识数据版本。名称、版本与引用放在一起，避免同名数据的不同划分混用。
2. **[sample unit and task-relevant coverage]**：说明一条样本是什么。交代输入、标签或场景覆盖中影响评价的部分，详细统计可放数据章节或附录。
3. **[training, development, and test split or official evaluation protocol]**：交代真实划分。按真实方案填写；纯推理评价可写官方测试集，没有调参就删去开发集选参句，不虚构训练集或开发集。
4. **[Inclusion rules and resulting sample counts] define the evaluated population**：固定统计范围。说明纳入规则和有效数量；排除、不适用与无效输出按真实协议分别处理。

<a id="annotated-experiments-baselines"></a>

#### 比较方法

这一段说明与谁比较、为什么选它们，以及比较条件。

**English 填空模板**

**Baselines.** We compare [our method] with [baseline family A and citations], which [shared mechanism], and [baseline family B and citations], which [different relevant mechanism]. These baselines cover [comparison dimensions related to our contribution]. All methods use [matched data, model access, resources, or evaluation conditions]. [Unmatched conditions that may affect interpretation] are reported in [settings location].


**高亮与旁批**

1. **[baseline family A and citations], which [shared mechanism]**：按路线介绍比较对象。先归类，再用一句话说明机制；版本与引用紧跟名称，不在设置里提前评价输赢。
2. **[comparison dimensions related to our contribution]**：说明选择依据。覆盖与贡献有关的常用路线、强对照或最近工作；不是随意列几个弱基线。
3. **[matched data, model access, resources, or evaluation conditions]**：说清比较条件。只写实际控制的条件；不能把预算上限相同说成信息量完全相同。
4. **[Unmatched conditions that may affect interpretation]**：保留影响判断的差异。使用公开报告值、闭源模型或不同硬件时说明来源及限制。

<a id="annotated-experiments-implementation"></a>

#### 实现细节

把会改变结果的设置集中在这里，避免散在结果分析中。

**English 填空模板**

**Implementation Details.** We implement [method] with [backbone or dependency versions]. [Key parameters introduced in Method] are set to [actual values] using [selection procedure and data]. Evaluation uses [execution configuration, hardware, and resource budget relevant to the comparison]. We conduct [actual repeats] over [repeat unit] and report [aggregation and uncertainty definition]. [Evaluator identity, configuration, and assessment protocol, if applicable] are specified in [protocol location].


**高亮与旁批**

1. **[backbone or dependency versions]**：固定执行版本。写真实使用的模型、软件版本或代码版本，读者应能定位同一实现。
2. **[actual values] using [selection procedure and data]**：补全方法参数。Method 解释参数作用，这里给实际取值、搜索范围与选择依据；一次性固定值也如实说明。
3. **[execution configuration, hardware, and resource budget relevant to the comparison]**：写影响结果的条件。训练、推理、检索、解码和成本只保留与本研究有关的设置，完整配置可放附录。
4. **[actual repeats] over [repeat unit] and report [aggregation and uncertainty definition]**：定义重复与误差。写实际运行次数及重复单位，并注明统计或重采样方法。单次运行可以报告样本统计，但不能声称跨运行稳定性；不把样本量当作运行次数。
5. **[Evaluator identity, configuration, and assessment protocol, if applicable]**：单独交代评价器。有人工或模型判分时说明谁判什么、依据什么及如何核验。没有 judge 就删去该句。

<a id="annotated-experiments-metrics"></a>

#### 指标定义

保持一个紧凑自然段：总述评价目标，再编号定义各指标。

**English 填空模板**

**Metrics.** We assess [target properties linked to the task] on [evaluation units and scope]. 1) **[Metric 1 full name (abbreviation)]** measures [definition, unit, direction, and denominator]. 2) **[Metric 2 full name (abbreviation)]** measures [definition, unit, direction, and denominator]. 3) **[Metric 3 full name (abbreviation)]** measures [definition, unit, direction, and denominator]. We compute [per-unit quantities] and aggregate them using [macro, micro, weighted, or other actual rule]. [Invalid, missing, and not-applicable outputs] are handled according to [defined policy], with [applicable counts or coverage] reported in [location].


**高亮与旁批**

1. **We assess [target properties linked to the task] on [evaluation units and scope].**：先说明衡量什么。指标对应任务目标或方法贡献，评价单位与范围紧接其后。
2. **1) [Metric 1 full name (abbreviation)] measures [definition, unit, direction, and denominator].**：编号、加粗名称、简短定义。首次出现给全称和缩写，指标名只加粗，不斜体。按真实指标数量增删，不能为凑三项编造指标。
3. **We compute [per-unit quantities] and aggregate them using [macro, micro, weighted, or other actual rule].**：说明如何汇总。写清先按什么单位计算，再怎样取平均；自定义指标的公式与判定细节给附录入口。
4. **[Invalid, missing, and not-applicable outputs] are handled according to [defined policy]**：交代异常处理。失败、缺失和不适用是不同情况，按实际协议处理并报告适用覆盖，不静默删样本。

<a id="annotated-experiments-main-teaching"></a>

#### 主要结果

每个结果段先给一项发现，再给关键数字，最后解释它回答了什么。

**English 填空模板**

**[Main finding under the tested conditions].** Table [main results] shows that [method] achieves [verified value and unit] on [metric], compared with [baseline value] for [named baseline]. This corresponds to [verified difference with its unit and measured uncertainty, if available] across [actual evaluation scope]. The comparison supports [the Introduction claim answered by this result]. [A relevant exception or measured trade-off, if observed].


**高亮与旁批**

1. **[Main finding under the tested conditions].**：段首先给结论。用加粗的一句话说清主要关系；填真实发现，不预设所有指标都提升。
2. **[verified value and unit] on [metric], compared with [baseline value] for [named baseline]**：挑有解释力的数字。给出决定结论的成绩与比较对象，避免逐行复述整张表。
3. **[verified difference with its unit and measured uncertainty, if available]**：把差值写准确。百分比与百分点分开；显著、稳定等词需要对应统计证据。
4. **The comparison supports [the Introduction claim answered by this result].**：回扣动机与贡献。说明这组结果回答了前文哪个问题。整套方法的优势不能直接拆成各模块的作用。
5. **[A relevant exception or measured trade-off, if observed].**：补充影响结论的取舍。有重要代价或不成立的条件就写清；没有相关证据时删去，不机械加免责声明。

<a id="experiments-experiment-ablation-table-template-writing-templates"></a>

<a id="experiment-ablation-table-template"></a>
#### 结果表：变体、指标与标记

先定行列再填结果。表头按“数据集—指标”分两级，表体每行就是 Setting 定义的一种变体。

- 【铁律】完整名称、引用、数值与误差在同一单元格内保持单行。优先调整列宽，必要时用通栏表，不用缩写、折行或整体缩放掩盖拥挤。
- 共同的数据集、指标、方向、单位与精度固定。读者应能横向查同一变体，纵向比同一指标。
- 路线很多时用分组行；消融表则将完整方法与匹配变体邻近摆放。表内变体名与 Setting 一致。
- 【铁律】均值与不确定性必须基于真实观测和明确方法；说明统计或重采样单位、实际数量及 SD、SE 或 CI。单次运行不能冒称跨运行稳定性，不套用示例论文的重复次数。
- 最优与次优只在可比组内逐列标记，按指标方向判断，并列共用标记。不能给整行自动加粗或声称每列都胜出。
- Caption 写范围、单位、汇总、误差含义和标记规则；未测量写未测量，N/A 说明不适用原因，二者不能填零。
- 最终 PDF 核查最长名称、误差上标、两级表头、列距和页边距。booktabs、multirow 在导言区加载；模板占位值逐格替换。

**两级表头：数据集 → 指标**

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
 & [Metric 1] $\uparrow$ & [Metric 2] $\uparrow$ & [Metric 1] $\uparrow$ & [Metric 2] $\uparrow$ \\
\midrule
{[Control variant full name]} & [value] & [value] & [value] & [value] \\
{[Module A variant full name]} & [value] & [value] & [value] & [value] \\
{[Module B variant full name]} & [value] & [value] & [value] & [value] \\
\bottomrule
\end{tabular*}
\end{table*}
```

按指标方向修改箭头；主结果表将 Variant 换成 Method。导言区加载 booktabs、multirow，逐格填实测值，最优与次优只在可比列内标记。

<a id="ablation-evidence-structure"></a>

#### 消融：每个模块先设置，再分析结果

对每个模块重复这组 Setting、Results，分别检验对应设计的作用。

**English 填空模板**

**Setting.** To examine [the specific role of Module A], we compare [control variant full name] with [variant containing Module A]. The two variants differ only in [Module A or its specified replacement]. Both retain [other modules] and use [matched data, backbone, training or inference settings, and evaluation protocol]. [Required retraining and downstream changes caused by this intervention] are described in [settings location].

**Results.** **[Verified finding about Module A under these conditions].** Table [ablation] compares [the two variant rows] on [the metric tied to this module's purpose]. [Metric] changes from [control value] for [control variant] to [observed value] for [tested variant], with [measured uncertainty, if available]. This result supports [the module's role within this configuration]. [Relevant exception or trade-off, if observed].


**高亮与旁批**

1. **To examine [the specific role of Module A]**：先点明要检验的作用。目的与 Method 中这一模块的设计动机对应，读者先知道为什么做这组消融。
2. **[control variant full name] with [variant containing Module A]**：先定义表中的两行。变体名称在设置、表格与结果中完全一致；说明删去、替换或改变了什么。
3. **Both retain [other modules] and use [matched data, backbone, training or inference settings, and evaluation protocol].**：固定其余条件。控制其他会影响结果的条件，并说明干预造成的后续变化。若存在无法对齐的额外条件，列出差异、改掉 differ only，并收窄归因；训练型模块按实际协议重新训练。
4. **[Verified finding about Module A under these conditions].**：Results 开头回答这个问题。先写真实发现，再引出数字；提升、下降或无明确差异都按记录写。
5. **[the two variant rows] on [the metric tied to this module's purpose]**：结果回到刚定义的对照。只分析这两行及相关指标，不拿完整方法的总增益归因给当前模块。
6. **[the module's role within this configuration]**：解释模块作用与范围。有其他模块固定时，结论是该配置下的增量作用；不能自动写成单独作用或协同效应。

<a id="annotated-experiments-further-analysis"></a>

#### 补充分析

按贡献选择稳健性、效率、迁移或失败诊断；每组围绕一个明确问题。

**English 填空模板**

To investigate [question not answered by the main comparison], we [analysis action stated as a verb phrase] using [actual evidence and comparison conditions]. Figure [analysis] shows [verified pattern], with [key value or contrast] under [tested scope]. This finding explains [the aspect of the original research question supported by the analysis]. [Implication for the method or a remaining question].


**高亮与旁批**

1. **[question not answered by the main comparison]**：先说为什么还要分析。补充实验应增加信息：检验适用范围、定位失败、衡量成本或检查稳定性。
2. **[actual evidence and comparison conditions]**：写清改变与保留什么。参数分析、迁移和效率比较各自给实际条件。诊断比例就近说明对象、分母与范围。
3. **[verified pattern], with [key value or contrast] under [tested scope]**：围绕一个图给发现。先概括关系，再给有解释力的数字，不逐点读图。
4. **[the aspect of the original research question supported by the analysis]**：连接全文问题。解释这项发现怎样支持、修正或限制引言的主张；相关模式不自动成为因果解释。

<a id="annotated-experiments-case-study"></a>

#### 案例分析

用一个真实记录或明确标注的示例，展示方法在哪一步发挥作用。

**English 填空模板**

We select [case] because it contains [challenge tied to the Introduction]. Figure [case study] presents [input and available evidence]. In [method stage], [actual operation] produces [recorded intermediate artifact], where [marked evidence] determines [the next decision]. The final output [observed behavior], whereas [a comparable baseline, if available] [observed contrast]. This case illustrates [the specific operation or failure], consistent with [the relevant quantitative finding, if established].


**高亮与旁批**

1. **[challenge tied to the Introduction]**：先交代选例理由。选择典型困难、关键设计或失败边界，避免只挑最好看的成功例子。
2. **[input and available evidence]**：从真实输入开始。给理解案例所需的完整信息；涉及敏感数据时使用已获公开许可的版本。
3. **[recorded intermediate artifact], where [marked evidence] determines [the next decision]**：解释关键一步怎么起作用。展示可核查的中间产物，用局部高亮、编号和旁注指出证据与下一步的关系。
4. **[observed behavior], whereas [a comparable baseline, if available] [observed contrast]**：展示输出与具体差异。有公平对照就并排展示；没有对照就删去 whereas 分句，不编造模型输出。
5. **[the specific operation or failure]**：收束到这个案例的含义。案例解释方法运行，不能替代主要结论所需的验证。颜色按语义分组，并用图形或标记辅助区分。

---

Da1yuqin / [StarPaper](https://da1yuqin.github.io/StarPaper/)，[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)。转载保留署名、出处与许可，改编注明改动。
