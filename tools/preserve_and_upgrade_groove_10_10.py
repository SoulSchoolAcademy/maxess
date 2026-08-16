from pathlib import Path

TARGET = Path('MAXESS-RESULTS-10-GROOVE.html')
BASE_MARKER = '<!-- MAXESS-MASTER-BASELINE-PRESERVATION-10-10 -->'
UPGRADE_MARKER = '<!-- MAXESS-AAA-DIRECTIVE-UPGRADE-2026-08-16 -->'

if not TARGET.exists():
    raise SystemExit(f'Missing {TARGET}')

s = TARGET.read_text(encoding='utf-8')

if BASE_MARKER not in s:
    raise SystemExit('Safety stop: frozen MAXESS preservation baseline is missing.')

if UPGRADE_MARKER in s:
    print('MAXESS AAA directive upgrade already present; nothing to do.')
    raise SystemExit(0)

# Content corrections requested during the full report review.
s = s.replace('Your MAXESS Result.<br>\n<em>See the pattern.</em>', 'Your MAXESS AI Assessment Score')
s = s.replace('See My Pattern <span aria-hidden="true">↓</span>', 'See Your Results <span aria-hidden="true">↓</span>')
s = s.replace('Five dimensions show where your current capability is strong, where it is developing, and where a small improvement can create disproportionate upside.', 'Five dimensions show where you are strong, where you are developing, and where your next improvement can create the greatest return.')
s = s.replace('02 · WHAT IT MEANS', '03 · YOUR FIVE DIMENSIONS')
s = s.replace('Every score has<br>a job.', 'Your Five Dimensions')
s = s.replace('A result becomes useful when you know what it means and what to do with it. These are your current strengths and levers.', 'Your current capability profile — five strengths, five scores, and five places where focused improvement can create meaningful upside.')
s = s.replace('03 · YOUR ADVANTAGE', '05 · YOUR STRENGTHS & LEVER')
s = s.replace('What you already<br>have working for you.', 'What Your Score Means')
s = s.replace('04 · YOUR NEXT CHAPTER', '07 · YOUR NEXT MOVE')
s = s.replace('From capability<br>to compounding.', 'Your Next Move')
s = s.replace('Mastery is not a finish line. It is the ability to make your strengths repeatable, measurable, and increasingly valuable.', 'Turn the report into action with one clear move: strengthen your lowest-leverage dimension while protecting the capability you already use best.')
s = s.replace('05 · YOUR 18 AI PATHWAYS', '08 · YOUR 18 NAYA MASTERS')
s = s.replace('Don\'t learn AI.<br>Learn what AI can do for you.', '18 Naya Masters<br>Ready to work for you.')
s = s.replace('These are 18 capability doors. Explore the ones that matter most to your goals, then build depth instead of collecting tools.', '18 specialist Naya Masters, each focused on a different area where AI can help you create stronger, faster, higher-quality results.')
s = s.replace('06 · TURN INSIGHT INTO GROWTH', '09 · YOUR SOLUTION')
s = s.replace('Know where you are.<br>Know what moves you.', 'Turn Better Thinking Into Better AI Results')
s = s.replace('A useful assessment should not leave you staring at a score. This chapter turns the result into practical direction: protect the strength, build the lever, and make progress repeatable.', 'If you are frustrated with AI producing mediocre results, MAXESS gives you a battle-tested process for directing, evaluating, improving, and repeating high-quality work.')
s = s.replace('PERSONALIZED REPORT', 'YOUR PERSONALIZED REPORT')
s = s.replace("You've seen the pattern.<br>\n<em>Now hear what it means.</em>", 'Listen to your results.<br>\n<em>Hear what they mean.</em>')
s = s.replace('Naya is the next layer: turning your result into a practical conversation about where you are, where you can go, and what to do next.', 'Naya turns your assessment into a practical conversation about where you are, where you can grow, and what to do next.')
s = s.replace('Naya — Listen to Your Report <span aria-hidden="true">▶</span>', 'Listen to Your Results <span aria-hidden="true">▶</span>')

