# PaperBank · 论文少走弯路指南

先讲清贡献，再交代证据。13 章、102 项 checklist、102 个中英双语例子，卡住了再展开看分析与原文。

[在线阅读](https://Da1yuqin.github.io/PaperBank/) · [写作 skill 下载](assets/paperbank-writing-skill.zip) · [写作铁律](https://Da1yuqin.github.io/PaperBank/#chapter-rules) · [Markdown 全文](book/guide.md) · [好用工具](https://Da1yuqin.github.io/PaperBank/#tools) · [来源说明](SOURCES.md) · [使用许可](LICENSE)

主要面向实证型 CS / AI 论文。包含 RQ、引言论证、方法与实验、图表、AI 写作提示词和 14 条审稿回应检查。普通条目简短，图表保留分析；62 项附九篇论文的英文摘录、中文翻译与拆解，覆盖 PlanCraft、SAGE、GreenPlanner、EviNoteRAG、TCDiff、TCDiff++、WebFilter、MindAligner 和 CARD，正式发表版与预印本分别注明。8 项用 UrbanZero 的公开项目介绍做中英教学改写，不作为论文原文。32 条写作铁律各配中英教学例子，假设情境单独标注。审稿回复为基于论文证据的模拟示范，不是真实审稿记录。网页支持搜索、章节筛选、本地勾选与深色模式。另附 23 项工具与资源，按阅读、画图、引用核验、代码阅读和论文维护分类；每项有中英使用例子，附保留程序行为的开源整理提示词。工具只核对公开说明，未逐项安装评测。

## PaperBank 写作 skill

[下载 ZIP](assets/paperbank-writing-skill.zip) · [查看 SKILL.md](skills/paperbank-writing/SKILL.md) · [32 条双语规则参考](skills/paperbank-writing/references/checklist.md)

解压后把整个 `paperbank-writing/` 文件夹交给 Codex，要求先读取 `SKILL.md`，再补上当前文件、任务和允许修改的范围。首页有中英使用提示词。按任务选规则，不需要每次执行全部清单。包内只有原创说明、教学例子和许可，不含论文源稿或第三方摘录。

## 欢迎来用，也欢迎带走

写论文、改论文、给 Codex 等工具做 skill，都欢迎。使用时选适合当前任务的条目，不必把整本变成每次写作的硬性规则。

原创正文、提示词与教学示意图采用 **CC BY 4.0**，原创代码采用 **MIT**。允许使用、改写与商业使用；转载或分享改编正文时，保留作者、原文链接和许可，改过请注明。知识可以搬家，门牌别摘。论文摘录、摘录译文与原图保留各自版权，不能随原创指南一并转授。复用例子时保留紧邻的论文出处与许可。

可直接使用的署名：

> 来源：Da1yuqin，《PaperBank · 论文少走弯路指南》，https://Da1yuqin.github.io/PaperBank/ ，CC BY 4.0。本文有修改。

觉得省了点力，欢迎顺手点个 **Star**，给这家论文银行攒点信用。Star 自愿，署名认真。

## 本地阅读与修改

Python 3 即可，无第三方依赖：

```sh
python3 run.py --serve
```

打开终端显示的地址。只重建网页与 Markdown，用 `python3 run.py`。

- `data/guide.json`：章节、checklist、分析、例子、参考与工具清单。
- `assets/`：模板、样式、交互、原创素材与标明出处的论文原图。
- `skills/paperbank-writing/SKILL.md`：skill 入口。
- `index.html`、`book/guide.md`、skill 参考与 ZIP：生成文件，修改内容后一起重建。

GitHub Pages 选择 `main` 分支根目录。页面组织与表达受到 eternity4719 的[《高性价比人生指南》](https://eternity4719.github.io/HowToLiveBetter/)启发，正文与代码独立编写。欢迎在 [Issues](https://github.com/Da1yuqin/PaperBank/issues)补充具体问题、改法与适用条件。
