#!/usr/bin/env python3
"""Build PaperBank and StrongResponse; use --serve to preview with Python 3."""
import argparse
import html
import json
import re
import zipfile
from copy import deepcopy
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

ROOT = Path(__file__).resolve().parent
REPO = 'https://github.com/Da1yuqin/PaperBank'
FIGURE_SECTIONS = [
 ('figure-mainfig','Mainfig：研究动机与贡献'),
 ('figure-framework','Framework：方法流程与设计作用'),
 ('figure-skill','绘图准备'),
 ('figure-rules','绘图规范'),
 ('figure-types','统计图与案例图'),
 ('notion-gallery','图例与说明'),
 ('figure-references','补充参考'),
]

def rule_html(text):
 """Render explicit rule labels; do not infer hard rules from prose."""
 label='【铁律】'
 return ('<span class="iron-law">铁律</span> '+html.escape(text[len(label):]) if text.startswith(label) else html.escape(text))

def render_codex_prompt(data, key, label_zh, label_en='English prompt'):
 """Use one skill-grounded prompt for the page and portable references."""
 e=html.escape;prompt=data['codex_prompts'][key]
 rendered='';md=[]
 languages=[('zh',label_zh,'zh-CN')]
 if not data.get('_tutorial_layout'):languages.append(('en',label_en,'en'))
 for language,label,lang in languages:
  text=prompt[language]
  rendered+=f'<details class="prompt" data-prompt-ref="{e(key)}" data-prompt-lang="{language}"><summary>{e(label)}</summary><pre lang="{lang}">{e(text)}</pre><button class="copy js-only">复制提示词</button></details>'
  md+=['','**'+label+'**','','```text',text,'```']
 source=(f'{REPO}/blob/main/skills/{prompt["skill"]}/references/prompts.md#{key}' if prompt['skill'] else f'{REPO}/blob/main/data/guide.json')
 rendered+=f'<p class="example-source">依据：{e(" · ".join(prompt["sources"]))} · <a href="{e(source)}">对应铁律与完整提示词</a></p>'
 md+=['','依据：'+' · '.join(prompt['sources'])+f' · [对应铁律与完整提示词]({source})']
 return rendered,md

def package_prompt_reference(data, folder, keys):
 lead=('填写【】后使用。材料权限、证据与当轮回复规定先确认；不附真实审稿记录，不推测审稿人身份或评分变化。' if folder.name=='rebuttal' else '填写【】后使用。以下采用适用于实证型 CS 论文的通用规则；不套用某篇论文的固定宽度、色值、模型阵容或重复次数。Nature 系列使用独立体系。')
 md=['# 给 Codex 的提示词','',lead,'']
 for key in keys:
  prompt=data['codex_prompts'][key]
  md+=['',f'<a id="{key}"></a>','## '+prompt['title'],'','依据：'+' · '.join(prompt['sources'])+'。','', '对应规则：'+'；'.join(prompt['basis'])+'。']
  for lang,label in [('zh','中文'),('en','English')]:
   md+=['','### '+label,'','```text',prompt[lang],'```']
 md+=['','---','','Da1yuqin / PaperBank，[原文](https://da1yuqin.github.io/PaperBank/)，[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)。']
 (folder/'references/prompts.md').write_text('\n'.join(md)+'\n',encoding='utf-8')

def section_label(section):
 return '先读 · ' if int(section['number'])==0 else str(int(section['number']))+'. '

def render_writing_templates(content, section):
 """Keep reusable fill-in paragraphs together, separate from paper excerpts."""
 e=html.escape;key=section+'-writing-templates'
 rendered=f'<section class="writing-templates" id="{key}"><h4>{e(content["title"])}</h4><p>{e(content["lead"])}</p>'
 md=['',f'<a id="{key}"></a>','#### '+content['title'],'',content['lead']]
 for template in content['templates']:
  rendered+=f'<details class="chapter-templates writing-template" id="{e(template["id"])}"><summary>{e(template["title"])}</summary><div class="paragraph-lesson writing-template-body" data-section="{section}"><p class="template-purpose">{e(template["when"])}</p>'
  md+=['',f'<a id="{template["id"]}"></a>',f'<details><summary>{template["title"]}</summary>','',template['when']]
  for paragraph in template['paragraphs']:
   text=paragraph['text']
   display=e(re.sub(r'(Table|Figure)~\\ref\{(\[[^\]]+\])\}',r'\1 \2',text))
   display=re.sub(r'\\textbf\{([^{}]*)\}',r'<strong>\1</strong>',display)
   tag='pre' if paragraph.get('format')=='latex' else 'p'
   rendered+=f'<div class="template-paragraph"><h5>{e(paragraph["heading"])}</h5><{tag} lang="en" class="template-text" data-template-raw="{e(text,quote=True)}">{display}</{tag}><p class="template-guidance">{rule_html(paragraph["note"])}</p></div>'
   md+=['','**'+paragraph['heading']+'**','']+(['```latex',text,'```'] if tag=='pre' else [text])+['',paragraph['note']]
  rendered+='<button type="button" class="copy js-only" data-copy-writing-template data-copy-label="复制完整模板">复制完整模板</button></div></details>'
  md+=['','</details>']
 return rendered+'</section>',md

def render_intro_connections(data):
 """Show concrete paragraph hooks and aligned Abstract–Introduction claims."""
 content=data['intro_connections'];e=html.escape
 rendered=f'<section class="paragraph-lesson intro-connections" id="intro-hooks" data-section="intro"><h4>{e(content["title"])}</h4><p>{e(content["lead"])}</p>'
 md=['','<a id="intro-hooks"></a>','#### '+content['title'],'',content['lead'],'']
 rendered+=f'<figure class="argument-map" id="abstract-intro-map"><figcaption>{e(content["map_title"])}</figcaption><p class="lesson-context">{e(content["map_note"])}</p>'
 md+=['','<a id="abstract-intro-map"></a>','#### '+content['map_title'],'',content['map_note'],'']
 for pair in content['pairs']:
  key='argument-'+pair['id'];rendered+=f'<div class="argument-pair tone-{pair["tone"]}">'
  for side in ('abstract','intro'):
   text=pair[side];quote=pair[side+'_mark'];assert text.count(quote)==1
   before,after=text.split(quote,1)
   marked=e(before)+'<mark class="argument-mark">'+e(quote)+'</mark>'+e(after)
   rendered+=f'<div class="argument-quote argument-{side}"><p class="argument-role">{("Abstract" if side=="abstract" else "Intro")} · {e(pair["label"])}</p><p lang="en">'
   rendered+=(f'<a href="#{e(pair["link"])}">{marked}</a>' if side=='intro' else marked)
   rendered+='</p></div>'
   if side=='abstract':
    rendered+=f'<div class="argument-arrow" data-annotation-exclude><span class="argument-relation">{e(pair["relation"])}</span><svg viewBox="0 0 100 100" preserveAspectRatio="none" aria-hidden="true"><defs><marker id="{key}-tip" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0 0 L10 5 L0 10 Z" fill="currentColor"/></marker></defs><path class="argument-link" d="M 5 55 C 35 55, 65 55, 93 55" fill="none" stroke="currentColor" stroke-width="1.5" vector-effect="non-scaling-stroke" marker-end="url(#{key}-tip)"/></svg></div>'
  rendered+='</div>'
  md+=['','**'+pair['label']+' · '+pair['relation']+'**','', '**Abstract**：'+pair['abstract'],'','**Intro**：'+pair['intro'],f' · [查看对应关系](#{pair["link"]})']
 rendered+='</figure>'
 body_html,body_md=render_intro_body_map(data['tutorial_layout']['intro_body_map'])
 return rendered+body_html+'</section>',md+body_md

