# 给 Codex 的提示词

填写【】后使用，适用于实证型 CS 论文。宽度、色值、模型与重复次数按本篇确定。Nature 系列使用独立体系。


<a id="figures"></a>
## 绘图提示词

依据：paper-visual-standards · academic-plotting · clean-flow-figures。

对应规则：最终宽度和统一字号；输入、输出与评价边界；案例全文唯一使用；统计图的真实数据与自解释；Caption、顶部浮动与最终 PDF 验收。

### 中文

```text
读取 starpaper-figures/SKILL.md 和 references/rules.md。
核对会议及 track 的 AI 规定，按要求披露。
确认材料权限及工具的数据处理方式。
未经许可，不上传未公开稿件、review、个人数据或密钥。
图型：【mainfig／framework／统计图／案例图】
问题与贡献：【Intro 中的困难、方法改动及依据】
材料：【稿件、真实数据、参考图出处、案例使用位置】
结构：【输入、操作、输出、接收者；并行、汇合、反馈】
阶段：【训练／推理／评价】；允许修改：【】
最终宽度：【mm】；正文实测字体与字号：【字体，pt】
已确认色板：【】

铁律：
1. mainfig 讲问题、缺口与关键改动，默认最多 5 个环节。
   framework 讲设计为何有效，再画输入、操作和产物。
2. 箭头表示真实依赖，不穿文字。
   保留并行与反馈，训练、推理、评价分开。
   输入、输出、评价用三种边框，附图例。
   仅供评价的信息不能画成模型输入。
3. 按最终宽度起稿，所有图中文字用同一字号。
   正文减 2 pt ≤ 图字 ≤ 正文，字体家族匹配。
   放不下就重排或拆图，不缩字号或非等比缩放。
   不改论文模板。
4. 白底、近白面板、深色文字、低饱和配色。
   同一对象全篇同色，形状或线型辅助区分。
   不加渐变、阴影或光效。
   通栏参考 16:9，单栏参考 4:3，可读性优先。
5. 模块名与正文一致，图标旁标对象名。
   每图解释自身的简称、变量、单位和视觉编码。
   标签用自然语言，颜色说明点明对象。
6. 同一案例全文只呈现一次，其他位置交叉引用。
   翻译、裁剪、改名仍算同一案例，先查来源与位置。
   对话一轮一框，具体条件对应困难。
   作者示例与实测回复分开，无评分不画勾。
   评分通过不写成真实执行。
7. 统计图用 Python 等工具读取所附真实数据。
   保留数值、坐标几何、分母、单位及 SD／SE／CI 定义。
   同类比较统一尺度。不为美观补缺测、改数据或平滑曲线。
   不重跑实验。
   KDE 等估计图注明样本量、方法和带宽。
   概念图按环境使用 imagegen，只画已确认流程。
   不生成虚构结果。
8. Caption 先定位，再解释标记，按读序带读。
   本条 Caption 展开简称。
   最后给有证据的发现与贡献意义。
   方法图解释机制，不编实验结论。
   尽量三行，定义与事实边界优先。
   单项判定用 \footnote，复用用 \footref。
   跨栏脚注可用 savenotes，检查落页与跳转。
9. PDF 文字可见、可选，字体嵌入。
   不叠两套字形或隐藏 OCR。
   统计图优先矢量 PDF，含位图不称全矢量。
   CS 图表默认 [!t]，位置跟随正文首次引用。
   移到附录时同步详解、Overview 和引用。
10. 先交问题、布局和证据缺口，再绘制。
    插回论文检查字号、图例、裁切、碰撞与引用顺序。
    交付源文件、PDF、预览及实际检查结果。
    只改色时保留布局、文字、连线与图片。
    显示改名不改冻结记录，保留他人修改与授权边界。
```

### English

```text
Read starpaper-figures/SKILL.md and references/rules.md. Draw from these materials.
Before use: check the AI policy for the target venue and track, stay within the permitted drafting, editing, and figure-generation scope, and disclose use as required. Confirm material permissions and the tool’s data-handling practices; do not send unpublished manuscripts, reviews, personal data, or credentials to external services without permission.
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
8. Captions identify the figure, explain necessary marks and terms, follow the actual panel order, and end with evidenced findings and contribution. Include necessary comparisons and scope. Expand abbreviations in each caption. Method figures explain mechanisms without fabricated experimental conclusions. Aim for three final lines; necessary definitions and factual limits take priority.
9. Use visible, selectable PDF text and embedded fonts; avoid duplicate lettering and hidden OCR. Prefer vector PDF for statistical plots; a PDF containing raster images is not fully vector. Use [!t] for CS figures and tables by default. Verify actual order against first body citations and retain appendix ownership.
10. Propose the question, layout, and evidence gaps before drawing. Insert the figure into the paper, compile, and inspect final-size text, legends, crops, collisions, and citation order. Deliver sources, PDF, preview, and completed checks. A color-only edit preserves layout, text, edges, and images. Preserve concurrent edits and the authorized scope.
Define each figure’s abbreviations locally, match concrete case conditions to challenges, and name the objects connected by colors. Keep shared reading guidance in captions and use \footnote and \footref for item-specific notes; savenotes can support full-width floats, with page and link checks. Passing an evaluation does not mean successful execution. When moving figures to the appendix, update explanations, overviews, and references. Display-name changes must preserve frozen records.
```

---

Da1yuqin / StarPaper，[原文](https://da1yuqin.github.io/StarPaper/)，[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)。
