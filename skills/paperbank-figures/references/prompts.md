# 给 Codex 的提示词

填写【】后使用。以下采用本地技能中适用于实证型 CS 论文的通用规则；不套用某篇论文的固定宽度、色值、模型阵容或重复次数。Nature 系列使用独立体系。


<a id="figures"></a>
## 给 Codex 的绘图说明单

依据：paper-visual-standards · academic-plotting · clean-flow-figures。

对应规则：最终宽度和统一字号；输入、输出与评价边界；案例全文唯一使用；统计图的真实数据与自解释；Caption、顶部浮动与最终 PDF 验收。

### 中文

```text
读取 paperbank-figures/SKILL.md 和 references/rules.md。按以下材料画图。
图型：【mainfig／framework／统计图／案例图】
要突出的问题与贡献：【对应 Intro 的哪项困难，方法改了什么，依据在哪里】
材料：【稿件、真实数据、参考图与出处、已有案例及使用位置】
真实结构：【输入、操作、输出、接收者；并行、汇合、反馈；训练／推理／评价】
允许修改：【文件与范围】；最终插入宽度：【mm】
正文 PDF 实测字体与字号：【字体，pt】；本篇已确认色板：【】

铁律：
1. mainfig 讲问题、已有缺口与关键改动，默认不超过 5 个环节；framework 先让人看懂设计为什么好，再画完整输入、操作与产物。两图分别承担不同叙述任务。
2. 每条箭头对应真实依赖，不穿文字。保留并行与反馈；训练、推理、评价分开。输入、输出、评价规则用三种边框并给图例；仅供评价的信息不能画成模型输入。
3. 按最终宽度起稿。所有标题、坐标、刻度、图例、数字、注释用同一字号，正文减 2 pt ≤ 图字 ≤ 正文，字体家族匹配。放不下就重排或拆图，不缩小规定字号、不进行非等比缩放、不修改论文模板。
4. 白底、近白面板、深色文字、低饱和配色。同一对象全篇同色，用形状或线型辅助区分；不加渐变、阴影和装饰光效。通栏先参考 16:9，单栏参考 4:3，内容与可读性优先。
5. 模块名与正文一致。缩写、变量、单位、图标、颜色和线型都能解释；图标旁写对象名。标签用自然语言，不用符号拼句。
6. 同一案例全文只呈现一次，翻译、裁剪或改名仍算同一个。先按来源核对使用位置，其他位置交叉引用。对话一轮一框；作者示例与实测回复分清，没有评分不画勾。
7. 统计图用 Python 等专业工具读取所附数据，保留数值、坐标几何、分母、单位与 SD／SE／CI 定义；同类比较统一尺度。不为美观补缺测、改数据或平滑曲线，不重跑实验；KDE 等估计图说明样本量、方法和带宽。概念图按当前环境使用 imagegen，生成内容须依据已确认流程，不生成虚构结果。
8. Caption 说明读法、比较、必要口径与实际发现，简称在本条 Caption 写全称。方法图说明机制，不编实验结论。尽量三行，必要定义与事实边界优先。
9. PDF 文字可见、可选，字体嵌入；不叠两套字形或隐藏 OCR。统计图优先矢量 PDF，含位图的 PDF 不称全矢量。CS 图表默认 [!t]，实际位置跟随正文首次引用，保留附录归属。
10. 先给问题、布局和缺口，再绘制。插回论文编译，看最终页面的字号、图例、裁切、碰撞和引用顺序。交付源文件、PDF、预览及实际检查结果。只改色时保留原布局、文字、连线与图片；保留他人修改，不扩大范围。
```

### English

```text
Read paperbank-figures/SKILL.md and references/rules.md. Draw from these materials.
Type: [main figure / framework / quantitative chart / case]
Problem and contribution: [Introduction challenge, actual design change, evidence]
Materials: [manuscript, original data, references and sources, cases and their existing locations]
Actual structure: [inputs, operations, outputs, recipients; parallel paths, merges, feedback; training / inference / evaluation]
Editable files and scope: [ ]; final insertion width: [mm]
Font family and body size measured in the manuscript PDF: [family, pt]; approved palette: [ ]

Hard rules:
1. The main figure shows the problem, existing gap, and key change, with at most five stages by default. The framework explains why the design addresses the challenge before showing inputs, operations, and products. Give the two figures distinct jobs.
2. Every arrow represents an actual dependency and avoids text. Preserve parallel paths and feedback; separate training, inference, and evaluation. Use three explained border encodings for inputs, outputs, and evaluation criteria. Evaluation-only information must not appear as model input.
3. Design at the final width. Use one size for titles, axes, ticks, legends, numbers, and annotations: body size minus 2 pt ≤ figure text ≤ body size, with a matching font family. Rearrange or split crowded content; do not shrink text, distort geometry, or change the paper template.
4. Use a white canvas, near-white panels, dark text, and muted colors. Keep each object's color consistent throughout the paper; add shapes or line styles. Avoid gradients, shadows, and decorative glow. Start near 16:9 for full-width figures and 4:3 for single-column figures; prioritize content and readability.
5. Match module names to the body. Explain abbreviations, variables, units, icons, colors, and line styles; label icons with object names. Use natural-language labels rather than symbol-packed prose.
6. Present each source case only once across the paper. Translations, crops, and renamed versions still count as the same case. Check existing locations by source and cross-reference elsewhere. Use one frame per dialogue turn. Distinguish author examples from measured outputs; do not show unrecorded check marks.
7. Use Python or equivalent professional plotting tools for supplied quantitative data. Preserve values, coordinate geometry, denominators, units, and SD / SE / CI definitions; use common scales for comparable plots. Do not fill missing measurements, alter data, or smooth curves for appearance, and do not rerun experiments. For KDE and other estimated plots, specify sample counts, methods, and bandwidth where applicable. Use imagegen for conceptual figures in the current environment; do not let a generator invent dependencies or results.
8. Captions explain reading, comparisons, necessary scope, and actual findings. Expand abbreviations in each caption. Method figures explain mechanisms without fabricated experimental conclusions. Aim for three final lines; necessary definitions and factual limits take priority.
9. Use visible, selectable PDF text and embedded fonts; avoid duplicate lettering and hidden OCR. Prefer vector PDF for statistical plots; a PDF containing raster images is not fully vector. Use [!t] for CS figures and tables by default. Verify actual order against first body citations and retain appendix ownership.
10. Propose the question, layout, and evidence gaps before drawing. Insert the figure into the paper, compile, and inspect final-size text, legends, crops, collisions, and citation order. Deliver sources, PDF, preview, and completed checks. A color-only edit preserves layout, text, edges, and images. Preserve concurrent edits and the authorized scope.
```

---

Da1yuqin / PaperBank，[原文](https://da1yuqin.github.io/PaperBank/)，[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)。