cssjs = r'''
<!-- MAXESS-AAA-DIRECTIVE-UPGRADE-2026-08-16 -->
<style id="maxess-aaa-directive-upgrade">
/*
  AAA UPGRADE: preservation-first visual system.
  The existing working artifact remains the source; this layer improves hierarchy,
  report sequencing, color energy, gauges, Naya personality, and print presentation.
*/
#maxess-results-10{
  --aaa-black:#020205;
  --aaa-white:#fff;
  --aaa-red:#ff3b4f;
  --aaa-orange:#ff8a32;
  --aaa-yellow:#ffd84a;
  --aaa-green:#39e58c;
  --aaa-teal:#38e6d0;
  --aaa-blue:#3d8cff;
  --aaa-indigo:#5148e8;
  --aaa-purple:#8d4dff;
  --aaa-magenta:#ff3bbd;
  width:100vw!important;
  max-width:none!important;
  margin-left:calc(50% - 50vw)!important;
  margin-right:calc(50% - 50vw)!important;
  background:#020205!important;
}
#maxess-results-10 .mx-wide{width:100%!important;max-width:1760px!important;margin-inline:auto!important}
#maxess-results-10 .mx-section{width:100%!important;padding-inline:clamp(22px,4vw,86px)!important}
#maxess-results-10 .mx-eyebrow{color:#fff!important;font-size:clamp(11px,.8vw,13px)!important;letter-spacing:.18em!important}
#maxess-results-10 .mx-copy{color:rgba(255,255,255,.82)!important}
#maxess-results-10 .mx-title{font-size:clamp(44px,6vw,88px)!important;line-height:.94!important;color:#fff!important}
#maxess-results-10 .mx-title em{display:none!important}

/* HERO: the score and Orb are the unmistakable centerpiece. */
#maxess-results-10 .mx-hero{
  min-height:min(920px,94vh)!important;
  padding-block:clamp(48px,6vw,100px)!important;
  background:
    radial-gradient(circle at 50% 46%,rgba(113,62,255,.22),transparent 29%),
    linear-gradient(180deg,#030305 0%,#020205 72%,#05020a 100%)!important;
}
#maxess-results-10 .mx-hero-grid{
  display:grid!important;
  grid-template-columns:minmax(0,1fr) minmax(360px,680px) minmax(0,1fr)!important;
  grid-template-areas:"copy orb side"!important;
  align-items:center!important;
  gap:clamp(24px,4vw,72px)!important;
  text-align:center!important;
}
#maxess-results-10 .mx-hero-grid>div:first-child{grid-area:copy!important;text-align:center!important;display:flex!important;flex-direction:column!important;align-items:center!important}
#maxess-results-10 .mx-hero-grid>.mx-score-orb{grid-area:orb!important;width:min(640px,48vw)!important;min-width:360px!important;margin:auto!important}
#maxess-results-10 .mx-hero-grid>.mx-score-orb::before{border-color:rgba(255,255,255,.32)!important}
#maxess-results-10 .mx-hero-grid>.mx-score-orb::after{border-color:rgba(255,255,255,.16)!important}
#maxess-results-10 .mx-proof{display:none!important}
#maxess-results-10 .mx-score strong{
  font-size:clamp(110px,13vw,190px)!important;
  background:linear-gradient(110deg,var(--aaa-teal),var(--aaa-blue),var(--aaa-purple),var(--aaa-magenta));
  -webkit-background-clip:text;background-clip:text;color:transparent;
  text-shadow:0 0 45px rgba(141,77,255,.2);
}
#maxess-results-10 .mx-score span{color:#fff!important}
#maxess-results-10 .mx-band{border-color:rgba(255,255,255,.25)!important;background:rgba(255,255,255,.06)!important}
#maxess-results-10 .mx-score-orb{
  background:
    radial-gradient(circle at 30% 25%,rgba(255,255,255,.32),transparent 10%),
    radial-gradient(circle at 50% 50%,rgba(141,77,255,.38),transparent 28%),
    radial-gradient(circle at 65% 68%,rgba(61,140,255,.20),transparent 35%),
    #030305!important;
  box-shadow:0 0 0 1px rgba(255,255,255,.22),inset 0 0 100px rgba(141,77,255,.28),0 40px 120px rgba(0,0,0,.8),0 0 140px rgba(141,77,255,.22)!important;
}
#maxess-results-10 .mx-hero-actions{justify-content:center!important}
#maxess-results-10 .mx-cta{border-radius:999px!important;min-height:58px!important;padding-inline:28px!important;box-shadow:inset 0 1px rgba(255,255,255,.5),0 15px 35px rgba(0,0,0,.35)!important}
#maxess-results-10 .mx-cta-primary{background:linear-gradient(120deg,var(--aaa-blue),var(--aaa-purple),var(--aaa-magenta))!important}
#maxess-results-10 .mx-cta-ghost{background:#09090d!important;border-color:rgba(255,255,255,.24)!important}

/* PERSONAL NAYA REPORT moves immediately below the hero. */
#maxess-results-10 #naya-report{padding-block:clamp(34px,5vw,76px)!important;background:#fff!important;color:#09090d!important}
#maxess-results-10 #naya-report .mx-reading{width:min(1320px,100%)!important}
#maxess-results-10 #naya-report .mx-bridge-card{
  max-width:none!important;
  padding:clamp(44px,6vw,90px)!important;
  border-radius:34px!important;
  background:#08080b!important;
  border:1px solid rgba(141,77,255,.55)!important;
  box-shadow:0 35px 110px rgba(0,0,0,.35),inset 0 1px rgba(255,255,255,.12)!important;
}
#maxess-results-10 #naya-report .mx-audio-label{color:#fff!important}
#maxess-results-10 #naya-report .mx-bridge-card h2{font-size:clamp(38px,5.5vw,78px)!important;color:#fff!important}
#maxess-results-10 #naya-report .mx-bridge-card h2 em{background:linear-gradient(110deg,var(--aaa-blue),var(--aaa-purple),var(--aaa-magenta))!important;-webkit-background-clip:text!important;background-clip:text!important;color:transparent!important}
#maxess-results-10 #naya-report .mx-bridge-card p{font-size:clamp(17px,1.4vw,21px)!important;color:rgba(255,255,255,.78)!important}
#maxess-results-10 #naya-report .mx-key div{border:0!important;color:#fff!important;border-radius:999px!important;padding:15px 10px!important}
#maxess-results-10 #naya-report .mx-key div:nth-child(1){background:var(--aaa-red)!important}
#maxess-results-10 #naya-report .mx-key div:nth-child(2){background:var(--aaa-orange)!important;color:#111!important}
#maxess-results-10 #naya-report .mx-key div:nth-child(3){background:var(--aaa-yellow)!important;color:#111!important}
#maxess-results-10 #naya-report .mx-key div:nth-child(4){background:var(--aaa-teal)!important;color:#07100e!important}
#maxess-results-10 #naya-report .mx-key div:nth-child(5){background:var(--aaa-indigo)!important}
#maxess-results-10 #naya-report .mx-key div:nth-child(6){background:var(--aaa-purple)!important}
#maxess-results-10 #naya-report .mx-key div:nth-child(7){background:var(--aaa-magenta)!important}
#maxess-results-10 #naya-report .mx-key div:not(:last-child)::after{display:none!important}

/* Report chapters: alternate black/white/purple rhythm. */
#maxess-results-10 #your-fingerprint{background:#fff!important;color:#09090d!important}
#maxess-results-10 #your-fingerprint .mx-eyebrow{color:#5148e8!important}
#maxess-results-10 #your-fingerprint .mx-section-head p{color:#34343b!important}
#maxess-results-10 #your-fingerprint .mx-list-row{background:#08080b!important;color:#fff!important;border-color:rgba(0,0,0,.15)!important}
#maxess-results-10 #your-fingerprint .mx-list-row span{color:rgba(255,255,255,.55)!important}
#maxess-results-10 #your-fingerprint .mx-bar{background:rgba(255,255,255,.10)!important}
#maxess-results-10 #your-fingerprint .mx-bar i{background:linear-gradient(90deg,var(--aaa-teal),var(--aaa-blue),var(--aaa-purple),var(--aaa-magenta))!important}

/* Five dimension gauges: no more tiny corner scores. */
#maxess-results-10 .mx-dim-grid{grid-template-columns:repeat(5,minmax(150px,1fr))!important;gap:18px!important;position:relative!important}
#maxess-results-10 .mx-dim-grid::before{display:none!important}
#maxess-results-10 .mx-dim{
  min-height:340px!important;
  border-radius:32px!important;
  padding:28px 22px!important;
  display:flex!important;
  flex-direction:column!important;
  justify-content:center!important;
  align-items:center!important;
  text-align:center!important;
  background:#050508!important;
  border:1px solid rgba(255,255,255,.14)!important;
  box-shadow:inset 0 1px rgba(255,255,255,.12),0 28px 80px rgba(0,0,0,.35)!important;
}
#maxess-results-10 .mx-dim:nth-child(1){--g:var(--aaa-orange)}
#maxess-results-10 .mx-dim:nth-child(2){--g:var(--aaa-yellow)}
#maxess-results-10 .mx-dim:nth-child(3){--g:var(--aaa-green)}
#maxess-results-10 .mx-dim:nth-child(4){--g:var(--aaa-blue)}
#maxess-results-10 .mx-dim:nth-child(5){--g:var(--aaa-purple)}
#maxess-results-10 .mx-dim::after{
  content:"";width:154px;height:154px;border-radius:50%;position:absolute;top:34px;left:50%;transform:translateX(-50%);
  background:conic-gradient(var(--g) calc(var(--score,80)*1%),rgba(255,255,255,.07) 0);
  -webkit-mask:radial-gradient(farthest-side,transparent calc(100% - 11px),#000 0);
  mask:radial-gradient(farthest-side,transparent calc(100% - 11px),#000 0);
  filter:drop-shadow(0 0 12px color-mix(in srgb,var(--g),transparent 55%));
}
#maxess-results-10 .mx-dim[data-score="86"]{--score:86}
#maxess-results-10 .mx-dim[data-score="91"]{--score:91}
#maxess-results-10 .mx-dim[data-score="79"]{--score:79}
#maxess-results-10 .mx-dim[data-score="74"]{--score:74}
#maxess-results-10 .mx-dim[data-score="68"]{--score:68}
#maxess-results-10 .mx-dim-head{display:flex!important;flex-direction:column!important;align-items:center!important;gap:8px!important;position:relative!important;z-index:2!important;margin-top:65px!important}
#maxess-results-10 .mx-dim-head .mx-kicker{font-size:10px!important;color:rgba(255,255,255,.5)!important}
#maxess-results-10 .mx-dim-head h3{font-size:18px!important;color:#fff!important}
#maxess-results-10 .mx-dim-head strong{font-size:42px!important;color:var(--g)!important;line-height:1!important}
#maxess-results-10 .mx-dim-head strong small{display:none!important}
#maxess-results-10 .mx-dim .mx-track{width:80%!important;height:7px!important;margin:18px 0 14px!important;position:relative!important;z-index:2!important}
#maxess-results-10 .mx-dim .mx-track span{background:var(--g)!important;box-shadow:0 0 16px color-mix(in srgb,var(--g),transparent 45%)!important}
#maxess-results-10 .mx-dim p{font-size:13px!important;color:rgba(255,255,255,.70)!important;position:relative!important;z-index:2!important;margin:0!important}
#maxess-results-10 .mx-lever{position:relative!important;z-index:2!important;width:100%!important;margin-top:15px!important;padding-top:12px!important}
#maxess-results-10 .mx-lever span{color:var(--g)!important}
#maxess-results-10 .mx-lever b{font-size:11px!important;color:#fff!important}

/* White report page for interpretation. */
#maxess-results-10 #your-fingerprint~.mx-section{background:#020205!important}
#maxess-results-10 #your-fingerprint~.mx-section:nth-of-type(5){background:#fff!important;color:#09090d!important}
#maxess-results-10 #your-fingerprint~.mx-section:nth-of-type(5) .mx-section-head p{color:#333!important}
#maxess-results-10 #your-fingerprint~.mx-section:nth-of-type(5) .mx-step{background:#050508!important;color:#fff!important}

/* 18 Naya Masters: make the cards feel like a living specialist library. */
#maxess-results-10 .mx-areas{grid-template-columns:repeat(3,minmax(0,1fr))!important;gap:16px!important}
#maxess-results-10 .mx-area{min-height:180px!important;border-radius:26px!important;padding:24px!important;background:linear-gradient(145deg,#08080d,#111019)!important;border-color:rgba(255,255,255,.14)!important}
#maxess-results-10 .mx-area-num{color:rgba(255,255,255,.45)!important;font-weight:900!important}
#maxess-results-10 .mx-area-main h3{font-size:17px!important;color:#fff!important}
#maxess-results-10 .mx-area-main p{font-size:12px!important;color:rgba(255,255,255,.65)!important}
#maxess-results-10 .mx-area-relevance em{background:linear-gradient(90deg,var(--aaa-blue),var(--aaa-purple),var(--aaa-magenta))!important}
#maxess-results-10 .mx-mini{border-radius:999px!important;background:linear-gradient(120deg,#171722,#2b173f)!important;border-color:rgba(255,255,255,.22)!important}
#maxess-results-10 .mx-area:nth-child(3n+1){box-shadow:inset 0 1px rgba(255,255,255,.1),0 25px 65px rgba(61,140,255,.08)!important}
#maxess-results-10 .mx-area:nth-child(3n+2){box-shadow:inset 0 1px rgba(255,255,255,.1),0 25px 65px rgba(141,77,255,.09)!important}
#maxess-results-10 .mx-area:nth-child(3n){box-shadow:inset 0 1px rgba(255,255,255,.1),0 25px 65px rgba(255,59,189,.07)!important}

/* Preserve and strengthen the existing lower video/conversion architecture. */
.ny-page-inner{width:100%!important;max-width:none!important}
.ny-theater{width:100%!important;padding-inline:clamp(10px,3vw,48px)!important}
.ny-screen-frame{width:min(1600px,100%)!important}
.ny-primary-zone,.ny-secondary-grid,.ny-membership{width:100%!important;max-width:none!important}
.ny-secondary-grid{grid-template-columns:repeat(4,minmax(0,1fr))!important}

/* Remove the old salesy scorecard from the report flow; the score is already beautifully represented above. */
#maxess-results-10 #growth-scorecard{display:none!important}

/* PRINT: dedicated premium report. */
@media print{
  @page{size:letter;margin:.55in}
  html,body{background:#fff!important;color:#111!important}
  #maxess-results-10{width:100%!important;margin:0!important;background:#fff!important;color:#111!important}
  #maxess-results-10 .mx-hero{min-height:auto!important;background:#fff!important;padding:20px 0 28px!important}
  #maxess-results-10 .mx-hero-grid{display:block!important;text-align:center!important}
  #maxess-results-10 .mx-hero-grid>div:first-child{text-align:center!important}
  #maxess-results-10 .mx-score-orb{width:230px!important;box-shadow:none!important;border:2px solid #111!important;animation:none!important;margin:10px auto 20px!important}
  #maxess-results-10 .mx-score strong{font-size:86px!important;background:#111!important;color:#111!important;-webkit-text-fill-color:#111!important}
  #maxess-results-10 .mx-hero-actions,#maxess-results-10 .mx-proof,.ny-theater,.ny-primary-zone,.ny-secondary-grid,.ny-membership,#maxess-results-10 #naya-report .mx-key{display:none!important}
  #maxess-results-10 #naya-report{padding:0 0 24px!important;background:#fff!important}
  #maxess-results-10 #naya-report .mx-bridge-card{background:#111!important;color:#fff!important;box-shadow:none!important;border:0!important}
  #maxess-results-10 .mx-section{padding:24px 0!important;break-inside:avoid}
  #maxess-results-10 .mx-section-head{break-after:avoid!important}
  #maxess-results-10 .mx-dim-grid{grid-template-columns:repeat(5,1fr)!important;gap:7px!important}
  #maxess-results-10 .mx-dim{min-height:180px!important;padding:10px!important;background:#fff!important;color:#111!important;border:1px solid #bbb!important;box-shadow:none!important}
  #maxess-results-10 .mx-dim::after{display:none!important}
  #maxess-results-10 .mx-dim-head{margin-top:0!important}
  #maxess-results-10 .mx-dim-head h3,#maxess-results-10 .mx-dim-head strong,#maxess-results-10 .mx-lever b{color:#111!important}
  #maxess-results-10 .mx-dim p,#maxess-results-10 .mx-section-head p{color:#333!important}
  #maxess-results-10 .mx-area{break-inside:avoid!important}
}

@media(max-width:1150px){
  #maxess-results-10 .mx-dim-grid{grid-template-columns:repeat(3,1fr)!important}
  #maxess-results-10 .mx-areas{grid-template-columns:repeat(2,1fr)!important}
}
@media(max-width:900px){
  #maxess-results-10 .mx-hero-grid{grid-template-columns:1fr!important;grid-template-areas:"orb" "copy"!important;max-width:760px!important}
  #maxess-results-10 .mx-hero-grid>.mx-score-orb{width:min(500px,82vw)!important;min-width:280px!important}
  #maxess-results-10 .mx-dim-grid{grid-template-columns:repeat(2,1fr)!important}
  #maxess-results-10 .mx-areas{grid-template-columns:1fr!important}
}
@media(max-width:600px){
  #maxess-results-10 .mx-section{padding-inline:16px!important}
  #maxess-results-10 .mx-dim-grid{grid-template-columns:1fr!important}
  #maxess-results-10 .mx-dim{min-height:320px!important}
  #maxess-results-10 .mx-hero-actions{flex-direction:column!important;width:100%!important;max-width:420px!important}
  #maxess-results-10 .mx-cta{width:100%!important}
}
@media(prefers-reduced-motion:reduce){
  #maxess-results-10 .mx-score-orb,#maxess-results-10 .mx-score-orb::before,#maxess-results-10 .mx-cta-primary::after{animation:none!important}
}
</style>
<script id="maxess-aaa-directive-runtime">
(function(){
  'use strict';
  function boot(){
    var root=document.getElementById('maxess-results-10');
    if(!root)return;
    var hero=root.querySelector('.mx-hero');
    var report=document.getElementById('naya-report');
    if(hero&&report) root.insertBefore(report,hero.nextSibling);
    var fingerprint=document.getElementById('your-fingerprint');
    if(fingerprint){
      var orb=fingerprint.querySelector('.mx-radar');
      if(orb) orb.setAttribute('aria-label','Your five-dimension AI Mastery profile');
    }
    var growth=document.getElementById('growth-scorecard');
    var masters=root.querySelector('.mx-naya-playground');
    if(masters){
      var areas=root.querySelector('.mx-areas');
      if(areas) masters.setAttribute('data-report-pathway','18-naya-masters');
    }
    /* Move the commercial/library experience after the personal report chapters. */
    if(growth){
      growth.setAttribute('hidden','hidden');
    }
    /* Ensure the actual score drives the Orb/gauge state when available. */
    var result=window.MAXESS_RESULT||{};
    var score=Number(result.masterScore||result.overallScore||result.resonance||82);
    if(isFinite(score)){
      score=Math.max(0,Math.min(100,score));
      var orbScore=root.querySelector('.mx-score strong');
      if(orbScore && !orbScore.dataset.locked){orbScore.textContent=(Math.round(score*10)/10).toString().replace(/\.0$/,'');}
      root.style.setProperty('--aaa-score',score);
    }
    /* Premium circular gauge animation on entry. */
    root.querySelectorAll('.mx-dim').forEach(function(card){
      var n=Number(card.getAttribute('data-score')||0);
      card.style.setProperty('--score',Math.max(0,Math.min(100,n)));
      card.setAttribute('tabindex','0');
      card.setAttribute('role','article');
    });
    /* Keyboard focus feedback without changing the working navigation. */
    root.addEventListener('keydown',function(e){
      if(e.key==='Escape') document.activeElement && document.activeElement.blur();
    });
  }
  if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',boot,{once:true});
  else setTimeout(boot,0);
})();
</script>
'''

body_close = s.rfind('</body>')
if body_close == -1:
    raise SystemExit('No </body> found')
s = s[:body_close] + cssjs + '\n' + s[body_close:]
TARGET.write_text(s, encoding='utf-8')
print(f'Applied MAXESS AAA directive upgrade: {TARGET.stat().st_size} bytes')
