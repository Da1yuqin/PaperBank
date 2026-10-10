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
FIGURE_SECTIONS = [
 ('figure-skill','先给 Codex 绘图 skill'),
 ('figure-rules','绘图铁律：这些错别犯'),
 ('figure-types','按图的任务选模板'),
 ('notion-gallery','图例库：原图与逐图拆解'),
 ('figure-gallery','私藏图：好在哪里，怎么借鉴'),
 ('figure-references','更多参考图，带着问题看'),
]

def render_codex_prompt(data, key, label_zh, label_en='English prompt'):
 """Use one skill-grounded prompt for the page and portable references."""
 e=html.escape;prompt=data['codex_prompts'][key]
 rendered='';md=[]
 for language,label,lang in [('zh',label_zh,'zh-CN'),('en',label_en,'en')]:
  text=prompt[language]
  rendered+=f'<details class="prompt" data-prompt-ref="{e(key)}" data-prompt-lang="{language}"><summary>{e(label)}</summary><pre lang="{lang}">{e(text)}</pre><button class="copy js-only">复制提示词</button></details>'
  md+=['','**'+label+'**','','```text',text,'```']
 source=f'{REPO}/blob/main/skills/paperbank-{prompt["skill"]}/references/prompts.md#{key}'
 rendered+=f'<p class="example-source">依据：{e(" · ".join(prompt["sources"]))} · <a href="{e(source)}">对应铁律与完整提示词</a></p>'
 md+=['','依据：'+' · '.join(prompt['sources'])+f' · [对应铁律与完整提示词]({source})']
 return rendered,md

def package_prompt_reference(data, folder, keys):
 md=['# 给 Codex 的提示词','','填写【】后使用。以下采用本地技能中适用于实证型 CS 论文的通用规则；不套用某篇论文的固定宽度、色值、模型阵容或重复次数。Nature 系列使用独立体系。','']
 for key in keys:
  prompt=data['codex_prompts'][key]
  md+=['',f'<a id="{key}"></a>','## '+prompt['title'],'','依据：'+' · '.join(prompt['sources'])+'。','', '对应规则：'+'；'.join(prompt['basis'])+'。']
  for lang,label in [('zh','中文'),('en','English')]:
   md+=['','### '+label,'','```text',prompt[lang],'```']
 md+=['','---','','Da1yuqin / PaperBank，[原文](https://da1yuqin.github.io/PaperBank/)，[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)。']
 (folder/'references/prompts.md').write_text('\n'.join(md)+'\n',encoding='utf-8')

def section_label(section):
 return '先读 · ' if int(section['number'])==0 else str(int(section['number']))+'. '

def render_paragraph(lesson, refs, md_level=4, number=None, heading=True):
 """Show the paragraph's job before explaining its sentences."""
 e=html.escape
 title=(number+' ' if number else '')+lesson['title']
 label=f'<h{md_level}>{e(title)}</h{md_level}>' if heading else f'<p class="example-title"><strong>{e(title)}</strong></p>'
 rendered=f'<section class="paragraph-lesson" id="{e(lesson["id"])}" data-section="{e(lesson["section"])}">{label}<p class="paragraph-purpose">{e(lesson["purpose"])}</p>'
 md=['',f'{"#"*md_level} {title}' if heading else f'**{title}**','',lesson['purpose']]
 if lesson.get('context_zh'):
  rendered+=f'<p class="lesson-context">{e(lesson["context_zh"])}</p>'
  md+=['',lesson['context_zh']]
 if lesson.get('label'):
  rendered+=f'<p class="lesson-context">{e(lesson["label"])}</p>'
  md+=['',lesson['label']]
 if lesson.get('rules'):
  rendered+='<ul class="template-rules">'+''.join(f'<li>{e(r)}</li>' for r in lesson['rules'])+'</ul>'
  md+=['']+['- '+r for r in lesson['rules']]
 if lesson.get('scope'):
  rendered+=f'<p class="lesson-context">{e(lesson["scope"])}</p>';md+=['',lesson['scope']]
 if lesson.get('before_en'):
  rendered+=f'<p class="example-label">改前 · English</p><p lang="en">{e(lesson["before_en"])}</p><p>{e(lesson["before_zh"])}</p><p class="example-label">改后 · 逐句拆解</p>'
  md+=['','**改前**','',lesson['before_en'],'',lesson['before_zh'],'','**改后**']
 for n,sentence in enumerate(lesson.get('sentences',[]),1):
  rendered+=f'<div class="sentence"><p class="sentence-en" lang="en">{e(sentence["en"])}</p><p class="sentence-zh" lang="zh-CN">{e(sentence["zh"])}</p><p class="sentence-why"><strong>第 {n} 句：</strong>{e(sentence["why_zh"])}</p></div>'
  md+=['',sentence['en'],'',sentence['zh'],'',f'**第 {n} 句：**{sentence["why_zh"]}']
 if lesson.get('source'):
  r=refs[lesson['source']]
  rendered+=f'<p class="example-source"><a href="{e(r["url"])}">{e(r["title"])}</a> · {e(lesson.get("location",""))}</p>'
  md+=['',f'[{r["title"]}]({r["url"]}) · {lesson.get("location","")}']
 if lesson.get('latex_template'):
  rendered+=f'<details class="prompt full-template"><summary>完整 LaTeX 骨架</summary><pre>{e(lesson["latex_template"])}</pre><button class="copy js-only">复制提示词</button></details>'
  md+=['','**完整 LaTeX 骨架**','','```latex',lesson['latex_template'],'```']
 return rendered+'</section>',md

