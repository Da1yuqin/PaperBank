# 图表、Caption 与排版：按需参考

以下为通用规则与教学模板，不是真实论文原文、研究事实或实测。

- **每图明确一个主要任务：**mainfig 展示研究动机与观察，framework 说明设计如何对应问题，结果图提供验证证据。每图明确一个主要任务。

Show where the existing pipeline fails and which step our method changes.

画清旧流程在哪一步出问题，我们改了哪一步。

- **绘图先于正文精修：**先完成可供合作者审核的框架图与实验图，再精修正文。图未能体现贡献时，先调整内容与布局，再修改配色。

Panel (a) shows the observed gap; panel (b) tests the proposed repair.

(a) 展示实际缺口；(b) 检验我们的修补。

- **【铁律】统计图使用真实数据：**统计图用 Python 从真实数据绘制；imagegen 用于动机、框架和案例图。缺数据就停，不补点、不编误差、不为平滑改曲线。

Draw the recorded success rates with Python. Generate only the workflow illustration with imagegen.

成功率用 Python 按记录画；imagegen 只生成流程示意。

- **【铁律】按最终尺寸检查字号：**按最终栏宽排字，字体与正文一致；所有图内字同一字号，介于正文与正文减 2 pt 之间，标题也不能更大。放不下先重排，不缩小规定字号。

Use the paper’s column width and body font; remove repeated labels rather than shrinking text.

用论文栏宽和正文字体；删重复标签，不缩小规定字号。

- **【铁律】箭头表示真实依赖：**同层成组并命名；先后、并行、汇合、反馈按真实依赖画。每条箭头说清传什么，起止明确，避免穿过文字与无必要的迂回。

Retrieved passages enter the generator; the evaluator receives the generated answer.

检索段落送给生成器；生成的回答交给评价器。

- **【铁律】区分输入与评价信息：**输入、输出、评价规则用三种边框区分，并给图例。只供评价的 rubric 不连到被测模型；不同模型收到不同材料，也要标清。

Dashed boxes contain model inputs; solid boxes contain responses; dotted boxes contain evaluator-only criteria.

虚线框是模型输入，实线框是回复，点线框是只供评价的判据。

- **【铁律】低饱和配色与清晰对比：**常规模块用中性灰，关键改动用统一强调色。低饱和配色须保持清晰对比。

Blue circles denote the baseline; orange triangles denote our method in every panel.

每个面板都用蓝圆点表示基线，橙三角表示我们的方法。

- **【铁律】对话按轮次与语义分段：**一轮一框，注明角色；同一轮长回复按语义分段，不伪装成多轮。高亮只标关键约束、证据或错误，颜色含义要能读懂。

The left column contains evidence; the right column shows the model response and its evaluation.

左栏放证据；右栏放模型回复和评价。

- **【铁律】同一案例仅完整呈现一次：**同一来源的案例在全文只完整呈现一次，其他位置交叉引用。改名、翻译、裁剪也算同一个；必要对照集中展示，单个案例不能证明总体效果。

Figure 1 presents the case; Section 4 refers back to Figure 1 without repeating the dialogue.

案例放图 1；第 4 节回引图 1，不再抄一遍对话。

- **【铁律】同类子图使用一致尺度：**围绕一个问题排现象、诊断、对照和稳健性；同条件同顺序、同配色，同类轴和色标保持可比。

The first panel identifies the gap, the second locates it, and the third tests whether it persists.

第一图找差距，第二图找发生位置，第三图检验差距是否仍在。

- **【铁律】准确呈现坐标与差异：**查单位、分母、方向、坐标起点和误差类型；截断坐标要明确标出。相对增益同时给绝对值，柱长和数值必须对应。

Accuracy rises from 60% to 66%: 6 percentage points, or a 10% relative increase.

准确率从 60% 到 66%：增加 6 个百分点，相对提高 10%。

- **【铁律】Caption 按图的读序讲解：**先定位图表对象，在本图 Caption 或对应脚注解释实际简称，再按读序带读。案例条件对应难点标签，颜色点明连接对象；保留必要单位、分母与边界，不堆单项判定。“显著”须有统计检验。

