#!/usr/bin/env python3
"""MAXESS 10.3 cinematic experience pass.

Presentation-only. Preserves scoring and Result Contract. Builds on 10.2 rather
than replacing it. The goal is a visible, full-viewport, hero-first experience:
centered resonance orb, five connected dimension nodes, premium dark controls,
Naya personality, organic surfaces, ambient energy, and strong desktop/mobile
composition. No pink utility typography and no narrow desktop document column.
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
MARKER = 'MAXESS-VISUAL-PASS-10.3'

CSS = r'''<style id="maxess-visual-pass-10-3">
/* 10.3: cinematic MAXESS. Full canvas is a release requirement. */
#maxess-results-10{--m3-bg:#030307;--m3-panel:rgba(255,255,255,.055);--m3-panel2:rgba(255,255,255,.025);--m3-white:#fff;--m3-soft:rgba(255,255,255,.72);--m3-muted:rgba(255,255,255,.48);--m3-line:rgba(255,255,255,.13);--m3-violet:#8b5cf6;--m3-lilac:#c4b5fd;--m3-cyan:#55e8ff;--m3-teal:#58e0c0;--m3-gold:#f6d58b;position:relative;width:100vw!important;max-width:none!important;margin-left:calc(50% - 50vw)!important;margin-right:calc(50% - 50vw)!important;overflow:hidden;background:#030307;color:#fff}
#maxess-results-10 *{box-sizing:border-box}
#maxess-results-10 .mx-section{width:100%;max-width:none!important;padding-left:clamp(24px,5vw,96px)!important;padding-right:clamp(24px,5vw,96px)!important}
#maxess-results-10 .mx-wide{width:100%!important;max-width:1720px!important;margin:0 auto!important}
#maxess-results-10 .mx-hero{position:relative;min-height:min(940px,100vh);display:grid!important;place-items:center!important;padding:clamp(60px,8vh,110px) 24px!important;background:radial-gradient(circle at 50% 42%,rgba(117,69,221,.17),transparent 34%),radial-gradient(circle at 15% 55%,rgba(49,202,221,.055),transparent 27%),radial-gradient(circle at 85% 55%,rgba(141,72,223,.055),transparent 27%),linear-gradient(180deg,#020207,#05050a 70%,#020207)}
#maxess-results-10 .mx-hero::after{content:"";position:absolute;inset:0;pointer-events:none;background:radial-gradient(circle at 50% 45%,transparent 0 22%,rgba(255,255,255,.025) 23%,transparent 44%),linear-gradient(90deg,transparent 0 49.9%,rgba(255,255,255,.035) 50%,transparent 50.1%);opacity:.65}
#maxess-results-10 .mx-hero-grid{position:relative;z-index:2;width:min(1500px,100%)!important;max-width:none!important;display:grid!important;grid-template-columns:1fr minmax(360px,620px) 1fr!important;grid-template-areas:"left orb right";align-items:center;gap:clamp(28px,4vw,80px);text-align:center!important}
#maxess-results-10 .mx-hero-grid>.mx-score-orb{grid-area:orb;order:0;width:min(600px,44vw)!important;min-width:340px!important;margin:0 auto!important;aspect-ratio:1!important;position:relative;z-index:4}
#maxess-results-10 .mx-hero-grid>.mx-hero-copy:first-child{grid-area:left;text-align:right;align-self:center}
#maxess-results-10 .mx-hero-grid>.mx-hero-copy:last-child{grid-area:right;text-align:left;align-self:center}
#maxess-results-10 .mx-score-orb{border-radius:50%!important;background:radial-gradient(circle at 34% 27%,rgba(255,255,255,.16),rgba(137,78,241,.20) 20%,rgba(20,13,42,.92) 55%,#020207 76%)!important;border:1px solid rgba(196,181,253,.38)!important;box-shadow:0 0 0 10px rgba(139,92,246,.035),0 0 0 24px rgba(85,232,255,.018),inset 0 0 90px rgba(139,92,246,.34),inset 0 0 160px rgba(0,0,0,.72),0 40px 120px rgba(0,0,0,.72),0 0 130px rgba(139,92,246,.25)!important;animation:m103-breathe 5.2s ease-in-out infinite;will-change:transform,filter}
#maxess-results-10 .mx-score-orb::before{content:"";position:absolute;inset:-5%;border-radius:50%;border:1px solid rgba(196,181,253,.45);box-shadow:0 0 28px rgba(139,92,246,.18);animation:m103-ring 18s linear infinite}
#maxess-results-10 .mx-score-orb::after{content:"";position:absolute;inset:7%;border-radius:50%;border:1px solid rgba(85,232,255,.22);box-shadow:inset 0 0 28px rgba(85,232,255,.08);animation:m103-ring-reverse 25s linear infinite}
#maxess-results-10 .mx-score-orb .mx-score{position:relative;z-index:5;animation:m103-core 4s ease-in-out infinite;text-shadow:0 0 24px rgba(255,255,255,.22),0 0 70px rgba(139,92,246,.38)}
#maxess-results-10 .mx-orb-particles{position:absolute;inset:0;z-index:3;pointer-events:none}
#maxess-results-10 .mx-orb-particles i{position:absolute;width:7px;height:7px;border-radius:50%;background:#fff;box-shadow:0 0 18px var(--m3-cyan);opacity:.7;animation:m103-particle 4.8s ease-in-out infinite}
#maxess-results-10 .mx-orb-particles i:nth-child(1){left:17%;top:34%;animation-delay:-.4s}.mx-orb-particles i:nth-child(2){left:77%;top:29%;animation-delay:-1.1s}.mx-orb-particles i:nth-child(3){left:82%;top:63%;animation-delay:-2.2s}.mx-orb-particles i:nth-child(4){left:24%;top:72%;animation-delay:-3s}.mx-orb-particles i:nth-child(5){left:49%;top:9%;animation-delay:-3.7s}.mx-orb-particles i:nth-child(6){left:54%;top:88%;animation-delay:-4.2s}
#maxess-results-10 .mx-hero-grid .mx-hero-copy{padding:30px;border-radius:30px;background:linear-gradient(145deg,rgba(255,255,255,.045),rgba(255,255,255,.012));border:1px solid rgba(255,255,255,.09);box-shadow:inset 0 1px rgba(255,255,255,.08),0 30px 80px rgba(0,0,0,.28);backdrop-filter:blur(18px)}
#maxess-results-10 .mx-hero-grid .mx-hero-copy h1,#maxess-results-10 .mx-hero-grid .mx-hero-copy h2{color:#fff!important}
#maxess-results-10 .mx-eyebrow,#maxess-results-10 .mx-hero-grid .mx-hero-copy .mx-eyebrow{color:rgba(255,255,255,.62)!important;letter-spacing:.16em}
@keyframes m103-breathe{0%,100%{transform:scale(1);filter:brightness(1) saturate(1)}50%{transform:scale(1.035);filter:brightness(1.1) saturate(1.18)}}
@keyframes m103-core{0%,100%{transform:translateY(0) scale(1)}50%{transform:translateY(-5px) scale(1.015)}}
@keyframes m103-ring{to{transform:rotate(360deg)}}@keyframes m103-ring-reverse{to{transform:rotate(-360deg)}}
@keyframes m103-particle{0%,100%{transform:scale(.65);opacity:.25}50%{transform:scale(1.5);opacity:.9}}

/* Five dimensions become a constellation, not five spreadsheet boxes. */
#maxess-results-10 .mx-dim-grid{position:relative;display:grid!important;grid-template-columns:repeat(5,minmax(0,1fr))!important;gap:clamp(14px,2vw,28px)!important;padding:35px 0!important}
#maxess-results-10 .mx-dim-grid::before{content:"";position:absolute;left:10%;right:10%;top:50%;height:1px;background:linear-gradient(90deg,transparent,rgba(139,92,246,.4),rgba(85,232,255,.28),rgba(139,92,246,.4),transparent);box-shadow:0 0 22px rgba(139,92,246,.18)}
#maxess-results-10 .mx-dim{position:relative!important;z-index:2!important;aspect-ratio:1!important;min-height:0!important;width:100%!important;border-radius:50%!important;padding:26px!important;display:flex!important;align-items:center!important;justify-content:center!important;text-align:center!important;background:radial-gradient(circle at 32% 26%,rgba(255,255,255,.12),rgba(139,92,246,.07) 35%,rgba(3,3,7,.92) 76%)!important;border:1px solid rgba(255,255,255,.14)!important;box-shadow:inset 0 1px rgba(255,255,255,.14),inset 0 -20px 40px rgba(0,0,0,.3),0 24px 60px rgba(0,0,0,.45)!important;transition:transform .32s cubic-bezier(.2,.8,.2,1),box-shadow .32s ease,border-color .32s ease!important}
#maxess-results-10 .mx-dim:hover,#maxess-results-10 .mx-dim:focus-within{transform:translateY(-10px) scale(1.035)!important;border-color:rgba(196,181,253,.45)!important;box-shadow:inset 0 1px rgba(255,255,255,.2),0 32px 80px rgba(0,0,0,.55),0 0 42px rgba(139,92,246,.14)!important}
#maxess-results-10 .mx-dim::after{content:"";position:absolute;inset:8%;border-radius:50%;border:1px solid rgba(85,232,255,.10);pointer-events:none}
#maxess-results-10 .mx-dim .mx-dim-score{font-size:clamp(40px,4vw,68px)!important;color:#fff!important;text-shadow:0 0 32px rgba(139,92,246,.32)}
#maxess-results-10 .mx-dim strong,#maxess-results-10 .mx-dim b{color:#fff!important}

/* Section surfaces: depth without turning every section into a rectangle. */
#maxess-results-10 .mx-growth-grid,#maxess-results-10 .mx-naya-doors{display:grid!important;grid-template-columns:repeat(3,minmax(0,1fr))!important;gap:24px!important}
#maxess-results-10 .mx-growth-card,#maxess-results-10 .mx-naya-door{border-radius:32px!important;background:linear-gradient(145deg,rgba(255,255,255,.065),rgba(255,255,255,.018))!important;border:1px solid rgba(255,255,255,.11)!important;box-shadow:inset 0 1px rgba(255,255,255,.11),0 30px 90px rgba(0,0,0,.42)!important;backdrop-filter:blur(18px);transition:transform .28s ease,box-shadow .28s ease,border-color .28s ease!important}
#maxess-results-10 .mx-growth-card:hover,#maxess-results-10 .mx-naya-door:hover{transform:translateY(-7px)!important;border-color:rgba(196,181,253,.3)!important;box-shadow:inset 0 1px rgba(255,255,255,.16),0 40px 105px rgba(0,0,0,.5),0 0 55px rgba(139,92,246,.1)!important}
#maxess-results-10 .mx-naya-door{min-height:280px!important;position:relative;overflow:hidden}
#maxess-results-10 .mx-naya-door::before{content:"";position:absolute;width:180px;height:180px;border-radius:50%;right:-60px;top:-70px;background:radial-gradient(circle,rgba(85,232,255,.18),transparent 70%);filter:blur(4px)}
#maxess-results-10 .mx-naya-door:nth-child(2)::before{background:radial-gradient(circle,rgba(246,213,139,.17),transparent 70%)}
#maxess-results-10 .mx-naya-door:nth-child(3)::before{background:radial-gradient(circle,rgba(139,92,246,.2),transparent 70%)}

/* Premium controls: dark glass, white type, restrained luminous edge. */
#maxess-results-10 .mx-cta,#maxess-results-10 .mx-mini{position:relative;overflow:hidden;color:#fff!important;background:linear-gradient(145deg,#211737 0%,#0a090e 55%,#030306 100%)!important;border:1px solid rgba(255,255,255,.24)!important;border-radius:16px!important;min-height:52px;box-shadow:inset 0 1px rgba(255,255,255,.18),inset 0 -1px rgba(0,0,0,.75),0 18px 42px rgba(0,0,0,.42)!important;transition:transform .24s ease,box-shadow .24s ease,border-color .24s ease!important}
#maxess-results-10 .mx-cta::after,#maxess-results-10 .mx-mini::after{content:"";position:absolute;inset:0;background:linear-gradient(105deg,transparent 28%,rgba(255,255,255,.18) 48%,transparent 62%);transform:translateX(-120%);transition:transform .7s ease;pointer-events:none}
#maxess-results-10 .mx-cta:hover,#maxess-results-10 .mx-cta:focus-visible,#maxess-results-10 .mx-mini:hover,#maxess-results-10 .mx-mini:focus-visible{transform:translateY(-4px)!important;border-color:rgba(255,255,255,.48)!important;box-shadow:inset 0 1px rgba(255,255,255,.24),0 26px 60px rgba(0,0,0,.55),0 0 34px rgba(139,92,246,.15)!important}
#maxess-results-10 .mx-cta:hover::after,#maxess-results-10 .mx-mini:hover::after,#maxess-results-10 .mx-cta:focus-visible::after,#maxess-results-10 .mx-mini:focus-visible::after{transform:translateX(120%)}
#maxess-results-10 .mx-cta-primary{background:linear-gradient(145deg,#3a2365,#0b0911 72%)!important;border-color:rgba(196,181,253,.5)!important}

/* No pink utility labels. */
#maxess-results-10 .mx-eyebrow,#maxess-results-10 .mx-plan b,#maxess-results-10 .mx-growth-card b,#maxess-results-10 .mx-growth-card strong{color:rgba(255,255,255,.72)!important}

/* Make major sections feel like chapters rather than boxes. */
#maxess-results-10 .mx-section-title{color:#fff!important;letter-spacing:-.025em}
#maxess-results-10 .mx-section-title::after{background:linear-gradient(90deg,rgba(139,92,246,.75),rgba(85,232,255,.45),transparent)!important}

/* Naya gets a visible identity without a cartoon mascot. */
#maxess-results-10 .mx-naya-playground{position:relative;border-top:1px solid rgba(255,255,255,.08);border-bottom:1px solid rgba(255,255,255,.08);background:radial-gradient(circle at 50% 50%,rgba(139,92,246,.09),transparent 55%)}
#maxess-results-10 .mx-naya-playground::before{content:"NAYA";position:absolute;right:4vw;top:30px;font-size:clamp(70px,12vw,180px);font-weight:900;letter-spacing:-.08em;color:rgba(255,255,255,.018);pointer-events:none}

/* Full-bleed video/buttons retain the premium dark system. */
#maxess-results-10 video{border-radius:28px!important;box-shadow:0 35px 100px rgba(0,0,0,.58)!important;border:1px solid rgba(255,255,255,.12)}

@media(max-width:1150px){#maxess-results-10 .mx-hero-grid{grid-template-columns:1fr!important;grid-template-areas:"orb" "left" "right";max-width:760px!important}#maxess-results-10 .mx-hero-grid>.mx-score-orb{width:min(560px,76vw)!important}#maxess-results-10 .mx-hero-grid>.mx-hero-copy:first-child,#maxess-results-10 .mx-hero-grid>.mx-hero-copy:last-child{text-align:center}#maxess-results-10 .mx-dim-grid{grid-template-columns:repeat(3,minmax(0,1fr))!important}#maxess-results-10 .mx-growth-grid,#maxess-results-10 .mx-naya-doors{grid-template-columns:1fr 1fr!important}}
@media(max-width:700px){#maxess-results-10 .mx-hero{min-height:auto;padding-top:52px!important;padding-bottom:58px!important}#maxess-results-10 .mx-hero-grid>.mx-score-orb{width:min(480px,86vw)!important;min-width:280px!important}#maxess-results-10 .mx-dim-grid{grid-template-columns:repeat(2,minmax(0,1fr))!important}#maxess-results-10 .mx-growth-grid,#maxess-results-10 .mx-naya-doors{grid-template-columns:1fr!important}}
@media(max-width:480px){#maxess-results-10 .mx-section{padding-left:16px!important;padding-right:16px!important}#maxess-results-10 .mx-dim-grid{grid-template-columns:1fr 1fr!important;gap:12px!important}#maxess-results-10 .mx-dim{padding:18px!important}#maxess-results-10 .mx-dim .mx-dim-score{font-size:40px!important}}
@media(prefers-reduced-motion:reduce){#maxess-results-10 .mx-score-orb,#maxess-results-10 .mx-score-orb::before,#maxess-results-10 .mx-score-orb::after,#maxess-results-10 .mx-score-orb .mx-score,#maxess-results-10 .mx-orb-particles i{animation:none!important}#maxess-results-10 .mx-dim,#maxess-results-10 .mx-growth-card,#maxess-results-10 .mx-naya-door,#maxess-results-10 .mx-cta,#maxess-results-10 .mx-mini{transition:none!important}}
</style>'''

JS = r'''<script id="maxess-visual-pass-10-3-js">
(function(){
  'use strict';
  function boot(){
    var root=document.getElementById('maxess-results-10');
    if(!root)return;
    root.setAttribute('data-maxess-visual-pass','10.3');
    var orb=root.querySelector('.mx-score-orb');
    if(orb&&!orb.querySelector('.mx-orb-particles')){
      var p=document.createElement('span');p.className='mx-orb-particles';p.setAttribute('aria-hidden','true');
      p.innerHTML='<i></i><i></i><i></i><i></i><i></i><i></i>';orb.appendChild(p);
    }
    if(orb){orb.setAttribute('role','img');orb.setAttribute('aria-label','Living MAXESS resonance score');}
    root.querySelectorAll('.mx-dim').forEach(function(node,index){
      node.setAttribute('tabindex','0');
      node.setAttribute('data-dimension-node',String(index+1));
    });
  }
  if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',boot,{once:true});else boot();
})();
</script>'''

BLOCK='\n<!-- '+MARKER+' -->\n'+CSS+'\n'+JS+'\n'
changed=0
for path in FILES:
    if not path.exists(): continue
    html=path.read_text(encoding='utf-8')
    if MARKER in html: continue
    if '</body>' in html: html=html.replace('</body>',BLOCK+'</body>',1)
    elif '</html>' in html: html=html.replace('</html>',BLOCK+'</html>',1)
    else: html += BLOCK
    path.write_text(html,encoding='utf-8'); changed+=1
if changed==0: raise SystemExit('No Results artifacts received 10.3 pass.')
print(f'MAXESS 10.3 cinematic pass applied to {changed} artifact(s).')