def render_opening(data):
 e=html.escape
 lead=data['opening_lead']
 rendered='<section class="opening-rules" id="general-rules"><h3>3.1 全文规范</h3><p>'+e(lead)+'</p>'
 md=['','<a id="general-rules"></a>','### 3.1 全文规范','',lead]
 for n,group in enumerate(data['refine_standard_groups']):
  title=f'3.1.{chr(97+n)} '+group['title']
  rendered+=f'<h4>{e(title)}</h4><ul class="compact-rules">';md+=['','#### '+title]
  for rule in [r for r in data['refine_standards'] if r['group']==group['id']]:
   rendered+=f'<li id="{rule["id"]}"><strong>{e(rule["title"])}：</strong>{e(rule["purpose"])}<details class="short-example"><summary>中英改写与拆解</summary>'
   example=dict(rule);example['id']=rule['id']+'-example'
   rh,rm=render_paragraph(example,data['references'],heading=False);rendered+=rh.replace('class="paragraph-lesson"','class="global-example"')+'</details></li>';md+=rm
  rendered+='</ul>'
 rendered+='</section>'
 rendered+='<section class="paper-map" id="paper-order"><p class="outline-label"><strong>按论文顺序精修</strong></p><p>摘要概括全文，引言提问题，方法给做法，实验查效果，讨论讲范围，结论收尾。以下按实证型 CS / AI 论文组织。</p><ol>'
 md+=['','**按论文顺序精修**','','摘要概括全文，引言提问题，方法给做法，实验查效果，讨论讲范围，结论收尾。','']
 for section in data['sections']:
  if section.get('manuscript',False):
   purpose=section.get('purpose',section['description'])
   title=f'3.{int(section["number"])+1} '+section['nav']
   rendered+=f'<li><a href="#chapter-{section["id"]}">{e(title)}</a>：{e(purpose)}</li>'
   md+=['- '+title+'：'+purpose]
 rendered+=f'</ol><p class="teaching-note">{e(data["simulation_context"])}</p></section>'
 md+=['',data['simulation_context']]
 return rendered,md

def render_preface(data):
 e=html.escape
 p=data['preface']
 rendered=f'<figure class="accept-banner"><img src="{e(p["image"])}" alt="{e(p["image_alt"])}" width="1672" height="941" fetchpriority="high"></figure><section class="preface" id="preface"><h2>{e(p["title"])}</h2>'
 rendered+=''.join(f'<p>{e(text)}</p>' for text in p['paragraphs'])
 rendered+=f'<p class="preface-aside"><em>{e(p["aside"])}</em></p>'
 rendered+=f'<p>{e(p["homepage_text"])}<a href="{e(p["homepage_url"])}">{e(p["homepage_label"])}</a></p></section>'
 md=['',f'![{p["image_alt"]}](../{p["image"]})','','## '+p['title'],'']
 md+=sum(([text,''] for text in p['paragraphs']),[])
 md+=['*'+p['aside']+'*','']
 md+=[p['homepage_text']+f'[{p["homepage_label"]}]({p["homepage_url"]})','']
 return rendered,md

