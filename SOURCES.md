# 来源说明

## 写作笔记

主体来自作者提供的论文写作笔记，以及绘图、引言进阶与审稿回复笔记。内容按论文成稿顺序重组；新增 RQ、结构与图表建议经公开原文核对。未发布私人 Notion 页面、原始粘贴材料或协作者信息。

2026-10-10 回读作者的《一篇论文的写作流程-Vibe Writing版》《Intro 写作进阶》《参考绘图》《合作写论文》《高级的实验》。原句按章节目的融入正文，并配中英模板与拆解：例如“不要误解成 Preliminary”“不要读数字”“先看框架图和实验”。引号中的片段保留原措辞；相邻解释为本指南整理，不公开私人页面全文、协作者评论或未发表案例。

审稿回复按意见类型选择澄清、修正、补证据或解释范围，不推测审稿人身份和情绪，不预测涨分，不把投入的算力当论证。影响结论的负结果和未解决问题如实交代。

个人经验不是录用公式。未保留无依据的录用率、固定引用数、万能篇幅比例或“37%规则”；不把可视化当理论证明，不用措辞替代真实实验。

## 写作技能

吸收作者日常使用的 `paper-writing-clarity`、`cs-writing-skill`、`paper-visual-standards`、`paper-reading-assistant` 中可迁移的检查习惯：定义具体对象，核对主张与证据，说明输入输出，统一术语与图注。

公开下载分为 `cs-paper-writing` 与 `paperbank-figures` 两个独立 skill，分别负责正文与绘图。规则由上述检查习惯及 `paper-introduction`、`clean-flow-figures`、`minimal-code-layout` 的通用要求重新表述；区分证据、记录和权限边界与可调整的写法。每条配原创中英教学例子，假设情境不是真实论文结果。未把特定项目的色板、尺寸、段落配额、固定连接词或禁用全部代词推广为通用学术规范。

公开 skill 由本项目独立编写，包含入口、生成的规则参考及许可；网页和 skill 参考从同一份章节数据生成，避免两套规则分叉。ZIP 不含私人 skill 原件、机器路径、论文源稿、真实审稿记录或第三方摘录。

写作包于 2026-10-12 改为按章节加载：`cs-paper-writing` 入口、`cs-writing-common` 共享规则，以及摘要与引言、相关工作、方法、实验、图表、全文整合六个章节 skill。旧下载地址和规则索引保留；解压后保留八个同级目录，只读取当前任务相关章节和按需模板。

本次同步通用钩子、贡献列表、方法动机与实验论证组织，并更新网页中的对应模板和提示词。私人稿件名称、统计、模型配置、内部构建流程、修订记录及授权轮次均未迁入公开包；保留原已公开论文摘录，未用私人稿件替换教学例。

全文及各章要求依据最新的通用 CS 写作规则整理，分别覆盖摘要与引言、相关工作、方法、实验和全文整合。只有明确必须遵守或禁止违反的要求标为铁律，写法偏好与可调整建议不作硬性约束。篇幅利用、实验页呈现与超页删减顺序来自作者笔记，说明为何需要充分展开证据；它们不是官方最低页数或固定扣分标准。保留已有论文摘录，不将私人项目的具体事实、配置或例外写入通用规则。

## 公开参考与适用范围

