/* Zgoda na cookies + Piksel Meta + tag Google (15.11.2026).
   Nic się nie ładuje, dopóki odwiedzający nie kliknie „Akzeptieren”.
   Dopóki oba identyfikatory poniżej są puste, skrypt nie robi nic i baner się nie pokazuje. */
(function(){
  /* Kliknięcie w link do sklepu Etsy → zdarzenie „klik_etsy” w warstwie danych (dataLayer).
     Nic nie ładuje się tu bez zgody; GTM wysyła zdarzenie do GA4 dopiero po akceptacji cookies. */
  document.addEventListener('click', function(e){
    var a = e.target && e.target.closest ? e.target.closest('a[href*="etsy.com"]') : null;
    if(!a) return;
    window.dataLayer = window.dataLayer || [];
    window.dataLayer.push({event: 'klik_etsy', etsy_url: a.href, etsy_miejsce: a.closest('nav,footer,section') ? (a.closest('footer') ? 'stopka' : (a.closest('.startowe-social') ? 'start' : 'inne')) : 'inne'});
  }, true);
  var META_PIXEL = '2628116907652058';   // identyfikator Piksela Meta (same cyfry)
  var GOOGLE_TAG = 'GTM-W94H254N';   // kontener Google Tag Manager (GTM-…); tag GA4 ustawia się w GTM
  var GOOGLE_LEAD = '';  // etykieta konwersji Google Ads „zapytanie” (AW-…/…), opcjonalnie

  if(!META_PIXEL && !GOOGLE_TAG) return;
  var KLUCZ='dp_zgoda_v1', d=document, w=window, zaladowane=false;
  var kto=[META_PIXEL?'Meta':'',GOOGLE_TAG?'Google':''].filter(Boolean);
  var T={
    de:{t:'Wir nutzen Cookies von '+kto.join(' und ')+', um zu messen, wie unsere Website genutzt wird und ob unsere Werbung wirkt – nur mit Ihrer Zustimmung.',w:'Mehr dazu in der Datenschutzerklärung',tak:'Akzeptieren',nie:'Ablehnen',u:'Cookie-Einstellungen',p:'/datenschutz.html'},
    pl:{t:'Używamy plików cookie '+kto.join(' i ')+', żeby mierzyć, jak korzysta się ze strony i czy nasze reklamy działają – tylko za Twoją zgodą.',w:'Więcej w polityce prywatności',tak:'Akceptuję',nie:'Odrzucam',u:'Ustawienia cookies',p:'/polityka-prywatnosci.html'},
    en:{t:'We use cookies from '+kto.join(' and ')+' to measure how the website is used and whether our ads work – only with your consent.',w:'More in the privacy policy',tak:'Accept',nie:'Decline',u:'Cookie settings',p:'/privacy-policy.html'}
  };
  function jez(){var l=(d.documentElement.lang||'de').slice(0,2);return T[l]?l:'de';}
  function czytaj(){try{return localStorage.getItem(KLUCZ);}catch(e){return null;}}
  function zapisz(v){try{localStorage.setItem(KLUCZ,v);}catch(e){}}

  function laduj(){
    if(zaladowane) return; zaladowane=true;
    if(META_PIXEL){
      !function(f,b,e,v,n,t,s){if(f.fbq)return;n=f.fbq=function(){n.callMethod?n.callMethod.apply(n,arguments):n.queue.push(arguments)};
        if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';n.queue=[];t=b.createElement(e);t.async=!0;t.src=v;
        s=b.getElementsByTagName(e)[0];s.parentNode.insertBefore(t,s)}(w,d,'script','https://connect.facebook.net/en_US/fbevents.js');
      w.fbq('init',META_PIXEL); w.fbq('track','PageView');
    }
    if(GOOGLE_TAG){
      w.dataLayer=w.dataLayer||[]; w.gtag=function(){w.dataLayer.push(arguments);};
      w.gtag('consent','default',{ad_storage:'denied',ad_user_data:'denied',ad_personalization:'denied',analytics_storage:'granted'});
      if(GOOGLE_TAG.indexOf('GTM-')===0){
        w.dataLayer.push({'gtm.start':new Date().getTime(),event:'gtm.js'});
        var g=d.createElement('script'); g.async=true; g.src='https://www.googletagmanager.com/gtm.js?id='+encodeURIComponent(GOOGLE_TAG); d.head.appendChild(g);
      } else {
        w.gtag('js',new Date()); w.gtag('config',GOOGLE_TAG);
        var s=d.createElement('script'); s.async=true; s.src='https://www.googletagmanager.com/gtag/js?id='+encodeURIComponent(GOOGLE_TAG); d.head.appendChild(s);
      }
    }
  }
  // Przy GTM zdarzenia idą przez dataLayer (GTM je odbiera), przy bezpośrednim tagu przez gtag.
  function gaZdarzenie(nazwa,parametry){
    if(GOOGLE_TAG.indexOf('GTM-')===0){ var o={event:nazwa}; for(var k in parametry) o[k]=parametry[k]; w.dataLayer.push(o); }
    else w.gtag('event',nazwa,parametry||{});
  }
  function odslona(){
    if(!zaladowane) return;
    if(w.fbq) w.fbq('track','PageView');
    if(w.gtag) gaZdarzenie('page_view',{page_location:location.href,page_title:d.title});
  }
  function zapytanie(){
    if(!zaladowane) return;
    if(w.fbq) w.fbq('track','Lead');
    if(w.gtag){ gaZdarzenie('generate_lead'); if(GOOGLE_LEAD) w.gtag('event','conversion',{send_to:GOOGLE_LEAD}); }
  }

  // Strona przełącza podstrony bez przeładowania – liczymy każdą odsłonę.
  ['pushState','replaceState'].forEach(function(n){var o=history[n];history[n]=function(){var s=location.pathname;var r=o.apply(this,arguments);if(location.pathname!==s)setTimeout(odslona,50);return r;};});
  w.addEventListener('popstate',function(){setTimeout(odslona,50);});

  // Wysłany formularz = zapytanie.
  d.addEventListener('submit',function(e){
    var f=e.target; if(!f||!f.checkValidity||!f.checkValidity()) return;
    if(f.id==='formularz'){var a=d.getElementById('f-name'),b=d.getElementById('f-msg'); if(!a||!b||!a.value.trim()||!b.value.trim()) return;}
    zapytanie();
  },true);

  var baner=null;
  function styl(){
    if(d.getElementById('zgoda-styl')) return;
    var s=d.createElement('style'); s.id='zgoda-styl';
    s.textContent='.dp-cookie{position:fixed;left:50%;transform:translateX(-50%);bottom:calc(14px + env(safe-area-inset-bottom,0px));z-index:60;width:min(680px,calc(100% - 24px));'
      +'display:flex;flex-wrap:wrap;align-items:center;gap:14px 18px;padding:16px 18px;border-radius:18px;background:var(--granat,#0a1426);border:1px solid var(--linia,#1d2c47);'
      +'box-shadow:0 18px 50px -12px #000c;color:var(--tekst,#eef3fb);font:400 14.5px/1.5 var(--font-body,Arial,sans-serif)}'
      +'.dp-cookie p{margin:0;flex:1 1 300px}.dp-cookie p a{color:var(--tekst-2,#a9b8d0);text-decoration:underline}'
      +'.dp-cookie div{display:flex;gap:10px;flex:0 0 auto}'
      +'.dp-cookie button{font:600 14.5px/1 var(--font-body,Arial,sans-serif);padding:12px 20px;border-radius:999px;cursor:pointer;border:1.5px solid #ffffff55;background:transparent;color:var(--tekst,#eef3fb)}'
      +'.dp-cookie button[data-z="tak"]{background:var(--tekst,#eef3fb);border-color:var(--tekst,#eef3fb);color:#0a1426}'
      +'@media (max-width:560px){.dp-cookie div{flex:1 1 100%}.dp-cookie button{flex:1}}';
    d.head.appendChild(s);
  }
  function pokaz(){
    styl(); if(baner) baner.remove();
    var t=T[jez()];
    baner=d.createElement('div'); baner.className='dp-cookie'; baner.setAttribute('role','dialog'); baner.setAttribute('aria-label',t.u);
    var p=d.createElement('p'); p.appendChild(d.createTextNode(t.t+' '));
    var a=d.createElement('a'); a.href=t.p; a.textContent=t.w; p.appendChild(a); p.appendChild(d.createTextNode('.'));
    var k=d.createElement('div');
    [['nie',t.nie],['tak',t.tak]].forEach(function(x){var b=d.createElement('button'); b.type='button'; b.setAttribute('data-z',x[0]); b.textContent=x[1];
      b.addEventListener('click',function(){zapisz(x[0]); baner.remove(); baner=null; if(x[0]==='tak') laduj(); else if(zaladowane) location.reload();}); k.appendChild(b);});
    baner.appendChild(p); baner.appendChild(k); d.body.appendChild(baner);
  }
  // Link „Cookie-Einstellungen” w stopce – zmiana decyzji w każdej chwili.
  function link(){
    var l=d.querySelector('footer a[href*="datenschutz"],footer a[href*="polityka-prywatnosci"],footer a[href*="privacy-policy"]');
    if(!l||!l.parentNode||!l.parentNode.parentNode) return;
    var li=d.getElementById('zgoda-link');
    if(!li){li=d.createElement('li'); li.id='zgoda-link'; var a=d.createElement('a'); a.href='#'; a.addEventListener('click',function(e){e.preventDefault(); pokaz();}); li.appendChild(a); l.parentNode.parentNode.appendChild(li);}
    li.firstChild.textContent=T[jez()].u;
  }
  function start(){
    link();
    new MutationObserver(function(){link(); if(baner) pokaz();}).observe(d.documentElement,{attributes:true,attributeFilter:['lang']});
    var z=czytaj();
    if(z==='tak') laduj(); else if(z!=='nie') pokaz();
  }
  if(d.readyState==='loading') d.addEventListener('DOMContentLoaded',start); else start();
})();