def render_quick_start(data, include_figures=True):
 e=html.escape
 q=data['quick_start']
 rendered=f'<section class="quick-start major-chapter" id="quick-start"><h2>1. {e(q["title_zh"])}</h2><p>{e(q["lead_zh"])}</p>'
 md=['','<a id="quick-start"></a>','## 1. '+q['title_zh'],'',q['lead_zh']]
 if q.get('example_note'):
  rendered+=f'<p class="example-source">{e(q["example_note"])}</p>'
  md+=['',q['example_note']]
 for n,s in enumerate(q['steps'],1):
  rendered+=f'<section class="draft-step" id="{s["id"]}"><h3>{e(s["title_zh"])}</h3>'
  md+=['','### '+s['title_zh']]
  if n==2:
   skill=data['figure_chapter']['skill']
   rendered+=f'<p class="skill-links"><a href="{e(skill["download"])}" download>先下载绘图 skill ZIP</a> · <a href="{REPO}/blob/main/{e(skill["source"])}">查看 SKILL.md</a> · <a href="#figure-rules">绘图铁律</a></p>'
   md+=['',f'[先下载绘图 skill ZIP](../{skill["download"]}) · [查看 SKILL.md](../{skill["source"]}) · [绘图铁律](#figure-rules)']
  rendered+=f'<p>{e(s["text_zh"])}</p>'
  md+=['',s['text_zh']]
  blocks=s.get('blocks',[])
  for b,block in enumerate(blocks):
   title=(f'1.{n}.{chr(97+b)} ' if len(blocks)>1 else '')+block['title']
   label=f'<h4>{e(title)}</h4>' if len(blocks)>1 else f'<p class="example-title"><strong>{e(title)}</strong></p>'
   rendered+=f'<div class="draft-block">{label}'
   md+=['','#### '+title if len(blocks)>1 else '**'+title+'**']
   if block.get('rules'):
    rendered+='<ul class="draft-rules">'
    for rule in block['rules']:
     rendered+=f'<li><strong>{e(rule["label"])}：</strong>{e(rule["text"])}<details class="short-example"><summary>中英例子</summary><p>{e(rule["example_zh"])}</p><p lang="en">{e(rule["example_en"])}</p></details></li>'
     md+=['',f'- **{rule["label"]}：**{rule["text"]}','',rule['example_zh'],'',rule['example_en']]
    rendered+='</ul>'
   if block.get('figure_reference'):
    v=next(v for v in data['figure_chapter']['visual_examples'] if v['id']==block['figure_reference'])
    rendered+=f'<p class="example-title"><strong>{e(block["figure_title"])}</strong></p><p>{e(block["figure_zh"])}</p>'
    if include_figures:
     rendered+=f'<figure class="draft-figure"><a href="{e(v["asset"])}"><img src="{e(v["asset"])}" alt="{e(block["figure_title"])}" loading="lazy"></a><figcaption>{e(v["license"])} <a href="{e(v["source_url"])}">原论文</a> · <a href="{e(v["license_url"])}">许可</a></figcaption></figure>'
     md+=['',f'![{block["figure_title"]}](../{v["asset"]})']
    rendered+=f'<details class="short-example"><summary>English</summary><p lang="en">{e(block["figure_en"])}</p></details>'
    md+=['',block['figure_zh'],'',block['figure_en'],'',v['license']+f' [原论文]({v["source_url"]}) · [许可]({v["license_url"]})']
   if block.get('table'):
    t=block['table']
    rendered+=f'<div class="draft-table-wrap"><table class="draft-table"><caption>{e(t["caption"])}</caption><thead><tr>'+''.join(f'<th scope="col">{e(h)}</th>' for h in t['headers'])+'</tr></thead><tbody>'
    md+=['',t['caption'],'','| '+' | '.join(t['headers'])+' |','| --- | --- | --- |']
    for row in t['rows']:
     rendered+=f'<tr><th scope="row">{e(row["method"])}</th>'
     cells=[]
     for cell in row['cells']:
      mark=cell.get('mark','')
      value=e(cell['value'])
      if mark=='best': value=f'<strong>{value}</strong>'
      elif mark=='second': value=f'<u>{value}</u>'
      rendered+=f'<td class="{mark}">{value}<sup>±{e(cell["uncertainty"])}</sup></td>'
      cells.append(cell['value']+' ±'+cell['uncertainty'])
     rendered+='</tr>'
     md+=['| '+row['method']+' | '+' | '.join(cells)+' |']
    rendered+='</tbody></table></div>'
   if block.get('prompt_ref'):
    ph,pm=render_codex_prompt(data,block['prompt_ref'],block['code_title']);rendered+=ph;md+=pm
   elif block.get('code'):
    rendered+=f'<details class="prompt"><summary>{e(block["code_title"])}</summary><pre>{e(block["code"])}</pre><button class="copy js-only" data-copy-label="复制模板">复制模板</button></details>'
    md+=['','**'+block['code_title']+'**','','```'+block['code_language'],block['code'],'```']
    if block.get('code_note'):
     rendered+=f'<p class="example-source">{e(block["code_note"])}</p>'
     md+=['',block['code_note']]
   rendered+='</div>'
  rendered+=f'<details class="short-example"><summary>中英例子</summary><p>{e(s["example_zh"])}</p><p lang="en">{e(s["example_en"])}</p><p lang="en">{e(s["text_en"])}</p></details>'
  md+=['',s['example_zh'],'',s['example_en'],'',s['text_en']]
  if n==1:
   rendered+=f'<p class="fill-hint"><strong>填什么：</strong>{e(q["fill_hint_zh"])}</p><p class="skill-links"><a href="{data["writing_skill"]["download"]}" download>下载 PaperBank 写作 skill</a> · <a href="#writing-skill">安装与用法</a></p>'
   ph,pm=render_codex_prompt(data,q['prompt_ref'],'复制这个提示词，填空就能用');rendered+=ph;md+=pm
   rendered+=f'<p class="example-source">{e(s["note_zh"])} <a href="{q["sources"][0]["url"]}">Git 同步说明</a> · <a href="{q["sources"][1]["url"]}">ZIP 下载说明</a></p>'
   md+=['',s['note_zh'],'',' · '.join(f'[{r["title"]}]({r["url"]})' for r in q['sources'][:2])]
  if n==2: rendered+='<p><a href="#figures">第二章：光速出美图，继续精修 ↗</a></p>'
  if n==4: rendered+='<p><a href="#refine">第三章：古法精修，逐段查写法 ↗</a></p>'
  rendered+='</section>'
 return rendered+'</section>',md

