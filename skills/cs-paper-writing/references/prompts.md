# 给 Codex 的提示词

填写【】后使用，适用于实证型 CS 论文。宽度、色值、模型与重复次数按本篇确定。Nature 系列使用独立体系。


<a id="draft"></a>
## 初稿提示词

依据：cs-writing-common · cs-abstract-introduction · cs-related-work · cs-method · cs-experiments · cs-visuals · cs-integration · cs-limitations。

对应规则：只加载当前任务相关章节；真实句间钩子与问题—设计—证据对应；固定三项贡献：对象、机制与用途、发现；当前人工定版与证据边界优先。

### 中文

```text
读取 cs-paper-writing/SKILL.md。
先读共享规则，再加载当前章节。
核对会议及 track 的 AI 规定与材料权限。
遵守当前授权范围，按要求披露 AI 使用。
未经许可，不外传未公开稿件、review、个人数据或密钥。
会议、官方模板、正文页数与附录规定：【】
研究问题与已有不足：【】；真实设计与依据：【】
实验材料、指标、对照与实测结果：【】
参考论文及借鉴部分：【】；允许修改：【】

1. 核对模板并编译。
   保留最新源、原始结果与合作者修改。
2. 梳理参考论文的章节职责、顺序和输入输出。
   据此拟定大纲，只借鉴组织，不复制措辞或主张。
3. 先完成关键图，对应问题、设计与证据。
   读取 cs-visuals，精修图形时另读绘图 skill。
4. 列出各节标题、任务、证据和篇幅。
   Method Overview 承接困难，串起输入输出。
   各模块先讲动机，再讲设计。
5. 按主张组织实验，给出对应证据。
   整体结果、局部差异、条件分析分别交代范围与分母。
   不补造分析、标题或结果。
6. 引言依次说明已有能力、不足、解法和发现。
   写明机制与用途，段首承接具体对象。
7. 贡献用原生 itemize，固定三项。
   第一项写整体工作，第三项写实验发现。
   第二项按论文类型写关键设计或证据贡献。
   可写机制、构建、评价、比较或测量，不虚构工作。
8. 先交中文提纲和证据，再按授权写英文。
   核对数值、引用、图表、分页与最终 PDF。
   远端源与服务端 PDF 分开核验。
9. 局限性读取 cs-limitations。
   用单段 First / Second 写两点。
   每点先肯定有据工作，再说明具体边界。
```

### English

```text
Read cs-paper-writing/SKILL.md. Load the shared rules once and only the chapter skills relevant to this task; do not load every example by default.
Check the current venue and track AI policy and permissions for the material. Do not send unpublished manuscripts, reviews, personal data, or credentials to external services without authorization.
Venue, official template, body-page limit, and appendix rules: [ ]
Research question and prior limitations: [ ]; actual design and basis: [ ]
Experiments, metric definitions, controls, and measured results: [ ]
Suitable reference paper and selected sections for structural guidance: [ ]
Allowed files and edit scope: [ ]

1. Check and compile the template; preserve current sources, original results, and concurrent edits.
2. Explain the reference sections’ roles, argument order, and real dependencies, then outline this research. Borrow organization, not wording, facts, or claims.
3. Settle key figures and the problem-design-evidence mapping. Load cs-visuals; use the public drawing skill when needed.
4. List section titles, purposes, evidence, and page budgets. Connect the Method Overview through real inputs and outputs; begin each module with its specific motivation and actual design.
5. Organize experiments around claims. Give separate populations and denominators for overall results, local differences, and independent conditional analyses. Do not invent analyses.
6. Establish prior capabilities and concrete limitations, then explain matched solutions, mechanisms, uses, and supported findings. Hooks must connect real objects and relationships.
7. Use three native itemize contributions: overall work, key design or evidence contribution, and empirical findings. Adapt item 2 to the paper type: a mechanism, construction or evaluation design, controlled comparison, or measurement. Do not invent a mechanism or diagnostic experiment.
8. Present a Chinese outline and evidence for author review before authorized English drafting. Verify data, references, layout, and the rendered PDF; distinguish remote-source sync from the server PDF.
Use cs-limitations for Limitations: one paragraph, First and Second, with verified completed work and concrete relevant boundaries.
```

