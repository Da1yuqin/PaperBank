#!/usr/bin/env python3
"""Build PaperBank; use --serve to preview with Python 3 and no dependencies."""
import argparse
import html
import json
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

ROOT = Path(__file__).resolve().parent
REPO = 'https://github.com/Da1yuqin/PaperBank'

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
  nav+=f'<button data-chapter="{s["id"]}" aria-pressed="false">{int(s["number"])}. {e(s["nav"])}<i>{len(group)}</i></button>'
 entries=''
 md=['# PaperBank · 论文少走弯路指南','','先把贡献讲清楚，再把证据交代全。按主题检查，卡住了再展开例子。','','主要面向实证型 CS / AI 论文；按学科、研究类型与投稿要求取舍。下文“写法示例”均为原创教学情境，假设数字不代表实验结果。','','欢迎使用、改写、转载，也欢迎拿去给 Codex 等工具做 skill。转载请保留作者 Da1yuqin、[原文链接](https://Da1yuqin.github.io/PaperBank/)和 [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) 许可，改过请注明。Star 自愿，署名别失联。','','## 目录','']
 md += [f'- [{int(s["number"])}. {s["title"]}](#{s["id"]})' for s in sections]
 for s in sections:
  group=[i for i in items if i['section']==s['id']]
  entries+=f'<section class="chapter" id="chapter-{s["id"]}"><div class="chapter-head"><h2>{int(s["number"])}. {e(s["title"])}</h2><span class="shown">{len(group)} 条</span></div><p class="chapter-desc">{e(s.get("summary",s["description"]))}</p>'
  md+=['',f'<a id="{s["id"]}"></a>',f'## {int(s["number"])}. {s["title"]}','',s.get('summary',s['description'])]
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
     entries+=f'<div class="example"><h5>{e(example["title"])}</h5>'
     if example.get('before'):entries+=f'<p><strong>改前：</strong>{e(example["before"])}</p>'
     if example.get('after'):entries+=f'<p><strong>改后：</strong>{e(example["after"])}</p>'
     entries+=f'<p class="why">{e(example["why"])}</p>'
     if example.get('image'):entries+=f'<img class="teaching-figure" src="{e(example["image"])}" alt="{e(example["alt"])}" loading="lazy">'
     entries+='</div>'
     md+=['',f'**{example["title"]}**']
     for key,label in [('before','改前'),('after','改后'),('why','说明')]:
      if example.get(key):md+=['',f'**{label}：**{example[key]}']
     if example.get('image'):md+=['',f'![{example["alt"]}](../{example["image"]})']
    if i.get('prompt'):
     entries+=f'<details class="prompt"><summary>复制用的提示词</summary><pre>{e(i["prompt"])}</pre><button class="copy js-only">复制提示词</button></details>'
     md+=['','```text',i['prompt'],'```']
    sources=list(dict.fromkeys([i['source']]+i.get('refs',[])))
    entries+='<p class="sources"><strong>来源与延伸阅读：</strong>'+'；'.join(link(k) for k in sources)+'</p></div></details></li>'
    md+=['','来源与延伸阅读：'+'；'.join(f'[{refs[k]["title"]}]({refs[k]["url"]})' for k in sources),'','</details>','']
   entries+='</ul></div>'
  entries+='</section>'
 examples=sum(len(i.get('examples',[])) for i in items)
 reading=''.join(f'<li>{link(k)}<span> — {e(r["scope"])}</span></li>' for k,r in refs.items() if r.get('public'))
 t=(ROOT/'assets/template.html').read_text(encoding='utf-8')
 for k,v in {'NAV':nav,'ENTRIES':entries,'READING':reading,'TOTAL':str(len(items)),'CHAPTERS':str(len(sections)),'EXAMPLES':str(examples)}.items():t=t.replace('{{'+k+'}}',v)
 (ROOT/'index.html').write_text(t,encoding='utf-8')
 (ROOT/'book').mkdir(exist_ok=True)
 md+=['','## 参考阅读','']+[f'- [{r["title"]}]({r["url"]})：{r["scope"]}' for r in refs.values() if r.get('public')]
 (ROOT/'book/guide.md').write_text('\n'.join(md)+'\n',encoding='utf-8')
 print(f'Built {len(sections)} chapters, {len(items)} checks, {examples} examples.')

if __name__=='__main__':
 p=argparse.ArgumentParser(description=__doc__)
 p.add_argument('--serve',action='store_true');p.add_argument('--port',type=int,default=8000)
 a=p.parse_args();build()
 if a.serve:
  print(f'Preview: http://127.0.0.1:{a.port}',flush=True)
  ThreadingHTTPServer(('127.0.0.1',a.port),partial(SimpleHTTPRequestHandler,directory=str(ROOT))).serve_forever()
