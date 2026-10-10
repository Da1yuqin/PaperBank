# 给 Codex 的提示词

填写【】后使用。以下采用本地技能中适用于实证型 CS 论文的通用规则；不套用某篇论文的固定宽度、色值、模型阵容或重复次数。Nature 系列使用独立体系。


<a id="figures"></a>
## 给 Codex 的绘图说明单

依据：paper-visual-standards · academic-plotting · clean-flow-figures。

对应规则：最终宽度和统一字号；输入、输出与评价边界；案例全文唯一使用；统计图的真实数据与自解释；Caption、顶部浮动与最终 PDF 验收。

### 中文

```text
读取 paperbank-figures/SKILL.md 和 references/rules.md。按以下材料画图。
图型：【mainfig／framework／统计图／案例图】
要突出的问题与贡献：【对应 Intro 的哪项困难，方法改了什么，依据在哪里】
材料：【稿件、真实数据、参考图与出处、已有案例及使用位置】
真实结构：【输入、操作、输出、接收者；并行、汇合、反馈；训练／推理／评价】
允许修改：【文件与范围】；最终插入宽度：【mm】
正文 PDF 实测字体与字号：【字体，pt】；本篇已确认色板：【】

铁律：
1. mainfig 讲问题、已有缺口与关键改动，默认不超过 5 个环节；framework 先让人看懂设计为什么好，再画完整输入、操作与产物。两张图别画成同一张。
2. 每条箭头对应真实依赖，不穿文字。保留并行与反馈；训练、推理、评价分开。输入、输出、评价规则用三种边框并给图例；仅供评价的信息不能画成模型输入。
3. 按最终宽度起稿。所有标题、坐标、刻度、图例、数字、注释用同一字号，正文减 2 pt ≤ 图字 ≤ 正文，字体家族匹配。放不下就重排或拆图，不缩字、拉扁或改论文模板。
4. 白底、近白面板、深色文字、低饱和配色。同一对象全篇同色，用形状或线型辅助区分；不加渐变、阴影和装饰光效。通栏先参考 16:9，单栏参考 4:3，内容与可读性优先。
5. 模块名与正文一致。缩写、变量、单位、图标、颜色和线型都能解释；图标旁写对象名。标签用自然语言，不用符号拼句。
6. 同一案例全文只呈现一次，翻译、裁剪或改名仍算同一个。先按来源核对使用位置，其他位置交叉引用。对话一轮一框；作者示例与实测回复分清，没有评分不画勾。
7. 统计图用 Python 等专业工具读取所附数据，保留数值、坐标几何、分母、单位与 SD／SE／CI 定义；同类比较统一尺度。不为美观补缺测、改数据或平滑曲线，不重跑实验；KDE 等估计图说明样本量、方法和带宽。概念图按当前环境使用 imagegen，不让生成器猜流程或造结果。
8. Caption 说明读法、比较、必要口径与实际发现，简称在本条 Caption 写全称。方法图说明机制，不编实验结论。尽量三行，必要定义与事实边界优先。
9. PDF 文字可见、可选，字体嵌入；不叠两套字形或隐藏 OCR。统计图优先矢量 PDF，含位图的 PDF 不称全矢量。CS 图表默认 [!t]，实际位置跟随正文首次引用，保留附录归属。
10. 先给问题、布局和缺口，再绘制。插回论文编译，看最终页面的字号、图例、裁切、碰撞和引用顺序。交付源文件、PDF、预览及实际检查结果。只改色时保留原布局、文字、连线与图片；保留他人修改，不扩大范围。
```

### English

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

<a id="draft"></a>
## 一天拉完草稿：给 Codex 的提示词

依据：cs-paper-writing · paper-writing-clarity · cs-writing-skill · paper-visual-standards。

对应规则：贡献可见性与问题—设计—证据对应；章节与 Overview 逻辑；先粗写再人工审核；最终字号、成绩表与引用顺序。

### 中文

