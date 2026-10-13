# 摘要、引言与贡献：按需参考

以下为通用规则与教学模板，不是真实论文原文、研究事实或实测。

#### 摘要：问题到结果

摘要先说明研究价值与新增内容，再给主要结果。使用准确、常见的词，仅保留必要术语。

教学模板；【】填真实材料。

- 首次出现的术语就近解释；摘要主张必须有正文支持。
- 保留关键发现、比较对象和必要数字，不逐项报分。

推荐结构模板；长度按投稿要求

[Task] requires [specific capability] in [setting].

[任务]在[场景]下需要[具体能力]。

**第 1 句：**开门见山写任务需求，不先夸领域前景。

Existing approaches [established capability], but [specific limitation].

现有方法已能[已有能力]，但仍有[具体不足]。

**第 2 句：**先承认已有能力，再限定本研究的缺口。

For [specific limitation], we propose [method] that [key operation].

针对[具体限制]，我们提出[方法]，通过[关键操作]实现改进。

**第 3 句：**【铁律】摘要解法用 For 点名前文同一 limitation，再给实际动作。

Experiments on [tested scope] show [main finding] compared with [comparison].

在[实测范围]上的实验表明，相比[对照]，[主要发现]。

**第 4 句：**说明比较条件和主要发现，不能只写 achieves superior performance。

This finding supports [specific value] under [necessary condition].

这个发现说明，在[必要条件]下，[具体价值]成立。

**第 5 句：**收束意义及范围；若与上一句重复就合并，不固定为五句。

#### 先选主线：价值，还是发现

按主要贡献选择论证顺序。发现型工作可用“现象→质疑→诊断→方法→验证”；多个困难按类别逐项展开。

教学模板；【】填真实发现，不是论文原句或实测。

- 先概括领域与已有能力，再说明具体局限、对应设计与贡献。按真实困难分段，不固定为四段。
- 用具体对象与操作解释核心思想，写明输入、处理与证据，不能通过命名暗示未经验证的能力。

[Established expectation] suggests [expected behavior], yet we observe [verified contrary phenomenon] under [conditions].

按[已有认识]，应当出现[预期行为]，但我们在[条件]下观察到[已验证的相反现象]。

**第 1 句：**反直觉要有明确预期与真实观察；不要给普通结果硬加 surprisingly。

To test whether [candidate explanation] accounts for this pattern, we [controlled comparison].

为检验[候选解释]是否造成该现象，我们进行[控制比较]。

**第 2 句：**现象产生疑问，再用诊断排除解释；不能根据有利结果反向编写诊断理由。

Motivated by [supported diagnosis], we [matching design] and evaluate [targeted outcome].

根据[有证据的诊断]，我们采用[对应设计]，检验[针对性结果]。

**第 3 句：**诊断接方法，验证接贡献；不把相关现象直接写成原因。

#### 引言开头：方向与任务

从研究方向进入具体任务，背景仅保留理解后文问题所需的信息。

按论证顺序选用，段落可合并或拆分。

教学模板；【】填真实材料。

- 前两段可以先讲领域与进展，也可以从具体问题进入，再回顾和比较已有路线；段落顺序服务于论证。
- 领域背景、相关工作与比较都要交代；背景只留理解问题所需的信息，不固定“第一段背景、第二段局限”。

StarPaper 推荐结构模板

[Research direction] aims to [clear task objective] [citations].

[研究方向]旨在[清楚的任务目标][引用]。

**第 1 句：**先立研究对象，引用就近支持这个判断。

In [application], this capability matters because [evidence-supported value].

在[应用]中，这种能力影响[有依据的实际价值]。

**第 2 句：**用一句说明值得做，未经评估不能声称提高商业收益。

In this setting, [input] must be converted into [output] while satisfying [constraint].

在这一场景下，需要将[输入]转为[输出]，同时满足[约束]。

**第 3 句：**把大方向落到具体任务，接着概括已有解法做到哪一步。

#### 引言开头：领域回顾与比较

概括已有路线的机制与能力，比较相关工作的差异和边界；可与背景或局限放在同一自然段。

教学模板；【】填真实材料。

- 按任务、机制或评价目标分组，不逐篇点名。
- 引言与 Related Work 的分类、对象和关键词一致；机制细节放后者。
- 与背景的先后和段落分工可调整；开头要有领域回顾和有依据的比较，不能只有泛化背景。

StarPaper 规范化写法；段数按内容调整

Existing [research line] uses [shared mechanism] to [established capability] [citations].

现有[研究路线]通过[共同机制]实现[已建立的能力][引用]。

**第 1 句：**先承认已经解决的部分，再让读者理解下一段为何还提出困难。

Another line uses [different mechanism] to support [additional capability] [citations].

另一条路线通过[不同机制]支持[另一项能力][引用]。

**第 2 句：**只保留有实质差别的第二类方法；没有这类研究就删掉此句。

#### 引言承接：具体局限

写清现有方法在何种条件下不足，以及问题产生的原因。不能只用 expensive、limited、inefficient 概括。

按论证顺序选用，段落可合并或拆分。

教学模板；【】填真实材料。

- 用符合真实关系的转折承接已有能力；具体局限可与领域回顾放在同一段，也可另起一段，再进入对应设计。
- 给 2～3 个词的自明短名，首次就解释；困难数量按真实贡献，按实际内容确定。
- 每个困难都能指向后文设计与实验；命名新不等于发现新。

StarPaper 规范化写法

However, [existing capability] does not establish [missing property] when [condition].

