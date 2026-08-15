/*
 MAXESS RESULTS — AAA EXPERIENCE ENHANCER
 Oscar pass: personalization, revelation, accessibility, motion, and final
 NayaNET handoff. This layer is deliberately data-driven and never invents
 assessment facts. It consumes window.MAXESS_RESULT created by the bridge.
*/
(function(){
  'use strict';

  const NS='maxess-aaa';
  const $=(s,r=document)=>r.querySelector(s);
  const $$=(s,r=document)=>Array.from(r.querySelectorAll(s));
  const clamp=(n,min=0,max=100)=>Math.max(min,Math.min(max,Number(n)||0));
  const esc=(v)=>String(v??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
  const result=window.MAXESS_RESULT||{};
  const dims=Array.isArray(result.dimensions)?result.dimensions.map((d,i)=>({id:d.id||`dimension-${i+1}`,name:d.name||`Dimension ${i+1}`,score:clamp(d.score),description:d.description||''})):[];
  const overall=clamp(result.overallScore);
  const strengths=Array.isArray(result.strengths)?result.strengths:[];
  const opportunities=Array.isArray(result.opportunities)?result.opportunities:[];

  const byScore=[...dims].sort((a,b)=>b.score-a.score);
  const strongest=byScore[0]||strengths[0]||{name:'Your strongest dimension',score:overall};
  const weakest=[...dims].sort((a,b)=>a.score-b.score)[0]||opportunities[0]||{name:'Your growth opportunity',score:overall};
  const gap=Math.max(0,Math.round((strongest.score||0)-(weakest.score||0)));

  function tier(score){
    if(score>=90)return 'Exceptional';
    if(score>=75)return 'Advanced';
    if(score>=60)return 'Developing';
    if(score>=40)return 'Emerging';
    return 'Foundational';
  }

  function dimensionMeaning(name,score){
    const n=String(name).toLowerCase();
    const t=tier(score);
    const map={
      direction:{high:'You are increasingly able to give AI a clear destination instead of simply asking it for answers.',low:'Your next lift is learning to define the outcome, constraints, audience, and success criteria before asking AI to produce.',mid:'You have the beginnings of clear direction; making the desired outcome explicit will increase the quality of almost everything that follows.'},
      communication:{high:'You can translate what you mean into instructions AI can act on with much less ambiguity.',low:'Your next lift is making context, audience, tone, examples, and constraints explicit.',mid:'Your communication foundation is working; adding context and examples will make your instructions much more reliable.'},
      evaluation:{high:'You naturally judge AI output instead of accepting the first answer. That is one of the most valuable human skills in AI.',low:'Your next lift is learning to score outputs against a clear standard before deciding they are good enough.',mid:'You are beginning to evaluate output critically; a repeatable scorecard will turn that instinct into a system.'},
      iteration:{high:'You understand that strong AI work is built through refinement rather than one perfect prompt.',low:'Your next lift is adopting a deliberate create → score → improve loop.',mid:'You already refine some work; making iteration systematic will increase consistency.'},
      systems:{high:'You see AI as part of a repeatable workflow rather than an isolated chat.',low:'Your next lift is connecting prompts, tools, people, information, and repeatable steps into a system.',mid:'You are starting to think in workflows; documenting the repeatable parts will create leverage.'}
    };
    const key=Object.keys(map).find(k=>n.includes(k));
    if(!key)return `${t} capability in ${esc(name)}. Your next step is to turn this capability into a repeatable advantage.`;
    if(score>=75)return map[key].high;
    if(score<50)return map[key].low;
    return map[key].mid;
  }

  function pathwayFor(name){
    const n=String(name).toLowerCase();
    if(n.includes('direction'))return ['Define outcomes','Add constraints','Create success criteria'];
    if(n.includes('communication'))return ['Add context','Specify audience','Give examples'];
    if(n.includes('evaluation'))return ['Create scorecards','Compare alternatives','Refine deliberately'];
    if(n.includes('iteration'))return ['Create a first version','Score it','Improve and repeat'];
    if(n.includes('systems'))return ['Map the workflow','Automate repeatable steps','Measure the result'];
    return ['Understand the pattern','Practice deliberately','Build a repeatable workflow'];
  }

  function addStyles(){
    if($('#'+NS+'-styles'))return;
    const s=document.createElement('style');
    s.id=NS+'-styles';
    s.textContent=`
      .${NS}-section{padding:clamp(72px,9vw,132px) 0;position:relative}
      .${NS}-section:before{content:"";position:absolute;left:50%;top:0;width:min(900px,100%);height:1px;transform:translateX(-50%);background:linear-gradient(90deg,transparent,rgba(205,153,255,.28),transparent)}
      .${NS}-head{max-width:820px;margin:0 auto 40px;text-align:center}
      .${NS}-head h2{font-size:clamp(38px,5.2vw,72px);line-height:.96;letter-spacing:-.058em;margin:12px 0}
      .${NS}-head p{max-width:720px;margin:16px auto 0;color:rgba(255,255,255,.64);font-size:17px;line-height:1.65}
      .${NS}-insight{position:relative;overflow:hidden;border:1px solid rgba(201,145,255,.28);border-radius:34px;padding:clamp(30px,6vw,78px);background:radial-gradient(circle at 50% 0,rgba(167,80,255,.20),transparent 60%),linear-gradient(145deg,rgba(255,255,255,.055),rgba(255,255,255,.012));box-shadow:0 30px 100px rgba(0,0,0,.46)}
      .${NS}-insight:after{content:"";position:absolute;inset:auto -10% -55%;height:75%;background:radial-gradient(ellipse,rgba(169,92,255,.15),transparent 68%);filter:blur(20px);pointer-events:none}
      .${NS}-quote{position:relative;z-index:1;font-size:clamp(28px,4.6vw,64px);line-height:1.02;letter-spacing:-.052em;max-width:1080px}
      .${NS}-quote em{font-style:normal;color:#d4a2ff}
      .${NS}-proof{position:relative;z-index:1;display:grid;grid-template-columns:repeat(3,1fr);gap:10px;margin-top:34px}
      .${NS}-proof-card{padding:19px;border-radius:18px;border:1px solid rgba(255,255,255,.08);background:rgba(0,0,0,.23)}
      .${NS}-proof-card small{display:block;color:rgba(255,255,255,.45);text-transform:uppercase;letter-spacing:.14em;font-weight:800;font-size:9px}
      .${NS}-proof-card strong{display:block;margin-top:8px;font-size:17px}
      .${NS}-proof-card p{margin-top:6px;color:rgba(255,255,255,.58);font-size:12px;line-height:1.45}
      .${NS}-path{display:grid;grid-template-columns:1fr .8fr;gap:18px;align-items:stretch}
      .${NS}-path-main,.${NS}-path-side{border:1px solid rgba(255,255,255,.10);border-radius:28px;background:linear-gradient(145deg,rgba(255,255,255,.055),rgba(255,255,255,.014));padding:clamp(25px,4vw,42px)}
      .${NS}-path-main h3{font-size:clamp(31px,4vw,54px);line-height:.98;letter-spacing:-.05em;margin:10px 0 20px}
      .${NS}-steps{display:grid;gap:10px}
      .${NS}-step{display:grid;grid-template-columns:38px 1fr;gap:13px;align-items:center;padding:14px;border:1px solid rgba(255,255,255,.07);border-radius:16px;background:rgba(0,0,0,.18)}
      .${NS}-step b{width:38px;height:38px;display:grid;place-items:center;border-radius:50%;background:linear-gradient(145deg,#e6c8ff,#762bd4);color:#fff;font-size:13px;box-shadow:0 0 22px rgba(169,92,255,.28)}
      .${NS}-step strong{font-size:14px}.${NS}-step span{display:block;margin-top:3px;color:rgba(255,255,255,.48);font-size:12px}
      .${NS}-path-side .kicker{font-size:9px;letter-spacing:.16em;text-transform:uppercase;color:#d4a2ff;font-weight:900}
      .${NS}-path-side h4{font-size:29px;line-height:1;margin:10px 0}.${NS}-path-side p{color:rgba(255,255,255,.62);line-height:1.6;font-size:14px}
      .${NS}-matrix{display:grid;grid-template-columns:repeat(3,1fr);gap:12px}
      .${NS}-matrix-card{padding:24px;border:1px solid rgba(255,255,255,.09);border-radius:22px;background:rgba(255,255,255,.025)}
      .${NS}-matrix-card .num{font-size:10px;letter-spacing:.14em;color:#d4a2ff;font-weight:900}.${NS}-matrix-card h3{font-size:22px;margin:11px 0 8px}.${NS}-matrix-card p{font-size:13px;line-height:1.55;color:rgba(255,255,255,.57)}
      .${NS}-transition{text-align:center;padding:clamp(55px,8vw,100px) 0 20px}.${NS}-transition h2{font-size:clamp(42px,6vw,82px);line-height:.92;letter-spacing:-.06em;margin:12px 0}.${NS}-transition p{max-width:700px;margin:auto;color:rgba(255,255,255,.62);font-size:17px;line-height:1.65}
      .${NS}-progress{position:fixed;top:0;left:0;height:2px;width:0;background:linear-gradient(90deg,#7c2be0,#f0d5ff,#8d43ff);z-index:1000;box-shadow:0 0 12px rgba(180,100,255,.65);pointer-events:none}
      @media(max-width:820px){.${NS}-proof,.${NS}-path,.${NS}-matrix{grid-template-columns:1fr}.${NS}-proof-card{min-height:0}}
      @media(prefers-reduced-motion:reduce){.${NS}-insight,.${NS}-section{scroll-margin-top:30px}}
    `;
    document.head.appendChild(s);
  }

  function buildInsight(){
    const section=document.createElement('section');
    section.className=NS+'-section reveal';
    section.id='maxessPersonalInsight';
    section.innerHTML=`<div class="wrap"><div class="${NS}-head"><div class="eyebrow">05 · YOUR DISCOVERY</div><h2>The pattern underneath your score.</h2><p>This is where numbers become useful: they show the way your capabilities work together.</p></div><article class="${NS}-insight"><div class="${NS}-quote">Your strongest signal is <em>${esc(strongest.name)}</em>. Your biggest growth opportunity is <em>${esc(weakest.name)}</em>. The ${gap}-point gap is where your next meaningful lift can begin.</div><div class="${NS}-proof"><div class="${NS}-proof-card"><small>Strongest signal</small><strong>${esc(strongest.name)} · ${Math.round(strongest.score)}/100</strong><p>${esc(dimensionMeaning(strongest.name,strongest.score))}</p></div><div class="${NS}-proof-card"><small>Growth signal</small><strong>${esc(weakest.name)} · ${Math.round(weakest.score)}/100</strong><p>${esc(dimensionMeaning(weakest.name,weakest.score))}</p></div><div class="${NS}-proof-card"><small>Overall pattern</small><strong>${Math.round(overall)}/100 · ${tier(overall)}</strong><p>Your score is a starting point for deliberate practice, not a label for who you are.</p></div></div></article></div></section>`;
    return section;
  }

  function buildPath(){
    const steps=pathwayFor(weakest.name);
    const section=document.createElement('section');
    section.className=NS+'-section reveal';
    section.id='maxessMasteryPath';
    section.innerHTML=`<div class="wrap"><div class="${NS}-head"><div class="eyebrow">06 · YOUR NEXT LEVEL</div><h2>Don't just know your score. Use it.</h2><p>MAXESS turns your result into a practical path. Start with the capability that can create the most leverage.</p></div><div class="${NS}-path"><article class="${NS}-path-main"><div class="eyebrow">YOUR FIRST PATH</div><h3>Strengthen ${esc(weakest.name)}.</h3><div class="${NS}-steps">${steps.map((s,i)=>`<div class="${NS}-step"><b>${i+1}</b><div><strong>${esc(s)}</strong><span>${esc(i===0?'Understand the skill in a real AI task.':i===1?'Practice it with a repeatable method.':'Make it part of a workflow you can reuse.')}</span></div></div>`).join('')}</div></article><aside class="${NS}-path-side"><div class="kicker">Why this path</div><h4>${esc(weakest.name)} is your highest-leverage next move.</h4><p>${esc(dimensionMeaning(weakest.name,weakest.score))}</p><div style="margin-top:22px;padding:15px;border:1px solid rgba(255,255,255,.08);border-radius:15px;background:rgba(0,0,0,.2)"><small style="color:rgba(255,255,255,.45);text-transform:uppercase;letter-spacing:.13em">Current signal</small><strong style="display:block;font-size:38px;letter-spacing:-.06em;margin-top:5px">${Math.round(weakest.score)}<span style="font-size:15px;color:rgba(255,255,255,.4)">/100</span></strong></div></aside></div></div></section>`;
    return section;
  }

  function buildDimensionCoaching(){
    const chosen=dims.length?dims.slice().sort((a,b)=>b.score-a.score).slice(0,3):[];
    if(!chosen.length)return null;
    const section=document.createElement('section');
    section.className=NS+'-section reveal';
    section.id='maxessDimensionCoaching';
    section.innerHTML=`<div class="wrap"><div class="${NS}-head"><div class="eyebrow">07 · YOUR CAPABILITY STACK</div><h2>Three places to put your attention.</h2><p>Use your strongest capability as an advantage while deliberately strengthening the capabilities around it.</p></div><div class="${NS}-matrix">${chosen.map((d,i)=>`<article class="${NS}-matrix-card"><div class="num">0${i+1} · ${Math.round(d.score)}/100</div><h3>${esc(d.name)}</h3><p>${esc(dimensionMeaning(d.name,d.score))}</p></article>`).join('')}</div></div></section>`;
    return section;
  }

  function buildTransition(){
    const section=document.createElement('section');
    section.className=NS+'-transition reveal';
    section.id='maxessNayaTransition';
    section.innerHTML=`<div class="wrap"><div class="eyebrow">NEXT · YOUR AI PARTNER</div><h2>Now let Naya help you use it.</h2><p>Your result tells you where you are. The next experience is about turning that awareness into action.</p></div>`;
    return section;
  }

  function insertBeforeNaya(){
    const naya=$('.naya-end')||$('.naya-section')||$('#nayaEnd');
    if(!naya||$('#maxessPersonalInsight'))return false;
    const frag=document.createDocumentFragment();
    frag.append(buildInsight());
    frag.append(buildPath());
    const coaching=buildDimensionCoaching(); if(coaching)frag.append(coaching);
    frag.append(buildTransition());
    naya.parentNode.insertBefore(frag,naya);
    return true;
  }

  function enhanceExistingText(){
    const identity=$('#identityCopy');
    if(identity&&overall)identity.textContent=`Your MAXESS score is ${Math.round(overall)}/100. The most useful part is not the number — it is the pattern behind it.`;
    const band=$('#band');
    if(band&&!band.textContent.trim())band.textContent=tier(overall);
    const profile=$('#profileCopy');
    if(profile&&strongest.name)profile.textContent=`Your strongest signal is ${strongest.name}. Your next leverage is in ${weakest.name}.`;
  }

  function addProgress(){
    if($('#maxessReadingProgress'))return;
    const bar=document.createElement('div');bar.id='maxessReadingProgress';bar.className=NS+'-progress';document.body.appendChild(bar);
    const update=()=>{const d=document.documentElement;const max=d.scrollHeight-innerHeight;bar.style.width=(max>0?(scrollY/max)*100:0)+'%';};
    addEventListener('scroll',update,{passive:true});addEventListener('resize',update,{passive:true});update();
  }

  function animateScore(){
    const el=$('#score');
    if(!el||!Number.isFinite(overall))return;
    const target=Math.round(overall);const reduce=matchMedia('(prefers-reduced-motion: reduce)').matches;
    if(reduce){el.textContent=target;return;}
    const start=performance.now();const duration=900;
    const tick=now=>{const p=Math.min(1,(now-start)/duration);const eased=1-Math.pow(1-p,3);el.textContent=Math.round(target*eased);if(p<1)requestAnimationFrame(tick);};
    requestAnimationFrame(tick);
  }

  function revealObserver(){
    const items=$$('.reveal:not(.is-in)');
    if(!items.length)return;
    if(!('IntersectionObserver' in window)){items.forEach(x=>x.classList.add('is-in'));return;}
    const io=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('is-in');io.unobserve(e.target);}}),{threshold:.08});
    items.forEach(x=>io.observe(x));
  }

  function validate(){
    const errors=[];
    if(!Number.isFinite(overall))errors.push('overall score');
    if(dims.length<5)errors.push('five dimensions');
    if(!$('.naya-end')&&!$('.naya-section')&&!$('#nayaEnd'))errors.push('NayaNET endpoint');
    if(errors.length)console.warn('[MAXESS AAA] Validation warnings:',errors.join(', '));
    else console.info('[MAXESS AAA] Result model validated: overall + five dimensions + NayaNET endpoint.');
  }

  function run(){
    addStyles();
    enhanceExistingText();
    if(insertBeforeNaya()){
      addProgress();
      animateScore();
      revealObserver();
    }
    validate();
    document.documentElement.dataset.maxessAaa='enhanced';
  }

  if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',()=>setTimeout(run,0));
  else setTimeout(run,0);
})();
