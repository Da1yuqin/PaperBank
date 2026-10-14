# 图表、Caption 与排版：按需参考

以下为通用规则与教学模板，不是真实论文原文、研究事实或实测。

- **每图明确一个主要任务：**mainfig 展示动机与观察。framework 解释设计如何解决问题。结果图验证主张。

Show where the existing pipeline fails and which step our method changes.

画清旧流程在哪一步出问题，我们改了哪一步。

- **绘图先于正文精修：**先画框架图与实验图，供合作者审核，再精修正文。图未体现贡献时，先改内容和布局，再改颜色。

Panel (a) shows the observed gap; panel (b) tests the proposed repair.

(a) 展示实际缺口；(b) 检验我们的修补。

- **【铁律】统计图使用真实数据：**统计图用 Python 从真实数据绘制。imagegen 用于动机、框架和案例示意。缺数据就停，不补点、不编误差、不为平滑改曲线。

Draw the recorded success rates with Python. Generate only the workflow illustration with imagegen.

成功率用 Python 按记录画；imagegen 只生成流程示意。

- **【铁律】按最终尺寸检查字号：**按最终栏宽排字，字体与正文一致。图内统一字号，范围为正文减 2 pt 至正文。标题也不放大；放不下就重排。

Use the paper’s column width and body font; remove repeated labels rather than shrinking text.

用论文栏宽和正文字体；删重复标签，不缩小规定字号。

- **【铁律】箭头表示真实依赖：**同层内容成组并命名。先后、并行、汇合与反馈按真实依赖绘制。箭头注明传递内容，起止清楚，不穿文字、不绕远路。

Retrieved passages enter the generator; the evaluator receives the generated answer.

检索段落送给生成器；生成的回答交给评价器。

- **【铁律】区分输入与评价信息：**输入、输出和评价规则用三种边框区分，并给图例。评价专用的 rubric 不连到被测模型。模型收到的材料不同，也须标明。

Dashed boxes contain model inputs; solid boxes contain responses; dotted boxes contain evaluator-only criteria.

虚线框是模型输入，实线框是回复，点线框是只供评价的判据。

- **【铁律】低饱和配色与清晰对比：**常规模块用中性灰，关键改动用统一强调色。配色低饱和，对比清楚。

Blue circles denote the baseline; orange triangles denote our method in every panel.

每个面板都用蓝圆点表示基线，橙三角表示我们的方法。

- **【铁律】对话按轮次与语义分段：**对话一轮一框，并注明角色。长回复按语义分段，不拆成虚假的多轮。只高亮关键约束、证据或错误，并解释颜色。

The left column contains evidence; the right column shows the model response and its evaluation.

左栏放证据；右栏放模型回复和评价。

- **【铁律】同一案例仅完整呈现一次：**同一案例全文只完整展示一次，其他位置交叉引用。改名、翻译或裁剪仍算同一案例。必要对照集中展示，单个案例不证明总体效果。

Figure 1 presents the case; Section 4 refers back to Figure 1 without repeating the dialogue.

案例放图 1；第 4 节回引图 1，不再抄一遍对话。

- **【铁律】同类子图使用一致尺度：**围绕同一问题排列现象、诊断、对照和稳健性。条件顺序与配色统一，同类轴和色标保持可比。

The first panel identifies the gap, the second locates it, and the third tests whether it persists.

第一图找差距，第二图找发生位置，第三图检验差距是否仍在。

- **【铁律】准确呈现坐标与差异：**核对单位、分母、方向、坐标起点和误差类型。截断坐标须标明；相对增益同时给绝对值。柱长必须对应数值。

Accuracy rises from 60% to 66%: 6 percentage points, or a 10% relative increase.

准确率从 60% 到 66%，增加 6 个百分点。相对增益为 10%。

- **【铁律】Caption 按图的读序讲解：**图注先说明图表对象，再按读图顺序讲解。简称在本图 Caption 或脚注解释。案例条件对应难点标签，颜色说明连接对象。保留必要单位、分母与边界，单项判定移到脚注。“显著”须有统计检验。

Error bars show 95% question-level bootstrap intervals; the horizontal line marks zero gain.

误差条表示按题目重采样的 95% 区间；水平线表示零增益。

- **【铁律】编译后检查最终页面：**放回论文检查字号、字体嵌入与可选文字。再查裁切、碰撞、图注总高度和首次引用顺序。源码字号正确，不代表插入后正确。图表移到附录时，同步详解、Overview 与引用。正文保留主要结论。

Place the figure after its first mention and check all labels at normal reading size.

按首次引用顺序排图，以正常阅读大小检查全部文字。

- **【铁律】明确模块输入与输出：**模块写清输入、操作、产物及接收者。名称与 Method 一致，缩写就近解释。

The checker receives evidence and returns supported constraints to the planner.

核查器接收证据，把已支持的约束交给规划器。

- **【铁律】解释图中所有标记：**图标旁写对象名，缩写、符号、边框和线型就近解释。图与图注应讲清每个标记和数字。

Label the robot as the planner and define dashed edges as feedback.

机器人标为规划器，虚线箭头定义为反馈。

- **【铁律】Framework 展示操作与产物：**用一个真实输入串起中间产物与输出。旁边指出各项设计解决的困难。

Trace one task from the evidence input through checking to the final plan.

用同一个任务走完证据输入、核查和最终计划。

- **【铁律】区分示意与实测：**区分估计、作者示例和实测输出。可选路径不能画成必经步骤。面积、线宽和箭头不能暗示无依据的比例或因果。图形须准确，不能靠图注补救。评分通过不等于执行、成交或部署成功。显示改名时，保留冻结 prompt、机器字段和统计。改写不能冒称执行原文。

