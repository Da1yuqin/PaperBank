# 实验、评价与诊断：按需参考

以下为通用规则与教学模板，不是真实论文原文、研究事实或实测。

#### Experiments：先列要验证的问题

先列 Introduction 的主张与检验标准，再安排主结果、消融及补充分析。

教学模板；【】填真实材料。

- RQ 可用于组织，不必每表一个编号；标题写 Main Results、Ablation Studies 或具体目的。
- 按论文贡献选实验，不照搬另一类研究的实验清单。

通用要求；推荐结构模板

After constructing [method or benchmark], we evaluate [actual target] on [scope].

构建[方法或基准]后，我们在[范围]内评价[实际对象]。

**第 1 句：**承接前章产物，先给比较范围。

We first test whether [design] improves [goal] under [fixed conditions].

我们先检验，在[固定条件]下，[设计]能否改善[目标]。

**第 2 句：**主结果使用能检验 Introduction 主张的指标，不根据有利结果临时更换指标。

We then isolate [component] and examine [robustness, efficiency, or transfer question].

随后，我们单独检验[组件]，并检查[稳健性、效率或迁移问题]。

**第 3 句：**只预告实际存在的分析，不能为了补齐模板虚构实验。

#### Experimental Setup：比较设置

集中定义指标、方向、分母、简称与实验设置，新增指标说明用途与贡献。

教学模板；【】填真实材料。

- Metrics：定义、方向、分母、汇总方式和无效输出处理。指标多时编号，名称与简称便于查找；新指标单独起段。
- Baselines：按路线分类，给引用和可影响结果的共享条件。简介讲它做什么，结果差异留给分析。
- Implementation Details：Method 出现的参数给实际值与选择依据；完整参数表可放附录。训练、推理、硬件、重复次数和成本口径说全。
- 人工或模型 judge：谁判什么、按什么判、核验多少。设置是为了让人判断比较是否成立，不是报设备清单。

通用要求；Metrics/Baselines 为推荐组织

We evaluate [unit] from [dataset version], using [split or selection rule].

我们从[数据版本]中按[划分或选择规则]评价[样本单位]。

**第 1 句：**先定义比较对象与分母，不根据结果更换统计范围。

Metrics. We measure [property] using [metric definition]; [direction] is better.

指标。我们用[指标定义]测量[性质]；[方向]表示更好。

**第 2 句：**不是只列缩写；定义、单位和方向决定读法。

We compute [per-unit statistic] and aggregate by [rule]. [Invalid-output policy].

先计算[单位统计量]，再按[规则]汇总；[无效输出处理规则]。

**第 3 句：**宏平均、微平均与条件子集不能混用。

Baselines. We compare [method] with [routes and citations] using [shared conditions].

基线。我们在[共享条件]下，将[方法]与[基线路线及引用]比较。

**第 4 句：**把可影响结果的条件说明白，不只报模型名字。

Implementation Details. We select [parameters] on [development data] and fix them before [final evaluation].

实现细节。我们在[开发数据]上选择[参数]，并在[最终评价]前固定这些选择。

**第 5 句：**明确选择边界；具体值与来源按真实记录填。

#### Main Results：先写发现

解释主要差异、可能原因及对应设计，不逐行重复表格数值。

教学模板；【】填真实材料。

- 把有依据的结论写在段首或小标题。一段优先围着一个实验、一个图表、一个结论讲，不混三件事。
- 先说明关键关系，再给决定判断的数字与范围；全面胜出、显著、稳定需要对应证据。
- 观察之后解释原因，消融才能帮助归因；有利、不利指标与代价都照实解释。

通用要求；加粗发现为 PaperBank 偏好

[Design] improves [specific ability] under [tested condition].

在[实测条件]下，[设计]改善了[具体能力]。

**第 1 句：**作为加粗结论；无提升就写真实差异或未支持的主张。

Table [ref] shows [qualitative contrast] relative to [comparison].

表[真实编号]显示，相比[对照]，[关键关系]。

**第 2 句：**只讲决定结论的对照，不逐行复述数字。

This contrast supports [Intro contribution], while [observed trade-off] limits [scope].

这一对照支持[引言贡献]，但[已观察代价]限制了[适用范围]。

**第 3 句：**解释结果意味着什么，同时保留真实取舍。

#### Ablation：改一项，查一个作用

消融每次去掉或替换一个因素，固定其他条件，检验对应设计的作用。

教学模板；【】填真实材料。

- 同时改多项时补匹配对照，或只评价整套改动。
- 写清目的、改动和发现，不只贴 w/o A、w/o B。

通用要求；按机制归因需求选用

To examine [component purpose], we replace [component] with [control].

为检验[组件作用]，我们用[对照]替换[组件]。

**第 1 句：**消融对准方法声称的作用。

We keep [other settings] fixed.

其余[设置]保持不变。

**第 2 句：**告诉读者哪些替代解释受到控制。

Figure [ref] shows [observed change], supporting [limited component role] in [tested setting].

图[真实编号]显示[观察变化]，支持该组件在[实测设置]中具有[有限作用]。

**第 3 句：**作用不超过实际控制的因素与范围。

#### 扩展实验：稳定性、效率、迁移

按主张选择稳健性、效率或迁移分析。保留失败记录，报告有助于判断贡献的负结果。

教学模板；【】填真实材料。

- 效率比较给端到端成本、资源和质量取舍；计入生成与审核。
- 每组先说为什么测、改什么、固定什么，再说发现和范围。
- 哪些条件有效、哪条路走不通，都是有信息的结果；不能只挑最好一次，或把失败全藏起来。

按贡献选择必要分析

To test [stability or transfer claim], we vary [factor] while holding [controls] fixed.

为检验[稳定或迁移主张]，我们改变[因素]，保持[控制项]不变。

**第 1 句：**问题与实际变化必须匹配。

We report [variation or outcome] across [repeat unit or new setting].

我们报告跨[重复单位或新设置]的[变化或结果]。

**第 2 句：**说清独立运行、样本和重复层级，不靠最好一次说明稳定。

These comparisons support [scope-limited finding], but do not establish [broader claim].

这些比较支持[有限范围的发现]，尚不能说明[更广主张]成立。

**第 3 句：**范围边界具体写；不是在每段末尾机械加免责声明。

#### Case Study：走一遍流程

用明确来源的输入与输出展示流程及判断依据，案例不能替代总体统计。

教学模板；【】填真实材料。

- 保留原始文本、实测回复和标签；自构例子标清。案例不能代替总体结果。
- 位置按叙述需要安排；帮助理解评价时，也可放在总体结果之前。

通用要求；教学案例须明示

In [a recorded case or a stated constructed example], [input] requires [specific behavior].

在[有来源的真实案例或明示构造案例]中，[输入]要求[具体行为]。

**第 1 句：**先给来源类型与任务，明确区分教学示例与实测案例。

[Stage] uses [evidence] to produce [intermediate output].

[阶段]利用[证据]生成[中间产物]。

**第 2 句：**把可见处理与 framework 对上。

The final output [meets or violates requirement] because [observable evidence].

最终输出[满足或违反要求]，依据是[可见证据]。

**第 3 句：**判定与证据直接连接，不只写一个勾叉。

---

Da1yuqin / [PaperBank](https://da1yuqin.github.io/PaperBank/)，[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)。转载保留署名、出处与许可，改编注明改动。
