# 摘要、引言与贡献：按需参考

以下为通用规则与教学模板，不是真实论文原文、研究事实或实测。

<a id="annotated-abstract"></a>

#### 摘要模板

用一个自然段概括问题、对应解法和实验亮点。

**English 填空模板**

[Research task] requires [capability needed in practice]. Existing methods in [research line] face ***[limitation A]*** and ***[limitation B]***, which hinder [specific goal]. We introduce [Method], a [concrete artifact and its purpose]. For [same limitation A], we [design A and its function]. For [same limitation B], we [design B and its function]. Experiments on [evaluation scope] show that [verified quantitative result with its metric, unit, and comparison reference]. Further analysis reveals [key experimental finding], showing [what this finding answers about the research question].


**高亮与旁批**

1. **[Research task] requires [capability needed in practice].**：背景：任务为什么需要研究。用一句话交代具体任务与能力需求，让下一句的不足有比较标准。
2. **Existing methods in [research line] face [limitation A] and [limitation B], which hinder [specific goal].**：局限：列出本文要解决的问题。A、B 分别填具体缺失或障碍，关键词用粗斜体。存在更多独立局限时可继续展开；不要为了模板凑数，也不要把多个局限合成一个空泛问题。
3. **We introduce [Method], a [concrete artifact and its purpose].**：贡献总述：对象与用途。先告诉读者提出了什么、用来做什么，再展开具体设计。
4. **For [same limitation A], we [design A and its function]. For [same limitation B], we [design B and its function].**：解法：逐项回应前述局限。两个 For 后分别沿用 A、B 的问题关键词，后半句填真实设计及作用。每个问题都应找到对应解法。
5. **Experiments on [evaluation scope] show that [verified quantitative result with its metric, unit, and comparison reference].**：实验亮点：数字与比较对象。选择最能支持主要贡献的实测数字。方法论文可填相对可比基线的提升，评价或发现型论文可填样本占比、得分差距等关键结果；范围、指标与单位必须明确。
6. **Further analysis reveals [key experimental finding], showing [what this finding answers about the research question].**：关键结论：实验让我们知道了什么。填重要发现及其意义，例如在哪种条件下有效、哪个设计解决了哪类困难。发现型论文可先讲核心发现，再给最有说服力的数字。

<a id="annotated-intro"></a>

#### 领域与任务模板

从领域价值收束到本文的具体任务与能力需求。

**English 填空模板**

[Research area] supports [concrete application or research goal]. In [target scenario], [the system or researcher] must [specific task] using [available inputs]. Successful [task] requires [capability A] and [capability B], motivating research on [the problem studied here].


**高亮与旁批**

1. **[Research area] supports [concrete application or research goal].**：领域价值。先写具体应用或研究用途，让读者知道为什么关心这个方向。
2. **In [target scenario], [the system or researcher] must [specific task] using [available inputs].**：落到研究任务。说明目标场景、任务执行者、具体动作与可用输入，把领域背景收束到本文对象。
3. **Successful [task] requires [capability A] and [capability B], motivating research on [the problem studied here].**：建立判断标准。说明任务需要哪些关键能力。下段回顾已有工作在这些方面做到了什么，再据此指出不足。

<a id="annotated-intro-comparison"></a>

#### 已有工作与问题模板

归类已有工作，承认能力，再引出本文的具体问题。

**English 填空模板**

To support [the task introduced above], methods in [family A] use [shared mechanism] to achieve [established capability] [supporting citations]. Methods in [family B] address [another relevant need] through [shared mechanism] [supporting citations]. However, these advances have not established [the capability required in the target condition], leaving [the specific research gap].


**高亮与旁批**

1. **To support [the task introduced above], methods in [family A] use [shared mechanism] to achieve [established capability] [supporting citations].**：已有路线 A。钩子接上段任务，按机制归类工作，交代已有能力并给对应引用。
2. **Methods in [family B] address [another relevant need] through [shared mechanism] [supporting citations].**：已有路线 B。补充另一类思路及其能力，按真实文献选择类别数量，不凑两类。
3. **However, these advances have not established [the capability required in the target condition], leaving [the specific research gap].**：回顾结束，问题出现。局限针对刚介绍的能力和条件。下一段再拆成具体困难，并说明成因与后果。

