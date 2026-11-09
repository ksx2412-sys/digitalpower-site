#!/usr/bin/env python3
"""SEO podstron digitalpower.art (9.11.2026).

Uruchamiać PO każdym wygenerowaniu podstron (zbuduj.py), bo generator kopiuje index.html
do każdej podstrony. Skrypt jest bezpieczny do wielokrotnego uruchamiania.

Co robi (wygląd i działanie strony bez zmian):
 1. Na każdej podstronie usługi nagłówek jej sekcji staje się <h1> (zamiast <h2>),
    a w CSS dopisane są te same style dla h1 – wygląda identycznie.
 2. Dodaje dane strukturalne JSON-LD (Service) z tytułem i opisem podstrony.
 3. Usuwa z sitemap.xml strony prawne z noindex (Impressum, Datenschutz, KI-Hinweis).
"""
import json, re, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
TR = json.loads(re.search(r'window\.__TR=(\{.*?\});', (ROOT / 'trasy.js').read_text('utf-8')).group(1))
NAGLOWEK = {'angebot': 'oferta-tytul', 'druk-3d': 'druk-tytul', 'drony': 'drony-tytul',
            'marketing': 'mk-tytul', 'kontakt': 'kontakt-tytul'}
SELEKTORY = ['.oferta-glowa h2', '#drony .kino h2', '.kino h2', '.druk h2', '.mk-glowa h2',
             '.kontakt h2', '.onas h2', '#kontakt h2']
ZNACZNIK = 'data-seo="podstrona"'


def popraw(plik: pathlib.Path, klucz: str):
    h = plik.read_text('utf-8')
    hid = NAGLOWEK[klucz]
    # 1) h2 -> h1 w sekcji tej podstrony
    h = re.sub(r'<h2 id="%s"([^>]*)>(.*?)</h2>' % hid, r'<h1 id="%s"\1>\2</h1>' % hid, h, count=1, flags=re.S)
    # 2) te same style dla h1 (tylko raz)
    if '/*seo-h1*/' not in h:
        def regula(m):
            czesci = m.group(1).split(',')
            dodaj = [c.strip()[:-2] + 'h1' for c in czesci if c.strip() in SELEKTORY]
            return ','.join(czesci + dodaj) + '{' if dodaj else m.group(0)

        def css(m):
            s = re.sub(r'([^{}]+)\{', regula, m.group(0))
            return s.replace('</style>', '/*seo-h1*/</style>', 1)
        h = re.sub(r'<style[^>]*>.*?</style>', css, h, count=1, flags=re.S)
    # 3) JSON-LD Service
    if ZNACZNIK not in h:
        tytul = re.search(r'<title>(.*?)</title>', h).group(1).replace('&amp;', '&')
        opis = re.search(r'<meta name="description" content="([^"]*)"', h).group(1).replace('&amp;', '&')
        url = re.search(r'<link rel="canonical" href="([^"]+)"', h).group(1)
        lang = re.search(r'<html lang="(\w+)"', h).group(1)
        dane = {'@context': 'https://schema.org', '@type': 'Service' if klucz != 'kontakt' else 'ContactPage',
                'name': tytul, 'description': opis, 'url': url, 'inLanguage': lang}
        firma = {'@type': 'Organization', 'name': 'Digital 3D Power', 'url': 'https://digitalpower.art/'}
        if klucz == 'kontakt':
            dane['about'] = firma
        else:
            dane['provider'] = firma
            dane['areaServed'] = {'@type': 'City', 'name': 'Dortmund'}
        blok = '<script type="application/ld+json" %s>%s</script>' % (ZNACZNIK, json.dumps(dane, ensure_ascii=False))
        h = re.sub(r'(<link rel="canonical" href="[^"]+">)', lambda m: m.group(1) + blok, h, count=1)
    plik.write_text(h, 'utf-8')


for jezyk, trasy in TR.items():
    for klucz, sciezka in trasy.items():
        if klucz == 'start':
            continue
        popraw(ROOT / sciezka.strip('/') / 'index.html', klucz)
        print('ok', sciezka)

sm = ROOT / 'sitemap.xml'
t = sm.read_text('utf-8')
t2 = re.sub(r'\s*<url><loc>https://digitalpower\.art/(impressum|datenschutz|ki-hinweis)\.html</loc>.*?</url>', '', t)
sm.write_text(t2, 'utf-8')
print('sitemap: usunięto', t.count('<url>') - t2.count('<url>'), 'stron prawnych')
