/* Poprawki 28.10.2026 (1/2): osobne pole na plik w formularzu kontaktowym – niezależne od kalkulatora */
(function(){
 var m=document.getElementById('f-msg'); if(!m||document.getElementById('f-file')) return;
 var pole=m.closest('.pole'); var d=document.createElement('div'); d.className='pole pelne';
 d.innerHTML='<label for="f-file" data-dp="plikpole">Datei</label><input id="f-file" name="datei" type="file" accept=".stl,.3mf,.jpg,.jpeg,.png,.pdf">';
 pole.parentNode.insertBefore(d,pole.nextSibling);
})();

/* Poprawki 15.10.2026: chowany przycisk Kontakt + własny przycisk wyboru pliku */
(function(){
 var p=document.getElementById('plywajacy'),y=window.scrollY||0;
 window.addEventListener('scroll',function(){var n=window.scrollY||0;if(p){if(n>y+6&&n>120)p.classList.add('schowany');else if(n<y-6||n<120)p.classList.remove('schowany')}y=n},{passive:true});
 var T={de:['Datei auswählen','Keine Datei ausgewählt'],pl:['Wybierz plik','Nie wybrano pliku'],en:['Choose file','No file chosen']};
 var inp=document.getElementById('f-file');if(!inp)return;
 var w=document.createElement('div');w.className='fpl-wrap';inp.parentNode.insertBefore(w,inp);
 var bt=document.createElement('span');bt.className='fpl-btn';var nm=document.createElement('span');nm.className='fpl-nazwa';
 w.appendChild(bt);w.appendChild(nm);w.appendChild(inp);
 function od(){var t=T[document.documentElement.lang]||T.de;bt.textContent=t[0];nm.textContent=(inp.files&&inp.files[0])?inp.files[0].name:t[1]}
 inp.addEventListener('change',od);new MutationObserver(od).observe(document.documentElement,{attributes:true,attributeFilter:['lang']});window.addEventListener('hashchange',od);document.addEventListener('click',function(){setTimeout(od,60)});od();
})();

/* Poprawki 28.10.2026 (2/2): formularz wysyła dane i plik (STL, 3MF, zdjęcie, PDF) prosto na dpx369@gmail.com
   przez Google Apps Script (konto dpx369). Zamiast otwierania programu pocztowego. */