<a id="annotated-intro-obstacles"></a>

#### 局限与研究必要性模板

将研究问题拆成具体局限，并说明原因和实际妨碍。

**English 填空模板**

Achieving [the established research goal] remains difficult for two reasons. First, ***[limitation A]*** arises because [specific cause or missing capability]. This prevents [the concrete operation or evaluation needed for the goal]. Second, ***[limitation B]*** occurs when [relevant condition], making [another required operation] difficult. Together, these limitations prevent [the precise objective this paper will address].


**高亮与旁批**

1. **Achieving [the established research goal] remains difficult for two reasons.**：段首钩子。接回上一段目标，再解释困难。模板演示两项，数量按真实问题调整。
2. **First, [limitation A] arises because [specific cause or missing capability]. This prevents [the concrete operation or evaluation needed for the goal].**：局限 A：原因与妨碍。先命名具体困难，再解释其成因和实际后果。不要只给一个中性的属性标签。
3. **Second, [limitation B] occurs when [relevant condition], making [another required operation] difficult.**：局限 B：另一独立问题。与 A 区分清楚，写明在哪种条件下妨碍什么。两项应共同服务本文目标。
4. **Together, these limitations prevent [the precise objective this paper will address].**：承上启下。把局限落到目标上，下一段的设计才能自然出现。这个目标应与摘要、方法和实验问题保持一致。

<a id="annotated-intro-design"></a>

#### 设计与贡献总述模板

概述提出的产物，逐项解释设计如何回应前述局限。

**English 填空模板**

To address these limitations, we introduce *[Method]*, a [concrete artifact with its core design and purpose]. For [same limitation A], we [design A], which [verb phrase explaining how A resolves the limitation]. For [same limitation B], we [design B], allowing [the required operation]. [Key contribution object] is constructed from [verified source or selection rule] to [specific use]. Together, these designs enable [the task established in the preceding paragraph].


**高亮与旁批**

1. **To address these limitations, we introduce [Method], a [concrete artifact with its core design and purpose].**：段首先接问题，再报贡献。these limitations 指向上一段 A、B。方法名后立即交代产物与用途，不让读者读到段末才知道提出了什么。
2. **For [same limitation A], we [design A], which [verb phrase explaining how A resolves the limitation].**：A 对应设计 A。复用局限关键词，紧接真实设计和作用。这里讲解决思路，参数与实现步骤留到 Method。
3. **For [same limitation B], we [design B], allowing [the required operation].**：B 对应设计 B。同样建立问题与解法的对应关系。A、B 不能只在开头列出，方法介绍却不再回应。
4. **[Key contribution object] is constructed from [verified source or selection rule] to [specific use].**：关键产物先出现。先写读者需要记住的产物，再说明来源、筛选依据及用途；这些位置只填实际做过的工作。
5. **Together, these designs enable [the task established in the preceding paragraph].**：收束到目标。回到上一段的研究目标。读者应能看出几个设计为什么要组合成同一个方法。

<a id="annotated-intro-findings"></a>

#### 实验发现模板

先给发现总览，再用关键数字和分析回扣研究动机。

**English 填空模板**

To answer [the research question introduced above], we evaluate [Method or evaluated systems] on [datasets or tasks] against [comparison scope]. The experiments reveal [one-sentence overview of the main finding]. Specifically, [verified quantitative result with its comparator and unit]. Further analysis shows [which design or condition is associated with the observed outcome], supporting [the corresponding motivation or claim].


**高亮与旁批**

