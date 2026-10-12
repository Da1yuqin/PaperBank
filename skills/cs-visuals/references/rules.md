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

- **【铁律】表格用于结果与数据：**BeautyPaper 默认表格只放真实结果或数据。术语、方法、实验计划和案例点评写正文，不能通过截图规避该规则；统计数字也不能把说明表变成实验结果。

Put success rates in a table and explain the checking procedure in the text.

成功率放表格，核查流程写正文。

- **【铁律】重排文字与图形重叠处：**图例、标题、刻度和注释不能挡数据、箭头或边框。为文字保留空间，通过重排解决重叠，不能用遮盖隐藏问题。

Move the legend outside the plotted curves while preserving the data and axes.

把图例移出曲线区，保留数据和坐标轴。

---

Da1yuqin / [BeautyPaper](https://da1yuqin.github.io/PaperBank/)，[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)。转载保留署名、出处与许可，改编注明改动。
