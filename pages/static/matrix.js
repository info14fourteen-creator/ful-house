/* Fullhouse UI extension; no model keys or credentials are stored here. */
(() => {
  'use strict';
  document.documentElement.classList.remove('light');
  document.documentElement.classList.add('dark');
  localStorage.setItem('theme','dark');
  const controls=document.createElement('aside');
  controls.id='fh-controls'; controls.hidden=true; controls.setAttribute('aria-label','Управление сервером');
  controls.innerHTML='<span id="fh-dot"></span><span id="fh-status" role="status" aria-live="polite">Проверяем сервер…</span><button id="fh-toggle" type="button">Запустить</button>';
  const wait=document.createElement('section');wait.id='fh-wait';wait.hidden=true;wait.setAttribute('aria-label','Запуск сервера');
  wait.innerHTML='<canvas id="fh-rain" aria-hidden="true"></canvas><div class="fh-wait-copy"><div class="fh-eyebrow">FUL.HOUSE / ПРАВЕЦ 8А</div><h2>Пробуждаем машину<span class="fh-cursor"></span></h2><p id="fh-phase" role="status" aria-live="polite">Запускаем сервер</p><button id="fh-hide" type="button">Вернуться к чатам</button></div>';
  document.body.append(controls,wait);
  const status=controls.querySelector('#fh-status'),toggle=controls.querySelector('button'),phase=wait.querySelector('#fh-phase');
  let running=false,busy=false,frame=0,previousFocus=null;
  function showWait(){previousFocus=document.activeElement;wait.hidden=false;wait.querySelector('button').focus();animate();}
  function hideWait(){wait.hidden=true;cancelAnimationFrame(frame);previousFocus?.focus();}
  wait.querySelector('button').onclick=hideWait;
  wait.addEventListener('keydown',e=>{if(e.key==='Escape')hideWait();if(e.key==='Tab'){e.preventDefault();wait.querySelector('button').focus();}});
  const phrases={stopped:'GPU выключен',starting:'Запускаем сервер',loading:'Подготовка',ready:'Готово',stopping:'Останавливаем GPU',unconfigured:'Нужно подключить управление GPU',error:'Ошибка запуска — можно повторить'};
  async function api(path,method='GET'){
    const token=localStorage.getItem('token'); if(!token)throw new Error('auth');
    const r=await fetch('/fulhouse/api/'+path,{method,headers:{Authorization:'Bearer '+token,'Content-Type':'application/json'}});
    if(!r.ok)throw new Error(r.status===401||r.status===403?'auth':'request');
    return r.json();
  }
  async function refresh(){
    if(!localStorage.getItem('token')){controls.hidden=true;return;}
    try {const s=await api('status');controls.hidden=false;running=s.phase==='ready';busy=['starting','loading','stopping'].includes(s.phase);status.textContent=phrases[s.phase]||'Проверяем сервер';phase.textContent=status.textContent;controls.querySelector('#fh-dot').dataset.ready=String(running);toggle.textContent=running?'Выключить':busy?'Подождите…':'Запустить';toggle.disabled=busy||s.phase==='unconfigured';if(running&&!wait.hidden)hideWait();}
    catch(e){if(e.message==='auth'){controls.hidden=true;hideWait();}else {status.textContent='Нет связи с сервером';phase.textContent='Связь прервалась. Повторяем проверку…';}}
  }
  toggle.onclick=async()=>{toggle.disabled=true;try{await api(running?'stop':'start','POST');if(!running)showWait();await refresh();}catch{status.textContent='Не удалось выполнить команду';toggle.disabled=false;}};
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
  refresh();setInterval(()=>{if(!document.hidden)refresh();},4000);
})();
