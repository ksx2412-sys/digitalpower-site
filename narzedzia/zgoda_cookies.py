#!/usr/bin/env python3
"""Baner zgody + Piksel Meta + tag Google (15.11.2026).

Dopina /zgoda.js do każdej podstrony i poszerza politykę bezpieczeństwa strony (CSP) o adresy Meta i Google.
Identyfikatory wpisuje się na górze pliku zgoda.js. Uruchamiany automatycznie przez seo_podstrony.py.
"""
import json, re, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
TAG = '<script src="/zgoda.js?v=20261115c" defer></script>'
DODAJ = {
    'script-src': 'https://connect.facebook.net https://www.googletagmanager.com',
    'img-src': 'https://www.facebook.com https://www.googletagmanager.com https://*.google-analytics.com https://www.google.com https://www.google.de https://googleads.g.doubleclick.net',
    'connect-src': 'https://www.facebook.com https://connect.facebook.net https://www.googletagmanager.com https://*.google-analytics.com https://*.analytics.google.com https://www.google.com https://googleads.g.doubleclick.net https://pagead2.googlesyndication.com',
    'frame-src': 'https://td.doubleclick.net https://www.googletagmanager.com',
}


def csp(m):
    czesci = [c.strip() for c in m.group(2).split(';') if c.strip()]
    wynik = []
    for c in czesci:
        nazwa, _, reszta = c.partition(' ')
        if nazwa in DODAJ:
            wart = [x for x in reszta.split() if x != "'none'"]
            for x in DODAJ[nazwa].split():
                if x not in wart:
                    wart.append(x)
            c = nazwa + ' ' + ' '.join(wart)
        wynik.append(c)
    return m.group(1) + '; '.join(wynik) + m.group(3)


def uruchom():
    tr = json.loads(re.search(r'window\.__TR=(\{.*?\});', (ROOT / 'trasy.js').read_text('utf-8')).group(1))
    pliki = sorted({ROOT / s.strip('/') / 'index.html' for t in tr.values() for s in t.values()})
    for plik in pliki:
        h = plik.read_text('utf-8')
        h = re.sub(r'(<meta http-equiv="Content-Security-Policy" content=")([^"]*)(")', csp, h, count=1)
        h = re.sub(r'<script src="/zgoda\.js[^>]*></script>\n?', '', h)
        h = h.replace('<script src="/poprawki.js', TAG + '\n<script src="/poprawki.js', 1)
        plik.write_text(h, 'utf-8')
    print('zgoda cookies ok', len(pliki))


if __name__ == '__main__':
    uruchom()
