/* Fullhouse UI extension; no model keys or credentials are stored here. */
(() => {
  'use strict';
  document.documentElement.classList.remove('light');
  document.documentElement.classList.add('dark');
  localStorage.setItem('theme','dark');
  const controls=document.createElement('aside');
  controls.id='fh-controls'; controls.hidden=true; controls.setAttribute('aria-label','Server controls');
  controls.innerHTML='<span id="fh-dot"></span><span id="fh-status" role="status" aria-live="polite">Checking server…</span><button id="fh-toggle" type="button">Start</button>';
  const wait=document.createElement('section');wait.id='fh-wait';wait.hidden=true;wait.setAttribute('aria-label','Server startup');
  wait.innerHTML='<canvas id="fh-rain" aria-hidden="true"></canvas><div class="fh-wait-copy"><img src="/matrix-symbol-logo.svg?v=brand-1" alt="ful.house" width="48" height="48"><div class="fh-eyebrow">FUL.HOUSE / PRAVETZ 8A</div><h2>Waking the machine<span class="fh-cursor"></span></h2><p id="fh-phase" role="status" aria-live="polite">Starting server</p><button id="fh-hide" type="button">Back to chats</button></div>';
  document.body.append(controls,wait);
  const status=controls.querySelector('#fh-status'),toggle=controls.querySelector('button'),phase=wait.querySelector('#fh-phase');
  let running=false,busy=false,frame=0,previousFocus=null;
  let startAfterLogin=sessionStorage.getItem('fh-start-after-login')==='1';
  function showWait(){previousFocus=document.activeElement;wait.hidden=false;wait.querySelector('button').focus();animate();}
  function hideWait(){wait.hidden=true;cancelAnimationFrame(frame);previousFocus?.focus();}
  wait.querySelector('button').onclick=hideWait;
  wait.addEventListener('keydown',e=>{if(e.key==='Escape')hideWait();if(e.key==='Tab'){e.preventDefault();wait.querySelector('button').focus();}});
  const phrases={stopped:'Server stopped',starting:'Starting server',loading:'Preparing',ready:'Ready',stopping:'Stopping server',unconfigured:'Server controls unavailable',error:'Startup failed — try again'};
  async function api(path,method='GET'){
    const token=localStorage.getItem('token'); if(!token)throw new Error('auth');
    const r=await fetch('/fulhouse/api/'+path,{method,headers:{Authorization:'Bearer '+token,'Content-Type':'application/json'}});
    if(!r.ok)throw new Error(r.status===401||r.status===403?'auth':'request');
    return r.json();
  }
  async function refresh(){
    if(!localStorage.getItem('token')){controls.hidden=true;return;}
    try {let s=await api('status');
      if(startAfterLogin){
        startAfterLogin=false;sessionStorage.removeItem('fh-start-after-login');
        if(['stopped','error'].includes(s.phase))s=await api('start','POST');
      }
      controls.hidden=false;running=s.phase==='ready';busy=['starting','loading','stopping'].includes(s.phase);status.textContent=s.failure_reason==='capacity'?'No GPU capacity — try again':phrases[s.phase]||'Checking server';phase.textContent=status.textContent;controls.querySelector('#fh-dot').dataset.ready=String(running);toggle.textContent=running?'Stop':busy?'Please wait…':'Start';toggle.disabled=busy||s.phase==='unconfigured';if(running&&!wait.hidden)hideWait();}
    catch(e){if(e.message==='auth'){controls.hidden=true;hideWait();}else {status.textContent='Server unreachable';phase.textContent='Connection lost. Retrying…';}}
  }
  toggle.onclick=async()=>{toggle.disabled=true;try{await api(running?'stop':'start','POST');if(!running)showWait();await refresh();}catch{status.textContent='Command failed';toggle.disabled=false;}};
  function animate(){
    if(matchMedia('(prefers-reduced-motion: reduce)').matches)return;
    const canvas=wait.querySelector('canvas'),ctx=canvas.getContext('2d');if(!ctx)return;
    canvas.width=innerWidth;canvas.height=innerHeight;
    const cell=19,drops=Array.from({length:Math.ceil(canvas.width/cell)},()=>-Math.random()*80),glyphs='01ПРАВЕЦFULHOUSEアイウエオカキクケコ';let last=0;
    function draw(t){if(wait.hidden)return;frame=requestAnimationFrame(draw);if(t-last<55)return;last=t;ctx.fillStyle='rgba(0,0,0,.065)';ctx.fillRect(0,0,canvas.width,canvas.height);ctx.font='14px monospace';drops.forEach((y,i)=>{ctx.fillStyle=Math.random()>.98?'#d3ffce':'#38b72f';ctx.fillText(glyphs[Math.floor(Math.random()*glyphs.length)],i*cell,y*cell);if(y*cell>canvas.height&&Math.random()>.985)drops[i]=-10;else drops[i]++;});}frame=requestAnimationFrame(draw);
  }
  // Upstream SPA redirects must reach the dedicated terminal login at the edge.
  let redirecting=false;
  function terminalLogin(){if(!redirecting&&location.pathname==='/auth'){redirecting=true;location.replace('/auth'+location.search);}}
  const observer=new MutationObserver(terminalLogin);
  observer.observe(document.body,{childList:true,subtree:true});
  addEventListener('popstate',terminalLogin);terminalLogin();
  if(startAfterLogin)showWait();

  const engines={codex:'fullhouse-codex-api',qwen:'huihui_ai/qwen3-coder-abliterated:30b'};
  let engine=localStorage.getItem('fh-engine') || 'qwen';
  if(!engines[engine])engine='qwen';
  function setEngine(next){engine=engines[next]?next:'qwen';localStorage.setItem('fh-engine',engine);document.querySelectorAll('[data-fh-engine]').forEach(button=>button.dataset.active=String(button.dataset.fhEngine===engine));}
  function installEngineButtons(){
    if(location.pathname==='/auth')return;
    const input=document.querySelector('textarea,[contenteditable="true"]');
    if(!input || document.querySelector('#fh-engine-switch'))return;
    const host=input.closest('form') || input.parentElement?.parentElement || input.parentElement;
    if(!host)return;
    const box=document.createElement('div');box.id='fh-engine-switch';box.setAttribute('aria-label','Model engine');
    box.innerHTML='<button type="button" data-fh-engine="codex">CODEX</button><button type="button" data-fh-engine="qwen">QWEN</button>';
    box.addEventListener('click',event=>{const button=event.target.closest('[data-fh-engine]');if(button)setEngine(button.dataset.fhEngine);});
    host.append(box);setEngine(engine);
  }
  function rewriteBody(init){
    if(!init?.body || typeof init.body!=='string')return init;
    try{
      const data=JSON.parse(init.body);
      if(data && (Object.prototype.hasOwnProperty.call(data,'model') || Object.prototype.hasOwnProperty.call(data,'models'))){
        const selected=engines[engine];
        data.model=selected;
        if(Object.prototype.hasOwnProperty.call(data,'models'))data.models=[selected];
        if(Array.isArray(data.model))data.model=[selected];
        return {...init,body:JSON.stringify(data)};
      }
    }catch{}
    return init;
  }
  const nativeFetch=window.fetch.bind(window);
  window.fetch=(resource,init={})=>{
    const url=typeof resource==='string'?resource:resource?.url || '';
    if(/\/(api\/chat|api\/chat\/completions|ollama\/api\/chat|v1\/chat\/completions)(?:\?|$)/.test(url))init=rewriteBody(init);
    return nativeFetch(resource,init);
  };
  setInterval(installEngineButtons,700);installEngineButtons();setEngine(engine);

  refresh();setInterval(()=>{if(!document.hidden)refresh();},4000);
})();
