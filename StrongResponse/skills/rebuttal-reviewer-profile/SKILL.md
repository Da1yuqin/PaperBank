---
name: rebuttal-reviewer-profile
description: Infer evidence-grounded reviewer profiles and preferences from complete reviews, then simulate each reviewer's response to a rebuttal and run a targeted revision loop.
---

# 审稿人画像与模拟

独立分析审稿人，再按同一画像模拟审核回复。完整画像、刻板印象、投入表和 Revise loop 见 [rules.md](references/rules.md)，复制提示词见 [prompts.md](references/prompts.md)。

## 分析画像

读取论文、完整 review、评分和 Confidence、真实讨论。逐句提取 Weaknesses、Questions、Strengths、Summary、附录与评分理由里的信号，保留原话及位置。

1. 从 Weaknesses 和审稿文本逆推真正的核心关切，列出要求最高的问题。
2. 记录最欣赏的点、阅读深度与理解偏差、期待的 evidence、参与和改评信号、负面风险。
3. 逐项判断偏好：情绪价值和尊重、实验量和覆盖、背景知识与解释、技术细节和扫读习惯。低 Confidence 结合基础概念问题，可能意味着需要背景解释；也可能是论文没有讲清楚。
4. 每项附原话依据与不确定性。高分、客气不代表要求低；笑面虎优先级极高。每位审稿人都要完整回复，再按高、极大、中和极高分配额外投入。
5. 输出画像、原问题清单和模拟设置，作为 Rebuttal 起草与复核的输入；分类只供作者内部使用。

## 按画像模拟审核

写完回复后，先载入画像再进入审稿人角色。按画像设严格程度，拟合核心关切和要求最高的问题；实验导向查数据，情绪价值导向查是否被理解，背景解释导向查术语和中间推理。不要默认所有人都是同一种专家。

按原问题清单逐题带着疑问读 Rebuttal，定位答案与证据，检查实验分析、解释深度、语气、长度与扫读效果。输出：Q、原问题、画像关注点、回复位置、通过/不通过、具体原因、最小改法、缺失证据。

## Revise loop

把反馈交给独立的 Rebuttal skill 修改，再用同一画像和原问题清单审核。未通过就继续修改、复核；新 review 信息出现时才更新画像，不为通过而降低要求。所有问题得到明确回答，关键证据与分析到位，语气和解释深度符合画像后停止。

模拟反馈供作者自检，不能冒充真实认可或真实改分。需要实验或事实补充时交作者决定；不自动提交、改稿或运行实验。此 skill 不写 AC letter。

---

Da1yuqin / [StrongResponse](https://da1yuqin.github.io/StarPaper/StrongResponse/)，[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)。转载请保留署名、出处及许可，改写注明改动。
