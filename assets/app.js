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
const lessons=$$('.paragraph-lesson');
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
  chapter.hidden=!chapter.querySelector('.paragraph-lesson:not([hidden])');
  chapter.querySelectorAll('.more-lessons,.chapter-templates').forEach(detail=>{
   const matches=detail.querySelector('.paragraph-lesson:not([hidden])');detail.hidden=!matches;
   if(filtering&&matches&&!detail.open){detail.dataset.filterOpened='true';detail.open=true;}
   else if(!filtering&&detail.dataset.filterOpened){detail.open=false;delete detail.dataset.filterOpened;}
  });
 });
 $('#count').hidden=!filtering;
 $('#count').textContent=`找到 ${count} 段`;
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
  const text=b.hasAttribute('data-copy-writing-template')
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
