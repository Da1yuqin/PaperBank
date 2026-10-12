# 方法、任务定义与 Overview：按需参考

以下为通用规则与教学模板，不是真实论文原文、研究事实或实测。

#### Method Overview：完整模板

首句说明关键设计为何针对 Introduction 的困难，随后按真实依赖说明各步骤与章节位置。

教学模板；【】填真实材料。

- 先写核心设计相对已有做法的最有用区别，再介绍各节如何实现它；只列目录没有贡献。
- Overview、章节标题、framework 中的模块名称对应；章节名是阅读位置，不是执行动作的主体。
- 每步说目的、输入、操作与输出，用准确章节引用定位一次；后句接前句产物，并行关系照实写。
- 末句引用框架图；已有章首总览不再单开重复 Overview。格式转换不单独列为创新模块。

BeautyPaper 规范化写法；按真实依赖替换或删除阶段

To address [Intro challenge], we [key design] rather than [verified prior approach], so that [specific intended capability].

为解决[引言困难]，我们用[关键设计]替代[已核验的已有做法]，以实现[具体目标能力]。

**第 1 句：**第一句先交代为什么这个做法值得采用。区别有来源，收益是目标还是实测要分清。

In [Problem Formulation] (Section [ref]), we define [input] and [required output].

我们在[问题定义]（[真实节号]）中定义[输入]与[要求的输出]。

**第 2 句：**承接目的，定义真实任务；没有这个章节就删除导航，不凭空补一节。

Following this definition, in [Input Construction] (Section [ref]), we construct [inputs] from [verified source].

按照这一任务定义，我们在[输入构造]（[真实节号]）中从[已核验来源]构造[输入]。

**第 3 句：**承接任务定义，不凭空把定义写成数据产物。

Using [constructed inputs], in [Processing] (Section [ref]), we [operation] to obtain [intermediate output].

利用[已构造输入]，我们在[处理章节]（[真实节号]）中执行[操作]，得到[中间产物]。

**第 4 句：**上一句输出成为本句输入，目的和结果都有落点。

Given [intermediate output], in [Output Generation] (Section [ref]), we [operation] and produce [final output].

给定[中间产物]，我们在[输出生成]（[真实节号]）中执行[操作]，产生[最终输出]。

**第 5 句：**交代产物怎样进入下一步；实际并行则改成真实并行关系。

Figure [ref] summarizes this workflow.

图[真实编号]概括了这一流程。

**第 6 句：**收束到框架图，读者此时能把每个节点与正文对应。

**完整 LaTeX 结构模板**

```latex
To address [Intro challenge], we [key design] rather than [verified prior approach]
to [specific intended capability].
In \textbf{[Problem Formulation]}
(\S\ref{sec:problem}), we define [input] and [required output].
Following this definition, in \textbf{[Input Construction]}
(\S\ref{sec:inputs}), we construct [inputs] from [verified source].
Using [constructed inputs], in \textbf{[Processing]}
(\S\ref{sec:processing}), we [operation] to obtain [intermediate output].
Given [intermediate output], in \textbf{[Output Generation]}
(\S\ref{sec:output}), we [operation] and produce [final output].
Figure~\ref{fig:framework} summarizes this workflow.
```

#### Problem Formulation：任务定义

用必要对象、输入、输出与约束定义任务，符号随实际计算引入。

教学模板；【】填真实材料。

- 训练、推理、评价可见的信息分清；参考答案不能混入推理输入。
- 符号写对象、单位和下标；后文不用的定义删掉。

通用要求；有需要才设独立小节

Given [input], the task is to produce [output] that satisfies [requirements].

给定[输入]，任务是产生满足[要求]的[输出]。

**第 1 句：**先把任务讲通，读者随后才知道符号代表什么。

We denote [concrete object] by [symbol], where [indices and units].

我们用[符号]表示[具体对象]，其中[说明下标与单位]。

**第 2 句：**符号不能只给英文名，要与真实对象连接。

At inference time, [executor] receives [visible information]; [reference information] is used only for evaluation.

推理时，[执行者]接收[可见信息]；[参考信息]仅用于评价。

**第 3 句：**明确信息边界。实际方法确实使用额外信息时如实写，不照抄示例。

#### Method 小节：为什么这样做，再写怎么做

小节按创新点与对应困难组织，先写设计目的与依据，再写必要实现及产物。

教学模板；【】填真实材料。

- 【铁律】方法模块、subsection 和 Step 的正文开头先交代具体动机，用 To [具体问题或目的], [真实执行者] [设计或动作] 接回问题，再讲设计依据、输入输出与必要实现。目的不能反复写成泛泛的质量提升，Overview 的承接句不机械重复 To。
- 关键计算用编号公式，符号就近定义；长算法、完整 prompt 和参数表放附录。
- 粗体段首对应真实模块或步骤，名称与框架图一致。
- 并行、循环、反馈单独说明；训练信号注明样本、阶段、指标和更新对象。
- 自己的创新占主要篇幅，标准编码、调用与格式转换简写；不能把已有方法改名当创新。
- 每节结尾说明输出与后续用途，下一节使用对应产物。重点是为什么值得做，复现所需细节仍要给全。

通用要求；BeautyPaper 推荐句式

To [specific problem or purpose], we [actual design or operation] using [real input].

为处理[具体问题或目的]，我们利用[真实输入]进行[实际设计或操作]。

**第 1 句：**【铁律】首句先给本节具体动机、真实执行者与设计，不能用笼统的质量提升代替问题。

This design addresses [Intro limitation] by [reason the design targets it].

该设计通过[它为何针对这个问题]来处理[引言局限]。

**第 2 句：**不能只说“为了解决”；要解释做法与问题之间的关系，效果由后文对照验证。

For each [unit], we compute [quantity] from [signal source] under [condition].

对每个[计算单位]，我们在[条件]下从[信号来源]计算[量]。

**第 3 句：**操作落实到单位与来源，公式才有实际含义。

Here, [symbol] denotes [object], and [subscript] indexes [unit].

其中，[符号]表示[对象]，[下标]索引[单位]。

**第 4 句：**按公式实际需要逐一说明，不复制没用到的定义。

The resulting [output] is passed to [next step] for [purpose].

生成的[产物]交给[下一步]，用于[目的]。

**第 5 句：**末句启下；不存在这项依赖就如实改写。

---

Da1yuqin / [BeautyPaper](https://da1yuqin.github.io/PaperBank/)，[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)。转载保留署名、出处与许可，改编注明改动。
