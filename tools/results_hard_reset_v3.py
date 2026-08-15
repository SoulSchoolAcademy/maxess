from pathlib import Path

p = Path('code')
s = p.read_text(encoding='utf-8')
MARK = 'MAXESS RESULTS HARD RESET V3'
if MARK in s:
    print('Hard reset V3 already present')
    raise SystemExit(0)

CSS = r'''
/* =========================================================
   MAXESS RESULTS HARD RESET V3
   Replace the entire Results presentation with a clean slate.
========================================================= */
.results-v3{width:100%;color:#fff;background:
  radial-gradient(circle at 50% 0%,rgba(138,92,255,.13),transparent 34%),
  linear-gradient(180deg,#050507 0%,#020204 100%);}
.results-v3 *{box-sizing:border-box;}
.r3-wrap{width:min(1120px,100%);margin:0 auto;padding:clamp(28px,5vw,70px) clamp(18px,4vw,56px) 100px;}
.r3-kicker{font-size:10px;letter-spacing:.18em;text-transform:uppercase;color:#b895ff;font-weight:950;margin-bottom:14px;}
.r3-title{margin:0;font-size:clamp(38px,6.5vw,78px);line-height:.94;letter-spacing:-.055em;font-weight:950;}
.r3-copy{margin:18px 0 0;max-width:760px;color:#aaa6b2;font-size:clamp(15px,1.8vw,19px);line-height:1.6;}
.r3-hero{padding:28px 0 54px;text-align:center;}
.r3-hero h1{margin:0;font-size:clamp(42px,7vw,88px);line-height:.92;letter-spacing:-.06em;font-weight:950;}
.r3-hero h1 span{color:#b895ff;}
.r3-hero p{max-width:720px;margin:20px auto 0;color:#b8b2bf;font-size:clamp(16px,2vw,21px);line-height:1.55;}
.r3-gauge{margin:34px auto 0;max-width:560px;}
.r3-gauge svg{display:block;width:100%;height:auto;overflow:visible;}
.r3-gauge .track{fill:none;stroke:rgba(255,255,255,.09);stroke-width:24;stroke-linecap:round;}
.r3-gauge .fill{fill:none;stroke:url(#r3Gauge);stroke-width:24;stroke-linecap:round;filter:drop-shadow(0 0 14px rgba(138,92,255,.35));}
.r3-gauge .tick{stroke:rgba(255,255,255,.18);stroke-width:2;}
.r3-gauge .needle{stroke:#fff;stroke-width:5;stroke-linecap:round;filter:drop-shadow(0 0 8px rgba(255,255,255,.6));}
.r3-gauge .hub{fill:#fff;stroke:#8a5cff;stroke-width:7;}
.r3-gauge .score{fill:#fff;font:950 54px system-ui,sans-serif;letter-spacing:-.05em;}
.r3-gauge .label{fill:#aaa6b2;font:950 10px system-ui,sans-serif;letter-spacing:.16em;}
.r3-band{margin-top:-2px;color:#b895ff;font-size:11px;letter-spacing:.16em;text-transform:uppercase;font-weight:950;}
.r3-panel{padding:72px 0;border-top:1px solid rgba(255,255,255,.09);}
.r3-analysis{display:grid;grid-template-columns:minmax(0,1.35fr) minmax(260px,.65fr);gap:50px;align-items:end;}
.r3-analysis-lead{margin:0;font-size:clamp(25px,3.6vw,46px);line-height:1.08;letter-spacing:-.035em;font-weight:850;color:#fff;}
.r3-analysis-lead em{font-style:normal;color:#b895ff;}
.r3-meaning{display:grid;gap:20px;}
.r3-meaning-item{padding-top:18px;border-top:1px solid rgba(255,255,255,.08);}
.r3-meaning-item span{display:block;color:#7e7888;font-size:9px;text-transform:uppercase;letter-spacing:.14em;font-weight:950;}
.r3-meaning-item strong{display:block;margin-top:7px;color:#fff;font-size:24px;line-height:1.05;}
.r3-meaning-item small{display:block;margin-top:6px;color:#9e99a6;font-size:12px;line-height:1.45;}
.r3-fingerprint{display:grid;grid-template-columns:minmax(0,1fr) minmax(260px,.72fr);gap:50px;align-items:center;}
.r3-radar svg{display:block;width:100%;max-width:650px;margin:auto;}
.r3-radar .grid{fill:none;stroke:rgba(255,255,255,.08);stroke-width:1;}
.r3-radar .axis{stroke:rgba(255,255,255,.06);stroke-width:1;}
.r3-radar .shape{fill:rgba(138,92,255,.19);stroke:#b895ff;stroke-width:2.5;filter:drop-shadow(0 0 12px rgba(138,92,255,.18));}
.r3-radar .point{fill:#fff;stroke:#8a5cff;stroke-width:3;}
.r3-radar .label{fill:#a9a5b1;font:950 11px system-ui,sans-serif;}
.r3-read{display:grid;gap:20px;}
.r3-read article{padding:20px 0;border-top:1px solid rgba(255,255,255,.08);}
.r3-read article span{display:block;color:#817b8b;font-size:9px;letter-spacing:.14em;text-transform:uppercase;font-weight:950;}
.r3-read article h3{margin:8px 0 0;font-size:27px;line-height:1.02;color:#fff;}
.r3-read article p{margin:8px 0 0;color:#a39eaa;font-size:13px;line-height:1.5;}
.r3-process{text-align:center;}
.r3-process h2,.r3-naya h2,.r3-masters h2,.r3-next h2{margin:0;font-size:clamp(30px,4.6vw,56px);line-height:.98;letter-spacing:-.045em;font-weight:950;}
.r3-process h2 em{font-style:normal;color:#b895ff;}
.r3-process-line{display:flex;flex-wrap:wrap;justify-content:center;gap:10px;margin-top:32px;}
.r3-process-line .step{display:inline-flex;align-items:center;gap:9px;padding:12px 15px;border-radius:999px;border:1px solid rgba(181,140,255,.24);background:linear-gradient(180deg,rgba(138,92,255,.11),rgba(255,255,255,.025));box-shadow:inset 0 1px 0 rgba(255,255,255,.07);font-size:11px;letter-spacing:.11em;font-weight:950;}
.r3-process-line .gem{width:18px;height:18px;border-radius:50%;display:grid;place-items:center;font-size:10px;background:radial-gradient(circle at 30% 20%,#fff,#a980ff 34%,#35156e 72%,#07030d 100%);}
.r3-naya{display:grid;grid-template-columns:auto 1fr;gap:28px;align-items:center;max-width:930px;margin:0 auto;}
.r3-orb{width:96px;height:96px;border-radius:50%;display:grid;place-items:center;font-size:38px;font-weight:950;background:radial-gradient(circle at 28% 18%,#fff 0,#e4d7ff 12%,#9a73ff 38%,#3c1d80 68%,#07030e 100%);border:1px solid rgba(255,255,255,.65);box-shadow:inset 0 2px 7px rgba(255,255,255,.55),0 0 38px rgba(138,92,255,.26);}
.r3-naya h2{font-size:clamp(28px,4vw,48px);}
.r3-masters-stage{margin-top:32px;display:grid;grid-template-columns:1.3fr 1fr 1fr;gap:14px;}
.r3-master{position:relative;min-height:250px;padding:26px;border-radius:28px;border:1px solid rgba(255,255,255,.10);background:linear-gradient(180deg,rgba(255,255,255,.038),rgba(255,255,255,.012));overflow:hidden;display:flex;flex-direction:column;justify-content:flex-end;}
.r3-master:first-child{background:radial-gradient(circle at 18% 14%,rgba(138,92,255,.2),transparent 38%),linear-gradient(180deg,rgba(138,92,255,.07),rgba(255,255,255,.012));}
.r3-jewel{position:absolute;top:22px;left:22px;width:58px;height:58px;border-radius:20px;display:grid;place-items:center;font-size:23px;color:#fff;border:1px solid rgba(255,255,255,.55);box-shadow:inset 0 2px 5px rgba(255,255,255,.45),0 12px 24px rgba(0,0,0,.45);}
.r3-jewel.p{background:radial-gradient(circle at 30% 20%,#fff,#dcd1ff 14%,#8a5cff 45%,#160b2b 100%);}
.r3-jewel.b{background:radial-gradient(circle at 30% 20%,#fff,#d9e9ff 14%,#3ca8ff 45%,#07111d 100%);}
.r3-jewel.g{background:radial-gradient(circle at 30% 20%,#fff,#d8ffe9 14%,#35e39b 45%,#06130c 100%);}
.r3-master h3{margin:0;font-size:clamp(23px,2.7vw,34px);line-height:1.02;color:#fff;}
.r3-master p{margin:9px 0 0;color:#a8a3af;font-size:12px;line-height:1.5;}
.r3-role{margin-top:9px;color:#b895ff;font-size:9px;text-transform:uppercase;letter-spacing:.12em;font-weight:950;}
.r3-next{text-align:center;padding-bottom:40px;}
.r3-next p{max-width:720px;margin:16px auto 0;color:#a9a4b0;font-size:15px;line-height:1.6;}
.r3-actions{display:flex;justify-content:center;gap:12px;flex-wrap:wrap;margin-top:28px;}
.r3-actions button{min-width:190px;min-height:56px;padding:0 22px;border-radius:18px;font-weight:950;cursor:pointer;}
.r3-primary{border:1px solid rgba(181,140,255,.8);background:linear-gradient(180deg,#17131f,#08080b);color:#fff;box-shadow:0 14px 34px rgba(0,0,0,.5),0 0 30px rgba(138,92,255,.12);}
.r3-secondary{border:1px solid rgba(255,255,255,.14);background:transparent;color:#c8c3cf;}
@media(max-width:760px){.r3-analysis,.r3-fingerprint,.r3-masters-stage{grid-template-columns:1fr}.r3-naya{grid-template-columns:1fr}.r3-wrap{padding-inline:16px}.r3-panel{padding:54px 0}.r3-master{min-height:220px}}
@media(prefers-reduced-motion:reduce){.r3-actions button{transition:none;}}
'''

