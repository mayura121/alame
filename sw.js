const CACHE = 'mezamashi-v4';
const ASSETS = [
  '/', '/index.html', '/manifest.json', '/icon-192.svg', '/icon-512.svg',
  '/tea/', '/tea/golden-rule.html',
  '/tea/darjeeling.html', '/tea/milk-tea.html', '/tea/iced-tea.html',
  '/tea/tea-leaves-type.html', '/tea/teapot-choice.html', '/tea/afternoon-tea.html',
  '/tea/chai.html', '/tea/storage.html', '/tea/health.html', '/tea/food-pairing.html',
  '/coffee/', '/coffee/drip.html', '/coffee/camp-percolator.html',
  '/coffee/camp-drip.html', '/coffee/moka-pot.html', '/coffee/french-press.html',
  '/coffee/coffee-maker.html', '/coffee/beans.html', '/coffee/roast.html',
  '/coffee/cold-brew.html', '/coffee/latte.html'
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
  e.respondWith(
    caches.match(e.request).then(cached => cached || fetch(e.request))
  );
});
