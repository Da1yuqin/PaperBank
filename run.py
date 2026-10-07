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
 if example.get('analysis_zh'):
  analysis=example['analysis_zh']
  rendered+='<p class="example-label"><strong>逐句拆解</strong></p>'
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
 if example.get('image'):
  rendered+=f'<figure class="example-figure"><a href="{e(example["image"])}"><img class="teaching-figure" src="{e(example["image"])}" alt="{e(example["alt"])}" loading="lazy"></a>'
  md+=['',f'![{example["alt"]}](../{example["image"]})']
  captions=[example[k] for k in ['caption_en','caption_zh','caption'] if example.get(k)]
  if captions:
   rendered+='<figcaption>'+''.join(f'<p>{e(caption)}</p>' for caption in captions)+'</figcaption>'
   md+=['']+captions
  rendered+='</figure>'
 if example.get('provenance'):
  p=example['provenance']; r=refs[p['reference']]
  assert all(p.get(k) for k in ['location','version','status'])
  details='；'.join(p[k] for k in ['location','version','status'])
  rendered+=f'<p class="example-source"><strong>摘录出处：</strong><a href="{e(r["url"])}">{e(r["title"])}</a>；{e(details)}</p>'
  md+=['',f'**摘录出处：**[{r["title"]}]({r["url"]})；{details}']
 if example.get('license'):
  rendered+=f'<p class="example-source"><strong>原文／图片许可：</strong>{e(example["license"])}</p>'
  md+=['',f'**原文／图片许可：**{example["license"]}']
 return rendered+'</div>',md

def render_skill(data):
 """Keep the portable entry point separate from the full reading guide."""
 e=html.escape
 skill=data['writing_skill']
 rendered=f'<section class="writing-skill" id="writing-skill"><h2>PaperBank 写作 skill：让 Codex 也按这份清单检查</h2><p>{e(skill["intro"])}</p>'
 rendered+=f'<p class="skill-links"><a href="{e(skill["download"])}" download>下载写作 skill ZIP</a> · <a href="{REPO}/blob/main/{e(skill["source"])}">查看 SKILL.md</a> · <a href="#chapter-rules">32 条写作铁律</a></p><p>下载、解压，保留整个 <code>paperbank-writing/</code> 文件夹，把它交给 Codex 读取。下面提示词可直接用，再补上你的文件、任务和允许修改的范围。</p>'
 md=['','<a id="writing-skill"></a>','## PaperBank 写作 skill：让 Codex 也按这份清单检查','',skill['intro'],'',f'[下载 ZIP](../{skill["download"]}) · [查看 SKILL.md](../{skill["source"]}) · [32 条写作铁律](#rules)','','下载、解压，保留整个 paperbank-writing/ 文件夹，把它交给 Codex 读取；补上文件、任务和允许修改的范围。']
 for key,label,lang in [('prompt_zh','中文使用提示词','zh-CN'),('prompt_en','English usage prompt','en')]:
  rendered+=f'<details class="prompt"><summary>{label}</summary><pre lang="{lang}">{e(skill[key])}</pre><button class="copy js-only">复制提示词</button></details>'
  md+=['',f'**{label}**','','```text',skill[key],'```']
 return rendered+'</section>',md

