from pathlib import Path

MARK = 'MAXESS-RECOGNITION-FLOW-10.4'
FILES = [
    'MAXESS-RESULTS-10-GROOVE.html',
    'MAXESS-RESULTS-FINAL-GROOVE.html',
    'MAXESS-RESULTS-GROOVE-EMBED.html',
    'MAXESS-RESULTS-FINAL-GROOVE-EMBED.html',
    'MAXESS-RESULTS-GROOVE-EMBED-9.95.html',
]

CSS = r'''
/* MAXESS 10.4 — recognition-first visual system */
#maxess-results-10{--r-bg:#030305;--r-panel:rgba(255,255,255,.045);--r-line:rgba(255,255,255,.13);--r-white:#fff;--r-muted:rgba(255,255,255,.62);--r-violet:#9b63ff;--r-cyan:#55e6ff;--r-gold:#ffd47a;background:radial-gradient(ellipse 70% 38% at 50% 0,rgba(115,54,190,.28),transparent 72%),linear-gradient(180deg,#09050d 0,#030305 46%,#020204 100%);}
#maxess-results-10 .mx-wide{width:100%;max-width:none;margin:0;padding-left:clamp(28px,5vw,110px);padding-right:clamp(28px,5vw,110px)}
#maxess-results-10 .mx-section{width:100%;}
#maxess-results-10 .mx-hero{min-height:clamp(760px,92vh,980px);padding-top:clamp(50px,6vw,90px);padding-bottom:clamp(54px,6vw,90px)}
#maxess-results-10 .mx-hero-grid{width:100%;max-width:1700px;margin:auto;display:flex;flex-direction:column;align-items:center;gap:26px;text-align:center}
#maxess-results-10 .mx-hero-grid .mx-score-orb{order:-2;width:min(620px,64vw);min-width:340px;margin:0 auto;filter:drop-shadow(0 0 42px rgba(117,61,210,.2));}
#maxess-results-10 .mx-hero-grid>div:not(.mx-score-orb){width:min(1100px,100%);}
#maxess-results-10 .mx-hero .mx-title{font-size:clamp(42px,6vw,86px);max-width:1000px;margin:12px auto 0}
#maxess-results-10 .mx-hero .mx-copy{margin:18px auto 0;max-width:760px;color:var(--r-muted)}
#maxess-results-10 .mx-hero-actions{justify-content:center}
#maxess-results-10 .mx-cta{border-radius:18px;border:1px solid rgba(255,255,255,.18);box-shadow:inset 0 1px rgba(255,255,255,.34),0 18px 45px rgba(0,0,0,.3);}
#maxess-results-10 .mx-cta-primary{background:linear-gradient(135deg,#b58aff 0,#6331b5 48%,#241037 100%);}
#maxess-results-10 .mx-cta-ghost{background:linear-gradient(145deg,rgba(255,255,255,.09),rgba(255,255,255,.025));}
#maxess-results-10 .mx-recognition-naya{width:min(980px,100%);padding:18px 20px;border:1px solid rgba(85,230,255,.2);border-radius:22px;background:linear-gradient(110deg,rgba(85,230,255,.07),rgba(155,99,255,.08),rgba(255,255,255,.025));box-shadow:0 24px 70px rgba(0,0,0,.28),inset 0 1px rgba(255,255,255,.12);display:flex;align-items:center;justify-content:space-between;gap:18px;text-align:left}
#maxess-results-10 .mx-recognition-naya .rn-copy{display:grid;gap:3px}
#maxess-results-10 .mx-recognition-naya .rn-kicker{font-size:10px;letter-spacing:.18em;font-weight:900;color:rgba(85,230,255,.82)}
#maxess-results-10 .mx-recognition-naya .rn-title{font-size:clamp(18px,2vw,25px);font-weight:800;letter-spacing:-.025em}
#maxess-results-10 .mx-recognition-naya .rn-sub{font-size:13px;color:var(--r-muted)}
#maxess-results-10 .mx-pattern{padding-top:22px;padding-bottom:clamp(50px,6vw,86px)}
#maxess-results-10 .mx-pattern-head{text-align:center;margin-bottom:28px}
#maxess-results-10 .mx-pattern-head h2{margin:9px 0 0;font-size:clamp(32px,4.4vw,64px);letter-spacing:-.045em;line-height:.98}
#maxess-results-10 .mx-pattern-head p{max-width:680px;margin:14px auto 0;color:var(--r-muted)}
#maxess-results-10 .mx-constellation{position:relative;width:min(1220px,100%);min-height:360px;margin:auto;display:grid;grid-template-columns:repeat(5,1fr);gap:16px;align-items:center}
#maxess-results-10 .mx-constellation::before{content:"";position:absolute;left:10%;right:10%;top:50%;height:1px;background:linear-gradient(90deg,transparent,rgba(155,99,255,.35),rgba(85,230,255,.45),rgba(155,99,255,.35),transparent);box-shadow:0 0 24px rgba(85,230,255,.12)}
#maxess-results-10 .mx-node{position:relative;z-index:1;min-height:190px;padding:20px 14px;border-radius:50%;aspect-ratio:1;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;border:1px solid rgba(255,255,255,.15);background:radial-gradient(circle at 35% 25%,rgba(255,255,255,.15),rgba(155,99,255,.09) 35%,rgba(3,3,5,.92) 75%);box-shadow:inset 0 1px rgba(255,255,255,.2),0 22px 50px rgba(0,0,0,.35);transition:transform .25s ease,box-shadow .25s ease,border-color .25s ease}
#maxess-results-10 .mx-node:hover{transform:translateY(-8px) scale(1.035);border-color:rgba(85,230,255,.42);box-shadow:inset 0 1px rgba(255,255,255,.25),0 28px 65px rgba(0,0,0,.48),0 0 34px rgba(85,230,255,.11)}
#maxess-results-10 .mx-node .rn-dot{width:10px;height:10px;border-radius:50%;background:linear-gradient(135deg,var(--r-cyan),var(--r-violet));box-shadow:0 0 18px rgba(85,230,255,.6);margin-bottom:10px}
#maxess-results-10 .mx-node b{font-size:13px;line-height:1.15}
#maxess-results-10 .mx-node strong{font-size:31px;line-height:1;margin-top:8px}
#maxess-results-10 .mx-node small{color:var(--r-muted);font-size:9px;margin-top:7px;max-width:115px}
#maxess-results-10 .mx-naya-bridge{padding-top:clamp(38px,5vw,70px);padding-bottom:clamp(38px,5vw,70px)}
#maxess-results-10 .mx-naya-bridge .mx-reading{width:min(1180px,100%);margin:auto}
#maxess-results-10 .mx-naya-bridge .mx-bridge-card{border-radius:30px;border:1px solid rgba(85,230,255,.18);background:linear-gradient(135deg,rgba(85,230,255,.06),rgba(155,99,255,.09),rgba(255,255,255,.025));box-shadow:0 30px 90px rgba(0,0,0,.36),inset 0 1px rgba(255,255,255,.13)}
#maxess-results-10 #your-fingerprint{padding-top:clamp(42px,5vw,80px)}
#maxess-results-10 #your-fingerprint .mx-section-head{align-items:center}
#maxess-results-10 #your-fingerprint .mx-section-head h2{font-size:clamp(36px,5vw,72px)}
#maxess-results-10 #growth-scorecard{padding-top:clamp(46px,5vw,82px)}
#maxess-results-10 #growth-scorecard .mx-section-head h2{font-size:clamp(34px,4.5vw,64px)}
#maxess-results-10 .mx-naya-playground{padding-top:clamp(50px,6vw,96px)}
#maxess-results-10 .mx-naya-doors{grid-template-columns:repeat(3,minmax(0,1fr));gap:24px}
#maxess-results-10 .mx-naya-door{border-radius:32px;border:1px solid rgba(255,255,255,.14);background:linear-gradient(145deg,rgba(255,255,255,.075),rgba(255,255,255,.018));box-shadow:inset 0 1px rgba(255,255,255,.18),0 30px 90px rgba(0,0,0,.4);transition:transform .25s ease,box-shadow .25s ease,border-color .25s ease}
#maxess-results-10 .mx-naya-door:hover{transform:translateY(-8px);border-color:rgba(85,230,255,.28);box-shadow:inset 0 1px rgba(255,255,255,.2),0 38px 105px rgba(0,0,0,.52),0 0 55px rgba(85,230,255,.08)}
#maxess-results-10 .mx-naya-icon{filter:saturate(1.2) drop-shadow(0 0 10px rgba(85,230,255,.15))}
#maxess-results-10 .mx-eyebrow{color:rgba(255,255,255,.68)!important}
#maxess-results-10 [style*="#ff"],[style*="magenta"],[style*="hotpink"]{color:inherit!important}
@media(max-width:900px){#maxess-results-10 .mx-hero-grid .mx-score-orb{width:min(470px,82vw);min-width:270px}#maxess-results-10 .mx-recognition-naya{flex-direction:column;align-items:stretch}.mx-recognition-naya .mx-cta{width:100%}#maxess-results-10 .mx-constellation{grid-template-columns:repeat(2,1fr);min-height:0}.mx-constellation::before{display:none}.mx-node{min-height:170px}.mx-node:last-child{grid-column:1/-1;width:50%;margin:auto}#maxess-results-10 .mx-naya-doors{grid-template-columns:1fr}}
@media(max-width:560px){#maxess-results-10 .mx-wide{padding-left:16px;padding-right:16px}#maxess-results-10 .mx-hero{min-height:auto;padding-top:42px}#maxess-results-10 .mx-constellation{gap:10px}.mx-node{min-height:145px}.mx-node strong{font-size:26px}}
@media(prefers-reduced-motion:reduce){#maxess-results-10 .mx-node,#maxess-results-10 .mx-naya-door,#maxess-results-10 .mx-cta{transition:none!important}}
'''

