// Hero: najpierw statyczny kadr (szybki LCP), potem po załadowaniu strony wideo płynnie się pojawia.
(function () {
  var v = document.getElementById('film');
  if (!v) return;
  function start() {
    if (v.querySelector('source')) return;
    var s = document.createElement('source');
    s.src = '/media/hero.mp4';
    s.type = 'video/mp4';
    v.appendChild(s);
    v.addEventListener('playing', function () { v.classList.add('on'); }, { once: true });
    v.load();
  }
  if (document.readyState === 'complete') setTimeout(start, 300);
  else window.addEventListener('load', function () { setTimeout(start, 300); });
})();
