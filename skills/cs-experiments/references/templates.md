# 实验、评价与诊断：按需参考

以下为通用规则与教学模板，不是真实论文原文、研究事实或实测。

<a id="annotated-experiments-overview"></a>

#### 实验概述

承接方法，概述发现，再预告验证与分析。

**English 填空模板**

After constructing [method, dataset, or benchmark], we evaluate [target systems or behaviors] on [evaluation scope]. The results show [verified main finding that answers the Introduction question]. Specifically, we compare [method or systems] with [comparison group] to examine [primary claim]. We then analyze [component role or remaining question] through [actual ablation, diagnosis, or further test].


**高亮与旁批**

1. **After constructing [method, dataset, or benchmark]**：接回前章产物。接回已介绍的方法或数据。点明受测对象。
2. **The results show [verified main finding that answers the Introduction question].**：先概述主发现。填最重要的实验发现。与摘要和引言一致。
3. **to examine [primary claim]**：主实验回答核心主张。说明各项贡献如何检验。RQ 可编号，也可直接写入句中。
4. **through [actual ablation, diagnosis, or further test]**：预告后续分析。填实际开展的后续分析。分别交代它们回答什么问题。

<a id="annotated-experiments-datasets"></a>

#### 数据与划分

定义实验总体、样本单位与数据范围。

**English 填空模板**

**Datasets.** We evaluate on [dataset names, versions, and citations], which contain [sample unit and task-relevant coverage]. We use [training, development, and test split or official evaluation protocol]. [Parameters or model choices] are selected using [development data], while [test split] is reserved for final evaluation. [Inclusion rules and resulting sample counts] define the evaluated population. [Additional preprocessing details] are provided in Appendix [data].


**高亮与旁批**

1. **[dataset names, versions, and citations]**：标识数据版本。名称、版本与引用放在一起。不得混用同名数据的不同划分。
2. **[sample unit and task-relevant coverage]**：说明一条样本是什么。填影响评价的输入、标签或场景。详细统计放数据节或附录。
3. **[training, development, and test split or official evaluation protocol]**：交代真实划分。填实际划分与用途。纯推理可用官方测试集。没有调参则删除选参句。
4. **[Inclusion rules and resulting sample counts] define the evaluated population**：固定统计范围。填纳入规则与有效数量。分别说明排除、不适用和无效输出。

<a id="annotated-experiments-baselines"></a>

#### 比较方法

交代比较对象、选择依据与比较条件。

**English 填空模板**

**Baselines.** We compare [our method] with [baseline family A and citations], which [shared mechanism], and [baseline family B and citations], which [different relevant mechanism]. These baselines cover [comparison dimensions related to our contribution]. All methods use [matched data, model access, resources, or evaluation conditions]. [Unmatched conditions that may affect interpretation] are reported in [settings location].


**高亮与旁批**

1. **[baseline family A and citations], which [shared mechanism]**：按路线介绍比较对象。按路线归类，再简述机制。版本与引用紧跟名称。
2. **[comparison dimensions related to our contribution]**：说明选择依据。选与贡献有关的常用或强对照。覆盖相关近期工作。
3. **[matched data, model access, resources, or evaluation conditions]**：说清比较条件。只写实际控制的条件。预算上限相同不等于信息量相同。
4. **[Unmatched conditions that may affect interpretation]**：保留影响判断的差异。标明公开报告值及其来源。闭源模型、异构硬件等差异须交代。

<a id="annotated-experiments-implementation"></a>

#### 实现细节

集中交代会影响结果的执行设置。

**English 填空模板**

**Implementation Details.** We implement [method] with [backbone or dependency versions]. [Key parameters introduced in Method] are set to [actual values] using [selection procedure and data]. Evaluation uses [execution configuration, hardware, and resource budget relevant to the comparison]. We conduct [actual repeats] over [repeat unit] and report [aggregation and uncertainty definition]. [Evaluator identity, configuration, and assessment protocol, if applicable] are specified in [protocol location].


**高亮与旁批**

1. **[backbone or dependency versions]**：固定执行版本。填实际模型、软件或代码版本。让读者能定位同一实现。
2. **[actual values] using [selection procedure and data]**：补全方法参数。填参数值、搜索范围与选择依据。一次固定的参数也须说明。
3. **[execution configuration, hardware, and resource budget relevant to the comparison]**：写影响结果的条件。填相关训练、推理、检索与解码设置。涉及成本比较时给成本口径。完整配置可放附录。
4. **[actual repeats] over [repeat unit] and report [aggregation and uncertainty definition]**：定义重复与误差。写运行次数、重复单位与统计方法。单次可报告样本统计。不能据此声称跨运行稳定。样本量不是运行次数。
5. **[Evaluator identity, configuration, and assessment protocol, if applicable]**：单独交代评价器。有判分时写谁判什么、依据什么。说明判分如何核验。无评价器则删去。

<a id="annotated-experiments-metrics"></a>

#### 指标定义

一个紧凑自然段：评价目标 → 编号定义各指标。

**English 填空模板**

