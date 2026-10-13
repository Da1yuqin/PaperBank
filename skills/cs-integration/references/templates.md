# 全文整合、标题、讨论、结论与附录：按需参考

以下为通用规则与教学模板，不是真实论文原文、研究事实或实测。

<a id="annotated-title"></a>

#### 标题模板

用一行交代关键设计与研究任务。

**English 填空模板**

[Method Name]: [Core Design] for [Research Task]


**高亮与旁批**

1. **[Method Name]**：方法名。填已确定的方法或数据集名称；没有独立命名时，可直接从核心设计写起。
2. **[Core Design]**：关键改动。填区别于已有工作的具体设计，不填 novel、powerful 等自评。
3. **[Research Task]**：研究对象。让读者一眼知道解决什么任务。范围过宽时，补必要条件。

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
2. **By [core design and action], [work name] [actual capability].**：概括设计。留下最关键的设计与作用，不重新展开完整方法流程。
3. **Experiments on [evaluation scope] show [main quantitative result] and reveal [key finding].**：概括证据。填真实比较范围、代表性数字和关键实验结论；与摘要、引言及实验章对应。
4. **These findings indicate [answer to the research question within the established scope].**：回答起点。用一句话说清研究现在能回答什么，保持正文已经建立的结论强度。

<a id="template-references"></a>
#### 引文与书目格式

```latex
[Claim supported by the cited work] \citep{source_key}.
We use [component and actual version] \citep{component_key}.

@inproceedings{source_key,
  title     = {[Verified title]},
  author    = {[Verified author list]},
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