def render_intro_body_map(content):
 """Connect each Introduction function to its concrete manuscript destinations."""
 e=html.escape
 def highlight(text,quote):
  assert text.count(quote)==1,(text,quote)
  before,after=text.split(quote,1)
  return e(before)+'<mark class="argument-mark">'+e(quote)+'</mark>'+e(after)
 rendered=f'<figure class="intro-body-map" id="intro-body-map"><figcaption>{e(content["title"])}</figcaption><p>{e(content["lead"])}</p><p class="lesson-context">{e(content["caption"])}</p><div class="map-legend">'
 md=['','<a id="intro-body-map"></a>','#### '+content['title'],'',content['lead'],'',content['caption']]
 for item in content['legend']:
  rendered+=f'<p><strong>{e(item["key"])} · {e(item["label"])}</strong>：{e(item["text"])}</p>'
  md+=['',f'- **{item["key"]} · {item["label"]}：**{item["text"]}']
 rendered+='</div><p class="map-column-labels"><span>引言句子的任务</span><span>正文怎样展开与检验</span></p>'
 for n,row in enumerate(content['rows']):
  key='intro-map-'+row['id']
  rendered+=f'<div class="intro-body-row tone-{n%5}" id="{e(key)}"><div class="intro-map-source"><p class="argument-role">{e(row["key"])} · {e(row["label"])}</p><p>{highlight(row["intro_sentence"],row["intro_mark"])}</p><p class="map-hook"><strong>句首钩子</strong><code lang="en">{e(row["hook"])}</code></p><p class="map-check">{e(row["check"])}</p></div>'
  rendered+=f'<div class="intro-map-arrows" aria-hidden="true"><svg viewBox="0 0 100 100" preserveAspectRatio="none"><defs><marker id="{key}-tip" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5" markerHeight="5" orient="auto"><path d="M0 0 L10 5 L0 10 Z" fill="currentColor"/></marker></defs>'
  for target in row['targets']:
   rendered+=f'<path class="intro-body-link" d="M 4 50 C 35 50, 65 50, 95 50" fill="none" stroke="currentColor" stroke-width="1.3" vector-effect="non-scaling-stroke" marker-end="url(#{key}-tip)"/>'
  rendered+='</svg></div><div class="intro-map-targets">'
  md+=['','**'+row['key']+' · '+row['label']+'**','',row['intro_sentence'],'','句首钩子：`'+row['hook']+'`','']
  for target in row['targets']:
   rendered+=f'<a class="intro-map-target" href="#{e(target["link"])}"><p class="argument-role">{e(target["chapter"])} · {e(target["role"])}</p><p>{highlight(target["text"],target["mark"])}</p></a>'
   md+=['- ['+target['chapter']+'](#'+target['link']+') · '+target['role']+'：'+target['text']]
  rendered+='</div></div>';md+=['',row['check']]
 rendered+='<div class="map-return">'
 for chain in content['chains']:
  rendered+=f'<p><strong>{e(chain["key"])}</strong>：{e(chain["text"])}</p>';md+=['',chain['key']+'：'+chain['text']]
 rendered+=f'<p><strong>结果回写</strong>：{e(content["return_path"])}</p></div></figure>'
 md+=['','**结果回写**：'+content['return_path']]
 return rendered,md

def render_annotated_paragraph(example, refs, number=None, heading_level=4, workflow=False):
 """Keep source paragraphs intact and place matched comments beside them."""
 e=html.escape;key=example['id']
 assert len(example['paragraphs'])==1,(key,'one natural paragraph per case')
 english_label='English 原文' if example.get('source') else 'English 教学改写'
 title=(number+' ' if number else '')+example['title']
 rendered=f'<section class="paragraph-lesson annotated-example" id="{e(key)}" data-section="{e(example["section"])}">'
 if not workflow:rendered+=f'<h{heading_level}>{e(title)}</h{heading_level}><p class="lesson-context">{e(example["label"])}</p>'
 languages=[lang for lang in ('en','zh') if lang in example['paragraphs'][0]]
 labels={'en':english_label,'zh':'中文译文' if 'en' in languages else '流程说明'}
 if len(languages)>1:
  rendered+='<div class="paragraph-language js-only" role="group" aria-label="案例语言" data-annotation-exclude>'
  for lang in languages:
   rendered+=f'<button type="button" data-paragraph-language="{lang}" aria-pressed="{str(lang==languages[0]).lower()}" aria-controls="{e(key)}-{lang}">{labels[lang]}</button>'
  rendered+='</div>'
 md=['',f'<a id="{key}"></a>']
 if not workflow:md+=['','#'*heading_level+' '+title,'',example['label']]
 for lang in languages:
  language='en' if lang=='en' else 'zh-CN'
  rendered+=f'<div class="annotated-panel" id="{e(key)}-{lang}" data-paragraph-panel="{lang}">'
  md+=['','**'+labels[lang]+'**','']
  for n,paragraph in enumerate(example['paragraphs']):
   rendered+=f'<div class="annotated-row"><div class="annotated-text" lang="{language}">'
   text=paragraph[lang];marks=[]
   for i,note in enumerate(example['annotations'],1):
    if note['paragraph']!=n:continue
    quote=note[lang];assert text.count(quote)==1,(key,lang,quote)
    start=text.index(quote);marks.append((start,start+len(quote),i))
   marked='';end=0
   for start,stop,i in sorted(marks):
    assert start>=end,(key,'overlapping highlights')
    note_key=f'{key}-{lang}-{i}'
    marked+=e(text[end:start])+f'<mark class="paragraph-highlight tone-{(i-1)%5}" tabindex="0" data-note-key="{e(note_key)}" aria-describedby="{e(note_key)}">{e(text[start:stop])}<sup data-annotation-exclude>{i}</sup></mark>'
    end=stop
   rendered+='<p>'+marked+e(text[end:])+'</p></div><aside class="paragraph-notes" aria-label="段落写法批注" data-annotation-exclude>';md+=[text,'']
   for i,note in enumerate(example['annotations'],1):
    if note['paragraph']!=n:continue
    note_key=f'{key}-{lang}-{i}'
    rendered+=f'<div class="paragraph-note tone-{(i-1)%5}" id="{e(note_key)}" data-note-key="{e(note_key)}" tabindex="0"><p class="note-title"><span>{i}</span>{rule_html(note["title"])}</p><p>{e(note["body"])}</p></div>'
   rendered+='</aside></div>'
  rendered+='</div>'
 md+=['','**高亮与旁批**','']
 for i,note in enumerate(example['annotations'],1):
  md+=[f'{i}. **'+(' / '.join(note[lang] for lang in languages))+f'**：{note["title"]}。{note["body"]}']
 if example.get('source'):
  r=refs[example['source']]
  source=f'<a href="{e(r["url"])}">{e(example["paper_label"])}</a> · {e(example["location"])}'
  source_md=f'[{example["paper_label"]}]({r["url"]}) · {example["location"]}'
  rights=r['license']
 else:
  source=source_md=example.get('source_label','PaperBank · 教学改写')
  rights='本指南原创内容采用 CC BY 4.0；转载请附作者、原文链接与许可，改写注明改动。'
 if not workflow:rendered+=f'<p class="example-source">{source}</p><details class="annotation-rights"><summary>出处与复用范围</summary><p>{e(example["processing"])}</p><p>{e(rights)}</p></details>'
 rendered+='</section>'
 if not workflow:md+=['',source_md,'',example['processing'],'',rights]
 return rendered,md

