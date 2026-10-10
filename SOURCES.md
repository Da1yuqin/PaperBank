# 来源说明

## 写作笔记

主体来自作者提供的论文写作笔记，以及绘图、引言进阶与审稿回复笔记。内容按论文成稿顺序重组；新增 RQ、结构与图表建议经公开原文核对。未发布私人 Notion 页面、原始粘贴材料或协作者信息。

审稿回复按意见类型选择澄清、修正、补证据或解释范围，不推测审稿人身份和情绪，不预测涨分，不把投入的算力当论证。影响结论的负结果和未解决问题如实交代。

个人经验不是录用公式。未保留无依据的录用率、固定引用数、万能篇幅比例或“37%规则”；不把可视化当理论证明，不用措辞替代真实实验。

## 写作技能

吸收作者日常使用的 `paper-writing-clarity`、`cs-writing-skill`、`paper-visual-standards`、`paper-reading-assistant` 中可迁移的检查习惯：定义具体对象，核对主张与证据，说明输入输出，统一术语与图注。审稿回复部分还参考 `review-response`、`rebuttal-reviewer-profile`、`rebuttal-reviewer-simulator` 的通用做法：保留意见原意、逐题核对证据、说明完成状态与修改位置。未转载本地技能文件、真实审稿人画像或内部实验材料。

开头保留通用写法与规则索引；执行边界单独收录到 Codex skill与 `paperbank-writing` skill。规则由上述检查习惯及 `paper-introduction`、`clean-flow-figures`、`minimal-code-layout` 的通用要求重新表述；区分证据、记录和权限边界与可调整的写法。每条配原创中英教学例子，假设情境不是真实论文结果。未把特定项目的色板、尺寸、段落配额、固定连接词或禁用全部代词推广为通用学术规范。

公开 skill 由本项目独立编写，包含入口、生成的规则参考及许可；网页和 skill 参考从同一份章节数据生成，避免两套规则分叉。ZIP 不含私人 skill 原件、机器路径、论文源稿、真实审稿记录或第三方摘录。

## 公开参考与适用范围

