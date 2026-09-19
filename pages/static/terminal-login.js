(() => {
  'use strict';
  const form=document.querySelector('#terminal'),login=document.querySelector('#fh-command'),password=document.querySelector('#fh-response');
  const loginLine=document.querySelector('#login-line'),passwordLine=document.querySelector('#password-line'),feedback=document.querySelector('#feedback');
  let step='login',pending=false;
  const lines=[
    "Follow the white rabbit.",
    "Wake up, Neo.",
    "The Matrix has you.",
    "There is no spoon.",
    "Welcome to the real world.",
    "Guns. Lots of guns.",
    "I know kung fu.",
    "Show me.",
    "Free your mind.",
    "Stop trying to hit me and hit me!",
    "Dodge this.",
    "Ignorance is bliss.",
    "Welcome to the desert of the real.",
    "What is real?",
    "There is no try.",
    "You take the red pill — you stay in Wonderland."
];
  const previous=Number(sessionStorage.getItem('fh-last-movie-line') ?? -1);
  const choices=lines.map((_,i)=>i).filter(i=>i!==previous);
  const selected=choices[crypto.getRandomValues(new Uint32Array(1))[0]%choices.length];
  document.querySelector('.invitation').textContent=lines[selected];
  sessionStorage.setItem('fh-last-movie-line',String(selected));
  const pad=n=>String(n).padStart(2,'0');
  function tick(){const d=new Date(),clock=document.querySelector('#clock');clock.dateTime=d.toISOString();clock.textContent=`${pad(d.getMonth()+1)}-${pad(d.getDate())}-${d.getFullYear()} ${pad(d.getHours())}:${pad(d.getMinutes())}:${pad(d.getSeconds())}`;}
  async function health(){try{const r=await fetch('/health',{cache:'no-store',signal:AbortSignal.timeout(8000)});document.querySelector('#connection').textContent=r.ok?'Your server is available.':'Your server is starting.';}catch{document.querySelector('#connection').textContent='Connecting to your server.';}}
  for(const input of [login,password]){input.placeholder=' ';const resize=()=>{if(input===password)document.querySelector('#password-mask').textContent='*'.repeat(password.value.length);input.style.width=`${Math.max(1,input.value.length+1)}ch`;};for(const event of ['input','change','focus'])input.addEventListener(event,resize);resize();setTimeout(resize,250);}
  function enterPassword(){if(!login.value.trim())return;step='password';login.readOnly=true;login.tabIndex=-1;loginLine.classList.add('complete');passwordLine.hidden=false;feedback.textContent='';password.focus();}
  function resetLogin(){step='login';password.value='';document.querySelector('#password-mask').textContent='';passwordLine.hidden=true;login.readOnly=false;login.value='';login.style.width='1ch';login.tabIndex=0;loginLine.classList.remove('complete');feedback.textContent='';login.focus();}
  async function signIn(){
    if(!password.value){resetLogin();return;}
    pending=true;password.readOnly=true;feedback.textContent='Authenticating...';
    try{
      const r=await fetch('/api/v1/auths/signin',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({email:login.value.trim(),password:password.value}),signal:AbortSignal.timeout(30000)});
      const data=await r.json().catch(()=>null);
      if(!r.ok||!data?.token){resetLogin();return;}
      localStorage.setItem('fh-last-activity',String(Date.now()));
      localStorage.setItem('token',data.token);
      sessionStorage.setItem('fh-start-after-login','1');
      feedback.textContent='Access granted.';
      window.location.replace('/');
    }catch{resetLogin();}
    finally{password.value='';password.style.width='1ch';pending=false;password.readOnly=false;document.querySelector('#password-mask').textContent='';if(step==='password')password.focus();else login.focus();}
  }
  // Keep the terminal keyboard-only without intercepting `beforeinput`.
  // Safari can report ordinary keyboard/IME input as insertReplacementText,
  // which made the login field appear completely broken.
  for(const event of ['paste','drop'])form.addEventListener(event,e=>e.preventDefault());
  form.addEventListener('submit',event=>event.preventDefault());
  form.addEventListener('keydown',event=>{if(event.key==='Escape'){event.preventDefault();resetLogin();}if(event.key==='Enter'&&!event.isComposing){event.preventDefault();if(!pending){if(step==='login')enterPassword();else signIn();}}});
  tick();setInterval(tick,1000);health();setInterval(health,20000);login.focus();
})();
