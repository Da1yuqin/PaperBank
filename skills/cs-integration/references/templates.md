# 全文整合、标题、讨论、结论与附录：按需参考

以下以通用规则与教学模板为主；论文原题与简称全称另附出处，其余占位内容不代表研究事实或实测结果。

<a id="annotated-title"></a>

#### 短语引题：记忆点与研究内容

前半句用简短短语概括亮点，后半句交代研究对象、目标和方法。

**English 填空模板**

[Memorable Phrase]: [Research Goal] with [Core Approach]


**高亮与旁批**

1. **[Memorable Phrase]**：留下记忆点。用简短、准确的短语概括亮点。例题前半句用并列结构呼应查询与结果。
2. **[Research Goal]**：写清研究内容。冒号后交代研究对象和目标能力。例题写明教会 RAG 模型使用高级网页搜索工具。
3. **[Core Approach]**：点明实现手段。填支撑目标的核心方法。例题用 with Reinforcement Learning 交代训练方式。

**论文原题**：Careful Queries, Credible Results: Teaching RAG Models Advanced Web Search Tools with Reinforcement Learning

Careful Queries, Credible Results 用两段并列短语留下记忆点；Teaching… 交代对象与目标；with Reinforcement Learning 点明实现手段。不能只留前半句，让读者猜研究内容。

