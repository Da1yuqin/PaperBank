(function () {
  'use strict';
  const section = document.getElementById('footprints');
  if (!section) return;
  const api = section.dataset.api, page = section.dataset.page;
  const mainForm = section.querySelector('form'), list = section.querySelector('.blog-comments__list');
  const body = document.querySelector('[data-annotatable]');
  let comments = [], pending = null, ranges = [], lastFocus;
  const liking = new Set();
  let visitor = null;
  try {
    const key = 'paperbank-stats-visitor-id';
    let saved = localStorage.getItem(key);
    if (!/^[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$/i.test(saved || '')) {
      saved = crypto.randomUUID(); localStorage.setItem(key, saved);
    }
    if (localStorage.getItem(key) === saved) visitor = saved;
  } catch {}
  const element = (tag, className, text) => {
    const el = document.createElement(tag); if (className) el.className = className;
    if (text !== undefined) el.textContent = text; return el;
  };
  const action = (label, handler) => {
    const button = element('button', 'blog-comments__link', label); button.type = 'button';
    button.addEventListener('click', handler); return button;
  };
  async function request(path, options) {
    const controller = new AbortController(), timer = setTimeout(() => controller.abort(), 12000);
    try {
      const response = await fetch(api.replace(/\/$/, '') + path, {...options, signal: controller.signal});
      const result = await response.json();
      if (!response.ok) throw new Error(result.error || '评论服务暂时不可用。');
      return result;
    } finally { clearTimeout(timer); }
  }
  function setContext(form, parent, anchor) {
    form._parent = parent || null; form._anchor = anchor || null;
    const box = form.querySelector('.blog-comments__context');
    box.hidden = !parent && !anchor;
    box.querySelector('span').textContent = parent ? '回复 ' + (parent.name || '匿名') : anchor ? '批注所选正文' : '';
  }
  function bindForm(form) {
    const button = form.querySelector('[type=submit]'), status = form.querySelector('.blog-comments__status');
    button.disabled = !api;
    form.querySelector('[data-cancel-context]').addEventListener('click', () => {
      setContext(form, null, null); if (form === noteForm) {form.hidden = true; quotePreview.hidden = true; noteList.hidden = false;}
    });
    form.addEventListener('submit', async event => {
      event.preventDefault(); if (button.disabled || !form.reportValidity()) return;
      button.disabled = true; status.textContent = '正在发布…';
      const visibility = 'public';
      try {
        await request('/comments', {method: 'POST', headers: {'Content-Type': 'application/json'}, body: JSON.stringify({
          page, name: form.elements.name.value, content: form.elements.content.value, visibility,
          parent_id: form._parent ? form._parent.id : null, anchor: form._anchor || null
        })});
        form.elements.content.value = '';
        status.textContent = '评论已公开发布。';
        setContext(form, null, null);
        try { await load(); } catch (_) { status.textContent += ' 列表暂时加载失败，请稍后刷新。'; }
        if (form === noteForm) { panelStatus.textContent = status.textContent; form.hidden = true; quotePreview.hidden = true; noteList.hidden = false; }
      } catch (error) {
        status.textContent = error.name === 'AbortError' || error.message === 'Failed to fetch' ? '连接失败，请稍后重试；输入内容已保留。' : error.message;
      } finally { button.disabled = false; }
    });
  }
  let panel, noteForm, noteList, quotePreview, selectButton, toggle, panelStatus;
  function openNotes(focus = true) {
    if (!panel) return;
    if (panel.hidden) lastFocus = document.activeElement;
    panel.hidden = false; document.body.classList.add('day-notes-open');
    toggle.setAttribute('aria-expanded', 'true');
    document.dispatchEvent(new Event('paperbank:notes-open'));
    if (focus) panel.querySelector('[data-close-notes]').focus();
  }
  function closeNotes() {
    if (!panel || panel.hidden) return;
    panel.hidden = true; document.body.classList.remove('day-notes-open');
    toggle.setAttribute('aria-expanded', 'false');
    if (lastFocus && lastFocus.isConnected) lastFocus.focus();
  }
  function replyTo(comment, inNotes) {
    const form = inNotes ? noteForm : mainForm;
    setContext(form, comment, null); form.hidden = false;
    if (inNotes) { noteList.hidden = false; quotePreview.hidden = true; openNotes(false); }
    else form.scrollIntoView({block:'center', behavior:'smooth'});
    form.elements.content.focus();
  }
  function updateCommentLike(comment, buttons = document.querySelectorAll('[data-comment-like="' + comment.id + '"]')) {
    buttons.forEach(button => {
      button.textContent = (comment.liked ? '♥ 已赞 ' : '♡ 点赞 ') + comment.likes;
      button.setAttribute('aria-pressed', String(comment.liked));
      button.disabled = comment.liked || liking.has(comment.id);
    });
  }
  async function likeComment(comment, inNotes) {
    const status = inNotes ? panelStatus : mainForm.querySelector('.blog-comments__status');
    if (!visitor) {status.textContent = '允许浏览器保存网站数据后即可点赞。'; return;}
    if (comment.liked || liking.has(comment.id)) return;
    liking.add(comment.id); updateCommentLike(comment); status.textContent = '';
    try {
      const result = await request('/comments?action=like', {method: 'POST', headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({page, comment_id: comment.id, visitor_id: visitor})});
      if (result.comment_id !== comment.id || !Number.isSafeInteger(result.likes) || result.likes < 0 || result.liked !== true) throw new Error('点赞未确认。');
      const current = comments.find(item => item.id === comment.id);
      comment.likes = Math.max(comment.likes, result.likes, current?.likes || 0); comment.liked = true;
      if (current) {current.likes = comment.likes; current.liked = true;}
    } catch (error) {
      status.textContent = error.name === 'AbortError' || error.message === 'Failed to fetch' ? '点赞暂未确认，可重试；不会重复计数。' : error.message;
    } finally {liking.delete(comment.id); updateCommentLike(comments.find(item => item.id === comment.id) || comment);}
  }
  function renderComment(comment, host, inNotes, parent) {
    const item = element('article', 'blog-comments__item'); item.dataset.commentId = comment.id;
    const time = element('time', '', new Date(comment.created_at).toLocaleDateString('zh-CN')); time.dateTime = comment.created_at;
    item.append(element('strong', '', comment.name || '匿名'), time);
    if (parent) item.append(element('span', 'blog-comments__reply-to', '回复 ' + (parent.name || '匿名')));
    const actions = element('div', 'blog-comments__item-actions');
    const like = action('', () => likeComment(comment, inNotes));
    like.className = 'blog-comments__like'; like.dataset.commentLike = comment.id;
    actions.append(action('回复', () => replyTo(comment, inNotes)), like);
    item.append(element('p', '', comment.content), actions); host.append(item); updateCommentLike(comment, [like]);
    return item;
  }
  function renderThread(root, host, inNotes) {
    const first = renderComment(root, host, inNotes), children = element('div', 'blog-comments__replies');
    const visited = new Set([root.id]);
    // Keep the visual indentation constant even when a conversation has many levels.
    function walk(parent) {
      comments.filter(c => c.parent_id === parent.id && !visited.has(c.id)).sort((a,b) => a.id-b.id).forEach(c => {
        visited.add(c.id); renderComment(c, children, inNotes, parent); walk(c);
      });
    }
    walk(root); if (children.childElementCount) first.append(children);
  }
  function textIndex() {
    const nodes = [], walker = document.createTreeWalker(body, NodeFilter.SHOW_TEXT);
    let node, text = '';
    while ((node = walker.nextNode())) {
      // Keep folded and search-hidden prose in the index so anchors stay stable.
      if (node.parentElement.closest('script, style, form, button, input, textarea, select, .shown, #tool-count, #tool-empty, [data-annotation-exclude]')) continue;
      nodes.push({node, start:text.length, end:text.length + node.length}); text += node.data;
    }
    return {nodes, text};
  }
  function pointOffset(index, node, offset) {
    const textNode = index.nodes.find(part => part.node === node);
    if (textNode) return textNode.start + offset;
    const boundary = document.createRange();
    boundary.setStart(node, offset); boundary.collapse(true);
    const next = index.nodes.find(part => boundary.comparePoint(part.node, 0) >= 0);
    return next ? next.start : index.text.length;
  }
  function locate(anchor, text) {
    if (text.slice(anchor.start, anchor.end) === anchor.exact &&
        text.slice(Math.max(0,anchor.start-anchor.prefix.length), anchor.start) === anchor.prefix &&
        text.slice(anchor.end, anchor.end+anchor.suffix.length) === anchor.suffix) return anchor.start;
    const candidates = []; let at = text.indexOf(anchor.exact);
    while (at !== -1) { candidates.push(at); at = text.indexOf(anchor.exact, at+1); }
    const matched = candidates.filter(pos => (!anchor.prefix || text.slice(Math.max(0,pos-anchor.prefix.length),pos).endsWith(anchor.prefix)) &&
      (!anchor.suffix || text.slice(pos+anchor.exact.length,pos+anchor.exact.length+anchor.suffix.length).startsWith(anchor.suffix)));
    return matched.length === 1 ? matched[0] : candidates.length === 1 ? candidates[0] : -1;
  }
  function makeRange(index, start, end) {
    const first = index.nodes.find(n => n.start <= start && n.end > start);
    const last = index.nodes.find(n => n.start < end && n.end >= end);
    if (!first || !last) return null;
    const range = document.createRange(); range.setStart(first.node, start-first.start); range.setEnd(last.node, end-last.start); return range;
  }
  function highlight(roots) {
    if (!body) return;
    body.querySelectorAll('mark.day-text-highlight').forEach(mark => mark.replaceWith(...mark.childNodes)); body.normalize();
    const index = textIndex(); ranges = [];
    roots.forEach(c => {
      const start = locate(c.anchor,index.text), range = start < 0 ? null : makeRange(index,start,start+c.anchor.exact.length);
      if (range) ranges.push({comment:c, range, start, end:start+c.anchor.exact.length});
    });
    if (window.CSS && CSS.highlights && window.Highlight) CSS.highlights.set('day-notes', new Highlight(...ranges.map(r => r.range)));
    else {
      // Split text only; never replace links, images or other article elements.
      index.nodes.slice().reverse().forEach(n => {
        const segments = ranges.filter(r => r.start < n.end && r.end > n.start).map(r => [Math.max(0,r.start-n.start),Math.min(n.node.length,r.end-n.start)]).sort((a,b)=>a[0]-b[0]);
        const merged=[]; segments.forEach(s => {const last=merged[merged.length-1]; if(last && s[0]<=last[1]) last[1]=Math.max(last[1],s[1]); else merged.push(s);});
        merged.reverse().forEach(([start,end]) => {const text=n.node.splitText(start); text.splitText(end-start); const mark=element('mark','day-text-highlight'); text.replaceWith(mark); mark.append(text);});
      });
    }
    return ranges;
  }
  function render() {
    list.replaceChildren(); if (noteList) noteList.replaceChildren();
    const ids = new Set(comments.map(c => c.id));
    const roots = comments.filter(c => !c.parent_id || !ids.has(c.parent_id));
    const notes = roots.filter(c => c.anchor);
    const resolved = highlight(notes) || [];
    roots.filter(c => !c.anchor).forEach(c => renderThread(c,list,false));
    section.querySelector('.blog-comments__empty').hidden = list.childElementCount > 0;
    if (noteList) {
      section.querySelector('[data-note-count]').textContent = notes.length; toggle.textContent = '批注 ' + notes.length;
      if (!notes.length) noteList.append(element('p','day-notes__intro','选中一句正文，留下你的想法。'));
      notes.forEach(c => {
        const thread = element('section', 'day-notes__thread'), quote = action('', () => {
          const found = ranges.find(r => r.comment.id === c.id); if (!found) return;
          document.dispatchEvent(new CustomEvent('paperbank:annotation-focus', {detail: found.range.startContainer.parentElement}));
          const rect = found.range.getBoundingClientRect(); window.scrollBy({top:rect.top-120, behavior:'smooth'});
        });
        quote.className = 'day-notes__quote'; quote.append(element('blockquote','',c.anchor.exact)); thread.append(quote);
        if (!resolved.some(r=>r.comment.id===c.id)) thread.append(element('p','day-notes__notice','正文已变动，保留原文引用。'));
        renderThread(c,thread,true); noteList.append(thread);
      });
    }
  }
  async function load() {
    const result = await request('/comments?page=' + encodeURIComponent(page) + (visitor ? '&visitor_id=' + encodeURIComponent(visitor) : ''));
    if (!Array.isArray(result.comments) || result.comments.some(comment => !Number.isSafeInteger(comment.likes) || comment.likes < 0 || typeof comment.liked !== 'boolean')) throw new Error('评论列表暂时不可用。');
    const previous = new Map(comments.map(comment => [comment.id, comment]));
    comments = result.comments.map(comment => {
      const saved = previous.get(comment.id);
      return {...comment, likes: Math.max(comment.likes, saved?.likes || 0), liked: comment.liked || saved?.liked === true};
    });
    render();
  }
  if (body) {
    section.querySelector('.blog-comments__annotation-hint').hidden = false;
    panel = element('aside','day-notes'); panel.id = 'paperbank-notes'; panel.hidden = true; panel.setAttribute('aria-label','正文批注');
    panel.innerHTML = '<div class="day-notes__header"><h2>正文批注</h2><button type="button" class="blog-comments__link" data-close-notes aria-label="关闭批注">关闭 ×</button></div><p class="day-notes__intro">选中正文后留下批注；公开批注会高亮显示。</p>';
    noteList = element('div','day-notes__list'); quotePreview = element('blockquote','day-notes__draft-quote'); quotePreview.hidden = true;
    noteForm = mainForm.cloneNode(true); noteForm.hidden = true;
    noteForm.querySelectorAll('[id]').forEach(el => el.removeAttribute('id'));
    panelStatus = element('p','day-notes__notice'); panelStatus.setAttribute('role','status'); panel.append(panelStatus,noteList,quotePreview,noteForm); document.body.append(panel);
    panel.querySelector('[data-close-notes]').addEventListener('click',closeNotes);
    toggle = action('批注 0', () => openNotes()); toggle.className = 'day-annotation-toggle'; document.body.append(toggle);
    toggle.setAttribute('aria-controls', panel.id); toggle.setAttribute('aria-expanded', 'false');
    section.querySelector('[data-open-notes]').addEventListener('click', () => openNotes());
    selectButton = action('批注', () => {
      if (!pending) return;
      panelStatus.textContent=''; noteList.hidden=true; setContext(noteForm,null,pending); quotePreview.textContent = pending.exact; quotePreview.hidden = false; noteForm.hidden = false;
      selectButton.hidden = true; openNotes(false); lastFocus = toggle; noteForm.elements.content.focus();
    });
    selectButton.className = 'day-annotation-selection'; selectButton.hidden = true; document.body.append(selectButton);
    selectButton.addEventListener('pointerdown',event => event.preventDefault());
    function selection() {
      const selected = window.getSelection();
      if (!selected.rangeCount || selected.isCollapsed) {selectButton.hidden=true; return;}
      const range=selected.getRangeAt(0);
      if (!body.contains(range.startContainer) || !body.contains(range.endContainer)) {selectButton.hidden=true;return;}
      const exact=range.toString(); if (!exact.trim()) {selectButton.hidden=true;return;}
      const index=textIndex(), start=pointOffset(index,range.startContainer,range.startOffset), end=pointOffset(index,range.endContainer,range.endOffset);
      // Reject selections across non-prose controls rather than saving a wrong quote.
      if (index.text.slice(start,end)!==exact) {selectButton.hidden=true;return;}
      pending={exact,start,end,prefix:index.text.slice(Math.max(0,start-48),start),suffix:index.text.slice(end,end+48)};
      const rect=range.getBoundingClientRect(); selectButton.style.top=Math.max(70,Math.min(window.innerHeight-40,rect.bottom+7))+'px';
      selectButton.style.left=Math.max(8,Math.min(window.innerWidth-125,rect.left))+'px';
      selectButton.disabled=exact.length>1000; selectButton.textContent=exact.length>1000?'最多选 1000 字':'批注'; selectButton.hidden=false;
    }
    document.addEventListener('selectionchange',selection);
    document.addEventListener('scroll',()=>{selectButton.hidden=true;},true);
    document.addEventListener('keydown',event=>{if(event.key==='Escape'){selectButton.hidden=true;closeNotes();}});
    body.addEventListener('click',event=>{
      if(!window.getSelection().isCollapsed)return;
      let caret=document.caretRangeFromPoint ? document.caretRangeFromPoint(event.clientX,event.clientY) : null;
      if (!caret && document.caretPositionFromPoint) { const pos=document.caretPositionFromPoint(event.clientX,event.clientY); if(pos){caret=document.createRange();caret.setStart(pos.offsetNode,pos.offset);} }
      if(!caret || !body.contains(caret.startContainer))return;
      const offset=pointOffset(textIndex(),caret.startContainer,caret.startOffset), found=ranges.find(r=>offset>=r.start && offset<r.end);
      if(found){openNotes(false);const target=noteList.querySelector('[data-comment-id="'+found.comment.id+'"]');if(target)target.scrollIntoView({block:'nearest'});}
    });
    bindForm(noteForm);
  }
  bindForm(mainForm);
  if (!api) {mainForm.querySelector('.blog-comments__status').textContent='评论暂未开放。';return;}
  load().catch(()=>{mainForm.querySelector('.blog-comments__status').textContent='公开评论暂时加载失败，请稍后刷新。';});
}());