Error bars show 95% question-level bootstrap intervals; the horizontal line marks zero gain.

误差条表示按题目重采样的 95% 区间；水平线表示零增益。

- **【铁律】编译后检查最终页面：**放回论文检查实际字号、字体嵌入、可选文字、裁切、碰撞、图注总高度和首次引用顺序。源码字号正确，不代表插入后仍正确。图表移到附录时，同步详解、Overview 与引用，正文保留主要结论。

Place the figure after its first mention and check all labels at normal reading size.

按首次引用顺序排图，以正常阅读大小检查全部文字。

- **【铁律】明确模块输入与输出：**每个关键模块写清收到什么、做什么、交出什么，以及交给谁。模块名与 Method 一致，所有缩写就近解释。

The checker receives evidence and returns supported constraints to the planner.

核查器接收证据，把已支持的约束交给规划器。

- **【铁律】解释图中所有标记：**图标旁写对象名；新缩写、符号、边框、线型和数字就近解释。读者只看图与图注，应知道每个标记指什么。

Label the robot as the planner and define dashed edges as feedback.

机器人标为规划器，虚线箭头定义为反馈。

- **【铁律】Framework 展示操作与产物：**“结合 case 去绘制你的流程” 展示一个真实输入怎样变成中间产物和输出，旁边点出设计解决的困难。节点多不等于贡献多。

Trace one task from the evidence input through checking to the final plan.

用同一个任务走完证据输入、核查和最终计划。

- **【铁律】区分示意与实测：**估计、作者示例和实测输出分清；可选路径不能画成必经步骤。框的面积、线宽和箭头不能暗示没有证据的比例或因果，图形本身须准确，不能仅靠图注纠正。评分通过不等于真实执行、成交或部署成功；显示改名不改冻结 prompt、机器字段和统计，不冒称执行原文。

Keep illustrative module boxes equally sized; plot measured latency on a labeled axis.

示意模块框不靠大小表示耗时；实测延迟另用带坐标的图展示。

- **【铁律】准确区分矢量与位图：**统计图导出矢量 PDF 并嵌入字体。生成底图上的标签另排原生、可见、可选的 PDF 文字；不留重叠字形，不加隐藏 OCR 层。混合 PDF 仍含位图。

Export the plot as vector PDF and verify that its axis labels can be selected.

统计图导出矢量 PDF，再实际选中坐标轴文字检查。

- **【铁律】保持修改范围：**只改配色就保留布局、文字、换行、字号、公式、照片和连线；重排须在约定范围内。保留数据、实验和合作者的图。

Change panel fills while retaining every label, coordinate, and arrow endpoint.

只换面板底色，保留所有标签、坐标和箭头端点。

- **【铁律】按模板宽度布局：**按实际栏宽起稿，不改页边距、正文字号或页面方向。正文通栏约 16:9、单栏约 4:3 是起点，附录可纵排；不进行非等比缩放。CS 默认用 [!t]，再按正文首次引用检查实际落点。

Rearrange parallel branches within the column width; keep the paper template unchanged.

在栏宽内重排并行分支，保留论文模板。

- **【铁律】表格用于结果与数据：**StarPaper 默认表格只放真实结果或数据。术语、方法、实验计划和案例点评写正文，不能通过截图规避该规则；统计数字也不能把说明表变成实验结果。

Put success rates in a table and explain the checking procedure in the text.

成功率放表格，核查流程写正文。

- **【铁律】重排文字与图形重叠处：**图例、标题、刻度和注释不能挡数据、箭头或边框。为文字保留空间，通过重排解决重叠，不能用遮盖隐藏问题。

Move the legend outside the plotted curves while preserving the data and axes.

把图例移出曲线区，保留数据和坐标轴。

## 统计图补充

- **小样本：均值之外看原始观测：**比较小样本的连续测量时，优先展示原始观测点与样本量，可叠加均值或区间；较多观测可用箱线图或已有分布图。均值相同不代表分布相同。计数、比例等汇总量仍可用柱图，不把这条写成禁止所有柱图。

