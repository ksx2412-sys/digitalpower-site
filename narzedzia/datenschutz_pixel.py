#!/usr/bin/env python3
"""Polityka prywatności: zgoda na cookies i Piksel Meta (15.11.2026), DE/PL/EN.

Poprawia podsumowanie (pkt 2) i dodaje nowy pkt 7; dalsze punkty przesuwa o jeden.
Uruchamiany automatycznie przez seo_podstrony.py. Bezpieczny do wielokrotnego uruchamiania.
"""
import re, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
ZN = 'data-pixel-info'
META = 'https://www.facebook.com/privacy/policy/'

J = {
 'de': {
  'stare': [('Wir setzen keine Analyse- oder Werbe-Tracker ein und keine Cookies, die eine Einwilligung erfordern.',
             'Werbemessung (Meta Pixel) laden wir nur, wenn Sie im Cookie-Banner zustimmen. Ohne Zustimmung wird nichts davon geladen.'),
            ('Die Website speichert nichts in Ihrem Browser (keine Cookies, kein Local Storage).',
             'Ohne Ihre Zustimmung speichert die Website nur Ihre Entscheidung aus dem Cookie-Banner in Ihrem Browser (Local Storage) und setzt keine Cookies.')],
  'h': 'Cookie-Einwilligung und Meta Pixel',
  'p': ['Beim ersten Besuch fragen wir, ob wir Cookies zur Werbemessung einsetzen dürfen. Ihre Entscheidung speichern wir im Local Storage Ihres Browsers (Eintrag „dp_zgoda_v1“), damit wir nicht bei jedem Besuch erneut fragen. Sie können Ihre Entscheidung jederzeit über den Link „Cookie-Einstellungen“ am Seitenende ändern oder widerrufen.',
        'Nur wenn Sie zustimmen, laden wir das Meta Pixel der Meta Platforms Ireland Limited, Merrion Road, Dublin 4, D04 X2K5, Irland. Das Pixel setzt Cookies und überträgt Nutzungsdaten an Meta, zum Beispiel aufgerufene Seiten, das Absenden einer Anfrage, die IP-Adresse und Angaben zu Browser und Gerät. Damit messen wir, ob unsere Anzeigen auf Facebook und Instagram zu Anfragen führen, und können Anzeigen Personen zeigen, die unsere Website besucht haben. Für die Erhebung und Übermittlung dieser Daten sind wir gemeinsam mit Meta verantwortlich (Art. 26 DSGVO). Dabei können Daten in die USA übertragen werden; Meta Platforms, Inc. ist nach dem EU-U.S. Data Privacy Framework zertifiziert (Art. 45 DSGVO). Rechtsgrundlage ist Ihre Einwilligung (Art. 6 Abs. 1 lit. a DSGVO, § 25 Abs. 1 TDDDG). Mehr dazu in der <a href="%s" target="_blank" rel="noopener noreferrer">Datenschutzrichtlinie von Meta</a>.' % META],
 },
 'pl': {
  'stare': [('Nie używamy narzędzi analitycznych ani reklamowych, ani plików cookie wymagających zgody.',
             'Pomiar reklam (Piksel Meta) ładujemy tylko wtedy, gdy wyrazisz zgodę w banerze cookies. Bez zgody nic takiego się nie ładuje.'),
            ('Strona nic nie zapisuje w Twojej przeglądarce (brak cookies, brak Local Storage).',
             'Bez Twojej zgody strona zapisuje w przeglądarce (Local Storage) tylko Twoją decyzję z banera cookies i nie ustawia plików cookie.')],
  'h': 'Zgoda na cookies i Piksel Meta',
  'p': ['Przy pierwszej wizycie pytamy, czy możemy używać plików cookie do pomiaru reklam. Twoją decyzję zapisujemy w Local Storage przeglądarki (wpis „dp_zgoda_v1”), żeby nie pytać przy każdej wizycie. Decyzję możesz w każdej chwili zmienić lub wycofać przez link „Ustawienia cookies” na dole strony.',
        'Tylko po Twojej zgodzie ładujemy Piksel Meta firmy Meta Platforms Ireland Limited, Merrion Road, Dublin 4, D04 X2K5, Irlandia. Piksel ustawia pliki cookie i przekazuje Mecie dane o korzystaniu ze strony, na przykład odwiedzone podstrony, wysłanie zapytania, adres IP oraz informacje o przeglądarce i urządzeniu. Dzięki temu mierzymy, czy nasze reklamy na Facebooku i Instagramie prowadzą do zapytań, i możemy wyświetlać reklamy osobom, które odwiedziły naszą stronę. Za zbieranie i przekazywanie tych danych odpowiadamy wspólnie z Metą (art. 26 RODO). Dane mogą być przy tym przekazywane do USA; Meta Platforms, Inc. posiada certyfikat EU-U.S. Data Privacy Framework (art. 45 RODO). Podstawą prawną jest Twoja zgoda (art. 6 ust. 1 lit. a RODO, § 25 ust. 1 TDDDG). Więcej w <a href="%s" target="_blank" rel="noopener noreferrer">polityce prywatności Meta</a>.' % META],
 },
 'en': {
  'stare': [('We use no analytics or advertising trackers and no cookies that require consent.',
             'We load ad measurement (Meta Pixel) only if you agree in the cookie banner. Without your consent none of it is loaded.'),
            ('The website stores nothing in your browser (no cookies, no local storage).',
             'Without your consent the website stores only your cookie-banner choice in your browser (local storage) and sets no cookies.')],
  'h': 'Cookie consent and Meta Pixel',
  'p': ['On your first visit we ask whether we may use cookies for ad measurement. We store your choice in your browser\'s local storage (entry “dp_zgoda_v1”) so that we do not ask on every visit. You can change or withdraw your choice at any time via the “Cookie settings” link at the bottom of the page.',
        'Only if you agree do we load the Meta Pixel of Meta Platforms Ireland Limited, Merrion Road, Dublin 4, D04 X2K5, Ireland. The pixel sets cookies and sends usage data to Meta, for example pages viewed, sending a request, the IP address and information about your browser and device. This lets us measure whether our ads on Facebook and Instagram lead to requests, and show ads to people who have visited our website. We are jointly responsible with Meta for collecting and transmitting this data (Art. 26 GDPR). Data may be transferred to the USA; Meta Platforms, Inc. is certified under the EU-U.S. Data Privacy Framework (Art. 45 GDPR). The legal basis is your consent (Art. 6(1)(a) GDPR, Section 25(1) TDDDG). More in <a href="%s" target="_blank" rel="noopener noreferrer">Meta\'s privacy policy</a>.' % META],
 },
}


def uruchom():
    plik = ROOT / 'datenschutz.html'
    h = plik.read_text('utf-8')
    if ZN in h:
        print('datenschutz pixel: już jest'); return
    for l, t in J.items():
        i = h.index('<div data-l="%s">' % l)
        k = h.find('<div data-l="', i + 10)
        if k < 0: k = len(h)
        seg = h[i:k]
        for a, b in t['stare']:
            assert a in seg, (l, a)
            seg = seg.replace(a, b)
        # przesunięcie numerów 7–12 o jeden, od końca
        for n in range(12, 6, -1):
            assert '<h2>%d. ' % n in seg, (l, n)
            seg = seg.replace('<h2>%d. ' % n, '<h2>%d. ' % (n + 1))
        nowy = '<h2 %s>7. %s</h2>%s\n' % (ZN, t['h'], ''.join('<p>%s</p>' % p for p in t['p']))
        seg = seg.replace('<h2>8. ', nowy + '<h2>8. ', 1)
        h = h[:i] + seg + h[k:]
    plik.write_text(h, 'utf-8')
    print('datenschutz pixel ok')


if __name__ == '__main__':
    uruchom()
