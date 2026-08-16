from pathlib import Path

TARGET = Path('MAXESS-RESULTS-10-GROOVE.html')
MARKER = '<!-- MAXESS-MASTER-BASELINE-PRESERVATION-10-10 -->'

if not TARGET.exists():
    raise SystemExit(f'Missing {TARGET}')

s = TARGET.read_text(encoding='utf-8')
if MARKER in s:
    print('MAXESS master preservation pass already present; nothing to do.')
    raise SystemExit(0)

# Repair the known invalid post-</html> append pattern by moving trailing
# artifacts back inside the document. Nothing is discarded.
idx = s.find('</html>')
if idx != -1:
    before = s[:idx]
    after = s[idx + len('</html>'):]
    body_close = before.rfind('</body>')
    if body_close != -1 and after.strip():
        before = before[:body_close] + after + '\n' + before[body_close:]
    s = before

s = s.replace('Your AI capability<br>\n<em>has a shape.</em>', 'Your MAXESS Result.<br>\n<em>See the pattern.</em>')
s = s.replace("You didn't just receive a number. You created a picture of how you currently think, direct, evaluate, iterate, and build with AI.", "This is your personal AI Mastery report — a visual picture of how you currently direct, evaluate, improve, and work with AI.")
s = s.replace('Explore Your Results <span aria-hidden="true">↓</span>', 'See My Pattern <span aria-hidden="true">↓</span>')
s = s.replace('Meet Naya <span aria-hidden="true">→</span>', 'Listen to Your Results <span aria-hidden="true">▶</span>')