def render_example(example, refs):
 """Keep quoted text, translations and teaching adaptations distinguishable."""
 e=html.escape
 rendered=f'<div class="example"><p class="example-title"><strong>{e(example["title"])}</strong></p>'
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

def render_short_rules(rules, visuals=None):
 e=html.escape
 visuals=visuals or {}
 rendered='<ul class="compact-rules">';md=[]
 for r in rules:
  rendered+=f'<li><strong>{e(r["title"])}：</strong>{e(r["zh"])}'
  md+=['','- **'+r['title']+'：**'+r['zh']]
  if r.get('example_en'):
   rendered+=f'<details class="short-example"><summary>中英例子</summary><p lang="en">{e(r["example_en"])}</p><p>{e(r["example_zh"])}</p></details>'
   md+=['',r['example_en'],'',r['example_zh']]
  for key in r.get('visuals',[]):
   if key not in visuals:continue
   v=visuals[key]
   rendered+=f'<a class="rule-visual" href="#{e(v["id"])}"><img src="{e(v["asset"])}" alt="{e(v["title"])}" loading="lazy"><span>{e(v["title"])} · 点开原图与拆解 ↗</span></a>'
   md+=['',f'![{v["title"]}](../{v["asset"]})',f'[原图与拆解](#{v["id"]})']
  rendered+='</li>'
 return rendered+'</ul>',md

def render_figures(data):
 e=html.escape;f=data['figure_chapter']
 titles={key:f'2.{n} '+title for n,(key,title) in enumerate(FIGURE_SECTIONS,1)}
 visuals={v['id']:v for v in f.get('visual_examples',[])}
 rendered=f'<section class="major-chapter figure-chapter" id="figures"><h2>2. {e(f["title"])}</h2><p>{e(f["lead"])}</p><p class="lesson-context">{e(f["scope_note"])}</p>'
 md=['','<a id="figures"></a>','## 2. '+f['title'],'',f['lead'],'',f['scope_note']]
 skill=f['skill']
 rendered+=f'<section id="figure-skill"><h3>{e(titles["figure-skill"])}</h3><p class="skill-links"><a href="{e(skill["download"])}" download>下载绘图 skill ZIP</a> · <a href="{REPO}/blob/main/{e(skill["source"])}">查看 SKILL.md</a> · <a href="#figure-rules">绘图铁律</a></p><p>{e(skill["intro"])}</p>'
 md+=['','<a id="figure-skill"></a>','### '+titles['figure-skill'],'',f'[下载绘图 skill ZIP](../{skill["download"]}) · [查看 SKILL.md](../{skill["source"]}) · [绘图铁律](#figure-rules)','',skill['intro']]
 ph,pm=render_codex_prompt(data,f['prompt_ref'],'复制给 Codex：开始画图','Figure prompt · English');rendered+=ph;md+=pm
 rendered+=f'</section><h3 id="figure-rules">{e(titles["figure-rules"])}</h3>'
 rh,rm=render_short_rules(f['rules'],visuals);rendered+=rh;md+=['','<a id="figure-rules"></a>','### '+titles['figure-rules']]+rm
 rendered+=f'<h3 id="figure-types">{e(titles["figure-types"])}</h3><p class="lesson-context">下面均为教学句式；数值、误差和区间按实际记录填写。</p>'
 rh,rm=render_short_rules(f['types'],visuals);rendered+=rh;md+=['','<a id="figure-types"></a>','### '+titles['figure-types']]+rm
 if visuals:
  rendered+=f'<h3 id="notion-gallery">{e(titles["notion-gallery"])}</h3><p>同类图放一起；点击缩略图或展开目录看原图。</p>'
  md+=['','<a id="notion-gallery"></a>','### '+titles['notion-gallery'],'']
  for topic in dict.fromkeys(v['topic'] for v in visuals.values() if not v.get('existing')):
   group=[v for v in visuals.values() if v['topic']==topic and not v.get('existing')]
   rendered+=f'<details class="figure-set"><summary>{e(topic)} · {len(group)} 张图</summary>'
   md+=['','<details><summary>'+topic+' · '+str(len(group))+' 张图</summary>','']
   for v in group:
    license_link=f' · <a href="{e(v["license_url"])}">许可</a>' if v.get('license_url') else ''
    rendered+=f'<section class="visual-example" id="{e(v["id"])}"><p class="example-title"><strong>{e(v["title"])}</strong></p><p>{e(v["zh"])}</p><figure><a href="{e(v["asset"])}"><img src="{e(v["asset"])}" alt="{e(v["title"])}" loading="lazy"></a><figcaption>{e(v["license"])}{license_link}</figcaption></figure><details class="short-example"><summary>English 与拆解</summary><p lang="en">{e(v["en"])}</p>'
    md+=['',f'<a id="{v["id"]}"></a>','**'+v['title']+'**','',v['zh'],'',f'![{v["title"]}](../{v["asset"]})','',v['license'],'',v['en']]
    for why in v.get('analysis_zh',[]):rendered+=f'<p>{e(why)}</p>';md+=['',why]
    rendered+='</details>'
    if v.get('source_url'):
     rendered+=f'<p class="example-source">来源：<a href="{e(v["source_url"])}">{e(v["source_title"])}</a></p>'
     source_url=v['source_url'] if '://' in v['source_url'] else '../'+v['source_url']
     md+=['',f'来源：[{v["source_title"]}]({source_url})']
    if v.get('license_url'):md+=['',f'[图片许可]({v["license_url"]})']
    rendered+='</section>'
   rendered+='</details>';md+=['','</details>','']
 rendered+=f'<h3 id="figure-gallery">{e(titles["figure-gallery"])}</h3><p>先看原图，再看点评。借信息组织，不照搬别人的结果。</p>'
 md+=['','<a id="figure-gallery"></a>','### '+titles['figure-gallery'],'','先看原图，再看点评。借信息组织，不照搬别人的结果。']
 items={i['id']:i for i in data['items']}
 for g in f['gallery']:
  ex=items[g['item']]['examples'][g['example_index']]
  rendered+=f'<section class="gallery-example" id="{g["figure_id"]}"><p><strong>{e(g["comment"])}</strong></p>'
  eh,em=render_example(ex,data['references']);rendered+=eh+'</section>';md+=['',f'<a id="{g["figure_id"]}"></a>',g['comment']]+em
 rendered+=f'<h3 id="figure-references">{e(titles["figure-references"])}</h3>'
 rendered+=f'<details class="figure-source-links"><summary>原文图页与点评 · {len(f["links"])} 项</summary>'
 md+=['','<a id="figure-references"></a>','### '+titles['figure-references']]
 for n,g in enumerate(f['links'],1):
  rendered+=f'<section class="linked-figure" id="figure-link-{n}"><p class="example-title"><strong><a href="{e(g["url"])}">{e(g["title"])} ↗</a></strong></p><p>{e(g["zh"])}</p><details class="short-example"><summary>English 与拆解</summary><p lang="en">{e(g["en"])}</p>'
  if g.get('analysis'):rendered+=f'<p>{e(g["analysis"])}</p>'
  rendered+='</details>'
  if g.get('source'):rendered+=f'<p class="example-source">{e(g["source"])}</p>'
  if g.get('license'):rendered+=f'<p class="example-source">{e(g["license"])}</p>'
  rendered+='</section>'
  md+=['',f'**[{g["title"]}]({g["url"]})**','',g['zh'],'',g['en']]
  if g.get('analysis'):md+=['',g['analysis']]
  if g.get('source'):md+=['',g['source']]
  if g.get('license'):md+=['',g['license']]
 rendered+='</details>'
 return rendered+'</section>',md