def package_skill(data):
 """Generate the skill reference from the same rules used by the website."""
 folder=ROOT/'skills/paperbank-writing'
 rules=[i for i in data['items'] if i['section']=='rules']
 md=['# PaperBank 写作检查参考','','按本次任务选规则。证据和记录必须如实；结构与措辞是可调整的写法。下面示例均为假设的教学情境，不是论文原文、真实模型输出或实际完成的工作。改后假定已有对应记录；实际改稿须先核对事实，不能从改前文字推断或补造。','','网页：[32 条写作铁律](https://da1yuqin.github.io/PaperBank/#chapter-rules) · [70 个论文原文例子](https://da1yuqin.github.io/PaperBank/#chapter-core) · [rebuttal](https://da1yuqin.github.io/PaperBank/#chapter-rebuttal)']
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
 intro='按用途选一个先试。下面核对了公开页面或项目说明，未安装评测；“待探索”保留待试用状态。例子是使用情境，不代表实测效果。外部项目按自己的许可使用，链接收录不代表推荐它们的全部做法。'
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
 assert len({i['id'] for i in items})==len(items)
 assert all(i['section'] in {s['id'] for s in sections} for i in items)
 e=html.escape
 def link(key):
  r=refs[key]
  return f'<a href="{e(r["url"])}">{e(r["title"])}</a>'
 nav=f'<button data-chapter="all" aria-pressed="true" class="active">全部章节<i>{len(items)}</i></button>'
 for s in sections:
  group=[i for i in items if i['section']==s['id']]
  nav+=f'<button data-chapter="{s["id"]}" aria-pressed="false">{section_label(s)}{e(s["nav"])}<i>{len(group)}</i></button>'
 entries=''
 md=['# PaperBank · 论文少走弯路指南','','先把贡献讲清楚，再把证据交代全。按主题检查，卡住了再展开例子。','','主要面向实证型 CS / AI 论文；按学科、研究类型与投稿要求取舍。论文摘录就近标明出处与版本，中文为本指南翻译；教学改写与假设情境另行标注，不代表原论文结果。','','欢迎使用、改写、转载，也欢迎拿去给 Codex 等工具做 skill。原创内容采用 CC BY 4.0，论文摘录与图片保留各自许可。转载原创内容请保留作者 Da1yuqin、[原文链接](https://Da1yuqin.github.io/PaperBank/)和 [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) 许可，改过请注明。Star 自愿，署名别失联。','','## 目录','']
 skill,skill_md=render_skill(data)
 md[md.index('## 目录'):md.index('## 目录')]=skill_md+['']
 md += [f'- [{section_label(s)}{s["title"]}](#{s["id"]})' for s in sections]
 md += ['- [好用工具与开源整理提示词](#tools)']
 for s in sections:
  group=[i for i in items if i['section']==s['id']]
  entries+=f'<section class="chapter" id="chapter-{s["id"]}"><div class="chapter-head"><h2>{section_label(s)}{e(s["title"])}</h2><span class="shown">{len(group)} 条</span></div><p class="chapter-desc">{e(s.get("summary",s["description"]))}</p>'
  md+=['',f'<a id="{s["id"]}"></a>',f'## {section_label(s)}{s["title"]}','',s.get('summary',s['description'])]
  for subgroup in dict.fromkeys(i['group'] for i in group):
   entries+=f'<div class="check-group"><h3 class="group-title">{e(subgroup)}</h3><ul class="checklist">'
   md+=['',f'**{subgroup}**','']
   for i in [x for x in group if x['group']==subgroup]:
    num=int(i['id'][4:]); attrs=' '.join(f'data-{k}="{e(i[k])}"' for k in ['section','priority'])
    entries+=f'<li class="entry{ " entry-visual" if i.get("detail") else ""}" id="{i["id"]}" {attrs}><div class="check-row"><input class="task-check js-only" type="checkbox" id="check-{i["id"]}" data-id="{i["id"]}"><label class="check-text" for="check-{i["id"]}">{e(i["checklist"])}</label><a class="permalink" href="#{i["id"]}" aria-label="第 {num} 条">{num}</a></div>'
    md += [f'- [ ] **第 {num} 条：**{i["checklist"]}']
    entries+=f'<details class="explain"{ " open" if i.get("detail") else ""}><summary>说明{ "、例子" if i.get("examples") else ""}与参考</summary><div class="explain-body"><h4>{e(i["title"])}</h4><p>{e(i["lead"])}</p><p><strong>做法：</strong>{e(i["action"])}</p><p class="boundary"><strong>边界：</strong>{e(i["boundary"])}</p>'
    md+=['',f'<a id="{i["id"]}"></a>','<details>',f'<summary>第 {num} 条：{i["title"]} · 说明、例子与参考</summary>','',i['lead'],'',f'**做法：**{i["action"]}','',f'**边界：**{i["boundary"]}']
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
  entries+='</section>'
 examples=sum(len(i.get('examples',[])) for i in items)
 tools,tools_md=render_tools(data)
 md+=tools_md
 reading=''.join(f'<li>{link(k)}<span> — {e(r["scope"])}</span></li>' for k,r in refs.items() if r.get('public'))
 t=(ROOT/'assets/template.html').read_text(encoding='utf-8')
 for k,v in {'NAV':nav,'ENTRIES':entries,'TOOLS':tools,'SKILL':skill,'READING':reading,'TOTAL':str(len(items)),'CHAPTERS':str(len(sections)),'EXAMPLES':str(examples)}.items():t=t.replace('{{'+k+'}}',v)
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
