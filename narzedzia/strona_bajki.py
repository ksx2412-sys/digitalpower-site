#!/usr/bin/env python3
"""Podstrona „Märchen mit Moral” (bajki) – digitalpower.art, 16.11.2026.

Generuje /maerchen/, /pl/bajki/ i /en/fairy-tales/ w stylu strony głównej
(czcionki Fraunces + Sora, ciemny granat, własny kolor działu – bursztyn),
z animacją Fabla jako tłem nagłówka. Bezpieczne do wielokrotnego uruchamiania.

Uruchamiać PO zbuduj.py (jeśli kiedyś nadpisze pliki) – jest wywoływane
z narzedzia/seo_podstrony.py.
"""
import base64, hashlib, json, pathlib, re

ROOT = pathlib.Path(__file__).resolve().parent.parent
INDEX = ROOT / 'index.html'
WERSJA = '20261116a'

STRONY = {
    'de': {'sciezka': 'maerchen', 'html_lang': 'de'},
    'pl': {'sciezka': 'pl/bajki', 'html_lang': 'pl'},
    'en': {'sciezka': 'en/fairy-tales', 'html_lang': 'en'},
}
URL = {j: 'https://digitalpower.art/%s/' % d['sciezka'] for j, d in STRONY.items()}

TIKTOK_FABEL = 'https://www.tiktok.com/@fabelfabelfabel7'
INSTA_FABEL = 'https://www.instagram.com/fabelfabelfabel7/'
TIKTOK_BAJKI = 'https://www.tiktok.com/@bajkibajeczkibaje'
ETSY = 'https://www.etsy.com/shop/DigitalPowerArt3D'
AMAZON = [  # (kod języka książki, nazwa w jej języku, link)
    ('de', 'Deutsch', 'https://amzn.eu/d/0dQqpLUf'),
    ('pl', 'Polski', 'https://amzn.eu/d/0294uTRl'),
    ('en', 'English', 'https://amzn.eu/d/0b7ZYtCK'),
    ('es', 'Español', 'https://amzn.eu/d/04DdjIPf'),
]