def render_skill(data):
 """Keep the portable entry point separate from the full reading guide."""
 e=html.escape
 skill=data['writing_skill']
 rendered=f'<details class="writing-skill" id="writing-skill"><summary>给 Codex 用：下载 PaperBank 写作 skill</summary><p>{e(skill["intro"])}</p>'
 rendered+=f'<p class="skill-links"><a href="{e(skill["download"])}" download>下载写作 skill ZIP</a> · <a href="{REPO}/blob/main/{e(skill["source"])}">查看 SKILL.md</a> · <a href="#general-rules">写作规则索引</a></p><p>解压后将整个 <code>paperbank-writing/</code> 文件夹交给 Codex。填文件、任务和修改范围即可。</p>'
 md=['','<a id="writing-skill"></a>','### PaperBank 写作 skill','',skill['intro'],'',f'[下载 ZIP](../{skill["download"]}) · [查看 SKILL.md](../{skill["source"]}) · [写作铁律](#general-rules)','','下载、解压，保留整个 paperbank-writing/ 文件夹，把它交给 Codex 读取；补上文件、任务和允许修改的范围。']
 ph,pm=render_codex_prompt(data,skill['prompt_ref'],'中文使用提示词','English usage prompt');rendered+=ph;md+=pm
 return rendered+'</details>',md

