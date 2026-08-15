from pathlib import Path

p = Path('code')
s = p.read_text(encoding='utf-8')
MARKER = 'MAXESS RESULTS EXPERIENCE CLEAN SLATE'
if MARKER in s:
    print('Clean-slate Results Experience already present')
    raise SystemExit(0)

CSS = r'''
/* =========================================================
   MAXESS RESULTS EXPERIENCE CLEAN SLATE
   Presentation rule: preserve data and engine; rebuild the
   visible Results experience as a small number of premium
   compositions. No dashboard disease. No tiny-card soup.
========================================================= */
.maxess-clean-results{--cr-bg:#020204;--cr-purple:#8a5cff;--cr-lav:#b895ff;--cr-blue:#3ca8ff;--cr-green:#35e39b;--cr-violet:#765cff;--cr-magenta:#ed42c4;color:#f8f7fb;max-width:1120px;margin:0 auto;padding:0 20px 90px}
.maxess-clean-results .cr-section{margin-top:78px}
.maxess-clean-results .cr-kicker{color:var(--cr-lav);font-size:10px;font-weight:950;letter-spacing:.18em;text-transform:uppercase}
.maxess-clean-results .cr-title{margin:10px 0 0;font-size:clamp(30px,5vw,54px);line-height:1.00;letter-spacing:-.04em;font-weight:950}
.maxess-clean-results .cr-copy{max-width:760px;margin:16px 0 0;color:#b8b1c0;font-size:15px;line-height:1.68}

.cr-thermometer{margin-top:38px;display:grid;grid-template-columns:120px minmax(0,1fr);gap:22px;align-items:center}
.cr-score{display:flex;flex-direction:column;align-items:flex-start}.cr-score-number{font-size:clamp(58px,9vw,92px);line-height:.86;letter-spacing:-.06em;font-weight:1000}.cr-score-label{margin-top:10px;color:#918a99;font-size:10px;letter-spacing:.13em;text-transform:uppercase;font-weight:900}
.cr-meter{position:relative;height:22px;border-radius:999px;background:linear-gradient(90deg,rgba(255,255,255,.05),rgba(255,255,255,.08));border:1px solid rgba(184,149,255,.18);box-shadow:inset 0 1px 3px rgba(0,0,0,.6),0 0 28px rgba(138,92,255,.08);overflow:hidden}
.cr-meter-fill{height:100%;width:0;border-radius:inherit;background:linear-gradient(90deg,#5424b5,#765cff,#8a5cff,#b895ff);box-shadow:0 0 22px rgba(138,92,255,.34);transition:width 1s var(--ease)}
.cr-meter-ticks{display:flex;justify-content:space-between;margin-top:9px;color:#6f6878;font-size:9px;font-weight:850;letter-spacing:.08em}.cr-meter-caption{margin-top:14px;color:#c9c3cf;font-size:13px;line-height:1.45}.cr-meter-caption b{color:#fff}

.cr-analysis{margin-top:42px;padding:12px 0 0;border-top:1px solid rgba(184,149,255,.12)}
.cr-analysis h2{margin:9px 0 0;font-size:clamp(28px,4.5vw,46px);line-height:1.03;letter-spacing:-.035em}
.cr-analysis-lead{max-width:820px;margin-top:14px;color:#ddd7e4;font-size:18px;line-height:1.52}
.cr-analysis-points{display:flex;flex-wrap:wrap;gap:12px;margin-top:22px}.cr-analysis-point{padding:10px 14px;border-bottom:1px solid rgba(184,149,255,.20);color:#cbc5d3;font-size:12px;font-weight:850}.cr-analysis-point b{color:#b895ff}

.cr-signature{margin-top:64px;padding-top:10px}.cr-signature-head{display:flex;justify-content:space-between;gap:20px;align-items:end}.cr-signature-visual{margin-top:34px;max-width:760px}.cr-signature-visual svg{width:100%;height:auto}.cr-signature-visual .grid{fill:none;stroke:rgba(255,255,255,.08);stroke-width:1}.cr-signature-visual .axis{stroke:rgba(255,255,255,.07);stroke-width:1}.cr-signature-visual .radar{fill:rgba(138,92,255,.15);stroke:#b895ff;stroke-width:2;filter:drop-shadow(0 0 16px rgba(138,92,255,.24))}.cr-signature-visual .point{fill:#fff;stroke:#b895ff;stroke-width:2;filter:drop-shadow(0 0 9px rgba(138,92,255,.48))}.cr-signature-visual .label{fill:#aaa4b3;font-size:11px;font-weight:850}
.cr-dimension-story{margin-top:26px;display:grid;grid-template-columns:1fr 1fr;gap:22px}.cr-story{min-width:0}.cr-story-kicker{color:#8e8796;font-size:9px;font-weight:950;letter-spacing:.18em;text-transform:uppercase}.cr-story h3{margin:8px 0 0;font-size:clamp(24px,3.5vw,34px);line-height:1.06;letter-spacing:-.03em}.cr-story p{margin:10px 0 0;color:#b9b2c0;font-size:14px;line-height:1.62}.cr-story-adv{border-left:2px solid var(--cr-green);padding-left:18px}.cr-story-opp{border-left:2px solid var(--cr-purple);padding-left:18px}

.cr-insight{margin-top:74px;padding:38px 0;border-top:1px solid rgba(184,149,255,.10);border-bottom:1px solid rgba(184,149,255,.10)}.cr-insight blockquote{margin:12px 0 0;max-width:920px;font-size:clamp(28px,4.5vw,50px);line-height:1.04;letter-spacing:-.04em;font-weight:950}.cr-insight p{max-width:760px;margin:14px 0 0;color:#aaa3b1;font-size:15px;line-height:1.68}

.cr-naya{margin-top:74px;display:grid;grid-template-columns:auto minmax(0,1fr);gap:22px;align-items:center;padding:28px 0;border-top:1px solid rgba(184,149,255,.10);border-bottom:1px solid rgba(184,149,255,.10)}.cr-naya-orb{width:86px;height:86px;border-radius:50%;background:radial-gradient(circle at 30% 18%,#fff 0,#ded0ff 12%,#956eff 38%,#3b1b83 70%,#09050f 100%);border:1px solid #e5dbff;box-shadow:inset 0 2px 4px rgba(255,255,255,.76),0 0 32px rgba(116,76,255,.34),0 10px 20px rgba(0,0,0,.45);display:grid;place-items:center;color:#fff;font-size:24px;font-weight:1000}.cr-naya-name{color:#b895ff;font-size:10px;font-weight:950;letter-spacing:.18em;text-transform:uppercase}.cr-naya h3{margin:7px 0 0;font-size:clamp(24px,3.4vw,36px);line-height:1.05}.cr-naya p{margin:9px 0 0;max-width:760px;color:#b4adba;font-size:14px;line-height:1.62}

.cr-masterkey{margin-top:70px}.cr-keyline{display:flex;flex-wrap:wrap;gap:6px;margin-top:24px}.cr-keyline span{display:inline-flex;align-items:center;min-height:36px;padding:0 11px;border:1px solid rgba(184,149,255,.16);border-radius:999px;background:rgba(138,92,255,.035);color:#e0d9e7;font-size:11px;font-weight:950;letter-spacing:.03em}.cr-keyline span:not(:last-child)::after{content:'→';margin-left:10px;color:#7e7489}.cr-aaa{margin-top:26px;max-width:860px;color:#b7b0bd;font-size:14px;line-height:1.68}.cr-aaa strong{color:#fff}

.cr-doors{margin-top:78px}.cr-doorline{display:flex;align-items:center;gap:14px;margin-top:24px;overflow:auto;padding-bottom:10px;scrollbar-width:thin}.cr-door{min-width:205px;padding:18px 18px 16px;border:1px solid rgba(184,149,255,.14);border-radius:24px;background:linear-gradient(145deg,rgba(255,255,255,.035),rgba(255,255,255,.012));box-shadow:inset 0 1px 0 rgba(255,255,255,.05)}.cr-gem{width:48px;height:48px;border-radius:15px;display:grid;place-items:center;color:#fff;font-size:17px;font-weight:1000;border:1px solid rgba(255,255,255,.62);box-shadow:inset 0 2px 4px rgba(255,255,255,.70),0 0 22px rgba(138,92,255,.16)}.cr-door strong{display:block;margin-top:11px;font-size:14px;line-height:1.2}.cr-door p{margin:6px 0 0;color:#9e97a6;font-size:11px;line-height:1.45}

.cr-next{margin-top:82px;padding:48px 0 18px;border-top:1px solid rgba(184,149,255,.12);text-align:center}.cr-next h2{margin:8px auto 0;max-width:760px;font-size:clamp(30px,5vw,54px);line-height:1.02;letter-spacing:-.04em}.cr-next p{max-width:650px;margin:14px auto 0;color:#aaa4b2;font-size:14px;line-height:1.62}.cr-actions{display:flex;justify-content:center;gap:10px;flex-wrap:wrap;margin-top:24px}.cr-actions button{min-height:54px;padding:0 22px;border-radius:18px;font-weight:950;cursor:pointer}.cr-primary{border:1px solid rgba(184,149,255,.48);background:linear-gradient(180deg,#b895ff,#765cff);color:#09060e;box-shadow:0 16px 36px rgba(138,92,255,.18)}.cr-secondary{border:1px solid rgba(255,255,255,.14);background:#07070a;color:#fff}

@media(max-width:760px){
 .maxess-clean-results{padding:0 16px 66px}.cr-thermometer{grid-template-columns:1fr;gap:16px}.cr-score{align-items:flex-start}.cr-score-number{font-size:70px}.cr-meter{height:18px}.cr-dimension-story{grid-template-columns:1fr;gap:26px}.cr-naya{grid-template-columns:auto 1fr;gap:16px}.cr-naya-orb{width:68px;height:68px}.cr-doorline{gap:10px}.cr-door{min-width:190px}
}
'''

