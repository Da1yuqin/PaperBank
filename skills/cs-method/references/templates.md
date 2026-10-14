# 方法、任务定义与 Overview：按需参考

以下为通用规则与教学模板，不是真实论文原文、研究事实或实测。

<a id="annotated-method-task"></a>

#### 任务定义

定义输入、输出与任务完成标准。

**English 填空模板**

Given [input objects and their sources], the task is to produce [output object] that satisfies [task requirements]. We denote [essential object] by [symbol] and define [the decision or objective]. During [training or inference], [system] has access to [available information]. [Evaluation-only information, if any] is used only for [evaluation role].


**高亮与旁批**

1. **Given [input objects and their sources]**：先给输入。填实际输入及来源。后续输出必须由这些输入得到。
2. **[output object] that satisfies [task requirements]**：输出与任务要求。填输出形式与判断标准。供后续模块和指标使用。
3. **We denote [essential object] by [symbol] and define [the decision or objective].**：必要符号。先解释对象，再定义符号。模块公式放对应小节。
4. **During [training or inference], [system] has access to [available information]. [Evaluation-only information, if any] is used only for [evaluation role].**：各阶段可见信息。分清训练、推理与评价的信息。评价答案不能充当模型输入。不存在的阶段删去。

<a id="annotated-method-overview-teaching"></a>

#### 方法总览

概括模块职责、输入输出与所在小节。

**English 填空模板**

To address [Introduction limitation A], in [exact subsection A title] (Section [A]), we [design action] using [input] to obtain [intermediate output]. To address [Introduction limitation B], in [exact subsection B title] (Section [B]), we [next action] using this [intermediate output] and [additional input]. This step produces [output of module B]. Finally, in [exact subsection C title] (Section [C]), [actual executor] transforms this [output of module B] into [final output] for [task objective]. Figure [framework] summarizes these dependencies.


**高亮与旁批**

1. **To address [Introduction limitation A]**：接回引言问题。填引言已建立的局限。说明为何需要这项设计。
2. **in [exact subsection A title] (Section [A]), we [design action] using [input] to obtain [intermediate output]**：一句概括一个小节。填节名、节号、执行者与操作。写清接收什么、产出什么。
3. **we [next action] using this [intermediate output] and [additional input]. This step produces [output of module B].**：交接实际产物。串行模块交接实际产物。并行模块分别写输入与汇合点。
4. **transforms this [output of module B] into [final output] for [task objective]**：收束到任务目标。末个模块给最终输出。模块数量按真实结构增删。
5. **Figure [framework] summarizes these dependencies.**：图文结构一致。框架图、总览与小节同名。三处使用相同依赖关系。

<a id="annotated-method-module"></a>

#### 方法模块

每个模块写：目的、依据、操作、输出。

**English 填空模板**

To [solve the specific problem assigned to this module], we [key design action]. This design addresses [the specific insufficiency of the input or existing operation] by [the mechanism that meets the requirement]. Given [actual module input], [executor] performs [necessary operation] according to [criterion or equation]. The operation produces [output representation and relevant fields], which [next module] uses to [next purpose].


**高亮与旁批**

1. **To [solve the specific problem assigned to this module], we [key design action].**：首句：目的与设计。填该模块要解决的具体问题。紧接相应设计或动作。
2. **This design addresses [the specific insufficiency of the input or existing operation] by [the mechanism that meets the requirement].**：解释为什么这样做。填设计针对的缺陷与作用机制。解释设计依据，不能只列步骤。
3. **Given [actual module input], [executor] performs [necessary operation] according to [criterion or equation].**：说明如何执行。补充复现所需的操作与条件。外部组件注明名称和来源。
4. **[output representation and relevant fields], which [next module] uses to [next purpose]**：末句交接产物。写产物交给谁、用于什么。末个模块说明最终输出。参数数值放实现细节。

---

Da1yuqin / [StarPaper](https://da1yuqin.github.io/StarPaper/)，[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)。转载保留署名、出处与许可，改编注明改动。
