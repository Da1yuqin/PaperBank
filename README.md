# BeautyPaper & StrongResponse

两份教程，按任务选：

- [BeautyPaper](https://da1yuqin.github.io/PaperBank/)：初稿准备、论文绘图、正文精修、辅助工具。
- [💪StrongResponse【这边也长出肌肉】](https://da1yuqin.github.io/PaperBank/StrongResponse/)：整理审稿问题、逐题回复、四类回答模板、revise loop、追问与 AC 总结。

两个网页开头互相链接。章节先给原则，再给完整模板或段落批注；方括号填写自己的材料。BeautyPaper 的真实论文摘录与原图附出处、版本和许可；StrongResponse 只使用原创教学模板。

## 给 Codex 用

写作 ZIP 解压后保留全部八个同级目录，让 Codex 先读 `cs-paper-writing/SKILL.md`，再按任务加载共享规则和对应章节；不用一次读完全部模板。其他 ZIP 保留各自完整文件夹。再给材料、任务和允许修改的范围。

- [cs-paper-writing ZIP](assets/cs-paper-writing-skill.zip)：写作入口、共享规则和六个章节 skill（摘要与引言、相关工作、方法、实验、图表、全文整合）。更新于 2026-10-12。
- [绘图 ZIP](assets/paperbank-figures-skill.zip)：mainfig / framework、绘图铁律、图型和提示词；第三方原图不随包分发。
- [rebuttal ZIP](assets/rebuttal-skill.zip)：`Q1.1` 编号、首句回答、证据定位、逐题检查和 AC 总结。模板与 StrongResponse 使用同一份公开内容。

制作类似网页可使用[教程编排 skill](assets/tutorial-authoring-skill.zip)：按操作顺序组织内容，用完整案例和对应批注讲解。

下载包仅含通用规则和教学材料，不包含私人 skill 原件、论文源稿或真实审稿记录。

## 本地预览

Python 3 即可，无第三方依赖：

```sh
python3 run.py --serve
```

打开 `http://127.0.0.1:8000/` 或 `http://127.0.0.1:8000/StrongResponse/`。只重建用 `python3 run.py`。

BeautyPaper 内容在 `data/guide.json`，StrongResponse 在 `data/response.json`；模板、样式和交互在 `assets/`。构建同时生成两个网页、两份 Markdown 和四个 skill ZIP。网页支持搜索、目录、深色模式、评论和正文批注；两页批注分别保存。GitHub Pages 使用 `main` 分支根目录。

[BeautyPaper Markdown](book/guide.md) · [StrongResponse Markdown](book/response.md) · [来源说明](SOURCES.md) · [勘误与补充](https://github.com/Da1yuqin/PaperBank/issues)

## 使用与转载

欢迎使用、改写、转载，也欢迎拿去做 skill。原创正文和提示词采用 [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)，原创代码采用 MIT。转载保留作者、原文链接和许可，改过请注明。论文摘录、原图及第三方软件保留各自版权。

如有帮助，欢迎 Star。

组织与表达受到 eternity4719 的[《高性价比人生指南》](https://eternity4719.github.io/HowToLiveBetter/)启发，正文与代码独立编写。
