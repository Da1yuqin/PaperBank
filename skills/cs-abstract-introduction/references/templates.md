# 摘要、引言与贡献：按需参考

以下为通用规则与教学模板，不是真实论文原文、研究事实或实测。

<a id="annotated-abstract"></a>

#### 摘要模板

一个自然段写完问题、解法与实验亮点。

**English 填空模板**

[Research task] requires [capability needed in practice]. Existing methods in [research line] face ***[limitation A]*** and ***[limitation B]***, which hinder [specific goal]. We introduce [Method], a [concrete artifact and its purpose]. For [same limitation A], we [design A and its function]. For [same limitation B], we [design B and its function]. Experiments on [evaluation scope] show that [verified quantitative result with its metric, unit, and comparison reference]. Further analysis reveals [key experimental finding], showing [what this finding answers about the research question].


**高亮与旁批**

1. **[Research task] requires [capability needed in practice].**：背景：任务与能力。交代具体任务与能力需求。为下句的局限提供比较标准。
2. **Existing methods in [research line] face [limitation A] and [limitation B], which hinder [specific goal].**：局限：具体障碍。A、B 填具体障碍。关键词用粗斜体。按实际问题增删，不凑数量。
3. **We introduce [Method], a [concrete artifact and its purpose].**：贡献：对象与用途。先写提出什么、用于什么。下句再展开设计。
4. **For [same limitation A], we [design A and its function]. For [same limitation B], we [design B and its function].**：解法：回应局限。两个 For 分别接回 A、B。后半句填对应设计与作用。
5. **Experiments on [evaluation scope] show that [verified quantitative result with its metric, unit, and comparison reference].**：实验：数字与对照。填最能支持贡献的实测数字。方法型可写相对基线的提升。评价型可写占比或得分差距。标明范围、指标与单位。
6. **Further analysis reveals [key experimental finding], showing [what this finding answers about the research question].**：结论：发现与意义。填关键发现及其意义。如适用条件、解决的困难。发现型可先讲发现，再给数字。

<a id="annotated-intro"></a>

#### 领域与任务模板

从领域价值写到具体任务与能力需求。

**English 填空模板**

[Research area] supports [concrete application or research goal]. In [target scenario], [the system or researcher] must [specific task] using [available inputs]. Successful [task] requires [capability A] and [capability B], motivating research on [the problem studied here].


**高亮与旁批**

1. **[Research area] supports [concrete application or research goal].**：领域价值。填具体应用或研究用途。说明为何研究这个方向。
2. **In [target scenario], [the system or researcher] must [specific task] using [available inputs].**：落到研究任务。填场景、执行者、动作与输入。将背景收束到本文任务。
3. **Successful [task] requires [capability A] and [capability B], motivating research on [the problem studied here].**：建立判断标准。填任务必需的能力。下段据此比较已有工作。

<a id="annotated-intro-comparison"></a>

#### 已有工作与问题模板

先归类已有能力，再引出本文问题。

**English 填空模板**

To support [the task introduced above], methods in [family A] use [shared mechanism] to achieve [established capability] [supporting citations]. Methods in [family B] address [another relevant need] through [shared mechanism] [supporting citations]. However, these advances have not established [the capability required in the target condition], leaving [the specific research gap].


**高亮与旁批**

1. **To support [the task introduced above], methods in [family A] use [shared mechanism] to achieve [established capability] [supporting citations].**：已有路线 A。接回上段任务。按机制归类，并给能力与引用。
2. **Methods in [family B] address [another relevant need] through [shared mechanism] [supporting citations].**：已有路线 B。补充另一类思路及其能力。类别数量由文献决定。
3. **However, these advances have not established [the capability required in the target condition], leaving [the specific research gap].**：从能力引出不足。针对上述能力指出不足。下段解释具体成因与后果。

<a id="annotated-intro-obstacles"></a>

#### 局限与研究必要性模板

写清各项局限的成因及实际妨碍。

**English 填空模板**

