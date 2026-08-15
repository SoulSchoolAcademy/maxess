from pathlib import Path

p=Path('code')
s=p.read_text(encoding='utf-8')
MARK='MAXESS RESULTS EXPERIENCE OSCAR SUPERPASS'
if MARK in s:
    print('Oscar superpass already present')
    raise SystemExit(0)

CSS=r'''
/* =========================================================
   MAXESS RESULTS EXPERIENCE OSCAR SUPERPASS
   Ruthless rule: editorial experience > component inventory.
========================================================= */
.maxess-oscar-superpass{max-width:1180px;margin:0 auto;padding:0 clamp(18px,4vw,48px) 120px}
.os-kicker{color:#b895ff;font-size:10px;font-weight:950;letter-spacing:.22em;text-transform:uppercase}
.os-head{margin-top:96px;max-width:980px}
.os-head h2{margin:10px 0 0;font-size:clamp(42px,6vw,76px);line-height:.94;letter-spacing:-.05em;font-weight:980}
.os-head p{max-width:760px;margin:18px 0 0;color:#aaa3b1;font-size:16px;line-height:1.7}
.os-reveal{margin-top:70px;display:grid;grid-template-columns:minmax(0,1fr) minmax(300px,.72fr);gap:58px;align-items:end}
.os-reveal-quote{font-size:clamp(28px,4vw,52px);line-height:1.02;letter-spacing:-.04em;font-weight:900}
.os-reveal-quote em{font-style:normal;color:#b895ff}
.os-reveal-side{padding-left:22px;border-left:2px solid rgba(184,149,255,.34)}
.os-reveal-side strong{display:block;font-size:22px;line-height:1.15}.os-reveal-side p{margin:9px 0 0;color:#9e96a7;font-size:13px;line-height:1.55}

/* The five-dimensional fingerprint becomes the visual centerpiece. */
.os-fingerprint{margin-top:112px;text-align:center}
.os-fingerprint h3{margin:10px 0 0;font-size:clamp(32px,4.6vw,56px);line-height:.98;letter-spacing:-.045em}
.os-fingerprint p{max-width:710px;margin:16px auto 0;color:#aaa3b1;font-size:14px;line-height:1.65}
.os-radar{margin:34px auto 0;max-width:900px}.os-radar svg{width:100%;height:auto;filter:drop-shadow(0 30px 50px rgba(0,0,0,.35))}
.os-radar .grid{fill:none;stroke:rgba(255,255,255,.075);stroke-width:1}.os-radar .axis{stroke:rgba(184,149,255,.10);stroke-width:1}.os-radar .fill{fill:rgba(138,92,255,.13);stroke:#b895ff;stroke-width:2.5;filter:drop-shadow(0 0 18px rgba(138,92,255,.30))}.os-radar .pt{fill:#fff;stroke:#b895ff;stroke-width:2}.os-radar .lbl{fill:#aaa3b1;font-size:11px;font-weight:850}
.os-triad{margin:34px auto 0;max-width:840px;display:grid;grid-template-columns:repeat(3,1fr);gap:30px;text-align:left}
.os-triad-item{padding-top:14px;border-top:1px solid rgba(184,149,255,.15)}
.os-triad-item span{display:block;color:#8d8596;font-size:9px;font-weight:950;letter-spacing:.16em;text-transform:uppercase}.os-triad-item strong{display:block;margin-top:8px;font-size:18px}.os-triad-item p{margin:6px 0 0;color:#9e96a7;font-size:12px;line-height:1.5}

/* Make the Master Key a single intellectual gesture. */
.os-system{margin-top:112px;padding:58px 0 64px;border-top:1px solid rgba(184,149,255,.11);border-bottom:1px solid rgba(184,149,255,.11);text-align:center}
.os-system h3{margin:10px auto 0;max-width:820px;font-size:clamp(34px,4.8vw,58px);line-height:.98;letter-spacing:-.045em}.os-system p{max-width:720px;margin:15px auto 0;color:#aaa3b1;font-size:14px;line-height:1.65}
.os-sequence{display:flex;justify-content:center;align-items:center;gap:0;margin:34px auto 0;overflow:auto;padding:8px 0 14px;scrollbar-width:thin}.os-sequence span{color:#f2edf5;font-size:13px;font-weight:950;white-space:nowrap}.os-sequence span:not(:last-child)::after{content:'→';margin:0 10px;color:#7d7488}

/* Naya as a single premium encounter, not an expert catalogue. */
.os-naya{margin-top:112px;display:grid;grid-template-columns:auto minmax(0,1fr);gap:28px;align-items:center}
.os-orb{width:112px;height:112px;border-radius:50%;background:radial-gradient(circle at 30% 18%,#fff 0,#ded0ff 12%,#946dff 38%,#3b1b83 70%,#09050f 100%);border:1px solid #e4d9ff;box-shadow:inset 0 2px 5px rgba(255,255,255,.75),0 0 42px rgba(116,76,255,.42),0 14px 28px rgba(0,0,0,.5);display:grid;place-items:center;color:#fff;font-size:28px;font-weight:1000}
.os-naya-name{color:#b895ff;font-size:10px;font-weight:950;letter-spacing:.20em;text-transform:uppercase}.os-naya h3{margin:7px 0 0;font-size:clamp(30px,4.5vw,54px);line-height:.98;letter-spacing:-.04em}.os-naya blockquote{margin:12px 0 0;max-width:820px;color:#ddd6e4;font-size:18px;line-height:1.55}.os-naya small{display:block;margin-top:12px;color:#797082;font-size:11px;line-height:1.5}

/* Replace four-master card wall with one art-directed stage. */
.os-masters{margin-top:112px}.os-masters-head{display:flex;justify-content:space-between;gap:28px;align-items:end}.os-masters-head h3{margin:10px 0 0;max-width:720px;font-size:clamp(34px,4.8vw,58px);line-height:.98;letter-spacing:-.045em}.os-masters-head p{max-width:420px;margin:0;color:#8f8798;font-size:13px;line-height:1.55}
.os-master-stage{margin-top:32px;position:relative;display:grid;grid-template-columns:1.25fr 1fr;gap:14px}.os-master-main,.os-master-mini{position:relative;overflow:hidden;border-radius:32px;border:1px solid rgba(184,149,255,.18);background:radial-gradient(circle at 18% 8%,rgba(138,92,255,.16),transparent 46%),linear-gradient(145deg,rgba(255,255,255,.05),rgba(255,255,255,.012));box-shadow:inset 0 1px 0 rgba(255,255,255,.06),0 24px 50px rgba(0,0,0,.34)}
.os-master-main{min-height:390px;padding:32px}.os-master-mini{padding:22px;display:flex;align-items:end;min-height:188px}
.os-master-mini-wrap{display:grid;grid-template-rows:1fr 1fr;gap:14px}.os-gem{width:64px;height:64px;border-radius:22px;display:grid;place-items:center;color:#fff;font-size:20px;border:1px solid rgba(255,255,255,.72);background:radial-gradient(circle at 30% 16%,#fff 0,#ddd1ff 12%,#8a5cff 42%,#0b0711 100%);box-shadow:inset 0 2px 5px rgba(255,255,255,.74),0 0 28px rgba(138,92,255,.23),0 12px 20px rgba(0,0,0,.42)}
.os-master-mini:nth-child(2) .os-gem{background:radial-gradient(circle at 30% 16%,#fff 0,#ddd1ff 12%,#3ca8ff 42%,#06101a 100%)}.os-master-mini:nth-child(3) .os-gem{background:radial-gradient(circle at 30% 16%,#fff 0,#ddd1ff 12%,#35e39b 42%,#06110b 100%)}
.os-master-main h4{margin:22px 0 0;font-size:clamp(28px,4vw,46px);line-height:1.00;letter-spacing:-.04em}.os-master-main span,.os-master-mini span{display:block;margin-top:8px;color:#b895ff;font-size:10px;font-weight:950;letter-spacing:.14em;text-transform:uppercase}.os-master-main p,.os-master-mini p{max-width:640px;margin:14px 0 0;color:#aaa3b1;font-size:13px;line-height:1.62}.os-master-mini h5{margin:0;font-size:20px;line-height:1.05}.os-master-mini-copy{min-width:0}.os-master-mini .os-gem{margin-right:16px;flex:0 0 auto;width:54px;height:54px;border-radius:18px}

.os-final{margin-top:112px;text-align:center;padding:72px 0 24px;border-top:1px solid rgba(184,149,255,.12)}.os-final h3{max-width:860px;margin:10px auto 0;font-size:clamp(42px,6vw,72px);line-height:.94;letter-spacing:-.05em}.os-final p{max-width:680px;margin:16px auto 0;color:#a59eac;font-size:15px;line-height:1.65}.os-cta-row{display:flex;justify-content:center;gap:10px;flex-wrap:wrap;margin-top:28px}.os-cta{min-height:58px;padding:0 26px;border-radius:19px;font-weight:950;cursor:pointer}.os-cta.primary{border:1px solid rgba(205,188,255,.65);background:linear-gradient(180deg,#b895ff,#765cff);color:#09060f;box-shadow:0 18px 45px rgba(138,92,255,.20)}.os-cta.secondary{border:1px solid rgba(255,255,255,.14);background:#08080b;color:#fff}.os-footnote{margin-top:20px;color:#6f6778;font-size:10px}

.os-mounted~*{display:none!important}
@media(max-width:820px){.os-reveal{grid-template-columns:1fr;gap:28px}.os-triad{grid-template-columns:1fr;gap:20px}.os-master-stage{grid-template-columns:1fr}.os-master-mini-wrap{grid-template-rows:none;grid-template-columns:1fr 1fr}.os-master-mini{min-height:180px}.os-masters-head{display:block}.os-masters-head p{margin-top:12px}.os-naya{grid-template-columns:1fr;text-align:center}.os-orb{margin:0 auto}.os-naya blockquote{margin-left:auto;margin-right:auto}}
@media(max-width:560px){.os-head{margin-top:68px}.os-sequence{justify-content:flex-start}.os-master-mini-wrap{grid-template-columns:1fr}.os-master-main{min-height:340px;padding:24px}.os-master-mini{min-height:150px}}
'''

