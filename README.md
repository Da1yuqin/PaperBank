# PaperBank · 论文怎么写

五章：粗稿、绘图、正文精修、Rebuttal、AI 工具。附中英例子、Related Work / Method Overview 完整模板和 Codex skill。

[在线阅读](https://da1yuqin.github.io/PaperBank/) · [写作 skill](assets/paperbank-writing-skill.zip) · [Markdown 全文](book/guide.md) · [工具](https://da1yuqin.github.io/PaperBank/#tools) · [来源](SOURCES.md)

主要面向实证型 CS / AI 论文。逐句示范混合真实短引与明确标注的教学例句，不把不同论文拼成一篇文章。PlanCraft、SAGE、GreenPlanner、EviNoteRAG、TCDiff、TCDiff++、WebFilter、CARD 共提供 56 处短引和双语拆解；另有 UrbanZero 公开介绍的教学改写。Rebuttal 保留逐点回应例子，工具附中英使用情境。

## 给 Codex 用

[下载 skill ZIP](assets/paperbank-writing-skill.zip)，解压后让 Codex 读取整个 `paperbank-writing/` 文件夹，再说明当前文件、任务和允许修改的范围。包内只有原创规则、教学例子和许可，不含论文源稿或第三方摘录。

## 使用与转载

欢迎使用、改写、转载，也欢迎拿去做 skill。原创正文采用 [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)，代码采用 MIT；转载保留作者、原文链接和许可，改过请注明。论文摘录和原图保留各自版权，复用前查紧邻的出处与许可。

知识可以搬家，门牌别摘。觉得省了点力，欢迎 Star；本银行只收星，不收版面费。

> 来源：Da1yuqin，《PaperBank · 论文怎么写》，https://da1yuqin.github.io/PaperBank/ ，CC BY 4.0。本文有修改。

## 本地预览

Python 3 即可，无第三方依赖：

```sh
python3 run.py --serve
```

只重建用 `python3 run.py`。内容在 `data/guide.json`；模板、样式和交互在 `assets/`。网页、Markdown、skill 参考与 ZIP 从同一份数据生成，修改后一起重建。网页支持搜索、章节目录和深色模式；选中正文可留批注，公开批注显示高亮和侧栏，也可私密留言。

GitHub Pages 选择 `main` 分支根目录。组织与表达受到 eternity4719 的[《高性价比人生指南》](https://eternity4719.github.io/HowToLiveBetter/)启发，正文与代码独立编写。欢迎在 [Issues](https://github.com/Da1yuqin/PaperBank/issues)补充具体问题和改法。