1. **To answer [the research question introduced above], we evaluate [Method or evaluated systems] on [datasets or tasks] against [comparison scope].**：实验钩子与范围。先接回研究问题，再用一句话交代评了什么、在哪评、和谁比。不要在这里铺完整实验设置。
2. **The experiments reveal [one-sentence overview of the main finding].**：先给发现总览。填一句读完能记住的结论；后面的数字与分析都支撑这句话。
3. **Specifically, [verified quantitative result with its comparator and unit].**：再给亮眼数字。用最有说服力的实测结果支持总览，写清比较对象、单位与适用范围。数字应与摘要及正文一致。
4. **Further analysis shows [which design or condition is associated with the observed outcome], supporting [the corresponding motivation or claim].**：最后解释发现。回扣开头的困难或动机，指出设计为何有价值。这里只概述正文实际做过且支持的分析。

<a id="template-intro-contributions"></a>
#### 贡献列表模板

用 3 条收束引言：整体工作、关键设计或证据贡献、实验发现。第 2 条按论文类型选用 propose 或 provide，不虚构新机制。 填入正式方法名时用 textit，普通描述不加斜体。

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

按主要贡献选择一套模板，不把四套拼在同一篇引言里。前两段可合并或交错；贡献保持三项，分别填整体工作、关键设计或证据贡献、实验发现。

<a id="intro-template-method"></a>
<details><summary>方法型引言</summary>

核心贡献是新方法或新的系统设计。

**领域与研究问题**

[research area] aims to [goal] by mapping [input] to [output]. Recent [approach family] can [supported capability] [citations]. These capabilities support [application], where [task requirement] matters for [practical objective]. This requirement motivates [research question].

先说研究对象、已有能力和实际要求，再让研究问题从这些要求中自然出现；背景与下一段的回顾可穿插。

**比较依据与局限**

Existing [approach family A] uses [input A] to [supported operation A] [citations], whereas [approach family B] relies on [input B] to [supported operation B] [citations]. However, [specific limitation] restricts [required capability] because [documented cause or operating assumption]. Under [relevant condition], this restriction leads to [observable consequence]. Addressing it requires [corresponding design requirement].

比较同一维度，用 However 点出自明的局限，再说它为什么妨碍目标；紧接下一段的解法，不插入无关回顾。

**对应设计与贡献**

To address these limitations, we propose \textit{[method name]}, a [verified distinguishing design and purpose]. For [specific limitation], we [concrete design action and contribution] to meet [corresponding design requirement]. It takes [input] and produces [output] through [high-level mechanism]. For [another established limitation, if present], we [next design action] using [preceding output] to [corresponding purpose]. Together, these designs enable [supported capability] under [stated conditions].

【铁律】方法名后立即交代亮点和用途；解法钩子点名前文同一个局限并给对应动作。每项设计有依据，正面修饰能从来源、操作或结果中核查。

**实验概述与结论边界**

To answer [research question], we compare \textit{[method name]} with [appropriate baselines] under [shared evaluation conditions]. Experiments show [verified main finding] on [metric or measured outcome] within [tested scope]. To examine [design motivation], [ablation or controlled comparison] tests [specific design choice] and shows [verified design finding]. Further analysis identifies [supported pattern or remaining limitation], indicating [bounded answer to the original question].

先概述发现，再展开设计检验和分析；与摘要、实验、结论使用同一发现和范围，不自动填写最优、显著提升或因果收益。

**贡献总结**

```latex
In summary, our contributions are:
\begin{itemize}
    \item We introduce \textit{[method name]}, which [performs the target task through the core components].
    \item We propose \textit{[new mechanism]} based on [verified basis], enabling [specific function] and [actual application].
    \item Evaluation on [tested scope] reveals [key experimental finding], supported by [the most informative verified comparison].
\end{itemize}
```

三项依次写方法、关键机制和实验证据；第 2 项点名真实设计及用途，不重述全部流程。

</details>

<a id="intro-template-benchmark"></a>
<details><summary>基准与数据集型引言</summary>

核心贡献是新的数据集、基准或评价协议。

**能力与评价问题**

Progress in [research area] enables [supported capability] [citations]. These capabilities support [application], where [condition relevant to the task] affects [required behavior]. Evaluating this behavior requires [observable input or evaluation property]. This requirement raises [research question].

先说明为什么需要评价这个具体能力，研究问题须落到可观察的输入、行为或结果。

**已有基准与评价缺口**