<a id="writing"></a>
## 正文精修提示词

依据：cs-writing-common · cs-abstract-introduction · cs-related-work · cs-method · cs-experiments · cs-visuals · cs-integration · cs-limitations。

对应规则：只加载当前任务相关章节；真实句间钩子与问题—设计—证据对应；固定三项贡献：对象、机制与用途、发现；当前人工定版与证据边界优先；cs-limitations：单段 First/Second 两点让步模板。

### 中文

```text
读取 cs-paper-writing/SKILL.md。
先读共享规则，再加载当前章节。
核对会议及 track 的 AI 规定与材料权限。
遵守当前授权范围，按要求披露 AI 使用。
未经许可，不外传未公开稿件、review、个人数据或密钥。
任务与论文类型：【】；会议及限制：【】
材料：【最新源、实测结果、原文依据】；允许修改：【】

1. 核对不足、设计与证据的对应关系。
   每句承接前句的对象、问题或产物，再加一个判断。
2. Therefore 归纳，Specifically 展开，However 转折。
   引例句以 For example 或 For instance 开头。
   说明缺少某设计会妨碍什么判断。
   相邻句段避免重复过渡词。
3. 对象和动作前置，保留有依据的贡献描述。
   删掉重复语意，保留指向清楚的代词。
   符号、缩写、单位与来源就近定义。
4. 按当前章节规则改写。
   引言不固定使用 Therefore 或 To solve。
   贡献第二项写实际设计或证据、依据与用途。
   Related Work 用固定三句收尾。
   Method 按输入输出衔接，各模块先写动机。
5. 全文统一问题、名称、数字、范围与因果方向。
   整体发现与局部诊断分开。
   相关或条件结果不能冒充机制证明。
6. 保留原始记录、协议、冻结 prompt 和模型回复。
   不编结果或引用，保留人工定版及并发修改。
   只读任务不写文件，证据缺口交作者确认。
7. 检查最终 PDF 的句长、图表、脚注、分页与计页。
   只有明确必遵或禁止的要求标“铁律”。
8. 数字注明单位、分母与版本。
   区分百分比与百分点、宏平均与微平均。
   不用分号拼长句，核对文献日期、版本及预印本身份。
9. 局限性读取 cs-limitations。
   用单段 First / Second 写两点。
   每点先肯定有据工作，再说明边界。
   未测不等于失败，限制与全文结论一致。
```

### English

```text
Read cs-paper-writing/SKILL.md. Load the shared rules once and only the chapter skills relevant to this task; do not load every example by default.
Check the current venue and track AI policy and permissions for the material. Do not send unpublished manuscripts, reviews, personal data, or credentials to external services without authorization.
Task and paper type: [ ]; venue and constraints: [ ]
Material: [latest source, actual results, primary evidence]; allowed edits: [ ]

1. Match the concrete limitation, actual design, and supporting evidence. Each sentence inherits an object, question, or output and adds a judgment.
2. Use Therefore to infer from evidence, Specifically to unpack a judgment, and However for a concrete contrast. Put For example or For instance first in an example sentence. Explain what cannot be distinguished without a missing design feature. Vary transitions naturally across adjacent sentences and sections.
3. Put contribution objects and actions early. Retain supported informative modifiers and remove empty stacking. Keep clear nearby pronouns; define notation, abbreviations, units, and sources locally.
4. Follow the current chapter rules. Do not permanently require Therefore or To solve in the Introduction. Contribution 2 describes the actual design or evidence contribution, its basis and use, according to the paper type; it does not invent a new mechanism. Related Work uses its three-sentence ending; Method uses real input-output dependencies and motivation-first modules.
5. Align the Abstract, Introduction, method, experiments, and conclusion in problem, names, numbers, scope, and causal direction. Separate overall findings from local diagnosis and conditional evidence from mechanism proof.
6. Preserve original records, protocols, frozen prompts, replies, approved wording, and concurrent edits. Do not invent results or citations. Read-only tasks make no edits; evidence gaps remain for the author.
7. Inspect the rendered PDF for sentence length, tables, footnotes, layout, and page counting. Only explicit mandatory or prohibited requirements are hard rules.
Give units, denominators, and versions; distinguish percentages from percentage points and macro from micro averages. Do not rejoin long sentences with semicolons. Verify publication dates, versions, and preprint status.
For Limitations, load cs-limitations. Use one paragraph with First and Second; each point briefly states verified completed work before a concrete relevant boundary. Untested is not failed, and material limitations must agree with the manuscript’s claims.
```

