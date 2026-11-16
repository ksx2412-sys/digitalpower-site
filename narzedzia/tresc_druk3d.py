#!/usr/bin/env python3
"""Własna treść podstrony druku 3D (15.11.2026) – pod zapytania z całych Niemiec.

Uruchamiany automatycznie przez seo_podstrony.py (po każdym zbuduj.py). Bezpieczny do
wielokrotnego uruchamiania. Co robi:
 1. Na podstronach druku 3D (DE i PL) dokleja na końcu sekcji blok z własną treścią
    (co drukujemy, wysyłka, pytania i odpowiedzi) w stylu strony + dane FAQPage.
 2. Niemiecki tytuł i opis podstrony: nacisk na zamówienie online i wysyłkę w całych Niemczech
    (w pliku podstrony i w trasy.js, żeby tytuł nie wracał po kliknięciu w menu).
"""
import json, re, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
ZN = 'data-seo-blok'

STARY_T = '3D-Druck Service Dortmund – nach Datei, Foto oder Skizze'
NOWY_T = '3D-Druck Dortmund – Einzelstücke, Ersatzteile, Prototypen | Digital Power Art'
STARY_O = ('3D-Druck auf Bambu Lab P1S: Einzelstück, Ersatzteil, Prototyp oder Serie aus PLA, PETG, ASA oder TPU. '
           'Preisrechner online, Abholung in Dortmund oder Versand.')
NOWY_O = ('3D-Druck in Dortmund auf Bestellung: Einzelstück, Ersatzteil, Prototyp oder Serie aus '
          'PLA, PETG, ASA, TPU. Preisrechner online, Versand deutschlandweit.')

CSS = ('<style>.seo-blok{margin:clamp(56px,8vw,104px) 0 0;padding-top:clamp(40px,6vw,72px);border-top:1px solid var(--linia)}'
       '.seo-blok h2{font-family:var(--font-display);font-weight:700;font-size:clamp(26px,3.2vw,40px);line-height:1.1;margin:0 0 16px;text-wrap:balance}'
       '.seo-blok>p{color:var(--tekst-2);font-size:17px;max-width:46em;margin:0 0 40px}'
       '.seo-karty{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px;margin:0 0 48px}'
       '.seo-karty .material b{font-size:18px}.seo-karty .material span{font-size:14px}'
       '.seo-faq{max-width:52em;margin:0 0 40px}'
       '.seo-faq details{border:1px solid var(--linia);border-radius:14px;background:#0c1220;margin:0 0 10px;padding:0 18px}'
       '.seo-faq summary{cursor:pointer;padding:16px 0;font-weight:600;font-size:16px;color:var(--tekst)}'
       '.seo-faq details p{margin:0 0 16px;color:var(--tekst-2);font-size:15.5px;line-height:1.6}'
       'html:not([lang="de"]) .seo-blok[lang="de"],html:not([lang="pl"]) .seo-blok[lang="pl"]{display:none}'
       '@media (max-width:980px){.seo-karty{grid-template-columns:repeat(2,minmax(0,1fr))}}'
       '.seo-blok .podtytul{color:var(--akc,var(--czerwien))}.seo-blok .seo-karty .material{border-left:3px solid var(--akc,var(--czerwien))}'
       '.seo-blok .btn-czerwony{background:var(--czerwien);color:#fff;box-shadow:0 10px 30px -8px #ff4b5caa}'
       '.seo-blok .btn-czerwony:hover{background:#ff6a78}'
       '@media (max-width:560px){.seo-karty{grid-template-columns:1fr}}</style>')