Existing [benchmark family A] measures [evaluation target A] using [reported inputs and criteria] [citations]. [benchmark family B] instead evaluates [evaluation target B] under [reported setting] [citations]. However, [specific evaluation limitation] limits evaluation of [specific required capability], as shown by [evidence-bounded comparison]. [required input or criterion] is needed to distinguish [behavior of interest] from [alternative behavior], so [corresponding evaluation design] is necessary.

按输入、判据和目标对应比较，缺失、未报告、未公开分开写；明确这个缺口让哪一种行为无法被区分。

**建设障碍与设计要求**

However, establishing [required evaluation] faces [self-explanatory construction obstacle]. [documented source or annotation constraint] makes [required construction step] difficult. In addition, [another independent obstacle, if present] limits [another necessary step] because [documented reason]. Addressing these obstacles is necessary to obtain [usable evaluation artifact] for [research question].

建设困难不同于前人的评价缺口；每个困难写清受阻步骤和后果。没有独立的第二项就删去对应句，必要时与前段合并。

**数据、判据与核心贡献**

To address these limitations, we propose \textit{[benchmark or dataset name]}, a [verified source or distinguishing design] for [evaluation purpose]. For [data construction obstacle], we construct [data contribution] from [verified source] using [documented selection or collection rule]. For [specific evaluation limitation], we [evaluation contribution and action] to measure [capability linked to the earlier gap]. The tested system receives [task input], while [evaluation evidence or criteria] is used by [evaluator] to assess [system output]. These components support [supported evaluation capability] within [coverage boundary].

【铁律】先突出产物，再写可执行的来源与构建依据；解法钩子复用评价局限名称。受测系统输入与评分材料分开，数据与判据分别接回对应困难。

**基准结果与研究发现**

To answer [research question], we evaluate [systems or model families] using [shared protocol]. Results reveal [verified main finding] within [tested scope]. Specifically, [named finding, if useful] describes [observed behavior or result contrast]. To examine [observed limitation], [diagnostic analysis] shows [supported diagnostic finding]. These results indicate [bounded implication] and leave [remaining question] unresolved.

结果段先给实际发现，不从模型名单或指标层级开讲；命名现象紧接含义，诊断回扣原问题且不扩大为未经检验的机制。

**贡献总结**

```latex
In summary, our contributions are:
\begin{itemize}
    \item We introduce \textit{[benchmark or dataset name]}, which supports [evaluation task] with [verified coverage and core components].
    \item We propose [construction or evaluation design] based on [verified source or principle] to [address the specific evaluation difficulty].
    \item Evaluation of [systems or model families] under [shared protocol] reveals [key quantitative finding and its scope].
\end{itemize}
```

三项依次写基准或数据集、构建或评价设计、测评发现；不把数据规模当成全部贡献。

</details>

<a id="intro-template-diagnostic"></a>
<details><summary>诊断驱动的改进研究引言</summary>

先通过诊断发现问题、定位瓶颈，再据此提出改进。全文先讲 Diagnostic Analysis，再讲 Method 与验证；不能只把发现塞到常规方法型结尾。

**已有能力判断与可检验问题**

[research area] seeks to [goal]. Existing [approach family] achieves [supported result] under [reported conditions] [citations]. However, it remains unclear whether this result demonstrates [target capability]. If the capability holds, [testable expectation] should be satisfied under [controlled condition].

先区分已有成绩与它被解释成的能力，再用 However 提出可检验质疑。背景与比较可穿插，不硬套段落数。

**诊断设计与关键发现**

To test this expectation, we construct [diagnostic comparison] by changing [target condition] while preserving [relevant controls]. The comparison reveals [verified diagnostic finding]. Further [discriminating control or process analysis] shows [supported bottleneck evidence], suggesting that [bounded interpretation]. These observations motivate [design requirement].

诊断先于方法。写清改变与保留条件，发现接到有依据的瓶颈；未检验的机制不写成事实。

**针对瓶颈的设计**

To address these limitations, we propose \textit{[method name]}, a [distinguishing design and purpose]. For [diagnosed bottleneck], we [concrete design action] to [corresponding role]. For [another established bottleneck, if present], we [next design action] using [preceding output] to [corresponding role]. [training or execution procedure] combines these components to produce [output].

