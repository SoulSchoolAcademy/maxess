from pathlib import Path

p = Path('code')
s = p.read_text(encoding='utf-8')
MARKER = 'MAXESS RESULTS EXPERIENCE OPENING REFINEMENT'
if MARKER in s:
    print('Opening refinement already present')
    raise SystemExit(0)

CSS = r'''
/* =========================================================
   MAXESS RESULTS EXPERIENCE OPENING REFINEMENT
   Canonical opening: score -> personal analysis -> story ->
   how you work with AI. No dashboard cards.
========================================================= */
.cr-legacy-hidden{display:none!important}
.maxess-clean-results .cr-thermometer{display:none!important}
.cr-opening{padding:12px 0 0;margin-top:8px}
.cr-opening-kicker{color:#b895ff;font-size:10px;font-weight:950;letter-spacing:.20em;text-transform:uppercase}
.cr-opening-grid{display:grid;grid-template-columns:minmax(230px,.72fr) minmax(0,1.7fr);gap:46px;align-items:center;margin-top:22px}
.cr-speedometer{position:relative;max-width:300px;justify-self:center;filter:drop-shadow(0 0 28px rgba(138,92,255,.10))}
.cr-speedometer svg{display:block;width:100%;height:auto;overflow:visible}
.cr-speedometer .track{fill:none;stroke:rgba(255,255,255,.08);stroke-width:22;stroke-linecap:round}
.cr-speedometer .range{fill:none;stroke:url(#maxessSpeedGradient);stroke-width:22;stroke-linecap:round;filter:drop-shadow(0 0 10px rgba(138,92,255,.35))}
.cr-speedometer .tick{stroke:rgba(255,255,255,.18);stroke-width:2}
.cr-speedometer .needle{stroke:#fff;stroke-width:4;stroke-linecap:round;filter:drop-shadow(0 2px 6px rgba(0,0,0,.55))}
.cr-speedometer .hub{fill:#fff;stroke:#b895ff;stroke-width:5;filter:drop-shadow(0 0 10px rgba(138,92,255,.45))}
.cr-speedometer .value{fill:#fff;font-size:58px;font-weight:1000;letter-spacing:-.06em;text-anchor:middle}
.cr-speedometer .label{fill:#aaa4b3;font-size:10px;font-weight:900;letter-spacing:.16em;text-anchor:middle}
.cr-speedometer .minmax{fill:#716a79;font-size:9px;font-weight:850}
.cr-opening-copy h2{margin:9px 0 0;font-size:clamp(34px,5vw,62px);line-height:1.00;letter-spacing:-.045em}
.cr-opening-copy .lead{max-width:820px;margin:14px 0 0;color:#d8d2df;font-size:18px;line-height:1.55}
.cr-opening-story{margin-top:30px;padding-top:22px;border-top:1px solid rgba(184,149,255,.12)}
.cr-opening-story .story-kicker{color:#8f8798;font-size:9px;font-weight:950;letter-spacing:.18em;text-transform:uppercase}
.cr-opening-story h3{margin:8px 0 0;font-size:clamp(24px,3.4vw,38px);line-height:1.06;letter-spacing:-.03em}
.cr-opening-story p{max-width:820px;margin:10px 0 0;color:#b9b2c0;font-size:15px;line-height:1.66}
.cr-opening-work{margin-top:56px;padding:34px 0 10px;border-top:1px solid rgba(184,149,255,.10);border-bottom:1px solid rgba(184,149,255,.10)}
.cr-opening-work h3{margin:8px 0 0;font-size:clamp(28px,4vw,48px);line-height:1.03;letter-spacing:-.035em}
.cr-opening-work .work-lead{max-width:780px;margin:12px 0 0;color:#b8b1bf;font-size:15px;line-height:1.68}
.cr-workline{display:flex;flex-wrap:wrap;align-items:center;gap:9px;margin-top:22px}
.cr-workline span{color:#f8f7fb;font-size:12px;font-weight:950}
.cr-workline i{font-style:normal;color:#7d7188;font-size:15px}
.cr-opening-signals{display:flex;flex-wrap:wrap;gap:12px;margin-top:22px}
.cr-opening-signal{color:#c8c1cf;font-size:12px;font-weight:850;padding-bottom:9px;border-bottom:1px solid rgba(184,149,255,.18)}
.cr-opening-signal b{color:#b895ff}

@media(max-width:820px){
  .cr-opening-grid{grid-template-columns:1fr;gap:26px}
  .cr-speedometer{max-width:270px}
  .cr-opening-copy h2{font-size:40px}
}

@media(prefers-reduced-motion:reduce){
  .cr-speedometer .range,.cr-speedometer .needle{transition:none!important}
}
'''

