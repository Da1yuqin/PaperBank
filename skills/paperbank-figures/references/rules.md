# PaperBank 绘图参考

先查铁律，再按图型选模板。这里的中英句式是教学例子，数值和口径用自己的实际记录。

## 绘图铁律

- **别让一张图讲所有事：**mainfig 讲问题和改动，framework 讲真实流程，结果图讲比较。先写一句图的任务，再选内容；mainfig 默认不超过 5 个环节。

Show where the existing pipeline fails and which step our method changes.

画清旧流程在哪一步出问题，我们改了哪一步。

图例与拆解：[问题和解法放在同一张图](https://da1yuqin.github.io/PaperBank/#visual-tcod-fig-1)

- **别等正文定稿才画图：**先用草图和真实结果定论证，给合作者审。图里问题、做法和证据对不上，正文也别急着精修。

Panel (a) shows the observed gap; panel (b) tests the proposed repair.

(a) 展示实际缺口；(b) 检验我们的修补。

图例与拆解：[对照图要对齐改动](https://da1yuqin.github.io/PaperBank/#visual-tcod-fig-3)

- **别让 AI 编实验曲线：**统计图用 Python 从真实数据绘制；imagegen 用于动机、框架和案例图。缺数据就停，不补点、不编误差、不为平滑改曲线。

Draw the recorded success rates with Python. Generate only the workflow illustration with imagegen.

成功率用 Python 按记录画；imagegen 只生成流程示意。

图例与拆解：[大框先分两块，小框再编号](https://da1yuqin.github.io/PaperBank/#visual-interactcs-fig-1) · [KDE：看哪里密集，不是已经累计了多少](https://da1yuqin.github.io/PaperBank/#teaching-kde)

- **别看放大 PNG 判断字号：**按最终栏宽排字，字体与正文一致；所有图内字同一字号，介于正文与正文减 2 pt 之间，标题也不能更大。放不下先重排，不把字缩成蚂蚁。

Use the paper’s column width and body font; remove repeated labels rather than shrinking text.

用论文栏宽和正文字体；删重复标签，不把字缩成蚂蚁。

图例与拆解：[对照图要对齐改动](https://da1yuqin.github.io/PaperBank/#visual-tcod-fig-3)

- **别用箭头改写真实流程：**同层成组并命名；先后、并行、汇合、反馈按真实依赖画。每条箭头说清传什么，起止明确，不穿字、不绕远路。

Retrieved passages enter the generator; the evaluator receives the generated answer.

检索段落送给生成器；生成的回答交给评价器。

图例与拆解：[大框先分两块，小框再编号](https://da1yuqin.github.io/PaperBank/#visual-interactcs-fig-1)

- **别把评分规则画成模型输入：**输入、输出、评价规则用三种边框区分，并给图例。只供评价的 rubric 不连到被测模型；不同模型收到不同材料，也要标清。

Dashed boxes contain model inputs; solid boxes contain responses; dotted boxes contain evaluator-only criteria.

虚线框是模型输入，实线框是回复，点线框是只供评价的判据。

图例与拆解：[大框先分两块，小框再编号](https://da1yuqin.github.io/PaperBank/#visual-interactcs-fig-1)

- **别把低饱和画成一层灰雾：**白底，面板接近白色，文字和刻度保持深色。同对象全篇同色，再配点形或线型；不用浓重底色、渐变、阴影救场。

Blue circles denote the baseline; orange triangles denote our method in every panel.

每个面板都用蓝圆点表示基线，橙三角表示我们的方法。

图例与拆解：[消融：颜色分组，纹理分方法](https://da1yuqin.github.io/PaperBank/#visual-interactcs-fig-2)

- **别扔一整块对话让人读：**一轮一框，注明角色；同一轮长回复按语义分段，不伪装成多轮。高亮只标关键约束、证据或错误，颜色含义要能读懂。

The left column contains evidence; the right column shows the model response and its evaluation.

左栏放证据；右栏放模型回复和评价。

图例与拆解：[案例：相同信息同框](https://da1yuqin.github.io/PaperBank/#fig-interactcs-case)

- **别把同一案例复制三遍：**同一来源的案例在全文只完整呈现一次，其他位置交叉引用。改名、翻译、裁剪也算同一个；必要对照集中展示，别靠一个 case 证明总体效果。

Figure 1 presents the case; Section 4 refers back to Figure 1 without repeating the dialogue.

案例放图 1；第 4 节回引图 1，不再抄一遍对话。

图例与拆解：[案例：相同信息同框](https://da1yuqin.github.io/PaperBank/#fig-interactcs-case)

- **别每个子图换一套尺度：**围绕一个问题排现象、诊断、对照和稳健性；同条件同顺序、同配色，同类轴和色标保持可比。

The first panel identifies the gap, the second locates it, and the third tests whether it persists.

第一图找差距，第二图找发生位置，第三图检验差距是否仍在。

图例与拆解：[TCOD：四幅图围着一个诊断](https://da1yuqin.github.io/PaperBank/#visual-tcod-fig-2)

- **别靠断轴制造胜利：**查单位、分母、方向、坐标起点和误差类型；截断坐标要明确标出。相对增益同时给绝对值，柱长和数值必须对应。

Accuracy rises from 60% to 66%: 6 percentage points, or a 10% relative increase.

准确率从 60% 到 66%：增加 6 个百分点，相对提高 10%。

图例与拆解：[配对增益：同一任务，直接看差了多少](https://da1yuqin.github.io/PaperBank/#teaching-paired-gain)

- **别把图注写成画法说明：**写比较对象、读法和实际发现；解释缩写、单位、分母、误差和必要标记。图内已写清的别再抄，尽量三行，必要定义不省。

Error bars show 95% question-level bootstrap intervals; the horizontal line marks zero gain.

误差条表示按题目重采样的 95% 区间；水平线表示零增益。

图例与拆解：[置信带：先认统计单位，再认内外两层](https://da1yuqin.github.io/PaperBank/#teaching-confidence)

- **别把编译通过当作图没问题：**放回论文检查实际字号、字体嵌入、可选文字、裁切、碰撞、图注总高度和首次引用顺序。源码字号正确，不代表插入后仍正确。

Place the figure after its first mention and check all labels at normal reading size.

按首次引用顺序排图，以正常阅读大小检查全部文字。

图例与拆解：[问题和解法放在同一张图](https://da1yuqin.github.io/PaperBank/#visual-tcod-fig-1)

- **别省输入和输出：**每个关键模块写清收到什么、做什么、交出什么，以及交给谁。模块名与 Method 一致，别让图成为缩写接龙。

The checker receives evidence and returns supported constraints to the planner.

核查器接收证据，把已支持的约束交给规划器。

图例与拆解：[大框先分两块，小框再编号](https://da1yuqin.github.io/PaperBank/#visual-interactcs-fig-1)

- **别只留图标、缩写和颜色：**图标旁写对象名；新缩写、符号、边框、线型和数字就近解释。读者只看图与图注，应知道每个标记指什么。

Label the robot as the planner and define dashed edges as feedback.

机器人标为规划器，虚线箭头定义为反馈。

图例与拆解：[大框先分两块，小框再编号](https://da1yuqin.github.io/PaperBank/#visual-interactcs-fig-1)

- **别让 framework 变成模块名单：**从创新点组织少量子图，走一条能追踪的案例。保留必要背景、关键请求、证据、操作与输出；删内部编号和无关参数，不删关键文字。

Trace one task from the evidence input through checking to the final plan.

用同一个任务走完证据输入、核查和最终计划。

图例与拆解：[大框先分两块，小框再编号](https://da1yuqin.github.io/PaperBank/#visual-interactcs-fig-1) · [案例：相同信息同框](https://da1yuqin.github.io/PaperBank/#fig-interactcs-case)

- **别把示意画成实测：**估计、作者示例和实测输出分清；可选路径不能画成必经步骤。框的面积、线宽和箭头不能暗示没有证据的比例或因果，别指望图注替错误图形擦屁股。

Keep illustrative module boxes equally sized; plot measured latency on a labeled axis.

示意模块框不靠大小表示耗时；实测延迟另用带坐标的图展示。

图例与拆解：[成本性能：每个点对应一项明确配置](https://da1yuqin.github.io/PaperBank/#teaching-cost)

- **别拿截图 PDF 冒充矢量：**统计图导出矢量 PDF 并嵌入字体。生成底图上的标签另排原生、可见、可选的 PDF 文字；不留重叠字形，不加隐藏 OCR 层。混合 PDF 仍含位图。

Export the plot as vector PDF and verify that its axis labels can be selected.

统计图导出矢量 PDF，再实际选中坐标轴文字检查。

图例与拆解：[对照图要对齐改动](https://da1yuqin.github.io/PaperBank/#visual-tcod-fig-3)

- **别说只改色，顺手把内容改了：**只改配色就保留布局、文字、换行、字号、公式、照片和连线；重排须在约定范围内。数据、实验和合作者的图也别顺手动。

Change panel fills while retaining every label, coordinate, and arrow endpoint.

只换面板底色，保留所有标签、坐标和箭头端点。

图例与拆解：[消融：颜色分组，纹理分方法](https://da1yuqin.github.io/PaperBank/#visual-interactcs-fig-2)

- **别改论文模板给图腾地方：**按实际栏宽起稿，不改页边距、正文字号或页面方向。正文通栏约 16:9、单栏约 4:3 是起点，附录可纵排；不拉扁图。CS 默认用 [!t]，再按正文首次引用检查实际落点。

Rearrange parallel branches within the column width; keep the paper template unchanged.

在栏宽内重排并行分支，保留论文模板。

图例与拆解：[问题和解法放在同一张图](https://da1yuqin.github.io/PaperBank/#visual-tcod-fig-1)

- **别把说明文字塞进表格：**PaperBank 默认表格只放真实结果或数据。术语、方法、实验计划和案例点评写正文，不截成图片绕过去；统计数字也不能把说明表变成实验结果。

Put success rates in a table and explain the checking procedure in the text.

成功率放表格，核查流程写正文。

图例与拆解：[消融：颜色分组，纹理分方法](https://da1yuqin.github.io/PaperBank/#visual-interactcs-fig-2)

- **别拿白块盖住重叠：**图例、标题、刻度和注释不能挡数据、箭头或边框。给文字留空间，重排碰撞处；不是盖住就算修好了。

Move the legend outside the plotted curves while preserving the data and axes.

把图例移出曲线区，保留数据和坐标轴。

图例与拆解：[KDE：看哪里密集，不是已经累计了多少](https://da1yuqin.github.io/PaperBank/#teaching-kde)

## 按图的任务选模板

- **摘要图：**问题在哪、为什么现有解法不够、我们动哪一步。通常最多 5 个环节，必要对照并排。

Show the problem, the existing limitation, and the changed step.

展示问题、已有解法的缺口和我们改动的步骤。

图例与拆解：[问题和解法放在同一张图](https://da1yuqin.github.io/PaperBank/#visual-tcod-fig-1)

- **框架图：**输入是什么，经过哪几个模块，每步产物交给谁，输出是什么。旁边走一个可追踪例子。

Given a query, retrieve passages, rank evidence, and generate an answer with cited support.

输入问题，检索段落，筛选证据，再生成带来源的回答。

图例与拆解：[大框先分两块，小框再编号](https://da1yuqin.github.io/PaperBank/#visual-interactcs-fig-1)

- **案例图：**必要背景、有效需求、关键证据、动作、结果、判据；同类信息同框。

Separate the request, evidence, response, and evaluation.

把请求、证据、回复和评价分开。

图例与拆解：[案例：相同信息同框](https://da1yuqin.github.io/PaperBank/#fig-interactcs-case)

- **主结果与消融：**少量方法用点图或柱图；完整方法与删组件版本同顺序、同配色。说明误差的统计单位和计算方法。

Compare the complete model with variants that remove one component.

完整方法与只删除一个组件的变体对照。

图例与拆解：[消融：颜色分组，纹理分方法](https://da1yuqin.github.io/PaperBank/#visual-interactcs-fig-2)

- **配对增益：**同一样本的干预与对照，画差值和零线；写清收益方向与尺度。

Each point shows the intervention-minus-control accuracy on matched questions.

每个点表示同一批题目上干预相对对照的准确率差。

图例与拆解：[配对增益：同一任务，直接看差了多少](https://da1yuqin.github.io/PaperBank/#teaching-paired-gain)

- **训练或轮次动态：**折线只连有序变量；横轴写训练步数或轮次，不把无序方法连成趋势。

Track success rate and penalty magnitude against the same training steps.

用相同训练步数同时追踪成功率和惩罚强度。

图例与拆解：[训练动态：控制量和实际行为并排](https://da1yuqin.github.io/PaperBank/#visual-interactcs-fig-3)

- **KDE：看分布形状：**横轴是变量，纵轴是密度；颜色跟组走，均值线补位置，交代样本量和带宽。峰高不是人数，也不是累计比例。

Compare density shapes with a shared bandwidth; mark sample counts and mean values.

统一带宽比较密度形状，并标样本量与均值。

图例与拆解：[KDE：看哪里密集，不是已经累计了多少](https://da1yuqin.github.io/PaperBank/#teaching-kde)

- **ECDF：看阈值以下有多少：**横轴取阈值，纵轴直接读累计比例；同一坐标比两组，阶梯从 0 到 1。想读“多少样本低于 10”，别去量 KDE 的峰。

At a threshold of 10, the ECDF gives the fraction of observations at or below 10.

阈值取 10 时，ECDF 直接给出不超过 10 的样本比例。

图例与拆解：[ECDF：直接读有多少样本不超过这个值](https://da1yuqin.github.io/PaperBank/#teaching-ecdf)

- **热图：**条件乘方法，统一色标；正负增益以零为中点，缺测留空并说明。

Use one shared color scale for all conditions and mark missing cells.

全部条件使用统一色标，缺测单元明确标记。

图例与拆解：[热图：一个色标，缺测直接空出来](https://da1yuqin.github.io/PaperBank/#teaching-heatmap)

- **PCA：把高维关系投到二维：**说明输入特征、标准化、每轴解释方差。颜色或轨迹分别代表什么写清；分得开不等于泛化好。PaCMAP、t-SNE 也别改名叫 PCA。

Project standardized features onto two principal components and report the variance explained by each axis.

把标准化特征投到两个主成分，并报告每根轴的解释方差。

图例与拆解：[PCA：先定义输入，再看二维投影](https://da1yuqin.github.io/PaperBank/#teaching-pca)

- **雷达图：多指标逐轴读：**每轴一个指标，写尺度、归一化和好坏方向；颜色再配点形。量纲不同别比面积，轴换个顺序，面积也会换。

Compare normalized metrics spoke by spoke; polygon area is not an overall score.

沿每根轴比较归一化指标；多边形面积不是综合分数。

图例与拆解：[雷达：看各项轮廓，别拿面积当总分](https://da1yuqin.github.io/PaperBank/#teaching-radar)

- **成本性能图：**每点是一个实际配置；在线与离线成本分开，写单位和好坏方向。连接前沿不意味着有中间配置。

Plot measured accuracy against online cost; report one-time training cost separately.

实测准确率对照在线成本；一次性训练成本另报。

图例与拆解：[成本性能：每个点对应一项明确配置](https://da1yuqin.github.io/PaperBank/#teaching-cost)

- **数据集分布：**统计单位、样本量、类别和分母先写清；同一图别混案例数、回复数和判据数。重点是覆盖了什么，不是圆画得多圆。

Count unique cases by domain; report response counts separately.

按领域统计独立案例数；回复数量另报。

图例与拆解：[环图：组成比例，先说总数](https://da1yuqin.github.io/PaperBank/#teaching-donut)

- **置信带：**按实际重采样或模型计算区间，写清区间类型和置信水平。同一估计的嵌套区间才可比较覆盖范围；不同样本量、方差也会改变带宽。

Nested bands show the estimated 68% and 95% intervals under the stated procedure.

嵌套色带表示按所述方法估计的 68% 和 95% 区间。

图例与拆解：[置信带：先认统计单位，再认内外两层](https://da1yuqin.github.io/PaperBank/#teaching-confidence)

- **饼图、环图与圆环排名：**饼图只画互斥且组成整体的比例；圆环柱图可画排名，极值相邻只是环形排序，不是变量关系。要读精确差值，横向条图更方便。

Use slices for a composition and ordered bars for a ranking.

组成比例用扇区；排名用有顺序的柱条。

图例与拆解：[环图：组成比例，先说总数](https://da1yuqin.github.io/PaperBank/#teaching-donut)

- **二维增益与九宫格：**两轴分别写指标、单位和好坏方向；差值图以零线分区。九宫格用于两个有序因素的组合，别为凑九格补数据。

With both gains defined as higher is better, the upper-right quadrant shows improvements on both metrics.

两个增益都定义为越高越好时，右上象限表示两项指标都改善。

图例与拆解：[二维增益：右上都改善，其他象限看取舍](https://da1yuqin.github.io/PaperBank/#teaching-two-gain)

---

Da1yuqin / PaperBank，[原文](https://da1yuqin.github.io/PaperBank/#figures)，[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)。转载保留署名、出处与许可；改编注明改动。第三方原图不随包分发。
