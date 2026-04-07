self.addEventListener('install', function(e) {
    e.waitUntil(
        caches.open('projectsite-cache-v1').then(function(cache) {
            return cache.addAll([
                '/',
                '/static/css/sb-admin-2.min.css',
                '/static/js/sb-admin-2.js',
            ]);
        })
    );
});

self.addEventListener('fetch', function(e) {
    e.respondWidth (
        caches.match(e.request).then(function(response) {
            return response || fetch(e.request);
        })
    );
});