if '</style>' not in s: raise RuntimeError('missing style close')
s=s.replace('</style>',CSS+'\n</style>',1)

JS=r'''
(function(){
 const root=document.getElementById('resultsView'); if(!root) return;
 const mount=()=>{
  if(!root.classList.contains('visible') || root.dataset.osSuper==='1') return;
  const shell=root.querySelector('.maxess-clean-results'); if(!shell) return;
  const score=Math.round(Number(document.getElementById('overallScore')?.textContent||0));
  const dims=[...root.querySelectorAll('#dimensionConstellation .dimension-orb')].map((el,i)=>({name:el.querySelector('.dimension-name')?.textContent?.trim()||['Direction','Communication','Evaluation','Iteration','Systems Thinking'][i]||'Dimension',score:Number(el.querySelector('.dimension-score')?.textContent||0)}));
  dims.sort((a,b)=>b.score-a.score); const hi=dims[0]||{name:'Direction',score:score}; const lo=dims[dims.length-1]||hi;
  const src=shell.querySelector('.cr-signature-visual')?.innerHTML||shell.querySelector('.cr-signature-visual')?.outerHTML||'';
  const el=document.createElement('section'); el.className='maxess-oscar-superpass';
  el.innerHTML=`
   <div class="os-head"><div class="os-kicker">THE RESULTS ARE YOURS</div><h2>This is not a report.<br><span style="color:#b895ff">It's a map of your capability.</span></h2><p>Your score tells us where you are. The pattern underneath it tells us how you work — and where the next meaningful improvement can happen.</p></div>
   <div class="os-reveal"><div class="os-reveal-quote">Your natural advantage is <em>${escapeHTML(hi.name)}</em>.<br>Your next leverage is <em>${escapeHTML(lo.name)}</em>.</div><div class="os-reveal-side"><strong>${score}/100</strong><p>One number. Five capabilities. A much more useful picture than a grade alone.</p></div></div>
   <div class="os-fingerprint"><div class="os-kicker">YOUR AI FINGERPRINT</div><h3>The shape underneath your score.</h3><p>There is no perfect shape. There is only your shape — and the opportunity to make it more capable over time.</p><div class="os-radar">${src}</div><div class="os-triad"><div class="os-triad-item"><span>Your advantage</span><strong>${escapeHTML(hi.name)}</strong><p>${hi.score}/100 · the capability you can already lean on.</p></div><div class="os-triad-item"><span>Your tension</span><strong>${escapeHTML(lo.name)}</strong><p>${lo.score}/100 · the area with the clearest room for deliberate growth.</p></div><div class="os-triad-item"><span>Your next lever</span><strong>Better judgment</strong><p>Use the score to decide what to keep, what to improve, and what to turn into a repeatable method.</p></div></div></div>
   <div class="os-system"><div class="os-kicker">THE OPERATING SYSTEM</div><h3>AI is the engine.<br><span style="color:#b895ff">You are the director.</span></h3><p>Know the destination. Give the context. Shape the request. Inspect the result. Judge it. Improve it. Repeat.</p><div class="os-sequence">${['KNOW','TELL','ASK','LOOK','SCORE','IMPROVE','REPEAT'].map(x=>`<span>${x}</span>`).join('')}</div></div>
   <div class="os-naya"><div class="os-orb">N</div><div><div class="os-naya-name">NAYA · PERSONAL GUIDE</div><h3>“Okay. Now we know where to look.”</h3><blockquote>Your result isn't a verdict. It's a starting point. Keep the capability that's already working. Practice the one that creates the most leverage. Then use that combination to make something real.</blockquote><small>Naya appears here to interpret the pattern — not to take over your experience.</small></div></div>
   <div class="os-masters"><div class="os-masters-head"><div><div class="os-kicker">NAYA · MASTER INTELLIGENCE</div><h3>When the work gets specific, the intelligence gets specific.</h3></div><p>Not eighteen cards. Not a catalogue. A small, visual introduction to the kinds of mastery Naya can bring to the work in front of you.</p></div><div class="os-master-stage"><article class="os-master-main"><div class="os-gem">✦</div><h4>Naya Master ${escapeHTML(hi.name)}</h4><span>Your strongest current capability</span><p>Start with what is already working. Use this strength as the foundation for everything you build next.</p></article><div class="os-master-mini-wrap"><article class="os-master-mini"><div class="os-gem">◆</div><div class="os-master-mini-copy"><h5>Naya Master ${escapeHTML(lo.name)}</h5><span>Your leverage opportunity</span><p>Practice the capability with the clearest upside.</p></div></article><article class="os-master-mini"><div class="os-gem">△</div><div class="os-master-mini-copy"><h5>Naya Master Strategist</h5><span>From intent to action</span><p>Turn ideas into priorities, plans, and decisions.</p></div></article></div></div></div>
   <div class="os-final"><div class="os-kicker">YOUR NEXT CHAPTER</div><h3>Now make the capability real.</h3><p>You know more about where you are. You know where the leverage is. The next move is to use it — in work, learning, creation, or something that matters to you.</p><div class="os-cta-row"><button class="os-cta primary" type="button" data-os-go="1">MASTER AI</button><button class="os-cta secondary" type="button" data-os-save="1">SAVE MY RESULTS</button></div><div class="os-footnote">Your MAXESS result is a capability snapshot based on your assessment responses. It is not a diagnosis, prediction, or guarantee.</div></div>`;
  shell.parentElement.appendChild(el); root.dataset.osSuper='1'; el.querySelector('[data-os-go]')?.addEventListener('click',()=>document.getElementById('freeTrialButton')?.click()); el.querySelector('[data-os-save]')?.addEventListener('click',()=>document.getElementById('pdfButton')?.click());
 };
 new MutationObserver(mount).observe(root,{attributes:true,attributeFilter:['class']}); mount();
})();
'''

# insert CSS + JS; the existing self-contained renderer will keep its truth/data alive.
s=s.replace('</style>',CSS+'\n</style>',1)
s=s.replace('</script>',JS+'\n</script>',1)
# Suppress the immediately prior visible lower composition when this pass mounts.
s=s.replace('.cr-cinematic-mounted .cr-legacy-hidden{display:none!important}', '.cr-cinematic-mounted .cr-legacy-hidden{display:none!important}\n.os-superpass-hidden{display:none!important}')

p.write_text(s,encoding='utf-8')
print('Oscar superpass applied')