Achieving [the established research goal] remains difficult for two reasons. First, ***[limitation A]*** arises because [specific cause or missing capability]. This prevents [the concrete operation or evaluation needed for the goal]. Second, ***[limitation B]*** occurs when [relevant condition], making [another required operation] difficult. Together, these limitations prevent [the precise objective this paper will address].


**高亮与旁批**

1. **Achieving [the established research goal] remains difficult for two reasons.**：段首钩子。接回上一段目标，再解释困难。问题数量按实际调整。
2. **First, [limitation A] arises because [specific cause or missing capability]. This prevents [the concrete operation or evaluation needed for the goal].**：局限 A：成因与后果。先命名困难，再写成因与后果。不能只给属性标签。
3. **Second, [limitation B] occurs when [relevant condition], making [another required operation] difficult.**：局限 B：独立问题。填另一独立问题。写清发生条件及受阻任务。
4. **Together, these limitations prevent [the precise objective this paper will address].**：承上启下。说明局限如何阻碍研究目标。为下一段设计作铺垫。

<a id="annotated-intro-design"></a>

#### 设计与贡献总述模板

先报产物，再逐项解释设计如何解决局限。

**English 填空模板**

To address these limitations, we introduce *[Method]*, a [concrete artifact with its core design and purpose]. For [same limitation A], we [design A], which [verb phrase explaining how A resolves the limitation]. For [same limitation B], we [design B], allowing [the required operation]. [Key contribution object] is constructed from [verified source or selection rule] to [specific use]. Together, these designs enable [the task established in the preceding paragraph].


**高亮与旁批**

1. **To address these limitations, we introduce [Method], a [concrete artifact with its core design and purpose].**：承接问题，点明贡献。开头接回上一段 A、B。方法名后立即写产物与用途。
2. **For [same limitation A], we [design A], which [verb phrase explaining how A resolves the limitation].**：A 对应设计 A。复用 A 的名称，写解法与作用。实现细节留到 Method。
3. **For [same limitation B], we [design B], allowing [the required operation].**：B 对应设计 B。复用 B 的名称，写对应解法。与上一项设计区分清楚。
4. **[Key contribution object] is constructed from [verified source or selection rule] to [specific use].**：关键产物先出现。先写关键产物。再交代来源、筛选依据与用途。
5. **Together, these designs enable [the task established in the preceding paragraph].**：收束到目标。回到上一段研究目标。说明各设计如何共同完成它。

<a id="annotated-intro-findings"></a>

#### 实验发现模板

先概述发现，再给数字与分析，回答研究问题。

**English 填空模板**

To answer [the research question introduced above], we evaluate [Method or evaluated systems] on [datasets or tasks] against [comparison scope]. The experiments reveal [one-sentence overview of the main finding]. Specifically, [verified quantitative result with its comparator and unit]. Further analysis shows [which design or condition is associated with the observed outcome], supporting [the corresponding motivation or claim].


**高亮与旁批**

1. **To answer [the research question introduced above], we evaluate [Method or evaluated systems] on [datasets or tasks] against [comparison scope].**：实验钩子与范围。先接研究问题。再交代评什么、在哪评、和谁比。
2. **The experiments reveal [one-sentence overview of the main finding].**：先给发现总览。用一句话概括核心发现。后面的数字与分析支撑它。
3. **Specifically, [verified quantitative result with its comparator and unit].**：再给亮眼数字。填支持总览的关键结果。写清对照、单位与范围。
4. **Further analysis shows [which design or condition is associated with the observed outcome], supporting [the corresponding motivation or claim].**：最后解释发现。回扣研究动机，解释设计价值。只概述正文已有分析。

<a id="template-intro-contributions"></a>
<a id="draft-contribution-format"></a>
#### 贡献列表模板

用 3 条收束引言：整体工作、关键设计或证据、实验发现。第 2 条按类型选 propose 或 provide。正式方法名用 textit，普通描述不斜体。

