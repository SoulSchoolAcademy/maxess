from pathlib import Path

MARK = "NAYA-LAW-AAA-RESULTS-PASS-2"
FILES = [
    "MAXESS-RESULTS-10-GROOVE.html",
    "MAXESS-RESULTS-FINAL-GROOVE.html",
    "MAXESS-RESULTS-GROOVE-EMBED.html",
    "MAXESS-RESULTS-FINAL-GROOVE-EMBED.html",
    "MAXESS-RESULTS-GROOVE-EMBED-9.95.html",
]

CSS = r'''
/* NAYA LAW — preservation-first AAA visual pass */
#maxess-results-10{
  --nl-black:#020205;--nl-white:#fff;--nl-red:#ff4b55;--nl-orange:#ff9d3d;--nl-yellow:#ffd84a;
  --nl-green:#38df91;--nl-teal:#36d9d1;--nl-blue:#3c9cff;--nl-indigo:#586cff;--nl-purple:#965dff;--nl-magenta:#ef4bc8;
  width:100vw!important;max-width:none!important;margin-left:calc(50% - 50vw)!important;margin-right:calc(50% - 50vw)!important;
  background:var(--nl-black)!important;color:#fff!important;overflow:hidden!important;
}
#maxess-results-10 .mx-section{width:100%!important;padding-left:clamp(18px,4vw,86px)!important;padding-right:clamp(18px,4vw,86px)!important}
#maxess-results-10 .mx-wide{width:100%!important;max-width:1760px!important;margin-inline:auto!important}
#maxess-results-10 .mx-hero{min-height:min(920px,95vh)!important;background:radial-gradient(circle at 50% 44%,rgba(150,93,255,.22),transparent 31%),linear-gradient(180deg,#020205 0%,#050307 72%,#09040d 100%)!important}
#maxess-results-10 .mx-hero-grid{display:grid!important;grid-template-columns:minmax(0,1fr) minmax(360px,680px) minmax(0,1fr)!important;grid-template-areas:"copy orb side"!important;align-items:center!important;gap:clamp(22px,4vw,72px)!important;width:min(1660px,100%)!important;margin:auto!important;text-align:center!important}
#maxess-results-10 .mx-hero-grid>.mx-score-orb{grid-area:orb!important;width:min(650px,48vw)!important;min-width:350px!important;margin:auto!important;order:0!important}
#maxess-results-10 .mx-hero-grid>div:first-child{grid-area:copy!important;text-align:center!important;display:flex!important;flex-direction:column!important;align-items:center!important}
#maxess-results-10 .mx-title{font-size:clamp(44px,5.8vw,88px)!important;line-height:.94!important;color:#fff!important}
#maxess-results-10 .mx-copy{font-size:clamp(16px,1.35vw,20px)!important;color:rgba(255,255,255,.84)!important}
#maxess-results-10 .mx-proof{display:none!important}
#maxess-results-10 .mx-score-orb{--nl-orb-a:#965dff;--nl-orb-b:#ef4bc8;transition:filter .5s ease,box-shadow .5s ease!important;box-shadow:0 0 0 1px rgba(255,255,255,.22),inset 0 0 100px color-mix(in srgb,var(--nl-orb-a) 32%,transparent),0 40px 125px rgba(0,0,0,.75),0 0 145px color-mix(in srgb,var(--nl-orb-a) 25%,transparent)!important}
#maxess-results-10 .mx-score-orb::before{border-color:color-mix(in srgb,var(--nl-orb-a) 60%,white 10%)!important;box-shadow:0 0 55px color-mix(in srgb,var(--nl-orb-a) 28%,transparent)!important}
#maxess-results-10 .mx-score strong{font-size:clamp(110px,13vw,190px)!important;background:linear-gradient(110deg,var(--nl-orb-a),var(--nl-orb-b))!important;-webkit-background-clip:text!important;background-clip:text!important;color:transparent!important;text-shadow:0 0 45px color-mix(in srgb,var(--nl-orb-a) 25%,transparent)!important}
#maxess-results-10 .mx-hero-actions{justify-content:center!important}
#maxess-results-10 .mx-cta{min-height:58px!important;border-radius:18px!important;padding-inline:26px!important;border:1px solid rgba(255,255,255,.2)!important;box-shadow:inset 0 1px rgba(255,255,255,.35),0 18px 45px rgba(0,0,0,.48)!important}
#maxess-results-10 .mx-cta-primary{background:linear-gradient(120deg,#111116,#34224d 52%,#6533bd)!important}
#maxess-results-10 .mx-cta-ghost{background:#08080c!important}
#maxess-results-10 #naya-report{padding-top:clamp(34px,5vw,72px)!important;padding-bottom:clamp(48px,6vw,88px)!important;background:#08080b!important}
#maxess-results-10 #naya-report .mx-bridge-card{max-width:1320px!important;margin:auto!important;border-radius:34px!important;background:#050507!important;border:1px solid rgba(150,93,255,.42)!important;box-shadow:inset 0 1px rgba(255,255,255,.1),0 35px 110px rgba(0,0,0,.5)!important}
#maxess-results-10 #naya-report .mx-bridge-card h2{font-size:clamp(38px,5.4vw,78px)!important;color:#fff!important}
#maxess-results-10 #naya-report .mx-bridge-card p{font-size:clamp(17px,1.4vw,21px)!important;color:rgba(255,255,255,.8)!important}
#maxess-results-10 #naya-report .mx-key{margin-top:28px!important}
#maxess-results-10 #naya-report .mx-key div{border:0!important;border-radius:999px!important;padding:14px 10px!important;font-weight:950!important}
#maxess-results-10 #naya-report .mx-key div:nth-child(1){background:var(--nl-red)!important}
#maxess-results-10 #naya-report .mx-key div:nth-child(2){background:var(--nl-orange)!important;color:#111!important}
#maxess-results-10 #naya-report .mx-key div:nth-child(3){background:var(--nl-yellow)!important;color:#111!important}
#maxess-results-10 #naya-report .mx-key div:nth-child(4){background:var(--nl-teal)!important;color:#06100e!important}
#maxess-results-10 #naya-report .mx-key div:nth-child(5){background:var(--nl-indigo)!important}
#maxess-results-10 #naya-report .mx-key div:nth-child(6){background:var(--nl-purple)!important}
#maxess-results-10 #naya-report .mx-key div:nth-child(7){background:var(--nl-magenta)!important}
#maxess-results-10 .nl-print{display:inline-flex;align-items:center;gap:9px;margin-top:10px;min-height:50px;padding:0 17px;border-radius:15px;border:1px solid rgba(255,255,255,.18);background:#07070a;color:#fff;font-weight:900;cursor:pointer;box-shadow:inset 0 1px rgba(255,255,255,.12),0 12px 30px rgba(0,0,0,.35)}
#maxess-results-10 .nl-print:hover{transform:translateY(-2px);border-color:#b895ff;box-shadow:0 0 30px rgba(150,93,255,.18)}
#maxess-results-10 .mx-dim-grid{display:grid!important;grid-template-columns:repeat(5,minmax(150px,1fr))!important;gap:18px!important}
#maxess-results-10 .mx-dim{--g:var(--nl-purple);position:relative!important;min-height:340px!important;border-radius:32px!important;padding:24px 18px!important;display:flex!important;flex-direction:column!important;align-items:center!important;justify-content:flex-start!important;text-align:center!important;background:#050507!important;border:1px solid rgba(255,255,255,.13)!important;box-shadow:inset 0 1px rgba(255,255,255,.1),0 28px 80px rgba(0,0,0,.38)!important;overflow:hidden!important}
#maxess-results-10 .mx-dim:nth-child(1){--g:var(--nl-orange)}
#maxess-results-10 .mx-dim:nth-child(2){--g:var(--nl-yellow)}
#maxess-results-10 .mx-dim:nth-child(3){--g:var(--nl-green)}
#maxess-results-10 .mx-dim:nth-child(4){--g:var(--nl-blue)}
#maxess-results-10 .mx-dim:nth-child(5){--g:var(--nl-purple)}
#maxess-results-10 .mx-dim::before{content:"";position:absolute;top:22px;left:50%;width:156px;height:156px;transform:translateX(-50%);border-radius:50%;background:conic-gradient(var(--g) calc(var(--score,0)*1%),rgba(255,255,255,.08) 0);filter:drop-shadow(0 0 14px color-mix(in srgb,var(--g) 40%,transparent));}
#maxess-results-10 .mx-dim::after{content:"";position:absolute;top:34px;left:50%;width:132px;height:132px;transform:translateX(-50%);border-radius:50%;background:#050507;box-shadow:inset 0 0 28px rgba(0,0,0,.7),0 0 0 1px color-mix(in srgb,var(--g) 35%,transparent)}
#maxess-results-10 .mx-dim[data-score="86"]{--score:86}#maxess-results-10 .mx-dim[data-score="91"]{--score:91}#maxess-results-10 .mx-dim[data-score="79"]{--score:79}#maxess-results-10 .mx-dim[data-score="74"]{--score:74}#maxess-results-10 .mx-dim[data-score="68"]{--score:68}
#maxess-results-10 .mx-dim-head{position:relative!important;z-index:2!important;margin-top:52px!important;display:flex!important;flex-direction:column!important;align-items:center!important;gap:7px!important}
#maxess-results-10 .mx-dim-head .mx-kicker{font-size:10px!important;color:rgba(255,255,255,.52)!important}
#maxess-results-10 .mx-dim-head h3{font-size:17px!important;color:#fff!important}
#maxess-results-10 .mx-dim-head strong{font-size:43px!important;line-height:1!important;color:var(--g)!important;text-shadow:0 0 20px color-mix(in srgb,var(--g) 28%,transparent)!important}
#maxess-results-10 .mx-dim .mx-track{position:relative!important;z-index:2!important;width:82%!important;height:7px!important;margin:17px 0 12px!important;background:rgba(255,255,255,.08)!important}
#maxess-results-10 .mx-dim .mx-track span{background:var(--g)!important;box-shadow:0 0 16px color-mix(in srgb,var(--g) 42%,transparent)!important}
#maxess-results-10 .mx-dim p{position:relative!important;z-index:2!important;font-size:12px!important;line-height:1.5!important;color:rgba(255,255,255,.72)!important;margin:0!important}
#maxess-results-10 .mx-lever{position:relative!important;z-index:2!important;width:100%!important;margin-top:14px!important;padding-top:11px!important;border-top:1px solid rgba(255,255,255,.08)!important}
#maxess-results-10 .mx-lever span{color:var(--g)!important}#maxess-results-10 .mx-lever b{font-size:11px!important;color:#fff!important}
#maxess-results-10 #your-fingerprint{background:#fff!important;color:#08080b!important}
#maxess-results-10 #your-fingerprint .mx-eyebrow{color:#5b31a9!important}
#maxess-results-10 #your-fingerprint .mx-section-head p{color:#303038!important;font-size:clamp(17px,1.35vw,21px)!important;max-width:900px!important}
#maxess-results-10 #growth-scorecard{background:#030305!important;color:#fff!important}
#maxess-results-10 .mx-pattern-head h2{font-size:clamp(38px,5vw,74px)!important}
#maxess-results-10 .mx-pattern-head p{font-size:clamp(17px,1.35vw,21px)!important}
#maxess-results-10 .mx-node{border-radius:50%!important;box-shadow:inset 0 1px rgba(255,255,255,.55),0 25px 65px rgba(0,0,0,.3)!important}
#maxess-results-10 .mx-node strong{font-size:clamp(34px,4vw,56px)!important}
#maxess-results-10 .mx-naya-playground{background:linear-gradient(135deg,#160b24,#050507 72%)!important}
#maxess-results-10 .mx-naya-door{border-radius:30px!important;background:linear-gradient(145deg,#09090d,#15111c)!important;border:1px solid rgba(255,255,255,.14)!important;box-shadow:inset 0 1px rgba(255,255,255,.1),0 28px 80px rgba(0,0,0,.42)!important}
#maxess-results-10 .mx-naya-icon{filter:saturate(1.3) drop-shadow(0 0 14px rgba(150,93,255,.2))}
#maxess-results-10 .mx-area{border-radius:26px!important;background:linear-gradient(145deg,#08080d,#12101a)!important;border-color:rgba(255,255,255,.13)!important}
#maxess-results-10 .mx-area-main h3{color:#fff!important}#maxess-results-10 .mx-area-main p{color:rgba(255,255,255,.65)!important}
#maxess-results-10 .ny-page-inner{width:100%!important;max-width:none!important}.ny-theater{width:100%!important;padding-inline:clamp(10px,3vw,48px)!important}.ny-screen-frame{width:min(1600px,100%)!important}.ny-primary-zone,.ny-secondary-grid,.ny-membership{width:100%!important;max-width:none!important}
@media(max-width:1150px){#maxess-results-10 .mx-dim-grid{grid-template-columns:repeat(3,1fr)!important}.ny-secondary-grid{grid-template-columns:repeat(2,minmax(0,1fr))!important}}
@media(max-width:900px){#maxess-results-10 .mx-hero-grid{grid-template-columns:1fr!important;grid-template-areas:"orb" "copy" "side"!important;max-width:760px!important}#maxess-results-10 .mx-hero-grid>.mx-score-orb{width:min(500px,82vw)!important;min-width:280px!important}#maxess-results-10 .mx-dim-grid{grid-template-columns:repeat(2,1fr)!important}.ny-secondary-grid{grid-template-columns:repeat(2,minmax(0,1fr))!important}}
@media(max-width:600px){#maxess-results-10 .mx-section{padding-inline:16px!important}#maxess-results-10 .mx-dim-grid{grid-template-columns:1fr!important}#maxess-results-10 .mx-dim{min-height:320px!important}.ny-secondary-grid{grid-template-columns:1fr!important}}
@media(prefers-reduced-motion:reduce){#maxess-results-10 .mx-score-orb,#maxess-results-10 .mx-dim,#maxess-results-10 .mx-cta{animation:none!important;transition:none!important}}
@media print{
  @page{size:letter;margin:.55in}
  html,body{background:#fff!important;color:#111!important}
  #maxess-results-10{width:100%!important;margin:0!important;background:#fff!important;color:#111!important}
  #maxess-results-10 .mx-hero{min-height:auto!important;background:#fff!important;padding:24px 0 30px!important}
  #maxess-results-10 .mx-hero-grid{display:block!important;text-align:center!important}
  #maxess-results-10 .mx-hero-grid>div:first-child{text-align:center!important}
  #maxess-results-10 .mx-score-orb{width:250px!important;box-shadow:none!important;animation:none!important;margin:10px auto 22px!important}
  #maxess-results-10 .mx-hero-actions,#maxess-results-10 .mx-proof,.nl-print{display:none!important}
  #maxess-results-10 .mx-section{padding:24px 0!important;break-inside:avoid}
  #maxess-results-10 .mx-dim-grid{grid-template-columns:repeat(5,1fr)!important;gap:8px!important}
  #maxess-results-10 .mx-dim{min-height:190px!important;padding:10px!important;background:#fff!important;color:#111!important;border:1px solid #bbb!important;box-shadow:none!important}
  #maxess-results-10 .mx-dim::before,#maxess-results-10 .mx-dim::after{display:none!important}
  #maxess-results-10 .mx-dim-head{margin-top:0!important}
  #maxess-results-10 .mx-dim-head h3,#maxess-results-10 .mx-dim-head strong,#maxess-results-10 .mx-lever b{color:#111!important}
  #maxess-results-10 .mx-dim p,#maxess-results-10 .mx-section-head p{color:#333!important}
  #maxess-results-10 .mx-area,#maxess-results-10 .mx-naya-door{break-inside:avoid!important}
  #maxess-results-10 #naya-report{break-inside:avoid!important}
}
'''

