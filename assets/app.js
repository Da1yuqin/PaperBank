'use strict';
document.documentElement.classList.add('js');
const $=s=>document.querySelector(s), $$=s=>[...document.querySelectorAll(s)];
const entries=$$('.entry'), checks=$$('.task-check');
let checked=new Set();
try{const value=JSON.parse(localStorage.getItem('paperbank-checked')||'[]');if(Array.isArray(value))checked=new Set(value);if(localStorage.getItem('paperbank-theme')==='dark')document.documentElement.classList.add('dark');}catch{}
const filters={chapter:'all',priority:false,todo:false};
function sync(){
 const words=$('#search').value.trim().toLowerCase().split(/\s+/).filter(Boolean);let count=0;
 for(const entry of entries){const done=checked.has(entry.id);entry.classList.toggle('checked',done);entry.querySelector('.task-check').checked=done;entry.hidden=!((filters.chapter==='all'||entry.dataset.section===filters.chapter)&&(!filters.priority||entry.dataset.priority==='先做')&&(!filters.todo||!done)&&words.every(w=>entry.textContent.toLowerCase().includes(w)));if(!entry.hidden)count++;}
 $$('.chapter').forEach(c=>{const n=c.querySelectorAll('.entry:not([hidden])').length;c.hidden=!n;c.querySelector('.shown').textContent=`${n} 条`;});
 $$('.check-group').forEach(g=>g.hidden=!g.querySelector('.entry:not([hidden])'));
 $('#count').textContent=`显示 ${count} / ${entries.length} 项`;
 const done=entries.filter(e=>checked.has(e.id)).length;
 $('#progress').textContent=`已检查 ${done} / ${entries.length} 项`;
 $('#empty').hidden=count>0;
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
function reveal(){let id;try{id=decodeURIComponent(location.hash.slice(1));}catch{return;}const entry=document.getElementById(id);if(entry?.classList.contains('entry')){if(entry.hidden)reset();entry.querySelector('.explain').open=true;entry.scrollIntoView({behavior:'instant'});}}
$$('a[href^="#tip-"]').forEach(a=>a.addEventListener('click',()=>{const target=document.getElementById(a.hash.slice(1));if(target?.hidden)reset();if(target)target.querySelector('.explain').open=true;closeMenu();}));
window.addEventListener('hashchange',reveal);
$$('.copy').forEach(b=>b.addEventListener('click',async()=>{try{await navigator.clipboard.writeText(b.previousElementSibling.textContent);b.textContent='已复制';setTimeout(()=>b.textContent='复制提示词',2000);}catch{b.textContent='请选中文字复制';}}));
sync();themeState();if(location.hash)requestAnimationFrame(reveal);