def render_paragraph(lesson, refs, md_level=4, number=None, heading=True, compact=False):
 """Show the paragraph's job before explaining its sentences."""
 e=html.escape
 title=(number+' ' if number else '')+lesson['title']
 if compact:
  template=lesson.get('latex_template')
  if not template:return '',[]
  rendered=f'<section class="paragraph-lesson template-only" id="{e(lesson["id"])}" data-section="{e(lesson["section"])}"><h4>{e(title)}</h4><pre>{e(template)}</pre><button class="copy js-only" data-copy-label="复制模板">复制模板</button></section>'
  return rendered,['','#### '+title,'','```latex',template,'```']
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
  rendered+=f'<details class="prompt full-template"><summary>完整 LaTeX 结构模板</summary><pre>{e(lesson["latex_template"])}</pre><button class="copy js-only">复制提示词</button></details>'
  md+=['','**完整 LaTeX 结构模板**','','```latex',lesson['latex_template'],'```']
 return rendered+'</section>',md

def render_opening(data):
 e=html.escape
 lead=data.get('refine_global_lead',data['opening_lead'])
 rendered='<section class="opening-rules" id="general-rules"><h3>3.1 全文规范</h3><p>'+e(lead)+'</p>'
 md=['','<a id="general-rules"></a>','### 3.1 全文规范','',lead]
 for n,group in enumerate(data['refine_standard_groups']):
  title=group['title']
  rendered+=f'<h4>{e(title)}</h4><ul class="compact-rules">';md+=['','#### '+title]
  for rule in [r for r in data['refine_standards'] if r['group']==group['id']]:
   rendered+=f'<li id="{rule["id"]}"><strong>{rule_html(rule["title"])}：</strong>{e(rule["purpose"])}</li>'
   md+=['',f'- **{rule["title"]}：**{rule["purpose"]}']
  rendered+='</ul>'
 for example in data.get('refine_global_cases',[]):
  case_html,case_md=render_annotated_paragraph(example,data['references'])
  rendered+=case_html;md+=case_md
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
 skill=data['writing_skill']
 rendered='<p class="site-switch">写作与绘图：PaperBank · 审稿回复：<a href="StrongResponse/">💪StrongResponse【这边也长出肌肉】</a></p>'
 rendered+=f'<p class="skill-links"><strong>这里有两个可以直接使用的 skill，按任务下载。</strong> <a href="{e(skill["download"])}" download>cs-paper-writing</a> · <a href="{e(data["figure_chapter"]["skill"]["download"])}" download>绘图</a> · <a href="#writing-skill">用法</a></p>'
 rendered+=f'<figure class="accept-banner"><img src="{e(p["image"])}" alt="{e(p["image_alt"])}" width="1672" height="941" fetchpriority="high"></figure><section class="preface" id="preface"><h2>{e(p["title"])}</h2>'
 rendered+=''.join(f'<p>{e(text)}</p>' for text in p['paragraphs'])
 rendered+=f'<p class="preface-aside"><em>{e(p["aside"])}</em></p>'
 rendered+='</section>'
 md=['','写作与绘图：PaperBank · 审稿回复：[💪StrongResponse【这边也长出肌肉】](https://da1yuqin.github.io/PaperBank/StrongResponse/)','这里有两个可以直接使用的 skill，按任务下载。',f'[cs-paper-writing](../{skill["download"]}) · [绘图](../{data["figure_chapter"]["skill"]["download"]}) · [用法](#writing-skill)','',f'![{p["image_alt"]}](../{p["image"]})','','## '+p['title'],'']
 md+=sum(([text,''] for text in p['paragraphs']),[])
 md+=['*'+p['aside']+'*','']
 return rendered,md

def render_figure_case(visual, notes=None):
 """Keep the original figure and its reading guidance in one place."""
 e=html.escape;v=visual
 notes=notes or [{'title':f'观察 {n}','body':text} for n,text in enumerate(v.get('analysis_zh',[]),1)]
 figure_class=' single-column-figure' if v.get('layout')=='single-column' else ''
 rendered=f'<section class="visual-example" id="{e(v["id"])}"><h4>{e(v["title"])}</h4><figure class="{figure_class.strip()}"><a href="{e(v["asset"])}"><img src="{e(v["asset"])}" alt="{e(v["title"])}" loading="lazy"></a><figcaption>{e(v.get("zh",""))}</figcaption></figure><p class="figure-guidance">'
 md=['',f'<a id="{v["id"]}"></a>','#### '+v['title'],'',f'![{v["title"]}](../{v["asset"]})','',v.get('zh','')]
 for n,note in enumerate(notes,1):
  rendered+=e(note['body'])+' '
  md+=['',f'{n}. **{note["title"]}：**{note["body"]}']
 rendered+='</p>'
 if v.get('source_url'):
  rendered+=f'<p class="example-source"><a href="{e(v["source_url"])}">{e(v["source_title"])}</a></p>'
  url=v['source_url'] if '://' in v['source_url'] else '../'+v['source_url']
  md+=['',f'[{v["source_title"]}]({url})']
 rendered+=f'<p class="example-source">{e(v.get("license",""))}'
 if v.get('license_url'):rendered+=f' · <a href="{e(v["license_url"])}">许可</a>'
 rendered+='</p></section>';md+=['',v.get('license','')]
 return rendered,md

def render_paper_outline(content):
 e=html.escape
 key=content['id']
 rendered=f'<figure class="paper-outline" id="{e(key)}"><figcaption>{e(content["title"])}</figcaption><p class="lesson-context">{e(content["caption"])}</p><p class="outline-abstract">{e(content["abstract"])}</p>'
 md=['',f'<a id="{key}"></a>','#### '+content['title'],'',content['caption'],'',content['abstract']]
 def chapter(node):
  block=f'<div class="outline-section"><p><strong><a href="#{e(node["link"])}">{e(node["title"])}</a></strong></p><p>{e(node["summary"])}</p>'
  lines=['','**'+node['title']+'**','',node['summary']]
  if node.get('parts'):
   block+='<ul class="outline-parts">'
   for part in node['parts']:
    block+=f'<li><strong>{e(part["title"])}</strong>：{e(part["text"])}</li>'
    lines+=['','- **'+part['title']+'**：'+part['text']]
   block+='</ul>'
  block+='</div>'
  if node['bridge']:
   block+=f'<p class="outline-bridge"><span aria-hidden="true">↓</span>{e(node["bridge"])}</p>';lines+=['','↓ '+node['bridge']]
  return block,lines
 for node in content['before_method']:
  h,m=chapter(node);rendered+=h;md+=m
 method=content['method']
 rendered+=f'<div class="outline-method"><p><strong><a href="#chapter-method">{e(method["title"])}</a></strong></p><div class="overview-node"><p>{e(method["overview"])}</p></div><div class="overview-arrow" aria-hidden="true"><span>概括圈内各小节的职责与交接</span><svg viewBox="0 0 100 48"><defs><marker id="{key}-overview-tip" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0 0 L10 5 L0 10 Z" fill="currentColor"/></marker></defs><path d="M50 2 L50 43" stroke="currentColor" stroke-width="1.5" fill="none" marker-end="url(#{key}-overview-tip)"/></svg></div><div class="method-main-group"><p class="method-formulation"><strong>{e(method["formulation"]["title"])}</strong> · {e(method["formulation"]["summary"])}</p><div class="method-stages">'
 md+=['','**'+method['title']+'**','',method['overview'],'','↓ 概括各小节的职责与交接','',method['formulation']['title']+'：'+method['formulation']['summary']]
 for n,stage in enumerate(method['stages']):
  if n:rendered+='<span class="method-stage-arrow"><span aria-hidden="true">→</span><small>'+e(stage['handoff'])+'</small></span>'
  rendered+=f'<div class="method-stage"><p><strong>{e(stage["title"])}</strong></p><p><span>输入</span> {e(stage["input"])}</p><p>{e(stage["operation"])}</p><p><span>输出</span> {e(stage["output"])}</p></div>'
  md+=['','- **'+stage['title']+'**：'+stage['input']+' → '+stage['operation']+' → '+stage['output']]
 rendered+=f'</div><p class="method-input-route">{e(method["routing"])}</p></div></div><p class="outline-bridge"><span aria-hidden="true">↓</span>{e(method["bridge"])}</p>';md+=['',method['routing'],'','↓ '+method['bridge']]
 if method.get('variants'):
  rendered+='<p class="outline-variants">'+e(method['variants'])+'</p>';md+=['',method['variants']]
 for node in content['after_method']:
  h,m=chapter(node);rendered+=h;md+=m
 rendered+=f'<p class="outline-supplements">{e(content["supplements"])}</p>';md+=['',content['supplements']]
 if content.get('source'):
  source=content['source']
  rendered+=f'<p class="example-source"><a href="{e(source["url"])}">{e(source["title"])}</a> · {e(source["note"])}</p>'
  md+=['',f'[{source["title"]}]({source["url"]}) · {source["note"]}']
 return rendered+'</figure>',md

