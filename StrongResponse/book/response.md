# 💪 StrongResponse

首句回答，证据跟上。

<details><summary>更新记录</summary>


**2026-10-14 21:06 · 调整 AC letter 格式要求 · skill 更新**

- 移除对称呼与摘要标签的限制。

**2026-10-14 20:19 · 三个独立 skill、审稿偏好与模拟复核 · skill 更新**

- 拆分 AC letter、Rebuttal、审稿人画像与模拟三个下载包。
- 第一部分增加从 Weaknesses 和审稿文本逆推偏好，Revise loop 按画像审核、反馈、修改、再审核。
- 删除额外添加的“限定结论”批注，改为实验分析；AC letter 恢复正面引文、评分、真实改分与逐审稿人总结。
- 开头增加独立打卡统计与随机卡通提分动画。

**2026-10-14 16:39 · 上线与 StarPaper 互相链接**

- 开头增加“论文写作请参考：StarPaper”，StarPaper 开头增加 StrongResponse 入口。
- 德牧换为白色贴身肌肉背心，保留完整画面与肩臂肌肉。
- 发布六章教程、审稿人画像、更新记录与可下载 skill。

**2026-10-12 · 开头增加更新记录**

- 增加与 BeautyPaper 一致的折叠栏，展开后可用独立滚动条查看记录。
- 最近更新排在前面，网页与 Markdown 同步显示。

**2026-10-12 · 审稿人刻板印象与投入优先级 · skill 更新**

- 八种常见刻板印象按话量、语气、评分和 Confidence 描述，删除模拟审稿原话。
- 投入比例简写为高、极大（>90%）、中和极高，完整回复始终是合格线。
- 新手杀手“笑面虎”放在画像最后，并加入投入表最后一行，优先级为极高。
- 补充尊重、情绪价值，以及漏答、降分和影响 AC 判断的风险。

**2026-10-12 · 了解审稿人，分配回复精力 · skill 更新**

- 第一章改为“了解你的审稿人”，原有回复流程顺移，形成六章结构。
- 章首加入动机：Response 时间紧急，合理分配精力将拉开你和竞争者的差距。
- 用灰色斜体注明会议回复范围，期刊回复之后有空会更新。

**2026-10-11 · StrongResponse 独立整理 · skill 更新**

- 整理问题清单、逐题回复格式、四类回答模板、Revise loop、追问与 AC 总结。
- 用同一份内容生成网页、Markdown 和 rebuttal skill，保留完整回复案例与旁批。

</details>