核心动作靠前，每项设计接到前面的诊断。没有独立第二项就删去；训练或推理按实际方法写。

**回到诊断的改进验证**

To answer [original capability question], we evaluate \textit{[method name]} on [main task] and repeat [original diagnostic comparison]. Results show [verified main finding] and [verified finding under diagnostic conditions]. Further [process analysis or controlled ablation] examines [design motivation] and yields [verified result]. Together, these tests support [bounded conclusion] within [tested scope].

主任务表现、诊断复测和过程检验各有职责。先概述关键发现，再展开对应证据；结论回答最初的能力质疑。

**贡献总结**

```latex
In summary, our contributions are:
\begin{itemize}
    \item We investigate [target capability] through [diagnostic study], identifying [evidence-supported bottleneck] under [tested conditions].
    \item We propose \textit{[method name]} with [core design] to address [the diagnosed bottleneck].
    \item Evaluation on [main-task scope] and [diagnostic comparison] shows [the verified improvement or trade-off], answering [the original capability question].
\end{itemize}
```

三项依次写诊断得到的认识、针对瓶颈的设计、主任务与原诊断的验证结果。

</details>

<a id="intro-template-empirical"></a>
<details><summary>实证发现型引言</summary>

核心贡献是新的经验规律、系统比较或对既有解释的检验。

**现象与研究问题**

Understanding [research phenomenon] matters for [scientific or practical objective]. Prior [research route] establishes [supported finding] within [previously studied scope] [citations]. This evidence motivates [specific question about the phenomenon]. Answering this question requires distinguishing [competing possibilities] under [relevant condition].

把已知事实和未回答的问题分开，提前说明需要区分什么；与下一段的文献回顾可灵活合并。

**已有证据与检验缺口**

Existing studies examine [relationship or behavior] using [reported design] [citations]. They provide evidence for [supported interpretation] under [documented assumptions or scope]. However, [specific evidence limitation] prevents these results from resolving [research question]. A comparison that [required contrast or measurement] is needed to distinguish [explanation A] from [explanation B].

点出证据还不能回答的问题，紧接需要怎样检验；别把没测过写成失败，也别把相关性写成原因。

**研究设计与可检验贡献**

To address these limitations, we propose [study or analysis], a [verified distinguishing design] for testing [research question]. For [specific evidence limitation], we [core comparison or measurement]. We compare [groups or conditions] that differ in [examined factor], using [documented control or adjustment] to examine [alternative explanation]. [measurement or analysis contribution] measures [observable outcome] using [verified data or procedure]. This design estimates [precise quantity or relationship] within [study population and conditions].

【铁律】解法钩子点名证据缺口，贡献落到可复核的比较或测量。受控实验交代改变因素；观察研究交代自然差异、调整及估计对象，不把调整写成排除所有解释。

**主要发现与解释范围**

To answer [research question], we analyze [evidence] under [reported study conditions]. The results show [verified main relationship or contrast]. Further [robustness check or independent analysis] examines [specific alternative explanation] and yields [verified result]. These findings support [evidence-bounded interpretation] within [tested scope], while [unresolved limitation] restricts [claim or generalization].

先陈述发现，再说检验排除了什么、仍未排除什么；主结果和稳健性检查各有对象，最后回到同一研究问题与边界。

**贡献总结**

```latex
In summary, our contributions are:
\begin{itemize}
    \item We present a systematic study of [research question] using [data and study design].
    \item We provide [controlled comparisons, measurements, or an analysis protocol] that distinguish [the competing possibilities examined in this study].
    \item Our analysis reveals [key empirical finding] within [studied scope], supported by [the most informative verified contrast or robustness result].
\end{itemize}
```

三项依次写研究问题与范围、新的比较或测量证据、经验发现；没有新机制就不声称提出新机制。

</details>

---

Da1yuqin / [StarPaper](https://da1yuqin.github.io/StarPaper/)，[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)。转载保留署名、出处与许可，改编注明改动。
