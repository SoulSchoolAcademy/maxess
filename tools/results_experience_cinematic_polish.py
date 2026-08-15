from pathlib import Path

p = Path('code')
s = p.read_text(encoding='utf-8')
MARKER = 'MAXESS RESULTS EXPERIENCE CINEMATIC POLISH'
if MARKER in s:
    print('Cinematic polish already present')
    raise SystemExit(0)

CSS = r'''
/* =========================================================
   MAXESS RESULTS EXPERIENCE CINEMATIC POLISH
   Less UI. More story. Make the score feel like an arrival.
========================================================= */
.maxess-clean-results{max-width:1160px;padding-left:clamp(16px,3vw,34px);padding-right:clamp(16px,3vw,34px)}
.maxess-clean-results .cr-section{margin-top:86px}

/* SCORE ARRIVAL — visual, not a lonely number */
.cr-thermometer{display:none!important}
.cr-speedometer{position:relative;margin:34px auto 0;max-width:760px;padding:8px 0 0;text-align:center}
.cr-speedometer svg{display:block;width:100%;height:auto;overflow:visible}
.cr-speedometer .arc-bg{fill:none;stroke:rgba(255,255,255,.08);stroke-width:18;stroke-linecap:round}
.cr-speedometer .arc-fg{fill:none;stroke:url(#crSpeedGradient);stroke-width:18;stroke-linecap:round;filter:drop-shadow(0 0 12px rgba(138,92,255,.42))}
.cr-speedometer .tick{stroke:rgba(255,255,255,.16);stroke-width:2}
.cr-speedometer .tick.major{stroke:rgba(184,149,255,.38);stroke-width:3}
.cr-speedometer .needle{stroke:#fff;stroke-width:5;stroke-linecap:round;filter:drop-shadow(0 0 9px rgba(255,255,255,.5))}
.cr-speedometer .hub{fill:#0a0710;stroke:#d8cbff;stroke-width:2;filter:drop-shadow(0 0 14px rgba(138,92,255,.55))}
.cr-speedometer .score{font-size:76px;font-weight:1000;fill:#fff;letter-spacing:-.06em}
.cr-speedometer .label{font-size:10px;font-weight:950;letter-spacing:.18em;fill:#aaa3b2}
.cr-speedometer .band{font-size:12px;font-weight:900;fill:#d5cde2}
.cr-speedometer .caption{max-width:620px;margin:4px auto 0;color:#aaa4b2;font-size:14px;line-height:1.55}

/* Editorial opening — no panel, no tiny text soup */
.cr-analysis{margin-top:58px;padding:18px 0 0;border-top:1px solid rgba(184,149,255,.12)}
.cr-analysis h2{max-width:920px;margin:8px 0 0;font-size:clamp(34px,5.2vw,60px);line-height:.98;letter-spacing:-.045em}
.cr-analysis-lead{max-width:850px;margin-top:18px;color:#ddd7e4;font-size:clamp(17px,2.1vw,20px);line-height:1.55}
.cr-analysis-points{gap:14px;margin-top:24px}.cr-analysis-point{padding:0 0 8px;border-bottom:1px solid rgba(184,149,255,.18);color:#c7c0cf;font-size:12px}.cr-analysis-point b{color:#b895ff}

.cr-how-ai{margin-top:72px;padding-top:10px;border-top:1px solid rgba(184,149,255,.10)}
.cr-how-ai h3{max-width:920px;margin:8px 0 0;font-size:clamp(30px,4.5vw,48px);line-height:1.02;letter-spacing:-.04em}
.cr-how-ai>p{max-width:820px;margin:14px 0 0;color:#b7b0bd;font-size:15px;line-height:1.68}
.cr-how-ai .ai-pillars{display:flex;flex-wrap:wrap;gap:10px;margin-top:22px}
.cr-how-ai .ai-pillars span{position:relative;color:#eee9f3;font-size:13px;font-weight:900}
.cr-how-ai .ai-pillars span:not(:last-child)::after{content:'→';margin-left:10px;color:#7e7489}

/* Signature: more art, less dashboard */
.cr-signature{margin-top:78px;padding-top:8px}.cr-signature-head{display:block}.cr-signature-head .cr-copy{max-width:760px}
.cr-signature-visual{margin:30px auto 0;max-width:800px}
.cr-signature-visual svg{filter:drop-shadow(0 18px 40px rgba(0,0,0,.28))}
.cr-dimension-story{margin-top:34px;grid-template-columns:1fr 1fr;gap:42px}
.cr-story{border:0!important;padding:0!important;background:transparent!important;box-shadow:none!important}
.cr-story-kicker{color:#888091}.cr-story h3{font-size:clamp(28px,3.8vw,40px)}
.cr-story p{font-size:15px;line-height:1.68;max-width:540px}
.cr-story-adv{border-left:0!important;padding-left:0!important}.cr-story-adv::before,.cr-story-opp::before{content:'';display:block;width:34px;height:3px;border-radius:999px;margin-bottom:16px;background:#35e39b;box-shadow:0 0 18px rgba(53,227,155,.26)}
.cr-story-opp::before{background:#8a5cff;box-shadow:0 0 18px rgba(138,92,255,.28)}

/* Seven AI processes: one elegant constellation, not seven cards */
.cr-processes{margin-top:82px;padding:42px 0 18px;border-top:1px solid rgba(184,149,255,.10)}
.cr-processes h3{margin:8px 0 0;font-size:clamp(28px,4vw,44px);line-height:1.02;letter-spacing:-.035em}
.cr-process-line{position:relative;margin-top:34px;display:flex;align-items:center;gap:0;overflow:auto;padding:8px 0 16px;scrollbar-width:thin}
.cr-process-line::before{content:'';position:absolute;left:18px;right:18px;top:31px;height:2px;background:linear-gradient(90deg,rgba(138,92,255,.15),rgba(184,149,255,.55),rgba(138,92,255,.15));box-shadow:0 0 18px rgba(138,92,255,.10)}
.cr-process-step{position:relative;z-index:1;min-width:124px;display:flex;flex-direction:column;align-items:center;text-align:center}
.cr-process-step .gem{width:52px;height:52px;border-radius:18px;display:grid;place-items:center;color:#fff;font-size:15px;font-weight:1000;border:1px solid rgba(255,255,255,.58);background:radial-gradient(circle at 30% 18%,#fff 0,#dfd4ff 12%,#8a5cff 42%,#0b0711 100%);box-shadow:inset 0 2px 4px rgba(255,255,255,.72),0 0 24px rgba(138,92,255,.18),0 8px 16px rgba(0,0,0,.42)}
.cr-process-step:nth-child(2) .gem{background:radial-gradient(circle at 30% 18%,#fff 0,#dfd4ff 12%,#3ca8ff 42%,#06101a 100%)}
.cr-process-step:nth-child(3) .gem{background:radial-gradient(circle at 30% 18%,#fff 0,#dfd4ff 12%,#35e39b 42%,#06110b 100%)}
.cr-process-step:nth-child(4) .gem{background:radial-gradient(circle at 30% 18%,#fff 0,#dfd4ff 12%,#765cff 42%,#0a0710 100%)}
.cr-process-step:nth-child(5) .gem{background:radial-gradient(circle at 30% 18%,#fff 0,#dfd4ff 12%,#b895ff 42%,#0a0710 100%)}
.cr-process-step:nth-child(6) .gem{background:radial-gradient(circle at 30% 18%,#fff 0,#dfd4ff 12%,#8a5cff 42%,#0a0710 100%)}
.cr-process-step:nth-child(7) .gem{background:radial-gradient(circle at 30% 18%,#fff 0,#dfd4ff 12%,#ed42c4 42%,#12050f 100%)}
.cr-process-step strong{margin-top:12px;color:#fff;font-size:12px;letter-spacing:.02em}.cr-process-step span{margin-top:5px;color:#8f8798;font-size:10px}

/* Naya should feel like a branded guide, not another card */
.cr-naya{margin-top:82px;padding:34px 0;border-top:1px solid rgba(184,149,255,.10);border-bottom:1px solid rgba(184,149,255,.10);background:radial-gradient(circle at 5% 50%,rgba(138,92,255,.09),transparent 30%)}
.cr-naya-orb{width:92px;height:92px;box-shadow:inset 0 2px 5px rgba(255,255,255,.76),0 0 38px rgba(116,76,255,.38),0 12px 22px rgba(0,0,0,.45)}
.cr-naya-name{font-size:10px;color:#b895ff}.cr-naya h3{font-size:clamp(28px,4vw,40px)}.cr-naya p{font-size:15px;max-width:780px}

/* Doors: beautiful visual destinations, not card soup */
.cr-doors{margin-top:82px}.cr-doorline{gap:14px}.cr-door{min-width:220px;padding:18px 18px 18px;border:0;border-top:1px solid rgba(184,149,255,.20);border-radius:0;background:transparent;box-shadow:none}.cr-door:hover{background:rgba(255,255,255,.012)}
.cr-door strong{font-size:15px}.cr-door p{font-size:11px}.cr-gem{width:54px;height:54px;border-radius:18px}

.cr-next{margin-top:88px;padding:64px 0 22px;border-top:1px solid rgba(184,149,255,.12)}
.cr-next h2{font-size:clamp(34px,5.4vw,60px)}.cr-next p{font-size:15px}

.cr-cinematic-mounted .cr-legacy-hidden{display:none!important}

@media(max-width:760px){
 .cr-analysis h2,.cr-how-ai h3{font-size:32px}.cr-analysis-lead{font-size:16px}.cr-dimension-story{grid-template-columns:1fr;gap:30px}.cr-process-step{min-width:108px}.cr-process-line::before{left:12px;right:12px}.cr-naya{grid-template-columns:74px 1fr}.cr-naya-orb{width:70px;height:70px}.cr-door{min-width:200px}
}
'''