s = s.replace('</style>', CSS + '\n</style>', 1)

JS = r'''

(function(){
  const root=document.getElementById('resultsView');
  if(!root || root.dataset.maxessOpeningRefined==='1') return;

  function esc(v){
    return String(v==null?'':v).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
  }
  function rad(deg){return deg*Math.PI/180;}
  function point(cx,cy,r,deg){return {x:cx+r*Math.cos(rad(deg)),y:cy+r*Math.sin(rad(deg))};}
  function pathArc(cx,cy,r,a0,a1){
    const p0=point(cx,cy,r,a0),p1=point(cx,cy,r,a1),large=(a1-a0)>180?1:0;
    return `M ${p0.x.toFixed(2)} ${p0.y.toFixed(2)} A ${r} ${r} 0 ${large} 1 ${p1.x.toFixed(2)} ${p1.y.toFixed(2)}`;
  }
  function buildSpeedometer(score){
    const clamped=Math.max(0,Math.min(100,score));
    const start=-140,end=140,angle=start+(end-start)*(clamped/100);
    const cx=180,cy=170,r=118;
    const needle=point(cx,cy,92,angle);
    const pStart=point(cx,cy,r,start), pEnd=point(cx,cy,r,end);
    return `<svg viewBox="0 0 360 250" role="img" aria-label="MAXESS score ${clamped} out of 100">
      <defs><linearGradient id="maxessSpeedGradient" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="#5424b5"/><stop offset="55%" stop-color="#8a5cff"/><stop offset="100%" stop-color="#b895ff"/></linearGradient></defs>
      <path class="track" d="${pathArc(cx,cy,r,start,end)}"/>
      <path class="range" d="${pathArc(cx,cy,r,start,angle)}"/>
      <line class="tick" x1="${pStart.x}" y1="${pStart.y}" x2="${point(cx,cy,r+12,start).x}" y2="${point(cx,cy,r+12,start).y}"/>
      <line class="tick" x1="${pEnd.x}" y1="${pEnd.y}" x2="${point(cx,cy,r+12,end).x}" y2="${point(cx,cy,r+12,end).y}"/>
      <line class="needle" x1="${cx}" y1="${cy}" x2="${needle.x.toFixed(2)}" y2="${needle.y.toFixed(2)}"/>
      <circle class="hub" cx="${cx}" cy="${cy}" r="9"/>
      <text class="value" x="${cx}" y="${cy-22}">${clamped}</text>
      <text class="label" x="${cx}" y="${cy+4}">MAXESS SCORE</text>
      <text class="minmax" x="${cx-r-2}" y="${cy+22}">0</text>
      <text class="minmax" x="${cx+r-12}" y="${cy+22}">100</text>
    </svg>`;
  }

  function mount(){
    if(!root.classList.contains('visible') || root.dataset.maxessOpeningRefined==='1') return;
    const score=Math.round(Number(document.getElementById('overallScore')?.textContent||0));
    const dims=[...root.querySelectorAll('#dimensionConstellation .dimension-orb')].map((el,i)=>({
      name:el.querySelector('.dimension-name')?.textContent?.trim()||['Direction','Communication','Evaluation','Iteration','Systems Thinking'][i]||'Dimension',
      score:Number(el.querySelector('.dimension-score')?.textContent||0)
    }));
    if(!dims.length) return;
    dims.sort((a,b)=>b.score-a.score);
    const strongest=dims[0];
    const opportunity=dims[dims.length-1];

    const hero=root.querySelector('.result-hero');
    const clean=root.querySelector('.maxess-clean-results');
    if(!hero || !clean) return;

    clean.querySelectorAll('.cr-opening').forEach(el=>el.remove());
    clean.querySelectorAll('.cr-legacy-cleanup').forEach(el=>el.remove());

    const oldAnalysis=clean.querySelector('.cr-analysis');
    const oldSignature=clean.querySelector('.cr-signature');
    const oldDoors=clean.querySelector('.cr-doors');
    const oldNext=clean.querySelector('.cr-next');

    /* Hide the old hero signal entirely. The opening becomes the single source of truth. */
    clean.querySelectorAll('.cr-analysis, .cr-signature, .cr-insight, .cr-naya, .cr-masterkey, .cr-doors, .cr-next').forEach(el=>el.classList.add('cr-legacy-cleanup'));

    const strongestText=document.getElementById('strongestText')?.textContent?.trim()||`Your strongest current capability is ${strongest.name}.`;
    const band=score>=90?'Highly developed AI capability':score>=75?'Strong AI capability':score>=60?'Developing AI capability':'Foundational AI capability';

    const opening=document.createElement('section');
    opening.className='cr-opening';
    opening.innerHTML=`
      <div class="cr-opening-kicker">YOUR PERSONALIZED ANALYSIS</div>
      <div class="cr-opening-grid">
        <div class="cr-speedometer">${buildSpeedometer(score)}</div>
        <div class="cr-opening-copy">
          <div class="cr-opening-kicker">WHAT YOUR SCORE TELLS THE STORY</div>
          <h2>${score}<span style="font-size:.42em;color:#b895ff;vertical-align:super;letter-spacing:0">/100</span></h2>
          <p class="lead">Your score is a snapshot of how deliberately you currently work with AI. It is not a judgment. It shows where your current capability is strongest and where the next gains may live.</p>
          <div class="cr-opening-signals">
            <div class="cr-opening-signal"><b>${esc(band)}</b></div>
            <div class="cr-opening-signal"><b>${esc(strongest.name)}</b> is your natural advantage</div>
            <div class="cr-opening-signal"><b>${esc(opportunity.name)}</b> is your clearest leverage opportunity</div>
          </div>
        </div>
      </div>
      <div class="cr-opening-story">
        <div class="story-kicker">YOUR STORY</div>
        <h3>${esc(strongest.name)} is already showing up in the way you work with AI.</h3>
        <p>${esc(strongestText)} The opportunity isn't to become better at everything. It's to protect what is already working while deliberately developing ${esc(opportunity.name)}.</p>
      </div>
      <div class="cr-opening-work">
        <div class="cr-opening-kicker">HOW YOU WORK WITH AI</div>
        <h3>AI is the engine. You are the director.</h3>
        <p class="work-lead">Your leverage grows when you know what you want, tell AI what matters, ask clearly, look closely at the result, score it honestly, and improve what isn't there yet.</p>
        <div class="cr-workline"><span>KNOW</span><i>→</i><span>TELL</span><i>→</i><span>ASK</span><i>→</i><span>LOOK</span><i>→</i><span>SCORE</span><i>→</i><span>IMPROVE</span><i>→</i><span>REPEAT</span></div>
      </div>`;

    hero.insertAdjacentElement('afterend',opening);
    root.dataset.maxessOpeningRefined='1';
  }

  const obs=new MutationObserver(mount);
  obs.observe(root,{attributes:true,attributeFilter:['class'],childList:true,subtree:true});
  mount();
})();
'''

idx=s.lower().rfind('</script>')
if idx<0: raise RuntimeError('script closing tag missing')
s=s[:idx]+JS+s[idx:]
s=s.replace('</head>', '\n<!-- '+MARKER+' -->\n</head>', 1)
p.write_text(s,encoding='utf-8')
print('Opening refinement applied')
