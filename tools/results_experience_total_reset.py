from pathlib import Path

p=Path('code')
s=p.read_text(encoding='utf-8')
MARK='MAXESS RESULTS EXPERIENCE TOTAL RESET'
if MARK in s:
    print('Total reset already present')
    raise SystemExit(0)

CSS=r'''
/* =========================================================
   MAXESS RESULTS EXPERIENCE TOTAL RESET
   Preserve engine + truth. Replace accumulated presentation.
========================================================= */
.maxess-total-reset{max-width:1160px;margin:0 auto;padding:0 clamp(16px,3vw,34px) 110px;color:#f8f7fb}
.maxess-total-reset .tr-section{margin-top:92px}
.tr-kicker{color:#b895ff;font-size:10px;font-weight:950;letter-spacing:.20em;text-transform:uppercase}
.tr-title{margin:10px 0 0;font-size:clamp(34px,5vw,62px);line-height:.98;letter-spacing:-.045em;font-weight:950}
.tr-copy{max-width:780px;margin:15px 0 0;color:#aaa4b2;font-size:15px;line-height:1.68}
.tr-story{display:grid;grid-template-columns:minmax(0,1.25fr) minmax(280px,.75fr);gap:52px;align-items:end}
.tr-story-quote{margin-top:28px;max-width:900px;font-size:clamp(24px,3.6vw,44px);line-height:1.08;letter-spacing:-.035em;font-weight:850}
.tr-story-quote em{font-style:normal;color:#b895ff}
.tr-proof{display:grid;grid-template-columns:1fr 1fr;gap:22px;margin-top:30px}
.tr-proof-item{padding-top:14px;border-top:1px solid rgba(184,149,255,.15)}
.tr-proof-label{color:#898293;font-size:9px;font-weight:950;letter-spacing:.18em;text-transform:uppercase}
.tr-proof-item strong{display:block;margin-top:7px;font-size:24px;line-height:1.05}
.tr-proof-item p{margin:7px 0 0;color:#a7a0ae;font-size:13px;line-height:1.55}

.tr-signature{margin-top:98px;text-align:center}
.tr-signature-wrap{margin:28px auto 0;max-width:760px}
.tr-signature-wrap svg{width:100%;filter:drop-shadow(0 24px 50px rgba(0,0,0,.30))}
.tr-signature-note{max-width:700px;margin:18px auto 0;color:#a7a0ae;font-size:13px;line-height:1.6}

.tr-process{margin-top:104px}
.tr-process-line{position:relative;margin-top:34px;display:grid;grid-template-columns:repeat(7,1fr);gap:0}
.tr-process-line::before{content:"";position:absolute;top:30px;left:4%;right:4%;height:2px;background:linear-gradient(90deg,rgba(138,92,255,.12),rgba(184,149,255,.55),rgba(138,92,255,.12));box-shadow:0 0 20px rgba(138,92,255,.10)}
.tr-process-step{position:relative;z-index:1;text-align:center}
.tr-process-gem{width:58px;height:58px;margin:0 auto;display:grid;place-items:center;border-radius:20px;border:1px solid rgba(255,255,255,.66);color:#fff;font-size:17px;font-weight:1000;background:radial-gradient(circle at 30% 16%,#fff 0,#ddd1ff 12%,#8a5cff 42%,#0a0610 100%);box-shadow:inset 0 2px 4px rgba(255,255,255,.75),0 0 28px rgba(138,92,255,.18),0 10px 18px rgba(0,0,0,.42)}
.tr-process-step:nth-child(2) .tr-process-gem{background:radial-gradient(circle at 30% 16%,#fff 0,#ddd1ff 12%,#3ca8ff 42%,#06101a 100%)}
.tr-process-step:nth-child(3) .tr-process-gem{background:radial-gradient(circle at 30% 16%,#fff 0,#ddd1ff 12%,#35e39b 42%,#06110b 100%)}
.tr-process-step:nth-child(4) .tr-process-gem{background:radial-gradient(circle at 30% 16%,#fff 0,#ddd1ff 12%,#765cff 42%,#0a0710 100%)}
.tr-process-step:nth-child(5) .tr-process-gem{background:radial-gradient(circle at 30% 16%,#fff 0,#ddd1ff 12%,#b895ff 42%,#0a0710 100%)}
.tr-process-step:nth-child(6) .tr-process-gem{background:radial-gradient(circle at 30% 16%,#fff 0,#ddd1ff 12%,#8a5cff 42%,#0a0710 100%)}
.tr-process-step:nth-child(7) .tr-process-gem{background:radial-gradient(circle at 30% 16%,#fff 0,#ddd1ff 12%,#ed42c4 42%,#12050f 100%)}
.tr-process-step strong{display:block;margin-top:13px;font-size:12px;letter-spacing:.02em}.tr-process-step span{display:block;margin-top:5px;color:#827a8c;font-size:10px;line-height:1.35}

.tr-masters{margin-top:104px}
.tr-master-intro{display:flex;justify-content:space-between;gap:32px;align-items:end}
.tr-master-intro p{max-width:620px;text-align:right;margin:0;color:#8f8798;font-size:13px;line-height:1.55}
.tr-master-stage{position:relative;margin-top:30px;display:grid;grid-template-columns:1.25fr 1fr 1fr;gap:14px;align-items:stretch}
.tr-master{position:relative;min-height:220px;padding:24px;border:1px solid rgba(184,149,255,.16);border-radius:30px;overflow:hidden;background:radial-gradient(circle at 20% 10%,rgba(138,92,255,.13),transparent 48%),linear-gradient(145deg,rgba(255,255,255,.045),rgba(255,255,255,.012));box-shadow:inset 0 1px 0 rgba(255,255,255,.06),0 22px 44px rgba(0,0,0,.34)}
.tr-master.feature{grid-row:span 2;min-height:454px;padding:30px}
.tr-master::after{content:'NAYA';position:absolute;right:18px;top:15px;color:rgba(184,149,255,.16);font-size:8px;font-weight:1000;letter-spacing:.20em}
.tr-gem{width:64px;height:64px;border-radius:22px;display:grid;place-items:center;color:#fff;border:1px solid rgba(255,255,255,.72);font-size:20px;font-weight:1000;background:radial-gradient(circle at 30% 16%,#fff 0,#ddd1ff 12%,#8a5cff 42%,#0b0711 100%);box-shadow:inset 0 2px 5px rgba(255,255,255,.73),0 0 28px rgba(138,92,255,.21),0 12px 20px rgba(0,0,0,.45)}
.tr-master:nth-child(2) .tr-gem{background:radial-gradient(circle at 30% 16%,#fff 0,#ddd1ff 12%,#3ca8ff 42%,#06101a 100%)}
.tr-master:nth-child(3) .tr-gem{background:radial-gradient(circle at 30% 16%,#fff 0,#ddd1ff 12%,#35e39b 42%,#06110b 100%)}
.tr-master:nth-child(4) .tr-gem{background:radial-gradient(circle at 30% 16%,#fff 0,#ddd1ff 12%,#ed42c4 42%,#12050f 100%)}
.tr-master-name{margin-top:18px;font-size:clamp(20px,2.4vw,30px);line-height:1.06;letter-spacing:-.025em;font-weight:950}.feature .tr-master-name{font-size:clamp(28px,4vw,46px)}
.tr-master-role{margin-top:8px;color:#b895ff;font-size:10px;font-weight:950;letter-spacing:.14em;text-transform:uppercase}.tr-master-copy{margin-top:14px;max-width:520px;color:#aaa3b1;font-size:13px;line-height:1.62}
.tr-master-lighthouse{position:absolute;right:20px;bottom:19px;color:#7f748d;font-size:9px;font-weight:850;letter-spacing:.08em;text-transform:uppercase}

.tr-next{margin-top:106px;padding:70px 0 26px;border-top:1px solid rgba(184,149,255,.12);text-align:center}
.tr-next h2{max-width:800px;margin:9px auto 0;font-size:clamp(38px,5.6vw,64px);line-height:.98;letter-spacing:-.045em}
.tr-next p{max-width:650px;margin:16px auto 0;color:#a69fad;font-size:15px;line-height:1.65}
.tr-actions{display:flex;justify-content:center;gap:10px;flex-wrap:wrap;margin-top:27px}.tr-actions button{min-height:56px;padding:0 24px;border-radius:19px;font-weight:950;cursor:pointer}.tr-primary{border:1px solid rgba(205,188,255,.65);background:linear-gradient(180deg,#b895ff,#765cff);color:#0b0710;box-shadow:0 18px 44px rgba(138,92,255,.20)}.tr-secondary{border:1px solid rgba(255,255,255,.14);background:#08080b;color:#fff}
.tr-note{margin-top:22px;color:#6f6778;font-size:10px;line-height:1.5}

@media(max-width:900px){.tr-story{grid-template-columns:1fr}.tr-master-stage{grid-template-columns:1fr 1fr}.tr-master.feature{grid-row:auto;min-height:270px}.tr-process-line{grid-template-columns:repeat(7,minmax(100px,1fr));overflow:auto;padding-bottom:14px}.tr-master-intro{display:block}.tr-master-intro p{text-align:left;margin-top:12px}}
@media(max-width:640px){.tr-proof{grid-template-columns:1fr}.tr-master-stage{grid-template-columns:1fr}.tr-master.feature{min-height:310px}.tr-next{padding-top:56px}}
'''
if '</style>' not in s: raise RuntimeError('style tag missing')
s=s.replace('</style>',CSS+'\n</style>',1)