cssjs = r'''
<!-- MAXESS-MASTER-BASELINE-PRESERVATION-10-10 -->
<style id="maxess-master-baseline-10-10">
/* FINAL MASTER PASS: preserve the working Groove conversion architecture; upgrade the report around it. */
#maxess-results-10{width:100vw!important;max-width:none!important;margin-left:calc(50% - 50vw)!important;margin-right:calc(50% - 50vw)!important;background:#030307!important;color:#fff!important;overflow:hidden!important}
#maxess-results-10 .mx-wide{width:100%!important;max-width:1760px!important;margin:0 auto!important}
#maxess-results-10 .mx-section{width:100%!important;padding-left:clamp(20px,4vw,86px)!important;padding-right:clamp(20px,4vw,86px)!important}
/* REPORT-FIRST HERO */
#maxess-results-10 .mx-hero{min-height:min(900px,96vh)!important;padding-top:clamp(48px,6vw,92px)!important;padding-bottom:clamp(44px,5vw,80px)!important;background:radial-gradient(circle at 50% 44%,rgba(116,68,216,.18),transparent 34%),linear-gradient(180deg,#09050f,#030307 72%,#020204)!important}
#maxess-results-10 .mx-hero-grid{width:min(1500px,100%)!important;display:grid!important;grid-template-columns:1fr minmax(360px,620px) 1fr!important;grid-template-areas:"copy orb side"!important;align-items:center!important;gap:clamp(28px,5vw,80px)!important;text-align:center!important}
#maxess-results-10 .mx-hero-grid>.mx-score-orb{grid-area:orb!important;order:0!important;width:min(600px,46vw)!important;min-width:330px!important;margin:0 auto!important}
#maxess-results-10 .mx-hero-grid>div:first-child{grid-area:copy!important;text-align:right!important}
#maxess-results-10 .mx-hero-grid>div:first-child .mx-copy{margin-left:auto}
#maxess-results-10 .mx-hero-grid>div:first-child .mx-hero-actions{justify-content:flex-end}
#maxess-results-10 .mx-proof{display:none!important}
#maxess-results-10 .mx-title{font-size:clamp(44px,5.5vw,82px)!important}
#maxess-results-10 .mx-copy{font-size:clamp(16px,1.35vw,19px)!important}
#maxess-results-10 .mx-score-orb{border:1px solid rgba(196,181,253,.42)!important;box-shadow:0 0 0 10px rgba(139,92,246,.03),inset 0 0 100px rgba(139,92,246,.3),0 40px 130px rgba(0,0,0,.7),0 0 130px rgba(139,92,246,.24)!important;animation:masterOrb 5s ease-in-out infinite!important}
@keyframes masterOrb{0%,100%{transform:scale(1);filter:brightness(1)}50%{transform:scale(1.025);filter:brightness(1.1)}}
/* The personal Naya report is a hero-adjacent chapter, not a footer widget. */
#maxess-results-10 #naya-report{padding-top:24px!important;padding-bottom:54px!important}
#maxess-results-10 #naya-report .mx-bridge-card{max-width:1250px!important;margin:0 auto!important;border-radius:34px!important;background:radial-gradient(ellipse 70% 100% at 50% 0,rgba(149,86,235,.22),transparent 65%),linear-gradient(145deg,rgba(255,255,255,.075),rgba(255,255,255,.018))!important;border:1px solid rgba(196,181,253,.2)!important;box-shadow:0 35px 100px rgba(0,0,0,.45)!important}
#maxess-results-10 #naya-report .mx-bridge-card h2{font-size:clamp(34px,4.8vw,66px)!important}
/* Kill the weak/intermediate salesy blocks in the report area. */
#maxess-results-10 .mx-insight{display:none!important}
/* Five dimensions = one premium gauge system. */
#maxess-results-10 .mx-dim-grid{display:grid!important;grid-template-columns:repeat(5,minmax(150px,1fr))!important;gap:14px!important;position:relative!important;padding:18px 0 12px!important}
#maxess-results-10 .mx-dim-grid::before{content:"";position:absolute;left:5%;right:5%;top:50%;height:1px;background:linear-gradient(90deg,transparent,rgba(139,92,246,.35),rgba(85,232,255,.28),rgba(139,92,246,.35),transparent);pointer-events:none}
#maxess-results-10 .mx-dim{aspect-ratio:auto!important;min-height:300px!important;border-radius:28px!important;padding:24px!important;display:flex!important;flex-direction:column!important;justify-content:center!important;text-align:left!important;align-items:stretch!important;background:linear-gradient(145deg,rgba(255,255,255,.07),rgba(255,255,255,.018))!important;border:1px solid rgba(255,255,255,.12)!important;box-shadow:inset 0 1px rgba(255,255,255,.14),0 25px 65px rgba(0,0,0,.4)!important}
#maxess-results-10 .mx-dim:hover{transform:translateY(-7px)!important;border-color:rgba(196,181,253,.4)!important}
#maxess-results-10 .mx-dim-head{grid-template-columns:34px 1fr auto!important;align-items:center!important}
#maxess-results-10 .mx-dim-head strong{font-size:30px!important}
#maxess-results-10 .mx-track{height:9px!important;margin:20px 0!important;background:rgba(255,255,255,.07)!important;box-shadow:inset 0 1px rgba(0,0,0,.5)!important}
#maxess-results-10 .mx-track span{background:linear-gradient(90deg,#6d39c9,#b99aff,#55e8ff)!important;box-shadow:0 0 18px rgba(139,92,246,.4)!important}
#maxess-results-10 .mx-dim p{font-size:13px!important;color:rgba(255,255,255,.62)!important}
#maxess-results-10 .mx-lever{margin-top:16px!important}
/* Naya masters become the bridge into the preserved conversion architecture. */
#maxess-results-10 .mx-naya-playground{margin-top:24px!important;padding-top:70px!important;padding-bottom:70px!important;border-top:1px solid rgba(255,255,255,.08)!important;background:radial-gradient(circle at 50% 50%,rgba(139,92,246,.08),transparent 58%)!important}
#maxess-results-10 .mx-naya-doors{grid-template-columns:repeat(3,minmax(0,1fr))!important;gap:20px!important}
#maxess-results-10 .mx-naya-door{min-height:300px!important;border-radius:30px!important;background:linear-gradient(145deg,rgba(255,255,255,.075),rgba(255,255,255,.018))!important;border:1px solid rgba(255,255,255,.14)!important;box-shadow:inset 0 1px rgba(255,255,255,.14),0 30px 90px rgba(0,0,0,.42)!important}
/* Preserve the existing video + conversion controls exactly as the lower conversion chapter. */
.ny-page-inner{width:100%!important;max-width:none!important}
.ny-theater{width:100%!important;padding-left:clamp(10px,3vw,48px)!important;padding-right:clamp(10px,3vw,48px)!important}
.ny-screen-frame{width:min(1600px,100%)!important}
.ny-primary-zone,.ny-secondary-grid,.ny-membership{width:100%!important;max-width:none!important}
.ny-secondary-grid{grid-template-columns:repeat(4,minmax(0,1fr))!important}
.ny-primary,.ny-secondary{font-family:Inter,ui-sans-serif,system-ui!important}
/* No pink utility copy. Keep the multicolor icon language. */
#maxess-results-10 .mx-eyebrow,#maxess-results-10 .mx-plan b,#maxess-results-10 .mx-growth-card b{color:rgba(255,255,255,.7)!important}
/* Print = beautiful report, not website chrome. */
@media print{
body{background:#fff!important;color:#111!important}
#maxess-results-10{width:100%!important;margin:0!important;background:#fff!important;color:#111!important}
#maxess-results-10 .mx-hero{min-height:auto!important;background:#fff!important;padding:30px 0!important}
#maxess-results-10 .mx-hero-grid{display:block!important;text-align:center!important}
#maxess-results-10 .mx-score-orb{width:260px!important;margin:0 auto 24px!important;box-shadow:none!important;border:1px solid #888!important;animation:none!important}
#maxess-results-10 .mx-hero-grid>div:first-child{text-align:center!important}
#maxess-results-10 .mx-hero-actions,#maxess-results-10 .mx-proof,.ny-theater,.ny-primary-zone,.ny-secondary-grid,.ny-membership,#maxess-results-10 .mx-naya-playground{display:none!important}
#maxess-results-10 .mx-section{padding:24px 0!important;break-inside:avoid}
#maxess-results-10 .mx-dim-grid{grid-template-columns:repeat(5,1fr)!important;gap:8px!important}
#maxess-results-10 .mx-dim{min-height:190px!important;padding:14px!important;background:#fff!important;color:#111!important;box-shadow:none!important;border:1px solid #bbb!important}
#maxess-results-10 .mx-dim p,#maxess-results-10 .mx-lever b,#maxess-results-10 .mx-section-head p{color:#333!important}
}
@media(max-width:1150px){#maxess-results-10 .mx-dim-grid{grid-template-columns:repeat(3,1fr)!important}#maxess-results-10 .mx-naya-doors{grid-template-columns:1fr 1fr!important}}
@media(max-width:900px){#maxess-results-10 .mx-hero-grid{grid-template-columns:1fr!important;grid-template-areas:"orb" "copy" "side"!important;max-width:760px!important}#maxess-results-10 .mx-hero-grid>div:first-child{text-align:center!important}#maxess-results-10 .mx-hero-grid>div:first-child .mx-copy{margin-left:auto}#maxess-results-10 .mx-hero-grid>div:first-child .mx-hero-actions{justify-content:center}#maxess-results-10 .mx-hero-grid>.mx-score-orb{width:min(500px,82vw)!important}#maxess-results-10 .mx-dim-grid{grid-template-columns:repeat(2,1fr)!important}#maxess-results-10 .mx-naya-doors{grid-template-columns:1fr!important}}
@media(max-width:560px){#maxess-results-10 .mx-section{padding-left:16px!important;padding-right:16px!important}#maxess-results-10 .mx-dim-grid{grid-template-columns:1fr!important}#maxess-results-10 .mx-dim{min-height:250px!important}.ny-secondary-grid{grid-template-columns:repeat(2,minmax(0,1fr))!important}}
@media(prefers-reduced-motion:reduce){#maxess-results-10 .mx-score-orb{animation:none!important}}
</style>
<script id="maxess-master-baseline-preservation-10-10">
(function(){
  'use strict';
  function boot(){
    var root=document.getElementById('maxess-results-10'); if(!root)return;
    var hero=root.querySelector('.mx-hero');
    var report=document.getElementById('naya-report');
    if(hero&&report) root.insertBefore(report,hero.nextSibling);
    var play=root.querySelector('.mx-naya-playground');
    var growth=document.getElementById('growth-scorecard');
    if(play&&growth) root.insertBefore(play,growth.nextSibling);
    var foundation=document.querySelector('.ny-page-inner');
    if(foundation){root.appendChild(foundation);foundation.setAttribute('data-maxess-preserved-conversion','true');}
    var nayaBtn=document.getElementById('mx-naya-listen');
    var heroListen=root.querySelector('.mx-hero-actions .mx-cta-ghost');
    if(heroListen&&nayaBtn) heroListen.onclick=function(e){e.preventDefault();nayaBtn.click();};
    root.querySelectorAll('.mx-bridge-card h2').forEach(function(h){if(/You've seen the pattern/i.test(h.textContent))h.innerHTML='Listen to your results.<br><em>Hear what your pattern means.</em>';});
  }
  if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',boot,{once:true});else setTimeout(boot,0);
})();
</script>
'''
body_close = s.rfind('</body>')
if body_close == -1:
    raise SystemExit('No </body> found')
s = s[:body_close] + cssjs + '\n' + s[body_close:]
TARGET.write_text(s, encoding='utf-8')
print(f'Patched {TARGET}: {TARGET.stat().st_size} bytes')