然而，在[条件]下，[已有能力]仍不能说明[尚缺性质]成立。

**第 1 句：**说清评价或能力的证明边界，不把未证明改写成完全失败。

We call this difficulty [short name]. It occurs when [plain-language condition and consequence].

我们将这个困难称为[短名]。它发生在[普通语言说明的条件与后果]下。

**第 2 句：**名称帮助记住困难，紧接解释帮人理解。没有对应观察就不能仅凭名字制造新问题。

For example, [concrete input or situation] requires [specific behavior], which [existing comparison] does not assess.

例如，[具体输入或场景]需要[具体行为]，而[对照评价]尚未检验这一点。

**第 3 句：**例子显示缺口怎样发生，是否未检验仍需核对实际来源。

#### Intro 方法介绍段：固定开头句

these limitations 指前段已建立的具体局限。方法名后立即说明核心设计与用途，再按同一局限顺序展开解法；这是本教程的默认句式，当前人工定版优先。

按论证顺序选用，段落可合并或拆分。

教学模板；【】填真实材料。

- 【铁律】方法介绍段首接回前段已建立的具体局限；方法名后同一句说明产物、核心设计与用途。随后逐项点名局限及对应解法。本教程默认开头为 To address these limitations, we propose；当前稿的人工定版优先。引言讲设计思路，实现细节留给 Method。
- Introduction 说明设计思路与作用；公式、模型细节与实现参数放在 Method。
- 关键词与 Related Work、Method、图、实验一致。预期作用与实测效果分开。

StarPaper 规范化写法

To address these limitations, we propose [Method Name], a [method/framework] that [core design] to [specific purpose].

为应对这些局限，我们提出[方法名]，一种通过[核心设计]实现[具体目的]的[方法／框架]。

**第 1 句：**these limitations 接回前段局限；同一句给出方法名、设计与用途，不用名称代替解释。

For [challenge A], we [design A] using [actual input or signal].

为解决[困难 A]，我们利用[实际输入或信号]设计[A 方案]。

**第 2 句：**一对一接回上一段的困难。

This design [specific operation], allowing [specific intended capability].

该设计通过[具体操作]，支持[明确的目标能力]。

**第 3 句：**解释如何发生，不只把方案换个词再说一遍。

For [challenge B], we [design B].

为解决[困难 B]，我们采用[B 方案]。

**第 4 句：**第二项方案处理另一项真实问题；没有就删除，不添加无必要的模块。

**完整 LaTeX 结构模板**

```latex
To address these limitations, we propose [Method Name], a [method/framework] that [core design] to [specific purpose].
For [specific limitation A], we [design A and its concrete role].
For [another established limitation, if present], we [design B and its concrete role].
```

#### 引言收束：主要发现

设计之后写主要发现与启示，并给关键比较、条件及范围，不局限于分数提升。

按论证顺序选用，段落可合并或拆分。

教学模板；【】填真实材料。

- 发现可取短名，随后解释含义；不添加未测能力。
- 只讲关键关系，不复述结果表；引言图用来讲动机。

StarPaper 规范化写法

Experiments on [tested tasks] reveal [specific finding] under [comparison conditions].

在[比较条件]下，[实测任务]的实验揭示[具体发现]。

**第 1 句：**先说结果，限定实测范围。

This finding indicates [what is supported], while [remaining limitation] remains unresolved.

该发现支持[已证实的认识]，但[剩余局限]仍未解决。

**第 2 句：**解释贡献及边界，不扩大主张。

#### 引言最后：贡献列表

依次概括本文对象、机制及实际用途、有证据的发现；正文负责建立问题与解法的对应。

按论证顺序选用，段落可合并或拆分。

教学模板；【】填真实材料。

- 【铁律】普通正文引导句后接原生 itemize，固定三项：工作概述、新机制与实际用途、实验发现。第 2 项用 We propose [机制] 点名真正的新设计，说明依据、具体作用及实际应用；正文已建立问题与解法时，不再重复障碍标签。第 3 项给证据范围，新名称首次就近定义，列表后直接下一节。

本套 CS 写作约定：固定三项，不是所有会议的官方要求

In summary, our contributions are:

概括而言，我们的贡献如下：

**第 1 句：**普通正文引导句，后接原生 itemize。

We introduce [research object], a [verified distinguishing feature] for [task and purpose].

我们提出[研究对象]，以[已核验的核心特点]服务[任务与目的]。

**第 2 句：**第一项 Overview：先概括做了什么，不塞流程细账或排名。

We propose [mechanism], derived from [verified basis], which [specific function] and supports [actual application].

我们提出[机制]，依据[已核验来源]实现[具体作用]，并支持[实际应用]。

**第 3 句：**【铁律】第二项点名新机制，解释它做到了什么、用于什么；不再重复已经说明的障碍标签。

Experiments within [tested scope] reveal [verified main finding and necessary conditions].

在[实测范围]内，实验揭示[已核验的主要发现及必要条件]。

**第 4 句：**第三项概括发现，保持真实范围，不把常规实现另列为创新。

**完整 LaTeX 结构模板**

```latex
In summary, our contributions are:
\begin{itemize}
    \item We introduce [research object], which supports [task] with [verified distinguishing feature].
    \item We propose [mechanism], derived from [verified basis], which [specific function] and supports [actual application].
    \item Experiments within [tested scope] reveal [verified finding]. Further diagnosis identifies [supported recurring problems].
\end{itemize}
```

---

Da1yuqin / [StarPaper](https://da1yuqin.github.io/StarPaper/)，[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)。转载保留署名、出处与许可，改编注明改动。