JS = r'''
/* =========================================================
   MAXESS RESULTS HARD RESET V3
   The old Results DOM is discarded. Only score data survives.
========================================================= */
(function(){
  const root=document.getElementById('resultsView');
  if(!root) return;
  const marker='maxessResultsV3Mounted';
  const esc=v=>String(v==null?'':v).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
  const getDims=()=>[...root.querySelectorAll('.dimension-orb')].map((el,i)=>({name:el.querySelector('.dimension-name')?.textContent?.trim()||['Direction','Communication','Evaluation','Iteration','Systems Thinking'][i]||'Dimension',score:Number(el.querySelector('.dimension-score')?.textContent||0)})).filter(d=>Number.isFinite(d.score));
  const buildRadar=ds=>{const a=ds.slice(0,5);while(a.length<5)a.push({name:'Dimension',score:0});const cx=300,cy=220,r=152,n=5;const p=(i,rr)=>{const t=-Math.PI/2+(i*2*Math.PI/n);return [cx+Math.cos(t)*rr,cy+Math.sin(t)*rr]};const poly=f=>a.map((_,i)=>p(i,r*f).join(',')).join(' ');const shape=a.map((d,i)=>p(i,r*Math.max(.06,Math.min(100,d.score))/100).join(',')).join(' ');const axes=a.map((_,i)=>{const q=p(i,r);return `<line class="axis" x1="${cx}" y1="${cy}" x2="${q[0]}" y2="${q[1]}"/>`}).join('');const labels=a.map((d,i)=>{const q=p(i,r+38);return `<text class="label" x="${q[0]}" y="${q[1]}" text-anchor="middle">${esc(d.name)}</text>`}).join('');const pts=a.map((d,i)=>{const q=p(i,r*Math.max(.06,Math.min(100,d.score))/100);return `<circle class="point" cx="${q[0]}" cy="${q[1]}" r="5"/>`}).join('');return `<svg viewBox="0 0 600 440" role="img" aria-label="Your AI capability fingerprint">${[.25,.5,.75,1].map(f=>`<polygon class="grid" points="${poly(f)}"/>`).join('')}${axes}<polygon class="shape" points="${shape}"/>${pts}${labels}</svg>`};
  const mount=()=>{
    if(!root.classList.contains('visible')||root.dataset[marker]==='1') return;
    const score=Math.round(Number(document.getElementById('overallScore')?.textContent||0));
    const dims=getDims();if(!dims.length) return;dims.sort((a,b)=>b.score-a.score);
    const hi=dims[0],lo=dims[dims.length-1];
    const oldPdf=document.getElementById('pdfButton');
    const oldStart=document.getElementById('freeTrialButton');
    const oldText=document.getElementById('strongestText')?.textContent?.trim()||`Your strongest current capability is ${hi.name}.`;

    root.dataset[marker]='1';
    root.classList.add('maxess-results-v3');
    root.innerHTML='';

    const wrap=document.createElement('main');wrap.className='results-v3';
    const startAngle=-2.46,endAngle=2.46,clamped=Math.max(0,Math.min(100,score)),angle=startAngle+(endAngle-startAngle)*clamped/100,cx=300,cy=260,r=180;
    const pt=(a,rr)=>[cx+Math.cos(a)*rr,cy+Math.sin(a)*rr];
    const ps=pt(startAngle,r),pe=pt(endAngle,r),pf=pt(angle,r),needle=pt(angle,125);
    const arc=(p0,p1)=>`M ${p0[0]} ${p0[1]} A ${r} ${r} 0 0 1 ${p1[0]} ${p1[1]}`;
    const scoreBand=score>=90?'MASTERFUL CAPABILITY':score>=75?'STRONG AI CAPABILITY':score>=60?'DEVELOPING AI CAPABILITY':'EMERGING AI CAPABILITY';
    wrap.innerHTML=`<div class="r3-wrap">
      <section class="r3-hero"><div class="r3-kicker">YOUR MAXESS RESULT</div><h1>${score}<span>/100</span></h1><p>${esc(scoreBand)}. This is your capability snapshot — a starting point for understanding how you work with AI.</p><div class="r3-gauge"><svg viewBox="0 0 600 390" role="img" aria-label="MAXESS score ${score} out of 100"><defs><linearGradient id="r3Gauge" x1="0" x2="1"><stop offset="0" stop-color="#5424b5"/><stop offset=".6" stop-color="#8a5cff"/><stop offset="1" stop-color="#c1a1ff"/></linearGradient></defs><path class="track" d="${arc(ps,pe)}"/><path class="fill" d="${arc(ps,pf)}"/><line class="tick" x1="${pt(startAngle,r-12)[0]}" y1="${pt(startAngle,r-12)[1]}" x2="${pt(startAngle,r+10)[0]}" y2="${pt(startAngle,r+10)[1]}"/><line class="tick" x1="${pt(endAngle,r-12)[0]}" y1="${pt(endAngle,r-12)[1]}" x2="${pt(endAngle,r+10)[0]}" y2="${pt(endAngle,r+10)[1]}"/><line class="needle" x1="${cx}" y1="${cy}" x2="${needle[0]}" y2="${needle[1]}"/><circle class="hub" cx="${cx}" cy="${cy}" r="15"/><text class="score" x="${cx}" y="${cy-4}" text-anchor="middle">${score}</text><text class="label" x="${cx}" y="${cy+28}" text-anchor="middle">YOUR AI MASTERY SCORE</text></svg></div><div class="r3-band">${esc(scoreBand)}</div></section>
      <section class="r3-panel r3-analysis"><div><div class="r3-kicker">YOUR PERSONALIZED ANALYSIS</div><p class="r3-analysis-lead">${esc(oldText)} <em>Your next meaningful lift is ${esc(lo.name).toLowerCase()}.</em></p></div><div class="r3-meaning"><div class="r3-meaning-item"><span>Natural advantage</span><strong>${esc(hi.name)}</strong><small>${Math.round(hi.score)}/100 · your strongest dimension.</small></div><div class="r3-meaning-item"><span>Highest-leverage opportunity</span><strong>${esc(lo.name)}</strong><small>${Math.round(lo.score)}/100 · the clearest place to grow.</small></div></div></section>
      <section class="r3-panel"><div class="r3-kicker">YOUR AI CAPABILITY SIGNATURE</div><h2 class="r3-title">This is your AI fingerprint.</h2><p class="r3-copy">Not five disconnected scores. One recognizable shape — the way your capabilities combine.</p><div class="r3-fingerprint"><div class="r3-radar">${buildRadar(dims)}</div><div class="r3-read"><article><span>Strongest</span><h3>${esc(hi.name)}</h3><p>You already have meaningful strength here.</p></article><article><span>Highest leverage</span><h3>${esc(lo.name)}</h3><p>This is the most useful capability to deliberately develop next.</p></article><article><span>The test</span><h3>What would make this a 10?</h3><p>Judge the work. Improve the weak point. Repeat.</p></article></div></div></section>
      <section class="r3-panel r3-process"><div class="r3-kicker">HOW YOU WORK WITH AI</div><h2>AI is the engine.<br><em>You are the director.</em></h2><p class="r3-copy" style="margin-left:auto;margin-right:auto">Know what you want. Tell AI what matters. Ask clearly. Look closely. Score honestly. Improve deliberately. Repeat.</p><div class="r3-process-line">${['KNOW','TELL','ASK','LOOK','SCORE','IMPROVE','REPEAT'].map(x=>`<span class="step"><i class="gem">✦</i>${x}</span>`).join('')}</div></section>
      <section class="r3-panel r3-naya"><div class="r3-orb">N</div><div><div class="r3-kicker">NAYA · YOUR PERSONAL GUIDE</div><h2>Okay. Now we know where to look.</h2><p class="r3-copy">${esc(lo.name)} is the place to experiment next. Keep what works, improve what doesn't, and turn the result into something you can use.</p></div></section>
      <section class="r3-panel r3-masters"><div class="r3-kicker">NAYA · MASTER INTELLIGENCE</div><h2>Specific work deserves specific mastery.</h2><p class="r3-copy">One Naya. Many forms of mastery. These are examples of the specialized intelligence available when you need it.</p><div class="r3-masters-stage"><article class="r3-master"><div class="r3-jewel p">✦</div><h3>Naya Master ${esc(hi.name)}</h3><div class="r3-role">Your natural advantage</div><p>Turn what you already do well into a repeatable strength.</p></article><article class="r3-master"><div class="r3-jewel b">◆</div><h3>Naya Master ${esc(lo.name)}</h3><div class="r3-role">Your next leverage</div><p>Practice the capability that can create the biggest lift.</p></article><article class="r3-master"><div class="r3-jewel g">△</div><h3>Naya Master Strategist</h3><div class="r3-role">Turn intent into action</div><p>Move from what you want to what you can actually build.</p></article></div></section>
      <section class="r3-panel r3-next"><div class="r3-kicker">YOUR NEXT CHAPTER</div><h2>Now make the capability real.</h2><p>Your result shows you where you are. The next step is choosing where to apply it — then doing the work.</p><div class="r3-actions"><button class="r3-primary" type="button" data-r3-start>MASTER AI</button><button class="r3-secondary" type="button" data-r3-save>SAVE MY RESULTS</button></div></section>
    </div>`;
    root.appendChild(wrap);
    root.querySelector('[data-r3-start]')?.addEventListener('click',()=>oldStart?.click());
    root.querySelector('[data-r3-save]')?.addEventListener('click',()=>oldPdf?.click());
  };
  const obs=new MutationObserver(mount);obs.observe(root,{attributes:true,attributeFilter:['class']});mount();
})();
'''

if '</style>' not in s: raise RuntimeError('style closing tag missing')
if '</script>' not in s: raise RuntimeError('script closing tag missing')
s=s.replace('</style>',CSS+'\n</style>',1)
pos=s.rfind('</script>')
s=s[:pos]+'\n'+JS+'\n'+s[pos:]
p.write_text(s,encoding='utf-8')
print('Applied MAXESS Results Hard Reset V3')