TRESC = {
 'de': {
  'plik': '3d-druck/index.html', 'kontakt': '/kontakt/',
  'h2': '3D-Druck Service online – Versand deutschlandweit',
  'p': 'Sie müssen nicht in Dortmund wohnen: Datei hochladen oder Foto schicken, Angebot erhalten – und wir senden '
       'das fertige Teil per Paket zu Ihnen. Deutschlandweit, auf Anfrage auch ins EU-Ausland. Gedruckt wird erst '
       'nach Ihrer Freigabe.',
  'kt': 'Was wir für Sie drucken',
  'karty': [
   ('Ersatzteile und Gebrauchsteile', 'Halterungen, Clips, Abdeckungen und Adapter aus PETG oder ASA – auch für draußen.'),
   ('Prototypen', 'Ein Stück zum Anfassen und Testen, bevor eine Serie entsteht.'),
   ('Kleinserien', 'Wir drucken zuerst ein Muster. Die Serie startet nach Ihrer Freigabe.'),
   ('Figuren und Deko', 'Eigene Sammelfiguren und Dekoration in bis zu 4 Farben in einem Druck.'),
   ('Personalisierte Geschenke', 'Schlüsselanhänger, Namensschilder und Organizer mit Namen.'),
   ('3D-Modell nach Foto oder Skizze', 'Kein Modell vorhanden? Wir entwerfen es nach Foto und Maßen.'),
  ],
  'ft': 'Häufige Fragen zum 3D-Druck',
  'faq': [
   ('Was kostet ein 3D-Druck?', 'Der Preis hängt von Material, Größe, Druckzeit und Stückzahl ab. Kleine Teile gibt es ab 5 €. '
    'Im Preisrechner auf dieser Seite sehen Sie sofort einen Richtpreis. Das verbindliche Angebot erhalten Sie vor dem Druck.'),
   ('Welche Dateien kann ich schicken?', '3MF (empfohlen) oder STL, bis 50 MB. Ohne 3D-Modell genügen Fotos und eine Skizze mit Maßen.'),
   ('Liefern Sie auch außerhalb von Dortmund?', 'Ja. Wir versenden deutschlandweit per Paket, auf Anfrage auch ins EU-Ausland. '
    'In Dortmund können Sie Ihr Teil persönlich abholen.'),
   ('Wie groß darf ein Teil sein?', 'Unsere Bambu Lab P1S druckt Teile bis 256 × 256 × 256 mm. Größere Modelle auf Anfrage.'),
   ('Welches Material ist das richtige?', 'PLA für Deko, Figuren und Prototypen. PETG für robuste Gebrauchsteile. ASA für Teile im Freien, '
    'weil es UV-beständig ist. TPU für flexible Teile. Wir beraten Sie bei der Auswahl.'),
   ('Drucken Sie auch mehrfarbig?', 'Ja, bis zu 4 Farben in einem Druck.'),
  ],
  'btn': 'Anfrage senden',
 },
 'pl': {
  'plik': 'pl/druk-3d/index.html', 'kontakt': '/pl/kontakt/',
  'h2': 'Druk 3D na zamówienie – wysyłka w całych Niemczech',
  'p': 'Nie musisz mieszkać w Dortmundzie: wyślij plik albo zdjęcie, dostaniesz wycenę, a gotowy wydruk wyślemy '
       'paczką. W całych Niemczech, na życzenie także do innych krajów UE. Drukujemy dopiero po Twojej akceptacji.',
  'kt': 'Co drukujemy',
  'karty': [
   ('Części zamienne i użytkowe', 'Uchwyty, klipsy, zaślepki i adaptery z PETG lub ASA – także na zewnątrz.'),
   ('Prototypy', 'Jedna sztuka do sprawdzenia, zanim powstanie seria.'),
   ('Małe serie', 'Najpierw drukujemy wzór. Seria rusza po Twojej akceptacji.'),
   ('Figurki i dekoracje', 'Własne figurki kolekcjonerskie i dekoracje, do 4 kolorów w jednym wydruku.'),
   ('Prezenty z imieniem', 'Breloki, tabliczki z imieniem i organizery z napisem.'),
   ('Model 3D ze zdjęcia lub szkicu', 'Nie masz modelu? Zaprojektujemy go według zdjęcia i wymiarów.'),
  ],
  'ft': 'Najczęstsze pytania o druk 3D',
  'faq': [
   ('Ile kosztuje druk 3D?', 'Cena zależy od materiału, wielkości, czasu druku i liczby sztuk. Małe elementy od 5 €. '
    'W kalkulatorze na tej stronie od razu zobaczysz cenę orientacyjną. Wiążącą wycenę dostajesz przed drukiem.'),
   ('Jakie pliki mogę wysłać?', '3MF (zalecany) lub STL, do 50 MB. Bez modelu 3D wystarczą zdjęcia i szkic z wymiarami.'),
   ('Czy wysyłacie poza Dortmund?', 'Tak. Wysyłamy paczką w całych Niemczech, na życzenie także do innych krajów UE. '
    'W Dortmundzie możliwy odbiór osobisty.'),
   ('Jak duży może być element?', 'Nasza Bambu Lab P1S drukuje elementy do 256 × 256 × 256 mm. Większe modele po uzgodnieniu.'),
   ('Jaki materiał wybrać?', 'PLA do dekoracji, figurek i prototypów. PETG do wytrzymałych części użytkowych. ASA na zewnątrz, '
    'bo jest odporny na UV. TPU do elementów elastycznych. Pomożemy w wyborze.'),
   ('Czy drukujecie w kilku kolorach?', 'Tak, do 4 kolorów w jednym wydruku.'),
  ],
  'btn': 'Wyślij zapytanie',
 },
}


