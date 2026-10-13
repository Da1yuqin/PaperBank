# 给 Codex 的提示词

填写【】后使用。以下采用适用于实证型 CS 论文的通用规则；不套用某篇论文的固定宽度、色值、模型阵容或重复次数。Nature 系列使用独立体系。


<a id="draft"></a>
## 一天拉完草稿：给 Codex 的提示词

依据：cs-writing-common · cs-abstract-introduction · cs-related-work · cs-method · cs-experiments · cs-visuals · cs-integration · cs-limitations。

对应规则：只加载当前任务相关章节；真实句间钩子与问题—设计—证据对应；固定三项贡献：对象、机制与用途、发现；当前人工定版与证据边界优先。

### 中文

```text
读取 cs-paper-writing/SKILL.md：先读共享规则，只加载当前任务相关的章节 skill；不默认读全部例库。
核对目标会议及 track 的 AI 规定和材料使用权限，遵守当轮允许范围。未经许可，不向外部服务发送未公开稿件、review、个人数据或密钥。
会议、官方模板、正文页数与附录规定：【】
研究问题与已有不足：【】；真实设计与依据：【】
实验材料、指标口径、对照与真实结果：【】
结构适合的参考论文与想借鉴的部分：【】
允许修改的文件与范围：【】

1. 核对模板并编译，保留最新源、原始结果与合作者修改。
2. 先梳理参考部分的各节职责、论证顺序与输入输出衔接，再按自己的研究拟大纲。只借鉴组织，不复制措辞、事实或主张。
3. 完成关键图，确定问题、设计与证据的对应；绘图读取 cs-visuals，精修图形可另读公开绘图 skill。
4. 列章节标题、任务、证据与篇幅。Method Overview 接回具体困难并串起真实输入输出；模块开头先写动机，再写真实设计。
5. 按主张组织实验；整体结果、局部差异与独立条件分析分别给比较范围和分母。没有实际分析，不补标题或结果。
6. 引言先说明已有能力与具体不足，再逐项说明解法、机制用途和有依据的发现。段首承接具体对象，连接词服从真实逻辑。
7. 贡献用原生 itemize，固定三项：整体工作、关键设计或证据贡献、实验发现。第 2 项按论文类型写新机制、构建或评价设计、比较或测量贡献，不虚构新机制或诊断实验。
8. 先给我中文提纲和证据，再按当前授权写英文。检查真实数值、引用、图表、分页与最终 PDF；远端源和服务端 PDF 分开核验。
局限性按 cs-limitations：用一个自然段、First 和 Second 两点，让步说明有据工作与具体边界。
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
## 给 Codex 的写作与精修提示词

依据：cs-writing-common · cs-abstract-introduction · cs-related-work · cs-method · cs-experiments · cs-visuals · cs-integration · cs-limitations。

对应规则：只加载当前任务相关章节；真实句间钩子与问题—设计—证据对应；固定三项贡献：对象、机制与用途、发现；当前人工定版与证据边界优先；cs-limitations：单段 First/Second 两点让步模板。

### 中文

```text
读取 cs-paper-writing/SKILL.md：先读共享规则，只加载当前任务相关的章节 skill；不默认读全部例库。
核对目标会议及 track 的 AI 规定和材料使用权限，遵守当轮允许范围。未经许可，不向外部服务发送未公开稿件、review、个人数据或密钥。
任务与论文类型：【】；目标会议及限制：【】
材料：【最新源、真实结果、原文依据】；允许修改：【】

1. 先核对具体不足、实际设计和对应证据。后句承接前句的对象、问题或产物，再增加一个判断。
2. Therefore 归纳证据，Specifically 展开判断，However 写具体转折；For example 或 For instance 放在引例句首。缺少某设计后，说清因此不能区分什么。相邻句段不反复使用同一个过渡词。
3. 对象和动作尽早出现；保留有依据的贡献信息，删除无信息叠加。清楚、就近且唯一的代词保留，符号、缩写、单位与来源就近定义。
4. 按当前章规则修改。引言不永久强制 Therefore 或 To solve；贡献第 2 项按论文类型写关键设计或证据贡献、依据与实际用途，不虚构新机制。Related Work 按固定三句收尾，Method 按真实输入输出衔接，模块先交代动机。
5. 摘要、引言、方法、实验与结论统一问题、名称、数字、范围和因果方向。整体发现与局部诊断分开，不能用相关或条件结果冒充机制证明。
6. 不改原始记录、实验协议、冻结 prompt 或模型回复，不编结果和引用。保留人工定版及并发修改。只读任务不写文件，缺证据的问题留给作者。
7. 检查最终 PDF 的句长、图表、脚注、分页与计页。只有明确必须遵守或禁止违反的要求标“铁律”，写法建议不升级为硬规则。
数字给单位、分母与版本，区分百分比与百分点、宏平均与微平均；不以分号拼接长句。核对文献实际版本、发布日期与预印本身份。
涉及 Limitations 时加载 cs-limitations：一个自然段，用 First 和 Second 写两项有据工作与具体边界；未测不当失败，实质限制与全文结论一致。
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
## 给 Codex 的实验整理提示词

