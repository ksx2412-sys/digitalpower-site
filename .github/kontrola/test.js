// Cotygodniowa kontrola digitalpower.art – jeśli coś nie działa, test kończy się błędem i GitHub wysyła e-mail.
const { chromium } = require('playwright');
const BAZA = process.env.BAZA || 'https://digitalpower.art';
const STRONY = ['/', '/leistungen/', '/3d-druck/', '/drohnenaufnahmen/', '/digital-marketing/', '/kontakt/',
  '/pl/', '/pl/oferta/', '/pl/druk-3d/', '/pl/zdjecia-z-drona/', '/pl/marketing-cyfrowy/', '/pl/kontakt/',
  '/en/', '/en/services/', '/en/3d-printing/', '/en/drone-photography/', '/en/digital-marketing/', '/en/contact/',
  '/impressum.html', '/datenschutz.html', '/ki-hinweis.html'];
const KARTY = { '/leistungen/': ['/3d-druck/', '/drohnenaufnahmen/', '/digital-marketing/'],
  '/pl/oferta/': ['/pl/druk-3d/', '/pl/zdjecia-z-drona/', '/pl/marketing-cyfrowy/'],
  '/en/services/': ['/en/3d-printing/', '/en/drone-photography/', '/en/digital-marketing/'] };
const bledy = []; const zle = (m) => { bledy.push(m); console.log('❌ ' + m); };
(async () => {
  const b = await chromium.launch();
  for (const vp of [{ width: 390, height: 844, n: 'telefon' }, { width: 1366, height: 900, n: 'komputer' }]) {
    const ctx = await b.newContext({ viewport: { width: vp.width, height: vp.height } });
    const linki = new Set();
    for (const s of STRONY) {
      const p = await ctx.newPage(); const js = [];
      p.on('pageerror', e => js.push(e.message));
      const r = await p.goto(BAZA + s, { waitUntil: 'domcontentloaded', timeout: 30000 }).catch(e => null);
      if (!r || r.status() !== 200) { zle(`[${vp.n}] ${s} nie otwiera się (kod ${r ? r.status() : 'brak odpowiedzi'})`); await p.close(); continue; }
      await p.waitForTimeout(800);
      const widoczny = await p.evaluate(() => [...document.querySelectorAll('section,header,main')].some(e => !e.hidden && e.offsetHeight > 100));
      if (!widoczny) zle(`[${vp.n}] ${s} jest pusta`);
      if (js.length) zle(`[${vp.n}] ${s} błąd skryptu: ${js[0]}`);
      (await p.evaluate(() => [...document.querySelectorAll('a[href]')].map(a => a.href))).forEach(h => { if (h.startsWith(new URL(BAZA).origin)) linki.add(h.split('#')[0]); });
      await p.close();
    }
    for (const [od, cele] of Object.entries(KARTY)) for (let i = 0; i < cele.length; i++) {
      for (const gdzie of ['.kadr', '.karta-link']) {
        const p = await ctx.newPage(); await p.goto(BAZA + od); await p.waitForTimeout(800);
        const k = p.locator('#angebot .karta').nth(i).locator(gdzie);
        await k.scrollIntoViewIfNeeded().catch(() => {}); await k.click({ force: true }).catch(e => zle(`[${vp.n}] ${od} karta ${i + 1}: nie da się kliknąć`));
        await p.waitForTimeout(800);
        if (new URL(p.url()).pathname !== cele[i]) zle(`[${vp.n}] ${od}: klik w kartę ${i + 1} (${gdzie === '.kadr' ? 'zdjęcie' : 'link'}) prowadzi do ${new URL(p.url()).pathname} zamiast ${cele[i]}`);
        await p.close();
      }
    }
    for (const h of linki) {
      const r = await ctx.request.get(h).catch(() => null);
      if (!r || r.status() >= 400) zle(`[${vp.n}] martwy link: ${h} (kod ${r ? r.status() : 'brak'})`);
    }
    await ctx.close();
  }
  await b.close();
  if (bledy.length) { console.log(`\nZnaleziono problemów: ${bledy.length}`); process.exit(1); }
  console.log('✅ Wszystko działa');
})();
