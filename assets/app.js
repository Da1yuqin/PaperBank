'use strict';
document.documentElement.classList.add('js');
const $=s=>document.querySelector(s), $$=s=>[...document.querySelectorAll(s)];
function alignParagraphNotes(panel){
 if(panel.hidden||!panel.getClientRects().length)return;
 const notes=[...panel.querySelectorAll('.paragraph-note')];
 notes.forEach(note=>note.style.marginTop='0px');
 if(matchMedia('(max-width:820px)').matches)return;
 for(const note of notes){
  const mark=panel.querySelector(`.paragraph-highlight[data-note-key="${note.dataset.noteKey}"]`);
  if(!mark)continue;
  const offset=mark.getClientRects()[0].top-note.getBoundingClientRect().top;
  note.style.marginTop=Math.max(0,offset)+'px';
 }
}
for(const example of $$('.annotated-example')){
 const panels=[...example.querySelectorAll('[data-paragraph-panel]')];
 const buttons=[...example.querySelectorAll('[data-paragraph-language]')];
 function chooseLanguage(language){
  panels.forEach(panel=>panel.hidden=panel.dataset.paragraphPanel!==language);
  buttons.forEach(button=>button.setAttribute('aria-pressed',button.dataset.paragraphLanguage===language));
  requestAnimationFrame(()=>panels.forEach(alignParagraphNotes));
 }
 buttons.forEach(button=>button.addEventListener('click',()=>chooseLanguage(button.dataset.paragraphLanguage)));
 chooseLanguage(panels[0]?.dataset.paragraphPanel||'zh');
 for(const panel of panels){
  for(const node of panel.querySelectorAll('[data-note-key]')){
   const matching=[...panel.querySelectorAll('[data-note-key]')].filter(other=>other.dataset.noteKey===node.dataset.noteKey);
   const focus=active=>matching.forEach(other=>other.classList.toggle('is-focused',active));
   node.addEventListener('mouseenter',()=>focus(true));node.addEventListener('mouseleave',()=>focus(false));
   node.addEventListener('focus',()=>focus(true));node.addEventListener('blur',()=>focus(false));
  }
  const observer=new ResizeObserver(()=>alignParagraphNotes(panel));
  panel.querySelectorAll('.annotated-text').forEach(text=>observer.observe(text));
 }
}
window.addEventListener('resize',()=>$$('.annotated-panel').forEach(alignParagraphNotes));
function alignArgumentArrows(){
 if(matchMedia('(max-width:820px)').matches)return;
 for(const pair of $$('.argument-pair')){
  if(!pair.getClientRects().length)continue;
  const svg=pair.querySelector('svg'),box=svg.getBoundingClientRect();
  if(!box.height)continue;
  const center=selector=>{
   const mark=pair.querySelector(selector).getClientRects()[0];
   return ((mark.top+mark.height/2-box.top)/box.height*100).toFixed(2);
  };
  const start=center('.argument-abstract .argument-mark'),end=center('.argument-intro .argument-mark');
  pair.querySelector('.argument-link').setAttribute('d',`M 5 ${start} C 35 ${start}, 65 ${end}, 93 ${end}`);
 }
 for(const row of $$('.intro-body-row')){
  if(!row.getClientRects().length)continue;
  const box=row.querySelector('svg').getBoundingClientRect();
  if(!box.height)continue;
  const center=mark=>{
   const rect=mark.getClientRects()[0];
   return ((rect.top+rect.height/2-box.top)/box.height*100).toFixed(2);
  };
  const start=center(row.querySelector('.intro-map-source .argument-mark'));
  const targets=[...row.querySelectorAll('.intro-map-target .argument-mark')];
  row.querySelectorAll('.intro-body-link').forEach((path,n)=>{
   const end=center(targets[n]);
   path.setAttribute('d',`M 4 ${start} C 35 ${start}, 65 ${end}, 95 ${end}`);
  });
 }
}
const argumentObserver=new ResizeObserver(alignArgumentArrows);
$$('.argument-pair,.intro-body-row').forEach(pair=>argumentObserver.observe(pair));
window.addEventListener('resize',alignArgumentArrows);
requestAnimationFrame(alignArgumentArrows);
const lessons=$$('.paragraph-lesson,.inline-figures');
try{if(localStorage.getItem('paperbank-theme')==='dark')document.documentElement.classList.add('dark');}catch{}
function sync(){
 const words=$('#search').value.trim().toLowerCase().split(/\s+/).filter(Boolean);
 const filtering=words.length>0;
 let count=0;
 for(const lesson of lessons){
  lesson.hidden=!words.every(w=>lesson.textContent.toLowerCase().includes(w));if(!lesson.hidden)count++;
  if(filtering&&!lesson.hidden&&lesson.matches('.annotated-example')){
   const panels=[...lesson.querySelectorAll('[data-paragraph-panel]')];
   const visible=panels.find(panel=>!panel.hidden);
   const matches=panel=>words.every(word=>panel.textContent.toLowerCase().includes(word));
   if(visible&&!matches(visible)){
    const matching=panels.find(matches);
    if(matching)lesson.querySelector(`[data-paragraph-language="${matching.dataset.paragraphPanel}"]`).click();
   }
  }
 }
 $$('.chapter').forEach(chapter=>{
  chapter.hidden=!chapter.querySelector('.paragraph-lesson:not([hidden]),.inline-figures:not([hidden])');
  chapter.querySelectorAll('.more-lessons,.chapter-templates').forEach(detail=>{
   const matches=detail.querySelector('.paragraph-lesson:not([hidden])');detail.hidden=!matches;
   if(filtering&&matches&&!detail.open){detail.dataset.filterOpened='true';detail.open=true;}
   else if(!filtering&&detail.dataset.filterOpened){detail.open=false;delete detail.dataset.filterOpened;}
  });
 });
 $('#count').hidden=!filtering;
 $('#count').textContent=`找到 ${count} 项`;
 $('#empty').hidden=count>0;
}
function closeMenu(){$('#sidebar').classList.remove('open');$('#mobile-toggle').setAttribute('aria-expanded','false');}
function reset(){$('#search').value='';sync();}
$('#search').addEventListener('input',sync);
$$('[data-reset]').forEach(button=>button.addEventListener('click',reset));
$('#mobile-toggle').addEventListener('click',()=>{const open=$('#sidebar').classList.toggle('open');$('#mobile-toggle').setAttribute('aria-expanded',open);});
function themeState(){const dark=document.documentElement.classList.contains('dark');$('#theme-toggle').setAttribute('aria-pressed',dark);$('#theme-toggle').textContent=dark?'☾':'☼';$('#theme-toggle').setAttribute('aria-label',dark?'切换浅色模式':'切换深色模式');}
$('#theme-toggle').addEventListener('click',()=>{const dark=document.documentElement.classList.toggle('dark');try{localStorage.setItem('paperbank-theme',dark?'dark':'light');}catch{}themeState();});
document.addEventListener('keydown',e=>{if(e.key==='/'&&!['INPUT','TEXTAREA'].includes(document.activeElement.tagName)&&!e.ctrlKey&&!e.metaKey&&!e.altKey){e.preventDefault();$('#search').focus();}if(e.key==='Escape'){closeMenu();if(document.activeElement===$('#search')){$('#search').value='';sync();}}});
function revealTarget(target,scroll=true){
 if(!target)return;
 if(target.closest('.tool-item[hidden]')&&$('#tool-search')){
  $('#tool-search').value='';$('#tool-search').dispatchEvent(new Event('input'));
 }
 if(target.closest('[hidden]'))reset();
 for(let ancestor=target;ancestor;ancestor=ancestor.parentElement){if(ancestor.tagName==='DETAILS'){ancestor.open=true;delete ancestor.dataset.filterOpened;}}
 if(scroll)target.scrollIntoView({behavior:'instant'});
}
function reveal(){let id;try{id=decodeURIComponent(location.hash.slice(1));}catch{return;}revealTarget(document.getElementById(id));}
$$('a[href^="#"]').forEach(a=>a.addEventListener('click',()=>{let id;try{id=decodeURIComponent(a.hash.slice(1));}catch{return;}revealTarget(document.getElementById(id),false);closeMenu();}));
window.addEventListener('hashchange',reveal);
document.addEventListener('paperbank:notes-open',closeMenu);
document.addEventListener('paperbank:annotation-focus',event=>{
 const target=event.detail;
 if(target instanceof Element&&target.closest('[data-annotatable]'))revealTarget(target,false);
});
$$('.copy').forEach(b=>b.addEventListener('click',async()=>{
 try{
  const text=b.hasAttribute('data-copy-text') ? b.dataset.copyText : b.hasAttribute('data-copy-writing-template')
   ? [...b.closest('.writing-template-body').querySelectorAll('[data-template-raw]')].map(p=>p.dataset.templateRaw).join('\n\n')
   : b.previousElementSibling.textContent;
  await navigator.clipboard.writeText(text);b.textContent='已复制';setTimeout(()=>b.textContent=b.dataset.copyLabel||'复制提示词',2000);
 }catch{b.textContent='请选中文字复制';}
}));
sync();themeState();if(location.hash)requestAnimationFrame(reveal);

