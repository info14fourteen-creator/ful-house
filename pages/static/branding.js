/* Apply the supplied artwork to upstream SPA branding, never chat attachments. */
(() => {
  const logo='/matrix-symbol-logo.svg?v=brand-1';
  function brand() {
    document.querySelectorAll('img').forEach(img => {
      const src=img.getAttribute('src') || '';
      if (/^\/(?:static\/(?:favicon[^/]*|logo\.png|splash(?:-dark)?\.png)|api\/v1\/models\/model\/profile\/image)(?:\?|$)/.test(src)) {
        img.src=logo;img.dataset.fhBrand='true';
        if (!img.alt || img.alt==='profile') img.alt='ful.house';
      }
    });
    document.querySelectorAll('link[rel*="icon"],link[rel="manifest"]').forEach(link => {
      const target=link.rel==='apple-touch-icon'?'/apple-touch-icon.png?v=brand-1':link.rel==='manifest'?'/manifest.json?v=brand-1':'/favicon.svg?v=brand-1';
      if(link.getAttribute('href')!==target)link.setAttribute('href',target);
      if(link.rel.includes('icon')&&link.rel!=='apple-touch-icon') {link.setAttribute('type','image/svg+xml');link.removeAttribute('sizes');}
    });
  }
  let scheduled=false;
  new MutationObserver(()=>{if(!scheduled){scheduled=true;requestAnimationFrame(()=>{scheduled=false;brand();});}}).observe(document.documentElement,{childList:true,subtree:true});
  brand();
})();