<a id="experiments"></a>
## 实验整理提示词

依据：cs-writing-common · cs-abstract-introduction · cs-related-work · cs-method · cs-experiments · cs-visuals · cs-integration。

对应规则：只加载当前任务相关章节；真实句间钩子与问题—设计—证据对应；固定三项贡献：对象、机制与用途、发现；当前人工定版与证据边界优先。

### 中文

```text
读取 cs-paper-writing/SKILL.md。
先读共享规则，再加载当前章节。
核对会议及 track 的 AI 规定与材料权限。
遵守当前授权范围，按要求披露 AI 使用。
未经许可，不外传未公开稿件、review、个人数据或密钥。
材料：【引言主张、实测结果、指标、对照、重复记录与版本】
允许修改：【】；保护：【原始结果、执行协议、评价输入】

1. 将每项主张对应到真实比较与证据。
   按需使用 RQ，不要求每张表编号。
2. Setup 交代数据划分、指标、模型、基线与预算。
   写明实际设置。
   指标注明单位、分母、汇总方式及无效输出处理。
   单独说明不适用情形。
3. 先概述主发现，再用 Specifically 展开。
   However 指出整体结果掩盖的差异。
   独立分析用 Separately 或 Next，不虚构因果。
4. 每段写发现、对照、范围和含义，不逐行读表。
   全局组成、场景发生率、条件子集各用真实分母。
   不混称、不直接相减，也不预设共同子集。
5. 消融先定义 setting，再比较结果。
   联合改变不能归因于单个模块。
   区分诊断、关联、因果证据与评价器一致率。
   初始判分、复核标签、最终得分分开报告。
   一致率不是独立准确率。
6. 表体名称、引用、数值及上标误差保持单行。
   换行时先调模板允许的列宽。
   均值及 SD、SE、CI 基于真实观测和明确方法。
   说明统计或重采样单位及数量。
   单次运行不证明稳定性，排名不证明显著性。
   Caption 留核心口径，局部例外放脚注。
   插回论文检查最终 PDF。
7. 结果变化后回读授权范围内的摘要、引言和结论。
   不改冻结材料，不新增未经授权的实验。
```

### English

```text
Read cs-paper-writing/SKILL.md. Load the shared rules once and only the chapter skills relevant to this task; do not load every example by default.
Check the current venue and track AI policy and permissions for the material. Do not send unpublished manuscripts, reviews, personal data, or credentials to external services without authorization.
Material: [Introduction claims, actual results, metrics, controls, repeat records, and versions]
Allowed edits: [ ]; protect: [original results, execution protocol, and assessment inputs]

1. Map each claim to an actual comparison and evidence. Use RQs when helpful, not for every table.
2. Explain data splits, metrics, models and baselines, budgets, and actual settings. Give units, denominators, aggregation, inapplicability, and invalid-output handling.
3. Overview the main finding, then organize local differences and independent conditional analyses by evidence level. However exposes a difference hidden by the aggregate; Separately or Next moves to a genuinely independent question, not an invented causal chain.
4. Each paragraph gives a finding, key comparison, scope, and meaning. Do not narrate every table row. Global composition, scenario incidence, and conditional subsets retain their own denominators and cannot be directly subtracted.
5. Use suitable ablation controls for actual designs. Joint changes cannot be attributed to one module. Distinguish diagnosis, association, causal evidence, and judge agreement.
6. Keep table-body names, references, values, and superscript uncertainty on one line; adjust permitted column widths first. Base means and SD, SE, or CI on actual observations and an explicit method; state the statistical or resampling units and their counts. A single run does not establish stability across runs. Ranking is not significance. Keep core definitions in captions and local exceptions in linked footnotes; inspect the final PDF.
7. Re-read authorized Abstract, Introduction, and Conclusion sections when findings change. Preserve frozen materials and do not run unauthorized new experiments.
Overview the supported main finding before using Specifically to expand the analysis. Verify actual coverage without presuming a common subset. Separate initial judgments, human-reviewed labels, and reported scores; label agreement is not independent accuracy.
```