```text
读取 paperbank-writing/SKILL.md、references/checklist.md；绘图同时读 paperbank-figures/SKILL.md。先拉粗稿，再由我审中文逻辑。本提示词用于实证型 CS 论文，Nature 系列另用独立体系。
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
5. 按 Intro 主张整理实验。Setup 写清数据与划分，按 Metrics、Baselines、Implementation Details 说明指标口径、比较路线和真实设置。Main Results 先给有证据的结论，再讲关键对照与范围；消融固定其他条件，不逐行念表。
6. 表格用 booktabs，列宽、精度与单位一致。真实可比组内最优加粗浅红，第二个不同显示值下划线浅蓝，并列共享标记；不把排名当显著性。有真实重复才写均值与不确定性，说明次数、SD／SE／CI 和有效子集。不用 resizebox 硬塞。
7. 最后组织 Intro：已有能力→具体不足→对应设计→实际发现→平行贡献。写清真正新增了什么，设计为什么回应不足；不把普通工程步骤包装成创新。不够的证据单列给我，不编结果、引用或 first／unique。
8. 每次给我一节中文提纲与真实证据，确认后再写英文。一句一个完整判断，一段一个任务；定义术语、符号和信号来源，同对象同名称，正文不用 it／they 及同族代词。贡献形容词须有依据，一词换一词，不堆修饰。超页先删重复，不缩模板字号或间距。交付实际编译与 PDF 检查结果，远端同步单独说明。
```

### English

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
```

<a id="writing"></a>
## 给 Codex 的写作与精修提示词

依据：cs-paper-writing · paper-writing-clarity · cs-writing-skill。

对应规则：新贡献、具体对象与证据边界；句间承接与最新短句要求；Related Work 主题缺口与 Overview 章节定位；实验结论优先。

### 中文

```text
读取 paperbank-writing/SKILL.md 和 references/checklist.md，按当前任务选规则。
任务：【起草／精修哪节／只读检查】；目标会议与限制：【】
材料：【最新稿件、真实结果、参考原文】；允许修改：【文件与范围】

铁律：
1. 先查“具体不足→新增设计→实际证据”。Abstract、Intro 贡献和 Method Overview 明说新对象或设计及其价值，与最近工作比较；全篇困难、模块和发现名称一致。不猜技术设定，不编引用、数字或优先权。
2. 一句一个完整判断，一段一个任务，后句接前句对象、问题或产物。正文不用 it／they 及同族代词，we／our 和 this + 明确名词可保留。用短对象名，不拼符号、堆形容词；有依据的贡献词一词换一词。
3. 缩写、符号首次出现定义对象、来源、单位与下标；摘要、引言、实验各自能读懂。按最终 PDF 检查句长，双栏一句默认最多三行、单栏一句默认一行半，完整语义优先；不用缩字、改栏宽或硬换行凑行数。
4. Related Work 按主题写已有路线、能力、具体不足和本文方案；However 与 To address 的对象、关键词对齐 Intro，不逐篇点名或凑引用。Method Overview 先讲设计为什么回应困难，再写目的、操作、产物；用 in [准确章节名] (ref) 定位，每个章节名与引用出现一次，保留并行关系，末句引 framework。
5. 实验段先给有证据的结论，再讲比较条件、关键对照与含义；消融固定其他条件。指标说明方向、分母和不确定性，区分记录与独立样本、百分比与百分点、观察与因果；保留影响解释的负结果。RQ 按需要使用。
6. 数据、公式含义、实验设置、引文、原始 prompt 和模型回复不因润色改变；保留他人修改。先给中文逻辑与最小改法，确认后改英文。缺证据单列给我，不塞进论文；只读任务不写文件。最后说明实际改动和检查，编译与最终 PDF 目检分别确认。
```

### English

```text
Read paperbank-writing/SKILL.md and references/checklist.md and select rules for this task.
Task: [draft / refine a specified section / read-only check]; venue and limits: [ ]
Materials: [current manuscript, actual results, source passages]; editable files and scope: [ ]

