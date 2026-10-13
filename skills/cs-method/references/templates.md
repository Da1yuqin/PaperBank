# 方法、任务定义与 Overview：按需参考

以下为通用规则与教学模板，不是真实论文原文、研究事实或实测。

<a id="annotated-method-task"></a>

#### 任务定义

这一段交代研究处理什么、得到什么，以及什么算完成任务。

**English 填空模板**

Given [input objects and their sources], the task is to produce [output object] that satisfies [task requirements]. We denote [essential object] by [symbol] and define [the decision or objective]. During [training or inference], [system] has access to [available information]. [Evaluation-only information, if any] is used only for [evaluation role].


**高亮与旁批**

1. **Given [input objects and their sources]**：先给输入。填真实对象及来源；下一句的输出必须由这些输入得到。
2. **[output object] that satisfies [task requirements]**：定义输出与任务要求。写清输出形式和判断标准，让后面的模块与指标围绕同一目标。
3. **We denote [essential object] by [symbol] and define [the decision or objective].**：只引入必要符号。先解释对象，再定义下文实际使用的符号；具体模块公式留在对应小节。
4. **During [training or inference], [system] has access to [available information]. [Evaluation-only information, if any] is used only for [evaluation role].**：区分各阶段可见信息。存在训练、推理、评价阶段时分别交代，避免把评价答案写成模型输入。没有对应阶段就删去。

<a id="annotated-method-overview-teaching"></a>

#### 方法总览

这一段是后续小节的地图：目的、模块职责、输入输出、阅读位置。

**English 填空模板**

To address [Introduction limitation A], in [exact subsection A title] (Section [A]), we [design action] using [input] to obtain [intermediate output]. To address [Introduction limitation B], in [exact subsection B title] (Section [B]), we use this [intermediate output] together with [additional input] to [next action]. Finally, in [exact subsection C title] (Section [C]), [actual executor] transforms [preceding output] into [final output] for [task objective]. Figure [framework] summarizes these dependencies.


**高亮与旁批**

1. **To address [Introduction limitation A]**：从引言的问题起笔。填前文已经建立的具体局限，说明这项设计为什么需要。
2. **in [exact subsection A title] (Section [A]), we [design action] using [input] to obtain [intermediate output]**：用一句话概括一个小节。章节名与节号负责导航，执行者负责操作；同时交代这一节接收和产出什么。
3. **we use this [intermediate output] together with [additional input]**：把真实产物接到下一步。此模板展示串行依赖；并行模块分别写其输入，再说明汇合位置，不能把独立来源强行串起来。
4. **transforms [preceding output] into [final output] for [task objective]**：收束到任务目标。末个模块给出最终产物，并接回任务定义的输出要求。模块不足或超过三项时按真实结构增删。
5. **Figure [framework] summarizes these dependencies.**：图文共同指向同一结构。框架图、总览与后续小节使用相同名称和依赖关系。

<a id="annotated-method-module"></a>

#### 方法模块

每个实际模块重复这一结构：具体目的、设计依据、操作、输出。

**English 填空模板**

To [solve the specific problem assigned to this module], we [key design action]. This design addresses [the specific insufficiency of the input or existing operation] by [the mechanism that meets the requirement]. Given [actual module input], [executor] performs [necessary operation] according to [criterion or equation]. The operation produces [output representation and relevant fields], which [next module] uses to [next purpose].


**高亮与旁批**

1. **To [solve the specific problem assigned to this module], we [key design action].**：首句连接目的与设计。不要只写模块名字，也不要反复用泛泛的“提高质量”。
2. **This design addresses [the specific insufficiency of the input or existing operation] by [the mechanism that meets the requirement].**：解释为什么这样做。写出设计针对的具体缺陷和作用机制；这一步比罗列实现步骤更重要。
3. **Given [actual module input], [executor] performs [necessary operation] according to [criterion or equation].**：再交代如何执行。按读者复现所需补充关键操作、条件或公式；使用外部组件时给名称与来源。
4. **[output representation and relevant fields], which [next module] uses to [next purpose]**：末句交接产物。写清产物交给哪个模块、供它完成什么操作。最后一个模块改为说明如何满足最终输出要求；参数数值放实现细节。

---

Da1yuqin / [StarPaper](https://da1yuqin.github.io/StarPaper/)，[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)。转载保留署名、出处与许可，改编注明改动。
