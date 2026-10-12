# StarPaper

要把论文像明星一样包装起来。

开源论文写作与学术绘图指南，附可直接用于 Codex 的 `cs-paper-writing` 写作 skill 和 `starpaper-figures` 绘图 skill。

Open-source **CS paper writing and academic figure drawing skills for Codex**, with section templates, annotated paragraphs, main figures, framework diagrams, and LaTeX figures and tables.

[阅读 StarPaper](https://da1yuqin.github.io/StarPaper/) · [下载写作 skill](assets/cs-paper-writing-skill.zip) · [下载绘图 skill](assets/starpaper-figures-skill.zip)

论文绘图分 Mainfig、Framework、实验绘图三节，每节两个模板例子，附优化前后对照；其他图集中在文末参考绘图附录。

章节先给原则，再给完整模板或段落批注；方括号填写自己的材料。StarPaper 的真实论文摘录与原图附出处、版本和许可。

## 论文写作与学术绘图 skills

写作 ZIP 解压后保留全部九个同级目录，让 Codex 先读 `cs-paper-writing/SKILL.md`，再按任务加载共享规则和对应章节；不用一次读完全部模板。其他 ZIP 保留各自完整文件夹。再给材料、任务和允许修改的范围。

| Skill | 用途 | 源码与下载 |
| --- | --- | --- |
| `cs-paper-writing` · CS paper writing | 摘要与引言、相关工作、方法、实验、图表和全文整合；按章节加载规则与模板。 | [SKILL.md](skills/cs-paper-writing/SKILL.md) · [写作 ZIP](assets/cs-paper-writing-skill.zip) |
| `starpaper-figures` · Academic figure drawing | mainfig、framework、案例图和统计图；核对真实输入输出、字号、配色、Caption 与最终 PDF。 | [SKILL.md](skills/starpaper-figures/SKILL.md) · [绘图 ZIP](assets/starpaper-figures-skill.zip) |

两个下载包 latest:【2026-10-13 00:38】。第三方论文原图不随包分发。

制作类似网页可使用[教程编排 skill](assets/tutorial-authoring-skill.zip)：按操作顺序组织内容，用完整案例和对应批注讲解。

下载包仅含通用规则和教学材料，不包含私人 skill 原件、论文源稿或真实审稿记录。

## 本地预览

Python 3 即可，无第三方依赖：

```sh
python3 run.py --serve
```

打开 `http://127.0.0.1:8000/`。只重建用 `python3 run.py`。

正文数据在 `data/guide.json`；模板、样式和交互在 `assets/`。构建同时生成网页、Markdown 和三个 skill ZIP。网页支持搜索、目录、深色模式、评论、正文批注、共享点赞数和页面浏览次数。统计从启用后累计，同一浏览器可点赞或取消。GitHub Pages 使用 `main` 分支根目录。

[StarPaper Markdown](book/guide.md) · [来源说明](SOURCES.md) · [勘误与补充](https://github.com/Da1yuqin/StarPaper/issues)

## 使用与转载

欢迎使用、改写、转载，也欢迎拿去做 skill。原创正文和提示词采用 [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)，原创代码采用 MIT。转载保留作者、原文链接和许可，改过请注明。论文摘录、原图及第三方软件保留各自版权。

如有帮助，欢迎 Star。

组织与表达受到 eternity4719 的[《高性价比人生指南》](https://eternity4719.github.io/HowToLiveBetter/)启发，正文与代码独立编写。
