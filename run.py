#!/usr/bin/env python3
"""Build PaperBank; use --serve to preview with Python 3 and no dependencies."""
import argparse
import html
import json
import zipfile
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

ROOT = Path(__file__).resolve().parent
REPO = 'https://github.com/Da1yuqin/PaperBank'

def section_label(section):
 return '先读 · ' if int(section['number'])==0 else str(int(section['number']))+'. '

def render_paragraph(lesson, refs):
 """Show the paragraph's job before explaining its sentences."""
 e=html.escape
 rendered=f'<section class="paragraph-lesson" id="{e(lesson["id"])}" data-section="{e(lesson["section"])}"><h3>{e(lesson["title"])}</h3><p class="paragraph-purpose">{e(lesson["purpose"])}</p>'
 md=['',f'### {lesson["title"]}','',lesson['purpose']]
 if lesson.get('context_zh'):
  rendered+=f'<p class="lesson-context">{e(lesson["context_zh"])}</p>'
  md+=['',lesson['context_zh']]
 if lesson.get('label'):
  rendered+=f'<p class="lesson-context">{e(lesson["label"])}</p>'
 for n,sentence in enumerate(lesson.get('sentences',[]),1):
  rendered+=f'<div class="sentence"><p class="sentence-en" lang="en">{e(sentence["en"])}</p><p class="sentence-zh" lang="zh-CN">{e(sentence["zh"])}</p><p class="sentence-why"><strong>第 {n} 句：</strong>{e(sentence["why_zh"])}</p></div>'
  md+=['',sentence['en'],'',sentence['zh'],'',f'**第 {n} 句：**{sentence["why_zh"]}']
 if lesson.get('source'):
  r=refs[lesson['source']]
  rendered+=f'<p class="example-source"><a href="{e(r["url"])}">{e(r["title"])}</a> · {e(lesson.get("location",""))}</p>'
  md+=['',f'[{r["title"]}]({r["url"]}) · {lesson.get("location","")}']
 return rendered+'</section>',md

def render_opening(data):
 e=html.escape
 rendered='<section class="opening-rules" id="general-rules"><h2>先记住这几条</h2><ul>'
 md=['','## 先记住这几条','']
 for rule in data['general_rules']:
  rendered+=f'<li>{e(rule)}</li>';md+=['- '+rule]
 rendered+='</ul><details id="chapter-rules" class="rule-index"><summary>完整写作规则：按当前问题查</summary><ul>'
 for item in [i for i in data['items'] if i.get('iron_rule')]:
  rendered+=f'<li><a href="#{item["id"]}">{e(item["checklist"])}</a></li>'
 rendered+='</ul></details></section>'
 rendered+='<section class="paper-map" id="paper-order"><h2>一篇论文的骨架</h2><p>摘要把全文缩成一段；引言提出问题，方法给出做法，实验检查做法，讨论说明边界，结论收尾。常见顺序如下，具体按领域和投稿模板调整。</p><ol>'
 md+=['','## 一篇论文的骨架','','摘要把全文缩成一段；引言提出问题，方法给出做法，实验检查做法，讨论说明边界，结论收尾。具体按领域和投稿模板调整。','']
 for section in data['sections']:
  if section.get('manuscript',False):
   purpose=section.get('purpose',section['description'])
   rendered+=f'<li><a href="#chapter-{section["id"]}">{e(section["nav"])}</a>：{e(purpose)}</li>'
   md+=['- '+section['nav']+'：'+purpose]
 rendered+=f'</ol><p class="teaching-note">{e(data["simulation_context"])}</p></section>'
 md+=['',data['simulation_context']]
 return rendered,md

