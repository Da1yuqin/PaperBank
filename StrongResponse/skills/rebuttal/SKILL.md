---
name: rebuttal
description: Draft and revise per-reviewer conference rebuttals with numbered questions, answer-first responses, experiment analysis, targeted explanations and traceable evidence.
---

# Rebuttal

只负责逐题回复、追问与根据模拟意见修改。审稿人分析和模拟交给独立的 rebuttal-reviewer-profile，AC 信交给独立的 ac-letter。完整格式与模板见 [rules.md](references/rules.md)，复制提示词见 [prompts.md](references/prompts.md)。

## 输入与起草

读取论文、完整 review、已有结果与位置、当轮规定和作者授权范围。有画像时，将其核心关切、证据偏好和解释需求作为输入。

- 每位审稿人单独一份 Markdown。按原 review 顺序提取 Weaknesses、Questions、建议与评分理由的具体问题，一句话有多问就拆开。
- 问题标题固定为 `> **Q1.1: [忠于原意的问题标题]**`；子问用 Q1.1a、Q1.1b，保留编号关系。
- 第一句直接回答。是否题给 Yes/No 或不能判断，原因题给理由，流程题给操作，数值题给具体值。
- 随后给必要设置、真实证据和解释。每个实验都分析现象，回答审稿人的疑虑，联系对应创新点或贡献，最后给表号、节号或行号。
- 可比较的数据用紧凑表格，保留数值、设置、单位与范围；结果不利时如实报告，说明实际差异，不编造借口。
- 根据画像调节回复：实验需求用对应数据，背景需求用概念和 case，讨论需求认真展开；感谢具体、克制，放在相关解释后或文末，首句仍先回答。
- 每问一个清楚的回应，短句与短段落。承诺不是已完成结果；已有结果、阶段性证据与未来计划分别写清。

## 根据模拟反馈修改

接收 reviewer-profile skill 的 Q、画像关注点、回复位置、具体问题和最小改法；只修改不通过项。补回答、证据、实验分析、术语解释、表格或语气后，把新回复交回同一画像复核，直至每题通过。

不重新编造审稿人人设，不用自己写的检查清单替代原问题。缺数据就说明缺口，补实验和改论文另由作者决定；只编辑获授权的回复文件，不编造结果、引用、真实改分或已经完成的修改。提交另按作者授权执行。

---

Da1yuqin / [StrongResponse](https://da1yuqin.github.io/StarPaper/StrongResponse/)，[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)。转载请保留署名、出处及许可，改写注明改动。