T = {
    'de': dict(
        title='Märchen mit Moral für Kinder – Videos & Malbücher | Digital Power Art',
        desc='Märchen mit Moral für Kinder von 3 bis 7 Jahren: neue Folgen auf TikTok, Malbücher auf Deutsch, Polnisch und Englisch sowie Figuren aus dem 3D-Drucker. Digital Power Art, Dortmund.',
        etykieta='Märchen & Kinder', back='Startseite',
        h1='Märchen mit Moral für Kinder',
        lead='Geschichten, die unterhalten und etwas mitgeben: neue Folgen auf TikTok, Malbücher zum Ausmalen und Figuren aus unserer 3D-Druck-Werkstatt in Dortmund.',
        btn_tiktok='Auf TikTok ansehen', btn_mal='Malbücher', lbl_tt='Auf TikTok ansehen', lbl_ig='Auf Instagram ansehen', alt_hero='Fabel-Figuren vor einem Holzhaus mit dem Schild „Fabel“', alt_f='Gruppe der Fabel-Figuren auf einer warmen Decke', alt_b='Kleine Giraffe mit verschränkten Armen neben blauen Gummistiefeln und einem Regenschirm',
        kanaly_et='Zwei Kanäle', kanaly_h='Unsere Geschichten',
        kanaly_p='Märchen mit Moral auf fabelfabelfabel7 und Gutenachtgeschichten auf bajkibajeczkibaje. Beide Kanäle sind für Kinder von 3 bis 7 Jahren gemacht – und für Eltern, die gemeinsam schauen.',
        fabel_p='Märchen mit Moral – animierte Geschichten mit Figuren, die auch als 3D-Druck bei uns entstehen.',
        bajki_p='Neue Gutenachtgeschichten dreimal pro Woche, für Kinder von 3 bis 7 Jahren.',
        rytm_f='Neue Folgen', rytm_b='3× pro Woche',
        mal_et='Malbücher', mal_h='Malbücher zum Ausmalen',
        mal_p='Die Abenteuer des kleinen Hasen als Malbuch mit kleinen Geschichten und großen Werten – erhältlich auf Amazon in vier Sprachen.',
        mal_btn='Auf Amazon ansehen', mal_hinweis='Auswahl nach Sprache des Buches.',
        werk_et='Aus der Werkstatt', werk_h='Figuren und Schlüsselanhänger',
        werk_p='Die Helden der Geschichten gibt es auch zum Anfassen: Figuren und Schlüsselanhänger aus dem 3D-Drucker, gefertigt in Dortmund.',
        werk_etsy='Zum Etsy-Shop', werk_druk='Mehr zum 3D-Druck',
        pod=['Figuren aus dem 3D-Drucker', 'Schlüsselanhänger', 'Entwurf am Computer'],
        faq_et='Für Eltern', faq_h='Fragen von Eltern',
        faq=[
            ('Für welches Alter sind die Geschichten?', 'Beide Kanäle richten sich an Kinder von etwa 3 bis 7 Jahren.'),
            ('Worum geht es in den Geschichten?', 'Jede Geschichte erzählt eine kleine Situation aus dem Kinderalltag – Freundschaft, Mut, Ehrlichkeit, Geduld – und endet mit einem Gedanken, über den man gemeinsam sprechen kann.'),
            ('Werden die Videos mit KI erstellt?', 'Ja. Die Animationen entstehen mit Unterstützung von KI-Werkzeugen und werden von uns geschnitten und vertont. Mehr dazu im KI-Hinweis.'),
            ('Wo gibt es die Malbücher?', 'Die Malbücher sind auf Amazon erhältlich – auf Deutsch, Polnisch, Englisch und Spanisch. Die Links finden Sie oben auf dieser Seite.'),
        ],
        stopka_p='3D-Druck, Drohnenaufnahmen und Digital Marketing aus Dortmund.',
        st_l='Leistungen', st_r='Rechtliches', u1='3D-Druck', u2='Drohnen', u3='Digital Marketing', u4='Märchen für Kinder',
        st_i='Impressum', st_d='Datenschutz', st_k='KI-Hinweis', kontakt='Kontakt',
        pryw='Privatsphäre hat bei uns Vorrang. Projekte unserer Kunden zeigen wir nur mit ihrer Zustimmung.',
        ki='KI',
        legal=('/impressum.html', '/datenschutz.html', '/ki-hinweis.html'),
        trasy=('/3d-druck/', '/drohnenaufnahmen/', '/digital-marketing/', '/kontakt/'),
        home='/',
    ),
    'pl': dict(
        title='Bajki z morałem dla dzieci – filmy i kolorowanki | Digital Power Art',
        desc='Bajki z morałem dla dzieci 3–7 lat: nowe odcinki na TikToku, kolorowanki po polsku, niemiecku i angielsku oraz figurki z drukarki 3D. Digital Power Art, Dortmund.',
        etykieta='Bajki i dzieci', back='Strona główna',
        h1='Bajki z morałem dla dzieci',
        lead='Historie, które bawią i czegoś uczą: nowe odcinki na TikToku, kolorowanki do pobrania i figurki z naszej pracowni druku 3D w Dortmundzie.',
        btn_tiktok='Zobacz na TikToku', btn_mal='Kolorowanki', lbl_tt='Zobacz na TikToku', lbl_ig='Zobacz na Instagramie', alt_hero='Bohaterowie Fabel przed drewnianym domkiem z napisem „Fabel”', alt_f='Grupa bohaterów Fabel na miękkim kocu', alt_b='Mała żyrafa ze skrzyżowanymi rękami obok niebieskich kaloszy i kolorowego parasola',
        kanaly_et='Dwa kanały', kanaly_h='Nasze bajki',
        kanaly_p='Bajki z morałem na fabelfabelfabel7 i bajeczki na dobranoc na bajkibajeczkibaje. Oba kanały są dla dzieci w wieku 3–7 lat i dla rodziców, którzy oglądają razem.',
        fabel_p='Bajki z morałem – animowane historie z bohaterami, którzy powstają u nas także jako wydruki 3D.',
        bajki_p='Nowe bajeczki na dobranoc trzy razy w tygodniu, dla dzieci od 3 do 7 lat.',
        rytm_f='Nowe odcinki', rytm_b='3× w tygodniu',
        mal_et='Kolorowanki', mal_h='Kolorowanki do pobrania',
        mal_p='Przygody Małego Króliczka jako kolorowanka z historiami i morałami – dostępna na Amazonie w czterech językach.',
        mal_btn='Zobacz na Amazonie', mal_hinweis='Wybór według języka książki.',
        werk_et='Z pracowni', werk_h='Figurki i breloki',
        werk_p='Bohaterów bajek można też wziąć do ręki: figurki i breloki z drukarki 3D, wykonane w Dortmundzie.',
        werk_etsy='Sklep Etsy', werk_druk='Więcej o druku 3D',
        pod=['Figurki z drukarki 3D', 'Breloki', 'Projekt na komputerze'],
        faq_et='Dla rodziców', faq_h='Pytania rodziców',
        faq=[
            ('Dla jakiego wieku są bajki?', 'Oba kanały są dla dzieci w wieku około 3–7 lat.'),
            ('O czym są historie?', 'Każda historia opowiada małą sytuację z życia dziecka – przyjaźń, odwagę, uczciwość, cierpliwość – i kończy się myślą, o której można razem porozmawiać.'),
            ('Czy filmy powstają z pomocą AI?', 'Tak. Animacje powstają z pomocą narzędzi AI, a my je montujemy i udźwiękawiamy. Więcej w informacji o AI.'),
            ('Gdzie kupić kolorowanki?', 'Kolorowanki są dostępne na Amazonie – po polsku, niemiecku, angielsku i hiszpańsku. Linki znajdziesz wyżej na tej stronie.'),
        ],
        stopka_p='Druk 3D, zdjęcia z drona i marketing cyfrowy z Dortmundu.',
        st_l='Usługi', st_r='Informacje prawne', u1='Druk 3D', u2='Drony', u3='Marketing cyfrowy', u4='Bajki dla dzieci',
        st_i='Impressum', st_d='Polityka prywatności', st_k='Informacja o AI', kontakt='Kontakt',
        pryw='Prywatność jest u nas najważniejsza. Projekty klientów pokazujemy tylko za ich zgodą.',
        ki='AI',
        legal=('/impressum.html', '/polityka-prywatnosci.html', '/ki-hinweis.html'),
        trasy=('/pl/druk-3d/', '/pl/zdjecia-z-drona/', '/pl/marketing-cyfrowy/', '/pl/kontakt/'),
        home='/pl/',
    ),
    'en': dict(
        title='Fairy tales with a moral for kids – videos & colouring books | Digital Power Art',
        desc='Fairy tales with a moral for children aged 3 to 7: new episodes on TikTok, colouring books in English, German and Polish, and 3D-printed figures. Digital Power Art, Dortmund.',
        etykieta='Fairy tales & kids', back='Home',
        h1='Fairy tales with a moral for kids',
        lead='Stories that entertain and leave something behind: new episodes on TikTok, colouring books and figures from our 3D-printing workshop in Dortmund.',
        btn_tiktok='Watch on TikTok', btn_mal='Colouring books', lbl_tt='Watch on TikTok', lbl_ig='Watch on Instagram', alt_hero='Fabel characters in front of a wooden house with a Fabel sign', alt_f='Group of Fabel characters on a soft blanket', alt_b='Small giraffe with crossed arms next to blue rain boots and a colourful umbrella',
        kanaly_et='Two channels', kanaly_h='Our stories',
        kanaly_p='Fairy tales with a moral on fabelfabelfabel7 and bedtime stories on bajkibajeczkibaje. Both channels are made for children aged 3 to 7 and for parents who watch together.',
        fabel_p='Fairy tales with a moral – animated stories with characters we also make as 3D prints.',
        bajki_p='New bedtime stories three times a week, for children aged 3 to 7.',
        rytm_f='New episodes', rytm_b='3× a week',
        mal_et='Colouring books', mal_h='Colouring books',
        mal_p='The Adventures of the Little Bunny as a colouring book with little stories and big values – available on Amazon in four languages.',
        mal_btn='View on Amazon', mal_hinweis='Choose by the language of the book.',
        werk_et='From the workshop', werk_h='Figures and keychains',
        werk_p='The heroes of the stories are also there to hold: figures and keychains from the 3D printer, made in Dortmund.',
        werk_etsy='Etsy shop', werk_druk='More about 3D printing',
        pod=['Figures from the 3D printer', 'Keychains', 'Design on the computer'],
        faq_et='For parents', faq_h='Questions from parents',
        faq=[
            ('What age are the stories for?', 'Both channels are for children aged about 3 to 7.'),
            ('What are the stories about?', 'Each story tells a small situation from a child’s everyday life – friendship, courage, honesty, patience – and ends with a thought to talk about together.'),
            ('Are the videos made with AI?', 'Yes. The animations are created with the help of AI tools and are edited and voiced by us. See our AI notice for details.'),
            ('Where can I get the colouring books?', 'The colouring books are available on Amazon – in English, German, Polish and Spanish. The links are at the top of this page.'),
        ],
        stopka_p='3D printing, drone photography and digital marketing from Dortmund.',
        st_l='Services', st_r='Legal', u1='3D printing', u2='Drones', u3='Digital marketing', u4='Fairy tales for kids',
        st_i='Legal notice', st_d='Privacy policy', st_k='AI notice', kontakt='Contact',
        pryw='Privacy comes first. We only show client projects with their consent.',
        ki='AI',
        legal=('/legal-notice.html', '/privacy-policy.html', '/ki-hinweis.html'),
        trasy=('/en/3d-printing/', '/en/drone-photography/', '/en/digital-marketing/', '/en/contact/'),
        home='/en/',
    ),
}

