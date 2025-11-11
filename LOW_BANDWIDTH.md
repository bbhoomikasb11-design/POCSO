# Low Bandwidth Optimizations (Applied)

## Enabled
- HTTP compression and cache-friendly static serving via WhiteNoise
- Long-lived static file caching (hashed filenames) using `CompressedManifestStaticFilesStorage`
- DRF pagination disabled by default (no heavy payloads by default)
- JSON endpoints scoped and minimal
- Image lazy-loading present in multiple pages (kept)

## Suggestions (Optional)
- Convert heavy images to WebP and reduce dimensions
- Inline critical CSS for landing above-the-fold (optional)
- Defer non-critical scripts and use `rel=preload` where meaningful
- Add a service worker for offline caching (optional enhancement)