def render_organization_templates(content):
 """Choose the manuscript argument before assigning sections."""
 e=html.escape
 rendered=f'<h4>{e(content["title"])}</h4><p>{e(content["lead"])}</p><div class="organization-table-wrap"><table class="organization-table"><caption>按主要贡献选择全文组织</caption><thead><tr><th scope="col">论文类型</th><th scope="col">引言的论证顺序</th><th scope="col">正文的展开顺序</th></tr></thead><tbody>'
 md=['','#### '+content['title'],'',content['lead'],'','| 论文类型 | 引言的论证顺序 | 正文的展开顺序 |','| --- | --- | --- |']
 for pattern in content['patterns']:
  rendered+=f'<tr><th scope="row"><a href="#{e(pattern["id"])}">{e(pattern["title"])}</a></th><td>{e(pattern["intro_chain"])}</td><td>{e(pattern["body_chain"])}</td></tr>'
  md+=['| ['+pattern['title']+'](#'+pattern['id']+') | '+pattern['intro_chain']+' | '+pattern['body_chain']+' |']
 rendered+='</tbody></table></div>'
 for pattern in content['patterns']:
  rendered+=f'<details class="organization-template" id="{e(pattern["id"])}"><summary>{e(pattern["title"])}：大纲与章节衔接</summary><p>{e(pattern["when"])}</p>'
  md+=['',f'<a id="{pattern["id"]}"></a>','<details><summary>'+pattern['title']+'：大纲与章节衔接</summary>','',pattern['when']]
  ph,pm=render_paper_outline(pattern['outline']);rendered+=ph+'</details>';md+=pm+['','</details>']
 rendered+=f'<p class="outline-variants">{e(content["variant_note"])}</p><h4 id="draft-contribution-format">{e(content["contributions"]["title"])}</h4>'
 md+=['',content['variant_note'],'','<a id="draft-contribution-format"></a>','#### '+content['contributions']['title']]
 for rule in content['contributions']['rules']:
  rendered+=f'<p>{rule_html(rule)}</p>';md+=['',rule]
 rendered+=f'<details class="prompt"><summary>贡献列表：LaTeX 格式</summary><pre>{e(content["contributions"]["code"])}</pre><button class="copy js-only" data-copy-label="复制格式">复制格式</button></details><p><a href="#intro-writing-templates">引言段落模板与精修要求 →</a></p>'
 md+=['','```latex',content['contributions']['code'],'```','','[引言段落模板与精修要求](#intro-writing-templates)']
 return rendered,md

def render_draft_chapter(data):
 e=html.escape;q=data['quick_start'];layout=data['tutorial_layout']
 rendered='<section class="quick-start major-chapter" id="quick-start"><h2>1. 初稿准备</h2><p>准备研究材料与模板，确定正文结构，再进入<a href="#figure-mainfig">论文绘图</a>。图先成型，方便合作者审阅；正文随后填充。</p>'
 md=['','<a id="quick-start"></a>','## 1. 初稿准备','','准备研究材料与模板，确定正文结构，再进入[论文绘图](#figure-mainfig)。图先成型，方便合作者审阅；正文随后填充。']
 for n,step in enumerate(layout['draft_steps'],1):
  rendered+=f'<section class="draft-step" id="{step["id"]}"><h3>{e(step["title"])}</h3>'
  md+=['',f'<a id="{step["id"]}"></a>','### '+step['title']]
  if step['id']=='draft-step-3':
   organization=layout['organization_templates']
   rendered+='<ul class="draft-requirements">'+''.join(f'<li>{e(rule)}</li>' for rule in organization['requirements'])+'</ul>'
   md+=['']+['- '+rule for rule in organization['requirements']]
   ph,pm=render_organization_templates(organization);rendered+=ph;md+=pm
  else:
   text=step['text']
   rendered+=f'<p>{e(text)}</p>';md+=['',text]
  if n==1:
   rendered+=f'<p class="skill-links"><a href="{data["writing_skill"]["download"]}" download>下载写作 skill</a> · <a href="#writing-skill">安装与用法</a></p>'
   ph,pm=render_codex_prompt(data,q['prompt_ref'],'填写研究材料，生成初稿');rendered+=ph;md+=pm
   rendered+='<p class="example-source">'+' · '.join(f'<a href="{e(s["url"])}">{e(s["title"])}</a>' for s in q['sources'][:2])+'</p>'
  if step['id']=='draft-step-3':
   block=next(b for b in q['steps'][2]['blocks'] if b.get('table'));t=block['table']
   rendered+='<div class="draft-table-wrap"><table class="draft-table"><caption>'+e(t['caption'])+'</caption><thead><tr>'+''.join(f'<th scope="col">{e(h)}</th>' for h in t['headers'])+'</tr></thead><tbody>'
   md+=['',t['caption'],'','| '+' | '.join(t['headers'])+' |','| --- | --- | --- |']
   for row in t['rows']:
    rendered+=f'<tr><th scope="row">{e(row["method"])}</th>';cells=[]
    for cell in row['cells']:
     mark=cell.get('mark','');value=e(cell['value'])
     if mark=='best':value=f'<strong>{value}</strong>'
     elif mark=='second':value=f'<u>{value}</u>'
     rendered+=f'<td class="{mark}">{value}<sup>±{e(cell["uncertainty"])}</sup></td>';cells.append(cell['value']+' ±'+cell['uncertainty'])
    rendered+='</tr>';md+=['| '+row['method']+' | '+' | '.join(cells)+' |']
   rendered+='</tbody></table></div>'
   rendered+=f'<details class="prompt"><summary>LaTeX 表格模板</summary><pre>{e(block["code"])}</pre><button class="copy js-only" data-copy-label="复制模板">复制模板</button><p class="example-source">{e(block["code_note"])}</p></details>'
   md+=['','**LaTeX 表格模板**','','```latex',block['code'],'```','',block['code_note']]
   closing=layout['organization_templates']['closing']
   rendered+=f'<p class="draft-next">{e(closing)} <a href="#figure-mainfig">进入第 2 章：论文绘图 →</a></p>'
   md+=['',closing,'','[进入第 2 章：论文绘图](#figure-mainfig)']
  rendered+='</section>'
 return rendered+'</section>',md