依据：cs-writing-common · cs-abstract-introduction · cs-related-work · cs-method · cs-experiments · cs-visuals · cs-integration。

对应规则：只加载当前任务相关章节；真实句间钩子与问题—设计—证据对应；固定三项贡献：对象、机制与用途、发现；当前人工定版与证据边界优先。

### 中文

```text
读取 cs-paper-writing/SKILL.md：先读共享规则，只加载当前任务相关的章节 skill；不默认读全部例库。
核对目标会议及 track 的 AI 规定和材料使用权限，遵守当轮允许范围。未经许可，不向外部服务发送未公开稿件、review、个人数据或密钥。
材料：【引言主张、真实结果、指标定义、对照、重复记录与版本】
允许修改：【】；保护：【原始结果、执行协议与评价输入】

1. 先将每项主张对应到真实比较与证据。RQ 按需要使用，不要求每张表编号。
2. Setup 说明数据划分、Metrics、模型与基线、预算和真实设置。各指标交代单位、分母、汇总、不适用与无效输出处理。
3. 概述主发现，再按证据层级组织局部差异与独立条件分析。However 指出整体结果掩盖的差异；Separately 或 Next 转向真正独立的问题，不虚构串行或因果。
4. 每段讲一项发现、关键对照、范围与含义；不逐行读表。全局组成、场景发生率和条件子集使用各自真实分母，不能混称或直接相减。
5. 消融用合适对照检验实际设计；联合改变不能归因于单个模块。诊断、描述关联、因果证据及评价器一致率分别说明。
6. 表体名称、引用、数值与上标误差保持单行，先调允许范围内的列宽。均值与 SD、SE 或 CI 须基于真实观测及明确方法，说明统计或重采样单位和数量；单次运行不冒称跨运行稳定性，排名不等于显著性。Caption 保留核心口径，局部例外放对应脚注，检查最终 PDF。
7. 结果改变后回读已授权的摘要、引言和结论，不改冻结材料、不新增未经授权的实验。
成稿章首先概述主发现，再用 Specifically 展开分析。先核对有效覆盖，不预设共同子集；区分初始判分、人工复核标签和最终得分，一致率不冒称独立准确率。
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
## Intro 中文提纲提示词

依据：cs-writing-common · cs-abstract-introduction · cs-related-work · cs-method · cs-experiments · cs-visuals · cs-integration。

对应规则：只加载当前任务相关章节；真实句间钩子与问题—设计—证据对应；固定三项贡献：对象、机制与用途、发现；当前人工定版与证据边界优先。

### 中文

```text
读取 cs-paper-writing/SKILL.md：先读共享规则，只加载当前任务相关的章节 skill；不默认读全部例库。
核对目标会议及 track 的 AI 规定和材料使用权限，遵守当轮允许范围。未经许可，不向外部服务发送未公开稿件、review、个人数据或密钥。
材料：【问题、已有工作原文、真实设计、已核验发现与范围】
允许修改：【摘要、引言或其中指定段落】

1. 前两段建立领域价值与已有能力，比较具体不足；可合并、穿插或拆分，不强制段数。
2. 每项不足解释条件、机制与实际妨碍。缺少某功能后，说明已有成功仍不能区分什么，未报告不写成不存在。
3. 方法段首接回已建立的障碍，方法名后立即写产物、亮点与用途。逐项用 For [困难] 等准确钩子交代解法，不按旧模板恢复人工已删的 Therefore 或 To solve。
4. 贡献对象先出现，再写可核验依据与实际作用。来源、原则、产物和应用各有职责，模型可见输入与评价材料分开。
5. 结果段先概述有证据的发现，再解释命名发现及范围；归纳用 Therefore，展开用 Specifically，词由关系决定。
6. 普通正文引导句后接原生 itemize，固定三项：整体工作与任务；关键设计或证据贡献、依据及用途；有范围的实验发现。按论文类型填写新机制、构建或评价协议、比较或测量贡献；不虚构工作，也不机械重复困难标签。贡献后直接进入下一节。
7. 回读摘要与授权范围内的正文：同一问题、设计、数字、名称、范围与因果方向一致，压缩和展开不逐字照抄。先给中文逻辑，再按授权组织英文。
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