def package_skill(data):
 """Generate the skill reference from the same rules used by the website."""
 folder=ROOT/'skills/paperbank-writing'
 rules=data.get('skill_rules') or [i for i in data['items'] if i.get('iron_rule') or i['section']=='rules']
 md=['# PaperBank 写作检查参考','','按本次任务选规则。下面示例是假设情境，不是论文原文或实测；实际改稿先核对事实。','','网页：[写作铁律](https://da1yuqin.github.io/PaperBank/#general-rules) · [论文结构与逐句例子](https://da1yuqin.github.io/PaperBank/#paper-order) · [rebuttal](https://da1yuqin.github.io/PaperBank/#chapter-rebuttal)']
 for group in dict.fromkeys(i['group'] for i in rules):
  md+=['','## '+group,'']
  for i in [x for x in rules if x['group']==group]:
   md+=['',f'### 第 {i["id"][4:]} 条：{i["title"]}','',i['checklist'],'','适用边界：'+i['boundary']]
   _,example_md=render_example(i['examples'][0],data['references'])
   md+=example_md
 _,draft_md=render_quick_start(data,include_figures=False)
 md+=draft_md
 md+=['','## 全文表达要求与中英改写','',data['opening_lead']]
 for rule in data['refine_standards']:
  _,rm=render_paragraph(rule,data['references']);md+=rm
 md+=['','## 各章先回答什么']
 for section in data['sections']:
  if not section.get('manuscript') and section['id']!='rebuttal':continue
  md+=['','### '+section['nav'],'',section['purpose']]
  if section.get('principle'):md+=['',section['principle']]
 md+=['','## 各章完整句式模板']
 for lesson in data['refine_templates']:
  _,rm=render_paragraph(lesson,data['references']);md+=rm
 md+=['','## 绘图规则与图型','',data['figure_chapter']['lead']]
 for key in ['rules','types']:
  _,rm=render_short_rules(data['figure_chapter'][key]);md+=rm
 md+=['','原图与出处：[光速出美图](https://da1yuqin.github.io/PaperBank/#figure-gallery)。第三方图片不随 skill 分发。']
 md+=['','---','','原创规则与教学示例：Da1yuqin / PaperBank，[原文](https://da1yuqin.github.io/PaperBank/)，[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)。转载保留署名、出处及许可，改编注明改动。']
 (folder/'references').mkdir(parents=True,exist_ok=True)
 (folder/'references/checklist.md').write_text('\n'.join(md)+'\n',encoding='utf-8')
 package_prompt_reference(data,folder,data['codex_prompts'])
 with zipfile.ZipFile(ROOT/data['writing_skill']['download'],'w',zipfile.ZIP_DEFLATED) as z:
  for name in ['SKILL.md','references/checklist.md','references/prompts.md','LICENSE']:
   info=zipfile.ZipInfo('paperbank-writing/'+name,date_time=(2026,10,7,0,0,0))
   info.compress_type=zipfile.ZIP_DEFLATED
   info.external_attr=0o644<<16
   z.writestr(info,(folder/name).read_bytes())

def package_figure_skill(data):
 """Publish generic drawing rules without private profiles or paper images."""
 figures=data['figure_chapter'];skill=figures['skill']
 folder=ROOT/Path(skill['source']).parent
 (folder/'references').mkdir(parents=True,exist_ok=True)
 (folder/'SKILL.md').write_text(skill['instructions'],encoding='utf-8')
 md=['# PaperBank 绘图参考','',figures['lead'],'','先查铁律，再按图型选模板。这里的中英句式是教学例子，数值和口径用自己的实际记录。','','## 绘图铁律']
 for key,title in [('rules','绘图铁律'),('types','按图的任务选模板')]:
  if key=='types':md+=['','## '+title]
  for rule in figures[key]:
   _,rm=render_short_rules([rule]);md+=rm
   links=[f'[{v["title"]}](https://da1yuqin.github.io/PaperBank/#{v["id"]})' for v in figures['visual_examples'] if v['id'] in rule.get('visuals',[])]
   if links:md+=['','图例与拆解：'+' · '.join(links)]
 md+=['','---','','Da1yuqin / PaperBank，[原文](https://da1yuqin.github.io/PaperBank/#figures)，[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)。转载保留署名、出处与许可；改编注明改动。第三方原图不随包分发。']
 (folder/'references/rules.md').write_text('\n'.join(md)+'\n',encoding='utf-8')
 package_prompt_reference(data,folder,['figures'])
 license_text=(ROOT/'skills/paperbank-writing/LICENSE').read_text(encoding='utf-8').replace('Writing Skill','Drawing Skill').replace('references/checklist.md','references/rules.md').replace('paperbank-writing','paperbank-figures')
 (folder/'LICENSE').write_text(license_text,encoding='utf-8')
 with zipfile.ZipFile(ROOT/skill['download'],'w',zipfile.ZIP_DEFLATED) as z:
  for name in ['SKILL.md','references/rules.md','references/prompts.md','LICENSE']:
   info=zipfile.ZipInfo('paperbank-figures/'+name,date_time=(2026,10,7,0,0,0))
   info.compress_type=zipfile.ZIP_DEFLATED
   info.external_attr=0o644<<16
   z.writestr(info,(folder/name).read_bytes())

