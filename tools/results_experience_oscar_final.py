from pathlib import Path

p = Path('code')
s = p.read_text(encoding='utf-8')
MARKER = 'MAXESS RESULTS EXPERIENCE OSCAR FINAL'
if MARKER in s:
    print('Oscar final already applied')
    raise SystemExit(0)

CSS = r'''
/* =========================================================
   MAXESS RESULTS EXPERIENCE OSCAR FINAL
   Remove weak card-dense presentation; replace with editorial,
   cinematic compositions. Fancy jewel language is semantic.
========================================================= */
.maxess-oscar-finale{--purple:#8a5cff;--lav:#b895ff;--sapphire:#3ca8ff;--emerald:#35e39b;--violet:#765cff;--magenta:#ed42c4;color:#f8f7fb;margin-top:76px;padding:48px 36px 54px;border:1px solid rgba(184,149,255,.20);border-radius:38px;background:radial-gradient(circle at 50% 0,rgba(138,92,255,.13),transparent 42%),linear-gradient(145deg,#0b0810,#030305 72%);box-shadow:0 30px 90px rgba(0,0,0,.46),inset 0 1px 0 rgba(255,255,255,.07)}
.maxess-oscar-kicker{color:var(--lav);font-size:9px;font-weight:950;letter-spacing:.22em;text-transform:uppercase}
.maxess-oscar-finale h3{margin:10px 0 0;font-size:clamp(28px,4vw,44px);line-height:1.02;letter-spacing:-.035em}.maxess-oscar-finale .lead{max-width:760px;margin:12px 0 0;color:#aaa5b3;font-size:14px;line-height:1.62}
.maxess-oscar-spine{display:grid;grid-template-columns:repeat(5,minmax(0,1fr));gap:9px;margin:30px 0 0}.maxess-oscar-spine .j{height:84px;padding:12px 8px;border:1px solid rgba(255,255,255,.07);border-radius:20px;background:rgba(255,255,255,.018);display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center}.maxess-oscar-spine .gem{width:38px;height:38px;border-radius:13px;display:grid;place-items:center;color:#fff;font-size:14px;font-weight:1000;border:1px solid rgba(255,255,255,.65);box-shadow:inset 0 2px 4px rgba(255,255,255,.70),0 0 20px rgba(138,92,255,.16)}.maxess-oscar-spine .t{margin-top:8px;color:#a9a3b1;font-size:8px;font-weight:900;letter-spacing:.08em;text-transform:uppercase}
.maxess-oscar-path{margin-top:28px;padding:26px 0 0;border-top:1px solid rgba(184,149,255,.10);display:grid;grid-template-columns:1fr auto 1fr;gap:18px;align-items:center}.maxess-oscar-path .way{padding:22px 0}.maxess-oscar-path .way h4{margin:0;color:#fff;font-size:14px}.maxess-oscar-path .way p{margin:7px 0 0;color:#a8a2b0;font-size:12px;line-height:1.5}.maxess-oscar-path .arrow{color:#b895ff;font-size:28px;font-weight:300}.maxess-oscar-door{margin-top:26px;padding:30px;border-radius:30px;border:1px solid rgba(184,149,255,.18);background:linear-gradient(145deg,rgba(138,92,255,.07),rgba(255,255,255,.014));text-align:center}.maxess-oscar-door h4{margin:6px 0 0;font-size:clamp(22px,3vw,32px)}.maxess-oscar-door p{max-width:660px;margin:9px auto 0;color:#aaa5b2;font-size:13px;line-height:1.6}.maxess-oscar-door .doors{display:flex;justify-content:center;gap:18px;flex-wrap:wrap;margin-top:24px}.maxess-oscar-door .door{min-width:150px;padding:17px 16px;border-radius:22px;border:1px solid rgba(184,149,255,.16);background:rgba(255,255,255,.018);text-align:left}.maxess-oscar-door .door .gem{width:42px;height:42px;border-radius:14px;display:grid;place-items:center;color:#fff;font-size:15px;font-weight:1000;border:1px solid rgba(255,255,255,.65);box-shadow:inset 0 2px 4px rgba(255,255,255,.70),0 0 20px rgba(138,92,255,.15)}.maxess-oscar-door .door strong{display:block;margin-top:10px;color:#fff;font-size:13px;line-height:1.2}.maxess-oscar-door .door span{display:block;margin-top:4px;color:#918a99;font-size:9px;line-height:1.35}
.maxess-oscar-naya{margin-top:26px;padding:30px;border-radius:32px;background:radial-gradient(circle at 9% 0,rgba(138,92,255,.16),transparent 36%),linear-gradient(145deg,#100b17,#050507);border:1px solid rgba(184,149,255,.22);display:flex;gap:20px;align-items:center}.maxess-oscar-naya .orb{width:74px;height:74px;flex:0 0 auto;border-radius:50%;background:radial-gradient(circle at 30% 18%,#fff 0,#dfd1ff 12%,#946dff 38%,#3b1b83 70%,#09050f 100%);border:1px solid #e4d9ff;box-shadow:inset 0 2px 4px rgba(255,255,255,.76),0 0 28px rgba(116,76,255,.36),0 10px 18px rgba(0,0,0,.45);display:grid;place-items:center;color:#fff;font-size:22px;font-weight:1000}.maxess-oscar-naya .ey{color:var(--lav);font-size:9px;font-weight:950;letter-spacing:.18em;text-transform:uppercase}.maxess-oscar-naya strong{display:block;margin-top:7px;font-size:18px}.maxess-oscar-naya p{margin:7px 0 0;color:#b3acbb;font-size:12px;line-height:1.55}
.maxess-oscar-final{margin-top:26px;padding:44px 32px;text-align:center;border-radius:38px;border:1px solid rgba(184,149,255,.22);background:radial-gradient(circle at 50% 0,rgba(138,92,255,.19),transparent 52%),linear-gradient(145deg,#0d0914,#030305);box-shadow:0 30px 90px rgba(0,0,0,.50),0 0 65px rgba(138,92,255,.08),inset 0 1px 0 rgba(255,255,255,.08)}
.maxess-oscar-final .k{color:var(--lav);font-size:9px;font-weight:950;letter-spacing:.20em;text-transform:uppercase}.maxess-oscar-final h4{margin:9px auto 0;max-width:720px;font-size:clamp(28px,4vw,46px);line-height:1.02;letter-spacing:-.035em}.maxess-oscar-final p{max-width:650px;margin:12px auto 0;color:#aaa5b2;font-size:13px;line-height:1.58}.maxess-oscar-final .actions{display:flex;justify-content:center;gap:10px;flex-wrap:wrap;margin-top:24px}.maxess-oscar-final button{min-height:54px;padding:0 22px;border-radius:18px;font-weight:950;cursor:pointer;border:1px solid rgba(184,149,255,.55)}.maxess-oscar-final .primary{background:linear-gradient(180deg,#b895ff,#765cff);color:#09060e;box-shadow:0 15px 34px rgba(138,92,255,.20)}.maxess-oscar-final .secondary{background:#07070a;color:#fff;border-color:rgba(255,255,255,.14)}
.maxess-oscar-disclaimer{margin-top:18px;text-align:center;color:#70697a;font-size:9px;line-height:1.45}
.legacy-hide-oscar{display:none!important}
.maxess-personal-editorial{margin:24px auto 0;max-width:980px;padding:8px 4px 0}.maxess-personal-editorial .k{color:#b895ff;font-size:9px;font-weight:950;letter-spacing:.20em;text-transform:uppercase}.maxess-personal-editorial h3{margin:10px 0 0;max-width:850px;font-size:clamp(28px,4vw,46px);line-height:1.02;letter-spacing:-.035em}.maxess-personal-editorial p{max-width:780px;margin:12px 0 0;color:#b8b1bf;font-size:15px;line-height:1.65}.maxess-personal-editorial .signal{margin-top:20px;display:flex;gap:12px;flex-wrap:wrap}.maxess-personal-editorial .signal span{padding:9px 12px;border-bottom:1px solid rgba(184,149,255,.22);color:#d7d1de;font-size:11px;font-weight:850}.maxess-personal-editorial .signal span b{color:#b895ff}
@media(max-width:760px){.maxess-oscar-finale{padding:34px 20px 40px;border-radius:30px}.maxess-oscar-spine{grid-template-columns:repeat(5,minmax(44px,1fr));gap:6px}.maxess-oscar-spine .j{height:76px;padding:9px 4px}.maxess-oscar-spine .gem{width:32px;height:32px;border-radius:11px}.maxess-oscar-spine .t{font-size:7px}.maxess-oscar-path{grid-template-columns:1fr;gap:4px}.maxess-oscar-path .arrow{display:none}.maxess-oscar-naya{align-items:flex-start}.maxess-oscar-naya .orb{width:58px;height:58px}.maxess-oscar-door{padding:24px 16px}.maxess-oscar-door .doors{gap:8px}.maxess-oscar-door .door{min-width:140px}.maxess-oscar-final{padding:34px 20px;border-radius:30px}.maxess-personal-editorial{padding-top:6px}.maxess-personal-editorial p{font-size:14px}}
'''

