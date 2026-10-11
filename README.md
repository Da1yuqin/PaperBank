# PaperBank

: 存入你的时间，取出你的 Accept

这里有三个可以直接使用的 skill：[cs-paper-writing](assets/cs-paper-writing-skill.zip)、[绘图](assets/paperbank-figures-skill.zip)、[rebuttal](assets/rebuttal-skill.zip)。按任务下载，解压后让 Codex 读取对应的 `SKILL.md`，填入材料、任务和允许修改的范围。

五章：起草、绘图、正文精修、Rebuttal、AI 工具。附中英例子、Related Work / Method Overview 完整模板和 Codex skill。

Intro、Related Work 与 Method 开头先读完整自然段，一例一段，中英可切换。高亮与旁批直接说哪里没对应、缺什么、为什么关键、怎么接；原文有不足也指出。句式与 LaTeX 模板保留在下方。Method 解释设计为何针对困难，Experiments 分析发现，Introduction 对应问题、设计与证据。先审核论证，再精修语言。

[在线阅读](https://da1yuqin.github.io/PaperBank/) · [cs-paper-writing](assets/cs-paper-writing-skill.zip) · [绘图 skill](assets/paperbank-figures-skill.zip) · [rebuttal skill](assets/rebuttal-skill.zip) · [Markdown 全文](book/guide.md) · [来源](SOURCES.md)

主要面向实证型 CS / AI 论文。逐句示范混合真实短引与明确标注的教学例句，不把不同论文拼成一篇文章。PlanCraft、SAGE、GreenPlanner、EviNoteRAG、TCDiff、TCDiff++、WebFilter、CARD 共提供 56 处短引和双语拆解；另有 UrbanZero 公开介绍的教学改写。Rebuttal 保留逐点回应例子，工具附中英使用情境。

## 给 Codex 用

[cs-paper-writing ZIP](assets/cs-paper-writing-skill.zip)：正文起草、章节模板、实验组织与语言精修。解压后读取 `cs-paper-writing/SKILL.md`。

绘图使用[绘图 skill ZIP](assets/paperbank-figures-skill.zip)：解压后让 Codex 读取 `paperbank-figures/SKILL.md`，附稿件、原始数据和参考图。包内有 mainfig / framework 区别、22 条绘图铁律、16 类图型及中英例子；图例链接回网页，不打包第三方原图。

[rebuttal ZIP](assets/rebuttal-skill.zip)：逐题回应、证据核对、revise loop 与 AC 总结。解压后读取 `rebuttal/SKILL.md`，不含真实审稿记录或审稿人画像。

保留完整文件夹，再说明材料、任务和允许修改的范围。三个包各有 `SKILL.md`、规则与中英模板、`references/prompts.md` 和 LICENSE，只分发通用规则、教学例子与公开来源，不含私人 skill 原件、论文源稿或第三方摘录。

提示词统一维护在 `data/guide.json` 的 `codex_prompts`，网页与对应下载包同步生成。起草、精修、实验、Intro 属于写作包；绘图与 rebuttal 分别独立。开源代码整理提示词保留在网页工具章节。

## 使用与转载

欢迎使用、改写、转载，也欢迎拿去做 skill。原创正文采用 [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)，代码采用 MIT；转载保留作者、原文链接和许可，改过请注明。论文摘录和原图保留各自版权，复用前查紧邻的出处与许可。

如有帮助，欢迎 Star。

> 来源：Da1yuqin，《PaperBank》，https://da1yuqin.github.io/PaperBank/ ，CC BY 4.0。本文有修改。

## 本地预览

Python 3 即可，无第三方依赖：

```sh
python3 run.py --serve
```

只重建用 `python3 run.py`。内容在 `data/guide.json`；模板、样式和交互在 `assets/`。网页、Markdown、skill 参考与 ZIP 从同一份数据生成，修改后一起重建。网页支持搜索、章节目录和深色模式；选中正文可留批注，公开批注显示高亮和侧栏，也可私密留言。

GitHub Pages 选择 `main` 分支根目录。组织与表达受到 eternity4719 的[《高性价比人生指南》](https://eternity4719.github.io/HowToLiveBetter/)启发，正文与代码独立编写。欢迎在 [Issues](https://github.com/Da1yuqin/PaperBank/issues)补充具体问题和改法。