Keep illustrative module boxes equally sized; plot measured latency on a labeled axis.

示意模块框不靠大小表示耗时；实测延迟另用带坐标的图展示。

- **【铁律】准确区分矢量与位图：**统计图导出矢量 PDF，并嵌入字体。底图标签另排原生、可见、可选的 PDF 文字。不叠字形，不加隐藏 OCR 层。混合 PDF 仍含位图。

Export the plot as vector PDF and verify that its axis labels can be selected.

统计图导出矢量 PDF，再实际选中坐标轴文字检查。

- **【铁律】保持修改范围：**只改配色时，保留布局、文字、换行、字号和公式。照片与连线也不变；重排须在约定范围内。保留数据、实验和合作者的图。

Change panel fills while retaining every label, coordinate, and arrow endpoint.

只换面板底色，保留所有标签、坐标和箭头端点。

- **【铁律】按模板宽度布局：**按实际栏宽起稿，不改页边距、正文字号或页面方向。通栏可从 16:9 起稿，单栏可从 4:3 起稿。附录可纵排，图不能非等比缩放。CS 默认用 [!t]，按首次引用检查实际落点。

Rearrange parallel branches within the column width; keep the paper template unchanged.

在栏宽内重排并行分支，保留论文模板。

- **【铁律】表格用于结果与数据：**本教程默认表格只放真实结果或数据。术语、方法、实验计划和案例点评写正文。不能把说明表截图规避，也不能靠添数字冒充结果。

Put success rates in a table and explain the checking procedure in the text.

成功率放表格，核查流程写正文。

- **【铁律】重排文字与图形重叠处：**图例、标题、刻度和注释不能遮挡数据与连线。重排并留出文字空间，不用遮盖掩饰重叠。

Move the legend outside the plotted curves while preserving the data and axes.

把图例移出曲线区，保留数据和坐标轴。

## 统计图补充

- **小样本：均值之外看原始观测：**小样本连续值优先展示原始点与样本量。可叠均值或区间；观测较多时可用箱线图或分布图。均值相同不代表分布相同。计数、比例等汇总量仍可用柱图。

Both groups average 6, but one is dispersed and the other is tightly clustered.

两组均值均为 6，原始点显示一组分散、一组集中。

- **散点遮挡：必要时改看二维计数：**重叠点可能隐藏数量和少数类别。先调透明度，检查密集区与稀疏区能否分清。大量重叠时用二维或六边形分箱。注明每格计数、范围与箱宽。保留真实坐标，不为分开点而移动数值。未定义时，颜色深浅不表示概率。

The scatter view hides repeated coordinates; each cell in the count view reports how many observations it contains.

相同坐标的散点会遮挡，二维计数图显示各区观测数。

- **连续色标：让明暗顺序对应数值：**类别用离散色板，连续量用明暗有序的色标。偏离有意义的基准时，用发散色标。连续量不默认用 rainbow／jet。其明暗不均可能掩盖差异或制造边界。保留已有颜色含义，并检查灰度下的数值顺序。

Equal steps in a continuous score should not acquire arbitrary bright boundaries from the palette.

等距分数不应因颜色骤变而出现虚假的数据边界。

- **【铁律】气泡面积与数量成正比：**气泡表示非负数量时，面积须与数量成正比。半径取数量的平方根，并给大小图例与单位。数量增至 4 倍，面积增至 4 倍、半径增至 2 倍。关系来自 A = πr²；其他颜色与位置编码另解释。

For counts 1, 4 and 9, proportional areas require radii in the ratio 1:2:3.

数量为 1、4、9 时，面积比为 1∶4∶9，对应半径比为 1∶2∶3。

- **误差线重叠：先认类型与比较设计：**不能只凭误差线是否重叠判断显著性。先看 SD、SE 或 CI 类型、样本量及独立／配对设计。用对应检验，或直接估计差值与区间。保留误差类型、重复单位和区间定义，不凭图补 p 值。

A paired comparison depends on within-pair differences; the two marginal error bars alone do not encode that pairing.

配对比较使用同一对象的差值。两组均值各自的误差线不体现配对关系。

## 相关参考和推荐阅读

- [Weissgerber 等（2015）· 小样本连续数据为何需要展示原始观测](https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.1002128)：原始点揭示均值与误差条隐藏的分布、离群点及配对。适用于小样本连续数据，不设统一样本阈值。不禁止所有柱图。
- [Wilke（2019）· 散点重叠的处理](https://clauswilke.com/dataviz/overlapping-points.html)：先调点大小与透明度。密集散点可用二维分箱或 hexbin，解释计数或密度。保留真实坐标，不用 jitter；分箱不保留逐点位置。
- [Wilke（2019）· 颜色使用的常见误区](https://clauswilke.com/dataviz/color-pitfalls.html)：连续量用明暗有序的色标，避免 rainbow/jet 误导。类别用离散色，偏离基准时用发散色。不指定唯一色板。
- [Rougier 等（2014）· 科研绘图的十条建议](https://doi.org/10.1371/journal.pcbi.1003833)：按读者与主要信息选图，核对布局、颜色和说明。气泡表示非负数量时，面积须成比例，不能直接缩放半径。示意形状不套用定量比例。
- [Cumming 等（2007）· 误差条与组间差异的解读](https://pmc.ncbi.nlm.nih.gov/articles/PMC2064100/)：区间比较取决于误差类型、独立样本数及独立／配对设计。特定条件的重叠近似规则不能推广为通用判据。配对比较使用差值及其不确定性。

---

Da1yuqin / [StarPaper](https://da1yuqin.github.io/StarPaper/)，[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)。转载保留署名、出处与许可，改编注明改动。
