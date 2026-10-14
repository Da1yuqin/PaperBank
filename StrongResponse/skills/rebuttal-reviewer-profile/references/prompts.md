# 审稿人画像与模拟 · 提示词

```text
读取 rebuttal-reviewer-profile/SKILL.md。完整 reviews：【】；评分与 Confidence：【】；论文：【】；二轮讨论：【】。先逐句提取 Weaknesses、Questions、Strengths、Summary 和评分理由，保留原话位置。建立每位审稿人的画像与投入表，逆推核心关切、情绪价值、实验量、背景解释与细节偏好；每项附原话依据，未知写未知。指出要求最高的问题、期待的回应和模拟严格程度。没有回复时先交付画像；已有 Rebuttal 时，再按画像逐题模拟审核，给出具体反馈，交给 Rebuttal skill 修改后重查。
```

## Revise loop

```text
运行 Revise loop。
论文：【】；完整 review：【】；第一部分的审稿人画像与偏好表：【】；当前 Rebuttal：【】；真实证据：【】；当轮规则和允许修改的文件：【】。

1. 读取 rebuttal-reviewer-profile skill，按画像扮演每位审稿人。依据原话设严格程度，重点拟合其核心关切、最高要求的问题、情绪价值、实验量、背景解释及扫读习惯。
2. 按原 review 的问题清单逐题审核回复。输出：Q｜原问题｜画像关注点｜回复位置｜通过/不通过｜原因｜最小改法｜缺失证据。
3. 读取 rebuttal skill，依据反馈只修改不通过项；不编造结果，不自动跑实验或改论文。
4. 用同一画像、原问题清单和反馈重新审核修改后的回复。未通过则再次修改、再次审核。只有新的 review 或讨论改变依据时才更新画像。
5. 所有问题都有明确回应，关键证据与实验分析到位，语气、长度和解释深度符合这位审稿人的要求后停止。

最终交付：每位审稿人的可复制 Rebuttal、作者内部的复核记录，以及需要作者决定的证据缺口。模拟意见和通过结果不粘入正式回复。
```

---

Da1yuqin / [StrongResponse](https://da1yuqin.github.io/StarPaper/StrongResponse/)，[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)。转载请保留署名、出处及许可，改写注明改动。
