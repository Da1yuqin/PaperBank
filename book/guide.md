# PaperBank · 论文少走弯路指南

按论文顺序看每个自然段要完成什么，再逐句看中英例子与解释。

主要面向方法与实证研究；按学科、研究类型和投稿要求调整。模拟段落明确标注，真实论文摘录另给出处与版本。

欢迎使用、改写、转载，也欢迎拿去给 Codex 做 skill。原创内容采用 CC BY 4.0，论文摘录与图片保留各自许可。转载原创内容请保留作者 Da1yuqin、[原文链接](https://Da1yuqin.github.io/PaperBank/)和 [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) 许可，改过请注明。Star 自愿，署名别失联。

## 先让 Codex 粗写，再自己精挑

先把论文要讲的事写成一句话：现有办法哪里不够，你改了什么，结果说明什么。把已有结果、表格、参考论文段落和投稿模板交给 Codex，先列提纲，再按章粗写。引言按大领域、已有路线、具体局限、对应设计、主要结果来展开，最后列贡献；方法按输入输出讲流程，实验逐项回答引言的问题。粗稿先求讲通，不急着逐句磨英语。接着画引言图和方法图，用真实案例串起步骤，参考好图挑配色，曲线和表格由实验数据绘制。然后人工精挑：故事够不够集中，图有没有把创新讲明白，术语、符号和数值是否统一。最后把图放回论文，通读全文，修句间衔接和重复内容，同步摘要、图注与结论。每个设计要有明确作用，每个实验要有值得记住的发现，正文别把表格再念一遍。

**填什么：**把【】换成这七项材料：结果尽量贴表格，参考写法贴原段落；大文件填文件名并附上文件，缺结果写要检验的问题。

<details>
<summary>复制这个提示词</summary>

```text
请根据下面七项材料，先给论文提纲，再按章写可讨论的粗稿。

1. 目标会议：【会议／期刊名称、年份、篇幅要求】
2. 一句话贡献：【研究对象、具体困难、你的改动、最主要发现】
3. 已有方法局限：【现有路线、原文依据、在哪些条件下不够；给每项局限一个短名称】
4. 对应设计：【每项局限对应哪个模块／操作，以及为什么这样做】
5. 已有结果／表格：【结果表、指标定义、基线与对照条件、消融；缺的结果标出要检验什么】
6. 参考论文段落：【原文段落或论文与页码；说明希望参考哪种写法】
7. 文件／模板：【正文或源稿、图表与结果数据、投稿模板；要生成或修改哪些文件】

先按论文顺序列出各节要讲什么，检查困难、设计、结果和贡献是否逐项对应，再写粗稿。引言按“大领域→已有路线→具体局限→对应设计→主要结果”展开，最后列贡献；局限和设计分段，沿用同一组关键词。方法开头串起真实流程，交代每一步的输入、操作和输出。实验逐项回答引言的问题，解释发现，不复述整张表。

语言简洁直白，少用生词，句子别太长。必要术语首次出现就解释，同一对象全文用同一个名称；公式符号首次出现就定义，前后保持一致。缺结果处写【待填结果：指标、比较和位置】，不要替我编数字或文献。先把粗稿讲通，标出需要引言图、方法图或结果图的位置，暂不逐句打磨英语。
贡献句可适度用具体、正面的修饰词，如 de-identified、expert-confirmed、tailored；有事实依据就直接写，等量替换，不堆词加长。
```

</details>

<details>
<summary>English prompt</summary>

```text
Use the seven inputs below to propose an outline, then write a rough manuscript section by section for discussion.

1. Target venue: [Conference or journal, year, and page limit]
2. Contribution in one sentence: [Research object, concrete difficulty, our change, and main finding]
3. Limitations of existing methods: [Existing approaches, source evidence, and conditions where they fall short; give each limitation a short name]
4. Corresponding designs: [The module or operation addressing each limitation, and why it should help]
5. Available results and tables: [Result tables, metric definitions, baselines, control conditions, and ablations; state what any missing result should test]
6. Reference paper passages: [Original passages, or paper titles and page numbers; specify the writing pattern to follow]
7. Files and template: [Manuscript or source files, figures and result data, venue template, and files to create or edit]

First outline the job of each section in manuscript order. Match each difficulty with its design, supporting result, and contribution before drafting. Organize the Introduction as broader context, existing approaches, concrete limitations, corresponding designs, and main results, followed by the contributions. Keep limitations and designs in separate paragraphs and reuse the same keywords. Begin the Method with the actual process, stating the inputs, operations, and outputs of each step. Use the Experiments to answer the Introduction's questions and interpret findings rather than repeat every table value.

Use plain language, few unfamiliar terms, and short sentences. Explain necessary terms at first use, keep one name for each object, and define formula symbols when introduced. Use symbols consistently. For missing results, write [Result to fill: metric, comparison, and location]; do not invent numbers or references. Make the rough draft understandable and mark where an introduction figure, method figure, or result plot is needed. Do not polish sentences one by one yet.
Use factual, positive modifiers such as de-identified, expert-confirmed, or tailored where they fit. Replace modifiers without increasing word count; avoid piling them up.
```

</details>

**粗稿出来后，人工挑这四件事：**

- **挑故事：**把主要贡献压成一句话，删掉抢主线的支线；检查每项局限是否有对应设计和结果。
- **挑图和案例：**选参考图定配色，用真实案例走过方法；核对图中模块、步骤和正文名称。
- **核对术语和数据：**统一术语与符号，核对表格数值和指标方向；图缩到论文尺寸后，字和标记仍要看得清。
- **通读后逐句修：**图定下来再通读全文。检查每句和前句怎样相接，删重复；同步摘要、图注和结论。

<a id="writing-skill"></a>
## PaperBank 写作 skill：让 Codex 也按这份清单检查

把这份指南交给 Codex，按当前任务选规则；研究事实仍要回到原文、数据和实验记录。

[下载 ZIP](../assets/paperbank-writing-skill.zip) · [查看 SKILL.md](../skills/paperbank-writing/SKILL.md) · [32 条写作铁律](#rules)

下载、解压，保留整个 paperbank-writing/ 文件夹，把它交给 Codex 读取；补上文件、任务和允许修改的范围。

**中文使用提示词**

```text
请读取我提供的 paperbank-writing/SKILL.md。按本次任务选择 references/checklist.md 中适用的规则。先核对当前稿件的研究问题、贡献和证据；区分事实、推测与未完成工作，再检查术语、输入输出、图表和必要的审稿回复。保持原始数据、实验设置与记录不变。只处理我指定的文件与范围；如果本次只允许阅读，就给建议和摘录，不修改文件。缺少证据时说明缺口，不编造引用、结果或完成状态。先给主要问题、依据和最小改法，再执行已获授权的修改。
```

**English usage prompt**

```text
Read the supplied paperbank-writing/SKILL.md and select the rules in references/checklist.md that apply to this task. Check the current manuscript's research questions, contributions, and evidence first. Distinguish facts, hypotheses, and unfinished work; then check terminology, inputs and outputs, figures, and reviewer responses when relevant. Preserve the original data, experimental settings, and records. Work only within the files and scope I specify. For a reading-only task, provide advice and excerpts without editing files. Identify missing evidence rather than inventing citations, results, or completion status. Explain the main issues, supporting evidence, and minimal fixes, then make authorized changes.
```

<a id="rules"></a>

## 先记住这几条

- 先用一句话说清核心贡献；标题、摘要和引言围着它写。
- 先说现有方法卡在哪里，再说本文怎么改、为什么这样改。
- 一段只讲一件事；第一句给观点，后面的句子给解释或证据。
- 关键词全文一致；同一个东西别在正文、图和公式里换三个名字。
- 先解释操作，再给术语和符号；名字响亮不能代替方法说明。
- 贡献写新增内容和作用，别只把流程步骤当三项贡献。
- 贡献用具体、正面、有记忆点的词，如 de-identified、expert-confirmed、tailored；等量替换，不堆词加长。
- 结果先写发现，再指向关键数字；表格已经会报分，正文别当复读机。
- 方法按输入、处理、输出讲；图中的箭头对应真实信息流。

## 一篇论文的骨架

摘要把全文缩成一段；引言提出问题，方法给出做法，实验检查做法，讨论说明边界，结论收尾。具体按领域和投稿模板调整。

- 标题：让读者看清研究对象、任务和关键改动。
- 摘要：用一段交代问题、缺口、方法、主要结果和范围。
- 引言：背景与已有路线→局限→对应设计→主要结果→贡献列表。
- 相关工作：按问题组织文献，准确说明本文与最相近工作的差别。
- 方法：先定义任务，再按真实依赖说明输入、处理和输出。
- 实验：用公平比较回答研究问题，报告发现、取舍与条件。
- 讨论与局限：解释证据支持的意义，交代未覆盖条件与未证实原因。
- 结论：回到开头的问题，用已报告证据概括主要贡献。
- 参考文献：让每个引用对得到正确原文和实际版本。
- 附录：把补充细节放在容易找到、足以复核的位置。

逐句示范有论文原文短引，也有明确标注的模拟段落。原文例子来自不同论文，不拼接成同一篇完整论文；模拟部分用同一个假设任务串联。

## 目录

- [1. 标题](#title)
- [2. 摘要](#abstract)
- [3. 引言](#intro)
- [4. 相关工作](#related)
- [5. 方法](#method)
- [6. 实验](#experiments)
- [7. 讨论与局限](#discussion)
- [8. 结论](#conclusion)
- [9. 参考文献](#references)
- [10. 附录](#appendix)
- [11. 全文验收](#revision)
- [12. 起草与协作](#workflow)
- [13. AI辅助](#ai)
- [14. Rebuttal](#rebuttal)
- [好用工具与开源整理提示词](#tools)

<a id="title"></a>
## 1. 标题

让读者看清研究对象、任务和关键改动。

### 标题示范

用研究对象和关键改动让读者判断相关性。

论文原文短引 · 中文为本指南翻译

WebFilter 教 RAG 模型使用高级网页搜索工具，下面摘录论文标题。

Careful Queries, Credible Results: Teaching RAG Models Advanced Web Search Tools with Reinforcement Learning

谨慎查询，可信结果：通过强化学习教会 RAG 模型使用高级网页搜索工具。

**第 1 句：**冒号前给出记忆点，冒号后交代研究对象、搜索工具和强化学习；标题能让读者判断主题。

[Yuqin Dai et al. (AAAI 2026) · Careful Queries, Credible Results: Teaching RAG Models Advanced Web Search Tools with Reinforcement Learning](https://ojs.aaai.org/index.php/AAAI/article/view/40299) · Title，PDF第1页（刊页30458）；AAAI 2026 camera-ready；2026-03-14正式发表

<details>
<summary>检查清单和真实论文例子（4 项）</summary>


**对象与贡献**

- [ ] **第 9 条：**标题写清研究对象与主要内容；少用缩写，结论型标题限定适用范围。

<a id="tip-09"></a>
<details>
<summary>说明、例子与参考</summary>

可分别试问题型、方法型和发现型标题。让不熟悉项目的人读一遍，检查读出的内容是否符合真实贡献。

**边界：**结论型标题尤其要收住范围。只在几种条件下成立的发现，别写得像普遍规律。

**标题同时交代工具与训练方式**

**论文原文 · English**

> Careful Queries, Credible Results: Teaching RAG Models Advanced Web Search Tools with Reinforcement Learning

**中文翻译 · 本指南翻译**

谨慎查询，可信结果：通过强化学习教会 RAG 模型使用高级网页搜索工具。

**逐句拆解**

1. 前半句给读者一个好记的结果方向；冒号后立即交代研究对象、工具和训练方式。
2. 只留下 Careful Queries, Credible Results 会让人猜主题。完整标题的后半句把主题落到了 RAG、网页搜索工具和强化学习。
3. “可信结果”是标题的主张，仍需正文中的来源质量与回答评价支撑，不能当作已自动证明的属性。

**摘录出处：**[Yuqin Dai et al. (AAAI 2026) · Careful Queries, Credible Results: Teaching RAG Models Advanced Web Search Tools with Reinforcement Learning](https://ojs.aaai.org/index.php/AAAI/article/view/40299)；Title，PDF第1页（刊页30458）；AAAI 2026 camera-ready；2026-03-14正式发表；已发表；作者源稿摘录

**原文／图片许可：**Yuqin Dai et al., AAAI 2026, pp.30458–30466. ©2026 AAAI，保留原版权；作者教学短引，不随本指南转授再版许可。中文为本指南翻译，拆解与教学改写单独标注。

来源与延伸阅读：[作者提供的写作、绘图与进阶笔记](https://github.com/Da1yuqin/PaperBank/blob/main/SOURCES.md#写作笔记)；[Mensh & Kording (2017) · Ten simple rules for structuring papers](https://doi.org/10.1371/journal.pcbi.1005619)；[NeurIPS · Paper Checklist](https://neurips.cc/public/guides/PaperChecklist)；[Yuqin Dai et al. (AAAI 2026) · Careful Queries, Credible Results: Teaching RAG Models Advanced Web Search Tools with Reinforcement Learning](https://ojs.aaai.org/index.php/AAAI/article/view/40299)

</details>

- [ ] **第 4 条：**先写实际操作，再定名称与比喻；名称不能暗示未验证的能力。

<a id="tip-04"></a>
<details>
<summary>说明、例子与参考</summary>

想用类比，就逐项说明类比对应哪种操作。拿掉名字和形容词，读者仍应知道你做了什么。

**边界：**别拿流行术语凑新意。名字拿掉以后，贡献也应该站得住。

**UrbanZero：解释“自进化”究竟做了什么**

**教学改写：依据 UrbanZero 公开项目介绍，非论文原文**

依据公开项目介绍中的语义简报、地块任务、逐块规划和程序反馈编写。中英示例为本指南教学改写；实验问题和模拟回复方案不代表项目已完成的工作。

**改前 · 中文**

我们提出一个会自己变聪明的城市规划模型。

**Before · English**

We propose an urban planner that makes itself smarter.

**改后 · 中文**

UrbanZero 让同一模型提出规划任务并逐块求解，再用程序检查的结果反馈调整后续任务。

**After · English**

UrbanZero uses one model to propose planning tasks and solve them patch by patch. Programmatic checks provide outcome feedback for later task generation.

**逐句拆解**

1. 把“自己变聪明”换成角色、动作和反馈来源，名称才有可核对的含义。
2. 无专家监督不等于没有人为定义：任务编译规则与检查目标仍需说明。

来源与延伸阅读：[作者提供的写作、绘图与进阶笔记](https://github.com/Da1yuqin/PaperBank/blob/main/SOURCES.md#写作笔记)；[Chaoyang Shi, Yuqin Dai et al. · UrbanZero（公开项目介绍）](https://github.com/Da1yuqin/Da1yuqin.github.io/blob/main/_pages/includes/pub.md#L193-L202)

</details>

- [ ] **第 81 条：**同一对象用固定术语；代词可能指向多个对象时，换成简短对象名。

<a id="tip-81"></a>
<details>
<summary>说明、例子与参考</summary>

读者不应靠猜来确定谁做什么。准确优先，不为词汇变化重复改名。

**边界：**适用：方法对象、状态、指标和跨章节措辞。这是推荐写法，按论文类型和当前投稿要求调整；清晰的代词和必要的长句可以保留。

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

来源与延伸阅读：[写作技能与检查方法](https://github.com/Da1yuqin/PaperBank/blob/main/SOURCES.md#写作技能)

</details>

- [ ] **第 71 条：**每个结论写清测试对象与条件；局部结果不推广全部任务，平均提升不保证每例。

<a id="tip-71"></a>
<details>
<summary>说明、例子与参考</summary>

说明结果在哪些任务、模型或人群成立，再解释证据支持的范围。

**边界：**适用：正文、摘要、标题、结论和回复审稿意见。证据与记录必须如实；不适用的检查注明原因。

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

来源与延伸阅读：[写作技能与检查方法](https://github.com/Da1yuqin/PaperBank/blob/main/SOURCES.md#写作技能)

</details>


</details>


<a id="abstract"></a>
## 2. 摘要

用一段交代问题、缺口、方法、主要结果和范围。

### 摘要·示范自然段1

一段给出问题、缺口、设计、结果和必要范围。

论文原文短引 · 中文为本指南翻译

PlanCraft 从不完整草图生成住宅场景，下面摘录摘要里的两句方法说明，不是完整摘要。

PlanCraft-Diff progressively sharpens an incomplete sketch into a geometrically precise, vectorizable floor plan through a coarse-to-fine strategy.

PlanCraft-Diff 通过由粗到细的策略，将不完整草图逐步细化为几何精确、可转为矢量的平面图。

**第 1 句：**先给输入、操作和产物：不完整草图经由粗到细处理，得到可矢量化的平面图。

With the spatial contract established, PlanCraft-Agent then furnishes the scene within well-defined room boundaries.

有了这份空间约束，PlanCraft-Agent 随后在明确的房间边界内为场景布置家具。

**第 2 句：**随后接住上一句的房间边界，再说家具装配；两个模块由产物连起来。

[Zeng, Dai et al. (2026 预印本) · PlanCraft: Sketch, Refine, and Furnish for Architect-Inspired Progressive 3D Residential Scene Generation](https://arxiv.org/abs/2607.23491v3) · Abstract，PlanCraft-Diff 与 PlanCraft-Agent 两句；PDF 第 1 页；arXiv:2607.23491v3，2026-09-05；短引对照作者源稿及公开 v3 正文

<details>
<summary>检查清单和真实论文例子（7 项）</summary>


**问题、方法与结果**

- [ ] **第 1 条：**用一句话写清研究对象、现有困难、你的改动和结果；删掉方法名，贡献仍要具体。

<a id="tip-01"></a>
<details>
<summary>说明、例子与参考</summary>

先写一句，再展开成一段。说不清时，先查是表达混乱还是证据不足，再润色英语。

**边界：**有时是表达没理顺，有时是证据还不够。先分清是哪一种，别让流畅的文字替你做判断。

**TCDiff：方法名之外，把动作与代价说清**

**论文原文 · English**

> To address these challenges, we propose a Trajectory-Controllable Diffusion (TCDiff) framework, which leverages non-overlapping trajectories to ensure coherent and aesthetically pleasing dance movements.

**中文翻译 · 本指南翻译**

为解决这些困难，我们提出轨迹可控扩散框架 TCDiff，利用不重叠轨迹来生成协调且具有美感的舞蹈动作。

**逐句拆解**

1. 先读出具体操作：先生成不同舞者的位置轨迹，再据此生成动作。去掉 TCDiff 名字，核心操作仍然成立。
2. collisions / foot sliding 的前文问题对应轨迹与脚步处理；“协调、美观”还要落到群舞、脚滑指标和用户研究，不能拿形容词代替结果。
3. Table1 的群舞真实感 GMR 从 CoDancers 的 26.10 到 13.86（越低越好），但 TCDiff 的个体保真度 FID 为 37.47、CoDancers 为 23.98。因此示范摘要要保留收益与代价。

**教学改写 · English（非论文原文）**

TCDiff generates dancer trajectories before motion. On AIOZ-GDance, it improves group-motion realism relative to CoDancers (GMR: 26.10 to 13.86, lower is better), with a trade-off in individual fidelity (FID: 23.98 to 37.47, lower is better).

**教学改写 · 中文（非论文原文）**

TCDiff 先生成舞者轨迹，再生成动作。在 AIOZ-GDance 上，相比 CoDancers，群舞真实感 GMR 从 26.10 降到 13.86，但个体保真度 FID 从 23.98 升到 37.47；两个指标都越低越好。

**摘录出处：**[Yuqin Dai et al. (AAAI 2025) · Harmonious Music-driven Group Choreography with Trajectory-Controllable Diffusion](https://ojs.aaai.org/index.php/AAAI/article/view/32268)；Abstract, PDF p.1 / proceedings p.2645；方法 §TCDiff；Table1, p.2650；正式发表论文；已发表；作者原文摘录

**原文／图片许可：**Yuqin Dai et al., AAAI 2025, pp.2645–2653. ©2025 AAAI，保留原版权；作者教学短引，不纳入本指南原创内容的 CC BY 许可。中文为本指南翻译。

来源与延伸阅读：[作者提供的写作、绘图与进阶笔记](https://github.com/Da1yuqin/PaperBank/blob/main/SOURCES.md#写作笔记)；[Mensh & Kording (2017) · Ten simple rules for structuring papers](https://doi.org/10.1371/journal.pcbi.1005619)；[NeurIPS · Paper Checklist](https://neurips.cc/public/guides/PaperChecklist)；[Yuqin Dai et al. (AAAI 2025) · Harmonious Music-driven Group Choreography with Trajectory-Controllable Diffusion](https://ojs.aaai.org/index.php/AAAI/article/view/32268)

</details>

- [ ] **第 10 条：**摘要依次交代具体问题、已有困难、关键方法和主要结果；按投稿要求控制篇幅。

<a id="tip-10"></a>
<details>
<summary>说明、例子与参考</summary>

每句话接住前一句，讲清做什么、为什么做、怎么做和结果怎样。型号与实现细节只留理解主线所必需的。

**边界：**摘要字数和格式看投稿要求。别把别人那篇的字数当成自己的标准。

**PlanCraft：摘要中的方法句沿产物流向衔接**

**论文原文 · English**

> PlanCraft-Diff progressively sharpens an incomplete sketch into a geometrically precise, vectorizable floor plan through a coarse-to-fine strategy. With the spatial contract established, PlanCraft-Agent then furnishes the scene within well-defined room boundaries.

**中文翻译 · 本指南翻译**

PlanCraft-Diff 通过由粗到细的策略，将不完整草图逐步细化为几何精确、可转为矢量的平面图。有了这份空间约束，PlanCraft-Agent 随后在明确的房间边界内为场景布置家具。

**逐句拆解**

1. 第一句产出平面图，第二句接住房间边界，再说明家具装配；两个模块的关系由产物解释，没有只并列名称。
2. 这两句位于摘要中部。前文先讲渐进设计与空间先验，后文再给 FID 和专家评分；摘录方法句不等于展示了完整摘要。
3. 教学改写保留“困难—动作—评价对象”的顺序；具体数字和 strongest 等比较范围必须回到原表核对。

**教学改写 · English（非论文原文）**

Architects refine incomplete sketches, while fully specified inputs leave this process unsupported. PlanCraft completes a sketch into a verified floor plan, then furnishes the bounded rooms. The reported evaluations compare floor-plan quality and expert-rated scene rationality.

**教学改写 · 中文（非论文原文）**

建筑师会逐步细化不完整草图，完整输入的要求难以支持这个过程。PlanCraft 先将草图补全为经过检查的平面图，再在房间边界内装配家具。原文评价分别比较平面图质量和专家评定的场景合理性。

**摘录出处：**[Zeng, Dai et al. (2026 预印本) · PlanCraft: Sketch, Refine, and Furnish for Architect-Inspired Progressive 3D Residential Scene Generation](https://arxiv.org/abs/2607.23491v3)；Abstract，PlanCraft-Diff 与 PlanCraft-Agent 两句；PDF 第 1 页；arXiv:2607.23491v3，2026-09-05；短引对照作者源稿及公开 v3 正文；公开预印本；教学改写不是论文原文或新增实测结果

**原文／图片许可：**Pengyu Zeng et al., arXiv:2607.23491v3 (2026). arXiv 为非独占分发许可，原文版权由权利人保留；作者授权的教学短引，不随本指南转授全文或原图再版许可。中文翻译、拆解及教学改写为本指南新增。

来源与延伸阅读：[写作技能与检查方法](https://github.com/Da1yuqin/PaperBank/blob/main/SOURCES.md#写作技能)；[Mensh & Kording (2017) · Ten simple rules for structuring papers](https://doi.org/10.1371/journal.pcbi.1005619)；[NeurIPS · Paper Checklist](https://neurips.cc/public/guides/PaperChecklist)；[Zeng, Dai et al. (2026 预印本) · PlanCraft: Sketch, Refine, and Furnish for Architect-Inspired Progressive 3D Residential Scene Generation](https://arxiv.org/abs/2607.23491v3)

</details>


**词语、数字与主张**

- [ ] **第 11 条：**先讲操作和原因，再给名称；必要术语首次解释，影响复现的版本后文交代。

<a id="tip-11"></a>
<details>
<summary>说明、例子与参考</summary>

摘要和引言先用普通话讲清动作。名称不能替代定义，少用术语也不能省略模型版本和实验设置。

**边界：**容易懂不等于随便写。模型是什么、用哪个版本、实验怎么做，后文仍要准确交代。

**SAGE：图节点先说各自做什么**

**论文原文 · English**

> We formalize each SOP as a directed graph G = (V, E) with three node types: Start/End, Decision (branching on conditions), and Action nodes.

**中文翻译 · 本指南翻译**

我们将每个标准操作流程（SOP）形式化为有向图 G = (V, E)，图中有三类节点：开始／结束节点、按条件分支的决策节点，以及动作节点。

**逐句拆解**

1. 三类节点后立即解释 Decision 是按条件分支，读者先知道动作，再记术语。
2. G 是整个流程图；V、E 在数学表示中分别对应节点和边。写自己的方法时，这两个符号也应就近定义。
3. 图的表示方式不能代替评价可靠性证据；具体标签、转移条件和动作仍需在方法中说明。

**摘录出处：**[Ling Shi, Yuqin Dai et al. · SAGE: An Extensible Benchmark for Service Agent Graph-guided Evaluation](https://arxiv.org/abs/2604.09285)；§ Universal Dialogue Graph Modeling，有向图定义段（作者源稿第 471 行）；作者终稿 2026-10-04 只读快照；公开链接为 arXiv v1；作者终稿短引；公开链接为不同版本预印本

**原文／图片许可：**作者终稿教学短引，保留原论文版权；不随 PaperBank 原创内容转授终稿转载权。公开 arXiv v1 的 CC BY 4.0 已核验，该许可不自动延伸到不同版本的作者终稿。

来源与延伸阅读：[写作技能与检查方法](https://github.com/Da1yuqin/PaperBank/blob/main/SOURCES.md#写作技能)；[Ling Shi, Yuqin Dai et al. · SAGE: An Extensible Benchmark for Service Agent Graph-guided Evaluation](https://arxiv.org/abs/2604.09285)

</details>

- [ ] **第 82 条：**中间量说明来自哪个样本、阶段和指标，用于哪个对象；必要下标逐一解释。

<a id="tip-82"></a>
<details>
<summary>说明、例子与参考</summary>

名称不能代替定义。读者应能追到量怎样得到、怎样使用。

**边界：**适用：学习信号、符号和中间量定义。这是推荐写法，按论文类型和当前投稿要求调整；清晰的代词和必要的长句可以保留。

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

来源与延伸阅读：[写作技能与检查方法](https://github.com/Da1yuqin/PaperBank/blob/main/SOURCES.md#写作技能)

</details>

- [ ] **第 80 条：**一句承担一项主要判断，一段完成一个任务；必要条件保留，拆句后仍要连贯。

<a id="tip-80"></a>
<details>
<summary>说明、例子与参考</summary>

把目的、操作和结果说清。多个独立结论可以分段，不能把长句切成互不承接的碎片。

**边界：**适用：正文、图注和附录说明。这是推荐写法，按论文类型和当前投稿要求调整；清晰的代词和必要的长句可以保留。

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

来源与延伸阅读：[写作技能与检查方法](https://github.com/Da1yuqin/PaperBank/blob/main/SOURCES.md#写作技能)

</details>

- [ ] **第 73 条：**分清记录数与独立样本、百分比与百分点；结果使用对应版本和协议。

<a id="tip-73"></a>
<details>
<summary>说明、例子与参考</summary>

原数、统计单位、分母和变化尺度写清。新结果另报，不覆盖旧实验记录。

**边界：**适用：数据规模、通过率、效果差异。证据与记录必须如实；不适用的检查注明原因。

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

来源与延伸阅读：[写作技能与检查方法](https://github.com/Da1yuqin/PaperBank/blob/main/SOURCES.md#写作技能)

</details>


**摘要与正文同步**

- [ ] **第 12 条：**摘要逐句对到正文证据，核对方法名、对象、数据范围和完成状态；同步标题与结论。

<a id="tip-12"></a>
<details>
<summary>说明、例子与参考</summary>

正文收回的结论，摘要也要收回。压缩可省细节，不能把有限结果写成全面胜出。

**边界：**压缩可以省细节，不能顺便把有限结果写成全面胜出。

**EviNoteRAG：摘要涨分逐项回到结果表**

**论文原文 · English**

> with relative F1 gains of 20% on HotpotQA (+0.093), 40% on Bamboogle (+0.151), and 91% on 2Wiki (+0.256)

**中文翻译 · 本指南翻译**

HotpotQA、Bamboogle、2Wiki 上的 F1 相对增幅分别为 20%、40%、91%，对应绝对增量为 0.093、0.151、0.256。

**逐句拆解**

1. 这段摘要同时给相对增幅和绝对增量。回查终稿主结果表，Search-R1 与 EviNoteRAG 在三项上的 F1 分别为 0.464→0.557、0.377→0.528、0.280→0.536。
2. 例如 2Wiki 的绝对差是 0.256，相对增幅约为 0.256/0.280 = 91%；不能把这两种口径互换。
3. 摘要要随正文的基线、数据范围和指标同步。原表中并非每项都最高，不能把选取的三项涨分改成所有任务全面胜出。

**摘录出处：**[Yuqin Dai et al. · EviNoteRAG: Enhancing RAG Models via Quality-Augmented Evidence Notes](https://arxiv.org/abs/2509.00877)；Abstract，结果句中的连续子句，PDF 第 1 页；核对 § Experiments 的主结果表（Table 1，PDF 第 5 页）；EMNLP 2026 revised 作者终稿；公开链接为 arXiv v3；作者终稿短引；公开链接为不同版本预印本

**原文／图片许可：**作者终稿教学短引，保留原论文版权；不随 PaperBank 原创内容转授原论文再版许可。公开 arXiv v3 为 non-exclusive distribution，并非 CC 授权；代码 Apache 2.0 不作为论文许可。

来源与延伸阅读：[写作技能与检查方法](https://github.com/Da1yuqin/PaperBank/blob/main/SOURCES.md#写作技能)；[Yuqin Dai et al. · EviNoteRAG: Enhancing RAG Models via Quality-Augmented Evidence Notes](https://arxiv.org/abs/2509.00877)

</details>


</details>


<a id="intro"></a>
## 3. 引言

背景与已有路线→局限→对应设计→主要结果→贡献列表。

### 引言·示范自然段1：任务与需求

从读者能理解的具体任务说明为什么值得研究。

教学例句，非论文原文或实测结果。

A support assistant often answers follow-up questions about a technical manual.

技术支持助手常要根据手册回答追问。

**第 1 句：**用一个实际任务建立语境，背景到够用就停。

A useful answer must satisfy earlier constraints and identify its supporting passages.

有用的回答既要满足前文约束，也要指出支持它的片段。

**第 2 句：**交代任务要求，后面的评价才有依据。

### 引言·示范自然段2：领域回顾

按路线概括已有进展，为下一段具体局限埋下伏笔。

论文原文短引 · 中文为本指南翻译

EviNoteRAG 研究检索后的证据使用，下面摘录引言里回顾已有 RAG 路线的一句。

To address this limitation, Retrieval-Augmented Generation (RAG) has emerged by incorporating a search tool that supplies up-to-date external evidence at inference time, enabling models to ground their responses in timely information and improve factual consistency.

为应对这一局限，检索增强生成（RAG）引入搜索工具，在推理时提供最新外部证据，让模型依据及时信息作答，并改善事实一致性。

**第 1 句：**先承接模型知识的局限，再概括既有路线：在推理时引入外部搜索证据；下一段才展开检索后仍有什么困难。

[Yuqin Dai et al. · EviNoteRAG: Enhancing RAG Models via Quality-Augmented Evidence Notes](https://arxiv.org/abs/2509.00877) · § 1 Introduction，第一段最后一句，PDF 第 1 页；作者终稿 content/01_introduction.tex；EMNLP 2026 revised 作者终稿；公开链接为 arXiv v3

### 引言第3段：现有方法的局限

接着上一段的做法，说清它在哪里不够用。下一段逐点解决。

教学例句，非论文原文。

假设前文介绍了按当前问题检索片段的问答方法。

However, passage relevance does not tell the generator which earlier constraints still apply.

但片段相关性不能告诉生成器，哪些前文约束仍然适用。

**第 1 句：**However接上一段的相关性检索；局限从它的做法里引出。

For example, a passage may recommend an online service even when the user previously requested offline operation.

例如，片段可能推荐在线服务，而用户之前要求离线操作。

**第 2 句：**一个具体例子解释约束遗漏，不让读者靠新名词猜意思。

### 引言·示范自然段4：方法逐点回应

每项设计都接回上一段的具体困难。

论文原文短引 · 中文为本指南翻译

TCDiff 生成多舞者群舞，下面用摘要里的设计句示范如何回应引言困难，不是整段引言。

To mitigate collisions, we introduce a Dance-Trajectory Navigator that generates collision-free trajectories for multiple dancers, utilizing a distance-consistency loss to maintain optimal spacing.

为减少碰撞，我们引入舞蹈轨迹导航器，为多名舞者生成无碰撞轨迹，并利用距离一致性损失维持合适间距。

**第 1 句：**To mitigate collisions 接住碰撞问题；轨迹导航器给出操作，距离一致性损失说明怎样维持舞者间距。

[Yuqin Dai et al. (AAAI 2025) · Harmonious Music-driven Group Choreography with Trajectory-Controllable Diffusion](https://ojs.aaai.org/index.php/AAAI/article/view/32268) · Abstract, PDF p.1 / p.2645；Table1, PDF p.6 / p.2650；正式发表论文

### 引言：设计之后，紧接主要结果

说完怎么解决，马上交代实验发现；最后再列贡献。

论文原文短引 · 中文为本指南翻译

接着 TCDiff 的设计句，看同一论文如何概括结果；原句位于实验分析。

TCDiff effectively captures inter-dancer correlations (high GMC) with a slight trade-off in individual fidelity (FID).

TCDiff 能较好捕捉舞者间相关性（GMC 较高），同时在个体保真度（FID）上存在一定代价。

**第 1 句：**报告整体协同性收益与个体保真度代价。这不是轨迹导航器单独作用的证据，模块作用另看消融。

[Yuqin Dai et al. (AAAI 2025) · Harmonious Music-driven Group Choreography with Trajectory-Controllable Diffusion](https://ojs.aaai.org/index.php/AAAI/article/view/32268) · §Quantitative Results，第3句；PDF p.6，proceedings p.2650；Table 1；正式发表版本；作者原文短引

### 引言·贡献列表

把贡献写成新增内容和验证方式，而非任务清单。

论文原文短引 · 中文为本指南翻译

PlanCraft 连接草图补全与场景装配，下面摘录引言贡献列表的第一项。

We identify two overlooked structural insights, design is progressive and the floor plan is a spatial prior, and propose PlanCraft, the first unified system that bridges incomplete design sketches to fully furnished 3D residential scenes.

我们指出两项此前未被充分注意的结构性认识：设计是渐进的，平面图是空间先验；并提出 PlanCraft 这一首个将不完整设计草图连接到完整带家具三维住宅场景的统一系统。

**第 1 句：**先写两条认识，再落到同一个输入输出任务：不完整草图到带家具住宅场景；贡献不只是罗列组件。

[Zeng, Dai et al. (2026 预印本) · PlanCraft: Sketch, Refine, and Furnish for Architect-Inspired Progressive 3D Residential Scene Generation](https://arxiv.org/abs/2607.23491v3) · Introduction，贡献列表第 1 项；PDF 第 2 页；arXiv:2607.23491v3，2026-09-05；短引对照作者源稿及公开 v3 正文

### 贡献措辞：给读者几个记得住的词

有事实依据就直接写。换掉没信息的修饰词，别给每个名词戴三顶帽子。

教学例句，非论文原文。

We release de-identified conversations for evaluating recommendation agents.

我们公开去标识化的对话，用于评估推荐智能体。

**第 1 句：**de-identified 点出隐私处理；比笼统的 processed 更有信息。

The agent requests additional help when a plan fails.

计划失败时，智能体会请求额外帮助。

**第 2 句：**additional help 把辅助能力写成动作，读者容易记住。

We evaluate citation accuracy using expert-confirmed labels.

我们使用专家确认的标签评估引用准确率。

**第 3 句：**expert-confirmed 点出标签质量，也带出人工投入。

A tailored prompt guides each role in checking the evidence.

各角色使用定制提示词核查证据。

**第 4 句：**tailored 点出针对性；无需在贡献句里展开提示词细节。

<details>
<summary>检查清单和真实论文例子（17 项）</summary>


**任务与已有进展**

- [ ] **第 13 条：**保留理解问题所需的背景；讲完现有做法就进入具体困难，文献按相关性选。

<a id="tip-13"></a>
<details>
<summary>说明、例子与参考</summary>

从应用或研究需求切入，只铺垫后面真正要处理的步骤。相关历史工作保留，不按年份一刀切。

**边界：**相关的历史工作该留就留，不按年份一刀切，也不为了数量堆文献。

**EviNoteRAG：背景直接铺到外部证据**

**论文原文 · English**

> To address this limitation, Retrieval-Augmented Generation (RAG) has emerged by incorporating a search tool that supplies up-to-date external evidence at inference time, enabling models to ground their responses in timely information and improve factual consistency.

**中文翻译 · 本指南翻译**

为应对这一局限，检索增强生成（RAG）引入搜索工具，在推理时提供最新外部证据，让模型依据及时信息作答，并改善事实一致性。

**逐句拆解**

1. 前句讲模型知识可能过时，这句紧接外部检索的应对方式；背景只铺到后文要分析的证据使用环节。
2. 下一段进入检索内容有噪声与多跳错误累积，而不是继续介绍整个 LLM 发展史。
3. 最新证据是工具的目标，不代表任意检索结果都新或可信；写自己的研究时，仍要说明来源与时间条件。

**摘录出处：**[Yuqin Dai et al. · EviNoteRAG: Enhancing RAG Models via Quality-Augmented Evidence Notes](https://arxiv.org/abs/2509.00877)；§ 1 Introduction，第一段最后一句，PDF 第 1 页；作者终稿 content/01_introduction.tex；EMNLP 2026 revised 作者终稿；公开链接为 arXiv v3；作者终稿短引；公开链接为不同版本预印本

**原文／图片许可：**作者终稿教学短引，保留原论文版权；不随 PaperBank 原创内容转授原论文再版许可。公开 arXiv v3 为 non-exclusive distribution，并非 CC 授权；代码 Apache 2.0 不作为论文许可。

来源与延伸阅读：[作者提供的写作、绘图与进阶笔记](https://github.com/Da1yuqin/PaperBank/blob/main/SOURCES.md#写作笔记)；[Yuqin Dai et al. · EviNoteRAG: Enhancing RAG Models via Quality-Augmented Evidence Notes](https://arxiv.org/abs/2509.00877)

</details>

- [ ] **第 72 条：**核对来源、书目信息和所支持主张；模型名称、版本与实际使用对应。

<a id="tip-72"></a>
<details>
<summary>说明、例子与参考</summary>

来源真实与引用准确分开检查。查具体段落，不只看标题或别人转引。

**边界：**适用：文献比较、模型／数据集／工具介绍。证据与记录必须如实；不适用的检查注明原因。

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

来源与延伸阅读：[写作技能与检查方法](https://github.com/Da1yuqin/PaperBank/blob/main/SOURCES.md#写作技能)

</details>

- [ ] **第 85 条：**先说前人已解决什么，再定位当前条件下未解或未测部分；未比较不写成失败。

<a id="tip-85"></a>
<details>
<summary>说明、例子与参考</summary>

说明差异的对象和条件，不用一概否定代替创新定位。

**边界：**适用：Related Work 和创新定位。这是推荐写法，按论文类型和当前投稿要求调整；清晰的代词和必要的长句可以保留。

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

来源与延伸阅读：[写作技能与检查方法](https://github.com/Da1yuqin/PaperBank/blob/main/SOURCES.md#写作技能)

</details>


**具体缺口与现象**

- [ ] **第 14 条：**写清哪种方法在什么条件下还有问题，用原文或诊断支持；未测过不等于做不到。

<a id="tip-14"></a>
<details>
<summary>说明、例子与参考</summary>

先承认已有能力，再说明当前任务多出的要求。未报告、未测试、明确失败分别写，不能互相替代。

**边界：**没报告不等于没能力，没测过不等于做不到。这两个区别要守住。

**UrbanZero：把“前人不行”缩成具体任务缺口**

**教学改写：依据 UrbanZero 公开项目介绍，非论文原文**

依据公开项目介绍中的语义简报、地块任务、逐块规划和程序反馈编写。中英示例为本指南教学改写；实验问题和模拟回复方案不代表项目已完成的工作。

**改前 · 中文**

已有方法无法做城市规划。

**Before · English**

Existing methods cannot perform urban planning.

**改后 · 中文**

我们关注模型怎样直接给地块分配用途，并从空间反馈中改进；这一任务要与提供规划建议、调用外部优化器分开比较。

**After · English**

We study how a model assigns land uses to parcels and improves from spatial feedback. This task should be compared separately with advisory systems and external optimization pipelines.

**逐句拆解**

1. 限定讨论对象为可执行地块分配，避免否定所有城市规划研究。
2. 这是教学定位；若要写某个既有系统没有能力，仍需读该系统原文或补诊断，不能只凭项目简介。

来源与延伸阅读：[写作技能与检查方法](https://github.com/Da1yuqin/PaperBank/blob/main/SOURCES.md#写作技能)；[NeurIPS · Paper Checklist](https://neurips.cc/public/guides/PaperChecklist)；[Mensh & Kording (2017) · Ten simple rules for structuring papers](https://doi.org/10.1371/journal.pcbi.1005619)；[Chaoyang Shi, Yuqin Dai et al. · UrbanZero（公开项目介绍）](https://github.com/Da1yuqin/Da1yuqin.github.io/blob/main/_pages/includes/pub.md#L193-L202)

</details>

- [ ] **第 54 条：**先展示可复核现象，再用对照区分常见解释；方法接在诊断之后，观察与验证分开。

<a id="tip-54"></a>
<details>
<summary>说明、例子与参考</summary>

说明测量条件和案例筛选规则。候选解释由诊断区分，改进由后续实验检验，一个难看案例不能宣布整条路线失效。

**边界：**不是找个难看的例子就能宣布整条路线失效。挑选案例需说明规则，总体结论需要相应样本与对照。

**TCDiff++：把“脚滑”写成读者看得见的现象**

**论文原文 · English**

> Foot sliding occurs when a dancer’s feet appear to glide across the ground while the upper body maintains proper movement

**中文翻译 · 本指南翻译**

脚滑表现为舞者双脚看起来在地面上滑动，而上半身仍保持正常动作。

**逐句拆解**

1. 短引保留原句的现象定义：先指出脚与上半身的不同表现，读者能回到图 1 检查，比“动作质量不好”更可复核。
2. 后文把全局轨迹与局部旋转的建模困难作为解释，再提出设计。现象、解释与消融支持要分开，不能把一段解释直接当作已证实机制。

**教学改写 · English（非论文原文）**

Teaching rewrite: First describe the visible mismatch between feet and upper-body motion. Then test whether the trajectory–rotation relationship explains the mismatch before attributing improvement to a specific module.

**教学改写 · 中文（非论文原文）**

教学改写：先描述双脚与上半身动作之间看得见的不一致，再检验轨迹与旋转关系能否解释这种不一致，最后依据实验讨论具体模块的作用。

**摘录出处：**[Yuqin Dai et al. (IJCV 2026；引文为 arXiv v4) · TCDiff++: An End-to-end Trajectory-Controllable Diffusion Model for Harmonious Music-Driven Group Choreography](https://link.springer.com/article/10.1007/s11263-025-02611-3)；§1 Introduction，Single-dancer foot sliding，第1句主干；arXiv v4 PDF p.2；Figure 1 p.3；短引来自 arXiv:2506.18671v4，2025-10-05；正式期刊元数据已核对，不将作者稿等同于期刊排版终版；该工作已发表；引文版本单独标明；教学改写与模拟回复不属于论文原文

**原文／图片许可：**arXiv 作者稿采用 non-exclusive distribution 许可，非 CC BY。正式期刊版权按 Springer 出版协议保留；本指南不向第三方转授原论文版权。

来源与延伸阅读：[作者提供的写作、绘图与进阶笔记](https://github.com/Da1yuqin/PaperBank/blob/main/SOURCES.md#写作笔记)；[Mensh & Kording (2017) · Ten simple rules for structuring papers](https://doi.org/10.1371/journal.pcbi.1005619)；[Liu et al. (2024) · Lost in the Middle, Figure 1 / §2](https://aclanthology.org/2024.tacl-1.9/)；[Yuqin Dai et al. (IJCV 2026；引文为 arXiv v4) · TCDiff++: An End-to-end Trajectory-Controllable Diffusion Model for Harmonious Music-Driven Group Choreography](https://link.springer.com/article/10.1007/s11263-025-02611-3)

</details>


**设计回应问题**

- [ ] **第 55 条：**把关键局限对到设计、作用位置和验证；未验证的作用只写目的，不为排比凑贡献。

<a id="tip-55"></a>
<details>
<summary>说明、例子与参考</summary>

多个设计共同解决一个问题，就写共同作用。贡献取决于新增知识和证据，不等于实现模块数量。

**边界：**不要把每个实现模块包装成一个独立科学贡献；也不要因表格好看而声称一项设计解决了未测的问题。

**TCDiff++：三个问题分别接上设计和检验**

**论文原文 · English**

> To address the aforementioned issues, we upgrade the preliminary conference version (Dai et al, 2025) into a fully end-to-end model.

**中文翻译 · 本指南翻译**

为解决前述问题，我们将先前会议版本（Dai 等，2025）升级为完全端到端模型。

**逐句拆解**

1. 前文提出碰撞、脚滑、长序列换位突变；后文分别接上位置与距离约束、脚步处理、长群舞采样和序列建模。端到端是设计变化，不是解释全部收益的万能词。
2. 对应验证包括基线比较、720 帧长序列比较与逐项消融。设计负责哪个问题，要回到相应证据；不能为排比宣称每个指标都提升。

**教学改写 · English（非论文原文）**

Teaching rewrite: Connect collisions to spatial distinction and distance constraints, foot sliding to footwork refinement, and long-sequence discontinuity to consistency-aware sampling. Cite the comparison or ablation that supports each connection.

**教学改写 · 中文（非论文原文）**

教学改写：将碰撞接到空间区分与距离约束，将脚滑接到脚步细化，将长序列不连续接到考虑一致性的采样。每项对应关系都引用相应比较或消融证据。

**摘录出处：**[Yuqin Dai et al. (IJCV 2026；引文为 arXiv v4) · TCDiff++: An End-to-end Trajectory-Controllable Diffusion Model for Harmonious Music-Driven Group Choreography](https://link.springer.com/article/10.1007/s11263-025-02611-3)；§1 Introduction，升级会议版本段第1句；arXiv v4 PDF p.3；对应§5.3–5.4与Table 3–4；短引来自 arXiv:2506.18671v4，2025-10-05；正式期刊元数据已核对，不将作者稿等同于期刊排版终版；该工作已发表；引文版本单独标明；教学改写与模拟回复不属于论文原文

**原文／图片许可：**arXiv 作者稿采用 non-exclusive distribution 许可，非 CC BY。正式期刊版权按 Springer 出版协议保留；本指南不向第三方转授原论文版权。

来源与延伸阅读：[作者提供的写作、绘图与进阶笔记](https://github.com/Da1yuqin/PaperBank/blob/main/SOURCES.md#写作笔记)；[Mensh & Kording (2017) · Ten simple rules for structuring papers](https://doi.org/10.1371/journal.pcbi.1005619)；[Yuqin Dai et al. (IJCV 2026；引文为 arXiv v4) · TCDiff++: An End-to-end Trajectory-Controllable Diffusion Model for Harmonious Music-Driven Group Choreography](https://link.springer.com/article/10.1007/s11263-025-02611-3)

</details>

- [ ] **第 15 条：**说明设计改变哪一步、为何回应当前困难；没有对照的机制解释写成可能原因。

<a id="tip-15"></a>
<details>
<summary>说明、例子与参考</summary>

引言讲核心思路，方法讲实际操作。用对象和动作替换“增强、优化、赋能”，让读者看见设计如何起作用。

**边界：**解释得通还不等于已经证明。实验没分清的原因，先写成可能解释。

**PlanCraft：过滤器究竟改了哪一步**

**论文原文 · English**

> Candidates whose floor plan region is not a single connected component (after removing door/window markings) are discarded.

**中文翻译 · 本指南翻译**

去掉门窗标记后，平面图区域若不是单一连通分量，这个候选就会被丢弃。

**逐句拆解**

1. 单一连通分量指平面图区域连成一整块。句子把筛选对象、操作前提与淘汰规则讲清，不用“质量增强模块”概括一切。
2. 过滤是在多个生成候选中去掉不合规则的样本，不是重新生成墙体，也不保证满足所有建筑约束；性能作用需结合原文消融看。

**教学改写 · English（非论文原文）**

The filter removes disconnected candidates after generation; it does not alter the geometry of retained candidates. Evaluate this selection step separately from the training strategy.

**教学改写 · 中文（非论文原文）**

过滤器在生成后去掉不连通候选，不修改保留候选的几何形状。评价时将这步筛选与训练策略分开比较。

**摘录出处：**[Zeng, Dai et al. (2026 预印本) · PlanCraft: Sketch, Refine, and Furnish for Architect-Inspired Progressive 3D Residential Scene Generation](https://arxiv.org/abs/2607.23491v3)；Method / PlanCraft-Diff / Inference and Quality Filtering，第 3 句；PDF 第 4 页；arXiv:2607.23491v3，2026-09-05；短引对照作者源稿及公开 v3 正文；公开预印本；教学改写不是论文原文或新增实测结果

**原文／图片许可：**Pengyu Zeng et al., arXiv:2607.23491v3 (2026). arXiv 为非独占分发许可，原文版权由权利人保留；作者授权的教学短引，不随本指南转授全文或原图再版许可。中文翻译、拆解及教学改写为本指南新增。

来源与延伸阅读：[作者提供的写作、绘图与进阶笔记](https://github.com/Da1yuqin/PaperBank/blob/main/SOURCES.md#写作笔记)；[Mensh & Kording (2017) · Ten simple rules for structuring papers](https://doi.org/10.1371/journal.pcbi.1005619)；[NeurIPS · Paper Checklist](https://neurips.cc/public/guides/PaperChecklist)；[Zeng, Dai et al. (2026 预印本) · PlanCraft: Sketch, Refine, and Furnish for Architect-Inspired Progressive 3D Residential Scene Generation](https://arxiv.org/abs/2607.23491v3)

</details>

- [ ] **第 56 条：**比喻后解释实际定义、操作和对应关系；交代类比范围，名字不能替代机制证据。

<a id="tip-56"></a>
<details>
<summary>说明、例子与参考</summary>

借用外学科理论时给来源，并说清是组织灵感、形式模型还是实测机制。“像人的记忆”不等于具有人的记忆机制。

**边界：**不把“像人的记忆”写成“具有人的记忆机制”；修辞强度不能超过证据强度。选论文也没有适用于所有项目的“37%规则”。

**先落地表示，再使用简称**

**论文原文 · English**

> It converts point data into image data for generation and back into point data for editing.

**中文翻译 · 本指南翻译**

这种表示把点数据转成图像数据用于生成，再把图像数据转回点数据用于编辑。

**逐句拆解**

1. 原文It指前一句定义的CMI-P；译文显式展开对象，帮助读者知道究竟是谁在转换。
2. 比喻可以说“翻译器”，正式定义还要落到点数据→图像→点数据和生成/编辑两个目的。
3. 此处是表示格式转换，不能误写成把任何模态任意转换、或无需数据的通用跨模态模型。

**摘录出处：**[Pengyu Zeng et al. (EMNLP 2025) · CARD: Cross-modal Agent Framework for Generative and Editable Residential Design](https://aclanthology.org/2025.emnlp-main.473/)；§3.2 Initial Generation / CMI-P，PDF第4页（刊页9307）；EMNLP 2025正式发表版；已发表；CC BY 4.0

**原文／图片许可：**Pengyu Zeng et al., EMNLP 2025, pp.9304–9319. 原文采用 CC BY 4.0；中文翻译、拆解为本指南新增。

来源与延伸阅读：[作者提供的写作、绘图与进阶笔记](https://github.com/Da1yuqin/PaperBank/blob/main/SOURCES.md#写作笔记)；[Mensh & Kording (2017) · Ten simple rules for structuring papers](https://doi.org/10.1371/journal.pcbi.1005619)；[Pengyu Zeng et al. (EMNLP 2025) · CARD: Cross-modal Agent Framework for Generative and Editable Residential Design](https://aclanthology.org/2025.emnlp-main.473/)

</details>

- [ ] **第 84 条：**每个关键困难接实际设计，再接检验作用的实验；未验证的设计只写目的。

<a id="tip-84"></a>
<details>
<summary>说明、例子与参考</summary>

允许多个设计共同解决一个问题，但不要把模块数量当成贡献数量。

**边界：**适用：引言、方法总览和实验组织。这是推荐写法，按论文类型和当前投稿要求调整；清晰的代词和必要的长句可以保留。

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

来源与延伸阅读：[写作技能与检查方法](https://github.com/Da1yuqin/PaperBank/blob/main/SOURCES.md#写作技能)

</details>


**贡献与证据**

- [ ] **第 2 条：**选出读者最该记住的贡献，说明其他设计如何支持它；独立发现交代共同范围。

<a id="tip-02"></a>
<details>
<summary>说明、例子与参考</summary>

每项设计说明解决了哪一步困难。多个独立发现可以保留，但要解释为什么放在同一篇论文里。

**边界：**一个中心不等于硬砍到只剩一个发现。能串起来就串，串不起来就重新想论文的范围。

**PlanCraft：先立住从草图到完整场景的主线**

**论文原文 · English**

> We identify two overlooked structural insights, design is progressive and the floor plan is a spatial prior, and propose PlanCraft, the first unified system that bridges incomplete design sketches to fully furnished 3D residential scenes.

**中文翻译 · 本指南翻译**

我们指出两项此前未被充分注意的结构性认识：设计是渐进的，平面图是空间先验；并提出 PlanCraft 这一首个将不完整设计草图连接到完整带家具三维住宅场景的统一系统。

**逐句拆解**

1. 这一项先给两条认识，再落到同一个任务：从不完整草图生成完整三维住宅。数据、扩散生成与家具装配因此有了共同服务的对象。
2. first unified system 是论文的新颖性主张，引用时要保留其具体任务范围；不能扩成“首个三维生成系统”。

**教学改写 · English（非论文原文）**

The central contribution is progressive scene generation from incomplete residential sketches. Partial-sketch supervision, floor-plan refinement, and bounded furnishing each support one stage of this task.

**教学改写 · 中文（非论文原文）**

主要贡献是不完整住宅草图的渐进式场景生成。局部草图监督、平面图细化与有边界的家具装配，各自支持这个任务的一步。

**摘录出处：**[Zeng, Dai et al. (2026 预印本) · PlanCraft: Sketch, Refine, and Furnish for Architect-Inspired Progressive 3D Residential Scene Generation](https://arxiv.org/abs/2607.23491v3)；Introduction，贡献列表第 1 项；PDF 第 2 页；arXiv:2607.23491v3，2026-09-05；短引对照作者源稿及公开 v3 正文；公开预印本；教学改写不是论文原文或新增实测结果

**原文／图片许可：**Pengyu Zeng et al., arXiv:2607.23491v3 (2026). arXiv 为非独占分发许可，原文版权由权利人保留；作者授权的教学短引，不随本指南转授全文或原图再版许可。中文翻译、拆解及教学改写为本指南新增。

来源与延伸阅读：[作者提供的写作、绘图与进阶笔记](https://github.com/Da1yuqin/PaperBank/blob/main/SOURCES.md#写作笔记)；[Zeng, Dai et al. (2026 预印本) · PlanCraft: Sketch, Refine, and Furnish for Architect-Inspired Progressive 3D Residential Scene Generation](https://arxiv.org/abs/2607.23491v3)

</details>

- [ ] **第 16 条：**贡献分别写提出、构建或发现了什么；合并重复项，每项都有正文展开与证据。

<a id="tip-16"></a>
<details>
<summary>说明、例子与参考</summary>

每项写新增内容与作用。用 de-identified、expert-confirmed、tailored 等具体正面的词点出特点；有依据就直接用，等量替换，不堆修饰词。

**边界：**不必凑三条或四条。“做了大量实验”本身没说明多知道了什么。

**UrbanZero：贡献按对象分，不按干活次数分**

**教学改写：依据 UrbanZero 公开项目介绍，非论文原文**

依据公开项目介绍中的语义简报、地块任务、逐块规划和程序反馈编写。中英示例为本指南教学改写；实验问题和模拟回复方案不代表项目已完成的工作。

**改前 · 中文**

我们写了数据处理脚本、改了提示词、搭了训练循环。

**Before · English**

We wrote preprocessing scripts, revised prompts, and implemented a training loop.

**改后 · 中文**

我们构建地块级评价基准，并设计由任务编译、逐块求解和程序反馈组成的自进化框架。

**After · English**

We construct a parcel-level evaluation benchmark and design a self-evolution framework that combines task compilation, patch-wise solving, and programmatic feedback.

**逐句拆解**

1. 基准与框架是两种可交付研究对象；脚本和提示词修改应回到支持它们的实现细节。
2. 这里仅整理公开介绍中的对象，不新增“首个”“全面优于”等未经核对的贡献主张。

**用一个准确的词留下贡献印象**

**教学改写：假设标签已由专家确认。**

只示范贡献句；不声称任何论文采用了这套标签。

**改前 · 中文**

我们使用处理后的标签评估引用准确率。

**Before · English**

We evaluate citation accuracy using processed labels.

**改后 · 中文**

我们使用专家确认的标签评估引用准确率。

**After · English**

We evaluate citation accuracy using expert-confirmed labels.

**逐句拆解**

1. processed 只说处理过，expert-confirmed 点出专家确认。一个修饰词换一个，不加长句子。
2. 标签实际经过专家确认才这样写；贡献句不用再逐词解释。

来源与延伸阅读：[写作技能与检查方法](https://github.com/Da1yuqin/PaperBank/blob/main/SOURCES.md#写作技能)；[Mensh & Kording (2017) · Ten simple rules for structuring papers](https://doi.org/10.1371/journal.pcbi.1005619)；[NeurIPS · Paper Checklist](https://neurips.cc/public/guides/PaperChecklist)；[Chaoyang Shi, Yuqin Dai et al. · UrbanZero（公开项目介绍）](https://github.com/Da1yuqin/Da1yuqin.github.io/blob/main/_pages/includes/pub.md#L193-L202)

</details>

- [ ] **第 87 条：**每项贡献写一个主要动作、研究对象和意义；工程步骤与命名不能替代创新。

<a id="tip-87"></a>
<details>
<summary>说明、例子与参考</summary>

用提出、构建或发现说明新增内容，再给能核对的证据。

**边界：**适用：贡献列表和摘要。这是推荐写法，按论文类型和当前投稿要求调整；清晰的代词和必要的长句可以保留。

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

来源与延伸阅读：[写作技能与检查方法](https://github.com/Da1yuqin/PaperBank/blob/main/SOURCES.md#写作技能)

</details>

- [ ] **第 3 条：**把主要主张对到设计和实验；缺证据就补实验或收窄主张，机制解释另需对照。

<a id="tip-03"></a>
<details>
<summary>说明、例子与参考</summary>

说省钱就比较成本，说更稳就报告波动。整体分数提高，只能先说明整套方法改善，不能自动归因给一个模块。

**边界：**整体分数上涨，只能先说明整体变好了。想说是某个机制起作用，还得有能区分原因的对照。

**TCDiff：引言说要避碰，实验就查碰撞指标**

**论文原文 · English**

> To mitigate collisions, we introduce a Dance-Trajectory Navigator that generates collision-free trajectories for multiple dancers, utilizing a distance-consistency loss to maintain optimal spacing.

**中文翻译 · 本指南翻译**

为减少碰撞，我们引入舞蹈轨迹导航器，为多名舞者生成无碰撞轨迹，并利用距离一致性损失维持合适间距。

**逐句拆解**

1. 原句给出“碰撞→轨迹导航器→距离损失→舞者间距”的链条，所以实验要查碰撞相关的 TIF，不只报动作多样性。
2. 原 Table1 的 TIF 为 TCDiff 0.13、CoDancers 0.10、GCD 0.17，越低越好：比 GCD 降低，但没有在这张表上超过 CoDancers。
3. 因此 collision-free 是原作者的设计措辞，不应转述为测试结果零碰撞或所有指标最优。补实验或缩小主张，都要回到实际证据。

**教学改写 · English（非论文原文）**

The navigator targets collision reduction. Table 1 reports TIF of 0.13 for TCDiff, 0.17 for GCD, and 0.10 for CoDancers; the result supports a reduction against GCD, not universal superiority or zero collisions.

**教学改写 · 中文（非论文原文）**

导航器针对碰撞问题。表 1 中 TCDiff、GCD、CoDancers 的 TIF 分别为 0.13、0.17、0.10；结果支持相对 GCD 的降低，不支持全面最优或零碰撞。

**摘录出处：**[Yuqin Dai et al. (AAAI 2025) · Harmonious Music-driven Group Choreography with Trajectory-Controllable Diffusion](https://ojs.aaai.org/index.php/AAAI/article/view/32268)；Abstract, PDF p.1 / p.2645；Table1, PDF p.6 / p.2650；正式发表论文；已发表；作者原文摘录

**原文／图片许可：**Yuqin Dai et al., AAAI 2025, pp.2645–2653. ©2025 AAAI，保留原版权；作者教学短引，不纳入本指南原创内容的 CC BY 许可。中文为本指南翻译。

来源与延伸阅读：[写作技能与检查方法](https://github.com/Da1yuqin/PaperBank/blob/main/SOURCES.md#写作技能)；[NeurIPS · Paper Checklist](https://neurips.cc/public/guides/PaperChecklist)；[Yuqin Dai et al. (AAAI 2025) · Harmonious Music-driven Group Choreography with Trajectory-Controllable Diffusion](https://ojs.aaai.org/index.php/AAAI/article/view/32268)

</details>

- [ ] **第 79 条：**每段解释场景、困难、设计、证据或意义；与贡献无关的领域流水账删掉。

<a id="tip-79"></a>
<details>
<summary>说明、例子与参考</summary>

保留让读者走到研究问题所必需的背景，删掉只有“领域很重要”的铺垫。

**边界：**适用：引言和全文组织。这是推荐写法，按论文类型和当前投稿要求调整；清晰的代词和必要的长句可以保留。

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

来源与延伸阅读：[写作技能与检查方法](https://github.com/Da1yuqin/PaperBank/blob/main/SOURCES.md#写作技能)

</details>

- [ ] **第 83 条：**转折确有转折，因果有依据；章节承接真实输入输出，并行步骤不能写成串行。

<a id="tip-83"></a>
<details>
<summary>说明、例子与参考</summary>

先确认内容关系，再选 However 或 Therefore。连接词不能补出不存在的因果或依赖。

**边界：**适用：句间、段间和章节衔接。这是推荐写法，按论文类型和当前投稿要求调整；清晰的代词和必要的长句可以保留。

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

来源与延伸阅读：[写作技能与检查方法](https://github.com/Da1yuqin/PaperBank/blob/main/SOURCES.md#写作技能)

</details>


**动机图**

- [ ] **第 28 条：**先写图要传达的主要信息，再选面板、连线和图型；画面不暗示未验证的优势。

<a id="tip-28"></a>
<details>
<summary>说明、例子与参考</summary>

动机图讲问题，流程图讲操作，结果图讲比较。只保留服务于主要信息的内容，布局按任务选择。

**边界：**左右对照只是选项，不是所有图的标准答案。没有验证的优势，别靠画面暗示出来。

**TCOD 图2：四个面板讲一个诊断**

**公开论文图例 · 点评为本指南整理**

图2(c)纵轴从50起；看标出的数值，不拿柱长解释倍数。

![TCOD Figure 2：训练KL、成功率、初末KL与逐轮KL四个面板](../assets/paper-tcod-fig2.png)

Figure 2 organizes the diagnosis by training progress, initial–final comparison, and dialogue turn.
按训练过程、初末比较、对话轮次组织诊断，图型随问题变化。

**逐句拆解**

1. (a)(b)对照训练步数上的KL与任务完成率；(c)比较三组师生的初末KL；(d)看KL随对话轮次如何变化。
2. 先看现象，再找差距和发生位置。四图围着同一问题，读者不用猜它们为什么拼在一起。
3. 可借鉴这条论证顺序。曲线同时变化并不独立证明因果；阴影统计定义不清时不要替作者猜。

**摘录出处：**[Jiaqi Wang et al. · TCOD (arXiv v3)](https://arxiv.org/abs/2604.24005v3)；Fig.2，PDF 第4页；公开 arXiv 版本；图与原 PDF 核对；公开预印本；不以项目笔记中的会议标记认定录用

**原文／图片许可：**Jiaqi Wang et al., TCOD, arXiv:2604.24005v3. CC BY 4.0（https://creativecommons.org/licenses/by/4.0/）。从原 PDF 裁切；图形、标签和数据未改。

**OneReason 图12：相同结构对照训练策略**

**链接读图 · 本指南点评，不转载原图**

原图见下方来源。已核对原PDF；分发许可不作为图片复用许可。

**逐句拆解**

1. 同一流程下比较两种优化策略，读者先看改动位置，再看对应操作。
2. 概念图解释设计；效果与稳定性还要实验支持。

**教学改写 · English（非论文原文）**

Keep the compared panels aligned. Mark where the optimization rules differ and explain each symbol in the caption.

**教学改写 · 中文（非论文原文）**

让对照面板对齐；标出优化规则在哪一步不同，图注解释各个符号。

**摘录出处：**[OneReason Technical Report · Figure 12](https://arxiv.org/pdf/2606.06260v1#page=34)；Fig.12，PDF 第34页；arXiv:2606.06260v1；公开预印本；仅链接分析

来源与延伸阅读：[作者提供的写作、绘图与进阶笔记](https://github.com/Da1yuqin/PaperBank/blob/main/SOURCES.md#写作笔记)；[Rougier et al. (2014) · Ten Simple Rules for Better Figures](https://doi.org/10.1371/journal.pcbi.1003833)；[Jiaqi Wang et al. · TCOD (arXiv v3)](https://arxiv.org/abs/2604.24005v3)

</details>

- [ ] **第 89 条：**写清对象、比较、指标、单位、方向和汇总；颜色、线型、误差条、阈值及缩写有解释。

<a id="tip-89"></a>
<details>
<summary>说明、例子与参考</summary>

输入和比较组写明，箭头按真实关系标注。图注只保留解释读法和发现所需的信息。

**边界：**数据、信息边界和完成状态按实际记录说明。

**看图就能知道比了什么**

**教学示例：假设情境，非论文原文／实测记录**

改后假定已有对应记录；实际改稿须先核对这些事实，不能从改前文字推断或补造。

**逐句拆解**

任务数和重复次数分开写；误差条是哪一种不确定性也写清。

**教学改写 · English（非论文原文）**

Accuracy on the same 100 held-out tasks. Bars show the mean across five independent runs; error bars show the standard deviation across runs. Higher is better. Blue denotes the baseline and green denotes the revised method.

**教学改写 · 中文（非论文原文）**

同一批 100 个留出任务上的准确率。柱高表示五次独立运行的均值；误差条表示运行间的标准差。指标越高越好。蓝色是基线，绿色是修改后的方法。

来源与延伸阅读：[写作技能与检查方法](https://github.com/Da1yuqin/PaperBank/blob/main/SOURCES.md#写作技能)

</details>


</details>


<a id="related"></a>
## 4. 相关工作

按问题组织文献，准确说明本文与最相近工作的差别。

### 相关工作·示范自然段1：方法归类

按解决的问题概括代表路线，避免逐篇点名。

教学例句，非论文原文或实测结果。

Retrieval methods differ in how they select and organize supporting text.

检索方法在支持文本的筛选与组织方式上有所不同。

**第 1 句：**先给分类维度，之后才能看出各路线的关系。

Dense retrieval selects passages, while evidence organization links selected text to answer claims.

稠密检索筛选片段，证据组织则将选中内容与答案主张关联。

**第 2 句：**概括有实质区别的路线；真实论文应为每类主张配准确引用。

### 相关工作·示范自然段2：近邻与差别

写准近邻研究已经覆盖什么，再限定本文差别。

教学例句，非论文原文或实测结果。

The closest comparison organizes evidence for individual questions.

最相近的比较对象针对单个问题组织证据。

**第 1 句：**先说近邻已能处理单问证据，下一句才引出本文增加的跨轮条件。

Our study examines whether keeping earlier constraints helps across dialogue turns.

本文检验跨轮保留前文约束是否有用。

**第 2 句：**差别落到研究条件，不凭方法名字宣称新颖。

<details>
<summary>检查清单和真实论文例子（3 项）</summary>


**按问题组织文献**

- [ ] **第 34 条：**按问题或技术路线归类，先讲共同思路再讲差异；具体说明与本研究的关系。

<a id="tip-34"></a>
<details>
<summary>说明、例子与参考</summary>

引用跟随类别主张，不逐篇点名。末尾接回引言中的真实困难和对应设计，已被前人解决的部分如实承认。

**边界：**不用每节硬找一个缺点。没有真实转折，强塞 However 只会显得生硬。

**SAGE：相关工作按任务组织**

**论文原文 · English**

> Service dialogue benchmarks cover human-like conversation, customer support resolution, multi-turn shopping interactions, and real-world dialogue analysis.

**中文翻译 · 本指南翻译**

服务对话基准覆盖类人对话、客服问题解决、多轮购物交互，以及真实对话分析。

**逐句拆解**

1. 四组都是具体研究任务，读者先看任务之间的关系，再沿原论文引用找到每组代表工作。
2. 本段后面才接到 SOP 的场景适配问题与 SAGE 的图表示、扩展机制，分类服务于研究位置。
3. 对近邻工作的限制判断应逐篇核对；不能因为本文要讨论跨领域，就断言已有基准完全没有可迁移设计。

**摘录出处：**[Ling Shi, Yuqin Dai et al. · SAGE: An Extensible Benchmark for Service Agent Graph-guided Evaluation](https://arxiv.org/abs/2604.09285)；§ Related Works / Benchmarks for Service Dialogue Systems，第一句（作者源稿第 421 行）；作者终稿 2026-10-04 只读快照；公开链接为 arXiv v1；作者终稿短引；公开链接为不同版本预印本

**原文／图片许可：**作者终稿教学短引，保留原论文版权；不随 PaperBank 原创内容转授终稿转载权。公开 arXiv v1 的 CC BY 4.0 已核验，该许可不自动延伸到不同版本的作者终稿。

来源与延伸阅读：[作者提供的写作、绘图与进阶笔记](https://github.com/Da1yuqin/PaperBank/blob/main/SOURCES.md#写作笔记)；[Ling Shi, Yuqin Dai et al. · SAGE: An Extensible Benchmark for Service Agent Graph-guided Evaluation](https://arxiv.org/abs/2604.09285)

</details>


**近邻工作与区别**

- [ ] **第 35 条：**对照最相近工作的任务、输入、方法和设置，写清沿用与改进；复现限制照实说明。

<a id="tip-35"></a>
<details>
<summary>说明、例子与参考</summary>

贡献靠具体差异成立。需要比较就认真比较，不能复现就交代原因；删引用不会删掉先例。

**边界：**删掉引用不会删掉先例。贡献需要经得起比较。

**EviNoteRAG：最接近的底座写在消融开头**

**论文原文 · English**

> Our experiments build on Base model Search-R1, an end-to-end RL-based RAG pipeline.

**中文翻译 · 本指南翻译**

我们的实验以 Base 模型 Search-R1 为基础；Search-R1 是一套端到端、基于强化学习的 RAG 流程。

**逐句拆解**

1. 一句话承认沿用的基础及来源，没有把已有端到端检索训练包装成本篇首次提出。
2. 随后依次比较强制摘要、可选摘要、带标记的 SEN，以及 SEN 加 EQR，读者能看出具体新增了什么。
3. 组件贡献应回到这些同一底座的比较，不把与其他底座之间的差距全部归给笔记机制。

**摘录出处：**[Yuqin Dai et al. · EviNoteRAG: Enhancing RAG Models via Quality-Augmented Evidence Notes](https://arxiv.org/abs/2509.00877)；§ 4.6 Ablation Study / Settings，首句，PDF 第 6 页；content/04_experiments.tex 第 131 行；EMNLP 2026 revised 作者终稿；公开链接为 arXiv v3；作者终稿短引；公开链接为不同版本预印本

**原文／图片许可：**作者终稿教学短引，保留原论文版权；不随 PaperBank 原创内容转授原论文再版许可。公开 arXiv v3 为 non-exclusive distribution，并非 CC 授权；代码 Apache 2.0 不作为论文许可。

来源与延伸阅读：[作者提供的写作、绘图与进阶笔记](https://github.com/Da1yuqin/PaperBank/blob/main/SOURCES.md#写作笔记)；[Mensh & Kording (2017) · Ten simple rules for structuring papers](https://doi.org/10.1371/journal.pcbi.1005619)；[NeurIPS · Paper Checklist](https://neurips.cc/public/guides/PaperChecklist)；[Yuqin Dai et al. · EviNoteRAG: Enhancing RAG Models via Quality-Augmented Evidence Notes](https://arxiv.org/abs/2509.00877)

</details>


**引用支持判断**

- [ ] **第 36 条：**逐条核对原文和书目信息，说明引用支持什么；按相关性选文献，预印本注明版本。

<a id="tip-36"></a>
<details>
<summary>说明、例子与参考</summary>

来源存在，不代表支持当前说法。早期与近期研究都按相关性保留，不用篇数或年份比例评价引用质量。

**边界：**预印本就按预印本写。年份、新旧比例和篇数都不能代替相关性。

**EviNoteRAG：模型来源的引用不能顶替方法验证**

**论文原文 · English**

> We realize the Entailment Judge through a lightweight NLI model, which evaluates whether the final SEN entails the correct answer.

**中文翻译 · 本指南翻译**

我们使用一个轻量自然语言推断（NLI）模型实现蕴含评判，评价最后一条支持性证据笔记（SEN）能否推出正确答案。

**逐句拆解**

1. 原句在 NLI 模型后引用 Sanh et al. (2019) 的 DistilBERT，引用服务于模型来源，而不是替本篇证明 EQR 的收益。
2. NLI 在这里比较证据笔记与正确答案命题；具体检查点、微调数据和输入构造仍须按本篇实现说明核对，不能从基础模型论文中猜。
3. 教学摘录移除了文献标记；实际写作应保留对应引文，并将采用了什么模型与本研究新增了什么奖励区分清楚。

**摘录出处：**[Yuqin Dai et al. · EviNoteRAG: Enhancing RAG Models via Quality-Augmented Evidence Notes](https://arxiv.org/abs/2509.00877)；§ 3.3 Evidence Quality Reward，Entailment Judge 实现句，PDF 第 3 页；原引文 Sanh et al. (2019), DistilBERT, arXiv:1910.01108；EMNLP 2026 revised 作者终稿；公开链接为 arXiv v3；作者终稿短引；公开链接为不同版本预印本

**原文／图片许可：**作者终稿教学短引，保留原论文版权；不随 PaperBank 原创内容转授原论文再版许可。公开 arXiv v3 为 non-exclusive distribution，并非 CC 授权；代码 Apache 2.0 不作为论文许可。

来源与延伸阅读：[作者提供的写作、绘图与进阶笔记](https://github.com/Da1yuqin/PaperBank/blob/main/SOURCES.md#写作笔记)；[Yuqin Dai et al. · EviNoteRAG: Enhancing RAG Models via Quality-Augmented Evidence Notes](https://arxiv.org/abs/2509.00877)

</details>


</details>


<a id="method"></a>
## 5. 方法

先定义任务，再按真实依赖说明输入、处理和输出。

### 方法·示范自然段1：任务定义

用具体对象定义输入、输出和不可见信息。

教学例句，非论文原文或实测结果。

The input contains the current question, dialogue history, and a searchable document collection.

输入包括当前问题、对话历史和可检索的文档集合。

**第 1 句：**先说明模型实际能看到什么。

The output is an answer with citations; reference answers are used only for evaluation.

输出是带引用的回答；参考答案只用于评价。

**第 2 句：**把生成输入与评估参照分开，避免图与文字造成答案泄漏。

### 方法开头：先把流程讲通

先讲输入怎样变成输出，再逐节讲模块。别把章节目录念一遍。

教学例句，非论文原文。

Given a question and dialogue history, the retriever selects relevant passages from the manuals.

检索器根据问题和对话历史，从手册中筛选相关片段。

**第 1 句：**先给输入与第一步操作，不让读者猜模型读了什么。

The note builder then links source quotes to the constraints from earlier turns.

笔记构建器随后将来源摘句与前文约束关联。

**第 2 句：**then 接住检索产物；来源与约束怎样组合，就是这一模块的作用。

The generator uses these notes to produce an answer with source citations.

生成器使用这些笔记，给出带来源引用的回答。

**第 3 句：**these notes 承接上一句；回答与引用落到最终输出。

### 方法总览：最后一句收束流程

前面讲清组件怎样接力，最后再概括整条流程。

论文原文短引 · 中文为本指南翻译

GreenPlanner 生成满足约束的规划，下面摘录框架图图注里的流程收束句，不是完整方法总览。

Together, these components form an end-to-end pipeline from data construction to constraint-driven generative design.

这些组成部分共同形成一条从数据构建到约束驱动生成设计的端到端流程。

**第 1 句：**Together 回指前文组件，随后用“数据构建到约束驱动设计”概括整条流程的起点和终点。

[Pengyu Zeng et al. (CVPR Findings 2026) · GreenPlanner: Practical Floorplan Layout Generation via an Energy-Aware and Function-Feasible Generative Framework](https://openaccess.thecvf.com/content/CVPR2026F/html/Zeng_GreenPlanner_Practical_Floorplan_Layout_Generation_via_an_Energy-Aware_and_Function-Feasible_CVPRF_2026_paper.html) · Figure 2 caption，最后一句；PDF p.3，proceedings p.8598；对应§3 Method；CVF Open Access 作者接受版；正式发表元数据已由 CVF 条目核对

### 方法·示范自然段3：表示与操作

每个关键步骤说清目的、操作与输出。

论文原文短引 · 中文为本指南翻译

SAGE 将服务对话流程建成图，下面摘录方法中定义流程表示的一句。

We formalize each SOP as a directed graph G = (V, E) with three node types: Start/End, Decision (branching on conditions), and Action nodes.

我们将每个标准操作流程（SOP）形式化为有向图 G = (V, E)，图中有三类节点：开始／结束节点、按条件分支的决策节点，以及动作节点。

**第 1 句：**输入对象是标准操作流程，输出表示是有向图；三类节点把图实际包含的内容立即说清。

[Ling Shi, Yuqin Dai et al. · SAGE: An Extensible Benchmark for Service Agent Graph-guided Evaluation](https://arxiv.org/abs/2604.09285) · § Universal Dialogue Graph Modeling，有向图定义段（作者源稿第 471 行）；作者终稿 2026-10-04 只读快照；公开链接为 arXiv v1

### 方法·示范自然段4：答案生成

说明生成器如何使用前面的产物。

教学例句，非论文原文或实测结果。

The generator receives the question and the evidence notes.

生成器接收问题和证据笔记。

**第 1 句：**明确下一模块的输入。

The generator returns an answer with links to the quoted sources.

生成器返回回答，并附上指向摘句来源的引用。

**第 2 句：**回答附上笔记中的来源，读者能回查证据。

<details>
<summary>检查清单和真实论文例子（12 项）</summary>


**任务与真实流程**

- [ ] **第 17 条：**方法开头串起目的、输入、操作和输出，讲清先后与并行关系；名称与正文、图一致。

<a id="tip-17"></a>
<details>
<summary>说明、例子与参考</summary>

从引言困难接到实际流程。前一步的产物如何用于下一步，连贯说清；不要逐项朗读目录。

**边界：**别把目录念一遍就算总览。哪些步骤并行，哪些依赖上一步，要讲准。

**PlanCraft：方法总览把四步的职责摆清楚**

**论文原文 · English**

> SketchPlan supplies partial-sketch supervision, PlanCraft-Diff refines incomplete inputs into floor plans, Rule-Based Post-Processing converts raster outputs into verified vectors, and PlanCraft-Agent furnishes 3D scenes within verified room boundaries.

**中文翻译 · 本指南翻译**

SketchPlan 提供局部草图监督，PlanCraft-Diff 将不完整输入细化为平面图，基于规则的后处理把栅格输出转换为经过检查的矢量，PlanCraft-Agent 则在经过检查的房间边界内装配三维场景。

**逐句拆解**

1. 四个名字后面都有动词与产物，读者可以顺着“训练数据—生成—几何转换—装配”找正文小节。
2. SketchPlan 提供的是训练监督，后三步构成生成与装配流程；不能把所有训练准备画成每次推理都必须执行。

**教学改写 · English（非论文原文）**

Separate training-data construction from inference. At inference, refine the condition into a floor plan, verify its vector geometry, and furnish the rooms using those boundaries.

**教学改写 · 中文（非论文原文）**

分开训练数据构建与推理。推理时先把条件补全为平面图，再检查矢量几何，最后沿这些边界装配房间。

**摘录出处：**[Zeng, Dai et al. (2026 预印本) · PlanCraft: Sketch, Refine, and Furnish for Architect-Inspired Progressive 3D Residential Scene Generation](https://arxiv.org/abs/2607.23491v3)；Method / Overview，第 2 句；PDF 第 2 页；arXiv:2607.23491v3，2026-09-05；短引对照作者源稿及公开 v3 正文；公开预印本；教学改写不是论文原文或新增实测结果

**原文／图片许可：**Pengyu Zeng et al., arXiv:2607.23491v3 (2026). arXiv 为非独占分发许可，原文版权由权利人保留；作者授权的教学短引，不随本指南转授全文或原图再版许可。中文翻译、拆解及教学改写为本指南新增。

来源与延伸阅读：[写作技能与检查方法](https://github.com/Da1yuqin/PaperBank/blob/main/SOURCES.md#写作技能)；[Mensh & Kording (2017) · Ten simple rules for structuring papers](https://doi.org/10.1371/journal.pcbi.1005619)；[Zeng, Dai et al. (2026 预印本) · PlanCraft: Sketch, Refine, and Furnish for Architect-Inspired Progressive 3D Residential Scene Generation](https://arxiv.org/abs/2607.23491v3)

</details>

- [ ] **第 18 条：**每个模块写清目的、输入、操作、输出和去向；说明来源、可见信息及沿用组件。

<a id="tip-18"></a>
<details>
<summary>说明、例子与参考</summary>

先说为什么需要，再说如何处理，最后交代输出交给谁。影响结果的处理条件保留；现成组件明确注明来源。

**边界：**现成组件就说明是现成组件。重新命名，不会把别人的方法变成你的贡献。

**WD-Net的输入和输出一眼可见**

**论文原文 · English**

> Specifically, WD-Net takes the residential layout as input and produces a residential floor plan with doors, windows, and walls.

**中文翻译 · 本指南翻译**

具体而言，WD-Net以住宅布局作为输入，输出包含门、窗和墙的住宅平面图。

**逐句拆解**

1. 输入是住宅布局，输出是补齐门窗墙的平面图；读者能看出模块实际新增了什么。
2. 把它写成“设计优化模块”会丢掉数据形态和操作内容。
3. 这里解释的是原论文模块的任务，不证明每个输出都通过真实建筑安全审查。

**摘录出处：**[Pengyu Zeng et al. (EMNLP 2025) · CARD: Cross-modal Agent Framework for Generative and Editable Residential Design](https://aclanthology.org/2025.emnlp-main.473/)；§3.2 Initial Generation / WD-Net，PDF第4页（刊页9307）；EMNLP 2025正式发表版；已发表；CC BY 4.0

**原文／图片许可：**Pengyu Zeng et al., EMNLP 2025, pp.9304–9319. 原文采用 CC BY 4.0；中文翻译、拆解为本指南新增。

来源与延伸阅读：[写作技能与检查方法](https://github.com/Da1yuqin/PaperBank/blob/main/SOURCES.md#写作技能)；[NeurIPS · Paper Checklist](https://neurips.cc/public/guides/PaperChecklist)；[Mensh & Kording (2017) · Ten simple rules for structuring papers](https://doi.org/10.1371/journal.pcbi.1005619)；[Pengyu Zeng et al. (EMNLP 2025) · CARD: Cross-modal Agent Framework for Generative and Editable Residential Design](https://aclanthology.org/2025.emnlp-main.473/)

</details>

- [ ] **第 57 条：**画清输入、操作、输出与依赖，再放一个可追踪案例；数据、评分和更新用图例区分。

<a id="tip-57"></a>
<details>
<summary>说明、例子与参考</summary>

布局方向统一，框旁给关键中间产物。案例帮助读步骤，不证明总体效果；企业标志的使用另查许可。

**边界：**箭头表示流程或依赖，不自动表示已证明的因果关系；学习信号需指出谁给分、评什么、更新谁。

**PlanCraft：同一张局部草图贯穿推理主线**

**论文原文 · English**

> PlanCraft-Diff then generates a complete floor plan, which is vectorized and furnished by PlanCraft-Agent.

**中文翻译 · 本指南翻译**

随后，PlanCraft-Diff 生成完整平面图，再将其转换为矢量，并由 PlanCraft-Agent 布置家具。

**逐句拆解**

1. Fig.2 给出两个输入入口：文字先转为图与块条件，局部矢量草图直接栅格化。教学时选一张局部草图，顺着“草图—完整平面图—检查后的矢量—三维场景”讲，避免来回换案例。
2. SketchPlan 位于训练监督分支。图中每个中间产物都应区分类型，矢量化与几何检查也不要被一根箭头省掉。
3. 这里短引图注并分析文中流程，未复制原图或第三方三维资产；流程图的箭头不构成效果证据。

**教学改写 · English（非论文原文）**

Follow one partial sketch: rasterize it as a condition, complete the floor plan, convert and verify the vector geometry, then furnish the rooms within those boundaries. Keep the training-supervision branch separate.

**教学改写 · 中文（非论文原文）**

跟随一张局部草图：将其栅格化为条件，补全平面图，转换并检查矢量几何，最后在房间边界内装配家具。训练监督分支单独画。

**摘录出处：**[Zeng, Dai et al. (2026 预印本) · PlanCraft: Sketch, Refine, and Furnish for Architect-Inspired Progressive 3D Residential Scene Generation](https://arxiv.org/abs/2607.23491v3)；Figure 2 caption，最后一句；PDF 第 3 页；输入分支另见 Method / Overview；arXiv:2607.23491v3，2026-09-05；短引对照作者源稿及公开 v3 正文；公开预印本；教学改写不是论文原文或新增实测结果

**原文／图片许可：**Pengyu Zeng et al., arXiv:2607.23491v3 (2026). arXiv 为非独占分发许可，原文版权由权利人保留；作者授权的教学短引，不随本指南转授全文或原图再版许可。中文翻译、拆解及教学改写为本指南新增。

来源与延伸阅读：[作者提供的写作、绘图与进阶笔记](https://github.com/Da1yuqin/PaperBank/blob/main/SOURCES.md#写作笔记)；[Rougier et al. (2014) · Ten Simple Rules for Better Figures](https://doi.org/10.1371/journal.pcbi.1003833)；[TCOD (2026 预印本) · Figure 1](https://arxiv.org/pdf/2604.24005v3)；[Reinforcing Real-world Service Agents (2026 预印本) · Figure 1](https://arxiv.org/html/2602.22697v1#S4.F1)；[Zeng, Dai et al. (2026 预印本) · PlanCraft: Sketch, Refine, and Furnish for Architect-Inspired Progressive 3D Residential Scene Generation](https://arxiv.org/abs/2607.23491v3)

</details>

- [ ] **第 90 条：**每步写清输入、操作和输出；训练、推理、评价分开，推理输入不含不可见答案或未来信息。

<a id="tip-90"></a>
<details>
<summary>说明、例子与参考</summary>

训练标签可以用于训练，评价答案可以供评价器使用；不能画进实际无权获得这些信息的推理步骤。

**边界：**可见信息按真实协议说明；训练标签可以用于训练，推理时不能获得的答案或未来信息不进入推理输入。

**箭头按真实依赖连，答案别进输入**

**教学示例：假设情境，非论文原文／实测记录**

改后假定已有对应记录；实际改稿须先核对这些事实，不能从改前文字推断或补造。

**逐句拆解**

未来记录可以进入评价框，不能沿箭头流回预测输入。

**教学改写 · English（非论文原文）**

The model receives records available by 2020 and predicts the 2022 outcome. A separate evaluation step compares the prediction with the observed 2022 record; the observed outcome is not supplied to the predictor.

**教学改写 · 中文（非论文原文）**

模型接收截至 2020 年已经知道的记录，预测 2022 年的结果。另一条评价流程用真实的 2022 年记录检验预测；真实结果不传给预测模型。

来源与延伸阅读：[写作技能与检查方法](https://github.com/Da1yuqin/PaperBank/blob/main/SOURCES.md#写作技能)

</details>


**符号、输入与反馈**

- [ ] **第 19 条：**符号首次出现就解释对象、下标和单位；同一对象统一记号，公式旁说明实际操作。

<a id="tip-19"></a>
<details>
<summary>说明、例子与参考</summary>

没用到的定义删掉。公式不是装饰：读者应能从文字看懂计算对象、计算方式和所得量的用途。

**边界：**符号多不代表理论强。简单关系能说清楚就够，关键公式则不能缺定义。

**给奖励一个可执行判据**

**论文原文 · English**

> We define the Source-restricting Reward R_src ∈ {0,1} to be 1 if any query in Q contains an advanced search pattern from K, and 0 otherwise.

**中文翻译 · 本指南翻译**

我们把来源限制奖励 R_src 定义为二值量：查询集合 Q 中只要有一个查询包含预定义集合 K 中的高级搜索模式，奖励就取 1，否则取 0。

**逐句拆解**

1. 先给二值范围，再给取1与取0的条件，公式因此可对应实现核验。
2. Q是从模型响应里提取的查询集合，K是预定义搜索模式；在第一次使用时就要解释这两个对象。
3. 任何查询命中模式只证明语法出现，不能把该奖励解释成答案正确或来源可信。

**摘录出处：**[Yuqin Dai et al. (AAAI 2026) · Careful Queries, Credible Results: Teaching RAG Models Advanced Web Search Tools with Reinforcement Learning](https://ojs.aaai.org/index.php/AAAI/article/view/40299)；Methodology / Source-restricting Reward，PDF第3页（刊页30460）；AAAI 2026 camera-ready；2026-03-14正式发表；已发表；作者源稿摘录

**原文／图片许可：**Yuqin Dai et al., AAAI 2026, pp.30458–30466. ©2026 AAAI，保留原版权；作者教学短引，不随本指南转授再版许可。中文为本指南翻译，拆解与教学改写单独标注。

来源与延伸阅读：[写作技能与检查方法](https://github.com/Da1yuqin/PaperBank/blob/main/SOURCES.md#写作技能)；[Yuqin Dai et al. (AAAI 2026) · Careful Queries, Credible Results: Teaching RAG Models Advanced Web Search Tools with Reinforcement Learning](https://ojs.aaai.org/index.php/AAAI/article/view/40299)

</details>

- [ ] **第 20 条：**沿一个样本说明输入、输出、评分者、规则和更新对象；区分奖励、优势、损失与梯度。

<a id="tip-20"></a>
<details>
<summary>说明、例子与参考</summary>

写清分数评价哪次输出，怎样进入更新。终端奖励若分给中间动作，要说明分配方式，不能默认每步都有贡献。

**边界：**整次任务成功，不代表每一步都有贡献。要把最终奖励分到中间动作，得交代分法。

**先区分行为信号与结果信号**

**论文原文 · English**

> The Source-restricting Reward (SR) acts as a behavior-based restriction, promoting the use of advanced search operators for precise, source-restricted queries. In contrast, the Retrieval-precision Reward (RR) serves as an outcome-based signal, leveraging external critique to assess and refine retrieval quality.

**中文翻译 · 本指南翻译**

来源限制奖励 SR 作为基于行为的约束，促进使用高级搜索操作符来构造精确且带来源限制的查询。相比之下，检索精度奖励 RR 是基于结果的信号，利用外部评判来评价并改进检索质量。

**逐句拆解**

1. SR对应操作符使用行为，RR对应外部评判的结果；两种学习信号没有混成一个“反馈”。
2. 写自己的奖励时还要逐一说明哪个模型看哪些输入、给哪个输出评分，结果更新哪个模型。
3. 原论文Implementation Details注明RR评判模型Qwen3-30B-A3B；Metrics中的GPT-4o-mini用于另一种评价，不能混称同一位judge。

**摘录出处：**[Yuqin Dai et al. (AAAI 2026) · Careful Queries, Credible Results: Teaching RAG Models Advanced Web Search Tools with Reinforcement Learning](https://ojs.aaai.org/index.php/AAAI/article/view/40299)；Methodology / Information-Filtering Reward Strategy，PDF第3页（刊页30460）；AAAI 2026 camera-ready；2026-03-14正式发表；已发表；作者源稿摘录

**原文／图片许可：**Yuqin Dai et al., AAAI 2026, pp.30458–30466. ©2026 AAAI，保留原版权；作者教学短引，不随本指南转授再版许可。中文为本指南翻译，拆解与教学改写单独标注。

来源与延伸阅读：[写作技能与检查方法](https://github.com/Da1yuqin/PaperBank/blob/main/SOURCES.md#写作技能)；[NeurIPS · Paper Checklist](https://neurips.cc/public/guides/PaperChecklist)；[Yuqin Dai et al. (AAAI 2026) · Careful Queries, Credible Results: Teaching RAG Models Advanced Web Search Tools with Reinforcement Learning](https://ojs.aaai.org/index.php/AAAI/article/view/40299)

</details>


**框架图与案例读法**

- [ ] **第 29 条：**按最终插入宽度排字，再以正常阅读大小检查 PDF；看不清就重排、精简或拆图。

<a id="tip-29"></a>
<details>
<summary>说明、例子与参考</summary>

检查放回论文后的实际效果。字号按当前模板定，不能把另一篇论文的画布尺寸直接搬来。

**边界：**字号按模板和最终效果决定，不照搬另一篇论文的画布尺寸。

**案例摘要框：先分信息，再排字**

**公开论文图例 · 点评为本指南整理**

这是原论文案例摘要，不是完整对话，也不是新收集的真实用户记录。

![InteractCS-RL 附录案例摘要框，评价和用户设定分栏](../assets/paper-interactcs-case-summary.png)

The header names the case; two columns separate evaluation scores from the simulated user profile. The dialogue continues on later pages.
深色标题交代案例，浅底分栏列出评价和用户设定；完整对话接在后页。

**逐句拆解**

1. 作者笔记强调像UI一样整洁：相同信息放一起，同类信息用同样的框，颜色只强调重点。
2. 左栏是三个评价结果，右栏是用户设定；标题、字段和值分层，不必把每个字段塞进独立气泡。
3. 字多时先分组、删重复、留白。放回双栏PDF后仍须检查字号；网页放大看清不等于论文里看清。

**摘录出处：**[Ning Gao et al. · Reinforcing Real-world Service Agents (arXiv v1)](https://arxiv.org/abs/2602.22697v1)；Appendix B.1，PDF 第13页；仅截取案例摘要框；公开 arXiv 版本；图与原 PDF 核对；公开预印本；不以项目笔记中的会议标记认定录用

**原文／图片许可：**Ning Gao et al., Reinforcing Real-world Service Agents, arXiv:2602.22697v1. CC BY 4.0（https://creativecommons.org/licenses/by/4.0/）。从原 PDF 裁切；图形、标签和数据未改。

来源与延伸阅读：[写作技能与检查方法](https://github.com/Da1yuqin/PaperBank/blob/main/SOURCES.md#写作技能)；[Rougier et al. (2014) · Ten Simple Rules for Better Figures](https://doi.org/10.1371/journal.pcbi.1003833)；[Ning Gao et al. · Reinforcing Real-world Service Agents (arXiv v1)](https://arxiv.org/abs/2602.22697v1)

</details>

- [ ] **第 30 条：**同类对象用同一颜色，全文统一；类别同时配文字、线型或形状，不只靠红绿区分。

<a id="tip-30"></a>
<details>
<summary>说明、例子与参考</summary>

先定颜色表示什么，再调美观。已有组件和新增设计可用轻重区分，类别多时以可读性为准。

**边界：**不能只靠红绿表达对错。类别确实多时，以看得清为准，别硬凑三种颜色。

**消融图：颜色分组，纹理分方法**

**公开论文图例 · 点评为本指南整理**

部分纵轴不从0开始，不能把柱高当倍数；误差线定义须查实验说明。

![InteractCS-RL Figure 2：四个消融指标，共用颜色、纹理和方法顺序](../assets/paper-interactcs-fig2.png)

All four panels share a method order. Colors identify comparison groups; hatching further distinguishes methods.
四面板共享方法顺序；颜色标比较组，纹理再区分方法。

**逐句拆解**

1. 作者绘图笔记的要点：除了颜色，柱状图的纹理也可以区分信息。
2. 读图先看图例：绿是RL基线，蓝是成本消融，橙是奖励消融，红是完整方法。
3. 四个指标沿用相同顺序，类别也能靠纹理识别。打印成灰度，信息不至于集体失联。
4. 指标旁写↑或↓：前三项高为好，发券率低为好。不同指标的柱高不能横着比。

**摘录出处：**[Ning Gao et al. · Reinforcing Real-world Service Agents (arXiv v1)](https://arxiv.org/abs/2602.22697v1)；Fig.2，PDF 第7页；公开 arXiv 版本；图与原 PDF 核对；公开预印本；不以项目笔记中的会议标记认定录用

**原文／图片许可：**Ning Gao et al., Reinforcing Real-world Service Agents, arXiv:2602.22697v1. CC BY 4.0（https://creativecommons.org/licenses/by/4.0/）。从原 PDF 裁切；图形、标签和数据未改。

来源与延伸阅读：[作者提供的写作、绘图与进阶笔记](https://github.com/Da1yuqin/PaperBank/blob/main/SOURCES.md#写作笔记)；[Rougier et al. (2014) · Ten Simple Rules for Better Figures](https://doi.org/10.1371/journal.pcbi.1003833)；[Ning Gao et al. · Reinforcing Real-world Service Agents (arXiv v1)](https://arxiv.org/abs/2602.22697v1)

</details>

- [ ] **第 32 条：**图注写清比较、指标、单位和必要图例，说明数据支持的发现；术语与正文一致。

<a id="tip-32"></a>
<details>
<summary>说明、例子与参考</summary>

解释影响读法的颜色、线型、误差条和统计方式。图中缩写给全称，图注保留独立读懂所需的信息，不复制整段分析。

**边界：**图注不用复制整段分析。把看懂图所必需的信息留下就行。

**图注：给读者一份读图说明**

**假设图注，非论文原文、非实测结果**

条件与数值为示范；使用前换成已核对的实验记录。

**改前 · 中文**

我们的方法取得了卓越表现。

**Before · English**

Our method achieves superior performance.

**改后 · 中文**

200道模拟多轮问题上的引用支持率，模型和证据上下文总预算相同。每题先计算支持率，再取平均；越高越好。

**After · English**

Citation support on 200 illustrative multi-turn questions, with the same model and total evidence-context budget. Support is computed per question and then averaged. Higher is better.

**逐句拆解**

1. 先写比较对象和设置，再解释指标如何算、方向是什么。
2. 有颜色就解释颜色，有误差条就解释统计量。图注没写的内容，读者没义务通灵。
3. 这段没有声称显著或因果。要写它们，另给对应检验和设计。

来源与延伸阅读：[写作技能与检查方法](https://github.com/Da1yuqin/PaperBank/blob/main/SOURCES.md#写作技能)；[Rougier et al. (2014) · Ten Simple Rules for Better Figures](https://doi.org/10.1371/journal.pcbi.1003833)；[NeurIPS · Paper Checklist](https://neurips.cc/public/guides/PaperChecklist)

</details>

- [ ] **第 91 条：**按模板插入宽度排字，在最终 PDF 查字号、字形、遮挡、裁切和读序；需可选文字就抽取验证。

<a id="tip-91"></a>
<details>
<summary>说明、例子与参考</summary>

源图清楚或编译通过都不够。字体、色板和尺寸按当前模板与读者需要定。

**边界：**字号、色板和版式以当前模板及读者需求为准，不要求固定尺寸或固定配色。

**按最终尺寸验收，别只看放大预览**

**教学示例：假设情境，非论文原文／实测记录**

改后假定已有对应记录；实际改稿须先核对这些事实，不能从改前文字推断或补造。

**逐句拆解**

缩图会连带缩字；把位图装进 PDF 也不会自动得到原生文字。

**教学改写 · English（非论文原文）**

A 160 mm source figure will be inserted at 80 mm, so its text will shrink by half. Re-export it for 80 mm and inspect the inserted page; extract the labels if the deliverable requires selectable text.

**教学改写 · 中文（非论文原文）**

源图宽 160 mm，插入论文时只有 80 mm，图中文字也会缩成一半。按 80 mm 重新导出，再看实际论文页面；交付要求文字可选择时，还要抽取标签验证。

来源与延伸阅读：[写作技能与检查方法](https://github.com/Da1yuqin/PaperBank/blob/main/SOURCES.md#写作技能)

</details>

- [ ] **第 92 条：**全文统一颜色、线型与名称；通过、失败、不适用用文字或符号分开，图例说明实际状态。

<a id="tip-92"></a>
<details>
<summary>说明、例子与参考</summary>

底纹可分组，判断用明确标签。没有通过记录，不画一个勾暗示已经通过。

**边界：**字号、色板和版式以当前模板及读者需求为准，不要求固定尺寸或固定配色。

**同一含义用同一标记，结论别只靠颜色**

**教学示例：假设情境，非论文原文／实测记录**

改后假定已有对应记录；实际改稿须先核对这些事实，不能从改前文字推断或补造。

**逐句拆解**

蓝色只是这个示例的自定映射，其他论文可以选自己的色板，但要前后一致。

**教学改写 · English（非论文原文）**

Blue dashed boxes denote model inputs throughout the paper. An evaluated rule is labeled Pass, Fail, or N/A; a rule that has not been evaluated remains unchecked.

**教学改写 · 中文（非论文原文）**

全文都用蓝色虚线框表示模型输入。已经评价的规则写通过、失败或不适用；还没评价的规则保留空框。

来源与延伸阅读：[写作技能与检查方法](https://github.com/Da1yuqin/PaperBank/blob/main/SOURCES.md#写作技能)

</details>

- [ ] **第 95 条：**教学例子、模型实测、人工评价与总体实验分开；无记录，不画评分、分歧或修订结果。

<a id="tip-95"></a>
<details>
<summary>说明、例子与参考</summary>

一个例子可以解释方法，不能证明模型实际如此回答，也不能代替总体实验。

**边界：**数据、信息边界和完成状态按实际记录说明。

**作者构造的例子，别写成模型实测**

**教学示例：假设情境，非论文原文／实测记录**

改后假定已有对应记录；实际改稿须先核对这些事实，不能从改前文字推断或补造。

**逐句拆解**

图面附近标出例子身份；总体表现仍由有记录的测试来支持。

**教学改写 · English（非论文原文）**

Illustrative response written by the authors: the assistant requests the missing budget before recommending an option. This example explains the intended behavior; it is not a recorded model output or evidence of a pass rate.

**教学改写 · 中文（非论文原文）**

作者构造的示例回复：助手先询问缺失的预算，再给建议。这个例子解释预期行为，不是记录中的模型输出，也不能证明通过率。

来源与延伸阅读：[写作技能与检查方法](https://github.com/Da1yuqin/PaperBank/blob/main/SOURCES.md#写作技能)

</details>


</details>


<a id="experiments"></a>
## 6. 实验

用公平比较回答研究问题，报告发现、取舍与条件。

### 实验·示范自然段1：研究问题

先确定要回答的问题，再决定比较和图表。

教学例句，非论文原文或实测结果。

We ask whether evidence notes improve citation support under a fixed language model and evidence-context token budget.

我们检验在语言模型和证据上下文词元预算固定时，证据笔记能否提高引用支持率。

**第 1 句：**问题、后面的公平比较和结果使用同一模型与实际生成输入预算，不把检索长度当全部输入成本。

We also test whether retaining earlier constraints contributes to this change.

我们还检验保留前文约束是否对这一变化有贡献。

**第 2 句：**第二个问题对应机制消融；RQ编号可用，也可以不用。

### 实验·示范自然段2：数据与指标

把样本范围、指标分母和评分方式说明白。

教学例句，非论文原文或实测结果。

The illustrative test set contains 200 multi-turn questions about static English manuals.

这份模拟测试集包含200个针对静态英语手册的多轮问题。

**第 1 句：**对象、范围和样本单位先写清；200是教学设定，不是实际采集量。

Under the illustrative protocol, human raters check each factual answer sentence against its cited evidence using the same rule.

在假设评分协议中，人工按同一规则核验每句事实能否由所引证据支持。

**第 2 句：**说明谁检查什么、按什么规则检查。真实实验还需报告评分说明与质量核验。

A factual sentence without a citation counts as unsupported.

没有引用的事实句按不支持计。

**第 3 句：**缺引用的句子也计入事实句分母，不能靠少给引用提高支持率。

For each question, citation support is the fraction of factual answer sentences supported by their cited evidence.

每个问题的引用支持率是其回答中获所引证据支持的事实句比例。

**第 4 句：**先以单个问题的事实句数作分母，而非把200个问题当事实句分母。

We then average the per-question rates, rather than pooling sentences across questions.

再对各问题的支持率取平均，不把所有问题的事实句混在一起计算。

**第 5 句：**先按问题计算，再汇总；回答较长的问题不会仅因事实句多而获得更大权重。

Answers with no factual sentences are reported separately as not applicable, with their count.

无事实句的回答单列不适用，并报告数量。

**第 6 句：**明确不能计算句子比例的情形，不填零、不静默删除；比较时核对两组的适用范围。

### 实验·示范自然段3：公平比较

按任务介绍基线，并对齐会影响结果的条件。

教学例句，非论文原文或实测结果。

We compare evidence notes with direct passage retrieval using the same language model.

我们在同一语言模型上比较证据笔记和直接片段检索。

**第 1 句：**基线按处理证据的方式介绍，而不是只列名字。

Both systems use the same evidence-context token budget and decoding settings.

两套系统使用相同的证据上下文词元预算与解码设置。

**第 2 句：**预算计入实际输入生成器的证据与笔记，避免只对齐检索长度却增加额外输入。

### 实验·示范自然段4：主要发现

先回答研究问题，再解释主要比较和取舍。

论文原文短引 · 中文为本指南翻译

TCDiff 评价群舞与个体动作，下面摘录结果分析里的收益与代价句。

TCDiff effectively captures inter-dancer correlations (high GMC) with a slight trade-off in individual fidelity (FID).

TCDiff 能较好捕捉舞者间相关性（GMC 较高），同时在个体保真度（FID）上存在一定代价。

**第 1 句：**一句同时报告舞者间协调性收益与个体保真度代价；结果分析要解释取舍，不能只说整体更好。

[Yuqin Dai et al. (AAAI 2025) · Harmonious Music-driven Group Choreography with Trajectory-Controllable Diffusion](https://ojs.aaai.org/index.php/AAAI/article/view/32268) · §Quantitative Results，第3句；PDF p.6，proceedings p.2650；Table 1；正式发表版本；作者原文短引

### 实验·示范自然段5：消融与解释

一次改变待检验因素，说明结果支持什么。

教学例句，非论文原文或实测结果。

We remove prior constraints from the notes while keeping source quotes unchanged.

我们从笔记中移除前文约束，保留来源摘句。

**第 1 句：**只改变一个因素，对应第二个研究问题。

If support decreases, this comparison indicates the value of retained constraints in the tested setting.

若支持率下降，这个比较说明在该设置下保留约束有用。

**第 2 句：**若唯一改动后表现下降，就支持该因素在当前设置下有用。

### 实验·示范自然段6：稳健性与复测

按主张补重复或分组检验，别只保留最好一次。

教学例句，非论文原文或实测结果。

We repeat generation with several seeds and report variation across runs.

我们用多个随机种子重复生成，并报告运行间变化。

**第 1 句：**说明重复单位和差异来源；真实稿件还需给具体次数与统计方式。

We also compare short and long dialogue histories using the same scoring rule.

我们还用同一评分规则比较短对话和长对话。

**第 2 句：**分组检验直接围绕跨轮约束，不为凑实验随意增加维度。

### 实验·示范自然段7：案例分析

用一个明确来源的案例解释流程与失败，别以案例代替总体证据。

教学例句，非论文原文或实测结果。

In a constructed example, the user requires offline operation in an earlier turn.

在一个构造案例中，用户在上一轮要求离线操作。

**第 1 句：**用技术手册问答中的具体约束说明跨轮过程，并先标明构造案例。

The case shows where the constraint enters the note, but it does not establish overall success.

案例展示约束在哪里进入笔记，但不能证明总体成功率。

**第 2 句：**案例服务于流程理解，整体效果仍看正式实验。

<details>
<summary>检查清单和真实论文例子（19 项）</summary>


**问题与比较设计**

- [ ] **第 53 条：**研究问题写清对象、条件和比较，逐项对到实验与结论；编号可选，探索与事先假设分开。

<a id="tip-53"></a>
<details>
<summary>说明、例子与参考</summary>

RQ 是要查明什么，假设是对结果的可检验预测。不要看到涨分后倒写问题，也不把 Registered Reports 要求套到全部 CS 论文。

**边界：**问题需说明指标和比较条件；效果阈值可按研究目的预先定义，别根据已看到的涨分倒写问题。RQ 不等于假设，Registered Reports 的规划要求也不能直接套到全部 CS 论文。

**UrbanZero：RQ 写成能由对照回答的问题**

**教学改写：依据 UrbanZero 公开项目介绍，非论文原文**

依据公开项目介绍中的语义简报、地块任务、逐块规划和程序反馈编写。中英示例为本指南教学改写；实验问题和模拟回复方案不代表项目已完成的工作。

**改前 · 中文**

RQ：我们的方案是不是非常有效？

**Before · English**

RQ: Is our approach highly effective?

**改后 · 中文**

教学 RQ：在模型与检查器相同的条件下，逐块规划是否比全图规划更容易完成有效地块分配？五类空间目标的得分如何变化？

**After · English**

Teaching RQ: with the same model and verifier, does patch-wise planning complete valid parcel assignments more reliably than full-map planning? How do scores change across the five spatial objectives?

**逐句拆解**

1. 问题给出对象、条件与待比较关系，可对应完成率和质量两类记录。
2. 编号本身不增加证据；这是本指南提出的教学问题，不声称项目原论文使用了这组 RQ。

来源与延伸阅读：[作者提供的写作、绘图与进阶笔记](https://github.com/Da1yuqin/PaperBank/blob/main/SOURCES.md#写作笔记)；[Henderson & Chambers (2022) · Ten simple rules for writing a Registered Report](https://doi.org/10.1371/journal.pcbi.1010571)；[NeurIPS · Paper Checklist](https://neurips.cc/public/guides/PaperChecklist)；[Chaoyang Shi, Yuqin Dai et al. · UrbanZero（公开项目介绍）](https://github.com/Da1yuqin/Da1yuqin.github.io/blob/main/_pages/includes/pub.md#L193-L202)

</details>

- [ ] **第 21 条：**每个实验写清检验哪项主张、固定什么、改变什么、比较谁；不按涨分倒改问题。

<a id="tip-21"></a>
<details>
<summary>说明、例子与参考</summary>

按问题选数据、对照和指标。先想什么结果会支持主张，什么结果需要收回主张，再决定跑什么。

**边界：**不要因为某个设置容易涨分，就倒过来把它当成论文一直要解决的问题。

**UrbanZero：先写逐块求解要验证什么**

**教学改写：依据 UrbanZero 公开项目介绍，非论文原文**

依据公开项目介绍中的语义简报、地块任务、逐块规划和程序反馈编写。中英示例为本指南教学改写；实验问题和模拟回复方案不代表项目已完成的工作。

**改前 · 中文**

多跑几套模型，看哪个分数最高。

**Before · English**

Run more models and report the highest score.

**改后 · 中文**

教学实验方案：固定模型、城市窗口和检查器，只改变逐块与全图求解方式；同时比较完成率和五类空间目标得分。

**After · English**

Teaching experiment: fix the model, urban windows, and verifier; vary patch-wise versus full-map solving. Compare completion rates and scores on the five spatial objectives.

**逐句拆解**

1. 完成率查能不能交出完整方案，目标分查交出的方案质量，两者不要混成一个模糊效果。
2. 这是拟议对照；需先确定解析规则、预算与失败计分，不能冒充原文已经按此方案测过。

来源与延伸阅读：[作者提供的写作、绘图与进阶笔记](https://github.com/Da1yuqin/PaperBank/blob/main/SOURCES.md#写作笔记)；[Chaoyang Shi, Yuqin Dai et al. · UrbanZero（公开项目介绍）](https://github.com/Da1yuqin/Da1yuqin.github.io/blob/main/_pages/includes/pub.md#L193-L202)

</details>

- [ ] **第 22 条：**交代模型、数据、可见信息、调参机会和预算；尽量匹配，不能匹配的差别照实报。

<a id="tip-22"></a>
<details>
<summary>说明、例子与参考</summary>

方法比较先看条件。双方应有合理调参机会；资源差距影响解释时，补同预算比较或明确限制。

**边界：**公平不等于超参数一模一样。关键是比较符合问题，双方都有合理的发挥机会。

**比较前交代共同训练数据**

**论文原文 · English**

> To ensure fairness, all the trainable models mentioned above are trained and tested on RPLAN.

**中文翻译 · 本指南翻译**

为保证公平，上述所有可训练模型都在RPLAN上训练和测试。

**逐句拆解**

1. 比较条件先落到共同的数据集，读者不会把训练数据差异误当成方法收益。
2. “所有可训练模型”限定了这项安排的对象，不能扩大为所有系统的模型容量、预算和输入都相同。
3. 自己的实验还要交代输入权限、训练规模与预算；同一数据集只是公平比较的一部分。

**摘录出处：**[Pengyu Zeng et al. (EMNLP 2025) · CARD: Cross-modal Agent Framework for Generative and Editable Residential Design](https://aclanthology.org/2025.emnlp-main.473/)；§4.1 Experimental Settings，PDF第6页（刊页9309）；EMNLP 2025正式发表版；已发表；CC BY 4.0

**原文／图片许可：**Pengyu Zeng et al., EMNLP 2025, pp.9304–9319. 原文采用 CC BY 4.0；中文翻译、拆解为本指南新增。

来源与延伸阅读：[写作技能与检查方法](https://github.com/Da1yuqin/PaperBank/blob/main/SOURCES.md#写作技能)；[NeurIPS · Paper Checklist](https://neurips.cc/public/guides/PaperChecklist)；[Pengyu Zeng et al. (EMNLP 2025) · CARD: Cross-modal Agent Framework for Generative and Editable Residential Design](https://aclanthology.org/2025.emnlp-main.473/)

</details>

- [ ] **第 24 条：**按解决的问题给基线分组，说明选择理由、来源和改动；不能绕开最相近工作。

<a id="tip-24"></a>
<details>
<summary>说明、例子与参考</summary>

每组先讲共同思路，再说为什么与本研究可比。结果分析沿用分组，影响公平性的实现改动单独说明。

**边界：**相关不等于一定可比，但最相近的工作不能因为不好超过就跳过去。

**SAGE：比较模型先交代分组依据**

**论文原文 · English**

> We evaluate 27 representative Large Language Models (LLMs) across closed-source and open-source families, covering diverse scales and architectures.

**中文翻译 · 本指南翻译**

我们评估来自闭源和开源系列的 27 个代表性大语言模型（LLM），覆盖不同规模与架构。

**逐句拆解**

1. 这句先按闭源与开源、规模与架构交代比较范围，后文再列具体系列，读者更容易组织方法名。
2. SAGE 是基准论文，这里分组的是被测模型；方法论文的基线应按解决的问题与技术路线分组，不能直接照搬商业属性。
3. 接着说明闭源模型经官方 API、开源模型经 vLLM 使用；模型分组清楚不等于部署条件完全相同。

**教学改写 · English（非论文原文）**

Teaching adaptation: first state the service-agent task and why each evaluated model belongs in the comparison. Report open versus closed access and model scale as coverage dimensions, rather than presenting them as different solutions to the research problem.

**教学改写 · 中文（非论文原文）**

教学迁移：先说被测服务智能体承担什么任务、为什么选这些模型。开闭源与规模另作为覆盖维度汇报，不能把商业属性当作解决研究问题的不同技术路线。

**摘录出处：**[Ling Shi, Yuqin Dai et al. · SAGE: An Extensible Benchmark for Service Agent Graph-guided Evaluation](https://arxiv.org/abs/2604.09285)；§ Experiments / Experiment Settings，第一段首句（作者源稿第 737 行）；作者终稿 2026-10-04 只读快照；公开链接为 arXiv v1；作者终稿短引；公开链接为不同版本预印本

**原文／图片许可：**作者终稿教学短引，保留原论文版权；不随 PaperBank 原创内容转授终稿转载权。公开 arXiv v1 的 CC BY 4.0 已核验，该许可不自动延伸到不同版本的作者终稿。

来源与延伸阅读：[作者提供的写作、绘图与进阶笔记](https://github.com/Da1yuqin/PaperBank/blob/main/SOURCES.md#写作笔记)；[Ling Shi, Yuqin Dai et al. · SAGE: An Extensible Benchmark for Service Agent Graph-guided Evaluation](https://arxiv.org/abs/2604.09285)

</details>

- [ ] **第 93 条：**人数、记录数、任务数与重复次数分开；说明共同样本、协议和无效项，不拿子集冒充全量。

<a id="tip-93"></a>
<details>
<summary>说明、例子与参考</summary>

同名指标也可能有不同分母。先核对单位和纳入规则，再做比较。

**边界：**数据、信息边界和完成状态按实际记录说明。

**比较用同一口径，样本写清单位与分母**

**教学示例：假设情境，非论文原文／实测记录**

改后假定已有对应记录；实际改稿须先核对这些事实，不能从改前文字推断或补造。

**逐句拆解**

先核对实际比较范围；是否把无效输出计入主指标，必须由评价协议决定并公开。

**教学改写 · English（非论文原文）**

On the 90 tasks for which both methods returned valid outputs, A scores 72/90 and B scores 75/90. Report the excluded 10 tasks and the invalid-output policy; these conditional scores do not describe all 100 tasks.

**教学改写 · 中文（非论文原文）**

两种方法都输出有效答案的 90 个任务中，A 答对 72 个，B 答对 75 个。另报排除的 10 个任务和无效输出处理规则；这组条件得分不代表全部 100 个任务。

来源与延伸阅读：[写作技能与检查方法](https://github.com/Da1yuqin/PaperBank/blob/main/SOURCES.md#写作技能)

</details>


**指标与主要发现**

- [ ] **第 23 条：**指标写清对象、分母、算法、方向与汇总；交代缺失项，分清百分点和相对增幅。

<a id="tip-23"></a>
<details>
<summary>说明、例子与参考</summary>

宏平均、微平均和不适用项处理分别解释。40% 到 50% 是增加 10 个百分点，相对增加 25%。

**边界：**从 40% 到 50% 是增加 10 个百分点，相对增加 25%。两种说法不要混着用。

**SAGE：路径指标说清比较对象与分母**

**论文原文 · English**

> Path Correctness measures the overlap between the agent's planned path and the Rule Engine's reference path:

**中文翻译 · 本指南翻译**

路径正确性衡量智能体规划路径与规则引擎参考路径之间的重合：

**逐句拆解**

1. 原句先说清比较的是两条路径；紧接的公式以参考路径长度为分母，不是以模型输出长度为分母。
2. 这个指标检查路径节点的重合；不能把高重合直接说成整条路径顺序完全正确，动作正确性还单独评价。
3. 教学例子只演示原公式，不是论文报告的实验个案或真实得分。

**教学改写 · English（非论文原文）**

Teaching example: suppose the reference path contains four distinct nodes and the predicted path shares two of those nodes. The reported overlap formula gives 2/4 = 0.5. This calculation alone does not verify node order or the final action.

**教学改写 · 中文（非论文原文）**

教学示例：假设参考路径包含四个不同节点，模型路径与参考路径共有其中两个节点。按原文重合公式，得分为 2/4 = 0.5。仅凭这项计算，不能确认节点顺序或最终动作正确。

**摘录出处：**[Ling Shi, Yuqin Dai et al. · SAGE: An Extensible Benchmark for Service Agent Graph-guided Evaluation](https://arxiv.org/abs/2604.09285)；公开 arXiv v1，§ 3.2.4 Dual-Axis Evaluation Metrics / Logical Compliance Evaluation，Path Correctness，式 (6)；作者终稿中亦保留同句；arXiv:2604.09285v1（2026-04-10）；与作者终稿相同短句已核对；公开预印本短引；教学示例非实验记录

**原文／图片许可：**Ling Shi, Yuqin Dai et al., SAGE, arXiv:2604.09285v1, 2026. CC BY 4.0；保留作者、题名、出处与版本。中文翻译和教学示例为本指南新增。

来源与延伸阅读：[作者提供的写作、绘图与进阶笔记](https://github.com/Da1yuqin/PaperBank/blob/main/SOURCES.md#写作笔记)；[NeurIPS · Paper Checklist](https://neurips.cc/public/guides/PaperChecklist)；[Ling Shi, Yuqin Dai et al. · SAGE: An Extensible Benchmark for Service Agent Graph-guided Evaluation](https://arxiv.org/abs/2604.09285)

</details>

- [ ] **第 25 条：**先写发现，再给图表、比较条件和必要差值；无对照支持的原因只作可能解释。

<a id="tip-25"></a>
<details>
<summary>说明、例子与参考</summary>

正文解释差别意味着什么、回应哪个问题，不逐行报分数。一个关键差值够用时，把剩余篇幅留给解释。

**边界：**可能原因就说可能。没有对照支持，别把顺耳的解释写成已经证明的机制。

**PlanCraft：先说趋势，再解释它意味着什么**

**论文原文 · English**

> Additional vectors mainly sharpen geometry.

**中文翻译 · 本指南翻译**

增加矢量主要使几何形状更精细。

**逐句拆解**

1. 这句先给段落的观察重点，随后原文用 Figure 3 说明 PSNR、IoU 在 25%–50% 完成度区间变化更明显，而 SSIM 变化较缓。
2. 后文关于粗分区与墙体细化的解释使用 suggests；指标走势与机制解释应分开，不能把观察到的相关变化写成已证明的原因。

**教学改写 · English（非论文原文）**

Additional vectors mainly sharpen geometry: PSNR and IoU change most strongly between 25% and 50% completeness, while SSIM changes more gradually. This pattern suggests, rather than proves, that later vectors refine wall placement.

**教学改写 · 中文（非论文原文）**

增加矢量主要细化几何：完成度从 25% 到 50% 时，PSNR 和 IoU 的变化更明显，SSIM 则较缓。这种趋势提示后续矢量主要细化墙体位置，尚不能单凭趋势证明机制。

**摘录出处：**[Zeng, Dai et al. (2026 预印本) · PlanCraft: Sketch, Refine, and Furnish for Architect-Inspired Progressive 3D Residential Scene Generation](https://arxiv.org/abs/2607.23491v3)；Experiments / Effect of Vector Completeness，结果段主题句；PDF 第 5 页（Figure 3 见第 6 页）；arXiv:2607.23491v3，2026-09-05；短引对照作者源稿及公开 v3 正文；公开预印本；教学改写不是论文原文或新增实测结果

**原文／图片许可：**Pengyu Zeng et al., arXiv:2607.23491v3 (2026). arXiv 为非独占分发许可，原文版权由权利人保留；作者授权的教学短引，不随本指南转授全文或原图再版许可。中文翻译、拆解及教学改写为本指南新增。

来源与延伸阅读：[写作技能与检查方法](https://github.com/Da1yuqin/PaperBank/blob/main/SOURCES.md#写作技能)；[NeurIPS · Paper Checklist](https://neurips.cc/public/guides/PaperChecklist)；[Mensh & Kording (2017) · Ten simple rules for structuring papers](https://doi.org/10.1371/journal.pcbi.1005619)；[Zeng, Dai et al. (2026 预印本) · PlanCraft: Sketch, Refine, and Furnish for Architect-Inspired Progressive 3D Residential Scene Generation](https://arxiv.org/abs/2607.23491v3)

</details>

- [ ] **第 86 条：**先写图表支持的关系，再说明回答哪个问题；保留条件和关键数字，不逐格抄分数。

<a id="tip-86"></a>
<details>
<summary>说明、例子与参考</summary>

表格放细数，正文讲比较的意义和证据支持的解释。

**边界：**适用：主实验、消融和案例分析。这是推荐写法，按论文类型和当前投稿要求调整；清晰的代词和必要的长句可以保留。

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

来源与延伸阅读：[写作技能与检查方法](https://github.com/Da1yuqin/PaperBank/blob/main/SOURCES.md#写作技能)

</details>

- [ ] **第 74 条：**先写观察，再写可能解释；没有排除替代解释的设计，不把相关性写成因果。

<a id="tip-74"></a>
<details>
<summary>说明、例子与参考</summary>

解释看起来合理，还不等于机制已经证实。因果结论说明对应识别条件。

**边界：**适用：结果分析和机制讨论。证据与记录必须如实；不适用的检查注明原因。

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

来源与延伸阅读：[写作技能与检查方法](https://github.com/Da1yuqin/PaperBank/blob/main/SOURCES.md#写作技能)

</details>

- [ ] **第 94 条：**同指标、同协议下判断最优，交代方向和并列；均值、标准差、区间写清，显著性另给依据。

<a id="tip-94"></a>
<details>
<summary>说明、例子与参考</summary>

粗体与底色只是排序标记，不能证明稳定领先或统计显著。

**边界：**数据、信息边界和完成状态按实际记录说明。

**最优按列判断，显著性另给证据**

**教学示例：假设情境，非论文原文／实测记录**

改后假定已有对应记录；实际改稿须先核对这些事实，不能从改前文字推断或补造。

**逐句拆解**

排名、显示精度和统计推断是三件事；不能用更多小数位或颜色制造结论。

**教学改写 · English（非论文原文）**

A and B both display 80.0 accuracy, so they share the displayed rank. If boldface marks the highest displayed value, define that rule. Claim a statistically significant difference only when the specified comparison and test support it.

**教学改写 · 中文（非论文原文）**

A 和 B 的准确率都显示为 80.0，就共享这个显示值的排名。若粗体表示最高显示值，在表注写明。只有指定比较和统计检验支持时，才能说差异显著。

来源与延伸阅读：[写作技能与检查方法](https://github.com/Da1yuqin/PaperBank/blob/main/SOURCES.md#写作技能)

</details>


**消融与原因判断**

- [ ] **第 26 条：**组件消融尽量只改一个因素；参数分析另报范围，无法控制的差别照实说明。

<a id="tip-26"></a>
<details>
<summary>说明、例子与参考</summary>

组件作用与参数敏感性分开讨论。删除模块时同时换模型、减预算或改提示词，就不能把全部差异归给模块。

**边界：**控制不了的差别照实写。结果解释的底气，来自实验设计，不来自语气。

**UrbanZero：去掉反馈时保留哪些条件**

**教学改写：依据 UrbanZero 公开项目介绍，非论文原文**

依据公开项目介绍中的语义简报、地块任务、逐块规划和程序反馈编写。中英示例为本指南教学改写；实验问题和模拟回复方案不代表项目已完成的工作。

**改前 · 中文**

去掉反馈，同时换模型、换窗口、减少生成次数。

**Before · English**

Remove feedback, switch models and windows, and use fewer samples.

**改后 · 中文**

教学消融方案：固定模型、任务编译、逐块求解和生成预算，只关闭结果反馈；再检查任务难度与规划质量怎样变化。

**After · English**

Teaching ablation: keep the model, task compiler, patch-wise solver, and generation budget fixed; disable only outcome feedback. Then examine task difficulty and planning quality.

**逐句拆解**

1. 一次改变三个因素，分数差无法对应到反馈；改后先把固定项列清。
2. 关闭反馈可能改变后续任务分布，因而还要报告任务变化；这不是“所有条件完全一样”的保证。

来源与延伸阅读：[写作技能与检查方法](https://github.com/Da1yuqin/PaperBank/blob/main/SOURCES.md#写作技能)；[NeurIPS · Paper Checklist](https://neurips.cc/public/guides/PaperChecklist)；[Chaoyang Shi, Yuqin Dai et al. · UrbanZero（公开项目介绍）](https://github.com/Da1yuqin/Da1yuqin.github.io/blob/main/_pages/includes/pub.md#L193-L202)

</details>

- [ ] **第 75 条：**写清固定项和改变项；模型、模块一起变化，只能说明整套配置的差异。

<a id="tip-75"></a>
<details>
<summary>说明、例子与参考</summary>

比较组件作用，尽量只改变目标组件；多项改变的收益不能全部算给一个模块。

**边界：**适用：消融、基线比较和组件收益。证据与记录必须如实；不适用的检查注明原因。

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

来源与延伸阅读：[写作技能与检查方法](https://github.com/Da1yuqin/PaperBank/blob/main/SOURCES.md#写作技能)

</details>


**取舍与负结果**

- [ ] **第 27 条：**保留全部运行，说明重复次数、变化因素和统计方式；报告波动，不只挑最高分。

<a id="tip-27"></a>
<details>
<summary>说明、例子与参考</summary>

误差条对应种子、划分还是案例差异，先定义再绘制。未运行不是零，最高分不等于稳定领先。

**边界：**没运行不是 0，最高分也不等于稳定领先。“显著”不是“看着差得挺多”的同义词。

**平均值之外还要让波动可见**

**论文原文 · English**

> A total of 37 experts and users were invited, and each person conducted 10 tests. The final result is the average value calculated from these tests.

**中文翻译 · 本指南翻译**

共邀请37位专家和用户，每人进行10次测试。最终结果是这些测试所得的平均值。

**逐句拆解**

1. 报告参与者数量、每人测试次数和平均方式，比只挑一次最好看的评分更清楚。
2. 这里重复的是人类评价任务，不能冒充多随机种子的模型训练。
3. 平均值仍不足以显示波动；自己的研究应按适当统计单位补充分布、标准差或区间，并明确独立样本的分母。

**摘录出处：**[Pengyu Zeng et al. (EMNLP 2025) · CARD: Cross-modal Agent Framework for Generative and Editable Residential Design](https://aclanthology.org/2025.emnlp-main.473/)；§4.4 CARD User Study / Consistency and Rationality，PDF第8页（刊页9311）；EMNLP 2025正式发表版；已发表；CC BY 4.0

**原文／图片许可：**Pengyu Zeng et al., EMNLP 2025, pp.9304–9319. 原文采用 CC BY 4.0；中文翻译、拆解为本指南新增。

来源与延伸阅读：[NeurIPS · Paper Checklist](https://neurips.cc/public/guides/PaperChecklist)；[Pengyu Zeng et al. (EMNLP 2025) · CARD: Cross-modal Agent Framework for Generative and Editable Residential Design](https://aclanthology.org/2025.emnlp-main.473/)

</details>

- [ ] **第 5 条：**保存失败实验的配置、输出和原因；区分程序故障与方法失效，保留重要负结果。

<a id="tip-05"></a>
<details>
<summary>说明、例子与参考</summary>

负结果也要检查对照。记录哪些条件下失效、哪些直觉不成立，后续分析和回复才能找回依据。

**边界：**程序出错和方法失效是两回事。负结果也得检查对照，不能把一个故障写成一个发现。

**GreenPlanner：较弱消融也要保留，别只抄涨分的一行**

**论文原文 · English**

> Pass rate (%) comparison under different input modes (Graph vs. Edge) across Base, w/o RL, and w/ RL.

**中文翻译 · 本指南翻译**

比较不同输入方式（Graph 与 Edge）下 Base、无 RL 和有 RL 的通过率（%）。

**逐句拆解**

1. 表 5 的 Graph 设置中，Fire 通过率从 Base 的 41.95% 到无 RL 的 38.75%，没有提升；加入 RL 后才到 79.38%。保留较弱变体，才能分清数据替换与 RL 的作用。
2. 这是一组有效消融的负向比较，不是程序崩溃。连同 Graph 输入、Fire 指标和三个变体一起保存，不能写成换数据必然改善全部约束。

**教学改写 · English（非论文原文）**

Teaching rewrite: Under Graph inputs, the Fire pass rate is 41.95% for Base, 38.75% without RL, and 79.38% for the full model. Retain the weaker no-RL result when discussing the separate effects of dataset replacement and RL.

**教学改写 · 中文（非论文原文）**

教学改写：在 Graph 输入下，Base、无 RL 和完整模型的 Fire 通过率分别为 41.95%、38.75% 和 79.38%。讨论更换数据与 RL 的不同作用时，保留无 RL 变体较弱的结果。

**摘录出处：**[Pengyu Zeng et al. (CVPR Findings 2026) · GreenPlanner: Practical Floorplan Layout Generation via an Energy-Aware and Function-Feasible Generative Framework](https://openaccess.thecvf.com/content/CVPR2026F/html/Zeng_GreenPlanner_Practical_Floorplan_Layout_Generation_via_an_Energy-Aware_and_Function-Feasible_CVPRF_2026_paper.html)；§4.7 Ablation Study，Table 5 表题与 Graph / Fire 行；PDF p.8，proceedings p.8603；CVF Open Access 作者接受版；正式发表元数据已由 CVF 条目核对；该工作已发表；引文版本单独标明；教学改写与模拟回复不属于论文原文

**原文／图片许可：**原权利人保留版权；CVF Open Access 未声明 CC BY。本指南仅作署名教学短引，不重新发布全文或原图，不向第三方转授原论文版权。

来源与延伸阅读：[作者提供的写作、绘图与进阶笔记](https://github.com/Da1yuqin/PaperBank/blob/main/SOURCES.md#写作笔记)；[Pengyu Zeng et al. (CVPR Findings 2026) · GreenPlanner: Practical Floorplan Layout Generation via an Energy-Aware and Function-Feasible Generative Framework](https://openaccess.thecvf.com/content/CVPR2026F/html/Zeng_GreenPlanner_Practical_Floorplan_Layout_Generation_via_an_Energy-Aware_and_Function-Feasible_CVPRF_2026_paper.html)

</details>

- [ ] **第 59 条：**性能与成本同图时写清坐标、单位和方向，统一预算条件；相对改善同时给绝对值。

<a id="tip-59"></a>
<details>
<summary>说明、例子与参考</summary>

说明 token、耗时或费用怎样统计，性能用已定义指标。配置选择规则、原数、分母和百分点差值保留，不能用测试集反复挑点。

**边界：**测试集不能用来反复挑最漂亮的点；漂亮的散点位置不证明部署净收益，经济结论另需相应成本与场景。

**TCDiff++：序列建模效率与动作指标分开报告**

**论文原文 · English**

> The SD replaces the Transformer with a State Space Model, enabling more efficient and coherent long-sequence modeling.

**中文翻译 · 本指南翻译**

SD 用状态空间模型替换 Transformer，以支持更高效且更连贯的长序列建模。

**逐句拆解**

1. 表 4 加入 SD 后，GMR 从 23.95 降至 14.67，FID 从 24.75 降至 20.37，但 PFC 从 1.49 升至 1.53；质量收益并非每列同向。
2. 原句未给运行时间、峰值显存或能耗测量，表 4 也不是成本表。性能与成本双维比较要另有统一长度、硬件和预算下的真实测量，不能凭“更高效”补加速倍数。

**教学改写 · English（非论文原文）**

Teaching rewrite: Report the quality changes from Table 4 separately from measured runtime or memory cost. Do not turn the architectural efficiency claim into an unreported speedup; keep the PFC increase beside the quality gains.

**教学改写 · 中文（非论文原文）**

教学改写：将表 4 的质量变化与实测运行时间或显存成本分开报告。不能把结构层面的效率描述改成未报告的加速倍数；质量收益旁保留 PFC 的上升。

**摘录出处：**[Yuqin Dai et al. (IJCV 2026；引文为 arXiv v4) · TCDiff++: An End-to-end Trajectory-Controllable Diffusion Model for Harmonious Music-Driven Group Choreography](https://link.springer.com/article/10.1007/s11263-025-02611-3)；§5.4 Ablation Study，Impact of Sequence Decoder (SD)，第1句；arXiv v4 PDF p.16；Table 4；短引来自 arXiv:2506.18671v4，2025-10-05；正式期刊元数据已核对，不将作者稿等同于期刊排版终版；该工作已发表；引文版本单独标明；教学改写与模拟回复不属于论文原文

**原文／图片许可：**arXiv 作者稿采用 non-exclusive distribution 许可，非 CC BY。正式期刊版权按 Springer 出版协议保留；本指南不向第三方转授原论文版权。

来源与延伸阅读：[作者提供的写作、绘图与进阶笔记](https://github.com/Da1yuqin/PaperBank/blob/main/SOURCES.md#写作笔记)；[NeurIPS · Paper Checklist](https://neurips.cc/public/guides/PaperChecklist)；[Rougier et al. (2014) · Ten Simple Rules for Better Figures](https://doi.org/10.1371/journal.pcbi.1003833)；[Yuqin Dai et al. (IJCV 2026；引文为 arXiv v4) · TCDiff++: An End-to-end Trajectory-Controllable Diffusion Model for Harmonious Music-Driven Group Choreography](https://link.springer.com/article/10.1007/s11263-025-02611-3)

</details>


**结果图与案例**

- [ ] **第 60 条：**按均值、分布、投影或时间变化选图型；说明变换和不确定性，图形不能证明机制。

<a id="tip-60"></a>
<details>
<summary>说明、例子与参考</summary>

KDE 写带宽和样本；PCA 写输入、标准化和解释方差；区间带说明类型；雷达图写归一化，各轴量纲不同不能直接比面积。

**边界：**KDE 不是累计分布；PCA 图分得开不等于证明机制或泛化；置信区间不表示某次观测落入范围的概率。不凭图形平滑程度评判方法。

**训练动态图：控制量和行为一起看**

**公开论文图例 · 点评为本指南整理**

阴影的统计含义未在原图注中明确，不称为标准差或置信区间。

![InteractCS-RL Figure 3：成本惩罚与发券率随训练变化，红蓝对应20%和30%目标](../assets/paper-interactcs-fig3.png)

The left panel shows penalty magnitude; the right shows voucher rate. Both use training steps and the same target colors.
左图看惩罚，右图看发券率；两图共用训练步数和预算颜色。

**逐句拆解**

1. 作者笔记用这类动态展示控制机制。左边是施加的惩罚，右边是实际发券行为，不只贴最终均值。
2. 红色目标20%，蓝色目标30%；同色跨面板对应同一设置，横轴对齐便于看变化顺序。
3. 它说明训练过程中发生了什么。要判断方法优势，还需同条件基线与多次运行；曲线本身不能包办。

**摘录出处：**[Ning Gao et al. · Reinforcing Real-world Service Agents (arXiv v1)](https://arxiv.org/abs/2602.22697v1)；Fig.3，PDF 第35页；公开 arXiv 版本；图与原 PDF 核对；公开预印本；不以项目笔记中的会议标记认定录用

**原文／图片许可：**Ning Gao et al., Reinforcing Real-world Service Agents, arXiv:2602.22697v1. CC BY 4.0（https://creativecommons.org/licenses/by/4.0/）。从原 PDF 裁切；图形、标签和数据未改。

来源与延伸阅读：[作者提供的写作、绘图与进阶笔记](https://github.com/Da1yuqin/PaperBank/blob/main/SOURCES.md#写作笔记)；[Rougier et al. (2014) · Ten Simple Rules for Better Figures](https://doi.org/10.1371/journal.pcbi.1003833)；[NeurIPS · Paper Checklist](https://neurips.cc/public/guides/PaperChecklist)；[Ning Gao et al. · Reinforcing Real-world Service Agents (arXiv v1)](https://arxiv.org/abs/2602.22697v1)

</details>

- [ ] **第 31 条：**生成工具可辅助构图；曲线、柱长、表格和误差条用真实数据，组合后核对几何与数值。

<a id="tip-31"></a>
<details>
<summary>说明、例子与参考</summary>

布局与图标可先生成，结果面板留给实际数据和绘图代码。数字对了，还要检查柱长、点位和坐标是否对应。

**边界：**图上的数字写对了，柱子的长度也可能错。漂亮和准确要分开检查。

**结果图：样式可以借，成绩不能借**

**假设教学例子，非论文原文、非实测结果**

以下数值只说明如何保留真实差异；正式绘图从实际数据文件读取。

**改前 · 中文**

把A画得明显比B好。

**Before · English**

Make method A look clearly better than B.

**改后 · 中文**

按同一刻度画记录值：A为81%，B为79%，标出2个百分点差值。

**After · English**

Plot the recorded values, A = 81% and B = 79%, on the same scale. Label the two-percentage-point difference.

**逐句拆解**

1. 先定数据，再定图形；别让绘图模型自由发挥柱长和曲线。
2. 差2个百分点就画2个百分点。可以讲实际意义，不把它画成翻倍。
3. 生成工具用于框架布局、配色草图；结果坐标、数值、误差条由统计代码控制。

来源与延伸阅读：[作者提供的写作、绘图与进阶笔记](https://github.com/Da1yuqin/PaperBank/blob/main/SOURCES.md#写作笔记)；[Rougier et al. (2014) · Ten Simple Rules for Better Figures](https://doi.org/10.1371/journal.pcbi.1003833)；[NeurIPS · Paper Checklist](https://neurips.cc/public/guides/PaperChecklist)；[ACL Rolling Review · Responsible NLP Research](https://aclrollingreview.org/responsibleNLPresearch/)

</details>

- [ ] **第 88 条：**按原始数据画图，点位、长度、面积和坐标与数值一致；不假装测过、不生成成绩。

<a id="tip-88"></a>
<details>
<summary>说明、例子与参考</summary>

可调整配色与布局，不可调整实验结果。数字标签正确还不够，图形尺度也要对应。

**边界：**数据、信息边界和完成状态按实际记录说明。

**好看可以调，数据不能调**

**教学示例：假设情境，非论文原文／实测记录**

改后假定已有对应记录；实际改稿须先核对这些事实，不能从改前文字推断或补造。

**逐句拆解**

2 个百分点的差异不能被画成两倍；没有测量的点不能为了曲线顺滑补上。

**教学改写 · English（非论文原文）**

Methods A and B score 62% and 64%. Plot the recorded values with the actual axis scale; if the axis is truncated, make the break explicit. Leave an unmeasured third condition missing.

**教学改写 · 中文（非论文原文）**

方法 A、B 的得分是 62% 和 64%。按记录值和真实刻度画图；截断坐标轴就明确标出断轴。第三个条件没有测量，就保留缺失。

来源与延伸阅读：[写作技能与检查方法](https://github.com/Da1yuqin/PaperBank/blob/main/SOURCES.md#写作技能)

</details>

- [ ] **第 58 条：**长文本按输入、输出和评价分区，统一层级、少量高亮；颜色类型用图例解释。

<a id="tip-58"></a>
<details>
<summary>说明、例子与参考</summary>

同类文字用同一颜色，只标出决定判断的几处。保留引用出处，按授权匿名；失败案例说明筛选方式，不能代替总体成功率。

**边界：**展示失败案例时说明筛选规则；一条漂亮的案例不能说明总体成功率。颜色区分的是信息类型，不是显著性。

**SAGE：长案例先分清三种角色**

**论文原文 · English**

> To operationalize the multi-agent system, we carefully crafted three prompt templates corresponding to each agent's role.

**中文翻译 · 本指南翻译**

为落实这一多智能体系统，我们按每种智能体的职责设计了三份提示词模板。

**逐句拆解**

1. 原文随后分别列出客服智能体、用户模拟器和评判智能体的提示词；长案例先按角色分组，才不容易把回复与评价混读。
2. 迁移到案例图时，可用白底及统一标题层级，把输入、被测回复、参考路径与评价结果分区；少量颜色只负责标明信息类型。
3. 颜色与版式建议属于教学迁移，不是对原图配色或实际对话的复现。若删节长文本，保留决定分支与判定的关键条件，并标注删节。

**教学改写 · English（非论文原文）**

Teaching layout: keep the scenario facts on a white background. Use consistent labels for the user input, service-agent reply, reference path, and judge output. Use one restrained color per information type, and explain the colors in a legend. Do not use color as a substitute for a correctness label.

**教学改写 · 中文（非论文原文）**

教学版式：场景事实放在白底上；用户输入、客服回复、参考路径、评判输出使用一致的标题层级。每种信息类型用一种克制的颜色，并在图例解释。判定仍写明确标签，不能只靠颜色暗示正确或错误。

**摘录出处：**[Ling Shi, Yuqin Dai et al. · SAGE: An Extensible Benchmark for Service Agent Graph-guided Evaluation](https://arxiv.org/abs/2604.09285)；附录 Example: Telecom Package Scenario / Prompts for Agent，开头；后续三种角色 promptbox（作者源稿第 1715 行起）；作者终稿 2026-10-04 只读快照；公开链接为 arXiv v1；作者终稿短引；公开链接为不同版本预印本；下方教学改写或模拟回复不属于论文原文

**原文／图片许可：**作者终稿教学短引，保留原论文版权；不随 PaperBank 原创内容转授终稿转载权。公开 arXiv v1 的 CC BY 4.0 已核验，该许可不自动延伸到不同版本的作者终稿。

来源与延伸阅读：[作者提供的写作、绘图与进阶笔记](https://github.com/Da1yuqin/PaperBank/blob/main/SOURCES.md#写作笔记)；[Rougier et al. (2014) · Ten Simple Rules for Better Figures](https://doi.org/10.1371/journal.pcbi.1003833)；[Ling Shi, Yuqin Dai et al. · SAGE: An Extensible Benchmark for Service Agent Graph-guided Evaluation](https://arxiv.org/abs/2604.09285)

</details>


</details>


<a id="discussion"></a>
## 7. 讨论与局限

解释证据支持的意义，交代未覆盖条件与未证实原因。

### 讨论·示范自然段1：发现的意义

回到研究问题解释发现，机制判断服从对照证据。

教学例句，非论文原文或实测结果。

The illustrative comparison suggests that organizing quotes and constraints can improve citation support.

模拟比较提示，组织摘句与约束可能提高引用支持率。

**第 1 句：**意义仍限于测过的引用支持率，不将其扩大成约束满足或整体答案质量。

The current comparison does not isolate source organization from added constraint information.

当前比较尚未区分来源组织与额外约束信息的各自作用。

**第 2 句：**把未区分原因写清，不把整体提高归因于全部设计。

### 局限·示范自然段1：尚未覆盖条件

把外推范围写具体，区分未知与失败。

教学例句，非论文原文或实测结果。

The evaluation concerns static English manuals.

评价针对静态英语手册。

**第 1 句：**把当前证据范围明确保留。

Cross-language questions and frequently updated documents remain untested.

跨语言问题和频繁更新的文档尚未检验。

**第 2 句：**未测设置不能写成已适用，也不能写成已失败。

<details>
<summary>检查清单和真实论文例子（2 项）</summary>


**解释与适用范围**

- [ ] **第 103 条：**回到研究问题，解释主要发现的意义、可能原因和成立条件。

<a id="tip-103"></a>
<details>
<summary>说明、例子与参考</summary>

先说结果如何回答问题；机制已检验和原因待验证分开写。

**边界：**Discussion可单列或并入结果分析；消融、观察或个例不能自动证明因果。

**讨论解释发现，不再念一遍结果**

**假设教学情境，非论文原文、非实测结果**

改后假定已有对应记录；实际改稿须先核对这些事实，不能从改前文字推断或补造。

**改前 · 中文**

分数提高说明模型理解了证据。

**Before · English**

A higher score proves that the model understands evidence.

**改后 · 中文**

假设证据笔记提高了引用支持率。这支持笔记在当前设置下的作用；收益来自引用组织还是额外信息，仍需对照检验。

**After · English**

Suppose that evidence notes improve citation support. This supports their value in this setting. Whether the gain comes from citation organization or additional information requires a further control.

**逐句拆解**

1. 先说已观察结果，再给范围内的意义。
2. 可能原因仍待检验，不冒充机制发现。

来源与延伸阅读：[写作技能与检查方法](https://github.com/Da1yuqin/PaperBank/blob/main/SOURCES.md#写作技能)；[Mensh & Kording (2017) · Ten simple rules for structuring papers](https://doi.org/10.1371/journal.pcbi.1005619)

</details>


**具体局限**

- [ ] **第 104 条：**指出未覆盖的数据、设置或预算，说明它们怎样限制当前结论。

<a id="tip-104"></a>
<details>
<summary>说明、例子与参考</summary>

每项写清缺什么证据、哪个结论因此需要收窄；已知失败与尚未检验分开。

**边界：**局限按论文类型和投稿要求安排；尚未检验不是已经失败。

**局限写具体条件，别只说以后再改**

**假设教学情境，非论文原文、非实测结果**

改后假定已有对应记录；实际改稿须先核对这些事实，不能从改前文字推断或补造。

**改前 · 中文**

还有一些局限，未来会改进。

**Before · English**

There are limitations that we will improve in future work.

**改后 · 中文**

假设评估仅覆盖静态英语文档，因此跨语言问题和实时更新文档仍未检验。

**After · English**

Suppose that the evaluation covers only static English documents. Cross-language questions and continuously updated documents remain untested.

**逐句拆解**

1. 给出具体评估范围。
2. 两个缺少证据的条件对应明确外推边界。

来源与延伸阅读：[写作技能与检查方法](https://github.com/Da1yuqin/PaperBank/blob/main/SOURCES.md#写作技能)；[Mensh & Kording (2017) · Ten simple rules for structuring papers](https://doi.org/10.1371/journal.pcbi.1005619)

</details>


</details>


<a id="conclusion"></a>
## 8. 结论

回到开头的问题，用已报告证据概括主要贡献。

### 结论·示范自然段1

用已有发现收束开头的问题，不在结尾新增结果。

教学例句，非论文原文或实测结果。

This study uses evidence notes to connect document quotes with dialogue constraints.

本研究用证据笔记关联文档摘句与对话约束。

**第 1 句：**回到具体设计和问题。

The illustrative evaluation shows higher citation support with extra latency; broader document settings require further tests.

模拟评价显示引用支持率提高但延迟增加；更广泛的文档设置还需检验。

**第 2 句：**把主要发现、取舍和外推范围一起收束，不再宣传一遍。

<details>
<summary>检查清单和真实论文例子（1 项）</summary>


**收束问题与贡献**

- [ ] **第 105 条：**用已报告证据概括研究问题、关键贡献和成立范围，不新增结果。

<a id="tip-105"></a>
<details>
<summary>说明、例子与参考</summary>

先回到问题，再给最主要发现；需要的后续方向对应已写明的局限。

**边界：**理论、实证、综述的结论形式可调整，但新主张仍需要正文证据。

**结论回答开头问题，别最后添加新卖点**

**假设教学情境，非论文原文、非实测结果**

改后假定已有对应记录；实际改稿须先核对这些事实，不能从改前文字推断或补造。

**改前 · 中文**

该系统适用于所有检索任务。

**Before · English**

The system works for every retrieval task.

**改后 · 中文**

假设证据笔记在静态文档问答中提高了引用支持率，但增加了延迟；后续应检验文档持续更新时的效果。

**After · English**

Suppose that evidence notes improve citation support in static-document question answering, at the cost of higher latency. Future work should evaluate continuously updated documents.

**逐句拆解**

1. 只收束正文已有贡献和取舍。
2. 下一步由局限导出，不把未测情境写成适用。

来源与延伸阅读：[写作技能与检查方法](https://github.com/Da1yuqin/PaperBank/blob/main/SOURCES.md#写作技能)；[Mensh & Kording (2017) · Ten simple rules for structuring papers](https://doi.org/10.1371/journal.pcbi.1005619)

</details>


</details>


<a id="references"></a>
## 9. 参考文献

让每个引用对得到正确原文和实际版本。

### 参考文献核对示范

让正文判断、引用键和实际文献版本对应。

教学例句，非论文原文或实测结果。

Each citation key resolves to one bibliography entry for the version actually used.

每个引用键对应一个条目，条目记录实际使用的版本。

**第 1 句：**这是引用整理说明，不是假造文献条目。

A source evaluated only on single-turn retrieval cannot support a claim about multi-turn retrieval.

只评估单轮检索的来源，不能支撑多轮检索结论。

**第 2 句：**核对支持关系比排版整齐更重要。

<details>
<summary>检查清单和真实论文例子（2 项）</summary>


**条目与版本**

- [ ] **第 106 条：**核对引用键、作者、题名、年份与实际版本，并确认该原文支持引用处判断。

<a id="tip-106"></a>
<details>
<summary>说明、例子与参考</summary>

从正文回查原文，再核对文末条目；修复缺失、重复或错版本，按投稿格式排版。

**边界：**预印本与发表版本分别核对；占位引用键只说明对应关系，不是真实文献。

**正文每个引用，都能在文末准确找到**

**假设教学情境，非论文原文、非实测结果**

改后假定已有对应记录；实际改稿须先核对这些事实，不能从改前文字推断或补造。

**改前 · 中文**

正文引用study_a，文末却列study_b。

**Before · English**

The text cites study_a, but the bibliography lists study_b.

**改后 · 中文**

占位键study_a应对应唯一条目。若该原文只评估单轮检索，正文也只引用其单轮结果。

**After · English**

The placeholder key study_a must resolve to one matching entry. If that source evaluates single-turn retrieval, cite only its single-turn result.

**逐句拆解**

1. 先核对引用键是否匹配。
2. 再核对实际版本与引用主张，而非只检查排版。

来源与延伸阅读：[写作技能与检查方法](https://github.com/Da1yuqin/PaperBank/blob/main/SOURCES.md#写作技能)；[Mensh & Kording (2017) · Ten simple rules for structuring papers](https://doi.org/10.1371/journal.pcbi.1005619)

</details>


**来源与开放条件**

- [ ] **第 96 条：**核对引用版本、年份与结论；代码、图表数据、原始数据分别查许可与可用性。

<a id="tip-96"></a>
<details>
<summary>说明、例子与参考</summary>

公开链接不等于可任意再用，也不等于有人完成了复现。

**边界：**数据、信息边界和完成状态按实际记录说明。

**引用回到原文，开放情况分开说**

**教学示例：假设情境，非论文原文／实测记录**

改后假定已有对应记录；实际改稿须先核对这些事实，不能从改前文字推断或补造。

**逐句拆解**

部分资源公开就写清部分资源；下载、运行和结果一致要按实际完成状态分别报告。

**教学改写 · English（非论文原文）**

The repository provides plotting code and aggregate figure data. The individual-level dataset requires approved access. We verified the release contents; we have not reproduced the reported experiment.

**教学改写 · 中文（非论文原文）**

仓库提供画图代码和汇总图表数据，个体数据需要审批访问。这里核对了公开包包含的文件，没有据此声称已复现实验。

来源与延伸阅读：[写作技能与检查方法](https://github.com/Da1yuqin/PaperBank/blob/main/SOURCES.md#写作技能)

</details>


</details>


<a id="appendix"></a>
## 10. 附录

把补充细节放在容易找到、足以复核的位置。

### 附录·示范自然段1：复核细节

用明确入口提供正文未展开的设置和补充结果。

教学例句，非论文原文或实测结果。

Appendix A lists the frozen prompts, retrieval settings, and scoring instructions.

附录A列出冻结提示词、检索设置和评分说明。

**第 1 句：**让正文读者能定位复核细节；真实稿件只列实际提供的内容。

Appendix B reports per-run results, including failures, with configuration identifiers.

附录B按配置标识报告每次运行的结果，包括失败记录。

**第 2 句：**结果与配置对应，不能只放最好的一次或把故障当成方法发现。

### 附录·示范自然段2：参数选择

交代选参数据和规则，区分选择过程与最终测试。

教学例句，非论文原文或实测结果。

We choose the maximum note length using development questions.

我们用开发集问题选择笔记最大长度。

**第 1 句：**说明参数怎样得到，而非只报最终值。

We freeze this choice before evaluating the test questions.

我们在评价测试问题前冻结这个选择。

**第 2 句：**把开发与测试边界写清，不能根据最终涨分倒选参数。

<details>
<summary>检查清单和真实论文例子（3 项）</summary>


**补充细节与入口**

- [ ] **第 37 条：**按实现、设置、结果和证明组织附录，正文指到具体小节；关键限制仍在正文写。

<a id="tip-37"></a>
<details>
<summary>说明、例子与参考</summary>

每节说明补充哪件事。影响主要结论的反例或限制，不能只藏在附录里。

**边界：**影响主结论的限制和反例，正文也得交代，不能靠放到附录就当不存在。

**GreenPlanner：正文告诉读者去附录查哪一种计算**

**论文原文 · English**

> Fire-safety distance: measured via a walkable-grid search of the maximum accessible path (detailed in Appendix. A1);

**中文翻译 · 本指南翻译**

消防安全距离：通过可行走网格搜索计算最长可达路径（详见附录 A1）；

**逐句拆解**

1. 不是只写“详见附录”，而是把检查对象、计算方法和具体附录号放在一起：要查最长可达路径，就去 A1。
2. 同段把连通性判定指向 A2，模型设计指向 A3，按问题分流。当前 CVF 正文 PDF 未包含这些附录正文，因此此处示范的是精确定位，不代表附件实现已被核对。

**教学改写 · English（非论文原文）**

Teaching rewrite: Place the walkable-grid search procedure in a named appendix subsection and point the fire-distance result to that subsection. Keep any limitation affecting the main feasibility claim in the body as well.

**教学改写 · 中文（非论文原文）**

教学改写：把可行走网格搜索过程放入明确命名的附录小节，让正文消防距离结果直接指向该节。影响主要可行性主张的限制，正文也要交代。

**摘录出处：**[Pengyu Zeng et al. (CVPR Findings 2026) · GreenPlanner: Practical Floorplan Layout Generation via an Energy-Aware and Function-Feasible Generative Framework](https://openaccess.thecvf.com/content/CVPR2026F/html/Zeng_GreenPlanner_Practical_Floorplan_Layout_Generation_via_an_Energy-Aware_and_Function-Feasible_CVPRF_2026_paper.html)；§3.1 Crafting DesignFD，Fire-safety distance 项；PDF p.3，proceedings p.8598；CVF Open Access 作者接受版；正式发表元数据已由 CVF 条目核对；该工作已发表；引文版本单独标明；教学改写与模拟回复不属于论文原文

**原文／图片许可：**原权利人保留版权；CVF Open Access 未声明 CC BY。本指南仅作署名教学短引，不重新发布全文或原图，不向第三方转授原论文版权。

来源与延伸阅读：[写作技能与检查方法](https://github.com/Da1yuqin/PaperBank/blob/main/SOURCES.md#写作技能)；[Pengyu Zeng et al. (CVPR Findings 2026) · GreenPlanner: Practical Floorplan Layout Generation via an Energy-Aware and Function-Feasible Generative Framework](https://openaccess.thecvf.com/content/CVPR2026F/html/Zeng_GreenPlanner_Practical_Floorplan_Layout_Generation_via_an_Energy-Aware_and_Function-Feasible_CVPRF_2026_paper.html)

</details>


**设置、调参与复现**

- [ ] **第 38 条：**对应保存版本、输入、配置、输出和统计脚本，写明入口；提供代码与复现成功分开说。

<a id="tip-38"></a>
<details>
<summary>说明、例子与参考</summary>

说明运行什么、读什么输入、产生什么输出。资源或数据限制照实写，仓库链接本身不是复现证据。

**边界：**有代码和已经复现成功不是一回事。哪些能跑、哪些受资源或数据限制，分别说清楚。

**教学迁移：代码入口与复现成功分开写**

**论文原文 · English**

> For implementation details, please refer to our GitHub repository.

**中文翻译 · 本指南翻译**

实现细节请参阅我们的 GitHub 仓库。

**逐句拆解**

1. 原句用于帮助读者定位实现材料，本身没有说明任何读者已经重现成绩。
2. 教学迁移补充的是交付应有的信息，不替原仓库编造运行入口、版本哈希或成功日志。

**教学改写 · English（非论文原文）**

A repository link identifies a starting point, not evidence of a successful reproduction.
A reproduction note should specify the code version, input data, configuration, execution command, and expected output.
If a full reproduction has not been run, describe the available code without claiming that the published results have been reproduced.

**教学改写 · 中文（非论文原文）**

仓库链接给出起点，不构成复现成功的证据。
复现说明应写明代码版本、输入数据、配置、执行命令与预期输出。
尚未运行完整复现时，说明提供了哪些代码，不宣称已复现发表结果。

**摘录出处：**[Yuqin Dai et al. (AAAI 2026) · Careful Queries, Credible Results: Teaching RAG Models Advanced Web Search Tools with Reinforcement Learning](https://ojs.aaai.org/index.php/AAAI/article/view/40299)；§ Methodology，Learning to Use Advanced Search Tools，最后一句；AAAI 2026 作者终稿；已发表论文；下方教学改写或模拟回复不属于论文原文

**原文／图片许可：**Yuqin Dai et al., AAAI 2026, pp.30458–30466. ©2026 AAAI，保留原版权；作者教学短引，不随本指南转授再版许可。中文为本指南翻译，拆解与教学改写单独标注。

来源与延伸阅读：[NeurIPS · Paper Checklist](https://neurips.cc/public/guides/PaperChecklist)；[Yuqin Dai et al. (AAAI 2026) · Careful Queries, Credible Results: Teaching RAG Models Advanced Web Search Tools with Reinforcement Learning](https://ojs.aaai.org/index.php/AAAI/article/view/40299)

</details>

- [ ] **第 39 条：**写清参数来自先例还是开发集，报告搜索范围；关键参数查敏感性，不拿测试集反复调。

<a id="tip-39"></a>
<details>
<summary>说明、例子与参考</summary>

完整参数表可放附录。质量或成本对参数敏感时，分析合理范围内的变化，不能只报一个好看的取值。

**边界：**把参数写详细，不能替代必要的验证。更不要反复看测试成绩来挑参数。

**GreenPlanner：报出参数，还要区分选择过程有没有依据**

**论文原文 · English**

> Early stopping (patience=3) is used to avoid overfitting.

**中文翻译 · 本指南翻译**

采用早停（耐心值为 3）来避免过拟合。

**逐句拆解**

1. 原句交代参数和用途。patience=3 通常表示容许连续 3 次监控指标未改善；检查间隔以实际实现为准，不等于重复实验三次。
2. 原句未说明试过哪些 patience 值，也未说明依据哪个开发集指标选定。应查实际记录，不能从最终配置倒推出调参流程。

**教学改写 · English（非论文原文）**

Teaching rewrite: Report the stopping metric, evaluation split, and search range if those choices are recorded. A final patience value alone does not establish how the parameter was selected.

**教学改写 · 中文（非论文原文）**

教学改写：若选择记录可查，应报告早停指标、评价划分和搜索范围。一个最终 patience 值不能证明参数是怎样选出的。

**摘录出处：**[Pengyu Zeng et al. (CVPR Findings 2026) · GreenPlanner: Practical Floorplan Layout Generation via an Energy-Aware and Function-Feasible Generative Framework](https://openaccess.thecvf.com/content/CVPR2026F/html/Zeng_GreenPlanner_Practical_Floorplan_Layout_Generation_via_an_Energy-Aware_and_Function-Feasible_CVPRF_2026_paper.html)；§4.2 Implementation Details，PDE 训练设置；PDF p.5，proceedings p.8600；CVF Open Access 作者接受版；正式发表元数据已由 CVF 条目核对；该工作已发表；引文版本单独标明；教学改写与模拟回复不属于论文原文

**原文／图片许可：**原权利人保留版权；CVF Open Access 未声明 CC BY。本指南仅作署名教学短引，不重新发布全文或原图，不向第三方转授原论文版权。

来源与延伸阅读：[NeurIPS · Paper Checklist](https://neurips.cc/public/guides/PaperChecklist)；[Pengyu Zeng et al. (CVPR Findings 2026) · GreenPlanner: Practical Floorplan Layout Generation via an Energy-Aware and Function-Feasible Generative Framework](https://openaccess.thecvf.com/content/CVPR2026F/html/Zeng_GreenPlanner_Practical_Floorplan_Layout_Generation_via_an_Energy-Aware_and_Function-Feasible_CVPRF_2026_paper.html)

</details>


</details>


<a id="revision"></a>
## 11. 全文验收

核对整篇论证、图表及最终交付版本。

<details>
<summary>检查清单和真实论文例子（5 项）</summary>


**全文论证与一致性**

- [ ] **第 40 条：**通读摘要至结论、图注和附录，核对问题、方法、结果是否对应；先修跳步，再改语法。

<a id="tip-40"></a>
<details>
<summary>说明、例子与参考</summary>

重复的合并，缺少联系的补上。只检查摘要和引言不能称为全文检查，图注和附录也要核对。

**边界：**只检查摘要和引言，不能叫全文检查。后面的图注和附录也会藏矛盾。

**SAGE：结尾回到前面承诺解决的问题**

**论文原文 · English**

> We presented SAGE, a scenario-extensible benchmark that addresses Scenario Silos and Dialogue Dynamics Gap by formalizing SOPs as directed graphs and coupling them with adversarial multi-turn simulation.

**中文翻译 · 本指南翻译**

我们提出 SAGE 这一可扩展场景的基准，通过将标准操作流程（SOP）形式化为有向图，并结合对抗性多轮模拟，回应场景孤岛和对话动态缺口。

**逐句拆解**

1. 结论没有另起一套故事：Scenario Silos 和 Dialogue Dynamics Gap 对应摘要与引言的问题，图表示和动态模拟对应方法设计。
2. 全文检查要沿这条对应关系回查方法与实验；术语一致只是起点，还要确认每项设计实际实现、每项效果有比较证据。
3. 这里陈述设计回应了什么问题，不能仅因结论写得连贯，就把所有领域的有效性说成已验证。

**摘录出处：**[Ling Shi, Yuqin Dai et al. · SAGE: An Extensible Benchmark for Service Agent Graph-guided Evaluation](https://arxiv.org/abs/2604.09285)；§ Conclusion，首句（作者源稿第 1042–1045 行）；作者终稿 2026-10-04 只读快照；公开链接为 arXiv v1；作者终稿短引；公开链接为不同版本预印本

**原文／图片许可：**作者终稿教学短引，保留原论文版权；不随 PaperBank 原创内容转授终稿转载权。公开 arXiv v1 的 CC BY 4.0 已核验，该许可不自动延伸到不同版本的作者终稿。

来源与延伸阅读：[写作技能与检查方法](https://github.com/Da1yuqin/PaperBank/blob/main/SOURCES.md#写作技能)；[Ling Shi, Yuqin Dai et al. · SAGE: An Extensible Benchmark for Service Agent Graph-guided Evaluation](https://arxiv.org/abs/2604.09285)

</details>


**衔接、指代与篇幅**

- [ ] **第 41 条：**检查相邻句是解释、转折还是因果；先讲清内容联系，再加连接词。

<a id="tip-41"></a>
<details>
<summary>说明、例子与参考</summary>

短句要接得上。前一句推不出后一句，就不能写“因此”；加 However 也不能创造原本不存在的转折。

**边界：**连接词不能替你造因果。前一句推不出后一句，就别硬写“因此”。

**UrbanZero：把两个模块写成真实承接关系**

**教学改写：依据 UrbanZero 公开项目介绍，非论文原文**

依据公开项目介绍中的语义简报、地块任务、逐块规划和程序反馈编写。中英示例为本指南教学改写；实验问题和模拟回复方案不代表项目已完成的工作。

**改前 · 中文**

我们生成任务。因此，我们使用逐块规划。

**Before · English**

We generate tasks. Therefore, we use patch-wise planning.

**改后 · 中文**

语义简报先由程序编译为地块任务。求解模型随后逐块分配用途，使每次决策只处理一部分空间信息。

**After · English**

Semantic briefs are first compiled into parcel-level tasks. The solver then assigns land uses patch by patch, so each decision handles only part of the spatial context.

**逐句拆解**

1. 第二句接住第一句的产物“地块任务”，先后关系自然成立。
2. 编译本身不能推出必须逐块；逐块设计回应的是每次处理的空间规模，不要用 therefore 硬造因果。

来源与延伸阅读：[写作技能与检查方法](https://github.com/Da1yuqin/PaperBank/blob/main/SOURCES.md#写作技能)；[Mensh & Kording (2017) · Ten simple rules for structuring papers](https://doi.org/10.1371/journal.pcbi.1005619)；[NeurIPS · Paper Checklist](https://neurips.cc/public/guides/PaperChecklist)；[Chaoyang Shi, Yuqin Dai et al. · UrbanZero（公开项目介绍）](https://github.com/Da1yuqin/Da1yuqin.github.io/blob/main/_pages/includes/pub.md#L193-L202)

</details>

- [ ] **第 42 条：**歧义代词换成简短对象名，同一对象统一称呼；必要时拆句，指向清楚的代词可留。

<a id="tip-42"></a>
<details>
<summary>说明、例子与参考</summary>

一句里出现多个模型或模块，说明每个动作由谁完成。不要靠换近义词制造变化，读者需要知道对象没变。

**边界：**指向清楚的代词可以留。目标是自然准确，不是把每句话写成重复全称。

**TCDiff++：让模块名承担动作，别用“它”包办流程**

**论文原文 · English**

> Our end-to-end TCDiff++ framework comprises two key components: the Group Dance Decoder (GDD) and the Footwork Adaptor (FA).

**中文翻译 · 本指南翻译**

端到端 TCDiff++ 框架包含两个关键组成部分：群舞解码器（GDD）与脚步适配器（FA）。

**逐句拆解**

1. 图注先引入 GDD 与 FA，再分别说明 GDD 产生原始动作，FA 利用位置细化脚步，最后将脚步融入动作；对象不同，动作也不同。
2. 教学改写用短模块名区分输入输出。单次训练不等于只有一个模块，也不等于删掉适配器；统称“它”会掩盖这些区别。

**教学改写 · English（非论文原文）**

Teaching rewrite: GDD generates the raw group motion from music. FA uses positional information from that motion to refine foot movements, which are then incorporated into the final dance sequence.

**教学改写 · 中文（非论文原文）**

教学改写：GDD 根据音乐生成群舞原始动作。FA 利用这些动作中的位置信息细化脚步，再将细化脚步融入最终舞蹈序列。

**摘录出处：**[Yuqin Dai et al. (IJCV 2026；引文为 arXiv v4) · TCDiff++: An End-to-end Trajectory-Controllable Diffusion Model for Harmonious Music-Driven Group Choreography](https://link.springer.com/article/10.1007/s11263-025-02611-3)；Figure 2 caption，第1句及随后模块流程；arXiv v4 PDF p.6；短引来自 arXiv:2506.18671v4，2025-10-05；正式期刊元数据已核对，不将作者稿等同于期刊排版终版；该工作已发表；引文版本单独标明；教学改写与模拟回复不属于论文原文

**原文／图片许可：**arXiv 作者稿采用 non-exclusive distribution 许可，非 CC BY。正式期刊版权按 Springer 出版协议保留；本指南不向第三方转授原论文版权。

来源与延伸阅读：[写作技能与检查方法](https://github.com/Da1yuqin/PaperBank/blob/main/SOURCES.md#写作技能)；[Yuqin Dai et al. (IJCV 2026；引文为 arXiv v4) · TCDiff++: An End-to-end Trajectory-Controllable Diffusion Model for Harmonious Music-Driven Group Choreography](https://link.springer.com/article/10.1007/s11263-025-02611-3)

</details>

- [ ] **第 43 条：**先删无新增信息的句子，合并重复定义，迁移次要细节；保留关键比较、条件与结论。

<a id="tip-43"></a>
<details>
<summary>说明、例子与参考</summary>

长列表和实现细节可放附录。删完回查论证是否完整，不按“永远先删某章”的固定顺序处理。

**边界：**没有“永远先删 Related Work”的规定。哪一段重复就处理哪一段。

**GreenPlanner：压缩效率结论，保留同任务的时间比较**

**论文原文 · English**

> Manual design took 24.7 minutes on average, while GreenFlow completed the same task in only 3.2 minutes

**中文翻译 · 本指南翻译**

人工设计平均用时 24.7 分钟，而 GreenFlow 完成同一任务只需 3.2 分钟。

**逐句拆解**

1. 短引保留原句的时间比较从句。“same task”给出比较对象，24.7 与 3.2 分钟给出绝对耗时，不能只剩“效率提高 87%”。
2. 该段来自 13 名参与者的研究，其中 4 名建筑师、9 名研究生。缩短时仍要保留参与者构成与任务范围，不能推广到所有建筑师和设计任务。

**教学改写 · English（非论文原文）**

Teaching rewrite: In the reported study of four architects and nine graduate students, the same design task took 24.7 minutes manually and 3.2 minutes with GreenFlow. Keep the task and participant scope when shortening the efficiency discussion.

**教学改写 · 中文（非论文原文）**

教学改写：在包含 4 名建筑师和 9 名研究生的研究中，同一设计任务人工用时 24.7 分钟，GreenFlow 用时 3.2 分钟。缩短效率讨论时，保留任务与参与者范围。

**摘录出处：**[Pengyu Zeng et al. (CVPR Findings 2026) · GreenPlanner: Practical Floorplan Layout Generation via an Energy-Aware and Function-Feasible Generative Framework](https://openaccess.thecvf.com/content/CVPR2026F/html/Zeng_GreenPlanner_Practical_Floorplan_Layout_Generation_via_an_Energy-Aware_and_Function-Feasible_CVPRF_2026_paper.html)；§4.6 Human Expert User Study，耗时原句前半句；PDF p.7，proceedings p.8602；CVF Open Access 作者接受版；正式发表元数据已由 CVF 条目核对；该工作已发表；引文版本单独标明；教学改写与模拟回复不属于论文原文

**原文／图片许可：**原权利人保留版权；CVF Open Access 未声明 CC BY。本指南仅作署名教学短引，不重新发布全文或原图，不向第三方转授原论文版权。

来源与延伸阅读：[作者提供的写作、绘图与进阶笔记](https://github.com/Da1yuqin/PaperBank/blob/main/SOURCES.md#写作笔记)；[Pengyu Zeng et al. (CVPR Findings 2026) · GreenPlanner: Practical Floorplan Layout Generation via an Energy-Aware and Function-Feasible Generative Framework](https://openaccess.thecvf.com/content/CVPR2026F/html/Zeng_GreenPlanner_Practical_Floorplan_Layout_Generation_via_an_Energy-Aware_and_Function-Feasible_CVPRF_2026_paper.html)

</details>


**最终图表与版本**

- [ ] **第 33 条：**在最终 PDF 检查引用顺序、图注归属、精度、高亮和整页布局；图表只传达实际信息。

<a id="tip-33"></a>
<details>
<summary>说明、例子与参考</summary>

表格的最优标记要有规则，图注要紧邻正确图。拥挤先调结构，空白先查排版，再检查全文是否一致。

**边界：**没有可靠依据能把美观换算成固定录用率。图的任务是帮助理解，不是制造保证。

**TCDiff++：高亮规则写在表旁，再回整页核对**

**论文原文 · English**

> The best results are highlighted in bold, the second best results are underlined

**中文翻译 · 本指南翻译**

最优结果用粗体标出，次优结果用下划线标出。

**逐句拆解**

1. 表 4 包含群舞与单舞指标，箭头说明各列的好坏方向。最优、次优应逐列检查，不能凭整行印象套标记。
2. 将表题、指标方向、数值与正文一起放回 PDF p.16 检查。高亮帮助比较，不代表完整模型赢得每列，更不是录用收益证据。

**教学改写 · English（非论文原文）**

Teaching rewrite: Verify each best and second-best mark against the metric direction in Table 4. Inspect the caption, numeric precision, and surrounding explanation together at the final page size.

**教学改写 · 中文（非论文原文）**

教学改写：依据表 4 各指标方向逐一检查最优与次优标记。按最终整页尺寸，同时检查表题、数值精度和邻近说明。

**摘录出处：**[Yuqin Dai et al. (IJCV 2026；引文为 arXiv v4) · TCDiff++: An End-to-end Trajectory-Controllable Diffusion Model for Harmonious Music-Driven Group Choreography](https://link.springer.com/article/10.1007/s11263-025-02611-3)；Table 4 caption，最后一分句；arXiv v4 PDF p.16；短引来自 arXiv:2506.18671v4，2025-10-05；正式期刊元数据已核对，不将作者稿等同于期刊排版终版；该工作已发表；引文版本单独标明；教学改写与模拟回复不属于论文原文

**原文／图片许可：**arXiv 作者稿采用 non-exclusive distribution 许可，非 CC BY。正式期刊版权按 Springer 出版协议保留；本指南不向第三方转授原论文版权。

来源与延伸阅读：[写作技能与检查方法](https://github.com/Da1yuqin/PaperBank/blob/main/SOURCES.md#写作技能)；[Rougier et al. (2014) · Ten Simple Rules for Better Figures](https://doi.org/10.1371/journal.pcbi.1003833)；[Yuqin Dai et al. (IJCV 2026；引文为 arXiv v4) · TCDiff++: An End-to-end Trajectory-Controllable Diffusion Model for Harmonious Music-Driven Group Choreography](https://link.springer.com/article/10.1007/s11263-025-02611-3)

</details>


</details>


<a id="workflow"></a>
## 12. 起草与协作

用提纲和证据推进写作，保护原始记录与他人修改。

<details>
<summary>检查清单和真实论文例子（3 项）</summary>


**提纲与篇幅**

- [ ] **第 6 条：**先写贡献句、提纲、草图和结果表；随证据调整主线，不成立的主张及时改。

<a id="tip-06"></a>
<details>
<summary>说明、例子与参考</summary>

方法和实验先说清，引言据此调整，摘要最后压缩。顺序可以变；概念图可先画，结果图必须等实际结果。

**边界：**顺序不是规定。概念图可以先画，结果图得等真实结果出来。

**PlanCraft：先写清能落地的数据与任务**

**论文原文 · English**

> Three automated pipelines produce paired inputs (graph-plus-block inputs or incomplete vectors) and complete floor plans for training PlanCraft-Diff.

**中文翻译 · 本指南翻译**

三条自动化流水线生成配对数据：输入为图与块组合或不完整矢量，目标为完整平面图，用于训练 PlanCraft-Diff。

**逐句拆解**

1. 这句话已给出训练数据的输入和目标，可以先作为方法骨架，再核对后文实验是否真的检验两类输入。
2. 这是根据成稿演示一种起草顺序，不是作者写作过程的记录；还没取得的比较不能提前写成结果。

**教学改写 · English（非论文原文）**

Start with the paired input and target, outline how each pair is built, and place the corresponding evaluation beside it. Refine the contribution sentence only after checking the available evidence.

**教学改写 · 中文（非论文原文）**

先写清配对输入与目标，再列它们怎样构建，并放上相应评价。核对已有证据后，再调整贡献句。

**摘录出处：**[Zeng, Dai et al. (2026 预印本) · PlanCraft: Sketch, Refine, and Furnish for Architect-Inspired Progressive 3D Residential Scene Generation](https://arxiv.org/abs/2607.23491v3)；Method / SketchPlan Dataset，开头第 2 句；PDF 第 3 页；arXiv:2607.23491v3，2026-09-05；短引对照作者源稿及公开 v3 正文；公开预印本；教学改写不是论文原文或新增实测结果

**原文／图片许可：**Pengyu Zeng et al., arXiv:2607.23491v3 (2026). arXiv 为非独占分发许可，原文版权由权利人保留；作者授权的教学短引，不随本指南转授全文或原图再版许可。中文翻译、拆解及教学改写为本指南新增。

来源与延伸阅读：[作者提供的写作、绘图与进阶笔记](https://github.com/Da1yuqin/PaperBank/blob/main/SOURCES.md#写作笔记)；[Mensh & Kording (2017) · Ten simple rules for structuring papers](https://doi.org/10.1371/journal.pcbi.1005619)；[Zeng, Dai et al. (2026 预印本) · PlanCraft: Sketch, Refine, and Furnish for Architect-Inspired Progressive 3D Residential Scene Generation](https://arxiv.org/abs/2607.23491v3)

</details>

- [ ] **第 7 条：**方法按步骤、实验按问题分节；同层标题统一逻辑，与模块名和图中名称一致。

<a id="tip-07"></a>
<details>
<summary>说明、例子与参考</summary>

标题写实际动作或对象。不同任务分开，过碎的小节合并，不用固定子节数代替判断。

**边界：**不用死守每节最多几个子节。太碎就合并，确实有不同任务就分开。

**PlanCraft：标题直接写出对象怎样变化**

**论文原文 · English**

> From Image to Vector: Rule-Based Post-Processing

**中文翻译 · 本指南翻译**

从图像到矢量：基于规则的后处理

**逐句拆解**

1. 标题给出输入、输出和处理方式，读者还没进小节就知道这里把生成图像变成可用的矢量几何。
2. 同层还有 Progressive Floor Plan Refinement 和 Grounded 3D Scene Assembly，依次对应平面图细化、格式转换与场景装配；这些名字与 Overview 的步骤一致。

**教学改写 · English（非论文原文）**

Organize the method around floor-plan refinement, image-to-vector conversion, and grounded scene assembly. Use these same names in the overview and framework figure.

**教学改写 · 中文（非论文原文）**

按平面图细化、图像转矢量与几何约束下的场景装配组织方法。总览与框架图使用同一组名称。

**摘录出处：**[Zeng, Dai et al. (2026 预印本) · PlanCraft: Sketch, Refine, and Furnish for Architect-Inspired Progressive 3D Residential Scene Generation](https://arxiv.org/abs/2607.23491v3)；Method，同层小节标题；PDF 第 4 页；arXiv:2607.23491v3，2026-09-05；短引对照作者源稿及公开 v3 正文；公开预印本；教学改写不是论文原文或新增实测结果

**原文／图片许可：**Pengyu Zeng et al., arXiv:2607.23491v3 (2026). arXiv 为非独占分发许可，原文版权由权利人保留；作者授权的教学短引，不随本指南转授全文或原图再版许可。中文翻译、拆解及教学改写为本指南新增。

来源与延伸阅读：[作者提供的写作、绘图与进阶笔记](https://github.com/Da1yuqin/PaperBank/blob/main/SOURCES.md#写作笔记)；[Zeng, Dai et al. (2026 预印本) · PlanCraft: Sketch, Refine, and Furnish for Architect-Inspired Progressive 3D Residential Scene Generation](https://arxiv.org/abs/2607.23491v3)

</details>

- [ ] **第 8 条：**按作者指南给问题、关键设计和结果留篇幅；超页先删重复，保留结论条件。

<a id="tip-08"></a>
<details>
<summary>说明、例子与参考</summary>

先列每章必须讲清的内容，再安排页数。最后看 PDF，确认背景没有挤掉关键比较和结果解释。

**边界：**写满不是目标，每页硬放一个实验也没必要。信息够了就停，格式按投稿要求来。

**GreenPlanner：篇幅先留给贯穿贡献的四个环节**

**论文原文 · English**

> GreenPlanner integrates four key components to unify evaluation and generation.

**中文翻译 · 本指南翻译**

GreenPlanner 整合四个关键组成部分，将评价与生成连接起来。

**逐句拆解**

1. 引言按 DesignFD、PDE、GreenPD、GreenFlow 的顺序解释标签数据、评价器、筛选后的数据与生成器；每一项都对后续环节有用途。
2. 省篇幅时保留这条贡献链，以及数据合规与生成质量的区别。可以减少背景和全称的重复，不能把四个环节压成一个无法解释的“智能系统”。

**教学改写 · English（非论文原文）**

Teaching rewrite: Reserve space for the four-part argument: feasibility labels train the evaluator, evaluator guidance builds compliant demand–plan pairs, and those pairs support constrained generation. Shorten repeated background before removing a necessary link.

**教学改写 · 中文（非论文原文）**

教学改写：给四部分的论证留位置：可行性标签训练评价器，评价器指导构建合规的需求与平面图配对，再用这些配对支持约束下的生成。先压缩重复背景，再处理理解这条论证所必需的环节。

**摘录出处：**[Pengyu Zeng et al. (CVPR Findings 2026) · GreenPlanner: Practical Floorplan Layout Generation via an Energy-Aware and Function-Feasible Generative Framework](https://openaccess.thecvf.com/content/CVPR2026F/html/Zeng_GreenPlanner_Practical_Floorplan_Layout_Generation_via_an_Energy-Aware_and_Function-Feasible_CVPRF_2026_paper.html)；§1 Introduction，四组件总览开头；PDF p.2，proceedings p.8597；CVF Open Access 作者接受版；正式发表元数据已由 CVF 条目核对；该工作已发表；引文版本单独标明；教学改写与模拟回复不属于论文原文

**原文／图片许可：**原权利人保留版权；CVF Open Access 未声明 CC BY。本指南仅作署名教学短引，不重新发布全文或原图，不向第三方转授原论文版权。

来源与延伸阅读：[作者提供的写作、绘图与进阶笔记](https://github.com/Da1yuqin/PaperBank/blob/main/SOURCES.md#写作笔记)；[Mensh & Kording (2017) · Ten simple rules for structuring papers](https://doi.org/10.1371/journal.pcbi.1005619)；[NeurIPS · Paper Checklist](https://neurips.cc/public/guides/PaperChecklist)；[Pengyu Zeng et al. (CVPR Findings 2026) · GreenPlanner: Practical Floorplan Layout Generation via an Energy-Aware and Function-Feasible Generative Framework](https://openaccess.thecvf.com/content/CVPR2026F/html/Zeng_GreenPlanner_Practical_Floorplan_Layout_Generation_via_an_Energy-Aware_and_Function-Feasible_CVPRF_2026_paper.html)

</details>


</details>


<a id="ai"></a>
## 13. AI辅助

给AI准确材料和明确任务，由作者核对事实和责任。

<details>
<summary>检查清单和真实论文例子（5 项）</summary>


**材料与任务**

- [ ] **第 44 条：**给AI问题、方法流程、真实结果表和参考段落，指定这次要写哪一段。

<a id="tip-44"></a>
<details>
<summary>说明、例子与参考</summary>

把输入组织成“具体缺口→对应设计→支持结果”；让AI解释这些材料的关系，别让它从标题猜实验。

**边界：**材料还不够就先补材料。顺口的段落不能当作实验记录。

**EviNoteRAG：先给 AI 精确的监督范围**

**论文原文 · English**

> To reduce computational overhead, EQR is applied only to the final SEN in each output sequence.

**中文翻译 · 本指南翻译**

为减少计算开销，每条输出序列只对最后一条支持性证据笔记（SEN）施加证据质量奖励（EQR）。

**逐句拆解**

1. 这是给 AI 的材料里必须冻结的事实：奖励应用于每条输出中的最后一条笔记，不是每一步或每个 token。
2. 输入材料还应交代奖励比较最后的 SEN 与由问题及正确答案构成的命题，区分训练可见真值与推理时可见证据。
3. 下面的教学提示只提供已核验方法约束，不替论文添加新的逐步奖励或训练实验。

**教学改写 · English（非论文原文）**

Teaching prompt: Write the EQR paragraph using these verified facts: a lightweight NLI judge compares the final SEN with a claim constructed from the query and ground-truth answer; EQR is applied only to the final SEN in each output sequence. Preserve the reported reward definition and do not introduce per-note or token-level supervision.

**教学改写 · 中文（非论文原文）**

教学提示：按以下已核验事实写 EQR 段落：轻量 NLI 评判模型比较最后一条 SEN 与由问题及正确答案构成的命题；每条输出序列只对最后一条 SEN 计算 EQR。保留原奖励定义，不增添逐条笔记或 token 级监督。

**摘录出处：**[Yuqin Dai et al. · EviNoteRAG: Enhancing RAG Models via Quality-Augmented Evidence Notes](https://arxiv.org/abs/2509.00877)；§ 3.3 Evidence Quality Reward，公式后计算开销句，PDF 第 3 页；content/03_method.tex 第 34 行；EMNLP 2026 revised 作者终稿；公开链接为 arXiv v3；作者终稿短引；公开链接为不同版本预印本；下方教学改写或模拟回复不属于论文原文

**原文／图片许可：**作者终稿教学短引，保留原论文版权；不随 PaperBank 原创内容转授原论文再版许可。公开 arXiv v3 为 non-exclusive distribution，并非 CC 授权；代码 Apache 2.0 不作为论文许可。

来源与延伸阅读：[作者提供的写作、绘图与进阶笔记](https://github.com/Da1yuqin/PaperBank/blob/main/SOURCES.md#写作笔记)；[Yuqin Dai et al. · EviNoteRAG: Enhancing RAG Models via Quality-Augmented Evidence Notes](https://arxiv.org/abs/2509.00877)

</details>

- [ ] **第 45 条：**先列每段的核心句，再展开解释；只读这些核心句，也应看懂问题、设计和证据。

<a id="tip-45"></a>
<details>
<summary>说明、例子与参考</summary>

先把引言中的困难、方法中的改动、实验中的验证对应起来；这条线通了，再展开句子。

**边界：**模板里写得再严格，作者还是要核对事实和引用。

**TCDiff++：先给一节的实际设置，再让 AI 起草**

**论文原文 · English**

> Following the protocol in (Le et al, 2023b), videos are partitioned into training (80%), validation (10%), and test (10%) sets.

**中文翻译 · 本指南翻译**

依照 Le 等人（2023b）的协议，将视频划分为训练集（80%）、验证集（10%）和测试集（10%）。

**逐句拆解**

1. 实验设置段落交代划分单位、比例与先例。单位是视频，不能让工具擅自改成人数、帧数或舞者互不重叠划分。
2. 将同节模型结构、数据来源与基线适配记录交给工具，再约束篇幅。原句未给具体视频数或随机种子，不能凭比例补造。

**教学改写 · English（非论文原文）**

Teaching prompt: Draft only the dataset paragraph using the provided video-level split, source, and proportions. Do not infer sample counts, dancer-disjoint partitions, or a random seed that the material does not report.

**教学改写 · 中文（非论文原文）**

教学提示词：仅依据给出的按视频划分、来源和比例，起草数据段落。不要推断材料未报告的样本数、舞者互不重叠划分或随机种子。

**摘录出处：**[Yuqin Dai et al. (IJCV 2026；引文为 arXiv v4) · TCDiff++: An End-to-end Trajectory-Controllable Diffusion Model for Harmonious Music-Driven Group Choreography](https://link.springer.com/article/10.1007/s11263-025-02611-3)；§5.1 Experimental Settings，Dataset，最后一句；arXiv v4 PDF p.10；短引来自 arXiv:2506.18671v4，2025-10-05；正式期刊元数据已核对，不将作者稿等同于期刊排版终版；该工作已发表；引文版本单独标明；教学改写与模拟回复不属于论文原文

**原文／图片许可：**arXiv 作者稿采用 non-exclusive distribution 许可，非 CC BY。正式期刊版权按 Springer 出版协议保留；本指南不向第三方转授原论文版权。

```text
请根据以下材料撰写【章节名称】，面向【领域与读者】。
材料：【研究问题、真实方法、已核验结果、引用来源】。
先列出本节主张与证据的对应关系，缺少依据的内容单独列出，不写入正文。随后给出正文：先交代目的，再解释具体对象、机制及证据。术语与【术语表】一致，符号首次出现时定义。每段围绕一个主要判断，相邻句有真实衔接。
保留实验范围、数值和不确定性；不要编造引文、补做实验、夸大新颖性或把计划写成结果。输出正文与简短核对清单。
```

来源与延伸阅读：[作者提供的写作、绘图与进阶笔记](https://github.com/Da1yuqin/PaperBank/blob/main/SOURCES.md#写作笔记)；[Yuqin Dai et al. (IJCV 2026；引文为 arXiv v4) · TCDiff++: An End-to-end Trajectory-Controllable Diffusion Model for Harmonious Music-Driven Group Choreography](https://link.springer.com/article/10.1007/s11263-025-02611-3)

</details>


**润色与绘图**

- [ ] **第 47 条：**明确 AI 可改范围，保护数据、公式、引用和原始提示词；检查差异与结论条件。

<a id="tip-47"></a>
<details>
<summary>说明、例子与参考</summary>

先修结构和指代，再修句子。影响含义的改动单独指出；原始输出、提示词和代码字段不能当普通正文润色。

**边界：**原始输出、实验提示词和代码字段，不按普通正文处理。

**EviNoteRAG：润色不能把可选步骤改成强制步骤**

**论文原文 · English**

> SEN generation is optional after each retrieval step, allowing the model to dynamically determine whether summarization is necessary based on retrieval outcomes.

**中文翻译 · 本指南翻译**

每次检索后是否生成支持性证据笔记（SEN）是可选的，模型根据检索结果动态决定是否需要摘要。

**逐句拆解**

1. optional 是方法约束；润色成“每次检索后必须生成笔记”，就把动态工作流改成了不同实验条件。
2. 每次检索不强制生成，不等于奖励格式允许整条输出完全没有笔记。Training Strategy 的格式条件仍要求至少一个 <summary>。
3. 原提示词、标签、奖励条件和消融配置都是研究协议，润色时应保护这些内容并检查差异。

**摘录出处：**[Yuqin Dai et al. · EviNoteRAG: Enhancing RAG Models via Quality-Augmented Evidence Notes](https://arxiv.org/abs/2509.00877)；§ 3.2 Supportive-Evidence Note / Dynamic SEN Workflow，首句，PDF 第 3 页；§ 3.4 Training Strategy 的格式条件，PDF 第 4 页；EMNLP 2026 revised 作者终稿；公开链接为 arXiv v3；作者终稿短引；公开链接为不同版本预印本

**原文／图片许可：**作者终稿教学短引，保留原论文版权；不随 PaperBank 原创内容转授原论文再版许可。公开 arXiv v3 为 non-exclusive distribution，并非 CC 授权；代码 Apache 2.0 不作为论文许可。

```text
请精修【指定范围】，保持数据、公式含义、引文、模型设定和结论边界不变。
先检查论证顺序，再修改句子。每段一个主要判断；解释必要术语；消除歧义指代；只有真实转折或因果关系才使用相应连接词。正文、图注和附录沿用同一术语。
不要增加未经证实的机制、新颖性或显著性。保护原始提示词、模型原话和代码字段。输出修订稿及会改变理解的主要修改；材料不足的问题单列说明。
```

来源与延伸阅读：[写作技能与检查方法](https://github.com/Da1yuqin/PaperBank/blob/main/SOURCES.md#写作技能)；[NeurIPS · Paper Checklist](https://neurips.cc/public/guides/PaperChecklist)；[ACL Rolling Review · Responsible NLP Research](https://aclrollingreview.org/responsibleNLPresearch/)；[Yuqin Dai et al. · EviNoteRAG: Enhancing RAG Models via Quality-Augmented Evidence Notes](https://arxiv.org/abs/2509.00877)

</details>

- [ ] **第 46 条：**讲清主要信息、输入输出与依赖，用自制或获准素材；先核对布局，再调配色。

<a id="tip-46"></a>
<details>
<summary>说明、例子与参考</summary>

给实际模块、连线和参考风格，避免照搬受保护的表达。结果面板留给真实数据，生成工具只辅助示意与构图。

**边界：**结果面板留给真实数据。工具不能替你生成实验成绩。

**GreenPlanner：画图先讲清数据和反馈从哪里来**

**论文原文 · English**

> Together, these components form an end-to-end pipeline from data construction to constraint-driven generative design.

**中文翻译 · 本指南翻译**

这些组成部分共同形成一条从数据构建到约束驱动生成设计的端到端流程。

**逐句拆解**

1. 图 2 的四部分不是随意并排的卡片：DesignFD 提供评价标签，PDE 学习快速预测，PDE 指导 GreenPD 重采样，GreenFlow 用 GreenPD 训练并接收 PDE 反馈。
2. 绘图说明要区分数据流与训练反馈，不能把 PDE 分数画成用户输入。原图保留来源；教学重绘另标为理解示意，不改原论文。

**教学改写 · English（非论文原文）**

Teaching diagram prompt: Show DesignFD labels training PDE, PDE-guided resampling creating GreenPD, GreenPD training GreenFlow, and PDE feedback refining the generator. Label dataset outputs and feedback arrows separately.

**教学改写 · 中文（非论文原文）**

教学绘图提示词：画出 DesignFD 标签训练 PDE，PDE 指导重采样得到 GreenPD，GreenPD 训练 GreenFlow，PDE 反馈进一步优化生成器。分别标出数据产物与反馈箭头。

**摘录出处：**[Pengyu Zeng et al. (CVPR Findings 2026) · GreenPlanner: Practical Floorplan Layout Generation via an Energy-Aware and Function-Feasible Generative Framework](https://openaccess.thecvf.com/content/CVPR2026F/html/Zeng_GreenPlanner_Practical_Floorplan_Layout_Generation_via_an_Energy-Aware_and_Function-Feasible_CVPRF_2026_paper.html)；Figure 2 caption，最后一句；PDF p.3，proceedings p.8598；对应§3 Method；CVF Open Access 作者接受版；正式发表元数据已由 CVF 条目核对；该工作已发表；引文版本单独标明；教学改写与模拟回复不属于论文原文

**原文／图片许可：**原权利人保留版权；CVF Open Access 未声明 CC BY。本指南仅作署名教学短引，不重新发布全文或原图，不向第三方转授原论文版权。

```text
为【研究问题】设计一张【方法图或动机图】的概念草图。读者看完应理解【唯一主要信息】。
真实内容：【输入、模块、输出、依赖关系】。模块和术语严格沿用正文，不添加不存在的步骤、结果或能力。并行与先后关系必须准确。
参考【自己制作、已获授权或许可允许使用的风格图】的留白、层级与少量协调色，保留清晰标签位置，避免复制受保护的具体表达。不要生成曲线、柱状图、表格数值、性能对比或误差条；需要结果面板时只预留位置，由真实数据另行绘制。
先给布局说明和信息检查清单，再给绘图提示词。
```

来源与延伸阅读：[作者提供的写作、绘图与进阶笔记](https://github.com/Da1yuqin/PaperBank/blob/main/SOURCES.md#写作笔记)；[Pengyu Zeng et al. (CVPR Findings 2026) · GreenPlanner: Practical Floorplan Layout Generation via an Energy-Aware and Function-Feasible Generative Framework](https://openaccess.thecvf.com/content/CVPR2026F/html/Zeng_GreenPlanner_Practical_Floorplan_Layout_Generation_via_an_Energy-Aware_and_Function-Feasible_CVPRF_2026_paper.html)

</details>


**核对与责任**

- [ ] **第 48 条：**人工核对来源和原始结果，按当年投稿规则披露 AI 使用；不上传未经授权的材料。

<a id="tip-48"></a>
<details>
<summary>说明、例子与参考</summary>

模型说“已确认”不算核验。打开关键来源，检查数字、图片和改动，再按实际使用情况披露。

**边界：**不要上传没有授权交给外部服务的材料。参考论文可以学写法，不能拼成自己的正文。

**TCDiff++：公开声明不能替代许可与 AI 政策检查**

**论文原文 · English**

> This work does not propose any new dataset.

**中文翻译 · 本指南翻译**

本工作未提出任何新数据集。

**逐句拆解**

1. Data availability 随后指向既有 AIOZ-GDance 数据集，让新增方法与既有数据来源分开，不把公开数据写成自己新建的数据集。
2. 该声明未说明可以把整篇稿件或数据上传到任意外部 AI 服务。公开可访问、数据许可和投稿当年的 AI 规则要各自核对，不能由一个链接推断全部授权。

**教学改写 · English（非论文原文）**

Teaching rewrite: Verify the cited dataset source and its reuse terms, then check the venue’s current AI policy. Disclose permitted AI assistance as required and retain responsibility for the final claims and citations.

**教学改写 · 中文（非论文原文）**

教学改写：核对被引数据集来源与复用条款，再核对会议或期刊当前 AI 政策。按要求披露允许的 AI 辅助，并对最终主张与引用负责。

**摘录出处：**[Yuqin Dai et al. (IJCV 2026；引文为 arXiv v4) · TCDiff++: An End-to-end Trajectory-Controllable Diffusion Model for Harmonious Music-Driven Group Choreography](https://link.springer.com/article/10.1007/s11263-025-02611-3)；Declarations，Data availability，第1句；arXiv v4 PDF p.17；正式期刊页Data Availability可交叉核对；短引来自 arXiv:2506.18671v4，2025-10-05；正式期刊元数据已核对，不将作者稿等同于期刊排版终版；该工作已发表；引文版本单独标明；教学改写与模拟回复不属于论文原文

**原文／图片许可：**arXiv 作者稿采用 non-exclusive distribution 许可，非 CC BY。正式期刊版权按 Springer 出版协议保留；本指南不向第三方转授原论文版权。

来源与延伸阅读：[ACL Rolling Review · Responsible NLP Research](https://aclrollingreview.org/responsibleNLPresearch/)；[NeurIPS · Paper Checklist](https://neurips.cc/public/guides/PaperChecklist)；[Yuqin Dai et al. (IJCV 2026；引文为 arXiv v4) · TCDiff++: An End-to-end Trajectory-Controllable Diffusion Model for Harmonious Music-Driven Group Choreography](https://link.springer.com/article/10.1007/s11263-025-02611-3)

</details>


</details>


<a id="rebuttal"></a>
## 14. Rebuttal

按原问题逐点给答案、证据、修改位置和完成状态。

<details>
<summary>检查清单和真实论文例子（16 项）</summary>


**读准问题，先给答案**

- [ ] **第 49 条：**拆出原意见的具体问题，先正面回答，再给证据和位置；笼统感谢不能替代回答。

<a id="tip-49"></a>
<details>
<summary>说明、例子与参考</summary>

对照 summary、strengths、weaknesses 和 questions 读原稿。一条意见有几层就拆几层，不改题目弱化质疑。

**边界：**问题标题保留真实关切，不通过改名、删条件或改成 Yes/No 来弱化质疑。引用原话就保持准确；转述就标明是转述。

**模拟回复：检索更强就等于证据推理更可靠吗？**

**论文原文 · English**

> Yet, stronger retrieval alone cannot address challenges in interpreting and reasoning over evidence.

**中文翻译 · 本指南翻译**

但更强的检索本身不能解决解释证据与基于证据推理的困难。

**逐句拆解**

1. 第一句直接回应模拟的二选一问题，后两句分别给出处与结论边界。
2. 这是依据公开结论写的模拟回复，不是实际审稿记录，也不声称已经完成新的推理实验或改稿。

**教学改写 · English（非论文原文）**

No: improved retrieval does not by itself establish reliable reasoning over evidence.
The conclusion explicitly separates these two capabilities.
The retrieval results should therefore be discussed within their measured scope rather than presented as proof that the reasoning problem is solved.

**教学改写 · 中文（非论文原文）**

不能：检索改善本身不证明证据推理可靠。
结论明确区分了这两项能力。
因此应按已测量范围讨论检索结果，不能将这些结果说成推理问题已经解决的证明。

**摘录出处：**[Yuqin Dai et al. (AAAI 2026) · Careful Queries, Credible Results: Teaching RAG Models Advanced Web Search Tools with Reinforcement Learning](https://ojs.aaai.org/index.php/AAAI/article/view/40299)；§ Conclusion，第 2 句；AAAI 2026 作者终稿；已发表论文；下方教学改写或模拟回复不属于论文原文

**原文／图片许可：**Yuqin Dai et al., AAAI 2026, pp.30458–30466. ©2026 AAAI，保留原版权；作者教学短引，不随本指南转授再版许可。中文为本指南翻译，拆解与教学改写单独标注。

来源与延伸阅读：[作者提供的写作、绘图与进阶笔记](https://github.com/Da1yuqin/PaperBank/blob/main/SOURCES.md#写作笔记)；[NeurIPS 2026 · Main Track Handbook V2026.3，Author Responses](https://neurips.cc/Conferences/2026/MainTrackHandbook)；[写作技能与检查方法](https://github.com/Da1yuqin/PaperBank/blob/main/SOURCES.md#写作技能)；[Yuqin Dai et al. (AAAI 2026) · Careful Queries, Credible Results: Teaching RAG Models Advanced Web Search Tools with Reinforcement Learning](https://ojs.aaai.org/index.php/AAAI/article/view/40299)

</details>

- [ ] **第 61 条：**按原文给问题编号，多个关切拆开；先处理影响结论的问题，困难问题也不能遗漏。

<a id="tip-61"></a>
<details>
<summary>说明、例子与参考</summary>

保留短引与位置，区分事实、对照、机制、复现和表达问题。优先级只改变处理顺序，不改变问题含义。

**边界：**优先级改变工作顺序，不改变问题含义，也不意味着可以遗漏难题。不要根据低分、高 confidence 或未回复推断审稿人水平。

**TCDiff：先分清问题问的是群舞还是单舞（模拟回复）**

**论文原文 · English**

> We employ metrics for both multi-dancer and single-dancer evaluations to assess our model.

**中文翻译 · 本指南翻译**

我们采用多舞者与单舞者两类评价指标来评估模型。

**逐句拆解**

1. 原文将群舞的真实感、协调性与碰撞，和单舞的保真度、多样性、音乐一致性与脚步指标分开。一条意见涉及两类质量时，应拆成两个关切。
2. 原句是评价设置，不是真实审稿意见。下面仅示范保留原问题、按对象拆解回复，不能据此虚构审稿人问过这些问题。

**教学改写 · English（非论文原文）**

Simulated reply structure: Preserve the reviewer’s original wording, then separate the concern about group coordination from the concern about individual fidelity. Answer each with the relevant metric and comparison rather than inventing an additional request.

**教学改写 · 中文（非论文原文）**

模拟回复结构：保留审稿人原话，再将群体协调性与个体保真度的关切分开。分别用相应指标与对照回答，不另替审稿人添加要求。

**摘录出处：**[Yuqin Dai et al. (AAAI 2025) · Harmonious Music-driven Group Choreography with Trajectory-Controllable Diffusion](https://ojs.aaai.org/index.php/AAAI/article/view/32268)；§Experiments，Metrics，第1句；PDF p.5，proceedings p.2649；正式发表版本；作者原文短引；该工作已发表；引文版本单独标明；教学改写与模拟回复不属于论文原文

**原文／图片许可：**作者教学复用；原论文英文短引与原图不受 PaperBank 原创内容 CC BY 授权覆盖。本文不转授第三方转载原论文材料的权利。

来源与延伸阅读：[作者提供的写作、绘图与进阶笔记](https://github.com/Da1yuqin/PaperBank/blob/main/SOURCES.md#写作笔记)；[写作技能与检查方法](https://github.com/Da1yuqin/PaperBank/blob/main/SOURCES.md#写作技能)；[NeurIPS 2026 · Main Track Handbook V2026.3，Author Responses](https://neurips.cc/Conferences/2026/MainTrackHandbook)；[Yuqin Dai et al. (AAAI 2025) · Harmonious Music-driven Group Choreography with Trajectory-Controllable Diffusion](https://ojs.aaai.org/index.php/AAAI/article/view/32268)

</details>

- [ ] **第 63 条：**第一句给实际答案，再给依据和位置；感谢简短，开放问题不用 Yes/No 糊过去。

<a id="tip-63"></a>
<details>
<summary>说明、例子与参考</summary>

参数直接给值，定义直接解释，合理批评说明承认什么。有条件的问题保留条件，真的完成修改才写“已修改”。

**边界：**不把开放问题硬改成 Yes/No，不用礼貌措辞掩盖没有答案。接受、澄清和合理不同意都可以自然表达。

**模拟回复：SEN 和普通摘要差在哪里，先直接答**

**论文原文 · English**

> SENs incorporate two annotation types: key information (denoted by *) and uncertain information (denoted by -).

**中文翻译 · 本指南翻译**

支持性证据笔记（SEN）包含两种标记：用 * 标记关键信息，用 - 标记不确定信息。

**逐句拆解**

1. 面对“SEN 与普通摘要有什么区别”的问题，先给两个具体标记与信息筛选对象，不用一段感谢把答案往后藏。
2. 定义位置与消融位置分别给出：前者告诉读者做了什么，后者提供比较依据；两者不能互相代替。
3. 模拟回复不宣称审稿人认可，也不虚构已按意见修改。

**教学改写 · English（非论文原文）**

Simulated response: SENs retain answer-supportive evidence and mark key information with * and uncertain information with -. These explicit annotations distinguish SENs from the Naive Summary configuration. The definition is in Section 3.2, and the comparison is reported in the ablation study in Section 4.6. Thank you for asking us to clarify the distinction.

**教学改写 · 中文（非论文原文）**

模拟回复：SEN 保留支持答案的证据，并用 * 标记关键信息、用 - 标记不确定信息。这些显式标记是 SEN 与 Naive Summary 配置的区别。定义见第 3.2 节，比较见第 4.6 节消融实验。感谢指出这一处需要澄清的区别。

**摘录出处：**[Yuqin Dai et al. · EviNoteRAG: Enhancing RAG Models via Quality-Augmented Evidence Notes](https://arxiv.org/abs/2509.00877)；§ 3.2 Supportive-Evidence Note / Evidence-aware Annotations，首句，PDF 第 3 页；相关消融 § 4.6，PDF 第 6 页；EMNLP 2026 revised 作者终稿；公开链接为 arXiv v3；作者终稿短引；公开链接为不同版本预印本；下方教学改写或模拟回复不属于论文原文

**原文／图片许可：**作者终稿教学短引，保留原论文版权；不随 PaperBank 原创内容转授原论文再版许可。公开 arXiv v3 为 non-exclusive distribution，并非 CC 授权；代码 Apache 2.0 不作为论文许可。

来源与延伸阅读：[作者提供的写作、绘图与进阶笔记](https://github.com/Da1yuqin/PaperBank/blob/main/SOURCES.md#写作笔记)；[写作技能与检查方法](https://github.com/Da1yuqin/PaperBank/blob/main/SOURCES.md#写作技能)；[ICLR 2026 · Author Guide，Discussion Stages](https://iclr.cc/Conferences/2026/AuthorGuide)；[Yuqin Dai et al. · EviNoteRAG: Enhancing RAG Models via Quality-Augmented Evidence Notes](https://arxiv.org/abs/2509.00877)

</details>

- [ ] **第 100 条：**多问题意见逐项拆开，给结论、证据和位置；未解决照实保留，不用“已改”包办。

<a id="tip-100"></a>
<details>
<summary>说明、例子与参考</summary>

完整回答不等于完成每个请求，关键是每个问题都有明确状态。

**边界：**模拟审稿问题与回复只用于教学，不是真实审稿记录。补实验、修订和回复格式以当轮官方政策为准；没有完成的事不写成已完成。

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

来源与延伸阅读：[写作技能与检查方法](https://github.com/Da1yuqin/PaperBank/blob/main/SOURCES.md#写作技能)

</details>


**证据与补实验**

- [ ] **第 62 条：**每项回复登记证据、设置、位置和完成状态，回查原始结果；没依据就保留未解决。

<a id="tip-62"></a>
<details>
<summary>说明、例子与参考</summary>

旧结果注明版本与行列，新结果注明配置、样本单位、指标和输出。引用汇总数要查分母及异常处理，投入资源不能代替效果证据。

**边界：**设计动机、开源承诺、投入了多少卡或 API，都不能代替效果证据。文献支持一般原理，也不能冒充本方法已经通过的实验。

**TCDiff：回复里的收益必须能定位到同一张表（模拟回复）**

**论文原文 · English**

> Tables 1 and 2 compare our model’s performance with baseline methods.

**中文翻译 · 本指南翻译**

表 1 与表 2 将本模型表现与基线方法进行比较。

**逐句拆解**

1. 表 1 的 GMR：TCDiff 为 13.86，CoDancers 为 26.10，越低越好；表 2 按人数展开。回复要注明总表或特定人数，不能混拿两张表的数值。
2. 同表 FID：TCDiff 为 37.47，CoDancers 为 23.98，越低越好。群舞真实感证据不能被写成对个体保真度也全面胜出。

**教学改写 · English（非论文原文）**

Simulated reply: Table 1 supports improved group-motion realism over CoDancers (GMR: 26.10 to 13.86, lower is better). The same comparison shows a trade-off in individual fidelity (FID: 23.98 versus 37.47, lower is better), so the claim is limited to the reported group-level benefit.

**教学改写 · 中文（非论文原文）**

模拟回复：表 1 支持相对 CoDancers 的群舞真实感提升（GMR 从 26.10 到 13.86，越低越好）。同一比较显示个体保真度的代价（FID 分别为 23.98 与 37.47，越低越好），因此主张限定为已报告的群体层面收益。

**摘录出处：**[Yuqin Dai et al. (AAAI 2025) · Harmonious Music-driven Group Choreography with Trajectory-Controllable Diffusion](https://ojs.aaai.org/index.php/AAAI/article/view/32268)；§Comparison to the State of the Art，Quantitative Results，第1句及Table 1–2；PDF p.6–7，proceedings pp.2650–2651；正式发表版本；作者原文短引；该工作已发表；引文版本单独标明；教学改写与模拟回复不属于论文原文

**原文／图片许可：**作者教学复用；原论文英文短引与原图不受 PaperBank 原创内容 CC BY 授权覆盖。本文不转授第三方转载原论文材料的权利。

来源与延伸阅读：[作者提供的写作、绘图与进阶笔记](https://github.com/Da1yuqin/PaperBank/blob/main/SOURCES.md#写作笔记)；[NeurIPS · Paper Checklist](https://neurips.cc/public/guides/PaperChecklist)；[写作技能与检查方法](https://github.com/Da1yuqin/PaperBank/blob/main/SOURCES.md#写作技能)；[Yuqin Dai et al. (AAAI 2025) · Harmonious Music-driven Group Choreography with Trajectory-Controllable Diffusion](https://ojs.aaai.org/index.php/AAAI/article/view/32268)

</details>

- [ ] **第 50 条：**区分原有结果、新分析、新实验和未完成计划；给设置与位置，缺证据就收窄主张。

<a id="tip-50"></a>
<details>
<summary>说明、例子与参考</summary>

补材料前查当轮规则。NeurIPS 2026 主会允许回复新结果但不许修订稿件或加附件；ICLR 2026 讨论期允许修订并说明变更。

**边界：**上面的流程只对应列出的版本。外链、字符数、附件和修订权限按当年赛道与系统通知重新核对；不能把一个会议的习惯套到所有会议。

**GreenPlanner：已有消融不能改称新实验（模拟回复）**

**论文原文 · English**

> This isolates the effect of RL optimization and is evaluated under four target energy levels (110–140 EUI).

**中文翻译 · 本指南翻译**

这用于隔离 RL 优化的作用，并在四个目标能耗水平（110–140 EUI）下评价。

**逐句拆解**

1. “This”指在 GreenPD 上训练但不用 PDE 强化学习的无 RL 变体。与完整模型比较，是为了分开数据与优化的作用。
2. 结果已在 §4.7、图 5 与表 5 中报告，应称已有消融证据。没有新增运行记录，不能写成刚补做实验；四个 EUI 条件也不能代表任意目标范围。

**教学改写 · English（非论文原文）**

Simulated reply: The existing ablation in Section 4.7 compares the GreenPD-only variant with the RL-enhanced model at four target EUI levels. This is previously reported evidence; broader target ranges are not established by this comparison.

**教学改写 · 中文（非论文原文）**

模拟回复：第 4.7 节已有消融在四个目标 EUI 水平下比较仅使用 GreenPD 的变体与加入 RL 的模型。这是先前报告的证据；这项比较尚不能确立更广目标范围上的表现。

**摘录出处：**[Pengyu Zeng et al. (CVPR Findings 2026) · GreenPlanner: Practical Floorplan Layout Generation via an Energy-Aware and Function-Feasible Generative Framework](https://openaccess.thecvf.com/content/CVPR2026F/html/Zeng_GreenPlanner_Practical_Floorplan_Layout_Generation_via_an_Energy-Aware_and_Function-Feasible_CVPRF_2026_paper.html)；§4.7 w/o RL 设置续段；PDF p.8，proceedings p.8603；Figure 5、Table 5；CVF Open Access 作者接受版；正式发表元数据已由 CVF 条目核对；该工作已发表；引文版本单独标明；教学改写与模拟回复不属于论文原文

**原文／图片许可：**原权利人保留版权；CVF Open Access 未声明 CC BY。本指南仅作署名教学短引，不重新发布全文或原图，不向第三方转授原论文版权。

来源与延伸阅读：[作者提供的写作、绘图与进阶笔记](https://github.com/Da1yuqin/PaperBank/blob/main/SOURCES.md#写作笔记)；[NeurIPS 2026 · Main Track Handbook V2026.3，Author Responses](https://neurips.cc/Conferences/2026/MainTrackHandbook)；[ICLR 2026 · Author Guide，Discussion Stages](https://iclr.cc/Conferences/2026/AuthorGuide)；[ACL Rolling Review · Authors Guidelines，Author response](https://aclrollingreview.org/authors#author-response)；[Pengyu Zeng et al. (CVPR Findings 2026) · GreenPlanner: Practical Floorplan Layout Generation via an Energy-Aware and Function-Feasible Generative Framework](https://openaccess.thecvf.com/content/CVPR2026F/html/Zeng_GreenPlanner_Practical_Floorplan_Layout_Generation_via_an_Energy-Aware_and_Function-Feasible_CVPRF_2026_paper.html)

</details>

- [ ] **第 64 条：**补实验先定解释、固定项、改变项和指标；报告完整比较与不确定性，再下结论。

<a id="tip-64"></a>
<details>
<summary>说明、例子与参考</summary>

匹配模型、样本、文档池和预算，只改变待检验因素。预先定纳入范围与重复方式；设置不同的数字分开报，先查当轮允许材料。

**边界：**一个消融的相关变化不自动证明机制；样本、资源与信息范围不一致的公开论文数字不能当作受控比较。补多少实验不等于态度分。

**UrbanZero：回复“只是多花预算”先设计匹配对照**

**教学改写：依据 UrbanZero 公开项目介绍，非论文原文**

依据公开项目介绍中的语义简报、地块任务、逐块规划和程序反馈编写。中英示例为本指南教学改写；实验问题和模拟回复方案不代表项目已完成的工作。

**改前 · 中文**

我们效果更好，所以肯定不是预算的原因。

**Before · English**

Our results are better, so the gain cannot come from extra budget.

**改后 · 中文**

模拟回复方案：感谢指出预算可能影响比较。我们会匹配模型、城市窗口和允许预算，对照两种求解方式，并分别报告完成率与空间目标得分。

**After · English**

Simulated response plan: thank you for identifying the possible budget effect. We would match the model, urban windows, and allowed budget across solving modes, then report completion rates and spatial-objective scores separately.

**逐句拆解**

1. 把审稿人的替代解释写成可检验对照，不能拿现有总分反驳尚未匹配的预算。
2. would 表示方案尚未完成；实际回复只有拿到记录后才能改成结果，且须遵守投稿当年的回复规则。

来源与延伸阅读：[作者提供的写作、绘图与进阶笔记](https://github.com/Da1yuqin/PaperBank/blob/main/SOURCES.md#写作笔记)；[NeurIPS · Paper Checklist](https://neurips.cc/public/guides/PaperChecklist)；[NeurIPS 2026 · Main Track Handbook V2026.3，Author Responses](https://neurips.cc/Conferences/2026/MainTrackHandbook)；[Chaoyang Shi, Yuqin Dai et al. · UrbanZero（公开项目介绍）](https://github.com/Da1yuqin/Da1yuqin.github.io/blob/main/_pages/includes/pub.md#L193-L202)

</details>

- [ ] **第 67 条：**说明未完成检验和关键负结果，保留分组、分母与选择规则；不支持的主张收窄或撤回。

<a id="tip-67"></a>
<details>
<summary>说明、例子与参考</summary>

阶段性结果说明实际覆盖。相关表行可精简，但不能删掉会改变判断的失败组，也不能换指标或样本把失败改写成成功。

**边界：**计划不是证据，负结果不等于工作毫无价值。若重要主张被否定，应纠正主张，而不是更换指标、样本或措辞把它重新说成成立。

**TCDiff++：未支持的控制输入就说未支持（模拟回复）**

**论文原文 · English**

> First, our model lacks support for multimodal or user-controllable inputs.

**中文翻译 · 本指南翻译**

首先，本模型尚不支持多模态或用户可控输入。

**逐句拆解**

1. 局限性段落说明当前主要做音乐到舞蹈的基础跨模态生成，文本描述、动作关键帧、舞种条件留给后续探索。不能因为方法名含“可控”就宣称交互已实现。
2. 回复时区分已有音乐条件与未实现的控制方式。未来方向不是已完成实验，内部位置约束也不能替代用户交互能力。

**教学改写 · English（非论文原文）**

Simulated reply: Text prompts, motion keyframes, and genre-specific user controls are outside the current model’s demonstrated scope. Section 6 identifies these extensions as future work; the present experiments do not validate them.

**教学改写 · 中文（非论文原文）**

模拟回复：文本提示、动作关键帧和舞种专属用户控制超出当前模型已展示的范围。第 6 节将这些扩展列为未来工作；当前实验未验证这些能力。

**摘录出处：**[Yuqin Dai et al. (IJCV 2026；引文为 arXiv v4) · TCDiff++: An End-to-end Trajectory-Controllable Diffusion Model for Harmonious Music-Driven Group Choreography](https://link.springer.com/article/10.1007/s11263-025-02611-3)；§6 Limitation，第2句及随后限定；arXiv v4 PDF p.16–17；短引来自 arXiv:2506.18671v4，2025-10-05；正式期刊元数据已核对，不将作者稿等同于期刊排版终版；该工作已发表；引文版本单独标明；教学改写与模拟回复不属于论文原文

**原文／图片许可：**arXiv 作者稿采用 non-exclusive distribution 许可，非 CC BY。正式期刊版权按 Springer 出版协议保留；本指南不向第三方转授原论文版权。

来源与延伸阅读：[作者提供的写作、绘图与进阶笔记](https://github.com/Da1yuqin/PaperBank/blob/main/SOURCES.md#写作笔记)；[NeurIPS · Paper Checklist](https://neurips.cc/public/guides/PaperChecklist)；[写作技能与检查方法](https://github.com/Da1yuqin/PaperBank/blob/main/SOURCES.md#写作技能)；[Yuqin Dai et al. (IJCV 2026；引文为 arXiv v4) · TCDiff++: An End-to-end Trajectory-Controllable Diffusion Model for Harmonious Music-Driven Group Choreography](https://link.springer.com/article/10.1007/s11263-025-02611-3)

</details>


**澄清与分歧**

- [ ] **第 65 条：**事实澄清给准确版本、定义和原稿位置，必要时举一个案例；不指责审稿人没看懂。

<a id="tip-65"></a>
<details>
<summary>说明、例子与参考</summary>

先核对稿件和代码，再说明训练用什么、推理见什么、评价由谁做。表达确有歧义就承认，修改状态照实写。

**边界：**不要为了避冲突保留错误描述，也不要纠缠不影响核心关切的措辞。澄清一个事实不自动解决相邻的效果质疑。

**模拟澄清：确定性具体属于哪一步**

**论文原文 · English**

> Note that while the Rule Engine itself is fully deterministic given fixed inputs

**中文翻译 · 本指南翻译**

需要注意，规则引擎在输入固定时本身是完全确定性的。

**逐句拆解**

1. 固定输入是定义边界，不能删掉后直接宣称整个多智能体评价完全确定。
2. 原文紧接着说明，上游分类标签由 LLM 评判模型产生，仍带随机性；三评判模型投票用来减少这种变化，不是消除所有偏差。
3. 模拟回复先给清楚答案，再给模块定义与出处；不把分歧归结为审稿人没认真读。

**教学改写 · English（非论文原文）**

Simulated response: Determinism applies to the Rule Engine conditional on fixed inputs, not to the entire judge pipeline. The Rule Engine uses the consensus classification, system information, and SOP graph; the upstream LLM judges can still vary. The distinction is stated in the Rule Engine subsection.

**教学改写 · 中文（非论文原文）**

模拟回复：确定性指固定输入条件下的规则引擎，而非整个评判流程。规则引擎接收共识分类、系统信息和 SOP 图；上游 LLM 评判仍可能变化。这个区分见 Rule Engine 小节。

**摘录出处：**[Ling Shi, Yuqin Dai et al. · SAGE: An Extensible Benchmark for Service Agent Graph-guided Evaluation](https://arxiv.org/abs/2604.09285)；§ Graph-Guided Multi-Agent Evaluation / Rule Engine，公式后限定句的前半句（作者源稿第 550 行）；作者终稿 2026-10-04 只读快照；公开链接为 arXiv v1；作者终稿短引；公开链接为不同版本预印本；下方教学改写或模拟回复不属于论文原文

**原文／图片许可：**作者终稿教学短引，保留原论文版权；不随 PaperBank 原创内容转授终稿转载权。公开 arXiv v1 的 CC BY 4.0 已核验，该许可不自动延伸到不同版本的作者终稿。

来源与延伸阅读：[作者提供的写作、绘图与进阶笔记](https://github.com/Da1yuqin/PaperBank/blob/main/SOURCES.md#写作笔记)；[写作技能与检查方法](https://github.com/Da1yuqin/PaperBank/blob/main/SOURCES.md#写作技能)；[NeurIPS · Paper Checklist](https://neurips.cc/public/guides/PaperChecklist)；[Ling Shi, Yuqin Dai et al. · SAGE: An Extensible Benchmark for Service Agent Graph-guided Evaluation](https://arxiv.org/abs/2604.09285)

</details>

- [ ] **第 51 条：**意见成立就承认并改；不同意时给定义、条件和证据，不推测审稿人的动机。

<a id="tip-51"></a>
<details>
<summary>说明、例子与参考</summary>

理论问题给推导与假设，实现问题给流程，效果问题给对应比较。礼貌不能替代理由，也不保证改分。

**边界：**礼貌不等于照单全收，也不保证改分或录用。按意见内容选择论证，不推测审稿人的身份、能力、情绪或动机。

**模拟回复：承认训练价值，说明本篇的评价范围**

**论文原文 · English**

> While SAGE evaluates agent behavior at inference time, it does not directly address how benchmark findings can be used to improve models via fine-tuning or reinforcement learning, which is seen as a promising direction.

**中文翻译 · 本指南翻译**

SAGE 评价的是推理阶段的智能体行为，并未直接研究如何通过微调或强化学习，利用基准发现来改进模型；这被视为有前景的后续方向。

**逐句拆解**

1. 原句先交代当前研究范围，再承认训练改进尚未解决；可以不同意把训练效果作为本篇已完成贡献的要求，同时承认这个方向有价值。
2. 模拟回复依据论文 Limitations 说明范围，不猜测审稿人的动机，也不虚构已完成微调或新增实验。
3. 如果论文先前声称基准已经改善模型，范围解释就不够，还需收回未被实验支持的主张。

**教学改写 · English（非论文原文）**

Simulated response: We agree that using the benchmark to improve model training is valuable. SAGE evaluates inference-time behavior; the current study does not test fine-tuning or reinforcement learning driven by the benchmark. We therefore limit the claim to evaluation and diagnosis, as stated in Limitations.

**教学改写 · 中文（非论文原文）**

模拟回复：我们同意，用基准改进模型训练是有价值的方向。SAGE 评价推理阶段的行为；本研究没有测试由该基准驱动的微调或强化学习。因此，我们将主张限定为评价与诊断，范围见 Limitations。

**摘录出处：**[Ling Shi, Yuqin Dai et al. · SAGE: An Extensible Benchmark for Service Agent Graph-guided Evaluation](https://arxiv.org/abs/2604.09285)；§ Limitations，最后一句（作者源稿第 1057 行）；作者终稿 2026-10-04 只读快照；公开链接为 arXiv v1；作者终稿短引；公开链接为不同版本预印本；下方教学改写或模拟回复不属于论文原文

**原文／图片许可：**作者终稿教学短引，保留原论文版权；不随 PaperBank 原创内容转授终稿转载权。公开 arXiv v1 的 CC BY 4.0 已核验，该许可不自动延伸到不同版本的作者终稿。

来源与延伸阅读：[作者提供的写作、绘图与进阶笔记](https://github.com/Da1yuqin/PaperBank/blob/main/SOURCES.md#写作笔记)；[写作技能与检查方法](https://github.com/Da1yuqin/PaperBank/blob/main/SOURCES.md#写作技能)；[NeurIPS 2026 · Main Track Handbook V2026.3，Author Responses](https://neurips.cc/Conferences/2026/MainTrackHandbook)；[Ling Shi, Yuqin Dai et al. · SAGE: An Extensible Benchmark for Service Agent Graph-guided Evaluation](https://arxiv.org/abs/2604.09285)

</details>

- [ ] **第 66 条：**不适用的请求说明目标、条件与限制；提供可回答原关切的替代，设置差别仍写清。

<a id="tip-66"></a>
<details>
<summary>说明、例子与参考</summary>

先分核心正确性检验和范围扩展。请求适用就完成；不适用给任务、权限、可见信息或预算差异，证据受限就收窄结论。

**边界：**不把“结果较差”当作设置不合理的证据；商业模型、私有数据或大预算也不天然无效。比较受限时收窄结论，不暗示自己或对方的机构身份。

**GreenPlanner：比较做不了，交代条件与替代检查（模拟回复）**

**论文原文 · English**

> Hence, these methods are excluded from quantitative energy evaluation.

**中文翻译 · 本指南翻译**

因此，这些方法未纳入定量能耗评价。

**逐句拆解**

1. 前文理由是部分方法缺少门窗等开口或必要功能组件，完整 EUI 评价条件不成立。这不等于这些方法在能耗指标上已经落败。
2. §4.5 与图 4 另报告向部分输出随机加入 1–2 个开口以支持评价，改变了原始输出。提出替代检查时保留修改说明，不能混作未经处理的基线结果。

**教学改写 · English（非论文原文）**

Simulated reply: A direct energy comparison requires layouts with the necessary openings and functional components. For an adjusted-output check, describe the added openings and keep that result separate from the original baseline outputs.

**教学改写 · 中文（非论文原文）**

模拟回复：直接比较能耗需要平面图具备必要开口与功能组件。若检查修改后的输出，说明新增开口，并将结果与原始基线输出分开。

**摘录出处：**[Pengyu Zeng et al. (CVPR Findings 2026) · GreenPlanner: Practical Floorplan Layout Generation via an Energy-Aware and Function-Feasible Generative Framework](https://openaccess.thecvf.com/content/CVPR2026F/html/Zeng_GreenPlanner_Practical_Floorplan_Layout_Generation_via_an_Energy-Aware_and_Function-Feasible_CVPRF_2026_paper.html)；§4.6 排除说明最后一句；PDF p.6，proceedings p.8601；交叉核对§4.5及Figure 4；CVF Open Access 作者接受版；正式发表元数据已由 CVF 条目核对；该工作已发表；引文版本单独标明；教学改写与模拟回复不属于论文原文

**原文／图片许可：**原权利人保留版权；CVF Open Access 未声明 CC BY。本指南仅作署名教学短引，不重新发布全文或原图，不向第三方转授原论文版权。

来源与延伸阅读：[作者提供的写作、绘图与进阶笔记](https://github.com/Da1yuqin/PaperBank/blob/main/SOURCES.md#写作笔记)；[写作技能与检查方法](https://github.com/Da1yuqin/PaperBank/blob/main/SOURCES.md#写作技能)；[NeurIPS 2026 · Main Track Handbook V2026.3，Author Responses](https://neurips.cc/Conferences/2026/MainTrackHandbook)；[Pengyu Zeng et al. (CVPR Findings 2026) · GreenPlanner: Practical Floorplan Layout Generation via an Energy-Aware and Function-Feasible Generative Framework](https://openaccess.thecvf.com/content/CVPR2026F/html/Zeng_GreenPlanner_Practical_Floorplan_Layout_Generation_via_an_Energy-Aware_and_Function-Feasible_CVPRF_2026_paper.html)

</details>

- [ ] **第 69 条：**当轮允许时，给 AC 汇总关切、证据位置和未解限制；准确引用反馈，不按分数选边。

<a id="tip-69"></a>
<details>
<summary>说明、例子与参考</summary>

领域主席负责汇总判断。摘要按问题说明已经回答什么、证据支持到哪步、还剩什么；流程问题走官方渠道，不猜测身份或心态。

**边界：**不存在适用于所有会议的审稿分数与 AC 摘要权重公式。摘要长度与私密读者权限按当轮规则；不隐去关键负结果，不猜测低分或未回复的原因，也不奉承 AC。

**TCDiff：给 AC 的摘要把收益和代价放一起（模拟摘要）**

**论文原文 · English**

> TCDiff effectively captures inter-dancer correlations (high GMC) with a slight trade-off in individual fidelity (FID).

**中文翻译 · 本指南翻译**

TCDiff 能较好捕捉舞者间相关性（GMC 较高），同时在个体保真度（FID）上存在一定代价。

**逐句拆解**

1. 原句同时报告群体收益与个体代价，适合示范定位摘要：说关切是什么、证据在哪、结论有哪些限制。
2. 表 1 的 GMC：81.98，对照 CoDancers 为 74.05；FID：37.47，对照为 23.98。不能因群体指标较好，就要求 AC 忽略代价或按审稿分数站队。

**教学改写 · English（非论文原文）**

Simulated AC summary: Group-coordination evidence is in Table 1 (GMC: 81.98 versus 74.05 for CoDancers, higher is better). Individual fidelity remains a trade-off (FID: 37.47 versus 23.98, lower is better). This locates the evidence and boundary without asking the AC to favor a reviewer.

**教学改写 · 中文（非论文原文）**

模拟 AC 摘要：群体协调性证据见表 1（GMC：81.98，对照 CoDancers 为 74.05，越高越好）。个体保真度仍有代价（FID：37.47，对照为 23.98，越低越好）。这定位了证据与边界，不要求 AC 偏向任何审稿人。

**摘录出处：**[Yuqin Dai et al. (AAAI 2025) · Harmonious Music-driven Group Choreography with Trajectory-Controllable Diffusion](https://ojs.aaai.org/index.php/AAAI/article/view/32268)；§Quantitative Results，第3句；PDF p.6，proceedings p.2650；Table 1；正式发表版本；作者原文短引；该工作已发表；引文版本单独标明；教学改写与模拟回复不属于论文原文

**原文／图片许可：**作者教学复用；原论文英文短引与原图不受 PaperBank 原创内容 CC BY 授权覆盖。本文不转授第三方转载原论文材料的权利。

来源与延伸阅读：[作者提供的写作、绘图与进阶笔记](https://github.com/Da1yuqin/PaperBank/blob/main/SOURCES.md#写作笔记)；[NeurIPS 2026 · Main Track Handbook V2026.3，Author Responses](https://neurips.cc/Conferences/2026/MainTrackHandbook)；[ICLR 2026 · Author Guide，Discussion Stages](https://iclr.cc/Conferences/2026/AuthorGuide)；[ACL Rolling Review · Authors Guidelines，Author response](https://aclrollingreview.org/authors#author-response)；[Yuqin Dai et al. (AAAI 2025) · Harmonious Music-driven Group Choreography with Trajectory-Controllable Diffusion](https://ojs.aaai.org/index.php/AAAI/article/view/32268)

</details>

- [ ] **第 102 条：**回答具体担忧，给理由和证据；不用“显然”或“你错了”，不为客气承认不存在的问题。

<a id="tip-102"></a>
<details>
<summary>说明、例子与参考</summary>

把讨论留在条件、结果和表述上。可以坚定不同意，但不评价审稿人的能力或动机。

**边界：**模拟审稿问题与回复只用于教学，不是真实审稿记录。补实验、修订和回复格式以当轮官方政策为准；没有完成的事不写成已完成。

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

来源与延伸阅读：[写作技能与检查方法](https://github.com/Da1yuqin/PaperBank/blob/main/SOURCES.md#写作技能)

</details>


**状态与提交**

- [ ] **第 68 条：**统一回复、修订稿和表格的版本、数值与主张；交叉引用先给答案，沉默不视为认可。

<a id="tip-68"></a>
<details>
<summary>说明、例子与参考</summary>

维护共同事实表，新增结果后更新全部相关回复。跳转给编号和短结论，不用另一位审稿人的高分替代当前问题的证据。

**边界：**未留言不代表接受解释；只有明确回复才能称为已确认。不要用其他审稿人的高分或赞许代替当前问题的证据。

**模拟事实统一：答案正确与笔记蕴含是两种信号**

**论文原文 · English**

> The answer criterion requires an exact match with the ground truth, and the note-taking criterion holds when Evidence-aware Annotations are marked according to the SEN design.

**中文翻译 · 本指南翻译**

答案条件要求与真实答案精确匹配；笔记条件则要求按 SEN 设计标注证据感知标记。

**逐句拆解**

1. 原句分别定义答案条件与笔记标记条件；EQR 的 NLI 蕴含分数又是另一项信号，不能在不同回复里混成一个 Judge。
2. 维护共同事实表时，记录每项信号的输入、对象和用途：答案匹配检查答案，标记检查笔记格式，EQR 检查最后一条笔记对正确答案命题的支持。
3. 这些共同定义可复用；各条回复仍应先回答当前问题，不用“见另一位审稿人的回复”代替答案。

**教学改写 · English（非论文原文）**

Simulated response: Answer correctness, note-taking compliance, and EQR play different roles in the reward. Answer correctness uses exact matching to the ground truth; note-taking compliance checks the evidence-aware annotations; EQR uses NLI to score whether the final SEN supports the correct-answer claim. We use these same definitions in every response.

**教学改写 · 中文（非论文原文）**

模拟回复：答案正确性、笔记标记合规性与 EQR 在奖励中承担不同职责。答案正确性使用真值精确匹配；笔记合规性检查证据感知标记；EQR 使用 NLI 评价最后一条 SEN 是否支持正确答案命题。各条回复统一使用这套定义。

**摘录出处：**[Yuqin Dai et al. · EviNoteRAG: Enhancing RAG Models via Quality-Augmented Evidence Notes](https://arxiv.org/abs/2509.00877)；§ 3.4 Training Strategy / Reward Strategy，奖励公式后的条件定义，PDF 第 4 页；EQR 定义 § 3.3，PDF 第 3 页；EMNLP 2026 revised 作者终稿；公开链接为 arXiv v3；作者终稿短引；公开链接为不同版本预印本；下方教学改写或模拟回复不属于论文原文

**原文／图片许可：**作者终稿教学短引，保留原论文版权；不随 PaperBank 原创内容转授原论文再版许可。公开 arXiv v3 为 non-exclusive distribution，并非 CC 授权；代码 Apache 2.0 不作为论文许可。

来源与延伸阅读：[作者提供的写作、绘图与进阶笔记](https://github.com/Da1yuqin/PaperBank/blob/main/SOURCES.md#写作笔记)；[ICLR 2026 · Author Guide，Discussion Stages](https://iclr.cc/Conferences/2026/AuthorGuide)；[NeurIPS 2026 · Main Track Handbook V2026.3，Author Responses](https://neurips.cc/Conferences/2026/MainTrackHandbook)；[Yuqin Dai et al. · EviNoteRAG: Enhancing RAG Models via Quality-Augmented Evidence Notes](https://arxiv.org/abs/2509.00877)

</details>

- [ ] **第 70 条：**请同事或获准工具按原意见查漏答、证据、语气和版本；模拟只作建议，不预测评分。

<a id="tip-70"></a>
<details>
<summary>说明、例子与参考</summary>

逐题查问题是否保留、首句是否回答、证据是否支持、状态是否准确，再人工回查。AI 使用先核对保密和工具政策，不公开私有评审材料。

**边界：**未经许可的审稿材料、真实匿名 ID、内部讨论和身份线索不发布到公共仓库。按意见类型检查，不生成身份画像、情绪推测或录用概率。

**TCDiff：模拟审核查组件和证据，别猜分数**

**论文原文 · English**

> Ablation study of Conditional Motion Denoising (CMD), Footwork Adaptor (FA) and Fusion Projection (FP).

**中文翻译 · 本指南翻译**

对条件动作去噪（CMD）、脚步适配器（FA）和融合投影（FP）进行消融实验。

**逐句拆解**

1. 表 3 列出具名变体，工具可检查回复是否写对组件、对照与指标方向。这是文本和证据核查，不是预测审稿人心情。
2. 移除 FP 时 FID 为 23.77，完整模型为 37.47；原文承认个体保真度代价。发现“所有指标都改善”时应收窄措辞，不能补造有利实验。

**教学改写 · English（非论文原文）**

Teaching audit prompt: Check each reply claim against the named ablation row and metric direction in Table 3. Flag missing trade-offs or unsupported claims, and do not predict reviewer scores or acceptance from the simulated audit.

**教学改写 · 中文（非论文原文）**

教学审核提示词：将每条回复主张与表 3 的具名消融行和指标方向核对。标出遗漏代价和缺少依据的主张，不根据模拟审核预测审稿分数或录用。

**摘录出处：**[Yuqin Dai et al. (AAAI 2025) · Harmonious Music-driven Group Choreography with Trajectory-Controllable Diffusion](https://ojs.aaai.org/index.php/AAAI/article/view/32268)；Table 3 caption，省略“Table 3:”编号的原文；PDF p.7，proceedings p.2651；Effectiveness of Fusion Projection段；正式发表版本；作者原文短引；该工作已发表；引文版本单独标明；教学改写与模拟回复不属于论文原文

**原文／图片许可：**作者教学复用；原论文英文短引与原图不受 PaperBank 原创内容 CC BY 授权覆盖。本文不转授第三方转载原论文材料的权利。

```text
请只根据我提供且允许用于此工具的材料，检查 rebuttal。按每条原始意见保留顺序，列出：实际关切、当前答案、证据位置、完成状态、遗漏或不一致、最小修改建议。不要虚构实验、引用或已完成修改；不要从评分、匿名编号、语气或未回复推断审稿人身份、能力与心理；不要预测涨分或录用。区分事实澄清、合理不同意、缺少证据与已完成修改。检查是否遗漏会改变结论的负结果，是否违反当轮匿名、保密、篇幅、外链或附件规则；未提供规则时只指出需核验的项目。最后逐句核对回复主张是否由给出的证据支持。
```

来源与延伸阅读：[作者提供的写作、绘图与进阶笔记](https://github.com/Da1yuqin/PaperBank/blob/main/SOURCES.md#写作笔记)；[写作技能与检查方法](https://github.com/Da1yuqin/PaperBank/blob/main/SOURCES.md#写作技能)；[NeurIPS 2026 · Main Track Handbook V2026.3，Author Responses](https://neurips.cc/Conferences/2026/MainTrackHandbook)；[Yuqin Dai et al. (AAAI 2025) · Harmonious Music-driven Group Choreography with Trajectory-Controllable Diffusion](https://ojs.aaai.org/index.php/AAAI/article/view/32268)

</details>

- [ ] **第 52 条：**按当轮指南查篇幅、匿名、权限和附件；提交后回读系统文件与评论，核对版本。

<a id="tip-52"></a>
<details>
<summary>说明、例子与参考</summary>

允许修订且已完成，才写修改位置；不许修订，回复里直接给答案。ICLR 审稿人和 AC 不必阅读每一版，关键证据应在回复中可找到。

**边界：**ICLR 2026 指南说明可多次修订，但审稿人和 AC 不必阅读每版；关键回答应在回复里可直接找到。把日志和内部备注留在提交包外，保留必要限制。

**教学提交检查：代码链接能打开，仍要检查系统里的文件**

**论文原文 · English**

> For implementation details, please refer to our GitHub repository.

**中文翻译 · 本指南翻译**

实现细节请参阅我们的 GitHub 仓库。

**逐句拆解**

1. 原句提供实现入口，但链接本身不能证明匿名权限、文件版本或提交内容已经核对。
2. 教学检查采用“应”与条件句，不编造系统上传或已修改状态，也不将某篇论文的代码公开方式当作所有会议规则。

**教学改写 · English（非论文原文）**

When a venue permits a repository link, verify reviewer access to the exact code snapshot referenced in the submission.
Upload only the manuscript and additional materials allowed by that round’s rules.
Reopen the actual system files and comments before claiming that a change has been submitted.

**教学改写 · 中文（非论文原文）**

会议允许仓库链接时，应核对审稿人能否访问提交材料引用的准确代码快照。
仅上传当轮规则允许的稿件与补充材料。
声称修改已提交前，重新打开系统中的实际文件与评论核对。

**摘录出处：**[Yuqin Dai et al. (AAAI 2026) · Careful Queries, Credible Results: Teaching RAG Models Advanced Web Search Tools with Reinforcement Learning](https://ojs.aaai.org/index.php/AAAI/article/view/40299)；§ Methodology，Learning to Use Advanced Search Tools，最后一句；AAAI 2026 作者终稿；已发表论文；下方教学改写或模拟回复不属于论文原文

**原文／图片许可：**Yuqin Dai et al., AAAI 2026, pp.30458–30466. ©2026 AAAI，保留原版权；作者教学短引，不随本指南转授再版许可。中文为本指南翻译，拆解与教学改写单独标注。

来源与延伸阅读：[写作技能与检查方法](https://github.com/Da1yuqin/PaperBank/blob/main/SOURCES.md#写作技能)；[NeurIPS 2026 · Main Track Handbook V2026.3，Author Responses](https://neurips.cc/Conferences/2026/MainTrackHandbook)；[ICLR 2026 · Author Guide，Discussion Stages](https://iclr.cc/Conferences/2026/AuthorGuide)；[Yuqin Dai et al. (AAAI 2026) · Careful Queries, Credible Results: Teaching RAG Models Advanced Web Search Tools with Reinforcement Learning](https://ojs.aaai.org/index.php/AAAI/article/view/40299)

</details>


</details>


<a id="tools"></a>
## 好用工具：省点手工，判断还得自己来

按用途挑一个先试。只核对公开说明，未逐项安装评测；例子是使用情境，许可和兼容版本看原项目。

核对日期：2026-10-07。

### 任务助手

- **[OpenClaw](https://docs.openclaw.ai/start/getting-started)：**把任务交给可调用工具的助手，在聊天或浏览器控制台中协作。

  <details><summary>中英例子与使用边界</summary>

  **例子：**先让助手只读整理三篇公开论文的题名、方法和出处；确认后再安排后续任务。

  **Example:** Start with a read-only task: list the titles, methods, and sources of three public papers, then decide what to do next.

  **注意：**工具权限与任务范围先配清楚；“只读”提示还应配合实际权限限制。不要把密钥贴进公开对话。

  [官方安全说明](https://docs.openclaw.ai/gateway/security)

  </details>


### 找文献与读原文

- **[AI-Powered Literature Review Skills](https://github.com/stephenlzc/AI-Powered-Literature-Review-Skills)：**按检索、去重、逐篇分析和综合写作组织文献回顾。

  <details><summary>中英例子与使用边界</summary>

  **例子：**限定研究问题、年份和纳入标准，先导出候选文献清单，再人工核对纳入与排除理由。

  **Example:** Specify the research question, date range, and inclusion criteria; export candidate papers and manually check inclusion and exclusion decisions.

  **注意：**README 的验证阶段包含基础元数据检查，不能替代全文核验；检索还取决于数据库访问权限和浏览器环境。

  </details>

- **[沉浸式翻译](https://immersivetranslate.com/zh-Hans/)：**给英文网页和 PDF 加双语对照，保留原文方便逐句核查。

  <details><summary>中英例子与使用边界</summary>

  **例子：**读英文工具文档时打开双语；复制代码和引用时仍使用原始内容。

  **Example:** Use bilingual views to read English documentation; copy code and quotations from the original.

  **注意：**术语、否定和统计结论可能误译，关键内容回原文核对。安装和账户要求看官方文档。

  [官方文档](https://immersivetranslate.com/docs/)

  </details>

- **[Zotero 中文社区插件目录](https://zotero-chinese.com/plugins/)：**按任务找插件，核对 Zotero 版本、更新记录和插件作者。

  <details><summary>中英例子与使用边界</summary>

  **例子：**只想把批注汇成笔记，先挑笔记插件；需要双语 PDF，再看翻译插件。

  **Example:** Choose a note plugin for annotation summaries, and a translation plugin for bilingual PDFs.

  **注意：**社区目录与 Zotero 官方无从属关系；排行榜不是兼容性或安全审计。

  [插件排行榜](https://zotero-chinese.com/plugins/charts)

  </details>

- **[Better Notes](https://github.com/windingwind/zotero-better-notes)：**把 Zotero 批注组织成笔记，连接相关笔记，导出 Markdown 等格式。

  <details><summary>中英例子与使用边界</summary>

  **例子：**建一页“跨被试迁移”笔记，把三篇论文的方法、数据和局限分别链接进去。

  **Example:** Create a cross-subject transfer note and link the methods, data, and limitations of three papers.

  **注意：**Markdown 自动同步是双向的；启用前确认需要同步的文件，保留原始批注。

  </details>

- **[Zotero PDF2zh](https://github.com/guaguastandup/zotero-pdf2zh)：**在 Zotero 内翻译 PDF，查看原文与译文，尽量保留公式和排版。

  <details><summary>中英例子与使用边界</summary>

  **例子：**先译方法节帮助定位，再对照英文核对变量定义、否定句和实验条件。

  **Example:** Translate the method section for navigation, then check definitions, negation, and experimental conditions against the original.

  **注意：**需要插件与翻译服务配合；译文只辅助阅读，关键结论仍回原文核对。

  </details>

- **[Zotero MCP](https://github.com/cookjohn/zotero-mcp)：**让支持 MCP 的 AI 客户端搜索 Zotero 文献、全文、批注和笔记。

  <details><summary>中英例子与使用边界</summary>

  **例子：**提示词：“只读检索我的跨被试论文，列出题名、年份和带出处的关键批注；不要改文献库。”

  **Example:** Read-only: search my cross-subject papers and list titles, years, and key annotations with sources. Do not modify the library.

  **注意：**插件也有写入笔记、标签和元数据的功能；需要只读时明确限制操作。连接云端 AI 后，读取内容可能发给模型服务商。

  </details>


### 写作、排版与汇报

- **[ChineseResearchLaTeX](https://github.com/huangwb8/ChineseResearchLaTeX)：**找中文科研 LaTeX 模板，覆盖标书、论文、学位论文和简历。

  <details><summary>中英例子与使用边界</summary>

  **例子：**选与你的文档类型相符的模板，先用示例内容编译，再迁移自己的正文。

  **Example:** Choose a template for your document type, compile the sample first, then migrate your own text.

  **注意：**模板先与当年的学校、基金或期刊官方要求对照；项目说明要求使用 XeLaTeX。

  </details>

- **[THU-PPT-Theme](https://github.com/atomiechen/THU-PPT-Theme)：**下载简洁的 PPTX 模板，用幻灯片母版统一答辩或组会排版。

  <details><summary>中英例子与使用边界</summary>

  **例子：**选 16:9 白底模板，先统一标题和图注，再放一页问题、一页方法、一页主结果。

  **Example:** Start with a 16:9 white template, then align headings and captions across the problem, method, and main-result slides.

  **注意：**采用 CC BY-NC-SA 4.0，保留署名、遵守非商业与相同方式共享条件；校徽等标识另按其规则使用。

  </details>


### 统计图与框架图

- **[Paper Plot Skills](https://github.com/Trae1ounG/paper-plot-skills)：**用自己的数据生成论文统计图，或把参考图的布局转成 matplotlib 脚本。

  <details><summary>中英例子与使用边界</summary>

  **例子：**给出方法名和准确率，用分组柱状图比较方法；保留数据来源和真实数值。

  **Example:** Provide method names and accuracy values, then compare them in a grouped bar chart with the original data preserved.

  **注意：**参考图用于借鉴表达；不要把复现图当成自己的实验结果。仓库首页未明确展示许可证，复制代码或原图前另查授权。

  </details>

- **[Paper Framework Figure Studio Pro](https://github.com/c-narcissus/paper-framework-figure-studio-pro)：**先核对方法的模块、箭头和变量，再分轮生成框架图候选。

  <details><summary>中英例子与使用边界</summary>

  **例子：**给出方法段落，先列出输入、三个模块和输出，确认数据流后再画图。

  **Example:** Provide the method section, verify its inputs, three modules, and outputs, then draw the confirmed data flow.

  **注意：**当前主线主要面向 ChatGPT 网页端；默认交付候选参考图，可编辑 SVG 或 PPT 通常还需另行重绘。

  </details>

- **[Lieflat Charts](https://github.com/larashero3-dotcom/lieflat-charts)：**把数据做成可交互 HTML 图表，也可生成一页报告。

  <details><summary>中英例子与使用边界</summary>

  **例子：**用公开实验汇总表生成按方法排序的交互柱状图，旁边写清指标、单位和数据出处。

  **Example:** Turn a public experiment table into an interactive bar chart sorted by method, with the metric, unit, and source stated alongside it.

  **注意：**项目采用非商业许可；商业使用需另行取得许可。图表工具不会替你验证输入数据。

  [项目 LICENSE](https://github.com/larashero3-dotcom/lieflat-charts/blob/main/LICENSE)

  </details>


### 引用存在吗，支持这句话吗

- **[Scholar Ref Cleaner](https://github.com/libo-huang/scholar-ref-cleaner)：**将 BibTeX、Word 或文本中的引用与学术数据库元数据比对，生成核验结果。

  <details><summary>中英例子与使用边界</summary>

  **例子：**对公开论文的 refs.bib 做首轮检查，再逐条复核题名、作者、年份、DOI 和出版社页面。

  **Example:** Screen refs.bib from a public paper, then verify titles, authors, years, DOIs, and publisher pages manually.

  **注意：**查无结果可能来自数据库覆盖或网络问题，不能直接判为伪造；元数据匹配也不证明引用支持正文论断。

  </details>

- **[TrueCite](https://www.wispaper.ai/agents/true-cite)：**上传 BibTeX 文件，与学术数据库比对，筛出需要复核的引用。

  <details><summary>中英例子与使用边界</summary>

  **例子：**先拿公开论文的小份 .bib 试用，检查每条异常的数据库来源和原始出版页面。

  **Example:** Try a small .bib from a public paper and inspect the database evidence and publication page for each flagged entry.

  **注意：**页面当前说明只支持 .bib，最大 1 MB；自动标记不是学术不端判定，核查正文论断仍需读原文。

  </details>

- **[ValiRef](https://github.com/Gianthard-cyh/ValiRef)：**从论文 PDF 提取引用，检索多个来源，并借助 LLM 给出核验报告。

  <details><summary>中英例子与使用边界</summary>

  **例子：**用公开 PDF 生成报告，把“论文是否存在”和“是否支持正文这句话”分开复核。

  **Example:** Generate a report for a public PDF, then separately verify paper existence and whether it supports the cited claim.

  **注意：**ruanyf/weekly 的链接是开发者自荐，不是独立评测；LLM 报告可能误判，项目的准确率主张未在这里复测。

  [开发者自荐讨论](https://github.com/ruanyf/weekly/issues/9505)

  </details>

- **[DrClaw · Check Review Alignment](https://github.com/InternScience/DrClaw/blob/main/drclaw/agent_hub/templates/proposal-writing/skills/check-review-alignment/SKILL.md)：**核对综述句子是否真的得到所引论文支持，并记录原句、证据和定位。

  <details><summary>中英例子与使用边界</summary>

  **例子：**正文写“方法 A 在低资源任务更好”，逐条找原文的任务、比较方法和结果；证据不足就记为待人工核验。

  **Example:** For a claim that method A performs better in low-resource tasks, locate the original task, comparison, and result; flag insufficient evidence for manual review.

  **注意：**核对已有引用与正文论断的对应关系；不能保证自动核验无误。排版导出另依赖项目里的综述 skill。

  </details>


### 读代码

- **[DeepWiki](https://deepwiki.com/)：**读公开 GitHub 仓库的架构说明，问具体函数和数据流，再沿源代码链接核对。

  <details><summary>中英例子与使用边界</summary>

  **例子：**提示词：“reward 在哪个函数定义？输入是什么？哪些调用会使用它？给出源文件位置。”

  **Example:** Where is the reward defined, what are its inputs, and which calls use it? Include source-file locations.

  **注意：**先核对索引版本与正在阅读的代码版本；生成文档不能替代源代码或运行结果。未索引的公开仓库可提交仓库 URL。

  [官方说明](https://docs.devin.ai/work-with-devin/deepwiki)

  </details>


### 论文公开与维护

- **[Hugging Face Daily Papers 投稿](https://huggingface.co/papers/submit)：**把已公开的 arXiv 论文提交到 Daily Papers，关联代码、模型、数据集或演示。

  <details><summary>中英例子与使用边界</summary>

  **例子：**准备 arXiv ID、公开项目页和 GitHub 仓库，再按投稿页面当前资格要求提交。

  **Example:** Prepare the arXiv ID, public project page, and GitHub repository, then follow the current submission requirements.

  **注意：**论文被索引、作者认领、进入 Daily Papers 是不同状态；当前资格与时间窗口以投稿页面为准。

  [官方 Paper Pages 说明](https://huggingface.co/docs/hub/paper-pages) · [官方 papers skill](https://github.com/huggingface/skills/blob/main/skills/huggingface-papers/SKILL.md)

  </details>

- **[Hugging Face 作者认领](https://huggingface.co/docs/hub/paper-pages#claiming-authorship-to-a-paper)：**打开自己的 Paper Page，点击自己的作者姓名，再选择 claim authorship 并等待验证。

  <details><summary>中英例子与使用边界</summary>

  **例子：**认领通过后，在 Papers 设置里选择是否展示在个人主页；公开链接只放论文页。

  **Example:** After verification, choose whether to show the paper on your profile; share the public paper page.

  **注意：**只认领自己署名的论文；把公开论文页用于分享，个人认领流程留在账号内。

  [Papers 设置](https://huggingface.co/settings/papers)

  </details>

- **[Hugging Face Daily Papers 历史页面](https://huggingface.co/papers)：**按日期浏览社区论文，检查自己的公开 Paper Page 和关联项目入口。

  <details><summary>中英例子与使用边界</summary>

  **例子：**打开指定日期页查论文是否出现，再进入论文页核对作者、摘要和项目链接。

  **Example:** Open a dated feed to check whether a paper appears, then verify its authors, abstract, and project links.

  **注意：**出现在日期页不代表会议接收、同行评审或结果复现；该链接是历史示例。

  [2026-02-06 示例页面](https://huggingface.co/papers/date/2026-02-06)

  </details>


### 待探索与社区补充

- **[Edit Banana](https://github.com/BIT-DataLab/Edit-Banana)：**把静态示意图转换成可编辑的 DrawIO 元素。

  <details><summary>中英例子与使用边界</summary>

  **例子：**用自己有权处理的流程图测试转换，逐一核对箭头、文字和公式，再调整布局。

  **Example:** Test a flowchart you are authorized to process, check each arrow, label, and formula, then adjust the layout.

  **注意：**项目说明线上服务与仓库功能可能不同。README 写 Apache 2.0，LICENSE 文件实际为 AGPL-3.0；复用或部署前先确认许可。

  [项目 LICENSE](https://github.com/BIT-DataLab/Edit-Banana/blob/main/LICENSE)

  </details>

- **[PDF Cut White](https://github.com/FFengIll/pdf-cut-white)：**裁剪 PDF 图表周围的白边，输出新的 PDF。

  <details><summary>中英例子与使用边界</summary>

  **例子：**把单页图表 input.pdf 裁成 output.pdf，随后检查轴标签、图例和误差线是否完整。

  **Example:** Crop a single-page figure from input.pdf into output.pdf, then check that axis labels, legends, and error bars remain intact.

  **注意：**README 说明默认只处理 PDF 第一页；保留原件，并为输出使用不同文件或目录。仓库首页未明确展示许可证，复制代码前另查授权。

  </details>

- **[科研 Skills 社区介绍 · 卡尔的AI沃茨](https://zhuanlan.zhihu.com/p/2063654777473569661)：**看看九类科研 skill 的使用介绍，用来找候选，再回项目原文核对。

  <details><summary>中英例子与使用边界</summary>

  **例子：**先按“读文献”或“画图”选候选，再用一篇公开论文或一份样例数据试用。

  **Example:** Choose a candidate for reading or plotting, then try it with a public paper or sample dataset.

  **注意：**作者的体验与排名是社区观点，不是统一条件下的基准测试，也不替项目做许可或安全保证。

  </details>


<a id="code-release-prompt"></a>
### 开源整理：翻译注释，清掉私货，保留行为

先写清允许处理的文件。中文界面、接口字符串、业务路径也可能影响运行，不能一键全换。

**中文提示词**

```text
只处理我指定的文件：<文件或目录>。
把中文注释、文档字符串和使用说明译成英文，保留解释代码所需的注释，删除版本更改流水账。把注释和文档中的个人信息、内部地址、机器绝对路径改成通用说明、相对路径和可运行的例子。保留必要的作者署名、引用与许可证信息。
保持算法、控制流程、变量名、接口、参数和数据不变。不要自行翻译程序输出、异常消息、协议字段或其他可执行字符串；若文档字符串被程序读取，也先报告影响。
疑似密钥、私有数据或运行时配置不要贴出原值。列出文件位置和处理建议；若替换会影响行为，先停在该处，说明需要什么决定。去秘检查也覆盖计划发布的样例、配置、日志和压缩包；若还发布 Git 历史，另查历史内容。
示例：文档中的机器路径改为 data/example.json，并说明从项目入口定位；只改说明，不改程序的路径解析逻辑。密钥示例使用 YOUR_API_KEY，不写真实值。
交付修改差异、处理过的内容类型、未解决项和实际验证结果。没有跑过的检查不要说通过；发现真实秘密时不要发布，先报告位置和处置需求。
```

**English prompt**

```text
Work only on the files I specify: <files or directory>.
Translate Chinese comments, docstrings, and usage documentation into English. Keep comments needed to understand the code and remove version-change notes. Replace personal information, internal addresses, and machine-specific absolute paths in comments and documentation with general instructions, relative paths, and runnable examples. Preserve required attribution, citations, and license notices.
Preserve algorithms, control flow, variable names, interfaces, parameters, and data. Do not automatically translate program output, error messages, protocol fields, or other executable strings. Report the impact first if a docstring is read by the program.
Do not quote the original values of suspected credentials, private data, or runtime configuration. Report their file locations and proposed treatment. If substitution would affect behavior, stop at that location and explain the decision needed. Check examples, configurations, logs, and archives intended for release; check Git history separately if it will also be published.
Example: replace a machine-specific path in documentation with data/example.json and explain that it is resolved from the project entry point. Change the explanation, not the program's path-resolution logic. Use YOUR_API_KEY in credential examples, never a real value.
Deliver the diff, the types of content handled, unresolved items, and the checks actually performed. Do not claim an unperformed check passed. If real secrets are found, do not publish them; report their locations and the required treatment.
```

## 参考阅读

- [Mensh & Kording (2017) · Ten simple rules for structuring papers](https://doi.org/10.1371/journal.pcbi.1005619)：中心贡献、读者视角与文章/段落结构；写法需要按研究取舍。
- [Rougier et al. (2014) · Ten Simple Rules for Better Figures](https://doi.org/10.1371/journal.pcbi.1003833)：根据读者与主要信息选择图型，检查布局、颜色及说明。
- [Henderson & Chambers (2022) · Ten simple rules for writing a Registered Report](https://doi.org/10.1371/journal.pcbi.1010571)：研究问题、适用时的假设与预先规划；不要求所有论文写 RQ1/H1。
- [NeurIPS · Paper Checklist](https://neurips.cc/public/guides/PaperChecklist)：主张、限制、设置、统计不确定性与复现；提交时以当年指南为准。
- [ACL Rolling Review · Responsible NLP Research](https://aclrollingreview.org/responsibleNLPresearch/)：NLP 研究责任与披露要求；其他领域检查自己的投稿政策。
- [Liu et al. (2024) · Lost in the Middle, Figure 1 / §2](https://aclanthology.org/2024.tacl-1.9/)：证据位置与问答表现的控制实验，适合学习“现象—诊断”的论证。
- [TCOD (2026 预印本) · Figure 1](https://arxiv.org/pdf/2604.24005v3)：多轮监督案例与课程设计并排呈现；概念图本身不证明效果。
- [Reinforcing Real-world Service Agents (2026 预印本) · Figure 1](https://arxiv.org/html/2602.22697v1#S4.F1)：交互环境、轨迹、学习信号与更新对象的框架图；模拟表现不等于真实部署收益。
- [NeurIPS 2026 · Main Track Handbook V2026.3，Author Responses](https://neurips.cc/Conferences/2026/MainTrackHandbook)：2026 主会回复流程、匿名、篇幅与新结果要求；其他年份和赛道另查指南。核查日期：2026-10-07。
- [ICLR 2026 · Author Guide，Discussion Stages](https://iclr.cc/Conferences/2026/AuthorGuide)：2026 讨论期修订与变更说明；审稿人和 AC 不必阅读每一版。实际投稿遵循当轮最新通知。核查日期：2026-10-07。
- [ACL Rolling Review · Authors Guidelines，Author response](https://aclrollingreview.org/authors#author-response)：截至 2026-10-07 可见的作者回复指南；页面注明此版适用至 2026 年 8 月轮次，后续轮次需重查。用于了解 ARR 与直接投会议的区别，不作后续轮次规则保证。
- [Yuqin Dai et al. (AAAI 2025) · Harmonious Music-driven Group Choreography with Trajectory-Controllable Diffusion](https://ojs.aaai.org/index.php/AAAI/article/view/32268)：论文作者在本指南中用少量原文短引讲解贡献、动机、方法与实验，逐项标明节名、页码和中文翻译；英文引句保持原貌，教学改写单独标注。TCDiff 的数据、性能与结论仅限论文报告的任务与比较条件。
- [Yuqin Dai et al. (AAAI 2026) · Careful Queries, Credible Results: Teaching RAG Models Advanced Web Search Tools with Reinforcement Learning](https://ojs.aaai.org/index.php/AAAI/article/view/40299)：AAAI 2026 正式发表；作者终稿短引，讲解问题、搜索操作、奖励、指标与消融。保留 AAAI 原版权。
- [Pengyu Zeng et al. (EMNLP 2025) · CARD: Cross-modal Agent Framework for Generative and Editable Residential Design](https://aclanthology.org/2025.emnlp-main.473/)：EMNLP 2025 正式发表；模块输入输出、公平比较、人评重复与表示转换。原文 CC BY 4.0，中文为本指南翻译。
- [Zeng, Dai et al. (2026 预印本) · PlanCraft: Sketch, Refine, and Furnish for Architect-Inspired Progressive 3D Residential Scene Generation](https://arxiv.org/abs/2607.23491v3)：摘录公开预印本中的短句与标题，分析渐进设计、方法总览、模块机制、结果段及 Fig.2 流程。英文、翻译和教学改写分开标注；结论限原文比较设置。
- [Chaoyang Shi, Yuqin Dai et al. · UrbanZero（公开项目介绍）](https://github.com/Da1yuqin/Da1yuqin.github.io/blob/main/_pages/includes/pub.md#L193-L202)：依据公开项目介绍编写双语教学示例，讲解任务编译、逐块规划与程序反馈；教学实验和模拟回复不代表论文原文或实测结果。
- [Ling Shi, Yuqin Dai et al. · SAGE: An Extensible Benchmark for Service Agent Graph-guided Evaluation](https://arxiv.org/abs/2604.09285)：用不同短引讲解术语、指标、比较对象、相关工作、全文论证、案例版式及事实澄清；不复制私有评审材料。模拟回复明确不属于实际 rebuttal。
- [Yuqin Dai et al. · EviNoteRAG: Enhancing RAG Models via Quality-Augmented Evidence Notes](https://arxiv.org/abs/2509.00877)：用八处不同短引讲解摘要核对、背景取舍、近邻比较、引文用途、给 AI 的真实材料、润色边界和逐点回复。数值只对应终稿表中实际比较；模拟回复并非真实评审记录。
- [Pengyu Zeng et al. (CVPR Findings 2026) · GreenPlanner: Practical Floorplan Layout Generation via an Energy-Aware and Function-Feasible Generative Framework](https://openaccess.thecvf.com/content/CVPR2026F/html/Zeng_GreenPlanner_Practical_Floorplan_Layout_Generation_via_an_Energy-Aware_and_Function-Feasible_CVPRF_2026_paper.html)：署名原文短引、中文翻译与写作拆解。数据合规、生成结果与不同输入设置分开；不将论文中的法规设置推广为一般建筑指导。
- [Yuqin Dai et al. (IJCV 2026；引文为 arXiv v4) · TCDiff++: An End-to-end Trajectory-Controllable Diffusion Model for Harmonious Music-Driven Group Choreography](https://link.springer.com/article/10.1007/s11263-025-02611-3)：说明模块命名、实验设置、问题与对应设计、收益与代价、未实现能力的边界；仅使用署名短引，不复制期刊原图或全文。
- [Jiaqi Wang et al. · TCOD (arXiv v3)](https://arxiv.org/abs/2604.24005v3)：多轮智能体蒸馏；图2说明如何把训练诊断组织成一条论证。公开预印本，CC BY 4.0。
- [Ning Gao et al. · Reinforcing Real-world Service Agents (arXiv v1)](https://arxiv.org/abs/2602.22697v1)：服务智能体的质量与成本；图2/3和附录案例用于讲解编码、动态和排版。公开预印本，CC BY 4.0。
- [OneReason Technical Report · Figure 12](https://arxiv.org/pdf/2606.06260v1#page=34)：训练策略对照图；仅链接分析，不转载原图。arXiv 分发许可不等于图片复用许可。
