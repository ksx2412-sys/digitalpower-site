#!/usr/bin/env python3
"""Link do sklepu Etsy (15.11.2026) – ikona obok Instagram/TikTok/Facebook + dane dla Google (sameAs).

Uruchamiany automatycznie przez seo_podstrony.py. Bezpieczny do wielokrotnego uruchamiania.
"""
import json, re, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
ETSY = 'https://www.etsy.com/shop/DigitalPowerArt3D'
FB = '"https://www.facebook.com/profile.php?id=61590071507349"'
IKONA = ('<a href="%s" target="_blank" rel="noopener noreferrer" aria-label="Etsy-Shop" style="background:#f1641e">'
         '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
         '<path d="M6 2 3 6v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6l-3-4z"/><path d="M3 6h18"/><path d="M16 10a4 4 0 0 1-8 0"/></svg></a>') % ETSY


def uruchom():
    tr = json.loads(re.search(r'window\.__TR=(\{.*?\});', (ROOT / 'trasy.js').read_text('utf-8')).group(1))
    pliki = sorted({ROOT / s.strip('/') / 'index.html' for t in tr.values() for s in t.values()})
    for plik in pliki:
        h = plik.read_text('utf-8')
        if ETSY not in h:
            # ikona po Facebooku w obu paskach social (kontakt i stopka)
            h = re.sub(r'(<nav class="social[^>]*>.*?aria-label="Facebook">.*?</a>)(</nav>)', lambda m: m.group(1) + '\n    ' + IKONA + m.group(2), h, flags=re.S)
            # dane strukturalne firmy
            h = h.replace(FB + ']', FB + ', "%s"]' % ETSY, 1)
            plik.write_text(h, 'utf-8')
        print('etsy ok', plik.relative_to(ROOT), h.count(ETSY))


if __name__ == '__main__':
    uruchom()