**Metrics.** We assess [target properties linked to the task] on [evaluation units and scope]. 1) **[Metric 1 full name (abbreviation)]** measures [definition, unit, direction, and denominator]. 2) **[Metric 2 full name (abbreviation)]** measures [definition, unit, direction, and denominator]. 3) **[Metric 3 full name (abbreviation)]** measures [definition, unit, direction, and denominator]. We compute [per-unit quantities] and aggregate them using [macro, micro, weighted, or other actual rule]. [Invalid, missing, and not-applicable outputs] are handled according to [defined policy], with [applicable counts or coverage] reported in [location].


**高亮与旁批**

1. **We assess [target properties linked to the task] on [evaluation units and scope].**：先说明衡量什么。填指标衡量的任务或贡献。紧接评价单位与范围。
2. **1) [Metric 1 full name (abbreviation)] measures [definition, unit, direction, and denominator].**：编号与指标定义。首次给全称与缩写。名称只加粗，不斜体。指标数量按实际增删。
3. **We compute [per-unit quantities] and aggregate them using [macro, micro, weighted, or other actual rule].**：说明如何汇总。写先按什么单位计算。再写如何汇总。自定义公式与判据给附录入口。
4. **[Invalid, missing, and not-applicable outputs] are handled according to [defined policy]**：交代异常处理。区分失败、缺失与不适用。按协议处理，并报告覆盖范围。不得静默删样本。

<a id="annotated-experiments-main-teaching"></a>

#### 主要结果

每段依次写：发现、数字、解释、适用范围。

**English 填空模板**

**[Main finding under the tested conditions].** Table [main results] shows that [method] achieves [verified value and unit] on [metric], compared with [baseline value] for [named baseline]. This corresponds to [verified difference with its unit and measured uncertainty, if available] across [actual evaluation scope]. The comparison supports [the Introduction claim answered by this result]. [A relevant exception or measured trade-off, if observed].


**高亮与旁批**

1. **[Main finding under the tested conditions].**：段首先给结论。加粗一句具体发现。不预设所有指标均提升。
2. **[verified value and unit] on [metric], compared with [baseline value] for [named baseline]**：挑有解释力的数字。填决定结论的数值与对照。不要逐行复述表格。
3. **[verified difference with its unit and measured uncertainty, if available]**：把差值写准确。区分百分比与百分点。显著、稳定须有统计证据。
4. **The comparison supports [the Introduction claim answered by this result].**：回扣动机与贡献。回答前文对应的问题。整体优势不能拆作各模块作用。
5. **[A relevant exception or measured trade-off, if observed].**：补充影响结论的取舍。填重要代价或失效条件。没有相关证据则删去。

<a id="experiment-results-table"></a>
#### 主结果表：排版与 LaTeX 模板

排版示例，数值均为假设。上标为标准差，浅红标最优，浅蓝标次优。

| Method | Success (%) ↑ | Latency (ms) ↓ |
| --- | --- | --- |
| Baseline A | 70.0 ±2.0 | 120 ±4 |
| Baseline B | 73.0 ±1.0 | 130 ±4 |
| Proposed method | 76.0 ±1.0 | 125 ±3 |

**LaTeX 表格模板**

```latex
% Add these packages to the preamble if the venue permits them.
\usepackage{booktabs}
\usepackage[table]{xcolor}
\definecolor{bestcell}{HTML}{F2EBEA}
\definecolor{secondcell}{HTML}{EDF0F4}

% Insert this environment in the body.
\begin{table}[!t]
\centering
\caption{Illustrative values only. Success rate is in percent;
latency is in milliseconds. Superscripts illustrate standard deviations.
Best values are bold; second-best values are underlined.}
\label{tab:main-results}
\begin{tabular}{lcc}
\toprule
Method & Success ($\uparrow$) & Latency ($\downarrow$) \\
\midrule
Baseline A & 70.0\textsuperscript{\(\pm2.0\)}
 & \cellcolor{bestcell}\textbf{120}\textsuperscript{\(\pm4\)} \\
Baseline B & \cellcolor{secondcell}\underline{73.0}\textsuperscript{\(\pm1.0\)}
 & 130\textsuperscript{\(\pm4\)} \\
Proposed method & \cellcolor{bestcell}\textbf{76.0}\textsuperscript{\(\pm1.0\)}
 & \cellcolor{secondcell}\underline{125}\textsuperscript{\(\pm3\)} \\
\bottomrule
\end{tabular}
\end{table}
```

先确认会议允许使用这些包。包声明放导言区，table 环境放正文。正式表换成真实数据。表注写统计单位、重复次数、可比范围与主要发现。跨栏用 table*，不改模板栏宽。

<a id="experiments-experiment-ablation-table-template-writing-templates"></a>

<a id="experiment-ablation-table-template"></a>
#### 结果表：变体、指标与标记

先定行列，再填结果。表头分数据集与指标两级，每行对应一种已定义变体。