def esc(s):
    return s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')


def blok(j, t):
    karty = ''.join('<div class="material"><b>%s</b><span>%s</span></div>' % (esc(a), esc(b)) for a, b in t['karty'])
    faq = ''.join('<details><summary>%s</summary><p>%s</p></details>' % (esc(a), esc(b)) for a, b in t['faq'])
    ld = {'@context': 'https://schema.org', '@type': 'FAQPage', 'inLanguage': j,
          'mainEntity': [{'@type': 'Question', 'name': a, 'acceptedAnswer': {'@type': 'Answer', 'text': b}} for a, b in t['faq']]}
    return ('<div class="seo-blok" %s lang="%s"@STYL@>@CSS@<h2>%s</h2><p>%s</p><h3 class="podtytul">%s</h3><div class="seo-karty">%s</div>'
            '<h3 class="podtytul">%s</h3><div class="seo-faq">%s</div><a class="@BTN@" href="%s">%s</a>'
            '<script type="application/ld+json">%s</script></div>'
            % (ZN, j, esc(t['h2']), esc(t['p']), esc(t['kt']), karty, esc(t['ft']), faq, t['kontakt'], esc(t['btn']),
               json.dumps(ld, ensure_ascii=False))).replace('@CSS@', CSS).replace('@BTN@', t.get('btn_klasa', 'btn btn-czerwony')).replace('@STYL@', ' style="%s"' % t['styl'] if t.get('styl') else '')


def uruchom():
    for j, t in TRESC.items():
        plik = ROOT / t['plik']
        h = plik.read_text('utf-8')
        if ZN not in h:
            i = h.index('<section class="druk" id="druk-3d"')
            k = h.index('</section>', i)
            h = h[:k] + blok(j, t) + h[k:]
        if j == 'de':
            h = h.replace(STARY_T, NOWY_T).replace(STARY_O, NOWY_O)
            h = h.replace('"url": "https://digitalpower.art/3d-druck/", "inLanguage": "de", "provider": {"@type": "Organization", '
                          '"name": "Digital 3D Power", "url": "https://digitalpower.art/"}, "areaServed": {"@type": "City", "name": "Dortmund"}',
                          '"url": "https://digitalpower.art/3d-druck/", "inLanguage": "de", "provider": {"@type": "Organization", '
                          '"name": "Digital 3D Power", "url": "https://digitalpower.art/"}, "areaServed": {"@type": "Country", "name": "Deutschland"}')
        plik.write_text(h, 'utf-8')
        print('treść druk 3D ok', t['plik'])
    tr = ROOT / 'trasy.js'
    s = tr.read_text('utf-8')
    tr.write_text(s.replace(STARY_T, NOWY_T).replace(STARY_O, NOWY_O), 'utf-8')


if __name__ == '__main__':
    uruchom()
