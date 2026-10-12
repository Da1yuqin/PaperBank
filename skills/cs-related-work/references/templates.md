# 相关工作：按需参考

以下为通用规则与教学模板，不是真实论文原文、研究事实或实测。

#### Related Work：完整模板

按共同机制归类。可直接比较的工作安排对应基线；不能直接比较时说明设置差异。

教学模板；【】填真实材料。

- 每个主题按路线、机制和已有能力归类，再用固定三句收尾：缺口、本文做法、应用及问题解决。
- 【铁律】每个主题末尾固定三句：However, [具体缺口]. → [承接短语], we [动作] [对象] based on [方法或原则]. → This enables [实际应用], [效果动词] [解决的同一问题].。位置不互换，最后落在缺口如何解决；预期用途不写成已验证效果。
- 结尾的对象、范围、关键词与 Intro 一致；各小节讲不同缺口。
- 小节标题简短。短主题一段写完，复杂主题按问题分段。
- 相近工作的差异提前讲清。引用准确完整，不因图相似或结果不利而漏引。
- 引用数量不是会议配额；删除重复说明，不加入无关文献。
- 【铁律】This enables 后写完整实际应用，末尾回扣 However 的同一缺口；不重复产物名称或局部属性。

StarPaper 规范化写法；主题数量按论文内容

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

[Transition], we [action] [object] based on [method or principle].

[承接短语]，我们基于[方法或原则]，对[对象]实施[动作]。

**第 5 句：**【铁律】缺口之后立即给本文做法；主语为 we，对象和原则应对前句同一个不足。

This enables [actual application], [resolving / addressing / reducing] [the same gap].

这支持[实际应用]，从而[解决／应对／减轻][同一个缺口]。

**第 6 句：**【铁律】先填完整实际应用，后半句处理 However 的同一缺口。不能只重复产物名或局部属性；效果动词按证据强度选择。

**完整 LaTeX 结构模板**

```latex
\section{Related Work}
\subsection{[Short Topic A]}
[Research line] addresses [shared task] by [shared mechanism]~\cite{...}.
One group [mechanism A], whereas another group [mechanism B]~\cite{...}.
More recent extensions [additional established capability]~\cite{...}.
However, these approaches do not establish [Intro challenge A] under [scope A].
To address this gap, we [action A] [object A] based on [method or principle A].
This enables [actual application A], [resolving / addressing / reducing] [the same gap A].

\subsection{[Short Topic B]}
[Research line B] evaluates [property] using [evaluation basis]~\cite{...}.
Other evaluations [substantive extension]~\cite{...}.
However, [Intro challenge B] remains unresolved under [scope B].
To overcome this limitation, we [action B] [object B] based on [method or principle B].
This enables [actual application B], [resolving / addressing / reducing] [the same gap B].
```

---

Da1yuqin / [StarPaper](https://da1yuqin.github.io/StarPaper/)，[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)。转载保留署名、出处与许可，改编注明改动。
