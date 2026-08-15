from pathlib import Path

p = Path('code')
s = p.read_text(encoding='utf-8')
MARK = 'MAXESS RESULTS FINAL AUTHORITY'

# Remove any previous copy of this authority section so the transform is deterministic.
if MARK in s:
    start = s.find('<!-- ' + MARK + ' -->')
    if start >= 0:
        s = s[:start] + s[s.find('</body>', start):]

body_marker = '</body>'
style_marker = '</style>'
script_marker = '</script>'

body_idx = s.rfind(body_marker)
if body_idx < 0:
    raise RuntimeError('body closing tag missing')

# Preserve only the first application script, then add our one authoritative Results renderer.
first_script_end = s.find(script_marker)
if first_script_end < 0 or first_script_end > body_idx:
    raise RuntimeError('main application script closing tag missing')
first_script_end += len(script_marker)

core = s[:first_script_end]

# The source has accumulated several historical Results runtime scripts after the core app.
# Delete all post-core markup/script/style noise and replace it with one clean authority.
core = core.rstrip()

CSS = r'''
/* =========================================================
   MAXESS RESULTS FINAL AUTHORITY
   One clean Results experience. No legacy presentation stack.
========================================================= */
#resultsView{width:100%;max-width:none!important;margin:0!important;display:none;}
#resultsView.visible{display:block;}
.board-wrap:has(#resultsView.visible){display:block!important;min-height:0!important;}
.board-wrap:has(#resultsView.visible) .board{min-height:0!important;overflow:visible!important;border-radius:30px;}
.board-wrap:has(#resultsView.visible) .board-content{min-height:0!important;padding:0!important;}
.board-wrap:has(#resultsView.visible) .board::before,
.board-wrap:has(#resultsView.visible) .board::after{display:none!important;}
.results-final{width:100%;background:radial-gradient(circle at 50% 0,rgba(138,92,255,.16),transparent 35%),linear-gradient(180deg,#050507 0%,#020204 100%);color:#f8f7fb;}
.results-final *{box-sizing:border-box;}
.rf-wrap{width:min(1180px,100%);margin:0 auto;padding:clamp(28px,5vw,72px) clamp(18px,4vw,52px) 104px;}
.rf-kicker{color:#b895ff;font-size:10px;font-weight:950;letter-spacing:.21em;text-transform:uppercase;}
.rf-hero{text-align:center;padding:16px 0 56px;}
.rf-hero h1{margin:10px 0 0;font-size:clamp(38px,6.5vw,78px);line-height:.95;letter-spacing:-.055em;font-weight:950;}
.rf-hero h1 span{color:#b895ff;}
.rf-hero p{max-width:760px;margin:18px auto 0;color:#b8b1c0;font-size:clamp(16px,2vw,20px);line-height:1.58;}
.rf-gauge{max-width:620px;margin:30px auto 0;}
.rf-gauge svg{display:block;width:100%;height:auto;overflow:visible;}
.rf-gauge .track{fill:none;stroke:rgba(255,255,255,.09);stroke-width:24;stroke-linecap:round;}
.rf-gauge .fill{fill:none;stroke:url(#rfGauge);stroke-width:24;stroke-linecap:round;filter:drop-shadow(0 0 15px rgba(138,92,255,.36));}
.rf-gauge .tick{stroke:rgba(255,255,255,.16);stroke-width:2;}
.rf-gauge .tick.major{stroke:rgba(184,149,255,.35);stroke-width:3;}
.rf-gauge .needle{stroke:#fff;stroke-width:5;stroke-linecap:round;filter:drop-shadow(0 0 8px rgba(255,255,255,.55));}
.rf-gauge .hub{fill:#08060d;stroke:#b895ff;stroke-width:3;filter:drop-shadow(0 0 12px rgba(138,92,255,.52));}
.rf-gauge .score{fill:#fff;font:1000 70px system-ui,sans-serif;letter-spacing:-.06em;}
.rf-gauge .label{fill:#a9a2b0;font:950 10px system-ui,sans-serif;letter-spacing:.17em;}
.rf-band{margin-top:-2px;color:#d5c8eb;font-size:11px;font-weight:950;letter-spacing:.16em;text-transform:uppercase;}
.rf-section{padding:82px 0;border-top:1px solid rgba(184,149,255,.11);}
.rf-analysis{display:grid;grid-template-columns:minmax(0,1.45fr) minmax(270px,.65fr);gap:52px;align-items:end;}
.rf-analysis h2{margin:9px 0 0;font-size:clamp(30px,4.8vw,56px);line-height:1.00;letter-spacing:-.04em;font-weight:950;}
.rf-lead{margin:16px 0 0;max-width:860px;color:#ddd6e3;font-size:clamp(17px,2.05vw,21px);line-height:1.56;}
.rf-lead em{font-style:normal;color:#b895ff;}
.rf-analysis-side{display:grid;gap:18px;}
.rf-side{padding-top:16px;border-top:1px solid rgba(255,255,255,.08);}
.rf-side span{display:block;color:#858090;font-size:9px;font-weight:950;letter-spacing:.15em;text-transform:uppercase;}
.rf-side strong{display:block;margin-top:8px;color:#fff;font-size:24px;line-height:1.04;}
.rf-side small{display:block;margin-top:6px;color:#9e97a7;font-size:12px;line-height:1.48;}
.rf-fingerprint{text-align:center;}
.rf-fingerprint h2{margin:10px 0 0;font-size:clamp(34px,5vw,62px);line-height:.97;letter-spacing:-.045em;font-weight:950;}
.rf-fingerprint p{max-width:760px;margin:15px auto 0;color:#aaa3b1;font-size:15px;line-height:1.62;}
.rf-radar{max-width:820px;margin:28px auto 0;}
.rf-radar svg{display:block;width:100%;height:auto;filter:drop-shadow(0 26px 48px rgba(0,0,0,.30));}
.rf-radar .grid{fill:none;stroke:rgba(255,255,255,.08);stroke-width:1;}
.rf-radar .axis{stroke:rgba(184,149,255,.08);stroke-width:1;}
.rf-radar .shape{fill:rgba(138,92,255,.15);stroke:#b895ff;stroke-width:2.6;filter:drop-shadow(0 0 16px rgba(138,92,255,.22));}
.rf-radar .point{fill:#fff;stroke:#b895ff;stroke-width:2;}
.rf-radar .label{fill:#a8a1b0;font:900 11px system-ui,sans-serif;}
.rf-stories{display:grid;grid-template-columns:1fr 1fr;gap:42px;margin-top:34px;text-align:left;}
.rf-story{padding-top:14px;border-top:1px solid rgba(184,149,255,.14);}
.rf-story::before{content:"";display:block;width:34px;height:3px;border-radius:99px;margin-bottom:16px;background:#35e39b;box-shadow:0 0 16px rgba(53,227,155,.25);}
.rf-story.opportunity::before{background:#8a5cff;box-shadow:0 0 16px rgba(138,92,255,.26);}
.rf-story span{display:block;color:#8a8394;font-size:9px;font-weight:950;letter-spacing:.16em;text-transform:uppercase;}
.rf-story h3{margin:8px 0 0;font-size:clamp(26px,3.5vw,38px);line-height:1.04;letter-spacing:-.03em;}
.rf-story p{margin:10px 0 0;color:#aaa3b1;font-size:14px;line-height:1.64;}
.rf-insight{padding:70px 0 76px;}
.rf-insight blockquote{margin:10px 0 0;max-width:980px;font-size:clamp(30px,4.8vw,58px);line-height:1.03;letter-spacing:-.04em;font-weight:950;}
.rf-insight p{max-width:760px;margin:15px 0 0;color:#aaa3b1;font-size:14px;line-height:1.65;}
.rf-process{text-align:center;}
.rf-process h2{margin:10px 0 0;font-size:clamp(32px,4.7vw,56px);line-height:.98;letter-spacing:-.04em;font-weight:950;}
.rf-process h2 em{font-style:normal;color:#b895ff;}
.rf-process > p{max-width:780px;margin:15px auto 0;color:#aaa3b1;font-size:14px;line-height:1.65;}
.rf-process-line{position:relative;display:flex;justify-content:center;gap:0;overflow:auto;margin:30px auto 0;padding:10px 0 14px;scrollbar-width:thin;}
.rf-process-line::before{content:"";position:absolute;left:4%;right:4%;top:37px;height:2px;background:linear-gradient(90deg,rgba(138,92,255,.12),rgba(184,149,255,.52),rgba(138,92,255,.12));}
.rf-step{position:relative;z-index:1;min-width:122px;text-align:center;}
.rf-gem{width:58px;height:58px;margin:0 auto;display:grid;place-items:center;border-radius:19px;border:1px solid rgba(255,255,255,.67);color:#fff;font-size:16px;font-weight:1000;box-shadow:inset 0 2px 5px rgba(255,255,255,.72),0 0 24px rgba(138,92,255,.18),0 9px 17px rgba(0,0,0,.42);}
.rf-gem.p{background:radial-gradient(circle at 28% 17%,#fff 0,#ddd2ff 12%,#8a5cff 42%,#09050f 100%);}
.rf-gem.b{background:radial-gradient(circle at 28% 17%,#fff 0,#d9ecff 12%,#3ca8ff 42%,#06101a 100%);}
.rf-gem.g{background:radial-gradient(circle at 28% 17%,#fff 0,#d8fff0 12%,#35e39b 42%,#06110b 100%);}
.rf-gem.v{background:radial-gradient(circle at 28% 17%,#fff 0,#ddd8ff 12%,#765cff 42%,#0a0710 100%);}
.rf-gem.m{background:radial-gradient(circle at 28% 17%,#fff 0,#ffd8f5 12%,#ed42c4 42%,#12050f 100%);}
.rf-step strong{display:block;margin-top:12px;color:#fff;font-size:12px;font-weight:950;letter-spacing:.04em;}
.rf-step span{display:block;margin-top:5px;color:#858090;font-size:10px;line-height:1.35;}
.rf-naya{display:grid;grid-template-columns:auto minmax(0,1fr);gap:25px;align-items:center;max-width:940px;margin:0 auto;}
.rf-naya-orb{width:96px;height:96px;border-radius:50%;display:grid;place-items:center;background:radial-gradient(circle at 28% 18%,#fff 0,#e2d7ff 12%,#9972ff 38%,#3c1d80 68%,#07030e 100%);border:1px solid #e4d9ff;box-shadow:inset 0 2px 5px rgba(255,255,255,.76),0 0 40px rgba(116,76,255,.36),0 12px 22px rgba(0,0,0,.48);color:#fff;font-size:32px;font-weight:1000;}
.rf-naya h2{margin:8px 0 0;font-size:clamp(30px,4.6vw,52px);line-height:.98;letter-spacing:-.04em;}
.rf-naya p{margin:10px 0 0;color:#aaa3b1;font-size:15px;line-height:1.64;max-width:800px;}
.rf-masters{text-align:center;}
.rf-masters h2{margin:10px 0 0;font-size:clamp(34px,4.9vw,60px);line-height:.97;letter-spacing:-.045em;}
.rf-masters > p{max-width:760px;margin:15px auto 0;color:#aaa3b1;font-size:14px;line-height:1.62;}
.rf-master-line{position:relative;display:grid;grid-template-columns:repeat(5,minmax(0,1fr));gap:12px;margin-top:34px;}
.rf-master-line::before{content:"";position:absolute;left:8%;right:8%;top:46px;height:1px;background:linear-gradient(90deg,transparent,rgba(184,149,255,.42),transparent);}
.rf-master{position:relative;z-index:1;text-align:center;}
.rf-master .rf-gem{width:88px;height:88px;border-radius:27px;margin:0 auto;}
.rf-master h3{margin:14px 0 0;font-size:15px;line-height:1.14;font-weight:950;}
.rf-master span{display:block;margin-top:6px;color:#9a92a4;font-size:10px;line-height:1.38;}
.rf-master small{display:block;margin-top:7px;color:#b895ff;font-size:8px;font-weight:950;letter-spacing:.12em;text-transform:uppercase;}
.rf-next{text-align:center;padding-bottom:28px;}
.rf-next h2{margin:9px auto 0;max-width:840px;font-size:clamp(38px,5.4vw,66px);line-height:.96;letter-spacing:-.05em;font-weight:950;}
.rf-next p{max-width:660px;margin:15px auto 0;color:#aaa3b1;font-size:15px;line-height:1.65;}
.rf-actions{display:flex;justify-content:center;gap:11px;flex-wrap:wrap;margin-top:26px;}
.rf-actions button{min-height:57px;padding:0 25px;border-radius:19px;font-weight:950;cursor:pointer;transition:transform .2s ease,box-shadow .2s ease;}
.rf-primary{border:1px solid rgba(205,188,255,.68);background:linear-gradient(180deg,#b895ff,#765cff);color:#09060f;box-shadow:0 17px 40px rgba(138,92,255,.20);}
.rf-secondary{border:1px solid rgba(255,255,255,.14);background:#08080b;color:#fff;}
.rf-actions button:hover{transform:translateY(-2px);}
.rf-disclaimer{margin-top:20px;color:#6e6677;font-size:10px;line-height:1.5;}
@media(max-width:840px){.rf-analysis{grid-template-columns:1fr}.rf-stories{grid-template-columns:1fr;gap:28px}.rf-master-line{grid-template-columns:repeat(3,minmax(0,1fr));gap:24px 9px}.rf-master-line::before{display:none}.rf-step{min-width:108px}}
@media(max-width:620px){.rf-wrap{padding-inline:16px}.rf-section{padding:58px 0}.rf-process-line{justify-content:flex-start}.rf-naya{grid-template-columns:1fr;text-align:center}.rf-naya-orb{margin:0 auto}.rf-master-line{grid-template-columns:repeat(2,minmax(0,1fr))}.rf-master .rf-gem{width:74px;height:74px;border-radius:23px}.rf-master h3{font-size:13px}.rf-next{padding-top:58px}.rf-hero h1{font-size:56px}}
@media(prefers-reduced-motion:reduce){.rf-actions button{transition:none}}
'''