JS = r'''
(function(){
  'use strict';
  const root=document.getElementById('maxess-results-10');
  if(!root || root.dataset.recognitionFlow104==='1') return;
  root.dataset.recognitionFlow104='1';

  function addStyle(){
    if(document.getElementById('maxess-recognition-flow-10-4')) return;
    const s=document.createElement('style');s.id='maxess-recognition-flow-10-4';s.textContent=CSS_PLACEHOLDER;s.textContent=s.textContent.replace(/\\n/g,'\n');document.head.appendChild(s);
  }
  function resultData(){
    const r=window.MAXESS_RESULT||{};
    let dims=r.dimensions||r.dimensionScores||{};
    if(Array.isArray(dims)){const o={};dims.forEach(x=>{if(x)o[x.name||x.label||('Dimension '+(Object.keys(o).length+1))]=x.score??x.value??0});dims=o}
    const entries=Object.entries(dims).slice(0,5);
    const fallback=[['Presence',82],['Clarity',78],['Power',74],['Grace',86],['Execution',71]];
    return entries.length===5?entries:fallback;
  }
  function move(id,parent,before){const el=document.getElementById(id);if(!el||!parent)return el;if(before)parent.insertBefore(el,before);else parent.appendChild(el);return el}
  function buildNaya(){
    const hero=root.querySelector('.mx-hero'); if(!hero)return;
    if(!hero.querySelector('.mx-recognition-naya')){
      const box=document.createElement('div');box.className='mx-recognition-naya';box.innerHTML='<div class="rn-copy"><span class="rn-kicker">NAYA IS HERE</span><span class="rn-title">Let Naya walk you through what your result means.</span><span class="rn-sub">Your score is the signal. Your pattern is the story.</span></div><button class="mx-cta mx-cta-primary" type="button" id="mx-naya-hero-listen">Listen to Naya <span aria-hidden="true">▶</span></button>';
      hero.querySelector('.mx-hero-grid')?.appendChild(box);
      box.querySelector('button').addEventListener('click',function(){
        const existing=document.getElementById('mx-naya-listen');
        if(existing) existing.click(); else window.dispatchEvent(new CustomEvent('maxess:naya-report'));
      });
    }
  }
  function buildPattern(){
    const fp=document.getElementById('your-fingerprint');if(!fp||document.getElementById('maxess-pattern-10-4'))return;
    const s=document.createElement('section');s.className='mx-section mx-pattern';s.id='maxess-pattern-10-4';
    const dims=resultData();
    s.innerHTML='<div class="mx-wide"><div class="mx-pattern-head"><span class="mx-eyebrow">02 · YOUR LIVING SIGNATURE</span><h2>See the pattern, not the score.</h2><p>Five signals. One you. Naya uses the relationships between them to reveal how you naturally work with AI.</p></div><div class="mx-constellation" role="list" aria-label="Five dimension signature">'+dims.map((d,i)=>'<div class="mx-node" role="listitem"><span class="rn-dot" aria-hidden="true"></span><b>'+esc(d[0])+'</b><strong>'+Math.round(Number(d[1])||0)+'</strong><small>'+dimensionCopy(d[0],i)+'</small></div>').join('')+'</div></div>';
    fp.parentNode.insertBefore(s,fp);
  }
  function dimensionCopy(name,i){const n=String(name).toLowerCase();if(n.includes('commun'))return 'How naturally you turn thoughts into useful words.';if(n.includes('clar'))return 'How clearly you direct and evaluate AI.';if(n.includes('power'))return 'How effectively you turn AI into action.';if(n.includes('grace'))return 'How naturally you adapt, connect and create.';if(n.includes('execut'))return 'How consistently you turn ideas into outcomes.';return ['Your natural signal.','How you direct your thinking.','Where your leverage lives.','Your adaptive strength.','How you turn insight into action.'][i]||'Part of your unique AI pattern.'}
  function esc(v){return String(v).replace(/[&<>"']/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]})}
  function reorder(){
    const hero=root.querySelector('.mx-hero'),naya=document.getElementById('naya-report'),fp=document.getElementById('your-fingerprint'),growth=document.getElementById('growth-scorecard'),play=document.getElementById('naya-playground');
    if(!hero)return;
    buildNaya();
    if(naya)root.insertBefore(naya,hero.nextElementSibling);
    buildPattern();
    const pattern=document.getElementById('maxess-pattern-10-4');
    if(pattern)root.insertBefore(pattern,fp||null);
    if(fp)root.insertBefore(fp,growth||play||null);
    if(growth)root.insertBefore(growth,play||null);
    if(play)root.appendChild(play);
    [...root.querySelectorAll('section')].forEach(sec=>{const t=(sec.textContent||'').toLowerCase();if(/ledger|ai capability shapes your life/.test(t)&&!sec.matches('#maxess-pattern-10-4,.mx-hero,#your-fingerprint,#growth-scorecard,#naya-report,#naya-playground'))sec.hidden=true});
    const h=fp?.querySelector('.mx-section-head h2');if(h)h.innerHTML='See the pattern,<br>not just the score.';
    const ne=naya?.querySelector('.mx-audio-label');if(ne)ne.textContent='NAYA · PERSONAL WELCOME';
  }
  function boot(){addStyle();reorder();}
  if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',boot,{once:true});else boot();
})();
'''

# Embed CSS directly in JS safely; this keeps the generated artifact self-contained.
JS = JS.replace('CSS_PLACEHOLDER', CSS.replace('\\','\\\\').replace('`','\\`').replace('${','\\${'))

BLOCK = '<style id="maxess-recognition-flow-10-4">' + CSS + '</style><script id="maxess-recognition-flow-10-4-js">' + JS + '</script>'

for name in FILES:
    p=Path(name)
    if not p.exists():
        continue
    text=p.read_text(encoding='utf-8')
    if MARK in text:
        continue
    insert='\n<!-- '+MARK+' -->\n'+BLOCK+'\n'
    if '</body>' in text:
        text=text.replace('</body>',insert+'</body>',1)
    elif '</html>' in text:
        text=text.replace('</html>',insert+'</html>',1)
    else:
        text+=insert
    p.write_text(text,encoding='utf-8')