SKRYPT = r"""(function(){var d=document,r=matchMedia('(prefers-reduced-motion:reduce)').matches;
if('IntersectionObserver'in window&&!r){var o=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('widac');o.unobserve(e.target)}})},{threshold:.15});d.querySelectorAll('.odslon').forEach(function(el){o.observe(el)})}else{d.querySelectorAll('.odslon').forEach(function(el){el.classList.add('widac')})}
var v=d.querySelector('.kino .kinobg');if(v&&!r){var t=false;addEventListener('scroll',function(){if(t)return;t=true;requestAnimationFrame(function(){v.style.setProperty('--par',Math.min(scrollY*.18,120)+'px');t=false})},{passive:true})}
})();"""


def hash_skryptu(s):
    return "'sha256-%s'" % base64.b64encode(hashlib.sha256(s.encode('utf-8')).digest()).decode()


def fonty():
    h = INDEX.read_text('utf-8')
    return '\n'.join(dict.fromkeys(re.findall(r'@font-face\{[^}]*\}', h)))


def csp(h_index, skrypt_hash):
    m = re.search(r'<meta http-equiv="Content-Security-Policy" content="([^"]+)">', h_index)
    c = m.group(1)
    c = c.replace("script-src 'self'", "script-src 'self' " + skrypt_hash, 1)
    return c