if '</style>' not in s:
    raise RuntimeError('style closing tag missing')
s = s.replace('</style>', CSS + '\n</style>', 1)

JS = r'''
(function(){
  const root=document.getElementById('resultsView');
  if(!root) return;
  const mount=()=>{
    if(!root.classList.contains('visible')) return;
    const shell=root.querySelector('.maxess-clean-results');
    if(!shell || shell.dataset.crPolish==='1') return;
    const score=Math.round(Number(document.getElementById('overallScore')?.textContent||0));
    const scoreBand=(score>=90?'EXCEPTIONAL AI CAPABILITY':score>=75?'STRONG AI CAPABILITY':score>=60?'DEVELOPING AI CAPABILITY':'EMERGING AI CAPABILITY');

    const meter=shell.querySelector('.cr-thermometer');
    if(meter){
      const speed=document.createElement('div');
      speed.className='cr-speedometer';
      const pct=Math.max(0,Math.min(100,score));
      const cx=300,cy=270,r=190,start=-Math.PI*0.82,end=Math.PI*0.82;
      const point=(a,rr)=>`${cx+Math.cos(a)*rr},${cy+Math.sin(a)*rr}`;
      const p0=point(start,r),p1=point(end,r);
      const large=end-start>Math.PI?'1':'0';
      const endAngle=start+(end-start)*(pct/100);
      const pf=point(endAngle,r);
      const fg=pct<=0?'':`M ${p0} A ${r} ${r} 0 ${large} 1 ${pf}`;
      let ticks='';
      for(let i=0;i<=10;i++){
        const a=start+(end-start)*(i/10); const ri=r-18,ro=r-2; const cls=i%2===0?'tick major':'tick';
        ticks += `<line class="${cls}" x1="${cx+Math.cos(a)*ri}" y1="${cy+Math.sin(a)*ri}" x2="${cx+Math.cos(a)*ro}" y2="${cy+Math.sin(a)*ro}"/>`;
      }
      const needle=point(start+(end-start)*(pct/100),132);
      speed.innerHTML=`<svg viewBox="0 0 600 360" role="img" aria-label="MAXESS score ${pct} out of 100"><defs><linearGradient id="crSpeedGradient" x1="0" x2="1"><stop offset="0" stop-color="#5424b5"/><stop offset=".55" stop-color="#8a5cff"/><stop offset="1" stop-color="#b895ff"/></linearGradient></defs><path class="arc-bg" d="M ${p0} A ${r} ${r} 0 ${large} 1 ${p1}"/><path class="arc-fg" d="${fg}"/><g>${ticks}</g><line class="needle" x1="${cx}" y1="${cy}" x2="${needle.split(',')[0]}" y2="${needle.split(',')[1]}"/><circle class="hub" cx="${cx}" cy="${cy}" r="18"/><text class="score" x="${cx}" y="${cy-2}" text-anchor="middle">${pct}</text><text class="label" x="${cx}" y="${cy+28}" text-anchor="middle">YOUR MAXESS SCORE</text><text class="band" x="${cx}" y="${cy+54}" text-anchor="middle">${scoreBand}</text></svg><p class="caption">A snapshot of how effectively you currently direct, evaluate, refine, and apply AI.</p>`;
      meter.replaceWith(speed);
    }

    const analysis=shell.querySelector('.cr-analysis');
    if(analysis && !shell.querySelector('.cr-how-ai')){
      const strongest=analysis.querySelector('.cr-analysis-point')?.textContent?.trim()||'Your strongest capability';
      const how=document.createElement('section');
      how.className='cr-how-ai';
      how.innerHTML=`<div class="cr-kicker">HOW YOU WORK WITH AI</div><h3>AI is the engine. You are the director.</h3><p>Your results are most useful when they change how you work. Know what you want. Tell AI what matters. Ask clearly. Look closely. Score the result. Improve it. Repeat.</p><div class="ai-pillars"><span>KNOW</span><span>TELL</span><span>ASK</span><span>LOOK</span><span>SCORE</span><span>IMPROVE</span><span>REPEAT</span></div>`;
      analysis.insertAdjacentElement('afterend',how);
    }

    if(!shell.querySelector('.cr-processes')){
      const master=shell.querySelector('.cr-masterkey');
      const anchor=master || shell.querySelector('.cr-signature');
      if(anchor){
        const processes=document.createElement('section');
        processes.className='cr-processes';
        processes.innerHTML=`<div class="cr-kicker">THE 7 AI PROCESSES</div><h3>A simple rhythm for making better work with AI.</h3><div class="cr-process-line">${[['KNOW','Define the destination'],['TELL','Give useful context'],['ASK','Shape the request'],['LOOK','Inspect the result'],['SCORE','Judge the quality'],['IMPROVE','Refine deliberately'],['REPEAT','Build the habit']].map(x=>`<div class="cr-process-step"><div class="gem">✦</div><strong>${x[0]}</strong><span>${x[1]}</span></div>`).join('')}</div>`;
        anchor.insertAdjacentElement('beforebegin',processes);
      }
    }

    shell.classList.add('cr-cinematic-mounted');
    shell.dataset.crPolish='1';
  };
  const observer=new MutationObserver(mount);
  observer.observe(root,{attributes:true,childList:true,subtree:true,attributeFilter:['class']});
  mount();
})();
'''

idx=s.lower().rfind('</script>')
if idx<0:
    raise RuntimeError('script closing tag missing')
s=s[:idx]+JS+s[idx:]
s=s.replace('</head>', '\n<!-- '+MARKER+' -->\n</head>', 1)
p.write_text(s,encoding='utf-8')
print('Cinematic polish applied')
