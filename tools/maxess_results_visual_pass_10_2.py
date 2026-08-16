#!/usr/bin/env python3
"""MAXESS 10.2 presentation pass.

Presentation-only. Protects scoring, Result Contract, and assessment logic.
Targets the live Results artifacts with a stronger desktop composition,
centered score hero, organic dimension language, premium controls, and a
visible cinematic layer rather than relying on hidden/unused CSS.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FILES = [
    ROOT / 'MAXESS-RESULTS-FINAL-GROOVE.html',
    ROOT / 'MAXESS-RESULTS-FINAL-GROOVE-EMBED.html',
    ROOT / 'MAXESS-RESULTS-10-GROOVE.html',
    ROOT / 'MAXESS-RESULTS-GROOVE-EMBED.html',
    ROOT / 'MAXESS-RESULTS-GROOVE-EMBED-9.95.html',
]
MARKER = 'MAXESS-VISUAL-PASS-10.2'

CSS = r'''<style id="maxess-visual-pass-10-2">
/* 10.2 HARD RULES: full desktop canvas, hero-first hierarchy, dark/high contrast. */
#maxess-results-10{
  --mx-bg:#020207;
  --mx-ink:#fff;
  --mx-soft:rgba(255,255,255,.76);
  --mx-muted:rgba(255,255,255,.48);
  --mx-line:rgba(255,255,255,.12);
  --mx-purple:#7b43e6;
  --mx-violet:#b99aff;
  --mx-cyan:#4ee7ff;
  --mx-gold:#f5d48b;
  --mx-green:#5ee7b2;
  --mx-max:1920px;
  width:100vw;
  max-width:none;
  margin-left:calc(50% - 50vw);
  margin-right:calc(50% - 50vw);
  background:
    radial-gradient(ellipse 55% 42% at 50% 7%,rgba(103,52,190,.24),transparent 72%),
    radial-gradient(ellipse 35% 35% at 8% 38%,rgba(39,126,188,.08),transparent 72%),
    radial-gradient(ellipse 35% 35% at 92% 55%,rgba(120,49,177,.08),transparent 72%),
    #020207;
}
#maxess-results-10 .mx-wide{width:min(1920px,100%);max-width:none;margin:0 auto}
#maxess-results-10 .mx-section{padding-left:clamp(28px,5vw,110px);padding-right:clamp(28px,5vw,110px)}

/* Remove the accidental document-column feeling. */
#maxess-results-10 .mx-hero{min-height:min(980px,100vh);display:flex;align-items:center;justify-content:center;padding-top:80px;padding-bottom:80px}
#maxess-results-10 .mx-hero-grid{display:flex;flex-direction:column;align-items:center;justify-content:center;gap:34px;width:100%;max-width:1500px;text-align:center}
#maxess-results-10 .mx-hero-grid > *{width:100%;max-width:1500px}
#maxess-results-10 .mx-hero-grid .mx-score-orb{order:-1}
#maxess-results-10 .mx-hero .mx-score-orb{width:min(590px,62vw);min-width:330px;margin:0 auto}
#maxess-results-10 .mx-hero .mx-score-orb::before{inset:7%;border:1px solid rgba(185,154,255,.52);box-shadow:0 0 70px rgba(123,67,230,.32),inset 0 0 28px rgba(78,231,255,.08)}
#maxess-results-10 .mx-hero .mx-score-orb::after{inset:13%;border:1px solid rgba(78,231,255,.20);box-shadow:0 0 45px rgba(78,231,255,.10)}
#maxess-results-10 .mx-hero .mx-score strong{text-shadow:0 0 25px rgba(255,255,255,.20),0 0 70px rgba(123,67,230,.28)}
#maxess-results-10 .mx-hero .mx-score span{color:rgba(255,255,255,.72)}
#maxess-results-10 .mx-hero .mx-band{border-color:rgba(255,255,255,.18);background:rgba(255,255,255,.06)}
#maxess-results-10 .mx-hero-actions{justify-content:center}

/* Make the orb visibly alive, not merely declared as an animation. */
#maxess-results-10 .mx-score-orb{animation:mx102-orb-breathe 4.8s ease-in-out infinite;will-change:transform,filter}
#maxess-results-10 .mx-score-orb::before{animation:mx102-ring 16s linear infinite}
#maxess-results-10 .mx-score-orb::after{animation:mx102-ring-reverse 22s linear infinite}
#maxess-results-10 .mx-score-orb{box-shadow:0 0 0 1px rgba(255,255,255,.18),inset 0 0 90px rgba(123,67,230,.26),0 40px 120px rgba(0,0,0,.72),0 0 150px rgba(123,67,230,.24)}
#maxess-results-10 .mx-score-orb .mx-score{animation:mx102-core 3.8s ease-in-out infinite}
@keyframes mx102-orb-breathe{0%,100%{transform:scale(1);filter:saturate(1) brightness(1)}50%{transform:scale(1.025);filter:saturate(1.22) brightness(1.08)}}
@keyframes mx102-core{0%,100%{transform:translateY(0)}50%{transform:translateY(-4px)}}
@keyframes mx102-ring{to{transform:rotate(360deg)}}
@keyframes mx102-ring-reverse{to{transform:rotate(-360deg)}}

/* Kill the repeated square-card language. Organic capsules/rings become the visual vocabulary. */
#maxess-results-10 .mx-dim{
  border-radius:50% !important;
  aspect-ratio:1/1;
  min-height:250px;
  display:flex;
  flex-direction:column;
  justify-content:center;
  align-items:center;
  text-align:center;
  padding:34px !important;
  border:1px solid rgba(255,255,255,.14) !important;
  background:radial-gradient(circle at 35% 25%,rgba(255,255,255,.10),rgba(255,255,255,.025) 55%,rgba(0,0,0,.18) 100%) !important;
  box-shadow:inset 0 1px rgba(255,255,255,.16),0 30px 90px rgba(0,0,0,.38) !important;
  transition:transform .3s cubic-bezier(.2,.8,.2,1),box-shadow .3s ease,border-color .3s ease;
}
#maxess-results-10 .mx-dim:hover{transform:translateY(-7px) scale(1.025);border-color:rgba(185,154,255,.40) !important;box-shadow:inset 0 1px rgba(255,255,255,.22),0 38px 110px rgba(0,0,0,.48),0 0 55px rgba(123,67,230,.12) !important}
#maxess-results-10 .mx-dim strong,#maxess-results-10 .mx-dim b{color:#fff !important}
#maxess-results-10 .mx-dim .mx-dim-score{font-size:clamp(42px,5vw,72px);text-shadow:0 0 35px rgba(123,67,230,.24)}
#maxess-results-10 .mx-dim-grid{display:grid;grid-template-columns:repeat(5,minmax(180px,1fr));gap:20px;align-items:stretch}

/* Premium controls: black/white first, luminous accents second. */
#maxess-results-10 .mx-cta,
#maxess-results-10 .mx-mini{
  color:#fff !important;
  background:linear-gradient(145deg,#17121e 0%,#08070c 62%,#050509 100%) !important;
  border:1px solid rgba(255,255,255,.22) !important;
  border-radius:18px !important;
  box-shadow:inset 0 1px rgba(255,255,255,.16),inset 0 -1px rgba(0,0,0,.6),0 18px 45px rgba(0,0,0,.38) !important;
  text-shadow:0 1px 2px rgba(0,0,0,.7);
  transition:transform .25s cubic-bezier(.2,.8,.2,1),box-shadow .25s ease,border-color .25s ease,background .25s ease !important;
}
#maxess-results-10 .mx-cta:hover,#maxess-results-10 .mx-cta:focus-visible,
#maxess-results-10 .mx-mini:hover,#maxess-results-10 .mx-mini:focus-visible{
  transform:translateY(-4px);
  border-color:rgba(255,255,255,.42) !important;
  background:linear-gradient(145deg,#25193b,#0a090f 68%,#050509) !important;
  box-shadow:inset 0 1px rgba(255,255,255,.22),0 24px 60px rgba(0,0,0,.50),0 0 35px rgba(123,67,230,.16) !important;
}
#maxess-results-10 .mx-cta-primary{background:linear-gradient(145deg,#2b1b4d,#0a090f 72%) !important;border-color:rgba(185,154,255,.45) !important}
#maxess-results-10 .mx-cta-primary::after{background:linear-gradient(90deg,transparent,rgba(255,255,255,.55),transparent) !important}

/* No pink utility typography. White/cool-neutral only. */
#maxess-results-10 .mx-eyebrow{color:rgba(255,255,255,.68) !important}
#maxess-results-10 .mx-eyebrow::before{background:linear-gradient(90deg,rgba(185,154,255,.8),transparent) !important}
#maxess-results-10 .mx-growth-card b,#maxess-results-10 .mx-growth-card strong{color:#fff !important}
#maxess-results-10 .mx-plan b{color:rgba(255,255,255,.78) !important}

/* Use the full canvas for sections that previously looked like a document column. */
#maxess-results-10 .mx-growth-grid{grid-template-columns:repeat(2,minmax(0,1fr));gap:28px}
#maxess-results-10 .mx-growth-card{border-radius:34px;background:linear-gradient(145deg,rgba(255,255,255,.065),rgba(255,255,255,.018))}
#maxess-results-10 .mx-naya-playground{width:100%;}
#maxess-results-10 .mx-naya-doors{grid-template-columns:repeat(3,minmax(0,1fr));gap:22px}
#maxess-results-10 .mx-naya-door{border-radius:34px;background:linear-gradient(145deg,rgba(255,255,255,.075),rgba(255,255,255,.015));box-shadow:inset 0 1px rgba(255,255,255,.15),0 35px 100px rgba(0,0,0,.42)}
#maxess-results-10 .mx-naya-door:hover{box-shadow:inset 0 1px rgba(255,255,255,.22),0 45px 120px rgba(0,0,0,.52),0 0 70px rgba(123,67,230,.14)}

/* Ambient cinematic field. */
#maxess-results-10::after{opacity:.11;background-image:radial-gradient(rgba(255,255,255,.28) .55px,transparent .7px);background-size:7px 7px;mask-image:linear-gradient(#000,transparent 78%)}
#maxess-results-10 .mx-hero::before{width:min(1100px,90vw);height:720px;background:radial-gradient(circle,rgba(123,67,230,.28),rgba(78,231,255,.045) 34%,transparent 70%);filter:blur(20px);animation:mx102-ambient 9s ease-in-out infinite}
@keyframes mx102-ambient{0%,100%{transform:translateX(-50%) scale(1);opacity:.78}50%{transform:translateX(-50%) scale(1.08);opacity:1}}

@media(max-width:1150px){#maxess-results-10 .mx-dim-grid{grid-template-columns:repeat(3,1fr)}#maxess-results-10 .mx-naya-doors{grid-template-columns:1fr 1fr}.mx-naya-door:last-child{grid-column:1/-1}}
@media(max-width:800px){#maxess-results-10 .mx-hero{min-height:auto;padding-top:60px}#maxess-results-10 .mx-hero .mx-score-orb{width:min(480px,82vw)}#maxess-results-10 .mx-dim-grid{grid-template-columns:repeat(2,1fr)}#maxess-results-10 .mx-growth-grid{grid-template-columns:1fr}}
@media(max-width:560px){#maxess-results-10 .mx-section{padding-left:18px;padding-right:18px}#maxess-results-10 .mx-dim-grid{grid-template-columns:1fr}#maxess-results-10 .mx-dim{min-height:220px}#maxess-results-10 .mx-naya-doors{grid-template-columns:1fr}.mx-naya-door:last-child{grid-column:auto}}
@media(prefers-reduced-motion:reduce){#maxess-results-10 .mx-score-orb,#maxess-results-10 .mx-score-orb::before,#maxess-results-10 .mx-score-orb::after,#maxess-results-10 .mx-score-orb .mx-score,#maxess-results-10 .mx-hero::before{animation:none !important}#maxess-results-10 .mx-dim,#maxess-results-10 .mx-cta,#maxess-results-10 .mx-mini{transition:none !important}}
</style>'''

JS = r'''<script id="maxess-visual-pass-10-2-js">
(function(){
  'use strict';
  function boot(){
    var root=document.getElementById('maxess-results-10');
    if(!root)return;
    root.setAttribute('data-maxess-visual-pass','10.2');
    /* Make the hero unquestionably the first visual focal point. */
    var orb=root.querySelector('.mx-score-orb');
    var hero=root.querySelector('.mx-hero');
    if(hero&&orb){
      var grid=hero.querySelector('.mx-hero-grid');
      if(grid)grid.classList.add('mx-hero-centered');
      orb.setAttribute('aria-label','MAXESS living resonance score');
    }
    /* Add a few inert visual particles around the orb. They never own score data. */
    if(orb&&!orb.querySelector('.mx-orb-particles')){
      var p=document.createElement('span');
      p.className='mx-orb-particles';
      p.setAttribute('aria-hidden','true');
      p.innerHTML='<i></i><i></i><i></i><i></i><i></i><i></i>';
      orb.appendChild(p);
    }
  }
  if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',boot,{once:true});else boot();
})();
</script>'''

BLOCK='\n<!-- '+MARKER+' -->\n'+CSS+'\n'+JS+'\n'

changed=0
for path in FILES:
    if not path.exists():
        continue
    html=path.read_text(encoding='utf-8')
    if MARKER in html:
        continue
    if '</body>' in html:
        html=html.replace('</body>',BLOCK+'</body>',1)
    elif '</html>' in html:
        html=html.replace('</html>',BLOCK+'</html>',1)
    else:
        html += BLOCK
    path.write_text(html,encoding='utf-8')
    changed += 1

if changed == 0:
    raise SystemExit('No Results artifacts received the 10.2 visual pass.')
print(f'MAXESS 10.2 visual pass applied to {changed} artifact(s).')