- 先用连贯段落说明核心工作、对应设计与实验发现。方法名后的同位语立即点明亮点与用途。不要先堆流程，再讲贡献。
- 【铁律】正文引导句后接原生 itemize，固定三项。依次写整体工作、设计或证据贡献、实验发现。列表后直接进入下一节。
- 方法论文第 2 项写新机制与用途。基准论文写构建或评价设计。实证研究写比较、测量或分析贡献。只写已完成的工作。
- 三项贡献是本套 CS 约定，不是所有会议的规定。论文类型与当轮要求优先。先删重复背景与次要流程，不改模板规避页数。
- 只填真实贡献，不虚构机制或诊断。已讲清的问题与解法无需重复局限标签。

```latex
Our contributions are summarized as follows:
\begin{itemize}
  \item We introduce [work and its type], which [supports the target task through its core contribution].
  \item We [propose or provide] [key design or evidence contribution] based on [verified basis], enabling [specific function or comparison].
  \item Our evaluation on [scope] reveals [key finding], with [the most informative verified evidence].
\end{itemize}
```

<a id="intro-writing-templates"></a>
#### 引言写作模板

按主要贡献选一套，不拼接四套。前两段可合并或交错。贡献固定三项：整体工作、设计或证据、实验发现。

<a id="intro-template-method"></a>
<details><summary>方法型引言</summary>

核心贡献是新方法或新的系统设计。

**领域与研究问题**

[research area] aims to [goal] by mapping [input] to [output]. Recent [approach family] can [supported capability] [citations]. These capabilities support [application], where [task requirement] matters for [practical objective]. This requirement motivates [research question].

先写研究对象、已有能力与任务要求，再引出问题。背景与文献回顾可穿插。

**比较依据与局限**

Existing [approach family A] uses [input A] to [supported operation A] [citations], whereas [approach family B] relies on [input B] to [supported operation B] [citations]. However, [specific limitation] restricts [required capability] because [documented cause or operating assumption]. Under [relevant condition], this restriction leads to [observable consequence]. Addressing it requires [corresponding design requirement].

按同一维度比较，用 However 点出局限及其后果。下一段紧接解法。

**对应设计与贡献**

To address these limitations, we propose \textit{[method name]}, a [verified distinguishing design and purpose]. For [specific limitation], we [concrete design action and contribution] to meet [corresponding design requirement]. It takes [input] and produces [output] through [high-level mechanism]. For [another established limitation, if present], we [next design action] using [preceding output] to [corresponding purpose]. Together, these designs enable [supported capability] under [stated conditions].

【铁律】方法名后立即写亮点与用途。钩子复用前文局限，紧接对应动作。设计及正面修饰须能从来源、操作或结果核查。

**实验概述与结论边界**

To answer [research question], we compare \textit{[method name]} with [appropriate baselines] under [shared evaluation conditions]. Experiments show [verified main finding] on [metric or measured outcome] within [tested scope]. To examine [design motivation], [ablation or controlled comparison] tests [specific design choice] and shows [verified design finding]. Further analysis identifies [supported pattern or remaining limitation], indicating [bounded answer to the original question].

先概述发现，再展开设计检验与分析。各章发现与范围一致，不预填最优或显著提升。

**贡献总结**

```latex
In summary, our contributions are:
\begin{itemize}
    \item We introduce \textit{[method name]}, which [performs the target task through the core components].
    \item We propose \textit{[new mechanism]} based on [verified basis], enabling [specific function] and [actual application].
    \item Evaluation on [tested scope] reveals [key experimental finding], supported by [the most informative verified comparison].
\end{itemize}
```

依次写方法、关键机制与实验证据。第 2 项点名设计及用途，无需复述流程。

</details>

<a id="intro-template-benchmark"></a>
<details><summary>基准与数据集型引言</summary>

核心贡献是新的数据集、基准或评价协议。

**能力与评价问题**

Progress in [research area] enables [supported capability] [citations]. These capabilities support [application], where [condition relevant to the task] affects [required behavior]. Evaluating this behavior requires [observable input or evaluation property]. This requirement raises [research question].