def render_quick_start(data):
 e=html.escape
 q=data['quick_start']
 rendered=f'<section class="quick-start" id="quick-start"><h2>先让 Codex 粗写，再自己精挑</h2><p>{e(q["brief_zh"])}</p><p class="fill-hint"><strong>填什么：</strong>{e(q["fill_hint_zh"])}</p>'
 md=['','## 先让 Codex 粗写，再自己精挑','',q['brief_zh'],'','**填什么：**'+q['fill_hint_zh']]
 for key,label,lang in [('prompt_zh','复制这个提示词','zh-CN'),('prompt_en','English prompt','en')]:
  rendered+=f'<details class="prompt"><summary>{label}</summary><pre lang="{lang}">{e(q[key])}</pre><button class="copy js-only">复制提示词</button></details>'
  md+=['','<details>',f'<summary>{label}</summary>','','```text',q[key],'```','','</details>']
 rendered+='<details class="manual-refinement"><summary>粗稿出来后，人工挑这四件事</summary><ul>'
 md+=['','**粗稿出来后，人工挑这四件事：**','']
 for a in q['manual_refinement']:
  rendered+=f'<li><strong>{e(a["title_zh"])}：</strong>{e(a["text_zh"])}</li>'
  md+=['- **'+a['title_zh']+'：**'+a['text_zh']]
 return rendered+'</ul></details></section>',md

def render_example(example, refs):
 """Keep quoted text, translations and teaching adaptations distinguishable."""
 e=html.escape
 rendered=f'<div class="example"><h5>{e(example["title"])}</h5>'
 md=['',f'**{example["title"]}**']
 if example.get('kind')=='teaching':
  label=example.get('label','教学示例：假设情境，非论文原文／实测记录')
  rendered+=f'<p class="example-label"><strong>{e(label)}</strong></p>'
  md+=['',f'**{label}**']
  note=example.get('context_zh','改后假定已有对应记录；实际改稿须先核对这些事实，不能从改前文字推断或补造。')
  rendered+=f'<p class="boundary">{e(note)}</p>'
  md+=['',note]
 if example.get('original_en'):
  assert all(example.get(k) for k in ['translation_zh','analysis_zh','provenance'])
  rendered+='<p class="example-label"><strong>论文原文 · English</strong></p>'
  rendered+=f'<blockquote class="original-quote" lang="en">{e(example["original_en"])}</blockquote>'
  md+=['','**论文原文 · English**','']+['> '+line for line in example['original_en'].split('\n')]
  rendered+=f'<p class="example-label"><strong>中文翻译 · 本指南翻译</strong></p><p class="example-translation" lang="zh-CN">{e(example["translation_zh"])}</p>'
  md+=['','**中文翻译 · 本指南翻译**','',example['translation_zh']]
 for key,label in [('before','改前'),('after','改后'),('why','说明')]:
  if example.get(key):
   style=' class="why"' if key=='why' else ''
   rendered+=f'<p{style}><strong>{label}：</strong>{e(example[key])}</p>'
   md+=['',f'**{label}：**{example[key]}']
 for key,label,lang in [('before_zh','改前 · 中文','zh-CN'),('before_en','Before · English','en'),('after_zh','改后 · 中文','zh-CN'),('after_en','After · English','en')]:
  if example.get(key):
   rendered+=f'<p class="example-label"><strong>{label}</strong></p><p lang="{lang}">{e(example[key])}</p>'
   md+=['',f'**{label}**','',example[key]]
 if example.get('image'):
  rendered+=f'<figure class="example-figure"><a href="{e(example["image"])}"><img class="teaching-figure" src="{e(example["image"])}" alt="{e(example["alt"])}" loading="lazy"></a>'
  md+=['',f'![{example["alt"]}](../{example["image"]})']
  captions=[example[k] for k in ['caption_en','caption_zh','caption'] if example.get(k)]
  if captions:
   rendered+='<figcaption>'+''.join(f'<p>{e(caption)}</p>' for caption in captions)+'</figcaption>'
   md+=['']+captions
  rendered+='</figure>'
 if example.get('analysis_zh'):
  analysis=example['analysis_zh']
  rendered+='<p class="example-label"><strong>'+('看图与点评' if example.get('image') else '逐句拆解')+'</strong></p>'
  md+=['','**逐句拆解**','']
  if isinstance(analysis,list):
   rendered+='<ol class="example-analysis">'+''.join(f'<li>{e(text)}</li>' for text in analysis)+'</ol>'
   md+=[f'{n}. {text}' for n,text in enumerate(analysis,1)]
  else:
   rendered+=f'<p class="example-analysis">{e(analysis)}</p>'
   md+=[analysis]
 for key,label,lang in [('transfer_en','教学改写 · English','en'),('transfer_zh','教学改写 · 中文','zh-CN')]:
  if example.get(key):
   rendered+=f'<div class="example-transfer"><p class="example-label"><strong>{label}</strong><span>（非论文原文）</span></p><p lang="{lang}">{e(example[key])}</p></div>'
   md+=['',f'**{label}（非论文原文）**','',example[key]]
 if example.get('provenance'):
  p=example['provenance']; r=refs[p['reference']]
  assert all(p.get(k) for k in ['location','version','status'])
  details='；'.join(p[k] for k in ['location','version','status'])
  rendered+=f'<p class="example-source"><strong>来源：</strong><a href="{e(r["url"])}">{e(r["title"])}</a>；{e(details)}</p>'
  md+=['',f'**摘录出处：**[{r["title"]}]({r["url"]})；{details}']
 if example.get('license'):
  rendered+=f'<p class="example-source"><strong>原文／图片许可：</strong>{e(example["license"])}</p>'
  md+=['',f'**原文／图片许可：**{example["license"]}']
 return rendered+'</div>',md

