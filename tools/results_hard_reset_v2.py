from pathlib import Path

p = Path('code')
s = p.read_text(encoding='utf-8')
MARK = 'MAXESS RESULTS HARD RESET V2'
if MARK in s:
    print('Hard reset V2 already present')
    raise SystemExit(0)

CSS = r'''
/* =========================================================
   MAXESS RESULTS HARD RESET V2
   Fresh presentation owns everything after the proven hero.
========================================================= */
#resultsView.results-hard-reset-v2 > :not(.result-hero):not(.maxess-fresh-results){display:none !important;}
#resultsView.results-hard-reset-v2 .maxess-fresh-results{display:block !important;width:100%;}
#resultsView.results-hard-reset-v2 .result-hero{background:transparent !important;border:0 !important;box-shadow:none !important;overflow:visible !important;}
.fresh-section{position:relative;width:100%;margin:0 auto;padding:clamp(56px,7vw,104px) clamp(12px,3vw,40px);}
.fresh-kicker{font-size:10px;letter-spacing:.18em;text-transform:uppercase;font-weight:950;color:#b895ff;margin-bottom:14px;}
.fresh-title{margin:0;font-size:clamp(32px,5vw,64px);line-height:.98;letter-spacing:-.04em;font-weight:950;color:#fff;}
.fresh-copy{margin:18px 0 0;max-width:760px;color:#b6b1be;font-size:clamp(15px,1.8vw,20px);line-height:1.65;}
.fresh-analysis{display:grid;grid-template-columns:minmax(0,1.35fr) minmax(280px,.65fr);gap:34px;align-items:end;border-top:1px solid rgba(255,255,255,.08);}
.fresh-lead{font-size:clamp(20px,2.8vw,34px);line-height:1.25;font-weight:800;color:#f8f7fb;max-width:880px;}
.fresh-lead em{font-style:normal;color:#b895ff;}
.fresh-points{display:grid;gap:14px;}
.fresh-point{padding:18px 0;border-bottom:1px solid rgba(255,255,255,.08);}
.fresh-point span{display:block;font-size:9px;letter-spacing:.14em;text-transform:uppercase;font-weight:900;color:#7f7a88;margin-bottom:7px;}
.fresh-point strong{display:block;font-size:22px;line-height:1.1;color:#fff;}
.fresh-point p{margin:6px 0 0;color:#a9a5b1;font-size:13px;line-height:1.45;}
.fresh-signature{border-top:1px solid rgba(255,255,255,.08);}
.fresh-radar-wrap{margin-top:36px;display:grid;grid-template-columns:minmax(320px,1fr) minmax(260px,.7fr);gap:36px;align-items:center;}
.fresh-radar{width:100%;max-width:640px;margin:auto;}
.fresh-radar svg{display:block;width:100%;height:auto;overflow:visible;}
.fresh-radar .grid{fill:none;stroke:rgba(255,255,255,.08);stroke-width:1;}
.fresh-radar .axis{stroke:rgba(255,255,255,.06);stroke-width:1;}
.fresh-radar .shape{fill:rgba(138,92,255,.17);stroke:#b895ff;stroke-width:2;}
.fresh-radar .point{fill:#fff;stroke:#b895ff;stroke-width:2;}
.fresh-radar .label{fill:#a9a5b1;font:900 11px system-ui,sans-serif;letter-spacing:.03em;}
.fresh-read{display:grid;gap:16px;}
.fresh-read-item{padding:18px 0;border-top:1px solid rgba(255,255,255,.08);}
.fresh-read-item span{font-size:9px;letter-spacing:.14em;text-transform:uppercase;font-weight:900;color:#8d859a;}
.fresh-read-item strong{display:block;margin-top:8px;font-size:24px;color:#fff;}
.fresh-read-item p{margin:6px 0 0;color:#aaa5b2;font-size:13px;line-height:1.5;}
.fresh-process{border-top:1px solid rgba(255,255,255,.08);text-align:center;}
.fresh-line{margin-top:34px;display:flex;flex-wrap:wrap;justify-content:center;align-items:center;gap:8px 10px;}
.fresh-line span{display:inline-flex;align-items:center;justify-content:center;min-width:92px;padding:13px 14px;border-radius:999px;border:1px solid rgba(181,140,255,.24);background:linear-gradient(180deg,rgba(138,92,255,.12),rgba(255,255,255,.025));color:#f7f4fb;font-size:11px;letter-spacing:.11em;font-weight:950;box-shadow:inset 0 1px 0 rgba(255,255,255,.07);}
.fresh-line b{color:#6d6678;font-size:14px;}
.fresh-naya{border-top:1px solid rgba(255,255,255,.08);display:grid;grid-template-columns:auto 1fr;gap:24px;align-items:center;max-width:980px;margin:0 auto;}
.fresh-naya-orb{width:88px;height:88px;border-radius:50%;display:grid;place-items:center;font-size:34px;font-weight:950;color:#fff;background:radial-gradient(circle at 30% 20%,#fff 0,#e1d5ff 12%,#9a73ff 38%,#3b1b83 68%,#07030e 100%);border:1px solid rgba(255,255,255,.65);box-shadow:inset 0 2px 6px rgba(255,255,255,.55),0 0 34px rgba(138,92,255,.28);}
.fresh-naya h3{margin:0;font-size:clamp(24px,3vw,40px);line-height:1.08;color:#fff;}
.fresh-naya p{margin:10px 0 0;color:#aaa5b2;font-size:15px;line-height:1.6;max-width:720px;}
.fresh-masters{border-top:1px solid rgba(255,255,255,.08);}
.fresh-master-stage{margin-top:34px;display:grid;grid-template-columns:1.35fr 1fr;gap:18px;align-items:stretch;}
.fresh-master-main,.fresh-master-side{border:1px solid rgba(255,255,255,.10);background:linear-gradient(180deg,rgba(255,255,255,.035),rgba(255,255,255,.012));}
.fresh-master-main{padding:34px;min-height:280px;display:flex;flex-direction:column;justify-content:end;border-radius:30px;background:radial-gradient(circle at 18% 12%,rgba(138,92,255,.2),transparent 35%),linear-gradient(180deg,rgba(138,92,255,.06),rgba(255,255,255,.012));}
.fresh-master-side{display:grid;grid-template-rows:1fr 1fr;border-radius:30px;overflow:hidden;}
.fresh-master-side article{padding:28px;border-bottom:1px solid rgba(255,255,255,.08);}
.fresh-master-side article:last-child{border-bottom:0;}
.fresh-jewel{width:62px;height:62px;border-radius:20px;display:grid;place-items:center;margin-bottom:28px;color:#fff;font-size:25px;border:1px solid rgba(255,255,255,.55);box-shadow:inset 0 2px 5px rgba(255,255,255,.45),0 10px 24px rgba(0,0,0,.45);}
.fresh-jewel.purple{background:radial-gradient(circle at 30% 20%,#fff 0,#ddd0ff 14%,#8a5cff 45%,#160c2b 100%);}
.fresh-jewel.blue{background:radial-gradient(circle at 30% 20%,#fff 0,#d9e9ff 14%,#3ca8ff 45%,#07111d 100%);}
.fresh-jewel.green{background:radial-gradient(circle at 30% 20%,#fff 0,#d8ffe9 14%,#35e39b 45%,#06130c 100%);}
.fresh-master-main h3,.fresh-master-side h4{margin:0;color:#fff;}
.fresh-master-main h3{font-size:clamp(28px,3.7vw,52px);line-height:1.02;}
.fresh-master-side h4{font-size:22px;line-height:1.1;}
.fresh-role{margin-top:10px;color:#b895ff;font-size:10px;letter-spacing:.12em;text-transform:uppercase;font-weight:900;}
.fresh-master-main p,.fresh-master-side p{margin:12px 0 0;color:#a9a5b2;line-height:1.55;font-size:13px;max-width:620px;}
.fresh-next{border-top:1px solid rgba(255,255,255,.08);padding-bottom:80px;text-align:center;}
.fresh-actions{display:flex;justify-content:center;gap:12px;flex-wrap:wrap;margin-top:28px;}
.fresh-actions button{min-width:180px;min-height:54px;padding:0 22px;border-radius:18px;font-weight:950;cursor:pointer;transition:transform .2s ease,box-shadow .2s ease;}
.fresh-actions button:hover{transform:translateY(-2px);}
.fresh-primary{border:1px solid rgba(181,140,255,.75);background:linear-gradient(180deg,#15131b,#08080b);color:#fff;box-shadow:0 12px 30px rgba(0,0,0,.5),0 0 28px rgba(138,92,255,.12);}
.fresh-secondary{border:1px solid rgba(255,255,255,.14);background:transparent;color:#c9c4d0;}
@media (max-width:760px){.fresh-analysis,.fresh-radar-wrap,.fresh-master-stage{grid-template-columns:1fr}.fresh-master-main{min-height:240px}.fresh-naya{grid-template-columns:1fr}.fresh-naya-orb{width:72px;height:72px;font-size:28px}.fresh-section{padding:46px 8px 72px}.fresh-line{gap:7px}.fresh-line span{min-width:78px;padding:11px 10px;font-size:10px}}
@media (prefers-reduced-motion:reduce){.fresh-actions button{transition:none;}}
'''