先说明为何评价该能力。问题落到可观察的输入、行为或结果。

**已有基准与评价缺口**

Existing [benchmark family A] measures [evaluation target A] using [reported inputs and criteria] [citations]. [benchmark family B] instead evaluates [evaluation target B] under [reported setting] [citations]. However, [specific evaluation limitation] limits evaluation of [specific required capability], as shown by [evidence-bounded comparison]. [required input or criterion] is needed to distinguish [behavior of interest] from [alternative behavior], so [corresponding evaluation design] is necessary.

按输入、判据与目标比较，区分缺失、未报告和未公开。说明缺口导致哪种行为无法区分。

**建设障碍与设计要求**

However, establishing [required evaluation] faces [self-explanatory construction obstacle]. [documented source or annotation constraint] makes [required construction step] difficult. In addition, [another independent obstacle, if present] limits [another necessary step] because [documented reason]. Addressing these obstacles is necessary to obtain [usable evaluation artifact] for [research question].

建设困难与已有评价缺口分开写。逐项写受阻步骤及后果，无独立第二项则删去。必要时与前段合并。

**数据、判据与核心贡献**

To address these limitations, we propose \textit{[benchmark or dataset name]}, a [verified source or distinguishing design] for [evaluation purpose]. For [data construction obstacle], we construct [data contribution] from [verified source] using [documented selection or collection rule]. For [specific evaluation limitation], we [evaluation contribution and action] to measure [capability linked to the earlier gap]. The tested system receives [task input], while [evaluation evidence or criteria] is used by [evaluator] to assess [system output]. These components support [supported evaluation capability] within [coverage boundary].

【铁律】先报产物，再写来源与构建依据。钩子复用评价局限，数据与判据各回应对应困难。受测输入与评分材料分开。

**基准结果与研究发现**

To answer [research question], we evaluate [systems or model families] using [shared protocol]. Results reveal [verified main finding] within [tested scope]. Specifically, [named finding, if useful] describes [observed behavior or result contrast]. To examine [observed limitation], [diagnostic analysis] shows [supported diagnostic finding]. These results indicate [bounded implication] and leave [remaining question] unresolved.

先给发现，再解释命名现象的含义。诊断回答原问题，不扩大为未验证的机制。

**贡献总结**

```latex
In summary, our contributions are:
\begin{itemize}
    \item We introduce \textit{[benchmark or dataset name]}, which supports [evaluation task] with [verified coverage and core components].
    \item We propose [construction or evaluation design] based on [verified source or principle] to [address the specific evaluation difficulty].
    \item Evaluation of [systems or model families] under [shared protocol] reveals [key quantitative finding and its scope].
\end{itemize}
```

依次写基准或数据集、构建或评价设计、测评发现。规模不等于全部贡献。

</details>

<a id="intro-template-diagnostic"></a>
<details><summary>诊断驱动的改进研究引言</summary>

先诊断瓶颈，再提出改进。正文依次写 Diagnostic Analysis、Method 与验证。

**已有能力判断与可检验问题**

[research area] seeks to [goal]. Existing [approach family] achieves [supported result] under [reported conditions] [citations]. However, it remains unclear whether this result demonstrates [target capability]. If the capability holds, [testable expectation] should be satisfied under [controlled condition].

区分已有成绩与被宣称的能力。用 However 提出可检验质疑，不硬套段数。

**诊断设计与关键发现**

To test this expectation, we construct [diagnostic comparison] by changing [target condition] while preserving [relevant controls]. The comparison reveals [verified diagnostic finding]. Further [discriminating control or process analysis] shows [supported bottleneck evidence], suggesting that [bounded interpretation]. These observations motivate [design requirement].

先写诊断，再写方法。交代改变与保留条件，由发现定位有据瓶颈。

**针对瓶颈的设计**

