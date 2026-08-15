from pathlib import Path

PATH = Path('code')
s = PATH.read_text(encoding='utf-8')
MARKER = 'MAXESS RESULTS EXPERIENCE 10-STAR'
if MARKER in s:
    print('10-star refinement already present')
    raise SystemExit(0)

CSS = r'''
/* =========================================================
   MAXESS RESULTS EXPERIENCE 10-STAR
   Cinematic capability-discovery system.
   Groove-safe, deterministic, accessible, restrained.
========================================================= */
.maxess-10star-results{--m10-bg:#030306;--m10-purple:#8a5cff;--m10-purple2:#b895ff;--m10-sapphire:#4e8cff;--m10-emerald:#35e39b;--m10-gold:#d9b34b;--m10-violet:#765cff;color:#f8f7fb}
.maxess-10star-results .report-section{margin-top:78px}
.maxess-10star-results .report-heading{margin-bottom:30px}
.maxess-results-journey{display:none}
.maxess-results-reveal{max-width:860px;margin:20px auto 0;text-align:center;color:#a7a2b1;font-size:12px;letter-spacing:.08em;text-transform:uppercase}
.maxess-results-reveal::after{content:"↓";display:block;margin-top:14px;color:#9f82ff;font-size:18px;animation:maxess10Arrow 2.2s ease-in-out infinite}
@keyframes maxess10Arrow{0%,100%{transform:translateY(0);opacity:.65}50%{transform:translateY(5px);opacity:1}}
.maxess-signature-shell{margin-top:68px;padding:34px;border:1px solid rgba(184,149,255,.18);border-radius:34px;background:radial-gradient(circle at 50% 0,rgba(138,92,255,.10),transparent 48%),linear-gradient(145deg,rgba(255,255,255,.035),rgba(255,255,255,.012));box-shadow:inset 0 1px 0 rgba(255,255,255,.07),0 24px 70px rgba(0,0,0,.34)}
.maxess-signature-head{display:flex;justify-content:space-between;gap:20px;align-items:end;flex-wrap:wrap}.maxess-signature-head h3{margin:0;font-size:clamp(26px,4vw,40px);line-height:1.02;letter-spacing:-.035em}.maxess-signature-head p{margin:7px 0 0;color:#a7a2b1;max-width:660px;font-size:13px;line-height:1.55}
.maxess-signature-viz{margin:28px auto 0;max-width:760px;aspect-ratio:1.75;position:relative}.maxess-signature-viz svg{width:100%;height:100%;overflow:visible}.maxess-signature-viz .grid{fill:none;stroke:rgba(255,255,255,.08);stroke-width:1}.maxess-signature-viz .radar{fill:rgba(138,92,255,.14);stroke:#b895ff;stroke-width:2;filter:drop-shadow(0 0 14px rgba(138,92,255,.24))}.maxess-signature-viz .axis{stroke:rgba(255,255,255,.07);stroke-width:1}.maxess-signature-viz .label{fill:#aaa5b2;font-size:11px;font-weight:800;letter-spacing:.04em}.maxess-signature-viz .point{fill:#fff;stroke:#b895ff;stroke-width:2;filter:drop-shadow(0 0 8px rgba(138,92,255,.55))}
.maxess-signature-table{display:grid;grid-template-columns:repeat(5,minmax(0,1fr));gap:8px;margin-top:20px}.maxess-signature-item{padding:13px;border:1px solid rgba(255,255,255,.08);border-radius:18px;background:rgba(255,255,255,.025);text-align:center}.maxess-signature-item strong{display:block;font-size:19px;line-height:1}.maxess-signature-item span{display:block;margin-top:7px;color:#8f8998;font-size:9px;line-height:1.3;font-weight:850;letter-spacing:.08em;text-transform:uppercase}
.maxess-meaning{margin-top:18px;padding:27px 28px;border:1px solid rgba(184,149,255,.18);border-radius:28px;background:linear-gradient(145deg,rgba(138,92,255,.07),rgba(255,255,255,.018));box-shadow:inset 0 1px 0 rgba(255,255,255,.06)}
.maxess-meaning-kicker{color:#9f82ff;font-size:9px;font-weight:950;letter-spacing:.20em;text-transform:uppercase}.maxess-meaning h4{margin:9px 0 0;font-size:clamp(22px,3vw,32px);line-height:1.05;letter-spacing:-.025em}.maxess-meaning p{margin:11px 0 0;color:#c4bfca;font-size:15px;line-height:1.62}
.maxess-ohwhy{margin-top:18px;padding:32px;border:1px solid rgba(184,149,255,.24);border-radius:30px;background:radial-gradient(circle at 50% 0,rgba(118,92,255,.14),transparent 50%),linear-gradient(145deg,#0f0c17,#050507);box-shadow:0 26px 80px rgba(0,0,0,.42),0 0 50px rgba(118,92,255,.08),inset 0 1px 0 rgba(255,255,255,.08)}
.maxess-ohwhy .kicker{color:#b895ff;font-size:9px;letter-spacing:.18em;font-weight:950;text-transform:uppercase}.maxess-ohwhy blockquote{margin:14px 0 0;font-size:clamp(23px,3.4vw,36px);line-height:1.08;letter-spacing:-.035em;font-weight:900}.maxess-ohwhy p{margin:14px 0 0;color:#aaa5b2;font-size:13px;line-height:1.6}
.maxess-naya-guide{margin-top:18px;padding:25px 27px;border:1px solid rgba(184,149,255,.18);border-radius:28px;background:linear-gradient(145deg,rgba(138,92,255,.09),rgba(255,255,255,.018));display:grid;grid-template-columns:auto minmax(0,1fr);gap:16px;align-items:center;box-shadow:inset 0 1px 0 rgba(255,255,255,.07),0 16px 40px rgba(0,0,0,.26)}
.maxess-naya-guide-orb{width:58px;height:58px;border-radius:50%;background:radial-gradient(circle at 30% 20%,#fff 0%,#dfd1ff 12%,#946dff 38%,#3b1b83 70%,#09050f 100%);border:1px solid #e4d9ff;box-shadow:inset 0 2px 4px rgba(255,255,255,.76),0 0 28px rgba(116,76,255,.40),0 8px 18px rgba(0,0,0,.55);position:relative;overflow:hidden}.maxess-naya-guide-orb::after{content:"N";position:absolute;inset:0;display:grid;place-items:center;color:#fff;font-size:18px;font-weight:1000;text-shadow:0 2px 8px rgba(0,0,0,.55)}
.maxess-naya-guide h4{margin:0;color:#b895ff;font-size:9px;letter-spacing:.18em;text-transform:uppercase;font-weight:950}.maxess-naya-guide strong{display:block;margin-top:7px;font-size:17px}.maxess-naya-guide p{margin:8px 0 0;color:#b9b3c1;font-size:13px;line-height:1.55}
.maxess-masterkey-10{margin-top:26px;padding:34px;border:1px solid rgba(184,149,255,.20);border-radius:34px;background:radial-gradient(circle at 50% 0,rgba(138,92,255,.12),transparent 48%),linear-gradient(145deg,#100c18,#050507);box-shadow:0 25px 72px rgba(0,0,0,.40),inset 0 1px 0 rgba(255,255,255,.07)}
.maxess-masterkey-10 h3{margin:7px 0 0;font-size:clamp(25px,4vw,38px);line-height:1.03;letter-spacing:-.03em}.maxess-masterkey-10>p{max-width:720px;margin:11px 0 0;color:#aaa5b1;font-size:13px;line-height:1.58}.maxess-keyline{display:grid;grid-template-columns:repeat(7,minmax(0,1fr));gap:7px;margin-top:24px}.maxess-key-step{padding:13px 7px;border:1px solid rgba(255,255,255,.08);border-radius:18px;background:rgba(255,255,255,.025);text-align:center}.maxess-key-step b{font-size:11px}.maxess-key-step span{display:block;margin-top:6px;color:#8f8998;font-size:8px;line-height:1.25;letter-spacing:.08em;text-transform:uppercase;font-weight:850}
.maxess-aaa-practical{margin-top:20px;display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:9px}.maxess-aaa-item{padding:18px 16px;border:1px solid rgba(255,255,255,.08);border-radius:20px;background:rgba(255,255,255,.024)}.maxess-aaa-item strong{display:block;font-size:11px}.maxess-aaa-item p{margin:7px 0 0;color:#aaa5b2;font-size:11px;line-height:1.45}
.maxess-opportunities{margin-top:26px;padding:34px;border:1px solid rgba(184,149,255,.18);border-radius:34px;background:linear-gradient(145deg,rgba(138,92,255,.06),rgba(255,255,255,.018));box-shadow:inset 0 1px 0 rgba(255,255,255,.06)}.maxess-opportunities h3{margin:7px 0 0;font-size:clamp(24px,3.5vw,34px)}.maxess-opportunities>p{max-width:700px;margin:10px 0 0;color:#a7a2af;font-size:13px;line-height:1.55}.maxess-door-list{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:10px;margin-top:22px}.maxess-door{padding:18px;border:1px solid rgba(255,255,255,.08);border-radius:22px;background:linear-gradient(145deg,rgba(255,255,255,.035),rgba(255,255,255,.012));box-shadow:inset 0 1px 0 rgba(255,255,255,.05)}.maxess-door .jewel{width:44px;height:44px;border-radius:14px;display:grid;place-items:center;color:#fff;font-size:16px;font-weight:1000;box-shadow:inset 0 2px 4px rgba(255,255,255,.72),0 0 20px rgba(138,92,255,.16),0 6px 12px rgba(0,0,0,.45)}.maxess-door strong{display:block;margin-top:11px;font-size:14px}.maxess-door p{margin:6px 0 0;color:#9d97a5;font-size:11px;line-height:1.45}.maxess-door .why{margin-top:8px;color:#c2bbc9;font-size:10px;line-height:1.45}
.maxess-naya-masters{margin-top:28px;padding:38px 32px;border:1px solid rgba(184,149,255,.24);border-radius:36px;background:radial-gradient(circle at 50% 0,rgba(138,92,255,.15),transparent 48%),linear-gradient(145deg,#100c18,#050507);box-shadow:0 28px 85px rgba(0,0,0,.44),0 0 60px rgba(138,92,255,.08),inset 0 1px 0 rgba(255,255,255,.08)}
.maxess-naya-brandline{display:flex;align-items:center;gap:14px}.maxess-naya-brandline .mini-orb{width:48px;height:48px;border-radius:50%;background:radial-gradient(circle at 30% 20%,#fff 0,#dfd1ff 12%,#946dff 38%,#3b1b83 70%,#09050f 100%);border:1px solid #ddd1ff;box-shadow:inset 0 2px 4px rgba(255,255,255,.75),0 0 22px rgba(116,76,255,.34)}.maxess-naya-brandline .wordmark{font-size:clamp(24px,4vw,40px);font-weight:1000;letter-spacing:-.03em}.maxess-naya-brandline .sub{display:block;color:#9d97a7;font-size:10px;font-weight:850;letter-spacing:.16em;text-transform:uppercase;margin-top:4px}
.maxess-naya-masters>p{max-width:760px;margin:16px 0 0;color:#aaa4b3;font-size:13px;line-height:1.6}.maxess-master-grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px;margin-top:26px}.maxess-master-card{padding:19px;border:1px solid rgba(255,255,255,.08);border-radius:24px;background:linear-gradient(145deg,rgba(255,255,255,.045),rgba(255,255,255,.014));box-shadow:inset 0 1px 0 rgba(255,255,255,.05),0 12px 28px rgba(0,0,0,.22)}.maxess-master-card .m-jewel{width:52px;height:52px;border-radius:17px;display:grid;place-items:center;color:#fff;font-size:17px;font-weight:1000;border:1px solid rgba(255,255,255,.65);box-shadow:inset 0 2px 4px rgba(255,255,255,.72),0 0 25px rgba(138,92,255,.20),0 6px 16px rgba(0,0,0,.48)}.maxess-master-card strong{display:block;margin-top:12px;font-size:15px;line-height:1.18}.maxess-master-card span{display:block;margin-top:5px;color:#9f99a8;font-size:10px;line-height:1.4}.maxess-master-card p{margin:8px 0 0;color:#c0bac7;font-size:11px;line-height:1.48}.maxess-master-card .naya-label{display:block;margin-top:11px;color:#b895ff;font-size:9px;font-weight:950;letter-spacing:.12em;text-transform:uppercase}
.maxess-threshold{margin-top:28px;padding:36px 32px;border-radius:38px;border:1px solid rgba(184,149,255,.22);background:radial-gradient(circle at 50% 0,rgba(138,92,255,.16),transparent 50%),linear-gradient(145deg,#0d0a14,#040405);box-shadow:0 30px 90px rgba(0,0,0,.48),inset 0 1px 0 rgba(255,255,255,.08);text-align:center}.maxess-threshold .k{color:#b895ff;font-size:9px;font-weight:950;letter-spacing:.20em;text-transform:uppercase}.maxess-threshold h3{margin:10px auto 0;max-width:720px;font-size:clamp(27px,4vw,44px);line-height:1.03;letter-spacing:-.035em}.maxess-threshold p{max-width:650px;margin:13px auto 0;color:#aaa5b2;font-size:13px;line-height:1.58}.maxess-threshold .actions{display:flex;justify-content:center;gap:10px;flex-wrap:wrap;margin-top:24px}.maxess-threshold button{min-height:56px;min-width:205px;padding:0 22px;border-radius:18px;border:1px solid rgba(184,149,255,.55);font-weight:950;cursor:pointer}.maxess-threshold .primary{background:linear-gradient(180deg,#b895ff,#765cff);color:#09060e;box-shadow:0 16px 36px rgba(138,92,255,.20),0 0 28px rgba(138,92,255,.12)}.maxess-threshold .secondary{background:#08080b;color:#fff;border-color:rgba(255,255,255,.16)}
.maxess-results-flow{padding-bottom:10px}.maxess-results-flow .legacy-hide{display:none!important}
@media(max-width:760px){.maxess-results-flow .report-section{margin-top:56px}.maxess-signature-shell,.maxess-ohwhy,.maxess-masterkey-10,.maxess-opportunities,.maxess-naya-masters,.maxess-threshold{padding:25px 18px;border-radius:28px}.maxess-signature-table{grid-template-columns:1fr 1fr}.maxess-signature-item:last-child{grid-column:1/-1}.maxess-keyline{grid-template-columns:repeat(4,1fr)}.maxess-key-step:last-child{grid-column:1/-1}.maxess-aaa-practical,.maxess-door-list,.maxess-master-grid{grid-template-columns:1fr}.maxess-naya-guide{grid-template-columns:1fr}.maxess-naya-guide-orb{width:48px;height:48px}.maxess-results-reveal{font-size:9px}.maxess-signature-shell{margin-top:52px}}
@media(prefers-reduced-motion:reduce){.maxess-results-reveal::after{animation:none}}
'''

