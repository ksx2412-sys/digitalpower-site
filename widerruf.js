/* Widerrufsfunktion (§ 356a BGB), 23.11.2026.
   Wysyła odstąpienie przez ten sam Google Apps Script co formularz kontaktowy.
   Skrypt (nowa wersja z narzedzia/formularz_google_Code.gs) wysyła klientowi potwierdzenie z datą i godziną.
   Gdy wysłanie się nie uda, pokazuje gotowy e-mail z odstąpieniem. */
(function(){
 var URL_SKRYPTU='https://script.google.com/macros/s/AKfycbw7ceQCslGjrgpgRRAUH_XDOx5jErVlY-SXowUebrwzSE_SMR_nuyKiAo4kqkLcvyek/exec';
 var ZIEL='dpx369@gmail.com';
 var form=document.getElementById('widerruf'); if(!form) return;
 var info=document.getElementById('w-info');
 var TX={
  de:{wys:'Wird gesendet …',err:'Bitte Name, Vertrag und eine gültige E-Mail-Adresse angeben.',
      ok:'Ihr Widerruf ist am {z} bei uns eingegangen.',okm:'Die Eingangsbestätigung haben wir an {m} gesendet.',
      okr:'Die Eingangsbestätigung senden wir Ihnen unverzüglich per E-Mail an {m}.',
      fail:'Das Senden hat leider nicht geklappt. Bitte senden Sie Ihren Widerruf per E-Mail – der Text ist schon vorbereitet:',
      mailbtn:'E-Mail mit Widerruf öffnen',betreff:'Widerruf',
      text:'Hiermit widerrufe ich den Vertrag.\n\nName: {n}\nVertrag / Bestellung: {b}\nE-Mail für die Bestätigung: {m}\nDatum: {z}'},
  pl:{wys:'Wysyłanie …',err:'Podaj imię i nazwisko, umowę i poprawny adres e-mail.',
      ok:'Twoje odstąpienie dotarło do nas {z}.',okm:'Potwierdzenie wysłaliśmy na {m}.',
      okr:'Potwierdzenie wyślemy niezwłocznie e-mailem na {m}.',
      fail:'Niestety wysłanie się nie udało. Wyślij odstąpienie e-mailem – treść jest już przygotowana:',
      mailbtn:'Otwórz e-mail z odstąpieniem',betreff:'Odstąpienie od umowy (Widerruf)',
      text:'Niniejszym odstępuję od umowy.\n\nImię i nazwisko: {n}\nUmowa / zamówienie: {b}\nE-mail do potwierdzenia: {m}\nData: {z}'},
  en:{wys:'Sending …',err:'Please enter your name, the contract and a valid email address.',
      ok:'We received your withdrawal on {z}.',okm:'We have sent the acknowledgement to {m}.',
      okr:'We will send the acknowledgement to {m} by email without delay.',
      fail:'Sorry, sending did not work. Please send your withdrawal by email – the text is already prepared:',
      mailbtn:'Open email with withdrawal',betreff:'Withdrawal from contract (Widerruf)',
      text:'I hereby withdraw from the contract.\n\nName: {n}\nContract / order: {b}\nEmail for the acknowledgement: {m}\nDate: {z}'}
 };
 function L(){var l=document.documentElement.lang;return TX[l]?l:'de'}
 function f(s,o){return s.replace(/\{(\w)\}/g,function(_,k){return o[k]||''})}
 function teraz(){var d=new Date(),p=function(x){return(x<10?'0':'')+x};
  return p(d.getDate())+'.'+p(d.getMonth()+1)+'.'+d.getFullYear()+', '+p(d.getHours())+':'+p(d.getMinutes())}
 function pokaz(html,ok){info.className='winfo '+(ok?'ok':'blad');info.innerHTML=html}
 function esc(s){return String(s).replace(/[&<>"]/g,function(c){return{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]})}
 form.addEventListener('submit',function(e){
  e.preventDefault();
  var t=TX[L()];
  var n=form.name.value.trim(),b=form.bestellung.value.trim(),m=form.email.value.trim();
  if(!n||!b||!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(m)){pokaz(esc(t.err),false);return;}
  var btn=form.querySelector('[type=submit]'); if(btn.disabled) return; btn.disabled=true;
  pokaz(esc(t.wys),true);
  var z=teraz();
  var tresc=f(t.text,{n:n,b:b,m:m,z:z});
  var dane={typ:'widerruf',name:n,email:m,bestellung:b,sprache:L(),website:form.website.value,
            leistung:'WIDERRUF',message:'WIDERRUF (über digitalpower.art/widerruf.html)\n\n'+tresc};
  fetch(URL_SKRYPTU,{method:'POST',body:JSON.stringify(dane)})
  .then(function(r){return r.json()})
  .then(function(o){
    if(!o||!o.ok) throw new Error('blad');
    var zz=o.zeit||z;
    pokaz('<b>'+esc(f(t.ok,{z:zz}))+'</b><br>'+esc(f(o.bestaetigt?t.okm:t.okr,{m:m})),true);
    form.querySelectorAll('input').forEach(function(x){x.disabled=true});
  })
  .catch(function(){
    var href='mailto:'+ZIEL+'?subject='+encodeURIComponent(t.betreff)+'&body='+encodeURIComponent(tresc);
    pokaz(esc(t.fail)+'<br><a class="wbtn" style="margin-top:12px" href="'+href+'">'+esc(t.mailbtn)+'</a><br><span style="font-size:13px">'+ZIEL+'</span>',false);
    btn.disabled=false;
  });
 });
})();
