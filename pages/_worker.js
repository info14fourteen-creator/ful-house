export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    const brand = {
      '/favicon.ico':'/favicon.ico','/static/favicon.ico':'/favicon.ico',
      '/favicon.svg':'/favicon.svg','/static/favicon.svg':'/favicon.svg',
      '/favicon.png':'/favicon-32x32.png','/favicon-32x32.png':'/favicon-32x32.png',
      '/static/favicon.png':'/favicon-32x32.png','/static/favicon-96x96.png':'/favicon-32x32.png','/static/fulhouse-icon.png':'/favicon-32x32.png',
      '/apple-touch-icon.png':'/apple-touch-icon.png','/static/apple-touch-icon.png':'/apple-touch-icon.png',
      '/matrix-symbol-logo.svg':'/matrix-symbol-logo.svg','/matrix-symbol-logo.png':'/matrix-symbol-logo.png',
      '/static/logo.png':'/matrix-symbol-logo.png','/static/splash.png':'/matrix-symbol-logo.png','/static/splash-dark.png':'/matrix-symbol-logo.png',
      '/manifest.json':'/manifest.json'
    };
    if (brand[url.pathname]) {
      const asset=await env.ASSETS.fetch(new URL(brand[url.pathname],url));
      const response=new Response(asset.body,asset);response.headers.set('Cache-Control','no-cache');return response;
    }
    if (['/static/homebrew.css','/static/matrix.js','/static/terminal-login.css','/static/terminal-login.js','/static/idle.js','/static/idle.css','/static/branding.js'].includes(url.pathname)) {
      const asset=await env.ASSETS.fetch(request);
      const response=new Response(asset.body,asset);
      response.headers.set('Cache-Control','no-cache');
      return response;
    }
    if (request.method==='GET' && url.pathname==='/auth') {
      const asset=await env.ASSETS.fetch(new URL('/login.html',url));
      const response=new Response(asset.body,asset);
      response.headers.set('Cache-Control','no-store');
      response.headers.set('X-Content-Type-Options','nosniff');
      response.headers.set('X-Frame-Options','DENY');
      response.headers.set('Referrer-Policy','same-origin');
      return response;
    }
    // Never publish source archives, configuration, or local environment files.
    if (/^\/(archive(?:\/|$)|\.env(?:\.|$)|\.git(?:\/|$))/.test(url.pathname)) {
      return new Response('Not found', {status:404});
    }
    if (!env.ORIGIN_URL || !env.FULHOUSE_ORIGIN_SECRET) {
      return new Response('Сервис готовится к запуску.', {status:503,headers:{'content-type':'text/plain; charset=utf-8','cache-control':'no-store'}});
    }
    const target = new URL(env.ORIGIN_URL);
    if (target.protocol !== 'https:') return new Response('Configuration error', {status:503});
    target.pathname=url.pathname;target.search=url.search;
    const headers=new Headers(request.headers);
    headers.set('X-Fulhouse-Origin',env.FULHOUSE_ORIGIN_SECRET);
    headers.delete('Host');
    // Do not trust client-supplied upstream identity headers.
    for (const name of ['x-openwebui-user-email','x-openwebui-user-name','x-openwebui-user-role','x-forwarded-user']) headers.delete(name);
    const navigation=request.method==='GET' && ['/', '/auth'].includes(url.pathname);
    let upstream;
    try {
      upstream=await fetch(target,new Request(request,{headers,redirect:'manual',...(navigation?{signal:AbortSignal.timeout(5000)}:{})}));
    } catch {
      upstream=new Response('Origin temporarily unavailable',{status:503});
    }
    if (upstream.status===101) return upstream;
    if ([502,503,504].includes(upstream.status) && request.method==='GET' && ['/', '/auth'].includes(url.pathname)) {
      const fallback=await env.ASSETS.fetch(new URL('/boot.html',url));
      const boot=new Response(fallback.body,{status:503,headers:fallback.headers});
      boot.headers.set('Cache-Control','no-store');
      boot.headers.set('Retry-After','10');
      return boot;
    }
    const response=new Response(upstream.body,upstream);
    response.headers.set('Cache-Control','no-store');
    response.headers.set('X-Content-Type-Options','nosniff');
    response.headers.set('Referrer-Policy','same-origin');
    response.headers.set('X-Frame-Options','DENY');
    response.headers.set('X-Robots-Tag','noindex, nofollow');
    if ((response.headers.get('content-type') || '').includes('text/html')) {
      return new HTMLRewriter()
        .on('head', {element(e){e.append('<script defer src="/static/branding.js?v=brand-1"></script><link rel="stylesheet" href="/static/idle.css?v=idle-3"><script defer src="/static/idle.js?v=idle-3"></script>',{html:true});}})
        .on('link[href="/static/homebrew.css"]', {element(e){e.setAttribute('href','/static/homebrew.css?v=brand-1');}})
        .on('script[src="/static/matrix.js"]', {element(e){e.setAttribute('src','/static/matrix.js?v=brand-1');}})
        .transform(response);
    }
    return response;
  }
};