def render_figures(data):
 e=html.escape;f=data['figure_chapter'];layout=data['tutorial_layout']
 titles={key:f'2.{n} '+title for n,(key,title) in enumerate(FIGURE_SECTIONS,1)}
 visuals={v['id']:v for v in f['visual_examples']}
 opening=layout['figure_opening']
 def figure(v):
  if v.get('existing'):
   gallery=next(g for g in f['gallery'] if g['figure_id']==v['id']);item=next(i for i in data['items'] if i['id']==gallery['item']);ex=item['examples'][gallery['example_index']]
   v=dict(v,zh=ex.get('caption_zh',ex.get('caption','')),analysis_zh=ex['analysis_zh'],license=ex['license'],source_url=data['references'][ex['provenance']['reference']]['url'],source_title=data['references'][ex['provenance']['reference']]['title'])
  return render_figure_case(v,layout.get('figure_notes',{}).get(v['id']))
 rendered='<section class="major-chapter figure-chapter" id="figures"><h2>2. 论文绘图</h2><p>'+e(opening['lead'])+'</p>'
 md=['','<a id="figures"></a>','## 2. 论文绘图','',opening['lead']]
 for part in opening['parts']:
  rendered+=f'<section id="{e(part["id"])}"><h3>{e(titles[part["id"]])}</h3><ul class="template-rules">'+''.join(f'<li>{e(rule)}</li>' for rule in part['rules'])+'</ul>'
  md+=['','<a id="'+part['id']+'"></a>','### '+titles[part['id']],'']+['- '+rule for rule in part['rules']]
  for key in part['visuals']:
   ph,pm=figure(visuals[key]);rendered+=ph;md+=pm
  rendered+='</section>'
 rendered+=f'<section id="figure-skill"><h3>{titles["figure-skill"]}</h3><p><a href="{e(f["skill"]["download"])}" download>下载绘图 skill</a> · <a href="{REPO}/blob/main/{e(f["skill"]["source"])}">SKILL.md</a></p><p>{e(f["scope_note"])}</p>'
 md+=['','<a id="figure-skill"></a>','### '+titles['figure-skill'],'',f'[下载绘图 skill](../{f["skill"]["download"]})','',f['scope_note']]
 ph,pm=render_codex_prompt(data,f['prompt_ref'],'填写绘图任务与数据');rendered+=ph+'</section>';md+=pm
 for key,field in [('figure-rules','rules'),('figure-types','types')]:
  rendered+=f'<h3 id="{key}">{titles[key]}</h3>'
  rules=f[field][2:] if field=='types' else f[field]
  rh,rm=render_short_rules(rules,visuals,compact=True);rendered+=rh;md+=['','<a id="'+key+'"></a>','### '+titles[key]]+rm
 rendered+=f'<h3 id="notion-gallery">{titles["notion-gallery"]}</h3><p>按图的任务整理统计图与案例图。</p><span id="figure-gallery"></span>'
 md+=['','<a id="notion-gallery"></a>','<a id="figure-gallery"></a>','### '+titles['notion-gallery'],'','按图的任务整理统计图与案例图。']
 shown={key for part in opening['parts'] for key in part['visuals']}
 for topic in dict.fromkeys(v['topic'] for v in visuals.values()):
  group=[v for v in visuals.values() if v['topic']==topic and v['id'] not in shown]
  if not group:continue
  rendered+=f'<section class="figure-topic"><p class="figure-topic-label"><strong>{e(topic)}</strong></p>';md+=['','#### '+topic]
  for v in group:
   ph,pm=figure(v);rendered+=ph;md+=pm
  rendered+='</section>'
 rendered+=f'<h3 id="figure-references">{titles["figure-references"]}</h3><details class="figure-source-links"><summary>补充图页与点评</summary>';md+=['','<a id="figure-references"></a>','### '+titles['figure-references']]
 for n,link in enumerate(f['links'],1):
  rendered+=f'<section class="linked-figure" id="figure-link-{n}"><p><strong><a href="{e(link["url"])}">{e(link["title"])}</a></strong>：{e(link["zh"])}</p>'
  if link.get('analysis'):rendered+=f'<p>{e(link["analysis"])}</p>'
  for key in ('source','license'):
   if link.get(key):rendered+=f'<p class="example-source">{e(link[key])}</p>'
  rendered+='</section>';md+=['',f'[{link["title"]}]({link["url"]})：'+link['zh'],'',link.get('analysis',''),'',link.get('source',''),'',link.get('license','')]
 return rendered+'</details></section>',md

def render_quick_start(data, include_figures=True):
 if data.get('_tutorial_layout'):return render_draft_chapter(data)
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
  if n==2 and not include_figures:
   rendered+=f'<p>{e(s["text_zh"])}</p></section>'
   md+=['',s['text_zh'],'','绘图规则与模板另见 [绘图 skill](https://github.com/Da1yuqin/PaperBank/tree/main/skills/paperbank-figures)。']
   continue
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
     figure_class='draft-figure'+(' single-column-figure' if v.get('layout')=='single-column' else '')
     rendered+=f'<figure class="{figure_class}"><a href="{e(v["asset"])}"><img src="{e(v["asset"])}" alt="{e(block["figure_title"])}" loading="lazy"></a><figcaption>{e(v["license"])} <a href="{e(v["source_url"])}">原论文</a> · <a href="{e(v["license_url"])}">许可</a></figcaption></figure>'
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
   rendered+=f'<p class="fill-hint"><strong>填什么：</strong>{e(q["fill_hint_zh"])}</p><p class="skill-links"><a href="{data["writing_skill"]["download"]}" download>下载 cs-paper-writing skill</a> · <a href="#writing-skill">安装与用法</a></p>'
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

def render_short_rules(rules, visuals=None, compact=False):
 e=html.escape
 visuals=visuals or {}
 rendered='<ul class="compact-rules">';md=[]
 for r in rules:
  rendered+=f'<li><strong>{rule_html(r["title"])}：</strong>{e(r["zh"])}'
  md+=['','- **'+r['title']+'：**'+r['zh']]
  if r.get('example_en') and not compact:
   rendered+=f'<details class="short-example"><summary>中英例子</summary><p lang="en">{e(r["example_en"])}</p><p>{e(r["example_zh"])}</p></details>'
   md+=['',r['example_en'],'',r['example_zh']]
  for key in r.get('visuals',[]):
   if key not in visuals:continue
   v=visuals[key]
   if compact:
    rendered+=f' <a class="rule-reference" href="#{e(v["id"])}">{e(v["title"])} ↗</a>'
    md+=['',f'[图例与批注：{v["title"]}](#{v["id"]})']
    continue
   rendered+=f'<a class="rule-visual" href="#{e(v["id"])}"><img src="{e(v["asset"])}" alt="{e(v["title"])}" loading="lazy"><span>{e(v["title"])} · 点开原图与拆解 ↗</span></a>'
   md+=['',f'![{v["title"]}](../{v["asset"]})',f'[原图与拆解](#{v["id"]})']
  rendered+='</li>'
 return rendered+'</ul>',md

def render_skill(data):
 """Keep the portable entry point separate from the full reading guide."""
 e=html.escape
 skill=data['writing_skill']
 rendered=f'<details class="writing-skill" id="writing-skill"><summary>给 Codex 用：写作与绘图 skill</summary><p>{e(skill["intro"])}</p>'
 md=['','<a id="writing-skill"></a>','### 写作与绘图 skill','',skill['intro']]
 for entry,label in [(skill,'cs-paper-writing'),(data['figure_chapter']['skill'],'绘图')]:
  rendered+=f'<p class="skill-links"><a href="{e(entry["download"])}" download>{e(label)} ZIP</a> · <a href="{REPO}/blob/main/{e(entry["source"])}">SKILL.md</a>：{e(entry["intro"])}</p>'
  md+=['',f'[{label} ZIP](../{entry["download"]}) · [SKILL.md](../{entry["source"]})：{entry["intro"]}']
 rendered+='<p>下载所需 ZIP，解压并保留完整文件夹，让 Codex 读取其中的 <code>SKILL.md</code>。填入材料、任务和允许修改的范围；需要写作和绘图时同时读取两个 skill。</p>'
 md+=['','下载所需 ZIP，解压并保留完整文件夹，让 Codex 读取其中的 SKILL.md。填入材料、任务和允许修改的范围；需要写作和绘图时同时读取两个 skill。']
 ph,pm=render_codex_prompt(data,skill['prompt_ref'],'中文使用提示词','English usage prompt');rendered+=ph;md+=pm
 return rendered+'</details>',md