JS = r'''
(function(){
  'use strict';
  const root=document.getElementById('maxess-results-10');
  if(!root || root.dataset.nayaLawAaaPass2==='1') return;
  root.dataset.nayaLawAaaPass2='1';
  const q=s=>root.querySelector(s);
  const qa=s=>Array.from(root.querySelectorAll(s));
  const result=()=>window.MAXESS_RESULT||{};
  const getScore=()=>{const r=result();const n=Number(r.masterScore??r.overallScore??r.overall??r.score??r.resonance);return Number.isFinite(n)?Math.max(0,Math.min(100,n)):0};
  const colors=['#ff9d3d','#ffd84a','#38df91','#3c9cff','#965dff'];
  function orbPalette(v){if(v<50)return['#ff4b55','#ff9d3d'];if(v<65)return['#ff9d3d','#ffd84a'];if(v<75)return['#ffd84a','#38df91'];if(v<85)return['#38df91','#36d9d1'];if(v<90)return['#36d9d1','#3c9cff'];if(v<95)return['#3c9cff','#965dff'];return['#965dff','#ef4bc8']}
  function applyScore(){const orb=q('.mx-score-orb');if(!orb)return;const v=getScore(),p=orbPalette(v);orb.style.setProperty('--nl-orb-a',p[0]);orb.style.setProperty('--nl-orb-b',p[1]);orb.style.filter=`drop-shadow(0 0 ${Math.round(26+v*.28)}px ${p[0]}55)`;root.style.setProperty('--nl-score',v)}
  function applyDimensions(){
    qa('.mx-dim').forEach((card,i)=>{const raw=Number(card.getAttribute('data-score')||0);const v=Math.max(0,Math.min(100,raw));card.style.setProperty('--score',v);card.style.setProperty('--g',colors[i%colors.length]);card.setAttribute('tabindex','0');card.setAttribute('role','article');const s=card.querySelector('.mx-dim-head strong');if(s)s.setAttribute('aria-label',`Score ${v}`)})
  }
  function addPrint(){const hero=q('.mx-hero');if(!hero||q('.nl-print'))return;const host=q('.mx-hero-actions')||hero;const b=document.createElement('button');b.type='button';b.className='nl-print';b.innerHTML='Print / Save PDF <span aria-hidden="true">↗</span>';b.addEventListener('click',()=>window.print());host.appendChild(b)}
  function improveNayaButton(){const b=document.getElementById('mx-naya-listen');if(!b)return;b.innerHTML='Listen to your results <span aria-hidden="true">▶</span>';b.setAttribute('aria-label','Listen to your results with Naya')}
  function reducePatternRepetition(){qa('button,.mx-cta').forEach(b=>{const t=(b.textContent||'').trim();if(/^see\s+the\s+pattern/i.test(t))b.textContent='See your results'})}
  function enhanceNayaMasters(){qa('.mx-naya-door,.mx-area').forEach((el,i)=>{el.style.setProperty('--naya-index',i+1);el.setAttribute('tabindex','0')})}
  function init(){applyScore();applyDimensions();addPrint();improveNayaButton();reducePatternRepetition();enhanceNayaMasters()}
  if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',init,{once:true});else init();
  window.addEventListener('maxess:result-ready',applyScore);
})();
'''


def inject(text: str) -> str:
    if MARK in text:
        return text
    block=f'<!-- {MARK} --><style id="naya-law-aaa-pass-2-css">{CSS}</style><script id="naya-law-aaa-pass-2-js">{JS}</script>'
    if '</body>' in text:
        return text.replace('</body>', block+'</body>', 1)
    return text+block

for name in FILES:
    p=Path(name)
    if not p.exists():
        continue
    old=p.read_text(encoding='utf-8')
    new=inject(old)
    if new!=old:
        p.write_text(new,encoding='utf-8')
        print(f'applied {name}')
    else:
        print(f'already present {name}')
