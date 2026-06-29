const CACHE = 'voicebridge-v1';
const ASSETS = [
  '/translate/',
  '/translate/index.html',
  '/translate/manifest.json',
  '/translate/icon-192.svg',
  '/translate/icon-512.svg'
];

self.addEventListener('install', e => {
  e.waitUntil(caches.open(CACHE).then(c => c.addAll(ASSETS)));
  self.skipWaiting();
});

self.addEventListener('activate', e => {
  e.waitUntil(caches.keys().then(keys =>
    Promise.all(keys.filter(k => k !== CACHE).map(k => caches.delete(k)))
  ));
  self.clients.claim();
});

self.addEventListener('fetch', e => {
  const url = new URL(e.request.url);
  // never cache translation API calls – always go to network
  if (url.hostname.includes('mymemory') || e.request.method !== 'GET') return;
  e.respondWith(caches.match(e.request).then(cached => cached || fetch(e.request)));
});
