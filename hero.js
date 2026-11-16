// Hero: na telefonie (do 640 px) wideo się nie ładuje, pokazuje się statyczny kadr.
(function () {
  var v = document.getElementById('film');
  if (!v || !window.matchMedia('(min-width:641px)').matches) return;
  if (v.querySelector('source')) return;
  var s = document.createElement('source');
  s.src = '/media/hero.mp4';
  s.type = 'video/mp4';
  v.appendChild(s);
  v.load();
})();
