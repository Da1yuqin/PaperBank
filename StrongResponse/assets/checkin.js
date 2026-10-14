'use strict';
(() => {
 const panel=document.querySelector('#page-stats');if(!panel)return;
 const button=document.querySelector('#page-like'),likes=document.querySelector('#page-like-count');
 const status=document.querySelector('#page-stats-status'),retry=document.querySelector('#page-stats-retry');
 const endpoint='https://day-blog-comments.pages.dev/stats',page='/StarPaper/StrongResponse/';
 const storageKey='strongresponse-stats-visitor-id',checkinKey='strongresponse-stats-checkin';
 const live=location.protocol==='https:'&&location.hostname==='da1yuqin.github.io'&&/^\/StarPaper\/StrongResponse\/(?:index\.html)?$/.test(location.pathname);
 const uuid=()=>crypto.randomUUID();
 let visitor=uuid(),persistent=false,confirmed=false;
 try{
  const saved=localStorage.getItem(storageKey);
  if(/^[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$/i.test(saved||''))visitor=saved;
  else localStorage.setItem(storageKey,visitor);
  persistent=localStorage.getItem(storageKey)===visitor;
  confirmed=localStorage.getItem(checkinKey)===visitor;
 }catch{}
 const star=(x,y,className='')=>`<path class="${className}" transform="translate(${x} ${y})" d="M0-9 2.6-3.3 9-2.8 4.2 1.6 5.6 8 0 4.8-5.6 8-4.2 1.6-9-2.8-2.6-3.3Z"/>`;
 const paperFace='<rect x="17" y="12" width="124" height="132" rx="17" fill="#fffaf0" stroke="#183247" stroke-width="4"/><path d="M35 46h35m-35 12h25" stroke="#a3b5bf" stroke-width="5" stroke-linecap="round"/><circle cx="65" cy="84" r="4" fill="#183247"/><circle cx="92" cy="84" r="4" fill="#183247"/><path d="M70 95q9 10 18 0" fill="none" stroke="#183247" stroke-width="4" stroke-linecap="round"/><circle cx="52" cy="94" r="7" fill="#f5b2a0"/><circle cx="106" cy="94" r="7" fill="#f5b2a0"/>';
 const cartoons=[
  {name:'stars',drawing:`${paperFace}<g fill="#ffd35b" stroke="#183247" stroke-width="2">${[43,61,79,97,115].map((x,i)=>star(x,124,i>1?'checkin-new-star':'')).join('')}</g><path class="checkin-rise-arrow" d="M120 64V27m-11 11 11-11 11 11" fill="none" stroke="#45a783" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/>`},
  {name:'bars',drawing:`${paperFace}<path d="M39 129h78" stroke="#183247" stroke-width="3" stroke-linecap="round"/><g stroke="#183247" stroke-width="2"><rect x="45" y="110" width="15" height="18" rx="3" fill="#82b6e0"/><rect class="checkin-growing-bar" x="71" y="100" width="15" height="28" rx="3" fill="#64bbae"/><rect class="checkin-growing-bar checkin-growing-bar--last" x="97" y="87" width="15" height="41" rx="3" fill="#ffd35b"/></g><path class="checkin-rise-arrow" d="m84 51 29-23m-16-2 18 0-2 18" fill="none" stroke="#45a783" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/>`},
  {name:'reviewer',drawing:`<path d="M38 74 29 29 62 44m41 0 28-15-6 46" fill="#c88954" stroke="#183247" stroke-width="4" stroke-linejoin="round"/><path d="M40 41 45 63 55 48m60 0 6 15 4-22" fill="#f2bda5"/><path d="M39 80c0-37 78-37 78 0v12c0 28-78 28-78 0Z" fill="#e7b078" stroke="#183247" stroke-width="4"/><path d="M78 81v8m-18 6q18 16 36 0" fill="none" stroke="#183247" stroke-width="4" stroke-linecap="round"/><g fill="#fff6d9" stroke="#183247" stroke-width="4"><rect x="45" y="65" width="26" height="18" rx="6"/><rect x="87" y="65" width="26" height="18" rx="6"/><path d="M71 71h16"/></g><circle cx="59" cy="73" r="3" fill="#183247"/><circle cx="100" cy="73" r="3" fill="#183247"/><path d="m37 117 6 25h71l9-25" fill="#fff" stroke="#183247" stroke-width="4" stroke-linejoin="round"/><g class="checkin-lifted-card"><rect x="30" y="105" width="98" height="28" rx="7" fill="#fffaf0" stroke="#183247" stroke-width="3"/><g fill="#ffd35b" stroke="#183247" stroke-width="1.7">${[43,61,79,97,115].map((x,i)=>star(x,119,i>1?'checkin-new-star':'')).join('')}</g></g><path class="checkin-rise-arrow" d="M135 102V73m-8 8 8-8 8 8" fill="none" stroke="#45a783" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>`}
 ];
 let lastCartoon=-1;
 function celebrate(){
  let layer=document.querySelector('#checkin-celebration');
  if(!layer){layer=document.createElement('div');layer.id='checkin-celebration';layer.setAttribute('aria-hidden','true');layer.setAttribute('data-annotation-exclude','');document.body.append(layer);}
  while(layer.childElementCount>=4)layer.firstElementChild.remove();
  const options=cartoons.map((_,i)=>i).filter(i=>i!==lastCartoon);
  const index=options[Math.floor(Math.random()*options.length)];lastCartoon=index;
  const group=document.createElement('div'),rect=button.getBoundingClientRect();
  group.className='checkin-celebration';group.dataset.cartoon=cartoons[index].name;
  group.style.left=Math.max(10,Math.min(innerWidth-200,rect.left+rect.width/2-92))+'px';
  group.style.top=Math.max(70,Math.min(innerHeight-230,rect.top-28))+'px';
  const stamp=document.createElement('span');stamp.className='checkin-accept';stamp.textContent='ACCEPT';
  const cartoon=document.createElement('div');cartoon.className='checkin-cartoon';
  cartoon.innerHTML=`<svg viewBox="0 0 160 160" xmlns="http://www.w3.org/2000/svg">${cartoons[index].drawing}<g class="checkin-sparkles" fill="#ffd35b" stroke="#183247" stroke-width="1.5">${star(11,20)}${star(146,52)}${star(141,140)}</g></svg>`;
  group.append(stamp,cartoon);layer.append(group);setTimeout(()=>group.remove(),2400);
 }
 const viewEvent={action:'view',page,visitor_id:visitor,event_id:uuid()};
 let stats=null,pending=false,activeAction=null,failedAction=null,queuedCheckin=false,queuedRefresh=false;
 function render(){
  likes.textContent=stats?stats.likes.toLocaleString():'—';
  button.setAttribute('aria-pressed',String(confirmed));
  button.querySelector('[data-like-label]').textContent=confirmed?'已打卡 · 再接个 ACCEPT':'点赞打卡';
 }
 async function request(action){
  const controller=new AbortController(),timeout=setTimeout(()=>controller.abort(),12000);
  try{
   const url=new URL(endpoint);url.searchParams.set('page',page);url.searchParams.set('visitor_id',visitor);
   if(action&&!live)throw new Error('Preview is read-only');
   const response=await fetch(action?endpoint:url.toString(),{method:action?'POST':'GET',credentials:'omit',cache:'no-store',signal:controller.signal,
    headers:action?{'Content-Type':'application/json'}:{Accept:'application/json'},...(action?{body:JSON.stringify(action)}:{})});
   if(!response.ok)throw new Error('Statistics unavailable');
   const data=await response.json();
   if(data.page!==page||!Number.isSafeInteger(data.likes)||data.likes<0||!Number.isSafeInteger(data.views)||data.views<0||typeof data.liked!=='boolean')throw new Error('Invalid statistics');
   if(action?.action==='like'&&!data.liked)throw new Error('Check-in unconfirmed');
   return data;
  }finally{clearTimeout(timeout);}
 }
 async function update(action=null){
  if(pending)return;
  pending=true;activeAction=action?.action;retry.disabled=true;retry.hidden=true;panel.setAttribute('aria-busy','true');status.textContent='';
  try{
   stats=await request(action);confirmed=stats.liked;failedAction=null;
   try{if(confirmed)localStorage.setItem(checkinKey,visitor);else localStorage.removeItem(checkinKey);}catch{}
   render();if(action?.action==='like')status.textContent='打卡成功！祝论文 ACCEPT。';
  }catch{
   failedAction=action;
   status.textContent=action?.action==='like'?'打卡暂未确认，请重试；不会重复计数。':'统计暂时不可用，点击仍可播放动画。';retry.hidden=false;
  }finally{
   pending=false;activeAction=null;retry.disabled=false;panel.setAttribute('aria-busy','false');
   if(queuedCheckin&&!confirmed){queuedCheckin=false;await update({action:'like',page,visitor_id:visitor,liked:true});}else queuedCheckin=false;
   if(queuedRefresh){queuedRefresh=false;await update();}
  }
 }
 button.addEventListener('click',()=>{
  celebrate();
  if(!live){status.textContent='预览只播放动画。';return;}
  if(!persistent){status.textContent='允许浏览器保存网站数据后即可打卡；动画照常播放。';return;}
  if(confirmed){status.textContent='已打卡，再接一个 ACCEPT！';return;}
  if(pending){queuedCheckin=activeAction!=='like';return;}
  update({action:'like',page,visitor_id:visitor,liked:true});
 });
 retry.addEventListener('click',()=>update(failedAction));
 window.addEventListener('storage',event=>{
  if(event.key===checkinKey&&event.newValue===visitor){confirmed=true;render();if(pending)queuedRefresh=true;else update();}
 });
 render();update().then(()=>{if(live)update(viewEvent);});
})();