def package_skill(data):
 """Generate the skill reference from the same rules used by the website."""
 skill=data['writing_skill'];folder=ROOT/Path(skill['source']).parent
 rules=[i for i in data['skill_rules'] if i['section']!='rebuttal' and i['id'] not in {'tip-89','tip-91','tip-92','tip-95','tip-88'}]
 md=['# CS 论文写作检查参考','','按本次任务选规则。下面示例是假设情境，不是论文原文或实测；实际改稿先核对事实。','','网页：[写作铁律](https://da1yuqin.github.io/PaperBank/#general-rules) · [论文结构与逐句例子](https://da1yuqin.github.io/PaperBank/#paper-order)']
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
  if not section.get('manuscript'):continue
  md+=['','### '+section['nav'],'',section['purpose']]
  if section.get('principle'):md+=['',section['principle']]
  if data['refine_section_principles'].get(section['id']):md+=['']+['- '+rule for rule in data['refine_section_principles'][section['id']]]
 md+=['','## 各章完整句式模板']
 for lesson in data['refine_templates']:
  if lesson['section']=='rebuttal':continue
  _,rm=render_paragraph(lesson,data['references']);md+=rm
 md+=['','---','','原创规则与教学示例：Da1yuqin / PaperBank，[原文](https://da1yuqin.github.io/PaperBank/)，[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)。转载保留署名、出处及许可，改编注明改动。']
 (folder/'references').mkdir(parents=True,exist_ok=True)
 (folder/'references/checklist.md').write_text('\n'.join(md)+'\n',encoding='utf-8')
 package_prompt_reference(data,folder,['draft','writing','experiments','intro'])
 package_archive(skill,['SKILL.md','references/checklist.md','references/prompts.md','LICENSE'])

def package_archive(skill, names):
 folder=ROOT/Path(skill['source']).parent
 with zipfile.ZipFile(ROOT/skill['download'],'w',zipfile.ZIP_DEFLATED) as z:
  for name in names:
   info=zipfile.ZipInfo(folder.name+'/'+name,date_time=(2026,10,7,0,0,0))
   info.compress_type=zipfile.ZIP_DEFLATED;info.external_attr=0o644<<16
   z.writestr(info,(folder/name).read_bytes())

def render_response_template(template, key, open_default=False):
 e=html.escape
 opened=' open' if open_default else ''
 rendered=f'<details class="chapter-templates response-template" id="{e(key)}"{opened}><summary>{e(template["title"])}</summary><div class="paragraph-lesson"><pre>{e(template["text"])}</pre><button type="button" class="copy js-only" data-copy-label="复制模板">复制模板</button><p class="lesson-context">{e(template["note"])}</p></div></details>'
 md=['',f'<a id="{key}"></a>','### '+template['title'],'','```markdown',template['text'],'```','',template['note']]
 return rendered,md

def build_response():
 """Build the independent guide and skill from one public source."""
 data=json.loads((ROOT/'data/response.json').read_text(encoding='utf-8'))
 e=html.escape;skill=data['skill'];nav='';chapters='';rules_md=[]
 for section in data['sections']:
  key=section['id'];title=section['title']
  nav+=f'<a href="#{e(key)}">{e(title)}</a>'
  chapters+=f'<section class="major-chapter chapter" id="{e(key)}"><h2>{e(title)}</h2><div class="paragraph-lesson"><p>{e(section["lead"])}</p><ul class="template-rules">'+''.join(f'<li>{rule_html(rule)}</li>' for rule in section['rules'])+'</ul></div>'
  rules_md+=['',f'<a id="{key}"></a>','## '+title,'',section['lead'],'']+['- '+rule for rule in section['rules']]
  templates=([section['template']] if section.get('template') else [])+section.get('templates',[])
  for n,template in enumerate(templates,1):
   template_html,template_md=render_response_template(template,key+'-template-'+str(n),key=='response-format')
   chapters+=template_html;rules_md+=template_md
  for n,example in enumerate(section.get('examples',[]),1):
   annotated={'id':key+'-example-'+str(n),'section':key,'title':example['title'],'label':'教学模板：把方括号换成自己的真实证据。','paragraphs':[{'en':example['paragraph']}],'annotations':[{'paragraph':0,'en':quote['text'],'title':'【铁律】'+label,'body':quote['note'].removeprefix('【铁律】')} for quote,label in zip(example['quotes'],['先答问题','交代对照','限定结论','给出位置'])],'processing':'原创教学模板，不是真实审稿回复。','source_label':'StrongResponse · 原创教学模板'}
   example_html,example_md=render_annotated_paragraph(annotated,{},heading_level=3)
   chapters+=example_html;rules_md+=example_md
  chapters+='</section>'
 usage=f'<details class="writing-skill" id="response-skill"><summary>skill 安装与用法</summary><p>下载 ZIP，解压并保留完整的 <code>rebuttal</code> 文件夹。让 Codex 读取 <code>rebuttal/SKILL.md</code>，填入论文、完整 review、已有证据、当轮规则和允许修改的范围。</p><p><a href="{REPO}/blob/main/{e(skill["source"])}">SKILL.md</a> · <a href="{REPO}/blob/main/skills/rebuttal/references/rules.md">规则与模板</a> · <a href="{REPO}/blob/main/skills/rebuttal/references/prompts.md">提示词</a></p><p>制作类似教程：<a href="../assets/tutorial-authoring-skill.zip" download>下载教程编排 skill</a> · <a href="{REPO}/blob/main/skills/tutorial-authoring/SKILL.md">SKILL.md</a>。内容顺序、简洁表达、完整案例与旁批、窄屏检查均包含在内。</p></details>'
 prompt_html,_=render_response_template({'title':'复制给 Codex：起草与逐题检查','text':data['quick_start_prompt'],'note':'把【】换成材料或文件。先查清问题，再写回复；缺证据的地方由作者决定如何处理。'},'response-prompt')
 preface=f'<p class="site-switch">论文写作与绘图：<a href="../">PaperBank</a> · 审稿回复：StrongResponse</p><p class="skill-links"><strong>这里有一份可以直接使用的 skill。</strong> <a href="../{e(skill["download"])}" download>下载 rebuttal skill</a> · <a href="#response-skill">用法</a></p><figure class="accept-banner"><img src="../{e(data["image"])}" alt="{e(data["image_alt"])}" width="1672" height="941" fetchpriority="high"></figure><p>{e(data["preface"])}</p>'+usage+prompt_html
 template=(ROOT/'assets/response-template.html').read_text(encoding='utf-8')
 for key,value in {'TITLE':e(data['title']),'SUBTITLE':e(data['subtitle']),'PREFACE':preface,'NAV':nav,'CHAPTERS':chapters}.items():template=template.replace('{{'+key+'}}',value)
 assert not re.search(r'{{[A-Z_]+}}',template)
 (ROOT/'StrongResponse').mkdir(exist_ok=True)
 (ROOT/'StrongResponse/index.html').write_text(template,encoding='utf-8')
 attribution=['','---','','Da1yuqin / [StrongResponse](https://da1yuqin.github.io/PaperBank/StrongResponse/)，[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)。转载请保留署名、出处及许可，改写注明改动。']
 md=['# '+data['title'],'',data['subtitle'],'','论文写作与绘图：[PaperBank](https://da1yuqin.github.io/PaperBank/)','',f'![{data["image_alt"]}](../{data["image"]})','',data['preface'],'',f'[下载 rebuttal skill](../{skill["download"]}) · [SKILL.md](../{skill["source"]})','', '解压并保留完整 rebuttal 文件夹，让 Codex 读取 rebuttal/SKILL.md。','', '## 给 Codex 的提示词','','```text',data['quick_start_prompt'],'```']+rules_md+attribution
 (ROOT/'book/response.md').write_text('\n'.join(md)+'\n',encoding='utf-8')
 folder=ROOT/Path(skill['source']).parent
 (folder/'references').mkdir(parents=True,exist_ok=True)
 (folder/'SKILL.md').write_text(skill['instructions'],encoding='utf-8')
 (folder/'references/rules.md').write_text('\n'.join(['# StrongResponse · 规则与模板','','以下均为原创教学模板，不是真实审稿记录；方括号填写已核实材料。']+rules_md+attribution)+'\n',encoding='utf-8')
 loop=next(s['template']['text'] for s in data['sections'] if s['id']=='revise-loop')
 prompts=['# 给 Codex 的提示词','','## 起草与逐题检查','','```text',data['quick_start_prompt'],'```','','## Revise loop','','```text',loop,'```']+attribution
 (folder/'references/prompts.md').write_text('\n'.join(prompts)+'\n',encoding='utf-8')
 license_text=(folder/'LICENSE').read_text(encoding='utf-8').replace('Da1yuqin / PaperBank','Da1yuqin / StrongResponse').replace('Website: https://da1yuqin.github.io/PaperBank/\n','Website: https://da1yuqin.github.io/PaperBank/StrongResponse/\n')
 (folder/'LICENSE').write_text(license_text,encoding='utf-8')
 package_archive(skill,['SKILL.md','references/rules.md','references/prompts.md','LICENSE'])
 package_archive({'source':'skills/tutorial-authoring/SKILL.md','download':'assets/tutorial-authoring-skill.zip'},['SKILL.md','LICENSE'])

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
 license_text=(ROOT/Path(data['writing_skill']['source']).parent/'LICENSE').read_text(encoding='utf-8').replace('CS Paper Writing Skill','PaperBank Drawing Skill').replace('references/checklist.md','references/rules.md').replace('cs-paper-writing','paperbank-figures')
 (folder/'LICENSE').write_text(license_text,encoding='utf-8')
 package_archive(skill,['SKILL.md','references/rules.md','references/prompts.md','LICENSE'])