CSS = r"""
:root{--noc:#03060d;--granat:#0a1426;--linia:#1d2c47;--tekst:#eef3fb;--tekst-2:#a9b8d0;--niebieski:#2f9bff;--czerwien:#ff4b5c;--lod:#dfe8f5;--bursztyn:#ffb547;--k:var(--bursztyn);--font-display:"Fraunces",Georgia,"Times New Roman",serif;--font-body:"Sora","Segoe UI",Arial,sans-serif;color-scheme:dark}
*{box-sizing:border-box}html{scroll-behavior:smooth}
body{margin:0;background:var(--noc);color:var(--tekst);font-family:var(--font-body);font-size:16px;line-height:1.6;-webkit-font-smoothing:antialiased}
a{color:inherit;text-decoration:none}img,video{max-width:100%;display:block}
.pasek{position:fixed;inset:0 0 auto 0;z-index:50;display:flex;align-items:center;gap:28px;padding:14px clamp(16px,4vw,48px);background:#03060df0;backdrop-filter:blur(10px);border-bottom:1px solid var(--linia)}
.logo{display:flex;align-items:center;gap:12px;flex:none}
.logo img{width:46px;height:46px;border-radius:50%;box-shadow:0 0 0 1px #2f9bff55,0 0 22px #2f9bff40}
.logo .adres{font-family:var(--font-body);font-weight:700;font-size:21px;letter-spacing:-.01em;white-space:nowrap}
.logo .w-digital{color:var(--niebieski)}.logo .w-power{color:#fff}.logo .w-art{font-style:normal;color:var(--tekst-2)}
.wstecz{display:inline-flex;align-items:center;gap:10px;padding:11px 20px 11px 16px;border-radius:999px;background:var(--tekst);color:var(--noc);font-size:15px;font-weight:700;box-shadow:0 6px 20px -6px #000c;transition:transform .2s,background .2s}
.wstecz svg{width:18px;height:18px}.wstecz:hover{background:#fff;transform:translateX(-2px)}
.jezyki{margin-left:auto;display:flex;border:1px solid var(--linia);border-radius:999px;padding:3px;background:#03060daa;flex:none}
.jezyki a{display:inline-flex;align-items:center;gap:7px;padding:5px 12px 5px 9px;border-radius:999px;font-size:12.5px;font-weight:600;color:var(--tekst-2);letter-spacing:.04em}
.jezyki a[aria-current="page"]{background:var(--tekst);color:var(--noc)}
.flaga{width:20px;height:13px;border-radius:2px;box-shadow:0 0 0 1px #ffffff30;flex:none;display:block}
.sekcja-etykieta{display:inline-block;font-size:14px;font-weight:600;color:var(--k);margin-bottom:14px;letter-spacing:.02em}
.sekcja-etykieta::before{content:"";display:inline-block;vertical-align:middle;margin:-3px 10px 0 0;width:28px;height:3px;border-radius:3px;background:var(--k)}
.kino{position:relative;min-height:clamp(520px,88vh,860px);display:flex;align-items:flex-end;overflow:hidden;background:var(--noc)}
.kino .kinobg{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:center 30%;transform:translateY(var(--par,0px)) scale(1.06);will-change:transform}
.kino::after{content:"";position:absolute;inset:0;background:linear-gradient(0deg,var(--noc) 0%,#03060dcc 30%,#03060d55 55%,transparent 80%),linear-gradient(90deg,#03060db3 0%,transparent 60%)}
.kino-tekst{position:relative;z-index:2;padding:120px clamp(16px,4vw,48px) clamp(40px,6vw,72px);max-width:860px}
.kino h1{font-family:var(--font-display);font-weight:700;font-size:clamp(38px,6vw,84px);line-height:1;letter-spacing:-.015em;margin:0 0 18px;text-wrap:balance;text-shadow:0 3px 20px #000c}
.kino h1 em{font-style:italic;font-weight:600;color:var(--bursztyn)}
.kino p{margin:0 0 26px;color:#dbe4f2;font-size:clamp(16px,1.6vw,19px);max-width:34em;text-shadow:0 2px 10px #000}
.akcje{display:flex;flex-wrap:wrap;gap:12px}
.btn{display:inline-flex;align-items:center;gap:10px;padding:15px 26px;border-radius:999px;font-weight:600;font-size:15.5px;border:1px solid transparent;transition:transform .15s,background .2s,border-color .2s,box-shadow .2s;cursor:pointer}
.btn:active{transform:translateY(1px)}.btn svg{width:18px;height:18px}
.btn-glowny{background:var(--bursztyn);color:#1a1000;box-shadow:0 10px 30px -8px #ffb547aa}.btn-glowny:hover{background:#ffc66b}
.btn-drugi{border-color:#ffffff40;background:#ffffff0d;backdrop-filter:blur(6px);color:#fff}.btn-drugi:hover{border-color:#ffffff90}
.btn-etsy{background:#f1641e;color:#fff;box-shadow:0 10px 30px -8px #f1641eaa}.btn-etsy:hover{background:#ff7a38}
.btn-duzy{padding:18px 34px;font-size:17px}
.znacznik-ki{position:absolute;z-index:3;bottom:14px;right:14px;font-size:10.5px;font-weight:500;color:#ffffffc0;background:#03060d8c;padding:2px 7px;border-radius:4px}
.sekcja{padding:clamp(56px,8vw,104px) clamp(16px,4vw,48px)}
.sekcja+.sekcja{border-top:1px solid var(--linia)}
.srodek{max-width:1180px;margin:0 auto}
.glowa{max-width:760px;margin-bottom:clamp(28px,4vw,44px)}
.glowa h2{font-family:var(--font-display);font-weight:700;font-size:clamp(32px,4.4vw,56px);line-height:1.04;letter-spacing:-.01em;margin:0 0 14px;text-wrap:balance}
.glowa p{margin:0;color:var(--tekst-2);font-size:clamp(16px,1.4vw,18px)}
.karty{display:grid;grid-template-columns:1fr 1fr;gap:22px}
.karta{position:relative;display:flex;flex-direction:column;min-width:0;background:var(--granat);border:1px solid var(--linia);border-radius:22px;overflow:hidden;transition:border-color .25s,transform .25s,box-shadow .25s}
.karta:hover{border-color:color-mix(in srgb,var(--k) 55%,var(--linia));transform:translateY(-3px);box-shadow:0 30px 60px -24px color-mix(in srgb,var(--k) 45%,#000)}
.kadr{position:relative;aspect-ratio:16/10;background:#000;overflow:hidden}
.kadr img,.kadr video{width:100%;height:100%;object-fit:cover}
.kadr::after{content:"";position:absolute;inset:0;background:linear-gradient(0deg,var(--granat) 0%,transparent 45%)}
.karta-tresc{display:flex;flex-direction:column;gap:14px;padding:24px 26px 26px;flex:1}
.karta h3{font-family:var(--font-display);font-weight:700;font-size:clamp(26px,2.6vw,32px);line-height:1.1;margin:0;color:var(--k);word-break:break-word}
.karta p{margin:0;color:var(--tekst-2);font-size:15.5px}
.rytm{display:inline-flex;align-items:center;gap:8px;font-size:13px;font-weight:600;color:var(--tekst);padding:6px 12px;border:1px solid var(--linia);border-radius:999px;background:#03060d80;align-self:flex-start}
.rytm i{width:8px;height:8px;border-radius:50%;background:var(--k);box-shadow:0 0 10px var(--k)}
.social{display:flex;flex-wrap:wrap;gap:8px;margin-top:auto;padding-top:8px}
.social a{width:48px;height:48px;border-radius:50%;display:grid;place-items:center;color:#fff;border:1.5px solid #ffffff40;box-shadow:0 6px 18px -6px #000c;transition:transform .2s,box-shadow .2s,filter .2s}
.social a:hover{transform:translateY(-2px);filter:brightness(1.12)}
.social a.z-napisem{width:auto;padding:0 16px 0 12px;gap:8px;display:inline-flex;align-items:center;white-space:nowrap;font-size:14px;font-weight:600;letter-spacing:.01em}
.social a.z-napisem span{line-height:1}
.social a[aria-label="Instagram"]{background:radial-gradient(circle at 30% 107%,#fdf497 0%,#fd5949 45%,#d6249f 60%,#285aeb 90%)}
.social a[aria-label="TikTok"]{background:#000;box-shadow:-2px -2px 0 #25f4ee inset,2px 2px 0 #fe2c55 inset,0 6px 18px -6px #000c}
.social a[aria-label="Facebook"]{background:#1877f2}.social a[aria-label="Etsy-Shop"]{background:#f1641e}
.social svg{width:20px;height:20px;stroke-width:2.1}
.social .btn{margin-left:auto}
.ksiazki{display:grid;grid-template-columns:repeat(4,1fr);gap:16px}
.ksiazka{display:flex;flex-direction:column;gap:12px;padding:22px 22px 20px;background:var(--granat);border:1px solid var(--linia);border-radius:20px;transition:border-color .25s,transform .25s}
.ksiazka:hover{border-color:var(--k);transform:translateY(-3px)}
.ksiazka .jez{display:inline-flex;align-items:center;gap:8px;font-family:var(--font-display);font-weight:600;font-size:22px;color:var(--tekst)}
.ksiazka .jez .flaga{width:26px;height:17px}
.ksiazka small{color:var(--tekst-2);font-size:13.5px}
.ksiazka .link{margin-top:auto;display:inline-flex;align-items:center;gap:8px;font-weight:600;font-size:14.5px;color:var(--k)}
.ksiazka .link svg{width:16px;height:16px;transition:transform .2s}.ksiazka:hover .link svg{transform:translateX(4px)}
.hinweis{margin:14px 0 0;color:var(--tekst-2);font-size:13.5px}
.werk{display:grid;grid-template-columns:1.05fr .95fr;gap:clamp(24px,4vw,48px);align-items:center}
.galeria{display:grid;grid-template-columns:1fr 1fr;gap:14px}
.galeria figure{margin:0;position:relative;border-radius:18px;overflow:hidden;border:1px solid var(--linia);background:#000}
.galeria figure:first-child{grid-column:1/-1;aspect-ratio:16/9}
.galeria figure{aspect-ratio:4/3}
.galeria img{width:100%;height:100%;object-fit:cover;transition:transform .5s}.galeria figure:hover img{transform:scale(1.04)}
.galeria figcaption{position:absolute;left:12px;bottom:10px;font-size:12.5px;font-weight:600;padding:4px 10px;border-radius:999px;background:#03060dcc;color:var(--tekst)}
.faq{display:grid;gap:10px;max-width:860px}
.faq details{background:var(--granat);border:1px solid var(--linia);border-radius:16px;padding:0;transition:border-color .25s}
.faq details[open]{border-color:color-mix(in srgb,var(--k) 55%,var(--linia))}
.faq summary{cursor:pointer;list-style:none;display:flex;justify-content:space-between;align-items:center;gap:16px;padding:18px 22px;font-weight:600;font-size:16.5px}
.faq summary::-webkit-details-marker{display:none}
.faq summary::after{content:"+";font-family:var(--font-display);font-size:24px;line-height:1;color:var(--k);transition:transform .25s}
.faq details[open] summary::after{transform:rotate(45deg)}
.faq details p{margin:0;padding:0 22px 20px;color:var(--tekst-2)}
.odslon{opacity:0;transform:translateY(18px);transition:opacity .7s ease,transform .7s ease}
.odslon.widac{opacity:1;transform:none}
.odslon:nth-child(2){transition-delay:.1s}.odslon:nth-child(3){transition-delay:.2s}.odslon:nth-child(4){transition-delay:.3s}
@media (prefers-reduced-motion:reduce){.odslon{opacity:1;transform:none;transition:none}.kino .kinobg{transform:none}}
.stopka{padding:clamp(40px,5vw,56px) clamp(16px,4vw,48px) 28px;background:#02040a;border-top:1px solid var(--linia);color:var(--tekst-2);font-size:14px}
.stopka-gora{display:grid;grid-template-columns:minmax(0,1.4fr) repeat(2,minmax(0,1fr));gap:28px;padding-bottom:28px;border-bottom:1px solid var(--linia)}
.stopka .logo span{font-family:var(--font-display);font-weight:700;font-size:19px}.stopka .logo em{font-style:italic;color:var(--czerwien);margin:0 .14em}
.stopka p{margin:14px 0 0;max-width:30em}
.stopka h3{font-size:13px;font-weight:600;color:var(--tekst);margin:0 0 12px;letter-spacing:.03em}
.stopka ul{list-style:none;margin:0;padding:0;display:grid;gap:8px}.stopka a:hover{color:var(--tekst)}
.stopka-social{margin-top:18px}.stopka-social a{width:42px;height:42px}
.stopka-dol{display:flex;flex-wrap:wrap;justify-content:space-between;gap:12px;padding-top:20px;font-size:13px}
.stopka-dol svg{width:15px;height:15px;vertical-align:-2px;margin-right:6px;color:var(--niebieski)}
@media (max-width:980px){.ksiazki{grid-template-columns:1fr 1fr}.werk{grid-template-columns:1fr}}
@media (max-width:900px){.stopka-gora{grid-template-columns:1fr 1fr}.stopka-gora>div:first-child{grid-column:1/-1}}
@media (max-width:760px){.karty{grid-template-columns:1fr}.kino{min-height:auto;flex-direction:column;align-items:stretch}.kino .kinobg{position:relative;height:auto;aspect-ratio:16/9;margin-top:76px;transform:none!important}.kino::after{background:linear-gradient(0deg,var(--noc) 0%,transparent 60%) top/100% calc(76px + 56.25vw) no-repeat}.kino-tekst{padding-top:8px;margin-top:-30vw}}
@media (max-width:640px){.pasek{gap:10px}.logo{gap:8px}.logo .adres{font-size:15px}.logo img{width:40px;height:40px}.wstecz span{display:none}.wstecz{padding:11px 12px}.jezyki a{padding:5px 7px;gap:4px;font-size:11.5px}.flaga{width:16px;height:11px}.galeria figure{aspect-ratio:3/2}}
@media (max-width:480px){.ksiazki{grid-template-columns:1fr}.jezyki a span{display:none}.jezyki a{padding:5px 6px}.wstecz{padding:10px 11px}}
"""

