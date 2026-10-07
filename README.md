# PaperBank · 论文少走弯路指南

先讲清贡献，再交代证据。12 章、70 项 checklist、50 个例子，卡住了再展开看分析与原文。

[在线阅读](https://Da1yuqin.github.io/PaperBank/) · [Markdown 全文](book/guide.md) · [来源说明](SOURCES.md) · [使用许可](LICENSE)

主要面向实证型 CS / AI 论文。包含 RQ、引言论证、方法与实验、图表、AI 写作提示词和 14 条审稿回应检查。普通条目简短，图表保留分析；例子明确区分教学假设与真实论文。网页支持搜索、章节筛选、本地勾选与深色模式。

## 欢迎来用，也欢迎带走

写论文、改论文、给 Codex 等工具做 skill，都欢迎。使用时选适合当前任务的条目，不必把整本变成每次写作的硬性规则。

原创正文、提示词与教学示意图采用 **CC BY 4.0**，原创代码采用 **MIT**。允许使用、改写与商业使用；转载或分享改编正文时，保留作者、原文链接和许可，改过请注明。知识可以搬家，门牌别摘。第三方论文与外链保留自己的许可。

可直接使用的署名：

> 来源：Da1yuqin，《PaperBank · 论文少走弯路指南》，https://Da1yuqin.github.io/PaperBank/ ，CC BY 4.0。本文有修改。

觉得省了点力，欢迎顺手点个 **Star**，给这家论文银行攒点信用。Star 自愿，署名认真。

## 比格行长 · 贝果

个人主页同款小比格，换上写作台词。网页右下角摸摸它，听一句笑话或写作提醒；累了让它休息，想它再叫醒。

[头像 PNG](assets/beagle-logo.png) · [全身 PNG](assets/beagle-pet.png) · [挥笔 GIF](assets/beagle-wave.gif) · [macOS 桌面伴侣](assets/beagle-desktop.zip) · [桌伴源码与构建](companion/README.md)

吉祥物以作者头像为参照，使用图像生成工具制作；素材可按 CC BY 4.0 使用，保留出处。桌面伴侣是可选的小浮窗。

## 本地阅读与修改

Python 3 即可，无第三方依赖：

```sh
python3 run.py --serve
```

打开终端显示的地址。只重建网页与 Markdown，用 `python3 run.py`。

- `data/guide.json`：章节、checklist、分析、例子与参考。
- `assets/`：模板、样式、交互与原创教学图。
- `index.html`、`book/guide.md`：生成文件，修改内容后一起重建。

GitHub Pages 选择 `main` 分支根目录。页面组织与表达受到 eternity4719 的[《高性价比人生指南》](https://eternity4719.github.io/HowToLiveBetter/)启发，正文与代码独立编写。欢迎在 [Issues](https://github.com/Da1yuqin/PaperBank/issues)补充具体问题、改法与适用条件。
