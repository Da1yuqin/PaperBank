# PaperBank 写作检查参考

按本次任务选规则。下面示例是假设情境，不是论文原文或实测；实际改稿先核对事实。

网页：[写作铁律](https://da1yuqin.github.io/PaperBank/#chapter-rules) · [论文结构与逐句例子](https://da1yuqin.github.io/PaperBank/#paper-order) · [rebuttal](https://da1yuqin.github.io/PaperBank/#chapter-rebuttal)

## 对象与贡献


### 第 81 条：一个对象一个名字

同一对象用固定术语；代词可能指向多个对象时，换成简短对象名。

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

清晰的代词可以保留；关键是读者不需要猜谁做了什么。

### 第 71 条：结论不超过证据

每个结论写清测试对象与条件；局部结果不推广全部任务，平均提升不保证每例。

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

限定任务与统计对象，才能让结论和已有证据对得上。

## 词语、数字与主张


### 第 82 条：定义交代对象与来源

中间量说明来自哪个样本、阶段和指标，用于哪个对象；必要下标逐一解释。

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

名字不能代替定义，信号来源和作用对象决定方法的实际含义。

### 第 80 条：一句一项判断

一句承担一项主要判断，一段完成一个任务；必要条件保留，拆句后仍要连贯。

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

拆句和分段是拆开论证任务，不能只把长句切成失去承接的碎片。

### 第 73 条：数字有单位与分母

分清记录数与独立样本、百分比与百分点；结果使用对应版本和协议。

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

分母、统计单位和变化尺度不清楚，再精确的数字也会误导。

## 任务与已有进展


### 第 72 条：引用回原文

核对来源、书目信息和所支持主张；模型名称、版本与实际使用对应。

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

真实文献也可能被错引，来源存在和来源支持主张是两件事。

### 第 85 条：先例能力如实说

先说前人已解决什么，再定位当前条件下未解或未测部分；未比较不写成失败。

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

具体边界比一概否定更能解释两项工作的真实区别。

## 设计回应问题


### 第 84 条：问题、设计、实验对上

每个关键困难接实际设计，再接检验作用的实验；未验证的设计只写目的。

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

读者应能沿同一条主线看到需要改什么、如何改以及是否改成。

## 贡献与证据


### 第 87 条：贡献写动作与证据

每项贡献写一个主要动作、研究对象和意义；工程步骤与命名不能替代创新。

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

普通词和具体动作足够表达贡献，名字及形容词不能替代验证。

### 第 79 条：每段服务于主线

每段解释场景、困难、设计、证据或意义；与贡献无关的领域流水账删掉。

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

背景要把读者带到具体研究问题，不能只营造“领域很重要”的气氛。

### 第 83 条：连接词符合关系

转折确有转折，因果有依据；章节承接真实输入输出，并行步骤不能写成串行。

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

连贯来自真实依赖关系，连接词不能凭空制造因果或流程。

## 动机图


### 第 89 条：图表能独立读懂

写清对象、比较、指标、单位、方向和汇总；颜色、线型、误差条、阈值及缩写有解释。

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

每步写清输入、操作和输出；训练、推理、评价分开，推理输入不含不可见答案或未来信息。

适用边界：可见信息按真实协议说明；训练标签可以用于训练，推理时不能获得的答案或未来信息不进入推理输入。

**箭头按真实依赖连，答案别进输入**

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

按模板插入宽度排字，在最终 PDF 查字号、字形、遮挡、裁切和读序；需可选文字就抽取验证。

适用边界：字号、色板和版式以当前模板及读者需求为准，不要求固定尺寸或固定配色。

**按最终尺寸验收，别只看放大预览**

**教学示例：假设情境，非论文原文／实测记录**

改后假定已有对应记录；实际改稿须先核对这些事实，不能从改前文字推断或补造。

**逐句拆解**

缩图会连带缩字；把位图装进 PDF 也不会自动得到原生文字。

**教学改写 · English（非论文原文）**

A 160 mm source figure will be inserted at 80 mm, so its text will shrink by half. Re-export it for 80 mm and inspect the inserted page; extract the labels if the deliverable requires selectable text.

**教学改写 · 中文（非论文原文）**

源图宽 160 mm，插入论文时只有 80 mm，图中文字也会缩成一半。按 80 mm 重新导出，再看实际论文页面；交付要求文字可选择时，还要抽取标签验证。

### 第 92 条：图形标记含义一致

全文统一颜色、线型与名称；通过、失败、不适用用文字或符号分开，图例说明实际状态。

适用边界：字号、色板和版式以当前模板及读者需求为准，不要求固定尺寸或固定配色。

**同一含义用同一标记，结论别只靠颜色**

**教学示例：假设情境，非论文原文／实测记录**

改后假定已有对应记录；实际改稿须先核对这些事实，不能从改前文字推断或补造。

**逐句拆解**

蓝色只是这个示例的自定映射，其他论文可以选自己的色板，但要前后一致。

**教学改写 · English（非论文原文）**

Blue dashed boxes denote model inputs throughout the paper. An evaluated rule is labeled Pass, Fail, or N/A; a rule that has not been evaluated remains unchecked.

**教学改写 · 中文（非论文原文）**

全文都用蓝色虚线框表示模型输入。已经评价的规则写通过、失败或不适用；还没评价的规则保留空框。

### 第 95 条：教学例子标明身份

教学例子、模型实测、人工评价与总体实验分开；无记录，不画评分、分歧或修订结果。

适用边界：数据、信息边界和完成状态按实际记录说明。

**作者构造的例子，别写成模型实测**

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

人数、记录数、任务数与重复次数分开；说明共同样本、协议和无效项，不拿子集冒充全量。

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

先写图表支持的关系，再说明回答哪个问题；保留条件和关键数字，不逐格抄分数。

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

结果文字应解释比较的意义；表格负责容纳读者可以直接查到的细数。

### 第 74 条：观察不写成因果

先写观察，再写可能解释；没有排除替代解释的设计，不把相关性写成因果。

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

相关关系允许多种解释，因果结论需要对应的识别条件。

### 第 94 条：最优不等于显著

同指标、同协议下判断最优，交代方向和并列；均值、标准差、区间写清，显著性另给依据。

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

写清固定项和改变项；模型、模块一起变化，只能说明整套配置的差异。

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

一次改变多个因素，就无法把全部差异归给其中一个因素。

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

按原始数据画图，点位、长度、面积和坐标与数值一致；不假装测过、不生成成绩。

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

核对引用版本、年份与结论；代码、图表数据、原始数据分别查许可与可用性。

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

**仓库换个地方也能跑，密钥别跟着发**

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

**只改获准的地方，别顺手动别人的稿**

**教学示例：假设情境，非论文原文／实测记录**

改后假定已有对应记录；实际改稿须先核对这些事实，不能从改前文字推断或补造。

**逐句拆解**

当前明确授权优先；发现问题和获得修改授权不是同一件事。

**教学改写 · English（非论文原文）**

Requested change: replace the green fill with gray. Change that fill only, preserve node positions and arrows, and report any unrelated text error separately rather than rewriting the figure.

**教学改写 · 中文（非论文原文）**

要求是把绿色填充换成灰色，就只改填充色，保留节点位置和箭头。发现别处文字错误，单独指出，不顺手重写整张图。

## 读准问题，先给答案


### 第 100 条：每个审稿关切有回应

多问题意见逐项拆开，给结论、证据和位置；未解决照实保留，不用“已改”包办。

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

完整回应意味着每个关切都有状态和证据，不等于每个请求都能完成。

## 澄清与分歧


### 第 102 条：回复讨论事实

回答具体担忧，给理由和证据；不用“显然”或“你错了”，不为客气承认不存在的问题。

适用边界：模拟审稿问题与回复只用于教学，不是真实审稿记录。补实验、修订和回复格式以当轮官方政策为准；没有完成的事不写成已完成。

**礼貌说事实，别评价审稿人**

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

把讨论留在条件、结果和表述上，可以坚定表达立场并节省双方时间。

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

一天拉完的是草稿，不是实验。先填材料，再定图、排章节、整理实验，最后理顺 Intro。英语先够用就行，第一天别和一个形容词决斗。

本章中英句子均为教学示例，不是论文原句或实测结论；两张论文图另附原文与许可。

### 1.1 填材料，准备模板和本地项目

把下面的提示词填好，再让 Codex 动笔。只说“帮我写篇顶会论文”，它也只能先给你写篇顶会味的。

#### 材料先给齐

- **贡献：**写清具体问题、对应设计、已有发现。方法名先放一边，先说你到底解决了什么。

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
请使用 paperbank-writing skill，按下面的材料先拉一稿，再由我审核中文逻辑。

会议／官方模板／页数：【】
具体问题与原文依据：【】
一句话贡献：【针对什么，用什么设计，已有发现是什么】
方法：【任务、输入、每步操作、输出及真实依赖】
实验：【数据与划分、指标定义、基线与预算、真实结果、消融】
参考段落／图片及出处：【】
本地项目／允许改的文件：【】

顺序：核对模板并同步最新项目；先定 mainfig、framework 和关键结果图；列全部章节标题、职责、图表和篇幅；整理实验设置、主结果、消融和必要分析；最后理顺 Intro，填正文。
图中输入、输出、评价规则分清；白底、低饱和、统一颜色；按论文实际宽度排字，图字与正文同大或最多小 2 pt。结果图只读真实数据，表格按本页模板整理。
Intro 按背景与已有能力、具体问题、对应设计、主要发现、贡献列表展开。每次给我一节中文，确认后再整理英文。缺证据单列问题，不编结果和引用。保留模板，超页先删重复。
```

**English prompt**

```text
Use the paperbank-writing skill to draft from the following material and let me review the reasoning in Chinese.

Venue / official template / page limit: [ ]
Concrete problem and original evidence: [ ]
Contribution: [Problem, design, and available finding]
Method: [Task, inputs, operations, outputs, and actual dependencies]
Experiments: [Data and splits, metric definitions, baselines and budgets, actual results, ablations]
Reference passages / figures with sources: [ ]
Local project / files you may edit: [ ]

Check the template and sync the latest project. Settle the main figure, framework, and key result plots. List all section titles, purposes, figures, tables, and space allocations. Organize the experimental setup, main results, ablations, and necessary analyses. Then build the Introduction and fill the body.
Separate inputs, outputs, and evaluation criteria in figures. Use white backgrounds, muted colors, and consistent encodings. Lay out text at the final paper width, using the body font size or at most 2 pt smaller. Plot actual data and follow the table template on this page.
Organize the Introduction as background and existing capabilities, specific problems, matched designs, main findings, and contributions. Show one section in Chinese for review before writing the English. List evidence gaps without inventing results or citations. Preserve the official template and remove repetition before reducing content. Use independent Nature writing skills for Nature-family journals.
```

Overleaf Git 是 Premium 功能，取决于项目拥有者订阅或相应授权；源文件 ZIP 不含 PDF。Git 同步可能影响网页版批注和修订痕迹，协作时先约定使用方式。

[Overleaf: Git integration](https://docs.overleaf.com/integrations-and-add-ons/git-integration-and-github-synchronization/git-integration) · [Overleaf: Downloading a project](https://docs.overleaf.com/managing-projects-and-files/downloading-a-project)

### 1.2 先定图：mainfig、framework 和结果图

图先给合作者看。看完能说清为什么做、怎么做、发现了什么，再填正文。流程讲不通，换个配色也救不了。

#### mainfig：读者先看懂为什么做

- **信息：**用一个具体问题串起现有做法、失败点和本文改动。保留读懂案例所需的输入与输出，通常不超过 5 个环节。

中：任务要求同时满足 A、B；旧计划遗漏 B；本文在生成前核查 B。

EN: The task requires both A and B. The existing plan omits B; our design checks B before generation.

- **取舍：**突出最关键的差别，少放模块、logo 和工程细节。示意趋势标明示意，实测结果给出对应来源。

中：只画“遗漏约束”和“核查后保留约束”的对照，不把所有训练参数塞进首图。

EN: Contrast an omitted constraint with its retention after checking; leave training parameters out of the main figure.

左侧先提出多轮误差问题，中间放大回复细节，右侧对齐训练范围。读序是“哪里出问题 → 改哪一段”，不是先背模块名。左侧曲线是示意；细节数值与颜色含义要结合原图注读。这里学习信息组织，不照搬原图的字号和配色。

Read from the multi-turn error problem to response details and the compared training ranges. The left curve is schematic; consult the original caption for the numeric blocks and color meanings. This example illustrates information order, not a universal font or palette.

Jiaqi Wang et al., TCOD, arXiv:2604.24005v3, Fig. 1. CC BY 4.0. 从原页裁切；图形与数据未改。 [原论文](https://arxiv.org/abs/2604.24005v3) · [许可](https://creativecommons.org/licenses/by/4.0/)

#### framework：读者看懂怎么做

- **真实流程：**画清每步的输入、操作、输出，箭头连到实际接收者。并行就并行，反馈就反馈；模块名与正文一致。

中：任务与证据进入核查器；核查结果进入规划器；生成的计划再交给评价器。

EN: The task and evidence enter the checker. The checked constraints enter the planner, and the generated plan goes to the evaluator.

- **信息边界：**输入、输出、评价规则分组并区分边框。仅供评价的 rubric 不画进被测模型。用必要案例解释关键操作；同一案例只在论文里完整展示一次。

中：蓝色虚线框是模型可见输入，灰绿实线框是输出；评价器另收冻结的评分规则。

EN: Blue dashed boxes denote model-visible inputs and green-gray solid boxes denote outputs. The evaluator separately receives the frozen scoring criteria.

这张图先分交互生成和策略优化两块：左侧用对话走流程，右侧分结果效用、过程信用和成本信号。大框讲职责，箭头讲数据去向，编号讲步骤。自己的图先写清每个框收到什么、交出什么，再加图标。

The figure separates interaction generation from policy optimization. A dialogue traces the left side; outcome utility, process credit, and cost signals organize the right. Groups explain responsibilities, arrows show information flow, and numbers order the steps.

Ning Gao et al., Reinforcing Real-world Service Agents, arXiv:2602.22697v1, Fig. 1. CC BY 4.0. 从原页裁切；图形与数据未改。 [原论文](https://arxiv.org/abs/2602.22697v1) · [许可](https://creativecommons.org/licenses/by/4.0/)

#### 三类图都要过的检查

- **配色：**白底，面板用极浅的低饱和色；文字保持深色。同一方法、角色、条件全篇同色，重要对照再配形状或线型，别让读者只靠分辨红绿。

中：基线用灰色圆点，本文方法用灰蓝菱形；颜色变淡，文字不跟着变淡。

EN: Use gray circles for the baseline and muted blue diamonds for the proposed method. Keep the text dark on pale backgrounds.

- **字号与字体：**字体与正文统一，按最终插入宽度检查 PDF。PaperBank 默认图内字与正文同大，最多小 2 pt；标题、轴、图例、注释也算。先减内容、重排，别靠整图缩放塞进一栏。统计图优先矢量 PDF；生成底图的文字另排成可选文字。

中：正文实际为 10 pt，图内字用 8–10 pt；在论文整页大小下读，不只看放大的 PNG。

EN: With 10 pt body text, use 8–10 pt figure text and inspect it at its final size in the paper, not only in a magnified PNG.

- **布局：**一个主读序，同级框对齐，箭头不穿字。双栏图先按约 16:9、单栏图约 4:3 起排；同时看图注总占高。比例是起点，不拉扁图、不删关键证据。

中：两个并行输入先汇合再进入模型；长解释移到图注，关键输入保留在图里。

EN: Merge parallel inputs before the model. Move long explanations to the caption while retaining the essential inputs in the figure.

- **结果图：**从真实数据绘制。轴写变量和单位，图例解释颜色与线型，误差条写 SD、SE 或 CI 及计算单位；同类图共用尺度。

中：纵轴写成功率（%）；误差条若是跨运行标准差，就别写成 95% 置信区间。

EN: Label the y-axis as success rate (%). If error bars show standard deviations across runs, do not label them as 95% confidence intervals.

- **图注：**短句说明图在回答什么、怎么读、结果支持什么。简称给全称；必要的分母、范围、误差含义保留。方法图讲机制，结果图才讲实测发现。

中：该图比较同一测试集上的成功率与推理成本；点表示方法配置。

EN: The figure compares success rate and inference cost on the same test set; each point represents a method configuration.

**给 Codex 的绘图说明单**

```text
图的用途：【mainfig／framework／结果图】
要讲清的贡献或问题：【】
输入、操作、输出及真实依赖：【】
案例来源／原始数据／比较条件：【】
必须保留的文字、变量、单位和图例：【】
论文插入宽度／正文实际字号／已确认色板：【】
先给布局，再出图；按最终 PDF 大小检查文字、连线与图注。结果图只从所附数据绘制。
```

教学例：mainfig 用一个约束冲突说明动机；framework 用另一个案例走完证据核查与计划生成；结果图比较同一批任务的成功率和成本。

Teaching example: The main figure motivates the work with a constraint conflict. The framework traces evidence checking and plan generation on a different case. Result plots compare success and cost on the same tasks.

Review the figures with coauthors before polishing the body. They should explain the motivation, the method, and the findings. Styling cannot repair an unclear workflow.

### 1.3 整理章节、实验和表格

图定了，就定正文骨架。每节只负责一个问题：为什么做、前人做到哪、我们怎么做、证据是什么。先排逻辑，再让 Codex 填段落。

#### 章节顺序与承接

- **先列职责：**列全部 section 标题、每节目的、所需图表和预计篇幅。Related Work 按主题归类；Method 按真实处理依赖；Experiments 按要检验的问题。

中：Related Work 的“约束规划”小节归纳已有能力，再落到 Intro 中的约束遗漏。

EN: A Related Work subsection on constrained planning summarizes existing capabilities, then returns to the omission problem stated in the Introduction.

- **Method overview：**开头承接 Intro 的困难，串起输入、操作、输出和对应小节；最后引用 framework。章节名是阅读位置，别把章节标题写成执行模块。

中：为减少约束遗漏，我们先检索证据（证据检索节），再用检索结果核查约束（约束核查节），最后据此生成计划（计划生成节）。

EN: To reduce omitted constraints, we first retrieve evidence (Evidence Retrieval), use it to check constraints (Constraint Checking), and generate a plan from the checked constraints (Plan Generation).

- **篇幅：**按页数和贡献分配正文。同级小节任务量相近，篇幅也应接近；明显长的一节先查职责混杂和重复。复现细节放附录，关键比较条件留正文。

中：Method 某节讲了核查、训练和评估三件事，先拆职责，不靠缩字号解决。

EN: If a Method subsection mixes checking, training, and evaluation, separate its responsibilities instead of shrinking the font.

**正文骨架与 overview 句式**

```latex
\section{Introduction}
\section{Related Work}
\subsection{[Theme linked to challenge A]}
\subsection{[Theme linked to challenge B]}
\section{Method}
To address [the specific challenge], we [operation] in
[First Section] (\S\ref{sec:first}), producing [output].
Using [that output], we [next operation] in
[Second Section] (\S\ref{sec:second}), producing [next output].
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

这是起排骨架，按实际工作增删小节。方括号全部换成真实内容；framework 标签须对应实际图片。

#### 实验先整理成论证

- **问题与证据：**每项主张对应一个要检验的问题，再选对照、数据和图表。RQ 可以写，但不是给所有标题加一句问号。

中：主张“核查减少遗漏”，就比较同题、有核查与无核查的遗漏率，保持其他设置一致。

EN: To test whether checking reduces omissions, compare omission rates with and without checking on the same tasks under otherwise matched settings.

- **实验设置：**先说明数据与划分，再分别写 Metrics、Baselines 和 Implementation Details。指标给定义、方向和分母；基线给来源与配置；训练、推理预算和重复次数讲清。

中：成功率是满足全部任务约束的计划比例；基线与本文方法用同一测试集，分别说明推理预算。

EN: Success rate is the fraction of plans satisfying all task constraints. Evaluate the baseline and proposed method on the same test set and report their inference budgets.

- **实验顺序：**主结果回答整体是否有效；消融回答哪项设计有用；再按贡献安排成本、稳健性、迁移或失败分析。没有对应主张的实验，不必为了凑齐套餐硬加。

中：若声称更省计算，就同时报告成功率和成本；若只验证同域效果，就不写跨域泛化。

EN: A computational-efficiency claim requires both success and cost measurements. In-domain evidence alone does not establish cross-domain generalization.

- **结果段：**一句结论开头，接关键对照，再解释含义和范围。不要把表格逐行朗读一遍；均值更高也不自动等于显著提升。

中：核查后的提升主要出现在冲突条件下。接着引用该分组的对照，解释它怎样回应 Intro 的遗漏问题。

EN: The gains after checking are concentrated in conflicting conditions. Cite the subgroup comparison, then explain how it addresses the omission problem in the Introduction.

**给 Codex 的实验整理提示词**

```text
读取我的真实结果和 Intro 主张，按“研究问题 → 比较对象与固定条件 → 指标 → 图表 → 可支持的结论”整理。
先写 Experimental Setup，再排 Main Results、Ablation Studies 和必要分析。设置按 Metrics、Baselines、Implementation Details 分段。
每个结果段先给一句有证据的结论，再解释关键对照与范围。缺对照就说明还需什么，不补造结果，不用一个个案代替整体结论。
```

#### 表格：先让人看清比较

- **结构：**表承载实测结果和数据。模型按实际类型分组；列写指标、单位与好坏方向。三线表，少网格，同一指标保持精度一致。

中：方法名一列，成功率（%）一列，延迟（ms）一列；不同测试集分组，不混算平均。

EN: Use columns for method, success rate (%), and latency (ms). Separate test sets into groups rather than averaging incompatible results.

- **标记：**可比组内逐列判断：最优加粗，次优加下划线；需要时用很浅的底色。性能和成本方向不同，并列共享标记。颜色不能替你证明显著性。

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

Intro 是全文的逻辑压缩包。先用中文把“问题 → 设计 → 证据”讲通，再写英文；别让漂亮句子替你绕过逻辑。

#### Intro 先按这条线排

- **第一段：背景与已有能力：**第一句进入研究方向，紧接实际价值，再概括现有路线及已做到的事。别从宇宙大爆炸写到你的模型。

中：约束规划将任务要求转成可执行计划。现有方法能生成候选方案，并通过搜索或反馈改进。

EN: Constrained planning turns task requirements into executable plans. Existing methods generate candidates and refine them through search or feedback.

- **第二段：具体问题：**说在哪种条件下、哪个对象出了什么问题，为什么已有做法还不够。用文献或动机实验支撑，别把前人写成什么都没做。

中：然而，在要求彼此冲突时，计划仍可能遗漏关键约束，使后续步骤不可执行。

EN: However, under conflicting requirements, plans may still omit critical constraints, leaving later steps infeasible.

- **第三段：对应设计：**逐个回应上一段的问题。用“为解决 X，我们做 Y，因此得到 Z”串起来；关键术语就近解释，别只报模块名。

中：为减少遗漏，我们在规划前核查每项约束的证据，并把已核实的约束交给规划器。

EN: To reduce omissions, we check the evidence for each constraint before planning and pass the verified constraints to the planner.

- **接着：主要发现：**设计后紧接关键实验发现：和谁比、在什么条件下、支持哪项贡献。只写真实结果，别把“我们做了大量实验”当发现。

中：若实际结果支持：在相同测试任务下，核查减少了约束遗漏；消融说明这项收益来自核查环节。

EN: If supported by the actual results: On the same test tasks, checking reduces constraint omissions; the ablation attributes this gain to the checking step.

- **最后：贡献列表：**以 “In summary, our contributions are:” 收尾。每项一件主要贡献，长度接近；概括工作、关键设计、验证和发现，按实质内容写，不凑条数。

中：我们设计一个规划前证据核查步骤，在生成前识别缺少支持的约束。

EN: We design a pre-planning evidence check that identifies unsupported constraints before generation.

**Intro 中文提纲提示词**

```text
根据我的真实材料，先只写中文 Introduction 提纲。
第一段：研究方向、实际价值、现有路线与能力。
第二段：具体条件下的不足及依据。每个问题都必须有后文设计回应。
第三段：对应设计；解释输入、操作、产物及为什么能回应问题。
接着：实际主要发现和比较范围；没有结果就不要写结果句。
最后：贡献列表，平行、简短，不把普通工程步骤包装成创新。
逐句检查前一句是否为后一句提供了对象或前提；把问题、设计与实验逐项对应。先让我看中文，再写英文。
```

#### 人工审核，再填全文

- **审顺序：**每次给你一节中文，先查问题有没有回答、操作能不能复现、证据够不够。定下全部 section 标题后，再组织英文写回去。

中：先看 Method 的中文流程；确认核查输出确实进入规划器，再润色英语。

EN: Review the Method workflow in Chinese first. Confirm that the checked constraints actually enter the planner before polishing the English.

- **审一致：**Intro 的问题、Related Work 的不足、Method 的设计、实验的结论用同一套对象和名称。摘要随后压缩这条线，别另讲一个故事。

中：全文都说“约束遗漏”；不要到实验突然换成“综合智能不足”。

EN: Use “constraint omission” consistently instead of switching to an unrelated “lack of general intelligence” claim in the experiments.

- **审篇幅与图表：**编译看真实页数、图字、表格溢出和首次引用顺序。超页先删重复和无关细节，保留比较条件；逐句精修再去第三章。

中：结果段重复了整张成绩表，就删逐行报分，保留关键差异及其含义。

EN: If the result paragraph repeats the entire score table, remove the row-by-row narration and retain the key difference and its meaning.

教学例：计划要同时满足多个条件；已有方法能生成计划，但冲突条件下会遗漏约束；因此先核查证据，再规划；随后用主结果与消融检验这项设计。

Teaching example: Plans must satisfy multiple conditions. Existing methods generate plans but can omit constraints when conditions conflict. We therefore check evidence before planning, and test this design with main comparisons and ablations.

The Introduction compresses the argument of the paper. Make the problem, design, and evidence clear in Chinese before drafting the English.

## 全文表达要求与中英改写

#### 少夸，写做法

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

**第 2 句：**these passages 接住上一句的具体产物。

The generator uses the notes to produce an answer with citations.

生成器使用这些笔记，产生带引用的回答。

**第 3 句：**继续接住笔记，落到最终输出。

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

代词指代不清时换成对象名，清楚时保留。

教学改写：假设已有对应设计或比较，非论文原文与实测结果。

通用要求：指代清楚时保留代词，歧义时换成具体对象。

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

#### 好词有事实支撑

tailored、expert-confirmed、de-identified 能突出真实贡献。有依据就用，一词换一词，不堆形容词。

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

PaperBank 命名与粗斜体偏好；不为了凑贡献创造标签

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

#### 句子前后接上

后句处理前句的问题或产物，Then 和 Therefore 不能补逻辑。

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

**第 2 句：**方案真正接住约束冲突，Therefore 才有前提。

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

开头接输入，结尾交代输出如何进入下一步。

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

**第 1 句：**只描述实际测过的对象和指标，不能替未测语言盖章。

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

## 各章完整句式模板

#### 标题：对象、任务、改动

写清研究什么、解决什么。方法名放不放都行，标题要有内容。

教学模板；【】填真实材料。

- 少用 novel、powerful。保留研究对象，缩写和标题形式按领域习惯。

推荐骨架

[Method Name]: [Key Design] for [Task under the Specific Difficulty]

[方法名]：用[关键设计]解决[具体困难下的任务]。

**第 1 句：**冒号前是名字，后半句给出研究对象和实际改动。

[Specific Finding] in [Research Setting]

[研究场景]中的[具体发现]。

**第 2 句：**发现或 benchmark 论文也能用结果组织标题，不必伪装成方法论文。

#### 摘要：问题到结果

任务 → 缺口 → 方法 → 结果与范围。

教学模板；【】填真实材料。

- 首次出现的术语就近解释；摘要主张必须有正文支持。
- 保留关键发现、比较对象和必要数字，不逐项报分。

推荐骨架；长度按投稿要求

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

**第 5 句：**收束意义及范围；若与上一句重复就合并，不机械凑五句。

#### 引言第一段：方向与任务

方向、价值和任务紧凑交代，接着概括已有能力。

按论证顺序选用，段落可合并或拆分。

教学模板；【】填真实材料。

- 背景只留理解问题所需的信息；接下面的已有方法句式，共同组织首段。

PaperBank 推荐骨架

[Research direction] aims to [clear task objective] [citations].

[研究方向]旨在[清楚的任务目标][引用]。

**第 1 句：**先立研究对象，引用就近支持这个判断。

In [application], this capability matters because [evidence-supported value].

在[应用]中，这种能力影响[有依据的实际价值]。

**第 2 句：**用一句说明值得做，未经评估别写提高商业收益。

In this setting, [input] must be converted into [output] while satisfying [constraint].

在这一场景下，需要将[输入]转为[输出]，同时满足[约束]。

**第 3 句：**把大方向落到具体任务，接着概括已有解法做到哪一步。

#### 引言首段后半：已有方法

概括已有路线和已解决的问题，引用跟着主张走。

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

写清哪种方法、在哪些条件下、还有什么问题。

按论证顺序选用，段落可合并或拆分。

教学模板；【】填真实材料。

- 只讲后文有设计和实验对应的困难；标签后接解释。
- 先把问题讲完，再介绍方案。first、ignored、cannot 回查原文。

PaperBank 规范化写法

However, [existing capability] does not establish [missing property] when [condition].

然而，在[条件]下，[已有能力]仍不能说明[尚缺性质]成立。

**第 1 句：**说清评价或能力的证明边界，不把未证明改写成完全失败。

We call this difficulty [short name]: [plain-language meaning].

我们将这一困难称为[短名]，具体是指[普通语言解释]。

**第 2 句：**名字服务记忆，解释服务理解；不能靠名字替代问题。

For example, [concrete input or situation] requires [specific behavior], which [existing comparison] does not assess.

例如，[具体输入或场景]需要[具体行为]，而[对照评价]尚未检验这一点。

**第 3 句：**例子显示缺口怎样发生，是否未检验仍需核对实际来源。

#### 引言第三段：设计

按局限的顺序介绍方案，讲清每个设计改哪一步、为什么有用。

按论证顺序选用，段落可合并或拆分。

教学模板；【】填真实材料。

- 关键词、方法名与后文和框架图一致；机制是否成立留给实验验证。

PaperBank 规范化写法

To address [challenge A], we [design A] using [actual input or signal].

为解决[困难 A]，我们利用[实际输入或信号]设计[A 方案]。

**第 1 句：**一对一接回上一段的困难。

This design [specific operation], allowing [specific intended capability].

该设计通过[具体操作]，支持[明确的目标能力]。

**第 2 句：**解释如何发生，不只把方案换个词再说一遍。

To address [challenge B], we [design B].

为解决[困难 B]，我们采用[B 方案]。

**第 3 句：**第二项方案处理另一项真实问题；没有就删除，不凑模块。

#### 引言第四段：主要发现

设计之后写最重要的发现，再列贡献。

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

**第 2 句：**解释贡献及边界，不顺手扩大主张。

#### 引言最后：贡献列表

用 In summary, our contributions are: 引出原生 itemize，列表后进入下一节。

按论证顺序选用，段落可合并或拆分。

教学模板；【】填真实材料。

- 每项一个主要贡献：核心工作、设计、评价或发现；长度接近。
- 常用四项，按真实贡献增减。下载模板和写脚本不算创新。

PaperBank 规范化写法；不强凑条数

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

**第 5 句：**发现用真实结果写，不用 extensive experiments demonstrate effectiveness 糊弄。

**完整 LaTeX 骨架**

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

主标题后直接进 subsection，不写目录介绍。

教学模板；【】填真实材料。

- 每个主题：路线概括 → 机制分组 → 已有扩展 → 缺口 → 本文方案。引用跟着类别走。
- 每个小节都收尾：However 讲不足，To address / To solve 讲对应方案。
- 结尾的对象、范围、关键词与 Intro 一致；各小节讲不同缺口。
- 小节标题简短。短主题一段写完，复杂主题按问题分段。

PaperBank 规范化写法；主题数量按论文内容

[Research line] addresses [shared task] by [shared mechanism] [citations].

[研究路线]通过[共同机制]处理[共同任务][引用]。

**第 1 句：**第一句定义本小节主题，把真正相近的工作归成一类。

One group [mechanism A], whereas another group [mechanism B] [citations].

一类方法采用[机制 A]，另一类采用[机制 B][引用]。

**第 2 句：**分组必须有实质机制差别，不是换作者名字。

More recent extensions [additional established capability] [citations].

后续扩展进一步实现了[已有额外能力][引用]。

**第 3 句：**承接基本路线的扩展，不能为了显得新随便插文献。

However, these approaches do not establish [Intro challenge] under [specific scope].

然而，在[具体范围]内，这些方法尚未说明[引言中的问题]得到解决。

**第 4 句：**不足直接复用引言关键词，并限定到原文支持的边界。

To address this limitation, we [matching design] to [specific purpose].

为解决这个不足，我们通过[对应设计]实现[具体目的]。

**第 5 句：**方案与引言一致；这句写完就结束本小节，不再空泛 Next。

**完整 LaTeX 骨架**

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

#### Problem Formulation：任务定义

先说任务，再定义输入、输出、目标和约束。

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

#### Method Overview：完整模板

接 Intro 的问题，按实际流程讲输入如何变成输出。

教学模板；【】填真实材料。

- 用 in [准确章节名] (ref) 定位，每个章节名和引用出现一次；后句接前句产物。
- 每步写目的、输入、操作和输出；模块名与框架图一致，并行关系照实写。
- 末句引用框架图。已有章首总览就不另建 Overview；没有任务定义阶段就不补一节。
- 模板中的阶段按真实流程增删；主语用 we、模型或模块，不用章节名执行动作。

PaperBank 规范化写法；按真实依赖替换或删除阶段

To address [Intro challenge], in [Problem Formulation] (Section [ref]), we define [input] and [required output].

为解决[引言中的困难]，我们在[问题定义]（[真实节号]）中定义[输入]与[要求的输出]。

**第 1 句：**接动机、定任务，并用章节名导航；不是“Problem Formulation performs...” 。

Following this definition, in [Input Construction] (Section [ref]), we construct [inputs] from [verified source].

按照这一任务定义，我们在[输入构造]（[真实节号]）中从[已核验来源]构造[输入]。

**第 2 句：**承接任务定义，不凭空把定义写成数据产物。

Using [constructed inputs], in [Processing] (Section [ref]), we [operation] to obtain [intermediate output].

利用[已构造输入]，我们在[处理章节]（[真实节号]）中执行[操作]，得到[中间产物]。

**第 3 句：**上一句输出成为本句输入，目的和结果都有落点。

Given [intermediate output], in [Output Generation] (Section [ref]), we [operation] and produce [final output].

给定[中间产物]，我们在[输出生成]（[真实节号]）中执行[操作]，产生[最终输出]。

**第 4 句：**交代产物怎样进入下一步；实际并行则改成真实并行关系。

Figure [ref] summarizes this workflow.

图[真实编号]概括了这一流程。

**第 5 句：**收束到框架图，读者此时能把每个节点与正文对应。

**完整 LaTeX 骨架**

```latex
To address [the Intro challenge], in \textbf{[Problem Formulation]}
(\S\ref{sec:problem}), we define [input] and [required output].
Following this definition, in \textbf{[Input Construction]}
(\S\ref{sec:inputs}), we construct [inputs] from [verified source].
Using [constructed inputs], in \textbf{[Processing]}
(\S\ref{sec:processing}), we [operation] to obtain [intermediate output].
Given [intermediate output], in \textbf{[Output Generation]}
(\S\ref{sec:output}), we [operation] and produce [final output].
Figure~\ref{fig:framework} summarizes this workflow.
```

#### Method 小节：输入到输出

开头说接收什么、处理什么，结尾交代产物去向。

教学模板；【】填真实材料。

- 关键计算用编号公式，符号就近定义；长算法、完整 prompt 和参数表放附录。
- 粗体段首对应真实模块或步骤，名称与框架图一致。
- 并行、循环、反馈单独说明；训练信号注明样本、阶段、指标和更新对象。

通用要求；PaperBank 推荐句式

Using [previous output], we [operation] to [specific purpose].

利用[上一步产物]，我们通过[操作]实现[具体目的]。

**第 1 句：**一句同时承接前文并给本节任务。

For each [unit], we compute [quantity] from [signal source] under [condition].

对每个[计算单位]，我们在[条件]下从[信号来源]计算[量]。

**第 2 句：**操作落实到单位与来源，公式才有实际含义。

Here, [symbol] denotes [object], and [subscript] indexes [unit].

其中，[符号]表示[对象]，[下标]索引[单位]。

**第 3 句：**按公式实际需要逐一说明，不复制没用到的定义。

The resulting [output] is passed to [next step] for [purpose].

生成的[产物]交给[下一步]，用于[目的]。

**第 4 句：**末句启下；不存在这项依赖就如实改写。

#### Experiments：先列要验证的问题

主结果测效果，消融查组件，扩展查范围。先导航，再给细节。

教学模板；【】填真实材料。

- RQ 可用于组织，不必每表一个编号；标题写 Main Results、Ablation Studies 或具体目的。
- 按论文贡献选实验，不照搬另一类研究的实验清单。

通用要求；推荐骨架

After constructing [method or benchmark], we evaluate [actual target] on [scope].

构建[方法或基准]后，我们在[范围]内评价[实际对象]。

**第 1 句：**承接前章产物，先给比较范围。

We first test whether [design] improves [goal] under [fixed conditions].

我们先检验，在[固定条件]下，[设计]能否改善[目标]。

**第 2 句：**主结果回应 Intro 的问题，而不是临时找个漂亮指标。

We then isolate [component] and examine [robustness, efficiency, or transfer question].

随后，我们单独检验[组件]，并检查[稳健性、效率或迁移问题]。

**第 3 句：**只预告实际存在的分析，不能为了补齐模板虚构实验。

#### Experimental Setup：比较设置

先写数据来源、版本、划分和实测范围；使用子集就注明。

教学模板；【】填真实材料。

- Metrics：定义、方向、分母、汇总方式和无效输出处理。
- Baselines：路线、来源，以及共享或不同的模型、数据、输入和预算。
- Implementation Details：超参数、选择依据、硬件、运行次数、seed 和成本口径。开发集调参，测试集只评价。
- 人工或模型 judge：谁判什么、按什么判、核验多少。
- 这些是说明的分组，不是执行流程。

通用要求；Metrics/Baselines 为推荐组织

We evaluate [unit] from [dataset version], using [split or selection rule].

我们从[数据版本]中按[划分或选择规则]评价[样本单位]。

**第 1 句：**先定义谁进入比较，不能结果出来后悄悄换分母。

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

首句写发现，再引用图表、解释比较，回扣贡献。

教学模板；【】填真实材料。

- 保留关键条件和数字；全面胜出、显著、稳定都需要相应证据。
- 有利和不利指标一起解释；benchmark 写它区分或揭示了什么。

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

写固定什么、改什么，再给结果和解释。

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

重复运行查随机波动，敏感性查参数影响，迁移查新对象。

教学模板；【】填真实材料。

- 效率比较给端到端成本、资源和质量取舍；计入生成与审核。
- 每组先说为什么测、改什么、固定什么，再说发现和范围。

按贡献选用，不是必做套餐

To test [stability or transfer claim], we vary [factor] while holding [controls] fixed.

为检验[稳定或迁移主张]，我们改变[因素]，保持[控制项]不变。

**第 1 句：**问题与实际变化必须匹配。

We report [variation or outcome] across [repeat unit or new setting].

我们报告跨[重复单位或新设置]的[变化或结果]。

**第 2 句：**说清独立运行、样本和重复层级，不靠最好一次说明稳定。

These comparisons support [scope-limited finding], but do not establish [broader claim].

这些比较支持[有限范围的发现]，尚不能说明[更广主张]成立。

**第 3 句：**范围边界具体写；不是在每段末尾机械加免责声明。

#### Case Study：走一遍流程

给具体输入、关键处理和输出，解释成功或失败发生在哪一步。

教学模板；【】填真实材料。

- 保留原始文本、实测回复和标签；自构例子标清。案例不能代替总体结果。
- 位置按叙述需要安排；帮助理解评价时，也可放在总体结果之前。

通用要求；教学案例须明示

In [a recorded case or a stated constructed example], [input] requires [specific behavior].

在[有来源的真实案例或明示构造案例]中，[输入]要求[具体行为]。

**第 1 句：**先给来源类型与任务，不能让虚构案例穿上实测外套。

[Stage] uses [evidence] to produce [intermediate output].

[阶段]利用[证据]生成[中间产物]。

**第 2 句：**把可见处理与 framework 对上。

The final output [meets or violates requirement] because [observable evidence].

最终输出[满足或违反要求]，依据是[可见证据]。

**第 3 句：**判定与证据直接连接，不只写一个勾叉。

#### Discussion / Limitations：意义与局限

解释主要发现，再写可能原因和成立范围。

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

概括任务、贡献、发现和范围，不添新结果。

教学模板；【】填真实材料。

- 未来工作接已说明的局限；计划不能写成能力。

通用要求；推荐骨架

We studied [research problem] by [core design].

我们通过[核心设计]研究了[问题]。

**第 1 句：**回到起点，不重新铺领域背景。

The evaluation establishes [supported finding] under [conditions].

评价表明，在[条件]下，[有证据的发现]成立。

**第 2 句：**收束真正得到的认识。

[Specific limitation] motivates future evaluation in [relevant setting].

[具体局限]说明，后续需要在[相关设置]继续检验。

**第 3 句：**实际需要未来工作才写，不能机械凑末句。

#### References：回查原文

核对原文支持哪句话，以及来源、版本和书目信息。

教学模板；【】填真实材料。

- 同一论文不同版本去重；模型和工具引原始报告或官方文档。
- 按相关性选引用，不为年份或数量凑文献。

通用要求

[Grouped claim] [citations that actually support the claim].

[归类判断][真正支持该判断的引用]。

**第 1 句：**每条引用都服务近旁判断，不能只把出处堆在段尾。

We use [model or tool version] [original report or official documentation].

我们使用[模型或工具版本][原始报告或官方文档]。

**第 2 句：**记录实际使用版本，不能用后发布的模型文档装饰早期实验。

#### Appendix：实现与补充实验

按实现、实验设置、补充结果和证明分组。

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

一问一行：问什么、缺什么证据、用什么回答。

教学模板；【】填真实材料。

- 保留原话和原稿位置；先处理影响结论的问题。
- 缺基线与机制不清分开处理；二者需要不同对照。
- 查当轮字数、补实验、链接和修订稿规则。

The reviewer asks whether the gain comes from retrieval quality or answer generation.

审稿人问的是：收益来自检索质量，还是答案生成。

**第 1 句：**先说清真正的问题；这里要区分两种解释。

We compare the two generators using the same retrieved passages.

我们使用相同的检索段落比较两个生成器。

**第 2 句：**对照必须扣住问题：固定检索，改变生成器。

#### 4.2 逐题回复

答案 → 证据 → 解释 → 位置。

教学模板；【】填真实材料。

- 标题沿用原问题；首句给结论或具体值。
- 给设置、对照、绝对值和指标方向；数据适合表格就用表格。
- 说明证据如何回答问题，附表号、节号或行号。

The gain persists when retrieval is held fixed.

固定检索后，收益仍然存在。

**第 1 句：**首句直接回答；只有相应对照支持时才能用。

With identical passages and decoding settings, 【method】 scores 【A】 versus 【B】 for 【baseline】 on 【metric】 (higher is better; Table 【R1】).

使用相同段落和解码设置时，【方法】在【指标】上为【A】，而【基线】为【B】（越高越好；表【R1】）。

**第 2 句：**给协议、对照、绝对值和位置，别只报“提升显著”。

This comparison isolates the generator change under the tested retrieval setting.

这一比较在所测试的检索设置下隔离了生成器改动。

**第 3 句：**收束到已检验的范围，不顺手扩大到所有场景。

#### 4.3 区分两种解释

写出对方解释，用对照区分它与自己的解释。

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

先给定义或案例，再指到原文位置。

教学模板；【】填真实材料。

- 术语不清给定义，流程不清给案例，效果不清给对照。
- 确有错误就改；不同意就给依据。别写“你误读了”。

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

粗写 → 查问题 → 修改 → 回查 → 人工定稿。

教学模板；【】填真实材料。

- 给 Codex 论文、原始 review、证据和回复。
- 逐题输出：原问题、回复位置、剩余缺口、改法、所需证据。
- 先查漏答、证据和逻辑，再缩文字、调语气。改完重查同一张问题清单。
- 每问有答、证据对应、逻辑通顺、篇幅合规就停；缺实验交给人决定。
- 模拟用于查漏洞，不预测涨分或录用。

Concern: 【verbatim concern】. Response location: 【paragraph/table】. Remaining gap: 【specific gap】.

原问题：【审稿原话】。回复位置：【段落/表】。剩余缺口：【具体缺口】。

**第 1 句：**每条批评必须定位，不接受“还不够有说服力”这种空话。

Minimal fix: 【edit】. Required evidence: 【existing result or experiment needed】.

最小修改：【改法】。所需证据：【已有结果或需要的实验】。

**第 2 句：**把改文字和补证据分开，便于作者判断。

#### 4.6 第二轮与 AC 总结

第二轮答新增问题；AC 总结写问题、回应和证据。

教学模板；【】填真实材料。

- 追问接回原问题和证据，不重贴整份回复。
- 写清剩余限制，不猜未回复审稿人的态度。
- 不请求提分或接收，把判断留给审稿方。

Regarding the follow-up on 【issue】, 【direct answer】; the supporting comparison is in 【location】.

针对【问题】的追问，【直接答案】；支持这一答案的比较见【位置】。

**第 1 句：**只写新增信息。

The main concern was 【issue】. Our response provides 【evidence】, supporting 【bounded conclusion】.

主要关切是【问题】。回复提供了【证据】，支持【限定结论】。

**第 2 句：**AC 扫一眼能知道问题怎么被回答。

## 绘图规则与图型

- **先定图的任务：**动机图讲问题，方法图讲流程，结果图讲比较；无关元素删掉。

Show where the existing pipeline fails and which step our method changes.

画清旧流程在哪一步出问题，我们改了哪一步。

- **先画图，再精修正文：**用草图和真实数据定论证，先给合作者看。

Panel (a) shows the observed gap; panel (b) tests the proposed repair.

(a) 展示实际缺口；(b) 检验我们的修补。

- **统计图与概念图：**统计图用 Python 读真实数据；框架、动机和案例图用 imagegen。

Draw the recorded success rates with Python. Generate only the workflow illustration with imagegen.

成功率用 Python 按记录画；imagegen 只生成流程示意。

- **按最终尺寸排字：**按会议栏宽起稿，统一字体；图内字号为正文字号至小 2 pt。通栏约 16:9，单栏约 4:3，长图可纵排。

Use the paper’s column width and body font; remove repeated labels rather than shrinking text.

用论文栏宽和正文字体；删重复标签，不把字缩成蚂蚁。

- **按阅读顺序布局：**同层成组，主方向一致；并行、汇合、反馈按真实依赖画。箭头写清传什么。

Retrieved passages enter the generator; the evaluator receives the generated answer.

检索段落送给生成器；生成的回答交给评价器。

- **输入、输出、评分分开：**用边框或线型区分；仅供评价的分数不能画成模型输入。

Dashed boxes contain model inputs; solid boxes contain responses; dotted boxes contain evaluator-only criteria.

虚线框是模型输入，实线框是回复，点线框是只供评价的判据。

- **颜色表示类别：**白底、低饱和、同类同色；再配文字、形状或纹理，黑白也能读。

Blue circles denote the baseline; orange triangles denote our method in every panel.

每个面板都用蓝圆点表示基线，橙三角表示我们的方法。

- **文字分组，重点高亮：**案例按背景、证据、动作、结果排；同类信息同框，图标旁写名称。

The left column contains evidence; the right column shows the model response and its evaluation.

左栏放证据；右栏放模型回复和评价。

- **案例不重复贴：**同一案例在论文里只完整展示一次，其他位置交叉引用；案例讲流程，总体效果看实验。

Figure 1 presents the case; Section 4 refers back to Figure 1 without repeating the dialogue.

案例放图 1；第 4 节回引图 1，不再抄一遍对话。

- **多子图合讲一个问题：**按现象、诊断、对照、稳健性排列；同条件同顺序，相关横轴对齐。

The first panel identifies the gap, the second locates it, and the third tests whether it persists.

第一图找差距，第二图找发生位置，第三图检验差距是否仍在。

- **图形对应数值：**查分母、单位、方向、坐标起点和误差；相对增益给绝对值，显著性另看统计。

Accuracy rises from 60% to 66%: 6 percentage points, or a 10% relative increase.

准确率从 60% 到 66%：增加 6 个百分点，相对提高 10%。

- **图注写读法和发现：**主题句、子图含义、关键口径；解释缩写、误差和参考线。尽量三行，定义不能省。

Error bars show 95% question-level bootstrap intervals; the horizontal line marks zero gain.

误差条表示按题目重采样的 95% 区间；水平线表示零增益。

- **放回论文检查：**统计图优先矢量 PDF；生成图可叠原生文字。检查字号、裁切、图注和引用顺序。

Place the figure after its first mention and check all labels at normal reading size.

按首次引用顺序排图，以正常阅读大小检查全部文字。

- **摘要图：**问题在哪、为什么现有解法不够、我们动哪一步。通常最多 5 个环节，必要对照并排。

Show the problem, the existing limitation, and the changed step.

展示问题、已有解法的缺口和我们改动的步骤。

- **框架图：**输入是什么，经过哪几个模块，每步产物交给谁，输出是什么。旁边走一个可追踪例子。

Given a query, retrieve passages, rank evidence, and generate an answer with cited support.

输入问题，检索段落，筛选证据，再生成带来源的回答。

- **案例图：**必要背景、有效需求、关键证据、动作、结果、判据；同类信息同框。

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

- **ECDF：看阈值以下有多少：**横轴取阈值，纵轴直接读累计比例；同一坐标比两组，阶梯从 0 到 1。想读“多少样本低于 10”，别去量 KDE 的峰。

At a threshold of 10, the ECDF gives the fraction of observations at or below 10.

阈值取 10 时，ECDF 直接给出不超过 10 的样本比例。

- **热图：**条件乘方法，统一色标；正负增益以零为中点，缺测留空并说明。

Use one shared color scale for all conditions and mark missing cells.

全部条件使用统一色标，缺测单元明确标记。

- **PCA：把高维关系投到二维：**说明输入特征、标准化、每轴解释方差。颜色或轨迹分别代表什么写清；分得开不等于泛化好。PaCMAP、t-SNE 也别改名叫 PCA。

Project standardized features onto two principal components and report the variance explained by each axis.

把标准化特征投到两个主成分，并报告每根轴的解释方差。

- **雷达图：多指标逐轴读：**每轴一个指标，写尺度、归一化和好坏方向；颜色再配点形。量纲不同别比面积，轴换个顺序，面积也会换。

Compare normalized metrics spoke by spoke; polygon area is not an overall score.

沿每根轴比较归一化指标；多边形面积不是综合分数。

- **成本性能图：**每点是一个实际配置；在线与离线成本分开，写单位和好坏方向。连接前沿不意味着有中间配置。

Plot measured accuracy against online cost; report one-time training cost separately.

实测准确率对照在线成本；一次性训练成本另报。

- **数据集分布：**统计单位、样本量、类别和分母先写清；同一图别混案例数、回复数和判据数。重点是覆盖了什么，不是圆画得多圆。

Count unique cases by domain; report response counts separately.

按领域统计独立案例数；回复数量另报。

- **置信带：**按实际重采样或模型计算区间，写清区间类型和置信水平。同一估计的嵌套区间才可比较覆盖范围；不同样本量、方差也会改变带宽。

Nested bands show the estimated 68% and 95% intervals under the stated procedure.

嵌套色带表示按所述方法估计的 68% 和 95% 区间。

- **饼图、环图与圆环排名：**饼图只画互斥且组成整体的比例；圆环柱图可画排名，极值相邻只是环形排序，不是变量关系。要读精确差值，横向条图更方便。

Use slices for a composition and ordered bars for a ranking.

组成比例用扇区；排名用有顺序的柱条。

- **二维增益与九宫格：**两轴分别写指标、单位和好坏方向；差值图以零线分区。九宫格用于两个有序因素的组合，别为凑九格补数据。

With both gains defined as higher is better, the upper-right quadrant shows improvements on both metrics.

两个增益都定义为越高越好时，右上象限表示两项指标都改善。

原图与出处：[光速出美图](https://da1yuqin.github.io/PaperBank/#figure-gallery)。第三方图片不随 skill 分发。

---

原创规则与教学示例：Da1yuqin / PaperBank，[原文](https://da1yuqin.github.io/PaperBank/)，[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)。转载保留署名、出处及许可，改编注明改动。
