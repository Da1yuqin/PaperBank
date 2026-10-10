'use strict';
document.documentElement.classList.add('js');
const $=s=>document.querySelector(s), $$=s=>[...document.querySelectorAll(s)];
const lessons=$$('.paragraph-lesson');
try{if(localStorage.getItem('paperbank-theme')==='dark')document.documentElement.classList.add('dark');}catch{}
function sync(){
 const words=$('#search').value.trim().toLowerCase().split(/\s+/).filter(Boolean);
 const filtering=words.length>0;
 let count=0;
 for(const lesson of lessons){lesson.hidden=!words.every(w=>lesson.textContent.toLowerCase().includes(w));if(!lesson.hidden)count++;}
 $$('.chapter').forEach(chapter=>{
  chapter.hidden=!chapter.querySelector('.paragraph-lesson:not([hidden])');
  chapter.querySelectorAll('.more-lessons').forEach(detail=>{
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
$$('.copy').forEach(b=>b.addEventListener('click',async()=>{try{await navigator.clipboard.writeText(b.previousElementSibling.textContent);b.textContent='已复制';setTimeout(()=>b.textContent=b.dataset.copyLabel||'复制提示词',2000);}catch{b.textContent='请选中文字复制';}}));
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