def render_tools(data):
 """Render linked resources separately from manuscript checks."""
 e=html.escape
 groups=data.get('tools',[])
 intro='按用途选。以下整理自公开文档，未逐项安装；版本和许可见原项目。'
 rendered=f'<section class="toolbox major-chapter" id="tools"><h2>5. 我推荐的 AI 工具</h2><p class="chapter-desc">{e(intro)}</p>'
 rendered+='<p class="tool-index">'+ ' · '.join(f'<a href="#tools-{e(g["id"])}">5.{n} {e(g["title"])}</a>' for n,g in enumerate(groups,1))+f' · <a href="#code-release-prompt">5.{len(groups)+1} 开源整理提示词</a></p>'
 total=sum(len(g['items']) for g in groups)
 rendered+=f'<div class="tool-search js-only"><label for="tool-search">搜索工具</label><input type="search" id="tool-search" placeholder="搜 Zotero、画图、引用……"><span id="tool-count" role="status" aria-live="polite">{total} 项资源</span></div>'
 md=['','<a id="tools"></a>','## 5. 我推荐的 AI 工具','',intro,'','核对日期：'+data['tools_checked_at']+'。']
 for n,group in enumerate(groups,1):
  rendered+=f'<section class="tool-group" id="tools-{e(group["id"])}"><h3>5.{n} {e(group["title"])}</h3><ul class="tool-list">'
  md+=['',f'### 5.{n} {group["title"]}','']
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
 title=f'5.{len(groups)+1} 开源整理：翻译注释，清掉私货，保留行为'
 rendered+=f'<section class="release-prompt" id="code-release-prompt"><h3>{e(title)}</h3><p>先写清允许处理的文件。中文界面、接口字符串、业务路径也可能影响运行，不能一键全换。下面中英两版都可复制。</p>'
 md+=['','<a id="code-release-prompt"></a>','### '+title,'','先写清允许处理的文件。中文界面、接口字符串、业务路径也可能影响运行，不能一键全换。']
 ph,pm=render_codex_prompt(data,data['code_release_prompt']['prompt_ref'],'中文提示词');rendered+=ph;md+=pm
 rendered+=f'<p class="tool-checked">文档核对：{e(data["tools_checked_at"])}。安装、版本和许可见项目原文。</p></section></section>'
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
 preface,preface_md=render_preface(data)
 quick_start,quick_md=render_quick_start(data)
 figures,figures_md=render_figures(data)
 opening,opening_md=render_opening(data)
 skill,skill_md=render_skill(data)
 draft_nav=''.join(f'<a href="#{e(s["id"])}">{e(s["title_zh"])}</a>' for s in data['quick_start']['steps'])
 figure_nav=''.join(f'<a href="#{key}">2.{n} {e(title)}</a>' for n,(key,title) in enumerate(FIGURE_SECTIONS,1))
 rebuttal_nav=''.join(f'<a href="#{e(p["id"])}">{e(p["title"])}</a>' for p in data['refine_templates'] if p['section']=='rebuttal')
 tools_nav=''.join(f'<a href="#tools-{e(g["id"])}">5.{n} {e(g["title"])}</a>' for n,g in enumerate(data['tools'],1))
 tools_nav+=f'<a href="#code-release-prompt">5.{len(data["tools"])+1} 开源整理提示词</a>'
 nav='<a href="#general-rules">3.1 全文规范</a>'
 for s in sections:
  if not s.get('manuscript'):continue
  group=[i for i in items if i['section']==s['id']]
  number=int(s['number'])+1
  nav+=f'<a href="#chapter-{s["id"]}">3.{number} {e(s["nav"])}</a>'
 entries='';chapter_html={};chapter_md={}
 md=['# '+data['site_title'],'','先用 Codex 拉草稿和图，再由你审逻辑、逐章精修。第四章写 Rebuttal，第五章收好用的工具。','','主要面向方法与实证研究；按学科、研究类型和投稿要求调整。模拟段落明确标注，真实论文摘录另给出处与版本。','','欢迎使用、改写、转载，也欢迎拿去给 Codex 做 skill。原创内容采用 CC BY 4.0，论文摘录与图片保留各自许可。转载原创内容请保留作者 Da1yuqin、[原文链接](https://Da1yuqin.github.io/PaperBank/)和 [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) 许可，改过请注明。Star 自愿，署名别失联。']
 md+=quick_md+skill_md+figures_md+['','<a id="refine"></a>','## 3. 古法精修','','先查全文，再逐节改。模板中的【】填自己的材料，段落按内容调整。','']+['','<a id="rules"></a>']+opening_md+['','### 本章目录','']
 md += [f'- [{section_label(s)}{s["title"]}](#{s["id"]})' for s in sections]
 md += ['- [好用工具与开源整理提示词](#tools)']
 for s in sections:
  html_start=len(entries);md_start=len(md)
  group=[i for i in items if i['section']==s['id']]
  purpose=s.get('purpose') or s.get('summary') or s['description']
  prefix='4. ' if s['id']=='rebuttal' else ('3.'+str(int(s['number'])+1)+' ' if s.get('manuscript') else '')
  heading_level=2 if s['id']=='rebuttal' else 3
  entries+=f'<section class="chapter" id="chapter-{s["id"]}"><div class="chapter-head"><h{heading_level}>{prefix}{e(s["title"])}</h{heading_level}></div><p class="chapter-desc"><strong>{e(purpose)}</strong></p>'
  md+=['',f'<a id="{s["id"]}"></a>',f'{"#"*heading_level} {prefix}{s["title"]}','',purpose]
  if s.get('principle'):
   entries+=f'<p class="chapter-principle">{e(s["principle"])}</p>'
   md+=['',s['principle']]
  templates=[p for p in data.get('refine_templates',[]) if p['section']==s['id']]
  for n,lesson in enumerate(templates):
   number=f'{prefix.strip()}.{chr(97+n)}' if s.get('manuscript') and len(templates)>1 else None
   lesson_html,lesson_md=render_paragraph(lesson,refs,md_level=3 if s['id']=='rebuttal' else 4,number=number,heading=len(templates)>1 or s['id']=='rebuttal')
   entries+=lesson_html;md+=lesson_md
  if any(p['section']==s['id'] for p in lessons):
   entries+='<details class="more-lessons"><summary>更多例子：论文原句与拆解</summary>'
   md+=['','<details><summary>更多例子：论文原句与拆解</summary>','']
  for lesson in [p for p in lessons if p['section']==s['id']]:
   lesson_html,lesson_md=render_paragraph(lesson,refs,heading=False)
   entries+=lesson_html
   if lesson.get('label') and lesson['label'] not in lesson_md:
    at=lesson_md.index(lesson['purpose'])+1
    lesson_md[at:at]=['',lesson['label']]
   md+=lesson_md
  if any(p['section']==s['id'] for p in lessons):
   entries+='</details>';md+=['','</details>','']
  entries+='</section>'
  chapter_html[s['id']]=entries[html_start:];chapter_md[s['id']]=md[md_start:]
 entries=''.join(chapter_html[s['id']] for s in sections if s.get('manuscript'))
 md=md[:1]+preface_md+md[1:7]+quick_md+skill_md+figures_md+['','<a id="refine"></a>','## 3. 古法精修','','先查全文，再逐节改。模板中的【】填自己的材料，段落按内容调整。','']+opening_md+['','### 本章目录','']
 md+=[f'- [3.{int(s["number"])+1} {s["nav"]}](#{s["id"]})' for s in sections if s.get('manuscript')]
 for s in sections:
  if s.get('manuscript'):md+=chapter_md[s['id']]
 examples=sum(len(i.get('examples',[])) for i in items)
 rebuttal='<section class="major-chapter" id="rebuttal">'+chapter_html['rebuttal']+'</section>'
 ph,pm=render_codex_prompt(data,data['rebuttal_prompt']['prompt_ref'],'复制给 Codex：Rebuttal + revise loop','Rebuttal + revise loop · English')
 rebuttal=rebuttal[:-len('</section>')]+ph+'</section>'
 md+=chapter_md['rebuttal']+pm
 tools,tools_md=render_tools(data)
 md+=tools_md
 reading=''.join(f'<li>{link(k)}<span> — {e(r["scope"])}</span></li>' for k,r in refs.items() if r.get('public'))
 t=(ROOT/'assets/template.html').read_text(encoding='utf-8')
 for k,v in {'TITLE':e(data['site_title']),'PREFACE':preface,'NAV':nav,'DRAFT_NAV':draft_nav,'FIGURE_NAV':figure_nav,'REBUTTAL_NAV':rebuttal_nav,'TOOLS_NAV':tools_nav,'ENTRIES':entries,'TOOLS':tools,'REBUTTAL':rebuttal,'QUICK_START':quick_start,'FIGURES':figures,'OPENING':opening,'SKILL':skill,'READING':reading,'TOTAL':str(len(items)),'CHAPTERS':'5','EXAMPLES':str(examples)}.items():t=t.replace('{{'+k+'}}',v)
 (ROOT/'index.html').write_text(t,encoding='utf-8')
 (ROOT/'book').mkdir(exist_ok=True)
 md+=['','## 参考阅读','']+[f'- [{r["title"]}]({r["url"]})：{r["scope"]}' for r in refs.values() if r.get('public')]
 (ROOT/'book/guide.md').write_text('\n'.join(md)+'\n',encoding='utf-8')
 package_skill(data)
 package_figure_skill(data)
 print(f'Built 5 chapters, {len(lessons)+len(data.get("refine_templates",[]))} paragraph lessons.')

if __name__=='__main__':
 p=argparse.ArgumentParser(description=__doc__)
 p.add_argument('--serve',action='store_true');p.add_argument('--port',type=int,default=8000)
 a=p.parse_args();build()
 if a.serve:
  print(f'Preview: http://127.0.0.1:{a.port}',flush=True)
  ThreadingHTTPServer(('127.0.0.1',a.port),partial(SimpleHTTPRequestHandler,directory=str(ROOT))).serve_forever()