Hard rules:
1. Check the specific limitation → new design → actual evidence chain first. The Abstract, Introduction contributions, and Method Overview state the new object or design, its value, and its difference from the closest work. Keep challenge, module, and finding names consistent. Invent no settings, citations, numbers, or priority claims.
2. Use one complete main judgment per sentence and one task per paragraph. Connect each sentence to the preceding object, question, or product. Replace it / they and related object pronouns in author prose with short object names; retain we / our and this plus an explicit noun. Avoid symbol-packed prose and stacked modifiers; use supported contribution words as concise replacements.
3. Define acronyms and notation at first use, including objects, sources, units, and indices. Make the Abstract, Introduction, and Experiments independently understandable. Check sentence length in the final PDF: default maximum three lines in a narrow two-column layout and one-and-a-half lines in a single-column layout. Retain complete meaning; do not shrink text, alter columns, or add hard line breaks.
4. Organize Related Work by topic: existing approach, capability, specific limitation, and the paper's response. Match However / To address objects and keywords to the Introduction; do not list papers or pad citations. The Method Overview explains why the design addresses the challenge before its purpose, operations, and products. Locate actions with in [exact section title] (ref), citing each title once; preserve parallel paths and cite the framework last.
5. Start result paragraphs with evidenced conclusions, then conditions, key comparisons, and implications. Hold other conditions fixed in ablations. Define metric direction, denominators, and uncertainty. Distinguish records from independent samples, percentages from percentage points, and observations from causal findings. Retain negative results that affect interpretation. Use RQs when useful.
6. Preserve data, formula meanings, settings, citations, original prompts, model outputs, and concurrent edits. Show Chinese reasoning and minimal fixes before revising English. Keep evidence gaps outside the paper; do not write files for read-only tasks. Report actual changes and checks, distinguishing compilation from visual inspection of the final PDF.
```

<a id="experiments"></a>
## 给 Codex 的实验整理提示词

依据：cs-paper-writing · paper-writing-clarity · paper-visual-standards。

对应规则：实验设置的 Metrics 与 Baselines；实验先结论再证据；消融与负结果；成绩表可比组、排名及不确定性。

### 中文

```text
读取 paperbank-writing/SKILL.md 的 Experiments 与图表规则。
材料：【Intro 主张、真实结果文件、数据划分、基线配置、预算、重复记录】
允许修改：【实验正文、表格及相关文件】；不得改动：【原始结果与实验协议】

1. 按“Intro 主张／研究问题→比较对象与固定条件→指标→图表→能支持的结论”整理。RQ 有需要再用，不给每个图硬凑一个。
2. 先写 Experimental Setup：数据来源与划分；Metrics 定义方向、分母、聚合；Baselines 按路线分组，注明来源与版本；Implementation Details 写真实训练／推理预算、硬件、超参数和重复次数。没有记录就列缺口，不猜默认值。
3. 再排 Main Results、Ablation Studies 与必要分析。每段首句给有证据的结论，随后讲关键对照、条件和范围；一个独立发现一段，不逐行念数。消融只改待检因素，保留其他条件，未排除的解释不能写成因果。
4. 表格用 booktabs；同类表统一列宽、组名、精度和单位。最优加粗浅红，第二个不同显示值下划线浅蓝，并列共享标记，限真实可比组。均值与不确定性同行，整段 ± 及误差可上标；写清真实重复次数、SD／SE／CI 和共同有效子集，不用排名替代显著性，不用 resizebox 缩整表。
5. Caption 写比较、实际发现与必要口径，每条展开简称，尽量三行。图表用 [!t]，核对最终首次引用顺序。百分比与百分点、记录与独立样本、整体与子集分开，保留影响结论的负结果。
6. 先给中文逻辑让我审，再写英文；只根据所附记录绘图制表，不补结果、重跑基线或改统计口径。编译检查实际页数、数值、标记、字体和溢出，报告证据缺口与已做检查。
```

### English

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

<a id="intro"></a>
## Intro 中文提纲提示词

依据：cs-paper-writing · paper-writing-clarity · cs-writing-skill。

对应规则：贡献可见性与有依据的贡献形容词；背景—困难—对应方案；引言句间承接与平行贡献；摘要与引言一致。

### 中文

```text
读取 paperbank-writing/SKILL.md 的 Introduction 规则与模板。
材料：【问题依据、最近工作、真实设计、已验证结果与范围】
任务：先写中文提纲；允许修改：【文件与范围】。