def render_tools(data):
 """Render linked resources separately from manuscript checks."""
 e=html.escape
 groups=data.get('tools',[])
 intro='按用途选。以下整理自公开文档，未逐项安装；版本和许可见原项目。'
 rendered=f'<section class="toolbox major-chapter" id="tools"><h2>4. 辅助工具</h2><p class="chapter-desc">{e(intro)}</p>'
 rendered+='<p class="tool-index">'+ ' · '.join(f'<a href="#tools-{e(g["id"])}">4.{n} {e(g["title"])}</a>' for n,g in enumerate(groups,1))+f' · <a href="#code-release-prompt">4.{len(groups)+1} 开源整理</a></p>'
 total=sum(len(g['items']) for g in groups)
 rendered+=f'<div class="tool-search js-only"><label for="tool-search">搜索工具</label><input type="search" id="tool-search" placeholder="搜 Zotero、画图、引用……"><span id="tool-count" role="status" aria-live="polite">{total} 项资源</span></div>'
 md=['','<a id="tools"></a>','## 4. 辅助工具','',intro,'','核对日期：'+data['tools_checked_at']+'。']
 for n,group in enumerate(groups,1):
  rendered+=f'<section class="tool-group" id="tools-{e(group["id"])}"><h3>4.{n} {e(group["title"])}</h3><ul class="tool-list">'
  md+=['',f'### 4.{n} {group["title"]}','']
  for tool in group['items']:
   assert all(tool.get(k) for k in ['id','title','url','use_zh','example_zh','example_en','boundary_zh'])
   rendered+=f'<li class="tool-item" id="tool-{e(tool["id"])}"><p><strong><a href="{e(tool["url"])}">{e(tool["title"])}</a>：</strong>{e(tool["use_zh"])}</p><p class="boundary">{e(tool["boundary_zh"])}</p>'
   md+=[f'- **[{tool["title"]}]({tool["url"]})：**{tool["use_zh"]}','',tool['boundary_zh']]
   if tool.get('links'):
    rendered+='<p class="sources">'+' · '.join(f'<a href="{e(link["url"])}">{e(link["title"])}</a>' for link in tool['links'])+'</p>'
    md+=['',' · '.join(f'[{link["title"]}]({link["url"]})' for link in tool['links'])]
   rendered+='</li>'
  rendered+='</ul></section>'
 rendered+='<p class="boundary js-only" id="tool-empty" hidden>没有匹配的工具。换个短词试试。</p>'
 title=f'4.{len(groups)+1} 开源整理'
 rendered+=f'<section class="release-prompt" id="code-release-prompt"><h3>{e(title)}</h3><p>先写清允许处理的文件。中文界面、接口字符串、业务路径也可能影响运行，不能一键全换。填写允许修改的范围后再使用。</p>'
 md+=['','<a id="code-release-prompt"></a>','### '+title,'','先写清允许处理的文件。中文界面、接口字符串、业务路径也可能影响运行，不能一键全换。']
 ph,pm=render_codex_prompt(data,data['code_release_prompt']['prompt_ref'],'中文提示词');rendered+=ph;md+=pm
 rendered+=f'<p class="tool-checked">文档核对：{e(data["tools_checked_at"])}。安装、版本和许可见项目原文。</p></section></section>'
 return rendered,md