def render_skill(data):
 """Keep the portable entry point separate from the full reading guide."""
 e=html.escape
 skill=data['writing_skill']
 rendered=f'<details class="writing-skill" id="writing-skill"><summary>给 Codex 用：下载 PaperBank 写作 skill</summary><p>{e(skill["intro"])}</p>'
 rendered+=f'<p class="skill-links"><a href="{e(skill["download"])}" download>下载写作 skill ZIP</a> · <a href="{REPO}/blob/main/{e(skill["source"])}">查看 SKILL.md</a> · <a href="#chapter-rules">写作规则索引</a></p><p>下载、解压，保留整个 <code>paperbank-writing/</code> 文件夹，把它交给 Codex 读取。下面提示词可直接用，再补上你的文件、任务和允许修改的范围。</p>'
 md=['','<a id="writing-skill"></a>','## PaperBank 写作 skill：让 Codex 也按这份清单检查','',skill['intro'],'',f'[下载 ZIP](../{skill["download"]}) · [查看 SKILL.md](../{skill["source"]}) · [32 条写作铁律](#rules)','','下载、解压，保留整个 paperbank-writing/ 文件夹，把它交给 Codex 读取；补上文件、任务和允许修改的范围。']
 for key,label,lang in [('prompt_zh','中文使用提示词','zh-CN'),('prompt_en','English usage prompt','en')]:
  rendered+=f'<details class="prompt"><summary>{label}</summary><pre lang="{lang}">{e(skill[key])}</pre><button class="copy js-only">复制提示词</button></details>'
  md+=['',f'**{label}**','','```text',skill[key],'```']
 return rendered+'</details>',md

def package_skill(data):
 """Generate the skill reference from the same rules used by the website."""
 folder=ROOT/'skills/paperbank-writing'
 rules=data.get('skill_rules') or [i for i in data['items'] if i.get('iron_rule') or i['section']=='rules']
 md=['# PaperBank 写作检查参考','','按本次任务选规则。下面示例是假设情境，不是论文原文或实测；实际改稿先核对事实。','','网页：[32 条写作铁律](https://da1yuqin.github.io/PaperBank/#chapter-rules) · [论文结构与逐句例子](https://da1yuqin.github.io/PaperBank/#paper-order) · [rebuttal](https://da1yuqin.github.io/PaperBank/#chapter-rebuttal)']
 for group in dict.fromkeys(i['group'] for i in rules):
  md+=['','## '+group,'']
  for i in [x for x in rules if x['group']==group]:
   md+=['',f'### 第 {i["id"][4:]} 条：{i["title"]}','',i['checklist'],'','适用边界：'+i['boundary']]
   _,example_md=render_example(i['examples'][0],data['references'])
   md+=example_md
 md+=['','---','','原创规则与教学示例：Da1yuqin / PaperBank，[原文](https://da1yuqin.github.io/PaperBank/)，[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)。转载保留署名、出处及许可，改编注明改动。']
 (folder/'references').mkdir(parents=True,exist_ok=True)
 (folder/'references/checklist.md').write_text('\n'.join(md)+'\n',encoding='utf-8')
 with zipfile.ZipFile(ROOT/data['writing_skill']['download'],'w',zipfile.ZIP_DEFLATED) as z:
  for name in ['SKILL.md','references/checklist.md','LICENSE']:
   info=zipfile.ZipInfo('paperbank-writing/'+name,date_time=(2026,10,7,0,0,0))
   info.compress_type=zipfile.ZIP_DEFLATED
   info.external_attr=0o644<<16
   z.writestr(info,(folder/name).read_bytes())

