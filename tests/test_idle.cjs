const test = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs'), vm = require('node:vm'), path = require('node:path');
const sandbox = {module:{exports:{}}};
vm.runInNewContext(fs.readFileSync(path.join(__dirname,'../pages/static/idle.js'),'utf8'),sandbox);
const create = sandbox.module.exports;
function setup(auth=true) {
  let time=100000, interval;
  const values=new Map(auth?[['token','test-token']]:[]), listeners={}, docListeners={}, calls=[], urls=[];
  const screen={hidden:true,setAttribute(){},querySelector(){return canvas;}};
  const canvas={getContext(){return null;}};
  const win={
    Date:{now:()=>time},localStorage:{getItem:k=>values.get(k)||null,setItem:(k,v)=>values.set(k,v),removeItem:k=>values.delete(k)},
    sessionStorage:{removeItem(){}},document:{hidden:false,body:{append(){}},createElement:()=>screen,addEventListener:(k,f)=>docListeners[k]=f},
    innerWidth:100,innerHeight:100,matchMedia:()=>({matches:false}),requestAnimationFrame:()=>1,cancelAnimationFrame(){},
    fetch:async(...args)=>{calls.push(args);return {ok:true};},AbortSignal:{timeout:()=>null},location:{replace:url=>urls.push(url)},
    addEventListener:(k,f)=>listeners[k]=f,setInterval:f=>interval=f
  };
  create(win);
  return {win,screen,values,calls,urls,advance:ms=>{time+=ms;},tick:()=>interval(),event:(type,extra={})=>{
    const e={type,isTrusted:true,preventDefault(){this.prevented=true;},stopImmediatePropagation(){this.stopped=true;},...extra};listeners[type](e);return e;
  },visibility:()=>docListeners.visibilitychange()};
}
test('one minute starts saver without stopping background work',()=>{
 const x=setup();x.advance(59999);x.tick();assert.equal(x.screen.hidden,true);
 x.advance(1);x.tick();assert.equal(x.screen.hidden,false);assert.equal(x.calls.length,0);assert.equal(x.values.get('token'),'test-token');
});
test('mouse wake requires no authentication and restarts minute',()=>{
 const x=setup();x.advance(60000);x.tick();x.event('pointermove');assert.equal(x.screen.hidden,true);
 x.advance(59999);x.tick();assert.equal(x.screen.hidden,true);x.advance(1);x.tick();assert.equal(x.screen.hidden,false);assert.equal(x.calls.length,0);
});
test('wake keystroke cannot submit underlying form',()=>{
 const x=setup(false);x.advance(60000);x.tick();const e=x.event('keydown');assert.equal(e.prevented,true);assert.equal(e.stopped,true);assert.equal(x.screen.hidden,true);
});
test('touch wake cannot click through overlay',()=>{
 const x=setup(false);x.advance(60000);x.tick();assert.equal(x.event('touchstart').prevented,true);assert.equal(x.event('click').prevented,true);
});
test('20-minute boundary revokes session once and redirects',async()=>{
 const x=setup();x.advance(1199999);x.tick();assert.equal(x.calls.length,0);x.advance(1);x.tick();x.tick();
 await new Promise(setImmediate);
 assert.equal(x.values.has('token'),false);assert.equal(x.calls.length,1);assert.equal(x.calls[0][0],'/api/v1/auths/signout');assert.deepEqual(x.urls,['/auth']);
});
test('first input after laptop sleep cannot resurrect expired session',async()=>{
 const x=setup();x.advance(1200000);const e=x.event('pointermove');await new Promise(setImmediate);
 assert.equal(e.prevented,true);assert.deepEqual(x.urls,['/auth']);
});
test('anonymous page gets saver but not repeated logout',()=>{
 const x=setup(false);x.advance(1200000);x.tick();assert.equal(x.screen.hidden,false);assert.equal(x.calls.length,0);assert.equal(x.urls.length,0);
});
test('activity in another tab wakes saver and postpones logout',()=>{
 const x=setup();x.advance(60000);x.tick();x.values.set('fh-last-activity','160000');x.event('storage',{key:'fh-last-activity'});
 assert.equal(x.screen.hidden,true);x.advance(1199999);x.tick();assert.equal(x.calls.length,0);
});
test('synthetic/background events do not count as human activity',()=>{
 const x=setup();x.advance(60000);x.event('pointermove',{isTrusted:false});x.tick();assert.equal(x.screen.hidden,false);
});
test('logout in another tab redirects this tab',()=>{
 const x=setup();x.values.delete('token');x.event('storage',{key:'token'});assert.deepEqual(x.urls,['/auth']);
});
test('offline timeout clears local login and leaves private page',async()=>{
 const x=setup();x.win.fetch=async()=>{throw Error('offline');};x.advance(1200000);x.tick();await new Promise(setImmediate);
 assert.equal(x.values.has('token'),false);assert.deepEqual(x.urls,['/auth']);
});
