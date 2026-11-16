#!/usr/bin/env python3
"""Własna treść podstron dronów i marketingu (15.11.2026), DE i PL.

Drony: zapytania lokalne (Dortmund, Zagłębie Ruhry, NRW). Marketing: praca online w całych Niemczech.
Uruchamiany automatycznie przez seo_podstrony.py. Bezpieczny do wielokrotnego uruchamiania.
"""
import pathlib
from tresc_druk3d import blok, ZN

ROOT = pathlib.Path(__file__).resolve().parent.parent
PAD = 'padding-left:clamp(16px,4vw,48px);padding-right:clamp(16px,4vw,48px);padding-bottom:clamp(64px,9vw,120px);'

STRONY = [
 ('de', '<section class="drony" id="drony"', {
  'plik': 'drohnenaufnahmen/index.html', 'kontakt': '/kontakt/', 'btn_klasa': 'btn btn-glowny',
  'styl': '--akc:var(--niebieski);' + PAD,
  'h2': 'Drohnenaufnahmen in Dortmund, im Ruhrgebiet und in ganz NRW',
  'p': 'Wir fliegen in Dortmund und Umgebung – bis 20 km ohne Anfahrtskosten. Weitere Einsätze in NRW und auf Anfrage '
       'deutschlandweit. Die Anfahrt steht dann vorab im Angebot. Drohnenaufnahmen liefern wir auch direkt für Ihre Website und Werbung – und Digital Marketing machen wir mit KI-Unterstützung: Texte, Bilder und Anzeigen für Website und Social Media.',
  'kt': 'Wofür Sie Drohnenaufnahmen nutzen',
  'karty': [
   ('Immobilien', 'Haus, Grundstück und Lage in einem Bild – für Exposé, Verkauf und Vermietung.'),
   ('Baustellen', 'Baufortschritt regelmäßig aus der Luft dokumentieren.'),
   ('Dach und Fassade', 'Dach, Rinne und Fassade ansehen, ohne Gerüst.'),
   ('Events und Hochzeiten', 'Feiern und Firmenevents von oben, vor Ort mit Ihnen abgestimmt.'),
   ('Firmen und Gelände', 'Gebäude, Hallen und Gelände für Website und Werbung.'),
   ('Reels für Social Media', 'Fertig geschnittene Kurzvideos im Hochformat.'),
  ],
  'ft': 'Häufige Fragen zu Drohnenaufnahmen',
  'faq': [
   ('Was kosten Drohnenaufnahmen?', 'Drohnenaufnahmen gibt es ab 50 €. Der Preis hängt von Ort, Dauer und Schnitt ab. '
    'Sie erhalten vorab ein Angebot.'),
   ('Wo fliegen Sie?', 'In Dortmund, im Ruhrgebiet und in ganz NRW. Bis 20 km ab Dortmund berechnen wir keine Anfahrt. '
    'Einsätze in anderen Bundesländern sind auf Anfrage möglich.'),
   ('Dürfen Sie überall fliegen?', 'Nein. Ob und wann geflogen werden kann, hängt von Ort, Wetter und Luftraum ab. '
    'Wir prüfen die Flugzone vor jedem Auftrag.'),
   ('Sind Sie lizenziert und versichert?', 'Ja. Wir fliegen mit EU-Drohnenführerschein A1/A3, sind als Betreiber registriert '
    'und haben eine Haftpflichtversicherung für Drohnen.'),
   ('Was bekomme ich nach dem Flug?', 'Einen fertig geschnittenen Film mit Farbkorrektur und ausgewählte Fotos – oder das '
    'gesamte Rohmaterial in 4K für Ihren eigenen Schnitt.'),
   ('Fliegen Sie auch in Innenräumen?', 'Ja, wir filmen drinnen und draußen.'),
  ],
  'btn': 'Drohnenflug anfragen',
 }),
 ('pl', '<section class="drony" id="drony"', {
  'plik': 'pl/zdjecia-z-drona/index.html', 'kontakt': '/pl/kontakt/', 'btn_klasa': 'btn btn-glowny',
  'styl': '--akc:var(--niebieski);' + PAD,
  'h2': 'Zdjęcia i filmy z drona w Dortmundzie, Zagłębiu Ruhry i całym NRW',
  'p': 'Latamy w Dortmundzie i okolicy – do 20 km bez kosztów dojazdu. Dalsze zlecenia w NRW, a na życzenie w całych '
       'Niemczech. Koszt dojazdu podajemy wtedy z góry w wycenie. Zdjęcia z drona robimy też bezpośrednio dla Twojej strony i reklamy – a digital marketing prowadzimy z pomocą AI: teksty, zdjęcia i reklamy na stronę i do social mediów.',
  'kt': 'Do czego przydają się ujęcia z drona',
  'karty': [
   ('Nieruchomości', 'Dom, działka i okolica na jednym ujęciu – do ogłoszenia sprzedaży lub wynajmu.'),
   ('Budowy', 'Regularna dokumentacja postępu prac z powietrza.'),
   ('Dach i elewacja', 'Obejrzenie dachu, rynien i elewacji bez rusztowania.'),
   ('Imprezy i wesela', 'Uroczystości i eventy firmowe z góry, uzgodnione z Tobą na miejscu.'),
   ('Firmy i tereny', 'Budynki, hale i teren firmy na stronę i do reklamy.'),
   ('Rolki do social mediów', 'Gotowe, zmontowane krótkie filmy w pionie.'),
  ],
  'ft': 'Najczęstsze pytania o zdjęcia z drona',
  'faq': [
   ('Ile kosztują zdjęcia z drona?', 'Ujęcia z drona od 50 €. Cena zależy od miejsca, czasu i montażu. Wycenę dostajesz z góry.'),
   ('Gdzie latacie?', 'W Dortmundzie, Zagłębiu Ruhry i całym NRW. Do 20 km od Dortmundu nie liczymy dojazdu. '
    'Zlecenia w innych landach są możliwe po uzgodnieniu.'),
   ('Czy możecie latać wszędzie?', 'Nie. To, czy i kiedy można latać, zależy od miejsca, pogody i przestrzeni powietrznej. '
    'Strefę lotu sprawdzamy przed każdym zleceniem.'),
   ('Czy macie uprawnienia i ubezpieczenie?', 'Tak. Latamy z uprawnieniami UE A1/A3, jesteśmy zarejestrowanym operatorem '
    'i mamy ubezpieczenie OC na drony.'),
   ('Co dostanę po locie?', 'Zmontowany film z korekcją kolorów i wybrane zdjęcia – albo cały surowy materiał w 4K do własnego montażu.'),
   ('Czy latacie też w pomieszczeniach?', 'Tak, filmujemy wewnątrz i na zewnątrz.'),
  ],
  'btn': 'Zapytaj o lot',
 }),
 ('de', '<section class="marketing" id="marketing"', {
  'plik': 'digital-marketing/index.html', 'kontakt': '/kontakt/', 'btn_klasa': 'btn btn-bialy',
  'styl': '--akc:var(--lod);',
  'h2': 'Website, Social Media und KI-Werbung für kleine Unternehmen – online in ganz Deutschland',
  'p': 'Die Zusammenarbeit läuft online, per E-Mail und Telefon. Deshalb arbeiten wir für kleine Unternehmen in ganz '
       'Deutschland – auf Deutsch oder Polnisch.',
  'kt': 'Was wir für Ihr Unternehmen übernehmen',
  'karty': [
   ('Website erstellen lassen', 'Aufbau, Texte und Bilder. Eine Seite, die Kunden zur Anfrage führt.'),
   ('Hosting und Wartung', 'Wir bringen die Seite online und kümmern uns um Updates und Änderungen.'),
   ('Inhalte für Social Media', 'Videos, Reels, Posts und Karussells für Instagram, TikTok und Facebook.'),
   ('KI-Werbevideos', 'Werbefilme mit KI – ohne teuren Dreh. KI-Inhalte kennzeichnen wir immer.'),
   ('Werbeanzeigen', 'Grafiken und Videos für Ihre Anzeigen, einzeln oder als Paket.'),
   ('Deutsch und Polnisch', 'Inhalte und Beratung in beiden Sprachen, auch für polnischsprachige Unternehmen in Deutschland.'),
  ],
  'ft': 'Häufige Fragen zum Digital Marketing',
  'faq': [
   ('Was kostet eine Website?', 'Eine Website gibt es ab 100 €. Der Preis hängt vom Umfang ab. Sie erhalten vorab ein Angebot.'),
   ('Für wen ist das Angebot gedacht?', 'Für kleine Unternehmen und Start-ups, zum Beispiel Handwerksbetriebe, Restaurants und Salons.'),
   ('Wie läuft die Zusammenarbeit ab?', 'Sie erzählen uns von Ihrem Angebot, und wir schlagen vor, womit Sie am besten starten. '
    'Eine kurze Erstberatung ist kostenlos. Alles Weitere klären wir online.'),
   ('Betreuen Sie die Website auch nach dem Start?', 'Ja. Hosting, Updates, Änderungen und Service gehören zum Angebot.'),
   ('Sind KI-Inhalte gekennzeichnet?', 'Ja. Viele Inhalte erstellen wir mit KI-Werkzeugen und kennzeichnen sie immer.'),
   ('Arbeiten Sie auch auf Polnisch?', 'Ja, wir beraten und erstellen Inhalte auf Deutsch und auf Polnisch.'),
  ],
  'btn': 'Projekt besprechen',
 }),
 ('pl', '<section class="marketing" id="marketing"', {
  'plik': 'pl/marketing-cyfrowy/index.html', 'kontakt': '/pl/kontakt/', 'btn_klasa': 'btn btn-bialy',
  'styl': '--akc:var(--lod);',
  'h2': 'Strony www, social media i reklamy z AI dla polskich firm w Niemczech',
  'p': 'Współpraca odbywa się online, mailowo i telefonicznie. Dlatego pracujemy dla małych firm w całych Niemczech – '
       'po polsku lub po niemiecku.',
  'kt': 'Co robimy dla Twojej firmy',
  'karty': [
   ('Strona internetowa', 'Układ, teksty i zdjęcia. Strona, która prowadzi klienta do zapytania.'),
   ('Hosting i opieka', 'Uruchamiamy stronę i zajmujemy się aktualizacjami oraz zmianami.'),
   ('Treści do social mediów', 'Filmy, rolki, posty i karuzele na Instagram, TikTok i Facebook.'),
   ('Filmy reklamowe z AI', 'Spoty tworzone z AI – bez drogiego planu zdjęciowego. Treści z AI zawsze oznaczamy.'),
   ('Reklamy', 'Grafiki i filmy do Twoich reklam, pojedynczo lub w pakiecie.'),
   ('Po polsku i po niemiecku', 'Treści i doradztwo w obu językach – dla polskich firm działających w Niemczech.'),
  ],
  'ft': 'Najczęstsze pytania o marketing',
  'faq': [
   ('Ile kosztuje strona internetowa?', 'Strona internetowa od 100 €. Cena zależy od zakresu. Wycenę dostajesz z góry.'),
   ('Dla kogo jest ta oferta?', 'Dla małych firm i start-upów, na przykład firm rzemieślniczych, restauracji i salonów.'),
   ('Jak wygląda współpraca?', 'Opowiadasz nam o swojej ofercie, a my proponujemy, od czego najlepiej zacząć. '
    'Krótka pierwsza konsultacja jest bezpłatna. Resztę ustalamy online.'),
   ('Czy opiekujecie się stroną po uruchomieniu?', 'Tak. Hosting, aktualizacje, zmiany i serwis są częścią oferty.'),
   ('Czy treści z AI są oznaczane?', 'Tak. Wiele treści tworzymy narzędziami AI i zawsze je oznaczamy.'),
   ('Czy niemieckie treści też przygotujecie?', 'Tak, doradzamy i tworzymy treści po polsku i po niemiecku.'),
  ],
  'btn': 'Omów projekt',
 }),
]


def uruchom():
    for j, start, t in STRONY:
        plik = ROOT / t['plik']
        h = plik.read_text('utf-8')
        if ZN not in h:
            i = h.index(start)
            k = h.index('</section>', i)
            h = h[:k] + blok(j, t) + h[k:]
            plik.write_text(h, 'utf-8')
        print('treść ok', t['plik'])


if __name__ == '__main__':
    uruchom()
