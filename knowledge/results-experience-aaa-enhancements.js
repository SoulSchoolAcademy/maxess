/* MAXESS AAA Results Enhancement Runtime
   Adds emotional reveal, one-action-per-dimension guidance, and a persistent Naya handoff.
*/
(function(){
  'use strict';
  const getResult=()=>window.MAXESS_RESULT||window.maxessResult||window.__MAXESS_RESULT||null;
  const clamp=(n,min,max)=>Math.max(min,Math.min(max,n));
  const scoreOf=(d)=>typeof d==='number'?d:typeof d?.score==='number'?d.score:0;
  const nameOf=(d,i)=>d?.name||d?.label||['Writing & Communication','Research & Information','Ideas & Brainstorming','Content Creation','Business & Strategy'][i]||`Dimension ${i+1}`;
  const iconOf=(i)=>['✦','⌕','✧','◈','◆'][i]||'•';
  const nextStep=(name,score)=>{
    const n=name.toLowerCase();
    if(n.includes('writing')||n.includes('communication')) return score>=75?'Turn your strongest ideas into reusable AI-assisted communication systems.':'Practice giving AI a clear audience, purpose, tone, and success standard before asking it to write.';
    if(n.includes('research')||n.includes('information')) return score>=75?'Build a repeatable verify-and-summarize research workflow.':'Practice asking for sources, uncertainty, competing explanations, and a concise evidence summary.';
    if(n.includes('brainstorm')||n.includes('idea')) return score>=75?'Use AI to expand, challenge, rank, and stress-test your best ideas.':'Run one idea through expand → challenge → rank → improve instead of stopping at the first answer.';
    if(n.includes('content')) return score>=75?'Turn one strong idea into a repeatable multi-format content engine.':'Practice transforming one core idea into a hook, outline, draft, visual concept, and distribution plan.';
    if(n.includes('business')||n.includes('strategy')) return score>=75?'Use AI as a strategic thinking partner: options, tradeoffs, risks, decision, action.':'Give AI the goal, constraints, alternatives, risks, and decision criteria before asking for strategy.';
    if(n.includes('marketing')||n.includes('sales')) return 'Practice customer → problem → promise → proof → action as one connected AI workflow.';
    if(n.includes('learning')||n.includes('education')) return 'Ask AI to teach, test, adapt, and reteach until you can explain the idea yourself.';
    if(n.includes('coding')||n.includes('software')) return 'Give AI the desired behavior, constraints, current code, tests, and acceptance criteria before building.';
    return score>=75?'Turn this strength into a repeatable system you can use every week.':'Choose one real task this week and deliberately practice this capability from start to finish.';
  };
  function encodeContext(result){
    try{return btoa(unescape(encodeURIComponent(JSON.stringify({source:'MAXESS',version:1,result,timestamp:new Date().toISOString()}))))}catch(e){return ''}
  }
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
    reveal.innerHTML=`<div class="mx-reveal-enhancement__inner"><div class="mx-reveal-enhancement__eyebrow">Your MAXESS revelation</div><h1 id="mx-reveal-title">This is how<br><span>you work with AI.</span></h1><div class="mx-reveal-enhancement__sub">Your assessment is more than a score. It is a picture of where your natural strengths are already working — and where one smart move can change the trajectory.</div><div class="mx-reveal-enhancement__score">Overall AI Mastery · <strong data-reveal-score>0</strong> / 100</div><div class="mx-reveal-enhancement__scroll">Your pattern is waiting below<span></span></div></div>`;
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
    next.innerHTML=`<div class="mx-next-move__inner"><div class="mx-kicker"><i></i> Your growth path</div><h2 id="mx-next-move-title" class="mx-next-move__heading">Don't wonder what to do next.<br><span>Here's your move.</span></h2><p class="mx-next-move__lead">You don't need to improve everything at once. Pick the next move that creates the most leverage, practice it on something real, and let the results teach you what comes next.</p><div class="mx-next-move__grid">${cards||'<article class="mx-next-move__card"><div class="mx-next-move__number">NEXT MOVE</div><div class="mx-next-move__icon">→</div><div class="mx-next-move__name">Start with one real task</div><div class="mx-next-move__step">Bring one meaningful task to Naya and use it as your first practice arena.</div><div class="mx-next-move__tag">One clear next move</div></article>'}</div><div class="mx-naya-bridge"><div class="mx-naya-bridge__copy"><strong>Your results don't end here.</strong><span>Naya can start with this profile instead of making you explain yourself all over again.</span></div><button class="mx-button" type="button" data-continue-naya><span class="mx-button-icon">→</span><span class="mx-button-copy"><span class="mx-button-title">Continue with Naya</span><span class="mx-button-sub">Carry my MAXESS profile forward</span></span></button></div></div>`;
    if(mountPoint) mountPoint.before(next); else tower.appendChild(next);

    const handoff=next.querySelector('[data-continue-naya]');
    handoff.addEventListener('click',()=>{
      const payload={source:'MAXESS',version:1,result,timestamp:new Date().toISOString()};
      try{localStorage.setItem('MAXESS_NAYA_CONTEXT',JSON.stringify(payload));sessionStorage.setItem('MAXESS_NAYA_CONTEXT',JSON.stringify(payload));}catch(e){}
      window.dispatchEvent(new CustomEvent('maxess:naya-context',{detail:payload}));
      const encoded=encodeContext(result);
      const target=document.querySelector('[data-naya-chat],#naya-chat,#naya')||mountPoint;
      if(target){target.scrollIntoView({behavior:'smooth',block:'start'});}
      const candidates=['window.Naya','window.naya','window.openNaya','window.startNayaChat'];
      try{if(typeof window.openNaya==='function') window.openNaya(payload); else if(typeof window.startNayaChat==='function') window.startNayaChat(payload); else if(typeof window.Naya?.open==='function') window.Naya.open(payload);}catch(e){}
      handoff.setAttribute('aria-label','MAXESS profile saved. Continue with Naya below.');
      if(encoded) handoff.dataset.contextReady='1';
    });
  }
  if(document.readyState==='loading') document.addEventListener('DOMContentLoaded',mount,{once:true}); else mount();
})();
