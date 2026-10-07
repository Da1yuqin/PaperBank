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
function reveal(){let id;try{id=decodeURIComponent(location.hash.slice(1));}catch{return;}const entry=document.getElementById(id);if(entry?.classList.contains('entry')){if(entry.hidden)reset();entry.querySelector('.explain').open=true;entry.scrollIntoView({behavior:'instant'});}else if(entry?.classList.contains('chapter')){if(entry.hidden)reset();entry.scrollIntoView({behavior:'instant'});}}
$$('a[href^="#tip-"]').forEach(a=>a.addEventListener('click',()=>{const target=document.getElementById(a.hash.slice(1));if(target?.hidden)reset();if(target)target.querySelector('.explain').open=true;closeMenu();}));
$$('a[href^="#chapter-"]').forEach(a=>a.addEventListener('click',()=>{if(document.getElementById(a.hash.slice(1))?.hidden)reset();closeMenu();}));
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

const beagle=$('#beagle-companion');
if(beagle){
 const intro=$('#beagle-wake'),wake=$('#beagle-wake-small'),handle=$('#beagle-drag'),dog=$('#beagle-remind'),bubble=$('#beagle-bubble');
 const lines={writing:['先讲清贡献，证据才能跟上。','证据够到哪里，结论就写到哪里。','百分点和相对提升，记得分开写。','回复审稿人：先答问题，再贴证据。','例子可以假设，实验结果不能编。','图里每条连线，都要说得出含义。','先把粗稿写出来，再逐句还债。'],joke:['本行只存证据，不替 p 值提供美颜。','我也在追 deadline，追着追着发现是饭点。','论文三件套：贡献、证据、给我一块小饼干。','西装是工作态度，摇尾巴是同行评议。','你负责论文，我负责装作很懂。','咖啡可以续，结论别无限续杯。']};
 let index={writing:0,joke:0},nextKind='writing',position=null,drag=null,hopTimer;
 function layoutBubble(){
  if(bubble.hidden)return;
  const r=beagle.getBoundingClientRect(),w=bubble.offsetWidth,h=bubble.offsetHeight,edge=$('.topbar').offsetHeight+8;
  const left=Math.max(8,Math.min(r.right-w,innerWidth-w-8));let top=r.top-h-12;if(top<edge)top=r.bottom+12;top=Math.max(edge,Math.min(top,innerHeight-h-8));
  Object.assign(bubble.style,{left:left-r.left+'px',top:top-r.top+'px',right:'auto',bottom:'auto'});bubble.style.setProperty('--beagle-tail',Math.max(10,Math.min(r.left+r.width/2-left-6,w-22))+'px');bubble.classList.toggle('below',top>=r.bottom);bubble.classList.toggle('overlap',top<r.bottom&&top+h>r.top);
 }
 function move(x,y){const r=beagle.getBoundingClientRect(),top=$('.topbar').offsetHeight+8;position={x:Math.max(8,Math.min(x,innerWidth-r.width-8)),y:Math.max(top,Math.min(y,innerHeight-r.height-8))};Object.assign(beagle.style,{left:position.x+'px',top:position.y+'px',right:'auto',bottom:'auto'});layoutBubble();}
 function hideBubble(focus=false){bubble.hidden=true;dog.setAttribute('aria-expanded','false');intro.setAttribute('aria-expanded','false');beagle.dataset.face='happy';clearTimeout(hopTimer);beagle.classList.remove('is-speaking');if(focus)(dog.hidden?wake:dog).focus();}
 function sleep(asleep){hideBubble();dog.hidden=asleep;handle.hidden=asleep;wake.hidden=!asleep;intro.textContent=asleep?'叫醒贝果':'摸摸贝果';if(position)move(position.x,position.y);try{sessionStorage.setItem('paperbank-beagle',asleep?'asleep':'awake');}catch{}}
 function chat(kind){
  if(dog.hidden)sleep(false);$('#beagle-speech').textContent=lines[kind][index[kind]++%lines[kind].length];$('#beagle-mood').textContent=kind==='joke'?'🤭':'✨';beagle.dataset.face=kind==='joke'?'laugh':'wink';bubble.hidden=false;dog.setAttribute('aria-expanded','true');intro.setAttribute('aria-expanded','true');layoutBubble();beagle.classList.remove('is-speaking');void beagle.offsetWidth;beagle.classList.add('is-speaking');clearTimeout(hopTimer);hopTimer=setTimeout(()=>beagle.classList.remove('is-speaking'),650);
 }
 intro.addEventListener('click',()=>chat('writing'));
 wake.addEventListener('click',()=>{sleep(false);chat('writing');dog.focus();});
 $('#beagle-close').addEventListener('click',()=>hideBubble(true));
 dog.addEventListener('click',()=>{chat(nextKind);nextKind=nextKind==='writing'?'joke':'writing';});
 $$('[data-beagle-kind]').forEach(b=>b.addEventListener('click',()=>{if(b.dataset.beagleKind==='sleep'){sleep(true);wake.focus();}else chat(b.dataset.beagleKind);}));
 document.addEventListener('keydown',e=>{if(e.key==='Escape'&&!bubble.hidden){e.preventDefault();hideBubble(beagle.contains(document.activeElement)||document.activeElement===intro);}});
 handle.addEventListener('keydown',e=>{const directions={ArrowLeft:[-1,0],ArrowRight:[1,0],ArrowUp:[0,-1],ArrowDown:[0,1]};if(e.key==='Home'){e.preventDefault();position=null;beagle.removeAttribute('style');layoutBubble();}else if(directions[e.key]){e.preventDefault();const r=beagle.getBoundingClientRect(),step=e.shiftKey?40:10,[dx,dy]=directions[e.key];move(r.left+dx*step,r.top+dy*step);}});
 handle.addEventListener('pointerdown',e=>{if(e.button!==0)return;const r=beagle.getBoundingClientRect();drag={id:e.pointerId,x:e.clientX-r.left,y:e.clientY-r.top};handle.setPointerCapture(e.pointerId);});
 handle.addEventListener('pointermove',e=>{if(drag?.id===e.pointerId)move(e.clientX-drag.x,e.clientY-drag.y);});
 function release(e){if(drag?.id===e.pointerId){drag=null;if(handle.hasPointerCapture(e.pointerId))handle.releasePointerCapture(e.pointerId);}}
 handle.addEventListener('pointerup',release);handle.addEventListener('pointercancel',release);handle.addEventListener('lostpointercapture',()=>{drag=null;});
 window.addEventListener('resize',()=>{if(position)move(position.x,position.y);else layoutBubble();});
 let asleep=false;try{asleep=sessionStorage.getItem('paperbank-beagle')==='asleep';}catch{}beagle.hidden=false;sleep(asleep);
}