- [Mensh & Kording (2017) · Ten simple rules for structuring papers](https://doi.org/10.1371/journal.pcbi.1005619)：中心贡献、读者视角与文章/段落结构；写法需要按研究取舍。
- [Rougier et al. (2014) · Ten Simple Rules for Better Figures](https://doi.org/10.1371/journal.pcbi.1003833)：根据读者与主要信息选择图型，检查布局、颜色及说明。
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

真实论文例子包含英文原文、中文翻译、逐句拆解及出处。需要迁移到自己的文章时，再给单独标注的教学改写；rebuttal 以模拟问题和模拟回复演示，不能当作真实审稿记录，也不表示作者已经补做实验。

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

`assets/flow-example.svg` 与 `assets/case-example.svg` 是原创教学示意图，展示信息布局，不模拟真实实验结果。

比格头像、全身形象与挥笔帧以作者提供的头像为参考，使用内置图像生成工具制作。挥笔 GIF 由生成的六个姿态统一尺度后编码；不是实拍。坐姿小狗沿用作者个人主页的原创吉祥物素材。素材为 `assets/beagle-logo.png`、`assets/beagle-pet.png`、`assets/beagle-wave.gif` 与 `assets/beagle-sitting.png`；按 CC BY 4.0 许可使用，保留作者与来源。

桌面伴侣源码在 `companion/`，实现采用 MIT；应用内上述素材仍采用 CC BY 4.0。

## 页面与语言

页面组织与表达受到 eternity4719 的[《高性价比人生指南》](https://eternity4719.github.io/HowToLiveBetter/)启发：按主题读、说清可执行动作、需要时再看说明。论文正文重新组织，页面实现独立编写，未转载原站生活建议或图片。

## 使用与转载

原创正文、提示词与教学图采用 [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)，原创代码采用 [MIT](https://opensource.org/license/mit)，详见 [LICENSE](LICENSE)。转载保留作者 Da1yuqin / PaperBank、原文链接及许可信息；改编注明改动。Star 不是许可条件。论文摘录、摘录译文与原图保留各自版权和许可；原创指南的授权不转授这些材料，复用时保留紧邻的论文出处与许可。

## checklist 怎么用

按当前稿件与任务选条目；勾选仅表示作者完成了这次检查，存在当前浏览器，不是外部审核结论。正文主要面向实证型 CS / AI 论文，不把一种文章的组织方法当作所有学科的硬性格式。

## 工具清单

工具与资源按项目公开页面、官方说明与 README 整理，核对日期为 2026-10-07。只链接原项目并用本指南文字说明用途，不转载第三方 README、SKILL、插件源码或配图。未逐项安装、测试效果或做安全审计；中英例子是使用情境，不代表实测输出。第三方工具按原项目许可使用，不纳入本指南的授权。

OpenClaw 的私人笔记只作为整理线索，公开页面链接官方文档。知乎文章以社区经验收录，不复述排名为客观结论；小红书去参入口未能显示笔记正文，相关绘图工具直接链接其 GitHub 仓库。使用公开入口，不保留社交分享参数、私人笔记地址或个人论文认领参数；Hugging Face 的日期页明确标为历史示例。

Lieflat Charts 的非商业许可、THU-PPT-Theme 的 CC BY-NC-SA 条件，以及 Edit Banana 的 README 与 LICENSE 不一致问题，均就近说明。工具“找到论文”与“论文支持正文论断”分开核验，自动报告不作为学术不端判定。

开源整理提示词由作者需求改写，限制在指定文件，区分注释翻译与可执行字符串、配置和路径改动；保留作者署名与许可，不把秘密原值写进报告，也不承诺只靠文字替换就完成去秘。


## 多来源例子

56 个原文例子来自八篇论文：PlanCraft、SAGE、GreenPlanner、EviNoteRAG、TCDiff、TCDiff++、WebFilter 和 CARD。每篇采用 4–8 处短引，按条目的写作问题选例子。原文、中文翻译与教学改写分别展示；终稿与所链公开预印本不同版本时就近说明。

UrbanZero 的 8 个例子依据作者公开主页仓库的项目介绍编写，仅为教学改写。公开介绍不能替代论文的实验记录；教学 RQ、对照与模拟回复不声称已经实施。skill 规则的 32 个双语例子仍为假设情境。

## 逐段逐句示范

29 组逐句示范包括 9 处真实论文短引，其余为明确标注的教学例句。真实短引沿用上面的出处、版本与位置，不把不同论文拼成同一篇文章；摘要或图注中的句子用于说明引言或方法写法时，标明实际来源位置。教学问答研究中的方法协议、200 道问题、72%→81% 支持率和 1.2→1.5 秒延迟均为假设，不是任何论文的实测结果。段落顺序展示论证任务，不规定固定段数；按领域、研究类型和投稿模板调整。

首页提示词按作者笔记的流程整理：先提纲与粗稿，再画图、人工精挑，最后通读全文精修。贡献修饰词例子对应已确认的写作要求：具体、正面、有事实依据；等量替换，不靠堆词增加篇幅。例句不声称描述任何已发表论文的事实。


## 四章结构与补充模板

起草、绘图、Refine、工具按作者提供的流程重新组织。全文表达要求、Related Work 和 Method Overview 等完整句式由 PaperBank 编写，方括号模板和改写均为教学示例，不是论文原文。原有 56 处短引保持原句与出处。公开 skill 同步包含全文规范和各章模板，不分发论文源稿或第三方原图。

Overleaf 本地 Git 同步的 Premium 权限与当前入口核对自 [Git integration](https://docs.overleaf.com/integrations-and-add-ons/git-integration-and-github-synchronization/git-integration)；无 Git 权限时的 ZIP 下载核对自 [Downloading a project](https://docs.overleaf.com/managing-projects-and-files/downloading-a-project)。

新版子刊图例对应 Bruno et al., *A universal framework for inclusive 15-minute cities*, Nature Cities 1, 633–641 (2024), [DOI](https://doi.org/10.1038/s44284-024-00119-4)。图 1、图 2 的内容与编码核对自作者的 [arXiv:2408.03794v1](https://arxiv.org/html/2408.03794v1)：颜色为 Gini，圆大小为人口密度；图 2b 为现有 POI 迁移比例。该预印本是 arXiv 非独占分发许可，出版社版本保留版权；本指南只链接原图并提供原创点评，不重新托管这两张图片。

## 绘图图例与逐图点评

图型拆分为 KDE、ECDF、PCA、雷达、置信带等；每条绘图要求链接对应的图例与中英拆解。KDE 是密度，ECDF 是累计比例；life2vec 正式图使用 PaCMAP，不称为 PCA。阴影和误差条的统计定义须看原图说明，不从外形推断置信水平。

重新核对 Notion 收藏中的 64 张图。公开版重现许可明确的 TCOD v3 图 1–6、InteractCS-RL v1 图 1–3，均从对应原 PDF 裁切，仅去掉周围页边，保留图内数据、文字和颜色，并署名、标示 CC BY 4.0 与裁切。图片中的角色图标不单独提取或重新授权。OneReason、ShoppingBench 和 life2vec 的图保留原文链接与原创点评。包含内部信息标记、账号水印、订单编号或匿名投稿材料的截图不公开；收藏在私人笔记中不自动意味着可转载。

标为“教学图”的统计图由 PaperBank 用固定模拟数据独立生成，只演示图型、读法和信息编码，不对应任何论文实验。绘图源码提供相对路径入口，数据和计算方法随源码公开；这些图与 Notion 原图明确区分。


## 评论与正文批注

复用作者个人主页的原创评论界面与批注脚本，沿用已有评论服务；PaperBank 的评论使用独立页面标识。公开批注显示所选正文和回复，私密留言仅由站点所有者查看。正文索引保留折叠及搜索隐藏内容，排除表单和按钮，保证筛选前后定位一致；引用点击可展开对应内容。未分发后台凭据或评论数据库。
