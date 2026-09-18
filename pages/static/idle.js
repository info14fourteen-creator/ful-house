/* Human inactivity only: inference and network traffic never reset these clocks. */
(function (root, create) {
  if (typeof module === 'object' && module.exports) module.exports = create;
  else create(root);
})(typeof window === 'undefined' ? null : window, function (win) {
  'use strict';
  const doc = win.document, storage = win.localStorage;
  const ACTIVITY = 'fh-last-activity', SCREEN_MS = 60_000, LOGOUT_MS = 20 * 60_000;
  const now = () => win.Date.now();
  let last = Number(storage.getItem(ACTIVITY)) || now();
  if (last > now()) last = now();
  let authenticated = !!storage.getItem('token'), exiting = false, frame = 0;
  let lastWrite = 0, swallowClickUntil = 0;
  if (!authenticated) {
    last = Number(win.sessionStorage.getItem('fh-anon-last-activity')) || now();
    win.sessionStorage.setItem('fh-anon-last-activity', String(last));
  }
  storage.setItem(ACTIVITY, String(last));
  const screen = doc.createElement('div');
  screen.id = 'fh-screensaver'; screen.hidden = true;
  screen.setAttribute('role', 'img'); screen.setAttribute('aria-label', 'Matrix screensaver');
  screen.innerHTML = '<canvas aria-hidden="true"></canvas>';
  doc.body.append(screen);
  const canvas = screen.querySelector('canvas'), ctx = canvas.getContext('2d');
  let drops = [], previousFrame = 0;
  function resize() {
    canvas.width = win.innerWidth; canvas.height = win.innerHeight;
    drops = Array.from({length: Math.ceil(canvas.width / 18)}, () => -Math.random() * 55);
  }
  function draw(time) {
    if (screen.hidden || doc.hidden || !ctx) return;
    frame = win.requestAnimationFrame(draw);
    if (time - previousFrame < 55) return;
    previousFrame = time;
    ctx.fillStyle = 'rgba(0,0,0,.075)'; ctx.fillRect(0, 0, canvas.width, canvas.height);
    ctx.font = '15px monospace'; ctx.fillStyle = '#38fe27';
    const glyphs = '01アイウエオカキクケコサシスセソ';
    drops.forEach((y, i) => {
      ctx.fillText(glyphs[Math.floor(Math.random() * glyphs.length)], i * 18, y * 18);
      drops[i] = y * 18 > canvas.height && Math.random() > .98 ? -5 : y + 1;
    });
  }
  function show() {
    if (!screen.hidden) return;
    screen.hidden = false; resize();
    if (!win.matchMedia('(prefers-reduced-motion: reduce)').matches) frame = win.requestAnimationFrame(draw);
  }
  function hide() {
    if (exiting) return;
    screen.hidden = true; win.cancelAnimationFrame(frame);
  }
  async function logout() {
    if (exiting) return;
    exiting = true; show();
    const token = storage.getItem('token');
    storage.removeItem('token');
    win.sessionStorage.removeItem('fh-start-after-login');
    win.sessionStorage.removeItem('fh-anon-last-activity');
    // Revoke upstream session and clear its HttpOnly cookie as well as local auth.
    try {
      await win.fetch('/api/v1/auths/signout', {
        method: 'POST', credentials: 'same-origin', keepalive: true,
        headers: token ? {Authorization: 'Bearer ' + token} : {},
        signal: win.AbortSignal.timeout(5000)
      });
    } catch { /* A disconnected browser still leaves the authenticated screen. */ }
    win.location.replace('/auth');
  }
  function tick() {
    if (exiting) return;
    if (storage.getItem('token')) authenticated = true;
    const shared = Number(storage.getItem(ACTIVITY));
    if (shared > last && shared <= now()) last = shared;
    if (authenticated && !storage.getItem('token')) { exiting = true; win.location.replace('/auth'); return; }
    const elapsed = now() - last;
    if (authenticated && elapsed >= LOGOUT_MS) { void logout(); return; }
    if (elapsed >= SCREEN_MS) show();
  }
  function activity(event) {
    if (!event.isTrusted) return;
    if (exiting) { event.preventDefault(); event.stopImmediatePropagation(); return; }
    // Check expiry BEFORE handling wake input (including after laptop sleep).
    tick();
    if (exiting) { event.preventDefault(); event.stopImmediatePropagation(); return; }
    const wasVisible = !screen.hidden;
    if (wasVisible && event.type !== 'pointermove' && event.type !== 'mousemove') {
      event.preventDefault(); event.stopImmediatePropagation(); swallowClickUntil = now() + 500;
    }
    last = now();
    if (!authenticated) win.sessionStorage.setItem('fh-anon-last-activity', String(last));
    if (wasVisible || last - lastWrite >= 500) { storage.setItem(ACTIVITY, String(last)); lastWrite = last; }
    hide();
  }
  for (const type of ['pointermove', 'mousemove', 'pointerdown', 'touchstart', 'keydown', 'wheel']) {
    win.addEventListener(type, activity, {capture: true, passive: false});
  }
  win.addEventListener('click', event => {
    if (now() < swallowClickUntil || exiting) { event.preventDefault(); event.stopImmediatePropagation(); }
  }, true);
  win.addEventListener('storage', event => {
    if (event.key === 'token') {
      if (authenticated && !storage.getItem('token')) { exiting = true; win.location.replace('/auth'); return; }
      authenticated = !!storage.getItem('token');
    }
    if (event.key === ACTIVITY) { last = Number(storage.getItem(ACTIVITY)) || last; hide(); }
    tick();
  });
  doc.addEventListener('visibilitychange', () => {
    win.cancelAnimationFrame(frame); tick();
    if (!doc.hidden && !screen.hidden && !win.matchMedia('(prefers-reduced-motion: reduce)').matches) frame = win.requestAnimationFrame(draw);
  });
  win.addEventListener('pageshow', tick);
  win.addEventListener('resize', () => { if (!screen.hidden) resize(); });
  win.setInterval(tick, 1000);
  tick();
});
