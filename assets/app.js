'use strict';
document.documentElement.classList.add('js');
const $=s=>document.querySelector(s), $$=s=>[...document.querySelectorAll(s)];
const entries=$$('.entry'), lessons=$$('.paragraph-lesson'), checks=$$('.task-check');
let checked=new Set();
try{const value=JSON.parse(localStorage.getItem('paperbank-checked')||'[]');if(Array.isArray(value))checked=new Set(value);if(localStorage.getItem('paperbank-theme')==='dark')document.documentElement.classList.add('dark');}catch{}
const filters={chapter:'all',priority:false,todo:false};
function sync(){
 const words=$('#search').value.trim().toLowerCase().split(/\s+/).filter(Boolean);let count=0, lessonCount=0;
 const filtering=words.length>0||filters.priority||filters.todo;
 for(const entry of entries){const done=checked.has(entry.id);entry.classList.toggle('checked',done);entry.querySelector('.task-check').checked=done;entry.hidden=!((filters.chapter==='all'||entry.dataset.section===filters.chapter)&&(!filters.priority||entry.dataset.priority==='先做')&&(!filters.todo||!done)&&words.every(w=>entry.textContent.toLowerCase().includes(w)));if(!entry.hidden)count++;}
 for(const lesson of lessons){lesson.hidden=!((filters.chapter==='all'||lesson.dataset.section===filters.chapter)&&words.every(w=>lesson.textContent.toLowerCase().includes(w)));if(!lesson.hidden)lessonCount++;}
 $$('.chapter').forEach(c=>{
  const n=c.querySelectorAll('.entry:not([hidden])').length, paragraphs=c.querySelectorAll('.paragraph-lesson:not([hidden])').length;
  c.hidden=!n&&!paragraphs;
  const shown=c.querySelector('.shown');if(shown)shown.textContent=paragraphs?`${paragraphs} 段 · ${n} 项检查`:`${n} 项检查`;
  c.querySelectorAll('.more-lessons').forEach(detail=>{const matches=detail.querySelector('.paragraph-lesson:not([hidden])');detail.hidden=!matches;if(filtering&&matches&&!detail.open){detail.dataset.filterOpened='true';detail.open=true;}else if(!filtering&&detail.dataset.filterOpened){detail.open=false;delete detail.dataset.filterOpened;}});
  c.querySelectorAll('.chapter-checks').forEach(detail=>{
   const matches=detail.querySelector('.entry:not([hidden])');detail.hidden=!matches;
   if(filtering&&matches&&!detail.open){detail.dataset.filterOpened='true';detail.open=true;}
   else if(!filtering&&detail.dataset.filterOpened){detail.open=false;delete detail.dataset.filterOpened;}
  });
 });
 $$('.check-group').forEach(g=>g.hidden=!g.querySelector('.entry:not([hidden])'));
 $('#count').textContent=lessons.length?`显示 ${lessonCount} / ${lessons.length} 段；${count} / ${entries.length} 项检查`:`显示 ${count} / ${entries.length} 项`;
 const done=entries.filter(e=>checked.has(e.id)).length;
 $('#progress').textContent=`已检查 ${done} / ${entries.length} 项`;
 $('#empty').hidden=count+lessonCount>0;
 $$('[data-chapter]').forEach(b=>{const active=b.dataset.chapter===filters.chapter;b.classList.toggle('active',active);b.setAttribute('aria-pressed',active);});
 $('#priority-only').setAttribute('aria-pressed',filters.priority);$('#todo-only').setAttribute('aria-pressed',filters.todo);
}
function save(){try{localStorage.setItem('paperbank-checked',JSON.stringify([...checked]));}catch{$('#storage-note').hidden=false;}}
function closeMenu(){$('#sidebar').classList.remove('open');$('#mobile-toggle').setAttribute('aria-expanded','false');}
function reset(){filters.chapter='all';filters.priority=false;filters.todo=false;$('#search').value='';sync();}
$('#search').addEventListener('input',sync);
$$('[data-chapter]').forEach(b=>b.addEventListener('click',()=>{filters.chapter=b.dataset.chapter;sync();closeMenu();$('#entries').scrollIntoView({behavior:'instant'});}));
for(const [id,key] of [['priority-only','priority'],['todo-only','todo']])$("#"+id).addEventListener('click',()=>{filters[key]=!filters[key];sync();});
$$('[data-reset]').forEach(b=>b.addEventListener('click',reset));
checks.forEach(c=>c.addEventListener('change',()=>{c.checked?checked.add(c.dataset.id):checked.delete(c.dataset.id);save();sync();}));
$('#reset-progress').addEventListener('click',()=>{checked.clear();save();sync();});
$('#mobile-toggle').addEventListener('click',()=>{const open=$('#sidebar').classList.toggle('open');$('#mobile-toggle').setAttribute('aria-expanded',open);});
function themeState(){const dark=document.documentElement.classList.contains('dark');$('#theme-toggle').setAttribute('aria-pressed',dark);$('#theme-toggle').textContent=dark?'☾':'☼';$('#theme-toggle').setAttribute('aria-label',dark?'切换浅色模式':'切换深色模式');}
$('#theme-toggle').addEventListener('click',()=>{const dark=document.documentElement.classList.toggle('dark');try{localStorage.setItem('paperbank-theme',dark?'dark':'light');}catch{}themeState();});
document.addEventListener('keydown',e=>{if(e.key==='/'&&!['INPUT','TEXTAREA'].includes(document.activeElement.tagName)&&!e.ctrlKey&&!e.metaKey&&!e.altKey){e.preventDefault();$('#search').focus();}if(e.key==='Escape'){closeMenu();if(document.activeElement===$('#search')){$('#search').value='';sync();}}});
function revealTarget(target,scroll=true){
 if(!target)return;
 if(target.closest('[hidden]'))reset();
 const entry=target.closest('.entry');
 if(entry)entry.querySelector('.explain').open=true;
 for(let ancestor=target;ancestor;ancestor=ancestor.parentElement){if(ancestor.tagName==='DETAILS'){ancestor.open=true;delete ancestor.dataset.filterOpened;}}
 if(scroll)target.scrollIntoView({behavior:'instant'});
}
function reveal(){let id;try{id=decodeURIComponent(location.hash.slice(1));}catch{return;}revealTarget(document.getElementById(id));}
$$('a[href^="#"]').forEach(a=>a.addEventListener('click',()=>{let id;try{id=decodeURIComponent(a.hash.slice(1));}catch{return;}revealTarget(document.getElementById(id),false);closeMenu();}));
window.addEventListener('hashchange',reveal);
$$('.copy').forEach(b=>b.addEventListener('click',async()=>{try{await navigator.clipboard.writeText(b.previousElementSibling.textContent);b.textContent='已复制';setTimeout(()=>b.textContent='复制提示词',2000);}catch{b.textContent='请选中文字复制';}}));
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
