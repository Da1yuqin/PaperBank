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

```latex
Our contributions are summarized as follows:
\begin{itemize}
  \item We introduce \textit{[Method or artifact]}, which [performs the task through the core components].
  \item We propose \textit{[new mechanism]} based on [verified basis], enabling [specific function] and [another actual use, if supported].
  \item Our evaluation on [scope] reveals [key finding], with [the most informative verified evidence].
\end{itemize}
```

---

Da1yuqin / [StarPaper](https://da1yuqin.github.io/StarPaper/)，[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)。转载保留署名、出处与许可，改编注明改动。