# Insert the final CSS at the end of the main stylesheet.
style_idx = core.rfind(style_marker)
if style_idx < 0:
    raise RuntimeError('stylesheet closing tag missing')
core = core[:style_idx] + CSS + '\n' + core[style_idx:]

JS = r'''
<!-- MAXESS RESULTS FINAL AUTHORITY -->
<script>
(function(){
  'use strict';
  const root=document.getElementById('resultsView');
  if(!root) return;
  const marker='maxessResultsFinalAuthority';
  const esc=v=>String(v==null?'':v).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
  const dimsFromDom=()=>[...root.querySelectorAll('#dimensionConstellation .dimension-orb')].map((el,i)=>({
    name:el.querySelector('.dimension-name')?.textContent?.trim()||['Direction','Communication','Evaluation','Iteration','Systems Thinking'][i]||'Dimension',
    score:Number(el.querySelector('.dimension-score')?.textContent||0)
  })).filter(d=>Number.isFinite(d.score));
  function pathArc(cx,cy,r,a0,a1){const p=(a)=>[cx+r*Math.cos(a),cy+r*Math.sin(a)];const s=p(a0),e=p(a1);return `M ${s[0]} ${s[1]} A ${r} ${r} 0 0 1 ${e[0]} ${e[1]}`;}
  function speedometer(score){
    const c=Math.max(0,Math.min(100,score)),cx=300,cy=260,r=180,a0=-2.46,a1=2.46,a=a0+(a1-a0)*c/100,p=(ang,rr)=>[cx+rr*Math.cos(ang),cy+rr*Math.sin(ang)],end=p(a,r),needle=p(a,125),s=p(a0,r),e=p(a1,r);
    let ticks='';
    for(let i=0;i<=10;i++){const t=a0+(a1-a0)*i/10,ri=r-14,ro=r+10,cls=i%2===0?'tick major':'tick';ticks+=`<line class="${cls}" x1="${cx+ri*Math.cos(t)}" y1="${cy+ri*Math.sin(t)}" x2="${cx+ro*Math.cos(t)}" y2="${cy+ro*Math.sin(t)}"/>`;}
    return `<svg viewBox="0 0 600 390" role="img" aria-label="MAXESS score ${c} out of 100"><defs><linearGradient id="rfGauge" x1="0" x2="1"><stop offset="0" stop-color="#5424b5"/><stop offset=".58" stop-color="#8a5cff"/><stop offset="1" stop-color="#c4a9ff"/></linearGradient></defs><path class="track" d="M ${s[0]} ${s[1]} A ${r} ${r} 0 0 1 ${e[0]} ${e[1]}"/><path class="fill" d="${pathArc(cx,cy,r,a0,a)}"/>${ticks}<line class="needle" x1="${cx}" y1="${cy}" x2="${needle[0]}" y2="${needle[1]}"/><circle class="hub" cx="${cx}" cy="${cy}" r="16"/><text class="score" x="${cx}" y="${cy-4}" text-anchor="middle">${c}</text><text class="label" x="${cx}" y="${cy+27}" text-anchor="middle">YOUR MAXESS SCORE</text></svg>`;
  }
  function radar(dims){
    const a=dims.slice(0,5),safe=a.length===5?a:[...a,...Array(5-a.length).fill({name:'Capability',score:0})],cx=300,cy=220,r=154,n=5,p=(i,rr)=>{const t=-Math.PI/2+i*2*Math.PI/n;return [cx+rr*Math.cos(t),cy+rr*Math.sin(t)]},poly=f=>safe.map((_,i)=>p(i,r*f).join(',')).join(' '),shape=safe.map((d,i)=>p(i,r*Math.max(.06,Math.min(100,d.score))/100).join(',')).join(' ');
    const axes=safe.map((_,i)=>{const q=p(i,r);return `<line class="axis" x1="${cx}" y1="${cy}" x2="${q[0]}" y2="${q[1]}"/>`;}).join('');
    const labels=safe.map((d,i)=>{const q=p(i,r+38);return `<text class="label" x="${q[0]}" y="${q[1]}" text-anchor="middle">${esc(d.name)}</text>`;}).join('');
    const points=safe.map((d,i)=>{const q=p(i,r*Math.max(.06,Math.min(100,d.score))/100);return `<circle class="point" cx="${q[0]}" cy="${q[1]}" r="5"/>`;}).join('');
    return `<svg viewBox="0 0 600 440" role="img" aria-label="Your AI capability fingerprint">${[.25,.5,.75,1].map(f=>`<polygon class="grid" points="${poly(f)}"/>`).join('')}${axes}<polygon class="shape" points="${shape}"/>${points}${labels}</svg>`;
  }
  function mount(){
    if(!root.classList.contains('visible')||root.dataset[marker]==='1') return;
    const dims=dimsFromDom();
    if(!dims.length) return;
    dims.sort((a,b)=>b.score-a.score);
    const score=Math.round(Number(document.getElementById('overallScore')?.textContent||0));
    const strongest=dims[0],opportunity=dims[dims.length-1];
    const strongestText=document.getElementById('strongestText')?.textContent?.trim()||`Your strongest current capability is ${strongest.name}.`;
    const opportunityText=document.getElementById('opportunityText')?.textContent?.trim()||`Your clearest leverage opportunity is ${opportunity.name}.`;
    const trial=document.getElementById('freeTrialButton');
    const save=document.getElementById('pdfButton');
    const band=score>=90?'MASTERFUL AI CAPABILITY':score>=75?'STRONG AI CAPABILITY':score>=60?'DEVELOPING AI CAPABILITY':'EMERGING AI CAPABILITY';
    const masters=[
      ['Naya Master Writer','Words · Communication · Persuasion','p'],
      ['Naya Master Researcher','Evidence · Discovery · Clarity','b'],
      ['Naya Master Strategist','Business · Direction · Decisions','g'],
      ['Naya Master Creator','Ideas · Visuals · Media','v'],
      ['Naya Master Systems Architect','Automation · Agents · Leverage','m']
    ];
    root.dataset[marker]='1';
    root.innerHTML=`<main class="results-final"><div class="rf-wrap">
      <section class="rf-hero"><div class="rf-kicker">YOUR PERSONALIZED ANALYSIS</div><h1>What your score tells the story.</h1><p>${esc(band)}. Your result is a capability snapshot — a way to understand where you already have momentum and where the next meaningful gain may be.</p><div class="rf-gauge">${speedometer(score)}</div><div class="rf-band">${score}/100 · ${esc(strongest.name)} is your natural advantage</div></section>
      <section class="rf-section rf-analysis"><div><div class="rf-kicker">YOUR STORY</div><h2>${esc(strongest.name)} is already showing up in how you work with AI.</h2><p class="rf-lead">${esc(strongestText)} <em>The opportunity is not to fix everything. It is to keep that strength while deliberately developing ${esc(opportunity.name)}.</em></p></div><div class="rf-analysis-side"><div class="rf-side"><span>Natural advantage</span><strong>${esc(strongest.name)}</strong><small>${Math.round(strongest.score)}/100 · your strongest dimension.</small></div><div class="rf-side"><span>Highest leverage</span><strong>${esc(opportunity.name)}</strong><small>${Math.round(opportunity.score)}/100 · your clearest next opportunity.</small></div></div></section>
      <section class="rf-section rf-fingerprint"><div class="rf-kicker">YOUR AI CAPABILITY SIGNATURE</div><h2>Your AI fingerprint.</h2><p>Five capabilities. One pattern. The graphic lets you recognize your shape before you read the explanation.</p><div class="rf-radar">${radar(dims)}</div><div class="rf-stories"><article class="rf-story"><span>Your natural advantage</span><h3>${esc(strongest.name)}</h3><p>${esc(strongestText)}</p></article><article class="rf-story opportunity"><span>Your highest-leverage opportunity</span><h3>${esc(opportunity.name)}</h3><p>${esc(opportunityText)}</p></article></div></section>
      <section class="rf-section rf-insight"><div class="rf-kicker">THE “OH… THAT’S WHY” MOMENT</div><blockquote>${esc(opportunityText)}</blockquote><p>This is the place to look next because it is directly connected to your assessment pattern — not because we invented a flattering story.</p></section>
      <section class="rf-section rf-process"><div class="rf-kicker">HOW YOU WORK WITH AI</div><h2>AI is the engine. <em>You are the director.</em></h2><p>Know what you want. Give the context. Ask clearly. Look closely. Score the result. Improve it. Repeat.</p><div class="rf-process-line">${[['KNOW','Define the destination','p'],['TELL','Give useful context','b'],['ASK','Shape the request','g'],['LOOK','Inspect the result','v'],['SCORE','Judge the quality','p'],['IMPROVE','Refine deliberately','b'],['REPEAT','Build the habit','m']].map(x=>`<div class="rf-step"><div class="rf-gem ${x[2]}">${x[0].slice(0,1)}</div><strong>${x[0]}</strong><span>${x[1]}</span></div>`).join('')}</div></section>
      <section class="rf-section rf-naya"><div class="rf-naya-orb">N</div><div><div class="rf-kicker">NAYA · YOUR PERSONAL GUIDE</div><h2>Okay. Now we know where to look.</h2><p>${esc(opportunityText)} Start small. Judge the result honestly. Improve it deliberately. Let the win become a repeatable capability.</p></div></section>
      <section class="rf-section rf-masters"><div class="rf-kicker">NAYA · MASTER INTELLIGENCE</div><h2>Specific work deserves specific mastery.</h2><p>One Naya. Many forms of mastery. These are five examples of the specialized intelligence available when the work calls for more focus.</p><div class="rf-master-line">${masters.map((m,i)=>`<article class="rf-master"><div class="rf-gem ${m[2]}">${['✦','⌁','◆','✧','◈'][i]}</div><h3>${m[0]}</h3><span>${m[1]}</span><small>NAYA INTELLIGENCE</small></article>`).join('')}</div></section>
      <section class="rf-section rf-next"><div class="rf-kicker">YOUR NEXT CHAPTER</div><h2>Now make the capability real.</h2><p>Your result shows where you are. The next step is choosing where you want to apply it — then doing the work.</p><div class="rf-actions"><button class="rf-primary" type="button" id="rfMaster">MASTER AI →</button><button class="rf-secondary" type="button" id="rfSave">SAVE MY RESULTS</button></div><div class="rf-disclaimer">Your MAXESS result is a capability snapshot based on your assessment responses. It is not a diagnosis, prediction, or guarantee.</div></section>
    </div></main>`;
    root.querySelector('#rfMaster')?.addEventListener('click',()=>trial?.click());
    root.querySelector('#rfSave')?.addEventListener('click',()=>save?.click());
  }
  const obs=new MutationObserver(mount);
  obs.observe(root,{attributes:true,attributeFilter:['class']});
  mount();
})();
</script>'''

final_code = core + '\n\n' + JS + '\n' + '</body>\n</html>\n'

# Validate the generated artifact before writing it.
if final_code.count('<!-- ' + MARK + ' -->') != 1:
    raise RuntimeError('final authority marker missing')
if final_code.count('<script>') < 1:
    raise RuntimeError('final authority script missing')
if re.search(r'</style>\s*\(function\s*\(', final_code):
    raise RuntimeError('raw JavaScript text detected after stylesheet')
if final_code.count('</body>') != 1:
    raise RuntimeError('unexpected body closing tag count')

p.write_text(final_code, encoding='utf-8')
print('Applied MAXESS Results final authority')