JS = r'''

/* =========================================================
   MAXESS RESULTS EXPERIENCE 10-STAR — RUNTIME
========================================================= */
(function(){
  'use strict';
  const ROOT='maxess-10star-results';
  const IMG_A='https://i.postimg.cc/LsKxt1sz/Naya-and-Shawn-ok-35.png';
  const IMG_B='https://i.postimg.cc/d1nncN9F/Naya-and-shawn-ok-44-a.png';
  const scoreColor=(n)=>n>=90?'#d9b34b':n>=75?'#35e39b':n>=60?'#4e8cff':'#765cff';
  const escape=(v)=>String(v).replace(/[&<>"']/g,m=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#039;'}[m]));
  const iconSet=[['◆','#8a5cff'],['✦','#4e8cff'],['◇','#35e39b'],['✧','#765cff'],['✦','#b895ff']];
  const insights={
    direction:{lead:'When the destination becomes clearer, AI has less room to guess.',why:'Your pattern suggests that sharper definition of the desired outcome could make your existing AI capability more consistent.'},
    communication:{lead:'The quality of the conversation shapes the quality of the result.',why:'Your opportunity appears to be giving AI richer context, audience, constraints, and intent so you spend less time correcting misunderstandings.'},
    evaluation:{lead:'You may not need better AI answers. You may need a better way to judge the answers you are already getting.',why:'Your pattern points toward strengthening the quality filter: what is correct, useful, complete, clear, and genuinely worth keeping.'},
    iteration:{lead:'The first answer does not have to be the final answer.',why:'Your pattern suggests that deliberate refinement could unlock more value from the AI output you already receive.'},
    systems:{lead:'A good AI result becomes much more valuable when you can repeat it.',why:'Your opportunity appears to be turning successful experiments into reusable workflows, standards, and capability.'}
  };
  const masters={
    writing:['Naya Master Writer','Writing & Communication','Words, tone, structure, persuasion and clarity.'],
    research:['Naya Master Researcher','Research & Information','Finding, comparing, synthesizing and explaining information.'],
    brainstorming:['Naya Master Idea Architect','Brainstorming & Ideas','Possibilities, concepts, angles and creative directions.'],
    content:['Naya Master Content Creator','Content Creation','Turning ideas into compelling, repeatable content.'],
    business:['Naya Master Strategist','Business & Strategy','Decisions, models, opportunities and growth.'],
    marketing:['Naya Master Growth Strategist','Marketing & Sales','Offers, positioning, campaigns and customer journeys.'],
    learning:['Naya Master Learning Guide','Learning & Education','Learning faster and building better teaching experiences.'],
    coding:['Naya Master Developer','Coding & Software','Building, debugging and improving software.'],
    images:['Naya Master Visual Creator','Images & Visual Creation','Visual concepts, composition, direction and design.'],
    video:['Naya Master Media Director','Video & Media','Video concepts, storytelling and production workflows.'],
    audio:['Naya Master Voice & Audio','Audio & Voice','Voice, narration, sound and podcast workflows.'],
    data:['Naya Master Analyst','Data & Analysis','Patterns, evidence, numbers and decisions.'],
    productivity:['Naya Master Automation Architect','Productivity & Automation','Repeatable systems that save time and increase leverage.'],
    personal:['Naya Master Reflection Guide','Personal Growth & Reflection','Thinking, reflection and clearer self-direction.'],
    career:['Naya Master Career Strategist','Career & Work','Skills, opportunities and professional value.'],
    creativity:['Naya Master Creative Director','Creativity & Design','Concepts, aesthetics, invention and creative direction.'],
    agents:['Naya Master Systems Architect','AI Agents & Systems','Intelligent multi-step systems and orchestration.'],
    other:['Naya Master Explorer','Something Else','A flexible Naya specialist for the territory you define.']
  };
  function makeSvg(dimensions){
    const cx=300,cy=210,r=155,n=dimensions.length;
    const pts=(factor)=>dimensions.map((d,i)=>{const a=(-Math.PI/2)+(Math.PI*2*i/n),rr=r*factor;return `${cx+Math.cos(a)*rr},${cy+Math.sin(a)*rr}`}).join(' ');
    const radar=dimensions.map((d,i)=>{const a=(-Math.PI/2)+(Math.PI*2*i/n),rr=r*Math.max(.08,d.score/100);return `${cx+Math.cos(a)*rr},${cy+Math.sin(a)*rr}`}).join(' ');
    const labels=dimensions.map((d,i)=>{const a=(-Math.PI/2)+(Math.PI*2*i/n),lr=r+30;return `<text class="label" x="${cx+Math.cos(a)*lr}" y="${cy+Math.sin(a)*lr}" text-anchor="middle">${escape(d.name)}</text>`}).join('');
    const axes=dimensions.map((d,i)=>{const a=(-Math.PI/2)+(Math.PI*2*i/n);return `<line class="axis" x1="${cx}" y1="${cy}" x2="${cx+Math.cos(a)*r}" y2="${cy+Math.sin(a)*r}"/>`}).join('');
    const rings=[.25,.5,.75,1].map(f=>`<polygon class="grid" points="${pts(f)}"/>`).join('');
    const points=dimensions.map((d,i)=>{const a=(-Math.PI/2)+(Math.PI*2*i/n),rr=r*Math.max(.08,d.score/100);return `<circle class="point" cx="${cx+Math.cos(a)*rr}" cy="${cy+Math.sin(a)*rr}" r="5"/>`}).join('');
    return `<svg viewBox="0 0 600 420" role="img" aria-label="AI Capability Signature radar visualization">${rings}${axes}<polygon class="radar" points="${radar}"/>${points}${labels}</svg>`;
  }
  function getResults(){return window.MAXESS_RUNTIME_RESULTS||null}
  function render(){
    const root=document.getElementById('resultsView');
    if(!root || !root.classList.contains('visible') || root.dataset.maxess10star==='1') return;
    root.dataset.maxess10star='1';
    root.classList.add('maxess-10star-results','maxess-results-flow');
    root.querySelectorAll('.maxess-treasure,.results-v4-intro,.results-master-v2,.results-v4-naya,.results-v4-masterkey,.final-cta').forEach(el=>el.classList.add('legacy-hide'));
    const scoreNode=document.getElementById('overallScore');
    const overall=Number(scoreNode?.textContent||0);
    const dims=[...root.querySelectorAll('#dimensionConstellation .dimension-orb')].map((el)=>({name:el.querySelector('.dimension-name')?.textContent?.trim()||'Dimension',score:Number(el.querySelector('.dimension-score')?.textContent||0),color:el.style.getPropertyValue('--dimensionColor')||'#8a5cff'}));
    if(!dims.length) return;
    const strongest=[...dims].sort((a,b)=>b.score-a.score)[0],opportunity=[...dims].sort((a,b)=>a.score-b.score)[0];
    const oKey=Object.keys(insights).find(k=>opportunity.name.toLowerCase().includes(k))||'evaluation';
    const sig=document.createElement('div');
    sig.className='maxess-results-reveal';
    sig.textContent='EXPLORE YOUR RESULTS';
    const hero=root.querySelector('.result-hero');
    if(hero){
      const eyebrow=hero.querySelector('.result-eyebrow'); if(eyebrow) eyebrow.textContent='YOUR MAXESS RESULT';
      const title=hero.querySelector('.result-title'); if(title) title.textContent='This is what we discovered about you.';
      const sub=hero.querySelector('.result-subtitle'); if(sub) sub.textContent=`${Math.round(overall)}/100 · ${strongest.name} is currently your natural advantage.`;
      hero.appendChild(sig);
    }
    const firstInsight=root.querySelector('.insight-flow')?.closest('.report-section');
    const dimSection=root.querySelector('#dimensionConstellation')?.closest('.report-section');
    if(!firstInsight || !dimSection) return;
    const signature=document.createElement('section'); signature.className='maxess-signature-shell';
    signature.innerHTML=`<div class="maxess-signature-head"><div><div class="report-kicker">YOUR AI CAPABILITY SIGNATURE</div><h3>Your AI fingerprint.</h3><p>Five capability dimensions create a shape that is uniquely yours. The graphic gives you the pattern; the words underneath give it meaning.</p></div></div><div class="maxess-signature-viz">${makeSvg(dims)}</div><div class="maxess-signature-table">${dims.map(d=>`<div class="maxess-signature-item"><strong>${Math.round(d.score)}</strong><span>${escape(d.name)}</span></div>`).join('')}</div></section>`;
    dimSection.insertAdjacentElement('afterend',signature);
    const meaning=document.createElement('section'); meaning.className='maxess-meaning'; meaning.innerHTML=`<div class="maxess-meaning-kicker">YOUR NATURAL ADVANTAGE</div><h4>${escape(strongest.name)} is where you already have momentum.</h4><p id="m10-strength-copy">${escape(document.getElementById('strongestText')?.textContent||'Your strongest capability gives you a foundation to build from.')}</p>`;
    signature.insertAdjacentElement('afterend',meaning);
    const op=document.createElement('section'); op.className='maxess-ohwhy'; op.innerHTML=`<div class="kicker">YOUR HIGHEST-LEVERAGE OPPORTUNITY</div><blockquote>“${escape(insights[oKey].lead)}”</blockquote><p>${escape(insights[oKey].why)}</p>`;
    meaning.insertAdjacentElement('afterend',op);
    const naya=document.createElement('section'); naya.className='maxess-naya-guide'; naya.innerHTML=`<div class="maxess-naya-guide-orb" aria-hidden="true"></div><div><h4>NAYA · YOUR PERSONAL GUIDE</h4><strong>“Okay, here's the interesting part…”</strong><p>${escape(insights[oKey].why)} Your result is a starting signal, not a verdict. The next move is to practice one improvement deliberately.</p></div>`;
    op.insertAdjacentElement('afterend',naya);
    const mk=document.createElement('section'); mk.className='maxess-masterkey-10'; mk.innerHTML=`<div class="report-kicker">THE MAXESS MASTER KEY</div><h3>This is the operating system.</h3><p>KNOW what you want. TELL AI what matters. ASK clearly. LOOK at the result. SCORE the quality. IMPROVE what is weak. REPEAT what works.</p><div class="maxess-keyline">${[['KNOW','Goal'],['TELL','Context'],['ASK','Direction'],['LOOK','Result'],['SCORE','Quality'],['IMPROVE','Refine'],['REPEAT','Mastery']].map(x=>`<div class="maxess-key-step"><b>${x[0]}</b><span>${x[1]}</span></div>`).join('')}</div><div class="maxess-aaa-practical">${[['PURPOSE','Did we solve the right problem?'],['CLARITY','Can a human understand it?'],['ACCURACY','Is it actually correct?'],['USEFULNESS','Does it help?'],['REFINEMENT','Did we improve it?'],['HUMAN VALUE','Is someone genuinely better off?']].map(x=>`<div class="maxess-aaa-item"><strong>${x[0]}</strong><p>${x[1]}</p></div>`).join('')}</div></section>`;
    naya.insertAdjacentElement('afterend',mk);
    const interests=[...root.querySelectorAll('#selectedInterests .interest-pill')].map(x=>x.textContent.trim()).filter(Boolean);
    const doors=document.createElement('section'); doors.className='maxess-opportunities';
    const fallback=['Writing & Communication','Research & Information','Business & Strategy'];
    const names=(interests.length?interests:fallback).slice(0,6);
    doors.innerHTML=`<div class="report-kicker">YOUR AI OPPORTUNITIES</div><h3>There are doors here. You choose which one to open.</h3><p>${interests.length?'Based on what you told us, these are the areas most naturally connected to your interests.':'Start with a few proven areas and explore from there.'}</p><div class="maxess-door-list">${names.map((name,i)=>{const key=Object.keys(masters).find(k=>masters[k][1].toLowerCase()===name.toLowerCase())||Object.keys(masters)[i%Object.keys(masters).length]; const m=masters[key]; const ic=iconSet[i%iconSet.length]; return `<article class="maxess-door"><div class="jewel" style="background:radial-gradient(circle at 30% 20%,#fff 0,#d8d2ff 12%,${ic[1]} 44%,#0a0710 100%)">${iconSet[i%iconSet.length][0]}</div><strong>${escape(m[0])}</strong><p>${escape(m[1])}</p><div class="why">${escape(m[2])}</div></article>`}).join('')}</div></section>`;
    mk.insertAdjacentElement('afterend',doors);
    const mastersSec=document.createElement('section'); mastersSec.className='maxess-naya-masters';
    const selected=(interests.length?interests:['Writing & Communication','Research & Information','Business & Strategy','Images & Visual Creation','AI Agents & Systems','Content Creation']).slice(0,6);
    mastersSec.innerHTML=`<div class="maxess-naya-brandline"><div class="mini-orb" aria-hidden="true"></div><div><div class="wordmark">Naya</div><span class="sub">Master intelligence · specialized expertise</span></div></div><p>Naya is the brand. The Masters are specialized forms of that intelligence. Each one is a doorway into a different capability — not another app tile.</p><div class="maxess-master-grid">${selected.map((name,i)=>{const key=Object.keys(masters).find(k=>masters[k][1].toLowerCase()===name.toLowerCase())||Object.keys(masters)[i%Object.keys(masters).length];const m=masters[key];const ic=iconSet[i%iconSet.length];return `<article class="maxess-master-card"><div class="m-jewel" style="background:radial-gradient(circle at 30% 20%,#fff 0,#dcd7ff 12%,${ic[1]} 44%,#08050d 100%)">${ic[0]}</div><strong>${escape(m[0])}</strong><span>${escape(m[1])}</span><p>${escape(m[2])}</p><span class="naya-label">NAYA MASTER</span></article>`}).join('')}</div></section>`;
    doors.insertAdjacentElement('afterend',mastersSec);
    const threshold=document.createElement('section'); threshold.className='maxess-threshold'; threshold.innerHTML=`<div class="k">READY TO GO FURTHER?</div><h3>Your results show you where you are. Now let's build what comes next.</h3><p>KNOW → LEARN → APPLY → CREATE → SHARE → EARN. Capability first. Opportunity second. No hype. No guarantees. Just a clearer path from what you can do to what you can build.</p><div class="actions"><button type="button" class="primary" id="maxess10MasterAi">MASTER AI <span class="button-arrow">→</span></button><button type="button" class="secondary" id="maxess10Save">SAVE MY RESULTS</button></div></section>`;
    mastersSec.insertAdjacentElement('afterend',threshold);
    const masterBtn=document.getElementById('freeTrialButton'); if(masterBtn) threshold.querySelector('#maxess10MasterAi').addEventListener('click',()=>masterBtn.click()); else threshold.querySelector('#maxess10MasterAi').addEventListener('click',()=>window.scrollTo({top:0,behavior:'smooth'}));
    threshold.querySelector('#maxess10Save').addEventListener('click',()=>document.getElementById('pdfButton')?.click());
    // Make the assessment shell stop behaving like the height-constrained quiz when Results opens.
    document.getElementById('assessmentView')?.classList.add('maxess-results-active');
  }
  const watch=document.getElementById('resultsView');
  if(watch)new MutationObserver(render).observe(watch,{attributes:true,attributeFilter:['class']});
  render();
})();
'''

if '</style>' in s:
    s = s.replace('</style>', CSS + '\n</style>', 1)
else:
    raise RuntimeError('style closing tag missing')

if '</body>' in s:
    s = s.replace('</body>', '<script>\n' + JS + '\n</script>\n</body>', 1)
else:
    raise RuntimeError('body closing tag missing')

# Add explicit result-state class behavior to existing shell.
CSS2 = r'''
<style id="maxess-10star-shell-style">
.board-wrap:has(#resultsView.visible){display:block;min-height:auto}
.board-wrap:has(#resultsView.visible) .board{min-height:auto;overflow:visible}
.board-wrap:has(#resultsView.visible) .board-content{min-height:auto}
.maxess-results-flow{min-height:0}
</style>
'''
s = s.replace('</body>', CSS2 + '\n</body>', 1)
PATH.write_text(s, encoding='utf-8')
print('MAXESS 10-star refinement applied')