JS = r'''
/* =========================================================
   MAXESS RESULTS HARD RESET V2
========================================================= */
(function(){
  const root=document.getElementById('resultsView');
  if(!root) return;
  const marker='maxessFreshResultsV2';
  const esc=v=>String(v==null?'':v).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
  const band=s=>s>=90?'MASTER':s>=75?'ADVANCING':s>=60?'DEVELOPING':'FOUNDATION';
  const readDims=()=>[...root.querySelectorAll('#dimensionConstellation .dimension-orb')].map((el,i)=>({name:el.querySelector('.dimension-name')?.textContent?.trim()||['Direction','Communication','Evaluation','Iteration','Systems Thinking'][i]||'Dimension',score:Number(el.querySelector('.dimension-score')?.textContent||0)}));
  const radar=ds=>{const safe=ds.slice(0,5),cx=300,cy=220,r=150,n=5;const pt=(i,rr)=>{const a=-Math.PI/2+i*2*Math.PI/n;return [cx+Math.cos(a)*rr,cy+Math.sin(a)*rr]};const poly=f=>safe.map((_,i)=>pt(i,r*f).join(',')).join(' ');const shape=safe.map((d,i)=>pt(i,r*Math.max(.08,d.score/100)).join(',')).join(' ');const axes=safe.map((_,i)=>{const p=pt(i,r);return `<line class="axis" x1="${cx}" y1="${cy}" x2="${p[0]}" y2="${p[1]}"/>`}).join('');const labels=safe.map((d,i)=>{const p=pt(i,r+34);return `<text class="label" x="${p[0]}" y="${p[1]}" text-anchor="middle">${esc(d.name)}</text>`}).join('');const pts=safe.map((d,i)=>{const p=pt(i,r*Math.max(.08,d.score/100));return `<circle class="point" cx="${p[0]}" cy="${p[1]}" r="5"/>`}).join('');return `<svg viewBox="0 0 600 440" role="img" aria-label="AI capability fingerprint">${[.25,.5,.75,1].map(f=>`<polygon class="grid" points="${poly(f)}"/>`).join('')}${axes}<polygon class="shape" points="${shape}"/>${pts}${labels}</svg>`};
  const mount=()=>{
    if(!root.classList.contains('visible')||root.dataset[marker]==='1') return;
    const hero=root.querySelector(':scope > .result-hero');if(!hero)return;
    const ds=readDims();if(!ds.length)return;ds.sort((a,b)=>b.score-a.score);
    const score=Math.round(Number(document.getElementById('overallScore')?.textContent||0));
    const hi=ds[0],lo=ds[ds.length-1];
    const analysis=document.getElementById('strongestText')?.textContent?.trim()||`Your strongest capability is ${hi.name}.`;
    root.classList.add('results-hard-reset-v2');
    root.querySelectorAll(':scope > *').forEach(el=>{if(el!==hero)el.classList.add('fresh-legacy-inert');});
    const out=document.createElement('div');out.className='maxess-fresh-results';
    out.innerHTML=`
      <section class="fresh-section fresh-analysis"><div><div class="fresh-kicker">YOUR PERSONALIZED ANALYSIS</div><p class="fresh-lead">${esc(analysis)} <em>Your next meaningful lift is in ${esc(lo.name).toLowerCase()}.</em></p></div><div class="fresh-points"><div class="fresh-point"><span>NATURAL ADVANTAGE</span><strong>${esc(hi.name)}</strong><p>${Math.round(hi.score)}/100 · your strongest capability.</p></div><div class="fresh-point"><span>HIGHEST LEVERAGE</span><strong>${esc(lo.name)}</strong><p>${Math.round(lo.score)}/100 · your clearest next opportunity.</p></div></div></section>
      <section class="fresh-section fresh-signature"><div class="fresh-kicker">YOUR AI CAPABILITY SIGNATURE</div><h2 class="fresh-title">The shape underneath your score.</h2><p class="fresh-copy">Five capabilities create a pattern. This is your AI fingerprint — visual first, understandable second.</p><div class="fresh-radar-wrap"><div class="fresh-radar">${radar(ds)}</div><div class="fresh-read"><div class="fresh-read-item"><span>Your strongest dimension</span><strong>${esc(hi.name)}</strong><p>${Math.round(hi.score)}/100 · ${band(hi.score)}.</p></div><div class="fresh-read-item"><span>Your highest-leverage opportunity</span><strong>${esc(lo.name)}</strong><p>${Math.round(lo.score)}/100 · where deliberate practice can create the most lift.</p></div><div class="fresh-read-item"><span>The question to carry forward</span><strong>What would make the next result a 10?</strong><p>Keep what works. Identify what doesn't. Improve deliberately.</p></div></div></div></section>
      <section class="fresh-section fresh-process"><div class="fresh-kicker">HOW YOU WORK WITH AI</div><h2 class="fresh-title">AI is the engine.<br><span style="color:#b895ff">You are the director.</span></h2><p class="fresh-copy">Know what you want. Give the context. Ask clearly. Look closely. Score the result. Improve it. Repeat.</p><div class="fresh-line">${['KNOW','TELL','ASK','LOOK','SCORE','IMPROVE','REPEAT'].map((x,i)=>`<span>${x}</span>${i<6?'<b>→</b>':''}`).join('')}</div></section>
      <section class="fresh-section fresh-naya"><div class="fresh-naya-orb">N</div><div><div class="fresh-kicker">NAYA · YOUR PERSONAL GUIDE</div><h3>Okay. Now we know where to look.</h3><p>${esc(lo.name)} is the place to experiment next. Start small. Judge the result honestly. Improve it deliberately. Let the win become a repeatable capability.</p></div></section>
      <section class="fresh-section fresh-masters"><div class="fresh-kicker">NAYA · MASTER INTELLIGENCE</div><h2 class="fresh-title">Specific work deserves specific mastery.</h2><p class="fresh-copy">Not a catalogue. A glimpse of the specialized intelligence available when you want to go deeper.</p><div class="fresh-master-stage"><article class="fresh-master-main"><div class="fresh-jewel purple">✦</div><div class="fresh-role">NAYA · MASTER SPECIALIST</div><h3>Naya Master ${esc(hi.name)}</h3><p>Start from the capability you already own. Use it as the foundation for what you build next.</p></article><div class="fresh-master-side"><article><div class="fresh-jewel blue">◆</div><div class="fresh-role">NAYA · MASTER SPECIALIST</div><h4>Naya Master ${esc(lo.name)}</h4><p>Practice the capability with the clearest leverage.</p></article><article><div class="fresh-jewel green">△</div><div class="fresh-role">NAYA · MASTER STRATEGIST</div><h4>Turn intent into action</h4><p>Use direction, priorities, and decisions to make the work move.</p></article></div></div></section>
      <section class="fresh-section fresh-next"><div class="fresh-kicker">YOUR NEXT CHAPTER</div><h2 class="fresh-title">Now make the capability real.</h2><p class="fresh-copy">Your result shows where you are. The next step is choosing what you want to build with it.</p><div class="fresh-actions"><button type="button" class="fresh-primary" data-fresh-go>MASTER AI →</button><button type="button" class="fresh-secondary" data-fresh-save>SAVE MY RESULTS</button></div></section>`;
    root.appendChild(out);
    out.querySelector('[data-fresh-go]')?.addEventListener('click',()=>document.getElementById('freeTrialButton')?.click());
    out.querySelector('[data-fresh-save]')?.addEventListener('click',()=>document.getElementById('pdfButton')?.click());
    root.dataset[marker]='1';
  };
  new MutationObserver(mount).observe(root,{attributes:true,attributeFilter:['class'],childList:true,subtree:true});
  mount();
})();
'''

if '</style>' not in s or '</script>' not in s:
    raise RuntimeError('MAXESS document anchors missing')
if MARK not in s:
    s=s.replace('</style>',f'\n<!-- {MARK} -->\n'+CSS+'\n</style>',1)
pos=s.rfind('</script>')
s=s[:pos]+'\n'+JS+'\n'+s[pos:]
p.write_text(s,encoding='utf-8')
print('Applied MAXESS Results hard reset V2')