1. 先写“具体不足→对应设计→实际证据”映射，缺证据单列，不补造。
2. 背景段：说清研究方向与价值，紧接已有路线怎么做、已经能做什么。用必要原文引用，不从“随着技术发展”开始绕圈。
3. 问题段：指出哪个条件下，已有做法不能证明或处理什么，并给依据。每个问题须有后文设计回应，不把已有能力写成没人做过。
4. 方案段：明确本文新增的对象或设计，与最近工作区别在哪里；先解释为什么针对该困难，再写输入、操作、产物。不要只报模块名或排流水线。
5. 发现段：只写实际主要发现、关键比较和适用范围。没有结果不写结果句，诊断不冒充因果，有限测试不推广全部场景。
6. 贡献用原生 itemize，平行、简短、长度相近，项数按真实工作调整。一项一个主要贡献，普通实现不凑创新。de-identified、expert-confirmed、tailored 等词须有对应事实，一词换一词，不堆夸奖；不用无依据的 first／unique。
7. 逐句查前句是否提供后句的对象或前提，问题、机制与实验名称是否一致。定义必要术语，用具体对象替代 it／they；不为套段数破坏逻辑。先让我审中文，再组织英文。研究事实有实质调整才同步改摘要，保留原始结果、引文和并发修改。
```

### English

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

<a id="rebuttal"></a>
## Rebuttal + revise loop

依据：rebuttal · rebuttal-reviewer-simulator。

对应规则：原始问题逐条覆盖；事实来源与承诺边界；每问首句结论与精简表格；revise loop 与 AC 总结。

### 中文

```text
读取 paperbank-writing/SKILL.md 的 Rebuttal 与 revise loop。
材料：【论文、完整 review、当前回复、已验证补充结果】
会议当轮规则：【字数／字符限制、补实验／链接／修订稿／AI 使用规定】
阶段：【初次／追问】；允许修改：【回复文件与范围】

1. 先保留 review 原文，逐条拆出 Summary、Weaknesses、Questions、建议和评分理由里的具体关切；Strengths 记录已认可点。列“原问题→需要的证据→现有依据与位置→缺口”，不按回复现有顺序漏问，不猜审稿人动机或水平。
2. 每问首句直接回答，随后给证据、解释和位置；问题标题忠于原意，感谢简短。数据、对照或成本适合表格就用紧凑表格，保留必要比较条件、数值口径与范围，不用文字重复每格。
3. 每个事实回到论文、原 review、真实结果或已确认推导。合理批评就承认并改，争议就查前提与证据；不隐藏影响比较的条件。补实验的承诺不能替代结果；缺结果交给我决定，不编数字、不把 future work 写成已完成，不自动跑实验或提交回复。
4. 执行 revise loop：按原问题清单查“原问题→回复位置→是否回答→证据是否匹配→剩余疑问→最小改法→还缺什么”。先修漏答、证据与逻辑，再压文字、调语气。只改不通过项，改后重查同一张清单，不盲目重跑全部基线。
5. 所有问题明确覆盖、事实与证据对应、逻辑通顺、长度和当轮政策合规后停止，由我定稿。证据不足就交回缺口，不通过模拟预测涨分或录用。
6. 追问轮只答新增关切；AC 总结写关键问题、回应、证据与限制，不请求提分或接收。英文回复逐段附中文供我审，内部检查和缺口不混入提交文本。
```

### English

```text
Read Rebuttal and revise loop in paperbank-writing/SKILL.md.
Materials: [paper, complete reviews, current response, verified supplementary results]
Current venue rules: [word / character limit; experiments, links, revised PDFs, and AI-use policies]
Stage: [initial / follow-up]; editable response files and scope: [ ].