if '</style>' not in s:
    raise RuntimeError('style closing tag missing')
s = s.replace('</style>', CSS + '\n</style>', 1)

JS = r'''
(function(){
  const root=document.getElementById('resultsView');
  if(!root) return;
  const marker='maxess-clean-slate-mounted';

  function esc(v){
    return String(v==null?'':v).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
  }

  function read(){
    const score=Math.round(Number(document.getElementById('overallScore')?.textContent||0));
    const dims=[...root.querySelectorAll('#dimensionConstellation .dimension-orb')].map((el,i)=>({
      name:el.querySelector('.dimension-name')?.textContent?.trim()||['Direction','Communication','Evaluation','Iteration','Systems Thinking'][i]||'Dimension',
      score:Number(el.querySelector('.dimension-score')?.textContent||0)
    }));
    dims.sort((a,b)=>b.score-a.score);
    const strongest=dims[0]||{name:'Capability',score:score};
    const opportunity=dims[dims.length-1]||strongest;
    const existing=document.getElementById('strongestText')?.textContent?.trim()||`Your strongest current capability is ${strongest.name}.`;
    const insights={direction:'You may already know what you want AI to accomplish. The next leap is making the destination even more deliberate.',communication:'You may already have useful intent. The next leap is giving AI enough context and direction to make that intent executable.',evaluation:'You may benefit most from becoming a stronger judge of AI output. Better judgment changes what you keep, reject, and improve.',iteration:'You may benefit most from making improvement deliberate: preserve what works, diagnose what does not, and repeat.',systems:'You may be ready to turn individual wins into repeatable workflows that create leverage.'};
    const key=Object.keys(insights).find(k=>opportunity.name.toLowerCase().includes(k))||'evaluation';
    return {score,dims,strongest,opportunity,existing,why:insights[key]};
  }

  function makeRadar(dims){
    const cx=300,cy=220,r=156,n=Math.max(dims.length,5);
    const five=dims.slice(0,5); const safe=[...five]; while(safe.length<5)safe.push({name:'Capability',score:0});
    const point=(d,scale=1)=>{const i=safe.indexOf(d),a=(-Math.PI/2)+(Math.PI*2*i/5),rr=r*scale;return `${cx+Math.cos(a)*rr},${cy+Math.sin(a)*rr}`};
    const ring=(f)=>safe.map(d=>point(d,f)).join(' ');
    const radar=safe.map(d=>{const i=safe.indexOf(d),a=(-Math.PI/2)+(Math.PI*2*i/5),rr=r*Math.max(.08,d.score/100);return `${cx+Math.cos(a)*rr},${cy+Math.sin(a)*rr}`}).join(' ');
    const axes=safe.map(d=>{const i=safe.indexOf(d),a=(-Math.PI/2)+(Math.PI*2*i/5);return `<line class="axis" x1="${cx}" y1="${cy}" x2="${cx+Math.cos(a)*r}" y2="${cy+Math.sin(a)*r}"/>`}).join('');
    const labels=safe.map(d=>{const i=safe.indexOf(d),a=(-Math.PI/2)+(Math.PI*2*i/5),lr=r+34;return `<text class="label" x="${cx+Math.cos(a)*lr}" y="${cy+Math.sin(a)*lr}" text-anchor="middle">${esc(d.name)}</text>`}).join('');
    const pts=safe.map(d=>{const i=safe.indexOf(d),a=(-Math.PI/2)+(Math.PI*2*i/5),rr=r*Math.max(.08,d.score/100);return `<circle class="point" cx="${cx+Math.cos(a)*rr}" cy="${cy+Math.sin(a)*rr}" r="5"/>`}).join('');
    return `<svg viewBox="0 0 600 440" role="img" aria-label="Your AI Capability Signature">${[.25,.5,.75,1].map(f=>`<polygon class="grid" points="${ring(f)}"/>`).join('')}${axes}<polygon class="radar" points="${radar}"/>${pts}${labels}</svg>`;
  }

  function mount(){
    if(!root.classList.contains('visible') || root.dataset[marker]==='1') return;
    const data=read();
    const hero=root.querySelector('.result-hero');
    if(!hero || !data.dims.length) return;

    /* Keep the proven hero and all engine-generated data; hide every presentation layer
       created by the accumulated Results passes. */
    [...root.children].forEach(child=>{
      if(child===hero) return;
      child.classList.add('cr-legacy-hidden');
    });

    hero.querySelector('.result-eyebrow')?.replaceChildren(document.createTextNode('YOUR PERSONALIZED ANALYSIS'));
    const title=hero.querySelector('.result-title'); if(title) title.textContent='What your score tells the story.';
    const subtitle=hero.querySelector('.result-subtitle'); if(subtitle) subtitle.textContent=`${data.score}/100 · A snapshot of how you currently work with AI.`;

    const shell=document.createElement('div'); shell.className='maxess-clean-results'; shell.innerHTML=`
      <section class="cr-section cr-analysis" aria-labelledby="crAnalysisTitle">
        <div class="cr-kicker">YOUR SCORE</div>
        <h2 id="crAnalysisTitle">${data.score} tells the story.</h2>
        <div class="cr-thermometer" aria-label="MAXESS score ${data.score} out of 100">
          <div class="cr-score"><div class="cr-score-number">${data.score}</div><div class="cr-score-label">MAXESS SCORE</div></div>
          <div><div class="cr-meter"><div class="cr-meter-fill" style="width:${Math.max(0,Math.min(100,data.score))}%"></div></div><div class="cr-meter-ticks"><span>FOUNDATION</span><span>CAPABLE</span><span>STRONG</span><span>MASTERFUL</span></div><div class="cr-meter-caption"><b>${esc(data.strongest.name)}</b> is currently your strongest capability.</div></div>
        </div>
        <p class="cr-analysis-lead">${esc(data.existing)}</p>
        <div class="cr-analysis-points"><span class="cr-analysis-point"><b>${data.strongest.name}</b> · ${Math.round(data.strongest.score)}/100</span><span class="cr-analysis-point"><b>${data.opportunity.name}</b> · ${Math.round(data.opportunity.score)}/100</span></div>
      </section>

      <section class="cr-section cr-signature" aria-labelledby="crSignatureTitle">
        <div class="cr-signature-head"><div><div class="cr-kicker">YOUR AI CAPABILITY SIGNATURE</div><h2 class="cr-title" id="crSignatureTitle">Your AI fingerprint.</h2><p class="cr-copy">Five dimensions create a recognizable shape. The picture shows the pattern. The words tell you what it means.</p></div></div>
        <div class="cr-signature-visual">${makeRadar(data.dims)}</div>
        <div class="cr-dimension-story">
          <div class="cr-story cr-story-adv"><div class="cr-story-kicker">YOUR NATURAL ADVANTAGE</div><h3>${esc(data.strongest.name)}</h3><p>${esc(data.existing)}</p></div>
          <div class="cr-story cr-story-opp"><div class="cr-story-kicker">YOUR HIGHEST-LEVERAGE OPPORTUNITY</div><h3>${esc(data.opportunity.name)}</h3><p>${esc(data.why)}</p></div>
        </div>
      </section>

      <section class="cr-section cr-insight"><div class="cr-kicker">THE INSIGHT</div><blockquote>“${esc(data.why)}”</blockquote><p>This is not a judgment. It is the most useful place to look next based on the pattern in your assessment.</p></section>

      <section class="cr-section cr-naya" aria-labelledby="crNayaTitle"><div class="cr-naya-orb" aria-hidden="true">N</div><div><div class="cr-naya-name">NAYA · YOUR PERSONAL GUIDE</div><h3 id="crNayaTitle">Okay. Now we know where to look.</h3><p>${esc(data.opportunity.name)} is the place to experiment next. Keep it small, judge the result honestly, and improve it deliberately.</p></div></section>

      <section class="cr-section cr-masterkey"><div class="cr-kicker">THE MAXESS MASTER KEY</div><h2 class="cr-title">How to work with AI.</h2><p class="cr-copy">You do not need to memorize hundreds of prompts. Build the habit of thinking around the result.</p><div class="cr-keyline"><span>KNOW</span><span>TELL</span><span>ASK</span><span>LOOK</span><span>SCORE</span><span>IMPROVE</span><span>REPEAT</span></div><p class="cr-aaa"><strong>AAA means:</strong> solve the right problem, make the result clear, check that it is accurate, make it useful, refine it, and create genuine human value.</p></section>

      <section class="cr-section cr-doors"><div class="cr-kicker">YOUR POSSIBILITIES</div><h2 class="cr-title">Choose a door worth opening.</h2><p class="cr-copy">These are directions, not a catalogue. Start with the one that feels most useful to you.</p><div class="cr-doorline">
        <article class="cr-door"><div class="cr-gem" style="background:radial-gradient(circle at 30% 20%,#fff 0,#d9d3ff 13%,#8a5cff 44%,#09050f 100%)">◆</div><strong>Keep your advantage</strong><p>Use your strongest capability deliberately.</p></article>
        <article class="cr-door"><div class="cr-gem" style="background:radial-gradient(circle at 30% 20%,#fff 0,#d9d3ff 13%,#3ca8ff 44%,#07101a 100%)">✦</div><strong>Build your opportunity</strong><p>Practice the area with the most leverage.</p></article>
        <article class="cr-door"><div class="cr-gem" style="background:radial-gradient(circle at 30% 20%,#fff 0,#d9d3ff 13%,#35e39b 44%,#06110b 100%)">△</div><strong>Create something real</strong><p>Turn capability into useful output.</p></article>
        <article class="cr-door"><div class="cr-gem" style="background:radial-gradient(circle at 30% 20%,#fff 0,#d9d3ff 13%,#765cff 44%,#09050f 100%)">✧</div><strong>Explore Naya Masters</strong><p>Find specialized intelligence for your next task.</p></article>
        <article class="cr-door"><div class="cr-gem" style="background:radial-gradient(circle at 30% 20%,#fff 0,#d9d3ff 13%,#ed42c4 44%,#12050f 100%)">✦</div><strong>Take the next step</strong><p>Turn what you know into what you do.</p></article>
      </div></section>

      <section class="cr-section cr-next"><div class="cr-kicker">READY TO GO FURTHER?</div><h2>Your result shows where you are. Now build what comes next.</h2><p>Capability first. Practice second. Opportunity follows useful work.</p><div class="cr-actions"><button type="button" class="cr-primary" id="crMasterAi">MASTER AI →</button><button type="button" class="cr-secondary" id="crSave">SAVE MY RESULTS</button></div></section>
    `;

    hero.insertAdjacentElement('afterend',shell);
    shell.querySelector('#crMasterAi')?.addEventListener('click',()=>document.getElementById('freeTrialButton')?.click());
    shell.querySelector('#crSave')?.addEventListener('click',()=>document.getElementById('pdfButton')?.click());
    requestAnimationFrame(()=>{const f=shell.querySelector('.cr-meter-fill'); if(f){const w=f.style.width; f.style.width='0%'; requestAnimationFrame(()=>f.style.width=w);}});
    root.dataset[marker]='1';
  }

  const obs=new MutationObserver(mount);
  obs.observe(root,{attributes:true,attributeFilter:['class'],childList:true,subtree:true});
  mount();
})();
'''

idx=s.lower().rfind('</script>')
if idx<0: raise RuntimeError('script closing tag not found')
s=s[:idx]+JS+'\n'+s[idx:]
s=s.replace('</head>', '\n<!-- '+MARKER+' -->\n</head>',1)
p.write_text(s,encoding='utf-8')
print('Clean-slate Results Experience applied')