To address these limitations, we propose \textit{[method name]}, a [distinguishing design and purpose]. For [diagnosed bottleneck], we [concrete design action] to [corresponding role]. For [another established bottleneck, if present], we [next design action] using [preceding output] to [corresponding role]. [training or execution procedure] combines these components to produce [output].

动作靠前，每项设计回应诊断。无独立第二项则删去；训练或推理按实际写。

**回到诊断的改进验证**

To answer [original capability question], we evaluate \textit{[method name]} on [main task] and repeat [original diagnostic comparison]. Results show [verified main finding] and [verified finding under diagnostic conditions]. Further [process analysis or controlled ablation] examines [design motivation] and yields [verified result]. Together, these tests support [bounded conclusion] within [tested scope].

先概述发现，再给主任务、诊断复测及过程检验证据。各项回答最初的能力质疑。

**贡献总结**

```latex
In summary, our contributions are:
\begin{itemize}
    \item We investigate [target capability] through [diagnostic study], identifying [evidence-supported bottleneck] under [tested conditions].
    \item We propose \textit{[method name]} with [core design] to address [the diagnosed bottleneck].
    \item Evaluation on [main-task scope] and [diagnostic comparison] shows [the verified improvement or trade-off], answering [the original capability question].
\end{itemize}
```

依次写诊断认识、针对瓶颈的设计、主任务与诊断复测结果。

</details>

<a id="intro-template-empirical"></a>
<details><summary>实证发现型引言</summary>

核心贡献是新的经验规律、系统比较或对既有解释的检验。

**现象与研究问题**

Understanding [research phenomenon] matters for [scientific or practical objective]. Prior [research route] establishes [supported finding] within [previously studied scope] [citations]. This evidence motivates [specific question about the phenomenon]. Answering this question requires distinguishing [competing possibilities] under [relevant condition].

分清已知事实与未答问题，点明需要区分什么。可与文献回顾合并。

**已有证据与检验缺口**

Existing studies examine [relationship or behavior] using [reported design] [citations]. They provide evidence for [supported interpretation] under [documented assumptions or scope]. However, [specific evidence limitation] prevents these results from resolving [research question]. A comparison that [required contrast or measurement] is needed to distinguish [explanation A] from [explanation B].

点出证据缺口，紧接检验要求。未测试不等于失败，相关不等于因果。

**研究设计与可检验贡献**

To address these limitations, we propose [study or analysis], a [verified distinguishing design] for testing [research question]. For [specific evidence limitation], we [core comparison or measurement]. We compare [groups or conditions] that differ in [examined factor], using [documented control or adjustment] to examine [alternative explanation]. [measurement or analysis contribution] measures [observable outcome] using [verified data or procedure]. This design estimates [precise quantity or relationship] within [study population and conditions].

【铁律】钩子点名证据缺口，贡献落到比较或测量。受控实验写改变因素。观察研究写自然差异、调整及估计对象。调整不等于排除全部解释。

**主要发现与解释范围**

To answer [research question], we analyze [evidence] under [reported study conditions]. The results show [verified main relationship or contrast]. Further [robustness check or independent analysis] examines [specific alternative explanation] and yields [verified result]. These findings support [evidence-bounded interpretation] within [tested scope], while [unresolved limitation] restricts [claim or generalization].

先陈述发现，再说排除及未排除的解释。主结果与稳健性各有对象，回答同一问题。

**贡献总结**

```latex
In summary, our contributions are:
\begin{itemize}
    \item We present a systematic study of [research question] using [data and study design].
    \item We provide [controlled comparisons, measurements, or an analysis protocol] that distinguish [the competing possibilities examined in this study].
    \item Our analysis reveals [key empirical finding] within [studied scope], supported by [the most informative verified contrast or robustness result].
\end{itemize}
```

依次写问题与范围、比较或测量证据、经验发现。没有新机制则不声称提出新机制。

</details>

---

Da1yuqin / [StarPaper](https://da1yuqin.github.io/StarPaper/)，[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)。转载保留署名、出处与许可，改编注明改动。
