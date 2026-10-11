# PaperBank

: 存入你的时间，取出你的 Accept

这里有三个可以直接使用的 skill：[cs-paper-writing](assets/cs-paper-writing-skill.zip)、[绘图](assets/paperbank-figures-skill.zip)、[rebuttal](assets/rebuttal-skill.zip)。按任务下载，解压后让 Codex 读取对应的 `SKILL.md`，填入材料、任务和允许修改的范围。

五章：初稿准备、论文绘图、正文精修、审稿回复、辅助工具。正文精修先读本节原则，再看整段批注；其他章节集中给操作要求、图例和模板。

初稿准备分为研究材料与模板、正文结构与实验两节。Mainfig 和 framework 集中放在论文绘图章开头，由作者审核逻辑并人工精修；统计图随后用 Python 从真实数据绘制。大纲图展示章节目的、方法的输入输出和 Overview；正文精修按论文顺序讲解。Related Work 用 However 说明局限，紧接对应解法。引言对应图将问题、局限、设计、发现和适用范围连到正文，再由实验结果回写摘要与引言。

[在线阅读](https://da1yuqin.github.io/PaperBank/) · [cs-paper-writing](assets/cs-paper-writing-skill.zip) · [绘图 skill](assets/paperbank-figures-skill.zip) · [rebuttal skill](assets/rebuttal-skill.zip) · [Markdown 全文](book/guide.md) · [来源](SOURCES.md)

主要面向实证型 CS / AI 论文。整段原文附出处；教学改写与审稿回复模板另行标注。原图保留数据、标签及许可，说明集中解释坐标、对照、流程和结论范围。

## 给 Codex 用

[cs-paper-writing ZIP](assets/cs-paper-writing-skill.zip)：正文起草、章节模板、实验组织与语言精修。解压后读取 `cs-paper-writing/SKILL.md`。

绘图使用[绘图 skill ZIP](assets/paperbank-figures-skill.zip)：解压后让 Codex 读取 `paperbank-figures/SKILL.md`，附稿件、原始数据和参考图。包内有 mainfig / framework 区别、22 条绘图铁律、16 类图型及中英例子；图例链接回网页，不打包第三方原图。

[rebuttal ZIP](assets/rebuttal-skill.zip)：逐题回应、证据核对、revise loop 与 AC 总结。解压后读取 `rebuttal/SKILL.md`，不含真实审稿记录或审稿人画像。

保留完整文件夹，再说明材料、任务和允许修改的范围。三个包各有 `SKILL.md`、规则与中英模板、`references/prompts.md` 和 LICENSE，只分发通用规则、教学例子与公开来源，不含私人 skill 原件、论文源稿或第三方摘录。

提示词统一维护在 `data/guide.json` 的 `codex_prompts`，网页默认只展示中文提示词，下载包保留中英版本。起草、精修、实验、Intro 属于写作包；绘图与 rebuttal 分别独立。开源代码整理提示词保留在网页工具章节。

## 使用与转载

欢迎使用、改写、转载，也欢迎拿去做 skill。原创正文采用 [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)，代码采用 MIT；转载保留作者、原文链接和许可，改过请注明。论文摘录和原图保留各自版权，复用前查紧邻的出处与许可。

如有帮助，欢迎 Star。

> 来源：Da1yuqin，《PaperBank》，https://da1yuqin.github.io/PaperBank/ ，CC BY 4.0。本文有修改。

## 本地预览

Python 3 即可，无第三方依赖：

```sh
python3 run.py --serve
```

只重建用 `python3 run.py`。内容在 `data/guide.json`；模板、样式和交互在 `assets/`。网页与 Markdown 使用 `tutorial_layout` 集中组织案例；公共 skill 使用既有通用规则。三个下载包保留原有内容。修改后运行构建。网页支持搜索、章节目录和深色模式；选中正文可留批注，公开批注显示高亮和侧栏，也可私密留言。

GitHub Pages 选择 `main` 分支根目录。组织与表达受到 eternity4719 的[《高性价比人生指南》](https://eternity4719.github.io/HowToLiveBetter/)启发，正文与代码独立编写。欢迎在 [Issues](https://github.com/Da1yuqin/PaperBank/issues)补充具体问题和改法。