FLAGI = {
    'de': '<svg class="flaga" viewBox="0 0 5 3" aria-hidden="true"><rect width="5" height="1" fill="#000"/><rect y="1" width="5" height="1" fill="#DD0000"/><rect y="2" width="5" height="1" fill="#FFCE00"/></svg>',
    'pl': '<svg class="flaga" viewBox="0 0 8 5" aria-hidden="true"><rect width="8" height="5" fill="#DC143C"/><rect width="8" height="2.5" fill="#fff"/></svg>',
    'en': '<svg class="flaga" viewBox="0 0 60 30" aria-hidden="true"><clipPath id="uk-c"><path d="M0 0v30h60V0z"/></clipPath><clipPath id="uk-t"><path d="M30 15h30v15zv15H0zH0V0zV0h30z"/></clipPath><g clip-path="url(#uk-c)"><path d="M0 0v30h60V0z" fill="#012169"/><path d="M0 0l60 30m0-30L0 30" stroke="#fff" stroke-width="6"/><path d="M0 0l60 30m0-30L0 30" clip-path="url(#uk-t)" stroke="#C8102E" stroke-width="4"/><path d="M30 0v30M0 15h60" stroke="#fff" stroke-width="10"/><path d="M30 0v30M0 15h60" stroke="#C8102E" stroke-width="6"/></g></svg>',
    'es': '<svg class="flaga" viewBox="0 0 6 4" aria-hidden="true"><rect width="6" height="4" fill="#AA151B"/><rect y="1" width="6" height="2" fill="#F1BF00"/></svg>',
}
IK_TIKTOK = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M9 12a4 4 0 1 0 4 4V2c.5 3 2.5 5 6 5"/></svg>'
IK_INSTA = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="2" y="2" width="20" height="20" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r=".8" fill="currentColor"/></svg>'
IK_FB = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"/></svg>'
IK_ETSY = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M6 2 3 6v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6l-3-4z"/><path d="M3 6h18"/><path d="M16 10a4 4 0 0 1-8 0"/></svg>'
IK_STRZ = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14"/><path d="m13 6 6 6-6 6"/></svg>'
IK_WSTECZ = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M19 12H5"/><path d="m11 18-6-6 6-6"/></svg>'
IK_ZAMEK = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="4" y="11" width="16" height="10" rx="2"/><path d="M8 11V7a4 4 0 0 1 8 0v4"/></svg>'
IK_ZEW = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M14 4h6v6"/><path d="M20 4 10 14"/><path d="M20 14v5a1 1 0 0 1-1 1H5a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h5"/></svg>'