- [Mensh & Kording (2017) · Ten simple rules for structuring papers](https://doi.org/10.1371/journal.pcbi.1005619)：中心贡献、读者视角与文章/段落结构；写法需要按研究取舍。
- [Rougier et al. (2014) · Ten Simple Rules for Better Figures](https://doi.org/10.1371/journal.pcbi.1003833)：根据读者与主要信息选择图型，检查布局、颜色及说明。
- [pymoo · Basics and Challenges](https://pymoo.org/getting_started/preface.html)：多目标比较与支配关系。有限配置中找到非支配解，不等于证明全局 Pareto 最优。
- [Callaway & Sant’Anna · Difference-in-Differences with Multiple Time Periods](https://arxiv.org/abs/1803.09015)：DID 比较设计与平行趋势等识别条件。正文的两组前后数值为虚构教学例子，不把普通算法消融当作 DID。
- [Henderson & Chambers (2022) · Ten simple rules for writing a Registered Report](https://doi.org/10.1371/journal.pcbi.1010571)：研究问题、适用时的假设与预先规划；不要求所有论文写 RQ1/H1。
- [NeurIPS · Paper Checklist](https://neurips.cc/public/guides/PaperChecklist)：主张、限制、设置、统计不确定性与复现；提交时以当年指南为准。
- [ACL Rolling Review · Responsible NLP Research](https://aclrollingreview.org/responsibleNLPresearch/)：NLP 研究责任与披露要求；其他领域检查自己的投稿政策。
- [Liu et al. (2024) · Lost in the Middle, Figure 1 / §2](https://aclanthology.org/2024.tacl-1.9/)：证据位置与问答表现的控制实验，适合学习“现象—诊断”的论证。
- [TCOD (2026 预印本) · Figure 1](https://arxiv.org/pdf/2604.24005v3)：多轮监督案例与课程设计并排呈现；概念图本身不证明效果。
- [Reinforcing Real-world Service Agents (2026 预印本) · Figure 1](https://arxiv.org/html/2602.22697v1#S4.F1)：交互环境、轨迹、学习信号与更新对象的框架图；模拟表现不等于真实部署收益。

- [NeurIPS 2026 · Main Track Handbook V2026.3，Author Responses](https://neurips.cc/Conferences/2026/MainTrackHandbook)：2026 主会回复流程、匿名、篇幅与新结果要求；其他年份和赛道另查指南。核查日期：2026-10-07。
- [ICLR 2026 · Author Guide，Discussion Stages](https://iclr.cc/Conferences/2026/AuthorGuide)：2026 讨论期修订与变更说明；审稿人和 AC 不必阅读每一版。实际投稿遵循当轮最新通知。核查日期：2026-10-07。
- [ACL Rolling Review · Authors Guidelines，Author response](https://aclrollingreview.org/authors#author-response)：截至 2026-10-07 可见的作者回复指南；页面注明此版适用至 2026 年 8 月轮次，后续轮次需重查。用于了解 ARR 与直接投会议的区别，不作后续轮次规则保证。

写作指南提供组织方法，会议清单提供报告要求，研究论文提供特定任务与模型上的例子。来源链接是延伸阅读，不代表它们验证或认可了全部个人经验。具体投稿政策以当年的官方指南为准。

## 例子与图片

`assets/paperbank-accept-team.png` 是为 PaperBank 生成的 AI 开场插画：红色 accept 和庆祝彩带下，边牧、魔法橘猫和龙收到论文录用邮件后庆祝。它不对应真实录用通知，不含会议标识。生成时参考作者提供的蓝色 accept 草图及魔法橘猫角色图；参考角色的权利归原权利人，项目许可不授予第三方角色权利。

Intro、Related Work 与 Method 开头新增整段教学展示：GreenPlanner（CVPR Findings 2026）§1 前两自然段及 §3 开头段，TCDiff（AAAI 2025）Related Work 的 Music-driven Multi-dancer Generation 段。以作者授权的教学复用方式保留原段及引文，新增中英对应高亮和旁批，未润色英文原句。仅还原 PDF 排版断词、字体连字和空白，不发布整篇论文或源稿；原版权与出处保留。下载的三个 skill 仅包含原创规则和教学模板，不打包这些论文段落。

每个整段 case 只放一个自然段；旁批分别说明写法、缺口和修改方向，不将已发表原文视为标准答案。三组购物场景修改 case 及 Abstract ↔ Intro 对照图，根据作者提供的批注独立撰写，分别演示困难铺垫、专家产物与筛选、发现总览与分析。它们是教学改写，方括号中的方法名、图号和模型范围为占位，不报告当前稿件的名称、数量、引用、实测结果或未经核对的比较结论。

真实论文例子包含英文原文、中文翻译、逐句拆解及出处。需要迁移到自己的文章时，再给单独标注的教学改写。

摘录核对作者终稿或正式发表 PDF，仅移除 LaTeX 排版、文献标记和排版断词，合并换行；数学符号以可读形式转写，图表引用按正式版解析。原句不作润色，中文为本指南翻译。原文中的强主张、指标局限或单位问题，在拆解中解释，不静默改动引文。

作者终稿通过只读副本核对，其他短引依据公开论文 PDF。未编辑原论文项目，不公开完整源稿、私人项目链接或内部路径。

| 摘录论文 | 原始发表与摘录版本 | 许可与复用范围 |
| --- | --- | --- |
| Yuqin Dai et al., [Careful Queries, Credible Results: Teaching RAG Models Advanced Web Search Tools with Reinforcement Learning（WebFilter）](https://ojs.aaai.org/index.php/AAAI/article/view/40299) | AAAI 2026, 40(36):30458–30466；2026-03-14 正式发表。摘录核对作者 camera-ready 终稿与正式版。 | © 2026 AAAI，保留原版权；以作者教学短引展示，不随本指南转授第三方再版权利。 |
| Yuqin Dai et al., [Harmonious Music-driven Group Choreography with Trajectory-Controllable Diffusion（TCDiff）](https://ojs.aaai.org/index.php/AAAI/article/view/32268) | AAAI 2025, 39(3):2645–2653；摘录来自正式发表版。 | © 2025 AAAI，保留原版权；作者教学短引，不纳入本指南原创内容的 CC BY 许可。 |
| Pengyu Zeng et al., [CARD: Cross-modal Agent Framework for Generative and Editable Residential Design](https://aclanthology.org/2025.emnlp-main.473/) | EMNLP 2025:9304–9319；短引来自正式发表版。 | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)。保留原论文署名、出处与许可，说明中文翻译。 |
| [Zeng, Dai et al. (2026 预印本) · PlanCraft: Sketch, Refine, and Furnish for Architect-Inspired Progressive 3D Residential Scene Generation](https://arxiv.org/abs/2607.23491v3) | arXiv v3，2026-09-05，公开预印本 | arXiv.org perpetual non-exclusive license；原文权利保留 |
| [Ling Shi, Yuqin Dai et al. · SAGE: An Extensible Benchmark for Service Agent Graph-guided Evaluation](https://arxiv.org/abs/2604.09285) | 教学摘录采用作者终稿 2026-10-04 只读快照；公开 arXiv v1（2026-04-10）题名为 SAGE: A Service Agent Graph-guided Evaluation Benchmark，两者不是同一版本。 | 作者终稿教学短引，保留原论文版权；不随 PaperBank 原创内容转授终稿转载权。公开 arXiv v1 的 CC BY 4.0 已核验，该许可不自动延伸到不同版本的作者终稿。 |
| [Pengyu Zeng et al. (CVPR Findings 2026) · GreenPlanner: Practical Floorplan Layout Generation via an Energy-Aware and Function-Feasible Generative Framework](https://openaccess.thecvf.com/content/CVPR2026F/html/Zeng_GreenPlanner_Practical_Floorplan_Layout_Generation_via_an_Energy-Aware_and_Function-Feasible_CVPRF_2026_paper.html) | CVF Open Access 作者接受版；正式发表元数据已由 CVF 条目核对 | 原权利人保留版权；CVF Open Access 未声明 CC BY。本指南仅作署名教学短引，不重新发布全文或原图，不向第三方转授原论文版权。 |
| [Yuqin Dai et al. · EviNoteRAG: Enhancing RAG Models via Quality-Augmented Evidence Notes](https://arxiv.org/abs/2509.00877) | 教学摘录采用作者提供的 EMNLP 2026 revised 终稿；公开 arXiv v3（2025-10-16）题名为 EviNote-RAG: Enhancing RAG Models via Answer-Supportive Evidence Notes，两者不是同一版本。 | 作者终稿教学短引，保留原论文版权；不随 PaperBank 原创内容转授原论文再版许可。公开 arXiv v3 为 non-exclusive distribution，并非 CC 授权；代码 Apache 2.0 不作为论文许可。 |
| [Yuqin Dai et al. (IJCV 2026；引文为 arXiv v4) · TCDiff++: An End-to-end Trajectory-Controllable Diffusion Model for Harmonious Music-Driven Group Choreography](https://link.springer.com/article/10.1007/s11263-025-02611-3) | 短引来自 arXiv:2506.18671v4，2025-10-05；正式期刊元数据已核对，不将作者稿等同于期刊排版终版 | arXiv 作者稿采用 non-exclusive distribution 许可，非 CC BY。正式期刊版权按 Springer 出版协议保留；本指南不向第三方转授原论文版权。 |
| [Chaoyang Shi, Yuqin Dai et al. · UrbanZero（公开项目介绍）](https://github.com/Da1yuqin/Da1yuqin.github.io/blob/main/_pages/includes/pub.md#L193-L202) | 作者公开项目介绍（GitHub 仓库） | 项目论文及原图版权保留；本指南教学改写单独授权，不转授论文或原图许可。 |

AAAI 的[版权与作者复用说明](https://aaai.org/aaai-publications/request-to-reproduce-copyrighted-materials/)与 [PMLR 许可说明](https://proceedings.mlr.press/pmlr-license-agreement.html)分别适用原论文材料。网页许可不覆盖原论文全文或所有外部图片；复用带原文的例子时，一并检查原材料许可。

现有四张图片来自作者绘图笔记中已逐图核对的公开材料：

| 文件 | 原出处 | 处理 |
| --- | --- | --- |
| `paper-tcod-fig2.png` | Jiaqi Wang et al., TCOD, arXiv:2604.24005v3, Fig.2, PDF p.4 | 保留四面板及完整图注 |
| `paper-interactcs-fig2.png` | Ning Gao et al., Reinforcing Real-world Service Agents, arXiv:2602.22697v1, Fig.2, PDF p.7 | 保留四面板、图例与图注 |
| `paper-interactcs-fig3.png` | 同上，Fig.3, PDF p.35 | 保留双面板、坐标与图注 |
| `paper-interactcs-case-summary.png` | 同上，Appendix B.1, PDF p.13 | 仅截取案例摘要框；完整对话见原文后页 |

以上图来自对应版本的公开 PDF，采用 [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)。仅裁切图外区域并渲染为 PNG，未修改图形、标签、分数或曲线；中文点评与双语读图说明为本指南新增。原图未明确定义的阴影和误差线不代称为标准差或置信区间。截断坐标轴保留，并在点评中提醒不能据柱高推倍数。

作者笔记中 OneReason Technical Report 的 Figure 12 已核对至 arXiv:2606.06260v1、PDF p.34。仅链接并分析结构，不复制整图；arXiv 分发许可不是第三方复用图片许可。未核实来源的图片不以相邻链接猜出处。

单栏 mainfig 示例 `assets/paper-lost-middle-fig-1.png` 来自 Liu et al., *Lost in the Middle: How Language Models Use Long Contexts*, TACL 12 (2024), Figure 1，期刊 p.158 / PDF p.2（[正式论文](https://aclanthology.org/2024.tacl-1.9/)）。PDF 首页明确采用 CC BY 4.0。仅提取完整图面，保留原始曲线、坐标、标题与图例；中英读图说明为本指南新增。图中为 GPT-3.5-Turbo 在 20 文档任务中的位置对照，用于讲解发现型首图，不推广至所有模型与任务。

`assets/flow-example.svg` 与 `assets/case-example.svg` 是原创教学示意图，展示信息布局，不模拟真实实验结果。

比格头像、全身形象与挥笔帧以作者提供的头像为参考，使用内置图像生成工具制作。挥笔 GIF 由生成的六个姿态统一尺度后编码；不是实拍。坐姿小狗沿用作者个人主页的原创吉祥物素材。素材为 `assets/beagle-logo.png`、`assets/beagle-pet.png`、`assets/beagle-wave.gif` 与 `assets/beagle-sitting.png`；按 CC BY 4.0 许可使用，保留作者与来源。

桌面伴侣源码在 `companion/`，实现采用 MIT；应用内上述素材仍采用 CC BY 4.0。

## 页面与语言

页面组织与表达受到 eternity4719 的[《高性价比人生指南》](https://eternity4719.github.io/HowToLiveBetter/)启发：按主题读、说清可执行动作、需要时再看说明。论文正文重新组织，页面实现独立编写，未转载原站生活建议或图片。

## 使用与转载

原创正文、提示词与教学图采用 [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)，原创代码采用 [MIT](https://opensource.org/license/mit)，详见 [LICENSE](LICENSE)。转载保留作者 Da1yuqin / PaperBank、原文链接及许可信息；改编注明改动。Star 不是许可条件。论文摘录、摘录译文与原图保留各自版权和许可；原创指南的授权不转授这些材料，复用时保留紧邻的论文出处与许可。

## checklist 怎么用

正文主要面向实证型 CS / AI 论文，不把一种文章的组织方法当作所有学科的硬性格式。

## 工具清单

工具与资源按项目公开页面、官方说明与 README 整理，核对日期为 2026-10-07。只链接原项目并用本指南文字说明用途，不转载第三方 README、SKILL、插件源码或配图。未逐项安装、测试效果或做安全审计；中英例子是使用情境，不代表实测输出。第三方工具按原项目许可使用，不纳入本指南的授权。

知乎文章以社区经验收录，不复述排名为客观结论；小红书去参入口未能显示笔记正文，相关绘图工具直接链接其 GitHub 仓库。使用公开入口，不保留社交分享参数、私人笔记地址或个人论文认领参数；Hugging Face 的日期页明确标为历史示例。

Lieflat Charts 的非商业许可、THU-PPT-Theme 的 CC BY-NC-SA 条件，以及 Edit Banana 的 README 与 LICENSE 不一致问题，均就近说明。工具“找到论文”与“论文支持正文论断”分开核验，自动报告不作为学术不端判定。

开源整理提示词由作者需求改写，限制在指定文件，区分注释翻译与可执行字符串、配置和路径改动；保留作者署名与许可，不把秘密原值写进报告，也不承诺只靠文字替换就完成去秘。


## 多来源例子

56 个原文例子来自八篇论文：PlanCraft、SAGE、GreenPlanner、EviNoteRAG、TCDiff、TCDiff++、WebFilter 和 CARD。每篇采用 4–8 处短引，按条目的写作问题选例子。原文、中文翻译与教学改写分别展示；终稿与所链公开预印本不同版本时就近说明。

UrbanZero 的 8 个例子依据作者公开主页仓库的项目介绍编写，仅为教学改写。公开介绍不能替代论文的实验记录；教学 RQ、对照与模拟回复不声称已经实施。skill 规则的 32 个双语例子仍为假设情境。

## 逐段逐句示范

29 组逐句示范包括 9 处真实论文短引，其余为明确标注的教学例句。真实短引沿用上面的出处、版本与位置，不把不同论文拼成同一篇文章；摘要或图注中的句子用于说明引言或方法写法时，标明实际来源位置。教学问答研究中的方法协议、200 道问题、72%→81% 支持率和 1.2→1.5 秒延迟均为假设，不是任何论文的实测结果。段落顺序展示论证任务，不规定固定段数；按领域、研究类型和投稿模板调整。

首页提示词按作者笔记的流程整理：先形成提纲与初稿，再绘图、人工审核，最后通读全文精修。贡献修饰词例子对应已确认的写作要求：具体、正面、有事实依据；等量替换，避免重复修饰。例句不声称描述任何已发表论文的事实。


## 五章结构与补充模板

起草、绘图、Refine、工具按作者提供的流程重新组织。全文表达要求、Related Work 和 Method Overview 等完整句式由 PaperBank 编写，方括号模板和改写均为教学示例，不是论文原文。原有 56 处短引保持原句与出处。公开 skill 同步包含全文规范和各章模板，不分发论文源稿或第三方原图。

Overleaf 本地 Git 同步的 Premium 权限与当前入口核对自 [Git integration](https://docs.overleaf.com/integrations-and-add-ons/git-integration-and-github-synchronization/git-integration)；无 Git 权限时的 ZIP 下载核对自 [Downloading a project](https://docs.overleaf.com/managing-projects-and-files/downloading-a-project)。

新版子刊图例对应 Bruno et al., *A universal framework for inclusive 15-minute cities*, Nature Cities 1, 633–641 (2024), [DOI](https://doi.org/10.1038/s44284-024-00119-4)。图 1、图 2 的内容与编码核对自作者的 [arXiv:2408.03794v1](https://arxiv.org/html/2408.03794v1)：颜色为 Gini，圆大小为人口密度；图 2b 为现有 POI 迁移比例。该预印本是 arXiv 非独占分发许可，出版社版本保留版权；本指南只链接原图并提供原创点评，不重新托管这两张图片。

## 绘图图例与逐图点评

图型拆分为 KDE、ECDF、PCA、雷达、置信带等；每条绘图要求链接对应的图例与中英拆解。KDE 是密度，ECDF 是累计比例；life2vec 正式图使用 PaCMAP，不称为 PCA。阴影和误差条的统计定义须看原图说明，不从外形推断置信水平。

重新核对 Notion 收藏中的 64 张图。公开版重现许可明确的 TCOD v3 图 1–6、InteractCS-RL v1 图 1–3，均从对应原 PDF 裁切，仅去掉周围页边，保留图内数据、文字和颜色，并署名、标示 CC BY 4.0 与裁切。图片中的角色图标不单独提取或重新授权。OneReason、ShoppingBench 和 life2vec 的图保留原文链接与原创点评。包含内部信息标记、账号水印、订单编号或匿名投稿材料的截图不公开；收藏在私人笔记中不自动意味着可转载。

标为“教学图”的统计图由 PaperBank 用固定模拟数据独立生成，只演示图型、读法和信息编码，不对应任何论文实验。绘图源码提供相对路径入口，数据和计算方法随源码公开；这些图与 Notion 原图明确区分。


## 评论与正文批注

复用作者个人主页的原创评论界面与批注脚本，沿用已有评论服务；PaperBank 的评论使用独立页面标识。公开批注显示所选正文和回复，私密留言仅由站点所有者查看。正文索引保留折叠及搜索隐藏内容，排除表单和按钮，保证筛选前后定位一致；引用点击可展开对应内容。未分发后台凭据或评论数据库。

## 起草流程与图表模板

第一章按填材料、定图、组织章节与实验、审核 Intro 四步整理。规则参考作者最新的 cs-paper-writing、paper-writing-clarity、cs-writing-skill 和 paper-visual-standards，重新表述为公开教学内容；不公开私人项目配置、提示词或数据。字号与比例是 PaperBank 的起排建议，会议官方格式优先。章节和中英句式为教学模板，需替换为实际研究。

动机图和框架图沿用图例库已署名的 TCOD v3 图 1、InteractCS-RL v1 图 1，未改原图。LaTeX 表格和网页预览使用明确标注的假设数值，仅演示排版和标记。Overleaf Git 权限、同步限制及源文件 ZIP 说明于 2026-10-10 回查官方文档。

## 公开绘图 skill

`paperbank-figures` 将作者的通用图表规范、流程图规则与统计绘图要求整理为独立公开包：SKILL.md、22 条绘图规范与 16 类图型的中英参考、CC BY 4.0 许可。它与网页使用同一份规则，不包含私人项目配置、本地路径、稿件、实验数据或第三方图片。图例只链接网页已有的署名与出处。CS 默认约定不作为所有学科、会议的硬性标准；当前稿件配置与官方要求优先。


## 古法精修：各节原则与整段旁批

标题至附录的节首原则参考作者的 Notion 写作笔记与最新 CS 写作规范，重新表述为公开教学内容。Related Work 小节结尾按 However → 具体局限 → 对应方案组织，对齐 Introduction；客观限定原工作实际覆盖的范围。

新增原文案例为 WebFilter 的完整标题、TCDiff 的 Footwork Adaptor 消融段（AAAI 2025，p.2651）和 EviNote-RAG 的公开 arXiv:2509.00877v3 Conclusion 第一自然段。英文保持原文；中译、高亮与旁批为 PaperBank 添加，出处、版本和原文许可紧邻案例。其他新增段落均标明假设教学场景，不作为真实文献判断或实验结果。

## 教程编排

公开教程编排 skill 总结内容顺序、标题、简洁表达、完整案例与旁批、窄屏和交付检查；为独立的通用规则，不分发私人材料或路径。

## BeautyPaper 品牌与新主图（2026-10-12）

展示名由 PaperBank 更为 BeautyPaper；原仓库地址、网页地址、skill 机器名及批注页面标识保留兼容。原有论文摘录、引用和研究事实未因品牌变化修改。

`assets/beautypaper-presentation.png` 由 imagegen 生成，参考旧主图的整体插画风格与三位通用动物角色，重新组织为西施犬展示论文、边牧／魔法橘猫／龙举 ACCEPT 牌的场景。红色 ACCEPT 与彩带是庆祝性的品牌插画，不对应真实录用决定；论文、表格和图形为装饰示意，无实测数字或会议标识。生成说明见 `assets/beautypaper-presentation-prompt.txt`。旧主图及其来源记录保留。

## 分章写作包细则同步（2026-10-12 14:44 UTC+8）

核对当时的 cs-writing-common、cs-abstract-introduction、cs-related-work、cs-method、cs-experiments、cs-visuals 与 cs-integration 当前章节规则。原有钩子、可变引言结构、贡献格式及 Related Work 收尾已在公开包；本次补齐数字与文献版本口径、完整应用字段、实验章首发现概述、实际覆盖与判分可靠性、章节承接边界、图注与脚注细则。网页、Markdown、章节 skill 与下载包从同一公开规则生成。

只提取可迁移要求并重新表述。私人论文的命名、数量、结果、固定篇幅、章节编号、内部流程、路径和未公开范例不迁入公开包；项目特例不当作通用写作要求。原论文段落与图资产未改。

开头更新记录采用原生 details，默认折叠；历史两项日期来自对应公开提交的作者时间。本次写作及绘图包、各章 SKILL.md 和网页下载入口统一标注 latest 日期与分钟。

## 三类绘图模板与教学改排（2026-10-12）

绘图正文按 Mainfig、Framework、实验绘图组织。节首心得来自作者的 Notion 绘图笔记：先简化、问题与改动对齐、位置与分组表达关系、同一案例展示中间产物、白底局部高亮、颜色与纹理共同编码、绝对值与相对增益同报。按当前 CS 绘图规范标出必须遵守的要求，编排建议不升格为铁律。

新增 `assets/figure-mainfig-before-after.svg`、`assets/figure-framework-before-after.svg` 和 `assets/figure-experiment-before-after.svg` 是原创教学改排，分别展示重点、信息流和统计图排版。前两张是假设流程；第三张两侧使用同一组教学数值（60%、66%），未补造误差或实验记录。三张都不是原论文真实修改历史，采用 CC BY 4.0。其余已有原图与教学图移动至文末附录，图面、出处与许可不变；KDE、ECDF 等点评保留。

## StarPaper 更名、流星插画与写作包同步（2026-10-13）

当前教程、仓库及公开网址更名为 StarPaper。历史记录、原论文摘录和研究事实保留；评论、批注与统计沿用历史逻辑标识，避免数据分叉。

assets/starpaper-logo.png 与 assets/starpaper-night-accept.png 由内置 imagegen 生成，分别参考自有 StrongResponse 标题质感和作者提供的三位动物角色。流星和 ACCEPT 为庆祝性的品牌插画，不对应真实论文接收或实验结果。生成说明见同目录的 prompt 文本。

`assets/refine-alignment-comic.png` 与 `assets/refine-attribution-comic.png` 沿用封面三位角色，由内置 imagegen 生成。两幅教学漫画分别说明问题、设计与实验的对应关系，以及模块归因所需的对照；不展示实测结果。生成说明见 `assets/refine-comics-prompts.json`，角色复用边界同封面。

写作包新增 cs-limitations，九个同级模块，附单段 First/Second 模板；同步 Metrics 编号、贡献格式和篇幅规则。只提取通用要求，未复制私人论文案例、数量、模型、费用、路径或审核记录。官方要求与当前人工要求优先。

## 相关参考和推荐阅读（2026-10-13 绘图补充）

本次仅补充原有绘图内容的五处缺口：小样本连续数据的原始观测、散点重叠、连续量色标、气泡面积编码，以及误差条重叠的解释边界。正文与教学例子由 StarPaper 独立归纳，不复制下列来源的图文；链接统一收录在文末推荐阅读，不插入正文。既有绘图规则和非定量示意图流程保留。

- [Weissgerber, Milic, Winham & Garovic (2015) · Beyond Bar and Line Graphs: Time for a New Data Presentation Paradigm](https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.1002128)：小样本连续数据的均值与误差条可能隐藏离群点、分布差异和配对关系，适合补充原始观测点；不将其建议扩展为禁止所有柱图，也不规定统一的小样本阈值。
- [Wilke (2019) · Fundamentals of Data Visualization, Chapter 18: Handling overlapping points](https://clauswilke.com/dataviz/overlapping-points.html)：适当调整点大小与透明度；密集散点可改用二维分箱或 hexbin，并说明格子的计数或密度。本指南保留原始坐标，不采用该章的 jitter 方案；分箱不等于展示每个观测点。
- [Wilke (2019) · Fundamentals of Data Visualization, Chapter 19: Common pitfalls of color use](https://clauswilke.com/dataviz/color-pitfalls.html)：连续数值应使用能传递大小顺序的色标，避免 rainbow/jet 的非单调明度产生误导；无序类别与有意义参照值两侧的偏离分别选择离散或发散色板，不把某一个色板规定为唯一选择。
- [Rougier, Droettboom & Bourne (2014) · Ten Simple Rules for Better Figures, Rule 7](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1003833)：扩展现有来源的适用范围，核对气泡以面积而非半径编码非负数量。半径与数值平方根成正比由圆面积公式推导；形状大小用于示意时不套用定量比例要求。
- [Cumming, Fidler & Vaux (2007) · Error bars in experimental biology](https://pmc.ncbi.nlm.nih.gov/articles/PMC2064100/)：误差类型、独立样本数与独立或配对设计共同影响区间比较。原文针对特定条件提供近似重叠规则，本指南不将其推广为通用显著性判据；配对或重复测量比较应分析差值及相应不确定性。

来源按原作者教程与正式论文内容筛选，并逐项核对适用条件。2026-10-13 读取的 GitHub 数据中，Wilke 的 [dataviz](https://github.com/clauswilke/dataviz) 为 3,540 stars，Rougier 的 [scientific-visualization-book](https://github.com/rougier/scientific-visualization-book) 为 11,623 stars；这些计数仅说明关注度，不作为建议正确或有效的证据。
