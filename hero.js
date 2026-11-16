// Hero: na komputerze wideo startuje od razu; na telefonie najpierw statyczny kadr (szybki LCP), potem wideo się pojawia.
(function () {
  var v = document.getElementById('film');
  if (!v) return;
  var mobile = window.matchMedia('(max-width:640px)').matches;
  function start() {
    if (v.querySelector('source')) return;
    var s = document.createElement('source');
    s.src = mobile ? '/media/hero-m.mp4' : '/media/hero.mp4';
    s.type = 'video/mp4';
    v.appendChild(s);
    v.addEventListener('playing', function () { v.classList.add('on'); }, { once: true });
    v.muted = true;
    v.load();
    var p = v.play();
    if (p && p.catch) p.catch(function () {});
    v.addEventListener('canplay', function () { var q = v.play(); if (q && q.catch) q.catch(function () {}); }, { once: true });
    // Zabezpieczenie: jeśli wideo nie ruszy w ciągu 1,5 s, ponownie ładujemy i startujemy je,
    // a po 3 s pokazujemy kadr, żeby koń nie zostawał zamrożony.
    setTimeout(function () {
      if (!v.paused && v.readyState >= 3) return;
      v.load();
      var r = v.play(); if (r && r.catch) r.catch(function () {});
    }, 1500);
    setTimeout(function () { v.classList.add('on'); }, 3000);
    v.addEventListener('click', function () { if (v.paused) { var r = v.play(); if (r && r.catch) r.catch(function () {}); } });
  }
  if (!mobile) start();
  else if (document.readyState === 'complete') setTimeout(start, 300);
  else window.addEventListener('load', function () { setTimeout(start, 300); });
})();

// Plakaty filmów poniżej ekranu ładują się dopiero, gdy zbliżają się do widoku.
(function () {
  var vids = document.querySelectorAll('video[data-poster]');
  if (!vids.length) return;
  function set(v) { v.setAttribute('poster', v.getAttribute('data-poster')); v.removeAttribute('data-poster'); }
  if (!('IntersectionObserver' in window)) { vids.forEach(set); return; }
  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (e) {
      if (e.isIntersecting) {
        var v = e.target; set(v);
        if (v.hasAttribute('data-autoplay')) { var p = v.play(); if (p && p.catch) p.catch(function () {}); }
        io.unobserve(v);
      }
    });
  }, { rootMargin: '400px 0px' });
  vids.forEach(function (v) { io.observe(v); });
})();