if($('#tool-search')){
function filterTools(){
 const words=$('#tool-search').value.trim().toLowerCase().split(/\s+/).filter(Boolean), tools=$$('.tool-item');
 for(const tool of tools)tool.hidden=!words.every(word=>tool.textContent.toLowerCase().includes(word));
 $$('.tool-group').forEach(group=>group.hidden=!group.querySelector('.tool-item:not([hidden])'));
 const count=tools.filter(tool=>!tool.hidden).length;
 $('#tool-count').textContent=`显示 ${count} / ${tools.length} 项资源`;$('#tool-empty').hidden=count>0;
}
$('#tool-search').addEventListener('input',filterTools);
$$('a[href^="#tools"]').forEach(link=>link.addEventListener('click',()=>{$('#tool-search').value='';filterTools();closeMenu();}));
filterTools();
}

function celebrateCheckin(button){
 let layer=$('#checkin-celebration');
 if(!layer){
  layer=document.createElement('div');layer.id='checkin-celebration';
  layer.setAttribute('aria-hidden','true');layer.setAttribute('data-annotation-exclude','');document.body.append(layer);
 }
 while(layer.childElementCount>=6)layer.firstElementChild.remove();
 const group=document.createElement('div'),rect=button.getBoundingClientRect();
 group.className='checkin-drop';
 group.style.left=Math.max(100,Math.min(innerWidth-110,rect.left+rect.width/2))+'px';
 group.style.top=Math.max(12,Math.min(innerHeight-100,rect.top-12))+'px';
 const accept=document.createElement('span'),star=document.createElement('span');
 accept.className='checkin-drop__accept';accept.textContent='ACCEPT';
 star.className='checkin-drop__star';star.textContent='🌟';
 group.append(accept,star);layer.append(group);setTimeout(()=>group.remove(),1600);
}

