#!/usr/bin/env python3
"""Erzeugt wix/embed.html aus index.html: ohne Manifest, Icons und Service Worker,
die in einer eingebetteten Seite ohnehin nicht funktionieren. Aufruf: python3 tools/build-wix-embed.py"""
import re, pathlib
root = pathlib.Path(__file__).resolve().parent.parent
t = (root / "index.html").read_text(encoding="utf-8")
t = re.sub(r'<link rel="(manifest|icon|apple-touch-icon)"[^>]*>\n', "", t)
t = re.sub(r'<meta name="(apple-mobile-web-app-[a-z-]+|mobile-web-app-capable)"[^>]*>\n', "", t)
t = re.sub(r'<script>\nif \("serviceWorker".*?</script>\n', "", t, flags=re.S)
import base64
font = base64.b64encode((root / "fonts" / "baloo2-latin.woff2").read_bytes()).decode()
t = t.replace("url(fonts/baloo2-latin.woff2)", "url(data:font/woff2;base64," + font + ")")
for name in ("logo-kopf", "logo"):
    data = base64.b64encode((root / "img" / (name + ".png")).read_bytes()).decode()
    t = t.replace('src="img/' + name + '.png"', 'src="data:image/png;base64,' + data + '"')
assert "img/logo" not in t
assert "serviceWorker" not in t and "manifest" not in t
(root / "wix").mkdir(exist_ok=True)
(root / "wix" / "embed.html").write_text(t, encoding="utf-8")
print("wix/embed.html geschrieben,", len(t), "Zeichen")
