// Hero: najpierw statyczny kadr (szybki LCP), potem po załadowaniu strony wideo płynnie się pojawia.
(function () {
  var v = document.getElementById('film');
  if (!v) return;
  function start() {
    if (v.querySelector('source')) return;
    var s = document.createElement('source');
    s.src = window.matchMedia('(max-width:640px)').matches ? '/media/hero-m.mp4' : '/media/hero.mp4';
    s.type = 'video/mp4';
    v.appendChild(s);
    v.addEventListener('playing', function () { v.classList.add('on'); }, { once: true });
    v.load();
  }
  if (document.readyState === 'complete') setTimeout(start, 300);
  else window.addEventListener('load', function () { setTimeout(start, 300); });
})();

// Plakaty filmów poniżej ekranu ładują się dopiero, gdy zbliżają się do widoku.
(function () {
  var vids = document.querySelectorAll('video[data-poster]');
  if (!vids.length) return;
  function set(v) { v.setAttribute('poster', v.getAttribute('data-poster')); v.removeAttribute('data-poster'); }
  if (!('IntersectionObserver' in window)) { vids.forEach(set); return; }
  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (e) { if (e.isIntersecting) { var v = e.target; set(v); if (v.hasAttribute('data-autoplay')) { v.play().catch(function () {}); } io.unobserve(v); } });
  }, { rootMargin: '400px 0px' });
  vids.forEach(function (v) { io.observe(v); });
})();
