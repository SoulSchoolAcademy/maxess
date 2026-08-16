/* MAXESS AAA Results Enhancement Runtime
   Emotional reveal + one clear next move per canonical AI dimension + Naya handoff.
*/
(function(){
  'use strict';
  const getResult=()=>window.MAXESS_RESULT||window.maxessResult||window.__MAXESS_RESULT||null;
  const clamp=(n,min,max)=>Math.max(min,Math.min(max,n));
  const scoreOf=(d)=>typeof d==='number'?d:typeof d?.score==='number'?d.score:0;
  const canonical=['Direction','Communication','Evaluation','Iteration','Systems Thinking'];
  const nameOf=(d,i)=>d?.name||d?.label||canonical[i]||`Dimension ${i+1}`;
  const iconOf=(i)=>['◎','✦','◉','↻','◇'][i]||'•';
  const nextStep=(name,score)=>{
    const n=name.toLowerCase();
    if(n.includes('direction')) return score>=75?'Turn your strongest goals into repeatable AI briefs with a clear outcome and decision standard.':'Before prompting, define the outcome, constraints, audience, and what a successful answer must accomplish.';
    if(n.includes('communication')) return score>=75?'Turn your communication strength into reusable AI templates for writing, teaching, selling, and explaining.':'Practice giving AI audience, purpose, tone, examples, and a clear definition of “good” before asking it to create.';
    if(n.includes('evaluation')) return score>=75?'Make scorecards part of every important AI workflow so quality improves before you ship.':'Before accepting an AI answer, define the criteria, inspect the evidence, and ask what is missing or weak.';
    if(n.includes('iteration')) return score>=75?'Turn Create → Score → Improve → Repeat into your default AI working rhythm.':'Take one real AI output through at least two deliberate improvement passes instead of accepting version one.';
    if(n.includes('systems')) return score>=75?'Package your best AI workflows into reusable systems that compound over time.':'Stop solving the same task twice: document one successful workflow and turn it into a reusable system.';
    return score>=75?'Turn this strength into one repeatable system you can use every week.':'Choose one real task this week and deliberately practice this capability from start to finish.';
  };
  function mount(){
    const tower=document.querySelector('.mx-tower');
    if(!tower||tower.dataset.aaaEnhancements==='1') return;
    tower.dataset.aaaEnhancements='1';
    const result=getResult()||{};
    const score=clamp(Number(result.score??result.overallScore??result.totalScore??0)||0,0,100);
    const dims=Array.isArray(result.dimensions)?result.dimensions:(Array.isArray(result.scores)?result.scores:[]);
    const dimensionData=dims.slice(0,5);
    const reveal=document.createElement('section');
    reveal.className='mx-reveal-enhancement mx-cinematic-reveal';
    reveal.setAttribute('aria-labelledby','mx-reveal-title');
    reveal.innerHTML=`<div class="mx-reveal-enhancement__inner"><div class="mx-reveal-enhancement__eyebrow">Your MAXESS revelation</div><h1 id="mx-reveal-title">This is how<br><span>you work with AI.</span></h1><div class="mx-reveal-enhancement__sub">Your assessment is more than a score. It is a picture of how you naturally think, create, judge, improve, and build with AI — and where one smart move can change your trajectory.</div><div class="mx-reveal-enhancement__score">Overall AI Mastery · <strong data-reveal-score>0</strong> / 100</div><div class="mx-reveal-enhancement__scroll">Your unique pattern is waiting below<span></span></div></div>`;
    const firstSection=tower.querySelector('.mx-section');
    if(firstSection) firstSection.before(reveal); else tower.prepend(reveal);
    const scoreNode=reveal.querySelector('[data-reveal-score]');
    const start=performance.now(),duration=1900;
    const tick=(now)=>{const p=Math.min(1,(now-start)/duration);const eased=1-Math.pow(1-p,4);scoreNode.textContent=Math.round(score*eased);if(p<1)requestAnimationFrame(tick)};
    requestAnimationFrame(tick);

    const mountPoint=tower.querySelector('#nayanet-source-mount');
    const next=document.createElement('section');
    next.className='mx-next-move';
    next.setAttribute('aria-labelledby','mx-next-move-title');
    const cards=dimensionData.map((d,i)=>{const s=scoreOf(d);return `<article class="mx-next-move__card"><div class="mx-next-move__number">MOVE 0${i+1}</div><div class="mx-next-move__icon" aria-hidden="true">${iconOf(i)}</div><div class="mx-next-move__name">${nameOf(d,i)}</div><div class="mx-next-move__step">${nextStep(nameOf(d,i),s)}</div><div class="mx-next-move__tag">One clear next move</div></article>`}).join('');
    next.innerHTML=`<div class="mx-next-move__inner"><div class="mx-kicker"><i></i> Your growth path</div><h2 id="mx-next-move-title" class="mx-next-move__heading">Don't wonder what to do next.<br><span>Here's your move.</span></h2><p class="mx-next-move__lead">You do not need to improve everything at once. Each dimension gives you one practical move. Start with the highest-leverage one, practice it on something real, and let the results teach you what comes next.</p><div class="mx-next-move__grid">${cards||'<article class="mx-next-move__card"><div class="mx-next-move__number">NEXT MOVE</div><div class="mx-next-move__icon">→</div><div class="mx-next-move__name">Start with one real task</div><div class="mx-next-move__step">Bring one meaningful task to Naya and use it as your first practice arena.</div><div class="mx-next-move__tag">One clear next move</div></article>'}</div><div class="mx-naya-bridge"><div class="mx-naya-bridge__copy"><strong>Your results don't end here.</strong><span>Naya can start with this profile instead of making you explain yourself all over again.</span></div><button class="mx-button" type="button" data-continue-naya><span class="mx-button-icon">→</span><span class="mx-button-copy"><span class="mx-button-title">Continue with Naya</span><span class="mx-button-sub">Carry my MAXESS profile forward</span></span></button></div></div>`;
    if(mountPoint) mountPoint.before(next); else tower.appendChild(next);

    const handoff=next.querySelector('[data-continue-naya]');
    handoff.addEventListener('click',()=>{
      const payload={source:'MAXESS',version:1,result,timestamp:new Date().toISOString()};
      try{localStorage.setItem('MAXESS_NAYA_CONTEXT',JSON.stringify(payload));sessionStorage.setItem('MAXESS_NAYA_CONTEXT',JSON.stringify(payload));}catch(e){}
      window.MAXESS_NAYA_CONTEXT=payload;
      window.dispatchEvent(new CustomEvent('maxess:naya-context',{detail:payload}));
      const target=document.querySelector('[data-naya-chat],#naya-chat,#naya')||mountPoint;
      if(target) target.scrollIntoView({behavior:'smooth',block:'start'});
      try{if(typeof window.openNaya==='function') window.openNaya(payload); else if(typeof window.startNayaChat==='function') window.startNayaChat(payload); else if(typeof window.Naya?.open==='function') window.Naya.open(payload);}catch(e){}
      handoff.setAttribute('aria-label','MAXESS profile saved. Continue with Naya below.');
      handoff.dataset.contextReady='1';
    });
  }
  if(document.readyState==='loading') document.addEventListener('DOMContentLoaded',mount,{once:true}); else mount();
})();
