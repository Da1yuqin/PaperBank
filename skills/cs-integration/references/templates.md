# 全文整合、标题、讨论、结论与附录：按需参考

以下以通用规则与教学模板为主；论文原题与简称全称另附出处，其余占位内容不代表研究事实或实测结果。

<a id="annotated-title"></a>

#### 短语型：亮点与研究内容

前半句概括亮点；冒号后交代目标与方法。

**English 填空模板**

[Memorable Phrase]: [Research Goal] with [Core Approach]


**高亮与旁批**

1. **[Memorable Phrase]**：留下记忆点。用短语概括亮点。例题并列强调查询与结果。
2. **[Research Goal]**：写清研究内容。冒号后交代对象与目标。例题教 RAG 模型使用搜索工具。
3. **[Core Approach]**：点明实现手段。填支撑目标的核心方法。例题用强化学习训练。

**论文原题**：Careful Queries, Credible Results: Teaching RAG Models Advanced Web Search Tools with Reinforcement Learning

前半句用并列短语概括亮点。Teaching… 交代对象与目标。with Reinforcement Learning 点明实现手段。

[论文原题 · AAAI 2026](https://ojs.aaai.org/index.php/AAAI/article/view/40299)

<a id="title-purpose"></a>

#### 目标型：实现什么能力

适合围绕某项能力提出设计的论文。

**English 填空模板**

Unlocking [Target Capability] in [Task or Setting]


**高亮与旁批**

1. **[Target Capability]**：目标要具体。填本文实现或改善的能力。后半句限定任务。

**论文原题**：Unlocking Proactivity in Task-Oriented Dialogue

Unlocking 引出目标，Proactivity 点名能力。Task-Oriented Dialogue 限定场景。

[论文原题 · arXiv v2](https://arxiv.org/abs/2605.22240v2)

<a id="title-acronym"></a>

#### 简称型：让名字好记

适合命名方法、系统、数据集或基准。冒号后交代研究内容。

**English 填空模板**

[ACRONYM]: [Full Name or Core Contribution]


**高亮与旁批**

1. **[ACRONYM]**：简称与全称对应。先定准确全称，再选易记简称。首次定义时加粗对应字母。

**论文原题**：SEAD: Self-Evolving Agent for Multi-Turn Service Dialogue

**正文首次定义（加粗为教学标示）**

**S**elf-**E**volving **A**gent for Service **D**ialogue (SEAD)

```latex
\textbf{S}elf-\textbf{E}volving \textbf{A}gent for Service \textbf{D}ialogue (SEAD)
```

S、E、A、D 分别取自 Self、Evolving、Agent、Dialogue。摘要全称不含标题中的 Multi-Turn。Service 保留，但不另取字母。

[论文原题与摘要全称 · arXiv v3](https://arxiv.org/abs/2602.03548v3)

**论文原题**：SAGE: A Service Agent Graph-guided Evaluation Benchmark

**正文首次定义（加粗为教学标示）**

**S**ervice **A**gent **G**raph-guided **E**valuation (SAGE)

```latex
\textbf{S}ervice \textbf{A}gent \textbf{G}raph-guided \textbf{E}valuation (SAGE)
```

S、A、G、E 分别取自 Service、Agent、Graph-guided、Evaluation。A 来自 Agent，不是标题开头的冠词。Benchmark 不进入简称。

[论文原题与摘要全称 · arXiv v1](https://arxiv.org/abs/2604.09285v1)

<a id="annotated-discussion"></a>

#### 讨论：发现的含义

解释发现的含义及实际用途。

**English 填空模板**

Together, [finding 1] and [finding 2] suggest [answer to the research question] under [tested conditions]. This pattern is consistent with [explanation linked to the design], as supported by [specific comparison or analysis]. For [target use], these findings imply [practical meaning within the tested scope]. [Unresolved question] motivates further study of [specific follow-up].


**高亮与旁批**

1. **[finding 1] and [finding 2]**：已有发现。填实验章已建立的发现。各项共同回答同一个问题。
2. **[answer to the research question] under [tested conditions]**：研究含义。回答 Intro 的问题。保留发现成立的条件。
3. **[explanation linked to the design], as supported by [specific comparison or analysis]**：解释与依据。填设计解释及其支持证据。未经机制检验时保留推断措辞。
4. **For [target use], these findings imply [practical meaning within the tested scope].**：实际意义。填使用者、任务与可支持的判断。按研究类型选用。
5. **[Unresolved question] motivates further study of [specific follow-up].**：后续问题。由未回答的问题引出下一步。仅在需要时保留。

<a id="annotated-conclusion"></a>

#### 结论：工作、证据与回答

用核心设计与发现回答 Intro 的问题。

**English 填空模板**

We introduced [work name and type] to address [research problem]. By [core design and action], [work name] [actual capability]. Experiments on [evaluation scope] show [main quantitative result] and reveal [key finding]. These findings indicate [answer to the research question within the established scope].


**高亮与旁批**

1. **We introduced [work name and type] to address [research problem].**：收束贡献。填本文工作及其解决的问题。沿用 Intro 的研究对象。
2. **By [core design and action], [work name] [actual capability].**：概括设计。By 后填动作的 -ing 形式。再写核心设计能完成什么。
3. **Experiments on [evaluation scope] show [main quantitative result] and reveal [key finding].**：概括证据。填比较范围、数字与关键发现。对应摘要、引言及实验。
4. **These findings indicate [answer to the research question within the established scope].**：回答起点。写研究现在能回答什么。结论强度与正文一致。

<a id="template-references"></a>
#### 引文与书目格式

引文放 .tex，条目放 .bib，两处引用键一致。命令与书目样式沿用会议模板。

**正文引用（.tex）**

引用紧跟判断。本例用 citep；模板只支持 cite 时换用 cite。书目加载命令沿用官方模板。

```latex
[Claim supported by the cited work] \citep{source_key}.
```

**文献条目（.bib）**

会议用 inproceedings；期刊用 article，填写 journal。字段逐项核对原文，作者间用 and 分隔。无 DOI 则删除，可补真实 URL。

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

#### 附录：说明补充内容

每节对应一项正文内容，补足复现或分析细节。

**English 填空模板**

To reproduce [method or experiment] in Section [X], this section provides [necessary implementation or evaluation details]. We specify [actual settings and selection procedure] for [all relevant systems or conditions]. Table [Y] reports [supplementary results and their aggregation], extending the analysis of [main-text question] to [additional tested condition]. The results show [supported conclusion about that condition].


**高亮与旁批**

1. **To reproduce [method or experiment] in Section [X]**：正文入口。点名对应的正文方法或实验。正文也引用本附录节。
2. **[necessary implementation or evaluation details]**：本节材料。填算法、参数、提示词或评分规则。按主题保留复现所需信息。
3. **[actual settings and selection procedure] for [all relevant systems or conditions]**：设置与选择依据。填实际设置及选择依据。覆盖本节全部比较对象。
4. **Table [Y] reports [supplementary results and their aggregation], extending the analysis of [main-text question] to [additional tested condition].**：补充结果。有补充实验时保留。写清表中内容、汇总方式与问题。
5. **The results show [supported conclusion about that condition].**：本节结论。填该条件下的发现。纯实现节删去本句及前一句。

---

Da1yuqin / [StarPaper](https://da1yuqin.github.io/StarPaper/)，[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)。转载保留署名、出处与许可，改编注明改动。