1. Preserve raw reviews. Extract each concrete concern from Summary, Weaknesses, Questions, suggestions, and scoring reasons; record acknowledged strengths. Map original question → required evidence → available evidence and location → gap. Follow original questions rather than the response's order; do not infer reviewer motives or competence.
2. Answer each question in the first sentence, then give evidence, explanation, and location. Keep question headings faithful and thanks brief. Use compact tables for suitable results, comparisons, or costs, retaining necessary conditions, definitions, and scope. Do not repeat every cell in prose.
3. Ground each fact in the paper, review, actual results, or confirmed derivations. Acknowledge and repair valid criticisms; check disputed premises against evidence. Retain conditions that affect comparability. Promised experiments do not replace results. Bring missing evidence to me; invent no numbers or completed work and do not automatically run experiments or submit responses.
4. Run the revise loop against the original issue list: question → response location → answered? → matching evidence? → remaining doubt → minimal fix → missing evidence. Repair coverage, evidence, and logic before shortening or adjusting tone. Revise failed items only, then recheck the same list; do not blindly rerun every baseline.
5. Stop when all issues are explicitly covered, facts match evidence, logic is clear, and length and venue rules are satisfied. I make the final decision. Return unresolved evidence gaps; do not predict score changes or acceptance from simulations.
6. Answer new concerns only in follow-ups. An AC summary states key concerns, responses, evidence, and limits without asking for score increases or acceptance. Add a Chinese translation per English paragraph for my review; keep internal checks and evidence gaps outside the submitted text.
```

<a id="code-release"></a>
## 开源整理提示词

依据：minimal-code-layout · 作者指定的翻译与去秘范围。

对应规则：相对路径与凭据边界；不改变代码行为；保留署名、引用与许可。

### 中文

```text
只处理我指定的文件：<文件或目录>。
把中文注释、文档字符串和使用说明译成英文，保留解释代码所需的注释，删除版本更改流水账。把注释和文档中的个人信息、内部地址、机器绝对路径改成通用说明、相对路径和可运行的例子。保留必要的作者署名、引用与许可证信息。
保持算法、控制流程、变量名、接口、参数和数据不变。不要自行翻译程序输出、异常消息、协议字段或其他可执行字符串；若文档字符串被程序读取，也先报告影响。
疑似密钥、私有数据或运行时配置不要贴出原值。列出文件位置和处理建议；若替换会影响行为，先停在该处，说明需要什么决定。去秘检查也覆盖计划发布的样例、配置、日志和压缩包；若还发布 Git 历史，另查历史内容。
示例：文档中的机器路径改为 data/example.json，并说明从项目入口定位；只改说明，不改程序的路径解析逻辑。密钥示例使用 YOUR_API_KEY，不写真实值。
交付修改差异、处理过的内容类型、未解决项和实际验证结果。没有跑过的检查不要说通过；发现真实秘密时不要发布，先报告位置和处置需求。
```

### English

```text
Work only on the files I specify: <files or directory>.
Translate Chinese comments, docstrings, and usage documentation into English. Keep comments needed to understand the code and remove version-change notes. Replace personal information, internal addresses, and machine-specific absolute paths in comments and documentation with general instructions, relative paths, and runnable examples. Preserve required attribution, citations, and license notices.
Preserve algorithms, control flow, variable names, interfaces, parameters, and data. Do not automatically translate program output, error messages, protocol fields, or other executable strings. Report the impact first if a docstring is read by the program.
Do not quote the original values of suspected credentials, private data, or runtime configuration. Report their file locations and proposed treatment. If substitution would affect behavior, stop at that location and explain the decision needed. Check examples, configurations, logs, and archives intended for release; check Git history separately if it will also be published.
Example: replace a machine-specific path in documentation with data/example.json and explain that it is resolved from the project entry point. Change the explanation, not the program's path-resolution logic. Use YOUR_API_KEY in credential examples, never a real value.
Deliver the diff, the types of content handled, unresolved items, and the checks actually performed. Do not claim an unperformed check passed. If real secrets are found, do not publish them; report their locations and the required treatment.
```

---

Da1yuqin / PaperBank，[原文](https://da1yuqin.github.io/PaperBank/)，[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)。