def render_tools(data):
 """Render linked resources separately from manuscript checks."""
 e=html.escape
 groups=data.get('tools',[])
 intro='按用途挑一个先试。只核对公开说明，未逐项安装评测；例子是使用情境，许可和兼容版本看原项目。'
 rendered=f'<section class="toolbox" id="tools"><h2>好用工具：省点手工，判断还得自己来</h2><p class="chapter-desc">{e(intro)}</p>'
 rendered+='<p class="tool-index">'+ ' · '.join(f'<a href="#tools-{e(g["id"])}">{e(g["title"])}</a>' for g in groups)+' · <a href="#code-release-prompt">开源整理提示词</a></p>'
 total=sum(len(g['items']) for g in groups)
 rendered+=f'<div class="tool-search js-only"><label for="tool-search">搜索工具</label><input type="search" id="tool-search" placeholder="搜 Zotero、画图、引用……"><span id="tool-count" role="status" aria-live="polite">{total} 项资源</span></div>'
 md=['','<a id="tools"></a>','## 好用工具：省点手工，判断还得自己来','',intro,'','核对日期：'+data['tools_checked_at']+'。']
 for group in groups:
  rendered+=f'<section class="tool-group" id="tools-{e(group["id"])}"><h3>{e(group["title"])}</h3><ul class="tool-list">'
  md+=['',f'### {group["title"]}','']
  for tool in group['items']:
   assert all(tool.get(k) for k in ['id','title','url','use_zh','example_zh','example_en','boundary_zh'])
   rendered+=f'<li class="tool-item" id="tool-{e(tool["id"])}"><p><strong><a href="{e(tool["url"])}">{e(tool["title"])}</a>：</strong>{e(tool["use_zh"])}</p><details class="tool-detail"><summary>中英例子与使用边界</summary><p lang="zh-CN"><strong>例子：</strong>{e(tool["example_zh"])}</p><p lang="en"><strong>Example:</strong> {e(tool["example_en"])}</p><p class="boundary"><strong>注意：</strong>{e(tool["boundary_zh"])}</p>'
   md+=[f'- **[{tool["title"]}]({tool["url"]})：**{tool["use_zh"]}','',f'  <details><summary>中英例子与使用边界</summary>','',f'  **例子：**{tool["example_zh"]}','',f'  **Example:** {tool["example_en"]}','',f'  **注意：**{tool["boundary_zh"]}']
   if tool.get('links'):
    rendered+='<p class="sources">'+' · '.join(f'<a href="{e(link["url"])}">{e(link["title"])}</a>' for link in tool['links'])+'</p>'
    md+=['','  '+' · '.join(f'[{link["title"]}]({link["url"]})' for link in tool['links'])]
   rendered+='</details></li>'
   md+=['','  </details>','']
  rendered+='</ul></section>'
 rendered+='<p class="boundary js-only" id="tool-empty" hidden>没有匹配的工具。换个短词试试。</p>'
 prompt=data['code_release_prompt']
 rendered+='<section class="release-prompt" id="code-release-prompt"><h3>开源整理：翻译注释，清掉私货，保留行为</h3><p>先写清允许处理的文件。中文界面、接口字符串、业务路径也可能影响运行，不能一键全换。下面中英两版都可复制。</p>'
 md+=['','<a id="code-release-prompt"></a>','### 开源整理：翻译注释，清掉私货，保留行为','','先写清允许处理的文件。中文界面、接口字符串、业务路径也可能影响运行，不能一键全换。']
 for key,label,lang in [('zh','中文提示词','zh-CN'),('en','English prompt','en')]:
  rendered+=f'<details class="prompt"><summary>{label}</summary><pre lang="{lang}">{e(prompt[key])}</pre><button class="copy js-only">复制提示词</button></details>'
  md+=['','**'+label+'**','','```text',prompt[key],'```']
 rendered+=f'<p class="tool-checked">链接与文档核对日期：{e(data["tools_checked_at"])}。安装方法、兼容版本和许可可能变化，使用前再看项目原文。</p></section></section>'
 return rendered,md