[论文原题 · AAAI 2026](https://ojs.aaai.org/index.php/AAAI/article/view/40299)

<a id="title-purpose"></a>

#### 目标型：希望实现什么能力

适合围绕某项能力提出设计的论文。

**English 填空模板**

Unlocking [Target Capability] in [Task or Setting]


**高亮与旁批**

1. **[Target Capability]**：目标要具体。写本文实现或改善的能力，后半句限定任务。目标明确即可，不必在标题罗列所有模块。

**论文原题**：Unlocking Proactivity in Task-Oriented Dialogue

Unlocking 说明目标，Proactivity 点名能力，Task-Oriented Dialogue 限定场景；不在标题展开训练流程。

[论文原题 · arXiv v2](https://arxiv.org/abs/2605.22240v2)

<a id="title-acronym"></a>

#### 简称型：给工作一个好记的名字

适合需要命名的方法、系统、数据集或基准。冒号后写清是什么，名字本身不能代替研究信息。

**English 填空模板**

[ACRONYM]: [Full Name or Core Contribution]


**高亮与旁批**

1. **[ACRONYM]**：简称与全称对应。先确保全称准确，再选容易记住的简称。正文首次定义时，按下面示范加粗构成简称的字母。

**论文原题**：SEAD: Self-Evolving Agent for Multi-Turn Service Dialogue

**正文首次定义（加粗为教学标示）**

**S**elf-**E**volving **A**gent for Service **D**ialogue (SEAD)

```latex
\textbf{S}elf-\textbf{E}volving \textbf{A}gent for Service \textbf{D}ialogue (SEAD)
```

S、E、A、D 对应 Self、Evolving、Agent、Dialogue。摘要展开式不含标题中的 Multi-Turn；Service 保留在全称中，不另取字母。

[论文原题与摘要全称 · arXiv v3](https://arxiv.org/abs/2602.03548v3)

**论文原题**：SAGE: A Service Agent Graph-guided Evaluation Benchmark

**正文首次定义（加粗为教学标示）**

**S**ervice **A**gent **G**raph-guided **E**valuation (SAGE)

```latex
\textbf{S}ervice \textbf{A}gent \textbf{G}raph-guided \textbf{E}valuation (SAGE)
```

S、A、G、E 对应 Service、Agent、Graph-guided、Evaluation。标题开头的 A 是冠词；简称中的 A 来自 Agent，Benchmark 不进入简称。

[论文原题与摘要全称 · arXiv v1](https://arxiv.org/abs/2604.09285v1)

<a id="annotated-discussion"></a>

#### 讨论：发现的含义

解释关键发现改变了什么认识，以及对实际使用有什么意义。

**English 填空模板**

Together, [finding 1] and [finding 2] suggest [answer to the research question] under [tested conditions]. This pattern is consistent with [explanation linked to the design], as supported by [specific comparison or analysis]. For [target use], these findings imply [practical meaning within the tested scope]. [Unresolved question] motivates further study of [specific follow-up].


**高亮与旁批**

1. **[finding 1] and [finding 2]**：已有发现。填实验章已经建立的、共同回答同一个问题的发现。
2. **[answer to the research question] under [tested conditions]**：研究含义。说明这些发现如何回答 Intro 的问题，并保留实际成立的条件。
3. **[explanation linked to the design], as supported by [specific comparison or analysis]**：解释与依据。填与方法设计有关的解释，紧跟支持它的对照或分析。没有机制检验时，保留 is consistent with 这类推断措辞。
4. **For [target use], these findings imply [practical meaning within the tested scope].**：实际意义。说明谁在什么任务中可以据此做什么判断。此句按研究类型选用。
5. **[Unresolved question] motivates further study of [specific follow-up].**：后续问题。仅在需要时保留：从尚未回答的问题推出具体下一步，不重复贡献。

<a id="annotated-conclusion"></a>

#### 结论：工作、证据与回答

用核心设计与关键发现回答 Intro 的研究问题。

**English 填空模板**

We introduced [work name and type] to address [research problem]. By [core design and action], [work name] [actual capability]. Experiments on [evaluation scope] show [main quantitative result] and reveal [key finding]. These findings indicate [answer to the research question within the established scope].


**高亮与旁批**

1. **We introduced [work name and type] to address [research problem].**：收束贡献。填本文提出什么、解决什么问题；与 Intro 保持同一研究对象。
2. **By [core design and action], [work name] [actual capability].**：概括设计。By 后填实际动作的 -ing 形式，再写方法能完成什么。保留核心设计与作用，不展开完整流程。
3. **Experiments on [evaluation scope] show [main quantitative result] and reveal [key finding].**：概括证据。填真实比较范围、代表性数字和关键实验结论；与摘要、引言及实验章对应。
4. **These findings indicate [answer to the research question within the established scope].**：回答起点。用一句话说清研究现在能回答什么，保持正文已经建立的结论强度。

<a id="template-references"></a>
#### 引文与书目格式

正文引文放入 .tex，文献条目放入 .bib。引用键必须一致；沿用会议模板的引用命令与书目样式。

**正文引用（.tex）**

把引用紧跟在它支持的判断后。下面使用 citep；模板只支持 cite 时，改用 cite。书目加载命令沿用官方模板。

```latex
[Claim supported by the cited work] \citep{source_key}.
```

**文献条目（.bib）**

会议论文用 inproceedings，期刊论文用 article 并填写 journal。以下每个字段都从原文核对；作者之间用 and 分隔。无 DOI 就删掉该字段，必要时加真实 URL。

```bibtex
@inproceedings{source_key,
  title     = {[Verified title]},
  author    = {[Family name, Given name] and [Family name, Given name]},
  booktitle = {[Verified proceedings title]},
  year      = {[Publication year]},
  doi       = {[Verified DOI]}
}
```

<a id="annotated-appendix"></a>

#### 附录：开头说明补什么

给每个附录小节一个正文入口，集中交代复现细节或补充分析。

**English 填空模板**

To reproduce [method or experiment] in Section [X], this section provides [necessary implementation or evaluation details]. We specify [actual settings and selection procedure] for [all relevant systems or conditions]. Table [Y] reports [supplementary results and their aggregation], extending the analysis of [main-text question] to [additional tested condition]. The results show [supported conclusion about that condition].


**高亮与旁批**

1. **To reproduce [method or experiment] in Section [X]**：正文入口。点名正文哪项方法或实验需要这里的细节，正文也在对应位置引用本附录节。
2. **[necessary implementation or evaluation details]**：本节材料。填足以复现的具体信息类型，如算法、参数、提示词或评分规则；按小节主题选用。
3. **[actual settings and selection procedure] for [all relevant systems or conditions]**：设置与选择依据。交代实际采用的设置及如何确定，覆盖本节比较涉及的全部对象。
4. **Table [Y] reports [supplementary results and their aggregation], extending the analysis of [main-text question] to [additional tested condition].**：补充结果。有补充实验才保留：说明表里是什么、如何汇总、它扩展了正文的哪个问题。
5. **The results show [supported conclusion about that condition].**：本节结论。给该条件下的发现，回扣本节目的。纯实现细节小节删除这句及前一句。

---

Da1yuqin / [StarPaper](https://da1yuqin.github.io/StarPaper/)，[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)。转载保留署名、出处与许可，改编注明改动。