- 【铁律】单元格内名称、引用、数值及误差保持单行。先调列宽，必要时改通栏。不要靠缩写、折行或整体缩放掩盖拥挤。
- 固定数据集、指标、方向、单位与精度。横向查变体，纵向比指标。
- 多路线用分组行；消融将完整方法与变体相邻摆放。变体名与 Setting 一致。
- 【铁律】均值与不确定性基于真实观测和明确方法。说明统计或重采样单位、数量及 SD、SE 或 CI。单次运行不声称跨运行稳定，不照搬例题次数。
- 最优与次优按指标方向在可比组内逐列标记。并列共用标记，不自动加粗整行。
- Caption 说明范围、单位、汇总、误差及标记。未测量与 N/A 分开，后者说明不适用原因。二者均不能填零。
- 在 PDF 核对长名称、误差、表头、列距与页边距。导言区加载 booktabs、multirow，逐格替换占位值。

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

按指标方向改箭头；主结果将 Variant 改为 Method。逐格填实测值，标记可比列内最优与次优。

<a id="ablation-evidence-structure"></a>

#### 消融：设置与结果

每个模块先写 Setting，再写 Results。

**English 填空模板**

**Setting.** To examine [the specific role of Module A], we compare [control variant full name] with [variant containing Module A]. The two variants differ only in [Module A or its specified replacement]. Both retain [other modules] and use [matched data, backbone, training or inference settings, and evaluation protocol]. [Required retraining and downstream changes caused by this intervention] are described in [settings location].

**Results.** **[Verified finding about Module A under these conditions].** Table [ablation] compares [the two variant rows] on [the metric tied to this module's purpose]. [Metric] changes from [control value] for [control variant] to [observed value] for [tested variant], with [measured uncertainty, if available]. This result supports [the module's role within this configuration]. [Relevant exception or trade-off, if observed].


**高亮与旁批**

1. **To examine [the specific role of Module A]**：检验哪项作用。接回 Method 的设计动机。点明本组消融检验什么。
2. **[control variant full name] with [variant containing Module A]**：定义对照变体。写清变体删除或替换了什么。设置、表格与结果须同名。
3. **Both retain [other modules] and use [matched data, backbone, training or inference settings, and evaluation protocol].**：固定其余条件。固定其他条件，说明连带变化。存在额外差异时逐项列出。此时改掉 differ only，收窄归因。训练模块按协议重新训练。
4. **[Verified finding about Module A under these conditions].**：先回答实验问题。先写发现，再给数字。如实写提升、下降或无明确差异。
5. **[the two variant rows] on [the metric tied to this module's purpose]**：分析对应对照。只分析刚定义的对照与指标。不能归入完整方法的总增益。
6. **[the module's role within this configuration]**：解释作用范围。其他模块固定时，写条件增益。不能当作独立作用或协同效应。

<a id="annotated-experiments-further-analysis"></a>

#### 补充分析

按贡献选择分析，每组回答一个明确问题。

**English 填空模板**

To investigate [question not answered by the main comparison], we [analysis action stated as a verb phrase] using [actual evidence and comparison conditions]. Figure [analysis] shows [verified pattern], with [key value or contrast] under [tested scope]. This finding explains [the aspect of the original research question supported by the analysis]. [Implication for the method or a remaining question].


**高亮与旁批**

1. **[question not answered by the main comparison]**：先说为什么还要分析。填分析目的。可检验范围、失败、成本或稳定性。
2. **[actual evidence and comparison conditions]**：写清改变与保留什么。填改变因素与固定条件。诊断比例说明对象、分母与范围。
3. **[verified pattern], with [key value or contrast] under [tested scope]**：围绕一个图给发现。先概括关系，再给关键数字。不逐点复述图形。
4. **[the aspect of the original research question supported by the analysis]**：连接全文问题。说明发现如何支持或限制主张。相关模式不等于因果机制。

<a id="annotated-experiments-case-study"></a>

#### 案例分析

沿输入、中间产物与输出，说明方法如何起作用。

**English 填空模板**

We select [case] because it contains [challenge tied to the Introduction]. Figure [case study] presents [input and available evidence]. In [method stage], [actual operation] produces [recorded intermediate artifact], where [marked evidence] determines [the next decision]. The final output [observed behavior], whereas [a comparable baseline, if available] [observed contrast]. This case illustrates [the specific operation or failure], consistent with [the relevant quantitative finding, if established].


**高亮与旁批**

1. **[challenge tied to the Introduction]**：先交代选例理由。选典型困难、关键设计或失败案例。不要只选最好的成功例子。
2. **[input and available evidence]**：从真实输入开始。给理解案例必需的输入。敏感数据须已获公开许可。
3. **[recorded intermediate artifact], where [marked evidence] determines [the next decision]**：解释关键步骤。展示可核查的中间产物。用高亮、编号和旁注解释下一步。
4. **[observed behavior], whereas [a comparable baseline, if available] [observed contrast]**：输出与差异。公平对照可并排展示。没有对照则删 whereas 分句。不得编造输出。
5. **[the specific operation or failure]**：本例说明什么。解释本例，不替代主要验证。颜色按语义分组。再用形状或标记辅助区分。

---

Da1yuqin / [StarPaper](https://da1yuqin.github.io/StarPaper/)，[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)。转载保留署名、出处与许可，改编注明改动。
