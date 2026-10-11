# PaperBank

: 存入你的时间，取出你的 Accept


这里有三个可以直接使用的 skill，按任务下载。
[cs-paper-writing](../assets/cs-paper-writing-skill.zip) · [绘图](../assets/paperbank-figures-skill.zip) · [rebuttal](../assets/rebuttal-skill.zip) · [用法](#writing-skill)

![大字红色 accept 和庆祝彩带下，边牧、魔法橘猫和龙收到论文录用邮件，开心举起爪子。](../assets/paperbank-accept-team.png)

## 写在前头

本指南用于学术讨论，整理本人在论文写作与修改中的经验，供研究者参考。本人并非领域权威，内容可能有误。

网页开源并支持批注。欢迎指出错误、讨论具体写法，我会根据反馈修订。

*多数例子来自本人、本人参与或熟人的论文，另选少量具有参考价值的公开论文。各例均附出处；如用于研究，请引用对应原论文。*


先用 Codex 起草正文与关键图，再由作者审核逻辑、逐章精修。第四章为审稿回复，第五章为辅助工具。

主要面向方法与实证研究；按学科、研究类型和投稿要求调整。模拟段落明确标注，真实论文摘录另给出处与版本。

欢迎使用、改写、转载，也欢迎给 Codex 用作 skill。原创内容采用 CC BY 4.0，论文摘录与图片保留各自许可。转载原创内容请保留作者 Da1yuqin、[原文链接](https://Da1yuqin.github.io/PaperBank/)和 [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) 许可，修改版本注明改动。如有帮助，欢迎 Star。

<a id="quick-start"></a>
## 1. 初稿准备

整理材料，先做关键图，再组织正文与实验。用中文审核逻辑后，精修英文。

<a id="draft-step-1"></a>
### 1.1 研究材料与模板

先整理研究问题、已有局限、对应设计和真实结果，附上可核对的文献、图与数据。下载目标会议当年的官方模板，确认页数并编译。使用 Overleaf 时，将最新源文件同步到本地；Git 同步需要项目 owner 有会员或相应权限，没有则下载源文件 ZIP、本地编译，或跳过同步。写明允许修改的文件，再把材料填入提示词，让 Codex 先形成提纲和初稿。

**填写研究材料，生成初稿**

```text
读取 cs-paper-writing/SKILL.md、references/checklist.md；绘图同时读 paperbank-figures/SKILL.md。先形成初稿，再由我审中文逻辑。本提示词用于实证型 CS 论文，Nature 系列另用独立体系。
使用前：核对目标会议及 track 的 AI 规定，只在允许范围内起草、改写或绘图，按要求披露。确认材料使用权限和工具的数据处理方式；未获许可，不向外部服务上传未公开稿件、review、个人数据或密钥。
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
Intro 结构：前两个自然段可调整顺序和分工，交代领域背景与回顾，并比较相关工作的能力、差异和不足；可合并或拆分，不固定“第一段背景、第二段局限”。
```

依据：cs-paper-writing · paper-writing-clarity · cs-writing-skill · paper-visual-standards · [对应铁律与完整提示词](https://github.com/Da1yuqin/PaperBank/blob/main/skills/cs-paper-writing/references/prompts.md#draft)

<a id="draft-step-2"></a>
### 1.2 关键图绘制

先完成关键图，供合作者审核研究思路。mainfig 用一个问题或发现说明研究价值；framework 展示真实流程，每步写清输入、操作、输出，箭头连到实际接收者，仅供评价的规则不进入被测模型。结果图从真实数据绘制，轴、单位、比较条件和误差含义齐全。全篇名称、配色和字体统一；按最终栏宽设计，图内字控制在正文减 2 pt 至正文之间，放不下就重排。编译后按正常阅读大小检查，不用放大的截图验收。

<a id="visual-lost-middle-fig-1"></a>
#### 单栏首图：研究动机

![单栏首图：研究动机](../assets/paper-lost-middle-fig-1.png)

这张单栏图只问一件事：答案所在文档的位置，会不会影响问答准确率？横轴是答案文档在 20 篇输入文档中的位置，纵轴是 GPT-3.5-Turbo 的准确率。紫线是带文档问答，红虚线是同一模型不读文档时的准确率。中间位置更低，开头和结尾更高；读者先记住这个发现，再去正文看实验。

1. **横轴与纵轴：**横轴是答案文档在20篇输入文档中的位置，纵轴是问答准确率；两个量足以提出一个研究问题。

2. **紫线与红虚线：**紫线显示带文档问答，红虚线给出同一模型的无文档基准；对照说明中间位置的低谷为什么值得研究。

3. **图例与结论范围：**图例写明模型和条件。结论限于该模型与20文档设置；纵轴未从零开始，不能按曲线高度比较倍数。

[Liu et al. · Lost in the Middle (TACL 2024), Fig. 1, p. 158 / PDF p. 2](https://aclanthology.org/2024.tacl-1.9/)

Nelson F. Liu et al., Lost in the Middle: How Language Models Use Long Contexts, TACL 12 (2024), Fig. 1, p. 158. CC BY 4.0. 从正式 PDF 提取图面；图形、坐标、文字和图例未改。

<a id="visual-interactcs-fig-1"></a>
#### 框架层级与模块编号

![框架层级与模块编号](../assets/paper-interactcs-fig-1.png)

先分交互生成和策略优化两块，再编号结果、过程、成本三种信号；旁边的对话走一遍流程。

1. **左侧输入分组：**用户特征、外部需求与业务场景先分组，读者知道交互由什么输入产生。

2. **中间对话：**一个对话实例沿流程展开，连接抽象模块与实际交互；自己的案例须先处理身份信息。

3. **右侧编号模块：**结果、过程、成本三种信号分别编号。分组讲职责，箭头讲信息流，编号讲处理步骤。

4. **右上评分输出：**Task Score、Turn Credit和Global Cost并排显示，输入、回复与评分信号各有位置，避免混成一类。

[Reinforcing Real-world Service Agents: Balancing Utility and Cost in Task-oriented Dialogue · arXiv:2602.22697v1, Fig. 1, PDF p. 4](https://arxiv.org/abs/2602.22697v1)

Ning Gao et al., Reinforcing Real-world Service Agents, arXiv:2602.22697v1, Fig. 1. CC BY 4.0. 从原页裁切；图形与数据未改。

<a id="draft-step-3"></a>
### 1.3 正文结构与实验

- 先列全部章节标题、每节目的、所需图表及预计篇幅；按任务归类同级内容。
- Method 按实际依赖组织。Overview 概括完整流程，各小节写清输入、操作、输出和交接。
- 实验按待检验主张组织：主结果看整体表现，消融查设计作用，分析解释差异与失败。
- 各章开头接回前文的问题；结果段先给具体发现，再说明它怎样回应引言的动机。
- 表格按可比条件分组，写清指标方向和不确定性；逐列标最优、次优，长表先拆列或跨栏。

<a id="draft-paper-outline"></a>
#### 论文大纲与章节衔接

教学大纲，示例任务是评价对话回复怎样处理变化的需求与未决条件。章节名称和数量按实际研究调整；箭头说明承接关系。

Abstract 概括同一组问题、局限、设计与发现；正文结果确定后再压缩。

**1 Introduction**

交代已有能力与研究问题；指出需求时效和未知保留的评价缺口，再给对应设计与主要发现。

↓ 这些缺口的比较依据是什么？

**2 Related Work**

按任务或机制比较已有路线。末尾用 However 点名同一缺口，紧接本文的对应解法。

↓ 为评价这两个问题，方法需要哪些输入与判据？

**3 Method**

Overview 先概括全章：整理保留需求变化的对话案例，再制定逐案例判据，最后运行模型并评价回复。

↓ 概括各小节的职责与交接

3.1 Task Formulation：定义输入、回复与评价单位；区分给模型的案例和只给评价器的判据。

- **3.2 Case Construction**：对话记录与时间信息 → 筛选并保留需求变化和未决条件 → 可评价的对话案例

- **3.3 Criterion Construction**：对话案例与对应材料 → 定义回复需满足的条件及应保留的未知 → 逐案例评价判据

- **3.4 Evaluation Protocol**：案例、模型回复与评价判据 → 模型按案例作答；评价器按判据评分 → 可比较的分数与错误记录

案例 → 被测模型 → 回复；回复 + 评价判据 → 评价器 → 分数与错误。判据只用于评分。

↓ 这些设计是否回答了引言提出的问题？

**4 Experiments**

4.1 Setup 定义比较条件和指标；4.2 Main Results 回答研究问题；4.3 Ablation 检验设计作用；4.4 Analysis 解释差异并回扣原局限。

↓ 这些结果能说明什么，还不能说明什么？

**5 Discussion and Limitations**

解释发现与剩余限制；区分前人不足和本文未覆盖的范围。

↓ 在已测试范围内，开头的问题得到什么答案？

**6 Conclusion**

概括已验证的产物与发现，回答研究问题；不新增设计、结果或适用范围。

References 为比较与判断提供依据；Appendix 放可复核设置、完整判据和补充实验。

排版示例：以下数值均为假设，不是论文结果。上标演示均值旁的标准差；浅红为最优，浅蓝为次优。

| Method | Success (%) ↑ | Latency (ms) ↓ |
| --- | --- | --- |
| Baseline A | 70.0 ±2.0 | 120 ±4 |
| Baseline B | 73.0 ±1.0 | 130 ±4 |
| Proposed method | 76.0 ±1.0 | 125 ±3 |

**LaTeX 表格模板**

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

<a id="writing-skill"></a>
### 三个独立 skill

正文起草、章节模板、实验组织与语言精修。

[cs-paper-writing ZIP](../assets/cs-paper-writing-skill.zip) · [SKILL.md](../skills/cs-paper-writing/SKILL.md)：正文起草、章节模板、实验组织与语言精修。

[绘图 ZIP](../assets/paperbank-figures-skill.zip) · [SKILL.md](../skills/paperbank-figures/SKILL.md)：解压后让 Codex 读取整个 paperbank-figures/ 文件夹，并提供稿件、原始数据、参考图及允许修改的文件。

[rebuttal ZIP](../assets/rebuttal-skill.zip) · [SKILL.md](../skills/rebuttal/SKILL.md)：逐题回应、证据核对、revise loop 与 AC 总结。

下载所需 ZIP，解压并保留完整文件夹，让 Codex 读取其中的 SKILL.md。填入材料、任务和允许修改的范围；需要写作和绘图时同时读取两个 skill。

**中文使用提示词**

```text
读取 cs-paper-writing/SKILL.md 和 references/checklist.md，按当前任务选规则。
使用前：核对目标会议及 track 的 AI 规定，只在允许范围内起草、改写或绘图，按要求披露。确认材料使用权限和工具的数据处理方式；未获许可，不向外部服务上传未公开稿件、review、个人数据或密钥。
任务：【起草／精修哪节／只读检查】；目标会议与限制：【】
材料：【最新稿件、真实结果、参考原文】；允许修改：【文件与范围】

铁律：
1. 先查“具体不足→新增设计→实际证据”。Abstract、Intro 贡献和 Method Overview 明说新对象或设计及其价值，与最近工作比较；全篇困难、模块和发现名称一致。不猜技术设定，不编引用、数字或优先权。
2. 一句一个完整判断，一段一个任务，后句接前句对象、问题或产物。正文不用 it／they 及同族代词，we／our 和 this + 明确名词可保留。用短对象名，不以符号替代句子，不使用重复修饰；有依据的贡献词一词换一词。
3. 缩写、符号首次出现定义对象、来源、单位与下标；摘要、引言、实验各自能读懂。按最终 PDF 检查句长，双栏一句默认最多三行、单栏一句默认一行半，完整语义优先；不用缩字、改栏宽或硬换行凑行数。
4. Related Work 按主题写已有路线、能力、具体不足和本文方案；However 与 To address 的对象、关键词对齐 Intro，按类别概括文献，仅引用直接相关的工作。Method Overview 先讲设计为什么回应困难，再写目的、操作、产物；用 in [准确章节名] (ref) 定位，每个章节名与引用出现一次，保留并行关系，末句引 framework。
5. 实验段先给有证据的结论，再讲比较条件、关键对照与含义；消融固定其他条件。指标说明方向、分母和不确定性，区分记录与独立样本、百分比与百分点、观察与因果；保留影响解释的负结果。RQ 按需要使用。
6. 数据、公式含义、实验设置、引文、原始 prompt 和模型回复不因润色改变；保留他人修改。先给中文逻辑与最小改法，确认后改英文。缺证据单列给我，不写入论文正文；只读任务不写文件。最后说明实际改动和检查，编译与最终 PDF 目检分别确认。
语言要求：专业、简洁、直白；不添加调侃、比喻或空泛修饰。
Intro 结构：前两个自然段可调整顺序和分工，交代领域背景与回顾，并比较相关工作的能力、差异和不足；可合并或拆分，不固定“第一段背景、第二段局限”。
```

依据：cs-paper-writing · paper-writing-clarity · cs-writing-skill · [对应铁律与完整提示词](https://github.com/Da1yuqin/PaperBank/blob/main/skills/cs-paper-writing/references/prompts.md#writing)

<a id="figures"></a>
## 2. 论文绘图

按图的任务选择结构，结合原图理解绘图规范。

<a id="figure-skill"></a>
### 2.1 绘图准备

[下载绘图 skill](../assets/paperbank-figures-skill.zip)

以下是 PaperBank 面向 CS 论文的默认约定，会议硬性要求和当前稿件已确认的配置优先。参考图用来学信息组织，不照搬它的字号、色板或数据。

**填写绘图任务与数据**

```text
读取 paperbank-figures/SKILL.md 和 references/rules.md。按以下材料画图。
使用前：核对目标会议及 track 的 AI 规定，只在允许范围内起草、改写或绘图，按要求披露。确认材料使用权限和工具的数据处理方式；未获许可，不向外部服务上传未公开稿件、review、个人数据或密钥。
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

依据：paper-visual-standards · academic-plotting · clean-flow-figures · [对应铁律与完整提示词](https://github.com/Da1yuqin/PaperBank/blob/main/skills/paperbank-figures/references/prompts.md#figures)

<a id="figure-rules"></a>
### 2.2 绘图规范

- **每图明确一个主要任务：**mainfig 展示研究动机与观察，framework 说明设计如何对应问题，结果图提供验证证据。每图明确一个主要任务。

[图例与批注：单栏首图：研究动机](#visual-lost-middle-fig-1)

- **绘图先于正文精修：**先完成可供合作者审核的框架图与实验图，再精修正文。图未能体现贡献时，先调整内容与布局，再修改配色。

[图例与批注：训练范围对照](#visual-tcod-fig-3)

- **统计图使用真实数据：**统计图用 Python 从真实数据绘制；imagegen 用于动机、框架和案例图。缺数据就停，不补点、不编误差、不为平滑改曲线。

[图例与批注：框架层级与模块编号](#visual-interactcs-fig-1)

[图例与批注：KDE 密度分布](#teaching-kde)

- **按最终尺寸检查字号：**按最终栏宽排字，字体与正文一致；所有图内字同一字号，介于正文与正文减 2 pt 之间，标题也不能更大。放不下先重排，不缩小规定字号。

[图例与批注：训练范围对照](#visual-tcod-fig-3)

- **箭头表示真实依赖：**同层成组并命名；先后、并行、汇合、反馈按真实依赖画。每条箭头说清传什么，起止明确，避免穿过文字与无必要的迂回。

[图例与批注：框架层级与模块编号](#visual-interactcs-fig-1)

- **区分输入与评价信息：**输入、输出、评价规则用三种边框区分，并给图例。只供评价的 rubric 不连到被测模型；不同模型收到不同材料，也要标清。

[图例与批注：框架层级与模块编号](#visual-interactcs-fig-1)

- **低饱和配色与清晰对比：**常规模块用中性灰，关键改动用统一强调色。低饱和配色须保持清晰对比。

[图例与批注：消融结果](#visual-interactcs-fig-2)

- **对话按轮次与语义分段：**一轮一框，注明角色；同一轮长回复按语义分段，不伪装成多轮。高亮只标关键约束、证据或错误，颜色含义要能读懂。

[图例与批注：交互案例](#fig-interactcs-case)

- **同一案例仅完整呈现一次：**同一来源的案例在全文只完整呈现一次，其他位置交叉引用。改名、翻译、裁剪也算同一个；必要对照集中展示，单个案例不能证明总体效果。

[图例与批注：交互案例](#fig-interactcs-case)

- **同类子图使用一致尺度：**围绕一个问题排现象、诊断、对照和稳健性；同条件同顺序、同配色，同类轴和色标保持可比。

[图例与批注：多面板诊断](#visual-tcod-fig-2)

- **准确呈现坐标与差异：**查单位、分母、方向、坐标起点和误差类型；截断坐标要明确标出。相对增益同时给绝对值，柱长和数值必须对应。

[图例与批注：配对增益](#teaching-paired-gain)

- **Caption 说明读法与发现：**图注先说读法和发现，再点出与贡献的关系；图中的简称在 Caption 给全称。结论须有证据支持；“效果显著”须有对应统计检验。

[图例与批注：置信区间与误差带](#teaching-confidence)

- **编译后检查最终页面：**放回论文检查实际字号、字体嵌入、可选文字、裁切、碰撞、图注总高度和首次引用顺序。源码字号正确，不代表插入后仍正确。

[图例与批注：问题与解法对照](#visual-tcod-fig-1)

- **明确模块输入与输出：**每个关键模块写清收到什么、做什么、交出什么，以及交给谁。模块名与 Method 一致，所有缩写就近解释。

[图例与批注：框架层级与模块编号](#visual-interactcs-fig-1)

- **解释图中所有标记：**图标旁写对象名；新缩写、符号、边框、线型和数字就近解释。读者只看图与图注，应知道每个标记指什么。

[图例与批注：框架层级与模块编号](#visual-interactcs-fig-1)

- **Framework 展示操作与产物：**“结合 case 去绘制你的流程” 展示一个真实输入怎样变成中间产物和输出，旁边点出设计解决的困难。节点多不等于贡献多。

[图例与批注：交互案例](#fig-interactcs-case)

[图例与批注：框架层级与模块编号](#visual-interactcs-fig-1)

- **区分示意与实测：**估计、作者示例和实测输出分清；可选路径不能画成必经步骤。框的面积、线宽和箭头不能暗示没有证据的比例或因果，图形本身须准确，不能仅靠图注纠正。

[图例与批注：成本与性能](#teaching-cost)

- **准确区分矢量与位图：**统计图导出矢量 PDF 并嵌入字体。生成底图上的标签另排原生、可见、可选的 PDF 文字；不留重叠字形，不加隐藏 OCR 层。混合 PDF 仍含位图。

[图例与批注：训练范围对照](#visual-tcod-fig-3)

- **保持修改范围：**只改配色就保留布局、文字、换行、字号、公式、照片和连线；重排须在约定范围内。保留数据、实验和合作者的图。

[图例与批注：消融结果](#visual-interactcs-fig-2)

- **按模板宽度布局：**按实际栏宽起稿，不改页边距、正文字号或页面方向。正文通栏约 16:9、单栏约 4:3 是起点，附录可纵排；不进行非等比缩放。CS 默认用 [!t]，再按正文首次引用检查实际落点。

[图例与批注：问题与解法对照](#visual-tcod-fig-1)

- **表格用于结果与数据：**PaperBank 默认表格只放真实结果或数据。术语、方法、实验计划和案例点评写正文，不能通过截图规避该规则；统计数字也不能把说明表变成实验结果。

[图例与批注：消融结果](#visual-interactcs-fig-2)

- **重排文字与图形重叠处：**图例、标题、刻度和注释不能挡数据、箭头或边框。为文字保留空间，通过重排解决重叠，不能用遮盖隐藏问题。

[图例与批注：KDE 密度分布](#teaching-kde)

<a id="figure-types"></a>
### 2.3 图型选择

- **摘要图：**方法型画问题、旧做法和本文改动；发现型展示一个关键观察。通常最多 5 个环节，保留必要对照。

[图例与批注：单栏首图：研究动机](#visual-lost-middle-fig-1)

- **框架图：**输入是什么，经过哪几个模块，每步产物交给谁，输出是什么。旁边走一个可追踪例子。

[图例与批注：框架层级与模块编号](#visual-interactcs-fig-1)

- **案例图：**“不同highlight颜色表示不同类型的信息” 白底保留必要背景、需求、证据、动作与结果；输入、模型输出、judge 用可解释边框，位置表示真实层级。

[图例与批注：交互案例](#fig-interactcs-case)

- **主结果与消融：**少量方法用点图或柱图；完整方法与删组件版本同顺序、同配色。说明误差的统计单位和计算方法。

[图例与批注：消融结果](#visual-interactcs-fig-2)

- **配对增益：**同一样本的干预与对照，画差值和零线；写清收益方向与尺度。

[图例与批注：配对增益](#teaching-paired-gain)

- **训练或轮次动态：**折线只连有序变量；横轴写训练步数或轮次，不把无序方法连成趋势。

[图例与批注：训练动态](#visual-interactcs-fig-3)

- **KDE：看分布形状：**横轴是变量，纵轴是密度；颜色跟组走，均值线补位置，交代样本量和带宽。峰高不是人数，也不是累计比例。

[图例与批注：KDE 密度分布](#teaching-kde)

- **ECDF：看阈值以下有多少：**横轴取阈值，纵轴直接读累计比例；同一坐标比两组，阶梯从 0 到 1。低于某阈值的样本比例应从 ECDF 读取，KDE 峰值不能表示累计比例。

[图例与批注：ECDF 累积分布](#teaching-ecdf)

- **热图：**条件乘方法，统一色标；正负增益以零为中点，缺测留空并说明。

[图例与批注：热图：分组结果](#teaching-heatmap)

- **PCA：把高维关系投到二维：**“利用空间位置关系绑定数据，更换不同的颜色呈现不同属性” 同时交代特征、标准化与解释方差。分得开不等于泛化好；PaCMAP、t-SNE 不叫 PCA。

[图例与批注：PCA 二维投影](#teaching-pca)

- **雷达图：多指标逐轴读：**每轴一个指标，写尺度、归一化和好坏方向；颜色再配点形。不同量纲不能用面积直接比较，轴顺序也会改变面积。

[图例与批注：雷达图：多指标比较](#teaching-radar)

- **成本性能图：**每点是一个实际配置；在线与离线成本分开，写单位和好坏方向。连接前沿不意味着有中间配置。

[图例与批注：成本与性能](#teaching-cost)

- **数据集分布：**先写清统计单位、样本量、类别与分母。同一图不能混用案例数、回复数与判据数；说明类别覆盖范围与占比。

[图例与批注：环图：组成比例](#teaching-donut)

- **置信带：**按实际重采样或模型计算区间，写清区间类型和置信水平。同一估计的嵌套区间才可比较覆盖范围；不同样本量、方差也会改变带宽。

[图例与批注：置信区间与误差带](#teaching-confidence)

- **饼图、环图与圆环排名：**饼图只画互斥且组成整体的比例；圆环柱图可画排名，极值相邻只是环形排序，不是变量关系。要读精确差值，横向条图更方便。

[图例与批注：环图：组成比例](#teaching-donut)

- **二维增益与九宫格：**“可以用这种九宫格来分类，好处是可以看出两个渐进的变化” 两轴写指标、单位和好坏方向；差值图以零线分区，不为填满网格补造数据。

[图例与批注：双指标增益](#teaching-two-gain)

<a id="notion-gallery"></a>
<a id="figure-gallery"></a>
### 2.4 图例与说明

首图与框架图的入门案例见 [1.2 关键图绘制](#draft-step-2)。

#### 动机与框架

<a id="visual-tcod-fig-1"></a>
#### 问题与解法对照

![问题与解法对照](../assets/paper-tcod-fig-1.png)

左边画误差随轮次的示意，中间放大回复细节，右边对照三种训练范围；先看到问题，再看到改哪一步。

1. **左侧问题：**KL随轮次变化的示意先提出问题；这是示意曲线，不能当作实测结果。

2. **中间回复细节：**从完整轨迹放大到两轮回复，文本与数值块放在一起；数值含义须由原图注定义。

3. **右侧训练范围：**三条时间线沿同一方向对照训练范围，读者直接看到改了哪一段；未计算的轮次要解释原因。

[TCOD: Exploring Temporal Curriculum in On-Policy Distillation for Multi-turn Autonomous Agents · arXiv:2604.24005v3, Fig. 1, PDF p. 2](https://arxiv.org/abs/2604.24005v3)

Jiaqi Wang et al., TCOD, arXiv:2604.24005v3, Fig. 1. CC BY 4.0. 从原页裁切；图形与数据未改。

<a id="visual-tcod-fig-3"></a>
#### 训练范围对照

![训练范围对照](../assets/paper-tcod-fig-3.png)

基线和两种课程共用步骤框与师生图标，再沿轮数展开；读者直接看训练覆盖哪一段，不必重读三套流程。

1. **左侧基线：**先展示完整轨迹与师生关系，为后面两种课程提供共同参照。

2. **中间与右侧：**两种课程复用步骤框、师生图标和箭头，只改变训练覆盖位置，便于直接比较。

3. **轮数与颜色：**沿轮数向下读课程变化。步骤颜色、轮数标签和训练目标仍须在图注中定义，图标不能替代解释。

[TCOD: Exploring Temporal Curriculum in On-Policy Distillation for Multi-turn Autonomous Agents · arXiv:2604.24005v3, Fig. 3, PDF p. 5](https://arxiv.org/abs/2604.24005v3)

Jiaqi Wang et al., TCOD, arXiv:2604.24005v3, Fig. 3. CC BY 4.0. 从原页裁切；图形与数据未改。

#### 诊断与训练动态

<a id="visual-tcod-fig-4"></a>
#### 效果与机制曲线

![效果与机制曲线](../assets/paper-tcod-fig-4.png)

成功率和 KL 共用训练步数，效果与诊断可以就近对照；曲线一起变，不等于已经证明因果。

1. **相邻面板：**成功率与KL成对放置，效果与诊断就近对照；一起变化不等于已经证明因果。

2. **共用横轴：**所有面板使用训练步数，可按同一时间点比较；不同指标各用自己的纵轴。

3. **面板图例：**颜色区分训练条件。原图部分图例使用日志简写，自己的论文应换成可直接识别的模型和条件。

[TCOD: Exploring Temporal Curriculum in On-Policy Distillation for Multi-turn Autonomous Agents · arXiv:2604.24005v3, Fig. 4, PDF p. 8](https://arxiv.org/abs/2604.24005v3)

Jiaqi Wang et al., TCOD, arXiv:2604.24005v3, Fig. 4. CC BY 4.0. 从原页裁切；图形与数据未改。

<a id="visual-tcod-fig-5"></a>
#### 辅助指标对照

![辅助指标对照](../assets/paper-tcod-fig-5.png)

轮数、优势、长度、损失各占一格；共用训练步数，不同单位不挤在一根纵轴上。

1. **四个指标面板：**轮数、优势、最大回复长度和损失各占一格，避免不同单位挤在同一纵轴上。

2. **共用训练步数：**横轴一致，读者可在同一训练时刻核对不同过程指标。

3. **损失曲线：**损失下降描述训练过程，不能替代最终任务实验；诊断指标与任务结果要分清。

[TCOD: Exploring Temporal Curriculum in On-Policy Distillation for Multi-turn Autonomous Agents · arXiv:2604.24005v3, Fig. 5, PDF p. 9](https://arxiv.org/abs/2604.24005v3)

Jiaqi Wang et al., TCOD, arXiv:2604.24005v3, Fig. 5. CC BY 4.0. 从原页裁切；图形与数据未改。

<a id="visual-tcod-fig-2"></a>
#### 多面板诊断

![多面板诊断](../assets/paper-tcod-fig2.png)

每个师生组合紧挨着放 Initial／final 两根柱子，颜色区分阶段，柱顶数字省掉来回读轴。

1. **左侧训练诊断：**(a)(b)共用训练步数，把KL变化与成功率放在一起读；这是两种量的对照，不能仅凭曲线认定因果。

2. **中间配对柱图：**每个师生组合把Initial与final紧邻排列，横轴箭头写明配对方向，柱顶数值减少来回查轴。

3. **柱图纵轴：**纵轴从50开始，比较应读数值，不能用柱高判断初始值是最终值的多少倍。

4. **右侧轮次曲线：**按对话轮次展示KL，补充训练步数之外的诊断视角；色带含义应由原图注说明。

[Jiaqi Wang et al. · arXiv:2604.24005v3 · Fig. 2](https://arxiv.org/abs/2604.24005v3)

Jiaqi Wang et al., arXiv:2604.24005v3, Fig. 2. CC BY 4.0. 从原 PDF 裁切；图形与数据未改。

<a id="visual-interactcs-fig-3"></a>
#### 训练动态

![训练动态](../assets/paper-interactcs-fig3.png)

左边画成本，右边画使用率，红蓝固定对应两种目标；共用训练步数，把两条动态放到一起读。

1. **左侧成本与右侧使用率：**控制量与实际行为并排，共用训练步数，便于按同一时间点核对两条动态。

2. **两幅图的红蓝线：**红蓝始终对应20%与30%两种目标，同一条件跨面板保持同色。

3. **半透明色带：**色带显示了额外信息，但图面未说明统计含义；不能自行补成方差、标准误或置信区间。

[Ning Gao et al. · arXiv:2602.22697v1 · Fig. 3](https://arxiv.org/abs/2602.22697v1)

Ning Gao et al., arXiv:2602.22697v1, Fig. 3. CC BY 4.0. 从原 PDF 裁切；图形与数据未改。

#### 消融与资源成本

<a id="visual-tcod-fig-6"></a>
#### 方法效果比较

![方法效果比较](../assets/paper-tcod-fig-6.png)

两个任务各一幅图，方法顺序一致，柱顶给小时数。想讲省算力，就把时间写出来。

1. **两幅任务图：**每个任务各一幅图，方法顺序一致，比较时无需重新找位置。

2. **柱顶数值与单位：**柱顶直接标小时数，纵轴写Time (h)。这是训练耗时，不能当作在线推理延迟；另需交代硬件与训练条件。

3. **柱顶误差线：**误差线保留，但原图未给全其含义，不能自行补成标准差、置信区间或特定重复次数。

[TCOD: Exploring Temporal Curriculum in On-Policy Distillation for Multi-turn Autonomous Agents · arXiv:2604.24005v3, Fig. 6, PDF p. 10](https://arxiv.org/abs/2604.24005v3)

Jiaqi Wang et al., TCOD, arXiv:2604.24005v3, Fig. 6. CC BY 4.0. 从原页裁切；图形与数据未改。

<a id="visual-interactcs-fig-2"></a>
#### 消融结果

![消融结果](../assets/paper-interactcs-fig2.png)

颜色分方法族，实色、斜线和点纹再分组内方案，四个面板共用图例，误差棒也留在柱顶。

1. **顶部共享图例：**颜色区分方法族，实色、斜线和点纹区分组内方案，四个面板复用同一套编码。

2. **指标标题箭头：**↑与↓标出指标的优劣方向，避免把违规率下降读成性能变差。

3. **柱顶误差棒：**保留不确定性信息；图面没有定义误差棒，不能自行称为标准差或置信区间。

4. **前三幅纵轴：**前三幅图未从零开始，不能按柱高比较倍数；应读坐标和数值差异。

[Ning Gao et al. · arXiv:2602.22697v1 · Fig. 2](https://arxiv.org/abs/2602.22697v1)

Ning Gao et al., arXiv:2602.22697v1, Fig. 2. CC BY 4.0. 从原 PDF 裁切；图形与数据未改。

#### 案例

<a id="fig-interactcs-case"></a>
#### 交互案例

![交互案例](../assets/paper-interactcs-case-summary.png)

深色标题交代案例，浅底分栏列出评价和用户设定；完整对话接在后页。

1. **观察 1：**作者笔记强调像UI一样整洁：相同信息放一起，同类信息用同样的框，颜色只强调重点。

2. **观察 2：**左栏是三个评价结果，右栏是用户设定；标题、字段与数值分层，不必为每个字段单独设置对话框。

3. **观察 3：**字多时先分组、删重复、留白。放回双栏PDF后仍须检查字号；网页放大看清不等于论文里看清。

[Ning Gao et al. · Reinforcing Real-world Service Agents (arXiv v1)](https://arxiv.org/abs/2602.22697v1)

Ning Gao et al., Reinforcing Real-world Service Agents, arXiv:2602.22697v1. CC BY 4.0（https://creativecommons.org/licenses/by/4.0/）。从原 PDF 裁切；图形、标签和数据未改。

#### KDE 密度分布

<a id="teaching-kde"></a>
#### KDE 密度分布

![KDE 密度分布](../assets/kde.svg)

同一坐标对照两组模拟分数，曲线越高说明该处更密集；浅色填充只是曲线下面积。

1. **横轴与纵轴：**横轴是模拟分数，纵轴是概率密度；曲线越高，说明附近样本越密集，不是累计比例。

2. **两组曲线与填充：**两组共用坐标，便于比较分布位置；浅色填充是曲线下面积，不是置信区间。

3. **底部计算说明：**每组100个模拟样本，采用高斯核、固定带宽0.4；每条密度曲线的面积约为1。

[可复现教学绘图代码](../assets/generate-statistical-examples.py)

PaperBank 原创教学图 · 模拟数据，非论文结果 · CC BY 4.0

#### ECDF 累计分布

<a id="teaching-ecdf"></a>
#### ECDF 累积分布

![ECDF 累积分布](../assets/ecdf.svg)

阶梯线在每个样本处上升，纵轴是已累计的样本比例；不用把平滑密度误认成覆盖率。

1. **阶梯线：**每个样本使曲线上升，纵轴表示不超过当前横轴值的样本比例。

2. **两组共用坐标：**在同一阈值比较线高，读的是累计比例差，不是该位置的样本密度。

3. **底部样本说明：**与KDE使用同一批模拟样本，每组100个；比例直接由样本计数得到，无需平滑。

[可复现教学绘图代码](../assets/generate-statistical-examples.py)

PaperBank 原创教学图 · 模拟数据，非论文结果 · CC BY 4.0

#### PCA / 空间嵌入

<a id="teaching-pca"></a>
#### PCA 二维投影

![PCA 二维投影](../assets/pca.svg)

两组模拟样本的三个标准化特征投到前两主成分，轴上直接给真实计算的解释方差。

1. **两个主成分轴：**轴上写出计算得到的解释方差：PC1为62.4%，PC2为27.8%，避免只标抽象坐标。

2. **散点颜色：**颜色显示原分组，PCA未使用分组训练；投影分开不等于分类准确或泛化成立。

3. **底部输入说明：**80个模拟样本、3个特征，先中心化并除以样本标准差，再由协方差矩阵求主成分。

[可复现教学绘图代码](../assets/generate-statistical-examples.py)

PaperBank 原创教学图 · 模拟数据，非论文结果 · CC BY 4.0

#### 雷达与多指标

<a id="teaching-radar"></a>
#### 雷达图：多指标比较

![雷达图：多指标比较](../assets/radar.svg)

每根轴都是越高越好的0到1模拟分数，颜色贯穿点和线；逐项比较，比比较整块面积更有意义。

1. **各指标轴：**所有轴统一为0到1，方向统一为越高越好；真实图须先说明归一化方法。

2. **点、线与颜色：**同一组的点与线保持同色，逐轴比较各项表现。

3. **填充多边形：**图中未定义综合分数，多边形面积不能当作经过验证的总能力。

[可复现教学绘图代码](../assets/generate-statistical-examples.py)

PaperBank 原创教学图 · 模拟数据，非论文结果 · CC BY 4.0

#### 置信带

<a id="teaching-confidence"></a>
#### 置信区间与误差带

![置信区间与误差带](../assets/confidence.svg)

深线是模拟样本均值，内层是68%、外层是95%的逐点bootstrap区间；宽度有计算依据，不是调个透明度。

1. **均值线与两层色带：**深线是模拟样本均值；内层为68%、外层为95%的逐点bootstrap区间，宽度来自计算。

2. **底部重采样说明：**每个设置有40个独立模拟观测，按观测有放回重采样1000次，再取均值分位数。

3. **色带的解释范围：**区间针对各个均值，不是整个函数的同时置信带，也不表示样本本身落在带内。

[可复现教学绘图代码](../assets/generate-statistical-examples.py)

PaperBank 原创教学图 · 模拟数据，非论文结果 · CC BY 4.0

#### 配对增益

<a id="teaching-paired-gain"></a>
#### 配对增益

![配对增益](../assets/paired-gain.svg)

每点是一项模拟任务的干预减基线，零线右侧提高、左侧下降；既显示收益，也留下失败。

1. **每个任务一个点：**24个模拟任务各保留自己的配对关系；每点是同一任务的干预准确率减基线准确率。

2. **虚线零点：**零线右侧提高，左侧下降，收益与失败一起展示。

3. **横轴单位：**差值单位是百分点，不是相对百分比；任务散点没有进行显著性检验，也不能替代总体汇总。

[可复现教学绘图代码](../assets/generate-statistical-examples.py)

PaperBank 原创教学图 · 模拟数据，非论文结果 · CC BY 4.0

#### 热图

<a id="teaching-heatmap"></a>
#### 热图：分组结果

![热图：分组结果](../assets/heatmap.svg)

模型与任务交叉排，颜色和格内数值用同一尺度；缺测格单独写Missing，不能记作零分。

1. **行列与格内数字：**模型和任务交叉排列，格内直接标数值，让不辨色的读者也能比较。

2. **底部统一色标：**全图使用60%到80%的同一色标；不能逐行归一化后继续横向比较颜色。

3. **灰色Missing格：**灰色只表示缺测，单独标Missing；缺测不能记为零分。

[可复现教学绘图代码](../assets/generate-statistical-examples.py)

PaperBank 原创教学图 · 模拟数据，非论文结果 · CC BY 4.0

#### 成本性能图

<a id="teaching-cost"></a>
#### 成本与性能

![成本与性能](../assets/cost.svg)

横轴是模拟在线成本，纵轴是准确率，每个字母是一项配置；虚线只连接已画出的有效取舍点。

1. **成本与准确率两轴：**横轴按每1000次查询计模拟在线成本，纵轴是准确率；一次性训练成本须另行报告。

2. **字母配置点：**每个字母是一项明确的模拟配置，让成本与表现可以对应回具体设置。

3. **虚线连接：**虚线只连接已展示的非支配点，方便读取取舍；不证明中间配置存在，也不代表连续最优函数。

[可复现教学绘图代码](../assets/generate-statistical-examples.py)

PaperBank 原创教学图 · 模拟数据，非论文结果 · CC BY 4.0

#### 饼图与环图

<a id="teaching-donut"></a>
#### 环图：组成比例

![环图：组成比例](../assets/donut.svg)

中心写100个模拟对象，旁边同时列数量和比例；四类互斥，所有扇区合起来才是一个整体。

1. **中心总数：**先写100个模拟对象，明确统计单位与分母，再看各类占比。

2. **右侧数量与比例：**四类分别为40、30、20、10，总和为100；数量与比例同时列出，减少估读。

3. **四个扇区：**四类互斥，共同构成整体。精确比较相近比例时，数值或横向条图更直接。

[可复现教学绘图代码](../assets/generate-statistical-examples.py)

PaperBank 原创教学图 · 模拟数据，非论文结果 · CC BY 4.0

#### 二维增益

<a id="teaching-two-gain"></a>
#### 双指标增益

![双指标增益](../assets/two-gain.svg)

准确率增益向右更好，延迟减少向上更好；零线分四区，右上是两项同时改善。

1. **横轴与纵轴方向：**准确率增益向右更好，延迟减少向上更好；横轴用百分点，纵轴用相对百分比。

2. **两条零线与右上区：**零线分出四个象限，右上表示两项同时改善，其余象限显示不同取舍。

3. **配置点与结论范围：**每点是构造的模拟配置；象限只说明这两项指标的关系，不是论文结果或总体优越性的证明。

[可复现教学绘图代码](../assets/generate-statistical-examples.py)

PaperBank 原创教学图 · 模拟数据，非论文结果 · CC BY 4.0

<a id="figure-references"></a>
### 2.5 补充参考

[15-minute cities 图 1：地图、分布、多维散点](https://arxiv.org/html/2408.03794v1#S2.F1)：地图定位差异，累计分布看人口覆盖，散点把城市放到同一坐标系。横轴是人口加权平均邻近时间，纵轴是 15 分钟覆盖人口比例；颜色是 Gini，圆大小是人口密度。位置、颜色、大小各讲一件事。灰区是受概率约束的不可达组合，不是“平均不到 15 分钟就人人可达”。

适合“总体分布加个体差异”的多维呈现。四种编码有四种明确含义，再多就该拆图。

Bruno et al., A universal framework for inclusive 15-minute cities, Nature Cities (2024), DOI 10.1038/s44284-024-00119-4; arXiv:2408.03794v1

只链接原图，不重托管。arXiv 非独占分发许可。

[15-minute cities 图 2：算法、排名、前后变化](https://arxiv.org/html/2408.03794v1#S2.F2)：先画人口导向的 POI 重分配，再给城市迁移比例排名，最后用罗马的地图和直方图看前后变化。POI 是服务设施点；(b) 排的是现有 POI 的迁移比例，不是新增设施数。

三个层次回答“怎么做、改动多大、改到了哪里”。排名负责总体差异，地图负责空间位置，直方图负责分布，谁也不用兼职。

Bruno et al., A universal framework for inclusive 15-minute cities, Nature Cities (2024), DOI 10.1038/s44284-024-00119-4; arXiv:2408.03794v1

只链接原图，不重托管。arXiv 非独占分发许可。

[OneReason 图 12：对照策略的改动位置](https://arxiv.org/pdf/2606.06260v1#page=34)：相同结构对齐；改动位置突出，符号在图注解释。保留链接读图，不复制整图。







[KDE：OneReason 图 6](https://arxiv.org/pdf/2606.06260v1#page=13)：四个领域并排，两个方法保持同色；淡填充保留重叠，虚线与均值标注把位置变化说清，曲线不用自己兼职字幕。

四个领域沿用同色方法与均值线。横轴是 Margin，纵轴是密度；不是累计概率。是否表示任务收益，另看原文对 Margin 的定义。

OneRec Team, OneReason Technical Report, arXiv:2606.06260v1, Fig. 6

只链接原图，不重托管。该版本采用 arXiv 非独占分发许可。

[投影：life2vec 图 4，PaCMAP 与局部放大](https://www.nature.com/articles/s43588-023-00573-5/figures/4)：中间给完整嵌入空间，两侧放大选定区域，同一批点分别按性别、年龄、真实标签着色；位置保持，颜色换问题。

原图明确使用 PaCMAP；保持点的位置、分别换属性颜色，才能追踪同一批点。投影和 TCAV 是不同证据，不能合成因果结论。

Savcisens et al., Nature Computational Science 4, 43–56 (2024), Fig. 4, DOI 10.1038/s43588-023-00573-5

只链接出版社图页；期刊版本未标明可转载的 CC 许可。

[OneReason 图 1：把模型身份和结果放一起](https://arxiv.org/pdf/2606.06260v1#page=1)：左侧雷达看多任务表现，右侧成对柱图看推理和训练数据的作用；颜色、纹理、数值分工，提升与下降都直接标出。

雷达各轴的量纲与归一化必须定义，不能仅凭面积判断综合能力。 柱顶相对增幅与原分数同时保留；百分比不是百分点，下降项不能藏起来。

OneRec Team, OneReason Technical Report, arXiv:2606.06260v1, PDF p. 1

只链接原图，不重托管。该版本采用 arXiv 非独占分发许可。

[OneReason 图 7：颜色跟着流程职责走](https://arxiv.org/pdf/2606.06260v1#page=19)：两边保持相同网络层次，只换雪花与火焰标记；第一阶段和后续阶段分别更新哪些参数，一眼能对上。

图标要有明确图例；颜色是辅助，不能只让读者猜蓝色是冻结。 同一层在两边位置一致，适合解释训练范围变化，不说明阶段间性能差异。

OneRec Team, OneReason Technical Report, arXiv:2606.06260v1, PDF p. 19

只链接原图，不重托管。该版本采用 arXiv 非独占分发许可。

[OneReason 图 9：分布与多维特征分开读](https://arxiv.org/pdf/2606.06260v1#page=29)：左边堆叠条保留五档评分比例，右边雷达概括五项均分；先看分布，再看轮廓。

两面板使用同一组维度。雷达的数值标签便于准确读取，堆叠条显示不同评分构成；雷达面积不能替代具体分数。

OneRec Team, OneReason Technical Report, arXiv:2606.06260v1, PDF p. 29

只链接原图，不重托管。该版本采用 arXiv 非独占分发许可。

[ShoppingBench 图 1、2：任务概览与案例层级](https://ojs.aaai.org/index.php/AAAI/article/view/40640)：左边按请求、工具调用、观察和结果走流程，右边拆产品、优惠券和预算；高亮颜色贯穿两边，读者能把需求对到检查。 上面分产品采样和字段采样，下面把提示模板与生成指令逐行对齐；同一类任务同色，读者看得出结果从哪来。

背景、需求、动作、反馈分层；颜色和高亮有角色，不靠密集箭头补逻辑。

ShoppingBench: A Real-World Intent-Grounded Shopping Benchmark for LLM-based Agents, AAAI 2026, Fig. 1–2

只链接正式论文页，不重托管原图。

<a id="refine"></a>
## 3. 正文精修

先检查全文规范，再按章节精修。模板中的【】填自己的材料，段落按内容调整。


<a id="general-rules"></a>
### 3.1 全文规范

一篇论文围绕一个主要亮点。标题、摘要、引言、方法和实验讲同一件事；先审论证，再磨语言。模块多，不等于贡献多。

#### 逻辑：句子承接与对象一致

- **先说为什么值得做：**每项设计都要回答：已有做法在哪种条件下不足，本文改了什么，为什么有用，哪项证据支持。

- **句子之间有逻辑关系：**后句处理前句的问题或产物，Then 和 Therefore 须符合实际关系。

- **连接词用对：**转折用 However，有因果依据才用 Therefore；并列直接写。

- **章节按流程衔接：**开头说明输入，结尾说明输出及其在下一步的用途。

- **问题、设计、实验对应：**引言提出的问题，方法处理，实验检验。

#### 语言：完整判断与句长

- **用具体操作替代空泛评价：**用具体操作替换 powerful、comprehensive 等空评价。

- **短句，完整动作：**长句按步骤拆，后句接前句产物；主语、动作和条件写全。

- **正文写完整句子：**加号、箭头不能代替文字关系；公式、代码和图中照常使用。

- **同级小节篇幅相称：**任务相近，篇幅尽量接近；太长先查重复，复杂内容分段。

#### 术语：首次定义与名称一致

- **术语首次解释：**写清对象和用途，不让读者到后文找定义。

- **符号首次定义：**写对象、来源、算法、用途和下标；不用的符号删掉。

- **同一对象同一称呼：**同一对象同一名称；正文不用 it／they 及同族代词，换成简短对象名。

- **贡献词有事实依据：**tailored、expert-confirmed、de-identified 能突出真实贡献。有依据就用，一词换一词，避免重复或无依据的形容词。

- **发现可取短名：**短名后立即解释具体发现；优先四个英文词以内。

#### 主张：证据与适用范围

- **保留结论条件：**任务、模型、范围和分母写清；有限测试不推广所有场景。

- **观察与原因分开：**先报告现象，再讲可能原因；匹配对照支持后才归因。

- **首句写发现：**随后给图表、关键比较和意义，不复述表头。

<a id="annotated-global-flow"></a>

#### 贡献与句间衔接

假设的文档问答任务；只演示句间承接与证据范围，不是论文原文或实测结果。

**English 教学改写**

To make answers traceable to source evidence, [Method] records each retrieved quote with the corresponding manual location and relevant dialogue constraints. These records form evidence notes that guide answer generation together with the current question and retained constraints. With the inputs and inference budget held fixed, we compare note-guided generation with passage-only generation. Note-guided generation improves citation support by [support gain] but adds [latency cost] under [tested conditions], revealing a trade-off between traceable answers and response time.


**中文译文**

为让答案依据可追溯，[方法] 记录每个检索摘句、对应的手册位置与相关对话约束。这些记录构成证据笔记，与当前问题及保留的约束共同指导答案生成。在固定输入与推理预算后，我们比较笔记引导的生成与只使用片段的生成。在[实测条件]下，笔记引导的生成使引用支持率提高[提升幅度]，但增加[延迟开销]，说明答案可追溯性与响应时间存在取舍。


**高亮与旁批**

1. **records each retrieved quote with the corresponding manual location and relevant dialogue constraints / 记录每个检索摘句、对应的手册位置与相关对话约束**：写动作和对象。记录什么，直接说出来：摘句、位置、约束。“建立可靠证据框架”没有这些信息。
2. **These records form evidence notes / 这些记录构成证据笔记**：钩子接产物。These records 接前句的三类记录，再说明产物是证据笔记。不是突然换个模块。
3. **With the inputs and inference budget held fixed / 在固定输入与推理预算后**：比较条件写在近处。说明固定什么，后面的差别才可解释；只写“公平比较”不够。
4. **improves citation support by [support gain] but adds [latency cost] under [tested conditions] / 使引用支持率提高[提升幅度]，但增加[延迟开销]**：发现保留收益、代价与范围。引用支持率、延迟是两项不同结果。报告已测条件下的取舍，不一句话扩大成“全面提升问答性能”。

PaperBank · 教学改写

本段是原创教学示范。[support gain]、[latency cost] 与 [tested conditions] 必须由真实实验替换。

本指南原创内容采用 CC BY 4.0；转载请附作者、原文链接与许可，改写注明改动。

**按论文顺序精修**

摘要概括全文，引言提问题，方法给做法，实验查效果，讨论讲范围，结论收尾。

- 3.2 标题：先把最值得记住的发现放进标题。
- 3.3 摘要：让人用一段话看懂为什么这项工作值得做。
- 3.4 引言：让读者认同问题，并记住你的解法为什么有用。
- 3.5 相关工作：说明已有路线、本文差异及其与核心贡献的关系。
- 3.6 方法：铁律：告诉读者为什么你的方法好，比解释清楚方法更重要。
- 3.7 实验：用对照检验贡献，解释主要差异与发现。
- 3.8 讨论与局限：解释发现，写清适用范围和局限。
- 3.9 结论：回答开头的问题，概括贡献和发现。
- 3.10 参考文献：引用回查原文，信息和版本对齐。
- 3.11 附录：提供可定位、可复核的设置与补充材料。

逐句示范有论文原文短引，也有明确标注的模拟段落。原文例子来自不同论文，不拼接成同一篇完整论文；模拟部分用同一个假设任务串联。

### 本章目录

- [3.2 标题](#title)
- [3.3 摘要](#abstract)
- [3.4 引言](#intro)
- [3.5 相关工作](#related)
- [3.6 方法](#method)
- [3.7 实验](#experiments)
- [3.8 讨论与局限](#discussion)
- [3.9 结论](#conclusion)
- [3.10 参考文献](#references)
- [3.11 附录](#appendix)

<a id="title"></a>
<a id="chapter-title"></a>
### 3.2 标题

先把最值得记住的发现放进标题。

#### 本节原则

- 围绕最重要的贡献写标题，让人看出研究对象、任务或关键发现。
- 方法名只是名字，后半句要交代实际做了什么。发现型论文直接写发现，不必包装成方法论文。
- 记忆点应准确、好懂。避开需要正文解释才能理解的缩写和自我评价。

<a id="annotated-title"></a>

#### 标题结构

论文原文短引 · 中文为本指南翻译

**English 原文**

Careful Queries, Credible Results: Teaching RAG Models Advanced Web Search Tools with Reinforcement Learning


**中文译文**

谨慎查询，可信结果：通过强化学习教会 RAG 模型使用高级网页搜索工具。


**高亮与旁批**

1. **Careful Queries, Credible Results / 谨慎查询，可信结果**：先给记忆点。查询要谨慎，结果要可信。前半句让读者记住工作追求的价值，不列模块清单。
2. **Teaching RAG Models Advanced Web Search Tools / 教会 RAG 模型使用高级网页搜索工具**：交代对象与任务。后半句立即说清教谁、学会什么。仅有一句口号，读者还不知道论文做了什么。
3. **with Reinforcement Learning / 通过强化学习**：给出关键手段。强化学习解释任务怎样实现。标题保留关键手段，不必把训练流程全塞进来。

[WebFilter · AAAI 2026](https://ojs.aaai.org/index.php/AAAI/article/view/40299) · Title，PDF第1页（刊页30458）；AAAI 2026 camera-ready；2026-03-14正式发表

去除LaTeX排版与文献标记、合并换行；原词句未改。 数学符号改为可读文本形式。

©2026 AAAI. All rights reserved. 独立保留原论文版权；未授予PaperBank整篇或原图再许可。

<a id="abstract"></a>
<a id="chapter-abstract"></a>
### 3.3 摘要

让人用一段话看懂为什么这项工作值得做。

#### 本节原则

- 一段讲清问题、已有不足、核心贡献、主要发现。摘要能单独读懂，长度按会议要求。
- 贡献对象和动作尽早出现。关键改动要回应前句的不足，不先堆流程和数量。
- 每句接住上句的对象，再增加信息。术语首次解释，缩写展开；通常不放引文，投稿规定优先。
- 结果优先保留有信息增量的发现及比较范围；不逐项报分，不机械以最大数字结尾。

<a id="annotated-abstract"></a>

#### 摘要结构

假设教学段落，非论文原文或实测结果。

**English 教学改写**

Document-based dialogue requires answers that respect both source evidence and evolving user constraints. Passage-only generation supplies relevant text without explicitly recording which dialogue constraints the source quotes support. Structured evidence notes pair source quotes with the corresponding manual locations and active dialogue constraints. These notes let the generator cite sources and explain how the evidence relates to each constraint. In our comparison on static English manuals, notes increase citation support relative to direct generation but add latency. The comparison evaluates source support; the support scores do not establish that every user constraint is satisfied.


**中文译文**

基于文档的对话要求答案同时符合来源证据与不断变化的用户约束。只使用片段的生成方式提供相关文本，却不明确记录来源摘句支持哪些对话约束。结构化证据笔记将来源摘句与对应的手册位置及当前有效的对话约束配对。这些笔记帮助生成器引用来源，并说明证据与各项约束的关系。在针对静态英语手册的比较中，相比直接生成，笔记提高了引用支持率，但增加了延迟。这个比较评价的是来源支持，不能据此认定每项用户约束都得到满足。


**高亮与旁批**

1. **both source evidence and evolving user constraints / 来源证据与不断变化的用户约束**：任务需求写具体。证据与用户约束是两类要求。先建立它们，下一句的不足与后面的设计才有对象。
2. **without explicitly recording which dialogue constraints the source quotes support / 却不明确记录来源摘句支持哪些对话约束**：把缺口缩到本文负责的部分。承认片段提供了相关文本，再限定缺口：没有显式记录证据与约束的对应。对应设计也必须处理这个缺口。
3. **Structured evidence notes pair source quotes with the corresponding manual locations and active dialogue constraints. / 结构化证据笔记将来源摘句与对应的手册位置及当前有效的对话约束配对。**：贡献对象与动作前置。句首先报新增产物，pair 说具体改动：摘句、位置、约束配对。不是先报流程，最后才揭晓贡献。
4. **notes increase citation support relative to direct generation but add latency / 相比直接生成，笔记提高了引用支持率，但增加了延迟**：发现与取舍一起交代。这个假设案例保留引用支持率和延迟的取舍。真实论文换成核验过的结果，不逐项罗列排名。
5. **the support scores do not establish that every user constraint is satisfied / 不能据此认定每项用户约束都得到满足**：别让指标越界。引用支持率测来源支持，不能代替约束满足率。实际摘要只保留会影响结论理解的边界。

PaperBank · 教学改写

沿用文档问答的假设任务，展示信息顺序与论证作用，不代表新增研究结果。

本指南原创内容采用 CC BY 4.0；转载请附作者、原文链接与许可，改写注明改动。

<a id="intro"></a>
<a id="chapter-intro"></a>
### 3.4 引言

让读者认同问题，并记住你的解法为什么有用。

#### 本节原则

- 段首加钩子：接回刚提出的问题、困难或产物，再推进一层。However 写转折，To address 写解法；对象必须接得上。
- 前两段可穿插、合并或拆分，但要有领域回顾与已有方法比较。回顾给局限铺路：后面批评什么，前面先说明已有方法怎样处理它。
- 局限要具体：问题是什么、为什么存在、阻碍了什么。必要时用简短名称，后文沿用；不只列几个困难就开始报方法。
- 贡献对象与动作尽早出现。expert-confirmed、manually selected、tailored 等词要对应实际工作；写清选择依据，不用“高质量”代替依据。
- 方法段逐点解决前面的困难，只讲设计思路；公式与实现留给 Method。图句说明图里哪个例子或对比支持这项设计。
- 结果段先用钩子接回研究问题，再给主要发现。贡献、术语和发现与 Abstract 对应；不逐字复述，也不把排名当作分析。
- 给每个局限沿用同一名称和定义；Related Work 给比较依据，Method 写对应设计，实验检验这项设计并接回该局限。
- 结果概述对应正文实际结论。若实验只支持某些任务或条件，摘要、引言、讨论和结论都限定到相同范围。

<a id="intro-hooks"></a>
#### 段落承接

钩子把新段接回前文的具体问题，让读者知道这段在回答什么。常放句首；However、Therefore 后也要有明确对象。


<a id="abstract-intro-map"></a>
#### 摘要与引言：主张对应

教学对照。方括号填自己的材料；箭头连接对应内容，不规定段数。点击引言一侧可跳到修改 case。


**问题 · 同一问题，展开困难**

**Abstract**：We ask whether LLMs can handle changing needs and unresolved conditions in shopping conversations.

**Intro**：How well can LLMs handle changing needs and unresolved conditions? Answering this question faces data scarcity and case-dependent evaluation standards.
 · [修改 case](#annotated-intro-obstacles)

**贡献 · 同一产物，交代来源与作用**

**Abstract**：We introduce [Benchmark], pairing timestamped dialogue with case-specific evaluation criteria.

**Intro**：To address these obstacles, [Benchmark] retains timestamped dialogue. Experts distill Ideal Response Principles from manually selected replies to define case-specific evaluation criteria.
 · [修改 case](#annotated-intro-design)

**发现 · 名称一致，展开含义与分析**

**Abstract**：Models exhibit Product Evidence Overreach and Shopping Uncertainty Collapse.

**Intro**：To answer this question, we evaluate [models]. Replies exhibit Product Evidence Overreach through unsupported claims and Shopping Uncertainty Collapse by treating unknown needs as settled; further analysis examines [specific finding].
 · [修改 case](#annotated-intro-findings)

<a id="intro-body-map"></a>
#### 引言如何贯穿全文

引言提出什么问题，正文就检验什么问题。给同一局限、设计和实验沿用同一个名称；每个段首用具体对象接回前文。实验得出什么、只支持到哪里，再回写摘要、引言和结论。

教学结构示意。方括号替换为已核验材料；按论证组织句子和段落，不固定句数或段数。

- **Q / M / E · 问题、设计、检验：**编号相同表示同一条局限 → 设计 → 实验链。

- **L · 已有方法局限：**已有路线在某种任务、输入或评价范围内的不足。

- **D · 研究实施困难：**建立本文数据、方法或评价时需要克服的困难。

- **B · 本文剩余局限：**本文证据尚未覆盖的范围；不能冒充已解决的问题。

**A · 已有能力**

[已有方法]已能完成[任务]；这些能力支持对话助手理解用户需求。

句首钩子：`These capabilities support ...`

- [相关工作](#chapter-related) · 说明已有路线：按任务或机制归类，说明[已有方法]实际具有什么能力。
- [方法](#chapter-method) · 交代起点：说明本文使用了哪些已有能力，新增设计解决什么问题。

先承认已有能力，再指出不足；不能把前人已有的功能写成本文首次提供。

**Q · 研究问题**

然而，需求可能变化，也有条件仍未明确。对话助手能否同时处理变化的需求与未决条件？

句首钩子：`However, these needs can change or remain unresolved, ...`

- [方法 · 任务定义](#chapter-method) · 定义评价对象：定义“变化的需求”与“未决条件”，写清模型收到什么、回复须保留什么。
- [实验 · 研究问题](#chapter-experiments) · 转成可检验问题：To answer this question, we evaluate [对象] under [条件]，用对应判据检验需求处理与未知保留。
- [结论](#chapter-conclusion) · 回答开头：据实际结果回答对话助手能否处理变化的需求与未决条件。

任务定义、模型输入、评分对象和结论都回答同一问题，不从“回复评价”跳成“真实执行成功”。

**L1 → M1 → E1 · 局限一：需求时效**

[比较表]显示，[所比较基准]未报告需求时效所需的时间信息；据其公开说明，无法确认评价是否区分仍有效与已失效的历史需求。

句首钩子：`However, the compared benchmarks do not explicitly report [时间输入].`

- [相关工作 · 对比表](#chapter-related) · 给出 L1 依据：However, [L1 的具体不足]. To address this limitation, we [M1 的对应设计]，并引用核验后的输入比较。
- [方法 · M1](#chapter-method) · 说明设计作用：To assess whether earlier needs still apply, [M1]保留需求变化及时间信息，说明这些输入怎样影响判断。
- [实验 · E1](#chapter-experiments) · 检验原动机：To test this role of temporal information, [E1]比较对应条件，检验历史需求是否仍适用的判断。

L1 在引言、However 句、方法动机和实验解释中指同一不足。“未报告”不能改成“没有”；未做输入对照就不能宣称时间信息导致提升。

**L2 → M2 → E2 · 局限二：未知保留**

[已有评价]未明确检验回复是否保留关键未知，因而难以识别把未决条件当成确定事实的错误。

句首钩子：`To detect whether unresolved conditions are treated as settled, ...`

- [相关工作 · 评价比较](#chapter-related) · 给出 L2 依据：However, [已核验的评价不足]. To address this limitation, we [M2]，比较的是未知保留判据，不是有无模糊案例。
- [方法 · M2](#chapter-method) · 落实评价要求：For each case, [M2]明确哪些条件仍未知、回复不能擅自确定什么。
- [实验 · E2](#chapter-experiments) · 检验原动机：To evaluate uncertainty preservation, [E2]报告对应错误，解释模型是否把未决条件当成确定事实。

同一个未知条件须贯穿输入、判据、回复错误和结果解释；不能将“没有明确奖励保留未知”写成“前人完全没有模糊场景”。

**D1 / D2 · 实施困难**

建立这类评价还面临[材料获取困难 D1]与[逐案例标准困难 D2]；这些困难妨碍对需求变化与关键未知的精确评价。

句首钩子：`However, establishing this evaluation faces [具体困难].`

- [方法 · 数据与判据](#chapter-method) · 说明怎样克服困难：To address [D1/D2], [实际操作]形成[数据或判据]，交代来源、选择依据和产物用途。
- [附录](#chapter-appendix) · 提供可复核细节：给出对应的材料说明、判据定义与实际执行设置。

先解释困难怎样阻碍研究目标，再给解法。D 是本文实施难点，不是前人方法 L，也不是本文剩余局限 B。

**M1 / M2 · 对应设计**

为检验上述问题，[本文产物]结合可解释的需求变化输入与逐案例判据，分别支持需求时效判断和未知保留评价。

句首钩子：`To evaluate these two aspects, [本文产物] ...`

- [方法 · Overview](#chapter-method) · 展开实际流程：先说 M1 怎样处理 L1、M2 怎样处理 L2，再交代各部分的输入、操作、产物和依赖。
- [关键图与图注](#chapter-method) · 显示同一设计：图内名称与正文相同，箭头说明输入流向；评价判据不能画成模型已接收的输入。
- [实验 · 对照设置](#chapter-experiments) · 说明怎样检验：With [比较条件] held fixed, [E1/E2]检验对应设计的作用；输入、预算与判分条件按实际设置交代。

每项设计须能接回具体问题；图、Overview 和实验使用同一对象，不把整套方法的效果归给一个未单独检验的模块。

**E1 / E2 → Q · 实验发现**

为回答这一问题，[实验]发现[需求时效判断的真实结果]与[未知保留的真实结果]，说明模型在[实际测试范围]内有哪些能力或不足。

句首钩子：`To answer this question, we evaluate [对象] ...`

- [实验 · 主结果与分析](#chapter-experiments) · 先结论，再证据：To examine [L1/L2], 先给[具体发现]，再用关键对照、图表位置和评分口径解释发现如何得到。
- [实验 · 回扣动机](#chapter-experiments) · 解释结果回答了什么：This comparison shows [实际关系]，说明需求时效判断或未知保留是否达到研究目标。
- [摘要与引言](#chapter-abstract) · 回写主要发现：摘要压缩同一发现，引言展开含义；名称、对象、比较范围与实验一致。
- [讨论](#chapter-discussion) · 限定解释：区分观察到的差异、可能原因与已验证机制，不把回复错误扩大为真实执行失败。

结果必须回答开头的研究问题及方法动机。只有总体对比时不能补写模块因果；只有个例时不能写全体发生率。

**C / B · 贡献与结论范围**

本文提供[实际新增产物]并揭示[证据支持的发现]；结论限于[已测试任务与条件]，尚未覆盖[剩余范围 B]。

句首钩子：`Within these evaluated conditions, [受证据支持的结论] ...`

- [讨论与局限](#chapter-discussion) · 说明 B 与影响：说明未覆盖的条件怎样限制结论；未测试不等于已经失败。
- [结论](#chapter-conclusion) · 闭合研究问题：回答 Q，概括已验证的贡献与发现，并保留同一已测试任务与条件。
- [摘要与引言](#chapter-abstract) · 反向缩小主张：若实验只支持[某种范围]，摘要、引言和贡献句都缩至该范围，不留“全面解决”的旧句。

前人局限 L 可以被本文设计处理；本文剩余局限 B 则限定处理到哪里。二者不是同一标签，更不能把 B 写成已解决贡献。

L1 → M1 → E1 → Q：需求时效缺口 → 保留对应输入 → 检验需求有效性判断 → 回答需求变化问题。

L2 → M2 → E2 → Q：未知保留缺口 → 明确逐案例判据 → 检验擅自确定的错误 → 回答未决条件问题。

**结果回写**：实际实验结果与范围 → 摘要、引言的贡献与发现 → 讨论、结论。证据改变，前面的主张一起改。

<a id="annotated-intro-obstacles"></a>

#### 困难与评价目标

教学改写，非论文原文或实测结果；方括号替换自己的材料。

**English 教学改写**

However, answering this question faces two obstacles. First, data scarcity limits access to real commercial conversations, and identifying complex or ambiguous needs requires costly expert annotation. Second, case-dependent standards complicate evaluation: clothing recommendations require color and outfit coordination, whereas phone recommendations require different suitability checks. Even within one category, requirements and risks vary across cases. A fixed checklist can miss these differences. Together, these obstacles hinder accurate evaluation of LLMs on complex, ambiguous, and time-sensitive shopping requests.


**中文译文**

然而，回答这个问题有两个困难。首先，数据稀缺使真实商业对话难以获取，识别复杂或模糊的需求还需要成本较高的专家标注。其次，随案例变化的标准增加了评价难度：服装推荐要考虑颜色与穿搭搭配，手机推荐则要检查其他适配条件。即使是同类商品，不同案例的需求与风险也会变化。一张固定清单可能漏掉这些差异。这两类困难共同妨碍了对 LLM 处理复杂、模糊且有时效性的购物请求进行准确评价。


**高亮与旁批**

1. **However, answering this question faces two obstacles. / 然而，回答这个问题有两个困难。**：段首先加钩子。this question 接回上段的问题。先让读者知道这段为什么出现，再讲困难；只放一个 However 不够。
2. **data scarcity limits access to real commercial conversations, and identifying complex or ambiguous needs requires costly expert annotation / 数据稀缺使真实商业对话难以获取，识别复杂或模糊的需求还需要成本较高的专家标注**：数据与标准是两类困难。数据难拿、标注成本高，是数据问题；标准随情境变化，是评价问题。别把后者写成“进一步阻碍数据获取”。
3. **Even within one category, requirements and risks vary across cases. / 即使是同类商品，不同案例的需求与风险也会变化。**：category 和 case 别直接互换。服装与手机说明品类差异。这句再交代同类商品也有不同需求与风险，才接得上 case-dependent。
4. **Together, these obstacles hinder accurate evaluation of LLMs on complex, ambiguous, and time-sensitive shopping requests. / 这两类困难共同妨碍了对 LLM 处理复杂、模糊且有时效性的购物请求进行准确评价。**：加一句铺垫，再提解法。点明困难妨碍的是准确评价。下一段的数据与按例标准就有了来由，不要从困难直接跳到 We introduce。

PaperBank · 教学改写

根据作者提供的修改意见撰写的教学段落，不含当前稿件名称、数据数量、模型名单或未经核对的基准比较。Figure [X] 为图号占位。

本指南原创内容采用 CC BY 4.0；转载请附作者、原文链接与许可，改写注明改动。

<a id="annotated-intro-design"></a>

#### 设计与专家产物

教学改写，非论文原文或实测结果；方括号替换自己的材料。

**English 教学改写**

To address these obstacles, we introduce [Benchmark]. Business experts screen cases in de-identified shopping conversations. Each case retains timestamped dialogue, including changed needs and unanswered questions. Experts distill Ideal Response Principles from excellent replies manually selected from completed transactions. These principles guide case-specific criteria across Core, Excellence, and Safety and inform a tailored reasoning prompt. The tiers assess required completion, added value, and risk avoidance, respectively. Our example (Figure [X]) illustrates how elapsed time and unresolved information affect the advice a case requires.


**中文译文**

为处理这些困难，我们提出【Benchmark】。业务专家从去标识化的购物对话中筛选案例。每个案例保留带时间戳的对话，包括发生变化的需求和未得到回答的问题。专家提炼出理想回复原则，依据的是从成功交易中手工筛选出的优秀回复。这些原则指导针对每个案例制定 Core、Excellence 和 Safety 三层标准，并用于设计专门的推理提示词。三层分别评价必要要求的完成、额外价值和风险规避。我们的例子（图【X】）说明时间推移和未决信息如何影响一个案例所需的建议。


**高亮与旁批**

1. **Experts distill Ideal Response Principles / 专家提炼出理想回复原则**：专家的产物放前面。先说谁做了什么、产出了什么，再交代来源。不要读到句尾才知道核心贡献是提炼原则。
2. **excellent replies manually selected from completed transactions / 从成功交易中手工筛选出的优秀回复**：手工、优秀、成单都要交代。manually 写出手工；excellent 写出质量；成单写出来源。成单可筛选，但不自动证明回复好，还需给实际质量标准。
3. **These principles guide case-specific criteria across Core, Excellence, and Safety / 这些原则指导针对每个案例制定 Core、Excellence 和 Safety 三层标准**：这句接回前文的评价要求。These principles 接上专家的产物；case-specific 回应标准随案例变化。三层名称全文一致，分别说明检查什么。
4. **Our example (Figure [X]) illustrates how elapsed time and unresolved information affect the advice a case requires. / 我们的例子（图【X】）说明时间推移和未决信息如何影响一个案例所需的建议。**：图要接回刚才的输入。图中要能看到时间、需求变化与未决条件。若再比较别人缺少什么输入，逐项核对对比表；别凭方法名称推断。

PaperBank · 教学改写

根据作者提供的修改意见撰写的教学段落，不含当前稿件名称、数据数量、模型名单或未经核对的基准比较。Figure [X] 为图号占位。

本指南原创内容采用 CC BY 4.0；转载请附作者、原文链接与许可，改写注明改动。

<a id="annotated-intro-findings"></a>

#### 发现与分析

教学改写，非论文原文或实测结果；方括号替换自己的材料。

**English 教学改写**

To answer this question, we evaluate [commercial models] and [open-weight models]. Across these models, we observe Product Evidence Overreach, where replies add unsupported product claims, and Shopping Uncertainty Collapse, where unresolved needs are treated as settled. These failures may make shopping advice less reliable. Further analysis links these failures to changing requirements and unresolved information.


**中文译文**

为回答这个问题，我们评价【商业模型】与【开放权重模型】。在这些模型的回复中，我们观察到两类失败：Product Evidence Overreach，即回复添加了缺少证据支持的商品声明；Shopping Uncertainty Collapse，即将尚未确定的需求视为已经明确。这些失败可能降低购物建议的可靠性。进一步分析将这些失败与需求变化和未决信息联系起来。


**高亮与旁批**

1. **To answer this question / 为回答这个问题**：尤其是段首，要接回问题。先接前文的研究问题，再报模型范围。否则这段像突然开始列名单，读者不知道实验在回答什么。
2. **Across these models, we observe Product Evidence Overreach, where replies add unsupported product claims, and Shopping Uncertainty Collapse, where unresolved needs are treated as settled. / 在这些模型的回复中，我们观察到两类失败：Product Evidence Overreach，即回复添加了缺少证据支持的商品声明；Shopping Uncertainty Collapse，即将尚未确定的需求视为已经明确。**：先 overview，名称要对应。先用一句总览两类失败，再展开。与摘要和前文保留同一名称，解释可以转述；模型数量与分数不能代替发现。
3. **Further analysis links these failures to changing requirements and unresolved information. / 进一步分析将这些失败与需求变化和未决信息联系起来。**：这里还可以展开一个结论。links 还没说具体发现。补实际条件、对照与结果，说明哪类失败何时更明显；关联不能直接写成因果。

PaperBank · 教学改写

根据作者提供的修改意见撰写的教学段落，不含当前稿件名称、数据数量、模型名单或未经核对的基准比较。Figure [X] 为图号占位。

本指南原创内容采用 CC BY 4.0；转载请附作者、原文链接与许可，改写注明改动。

<a id="annotated-intro"></a>

#### 领域回顾

高亮与旁批按颜色和编号对应；点击切换中英。

**English 原文**

Humans spend nearly 90% of their time indoors [12], and the built environment contributes a substantial share of global carbon emissions [34, 65, 66]. Thus, building design sits at the nexus of daily life and sustainability. Traditional design relies heavily on expert knowledge and extensive manual iteration [2, 14, 20], often taking days to months to reach viable solutions. Recent advances in generative models on controllable [5, 32, 47] and multimodal generation [7, 24, 50] pave the way for automated building design generation.


**中文译文**

人们近 90% 的时间在室内度过 [12]，建筑环境也占全球碳排放的相当大一部分 [34, 65, 66]。因此，建筑设计连接着日常生活与可持续性。传统设计高度依赖专家知识和大量人工迭代 [2, 14, 20]，往往需要数天至数月才能得到可行方案。近期，可控生成 [5, 32, 47] 和多模态生成 [7, 24, 50] 的进展，为建筑设计的自动生成铺平了道路。


**高亮与旁批**

1. **at the nexus of daily life and sustainability / 连接着日常生活与可持续性**：背景要为后文服务。室内生活与碳排放对应两个实际问题，后文的功能和能耗也要分别接住。只说建筑重要，还没说本文为何重要。
2. **expert knowledge and extensive manual iteration / 专家知识和大量人工迭代**：先交代实际代价。依赖专家、人工迭代慢，是自动化要解决的代价。这样下一句介绍生成模型才有来由。
3. **pave the way for automated building design generation / 为建筑设计的自动生成铺平了道路**：进展接到具体任务。可控生成与多模态生成落到建筑设计，范围没跑远。接下来要写已有方法能做什么，再谈缺口。

[GreenPlanner · CVPR Findings 2026](https://openaccess.thecvf.com/content/CVPR2026F/html/Zeng_GreenPlanner_Practical_Floorplan_Layout_Generation_via_an_Energy-Aware_and_Function-Feasible_CVPRF_2026_paper.html) · §1 Introduction，第一自然段，p.8596

英文保持原文，仅还原 PDF 换行、断词与字体连字。中文、高亮和旁批为本指南添加；保留原文引文编号。

原权利人保留版权；CVF Open Access 未声明 CC BY。本指南仅作署名教学短引，不重新发布全文或原图，不向第三方转授原论文版权。

<a id="annotated-intro-comparison"></a>

#### 已有能力与研究缺口

高亮与旁批按颜色和编号对应；点击切换中英。

**English 原文**

To enable automation, prior works have employed conditioned generators [22, 31, 37, 38, 44, 48, 49, 59, 60, 63, 64] that translate coarse user requirements into concrete floorplan layouts. However, existing methods rely solely on user-specified conditions and thus often violate unspecified real-world design constraints. This neglect results in over 60% of samples in existing datasets [48] being practically unusable due to excessive energy use and flawed spatial-functional design. Some methods [38, 44] even fail to generate essential structural components such as windows, leading to unrealistic energy evaluations. Therefore, enforcing design constraints in generative models remains a major bottleneck for practical deployment.


**中文译文**

为实现自动化，已有工作采用条件生成器 [22, 31, 37, 38, 44, 48, 49, 59, 60, 63, 64]，将用户的粗略需求转为具体平面布局。然而，现有方法仅依赖用户明确给出的条件，因此往往违反未被明确提出的现实设计约束。这种忽视使现有数据集 [48] 中超过 60% 的样本因能耗过高、空间与功能设计不合理而无法实际使用。一些方法 [38, 44] 甚至无法生成窗户等必要结构，导致能耗评估不符合现实。因此，在生成模型中落实设计约束，仍是实际部署的主要瓶颈。


**高亮与旁批**

1. **translate coarse user requirements into concrete floorplan layouts / 将用户的粗略需求转为具体平面布局**：比较别换对象。输入是粗略需求，输出是平面布局。后面的不足围绕这个任务展开，不能突然换比较对象。
2. **violate unspecified real-world design constraints / 违反未被明确提出的现实设计约束**：缺口要有实际后果。关键是用户没说、现实仍要求满足的约束。后面用能耗、空间功能和窗户说明漏掉它们会怎样。
3. **enforcing design constraints in generative models / 在生成模型中落实设计约束**：后文要接住这个问题。末句回扣设计约束。方法接下来要解释约束从哪里来、怎样进入生成过程，不能只报组件名。

[GreenPlanner · CVPR Findings 2026](https://openaccess.thecvf.com/content/CVPR2026F/html/Zeng_GreenPlanner_Practical_Floorplan_Layout_Generation_via_an_Energy-Aware_and_Function-Feasible_CVPRF_2026_paper.html) · §1 Introduction，第二自然段，p.8596

英文保持原文，仅还原 PDF 换行、断词与字体连字。中文、高亮和旁批为本指南添加；保留原文引文编号。

原权利人保留版权；CVF Open Access 未声明 CC BY。本指南仅作署名教学短引，不重新发布全文或原图，不向第三方转授原论文版权。

<details><summary>结构模板</summary>


#### 贡献列表

```latex
In summary, our contributions are:
\begin{itemize}
    \item We propose [core contribution] to [research objective].
    \item We design [mechanism] that [specific operation].
    \item We introduce [evaluation] for [what it checks].
    \item Experiments across [scope] reveal [specific finding].
\end{itemize}
```

</details>


<a id="related"></a>
<a id="chapter-related"></a>
### 3.5 相关工作

说明已有路线、本文差异及其与核心贡献的关系。

#### 本节原则

- 按共同任务或机制分组，解释各路线怎样工作。先承认已有能力，再比较真正相近的工作。
- 每个小节的末尾固定这样写：However, [现有方法在具体范围内的局限]. To address this limitation, we [对应设计及作用]. 两句紧接，不夹一句空泛总结。
- However 的问题名称、对象与范围直接对齐 Intro；解决句也对齐 Intro 的方案。不同小节负责不同缺口。
- 不足要能回查原论文。未报告不等于没有；仅测单轮，不等于多轮一定失败。客观限定范围，不夸大缺陷。
- 引用按相关性选，不设篇数配额，也不因方法相似而漏引。可直接比较的近邻安排基线；设置不同就讲清差异。

<a id="annotated-related-closure"></a>

#### 局限与对应解法

教学示范；[A]、[B] 及其评价范围均是假设。正式写作先核验原论文，再替换路线、范围与引用。

**English 教学改写**

Evidence-grounded dialogue systems select supporting text before generating an answer. [A] retrieves passages for the current question, whereas [B] links retrieved passages to answer claims [citations]. These claim links make support easier to inspect, but [B] is evaluated only on isolated questions. However, these comparisons do not establish whether earlier constraints remain satisfied across dialogue turns. To address this limitation, we attach dialogue constraints to evidence notes and test their retention across turns.


**中文译文**

基于证据的对话系统先筛选支持文本，再生成答案。[A] 为当前问题检索片段，[B] 则把检索片段与答案主张关联[引用]。这些主张关联便于检查依据，但 [B] 的评价仅覆盖独立问题。然而，这些比较尚未说明前文约束能否在多轮对话中持续得到满足。为解决这个不足，我们把对话约束绑定到证据笔记，并检验约束在多轮中的保留情况。


**高亮与旁批**

1. **retrieves passages for the current question, whereas [B] links retrieved passages to answer claims / 为当前问题检索片段，[B] 则把检索片段与答案主张关联**：分类有共同尺度。比较支持文本怎样组织：只检索片段，还是关联到主张。不是每句换一个作者名字。
2. **These claim links make support easier to inspect / 这些主张关联便于检查依据**：先承认已有能力。说明关联主张带来的用途。后面的不足限定在跨轮评价，不否定这一已有能力。
3. **However, these comparisons do not establish whether earlier constraints remain satisfied across dialogue turns. / 然而，这些比较尚未说明前文约束能否在多轮对话中持续得到满足。**：However：说清哪项问题没被回答。接回上一句的独立问题评价，限定为未检验跨轮约束。不能偷换成“这些方法无法处理多轮”。
4. **To address this limitation, we attach dialogue constraints to evidence notes and test their retention across turns. / 为解决这个不足，我们把对话约束绑定到证据笔记，并检验约束在多轮中的保留情况。**：紧跟解法：同一个缺口，同一个对象。跨轮约束缺少检验→绑定约束并检验保留情况。这一设计也必须出现在 Intro、Method 和实验中。

PaperBank · 教学改写

本段为 PaperBank 原创教学示范。路线、评价范围与方法均为假设，不能直接当作文献综述使用。

本指南原创内容采用 CC BY 4.0；转载请附作者、原文链接与许可，改写注明改动。

<a id="annotated-related"></a>

#### 方法比较

高亮与旁批按颜色和编号对应；点击切换中英。

**English 原文**

Multi-dancer generation is an emerging area currently in its nascent stage. To the best of our knowledge, only a handful of studies (Yao et al. 2023; Le et al. 2023b,a; Yang et al. 2024) have focused on generating scenarios for more than two dancers. Among these, GDanceR (Le et al. 2023b) and GCD (Le et al. 2023a) utilize no special structures to avoid the imbalance issue in motion representation, resulting in a tendency for dancer ambiguity. CoDancers (Yang et al. 2024) splits group motions into single-person motions, preventing the occurrence of dancer ambiguity. However, completely isolating individual features results in incomplete group information, which leads to disharmony generation results. Therefore, a more optimal feature separation strategy is necessary. In this work, we introduce TCDiff, a method that first generates dancers’ trajectories and then produces logical movements. Together with our proposed effective plugin, Fusion Projection, this approach significantly reduces dancer ambiguity.


**中文译文**

多舞者生成是一个仍处于早期的新兴方向。据我们所知，只有少量研究（Yao et al. 2023; Le et al. 2023b,a; Yang et al. 2024）关注超过两名舞者的场景。其中，GDanceR（Le et al. 2023b）和 GCD（Le et al. 2023a）没有采用专门结构来避免运动表示的不平衡，因而容易出现舞者混淆。CoDancers（Yang et al. 2024）将群体动作拆成单人动作，避免了舞者混淆。然而，完全隔离个体特征会造成群体信息不完整，进而导致生成结果不协调。因此，需要更合适的特征分离策略。本文提出 TCDiff，先生成舞者轨迹，再生成合乎逻辑的动作。该做法结合我们提出的有效插件 Fusion Projection，显著减少了舞者混淆。


**高亮与旁批**

1. **utilize no special structures to avoid the imbalance issue in motion representation, resulting in a tendency for dancer ambiguity / 没有采用专门结构来避免运动表示的不平衡，因而容易出现舞者混淆**：先统一比较维度。两项工作按表示机制归类，有共同尺度。“表示不平衡→舞者混淆”仍需定义或文献依据。
2. **splits group motions into single-person motions / 将群体动作拆成单人动作**：承认别人解决了什么。先承认拆成单人动作处理了舞者混淆，再谈代价。后文才说得清本文要同时保留什么。
3. **completely isolating individual features results in incomplete group information / 完全隔离个体特征会造成群体信息不完整**：代价接上了，对象还可更具体。不足来自前一句的完全隔离，逻辑接得上。但“群体信息”仍宽泛；写自己的论文时应指出缺哪种关系。
4. **a more optimal feature separation strategy is necessary / 需要更合适的特征分离策略**：“更合适”还不够。收尾应说清需要兼顾个体区分与群体协调。“更合适的策略”本身不能代替设计目标。
5. **first generates dancers’ trajectories and then produces logical movements / 先生成舞者轨迹，再生成合乎逻辑的动作**：操作还要解释作用。先轨迹、后动作给出顺序，还需说明怎样回应前面的两种代价。Fusion Projection 也要讲机制，不能只写 effective。

[TCDiff · AAAI 2025](https://ojs.aaai.org/index.php/AAAI/article/view/32268) · Related Work / Music-driven Multi-dancer Generation，p.2646

英文保持原文段落，仅合并换行、还原排版断词与字体连字，规范引文括号空白；高亮和批注为本指南添加。中文为本指南翻译，不是作者原文。 保留原文全部作者年份引文。

作者教学复用；原论文英文短引与原图不受 PaperBank 原创内容 CC BY 授权覆盖。本文不转授第三方转载原论文材料的权利。

<details><summary>结构模板</summary>


#### 相关工作模板

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

</details>


<a id="method"></a>
<a id="chapter-method"></a>
### 3.6 方法

铁律：告诉读者为什么你的方法好，比解释清楚方法更重要。

#### 本节原则

- 铁律：为什么你的方法好，比解释清楚方法更重要。每项关键设计接回 Intro 的具体困难，再讲怎样实现。
- 任务定义写清实际输入、要求输出和约束；训练、推理、评价能看到的信息分开，符号随计算引入。
- Overview 先讲核心思路，再按真实依赖说明各节作用、输入和产物。章节名是阅读位置，不是处理者；每个章节名与节号只出现一次，框架图对应实际操作。
- 模块首句用 To + 具体目的。随后解释设计依据、关键操作与必要公式，末句交代产物给谁用。
- 自己的设计占主要篇幅。标准编码、格式转换简写；参数、长 prompt 和部署细节放可定位的附录。
- 公式说明对象、单位、下标、信号来源与更新对象；并行、循环、反馈不能硬写成顺序流水线。
- Overview 先接回 Intro 的具体局限，再概括各阶段怎样交接；每个小节开头说明本步目的，结尾交代输出怎样供下一步使用。

<a id="annotated-method-task"></a>

#### 任务定义

教学改写；示例方法与实验设置仅用于说明写法，不是已发表论文原文或实测结果。

**English 教学改写**

Given a question, the dialogue history, and a collection of English manuals, the task is to generate an answer that respects earlier constraints and cites supporting passages. At inference time, the system receives these inputs but no reference answer. We use reference answers only for evaluation. A prior requirement such as offline operation remains part of the task unless the user explicitly changes it.


**中文译文**

给定一个问题、它的对话历史和一组英语手册，任务是生成遵守前文约束、附有支持片段引用的回答。推理时，系统接收这些输入，但不接收参考答案。参考答案仅用于评价。离线操作等前文要求仍属于当前任务，除非用户明确更改。


**高亮与旁批**

1. **Given a question, the dialogue history, and a collection of English manuals / 给定一个问题、它的对话历史和一组英语手册**：输入先落到对象。问题、历史和手册是不同输入。读者先知道系统拿到了什么，再看符号。
2. **respects earlier constraints and cites supporting passages / 遵守前文约束、附有支持片段引用**：输出不只报名字。回答要满足哪两项要求，直接在任务定义里说。后面的指标也应检验这两件事。
3. **no reference answer / 不接收参考答案**：划清可见信息。评价参照不等于推理输入。图中也不能把参考答案连进生成器。
4. **unless the user explicitly changes it / 除非用户明确更改**：边界说具体。旧约束何时有效，给出规则；不要让模型或读者自行猜。

PaperBank · 教学改写

独立教学示例，使用静态手册问答说明组织方式，不对应私有项目。

本指南原创内容采用 CC BY 4.0；转载请附作者、原文链接与许可，改写注明改动。

<a id="annotated-method-overview-teaching"></a>

#### 方法概述

教学改写；示例方法与实验设置仅用于说明写法，不是已发表论文原文或实测结果。

**English 教学改写**

To retain earlier constraints during answering, we connect quoted evidence to the dialogue history before generating an answer. In History-aware Retrieval (Sec. [retrieval]), we select manual passages relevant to the current question and earlier requirements. Using these passages, in Constraint-linked Notes (Sec. [notes]), we attach the requirements to source quotes and retain their manual locations. Finally, in Grounded Answering (Sec. [answering]), the generator uses the resulting notes to produce an answer with source citations. Figure [framework] shows these dependencies.


**中文译文**

为在回答中保留前文约束，我们先把摘录证据与对话历史关联，再生成答案。在历史感知检索（第[retrieval]节）中，我们筛选与当前问题及前文需求相关的手册片段。使用这些片段，我们在约束关联笔记（第[notes]节）中将需求绑定到来源摘句，并保留手册位置。最后，在基于证据的回答（第[answering]节）中，生成器使用所得笔记生成带来源引用的答案。图[framework]展示这些依赖关系。


**高亮与旁批**

1. **To retain earlier constraints during answering / 为在回答中保留前文约束**：先讲为什么。接回 Intro 的约束丢失问题。读者先知道设计目的，再看章节位置。
2. **In History-aware Retrieval (Sec. [retrieval]), we select / 在历史感知检索（第[retrieval]节）中，我们筛选**：章节负责导航，we 执行操作。小节名与节号只出现一次。不是“这个章节检索了文本”；实际处理者是系统或作者。
3. **Using these passages / 使用这些片段**：接住上一节的产物。检索出的片段进入笔记构建。串行、并行或反馈按实际依赖写，不能为了顺口编先后。
4. **the generator uses the resulting notes / 生成器使用所得笔记**：再把笔记交给生成器。当前产物成为下一步输入。“先 A 再 B”还不够，要说明 B 使用 A 的什么。
5. **Figure [framework] shows these dependencies. / 图[framework]展示这些依赖关系。**：图与正文对上。填真实图号；框架图画出片段→笔记→答案的依赖，不只排三个模块名。

PaperBank · 教学改写

独立教学示例，使用静态手册问答说明组织方式，不对应私有项目。

本指南原创内容采用 CC BY 4.0；转载请附作者、原文链接与许可，改写注明改动。

<a id="annotated-method-module"></a>

#### 组件设计

教学改写；示例方法与实验设置仅用于说明写法，不是已发表论文原文或实测结果。

**English 教学改写**

To keep earlier requirements available during answering, the note builder links each retrieved quote to the relevant dialogue constraint. A retrieved passage may describe a feature correctly yet be unsuitable for an offline-only request. For each quote, we record the manual location and the constraint supported or contradicted by the quote; an unverified relation is left unresolved. The generator then receives these notes together with the current question, so the answer can cite the source and explain whether the requirement is met.


**中文译文**

为让回答阶段仍能使用前文要求，笔记构建器将每条检索摘句与相关对话约束关联。一个片段可能准确描述功能，却不适用于仅限离线的请求。对每条摘句，我们记录它在手册中的位置，以及它支持或违背的约束；尚未核验的关系保留为未确定。生成器随后接收这些笔记和当前问题，以便回答引用来源，并解释要求是否满足。


**高亮与旁批**

1. **To keep earlier requirements available during answering / 为让回答阶段仍能使用前文要求**：目的顶在第一句。To 后写具体目的，主句给执行者与关键设计。别先讲半段背景。
2. **unsuitable for an offline-only request / 不适用于仅限离线的请求**：解释为什么要这样做。“事实正确”不等于“符合需求”。矛盾明确，设计才有必要性。
3. **the manual location and the constraint supported or contradicted by the quote / 它在手册中的位置，以及它支持或违背的约束**：操作落实到字段。谁处理什么、保留哪些信息写清楚，后面的表示或公式才有内容。
4. **an unverified relation is left unresolved / 尚未核验的关系保留为未确定**：处理边界情况。不知道的关系不能自动写成支持或冲突；需要有明确处理规则。
5. **receives these notes together with the current question / 接收这些笔记和当前问题**：末句交给下一步。写明产物、接收者和用途；这里是目标能力，不能伪装成实测提升。

PaperBank · 教学改写

独立教学示例，使用静态手册问答说明组织方式，不对应私有项目。

本指南原创内容采用 CC BY 4.0；转载请附作者、原文链接与许可，改写注明改动。

<a id="annotated-method"></a>

#### 组件衔接

高亮与旁批按颜色和编号对应；点击切换中英。

**English 原文**

We propose GreenPlanner, an energy- and functionality-aware generative framework for residential design (Fig. 2). It integrates four components: (1) Design Feasibility Dataset (DesignFD), a dataset built from RPLAN [48] via expert-verified energy and functional evaluations; (2) Practical Design Evaluator (PDE), a predictor trained on DesignFD for fast simulation of energy and functional feasibility; (3) Green Plan Dataset (GreenPD), a PDE-guided dataset pairing user requirements with regulation-compliant layouts; and (4) GreenFlow, a generator trained on GreenPD with PDE feedback for controllable, constraint-grounded layout generation. We next describe each component of the framework in detail.


**中文译文**

我们提出 GreenPlanner，一套同时考虑能耗与功能的住宅设计生成框架（图 2）。该框架集成四个组件：（1）设计可行性数据集（DesignFD），由 RPLAN [48] 经专家核验的能耗与功能评估构建；（2）实用设计评估器（PDE），在 DesignFD 上训练，用于快速模拟能耗与功能可行性；（3）绿色规划数据集（GreenPD），由 PDE 引导，将用户需求与符合规范的布局配对；（4）GreenFlow，在 GreenPD 上训练并使用 PDE 反馈，生成可控且以约束为依据的布局。下面将详细介绍框架的各个组件。


**高亮与旁批**

1. **an energy- and functionality-aware generative framework for residential design / 一套同时考虑能耗与功能的住宅设计生成框架**：接回 Intro 的两类缺口。能耗与功能对应前文的问题。Overview 要说明设计为何针对这些问题，不能只复述方法名称。
2. **expert-verified energy and functional evaluations / 经专家核验的能耗与功能评估**：好词要有具体工作撑着。expert-verified 比“高质量”具体。数据章节仍要解释谁核验、核验什么、怎样处理分歧。
3. **a predictor trained on DesignFD for fast simulation of energy and functional feasibility / 在 DesignFD 上训练，用于快速模拟能耗与功能可行性**：依赖清楚，效果还需证据。DesignFD 成为预测器的训练数据，两个组件接上了。fast 是效果声明，要在效率实验中给依据。
4. **a PDE-guided dataset pairing user requirements with regulation-compliant layouts / 由 PDE 引导，将用户需求与符合规范的布局配对**：说明产物，也解释条件。PDE 引导构建需求—布局配对。regulation-compliant 需要后文说明采用哪些规范、怎样检查。
5. **a generator trained on GreenPD with PDE feedback / 在 GreenPD 上训练并使用 PDE 反馈**：这两条路径也要画出来。GreenPD 提供训练数据，PDE 提供反馈。对照 Fig. 2 检查两条路径，不能正文有反馈、图里没有。

[GreenPlanner · CVPR Findings 2026](https://openaccess.thecvf.com/content/CVPR2026F/html/Zeng_GreenPlanner_Practical_Floorplan_Layout_Generation_via_an_Energy-Aware_and_Function-Feasible_CVPRF_2026_paper.html) · §3 Method，开头自然段，p.8597

英文保持原文段落，仅合并换行、还原排版断词与字体连字，规范引文括号空白；高亮和批注为本指南添加。中文为本指南翻译，不是作者原文。 保留原文组件编号、Fig.2 与引文 [48]，仅清理 PDF 提取产生的标点空白。

原权利人保留版权；CVF Open Access 未声明 CC BY。本指南仅作署名教学短引，不重新发布全文或原图，不向第三方转授原论文版权。

<details><summary>结构模板</summary>


#### 方法概述模板

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

</details>


<a id="experiments"></a>
<a id="chapter-experiments"></a>
### 3.7 实验

用对照检验贡献，解释主要差异与发现。

#### 本节原则

- 先把 Intro 的核心主张变成可检验的问题，再安排主结果、消融和必要的扩展实验。RQ 是组织工具，不必每表编号。
- 设置按 Metrics、Baselines、Implementation Details 分组。指标写定义、方向、分母、汇总与无效输出处理；基线按路线介绍。
- 对齐会改变结果的条件。写清数据版本与划分、训练和推理预算、参数选择、重复单位，以及人工或模型 judge 的核验方式。
- 结果段先加粗一句具体发现，再给关键对照与意义。不要逐行读表；收益、代价和负结果都要解释。
- 消融一次删除或替换一个因素，固定其他条件。多项一起改，只能评价整套改动，不能把收益归给其中一项。
- 扩展实验围绕实际主张选取；效率算端到端成本，稳定性报告重复变化。个例解释过程，不能代替总体证据。
- 段首先接回 Intro 的研究问题或 Method 的设计动机，再报告发现、关键对照及图表依据；分析最后说明原问题回答到了哪一步。
- Intro 中的每项核心设计都应能找到对应检验。只得到整套方法的结果时，不把收益单独归给未经检验的模块。

<a id="annotated-experiments-metrics"></a>

#### 指标定义

教学改写；示例方法与实验设置仅用于说明写法，不是已发表论文原文或实测结果。

**English 教学改写**

To test whether evidence notes improve citation support, we evaluate multi-turn questions about static English manuals. Human raters check each factual answer sentence against its cited passage using a shared rule. A sentence without a citation counts as unsupported. For each question, citation support is the fraction of factual sentences supported by their cited evidence; higher is better. We average these per-question fractions rather than pooling sentences across questions. Answers with no factual sentences are reported separately as not applicable, together with their count.


**中文译文**

为检验证据笔记能否提高引用支持率，我们评价针对静态英语手册的多轮问题。指标。人工按同一规则检查每句事实能否由所引片段支持。没有引用的句子按不支持计。对每个问题，引用支持率是获所引证据支持的事实句比例，越高越好。我们对各问题的比例取平均，不把所有问题的事实句混在一起计算。没有事实句的回答单列为不适用，并报告数量。


**高亮与旁批**

1. **To test whether evidence notes improve citation support / 为检验证据笔记能否提高引用支持率**：问题接回方法作用。先说这组评价要检验什么，不能从设备型号开始。
2. **Human raters check each factual answer sentence / 人工按同一规则检查每句事实**：谁判什么。人工、判定单位与证据对象都可定位。完整说明和一致性核验另给实际记录。
3. **A sentence without a citation counts as unsupported. / 没有引用的句子按不支持计。**：缺失也进入口径。缺引用不能从分母中静默排除，否则少给引用反而可能得高分。
4. **We average these per-question fractions rather than pooling sentences across questions. / 我们对各问题的比例取平均，不把所有问题的事实句混在一起计算。**：说明怎样汇总。先按问题计算再平均，与把所有句子合并计算不同；长回答不会只因句子多而权重更大。
5. **reported separately as not applicable / 单列为不适用**：定义不能评分的情形。没有事实句时，比例无定义。不能自动算零或算满分，还要报告数量。

PaperBank · 教学改写

独立教学示例，使用静态手册问答说明组织方式，不对应私有项目。

本指南原创内容采用 CC BY 4.0；转载请附作者、原文链接与许可，改写注明改动。

<a id="annotated-experiments-main-teaching"></a>

#### 主结果

假设主结果段；比较与结果方向仅用于教学，实际须填核验后的差值、表号及统计范围。

**English 教学改写**

Evidence notes improve citation support under a fixed evidence-context budget. In the comparison in Table [main], the note-based system has higher support than direct passage retrieval when the language model, decoding settings, and evidence-context token budget are held fixed. The contrast supports note-guided generation as a whole; separate ablations are needed to distinguish quote organization from constraint retention. However, the note builder adds processing time, so the quality gain must be considered together with end-to-end latency.


**中文译文**

在证据上下文预算固定时，证据笔记提高了引用支持率。在表[主结果]所示的对照中，固定语言模型、解码设置和证据上下文词元预算后，笔记系统的支持率高于直接片段检索。这一对照支持该设置下的笔记引导生成整体；区分摘句组织与约束保留的作用，还需要分别消融。不过，笔记构建增加了处理时间，因此质量收益需要与端到端延迟一起考虑。


**高亮与旁批**

1. **Evidence notes improve citation support under a fixed evidence-context budget. / 在证据上下文预算固定时，证据笔记提高了引用支持率。**：段首先给一个发现。可加粗；对象、比较关系和条件明确。“实验效果很好”没有信息。
2. **the language model, decoding settings, and evidence-context token budget are held fixed / 固定语言模型、解码设置和证据上下文词元预算后**：关键对照撑起结论。模型、解码和上下文预算对齐。预算上限相同，不等于实际长度或信息完全相同；组件归因还需匹配消融。
3. **supports note-guided generation as a whole / 支持该设置下的笔记引导生成整体**：解释证据的意义。主结果比较整套系统；只对齐预算，不能宣称已经隔离某个组件或信息类型的作用。
4. **the note builder adds processing time / 笔记构建增加了处理时间**：代价跟收益一起说。效率不是只算生成器；端到端延迟应计入检索、笔记构建与生成。

PaperBank · 教学改写

独立教学示例，使用静态手册问答说明组织方式，不对应私有项目。

本指南原创内容采用 CC BY 4.0；转载请附作者、原文链接与许可，改写注明改动。

<a id="annotated-experiments-ablation"></a>

#### 消融分析

教学改写；示例方法与实验设置仅用于说明写法，不是已发表论文原文或实测结果。

**English 教学改写**

To examine the role of retained dialogue constraints, we remove those constraints from the notes while keeping source quotes unchanged. Both variants use the same language model, test questions, decoding settings, and maximum evidence-context budget. If constraint satisfaction decreases after this single change, the comparison supports retaining constraints in the tested setting. The comparison does not isolate the benefit of the entire note-building pipeline, because source selection and quotation remain active in both variants.


**中文译文**

为检验保留对话约束的作用，我们从笔记中移除这些约束，保留来源摘句。两种设置使用相同的语言模型、测试问题、解码设置和证据上下文预算上限。若这项单一改动后约束满足率下降，该比较支持在实测设置中保留约束有用。它不能单独确定整套笔记构建流程的收益，因为两种设置都仍在进行来源选择和摘句。


**高亮与旁批**

1. **To examine the role of retained dialogue constraints / 为检验保留对话约束的作用**：对准一项设计。消融目的应对应 Method 声称的作用，不是列一排 w/o 标签。
2. **remove those constraints from the notes while keeping source quotes unchanged / 从笔记中移除这些约束，保留来源摘句**：只改待检验因素。去掉约束，来源摘句保留。若同时改检索器或模型，就不能把差异归给约束。
3. **the same language model, test questions, decoding settings, and maximum evidence-context budget / 相同的语言模型、测试问题、解码设置和证据上下文预算上限**：其余条件给清楚。预算上限相同不代表实际词元数相同；正式实验仍要核对长度是否构成替代解释。
4. **If constraint satisfaction decreases after this single change / 若这项单一改动后约束满足率下降**：没有结果就不编发现。这里是条件句教学。正式结果段应替换为真实差异及统计范围。
5. **does not isolate the benefit of the entire note-building pipeline / 不能单独确定整套笔记构建流程的收益**：归因范围与改动一致。当前比较只检验保留约束，未单独识别检索、摘句等其他步骤的作用。

PaperBank · 教学改写

独立教学示例，使用静态手册问答说明组织方式，不对应私有项目。

本指南原创内容采用 CC BY 4.0；转载请附作者、原文链接与许可，改写注明改动。

<a id="annotated-experiments-ablation-source"></a>

#### 组件效果

论文原文整段 · 中文为本指南翻译；高亮与旁批按颜色和编号对应。

**English 原文**

We highlight the importance of natural footwork in enhancing visual aesthetics (Tseng, Castellon, and Liu 2023). As shown in Table 3, our Footwork Adaptor markedly enhances the model’s PFC value. Moreover, when utilized independently, it boosts the model’s GMC, underscoring the FA’s dual benefits: preventing foot slipping and augmenting dance coherence.


**中文译文**

我们强调自然脚步对提升视觉美感的重要性（Tseng、Castellon 与 Liu，2023）。如表 3 所示，Footwork Adaptor 明显改善了模型的 PFC 指标。此外，单独使用该模块时，它也提高了模型的 GMC，体现出 FA 的双重作用：减少脚部滑动，并增强舞蹈协调性。


**高亮与旁批**

1. **natural footwork in enhancing visual aesthetics / 自然脚步对提升视觉美感**：动机说明为何要测。自然脚步对应本文的脚部滑动问题。按现行结果写法，可先给主发现，再用这句解释其意义。
2. **As shown in Table 3 / 如表 3 所示**：证据位置直接给出。表中有 w/o FA、w/o FP 和组合消融；说明模块作用前，先找能只改变 FA 的匹配对照。
3. **enhances the model’s PFC value / 改善了模型的 PFC 指标**：指标先知道方向。PFC 是脚部接触相关指标，表中越低越好。改善不能误译为数值提高。
4. **when utilized independently / 单独使用该模块时**：单独作用要有对应行。对应 w/o FA and FP 与 w/o FP 的比较；两行都没有 FP，只增减 FA。不能拿多项同时变化的两行归因。
5. **preventing foot slipping and augmenting dance coherence / 减少脚部滑动，并增强舞蹈协调性**：两项作用分别给证据。PFC 对应脚步，GMC 对应群体协调。若篇幅允许，按一段一个核心发现分开分析。

[TCDiff · AAAI 2025](https://ojs.aaai.org/index.php/AAAI/article/view/32268) · §Ablation Study，Effectiveness of Footwork Adaptor，自然段；PDF p.7，proceedings p.2651；Table 3

英文保持原文，仅合并换行、还原排版断词，并移除粗体段标题；中文为本指南翻译。英文原文包含 PFC 与 GMC 的两项作用，教学批注明确各自的指标和对照，不改原句。

作者教学复用；原论文英文短引与原图不受 PaperBank 原创内容 CC BY 授权覆盖。本文不转授第三方转载原论文材料的权利。

<a id="discussion"></a>
<a id="chapter-discussion"></a>
### 3.8 讨论与局限

解释发现，写清适用范围和局限。

#### 本节原则

- 解释结果改变了什么认识，不再复述成绩表。结论保留实际测试范围。
- 解释与机制分开。没有单独控制某项设计，就不能把效果全部归因于它。
- 局限写具体条件：哪些数据、语言、信息或预算尚未覆盖。未测试不等于已失败。
- 未来工作接当前局限，说明补哪项验证，不空写更多数据、更大模型。

<a id="annotated-discussion"></a>

#### 结果解释与局限

假设教学段落，非论文原文或实测结果。

**English 教学改写**

Higher citation support is consistent with more explicit use of document evidence. However, the current comparison changes both quote organization and the amount of constraint information provided to the generator. The comparison therefore cannot identify which change accounts for the gain. Our evaluation covers static English manuals; cross-language questions and frequently updated documents remain untested. Separate evaluations are needed because language and document updates can change which quoted evidence supports an answer.


**中文译文**

引用支持率提高，与更明确地使用文档证据这一解释相符。然而，当前比较同时改变了摘句的组织方式和提供给生成器的约束信息量。因此，这个比较不能判断哪项改变带来了收益。当前评价覆盖静态英语手册；跨语言问题与频繁更新的文档尚未检验。这些设置需要另行评价，因为语言与文档更新可能改变哪些摘句能够支持答案。


**高亮与旁批**

1. **is consistent with more explicit use of document evidence / 与更明确地使用文档证据这一解释相符**：先说结果的意义。consistent with 表示解释与观察相符，尚未声称已证明机制。意义仍限于来源支持。
2. **changes both quote organization and the amount of constraint information provided to the generator / 同时改变了摘句的组织方式和提供给生成器的约束信息量**：写清替代解释。两项条件同时变化，就不能只把提升归给笔记组织。局限应指出实际没区分什么。
3. **The comparison therefore cannot identify which change accounts for the gain. / 因此，这个比较不能判断哪项改变带来了收益。**：However 之后要得出真实限制。前句说明两项条件同时变化，这句限定归因范围。Therefore 接住原因，不是只在句首加一个词。
4. **cross-language questions and frequently updated documents remain untested / 跨语言问题与频繁更新的文档尚未检验**：范围要具体。语言变化和文档更新是两个尚未测的设置。写出来，比一句 limited generalizability 有用。
5. **because language and document updates can change which quoted evidence supports an answer / 因为语言与文档更新可能改变哪些摘句能够支持答案**：未来工作说明为什么必要。下一步不是随手扩大任务，而是检查证据支持关系是否仍成立。

PaperBank · 教学改写

沿用文档问答的假设任务，展示信息顺序与论证作用，不代表新增研究结果。

本指南原创内容采用 CC BY 4.0；转载请附作者、原文链接与许可，改写注明改动。

<a id="conclusion"></a>
<a id="chapter-conclusion"></a>
### 3.9 结论

回答开头的问题，概括贡献和发现。

#### 本节原则

- 先回答引言的问题，再概括最重要的设计与发现。
- 只收束正文已经建立的认识，不新增结果、对照或能力。
- 保留关键取舍和适用范围。未来方向接实际局限，不重复整套方法流程。

<a id="annotated-conclusion"></a>

#### 结论结构

公开预印本原文段落 · 中文为本指南翻译

**English 原文**

We present EviNote-RAG, a framework that introduces a note-taking step to extract answer-supportive evidence before answering. By training LLMs to produce Supportive-Evidence Notes (SENs) and guiding them via a tailored entailment-based reward, our approach improves answer accuracy. Extensive experiments demonstrate that EviNote-RAG achieves state-of-the-art performance while enhancing training stability.


**中文译文**

我们提出 EviNote-RAG，在回答前加入笔记步骤，提取能够支持答案的证据。通过训练 LLM 生成能够支持答案的证据笔记（SENs），并用专门设计的蕴含奖励引导模型，方法提高了答案准确率。大量实验表明，EviNote-RAG 达到当前最优表现，同时改善了训练稳定性。


**高亮与旁批**

1. **a framework that introduces a note-taking step to extract answer-supportive evidence before answering / 在回答前加入笔记步骤，提取能够支持答案的证据**：先收束核心设计。一句话说清新增步骤、处理对象和目的，不重新展开完整流程。
2. **By training LLMs to produce Supportive-Evidence Notes (SENs) and guiding them via a tailored entailment-based reward / 通过训练 LLM 生成能够支持答案的证据笔记（SENs），并用专门设计的蕴含奖励引导模型**：说明设计怎样发挥作用。笔记明确训练目标，奖励引导模型形成这类笔记。这里概括共同作用，不把两个设计写成未经核验的执行先后。
3. **achieves state-of-the-art performance while enhancing training stability / 达到当前最优表现，同时改善了训练稳定性**：结尾回到已有证据。原文用性能与训练稳定性收束。state-of-the-art 只对应发表时的比较；自己的论文要核对基线与条件，不能照搬这个评价。

[EviNote-RAG · arXiv v3 公开预印本](https://arxiv.org/html/2509.00877v3#S5) · § 5 Conclusion，第一自然段（三句）；arXiv:2509.00877v3，2025-10-16；公开 HTML #S5。

摘录公开 arXiv v3 的 Conclusion 第一自然段，英文词句未改；中文翻译、高亮与旁批为本指南添加。

公开 arXiv v3 采用 non-exclusive distribution，原文版权由权利人保留。作者教学短引，不随本指南转授全文再版许可；中文翻译与分析为本指南新增。

<a id="references"></a>
<a id="chapter-references"></a>
### 3.10 参考文献

引用回查原文，信息和版本对齐。

#### 本节原则

- 引用支持附近的具体判断，先回查原文，不把搜索摘要或能编译的 BibTeX 当核验。
- 模型、数据、工具和外部方法在可独立阅读的章节首次实质出现时，就近引原始报告或官方文档。
- 条目与实际版本对应，核对题名、作者、年份和来源；同一论文的重复版本去重。
- 来源没测过的条件，不能用它支撑该条件下的结论。没有真实来源就缩小或删除说法。

<a id="annotated-references"></a>

#### 引用与主张

教学段落；方括号为来源与版本占位，不是假造文献条目。

**English 教学改写**

Retrieval-augmented generation combines retrieved passages with answer generation [primary method paper]. A study evaluated only on single-turn questions cannot establish performance on changing multi-turn constraints. We use [retriever and version] [official documentation for that version] to retrieve candidate passages. The method citation supports the approach; the version-specific documentation identifies the tool actually used.


**中文译文**

检索增强生成将检索到的段落与答案生成结合起来[原始方法论文]。只在单轮问题上评价的研究，不能证明方法能够处理多轮对话中变化的约束。我们使用[检索器与版本][该版本的官方文档]检索候选段落。方法引用说明采用哪条路线；对应版本的文档说明实际使用什么工具。


**高亮与旁批**

1. **[primary method paper] / [原始方法论文]**：方法回到原始来源。方括号是教学占位。填写核验过的原论文，不把博客、搜索摘要或转述当原始出处。
2. **A study evaluated only on single-turn questions cannot establish performance on changing multi-turn constraints. / 只在单轮问题上评价的研究，不能证明方法能够处理多轮对话中变化的约束。**：来源范围限制主张范围。一个来源真实存在，不等于它支持你附近写的每句话。任务条件也要对应。
3. **[retriever and version] [official documentation for that version] / [检索器与版本][该版本的官方文档]**：名称、版本、来源对应。工具或模型没有论文时，可以引用真实官方文档。不要用另一版本的报告补当前版本出处。
4. **The method citation supports the approach; the version-specific documentation identifies the tool actually used. / 方法引用说明采用哪条路线；对应版本的文档说明实际使用什么工具。**：别混淆引用的职责。方法来源与实际工具版本是两件事。引用准确后，还要核对运行记录是否采用这个版本。

PaperBank · 教学改写

用占位展示正文主张与真实来源的对应，不提供虚构作者、年份、题名或 DOI。

本指南原创内容采用 CC BY 4.0；转载请附作者、原文链接与许可，改写注明改动。

<a id="appendix"></a>
<a id="chapter-appendix"></a>
### 3.11 附录

提供可定位、可复核的设置与补充材料。

#### 本节原则

- 先删重复，再移次要细节。核心设计、关键证据和决定结论的限制留正文。
- 按技术细节、实验设置、补充结果等职责分组，不把所有剩余内容堆在一起。
- 正文在对应主张后指向具体节、图或表；附录每节先说补什么、服务哪项主张。
- 设置、符号、版本和统计范围与正文一致。补充结果改变主结论，正文同步说明。

<a id="annotated-appendix"></a>

#### 附录组织

假设教学段落，非论文原文或实测结果。

**English 教学改写**

To reproduce the citation-support comparison in Section [X], this appendix records the prompts, document versions, retrieval settings, and scoring rules for both systems. Each run is linked to the corresponding configuration and retains failed outputs. We select the maximum note length using development questions and freeze it before evaluating the test questions. Per-run scores and uncertainty estimates are reported in Table [Y], so the aggregate in the main text can be traced to the same runs.


**中文译文**

为复现第[X]节的引用支持率比较，本附录记录两个系统的提示词、文档版本、检索设置与评分规则。每次运行都关联对应配置，并保留失败输出。我们用开发集问题选择笔记最大长度，在评价测试问题前冻结这个选择。表[Y]报告各次运行得分与不确定性估计，使正文的汇总结果能追溯到同一批运行。


**高亮与旁批**

1. **To reproduce the citation-support comparison in Section [X] / 为复现第[X]节的引用支持率比较**：开头说明补什么。先点名服务哪个比较，读者不必回翻猜本节用途。正文也要指向这个具体附录节。
2. **for both systems / 两个系统的**：设置覆盖全部对照。只写自己的配置，不能复现比较。共享条件与不同条件要分别交代。
3. **using development questions and freeze it before evaluating the test questions / 用开发集问题选择笔记最大长度，在评价测试问题前冻结这个选择**：参数选择与测试分开。给出选择数据和冻结时点，说明参数如何确定。不能用最终测试结果倒选参数。
4. **so the aggregate in the main text can be traced to the same runs / 使正文的汇总结果能追溯到同一批运行**：附录与正文口径一致。补充表应对应正文统计，配置、运行与失败处理不能换一套范围。

PaperBank · 教学改写

沿用文档问答的假设任务，展示信息顺序与论证作用，不代表新增研究结果。

本指南原创内容采用 CC BY 4.0；转载请附作者、原文链接与许可，改写注明改动。

<a id="rebuttal"></a>
<a id="chapter-rebuttal"></a>
## 4. 审稿回复

[下载 rebuttal skill ZIP](../assets/rebuttal-skill.zip) · [SKILL.md](../skills/rebuttal/SKILL.md)：逐题回应、证据核对、revise loop 与 AC 总结。

用明确证据回答审稿人的具体关切。

首句回答原问题，再给证据、解释与位置；感谢简短，保持礼貌。

<a id="rebuttal-prepare"></a>
### 4.1 意见整理

读取完整 review：Summary 核对理解，Strengths 记录认可点，Weaknesses 与 Questions 提取待回应关切。

- 先查当轮 AI 与保密规定；确认材料可在所选工具中使用后，再提供稿件和 review。
- 保留原问题与顺序，一句话有多问就拆开。区分机制解释与实施情况，分别回应。
- 区分描述不清、缺对照和机制未证实；分别给案例、比较和针对性检验。
- 从原意见判断阅读关注点，不凭 confidence 猜身份或保证提分；查当轮回复规则。

<a id="rebuttal-answer"></a>
### 4.2 回复结构

首句直接回答问题，再给证据、解释与位置；流程问题用明确来源的案例展示。

- 标题沿用原问题；首句给结论或具体值。
- 给设置、对照、绝对值和指标方向；数据适合表格就用表格。
- 说明证据如何回答问题，附表号、节号或行号。
- 已有实验能回答就整理出来；缺关键证据时做能隔离争议的最小对照，不盲目把全部基线重跑。
- 感谢具体、简短。说明已经补出的内容，不用一句“我们将补充”代替答案。
- 一个段落回一个小点。表格写结果与必要设置差异，分析接回贡献；没有标准条件支持时不能把落后全归咎于不公平。

<a id="rebuttal-alternative"></a>
### 4.3 争议检验

准确复述审稿人的推理，用针对性对照检验争议前提，并说明证据支持的结论。

- 两种解释各预测什么？用什么实验分开？
- 无法区分就缩小机制主张；设计动机不能代替结果。

<a id="rebuttal-clarify"></a>
### 4.4 方法澄清

说明定义、真实输入与各步产物，定位争议环节；公式数量不能替代解释。

- 术语不清给定义，流程不清给案例，效果不清给对照。
- 确有错误就改；不同意就给依据。不以“你误读了”替代澄清与证据。

<a id="rebuttal-loop"></a>
### 4.5 迭代审核

按原问题逐轮检查覆盖、证据与逻辑，仅修改未通过的回复，再压缩文字并调整语气。

- 确认材料可在所选工具中使用后，再给 Codex 论文、原始 review、证据和回复。
- 逐题输出：原问题、回复位置、剩余缺口、改法、所需证据。
- 先查漏答、证据和逻辑，再缩文字、调语气。改完重查同一张问题清单。
- 每问有答、证据对应、逻辑通顺、篇幅合规就停；缺实验交给人决定。
- 模拟用于查漏洞，不预测评分变化或录用。

<a id="rebuttal-followup"></a>
### 4.6 后续回复与总结

先逐题回应，再向 AC 概括关键问题、证据与剩余分歧，准确引用已确认的评价。

- 追问接回原问题和证据，不重贴整份回复。
- 写清剩余限制，不猜未回复审稿人的态度。
- 不请求提分或接收，把判断留给审稿方。

**复制给 Codex：Rebuttal + revise loop**

```text
读取 rebuttal/SKILL.md 和 references/rules.md。
使用前：核对目标会议及 track 的 AI 规定，只在允许范围内起草、改写或绘图，按要求披露。确认材料使用权限和工具的数据处理方式；未获许可，不向外部服务上传未公开稿件、review、个人数据或密钥。
材料：【论文、完整 review、当前回复、已验证补充结果】
会议当轮规则：【字数／字符限制、补实验／链接／修订稿／AI 使用规定】
阶段：【初次／追问】；允许修改：【回复文件与范围】

1. 先保留 review 原文，逐条拆出 Summary、Weaknesses、Questions、建议和评分理由里的具体关切；Strengths 记录已认可点。列“原问题→需要的证据→现有依据与位置→缺口”，不按回复现有顺序漏问，不猜审稿人动机或水平。
2. 每问首句直接回答，随后给证据、解释和位置；问题标题忠于原意，感谢简短。数据、对照或成本适合表格就用紧凑表格，保留必要比较条件、数值口径与范围，不用文字重复每格。
3. 每个事实回到论文、原 review、真实结果或已确认推导。合理批评就承认并改，争议就查前提与证据；不隐藏影响比较的条件。补实验的承诺不能替代结果；缺结果交给我决定，不编数字、不把 future work 写成已完成，不自动跑实验或提交回复。
4. 执行 revise loop：按原问题清单查“原问题→回复位置→是否回答→证据是否匹配→剩余疑问→最小改法→还缺什么”。先修漏答、证据与逻辑，再压文字、调语气。只改不通过项，改后重查同一张清单，不盲目重跑全部基线。
5. 所有问题明确覆盖、事实与证据对应、逻辑通顺、长度和当轮政策合规后停止，由我定稿。证据不足就交回缺口，不通过模拟预测评分变化或录用。
6. 追问轮只答新增关切；AC 总结写关键问题、回应、证据与限制，不请求提分或接收。英文回复逐段附中文供我审，内部检查和缺口不混入提交文本。
```

依据：rebuttal · rebuttal-reviewer-simulator（通用证据核查规则） · [对应铁律与完整提示词](https://github.com/Da1yuqin/PaperBank/blob/main/skills/rebuttal/references/prompts.md#rebuttal)

<a id="tools"></a>
## 5. 辅助工具

按用途选。以下整理自公开文档，未逐项安装；版本和许可见原项目。

核对日期：2026-10-07。

### 5.1 文献检索与阅读

- **[AI-Powered Literature Review Skills](https://github.com/stephenlzc/AI-Powered-Literature-Review-Skills)：**检索、去重、逐篇分析，再组织综述。

README 的验证阶段包含基础元数据检查，不能替代全文核验；检索还取决于数据库访问权限和浏览器环境。
- **[沉浸式翻译](https://immersivetranslate.com/zh-Hans/)：**网页和 PDF 双语对照。

术语、否定和统计结论可能误译，关键内容回原文核对。安装和账户要求看官方文档。

[官方文档](https://immersivetranslate.com/docs/)
- **[Zotero 中文社区插件目录](https://zotero-chinese.com/plugins/)：**按任务和 Zotero 版本找插件。

社区目录与 Zotero 官方无从属关系；排行榜不是兼容性或安全审计。

[插件排行榜](https://zotero-chinese.com/plugins/charts)
- **[Better Notes](https://github.com/windingwind/zotero-better-notes)：**整理批注、连接笔记、导出 Markdown。

Markdown 自动同步是双向的；启用前确认需要同步的文件，保留原始批注。
- **[Zotero PDF2zh](https://github.com/guaguastandup/zotero-pdf2zh)：**在 Zotero 内翻译 PDF，原文与译文对照。

需要插件与翻译服务配合；译文只辅助阅读，关键结论仍回原文核对。
- **[Zotero MCP](https://github.com/cookjohn/zotero-mcp)：**让 AI 搜索 Zotero 文献、全文和笔记。

插件也有写入笔记、标签和元数据的功能；需要只读时明确限制操作。连接云端 AI 后，读取内容可能发给模型服务商。

### 5.2 写作与排版

- **[ChineseResearchLaTeX](https://github.com/huangwb8/ChineseResearchLaTeX)：**中文科研 LaTeX 模板：标书、论文、学位论文、简历。

模板先与当年的学校、基金或期刊官方要求对照；项目说明要求使用 XeLaTeX。
- **[THU-PPT-Theme](https://github.com/atomiechen/THU-PPT-Theme)：**PPTX 模板，统一答辩或组会排版。

采用 CC BY-NC-SA 4.0，保留署名、遵守非商业与相同方式共享条件；校徽等标识另按其规则使用。

### 5.3 论文绘图

- **[Paper Plot Skills](https://github.com/Trae1ounG/paper-plot-skills)：**用自己的数据画统计图，参考图布局转 matplotlib。

参考图用于借鉴表达；不要把复现图当成自己的实验结果。仓库首页未明确展示许可证，复制代码或原图前另查授权。
- **[Paper Framework Figure Studio Pro](https://github.com/c-narcissus/paper-framework-figure-studio-pro)：**核对模块与箭头，分轮生成框架图。

当前主线主要面向 ChatGPT 网页端；默认交付候选参考图，可编辑 SVG 或 PPT 通常还需另行重绘。
- **[Lieflat Charts](https://github.com/larashero3-dotcom/lieflat-charts)：**数据转交互 HTML 图表或一页报告。

项目采用非商业许可；商业使用需另行取得许可。图表工具不会替你验证输入数据。

[项目 LICENSE](https://github.com/larashero3-dotcom/lieflat-charts/blob/main/LICENSE)

### 5.4 引用核验

- **[Scholar Ref Cleaner](https://github.com/libo-huang/scholar-ref-cleaner)：**BibTeX、Word、文本引用与数据库元数据比对。

查无结果可能来自数据库覆盖或网络问题，不能直接判为伪造；元数据匹配也不证明引用支持正文论断。
- **[TrueCite](https://www.wispaper.ai/agents/true-cite)：**上传 BibTeX，筛出需复核的引用。

页面当前说明只支持 .bib，最大 1 MB；自动标记不是学术不端判定，核查正文论断仍需读原文。
- **[ValiRef](https://github.com/Gianthard-cyh/ValiRef)：**从 PDF 提取引用，检索来源，生成核验报告。

ruanyf/weekly 的链接是开发者自荐，不是独立评测；LLM 报告可能误判，项目的准确率主张未在这里复测。

[开发者自荐讨论](https://github.com/ruanyf/weekly/issues/9505)
- **[DrClaw · Check Review Alignment](https://github.com/InternScience/DrClaw/blob/main/drclaw/agent_hub/templates/proposal-writing/skills/check-review-alignment/SKILL.md)：**核对引用是否支持正文，记录原句、证据和位置。

核对已有引用与正文论断的对应关系；不能保证自动核验无误。排版导出另依赖项目里的综述 skill。

### 5.5 代码阅读

- **[DeepWiki](https://deepwiki.com/)：**看 GitHub 仓库架构，查函数和数据流。

先核对索引版本与正在阅读的代码版本；生成文档不能替代源代码或运行结果。未索引的公开仓库可提交仓库 URL。

[官方说明](https://docs.devin.ai/work-with-devin/deepwiki)

### 5.6 论文发布与维护

- **[Hugging Face Daily Papers 投稿](https://huggingface.co/papers/submit)：**将公开 arXiv 论文提交到 Daily Papers。

论文被索引、作者认领、进入 Daily Papers 是不同状态；当前资格与时间窗口以投稿页面为准。

[官方 Paper Pages 说明](https://huggingface.co/docs/hub/paper-pages) · [官方 papers skill](https://github.com/huggingface/skills/blob/main/skills/huggingface-papers/SKILL.md)
- **[Hugging Face 作者认领](https://huggingface.co/docs/hub/paper-pages#claiming-authorship-to-a-paper)：**在 Paper Page 点击自己的名字，认领署名并等待验证。

只认领自己署名的论文；把公开论文页用于分享，个人认领流程留在账号内。

[Papers 设置](https://huggingface.co/settings/papers)
- **[Hugging Face Daily Papers 历史页面](https://huggingface.co/papers)：**按日期看论文，检查自己的公开论文页。

出现在日期页不代表会议接收、同行评审或结果复现；该链接是历史示例。

[2026-02-06 示例页面](https://huggingface.co/papers/date/2026-02-06)

### 5.7 其他资源

- **[Edit Banana](https://github.com/BIT-DataLab/Edit-Banana)：**静态图转可编辑 DrawIO 元素。

项目说明线上服务与仓库功能可能不同。README 写 Apache 2.0，LICENSE 文件实际为 AGPL-3.0；复用或部署前先确认许可。

[项目 LICENSE](https://github.com/BIT-DataLab/Edit-Banana/blob/main/LICENSE)
- **[PDF Cut White](https://github.com/FFengIll/pdf-cut-white)：**裁剪 PDF 图表白边，另存新文件。

README 说明默认只处理 PDF 第一页；保留原件，并为输出使用不同文件或目录。仓库首页未明确展示许可证，复制代码前另查授权。
- **[科研 Skills 社区介绍 · 卡尔的AI沃茨](https://zhuanlan.zhihu.com/p/2063654777473569661)：**科研 skill 社区介绍；找候选后回项目原文。

作者的体验与排名是社区观点，不是统一条件下的基准测试，也不替项目做许可或安全保证。

<a id="code-release-prompt"></a>
### 5.8 开源整理

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

依据：minimal-code-layout · 作者指定的翻译与去秘范围 · [对应铁律与完整提示词](https://github.com/Da1yuqin/PaperBank/blob/main/data/guide.json)

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
- [Bruno et al. (2024) · A universal framework for inclusive 15-minute cities](https://arxiv.org/html/2408.03794v1)：地图、累计分布、多维气泡与设施迁移排名。原图只链接，点评为本指南整理；颜色和大小按原图注解释。
- [pymoo · Pareto dominance](https://pymoo.org/getting_started/preface.html)：多目标比较与非支配解的定义
- [Callaway & Sant’Anna · Difference-in-Differences with Multiple Time Periods](https://arxiv.org/abs/1803.09015)：DID 的比较设计与平行趋势识别条件
- [Yuqin Dai et al. · EviNote-RAG: Enhancing RAG Models via Answer-Supportive Evidence Notes](https://arxiv.org/html/2509.00877v3#S5)：Conclusion 第一自然段：核心设计、作用与结果如何收束；表现判断只对应该版本的比较。
