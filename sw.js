/* Money Tracker – offline engine. Keeps the app available without internet.
   It never stores your money data (that lives in the app's own storage on your device). */
const CACHE = 'trackme-v1';
const SHELL = ['./', './index.html', './manifest.webmanifest', './icon-192.png', './icon-512.png'];

self.addEventListener('install', e => { e.waitUntil(caches.open(CACHE).then(c => c.addAll(SHELL)).then(() => self.skipWaiting())); });
self.addEventListener('activate', e => {
  e.waitUntil(caches.keys().then(keys => Promise.all(keys.filter(k => k !== CACHE).map(k => caches.delete(k)))).then(() => self.clients.claim()));
});
self.addEventListener('fetch', e => {
  const r = e.request; if(r.method !== 'GET' || r.headers.get('range')) return;
  const u = new URL(r.url);
  if(r.mode === 'navigate'){   // pages: newest copy when online, saved copy when offline
    e.respondWith(fetch(r).then(res => { const cp = res.clone(); caches.open(CACHE).then(c => c.put('./index.html', cp)); return res; }).catch(() => caches.match('./index.html', { ignoreSearch:true })));
    return;
  }
  if(u.origin === location.origin || /(^|\.)(fonts\.googleapis\.com|fonts\.gstatic\.com)$/.test(u.hostname)){
    e.respondWith(caches.match(r).then(hit => {
      const net = fetch(r).then(res => { if(res.ok || res.type === 'opaque'){ const cp = res.clone(); caches.open(CACHE).then(c => c.put(r, cp)); } return res; }).catch(() => hit);
      return hit || net;
    }));
  }
});