JS = r'''

(function(){
  const root=document.getElementById('resultsView');
  if(!root || root.dataset.maxessOscarFinal==='1') return;
  const run=()=>{
    if(!root.classList.contains('visible') || root.dataset.maxessOscarFinal==='1') return;
    const scoreEl=document.getElementById('overallScore');
    const strongestText=document.getElementById('strongestText');
    const dims=[...root.querySelectorAll('#dimensionConstellation .dimension-orb')].map(el=>({name:el.querySelector('.dimension-name')?.textContent?.trim()||'Dimension',score:Number(el.querySelector('.dimension-score')?.textContent||0)}));
    if(!dims.length) return;
    const strongest=[...dims].sort((a,b)=>b.score-a.score)[0];
    const opportunity=[...dims].sort((a,b)=>a.score-b.score)[0];
    const score=Math.round(Number(scoreEl?.textContent||0));

    const hero=root.querySelector('.result-hero');
    if(hero){
      hero.querySelector('.result-eyebrow')?.replaceChildren(document.createTextNode('YOUR PERSONALIZED ANALYSIS'));
      const title=hero.querySelector('.result-title');
      if(title) title.textContent='What your score tells the story.';
      const sub=hero.querySelector('.result-subtitle');
      if(sub) sub.textContent=`Your ${score}/100 is a capability snapshot — the beginning of understanding how you work with AI.`;
    }

    root.querySelectorAll('.maxess-signal').forEach(el=>el.classList.add('legacy-hide-oscar'));
    root.querySelectorAll('.maxess-opportunities,.maxess-naya-masters,.maxess-threshold,.maxess-oscar-finale').forEach(el=>el.remove());

    const oldHeroSignal=root.querySelector('.maxess-results-reveal');
    if(oldHeroSignal) oldHeroSignal.textContent='EXPLORE WHAT YOUR SCORE REVEALS';

    const editorial=document.createElement('section');
    editorial.className='maxess-personal-editorial';
    editorial.innerHTML=`<div class="k">YOUR PERSONALIZED ANALYSIS</div><h3>You are already bringing ${escape(strongest.name).toLowerCase()} to your AI work.</h3><p>${escape(strongestText?.textContent||`Your strongest current capability is ${strongest.name}.`)} The most useful next move is not to fix everything. It is to keep that advantage while deliberately developing ${escape(opportunity.name)}.</p><div class="signal"><span><b>${score}</b> · MAXESS SCORE</span><span><b>${escape(strongest.name)}</b> · NATURAL ADVANTAGE</span><span><b>${escape(opportunity.name)}</b> · LEVERAGE OPPORTUNITY</span></div>`;
    if(hero) hero.insertAdjacentElement('afterend',editorial);

    const mk=root.querySelector('.maxess-masterkey-10');
    if(mk) mk.classList.add('legacy-hide-oscar');
    const existingMk=root.querySelector('.maxess-results-v4-masterkey');
    if(existingMk) existingMk.classList.add('legacy-hide-oscar');

    const sig=root.querySelector('.maxess-signature-shell');
    const anchor=mk||sig||root.querySelector('.maxess-naya-guide');
    if(!anchor) return;

    const jewels=[['◆','#ffd45a'],['✦','#35e39b'],['△','#3ca8ff'],['✧','#765cff'],['✦','#ed42c4']];
    const doors=[
      [strongest.name,'Your natural advantage'],
      [opportunity.name,'Where your next leverage lives'],
      ['Master AI','Turn capability into practical output'],
      ['Create','Apply your capability to something real'],
      ['Earn','Convert useful work into value']
    ];
    const finale=document.createElement('section');
    finale.className='maxess-oscar-finale';
    finale.innerHTML=`<div class="maxess-oscar-kicker">YOUR NEXT CHAPTER</div><h3>Now turn insight into capability.</h3><p class="lead">You know more about where you are. The next step is choosing where to grow — and then putting that capability to work.</p><div class="maxess-oscar-spine">${jewels.map((j,i)=>`<div class="j"><div class="gem" style="background:radial-gradient(circle at 30% 20%,#fff 0,#d9d3ff 13%,${j[1]} 44%,#08050d 100%)">${j[0]}</div><div class="t">${['KNOW','LEARN','APPLY','CREATE','EARN'][i]}</div></div>`).join('')}</div><div class="maxess-oscar-path"><div class="way"><h4>From capability</h4><p>Understand your advantage and the opportunity in front of you.</p></div><div class="arrow">→</div><div class="way"><h4>To possibility</h4><p>Choose a door that matters to you and practice it in real work.</p></div></div><div class="maxess-oscar-door"><div class="maxess-oscar-kicker">YOUR DOORS</div><h4>Five ways to move forward.</h4><p>These are not products or a catalogue. They are simple directions you can take from this result.</p><div class="doors">${doors.map((d,i)=>{const j=jewels[i];return `<div class="door"><div class="gem" style="background:radial-gradient(circle at 30% 20%,#fff 0,#d9d3ff 13%,${j[1]} 44%,#08050d 100%)">${j[0]}</div><strong>${escape(d[0])}</strong><span>${escape(d[1])}</span></div>`}).join('')}</div></div><div class="maxess-oscar-naya"><div class="orb">N</div><div><div class="ey">NAYA · YOUR PERSONAL GUIDE</div><strong>“Okay. Now we know where to look.”</strong><p>${escape(opportunity.name)} is the place to experiment next. Start small, judge the result honestly, and improve it deliberately.</p></div></div><div class="maxess-oscar-final"><div class="k">READY TO GO FURTHER?</div><h4>Your result shows you where you are. Now let's build what comes next.</h4><p>KNOW → LEARN → APPLY → CREATE → SHARE → EARN. Capability first. Opportunity second. No hype. No guarantees.</p><div class="actions"><button type="button" class="primary" data-oscar-master>MASTER AI →</button><button type="button" class="secondary" data-oscar-save>SAVE MY RESULTS</button></div></div><div class="maxess-oscar-disclaimer">Your MAXESS result is a capability snapshot based on your assessment responses. It is not a diagnosis, prediction, or guarantee.</div>`;
    anchor.insertAdjacentElement('afterend',finale);

    finale.querySelector('[data-oscar-master]')?.addEventListener('click',()=>document.getElementById('freeTrialButton')?.click());
    finale.querySelector('[data-oscar-save]')?.addEventListener('click',()=>document.getElementById('pdfButton')?.click());
    root.dataset.maxessOscarFinal='1';
  };
  const obs=new MutationObserver(run); obs.observe(root,{attributes:true,attributeFilter:['class']});
  run();
})();
'''

if '</style>' not in s:
    raise RuntimeError('style closing tag missing')
s=s.replace('</style>',CSS+'\n</style>',1)
if '</body>' in s:
    s=s.replace('</body>',JS+'\n</body>',1)
else:
    s=s.replace('</html>',JS+'\n</html>',1)

p.write_text(s,encoding='utf-8')
print('Oscar final results presentation applied')
