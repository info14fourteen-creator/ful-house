/* Set the interface language before the upstream SPA initializes on any device. */
(() => {
  document.documentElement.lang='en-US';
  try { localStorage.setItem('locale','en-US'); } catch {}
})();
