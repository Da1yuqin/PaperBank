# 给 Codex 的提示词

填写【】后使用。材料权限、证据与当轮回复规定先确认；不附真实审稿记录，不推测审稿人身份或评分变化。


<a id="rebuttal"></a>
## Rebuttal + revise loop

依据：rebuttal · rebuttal-reviewer-simulator（通用证据核查规则）。

对应规则：原始问题逐条覆盖；事实来源与承诺边界；每问首句结论与精简表格；revise loop 与 AC 总结。

### 中文

```text
读取 rebuttal/SKILL.md 和 references/rules.md。
使用前：核对目标会议及 track 的 AI 规定，只在允许范围内起草、改写或绘图，按要求披露。确认材料使用权限和工具的数据处理方式；未获许可，不向外部服务上传未公开稿件、review、个人数据或密钥。
材料：【论文、完整 review、当前回复、已验证补充结果】
会议当轮规则：【字数／字符限制、补实验／链接／修订稿／AI 使用规定】
阶段：【初次／追问】；允许修改：【回复文件与范围】

1. 先保留 review 原文，逐条拆出 Summary、Weaknesses、Questions、建议和评分理由里的具体关切；Strengths 记录已认可点。列“原问题→需要的证据→现有依据与位置→缺口”，不按回复现有顺序漏问，不猜审稿人动机或水平。
2. 每问首句直接回答，随后给证据、解释和位置；问题标题忠于原意，感谢简短。数据、对照或成本适合表格就用紧凑表格，保留必要比较条件、数值口径与范围，不用文字重复每格。
3. 每个事实回到论文、原 review、真实结果或已确认推导。合理批评就承认并改，争议就查前提与证据；不隐藏影响比较的条件。补实验的承诺不能替代结果；缺结果交给我决定，不编数字、不把 future work 写成已完成，不自动跑实验或提交回复。
4. 执行 revise loop：按原问题清单查“原问题→回复位置→是否回答→证据是否匹配→剩余疑问→最小改法→还缺什么”。先修漏答、证据与逻辑，再压文字、调语气。只改不通过项，改后重查同一张清单，不盲目重跑全部基线。
5. 所有问题明确覆盖、事实与证据对应、逻辑通顺、长度和当轮政策合规后停止，由我定稿。证据不足就交回缺口，不通过模拟预测评分变化或录用。
6. 追问轮只答新增关切；AC 总结写关键问题、回应、证据与限制，不请求提分或接收。英文回复逐段附中文供我审，内部检查和缺口不混入提交文本。
```

### English

```text
Read rebuttal/SKILL.md and references/rules.md.
Before use: check the AI policy for the target venue and track, stay within the permitted drafting, editing, and figure-generation scope, and disclose use as required. Confirm material permissions and the tool’s data-handling practices; do not send unpublished manuscripts, reviews, personal data, or credentials to external services without permission.
Materials: [paper, complete reviews, current response, verified supplementary results]
Current venue rules: [word / character limit; experiments, links, revised PDFs, and AI-use policies]
Stage: [initial / follow-up]; editable response files and scope: [ ].

1. Preserve raw reviews. Extract each concrete concern from Summary, Weaknesses, Questions, suggestions, and scoring reasons; record acknowledged strengths. Map original question → required evidence → available evidence and location → gap. Follow original questions rather than the response's order; do not infer reviewer motives or competence.
2. Answer each question in the first sentence, then give evidence, explanation, and location. Keep question headings faithful and thanks brief. Use compact tables for suitable results, comparisons, or costs, retaining necessary conditions, definitions, and scope. Do not repeat every cell in prose.
3. Ground each fact in the paper, review, actual results, or confirmed derivations. Acknowledge and repair valid criticisms; check disputed premises against evidence. Retain conditions that affect comparability. Promised experiments do not replace results. Bring missing evidence to me; invent no numbers or completed work and do not automatically run experiments or submit responses.
4. Run the revise loop against the original issue list: question → response location → answered? → matching evidence? → remaining doubt → minimal fix → missing evidence. Repair coverage, evidence, and logic before shortening or adjusting tone. Revise failed items only, then recheck the same list; do not blindly rerun every baseline.
5. Stop when all issues are explicitly covered, facts match evidence, logic is clear, and length and venue rules are satisfied. I make the final decision. Return unresolved evidence gaps; do not predict score changes or acceptance from simulations.
6. Answer new concerns only in follow-ups. An AC summary states key concerns, responses, evidence, and limits without asking for score increases or acceptance. Add a Chinese translation per English paragraph for my review; keep internal checks and evidence gaps outside the submitted text.
```

---

Da1yuqin / PaperBank，[原文](https://da1yuqin.github.io/PaperBank/)，[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)。