def build():
 source_data=json.loads((ROOT/'data/guide.json').read_text(encoding='utf-8'))
 data=deepcopy(source_data)
 data['_tutorial_layout']=True
 for update in data['tutorial_layout'].get('principle_updates',[]):
  rules=data['refine_section_principles'][update['section']]
  rules[rules.index(update['before'])]=update['after']
 for section,rules in data['tutorial_layout']['section_additions'].items():
  data['refine_section_principles'][section]+=rules
 names=data['tutorial_layout']['case_titles']
 for case in data['annotated_paragraphs']:case['title']=names.get(case['id'],case['title'])
 for figure in data['figure_chapter']['visual_examples']:figure['title']=data['tutorial_layout']['figure_titles'][figure['id']]
 for template in data['refine_templates']:template['title']=data['tutorial_layout']['template_titles'].get(template['id'],template['title'])
 data['refine_global_cases'][0]['title']='贡献与句间衔接'
 data['intro_connections']['title']='段落承接'
 data['intro_connections']['map_title']='摘要与引言：主张对应'
 data['intro_connections'].update(data['tutorial_layout']['abstract_intro_template'])
 for group,title in zip(data['tools'],['文献检索与阅读','写作与排版','论文绘图','引用核验','代码阅读','论文发布与维护','其他资源']):group['title']=title
 sections,items,refs=data['sections'],data['items'],data['references']
 lessons=data.get('manuscript_paragraphs',[])
 annotated=data.get('annotated_paragraphs',[])
 assert len({i['id'] for i in items})==len(items)
 assert all(i['section'] in {s['id'] for s in sections} for i in items)
 assert len({p['id'] for p in lessons})==len(lessons)
 assert all(p['section'] in {s['id'] for s in sections} for p in lessons)
 assert len({p['id'] for p in annotated})==len(annotated)
 assert all(p['section'] in {s['id'] for s in sections} for p in annotated)
 e=html.escape
 def link(key):
  r=refs[key]
  return f'<a href="{e(r["url"])}">{e(r["title"])}</a>'
 preface,preface_md=render_preface(data)
 quick_start,quick_md=render_quick_start(data)
 figures,figures_md=render_figures(data)
 opening,opening_md=render_opening(data)
 skill,skill_md=render_skill(data)
 draft_nav=''.join(f'<a href="#{e(s["id"])}">{e(s["title"])}</a>' for s in data['tutorial_layout']['draft_steps'])
 figure_nav=''.join(f'<a href="#{key}">2.{n} {e(title)}</a>' for n,(key,title) in enumerate(FIGURE_SECTIONS,1))
 tools_nav=''.join(f'<a href="#tools-{e(g["id"])}">4.{n} {e(g["title"])}</a>' for n,g in enumerate(data['tools'],1))
 tools_nav+=f'<a href="#code-release-prompt">4.{len(data["tools"])+1} 开源整理</a>'
 nav='<a href="#general-rules">3.1 全文规范</a>'
 for s in sections:
  if not s.get('manuscript'):continue
  group=[i for i in items if i['section']==s['id']]
  number=int(s['number'])+1
  nav+=f'<a href="#chapter-{s["id"]}">3.{number} {e(s["nav"])}</a>'
 entries='';chapter_html={};chapter_md={}
 md=['# '+data['site_title'],'','先用 Codex 起草正文与关键图，再由作者审核逻辑、逐章精修。第四章为辅助工具。审稿回复见独立网页 StrongResponse。','','主要面向方法与实证研究；按学科、研究类型和投稿要求调整。模拟段落明确标注，真实论文摘录另给出处与版本。','','欢迎使用、改写、转载，也欢迎给 Codex 用作 skill。原创内容采用 CC BY 4.0，论文摘录与图片保留各自许可。转载原创内容请保留作者 Da1yuqin、[原文链接](https://Da1yuqin.github.io/PaperBank/)和 [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) 许可，修改版本注明改动。如有帮助，欢迎 Star。']
 md+=quick_md+skill_md+figures_md+['','<a id="refine"></a>','## 3. 正文精修','','先检查全文规范，再按章节精修。模板中的【】填自己的材料，段落按内容调整。','']+['','<a id="rules"></a>']+opening_md+['','### 本章目录','']
 md += [f'- [{section_label(s)}{s["title"]}](#{s["id"]})' for s in sections]
 md += ['- [好用工具与开源整理提示词](#tools)']
 for s in sections:
  html_start=len(entries);md_start=len(md)
  group=[i for i in items if i['section']==s['id']]
  purpose=s.get('purpose') or s.get('summary') or s['description']
  prefix='3.'+str(int(s['number'])+1)+' ' if s.get('manuscript') else ''
  heading_level=3
  entries+=f'<section class="chapter" id="chapter-{s["id"]}"><div class="chapter-head"><h{heading_level}>{prefix}{e(s["title"])}</h{heading_level}></div><p class="chapter-desc"><strong>{e(purpose)}</strong></p>'
  md+=['',f'<a id="{s["id"]}"></a>',f'<a id="chapter-{s["id"]}"></a>',f'{"#"*heading_level} {prefix}{s["title"]}','',purpose]
  principles=data.get('refine_section_principles',{}).get(s['id'])
  if principles:
   entries+='<div class="section-principles"><h4>本节原则</h4><ul>'+''.join(f'<li>{rule_html(rule)}</li>' for rule in principles)+'</ul></div>'
   md+=['','#### 本节原则','']+['- '+rule for rule in principles]
  elif s.get('principle'):
   entries+=f'<p class="chapter-principle">{e(s["principle"])}</p>'
   md+=['',s['principle']]
  if s['id'] in data['tutorial_layout'].get('writing_templates',{}):
   templates_html,templates_md=render_writing_templates(data['tutorial_layout']['writing_templates'][s['id']],s['id'])
   entries+=templates_html;md+=templates_md
  if s['id']=='intro' and data.get('intro_connections'):
   connections_html,connections_md=render_intro_connections(data)
   entries+=connections_html;md+=connections_md
  for n,example in enumerate([p for p in annotated if p['section']==s['id']]):
   number=None
   example_html,example_md=render_annotated_paragraph(example,refs,number,heading_level=4)
   entries+=example_html;md+=example_md
  templates=[p for p in data.get('refine_templates',[]) if p['section']==s['id'] and p.get('latex_template')]
  if templates:
   entries+='<details class="chapter-templates"><summary>结构模板</summary>'
   md+=['','<details><summary>结构模板</summary>','']
  for n,lesson in enumerate(templates):
   number=None if any(p['section']==s['id'] for p in annotated) else (f'{prefix.strip()}.{chr(97+n)}' if s.get('manuscript') and len(templates)>1 else None)
   lesson_html,lesson_md=render_paragraph(lesson,refs,md_level=4,number=number,heading=len(templates)>1,compact=True)
   entries+=lesson_html;md+=lesson_md
  if templates:
   entries+='</details>';md+=['','</details>','']
  entries+='</section>'
  chapter_html[s['id']]=entries[html_start:];chapter_md[s['id']]=md[md_start:]
 entries=''.join(chapter_html[s['id']] for s in sections if s.get('manuscript'))
 md=md[:1]+['',data['site_subtitle'],'']+preface_md+md[1:7]+quick_md+skill_md+figures_md+['','<a id="refine"></a>','## 3. 正文精修','','先检查全文规范，再按章节精修。模板中的【】填自己的材料，段落按内容调整。','']+opening_md+['','### 本章目录','']
 md+=[f'- [3.{int(s["number"])+1} {s["nav"]}](#{s["id"]})' for s in sections if s.get('manuscript')]
 for s in sections:
  if s.get('manuscript'):md+=chapter_md[s['id']]
 examples=sum(len(i.get('examples',[])) for i in items)
 response_link='<p class="site-switch" id="rebuttal">审稿回复已独立为 <a href="StrongResponse/">💪StrongResponse【这边也长出肌肉】</a>，含回复模板与 rebuttal skill。</p>'
 md+=['','<a id="rebuttal"></a>','审稿回复：[💪StrongResponse【这边也长出肌肉】](https://da1yuqin.github.io/PaperBank/StrongResponse/)，含回复模板与 rebuttal skill。']
 tools,tools_md=render_tools(data)
 md+=tools_md
 reading=''.join(f'<li>{link(k)}<span> — {e(r["scope"])}</span></li>' for k,r in refs.items() if r.get('public'))
 t=(ROOT/'assets/template.html').read_text(encoding='utf-8')
 for k,v in {'TITLE':e(data['site_title']),'SUBTITLE':e(data['site_subtitle']),'PREFACE':preface,'NAV':nav,'DRAFT_NAV':draft_nav,'FIGURE_NAV':figure_nav,'TOOLS_NAV':tools_nav,'ENTRIES':entries,'TOOLS':tools,'RESPONSE_LINK':response_link,'QUICK_START':quick_start,'FIGURES':figures,'OPENING':opening,'SKILL':skill,'READING':reading,'TOTAL':str(len(items)),'CHAPTERS':'4','EXAMPLES':str(examples)}.items():t=t.replace('{{'+k+'}}',v)
 (ROOT/'index.html').write_text(t,encoding='utf-8')
 (ROOT/'book').mkdir(exist_ok=True)
 md+=['','## 参考阅读','']+[f'- [{r["title"]}]({r["url"]})：{r["scope"]}' for r in refs.values() if r.get('public')]
 (ROOT/'book/guide.md').write_text('\n'.join(md)+'\n',encoding='utf-8')
 package_skill(source_data)
 package_figure_skill(source_data)
 build_response()
 print(f'Built PaperBank (4 chapters) and StrongResponse (5 chapters), {len(lessons)+len(data.get("refine_templates",[]))+len(annotated)+bool(data.get("intro_connections"))} paragraph lessons.')

if __name__=='__main__':
 p=argparse.ArgumentParser(description=__doc__)
 p.add_argument('--serve',action='store_true');p.add_argument('--port',type=int,default=8000)
 a=p.parse_args();build()
 if a.serve:
  print(f'Preview: http://127.0.0.1:{a.port}',flush=True)
  ThreadingHTTPServer(('127.0.0.1',a.port),partial(SimpleHTTPRequestHandler,directory=str(ROOT))).serve_forever()