JS=r'''
(function(){
 const root=document.getElementById('resultsView'); if(!root) return;
 function mount(){
  if(!root.classList.contains('visible') || root.dataset.trTotalReset==='1') return;
  const shell=root.querySelector('.maxess-clean-results'); if(!shell) return;
  const score=Math.round(Number(document.getElementById('overallScore')?.textContent||0));
  const dims=[...root.querySelectorAll('#dimensionConstellation .dimension-orb')].map((el,i)=>({name:el.querySelector('.dimension-name')?.textContent?.trim()||['Direction','Communication','Evaluation','Iteration','Systems Thinking'][i]||'Dimension',score:Number(el.querySelector('.dimension-score')?.textContent||0)}));
  dims.sort((a,b)=>b.score-a.score);
  const strongest=dims[0]||{name:'Direction',score:score};
  const opportunity=dims[dims.length-1]||strongest;
  const oldHidden=[...root.querySelectorAll('.cr-signature,.cr-processes,.cr-naya,.cr-masterkey,.cr-doors,.cr-next')]; oldHidden.forEach(x=>x.style.display='none');
  const insightText=root.querySelector('.cr-analysis-lead')?.textContent?.trim()||`Your strongest current capability is ${strongest.name}.`;
  const scoreText=score>=90?'Exceptional AI capability':score>=75?'Strong AI capability':score>=60?'Developing AI capability':'Emerging AI capability';
  const content=document.createElement('section');
  content.className='maxess-total-reset';
  content.innerHTML=`
   <section class="tr-section tr-story">
    <div><div class="tr-kicker">WHAT YOUR SCORE TELLs THE STORY</div><div class="tr-story-quote">You already have a real advantage in <em>${escapeHTML(strongest.name)}</em>. Your next leap is not doing more — it is becoming more deliberate about ${escapeHTML(opportunity.name).toLowerCase()}.</div><p class="tr-copy">${escapeHTML(insightText)}</p></div>
    <div class="tr-proof"><div class="tr-proof-item"><div class="tr-proof-label">Natural advantage</div><strong>${strongest.name}</strong><p>${strongest.score}/100 · ${scoreText}</p></div><div class="tr-proof-item"><div class="tr-proof-label">Highest leverage</div><strong>${opportunity.name}</strong><p>${opportunity.score}/100 · where focused practice can create the most lift</p></div></div>
   </section>

   <section class="tr-section tr-signature"><div class="tr-kicker">YOUR AI CAPABILITY SIGNATURE</div><h2 class="tr-title">The shape of how you work with AI.</h2><div class="tr-signature-wrap">${buildRadar(dims)}</div><p class="tr-signature-note">Your score is one number. This is the fingerprint underneath it — five capabilities working together.</p></section>

   <section class="tr-section tr-process"><div class="tr-kicker">HOW YOU WORK WITH AI</div><h2 class="tr-title">AI is the engine. <span style="color:#b895ff">You are the director.</span></h2><p class="tr-copy">The simplest way to become exceptional with AI is to stop treating it like an answer machine and start treating it like a system you direct, inspect, improve, and reuse.</p><div class="tr-process-line">${[['KNOW','Define the destination'],['TELL','Give the context'],['ASK','Shape the request'],['LOOK','Inspect the result'],['SCORE','Judge the quality'],['IMPROVE','Refine deliberately'],['REPEAT','Build the habit']].map((x,i)=>`<div class="tr-process-step"><div class="tr-process-gem">${['◆','✦','△','✧','◈','✦','✺'][i]}</div><strong>${x[0]}</strong><span>${x[1]}</span></div>`).join('')}</div></section>

   <section class="tr-section tr-masters"><div class="tr-master-intro"><div><div class="tr-kicker">NAYA · MASTER INTELLIGENCE</div><h2 class="tr-title">The right intelligence for the work in front of you.</h2></div><p>Naya is not one generic assistant. She can bring focused mastery to the areas you care about — without making you learn another complicated system.</p></div>
    <div class="tr-master-stage">
      <article class="tr-master feature"><div class="tr-gem">✦</div><div class="tr-master-name">Naya Master ${escapeHTML(strongest.name)}</div><div class="tr-master-role">Your natural advantage</div><div class="tr-master-copy">Start here. Use the capability you already show strength in as the foundation for everything you build next.</div><div class="tr-master-lighthouse">Core specialization</div></article>
      <article class="tr-master"><div class="tr-gem">◆</div><div class="tr-master-name">Naya Master ${escapeHTML(opportunity.name)}</div><div class="tr-master-role">Your leverage opportunity</div><div class="tr-master-copy">This is where deliberate practice can create a meaningful improvement in your overall capability.</div><div class="tr-master-lighthouse">Growth specialization</div></article>
      <article class="tr-master"><div class="tr-gem">△</div><div class="tr-master-name">Naya Master Strategist</div><div class="tr-master-role">Turn intent into action</div><div class="tr-master-copy">Bring direction, priorities, and decisions into the conversation so AI can help you move from idea to outcome.</div><div class="tr-master-lighthouse">Strategic specialization</div></article>
      <article class="tr-master"><div class="tr-gem">✺</div><div class="tr-master-name">Naya Master Creator</div><div class="tr-master-role">Make something real</div><div class="tr-master-copy">Turn your ideas into writing, visuals, media, products, or systems people can actually use.</div><div class="tr-master-lighthouse">Creative specialization</div></article>
    </div>
   </section>

   <section class="tr-next"><div class="tr-kicker">YOUR NEXT CHAPTER</div><h2>Now turn insight into capability.</h2><p>You know more about where you are. Pick one direction, practice it deliberately, and let the result become the beginning of what you can do next.</p><div class="tr-actions"><button class="tr-primary" type="button" data-total-master>MASTER AI</button><button class="tr-secondary" type="button" data-total-save>SAVE MY RESULTS</button></div><div class="tr-note">Your MAXESS result is a capability snapshot based on your assessment responses. It is not a diagnosis, prediction, or guarantee.</div></section>
  `;
  shell.insertAdjacentElement('afterend',content);
  content.querySelector('[data-total-master]')?.addEventListener('click',()=>document.getElementById('freeTrialButton')?.click());
  content.querySelector('[data-total-save]')?.addEventListener('click',()=>document.getElementById('pdfButton')?.click());
  root.dataset.trTotalReset='1';
 }
 function escapeHTML(v){return String(v==null?'':v).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));}
 function buildRadar(ds){const cx=300,cy=220,r=155,a0=-Math.PI/2,n=5;const safe=ds.slice(0,5);while(safe.length<5)safe.push({name:'Capability',score:0});const pt=(i,rr)=>{const a=a0+i*2*Math.PI/n;return `${cx+Math.cos(a)*rr},${cy+Math.sin(a)*rr}`};const rings=[.25,.5,.75,1].map(f=>`<polygon points="${safe.map((_,i)=>pt(i,r*f)).join(' ')}" fill="none" stroke="rgba(255,255,255,.08)"/>`).join('');const axes=safe.map((_,i)=>`<line x1="${cx}" y1="${cy}" x2="${pt(i,r).split(',')[0]}" y2="${pt(i,r).split(',')[1]}" stroke="rgba(255,255,255,.07)"/>`).join('');const radar=safe.map((d,i)=>pt(i,r*Math.max(.08,d.score/100))).join(' ');const pts=safe.map((d,i)=>{const p=pt(i,r*Math.max(.08,d.score/100)).split(',');return `<circle cx="${p[0]}" cy="${p[1]}" r="5" fill="#fff" stroke="#b895ff" stroke-width="2"/>`}).join('');const labels=safe.map((d,i)=>{const p=pt(i,r+34).split(',');return `<text x="${p[0]}" y="${p[1]}" text-anchor="middle" fill="#aaa4b3" font-size="11" font-weight="850">${escapeHTML(d.name)}</text>`}).join('');return `<svg viewBox="0 0 600 440" role="img" aria-label="Your AI Capability Signature">${rings}${axes}<polygon points="${radar}" fill="rgba(138,92,255,.16)" stroke="#b895ff" stroke-width="2"/>${pts}${labels}</svg>`}
 const obs=new MutationObserver(m=>m.forEach(x=>{if(x.type==='attributes')mount()})); obs.observe(root,{attributes:true,attributeFilter:['class']}); mount();
})();
'''

s=s.replace('</script>',JS+'\n</script>',1)

# Mark and add permanent audit marker.
if '</style>' not in s: raise RuntimeError('style tag missing')
s=s.replace('</style>','\n/* '+MARK+' */\n</style>',1)
p.write_text(s,encoding='utf-8')
print('Total Results presentation reset applied')