<a id="intro"></a>
## 引言提纲提示词

依据：cs-writing-common · cs-abstract-introduction · cs-related-work · cs-method · cs-experiments · cs-visuals · cs-integration。

对应规则：只加载当前任务相关章节；真实句间钩子与问题—设计—证据对应；固定三项贡献：对象、机制与用途、发现；当前人工定版与证据边界优先。

### 中文

```text
读取 cs-paper-writing/SKILL.md。
先读共享规则，再加载当前章节。
核对会议及 track 的 AI 规定与材料权限。
遵守当前授权范围，按要求披露 AI 使用。
未经许可，不外传未公开稿件、review、个人数据或密钥。
材料：【问题、已有工作原文、设计、已核验发现与范围】
允许修改：【摘要、引言或指定段落】

1. 开头建立领域价值，回顾已有能力并比较不足。
   可合并、穿插或拆段，不固定段数。
2. 每项不足写清条件、机制和实际影响。
   说明缺少某功能后，已有成功仍不能区分什么。
   未报告不写成不存在。
3. 方法段首承接障碍，方法名后紧跟产物、亮点和用途。
   用 For [困难] 等钩子逐项对应解法。
   不恢复作者已删的 Therefore 或 To solve。
4. 先写贡献对象，再写依据与作用。
   来源、原则、产物、应用各有职责。
   模型输入与评价材料分开。
5. 结果段先概述发现，再解释命名发现及范围。
   Therefore 归纳，Specifically 展开。
6. 普通引导句后接原生 itemize，固定三项贡献。
   第一项：整体工作与任务。
   第二项：关键设计或证据、依据与用途。
   第三项：有明确范围的实验发现。
   第二项按论文类型写机制、构建、评价、比较或测量。
   不虚构工作，不重复困难标签。
   贡献后直接进入下一节。
7. 回读摘要与授权范围内的正文。
   统一问题、设计、数字、名称、范围与因果方向。
   压缩或展开表述，不逐字照抄。
   先交中文逻辑，再按授权组织英文。
```

### English

```text
Read cs-paper-writing/SKILL.md. Load the shared rules once and only the chapter skills relevant to this task; do not load every example by default.
Check the current venue and track AI policy and permissions for the material. Do not send unpublished manuscripts, reviews, personal data, or credentials to external services without authorization.
Material: [problem, primary prior-work passages, actual design, verified findings and scope]
Allowed edits: [Abstract, Introduction, or specified paragraphs]

1. Establish field value and prior capabilities before comparing limitations. Merge, interleave, or split the opening paragraphs as the argument requires.
2. Explain the conditions, mechanism, and practical obstruction for each limitation. State which distinction existing success cannot establish without the missing feature; unreported is not absent.
3. Connect the method paragraph to established obstacles and immediately describe the artifact, verified feature, and use. Use accurate matched hooks such as For [challenge]; do not restore Therefore or To solve after the author has removed them.
4. Put contribution objects first, then their verified basis and function. Distinguish sources, principles, artifacts, applications, model-visible inputs, and assessment targets.
5. Overview supported findings before defining named findings and their scope. Therefore makes an inference; Specifically expands a judgment. Choose words by relationship.
6. A normal prose lead introduces three native itemize items: overall work and task; the key design or evidence contribution, its basis and use; scoped empirical findings. Adapt item 2 to the actual mechanism, construction or evaluation protocol, comparison, or measurement. Do not invent work or mechanically repeat obstacle labels. Proceed directly to the next section after the list.
7. Re-read the Abstract and authorized body sections for consistent problem, design, numbers, names, scope, and causal direction. Compress or expand without copying verbatim. Present Chinese reasoning before authorized English drafting.
```

---

Da1yuqin / StarPaper，[原文](https://da1yuqin.github.io/StarPaper/)，[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)。
