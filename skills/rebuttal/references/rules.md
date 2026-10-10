# Rebuttal 规则与模板

以下均为教学模板与假设情境，不是真实审稿记录。填写真实证据；材料权限与当轮规定先确认。

## 通用要求

### 每个审稿关切有回应

一条意见有几个问题就逐个答；不能仅以“已全部修改”替代逐项回应。

模拟审稿问题与回复只用于教学，不是真实审稿记录。补实验、修订和回复格式以当轮官方政策为准；没有完成的事不写成已完成。

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

每个关切均须回应，并说明证据或无法完成的原因。

### 回复讨论事实

给理由和证据；不写“显然”“你错了”，也不乱认错。

模拟审稿问题与回复只用于教学，不是真实审稿记录。补实验、修订和回复格式以当轮官方政策为准；没有完成的事不写成已完成。

**讨论事实，不评价审稿人**

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

回复讨论条件、结果与表述，不评价审稿人的动机或能力。

### 回复能定位结果

给图表、章节或结果位置；完成、计划与未解决分开，未完成实验不配虚构结果。

模拟审稿问题与回复只用于教学，不是真实审稿记录。补实验、修订和回复格式以当轮官方政策为准；没有完成的事不写成已完成。

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

## 逐题回复与 revise loop

### 4.1 拆审稿意见

读取完整 review：Summary 核对理解，Strengths 记录认可点，Weaknesses 与 Questions 提取待回应关切。

教学模板；【】填真实材料。

- 先查当轮 AI 与保密规定；确认材料可在所选工具中使用后，再提供稿件和 review。
- 保留原问题与顺序，一句话有多问就拆开。区分机制解释与实施情况，分别回应。
- 区分描述不清、缺对照和机制未证实；分别给案例、比较和针对性检验。
- 从原意见判断阅读关注点，不凭 confidence 猜身份或保证提分；查当轮回复规则。

The reviewer asks whether the gain comes from retrieval quality or answer generation.

审稿人问的是：收益来自检索质量，还是答案生成。

**第 1 句：**先说清真正的问题；这里要区分两种解释。

We compare the two generators using the same retrieved passages.

我们使用相同的检索段落比较两个生成器。

**第 2 句：**对照须对应原问题：固定检索，改变生成器。

### 4.2 逐题回复

首句直接回答问题，再给证据、解释与位置；流程问题用明确来源的案例展示。

教学模板；【】填真实材料。

- 标题沿用原问题；首句给结论或具体值。
- 给设置、对照、绝对值和指标方向；数据适合表格就用表格。
- 说明证据如何回答问题，附表号、节号或行号。
- 已有实验能回答就整理出来；缺关键证据时做能隔离争议的最小对照，不盲目把全部基线重跑。
- 感谢具体、简短。说明已经补出的内容，不用一句“我们将补充”代替答案。
- 一个段落回一个小点。表格写结果与必要设置差异，分析接回贡献；没有标准条件支持时不能把落后全归咎于不公平。

The gain persists when retrieval is held fixed.

固定检索后，收益仍然存在。

**第 1 句：**首句直接回答；只有相应对照支持时才能用。

With identical passages and decoding settings, 【method】 scores 【A】 versus 【B】 for 【baseline】 on 【metric】 (higher is better; Table 【R1】).

使用相同段落和解码设置时，【方法】在【指标】上为【A】，而【基线】为【B】（越高越好；表【R1】）。

**第 2 句：**给协议、对照、绝对值和位置，不要只报“提升显著”。

This comparison isolates the generator change under the tested retrieval setting.

这一比较在所测试的检索设置下隔离了生成器改动。

**第 3 句：**收束到已检验的范围，不扩大到所有场景。

### 4.3 区分两种解释

准确复述审稿人的推理，用针对性对照检验争议前提，并说明证据支持的结论。

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

### 4.4 澄清：定义、流程、例子

说明定义、真实输入与各步产物，定位争议环节；公式数量不能替代解释。

教学模板；【】填真实材料。

- 术语不清给定义，流程不清给案例，效果不清给对照。
- 确有错误就改；不同意就给依据。不以“你误读了”替代澄清与证据。

Here, 【term】 denotes 【concrete definition】.

这里，【术语】指【具体定义】。

**第 1 句：**定义先落到对象，不绕回抽象名词。

For input 【x】, the module performs 【operation】 and returns 【y】 to 【next module】.

输入【x】后，该模块执行【操作】，将【y】交给【下一模块】。

**第 2 句：**一条样例走完整条路径。

Section 【N】 specifies this interface; we clarify 【ambiguous phrase】 in 【permitted revision location】.

第【N】节说明了这一接口；我们在【允许的修订位置】澄清【歧义表述】。

**第 3 句：**位置要真实存在；会议不允许改稿时，只在回复中澄清。

### 4.5 Revise loop

按原问题逐轮检查覆盖、证据与逻辑，仅修改未通过的回复，再压缩文字并调整语气。

教学模板；【】填真实材料。

- 确认材料可在所选工具中使用后，再给 Codex 论文、原始 review、证据和回复。
- 逐题输出：原问题、回复位置、剩余缺口、改法、所需证据。
- 先查漏答、证据和逻辑，再缩文字、调语气。改完重查同一张问题清单。
- 每问有答、证据对应、逻辑通顺、篇幅合规就停；缺实验交给人决定。
- 模拟用于查漏洞，不预测评分变化或录用。

Concern: 【verbatim concern】. Response location: 【paragraph/table】. Remaining gap: 【specific gap】.

原问题：【审稿原话】。回复位置：【段落/表】。剩余缺口：【具体缺口】。

**第 1 句：**每条批评必须定位，不能仅给“还不够有说服力”等笼统评价。

Minimal fix: 【edit】. Required evidence: 【existing result or experiment needed】.

最小修改：【改法】。所需证据：【已有结果或需要的实验】。

**第 2 句：**把改文字和补证据分开，便于作者判断。

### 4.6 第二轮与 AC 总结

先逐题回应，再向 AC 概括关键问题、证据与剩余分歧，准确引用已确认的评价。

教学模板；【】填真实材料。

- 追问接回原问题和证据，不重贴整份回复。
- 写清剩余限制，不猜未回复审稿人的态度。
- 不请求提分或接收，把判断留给审稿方。

Regarding the follow-up on 【issue】, 【direct answer】; the supporting comparison is in 【location】.

针对【问题】的追问，【直接答案】；支持这一答案的比较见【位置】。

**第 1 句：**只写新增信息。

The main concern was 【issue】. Our response provides 【evidence】, supporting 【bounded conclusion】.

主要关切是【问题】。回复提供了【证据】，支持【限定结论】。

**第 2 句：**明确说明问题、回复及其依据。

---

Da1yuqin / PaperBank，[原文](https://da1yuqin.github.io/PaperBank/#rebuttal)，[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)。
