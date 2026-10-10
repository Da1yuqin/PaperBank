# PaperBank 写作检查参考

按本次任务选规则。下面示例是假设情境，不是论文原文或实测；实际改稿先核对事实。

网页：[写作铁律](https://da1yuqin.github.io/PaperBank/#general-rules) · [论文结构与逐句例子](https://da1yuqin.github.io/PaperBank/#paper-order) · [rebuttal](https://da1yuqin.github.io/PaperBank/#chapter-rebuttal)

## 对象与贡献


### 第 81 条：一个对象一个名字

同一对象用同一术语；指代不清就写对象名。

适用边界：适用：方法对象、状态、指标和跨章节措辞。这是推荐写法，按论文类型和当前投稿要求调整；清晰的代词和必要的长句可以保留。

**一个对象用一个名字**

**教学示例：假设情境，非论文原文**

改后假定已有对应记录；实际改稿须先核对这些事实，不能从改前文字推断或补造。

**改前 · 中文**

检索器输出文档，重排器调整它们；它随后筛选结果。

**Before · English**

The retriever returns documents and the reranker reorders them; it then filters the results.

**改后 · 中文**

检索器输出候选文档。重排器调整文档顺序，并筛选高分文档。

**After · English**

The retriever returns candidate documents. The reranker reorders the documents and retains high-scoring documents.

**逐句拆解**

同一对象使用同一名称，明确每个动作的执行者与接收者。

### 第 71 条：结论不超过证据

结论写明测试对象和条件；平均提升不等于每例都好。

适用边界：适用：正文、摘要、标题、结论和回复审稿意见。证据与记录必须如实；不适用的检查注明原因。

**主张不能比证据更大**

**教学示例：假设情境，非论文原文**

改后假定已有对应记录；实际改稿须先核对这些事实，不能从改前文字推断或补造。

**改前 · 中文**

我们的模型解决了长文本理解。

**Before · English**

Our model solves long-context understanding.

**改后 · 中文**

在本次两个长文问答测试集上，模型的平均准确率高于基线；其他任务尚未测试。

**After · English**

On the two long-document QA test sets in this study, the model achieves higher mean accuracy than the baseline. Other tasks have not been tested.

**逐句拆解**

结论须限定任务、条件与统计对象，并与已有证据一致。

## 词语、数字与主张


### 第 82 条：定义交代对象与来源

中间量写清样本、阶段、指标和用途；下标逐个解释。

适用边界：适用：学习信号、符号和中间量定义。这是推荐写法，按论文类型和当前投稿要求调整；清晰的代词和必要的长句可以保留。

**首次出现，交代对象和来源**

**教学示例：假设情境，非论文原文**

改后假定已有对应记录；实际改稿须先核对这些事实，不能从改前文字推断或补造。

**改前 · 中文**

我们用他们的结果优化它。

**Before · English**

We use their outcomes to optimize it.

**改后 · 中文**

我们把每次执行的最终答案正确标记作为奖励（正确为 1，否则为 0），更新策略模型。

**After · English**

We use final-answer correctness for each execution as the reward (1 if correct, 0 otherwise) to update the policy model.

**逐句拆解**

定义须说明具体对象、信号来源与作用对象。

### 第 80 条：一句一项判断

一句一个主要判断，一段一个任务；拆句保留条件和衔接。

适用边界：适用：正文、图注和附录说明。这是推荐写法，按论文类型和当前投稿要求调整；清晰的代词和必要的长句可以保留。

**一句一个主张，一段一个任务**

**教学示例：假设情境，非论文原文**

改后假定已有对应记录；实际改稿须先核对这些事实，不能从改前文字推断或补造。

**改前 · 中文**

我们提出一个系统并构建数据集且加入模块并发现迁移有效同时改善效率。

**Before · English**

We propose a system, construct a dataset, add a module, find effective transfer, and improve efficiency.

**改后 · 中文**

我们构建数据集并定义评价协议。随后，我们检验模块的效果。迁移和效率结果分别在两个小节报告。

**After · English**

We construct the dataset and define the evaluation protocol. We then test the module. Transfer and efficiency results are reported in separate subsections.

**逐句拆解**

每句表达一个完整判断；拆句后仍须保留必要条件与逻辑关系。

### 第 73 条：数字有单位与分母

分清样本与记录、百分比与百分点；数值对应同一协议。

适用边界：适用：数据规模、通过率、效果差异。证据与记录必须如实；不适用的检查注明原因。

**数字带上单位、分母和版本**

**教学示例：假设情境，非论文原文**

改后假定已有对应记录；实际改稿须先核对这些事实，不能从改前文字推断或补造。

**改前 · 中文**

记录显示 200 条记录来自 120 名用户；稿件却写：200 名用户，准确率从 60% 到 66%，提升 6%。

**Before · English**

The records show 200 observations from 120 users, but the manuscript says: 200 users; accuracy rose from 60% to 66%, a 6% improvement.

**改后 · 中文**

准确率提高 6 个百分点，相对提高 10%；200 条记录来自 120 名用户。

**After · English**

Accuracy increased by 6 percentage points, or 10% relative. The 200 records came from 120 users.

**逐句拆解**

数字须注明单位、分母、统计对象及变化尺度。

## 任务与已有进展


### 第 72 条：引用回原文

核对引用支持哪句话；模型名和版本与实际使用一致。

适用边界：适用：文献比较、模型／数据集／工具介绍。证据与记录必须如实；不适用的检查注明原因。

**引用查原文，版本对得上**

**教学示例：假设情境，非论文原文**

改后假定已有对应记录；实际改稿须先核对这些事实，不能从改前文字推断或补造。

**改前 · 中文**

模型 v2 的能力由 v1 的报告证明。

**Before · English**

The v1 report establishes the capabilities of model v2.

**改后 · 中文**

引用 v2 的官方模型卡；若模型卡未报告该能力，就删去该能力主张。

**After · English**

Cite the official model card for v2. Remove any capability claim that the card does not support.

**逐句拆解**

分别核对来源是否存在，以及原文是否支持引用处主张。

### 第 85 条：先例能力如实说

先写前人解决了什么，再写还缺什么；未测过不等于失败。

适用边界：适用：Related Work 和创新定位。这是推荐写法，按论文类型和当前投稿要求调整；清晰的代词和必要的长句可以保留。

**先承认先例，再说具体边界**

**教学示例：假设情境，非论文原文**

改后假定已有对应记录；实际改稿须先核对这些事实，不能从改前文字推断或补造。

**改前 · 中文**

现有方法完全忽视用户约束。

**Before · English**

Existing methods completely ignore user constraints.

**改后 · 中文**

现有方法处理已明确的偏好；本研究评价偏好尚未明确时，回复是否给出条件建议或必要澄清。

**After · English**

Existing methods address stated preferences. This study evaluates whether responses provide conditional advice or necessary clarification when preferences remain unspecified.

**逐句拆解**

准确说明前人工作的能力与适用边界，避免一概否定。

## 设计回应问题


### 第 84 条：问题、设计、实验对上

问题、设计、实验一一对应；未验证的作用写成目的。

适用边界：适用：引言、方法总览和实验组织。这是推荐写法，按论文类型和当前投稿要求调整；清晰的代词和必要的长句可以保留。

**重新对齐研究设计：方案示范**

**教学示例：假设情境，非论文原文**

下面是重新对齐研究设计的教学方案，需要实际实施和验证；不能靠润色就宣称实验已完成。

**改前 · 中文**

困难是检索漏证据；方法只改答案格式；实验只报告运行速度。

**Before · English**

The problem is missing evidence; the method changes answer formatting; the experiment reports only runtime.

**改后 · 中文**

困难是检索漏证据；方法扩大相关片段覆盖；实验比较证据召回率与答案准确率，并报告成本。

**After · English**

The problem is missing evidence. The method expands coverage of relevant segments. The experiment compares evidence recall and answer accuracy, and reports the cost.

**逐句拆解**

引言问题、方法设计与实验验证逐项对应。

## 贡献与证据


### 第 87 条：贡献写动作与证据

一项贡献一个动作，写清对象和意义；命名不算创新。

适用边界：适用：贡献列表和摘要。这是推荐写法，按论文类型和当前投稿要求调整；清晰的代词和必要的长句可以保留。

**贡献写动作和证据**

**教学示例：假设情境，非论文原文**

改后假定已有对应记录；实际改稿须先核对这些事实，不能从改前文字推断或补造。

**改前 · 中文**

我们提出革命性的智慧闭环范式，并实现数据加载、缓存和日志模块。

**Before · English**

We introduce a revolutionary intelligent loop paradigm and implement data loading, caching, and logging modules.

**改后 · 中文**

我们提出按证据覆盖选择检索片段的方法，并在固定预算下检验其对答案准确率的影响。

**After · English**

We propose selecting retrieval segments by evidence coverage and evaluate the effect on answer accuracy under a fixed budget.

**逐句拆解**

用具体动作与证据说明贡献，名称和形容词不能替代验证。

### 第 79 条：每段服务于主线

每段服务问题、设计或证据；无关背景删掉。

适用边界：适用：引言和全文组织。这是推荐写法，按论文类型和当前投稿要求调整；清晰的代词和必要的长句可以保留。

**每段回答一个贡献问题**

**教学示例：假设情境，非论文原文**

改后假定已有对应记录；实际改稿须先核对这些事实，不能从改前文字推断或补造。

**改前 · 中文**

人工智能发展迅速。算力不断提升。各领域出现许多系统。

**Before · English**

AI is developing rapidly. Computing power is increasing. Many systems have appeared across fields.

**改后 · 中文**

长文问答需要定位分散证据；现有系统常漏掉跨段关系，因此本研究检验分段检索是否改善证据覆盖。

**After · English**

Long-document QA requires locating dispersed evidence. Existing systems often miss relations across paragraphs, so this study tests whether segment-level retrieval improves evidence coverage.

**逐句拆解**

每段须说明具体问题、设计、证据或意义，删除无关背景。

### 第 83 条：连接词符合关系

连接词符合真实关系；并行流程不能写成先后步骤。

适用边界：适用：句间、段间和章节衔接。这是推荐写法，按论文类型和当前投稿要求调整；清晰的代词和必要的长句可以保留。

**连接词要连接真实关系**

**教学示例：假设情境，非论文原文**

改后假定已有对应记录；实际改稿须先核对这些事实，不能从改前文字推断或补造。

**改前 · 中文**

模块 A 提取文本。Therefore，模块 B 检索图像。（B 不依赖 A）

**Before · English**

Module A extracts text. Therefore, module B retrieves images. [B does not depend on A.]

**改后 · 中文**

模块 A 提取文本，模块 B 独立检索图像。融合模块随后合并两路结果。

**After · English**

Module A extracts text, while module B independently retrieves images. The fusion module then combines both outputs.

**逐句拆解**

连接词须符合真实依赖关系，不能暗示未经证明的因果或步骤。

## 动机图


### 第 89 条：图表能独立读懂

图中对象、指标、单位、误差和图例都要说明。

适用边界：数据、信息边界和完成状态按实际记录说明。

**看图就能知道比了什么**

**教学示例：假设情境，非论文原文／实测记录**

改后假定已有对应记录；实际改稿须先核对这些事实，不能从改前文字推断或补造。

**逐句拆解**

任务数和重复次数分开写；误差条是哪一种不确定性也写清。

**教学改写 · English（非论文原文）**

Accuracy on the same 100 held-out tasks. Bars show the mean across five independent runs; error bars show the standard deviation across runs. Higher is better. Blue denotes the baseline and green denotes the revised method.

**教学改写 · 中文（非论文原文）**

同一批 100 个留出任务上的准确率。柱高表示五次独立运行的均值；误差条表示运行间的标准差。指标越高越好。蓝色是基线，绿色是修改后的方法。

## 任务与真实流程


### 第 90 条：训练与推理信息分开

训练、推理、评价分开；推理不能看到答案或未来信息。

适用边界：可见信息按真实协议说明；训练标签可以用于训练，推理时不能获得的答案或未来信息不进入推理输入。

**箭头按真实依赖连，正确答案不能进入推理输入**

**教学示例：假设情境，非论文原文／实测记录**

改后假定已有对应记录；实际改稿须先核对这些事实，不能从改前文字推断或补造。

**逐句拆解**

未来记录可以进入评价框，不能沿箭头流回预测输入。

**教学改写 · English（非论文原文）**

The model receives records available by 2020 and predicts the 2022 outcome. A separate evaluation step compares the prediction with the observed 2022 record; the observed outcome is not supplied to the predictor.

**教学改写 · 中文（非论文原文）**

模型接收截至 2020 年已经知道的记录，预测 2022 年的结果。另一条评价流程用真实的 2022 年记录检验预测；真实结果不传给预测模型。

## 框架图与案例读法


### 第 91 条：验收最终 PDF

最终 PDF 查字号、遮挡、裁切和读序；需要可选文字时实测。

适用边界：字号、色板和版式以当前模板及读者需求为准，不要求固定尺寸或固定配色。

**按最终尺寸验收，不要只看放大预览**

**教学示例：假设情境，非论文原文／实测记录**

改后假定已有对应记录；实际改稿须先核对这些事实，不能从改前文字推断或补造。

**逐句拆解**

缩图会连带缩字；把位图装进 PDF 也不会自动得到原生文字。

**教学改写 · English（非论文原文）**

A 160 mm source figure will be inserted at 80 mm, so its text will shrink by half. Re-export it for 80 mm and inspect the inserted page; extract the labels if the deliverable requires selectable text.

**教学改写 · 中文（非论文原文）**

源图宽 160 mm，插入论文时只有 80 mm，图中文字也会缩成一半。按 80 mm 重新导出，再看实际论文页面；交付要求文字可选择时，还要抽取标签验证。

### 第 92 条：图形标记含义一致

全文统一颜色、线型和名称；通过、失败、不适用标清。

适用边界：字号、色板和版式以当前模板及读者需求为准，不要求固定尺寸或固定配色。

**同一含义用同一标记，结论不要只靠颜色**

**教学示例：假设情境，非论文原文／实测记录**

改后假定已有对应记录；实际改稿须先核对这些事实，不能从改前文字推断或补造。

**逐句拆解**

蓝色只是这个示例的自定映射，其他论文可以选自己的色板，但要前后一致。

**教学改写 · English（非论文原文）**

Blue dashed boxes denote model inputs throughout the paper. An evaluated rule is labeled Pass, Fail, or N/A; a rule that has not been evaluated remains unchecked.

**教学改写 · 中文（非论文原文）**

全文都用蓝色虚线框表示模型输入。已经评价的规则写通过、失败或不适用；还没评价的规则保留空框。

### 第 95 条：教学例子标明身份

教学例子、模型实测和人工评价标清；无记录不画评分。

适用边界：数据、信息边界和完成状态按实际记录说明。

**明确区分作者示例与模型实测**

**教学示例：假设情境，非论文原文／实测记录**

改后假定已有对应记录；实际改稿须先核对这些事实，不能从改前文字推断或补造。

**逐句拆解**

图面附近标出例子身份；总体表现仍由有记录的测试来支持。

**教学改写 · English（非论文原文）**

Illustrative response written by the authors: the assistant requests the missing budget before recommending an option. This example explains the intended behavior; it is not a recorded model output or evidence of a pass rate.

**教学改写 · 中文（非论文原文）**

作者构造的示例回复：助手先询问缺失的预算，再给建议。这个例子解释预期行为，不是记录中的模型输出，也不能证明通过率。

## 问题与比较设计


### 第 93 条：比较统一口径

样本、记录、任务和重复次数分开；子集不能冒充全量。

适用边界：数据、信息边界和完成状态按实际记录说明。

**比较用同一口径，样本写清单位与分母**

**教学示例：假设情境，非论文原文／实测记录**

改后假定已有对应记录；实际改稿须先核对这些事实，不能从改前文字推断或补造。

**逐句拆解**

先核对实际比较范围；是否把无效输出计入主指标，必须由评价协议决定并公开。

**教学改写 · English（非论文原文）**

On the 90 tasks for which both methods returned valid outputs, A scores 72/90 and B scores 75/90. Report the excluded 10 tasks and the invalid-output policy; these conditional scores do not describe all 100 tasks.

**教学改写 · 中文（非论文原文）**

两种方法都输出有效答案的 90 个任务中，A 答对 72 个，B 答对 75 个。另报排除的 10 个任务和无效输出处理规则；这组条件得分不代表全部 100 个任务。

## 指标与主要发现


### 第 86 条：结果段解释关系

解释图表中的关系和它回答的问题，不逐格重复数值。

适用边界：适用：主实验、消融和案例分析。这是推荐写法，按论文类型和当前投稿要求调整；清晰的代词和必要的长句可以保留。

**结果段解释发现，不朗读表格**

**教学示例：假设情境，非论文原文**

改后假定已有对应记录；实际改稿须先核对这些事实，不能从改前文字推断或补造。

**改前 · 中文**

相同预算下，A 无检索 70 分、有检索 72 分；B 无检索 72 分、有检索 74 分。

**Before · English**

Under the same budget, A scores 70 without retrieval and 72 with retrieval; B scores 72 without retrieval and 74 with retrieval.

**改后 · 中文**

在相同预算下，加入检索的两个模型都比各自无检索版本更准确，支持检索在本任务中的作用（表 2）。

**After · English**

Under the same budget, both retrieval variants are more accurate than their respective no-retrieval controls, supporting the role of retrieval in this task (Table 2).

**逐句拆解**

正文说明比较关系及其对应的问题，详细数值由表格提供。

### 第 74 条：观察不写成因果

观察与解释分开；没有相应对照，不写因果。

适用边界：适用：结果分析和机制讨论。证据与记录必须如实；不适用的检查注明原因。

**观察、解释、机制分开写**

**教学示例：假设情境，非论文原文**

改后假定已有对应记录；实际改稿须先核对这些事实，不能从改前文字推断或补造。

**改前 · 中文**

使用更多工具让模型更聪明。

**Before · English**

Using more tools makes the model smarter.

**改后 · 中文**

工具调用次数与准确率相关；这项观察不能说明更多调用导致更高准确率。

**After · English**

Tool-call count is associated with accuracy. This observation does not establish that additional calls cause higher accuracy.

**逐句拆解**

区分观察与因果解释，因果结论须有对应识别条件。

### 第 94 条：最优不等于显著

同指标、同协议才比最优；均值最高不等于显著更好。

适用边界：数据、信息边界和完成状态按实际记录说明。

**最优按列判断，显著性另给证据**

**教学示例：假设情境，非论文原文／实测记录**

改后假定已有对应记录；实际改稿须先核对这些事实，不能从改前文字推断或补造。

**逐句拆解**

排名、显示精度和统计推断是三件事；不能用更多小数位或颜色制造结论。

**教学改写 · English（非论文原文）**

A and B both display 80.0 accuracy, so they share the displayed rank. If boldface marks the highest displayed value, define that rule. Claim a statistically significant difference only when the specified comparison and test support it.

**教学改写 · 中文（非论文原文）**

A 和 B 的准确率都显示为 80.0，就共享这个显示值的排名。若粗体表示最高显示值，在表注写明。只有指定比较和统计检验支持时，才能说差异显著。

## 消融与原因判断


### 第 75 条：收益归因看对照

写清固定项和改动项；同时改多项只能比较整套配置。

适用边界：适用：消融、基线比较和组件收益。证据与记录必须如实；不适用的检查注明原因。

**收益归因先看对照**

**教学示例：假设情境，非论文原文**

改后假定已有对应记录；实际改稿须先核对这些事实，不能从改前文字推断或补造。

**改前 · 中文**

换大模型并加入检索后分数提高，所以检索有效。

**Before · English**

Scores improved after we used a larger model and added retrieval, so retrieval is effective.

**改后 · 中文**

先固定模型、数据和预算，只改变是否使用检索，再比较同一测试集的分数。

**After · English**

Keep the model, data, and budget fixed. Vary only the use of retrieval, then compare scores on the same test set.

**逐句拆解**

同时改变多个因素时，不能把全部结果差异归因于其中一个因素。

## 取舍与负结果


### 第 76 条：计划不写成完成

已完成、进行中和未开展分开；“已补实验”必须有实际结果与位置。

适用边界：适用：实验结果、人工审核、复现和 rebuttal。证据与记录必须如实；不适用的检查注明原因。

**计划不写成完成**

**教学示例：假设情境，非论文原文**

改后假定已有对应记录；实际改稿须先核对这些事实，不能从改前文字推断或补造。

**改前 · 中文**

我们已验证跨语言能力。（实验还没做）

**Before · English**

We have verified cross-lingual transfer. [The experiment has not been run.]

**改后 · 中文**

本研究尚未测试跨语言迁移；现有结论限定于已测试的语言。

**After · English**

Cross-lingual transfer has not been tested in this study. Current conclusions are limited to the evaluated languages.

**逐句拆解**

时态和完成状态本身就是事实，不能靠措辞提前完成研究。

## 结果图与案例


### 第 88 条：数据与统计几何一致

点位、长度、面积和坐标对应真实数值。

适用边界：数据、信息边界和完成状态按实际记录说明。

**好看可以调，数据不能调**

**教学示例：假设情境，非论文原文／实测记录**

改后假定已有对应记录；实际改稿须先核对这些事实，不能从改前文字推断或补造。

**逐句拆解**

2 个百分点的差异不能被画成两倍；没有测量的点不能为了曲线顺滑补上。

**教学改写 · English（非论文原文）**

Methods A and B score 62% and 64%. Plot the recorded values with the actual axis scale; if the axis is truncated, make the break explicit. Leave an unmeasured third condition missing.

**教学改写 · 中文（非论文原文）**

方法 A、B 的得分是 62% 和 64%。按记录值和真实刻度画图；截断坐标轴就明确标出断轴。第三个条件没有测量，就保留缺失。

## 来源与开放条件


### 第 96 条：开放内容逐项核实

核对论文版本；代码、图片、数据分别查许可。

适用边界：数据、信息边界和完成状态按实际记录说明。

**引用回到原文，开放情况分开说**

**教学示例：假设情境，非论文原文／实测记录**

改后假定已有对应记录；实际改稿须先核对这些事实，不能从改前文字推断或补造。

**逐句拆解**

部分资源公开就写清部分资源；下载、运行和结果一致要按实际完成状态分别报告。

**教学改写 · English（非论文原文）**

The repository provides plotting code and aggregate figure data. The individual-level dataset requires approved access. We verified the release contents; we have not reproduced the reported experiment.

**教学改写 · 中文（非论文原文）**

仓库提供画图代码和汇总图表数据，个体数据需要审批访问。这里核对了公开包包含的文件，没有据此声称已复现实验。

## 设置、调参与复现


### 第 98 条：代码可搬走运行

资源用相对路径，按入口或配置定位；实际移动并换启动位置验证，密钥和私有配置不发布。

适用边界：数据、信息边界和完成状态按实际记录说明。

**使用相对路径，排除真实密钥**

**教学示例：假设情境，非论文原文／实测记录**

改后假定已有对应记录；实际改稿须先核对这些事实，不能从改前文字推断或补造。

**逐句拆解**

动态定位入口不是硬编码私人路径；配置示例只含字段和占位符，不能含真实凭据。

**教学改写 · English（非论文原文）**

Locate data with Path(__file__).resolve().parent / 'data' / 'examples.json'. Provide a credential-free configuration example. Copy the repository to a path containing spaces and launch it from another working directory to check resource loading.

**教学改写 · 中文（非论文原文）**

用 Path(__file__).resolve().parent / 'data' / 'examples.json' 定位数据，提供不含凭据的配置例子。把仓库复制到含空格的目录，再从另一工作目录启动，实际检查资源读取。

## 全文论证与一致性


### 第 77 条：核对不等于复现

分别说明查稿件、查记录、跑统计还是重跑实验；图表一致不能叫独立复现。

适用边界：适用：复核结论和复现声明。证据与记录必须如实；不适用的检查注明原因。

**表格一致不等于实验复现**

**教学示例：假设情境，非论文原文**

改后假定已有对应记录；实际改稿须先核对这些事实，不能从改前文字推断或补造。

**改前 · 中文**

读过结果表后：我们独立复现了全部实验。

**Before · English**

After checking the result table: We independently reproduced all experiments.

**改后 · 中文**

我们核对了正文与表格的一致性；尚未获得原始记录，因此未独立复现实验。

**After · English**

We checked consistency between the prose and tables. Without the raw records, we have not independently reproduced the experiments.

**逐句拆解**

检查陈述是否一致与重新得到同一实验结果，需要不同证据。

## 最终图表与版本


### 第 99 条：验收状态分开报

编译后检查最终页，核对数值、排版和文字；本地、远端、安装与实验只报实际完成状态。

适用边界：数据、信息边界和完成状态按实际记录说明。

**编译、目检和远端同步分别验收**

**教学示例：假设情境，非论文原文／实测记录**

改后假定已有对应记录；实际改稿须先核对这些事实，不能从改前文字推断或补造。

**逐句拆解**

交付结果和验证结果分开说，不把准备好、暂存好或生成好包装成完成全部流程。

**教学改写 · English（非论文原文）**

The local PDF compiled and the affected pages were inspected. The remote manuscript has not been synchronized. A skill ZIP was created, but that does not mean the skill is installed in the reader's environment.

**教学改写 · 中文（非论文原文）**

本地 PDF 已编译，受影响页面已经检查；远端稿件尚未同步。生成了 skill ZIP，也不代表已经在读者环境中安装。

## 记录与编辑边界


### 第 78 条：实验原件不润色

润色解释文字，不改实际数据、日志、提示词和协议中的原话、数值与设置。

适用边界：适用：语言修改、匿名化建议和公开材料整理。证据与记录必须如实；不适用的检查注明原因。

**润色文字，保留实验原件**

**教学示例：假设情境，非论文原文**

改后假定已有对应记录；实际改稿须先核对这些事实，不能从改前文字推断或补造。

**改前 · 中文**

为了语气统一，把历史模型回复和实验 prompt 一起改写。

**Before · English**

Rewrite historical model responses and experimental prompts to match the paper style.

**改后 · 中文**

只改解释段落；保留原始回复、prompt 和实测记录，在旁边补充准确说明。

**After · English**

Edit the explanatory prose. Preserve the original responses, prompts, and measured records, and add accurate explanations beside them.

**逐句拆解**

原始材料是研究发生过什么的证据，不是可随意润色的叙述。

### 第 97 条：修改不越范围

只读就只摘抄，改配色就保留数据与结构；读当前稿再局部改，不覆盖他人的新修改。

适用边界：数据、信息边界和完成状态按实际记录说明。

**仅修改获准范围，保留他人修改**

**教学示例：假设情境，非论文原文／实测记录**

改后假定已有对应记录；实际改稿须先核对这些事实，不能从改前文字推断或补造。

**逐句拆解**

当前明确授权优先；发现问题和获得修改授权不是同一件事。

**教学改写 · English（非论文原文）**

Requested change: replace the green fill with gray. Change that fill only, preserve node positions and arrows, and report any unrelated text error separately rather than rewriting the figure.

**教学改写 · 中文（非论文原文）**

仅将绿色填充改为灰色，保留节点位置与箭头。其他文字错误单独指出，不扩大修改范围。

## 读准问题，先给答案


### 第 100 条：每个审稿关切有回应

一条意见有几个问题就逐个答；不能仅以“已全部修改”替代逐项回应。

适用边界：模拟审稿问题与回复只用于教学，不是真实审稿记录。补实验、修订和回复格式以当轮官方政策为准；没有完成的事不写成已完成。

**审稿意见拆开，每点都有回应**

**教学示例：假设情境，非论文原文**

改后假定已有对应记录；实际改稿须先核对这些事实，不能从改前文字推断或补造。

**改前 · 中文**

意见包含缺基线、定义不清、速度未知；回复：感谢，均已修改。

**Before · English**

The comment raises missing baselines, an unclear definition, and unknown speed. Response: Thank you; everything is fixed.

**改后 · 中文**

基线比较见表 R1。定义补在第 3 节。速度尚未测试，现有稿件不作加速主张。

**After · English**

Baseline comparisons are in Table R1. The definition is clarified in Section 3. Runtime has not been measured, and the manuscript makes no speedup claim.

**逐句拆解**

每个关切均须回应，并说明证据或无法完成的原因。

## 澄清与分歧


### 第 102 条：回复讨论事实

给理由和证据；不写“显然”“你错了”，也不乱认错。

适用边界：模拟审稿问题与回复只用于教学，不是真实审稿记录。补实验、修订和回复格式以当轮官方政策为准；没有完成的事不写成已完成。

**讨论事实，不评价审稿人**

**教学示例：假设情境，非论文原文**

改后假定已有对应记录；实际改稿须先核对这些事实，不能从改前文字推断或补造。

**改前 · 中文**

审稿人显然没看懂，我们早就做了。

**Before · English**

The reviewer clearly misunderstood; we already did this.

**改后 · 中文**

感谢指出这处说明不清。该比较已列在表 3；我们已在第 4.2 节补充对照条件，方便定位。

**After · English**

Thank you for noting the unclear description. The comparison is in Table 3. We clarified the control conditions in Section 4.2 to make the evidence easier to locate.

**逐句拆解**

回复讨论条件、结果与表述，不评价审稿人的动机或能力。

## 状态与提交


### 第 101 条：回复能定位结果

给图表、章节或结果位置；完成、计划与未解决分开，未完成实验不配虚构结果。

适用边界：模拟审稿问题与回复只用于教学，不是真实审稿记录。补实验、修订和回复格式以当轮官方政策为准；没有完成的事不写成已完成。

**回复给位置，修改给状态**

**教学示例：假设情境，非论文原文**

改后假定已有对应记录；实际改稿须先核对这些事实，不能从改前文字推断或补造。

**改前 · 中文**

我们补了很多实验，效果很好。

**Before · English**

We added many experiments, and the results are excellent.

**改后 · 中文**

我们新增固定预算对比，结果见表 R2；跨领域实验尚未完成，本次回复不报告该项结果。

**After · English**

We added a comparison under a fixed budget; results are in Table R2. The cross-domain experiment is incomplete, and no result from that experiment is reported here.

**逐句拆解**

审稿人应能直接定位回应的依据，并区分证据与承诺。

<a id="quick-start"></a>
## 1. 一天拉完草稿：Codex 快速成型

填入研究问题、方法设计和真实结果，让 Codex 形成初稿。先完成关键图与章节结构，再由作者逐节审核逻辑、精修语言。

本章中英句子均为教学示例，不是论文原句或实测结论；两张论文图另附原文与许可。

### 1.1 填材料，准备模板和本地项目

先填核心贡献与主要发现，再提供对应设计和证据。输入材料须说明各模块的作用与关系。

**材料先给齐**

- **贡献：**写清具体问题、对应设计、已有发现。先说明解决的问题，再给方法名称。

中：针对条件冲突时的约束遗漏，我们在生成计划前核查证据。

EN: To address omitted constraints under conflicting conditions, we check the evidence before generating a plan.

- **方法：**给任务定义、输入、每步操作、输出和实现依据。上一阶段产物交给谁，也写上。

中：输入是任务和可用证据；核查器输出已支持的约束；规划器据此生成计划。

EN: The inputs are a task and available evidence. The checker returns supported constraints, which the planner uses to generate a plan.

- **实验：**附原始结果、指标定义、基线配置、数据划分和重复次数。参考文献附可核对的原文，图附来源。

中：附 results.csv；说明每行对应哪个方法、测试集和运行，以及成功率的分母。

EN: Attach results.csv and identify the method, test set, and run for each row, including the denominator of the success rate.

- **模板与同步：**下载当年的官方模板，查页数，先编译。Overleaf 有 Git 权限就从 Integrations → Git 拉到本地；没有就下载源文件 ZIP。写明允许改哪些文件，同步前先合入合作者的更新。

中：只改 main.tex、sections/ 和 figures/；保留官方模板。先拉最新版本，检查差异再同步。

EN: Edit only main.tex, sections/, and figures/. Preserve the official template, pull the latest version, and inspect the changes before syncing.

教学例：我们研究带约束的规划。已有方法能生成计划，但在条件冲突时容易遗漏约束；我们先核查证据，再生成计划。是否有效，交给同题对照和组件消融检验。

Teaching example: We study planning under constraints. Existing methods generate plans but may omit constraints when conditions conflict. We check the evidence before generating a plan, and test the design with matched comparisons and component ablations.

Fill in the prompt before asking Codex to draft. A venue name alone does not supply a contribution, a method, or evidence.

**复制这个提示词，填空就能用**

```text
读取 paperbank-writing/SKILL.md、references/checklist.md；绘图同时读 paperbank-figures/SKILL.md。先形成初稿，再由我审中文逻辑。本提示词用于实证型 CS 论文，Nature 系列另用独立体系。
会议、当年官方模板、页数与附录规则：【】
问题与依据：【已有做法能做什么，在哪个条件下不足】
一句话贡献：【新对象／设计、对应缺口、与最近工作的区别】
方法：【任务、输入、操作、输出、真实依赖与信号来源】
实验：【数据与划分、指标、基线与预算、真实结果、消融】
参考原文、图片与出处：【】
本地项目与允许改的文件：【】

执行顺序与铁律：
1. 核对官方模板，读取最新文件，先编译；保留并发修改、实验输入与记录，不改其他项目。
2. 先定 mainfig、framework 与关键结果图。mainfig 默认至多 5 环节，突出问题与改动；framework 解释设计为何有效，再讲输入、操作、产物。箭头必须是真依赖，训练、推理、评价分开，输入／输出／评价规则用可解释的边框。
3. 图按最终栏宽绘制。所有图字同一字号，正文减 2 pt 至正文；白底、低饱和、同对象同色，配形状或线型。结果图只读真实数据；同一案例全文只呈现一次。Caption 本条展开简称，写实际发现，尽量三行；图表用 [!t]，核对实际首次引用顺序。
4. 列全部 section、subsection 的标题、任务、承接、图表和篇幅，再填正文。Method Overview 先讲针对困难的关键设计，再写目的、操作与产物；章节名作为位置，每个标题与引用出现一次，后句接前句产物，末句引用 framework。
5. 按 Intro 主张整理实验。Setup 写清数据与划分，按 Metrics、Baselines、Implementation Details 说明指标口径、比较路线和真实设置。Main Results 先给有证据的结论，再讲关键对照与范围；消融固定其他条件，不逐行重复表格数值。
6. 表格用 booktabs，列宽、精度与单位一致。真实可比组内最优加粗浅红，第二个不同显示值下划线浅蓝，并列共享标记；不把排名当显著性。有真实重复才写均值与不确定性，说明次数、SD／SE／CI 和有效子集。不用 resizebox 整体缩放表格。
7. 最后组织 Intro：已有能力→具体不足→对应设计→实际发现→平行贡献。写清真正新增了什么，设计为什么回应不足；不把普通工程步骤包装成创新。不够的证据单列给我，不编结果、引用或 first／unique。
8. 每次给我一节中文提纲与真实证据，确认后再写英文。一句一个完整判断，一段一个任务；定义术语、符号和信号来源，同对象同名称，正文不用 it／they 及同族代词。贡献形容词须有依据，一词换一词，避免重复修饰。超页先删重复，不缩模板字号或间距。交付实际编译与 PDF 检查结果，远端同步单独说明。
语言要求：专业、简洁、直白；不添加调侃、比喻或空泛修饰。
```

**English prompt**

```text
Read paperbank-writing/SKILL.md and references/checklist.md; also read paperbank-figures/SKILL.md for figures. Draft first and let me review the reasoning in Chinese. This prompt targets empirical CS papers; use the independent Nature system for Nature-family journals.
Venue, current official template, page limit, and appendix rules: [ ]
Problem and evidence: [existing capabilities and the condition where they fall short]
Contribution: [new object / design, matched gap, difference from the closest work]
Method: [task, inputs, operations, outputs, actual dependencies, signal sources]
Experiments: [data and splits, metrics, baselines and budgets, actual results, ablations]
Reference passages, figures, and sources: [ ]
Local project and editable files: [ ]

Order and hard rules:
1. Check the official template, read current files, and compile first. Preserve concurrent edits, experimental inputs, and records; stay within the project and scope.
2. Settle the main figure, framework, and key result plots first. Give the main figure at most five stages by default to show the problem and change. Explain why the framework addresses the challenge before its inputs, operations, and products. Arrows must represent real dependencies; separate training, inference, and evaluation and explain border encodings for inputs, outputs, and criteria.
3. Draw at final column width. Use one figure-text size between body size minus 2 pt and body size, white backgrounds, muted consistent colors, and auxiliary shapes or line styles. Plot actual data; present each case once across the paper. Expand abbreviations in each caption, state actual findings, and aim for three lines. Use [!t] and check actual order against first body citations.
4. List every section and subsection with its title, purpose, connection, figures, tables, and space budget before drafting. The Method Overview first explains the design's response to the challenge, then its purpose, operations, and products. Treat section names as locations, cite each title once, connect successive products, and cite the framework last.
5. Organize experiments around Introduction claims. The setup specifies data and splits, Metrics, Baselines, and Implementation Details with actual definitions, comparison groups, and settings. Start Main Results with an evidenced finding, then the key comparison and scope. Hold other conditions fixed in ablations; do not recite tables.
6. Use booktabs and consistent widths, precision, and units. Within genuinely comparable groups, mark the best value in bold on pale red and the second distinct displayed value underlined on pale blue; share markings for ties. Rankings are not significance tests. Report means and uncertainty only for actual repeats, defining counts, SD / SE / CI, and valid subsets. Do not squeeze tables with resizebox.
7. Build the Introduction last: existing capabilities → specific limitation → matched design → actual finding → parallel contributions. State what is new and why each design responds to a limitation. Do not relabel routine engineering as innovation. List evidence gaps separately; invent no results, citations, or first / unique claims.
8. Show one Chinese section outline and its evidence for approval before English prose. Use one complete main judgment per sentence and one task per paragraph. Define terms, notation, and signal sources; name objects consistently and avoid it / they and related object pronouns in author prose. Use evidence-supported contribution modifiers as concise word replacements. Remove repetition before cutting supporting evidence; preserve template fonts and spacing. Report actual compilation and PDF checks separately from remote synchronization.
Language: use professional, concise, direct wording; omit jokes, metaphors, and empty modifiers.
```

依据：cs-paper-writing · paper-writing-clarity · cs-writing-skill · paper-visual-standards · [对应铁律与完整提示词](https://github.com/Da1yuqin/PaperBank/blob/main/skills/paperbank-writing/references/prompts.md#draft)

（Git 同步需要项目 owner 有会员或相应权限。没有就下载源文件 ZIP，在本地编译 LaTeX，或直接 skip 同步这步。可以及时求助有会员的老师或高产师兄师姐，请他们帮忙当 owner。）

[Overleaf: Git integration](https://docs.overleaf.com/integrations-and-add-ons/git-integration-and-github-synchronization/git-integration) · [Overleaf: Downloading a project](https://docs.overleaf.com/managing-projects-and-files/downloading-a-project)

### 1.2 先定图：mainfig、framework 和结果图

[先下载绘图 skill ZIP](../assets/paperbank-figures-skill.zip) · [查看 SKILL.md](../skills/paperbank-figures/SKILL.md) · [绘图铁律](#figure-rules)

先完成框架图与主要实验图，供合作者审核。确认研究价值、设计差异和实验发现后，再精修正文。

#### 1.2.a mainfig：读者先看懂为什么做

- **信息：**用一个具体问题串起现有做法、失败点和本文改动。保留读懂案例所需的输入与输出，通常不超过 5 个环节。

中：任务要求同时满足 A、B；旧计划遗漏 B；本文在生成前核查 B。

EN: The task requires both A and B. The existing plan omits B; our design checks B before generation.

- **取舍：**突出最关键的差别，少放模块、logo 和工程细节。示意趋势标明示意，实测结果给出对应来源。

中：只画“遗漏约束”和“核查后保留约束”的对照，首图不列全部训练参数。

EN: Contrast an omitted constraint with its retention after checking; leave training parameters out of the main figure.

左侧先提出多轮误差问题，中间放大回复细节，右侧对齐训练范围。读序是“哪里出问题 → 改哪一段”，先说明问题与对应改动，再介绍模块。左侧曲线是示意；细节数值与颜色含义要结合原图注读。这里学习信息组织，不照搬原图的字号和配色。

Read from the multi-turn error problem to response details and the compared training ranges. The left curve is schematic; consult the original caption for the numeric blocks and color meanings. This example illustrates information order, not a universal font or palette.

Jiaqi Wang et al., TCOD, arXiv:2604.24005v3, Fig. 1. CC BY 4.0. 从原页裁切；图形与数据未改。 [原论文](https://arxiv.org/abs/2604.24005v3) · [许可](https://creativecommons.org/licenses/by/4.0/)

#### 1.2.b framework：读者看懂怎么做

- **真实流程：**画清每步的输入、操作、输出，箭头连到实际接收者。并行就并行，反馈就反馈；模块名与正文一致。

中：任务与证据进入核查器；核查结果进入规划器；生成的计划再交给评价器。

EN: The task and evidence enter the checker. The checked constraints enter the planner, and the generated plan goes to the evaluator.

- **信息边界：**输入、输出、评价规则分组并区分边框。仅供评价的 rubric 不画进被测模型。用必要案例解释关键操作；同一案例只在论文里完整展示一次。

中：蓝色虚线框是模型可见输入，灰绿实线框是输出；评价器另收冻结的评分规则。

EN: Blue dashed boxes denote model-visible inputs and green-gray solid boxes denote outputs. The evaluator separately receives the frozen scoring criteria.

这张图先分交互生成和策略优化两块：左侧用对话走流程，右侧分结果效用、过程信用和成本信号。大框讲职责，箭头讲数据去向，编号讲步骤。自己的图先写清每个框收到什么、交出什么，再加图标。

The figure separates interaction generation from policy optimization. A dialogue traces the left side; outcome utility, process credit, and cost signals organize the right. Groups explain responsibilities, arrows show information flow, and numbers order the steps.

Ning Gao et al., Reinforcing Real-world Service Agents, arXiv:2602.22697v1, Fig. 1. CC BY 4.0. 从原页裁切；图形与数据未改。 [原论文](https://arxiv.org/abs/2602.22697v1) · [许可](https://creativecommons.org/licenses/by/4.0/)

#### 1.2.c 绘图铁律

- **配色：**白底，面板接近白色，文字和刻度保持深色。同对象全篇同色，再配点形、线型或纹理；低饱和配色仍须保持文字、标记与背景的清晰对比。

中：基线用灰色圆点，本文方法用灰蓝菱形；颜色变淡，文字不跟着变淡。

EN: Use gray circles for the baseline and muted blue diamonds for the proposed method. Keep the text dark on pale backgrounds.

- **字号与字体：**按最终栏宽起稿，图内所有字同字号、同字体家族；范围为正文减 2 pt 至正文，标题、轴、图例、注释都算。以论文 PDF 的实测字号为准，放不下先重排，不通过缩小字号解决空间不足。

中：正文实际为 10 pt，图内字用 8–10 pt；在论文整页大小下读，不只看放大的 PNG。

EN: With 10 pt body text, use 8–10 pt figure text and inspect it at its final size in the paper, not only in a magnified PNG.

- **布局：**一个主读序，同层成组并命名；并行先汇合，反馈另走清楚的路径。通栏约 16:9、单栏约 4:3 布局，附录可纵排。连图注一起查占高，不进行非等比缩放、不改论文模板。

中：两个并行输入先汇合再进入模型；长解释移到图注，关键输入保留在图里。

EN: Merge parallel inputs before the model. Move long explanations to the caption while retaining the essential inputs in the figure.

- **结果图：**从真实数据绘制。轴写变量和单位，图例解释颜色与线型，误差条写 SD、SE 或 CI 及计算单位；同类图共用尺度。

中：纵轴写成功率（%）；误差条若是跨运行标准差，不能标作 95% 置信区间。

EN: Label the y-axis as success rate (%). If error bars show standard deviations across runs, do not label them as 95% confidence intervals.

- **图注：**短句说明图在回答什么、怎么读、结果支持什么。简称给全称；必要的分母、范围、误差含义保留。方法图讲机制，结果图才讲实测发现。

中：该图比较同一测试集上的成功率与推理成本；点表示方法配置。

EN: The figure compares success rate and inference cost on the same test set; each point represents a method configuration.

- **箭头与信息边界：**每条箭头对应真实产物和接收者，避免穿过文字、交叉或错误连接。输入、输出、评价规则用三种边框；只供评价的 rubric 不接到模型。

中：核查结果交给规划器；评分规则只交给评价器。

EN: Checked constraints go to the planner; scoring criteria go only to the evaluator.

- **标签与图标：**缩写、符号、颜色、边框和图标就近解释。图标旁标明对象名，明确角色与模块。

中：机器人标为 Planner；虚线箭头注明 Feedback。

EN: Label the robot as Planner and dashed arrows as Feedback.

- **案例：**保留必要背景、关键请求、证据和输出，注明实测或作者示例。同一来源的案例只完整展示一次，改名、翻译或裁剪也算同一个。

中：图 1 展示案例，第 4 节回引图 1。

EN: Present the case in Figure 1 and refer back to it in Section 4.

- **PDF 导出：**统计图导出矢量 PDF；生成底图的标签另排原生、可见、可选文字。将截图封装为 PDF 仍是位图；隐藏 OCR 层不能替代可见的原生文字。

中：实际选中图内标签，核对字体和缩放后的字号。

EN: Select the labels in the manuscript PDF and verify their font and final size.

- **改图范围：**只改颜色就保留文字、布局、照片、公式、字号和连线。保留原始数据、实验和合作者的图。

中：只换底色，保留坐标与箭头端点。

EN: Change only the fills; retain all coordinates and arrow endpoints.

- **最终验收：**编译后在正常阅读大小查字号、碰撞、裁切、图注和首次引用顺序。CS 默认 [!t]；源码顺序对了，还要看实际 PDF。

中：图 1 先引用，就检查它是否真的先出现在 PDF。

EN: If Figure 1 is cited first, verify that it actually appears first in the PDF.

**给 Codex 的绘图说明单**

```text
读取 paperbank-figures/SKILL.md 和 references/rules.md。按以下材料画图。
图型：【mainfig／framework／统计图／案例图】
要突出的问题与贡献：【对应 Intro 的哪项困难，方法改了什么，依据在哪里】
材料：【稿件、真实数据、参考图与出处、已有案例及使用位置】
真实结构：【输入、操作、输出、接收者；并行、汇合、反馈；训练／推理／评价】
允许修改：【文件与范围】；最终插入宽度：【mm】
正文 PDF 实测字体与字号：【字体，pt】；本篇已确认色板：【】

铁律：
1. mainfig 讲问题、已有缺口与关键改动，默认不超过 5 个环节；framework 先让人看懂设计为什么好，再画完整输入、操作与产物。两图分别承担不同叙述任务。
2. 每条箭头对应真实依赖，不穿文字。保留并行与反馈；训练、推理、评价分开。输入、输出、评价规则用三种边框并给图例；仅供评价的信息不能画成模型输入。
3. 按最终宽度起稿。所有标题、坐标、刻度、图例、数字、注释用同一字号，正文减 2 pt ≤ 图字 ≤ 正文，字体家族匹配。放不下就重排或拆图，不缩小规定字号、不进行非等比缩放、不修改论文模板。
4. 白底、近白面板、深色文字、低饱和配色。同一对象全篇同色，用形状或线型辅助区分；不加渐变、阴影和装饰光效。通栏先参考 16:9，单栏参考 4:3，内容与可读性优先。
5. 模块名与正文一致。缩写、变量、单位、图标、颜色和线型都能解释；图标旁写对象名。标签用自然语言，不用符号拼句。
6. 同一案例全文只呈现一次，翻译、裁剪或改名仍算同一个。先按来源核对使用位置，其他位置交叉引用。对话一轮一框；作者示例与实测回复分清，没有评分不画勾。
7. 统计图用 Python 等专业工具读取所附数据，保留数值、坐标几何、分母、单位与 SD／SE／CI 定义；同类比较统一尺度。不为美观补缺测、改数据或平滑曲线，不重跑实验；KDE 等估计图说明样本量、方法和带宽。概念图按当前环境使用 imagegen，生成内容须依据已确认流程，不生成虚构结果。
8. Caption 说明读法、比较、必要口径与实际发现，简称在本条 Caption 写全称。方法图说明机制，不编实验结论。尽量三行，必要定义与事实边界优先。
9. PDF 文字可见、可选，字体嵌入；不叠两套字形或隐藏 OCR。统计图优先矢量 PDF，含位图的 PDF 不称全矢量。CS 图表默认 [!t]，实际位置跟随正文首次引用，保留附录归属。
10. 先给问题、布局和缺口，再绘制。插回论文编译，看最终页面的字号、图例、裁切、碰撞和引用顺序。交付源文件、PDF、预览及实际检查结果。只改色时保留原布局、文字、连线与图片；保留他人修改，不扩大范围。
```

**English prompt**

```text
Read paperbank-figures/SKILL.md and references/rules.md. Draw from these materials.
Type: [main figure / framework / quantitative chart / case]
Problem and contribution: [Introduction challenge, actual design change, evidence]
Materials: [manuscript, original data, references and sources, cases and their existing locations]
Actual structure: [inputs, operations, outputs, recipients; parallel paths, merges, feedback; training / inference / evaluation]
Editable files and scope: [ ]; final insertion width: [mm]
Font family and body size measured in the manuscript PDF: [family, pt]; approved palette: [ ]

Hard rules:
1. The main figure shows the problem, existing gap, and key change, with at most five stages by default. The framework explains why the design addresses the challenge before showing inputs, operations, and products. Give the two figures distinct jobs.
2. Every arrow represents an actual dependency and avoids text. Preserve parallel paths and feedback; separate training, inference, and evaluation. Use three explained border encodings for inputs, outputs, and evaluation criteria. Evaluation-only information must not appear as model input.
3. Design at the final width. Use one size for titles, axes, ticks, legends, numbers, and annotations: body size minus 2 pt ≤ figure text ≤ body size, with a matching font family. Rearrange or split crowded content; do not shrink text, distort geometry, or change the paper template.
4. Use a white canvas, near-white panels, dark text, and muted colors. Keep each object's color consistent throughout the paper; add shapes or line styles. Avoid gradients, shadows, and decorative glow. Start near 16:9 for full-width figures and 4:3 for single-column figures; prioritize content and readability.
5. Match module names to the body. Explain abbreviations, variables, units, icons, colors, and line styles; label icons with object names. Use natural-language labels rather than symbol-packed prose.
6. Present each source case only once across the paper. Translations, crops, and renamed versions still count as the same case. Check existing locations by source and cross-reference elsewhere. Use one frame per dialogue turn. Distinguish author examples from measured outputs; do not show unrecorded check marks.
7. Use Python or equivalent professional plotting tools for supplied quantitative data. Preserve values, coordinate geometry, denominators, units, and SD / SE / CI definitions; use common scales for comparable plots. Do not fill missing measurements, alter data, or smooth curves for appearance, and do not rerun experiments. For KDE and other estimated plots, specify sample counts, methods, and bandwidth where applicable. Use imagegen for conceptual figures in the current environment; do not let a generator invent dependencies or results.
8. Captions explain reading, comparisons, necessary scope, and actual findings. Expand abbreviations in each caption. Method figures explain mechanisms without fabricated experimental conclusions. Aim for three final lines; necessary definitions and factual limits take priority.
9. Use visible, selectable PDF text and embedded fonts; avoid duplicate lettering and hidden OCR. Prefer vector PDF for statistical plots; a PDF containing raster images is not fully vector. Use [!t] for CS figures and tables by default. Verify actual order against first body citations and retain appendix ownership.
10. Propose the question, layout, and evidence gaps before drawing. Insert the figure into the paper, compile, and inspect final-size text, legends, crops, collisions, and citation order. Deliver sources, PDF, preview, and completed checks. A color-only edit preserves layout, text, edges, and images. Preserve concurrent edits and the authorized scope.
```

依据：paper-visual-standards · academic-plotting · clean-flow-figures · [对应铁律与完整提示词](https://github.com/Da1yuqin/PaperBank/blob/main/skills/paperbank-figures/references/prompts.md#figures)

教学例：mainfig 用一个约束冲突说明动机；framework 用另一个案例走完证据核查与计划生成；结果图比较同一批任务的成功率和成本。

Teaching example: The main figure motivates the work with a constraint conflict. The framework traces evidence checking and plan generation on a different case. Result plots compare success and cost on the same tasks.

Review the figures with coauthors before polishing the body. They should explain the motivation, the method, and the findings. Styling cannot repair an unclear workflow.

### 1.3 整理章节、实验和表格

“要做到光看章节名称能看懂你的论文” 同一级的信息放一起，下一节接上一节的产物。章节标题应对应研究任务与步骤，不能直接复制代码目录。

#### 1.3.a 章节顺序与承接

- **先列职责：**列全部 section 标题、每节目的、所需图表和预计篇幅。Related Work 按主题归类；Method 按真实处理依赖；Experiments 按要检验的问题。

中：Related Work 的“约束规划”小节归纳已有能力，再落到 Intro 中的约束遗漏。

EN: A Related Work subsection on constrained planning summarizes existing capabilities, then returns to the omission problem stated in the Introduction.

- **Method overview：**开头承接 Intro 的困难，串起输入、操作、输出和对应小节；最后引用 framework。章节名用于定位内容，不能作为执行模块。

中：为减少约束遗漏，我们先检索证据（证据检索节），再用检索结果核查约束（约束核查节），最后据此生成计划（计划生成节）。

EN: To reduce omitted constraints, we first retrieve evidence (Evidence Retrieval), use it to check constraints (Constraint Checking), and generate a plan from the checked constraints (Plan Generation).

- **篇幅：**按页数和贡献分配正文。同级小节任务量相近，篇幅也应接近；明显长的一节先查职责混杂和重复。复现细节放附录，关键比较条件留正文。超页先删重复文献配文和常规实现，保留支撑核心贡献的实验分析。

中：Method 某节讲了核查、训练和评估三件事，先拆职责，不靠缩字号解决。

EN: If a Method subsection mixes checking, training, and evaluation, separate its responsibilities instead of shrinking the font.

**正文结构模板与 overview 句式**

```latex
\section{Introduction}
\section{Related Work}
\subsection{[Theme linked to challenge A]}
\subsection{[Theme linked to challenge B]}
\section{Method}
To address [the specific challenge], we [key design and why it
addresses the challenge].
To [first purpose], in [First Section] (\S\ref{sec:first}),
we [operation], producing [output].
Using [that output], in [Second Section] (\S\ref{sec:second}),
we [next operation], producing [next output].
Figure~\ref{fig:framework} summarizes the workflow.
\subsection{[First Section]}\label{sec:first}
\subsection{[Second Section]}\label{sec:second}
\section{Experiments}
\subsection{Experimental Setup}
\subsection{Main Results}
\subsection{Ablation Studies}
\subsection{[Analysis of the remaining research question]}
\section{Conclusion}
```

这是章节结构模板，按实际工作增删小节。方括号全部换成真实内容；framework 标签须对应实际图片。

#### 1.3.b 实验先整理成论证

- **问题与证据：**每项主张对应一个要检验的问题，再选对照、数据和图表。RQ 按研究需要设置，不要求每个实验标题使用疑问句。

中：主张“核查减少遗漏”，就比较同题、有核查与无核查的遗漏率，保持其他设置一致。

EN: To test whether checking reduces omissions, compare omission rates with and without checking on the same tasks under otherwise matched settings.

- **实验设置：**先说明数据与划分，再分别写 Metrics、Baselines 和 Implementation Details。指标给定义、方向和分母；基线给来源与配置；训练、推理预算和重复次数讲清。

中：成功率是满足全部任务约束的计划比例；基线与本文方法用同一测试集，分别说明推理预算。

EN: Success rate is the fraction of plans satisfying all task constraints. Evaluate the baseline and proposed method on the same test set and report their inference budgets.

- **实验顺序：**主结果回答整体是否有效；消融回答哪项设计有用；再按贡献安排成本、稳健性、迁移或失败分析。实验须对应具体主张，不要求每篇论文包含所有分析类型。

中：若声称更省计算，就同时报告成功率和成本；若只验证同域效果，就不写跨域泛化。

EN: A computational-efficiency claim requires both success and cost measurements. In-domain evidence alone does not establish cross-domain generalization.

- **结果段：**一句结论开头，接关键对照，再解释含义和范围。不逐行重复表格数值；均值更高也不自动等于显著提升。

中：核查后的提升主要出现在冲突条件下。接着引用该分组的对照，解释它怎样回应 Intro 的遗漏问题。

EN: The gains after checking are concentrated in conflicting conditions. Cite the subgroup comparison, then explain how it addresses the omission problem in the Introduction.

**给 Codex 的实验整理提示词**

```text
读取 paperbank-writing/SKILL.md 的 Experiments 与图表规则。
材料：【Intro 主张、真实结果文件、数据划分、基线配置、预算、重复记录】
允许修改：【实验正文、表格及相关文件】；不得改动：【原始结果与实验协议】

1. 按“Intro 主张／研究问题→比较对象与固定条件→指标→图表→能支持的结论”整理。RQ 有需要再用，不要求每张图单独设置 RQ。
2. 先写 Experimental Setup：数据来源与划分；Metrics 定义方向、分母、聚合；Baselines 按路线分组，注明来源与版本；Implementation Details 写真实训练／推理预算、硬件、超参数和重复次数。没有记录就列缺口，不猜默认值。
3. 再排 Main Results、Ablation Studies 与必要分析。每段首句给有证据的结论，随后讲关键对照、条件和范围；一个独立发现一段，不逐行重复数值。消融只改待检因素，保留其他条件，未排除的解释不能写成因果。
4. 表格用 booktabs；同类表统一列宽、组名、精度和单位。最优加粗浅红，第二个不同显示值下划线浅蓝，并列共享标记，限真实可比组。均值与不确定性同行，整段 ± 及误差可上标；写清真实重复次数、SD／SE／CI 和共同有效子集，不用排名替代显著性，不用 resizebox 缩整表。
5. Caption 写比较、实际发现与必要口径，每条展开简称，尽量三行。图表用 [!t]，核对最终首次引用顺序。百分比与百分点、记录与独立样本、整体与子集分开，保留影响结论的负结果。
6. 先给中文逻辑让我审，再写英文；只根据所附记录绘图制表，不补结果、重跑基线或改统计口径。编译检查实际页数、数值、标记、字体和溢出，报告证据缺口与已做检查。
```

**English prompt**

```text
Read the Experiments and figure/table rules in paperbank-writing/SKILL.md.
Materials: [Introduction claims, actual result files, data splits, baseline configurations, budgets, repeat records]
Editable files: [experiment prose, tables, related files]; preserve: [original results and protocols]

1. Map each Introduction claim or research question to comparison objects, fixed conditions, metrics, figures/tables, and supported conclusions. Use RQs when needed, without inventing one per plot.
2. Write Experimental Setup first: data sources and splits; Metrics with direction, denominators, and aggregation; Baselines grouped by approach with sources and versions; Implementation Details with actual training/inference budgets, hardware, hyperparameters, and repeat counts. List missing records rather than guessing defaults.
3. Organize Main Results, Ablation Studies, and necessary analyses. Start each paragraph with an evidenced finding, then key comparisons, conditions, and scope. Give each independent finding its own paragraph; do not recite rows. Change only the tested factor in an ablation, hold other conditions fixed, and avoid causal claims when alternatives remain.
4. Use booktabs and consistent widths, group names, precision, and units. Within comparable groups, mark the best value in bold on pale red and the second distinct displayed value underlined on pale blue, sharing marks for ties. Keep means and uncertainty on one line; the entire ± and error may be superscripted. Define actual repeat counts, SD / SE / CI, and common valid subsets. Rankings do not establish significance; do not scale whole tables with resizebox.
5. Captions state comparisons, actual findings, and necessary scope; expand abbreviations in each caption and aim for three lines. Use [!t] and verify actual order against first citations. Distinguish percentages from percentage points, records from independent samples, and full sets from subsets. Retain negative results that affect conclusions.
6. Show Chinese reasoning for approval before English. Use supplied records only; do not fabricate results, rerun baselines, or change aggregation. Compile and inspect pages, numbers, markings, fonts, and overflow; report evidence gaps and completed checks.
```

依据：cs-paper-writing · paper-writing-clarity · paper-visual-standards · [对应铁律与完整提示词](https://github.com/Da1yuqin/PaperBank/blob/main/skills/paperbank-writing/references/prompts.md#experiments)

#### 1.3.c 表格：先让人看清比较

- **结构：**表承载实测结果和数据。模型按实际类型分组；列写指标、单位与好坏方向。三线表，少网格，同一指标保持精度一致。

中：方法名一列，成功率（%）一列，延迟（ms）一列；不同测试集分组，不混算平均。

EN: Use columns for method, success rate (%), and latency (ms). Separate test sets into groups rather than averaging incompatible results.

- **标记：**可比组内逐列判断：最优加粗，次优加下划线；需要时用很浅的底色。性能和成本方向不同，并列共享标记。颜色标记不能证明统计显著性。

中：成功率越高越好，延迟越低越好；两列分别找最优，不把本文整行全部涂红。

EN: Higher success and lower latency are better. Mark each column independently rather than highlighting the entire proposed-method row.

- **统计与排版：**均值与不确定性放同一行，表注写清重复次数及 SD、SE 或 CI。缺失用破折号并解释；长表先拆列或跨栏，不整表 resizebox。

中：70.0 上标 ±2.0 表示均值及标准差；“—”表示未测，不是 0。

EN: A mean of 70.0 with superscript ±2.0 denotes a mean and standard deviation. A dash denotes an unmeasured value, not zero.

排版示例：以下数值均为假设，不是论文结果。上标演示均值旁的标准差；浅红为最优，浅蓝为次优。

| Method | Success (%) ↑ | Latency (ms) ↓ |
| --- | --- | --- |
| Baseline A | 70.0 ±2.0 | 120 ±4 |
| Baseline B | 73.0 ±1.0 | 130 ±4 |
| Proposed method | 76.0 ±1.0 | 125 ±3 |

**可复制的 LaTeX 表格模板**

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

包声明放导言区，table 环境放正文；先确认会议模板允许这些包。正式表替换真实数据，并在表注写清统计单位、重复次数、实际可比范围及主要发现。跨栏时用 table*，不改模板栏宽。

教学例：Intro 提出约束遗漏；Method 解释核查器如何保留约束；主实验比成功率，消融检验核查器，失败分析说明哪些约束仍会漏。

Teaching example: The Introduction identifies omitted constraints. The Method explains how the checker retains them. Main results compare success, ablations test the checker, and failure analysis identifies remaining omissions.

Once the figures are settled, define the body outline. Each section has a purpose: motivation, prior work, the method, or evidence. Organize the argument before filling paragraphs.

### 1.4 理顺 Intro，中文审核后填正文

先用中文说明现有问题、对应改进及作用机制，审核通过后再组织英文。

#### 1.4.a Intro 先按这条线排

- **第一段：背景与已有能力：**第一句进入研究方向，紧接实际价值，再概括现有路线及已做到的事。删除与具体研究问题无关的泛化背景。

中：约束规划将任务要求转成可执行计划。现有方法能生成候选方案，并通过搜索或反馈改进。

EN: Constrained planning turns task requirements into executable plans. Existing methods generate candidates and refine them through search or feedback.

- **第二段：具体问题：**说在哪种条件下、哪个对象出了什么问题，为什么已有做法还不够。用文献或动机实验支撑，准确说明已有工作的能力与适用条件。

中：然而，在要求彼此冲突时，计划仍可能遗漏关键约束，使后续步骤不可执行。

EN: However, under conflicting requirements, plans may still omit critical constraints, leaving later steps infeasible.

- **第三段：对应设计：**逐个回应上一段的问题。用“为解决 X，我们做 Y，因此得到 Z”串起来；关键术语就近解释，不要只报模块名。

中：为减少遗漏，我们在规划前核查每项约束的证据，并把已核实的约束交给规划器。

EN: To reduce omissions, we check the evidence for each constraint before planning and pass the verified constraints to the planner.

- **接着：主要发现：**设计后紧接关键实验发现：和谁比、在什么条件下、支持哪项贡献。只写真实结果，实验数量不能替代具体发现。

中：若实际结果支持：在相同测试任务下，核查减少了约束遗漏；消融说明这项收益来自核查环节。

EN: If supported by the actual results: On the same test tasks, checking reduces constraint omissions; the ablation attributes this gain to the checking step.

- **最后：贡献列表：**首项概括解决的核心问题，随后分别写关键设计与主要发现。每项说明一个独立贡献，避免重复列举流程。 按真实贡献增删，长度接近。

中：我们设计一个规划前证据核查步骤，在生成前识别缺少支持的约束。

EN: We design a pre-planning evidence check that identifies unsupported constraints before generation.

**Intro 中文提纲提示词**

```text
读取 paperbank-writing/SKILL.md 的 Introduction 规则与模板。
材料：【问题依据、最近工作、真实设计、已验证结果与范围】
任务：先写中文提纲；允许修改：【文件与范围】。

1. 先写“具体不足→对应设计→实际证据”映射，缺证据单列，不补造。
2. 背景段：说清研究方向与价值，紧接已有路线怎么做、已经能做什么。用必要原文引用，删除与具体问题无关的泛化背景。
3. 问题段：指出哪个条件下，已有做法不能证明或处理什么，并给依据。每个问题须有后文设计回应，不把已有能力写成没人做过。
4. 方案段：明确本文新增的对象或设计，与最近工作区别在哪里；先解释为什么针对该困难，再写输入、操作、产物。解释设计机制，不能仅列模块名称与步骤。
5. 发现段：只写实际主要发现、关键比较和适用范围。没有结果不写结果句，诊断不冒充因果，有限测试不推广全部场景。
6. 贡献用原生 itemize，平行、简短、长度相近，项数按真实工作调整。一项一个主要贡献，常规实现不单独列为创新。de-identified、expert-confirmed、tailored 等词须有对应事实，一词换一词，不使用空泛评价；不用无依据的 first／unique。
7. 逐句查前句是否提供后句的对象或前提，问题、机制与实验名称是否一致。定义必要术语，用具体对象替代 it／they；段落数量服从实际论证。先让我审中文，再组织英文。研究事实有实质调整才同步改摘要，保留原始结果、引文和并发修改。
```

**English prompt**

```text
Read the Introduction rules and templates in paperbank-writing/SKILL.md.
Materials: [problem evidence, closest work, actual designs, verified findings and scope]
Task: write a Chinese outline first; editable files and scope: [ ].

1. Map specific limitations to matched designs and actual evidence. List gaps separately without inventing support.
2. Background: explain the field and its value, then how existing approaches work and what they already achieve. Cite necessary original sources; skip generic technological-progress openings.
3. Problems: identify the condition where an existing approach cannot handle or establish something, with evidence. Match every problem to a later design; acknowledge existing capabilities.
4. Response: state the new object or design and its difference from the closest work. Explain why the design addresses the limitation before inputs, operations, and products. A module list or pipeline alone is insufficient.
5. Findings: report actual main findings, key comparisons, and scope only. Omit result sentences without results. Distinguish diagnosis from causality and bounded tests from universal claims.
6. Use native itemize for parallel, concise contributions of similar length; let the actual work determine the count. Give each item one main contribution; routine implementation is not novelty. Use de-identified, expert-confirmed, tailored, or similar modifiers only when supported, as concise word replacements. Avoid unsupported first / unique claims.
7. Check that each sentence supplies the next sentence's object or premise and that problem, mechanism, and experiment names agree. Define necessary terms and replace it / they with concrete objects. Adapt paragraph count to the argument. Let me review Chinese before English; update the Abstract only when research facts materially change. Preserve original results, citations, and concurrent edits.
```

依据：cs-paper-writing · paper-writing-clarity · cs-writing-skill · [对应铁律与完整提示词](https://github.com/Da1yuqin/PaperBank/blob/main/skills/paperbank-writing/references/prompts.md#intro)

#### 1.4.b 人工审核，再填全文

- **审顺序：**每次给你一节中文，先查问题有没有回答、操作能不能复现、证据够不够。定下全部 section 标题后，再组织英文写回去。

中：先看 Method 的中文流程；确认核查输出确实进入规划器，再润色英语。

EN: Review the Method workflow in Chinese first. Confirm that the checked constraints actually enter the planner before polishing the English.

- **审一致：**Intro 的问题、Related Work 的不足、Method 的设计、实验的结论用同一套对象和名称。摘要概括同一组问题、设计与发现。

中：全文都说“约束遗漏”；不要到实验突然换成“综合智能不足”。

EN: Use “constraint omission” consistently instead of switching to an unrelated “lack of general intelligence” claim in the experiments.

- **审篇幅与图表：**编译看真实页数、图字、表格溢出和首次引用顺序。超页先删重复和无关细节，保留比较条件；逐句精修再去第三章。

中：结果段重复了整张成绩表，就删逐行报分，保留关键差异及其含义。

EN: If the result paragraph repeats the entire score table, remove the row-by-row narration and retain the key difference and its meaning.

教学例：计划要同时满足多个条件；已有方法能生成计划，但冲突条件下会遗漏约束；因此先核查证据，再规划；随后用主结果与消融检验这项设计。

Teaching example: Plans must satisfy multiple conditions. Existing methods generate plans but can omit constraints when conditions conflict. We therefore check evidence before planning, and test this design with main comparisons and ablations.

The Introduction compresses the argument of the paper. Make the problem, design, and evidence clear in Chinese before drafting the English.

## 全文表达要求与中英改写

全文围绕核心贡献组织：现有问题是什么，本文新增什么，为什么这样设计，证据支持什么。先明确论证，再精修语言。

#### 先说为什么值得做

每项设计都要回答：已有做法在哪种条件下不足，本文改了什么，为什么有用，哪项证据支持。

教学改写：假设已有对应设计或比较，非论文原文与实测结果。

通用表达要求

**改前**

We combine retrieval, verification, and revision.

我们组合检索、验证和修改。

**改后**

To check whether retrieved evidence actually supports an answer, we verify each claim before revision.

为检查检索证据是否真正支持回答，我们在修改前逐条验证断言。

**第 1 句：**相同几个模块，现在说出了具体困难、设计目的和改动位置。实际效果另给对照证据。

#### 用具体操作替代空泛评价

用具体操作替换 powerful、comprehensive 等空评价。

教学改写：假设已有对应设计或比较，非论文原文与实测结果。

通用表达要求

**改前**

Our method is powerful, comprehensive, and highly innovative.

我们的方法强大、全面，而且高度创新。

**改后**

The method links source quotes to constraints from earlier dialogue turns.

该方法将来源摘句与前文对话约束关联。

**第 1 句：**具体操作直接告诉读者改了什么。

#### 短句，完整动作

长句按步骤拆，后句接前句产物；主语、动作和条件写全。

教学改写：假设已有对应设计或比较，非论文原文与实测结果。

PaperBank 短句偏好；实际行长按最终 PDF 检查

**改前**

The retriever selects relevant passages, which are organized into notes that are subsequently supplied to the generator so that the generator can produce cited answers.

检索器选出相关片段，片段被组织成笔记，随后提供给生成器，以便生成器产生带引用的回答。

**改后**

The retriever selects relevant passages.

检索器选出相关片段。

**第 1 句：**第一步：对象和动作明确。

We organize these passages into evidence notes.

我们将这些片段组织成证据笔记。

**第 2 句：**these passages 指向上一句的具体产物。

The generator uses the notes to produce an answer with citations.

生成器使用这些笔记，产生带引用的回答。

**第 3 句：**随后说明笔记如何用于生成最终输出。

#### 正文写完整句子

加号、箭头不能代替文字关系；公式、代码和图中照常使用。

教学改写：假设已有对应设计或比较，非论文原文与实测结果。

通用表达要求

**改前**

Notes + constraints → better answers.

笔记＋约束→更好的回答。

**改后**

The notes retain earlier constraints.

笔记保留前文约束。

**第 1 句：**先写实际处理。

We test whether retaining these constraints improves citation support.

我们检验保留这些约束是否提高引用支持率。

**第 2 句：**把想验证的作用写成问题，不能让箭头替你证明因果。

#### 术语首次解释

写清对象和用途，不让读者到后文找定义。

教学改写：假设已有对应设计或比较，非论文原文与实测结果。

通用表达要求

**改前**

We construct evidence notes.

我们构建证据笔记。

**改后**

We construct evidence notes that link source quotes to active dialogue constraints.

我们构建证据笔记，用于将来源摘句与仍需满足的对话约束关联。

**第 1 句：**读完这一句就知道笔记里面是什么、为什么要构建。

#### 符号首次定义

写对象、来源、算法、用途和下标；不用的符号删掉。

教学改写：假设已有对应设计或比较，非论文原文与实测结果。

通用表达要求

**改前**

We use r to update the model.

我们用 r 更新模型。

**改后**

For question q, r_q is the citation-support score of the generated answer.

对问题 q，r_q 是生成回答的引用支持得分。

**第 1 句：**交代哪个样本、哪个产物、什么指标。

We use this score as the terminal reward for the sampled answer.

我们将该得分用作这条采样回答的终端奖励。

**第 2 句：**说明信号在哪个阶段作用于哪个对象；真实算法另有条件时补上。

#### 同一对象同一称呼

同一对象同一名称；正文不用 it／they 及同族代词，换成简短对象名。

教学改写：假设已有对应设计或比较，非论文原文与实测结果。

本套 CS 写作约定：we／our、this case 等带明确名词的结构可保留；原始提示词、模型回复和直接引用不因润色改写。

**改前**

The retriever returns passages and notes. The generator uses them.

检索器返回片段和笔记。生成器使用它们。

**改后**

The retriever returns passages and evidence notes.

检索器返回片段和证据笔记。

**第 1 句：**先列清两种不同产物。

The generator uses the evidence notes.

生成器使用证据笔记。

**第 2 句：**读者不必猜到底是片段、笔记还是两者。

#### 贡献词有事实依据

tailored、expert-confirmed、de-identified 能突出真实贡献。有依据就用，一词换一词，避免重复或无依据的形容词。

教学改写：假设已有对应设计或比较，非论文原文与实测结果。

PaperBank 贡献措辞偏好；示例词不是跨论文固定词库

**改前**

We use personalized prompts for each role.

我们为每个角色使用个性化提示词。

**改后**

We use tailored prompts for each role.

我们为每个角色使用专门设计的提示词。

**第 1 句：**如果提示词确实针对角色设计，tailored 简短而直接；没有更好词时保留原词。

#### 发现可取短名

短名后立即解释具体发现；优先四个英文词以内。

教学改写：假设已有对应设计或比较，非论文原文与实测结果。

PaperBank 命名与粗斜体偏好；标签须对应真实发现

**改前**

We identify a Citation Support Gap.

我们发现引用支持差距。

**改后**

We identify a Citation Support Gap.

我们发现引用支持差距。

**第 1 句：**教学名称；确实有该比较才可作为发现，首次可用粗斜体强调。

Answers cite sources, but some answer claims are unsupported by those sources.

回答虽然列出来源，部分断言却得不到这些来源支持。

**第 2 句：**立即说明差距的两端，不把缺乏支持误写成真实断言必然为假。

#### 句子之间有逻辑关系

后句处理前句的问题或产物，Then 和 Therefore 须符合实际关系。

教学改写：假设已有对应设计或比较，非论文原文与实测结果。

通用表达要求

**改前**

Retrieved passages are relevant. Therefore, we use evidence notes.

检索片段具有相关性。因此，我们使用证据笔记。

**改后**

Relevant passages may conflict with constraints stated in earlier turns.

相关片段仍可能与前文提出的约束冲突。

**第 1 句：**前一句产生实际未解决的问题。

We therefore link each evidence note to the relevant active constraints.

因此，我们将每条证据笔记与相关的有效约束关联。

**第 2 句：**方案须能处理上述约束冲突，Therefore 才有成立前提。

#### 连接词用对

转折用 However，有因果依据才用 Therefore；并列直接写。

教学改写：假设已有对应设计或比较，非论文原文与实测结果。

通用表达要求

**改前**

Both systems use the same model. However, both systems use the same evidence-context budget.

两套系统使用同一模型。然而，它们使用同一证据上下文预算。

**改后**

Both systems use the same model and evidence-context budget.

两套系统使用相同的模型与证据上下文预算。

**第 1 句：**两个共同条件可以直接并列，However 在这里没有转折。

#### 章节按流程衔接

开头说明输入，结尾说明输出及其在下一步的用途。

教学改写：假设已有对应设计或比较，非论文原文与实测结果。

通用表达要求

**改前**

Next, we introduce the next module.

接下来，我们介绍下一个模块。

**改后**

We next organize the selected source quotes into evidence notes.

接下来，我们将已筛选的来源摘句组织成证据笔记。

**第 1 句：**读者知道下一步针对什么、将产生什么。

#### 问题、设计、实验对应

引言提出的问题，方法处理，实验检验。

教学改写：假设已有对应设计或比较，非论文原文与实测结果。

通用表达要求

**改前**

The problem is missing evidence. The method reformats answers. The experiment reports runtime.

问题是缺少证据。方法调整回答格式。实验只报告运行时间。

**改后**

The problem is incomplete coverage of supporting evidence.

问题是支持证据覆盖不完整。

**第 1 句：**困难落到可检验的性质。

The method expands the set of relevant evidence segments.

方法扩大相关证据片段的覆盖。

**第 2 句：**设计直接处理该困难。

The experiment evaluates evidence recall and citation support, together with inference cost.

实验评价证据召回与引用支持，同时报告推理成本。

**第 3 句：**效果与代价共同回应贡献。

#### 保留结论条件

任务、模型、范围和分母写清；有限测试不推广所有场景。

教学改写：假设已有对应设计或比较，非论文原文与实测结果。

通用表达要求

**改前**

The method improves answers in all languages.

该方法改善所有语言的回答。

**改后**

On the tested English-manual questions, the method improves citation support.

在已测试的英语手册问题上，该方法提高引用支持率。

**第 1 句：**只描述实际测过的对象和指标，不能推广到未经测试的语言。

#### 观察与原因分开

先报告现象，再讲可能原因；匹配对照支持后才归因。

教学改写：假设已有对应设计或比较，非论文原文与实测结果。

通用表达要求

**改前**

Evidence notes prove that better organization causes the improvement.

证据笔记证明，更好的组织造成了提升。

**改后**

Citation support is higher with evidence notes in the matched comparison.

在匹配比较中，使用证据笔记的引用支持率更高。

**第 1 句：**第一句只报告观察。

This comparison does not isolate quote organization from retained constraint information.

该比较尚未区分摘句组织与保留约束信息的各自作用。

**第 2 句：**机制归因服从控制范围，不用 prove 放大解释。

#### 首句写发现

随后给图表、关键比较和意义，不复述表头。

教学改写：假设已有对应设计或比较，非论文原文与实测结果。

通用表达要求

**改前**

Table 1 shows the scores of all methods.

表1展示了所有方法的分数。

**改后**

Retaining earlier constraints improves citation support in this comparison.

保留前文约束在该比较中提高了引用支持率。

**第 1 句：**第一句就是可判断的主要发现，前提是实际对照支持。

Table 1 reports the matched comparison with and without those constraints.

表1报告保留与移除这些约束的匹配对照。

**第 2 句：**给出证据入口与比较对象，不逐行念分。

#### 同级小节篇幅相称

任务相近，篇幅尽量接近；太长先查重复，复杂内容分段。

教学句式，非论文原文或实测记录。

PaperBank 篇幅与排版要求；各节内容需要优先

We separate evidence selection from answer generation because the two stages use different inputs.

证据筛选与回答生成使用不同输入，因此分别解释两个阶段。

**第 1 句：**按真实职责分段，复杂才多写；不用统一字数删除必要解释。

## 各章先回答什么

### 标题

先把最值得记住的发现放进标题。

标题突出核心贡献，不列举全部模块。

### 摘要

让人用一段话看懂为什么这项工作值得做。

突出问题、关键改动与主要发现，仅保留理解贡献所需的实现细节。

### 引言

让读者认同问题，并记住你的解法为什么有用。

具体说明已有困难、对应设计与验证依据，不仅扩写摘要。

### 相关工作

说明已有路线、本文差异及其与核心贡献的关系。

局限与对应方案须对齐 Introduction 的对象和关键词，不新增无关问题。

### 方法

铁律：告诉读者为什么你的方法好，比解释清楚方法更重要。

围绕本文设计组织内容，每个关键选择对应 Introduction 的具体困难。既有方法简要说明，不将 Method 写成 Preliminary。

### 实验

用对照检验贡献，解释主要差异与发现。

每项核心主张须有对应证据，分析解释结果如何支持或限制该主张。

### 讨论与局限

解释发现，写清适用范围和局限。

### 结论

回答开头的问题，概括贡献和发现。

### 参考文献

引用回查原文，信息和版本对齐。

### 附录

提供可定位、可复核的设置与补充材料。

详细设置、补充实验与完整案例分类组织，并从正文引用具体位置。

### Rebuttal

用明确证据回答审稿人的具体关切。

首句回答原问题，再给证据、解释与位置；感谢简短，保持礼貌。

## 各章完整句式模板

#### 标题：对象、任务、改动

标题写研究对象与核心贡献；有实测发现时可突出发现，疑问式标题须由正文回答。

教学模板；【】填真实材料。

- 标题围着最重要的一项贡献写；专业术语仅用于准确描述研究对象与贡献。
- 发现型、问题型、方法型都可用。名称新不等于方法新。

推荐结构模板

[Method Name]: [Key Design] for [Task under the Specific Difficulty]

[方法名]：用[关键设计]解决[具体困难下的任务]。

**第 1 句：**冒号前是名字，后半句给出研究对象和实际改动。

[Specific Finding] in [Research Setting]

[研究场景]中的[具体发现]。

**第 2 句：**发现或 benchmark 论文也能用结果组织标题，不必伪装成方法论文。

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

To address this limitation, we propose [method] that [key operation].

为解决这个问题，我们提出[方法]，通过[关键操作]实现改进。

**第 3 句：**方法对应上一句的不足，不突然转向另一件事。

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

#### 引言第一段：方向与任务

从研究方向进入具体任务，背景仅保留理解后文问题所需的信息。

按论证顺序选用，段落可合并或拆分。

教学模板；【】填真实材料。

- 背景只留理解问题所需的信息；接下面的已有方法句式，共同组织首段。

PaperBank 推荐结构模板

[Research direction] aims to [clear task objective] [citations].

[研究方向]旨在[清楚的任务目标][引用]。

**第 1 句：**先立研究对象，引用就近支持这个判断。

In [application], this capability matters because [evidence-supported value].

在[应用]中，这种能力影响[有依据的实际价值]。

**第 2 句：**用一句说明值得做，未经评估不能声称提高商业收益。

In this setting, [input] must be converted into [output] while satisfying [constraint].

在这一场景下，需要将[输入]转为[输出]，同时满足[约束]。

**第 3 句：**把大方向落到具体任务，接着概括已有解法做到哪一步。

#### 引言首段后半：已有方法

概括已有路线的操作与能力，为下一段具体局限提供依据。

教学模板；【】填真实材料。

- 按任务、机制或评价目标分组，不逐篇点名。
- 引言与 Related Work 的分类、对象和关键词一致；机制细节放后者。

PaperBank 规范化写法；段数按内容调整

Existing [research line] uses [shared mechanism] to [established capability] [citations].

现有[研究路线]通过[共同机制]实现[已建立的能力][引用]。

**第 1 句：**先承认已经解决的部分，再让读者理解下一段为何还提出困难。

Another line uses [different mechanism] to support [additional capability] [citations].

另一条路线通过[不同机制]支持[另一项能力][引用]。

**第 2 句：**只保留有实质差别的第二类方法；没有这类研究就删掉此句。

#### 引言第二段：局限

写清现有方法在何种条件下不足，以及问题产生的原因。不能只用 expensive、limited、inefficient 概括。

按论证顺序选用，段落可合并或拆分。

教学模板；【】填真实材料。

- 用 However 承接上一段真实能力；先讲问题，本段仅说明局限，方案在下一段展开。
- 给 2～3 个词的自明短名，首次就解释；困难数量按真实贡献，按实际内容确定。
- 每个困难都能指向后文设计与实验；命名新不等于发现新。

PaperBank 规范化写法

However, [existing capability] does not establish [missing property] when [condition].

然而，在[条件]下，[已有能力]仍不能说明[尚缺性质]成立。

**第 1 句：**说清评价或能力的证明边界，不把未证明改写成完全失败。

We call this difficulty [short name]. It occurs when [plain-language condition and consequence].

我们将这个困难称为[短名]。它发生在[普通语言说明的条件与后果]下。

**第 2 句：**名称帮助记住困难，紧接解释帮人理解。没有对应观察就不能仅凭名字制造新问题。

For example, [concrete input or situation] requires [specific behavior], which [existing comparison] does not assess.

例如，[具体输入或场景]需要[具体行为]，而[对照评价]尚未检验这一点。

**第 3 句：**例子显示缺口怎样发生，是否未检验仍需核对实际来源。

#### 引言第三段：设计

按局限顺序说明改进、作用机制与输入输出，不能只列模块名称。

按论证顺序选用，段落可合并或拆分。

教学模板；【】填真实材料。

- 用 To address / To solve 接回具体困难；逐项说明设计为什么针对它。
- Introduction 说明设计思路与作用；公式、模型细节与实现参数放在 Method。
- 关键词与 Related Work、Method、图、实验一致。预期作用与实测效果分开。

PaperBank 规范化写法

To address [challenge A], we [design A] using [actual input or signal].

为解决[困难 A]，我们利用[实际输入或信号]设计[A 方案]。

**第 1 句：**一对一接回上一段的困难。

This design [specific operation], allowing [specific intended capability].

该设计通过[具体操作]，支持[明确的目标能力]。

**第 2 句：**解释如何发生，不只把方案换个词再说一遍。

To address [challenge B], we [design B].

为解决[困难 B]，我们采用[B 方案]。

**第 3 句：**第二项方案处理另一项真实问题；没有就删除，不添加无必要的模块。

#### 引言第四段：主要发现

设计之后写主要发现与启示，并给关键比较、条件及范围，不局限于分数提升。

按论证顺序选用，段落可合并或拆分。

教学模板；【】填真实材料。

- 发现可取短名，随后解释含义；不添加未测能力。
- 只讲关键关系，不复述结果表；引言图用来讲动机。

PaperBank 规范化写法

Experiments on [tested tasks] reveal [specific finding] under [comparison conditions].

在[比较条件]下，[实测任务]的实验揭示[具体发现]。

**第 1 句：**先说结果，限定实测范围。

This finding indicates [what is supported], while [remaining limitation] remains unresolved.

该发现支持[已证实的认识]，但[剩余局限]仍未解决。

**第 2 句：**解释贡献及边界，不扩大主张。

#### 引言最后：贡献列表

首项概括解决的核心问题，随后分别写关键设计与主要发现。每项说明一个独立贡献，避免重复流程。

按论证顺序选用，段落可合并或拆分。

教学模板；【】填真实材料。

- 核心工作 → 关键设计 → 实验发现，是常用组织；独立评价创新可另列。按真实贡献增删，不固定四项。
- 每项说新增了什么、解决什么或发现什么；长度接近，不重复前文段落。

PaperBank 规范化写法；项数按真实贡献确定

In summary, our contributions are:

概括而言，我们的贡献如下：

**第 1 句：**用清楚的引导句收尾，不再另起论文目录预告。

We propose [core contribution] to [research objective].

我们提出[核心贡献]，用于[研究目标]。

**第 2 句：**第一项说新增研究对象或核心方法。

We design [mechanism] that [specific operation].

我们设计[机制]，通过[具体操作]实现[作用]。

**第 3 句：**第二项解释关键设计，不重复第一项。

We introduce [evaluation or verification] for [what it checks].

我们引入[评价或验证方式]，检验[具体性质]。

**第 4 句：**只有它本身构成实际贡献时单独列项。

Experiments across [scope] reveal [specific finding].

跨[实测范围]的实验揭示[具体发现]。

**第 5 句：**写出真实发现及比较条件，不能只写 extensive experiments demonstrate effectiveness。

**完整 LaTeX 结构模板**

```latex
In summary, our contributions are:
\begin{itemize}
    \item We propose [core contribution] to [research objective].
    \item We design [mechanism] that [specific operation].
    \item We introduce [evaluation] for [what it checks].
    \item Experiments across [scope] reveal [specific finding].
\end{itemize}
```

#### Related Work：完整模板

按共同机制归类。可直接比较的工作安排对应基线；不能直接比较时说明设置差异。

教学模板；【】填真实材料。

- 每个主题：路线概括 → 机制分组 → 已有扩展 → 缺口 → 本文方案。引用跟着类别走。
- 每个小节都收尾：However 讲不足，To address / To solve 讲对应方案。
- 结尾的对象、范围、关键词与 Intro 一致；各小节讲不同缺口。
- 小节标题简短。短主题一段写完，复杂主题按问题分段。
- 相近工作的差异提前讲清。引用准确完整，不因图相似或结果不利而漏引。
- 引用数量不是会议配额；删除重复说明，不加入无关文献。

PaperBank 规范化写法；主题数量按论文内容

[Research line] addresses [shared task] by [shared mechanism] [citations].

[研究路线]通过[共同机制]处理[共同任务][引用]。

**第 1 句：**第一句定义本小节主题，把真正相近的工作归成一类。

One group [mechanism A], whereas another group [mechanism B] [citations].

一类方法采用[机制 A]，另一类采用[机制 B][引用]。

**第 2 句：**分组必须有实质机制差别，不是换作者名字。

More recent extensions [additional established capability] [citations].

后续扩展进一步实现了[已有额外能力][引用]。

**第 3 句：**承接基本路线的扩展，新增引用须与所述扩展直接相关。

However, these approaches do not establish [Intro challenge] under [specific scope].

然而，在[具体范围]内，这些方法尚未说明[引言中的问题]得到解决。

**第 4 句：**不足直接复用引言关键词，并限定到原文支持的边界。

To address this limitation, we [matching design] to [specific purpose].

为解决这个不足，我们通过[对应设计]实现[具体目的]。

**第 5 句：**方案与引言一致；以对应方案结束本小节，不添加空泛的 Next 过渡句。

**完整 LaTeX 结构模板**

```latex
\section{Related Work}
\subsection{[Short Topic A]}
[Research line] addresses [shared task] by [shared mechanism]~\cite{...}.
One group [mechanism A], whereas another group [mechanism B]~\cite{...}.
More recent extensions [additional established capability]~\cite{...}.
However, these approaches do not establish [Intro challenge A] under [scope A].
To address this limitation, we [matching design A] to [purpose A].

\subsection{[Short Topic B]}
[Research line B] evaluates [property] using [evaluation basis]~\cite{...}.
Other evaluations [substantive extension]~\cite{...}.
However, [Intro challenge B] remains unresolved under [scope B].
To address this limitation, we [matching design B] to [purpose B].
```

#### Method Overview：完整模板

首句说明关键设计为何针对 Introduction 的困难，随后按真实依赖说明各步骤与章节位置。

教学模板；【】填真实材料。

- 先写核心设计相对已有做法的最有用区别，再介绍各节如何实现它；只列目录没有贡献。
- Overview、章节标题、framework 中的模块名称对应；章节名是阅读位置，不是执行动作的主体。
- 每步说目的、输入、操作与输出，用准确章节引用定位一次；后句接前句产物，并行关系照实写。
- 末句引用框架图；已有章首总览不再单开重复 Overview。格式转换不单独列为创新模块。

PaperBank 规范化写法；按真实依赖替换或删除阶段

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

- 关键计算用编号公式，符号就近定义；长算法、完整 prompt 和参数表放附录。
- 粗体段首对应真实模块或步骤，名称与框架图一致。
- 并行、循环、反馈单独说明；训练信号注明样本、阶段、指标和更新对象。
- 自己的创新占主要篇幅，标准编码、调用与格式转换简写；不能把已有方法改名当创新。
- 每节结尾说明输出与后续用途，下一节使用对应产物。重点是为什么值得做，复现所需细节仍要给全。

通用要求；PaperBank 推荐句式

To [specific purpose], [module] uses [previous output] to [key design].

为实现[具体目的]，[模块]利用[上一步产物]进行[关键设计]。

**第 1 句：**首句说明目的、真实输入与关键设计。

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

#### Experiments：先列要验证的问题

先列 Introduction 的主张与检验标准，再安排主结果、消融及补充分析。

教学模板；【】填真实材料。

- RQ 可用于组织，不必每表一个编号；标题写 Main Results、Ablation Studies 或具体目的。
- 按论文贡献选实验，不照搬另一类研究的实验清单。

通用要求；推荐结构模板

After constructing [method or benchmark], we evaluate [actual target] on [scope].

构建[方法或基准]后，我们在[范围]内评价[实际对象]。

**第 1 句：**承接前章产物，先给比较范围。

We first test whether [design] improves [goal] under [fixed conditions].

我们先检验，在[固定条件]下，[设计]能否改善[目标]。

**第 2 句：**主结果使用能检验 Introduction 主张的指标，不根据有利结果临时更换指标。

We then isolate [component] and examine [robustness, efficiency, or transfer question].

随后，我们单独检验[组件]，并检查[稳健性、效率或迁移问题]。

**第 3 句：**只预告实际存在的分析，不能为了补齐模板虚构实验。

#### Experimental Setup：比较设置

集中定义指标、方向、分母、简称与实验设置，新增指标说明用途与贡献。

教学模板；【】填真实材料。

- Metrics：定义、方向、分母、汇总方式和无效输出处理。指标多时编号，名称与简称便于查找；新指标单独起段。
- Baselines：按路线分类，给引用和可影响结果的共享条件。简介讲它做什么，结果差异留给分析。
- Implementation Details：Method 出现的参数给实际值与选择依据；完整参数表可放附录。训练、推理、硬件、重复次数和成本口径说全。
- 人工或模型 judge：谁判什么、按什么判、核验多少。设置是为了让人判断比较是否成立，不是报设备清单。

通用要求；Metrics/Baselines 为推荐组织

We evaluate [unit] from [dataset version], using [split or selection rule].

我们从[数据版本]中按[划分或选择规则]评价[样本单位]。

**第 1 句：**先定义比较对象与分母，不根据结果更换统计范围。

Metrics. We measure [property] using [metric definition]; [direction] is better.

指标。我们用[指标定义]测量[性质]；[方向]表示更好。

**第 2 句：**不是只列缩写；定义、单位和方向决定读法。

We compute [per-unit statistic] and aggregate by [rule]. [Invalid-output policy].

先计算[单位统计量]，再按[规则]汇总；[无效输出处理规则]。

**第 3 句：**宏平均、微平均与条件子集不能混用。

Baselines. We compare [method] with [routes and citations] using [shared conditions].

基线。我们在[共享条件]下，将[方法]与[基线路线及引用]比较。

**第 4 句：**把可影响结果的条件说明白，不只报模型名字。

Implementation Details. We select [parameters] on [development data] and fix them before [final evaluation].

实现细节。我们在[开发数据]上选择[参数]，并在[最终评价]前固定这些选择。

**第 5 句：**明确选择边界；具体值与来源按真实记录填。

#### Main Results：先写发现

解释主要差异、可能原因及对应设计，不逐行重复表格数值。

教学模板；【】填真实材料。

- 把有依据的结论写在段首或小标题。一段优先围着一个实验、一个图表、一个结论讲，不混三件事。
- 先说明关键关系，再给决定判断的数字与范围；全面胜出、显著、稳定需要对应证据。
- 观察之后解释原因，消融才能帮助归因；有利、不利指标与代价都照实解释。

通用要求；加粗发现为 PaperBank 偏好

[Design] improves [specific ability] under [tested condition].

在[实测条件]下，[设计]改善了[具体能力]。

**第 1 句：**作为加粗结论；无提升就写真实差异或未支持的主张。

Table [ref] shows [qualitative contrast] relative to [comparison].

表[真实编号]显示，相比[对照]，[关键关系]。

**第 2 句：**只讲决定结论的对照，不逐行复述数字。

This contrast supports [Intro contribution], while [observed trade-off] limits [scope].

这一对照支持[引言贡献]，但[已观察代价]限制了[适用范围]。

**第 3 句：**解释结果意味着什么，同时保留真实取舍。

#### Ablation：改一项，查一个作用

消融每次去掉或替换一个因素，固定其他条件，检验对应设计的作用。

教学模板；【】填真实材料。

- 同时改多项时补匹配对照，或只评价整套改动。
- 写清目的、改动和发现，不只贴 w/o A、w/o B。

通用要求；按机制归因需求选用

To examine [component purpose], we replace [component] with [control].

为检验[组件作用]，我们用[对照]替换[组件]。

**第 1 句：**消融对准方法声称的作用。

We keep [other settings] fixed.

其余[设置]保持不变。

**第 2 句：**告诉读者哪些替代解释受到控制。

Figure [ref] shows [observed change], supporting [limited component role] in [tested setting].

图[真实编号]显示[观察变化]，支持该组件在[实测设置]中具有[有限作用]。

**第 3 句：**作用不超过实际控制的因素与范围。

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

#### 进阶：性能与成本一起比

多目标实验同时报告收益与代价，按帕累托前沿讨论取舍，不将单项优势写成全面最优。

教学例子；假设质量越高越好、成本越低越好。

- 非支配：没有另一可比配置在所有目标上都不差、至少一个更好。只测有限配置，就称已测配置的非支配集，不宣称全局最优。

Configuration A is cheaper, whereas configuration B achieves higher quality. Neither dominates the other.

配置 A 更便宜，配置 B 质量更高，二者互不支配。

**第 1 句：**两个指标方向先说明，读者能看清换来了什么。

We report the non-dominated configurations among the tested settings.

我们报告已测试设置中的非支配配置。

**第 2 句：**写清搜索范围；散点连线不能证明所有中间配置都实测过。

[pymoo · Pareto dominance](https://pymoo.org/getting_started/preface.html) · Pareto dominance 定义；本文例句为独立教学改写

#### 进阶：同时做两个差

同期因素可能影响上线前后比较。适用条件下，可比较处理组与对照组各自的前后变化；普通算法消融不等于 DID。

假设教学例子；分数为虚构，不对应任何论文实验。

- 需要真实处理组、可比对照组和前后观测；因果解释还需平行趋势等识别条件。复杂的错时处理不能照搬简单均值相减。

The treated group improves from 60 to 75, while the comparison group improves from 60 to 65.

处理组从 60 升到 75，对照组同期从 60 升到 65。

**第 1 句：**先说同一指标和观察窗口，两组都有前后值。

The difference between these changes is 10 points, rather than the treated group’s 15-point increase.

两组变化相差 10 分，而不是把处理组的 15 分增长全算作处理效果。

**第 2 句：**(75−60)−(65−60)=10。算出差值只是一步，是否能因果解释还要核对识别条件。

[Callaway & Sant’Anna · Difference-in-Differences with Multiple Time Periods](https://arxiv.org/abs/1803.09015) · 比较设计与识别条件；数值为独立教学示例

#### Case Study：走一遍流程

用明确来源的输入与输出展示流程及判断依据，案例不能替代总体统计。

教学模板；【】填真实材料。

- 保留原始文本、实测回复和标签；自构例子标清。案例不能代替总体结果。
- 位置按叙述需要安排；帮助理解评价时，也可放在总体结果之前。

通用要求；教学案例须明示

In [a recorded case or a stated constructed example], [input] requires [specific behavior].

在[有来源的真实案例或明示构造案例]中，[输入]要求[具体行为]。

**第 1 句：**先给来源类型与任务，明确区分教学示例与实测案例。

[Stage] uses [evidence] to produce [intermediate output].

[阶段]利用[证据]生成[中间产物]。

**第 2 句：**把可见处理与 framework 对上。

The final output [meets or violates requirement] because [observable evidence].

最终输出[满足或违反要求]，依据是[可见证据]。

**第 3 句：**判定与证据直接连接，不只写一个勾叉。

#### Discussion / Limitations：意义与局限

解释发现的意义、可能原因与失效条件，区分经验解释与有对照支持的机制判断。

教学模板；【】填真实材料。

- 局限写具体数据、语言、条件和预算，说明没测什么、没解决什么。
- 未测条件不能直接写成失败；关键限制不能藏起来。

通用要求；标题位置按领域

The results suggest [specific interpretation] within [tested scope].

在[实测范围]内，结果提示[具体认识]。

**第 1 句：**解释发现的意义。

The present comparison does not isolate [alternative explanation].

当前比较尚未单独排除[替代解释]。

**第 2 句：**没做归因对照时直说仍不能区分什么。

Our evaluation covers [range], while [different condition] remains untested.

当前评价覆盖[范围]，[不同条件]尚未检验。

**第 3 句：**边界具体，能自然指导下一步研究。

#### Conclusion：回答开头的问题

回到研究问题，概括核心贡献、主要发现与范围，不重复完整方法流程。

教学模板；【】填真实材料。

- 未来工作接已说明的局限；计划不能写成能力。

通用要求；推荐结构模板

We studied [research problem] by [core design].

我们通过[核心设计]研究了[问题]。

**第 1 句：**回到起点，不重新铺领域背景。

The evaluation establishes [supported finding] under [conditions].

评价表明，在[条件]下，[有证据的发现]成立。

**第 2 句：**收束真正得到的认识。

[Specific limitation] motivates future evaluation in [relevant setting].

[具体局限]说明，后续需要在[相关设置]继续检验。

**第 3 句：**实际需要未来工作才写，不要求固定末句。

#### References：回查原文

逐条核对原文、版本及其对引用处主张的支持范围。

教学模板；【】填真实材料。

- 同一论文不同版本去重；模型和工具引原始报告或官方文档。
- 按相关性选择引用，不按年份或数量设配额。

通用要求

[Grouped claim] [citations that actually support the claim].

[归类判断][真正支持该判断的引用]。

**第 1 句：**每条引用都服务近旁判断，不能只把出处堆在段尾。

We use [model or tool version] [original report or official documentation].

我们使用[模型或工具版本][原始报告或官方文档]。

**第 2 句：**记录实际使用版本，引用版本须对应实际实验，不用后发布版本说明早期设置。

#### Appendix：实现与补充实验

先删除重复内容，再将次要细节移至附录。支撑核心贡献的比较与分析留在正文。

教学模板；【】填真实材料。

- 核心设计与关键限制留在正文；每个附录节说明补充什么，正文给入口。
- 术语、符号、版本和分母统一；补充结果改变结论时，正文一起改。

通用要求；分组名按内容

Appendix [ref] provides [details] needed to reproduce [method or comparison].

附录[编号]给出复现[方法或比较]所需的[具体细节]。

**第 1 句：**正文指向实际有用的入口，不笼统“更多见附录”。

This section tests [main-text claim] while controlling [alternative explanation].

本节在控制[替代解释]的条件下检验[正文主张]。

**第 2 句：**附录开头重建本节作用，读者不必回翻数页猜。

#### 4.1 拆审稿意见

读取完整 review：Summary 核对理解，Strengths 记录认可点，Weaknesses 与 Questions 提取待回应关切。

教学模板；【】填真实材料。

- 保留原问题与顺序，一句话有多问就拆开。区分机制解释与实施情况，分别回应。
- 区分描述不清、缺对照和机制未证实；分别给案例、比较和针对性检验。
- 从原意见判断阅读关注点，不凭 confidence 猜身份或保证提分；查当轮回复规则。

The reviewer asks whether the gain comes from retrieval quality or answer generation.

审稿人问的是：收益来自检索质量，还是答案生成。

**第 1 句：**先说清真正的问题；这里要区分两种解释。

We compare the two generators using the same retrieved passages.

我们使用相同的检索段落比较两个生成器。

**第 2 句：**对照须对应原问题：固定检索，改变生成器。

#### 4.2 逐题回复

首句直接回答问题，再给证据、解释与位置；流程问题用明确来源的案例展示。

教学模板；【】填真实材料。

- 标题沿用原问题；首句给结论或具体值。
- 给设置、对照、绝对值和指标方向；数据适合表格就用表格。
- 说明证据如何回答问题，附表号、节号或行号。
- 已有实验能回答就整理出来；缺关键证据时做能隔离争议的最小对照，不盲目把全部基线重跑。
- 感谢具体、简短。说明已经补出的内容，不用一句“我们将补充”代替答案。
- 一个段落回一个小点。表格写结果与必要设置差异，分析接回贡献；没有标准条件支持时不能把落后全归咎于不公平。

The gain persists when retrieval is held fixed.

固定检索后，收益仍然存在。

**第 1 句：**首句直接回答；只有相应对照支持时才能用。

With identical passages and decoding settings, 【method】 scores 【A】 versus 【B】 for 【baseline】 on 【metric】 (higher is better; Table 【R1】).

使用相同段落和解码设置时，【方法】在【指标】上为【A】，而【基线】为【B】（越高越好；表【R1】）。

**第 2 句：**给协议、对照、绝对值和位置，不要只报“提升显著”。

This comparison isolates the generator change under the tested retrieval setting.

这一比较在所测试的检索设置下隔离了生成器改动。

**第 3 句：**收束到已检验的范围，不扩大到所有场景。

#### 4.3 区分两种解释

准确复述审稿人的推理，用针对性对照检验争议前提，并说明证据支持的结论。

教学模板；【】填真实材料。

- 两种解释各预测什么？用什么实验分开？
- 无法区分就缩小机制主张；设计动机不能代替结果。

A plausible alternative is that the improvement comes from longer outputs.

一种合理的替代解释是：收益来自更长的输出。

**第 1 句：**准确点出竞争解释，不评价审稿人的水平。

We therefore match the output-token budget and compare 【A】 with 【B】 under the same evaluation protocol.

因此，我们匹配输出 token 预算，并在相同评测协议下比较【A】和【B】。

**第 2 句：**控制对方指出的混淆因素。

The difference is 【result】; this supports 【bounded conclusion】 but does not establish 【untested mechanism】.

差异为【结果】；它支持【限定结论】，但尚不能确立【未经检验的机制】。

**第 3 句：**结果支持到哪里，就写到哪里。

#### 4.4 澄清：定义、流程、例子

说明定义、真实输入与各步产物，定位争议环节；公式数量不能替代解释。

教学模板；【】填真实材料。

- 术语不清给定义，流程不清给案例，效果不清给对照。
- 确有错误就改；不同意就给依据。不以“你误读了”替代澄清与证据。

Here, 【term】 denotes 【concrete definition】.

这里，【术语】指【具体定义】。

**第 1 句：**定义先落到对象，不绕回抽象名词。

For input 【x】, the module performs 【operation】 and returns 【y】 to 【next module】.

输入【x】后，该模块执行【操作】，将【y】交给【下一模块】。

**第 2 句：**一条样例走完整条路径。

Section 【N】 specifies this interface; we clarify 【ambiguous phrase】 in 【permitted revision location】.

第【N】节说明了这一接口；我们在【允许的修订位置】澄清【歧义表述】。

**第 3 句：**位置要真实存在；会议不允许改稿时，只在回复中澄清。

#### 4.5 Revise loop

按原问题逐轮检查覆盖、证据与逻辑，仅修改未通过的回复，再压缩文字并调整语气。

教学模板；【】填真实材料。

- 给 Codex 论文、原始 review、证据和回复。
- 逐题输出：原问题、回复位置、剩余缺口、改法、所需证据。
- 先查漏答、证据和逻辑，再缩文字、调语气。改完重查同一张问题清单。
- 每问有答、证据对应、逻辑通顺、篇幅合规就停；缺实验交给人决定。
- 模拟用于查漏洞，不预测评分变化或录用。

Concern: 【verbatim concern】. Response location: 【paragraph/table】. Remaining gap: 【specific gap】.

原问题：【审稿原话】。回复位置：【段落/表】。剩余缺口：【具体缺口】。

**第 1 句：**每条批评必须定位，不能仅给“还不够有说服力”等笼统评价。

Minimal fix: 【edit】. Required evidence: 【existing result or experiment needed】.

最小修改：【改法】。所需证据：【已有结果或需要的实验】。

**第 2 句：**把改文字和补证据分开，便于作者判断。

#### 4.6 第二轮与 AC 总结

先逐题回应，再向 AC 概括关键问题、证据与剩余分歧，准确引用已确认的评价。

教学模板；【】填真实材料。

- 追问接回原问题和证据，不重贴整份回复。
- 写清剩余限制，不猜未回复审稿人的态度。
- 不请求提分或接收，把判断留给审稿方。

Regarding the follow-up on 【issue】, 【direct answer】; the supporting comparison is in 【location】.

针对【问题】的追问，【直接答案】；支持这一答案的比较见【位置】。

**第 1 句：**只写新增信息。

The main concern was 【issue】. Our response provides 【evidence】, supporting 【bounded conclusion】.

主要关切是【问题】。回复提供了【证据】，支持【限定结论】。

**第 2 句：**明确说明问题、回复及其依据。

## 绘图规则与图型

先确定图的主要任务与对应贡献，再安排内容和布局。复杂图先删去重复信息，保留必要输入、操作与输出。

- **每图明确一个主要任务：**mainfig 展示研究动机与观察，framework 说明设计如何对应问题，结果图提供验证证据。每图明确一个主要任务。

Show where the existing pipeline fails and which step our method changes.

画清旧流程在哪一步出问题，我们改了哪一步。

- **绘图先于正文精修：**先完成可供合作者审核的框架图与实验图，再精修正文。图未能体现贡献时，先调整内容与布局，再修改配色。

Panel (a) shows the observed gap; panel (b) tests the proposed repair.

(a) 展示实际缺口；(b) 检验我们的修补。

- **统计图使用真实数据：**统计图用 Python 从真实数据绘制；imagegen 用于动机、框架和案例图。缺数据就停，不补点、不编误差、不为平滑改曲线。

Draw the recorded success rates with Python. Generate only the workflow illustration with imagegen.

成功率用 Python 按记录画；imagegen 只生成流程示意。

- **按最终尺寸检查字号：**按最终栏宽排字，字体与正文一致；所有图内字同一字号，介于正文与正文减 2 pt 之间，标题也不能更大。放不下先重排，不缩小规定字号。

Use the paper’s column width and body font; remove repeated labels rather than shrinking text.

用论文栏宽和正文字体；删重复标签，不缩小规定字号。

- **箭头表示真实依赖：**同层成组并命名；先后、并行、汇合、反馈按真实依赖画。每条箭头说清传什么，起止明确，避免穿过文字与无必要的迂回。

Retrieved passages enter the generator; the evaluator receives the generated answer.

检索段落送给生成器；生成的回答交给评价器。

- **区分输入与评价信息：**输入、输出、评价规则用三种边框区分，并给图例。只供评价的 rubric 不连到被测模型；不同模型收到不同材料，也要标清。

Dashed boxes contain model inputs; solid boxes contain responses; dotted boxes contain evaluator-only criteria.

虚线框是模型输入，实线框是回复，点线框是只供评价的判据。

- **低饱和配色与清晰对比：**常规模块用中性灰，关键改动用统一强调色。低饱和配色须保持清晰对比。

Blue circles denote the baseline; orange triangles denote our method in every panel.

每个面板都用蓝圆点表示基线，橙三角表示我们的方法。

- **对话按轮次与语义分段：**一轮一框，注明角色；同一轮长回复按语义分段，不伪装成多轮。高亮只标关键约束、证据或错误，颜色含义要能读懂。

The left column contains evidence; the right column shows the model response and its evaluation.

左栏放证据；右栏放模型回复和评价。

- **同一案例仅完整呈现一次：**同一来源的案例在全文只完整呈现一次，其他位置交叉引用。改名、翻译、裁剪也算同一个；必要对照集中展示，单个案例不能证明总体效果。

Figure 1 presents the case; Section 4 refers back to Figure 1 without repeating the dialogue.

案例放图 1；第 4 节回引图 1，不再抄一遍对话。

- **同类子图使用一致尺度：**围绕一个问题排现象、诊断、对照和稳健性；同条件同顺序、同配色，同类轴和色标保持可比。

The first panel identifies the gap, the second locates it, and the third tests whether it persists.

第一图找差距，第二图找发生位置，第三图检验差距是否仍在。

- **准确呈现坐标与差异：**查单位、分母、方向、坐标起点和误差类型；截断坐标要明确标出。相对增益同时给绝对值，柱长和数值必须对应。

Accuracy rises from 60% to 66%: 6 percentage points, or a 10% relative increase.

准确率从 60% 到 66%：增加 6 个百分点，相对提高 10%。

- **Caption 说明读法与发现：**图注先说读法和发现，再点出与贡献的关系；图中的简称在 Caption 给全称。结论须有证据支持；“效果显著”须有对应统计检验。

Error bars show 95% question-level bootstrap intervals; the horizontal line marks zero gain.

误差条表示按题目重采样的 95% 区间；水平线表示零增益。

- **编译后检查最终页面：**放回论文检查实际字号、字体嵌入、可选文字、裁切、碰撞、图注总高度和首次引用顺序。源码字号正确，不代表插入后仍正确。

Place the figure after its first mention and check all labels at normal reading size.

按首次引用顺序排图，以正常阅读大小检查全部文字。

- **明确模块输入与输出：**每个关键模块写清收到什么、做什么、交出什么，以及交给谁。模块名与 Method 一致，所有缩写就近解释。

The checker receives evidence and returns supported constraints to the planner.

核查器接收证据，把已支持的约束交给规划器。

- **解释图中所有标记：**图标旁写对象名；新缩写、符号、边框、线型和数字就近解释。读者只看图与图注，应知道每个标记指什么。

Label the robot as the planner and define dashed edges as feedback.

机器人标为规划器，虚线箭头定义为反馈。

- **Framework 展示操作与产物：**“结合 case 去绘制你的流程” 展示一个真实输入怎样变成中间产物和输出，旁边点出设计解决的困难。节点多不等于贡献多。

Trace one task from the evidence input through checking to the final plan.

用同一个任务走完证据输入、核查和最终计划。

- **区分示意与实测：**估计、作者示例和实测输出分清；可选路径不能画成必经步骤。框的面积、线宽和箭头不能暗示没有证据的比例或因果，图形本身须准确，不能仅靠图注纠正。

Keep illustrative module boxes equally sized; plot measured latency on a labeled axis.

示意模块框不靠大小表示耗时；实测延迟另用带坐标的图展示。

- **准确区分矢量与位图：**统计图导出矢量 PDF 并嵌入字体。生成底图上的标签另排原生、可见、可选的 PDF 文字；不留重叠字形，不加隐藏 OCR 层。混合 PDF 仍含位图。

Export the plot as vector PDF and verify that its axis labels can be selected.

统计图导出矢量 PDF，再实际选中坐标轴文字检查。

- **保持修改范围：**只改配色就保留布局、文字、换行、字号、公式、照片和连线；重排须在约定范围内。保留数据、实验和合作者的图。

Change panel fills while retaining every label, coordinate, and arrow endpoint.

只换面板底色，保留所有标签、坐标和箭头端点。

- **按模板宽度布局：**按实际栏宽起稿，不改页边距、正文字号或页面方向。正文通栏约 16:9、单栏约 4:3 是起点，附录可纵排；不进行非等比缩放。CS 默认用 [!t]，再按正文首次引用检查实际落点。

Rearrange parallel branches within the column width; keep the paper template unchanged.

在栏宽内重排并行分支，保留论文模板。

- **表格用于结果与数据：**PaperBank 默认表格只放真实结果或数据。术语、方法、实验计划和案例点评写正文，不能通过截图规避该规则；统计数字也不能把说明表变成实验结果。

Put success rates in a table and explain the checking procedure in the text.

成功率放表格，核查流程写正文。

- **重排文字与图形重叠处：**图例、标题、刻度和注释不能挡数据、箭头或边框。为文字保留空间，通过重排解决重叠，不能用遮盖隐藏问题。

Move the legend outside the plotted curves while preserving the data and axes.

把图例移出曲线区，保留数据和坐标轴。

- **摘要图：**问题在哪、为什么现有解法不够、我们动哪一步。通常最多 5 个环节，必要对照并排。

Show the problem, the existing limitation, and the changed step.

展示问题、已有解法的缺口和我们改动的步骤。

- **框架图：**输入是什么，经过哪几个模块，每步产物交给谁，输出是什么。旁边走一个可追踪例子。

Given a query, retrieve passages, rank evidence, and generate an answer with cited support.

输入问题，检索段落，筛选证据，再生成带来源的回答。

- **案例图：**“不同highlight颜色表示不同类型的信息” 白底保留必要背景、需求、证据、动作与结果；输入、模型输出、judge 用可解释边框，位置表示真实层级。

Separate the request, evidence, response, and evaluation.

把请求、证据、回复和评价分开。

- **主结果与消融：**少量方法用点图或柱图；完整方法与删组件版本同顺序、同配色。说明误差的统计单位和计算方法。

Compare the complete model with variants that remove one component.

完整方法与只删除一个组件的变体对照。

- **配对增益：**同一样本的干预与对照，画差值和零线；写清收益方向与尺度。

Each point shows the intervention-minus-control accuracy on matched questions.

每个点表示同一批题目上干预相对对照的准确率差。

- **训练或轮次动态：**折线只连有序变量；横轴写训练步数或轮次，不把无序方法连成趋势。

Track success rate and penalty magnitude against the same training steps.

用相同训练步数同时追踪成功率和惩罚强度。

- **KDE：看分布形状：**横轴是变量，纵轴是密度；颜色跟组走，均值线补位置，交代样本量和带宽。峰高不是人数，也不是累计比例。

Compare density shapes with a shared bandwidth; mark sample counts and mean values.

统一带宽比较密度形状，并标样本量与均值。

- **ECDF：看阈值以下有多少：**横轴取阈值，纵轴直接读累计比例；同一坐标比两组，阶梯从 0 到 1。低于某阈值的样本比例应从 ECDF 读取，KDE 峰值不能表示累计比例。

At a threshold of 10, the ECDF gives the fraction of observations at or below 10.

阈值取 10 时，ECDF 直接给出不超过 10 的样本比例。

- **热图：**条件乘方法，统一色标；正负增益以零为中点，缺测留空并说明。

Use one shared color scale for all conditions and mark missing cells.

全部条件使用统一色标，缺测单元明确标记。

- **PCA：把高维关系投到二维：**“利用空间位置关系绑定数据，更换不同的颜色呈现不同属性” 同时交代特征、标准化与解释方差。分得开不等于泛化好；PaCMAP、t-SNE 不叫 PCA。

Project standardized features onto two principal components and report the variance explained by each axis.

把标准化特征投到两个主成分，并报告每根轴的解释方差。

- **雷达图：多指标逐轴读：**每轴一个指标，写尺度、归一化和好坏方向；颜色再配点形。不同量纲不能用面积直接比较，轴顺序也会改变面积。

Compare normalized metrics spoke by spoke; polygon area is not an overall score.

沿每根轴比较归一化指标；多边形面积不是综合分数。

- **成本性能图：**每点是一个实际配置；在线与离线成本分开，写单位和好坏方向。连接前沿不意味着有中间配置。

Plot measured accuracy against online cost; report one-time training cost separately.

实测准确率对照在线成本；一次性训练成本另报。

- **数据集分布：**先写清统计单位、样本量、类别与分母。同一图不能混用案例数、回复数与判据数；说明类别覆盖范围与占比。

Count unique cases by domain; report response counts separately.

按领域统计独立案例数；回复数量另报。

- **置信带：**按实际重采样或模型计算区间，写清区间类型和置信水平。同一估计的嵌套区间才可比较覆盖范围；不同样本量、方差也会改变带宽。

Nested bands show the estimated 68% and 95% intervals under the stated procedure.

嵌套色带表示按所述方法估计的 68% 和 95% 区间。

- **饼图、环图与圆环排名：**饼图只画互斥且组成整体的比例；圆环柱图可画排名，极值相邻只是环形排序，不是变量关系。要读精确差值，横向条图更方便。

Use slices for a composition and ordered bars for a ranking.

组成比例用扇区；排名用有顺序的柱条。

- **二维增益与九宫格：**“可以用这种九宫格来分类，好处是可以看出两个渐进的变化” 两轴写指标、单位和好坏方向；差值图以零线分区，不为填满网格补造数据。

With both gains defined as higher is better, the upper-right quadrant shows improvements on both metrics.

两个增益都定义为越高越好时，右上象限表示两项指标都改善。

原图与出处：[光速出美图](https://da1yuqin.github.io/PaperBank/#figure-gallery)。第三方图片不随 skill 分发。

---

原创规则与教学示例：Da1yuqin / PaperBank，[原文](https://da1yuqin.github.io/PaperBank/)，[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)。转载保留署名、出处及许可，改编注明改动。