论文写作请参考：[StarPaper](https://da1yuqin.github.io/StarPaper/)

![戴眼镜、穿白色贴身肌肉背心的健壮德牧，用“回答、证据、结论”说明研究，与一位惊讶的人类学者讨论。](../assets/strongresponse-negotiation.png?v=20261014-white-tanktop)

先用“审稿人画像与模拟”分析 review，再用 Rebuttal 起草；按画像模拟审核、根据意见修改，再审核。全部回复完成后，用独立 AC letter 总结真实评价与回应。当轮官方格式、字数、匿名与 AI 使用规定优先。

## 三个独立 skill

- **审稿人画像与模拟**：逆推关切与偏好，按画像模拟审核并给反馈。 [下载 ZIP](../assets/rebuttal-reviewer-profile-skill.zip) · [SKILL.md](../skills/rebuttal-reviewer-profile/SKILL.md)
- **Rebuttal**：起草逐题回复、追问，并根据模拟意见修改。 [下载 ZIP](../assets/rebuttal-skill.zip) · [SKILL.md](../skills/rebuttal/SKILL.md)
- **AC letter**：整理审稿人正面评价、评分、真实改分和核心回应。 [下载 ZIP](../assets/ac-letter-skill.zip) · [SKILL.md](../skills/ac-letter/SKILL.md)

## 给 Codex 的提示词

```text
分三步使用 StrongResponse：
1. 读取 rebuttal-reviewer-profile/SKILL.md，根据完整 reviews【】和真实讨论【】建立画像、偏好与原问题清单，每项保留原话依据。
2. 读取 rebuttal/SKILL.md，用论文【】、画像【】、真实证据【】起草逐题回复。随后用画像与模拟 skill 审核，Rebuttal skill 根据意见修改，再用同一画像复核，运行 Revise loop。
3. 全部回复完成后，读取 ac-letter/SKILL.md，用真实 review、二轮记录、评分和已完成的回应写 AC letter。
当轮规则【】；允许修改的文件【】。没有依据不编结果，模拟通过不冒充真实认可；补实验、改稿和提交另按作者授权。
```

<a id="reviewer-profile"></a>
## 1. 了解你的审稿人

Response 时间紧急，合理分配精力将拉开你和竞争者的差距。

*本教程针对会议回复，期刊回复之后有空会更新。*

- 先读懂每位审稿人真正卡在哪里，再决定把时间花在哪。这里的“价值”指额外回复投入可能带来的作用。
- 分开预估三件事：是否会参与第二轮讨论，解决关切后是否愿意调整评价，以及未解决的质疑会不会影响 AC 和其他审稿人的判断。
- 从 Weaknesses 和审稿人的全部文本逆推偏好：Strengths 看欣赏什么，Summary 看如何理解论文，Questions 看想得到什么证据，附录与细节问题看阅读深度。每项记录原话依据，不只凭分数或 Confidence 判断。
- 先看话量、语气、评分与 Confidence 的组合，形成初步画像；再看意见是不是触及论文的核心、有没有后续互动。尤其别被高分和客气语气麻痹：“笑面虎”也可能是需要极高投入的关键审稿人。
- 【铁律】每位审稿人都先得到完整、正确、证据可定位的回复。再把额外精力投入关键审稿人和高价值审稿人；低价值审稿人保证逐题回复完毕即可，不需要追求完美。
- 画像随讨论更新。高价值与关键可能重叠，重叠时按关键处理；不活跃但留下了决定性负面论点的人，仍要认真处理其论点，供 AC 核查。分类与投入判断留给作者使用，不写进正式回复。

<a id="reviewer-preferences"></a>
### 审稿偏好：从 Weaknesses 和审稿文本逆推

先找审稿人反复强调、措辞最强、与评分理由直接相连的关切。再判断他更需要实验、解释还是尊重感；同一人可以兼有多种偏好。下面是分析维度，不是替他预设身份。

| 偏好 | 看哪些原话 | 怎么回复 | 模拟复核重点 |
| :--- | :--- | :--- | :--- |
| 最关心的问题 | Weaknesses 中反复出现的质疑、明确的评分理由，以及二轮继续追问的部分。 | 先把这一问答透，其他回应围绕它补证据与解释。 | 把这一问设为最高要求；逐句检查是否真正消除疑虑。 |
| 情绪价值与尊重 | 肯定哪些细节，是否强调自己的建议被忽略，是否看重认真讨论和细致回应。 | 准确复述他的关切，解释意见如何帮助完善论文，给具体、克制的感谢。 | 检查是否被认真理解；强硬驳斥、敷衍感谢或转移问题都要给出反馈。 |
| 实验量与证据 | 多次要求对照、消融、重复实验、完整结果，或直接给出想看的实验设计。 | 按关切提供已有或新完成的对应实验，解释结果为何回答这道题。 | 按其要求检查证据类型、实验覆盖和结果分析；设计动机或未来承诺不能代替数据。 |
| 背景知识与解释 | 定义和流程问题较多，Summary 有误解，或低 Confidence 与基础概念问题同时出现。也可能是论文没有讲清楚。 | 可能需要更多背景：先解释概念和中间逻辑，用一个 case 带读，语气像认真讨论。 | 不默认他懂术语；检查解释是否足够、有无跳步，是否让人感到被说教。 |
| 细节与严格程度 | 是否读附录、发现细节遗漏、核对数字与设置，是否指出明确的逻辑链或近邻工作。 | 补齐其真正关注的细节，保持每题自洽；高分、客气也可能要求极高。 | 按阅读深度提高严格程度；重点检查漏答、实验设置、推理链和措辞是否经得起细读。 |

把“原话 → 偏好判断 → 回复方式 → 模拟检查重点”连起来。缺少依据的项写未知；有新追问或讨论记录时再更新画像。

| 类别 | 预估 | 投入比例 |
| :--- | :--- | :--- |
| 高价值审稿人 | 较可能参与第二轮，而且已有信号表明：核心关切得到解决后，愿意重新评价，存在涨分机会。 | 高 |
| 关键审稿人 | 较可能继续参与，且其负面论点可能被 AC 或其他审稿人采纳，拉低对论文的整体评价。是需要优先挽回的头疼类型。 | 极大（>90%，不亚于再写一篇） |
| 低价值审稿人 | 预估不会或很少参与后续回复，也没有仍未解决的决定性负面问题；继续打磨回复的额外收益较低。 | 中（肯定要回复呀！没有低投入审稿人！中规中矩到达合格线，至少 AC 会瞄一眼的） |
| 笑面虎审稿人（新手杀手） | 高分、客气、意见多、句句要点，Confidence 通常高。他尊重你，你尊重他；漏答或答不全有降分、影响 AC 拒稿判断的风险。 | 极高 |

下面是按话量、语气、评分和 Confidence 整理的常见刻板印象，用来提前分配精力。读 review 时把几项特征放在一起看，再根据具体问题与讨论更新判断。

### 1.1 高价值：友善支持型

**话量：**少到中等，关切比较集中；**语气：**正面、友善；**评分：**中高，或接近接收线；**Confidence：**通常中等。

**常见行为：**认可贡献，也愿意听解释。主要卡在一两个理解问题，反馈具体，解决关切后有重新评价的空间。

**优先级：**高

**理由：**有支持的基础，也有可以解决的卡点。让对方顺畅地理解你的答案，比反复铺已经认可的贡献更值得投入。

### 1.2 高价值：证据导向型

**话量：**中等到多，问题具体；**语气：**中性、克制；**评分：**中间或边界分；**Confidence：**通常中高。

**常见行为：**会提明确的对照、消融或解释要求，有相对清楚的判断门槛。比较在意证据能否回答原问题，而不是回复有多长。

**优先级：**高

**理由：**你知道他在等什么，投入方向比较明确。证据接得住，才有争取评价转变的空间。

### 1.3 关键：技术否定型

**话量：**多，分析很细；**语气：**负面，技术质疑明确；**评分：**低；**Confidence：**通常高。

**常见行为：**把核心结论拆开检查，盯数据泄漏、公平比较、替代解释或推导漏洞。不是只说不喜欢，而是能写出为什么结论不成立。

**优先级：**极高

**理由：**他的质疑直接影响论文能不能成立，也方便 AC 和其他审稿人沿着同一条论证理解。需要优先挽回核心问题。

### 1.4 关键：新颖性否定型

**话量：**中等到多，文献比较密集；**语气：**负面、挑剔；**评分：**低；**Confidence：**通常中高。

**常见行为：**很熟悉相关工作，反复盯最接近的方法，追问到底新在哪里。常把几个表面差异归为已有工作的组合或小改动。

**优先级：**极高

**理由：**新颖性不足是一个简洁、容易传播的拒稿理由。如果真实贡献没有解释清楚，其他正面结果也可能救不回来。

### 1.5 关键：强势讨论型

**话量：**多，后续跟进也多；**语气：**负面、立场鲜明；**评分：**低，或坚持负面推荐；**Confidence：**通常高。

**常见行为：**会读别人的意见，持续追问同一条核心争议，参与感很强。自己的否定理由写得清楚，容易成为讨论中的共同关注点。

**优先级：**极高

**理由：**不仅要回应他本人，还要处理这条论点对 AC 和其他审稿人的影响。回复如果漏了关键一步，讨论可能越来越不利。

### 1.6 低价值：简短支持型

**话量：**少，意见集中在小项；**语气：**正面；**评分：**高；**Confidence：**常见中或低。

**常见行为：**基本认可论文，主要提文字、引用和表达问题，不太展开技术追问，后续讨论也可能较少。

**优先级：**中

**理由：**肯定要回复呀！没有低投入审稿人！中规中矩到达合格线，至少 AC 会瞄一眼的。

### 1.7 低价值候选：公事公办型

**话量：**少，比较概括或有模板感；**语气：**中性、平淡；**评分：**常见中间分；**Confidence：**常见中或低。

**常见行为：**关注点较泛，详细展开和后续互动较少，主要问题也许只是表达、设置说明或小修。

**优先级：**中

**理由：**完整、正确地回复到合格线即可。如果少量意见里藏着决定性负面问题，就按关键审稿人投入，不能因为话少而漏掉。

### 1.8 新手杀手：笑面虎审稿人

**话量：**多，意见非常密集；**语气：**客气、诚恳、客观；**评分：**高；**Confidence：**通常高。

**常见行为：**给了高分，也给了你情绪价值，但是句句都是要点。读得非常认真，方法、实验、附录和论证细节都不放过，知道你的死穴。

**优先级：**极高

**理由：**他给了你情绪价值，你需要给他更大的情绪价值。他要的是尊重：他尊重你，你尊重他。认真接住每个问题、完整回答，就是这种尊重。发现你漏了问题，或者回答不全面，原本的高分也可能直接降下来。更要命的是，他的文字态度诚恳、客观，让人想要阅读（要命）；核心质疑一旦没有接住，可能直接把 AC 的判断推向拒稿。

参考：[ICLR 2026 Reviewer Guide](https://iclr.cc/Conferences/2026/ReviewerGuide)。官方指南要求参与讨论，并允许依据新信息调整推荐。这里的刻板印象与投入顺序是经验性整理；具体讨论方式以目标会议当轮规定为准。

<a id="reviewer-profile-template-1"></a>
### 审稿人画像、偏好与投入表

```markdown
审稿人 [ID]：
- 当前评分与 Confidence：【原始值、含义；缺失则写未知】
- 最欣赏的点：【Strengths / Summary 原话与位置】
- 阅读深度与理解偏差：【对应原话；是否读附录、哪里可能误解】
- 核心关切：【Q 编号、Weaknesses 原话；要求最高的问题】
- 偏好：【情绪价值 / 实验量 / 背景解释 / 技术细节；逐项附依据】
- 期待的回应：【实验、对照、case、引用、定义、讨论或尊重感】
- 模拟严格程度：【中 / 高 / 极高；依据与重点】
- 第二轮参与、改评开放程度、核心负面风险：【分别判断，附原话】
- 投入：【高价值：高；关键：极大；低价值：中；笑面虎：极高】
- 下一步与收手条件：【优先回答哪一问；何时转移精力】

原问题清单：
| Q | 原话与位置 | 真正在意什么 | 期待什么证据或解释 | 模拟审核重点 |
| :--- | :--- | :--- | :--- | :--- |
| Q1.1 | 【】 | 【】 | 【】 | 【】 |

每一项能回查 review 或真实讨论。画像交给 Rebuttal 起草与 Revise loop 复用；新的讨论改变判断时再更新。
```

作者内部使用。最关键的问题与最高回复要求必须明确；画像不是对审稿人身份或最终评分的确定判断。

<a id="prepare"></a>
## 2. 整理问题与证据

先读完整 review，再写回答。不要只盯着 Questions：具体关切也可能出现在 Weaknesses、建议和评分理由里。

- 【铁律】Weaknesses、Questions、建议和评分理由里的具体关切都要回答；保留原意，一句话有多问就拆开。
- 逐题记录：原问题 → 回应类型 → 现有依据及位置 → 缺口。
- 定义不清给定义，流程不清给案例，效果存疑给对照，实际错误就修正。
- 优先整理已有实验；确实缺证据时，提出能区分争议解释的最小检验，交作者决定。
- 【铁律】向工具提供材料前，确认当轮保密与 AI 规则允许；不上传密钥、个人数据或无权使用的材料。

<a id="prepare-template-1"></a>
### 问题清单

```markdown
| ID | 原问题 | 需要回答什么 | 已有证据与位置 | 缺口 |
| :--- | :--- | :--- | :--- | :--- |
| Q1.1 | 【审稿原话】 | 【具体结论】 | 【节、表、记录】 | 【仍缺什么；没有则写无】 |
| Q1.2a | 【子问题：定义】 | 【对象与判定方式】 | 【定义所在位置】 | 【歧义在哪里】 |
| Q1.2b | 【子问题：有效性】 | 【必要对照】 | 【已有比较】 | 【不能由现有结果回答的部分】 |
```

这张表供作者整理问题；正式回复按下一节的 Q&A 交付。

<a id="response-format"></a>
## 3. 逐题回复格式

一题一个答案：结论 → 证据 → 解释 → 位置。首句把问题答了，后面才有必要读。

- 【铁律】默认交付：每位审稿人单独一个 Markdown 代码块；提交时按平台要求粘贴正文。
- 【铁律】问题标题固定为 > **Q1.1: [问题标题]**：引用、加粗、编号、冒号都保留。
- 【铁律】一个大问题有多问，拆成 Q1.1a、Q1.1b，标题忠于原意。
- 【铁律】第一句直接回答：是否题先给结论，证据不足就说明不能判断；原因题给原因，流程题给操作，数值题给具体值。
- 【铁律】回答之后给必要设置、证据、解释与表号、节号或行号；不先感谢，不先讲背景。
- 【铁律】可比较数据用表格，写全条件、单位、指标方向和统计口径；表后解释结论，不逐格复述。
- 【铁律】一个小点一段；问题之间空一行。感谢具体、克制，放在相关解释后或文末，第一句仍先回答问题。
- 【铁律】修改给真实位置；只有实际改过稿件，才能写成已修改。
- 【铁律】同一实验跨 Q 引用，首次定义简短名称，后续统一使用；每个 Q 仍要独立读懂。

<a id="response-format-template-1"></a>
### 一位审稿人的完整回复

```markdown
> **Q1.1: How does [method] differ from [closest prior work]?**

The main difference is [specific mechanism or evaluation target]. [Prior work] uses [input or operation] to produce [output], whereas [our method] uses [corresponding input or operation] to produce [corresponding output]. This difference addresses [precise limitation] under [stated scope]. The description and comparison are in Section [X] and Table [Y].

> **Q1.2: Does [component] improve [metric]?**

Under [tested setting], [component] [improves / does not improve] [metric] relative to [control] by [absolute difference and unit]. We hold [necessary conditions] fixed and change only [tested component].

| Configuration | [Metric and direction] | [Sample size or number of runs] |
| :--- | :---: | :---: |
| [Control] | [Verified value] | [Verified count] |
| [With component] | [Verified value] | [Verified count] |

The observed [finding] addresses [the reviewer’s concern] because [explanation of the result], supporting [the corresponding contribution]. The results and protocol are in [table or record] and Section [X].
```

方括号全部换成已核实材料；增删表格列取决于比较需要，不能删掉影响公平性或解释结果的条件。若 Q1.2 同时问定义与效果，拆为 Q1.2a、Q1.2b，分别首句回答。

<a id="response-format-example-1"></a>

### 一段回复怎样读

教学模板：把方括号换成自己的真实证据。

**English 教学改写**

Under [tested setting], [component] improves [metric] relative to [control] by [absolute difference and unit]. We hold [confounding factors] fixed and compare [configurations] on [same test set]. The observed [finding] addresses [the reviewer’s concern] because [explanation of the result], supporting [the corresponding contribution]. The protocol and results are in Section [X] and Table [Y].


**高亮与旁批**

1. **Under [tested setting], [component] improves [metric] relative to [control] by [absolute difference and unit].**：【铁律】先答问题。首句给答案：条件、比较对象、指标与差异都在。仅在相应结果支持时使用。
2. **We hold [confounding factors] fixed and compare [configurations] on [same test set].**：【铁律】交代对照。交代怎样得到答案；对照要对应审稿人的质疑。
3. **The observed [finding] addresses [the reviewer’s concern] because [explanation of the result], supporting [the corresponding contribution].**：分析实验。实验后解释现象，回应审稿人的疑虑，并落到论文的创新点和贡献。
4. **The protocol and results are in Section [X] and Table [Y].**：【铁律】给出位置。给位置，便于核查。

StrongResponse · 原创教学模板

原创教学模板，不是真实审稿回复。

本指南原创内容采用 CC BY 4.0；转载请附作者、原文链接与许可，改写注明改动。

<a id="answer-types"></a>
## 4. 四类回答模板

按问题选证据，不强行把每个问题都变成补实验。澄清用定义和流程，效果用比较，机制用能区分解释的检验。

- 【铁律】解释性答复：先定义具体对象，再给输入、操作、输出；必要时用一条样例走完整个流程。
- 【铁律】实证答复：报告真实绝对值、比较对象、指标方向与必要条件。平均值涉及波动时给相应不确定性。
- 【铁律】合理不同意见：指出争议前提和证据，只讨论论文；确有错误就修正，不评价审稿人的能力或动机。
- 【铁律】承诺不是证据。阶段性结果写实际范围；没有直接证据就说明缺口、缩小主张，不能把计划写成已完成。
- 【铁律】表格保留影响判断的设置差异和负结果；删列是为了省阅读时间，不能为了改变结论。

<a id="answer-types-template-1"></a>
### 4.1 定义与流程

```markdown
> **Q1.2a: What does [term] mean, and how is it used?**

[Term] denotes [concrete object and decision rule]. For input [x], [module] performs [operation] and returns [y] to [next module]. This interface is specified in Section [X]; [example or algorithm] shows [the disputed step].
```

术语先落到对象；举例要解释被问到的环节，不重讲整篇方法。

<a id="answer-types-template-2"></a>
### 4.2 实验与对照

```markdown
> **Q1.2b: Could [alternative explanation] account for [result]?**

Under [matched setting], the result [persists / does not persist] when [confounding factor] is controlled. We compare [A] and [B] with identical [necessary conditions]; [metric] is [verified A] versus [verified B] ([direction]; Table [R]). This comparison [supports / does not support] [bounded conclusion]. [Remaining uncertainty] is not resolved by this test.
```

对照必须能检验替代解释；同一批数据换个表头，不等于排除了混淆。

<a id="answer-types-template-3"></a>
### 4.3 有依据的不同意见

```markdown
> **Q2.1: Does [specific concern] invalidate [claim]?**

[Specific concern] does not invalidate [bounded claim] under [stated setting], because [verified fact]. The concern assumes [premise], whereas [paper location or verified record] specifies [relevant fact]. This supports [limited conclusion]. We agree that [valid part of the concern], and [verified clarification or correction, if applicable] is documented in [location].
```

只有证据支持时才使用“不推翻主张”的首句；依据不够就说明不能判断。不同意见也要承认成立的部分。

<a id="answer-types-template-4"></a>
### 4.4 目前不能回答

```markdown
> **Q2.2: Does [claim] hold under [untested condition]?**

We do not have direct evidence for [claim] under [untested condition]. The available result in [location] covers [tested scope] only. We therefore limit our conclusion to [supported claim]. Establishing [broader claim] would require [specific comparison or measurement].
```

没有依据就把边界写清楚；只有稿件确已修订时，才能追加具体修改与位置。

<a id="revise-loop"></a>
## 5. Revise loop

Revise loop：用第一部分的画像模拟这位审稿人审核回复，给出意见；根据意见改 Rebuttal，再用同一画像复核。

- 【铁律】先读取第一部分的审稿人画像与全部原问题，再模拟审稿人；不要先读作者回复、再临时编一个宽松人设。
- 按画像设置严格程度，拟合核心关切和审稿偏好。最关心、要求最高的问题要最严格；看重实验就查实验，看重情绪价值就查是否被理解，需要背景解释就检查术语与中间逻辑。
- 【铁律】模拟复核以 review 原问题顺序为准。逐题指出回复位置、是否真正回答、证据是否合适，以及这位审稿人仍可能追问什么。
- 反馈必须具体：原问题、画像关注点、回复位置、通过或不通过、原因、最小改法和缺失证据。不要只说“更有说服力一点”。
- 【铁律】Rebuttal skill 依据反馈修改获授权的回复，再让画像与模拟 skill 用同一张清单复核；新 review 信息出现时才更新画像。
- 每问覆盖完整，关键关切有对应证据，解释深度、语气和长度符合画像要求后停止。补实验由作者决定；模拟通过不能写成真实审稿人已认可。

### 1. 带着画像进入审稿人角色

读取评分、Confidence、原话依据、核心关切、期待的证据与偏好。按这些信息设定难度，带着疑问读回复。

### 2. 模拟审核，给出具体意见

逐题检查答案、证据、实验分析、解释深度和尊重感。要求最高的问题细读；按其阅读习惯再扫一遍首句、表格和加粗结论。

### 3. 根据意见修改 Rebuttal

只修改不通过项：补回答或证据，分析实验，解释术语，缩短长段落，调整语气。需要新实验或新事实时交作者决定。

### 4. 用同一画像再审核

重新检查原问题与刚才的意见，确认修改确实解决了问题。有新疑问就继续修改，再复核；不要为了通过而降低原画像要求。

<a id="revise-loop-template-1"></a>
### 让 Codex 按画像运行 Revise loop

```markdown
运行 Revise loop。
论文：【】；完整 review：【】；第一部分的审稿人画像与偏好表：【】；当前 Rebuttal：【】；真实证据：【】；当轮规则和允许修改的文件：【】。

1. 读取 rebuttal-reviewer-profile skill，按画像扮演每位审稿人。依据原话设严格程度，重点拟合其核心关切、最高要求的问题、情绪价值、实验量、背景解释及扫读习惯。
2. 按原 review 的问题清单逐题审核回复。输出：Q｜原问题｜画像关注点｜回复位置｜通过/不通过｜原因｜最小改法｜缺失证据。
3. 读取 rebuttal skill，依据反馈只修改不通过项；不编造结果，不自动跑实验或改论文。
4. 用同一画像、原问题清单和反馈重新审核修改后的回复。未通过则再次修改、再次审核。只有新的 review 或讨论改变依据时才更新画像。
5. 所有问题都有明确回应，关键证据与实验分析到位，语气、长度和解释深度符合这位审稿人的要求后停止。

最终交付：每位审稿人的可复制 Rebuttal、作者内部的复核记录，以及需要作者决定的证据缺口。模拟意见和通过结果不粘入正式回复。
```

画像与模拟 skill 负责审核，Rebuttal skill 负责修改；同一画像贯穿循环。模拟反馈是作者内部检查，不是真实审稿意见。

<a id="follow-up"></a>
## 6. 追问与 AC letter

追问用 Rebuttal skill 只补新增信息。完成回复后，再用独立的 AC letter skill 总结审稿人的评价、改分与核心回应。

- 【铁律】保留原 Q 编号和问题关系；新子问可续为 Q1.2c，编号仍以平台要求为准。
- 【铁律】先回答追问，再定位新增证据；已经讲清的背景用位置引用。

<a id="follow-up-template-1"></a>
### 6.1 追问回复模板

```markdown
> **Q1.2c: [Faithful title of the follow-up question]**

[Direct answer to the new question, with the necessary scope].

**New evidence**: Compared with Q1.2, we now provide [verified result or clarification]. Under [necessary setting], [comparison or reasoning] shows [specific finding] ([table / section / lines]). This supports [bounded conclusion] because [link between the evidence and the question].

**Revision**: Section [X], lines [Y–Z], now states: “[Exact wording of the completed revision].”

**Remaining issue**: The evidence covers [tested scope]; it does not establish [unresolved claim]. [Specific evidence still needed, if any].
```

保留原 Q 编号，追问新子项续编。填真实证据与位置；无新结果就给已有依据和明确边界。未改稿删 Revision，没有剩余疑问删 Remaining issue；可比较数据改用紧凑表格。

<a id="ac-letter"></a>
### AC letter 怎么写

AC letter 最后写。先让 AC 看到审稿人的正面评价、评分和真实改分，再用简短段落说明关键关切如何得到回应。

- 先感谢审稿人的时间与意见，随后引用审稿人的正面评价原话，并带上 Overall 分数与 Confidence（若平台提供）。先报分，再讲关切。
- 有真实涨分、认可或问题解决的二轮回复，优先陈述改分前后与认可原话；没有就删去该项。没有回复只陈述客观状态，不能把沉默写成认可，也不能预期问题已经解决。
- 每位审稿人单独一段，通常 3–4 句：正面评价与评分 → 主要关切 → 我们做了什么 → 有证据的结论。每段加粗一两个关键结论，供 AC 扫读。
- AC 想知道关切是否被认真回应。概括最关键的数据、对照或修改，并给简短位置；不展开实验流程、方法细节、公式或整份逐题回复。
- 重点呈现论文的贡献、审稿人的认可和已经完成的回应。引用必须忠于原意；不把作者的解释写成审稿人的认可，不制造共识。确有剩余分歧时如实交代必要信息，不编造“全部解决”。
- 不要贬低或指挥审稿人和 AC。若有必要说明评审之间的分数差异，只用真实记录与可核对事实，让 AC 判断；不能仅凭 Confidence 或未回复就推断审稿人失职。
- 全文不超过 500 个英文单词；会议上限更低时遵守会议上限。不用破折号连接句子。
- 适用时补一句真实的代码开放或可复现状态；尚未完成的只能写真实承诺，不能冒充已发布。结尾使用：We hope these clarifications support a fair and informed assessment.

<a id="follow-up-template-2"></a>
### 6.2 AC letter 模板

```markdown
We thank all reviewers for their time and feedback. Reviewer [ID] (Overall [score], Confidence [confidence]) described [specific contribution] as “[exact positive quotation from the review].” [Optional genuine update: Following our rebuttal, Reviewer [ID] updated the Overall score from [old score] to [new score] and wrote, “[exact acknowledgement from the discussion].”]

**Reviewer [ID] (Overall [current score], Confidence [confidence]).** The reviewer recognized [specific strength] as “[exact positive quotation].” The main concern was [one faithful sentence summarizing the concern]. We addressed it with [completed response or evidence, summarized briefly] ([Q number / table / section]). **[Concise conclusion supported by that evidence, with a verified key result if useful].**

**Reviewer [ID] (Overall [current score], Confidence [confidence]).** The reviewer appreciated “[exact positive quotation].” The main concern was [one faithful sentence summarizing the concern]. Our response provided [completed clarification, comparison or revision] ([Q number / table / section]). **[Concise conclusion supported by the response].**

[Optional factual release statement: The [code / data / model weights] are available at [permitted location].]

We hope these clarifications support a fair and informed assessment.
```

按审稿人数增删段落；没有正面原话、改分或公开材料就删去相应句子。所有 ID、分数、引文、数据和位置填真实记录。英文骨架仅供参考；删除占位符后检查词数。

---

Da1yuqin / [StrongResponse](https://da1yuqin.github.io/StarPaper/StrongResponse/)，[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)。转载请保留署名、出处及许可，改写注明改动。
