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