async function setupPageStats(){
 const panel=$('#page-stats');if(!panel)return;
 const button=$('#page-like'),likes=$('#page-like-count'),views=$('#page-view-count');
 const status=$('#page-stats-status'),retry=$('#page-stats-retry');
 const endpoint='https://day-blog-comments.pages.dev/stats',page='/PaperBank/';
 const live=location.protocol==='https:'&&location.hostname==='da1yuqin.github.io'&&/^\/StarPaper\/(?:index\.html)?$/.test(location.pathname);
 const uuid=()=>crypto.randomUUID();
 let visitor=uuid(),persistent=false,confirmed=false;
 try{
  const saved=localStorage.getItem('paperbank-stats-visitor-id');
  if(/^[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$/i.test(saved||''))visitor=saved;
  else localStorage.setItem('paperbank-stats-visitor-id',visitor);
  persistent=localStorage.getItem('paperbank-stats-visitor-id')===visitor;
  confirmed=localStorage.getItem('paperbank-stats-checkin')===visitor;
 }catch{}
 const viewEvent={action:'view',page,visitor_id:visitor,event_id:uuid()};
 let stats=null,pending=false,failedAction=null,queuedCheckin=false,queuedRefresh=false;
 function render(){
  if(stats){likes.textContent=stats.likes.toLocaleString();views.textContent=stats.views.toLocaleString();}
  button.setAttribute('aria-pressed',String(confirmed));
  button.querySelector('[data-like-label]').textContent=confirmed?'已打卡 · 再接个 ACCEPT':'点赞打卡';
 }
 async function request(action){
  const controller=new AbortController(),timeout=setTimeout(()=>controller.abort(),12000);
  try{
   const url=new URL(endpoint);url.searchParams.set('page',page);url.searchParams.set('visitor_id',visitor);
   if(action&&!live)throw new Error('Preview is read-only');
   const response=await fetch(action?endpoint:url.toString(),{
    method:action?'POST':'GET',credentials:'omit',cache:'no-store',signal:controller.signal,
    headers:action?{'Content-Type':'application/json'}:{Accept:'application/json'},
    ...(action?{body:JSON.stringify(action)}:{})
   });
   if(!response.ok)throw new Error('Statistics unavailable');
   const data=await response.json();
   if(data.page!==page||!Number.isSafeInteger(data.likes)||data.likes<0||!Number.isSafeInteger(data.views)||data.views<0||typeof data.liked!=='boolean')throw new Error('Invalid statistics');
   if(action?.action==='like'&&!data.liked)throw new Error('Check-in unconfirmed');
   return data;
  }finally{clearTimeout(timeout);}
 }
 async function update(action=null){
  if(pending)return;
  pending=true;retry.disabled=true;retry.hidden=true;panel.setAttribute('aria-busy','true');status.textContent='';
  try{
   const fresh=await request(action);
   stats={...fresh,likes:Math.max(fresh.likes,stats?.likes??0),views:Math.max(fresh.views,stats?.views??0)};
   confirmed=confirmed||fresh.liked;failedAction=null;
   try{
    if(confirmed)localStorage.setItem('paperbank-stats-checkin',visitor);
   }catch{}
   render();
   if(action?.action==='like')status.textContent='打卡成功！祝论文 ACCEPT。';
  }catch{
   failedAction=action;
   status.textContent=action?.action==='like'?'打卡暂未确认，请重试；不会重复计数。':'统计暂时不可用，点击仍可播放动画。';retry.hidden=false;
  }finally{
   pending=false;retry.disabled=false;panel.setAttribute('aria-busy','false');
   if(queuedCheckin&&!confirmed){queuedCheckin=false;await update({action:'like',page,visitor_id:visitor,liked:true});}
   else queuedCheckin=false;
   if(queuedRefresh){queuedRefresh=false;await update();}
  }
 }
 button.addEventListener('click',()=>{
  celebrateCheckin(button);
  if(!live){status.textContent='预览只播放动画。';return;}
  if(!persistent){status.textContent='允许浏览器保存网站数据后即可打卡；动画照常播放。';return;}
  if(confirmed){status.textContent='已打卡，再接一个 ACCEPT！';return;}
  if(pending){queuedCheckin=true;return;}
  update({action:'like',page,visitor_id:visitor,liked:true});
 });
 retry.addEventListener('click',()=>update(failedAction));
 window.addEventListener('storage',event=>{
  if(event.key==='paperbank-stats-checkin'&&event.newValue===visitor){confirmed=true;render();if(pending)queuedRefresh=true;else update();}
 });
 render();await update();
 if(live)await update(viewEvent);
}
setupPageStats();

const backToTop=$('#back-to-top');
if(backToTop){
 const updateBackToTop=()=>{backToTop.hidden=window.scrollY<600;};
 window.addEventListener('scroll',updateBackToTop,{passive:true});
 backToTop.addEventListener('click',()=>{
  window.scrollTo({top:0,behavior:matchMedia('(prefers-reduced-motion:reduce)').matches?'instant':'smooth'});
  $('#main').setAttribute('tabindex','-1');$('#main').focus({preventScroll:true});
 });
 updateBackToTop();
}