(function(){
 var URL_SKRYPTU='https://script.google.com/macros/s/AKfycbw7ceQCslGjrgpgRRAUH_XDOx5jErVlY-SXowUebrwzSE_SMR_nuyKiAo4kqkLcvyek/exec';
 var MAX=25*1024*1024;
 var form=document.getElementById('formularz'); if(!form) return;
 var wplik=document.getElementById('w-plik');
 var TX={
  de:{fo_b:'Anfrage senden',
      fo_f:'Dateien bis 25 MB. Größere Dateien bitte als Link.',
      fo_z:'Ihre Angaben und die Datei werden verschlüsselt direkt an unser Postfach übermittelt.',
      w_up2:'3MF empfohlen, STL möglich, bis 25 MB (größer: Link im Formular)',
      mail:'E-Mail (für unsere Antwort)', plikpole:'Datei hochladen (STL, 3MF, Foto oder PDF, optional)', link:'Link zur Datei (optional, z. B. Google Drive, WeTransfer)',
      wys:'Wird gesendet …', ok:'Danke! Ihre Anfrage ist bei uns angekommen. Wir melden uns in Kürze.',
      err:'Bitte Name, Nachricht und E-Mail oder Telefon ausfüllen.',
      big:'Die Datei ist größer als 25 MB. Bitte laden Sie sie z. B. bei Google Drive oder WeTransfer hoch und fügen Sie den Link ein.',
      fail:'Senden hat nicht geklappt. Bitte schreiben Sie direkt an dpx369@gmail.com.',
      plik:'Datei (wird mitgeschickt): '},
  pl:{fo_b:'Wyślij zapytanie',
      fo_f:'Pliki do 25 MB. Większe prześlij jako link.',
      fo_z:'Twoje dane i plik trafiają szyfrowanym połączeniem prosto do naszej skrzynki.',
      w_up2:'Zalecamy 3MF, STL też przyjmujemy, do 25 MB (większe: link w formularzu)',
      mail:'E-mail (do odpowiedzi)', plikpole:'Dodaj plik (STL, 3MF, zdjęcie lub PDF, opcjonalnie)', link:'Link do pliku (opcjonalnie, np. Google Drive, WeTransfer)',
      wys:'Wysyłanie…', ok:'Dziękujemy! Zapytanie do nas dotarło. Odezwiemy się wkrótce.',
      err:'Uzupełnij imię, wiadomość oraz e-mail lub telefon.',
      big:'Plik ma ponad 25 MB. Wgraj go np. na Google Drive lub WeTransfer i wklej link.',
      fail:'Wysyłanie się nie udało. Napisz bezpośrednio na dpx369@gmail.com.',
      plik:'Plik (wysyłany razem z zapytaniem): '},
  en:{fo_b:'Send request',
      fo_f:'Files up to 25 MB. Please send larger files as a link.',
      fo_z:'Your details and the file are sent encrypted straight to our mailbox.',
      w_up2:'3MF recommended, STL accepted, up to 25 MB (larger: link in the form)',
      mail:'Email (for our reply)', plikpole:'Upload a file (STL, 3MF, photo or PDF, optional)', link:'Link to file (optional, e.g. Google Drive, WeTransfer)',
      wys:'Sending…', ok:'Thank you! Your request has reached us. We will get back to you shortly.',
      err:'Please fill in your name, message and email or phone.',
      big:'The file is larger than 25 MB. Please upload it e.g. to Google Drive or WeTransfer and paste the link.',
      fail:'Sending failed. Please write directly to dpx369@gmail.com.',
      plik:'File (sent with the request): '}
 };
 var STARE=['Datei (bitte an die E-Mail anhängen): ','Plik (dołączę do e-maila): ','File (I will attach it to the email): '];
 var L=function(){var l=(document.documentElement.lang||'de').slice(0,2);return TX[l]?l:'de'};
 var esc=function(t){return t.replace(/[&<>]/g,function(c){return{'&':'&amp;','<':'&lt;','>':'&gt;'}[c]}).replace(/3D/g,'<span class="r3d">3D</span>')};

 // Nowe pola: e-mail (do odpowiedzi), link do dużego pliku, pułapka na boty
 var telPole=document.getElementById('f-mail'); telPole=telPole&&telPole.closest('.pole');
 var mailPole=document.createElement('div');mailPole.className='pole';
 mailPole.innerHTML='<label for="f-email" data-dp="mail"></label><input id="f-email" name="email" type="email" autocomplete="email" inputmode="email">';
 if(telPole) telPole.parentNode.insertBefore(mailPole,telPole.nextSibling);
 var msgPole=document.getElementById('f-msg'); msgPole=msgPole&&msgPole.closest('.pole');
 var linkPole=document.createElement('div');linkPole.className='pole pelne';
 linkPole.innerHTML='<label for="f-link" data-dp="link"></label><input id="f-link" name="link" type="url" inputmode="url" placeholder="https://">';
 if(msgPole) msgPole.parentNode.insertBefore(linkPole,msgPole.nextSibling);
 var hp=document.createElement('input');hp.type='text';hp.name='website';hp.tabIndex=-1;hp.autocomplete='off';hp.setAttribute('aria-hidden','true');
 hp.style.cssText='position:absolute;left:-9999px;width:1px;height:1px;opacity:0';form.appendChild(hp);

 var zajete=false;
 function teksty(){
  if(zajete) return; zajete=true;
  var t=TX[L()];
  ['fo_b','fo_f','fo_z','w_up2'].forEach(function(k){document.querySelectorAll('[data-t="'+k+'"]').forEach(function(e){if(e.textContent!==t[k].replace(/<[^>]*>/g,'')) e.innerHTML=esc(t[k]);});});
  document.querySelectorAll('[data-dp]').forEach(function(e){e.textContent=t[e.getAttribute('data-dp')];});
  var m=document.getElementById('f-msg'); if(m) STARE.forEach(function(s){ if(m.value.indexOf(s)>=0) m.value=m.value.split('\n').filter(function(z){return z.indexOf(s)<0}).join('\n'); });
  setTimeout(function(){zajete=false},0);
 }
 teksty();
 new MutationObserver(function(){setTimeout(teksty,0)}).observe(document.documentElement,{attributes:true,attributeFilter:['lang']});
 document.querySelectorAll('[data-t="fo_b"],[data-t="fo_f"],[data-t="fo_z"],[data-t="w_up2"]').forEach(function(e){new MutationObserver(function(){setTimeout(teksty,0)}).observe(e,{childList:true,characterData:true,subtree:true});});
 // Kalkulator → formularz: bez ceny, wagi i czasu; plik z kalkulatora trafia do pola w formularzu
 var CENA=/\s*(Richtpreis|Cena orientacyjna|Guide price)[^()]*\([^)]*\)\.?/g;
 var _km=window.__kalkMsg; if(_km) window.__kalkMsg=function(){return String(_km()||'').replace(CENA,'').trim();};
 function bezCeny(){var m=document.getElementById('f-msg'); if(m&&CENA.test(m.value)){CENA.lastIndex=0;m.value=m.value.replace(CENA,'');} CENA.lastIndex=0;}
 function przeniesPlik(){var fp=document.getElementById('f-file'); if(!fp||!wplik||!wplik.files||!wplik.files[0]) return;
  try{var dt=new DataTransfer();dt.items.add(wplik.files[0]);fp.files=dt.files;fp.dispatchEvent(new Event('change'));}catch(_){}}
 var wb=document.getElementById('w-wyslij'); if(wb) wb.addEventListener('click',function(){setTimeout(function(){bezCeny();przeniesPlik();teksty();},30)});

 function base64(file){return new Promise(function(ok,zle){var r=new FileReader();r.onload=function(){ok(String(r.result).split(',')[1]||'')};r.onerror=zle;r.readAsDataURL(file)});}
 function info(tekst,sukces){var k=document.getElementById('komunikat');if(!k)return;k.textContent=tekst;k.classList.toggle('sukces',!!sukces);}

 // Przechwycenie wysyłki (faza capture: stary handler z mailto nie zostaje uruchomiony)
 document.addEventListener('submit',function(e){
  if(e.target!==form) return;
  e.preventDefault(); e.stopPropagation();
  var t=TX[L()];
  var v=function(id){var x=document.getElementById(id);return x?x.value.trim():''};
  bezCeny();
  var imie=v('f-name'),tel=v('f-mail'),mail=v('f-email'),msg=v('f-msg'),link=v('f-link');
  if(!imie||!msg||(!mail&&!tel)){info(t.err,false);return;}
  var fp=document.getElementById('f-file');
  var plik=(fp&&fp.files&&fp.files[0])||null;
  if(plik&&plik.size>MAX&&!link){info(t.big,false);document.getElementById('f-link').focus();return;}
  var usl=[].map.call(form.querySelectorAll('input[name=leistung]:checked'),function(x){return x.value});
  var btn=form.querySelector('[type=submit]'); if(btn&&btn.disabled) return; if(btn) btn.disabled=true;
  info(t.wys,false);
  var dane={name:imie,email:mail,telefon:tel,leistung:usl.join(', '),message:msg,link:link,sprache:L(),website:hp.value};
  (plik&&plik.size<=MAX?base64(plik).then(function(b){dane.datei={name:plik.name,inhalt:b}}):Promise.resolve())
  .then(function(){return fetch(URL_SKRYPTU,{method:'POST',body:JSON.stringify(dane)})})
  .then(function(r){return r.json()})
  .then(function(o){
    if(!o||!o.ok) throw new Error(o&&o.fehler||'blad');
    info(t.ok,true);
    ['f-msg','f-link'].forEach(function(id){var x=document.getElementById(id);if(x)x.value=''});
    if(fp){fp.value='';fp.dispatchEvent(new Event('change'));}
  })
  .catch(function(){info(t.fail,false);})
  .then(function(){if(btn)btn.disabled=false;});
 },true);
})();