def e(s):
    return s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot;')


def strona(j):
    t = T[j]
    h_index = INDEX.read_text('utf-8')
    sh = hash_skryptu(SKRYPT)
    jezyki = ''.join('<a href="%s" hreflang="%s" lang="%s"%s>%s%s</a>' % (
        URL[x], x, x, ' aria-current="page"' if x == j else '', FLAGI[x], '<span>%s</span>' % x.upper()) for x in ('de', 'pl', 'en'))
    hreflang = ''.join('<link rel="alternate" hreflang="%s" href="%s">' % (x, URL[x]) for x in ('de', 'pl', 'en')) + \
        '<link rel="alternate" hreflang="x-default" href="%s">' % URL['de']
    ksiazki = ''.join(
        '<a class="ksiazka odslon" href="%s" target="_blank" rel="noopener noreferrer" hreflang="%s"><span class="jez">%s%s</span><span class="link">%s %s</span></a>'
        % (link, kod, FLAGI[kod], e(nazwa), e(t['mal_btn']), IK_STRZ)
        for kod, nazwa, link in AMAZON)
    faq_html = ''.join('<details class="odslon"><summary>%s</summary><p>%s</p></details>' % (e(q), e(a)) for q, a in t['faq'])
    faq_ld = {'@context': 'https://schema.org', '@type': 'FAQPage', 'mainEntity': [
        {'@type': 'Question', 'name': q, 'acceptedAnswer': {'@type': 'Answer', 'text': a}} for q, a in t['faq']]}
    page_ld = {'@context': 'https://schema.org', '@type': 'WebPage', 'name': t['title'], 'description': t['desc'],
               'url': URL[j], 'inLanguage': j,
               'about': {'@type': 'Organization', 'name': 'Digital Power Art', 'url': 'https://digitalpower.art/',
                         'sameAs': [TIKTOK_FABEL, INSTA_FABEL, TIKTOK_BAJKI, ETSY]},
               'isPartOf': {'@type': 'WebSite', 'name': 'Digital Power Art', 'url': 'https://digitalpower.art/'}}
    u1, u2, u3, u4 = t['u1'], t['u2'], t['u3'], t['u4']
    r1, r2, r3, rk = t['trasy']
    l_imp, l_dat, l_ki = t['legal']
    html = f'''<!DOCTYPE html>
<html lang="{t.get('html_lang', j)}" translate="no"><head><meta charset="utf-8"><meta name="google" content="notranslate"><meta http-equiv="Content-Security-Policy" content="{csp(h_index, sh)}"><meta name="referrer" content="strict-origin-when-cross-origin"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(t['title'])}</title>
<meta name="description" content="{e(t['desc'])}">
<link rel="canonical" href="{URL[j]}">{hreflang}
<meta property="og:type" content="website"><meta property="og:url" content="{URL[j]}"><meta property="og:title" content="{e(t['title'])}"><meta property="og:description" content="{e(t['desc'])}"><meta property="og:image" content="https://digitalpower.art/media/fabel-og-bohaterowie.jpg"><meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/media/logo-circle.png">
<script type="application/ld+json">{json.dumps(page_ld, ensure_ascii=False)}</script>
<script type="application/ld+json">{json.dumps(faq_ld, ensure_ascii=False)}</script>
<style>{fonty()}
{CSS}</style>
</head>
<body data-strona="maerchen">
<header class="pasek">
  <a class="logo" href="{t['home']}" aria-label="digitalpower.art — Start" translate="no"><img src="/media/logo-circle.png" alt=""><span class="adres"><b class="w-digital">digital</b><b class="w-power">power</b><i class="w-art">.art</i></span></a>
  <a class="wstecz" href="{t['home']}">{IK_WSTECZ}<span>{e(t['back'])}</span></a>
  <nav class="jezyki" aria-label="Sprache / Język / Language">{jezyki}</nav>
</header>
<main>
<section class="kino" aria-labelledby="tytul">
  <img class="kinobg" src="/media/fabel-bohaterowie-naglowek-800.webp" srcset="/media/fabel-bohaterowie-naglowek-800.webp 800w, /media/fabel-bohaterowie-naglowek-1600.webp 1600w" sizes="100vw" width="1600" height="900" alt="{e(t['alt_hero'])}" fetchpriority="high">
  <span class="znacznik-ki">{e(t['ki'])}</span>
  <div class="kino-tekst">
    <span class="sekcja-etykieta">{e(t['etykieta'])}</span>
    <h1 id="tytul">{e(t['h1'])}</h1>
    <p>{e(t['lead'])}</p>
    <div class="akcje">
      <a class="btn btn-glowny btn-duzy" href="{TIKTOK_FABEL}" target="_blank" rel="noopener noreferrer">{IK_TIKTOK}{e(t['btn_tiktok'])}</a>
      <a class="btn btn-drugi btn-duzy" href="#malbuecher">{e(t['btn_mal'])}{IK_STRZ}</a>
    </div>
  </div>
</section>

<section class="sekcja" id="kanaele" aria-labelledby="kanaly-h">
  <div class="srodek">
    <div class="glowa odslon"><span class="sekcja-etykieta">{e(t['kanaly_et'])}</span><h2 id="kanaly-h">{e(t['kanaly_h'])}</h2><p>{e(t['kanaly_p'])}</p></div>
    <div class="karty">
      <article class="karta odslon">
        <div class="kadr"><img loading="lazy" src="/media/fabel-grupa-na-kocu-800.webp" width="800" height="450" alt="{e(t['alt_f'])}"><span class="znacznik-ki">{e(t['ki'])}</span></div>
        <div class="karta-tresc">
          <span class="rytm"><i></i>{e(t['rytm_f'])}</span>
          <h3 translate="no">fabelfabelfabel7</h3>
          <p>{e(t['fabel_p'])}</p>
          <nav class="social" aria-label="fabelfabelfabel7">
            <a class="z-napisem" href="{TIKTOK_FABEL}" target="_blank" rel="noopener noreferrer" aria-label="TikTok">{IK_TIKTOK}<span>{e(t['lbl_tt'])}</span></a>
            <a class="z-napisem" href="{INSTA_FABEL}" target="_blank" rel="noopener noreferrer" aria-label="Instagram">{IK_INSTA}<span>{e(t['lbl_ig'])}</span></a>
          </nav>
        </div>
      </article>
      <article class="karta odslon">
        <div class="kadr"><img loading="lazy" src="/media/fabel-zyrafa-w-deszczu-800.webp" width="800" height="450" alt="{e(t['alt_b'])}"></div>
        <div class="karta-tresc">
          <span class="rytm"><i></i>{e(t['rytm_b'])}</span>
          <h3 translate="no">bajkibajeczkibaje</h3>
          <p>{e(t['bajki_p'])}</p>
          <nav class="social" aria-label="bajkibajeczkibaje">
            <a class="z-napisem" href="{TIKTOK_BAJKI}" target="_blank" rel="noopener noreferrer" aria-label="TikTok">{IK_TIKTOK}<span>{e(t['lbl_tt'])}</span></a>
          </nav>
        </div>
      </article>
    </div>
  </div>
</section>

<section class="sekcja" id="malbuecher" aria-labelledby="mal-h">
  <div class="srodek">
    <div class="glowa odslon"><span class="sekcja-etykieta">{e(t['mal_et'])}</span><h2 id="mal-h">{e(t['mal_h'])}</h2><p>{e(t['mal_p'])}</p></div>
    <div class="ksiazki">{ksiazki}</div>
    <p class="hinweis">{e(t['mal_hinweis'])}</p>
  </div>
</section>

<section class="sekcja" id="werkstatt" aria-labelledby="werk-h">
  <div class="srodek werk">
    <div class="odslon">
      <span class="sekcja-etykieta" style="--k:var(--czerwien)">{e(t['werk_et'])}</span>
      <h2 id="werk-h" class="glowa-h" style="font-family:var(--font-display);font-weight:700;font-size:clamp(32px,4.4vw,56px);line-height:1.04;letter-spacing:-.01em;margin:0 0 14px;text-wrap:balance">{e(t['werk_h'])}</h2>
      <p style="margin:0 0 24px;color:var(--tekst-2);font-size:clamp(16px,1.4vw,18px)">{e(t['werk_p'])}</p>
      <div class="akcje">
        <a class="btn btn-etsy" href="{ETSY}" target="_blank" rel="noopener noreferrer">{IK_ETSY}{e(t['werk_etsy'])}</a>
        <a class="btn btn-drugi" href="{r1}">{e(t['werk_druk'])}{IK_STRZ}</a>
      </div>
    </div>
    <div class="galeria odslon">
      <figure><img loading="lazy" src="/media/fabel_fig.jpg" alt="{e(t['pod'][0])}"><figcaption>{e(t['pod'][0])}</figcaption></figure>
      <figure><img loading="lazy" src="/media/fabel_key.jpg" alt="{e(t['pod'][1])}"><figcaption>{e(t['pod'][1])}</figcaption></figure>
      <figure><img loading="lazy" src="/media/fabel_cad.jpg" alt="{e(t['pod'][2])}"><figcaption>{e(t['pod'][2])}</figcaption></figure>
    </div>
  </div>
</section>

<section class="sekcja" id="eltern" aria-labelledby="faq-h">
  <div class="srodek">
    <div class="glowa odslon"><span class="sekcja-etykieta">{e(t['faq_et'])}</span><h2 id="faq-h">{e(t['faq_h'])}</h2></div>
    <div class="faq">{faq_html}</div>
  </div>
</section>
</main>

<footer class="stopka">
  <div class="stopka-gora">
    <div>
      <a class="logo" href="{t['home']}" translate="no"><img src="/media/logo-circle.png" alt=""><span><b class="w-digital">Digital</b><em>3D</em><b class="w-power">Power</b></span></a>
      <p>{e(t['stopka_p'])}</p>
      <nav class="social stopka-social" aria-label="Social Media"><a href="https://www.instagram.com/digitalpower.art/" target="_blank" rel="noopener noreferrer" aria-label="Instagram">{IK_INSTA}</a><a href="https://www.tiktok.com/@digitalpower.art" target="_blank" rel="noopener noreferrer" aria-label="TikTok">{IK_TIKTOK}</a><a href="https://www.facebook.com/profile.php?id=61590071507349" target="_blank" rel="noopener noreferrer" aria-label="Facebook">{IK_FB}</a><a href="{ETSY}" target="_blank" rel="noopener noreferrer" aria-label="Etsy-Shop">{IK_ETSY}</a></nav>
    </div>
    <div><h3>{e(t['st_l'])}</h3><ul><li><a href="{r1}">{e(u1)}</a></li><li><a href="{r2}">{e(u2)}</a></li><li><a href="{r3}">{e(u3)}</a></li><li><a href="{URL[j]}" aria-current="page">{e(u4)}</a></li></ul></div>
    <div><h3>{e(t['st_r'])}</h3><ul><li><a href="{l_imp}">{e(t['st_i'])}</a></li><li><a href="{l_dat}">{e(t['st_d'])}</a></li><li><a href="{l_ki}">{e(t['st_k'])}</a></li><li><a href="{rk}">{e(t['kontakt'])}</a></li></ul></div>
  </div>
  <div class="stopka-dol"><span>© 2026 Digital Power Art</span><span>{IK_ZAMEK}<span>{e(t['pryw'])}</span></span></div>
</footer>
<script>{SKRYPT}</script>
<script src="/zgoda.js?v=20261115c" defer></script>
</body></html>
'''
    return html


def uruchom():
    for j, d in STRONY.items():
        cel = ROOT / d['sciezka'] / 'index.html'
        cel.parent.mkdir(parents=True, exist_ok=True)
        cel.write_text(strona(j), 'utf-8')
        print('bajki:', cel.relative_to(ROOT))


if __name__ == '__main__':
    uruchom()