def build():
 data=json.loads((ROOT/'data/guide.json').read_text(encoding='utf-8'))
 sections,items,refs=data['sections'],data['items'],data['references']
 lessons=data.get('manuscript_paragraphs',[])
 assert len({i['id'] for i in items})==len(items)
 assert all(i['section'] in {s['id'] for s in sections} for i in items)
 assert len({p['id'] for p in lessons})==len(lessons)
 assert all(p['section'] in {s['id'] for s in sections} for p in lessons)
 e=html.escape
 def link(key):
  r=refs[key]
  return f'<a href="{e(r["url"])}">{e(r["title"])}</a>'
 quick_start,quick_md=render_quick_start(data)
 opening,opening_md=render_opening(data)
 skill,skill_md=render_skill(data)
 nav=f'<button data-chapter="all" aria-pressed="true" class="active">全部章节<i>{len(items)}</i></button>'
 for s in sections:
  group=[i for i in items if i['section']==s['id']]
  nav+=f'<button data-chapter="{s["id"]}" aria-pressed="false">{section_label(s)}{e(s["nav"])}<i>{len(group)}</i></button>'
 entries=''
 md=['# PaperBank · 论文少走弯路指南','','按论文顺序看每个自然段要完成什么，再逐句看中英例子与解释。','','主要面向方法与实证研究；按学科、研究类型和投稿要求调整。模拟段落明确标注，真实论文摘录另给出处与版本。','','欢迎使用、改写、转载，也欢迎拿去给 Codex 做 skill。原创内容采用 CC BY 4.0，论文摘录与图片保留各自许可。转载原创内容请保留作者 Da1yuqin、[原文链接](https://Da1yuqin.github.io/PaperBank/)和 [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) 许可，改过请注明。Star 自愿，署名别失联。']
 md+=quick_md+skill_md+['','<a id="rules"></a>']+opening_md+['','## 目录','']
 md += [f'- [{section_label(s)}{s["title"]}](#{s["id"]})' for s in sections]
 md += ['- [好用工具与开源整理提示词](#tools)']
 for s in sections:
  group=[i for i in items if i['section']==s['id']]
  purpose=s.get('purpose') or s.get('summary') or s['description']
  entries+=f'<section class="chapter" id="chapter-{s["id"]}"><div class="chapter-head"><h2>{section_label(s)}{e(s["title"])}</h2><span class="shown">{len(group)} 条</span></div><p class="chapter-desc">{e(purpose)}</p>'
  md+=['',f'<a id="{s["id"]}"></a>',f'## {section_label(s)}{s["title"]}','',purpose]
  for lesson in [p for p in lessons if p['section']==s['id']]:
   lesson_html,lesson_md=render_paragraph(lesson,refs)
   entries+=lesson_html
   if lesson.get('label') and lesson['label'] not in lesson_md:
    at=lesson_md.index(lesson['purpose'])+1
    lesson_md[at:at]=['',lesson['label']]
   md+=lesson_md
  entries+=f'<details class="chapter-checks"><summary>检查清单和真实论文例子（{len(group)} 项）</summary>'
  md+=['','<details>',f'<summary>检查清单和真实论文例子（{len(group)} 项）</summary>','']
  for subgroup in dict.fromkeys(i['group'] for i in group):
   entries+=f'<div class="check-group"><h3 class="group-title">{e(subgroup)}</h3><ul class="checklist">'
   md+=['',f'**{subgroup}**','']
   for i in [x for x in group if x['group']==subgroup]:
    num=int(i['id'][4:]); attrs=' '.join(f'data-{k}="{e(i[k])}"' for k in ['section','priority'])
    entries+=f'<li class="entry{ " entry-visual" if i.get("detail") else ""}" id="{i["id"]}" {attrs}><div class="check-row"><input class="task-check js-only" type="checkbox" id="check-{i["id"]}" data-id="{i["id"]}"><label class="check-text" for="check-{i["id"]}">{e(i["checklist"])}</label><a class="permalink" href="#{i["id"]}" aria-label="第 {num} 条">{num}</a></div>'
    md += [f'- [ ] **第 {num} 条：**{i["checklist"]}']
    paragraph=i.get('paragraph') or i.get('action','')
    entries+=f'<details class="explain"><summary>说明{ "、例子" if i.get("examples") else ""}与参考</summary><div class="explain-body">'
    if paragraph:
     entries+=f'<p>{e(paragraph)}</p>'
    entries+=f'<p class="boundary"><strong>边界：</strong>{e(i["boundary"])}</p>'
    md+=['',f'<a id="{i["id"]}"></a>','<details>','<summary>说明、例子与参考</summary>']
    if paragraph:
     md+=['',paragraph]
    md+=['',f'**边界：**{i["boundary"]}']
    for example in i.get('examples',[]):
     example_html,example_md=render_example(example,refs)
     entries+=example_html;md+=example_md
    if i.get('prompt'):
     entries+=f'<details class="prompt"><summary>复制用的提示词</summary><pre>{e(i["prompt"])}</pre><button class="copy js-only">复制提示词</button></details>'
     md+=['','```text',i['prompt'],'```']
    sources=list(dict.fromkeys([i['source']]+i.get('refs',[])))
    entries+='<p class="sources"><strong>来源与延伸阅读：</strong>'+'；'.join(link(k) for k in sources)+'</p></div></details></li>'
    md+=['','来源与延伸阅读：'+'；'.join(f'[{refs[k]["title"]}]({refs[k]["url"]})' for k in sources),'','</details>','']
   entries+='</ul></div>'
  entries+='</details></section>'
  md+=['','</details>','']
 examples=sum(len(i.get('examples',[])) for i in items)
 tools,tools_md=render_tools(data)
 md+=tools_md
 reading=''.join(f'<li>{link(k)}<span> — {e(r["scope"])}</span></li>' for k,r in refs.items() if r.get('public'))
 t=(ROOT/'assets/template.html').read_text(encoding='utf-8')
 for k,v in {'NAV':nav,'ENTRIES':entries,'TOOLS':tools,'QUICK_START':quick_start,'OPENING':opening,'SKILL':skill,'READING':reading,'TOTAL':str(len(items)),'CHAPTERS':str(len(sections)),'EXAMPLES':str(examples)}.items():t=t.replace('{{'+k+'}}',v)
 (ROOT/'index.html').write_text(t,encoding='utf-8')
 (ROOT/'book').mkdir(exist_ok=True)
 md+=['','## 参考阅读','']+[f'- [{r["title"]}]({r["url"]})：{r["scope"]}' for r in refs.values() if r.get('public')]
 (ROOT/'book/guide.md').write_text('\n'.join(md)+'\n',encoding='utf-8')
 package_skill(data)
 print(f'Built {len(sections)} chapters, {len(items)} checks, {examples} examples.')

if __name__=='__main__':
 p=argparse.ArgumentParser(description=__doc__)
 p.add_argument('--serve',action='store_true');p.add_argument('--port',type=int,default=8000)
 a=p.parse_args();build()
 if a.serve:
  print(f'Preview: http://127.0.0.1:{a.port}',flush=True)
  ThreadingHTTPServer(('127.0.0.1',a.port),partial(SimpleHTTPRequestHandler,directory=str(ROOT))).serve_forever()