Both groups average 6, but one is dispersed and the other is tightly clustered.

两组均值都为 6，一组分散，另一组集中；原始点让差别可见。

- **散点遮挡：必要时改看二维计数：**重叠的点可能隐藏观测数量和少数类别。先检查透明度是否仍能呈现密集区与稀疏区；大量重叠时可用二维分箱或六边形分箱，说明每格计数、范围与箱宽。保留原始坐标，不为分开点而移动测量值；颜色深浅不是未经定义的概率。

The scatter view hides repeated coordinates; each cell in the count view reports how many observations it contains.

散点图中相同坐标被盖住；二维计数图显示每个区域实际包含多少观测。

- **连续色标：让明暗顺序对应数值：**无序类别用离散色板，连续大小用明暗顺序清楚的顺序色标；偏离有意义的参照值时用发散色标。连续数值不默认用 rainbow／jet：不均匀、非单调的明暗变化可能掩盖差异或制造边界。沿用现有色板的语义，检查灰度下的数值顺序。

Equal steps in a continuous score should not acquire arbitrary bright boundaries from the palette.

分数等距变化，不应因为色板突然变亮而看起来有一道数据边界。

- **【铁律】气泡面积与数量成正比：**用气泡面积表示非负数量时，面积必须与数量成正比，半径随数量平方根变化；给出大小图例与单位。数量变为 4 倍，面积变为 4 倍、半径变为 2 倍。圆面积关系来自 A = πr²；颜色或位置表示的其他变量分别解释。

For counts 1, 4 and 9, proportional areas require radii in the ratio 1:2:3.

数量为 1、4、9 时，面积比为 1∶4∶9，对应半径比为 1∶2∶3。

- **误差线重叠：先认类型与比较设计：**不能通用地把误差线重叠判作不显著，或把不重叠判作显著。解释依赖 SD、SE、CI 类型、样本量以及独立／配对设计；差异判断用相应检验或直接估计差值与区间。已有的误差类型、重复单位和区间定义继续保留，不凭图形外观补出 p 值。

A paired comparison depends on within-pair differences; the two marginal error bars alone do not encode that pairing.

配对比较取决于同一对象的差值，两组均值各自的误差线并没有表示这个配对关系。

## 相关参考和推荐阅读

- [Weissgerber 等（2015）· 小样本连续数据为何需要展示原始观测](https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.1002128)：小样本连续数据：原始观测点揭示均值与误差条隐藏的分布、离群点和配对关系；不禁止所有柱图，不规定统一的小样本阈值。
- [Wilke（2019）· 散点重叠的处理](https://clauswilke.com/dataviz/overlapping-points.html)：调整点大小和透明度；密集散点可用二维分箱或 hexbin，并解释计数或密度。保留原始坐标，不采用 jitter；分箱不等于逐点展示。
- [Wilke（2019）· 颜色使用的常见误区](https://clauswilke.com/dataviz/color-pitfalls.html)：连续量用有大小顺序的色标，避免 rainbow/jet 误导；类别与参照值两侧的偏离分别选择离散或发散色板，不规定唯一色板。
- [Rougier 等（2014）· 科研绘图的十条建议](https://doi.org/10.1371/journal.pcbi.1003833)：根据读者与主要信息选择图型，检查布局、颜色及说明；以气泡面积编码非负数量，避免将半径直接设为数值。示意性形状大小不套用定量比例要求。
- [Cumming 等（2007）· 误差条与组间差异的解读](https://pmc.ncbi.nlm.nih.gov/articles/PMC2064100/)：误差类型、独立样本数与独立或配对设计共同影响区间比较；不把特定条件下的近似重叠规则作为通用显著性判据。配对比较分析差值及相应不确定性。

---

Da1yuqin / [StarPaper](https://da1yuqin.github.io/StarPaper/)，[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)。转载保留署名、出处与许可，改编注明改动。
