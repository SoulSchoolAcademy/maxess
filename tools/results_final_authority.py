from pathlib import Path

p = Path("code")
s = p.read_text(encoding="utf-8")
MARK = "MAXESS RESULTS FINAL AUTHORITY V2"
HTML_MARK = "<!-- " + MARK + " -->"

while HTML_MARK in s:
    marker_start = s.find("<!-- " + MARK + " -->")
    if marker_start < 0:
        break
    body_end = s.find("</body>", marker_start)
    if body_end < 0:
        break
    s = s[:marker_start] + s[body_end:]

body_idx = s.rfind("</body>")
if body_idx < 0:
    raise RuntimeError("body closing tag missing")

first_script_end = s.find("</script>")
if first_script_end < 0 or first_script_end > body_idx:
    raise RuntimeError("main application script closing tag missing")
first_script_end += len("</script>")
core = s[:first_script_end].rstrip()

CSS = r'''
/* MAXESS RESULTS FINAL AUTHORITY V2 */
#resultsView{display:none!important;width:100%;max-width:none!important;margin:0!important;}
#resultsView.visible{display:block!important;}
.board-wrap:has(#resultsView.visible){display:block!important;min-height:0!important;}
.board-wrap:has(#resultsView.visible) .board{min-height:0!important;overflow:visible!important;border-radius:0!important;background:transparent!important;}
.board-wrap:has(#resultsView.visible) .board-content{min-height:0!important;padding:0!important;}
.board-wrap:has(#resultsView.visible) .board::before,.board-wrap:has(#resultsView.visible) .board::after{display:none!important;}
.maxess-r2{position:relative;isolation:isolate;width:100%;min-height:100vh;overflow:hidden;color:#f7f5fb;background:radial-gradient(circle at 50% -10%,rgba(126,78,255,.22),transparent 32%),radial-gradient(circle at 5% 42%,rgba(60,168,255,.06),transparent 26%),radial-gradient(circle at 95% 73%,rgba(53,227,155,.05),transparent 24%),linear-gradient(180deg,#050507 0%,#020204 38%,#030305 100%);}
.maxess-r2::before{content:"";position:absolute;inset:0;pointer-events:none;z-index:-1;background:linear-gradient(110deg,transparent 15%,rgba(255,255,255,.018) 50%,transparent 85%);mask-image:linear-gradient(to bottom,black,transparent 70%);}
.maxess-r2 *{box-sizing:border-box;}
.r2-wrap{width:min(1160px,100%);margin:0 auto;padding:clamp(24px,5vw,74px) clamp(16px,4vw,52px) 120px;}
.r2-kicker{font-size:10px;font-weight:950;letter-spacing:.2em;text-transform:uppercase;color:#b896ff;}
.r2-title{margin:8px 0 0;font-size:clamp(40px,6.5vw,80px);line-height:.94;letter-spacing:-.06em;font-weight:950;}
.r2-copy{margin:16px 0 0;color:#b7b0bf;font-size:clamp(16px,2vw,20px);line-height:1.58;max-width:820px;}
.r2-hero{text-align:center;padding:6px 0 64px;}
.r2-hero .r2-copy{margin-left:auto;margin-right:auto;}
.r2-gauge{width:min(650px,100%);margin:28px auto 0;}
.r2-gauge svg{display:block;width:100%;height:auto;overflow:visible;}
.r2-gauge .track{fill:none;stroke:rgba(255,255,255,.075);stroke-width:24;stroke-linecap:round;}
.r2-gauge .fill{fill:none;stroke:url(#r2Gauge);stroke-width:24;stroke-linecap:round;filter:drop-shadow(0 0 16px rgba(138,92,255,.38));}
.r2-gauge .tick{stroke:rgba(255,255,255,.14);stroke-width:2;}
.r2-gauge .tick.major{stroke:rgba(184,149,255,.35);stroke-width:3;}
.r2-gauge .needle{stroke:#fff;stroke-width:5;stroke-linecap:round;filter:drop-shadow(0 0 8px rgba(255,255,255,.52));}
.r2-gauge .hub{fill:#08060d;stroke:#b896ff;stroke-width:3;filter:drop-shadow(0 0 12px rgba(138,92,255,.48));}
.r2-gauge .score{fill:#fff;font:1000 74px system-ui,sans-serif;letter-spacing:-.065em;}
.r2-gauge .label{fill:#aaa3b0;font:950 10px system-ui,sans-serif;letter-spacing:.17em;}
.r2-band{margin-top:-4px;font-size:11px;font-weight:950;letter-spacing:.16em;text-transform:uppercase;color:#d3c7e7;}
.r2-section{position:relative;padding:clamp(66px,8vw,104px) 0;border-top:1px solid rgba(184,149,255,.1);}
.r2-editorial{max-width:970px;margin:0 auto;}
.r2-editorial h2{margin:8px 0 0;font-size:clamp(32px,5vw,62px);line-height:.98;letter-spacing:-.045em;font-weight:950;}
.r2-editorial .lead{margin:18px 0 0;color:#ddd7e3;font-size:clamp(18px,2.2vw,22px);line-height:1.58;max-width:900px;}
.r2-editorial .lead em{font-style:normal;color:#b896ff;}
.r2-sidefacts{display:flex;gap:28px;flex-wrap:wrap;margin-top:24px;}
.r2-fact{min-width:150px;padding-top:12px;border-top:1px solid rgba(255,255,255,.1);}
.r2-fact small{display:block;color:#7e7788;font-size:9px;font-weight:950;letter-spacing:.16em;text-transform:uppercase;}
.r2-fact strong{display:block;margin-top:7px;font-size:22px;line-height:1.04;}
.r2-spectrum{margin-top:28px;padding:24px 0 6px;}
.r2-spectrum-track{height:18px;border-radius:999px;background:linear-gradient(90deg,#34224f 0%,#573e8e 34%,#765cff 63%,#8ee8c8 100%);box-shadow:inset 0 1px 3px rgba(255,255,255,.16),0 12px 28px rgba(0,0,0,.22);position:relative;}
.r2-spectrum-mark{position:absolute;top:50%;width:26px;height:26px;border-radius:50%;transform:translate(-50%,-50%);background:radial-gradient(circle at 30% 22%,#fff 0,#e9ddff 14%,#b896ff 34%,#744cff 63%,#171021 100%);border:1px solid #f1e9ff;box-shadow:0 0 0 6px rgba(138,92,255,.09),0 0 28px rgba(138,92,255,.42);}
.r2-fingerprint{text-align:center;}
.r2-fingerprint h2{margin:8px 0 0;font-size:clamp(34px,5vw,62px);line-height:.97;letter-spacing:-.045em;font-weight:950;}
.r2-fingerprint p{max-width:820px;margin:16px auto 0;color:#aaa3b1;font-size:15px;line-height:1.64;}
.r2-fingerprint-svg{width:min(850px,100%);margin:30px auto 0;}
.r2-fingerprint-svg svg{display:block;width:100%;height:auto;}
.r2-fingerprint-svg .grid{fill:none;stroke:rgba(255,255,255,.08);stroke-width:1;}
.r2-fingerprint-svg .axis{stroke:rgba(184,149,255,.11);stroke-width:1;}
.r2-fingerprint-svg .shape{fill:rgba(138,92,255,.16);stroke:#b896ff;stroke-width:3;filter:drop-shadow(0 0 18px rgba(138,92,255,.24));}
.r2-fingerprint-svg .point{fill:#fff;stroke:#b896ff;stroke-width:2.5;}
.r2-fingerprint-svg .label{fill:#aaa3b1;font:900 11px system-ui,sans-serif;}
.r2-cap-grid{display:grid;grid-template-columns:1fr 1fr;gap:44px;margin-top:34px;}
.r2-cap{padding-top:16px;border-top:1px solid rgba(184,149,255,.14);}
.r2-cap .cap-line{width:44px;height:3px;border-radius:99px;margin-bottom:14px;background:#35e39b;box-shadow:0 0 18px rgba(53,227,155,.24);}
.r2-cap.opportunity .cap-line{background:#8a5cff;box-shadow:0 0 18px rgba(138,92,255,.24);}
.r2-cap small{display:block;color:#7f7888;font-size:9px;font-weight:950;letter-spacing:.16em;text-transform:uppercase;}
.r2-cap h3{margin:8px 0 0;font-size:clamp(28px,4vw,40px);line-height:1.03;letter-spacing:-.035em;}
.r2-cap .score{display:inline-block;margin-top:8px;color:#b896ff;font-size:14px;font-weight:950;}
.r2-cap p{margin:10px 0 0;color:#aaa3b1;font-size:14px;line-height:1.64;}
.r2-insight{padding:clamp(76px,11vw,140px) 0;}
.r2-insight .orbital{width:120px;height:120px;margin:0 0 24px;border-radius:50%;border:1px solid rgba(211,195,255,.68);background:radial-gradient(circle at 30% 20%,#fff 0,#e9ddff 10%,#a27aff 28%,#5b32b1 54%,#08050e 100%);box-shadow:inset 0 2px 7px rgba(255,255,255,.72),0 0 55px rgba(138,92,255,.32),0 19px 34px rgba(0,0,0,.44);position:relative;}
.r2-insight .orbital::after{content:"";position:absolute;inset:-20px;border:1px solid rgba(184,149,255,.09);border-radius:50%;transform:rotate(-12deg) scaleX(1.45);}
.r2-insight blockquote{margin:0;max-width:980px;font-size:clamp(34px,5.6vw,68px);line-height:.98;letter-spacing:-.05em;font-weight:950;}
.r2-insight p{max-width:780px;margin:18px 0 0;color:#aaa3b1;font-size:15px;line-height:1.64;}
.r2-report-artifact{display:flex;justify-content:center;align-items:center;gap:24px;flex-wrap:wrap;}
.r2-doc{width:min(330px,82vw);aspect-ratio:.73;border-radius:28px;padding:20px;background:linear-gradient(145deg,#17131f,#08080b);border:1px solid rgba(184,149,255,.28);box-shadow:inset 0 2px 5px rgba(255,255,255,.08),0 28px 64px rgba(0,0,0,.42),0 0 34px rgba(138,92,255,.1);transform:rotate(-3deg);}
.r2-doc .seal{width:42px;height:42px;border-radius:50%;display:grid;place-items:center;background:radial-gradient(circle,#c9b5ff,#7954ff 56%,#27104f);border:1px solid rgba(255,255,255,.5);font-weight:1000;}
.r2-doc h3{margin:20px 0 0;font-size:28px;line-height:1.02;letter-spacing:-.03em;}
.r2-doc p{margin:10px 0 0;color:#aaa3b1;font-size:11px;line-height:1.5;}
.r2-doc .lines{display:grid;gap:8px;margin-top:18px;}
.r2-doc .line{height:6px;border-radius:99px;background:linear-gradient(90deg,#8a5cff,#2b2635);}
.r2-report-copy{max-width:430px;}
.r2-report-copy h2{margin:0;font-size:clamp(30px,4.4vw,50px);line-height:.98;letter-spacing:-.04em;}
.r2-report-copy p{margin:12px 0 0;color:#aaa3b1;font-size:15px;line-height:1.62;}
.r2-naya{display:grid;grid-template-columns:180px minmax(0,1fr);gap:34px;align-items:center;max-width:1000px;margin:0 auto;}
.r2-naya-photo{width:180px;height:180px;border-radius:50%;overflow:hidden;border:1px solid rgba(240,233,255,.7);box-shadow:inset 0 2px 8px rgba(255,255,255,.72),0 0 55px rgba(138,92,255,.34),0 20px 30px rgba(0,0,0,.43);background:radial-gradient(circle at 30% 20%,#fff,#a27aff 38%,#341774 72%,#06040a);}
.r2-naya-photo img{width:100%;height:100%;display:block;object-fit:cover;}
.r2-naya h2{margin:7px 0 0;font-size:clamp(36px,5vw,60px);line-height:.96;letter-spacing:-.045em;}
.r2-naya p{margin:14px 0 0;color:#b2abb9;font-size:16px;line-height:1.62;max-width:760px;}
.r2-masters{text-align:center;}
.r2-masters h2{margin:8px 0 0;font-size:clamp(34px,4.9vw,60px);line-height:.97;letter-spacing:-.045em;font-weight:950;}
.r2-masters p{max-width:760px;margin:14px auto 0;color:#aaa3b1;font-size:14px;line-height:1.62;}
.r2-network{position:relative;width:min(980px,100%);height:390px;margin:34px auto 0;}
.r2-network .core{position:absolute;left:50%;top:50%;width:116px;height:116px;transform:translate(-50%,-50%);border-radius:50%;display:grid;place-items:center;background:radial-gradient(circle at 30% 20%,#fff 0,#e4d9ff 10%,#9c78ff 34%,#4f2ba8 63%,#08050e 100%);border:1px solid rgba(240,233,255,.7);box-shadow:inset 0 2px 8px rgba(255,255,255,.74),0 0 58px rgba(138,92,255,.42),0 20px 34px rgba(0,0,0,.44);font-weight:1000;font-size:24px;}
.r2-network .orbit{position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);border:1px solid rgba(184,149,255,.16);border-radius:50%;}
.r2-network .o1{width:250px;height:250px;}
.r2-network .o2{width:420px;height:260px;transform:translate(-50%,-50%) rotate(-8deg);}
.r2-network .node{position:absolute;width:128px;text-align:center;transform:translate(-50%,-50%);}
.r2-network .node .rf-gem{width:74px;height:74px;border-radius:23px;margin:0 auto;}
.r2-network .n1{left:17%;top:50%}.r2-network .n2{left:33%;top:12%}.r2-network .n3{left:67%;top:12%}.r2-network .n4{left:83%;top:50%}.r2-network .n5{left:50%;top:90%}
.r2-network .node h3{margin:10px 0 0;font-size:13px;line-height:1.12;}
.r2-network .node span{display:block;margin-top:5px;color:#90889a;font-size:9px;line-height:1.35;}
.r2-keys{text-align:center;}
.r2-keys h2{margin:8px 0 0;font-size:clamp(32px,4.7vw,56px);line-height:.98;letter-spacing:-.04em;font-weight:950;}
.r2-keys p{max-width:720px;margin:14px auto 0;color:#aaa3b1;font-size:14px;line-height:1.62;}
.r2-key-row{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:26px;margin:36px auto 0;max-width:940px;position:relative;}
.r2-key-row::before{content:"";position:absolute;left:18%;right:18%;top:58px;height:2px;background:linear-gradient(90deg,transparent,rgba(184,149,255,.48),transparent);}
.r2-key{position:relative;z-index:1;text-align:center;}
.r2-key .rf-gem{width:116px;height:116px;border-radius:50%;margin:0 auto;box-shadow:inset 0 2px 8px rgba(255,255,255,.74),0 0 38px rgba(138,92,255,.22),0 19px 30px rgba(0,0,0,.42);}
.r2-key h3{margin:16px 0 0;font-size:18px;}
.r2-key p{margin:7px auto 0;color:#90889a;font-size:11px;line-height:1.45;max-width:220px;}
.r2-cta{text-align:center;padding:clamp(80px,12vw,150px) 0 40px;}
.r2-cta h2{margin:8px auto 0;max-width:900px;font-size:clamp(40px,6vw,76px);line-height:.94;letter-spacing:-.055em;font-weight:950;}
.r2-cta p{max-width:700px;margin:16px auto 0;color:#b2abb9;font-size:16px;line-height:1.64;}
.r2-actions{display:flex;justify-content:center;gap:11px;flex-wrap:wrap;margin-top:28px;}
.r2-actions button{min-height:58px;padding:0 26px;border-radius:18px;font-weight:950;cursor:pointer;transition:transform .18s ease,box-shadow .18s ease;}
.r2-primary{border:1px solid rgba(238,228,255,.72);background:linear-gradient(180deg,#c9b0ff,#805cff);color:#0b0712;box-shadow:0 18px 44px rgba(138,92,255,.23);}
.r2-secondary{border:1px solid rgba(255,255,255,.14);background:rgba(8,8,11,.9);color:#fff;}
.r2-actions button:hover{transform:translateY(-2px);}
.r2-disclaimer{margin:22px auto 0;max-width:700px;color:#675f70;font-size:10px;line-height:1.5;}
.rf-gem{display:grid;place-items:center;color:#fff;font-weight:1000;border:1px solid rgba(255,255,255,.64);box-shadow:inset 0 2px 5px rgba(255,255,255,.68),0 0 24px rgba(138,92,255,.18),0 9px 17px rgba(0,0,0,.42);}
.rf-gem.p{background:radial-gradient(circle at 28% 17%,#fff 0,#ddd2ff 12%,#8a5cff 42%,#09050f 100%);}
.rf-gem.b{background:radial-gradient(circle at 28% 17%,#fff 0,#d9ecff 12%,#3ca8ff 42%,#06101a 100%);}
.rf-gem.g{background:radial-gradient(circle at 28% 17%,#fff 0,#d8fff0 12%,#35e39b 42%,#06110b 100%);}
.rf-gem.v{background:radial-gradient(circle at 28% 17%,#fff 0,#ddd8ff 12%,#765cff 42%,#0a0710 100%);}
.rf-gem.m{background:radial-gradient(circle at 28% 17%,#fff 0,#ffd8f5 12%,#ed42c4 42%,#12050f 100%);}
@media(max-width:900px){.r2-network{height:430px}.r2-network .n1{left:12%}.r2-network .n4{left:88%}}
@media(max-width:720px){.r2-cap-grid{grid-template-columns:1fr;gap:28px}.r2-naya{grid-template-columns:1fr;text-align:center}.r2-naya-photo{margin:0 auto}.r2-network{height:470px}.r2-network .n1{left:18%;top:42%}.r2-network .n2{left:36%;top:12%}.r2-network .n3{left:64%;top:12%}.r2-network .n4{left:82%;top:42%}.r2-network .n5{left:50%;top:88%}.r2-key-row{grid-template-columns:1fr;gap:18px}.r2-key .rf-gem{width:98px;height:98px}}
@media(prefers-reduced-motion:reduce){.r2-actions button{transition:none}}
'''

JS = r'''
<!-- MAXESS RESULTS FINAL AUTHORITY V2 -->
<script>
(function(){
  'use strict';
  const root=document.getElementById('resultsView');
  if(!root) return;
  const MARKER='maxessResultsFinalAuthorityV2';
  const NAYA_IMG='https://i.postimg.cc/593L5r04/Naya-and-shawn-ok-0.png';
  const esc=v=>String(v??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
  const clamp=(n,a,b)=>Math.max(a,Math.min(b,n));
  const getDims=()=>{const found=[...root.querySelectorAll('#dimensionConstellation .dimension-orb')].map((el,i)=>({name:el.querySelector('.dimension-name')?.textContent?.trim()||['Direction','Communication','Evaluation','Iteration','Systems Thinking'][i]||'Dimension',score:Number(el.querySelector('.dimension-score')?.textContent||0)})).filter(x=>Number.isFinite(x.score));return found.length===5?found:['Direction','Communication','Evaluation','Iteration','Systems Thinking'].map(name=>({name,score:0}));};
  const getScore=ds=>{const el=document.getElementById('overallScore');const n=Number((el?.textContent||'').replace(/[^\d.]/g,''));return Number.isFinite(n)&&n>=0?clamp(Math.round(n),0,100):clamp(Math.round(ds.reduce((a,b)=>a+b.score,0)/5),0,100);};
  const band=score=>score>=90?'MASTERING AI CAPABILITY':score>=80?'ADVANCING AI CAPABILITY':score>=65?'DEVELOPING AI CAPABILITY':score>=45?'EMERGING AI CAPABILITY':'EARLY AI CAPABILITY';
  const adv={Direction:'You tend to give AI a destination instead of treating every request as an isolated prompt.',Communication:'You tend to shape the conversation with useful context, intent, and direction.',Evaluation:'You tend to notice when an answer is not yet good enough and can judge what matters.',Iteration:'You tend to improve AI output instead of stopping at the first answer.','Systems Thinking':'You tend to connect successful AI work into repeatable methods and workflows.'};
  const opp={Direction:'Make the destination even clearer before asking AI to act.',Communication:'Give AI more of the context, constraints, examples, and standards that shape the result.',Evaluation:'Strengthen the habit of checking whether the result is correct, useful, and complete.',Iteration:'Turn revision into a deliberate loop rather than an occasional correction.','Systems Thinking':'Capture successful methods so you can reuse and improve them instead of starting over.'};
  const safeClick=ids=>{for(const id of ids){const el=document.getElementById(id);if(el){el.click();return true;}}return false;};
  const gauge=score=>{const c=clamp(Math.round(score),0,100),cx=300,cy=262,r=180,a0=-2.46,a1=2.46,a=a0+(a1-a0)*c/100,pt=(ang,rr)=>[cx+rr*Math.cos(ang),cy+rr*Math.sin(ang)],arc=(sAng,eAng)=>{const s=pt(sAng,r),e=pt(eAng,r);return `M ${s[0]} ${s[1]} A ${r} ${r} 0 0 1 ${e[0]} ${e[1]}`;};let ticks='';for(let i=0;i<=10;i++){const t=a0+(a1-a0)*i/10,ri=r-14,ro=r+10,u=pt(t,ri),v=pt(t,ro);ticks+=`<line class="tick ${i%5===0?'major':''}" x1="${u[0]}" y1="${u[1]}" x2="${v[0]}" y2="${v[1]}"/>`;}const labels=[0,25,50,75,100].map(v=>{const t=a0+(a1-a0)*v/100,q=pt(t,r+33);return `<text class="label" x="${q[0]}" y="${q[1]}" text-anchor="middle" dominant-baseline="middle" style="font-size:11px">${v}</text>`;}).join('');const needle=pt(a,126);return `<svg viewBox="0 0 600 400" role="img" aria-label="MAXESS score ${c} out of 100"><defs><linearGradient id="r2Gauge" x1="0" x2="1"><stop offset="0" stop-color="#5523b4"/><stop offset=".58" stop-color="#8a5cff"/><stop offset="1" stop-color="#c9b0ff"/></linearGradient></defs><path class="track" d="${arc(a0,a1)}"/><path class="fill" d="${arc(a0,a)}"/>${ticks}${labels}<line class="needle" x1="${cx}" y1="${cy}" x2="${needle[0]}" y2="${needle[1]}"/><circle class="hub" cx="${cx}" cy="${cy}" r="16"/><text class="score" x="${cx}" y="${cy-4}" text-anchor="middle">${c}</text><text class="label" x="${cx}" y="${cy+28}" text-anchor="middle" style="font-size:10px">YOUR MAXESS SCORE</text></svg>`;};
  const fingerprint=ds=>{const cx=300,cy=220,r=154,n=5,p=(i,rr)=>{const a=-Math.PI/2+i*2*Math.PI/n;return[cx+rr*Math.cos(a),cy+rr*Math.sin(a)];};const poly=f=>ds.map((_,i)=>p(i,r*f).join(',')).join(' ');let grid='';[1,.75,.5,.25].forEach(f=>grid+=`<polygon class="grid" points="${poly(f)}"/>`);let axes='',points='',labels='';ds.forEach((x,i)=>{const q=p(i,r);axes+=`<line class="axis" x1="${cx}" y1="${cy}" x2="${q[0]}" y2="${q[1]}"/>`;points+=`<circle class="point" cx="${q[0]}" cy="${q[1]}" r="6"/>`;const lp=p(i,r+37);labels+=`<text class="label" x="${lp[0]}" y="${lp[1]}" text-anchor="middle" dominant-baseline="middle">${esc(x.name)} · ${Math.round(x.score)}</text>`;});const shape=ds.map((x,i)=>p(i,r*clamp(x.score,0,100)/100).join(',')).join(' ');return `<svg viewBox="0 0 600 440" role="img" aria-label="AI capability fingerprint">${grid}${axes}<polygon class="shape" points="${shape}"/>${points}${labels}</svg>`;};
  function render(){
    if(!root.classList.contains('visible')||root.dataset[MARKER]==='1') return;
    const ds=getDims(),score=getScore(ds),ordered=[...ds].sort((a,b)=>b.score-a.score),strongest=ordered[0],weakest=ordered[4],capBand=band(score);
    const masters=[['Writing','Words & Communication','p','W'],['Research','Evidence & Discovery','b','R'],['Strategy','Direction & Decisions','g','S'],['Creation','Ideas & Media','v','C'],['Systems','Automation & Leverage','m','⚙']];
    const keys=[['01','MASTER KEY','The universal blueprint','p'],['02','SPECIALIZED KEY','Choose the territory','b'],['03','ACTIVATION ROLODEX','Activate the right expert','g']];
    const process=[['KNOW','See the goal','p'],['TELL','Set the context','b'],['ASK','Direct clearly','g'],['LOOK','Inspect the result','v'],['SCORE','Judge honestly','m'],['IMPROVE','Refine deliberately','p'],['REPEAT','Keep what works','b']];
    const insight=`Your strongest signal is ${strongest.name}. Your next leverage appears in ${weakest.name}. The opportunity is not to master everything at once — it is to turn ${strongest.name} into a repeatable advantage while deliberately strengthening ${weakest.name}.`;
    root.innerHTML=`<div class="maxess-r2"><div class="r2-wrap"><section class="r2-hero"><div class="r2-kicker">YOUR MAXESS RESULT</div><div class="r2-title">${score}%</div><div class="r2-band">${capBand}</div><div class="r2-gauge">${gauge(score)}</div><p class="r2-copy">Your score is a snapshot of how deliberately, confidently, and systematically you currently work with AI.</p></section><section class="r2-section"><div class="r2-editorial"><div class="r2-kicker">YOUR PERSONALIZED ANALYSIS</div><h2>Here’s what your result tells us about you.</h2><p class="lead">${esc(adv[strongest.name]||'You already have a meaningful capability to build on.')} <em>Your strongest signal is ${esc(strongest.name)} at ${Math.round(strongest.score)}/100.</em> Your clearest leverage point is ${esc(weakest.name)} at ${Math.round(weakest.score)}/100. ${esc(opp[weakest.name]||'Focused improvement here could create useful leverage.')}</p><div class="r2-sidefacts"><div class="r2-fact"><small>NATURAL ADVANTAGE</small><strong>${esc(strongest.name)}</strong></div><div class="r2-fact"><small>LEVERAGE OPPORTUNITY</small><strong>${esc(weakest.name)}</strong></div><div class="r2-fact"><small>CAPABILITY BAND</small><strong>${esc(capBand)}</strong></div></div></div></section><section class="r2-section"><div class="r2-editorial"><div class="r2-kicker">WHAT YOUR SCORE TELLS YOU</div><h2>Your number needs context.</h2><div class="r2-spectrum"><div class="r2-spectrum-track"><span class="r2-spectrum-mark" style="left:${score}%"></span></div></div><p class="lead">Your ${score}/100 places you in <em>${esc(capBand.toLowerCase())}</em>. The number matters, but the shape underneath it explains where your capability is coming from and where your next leverage lives.</p></div></section><section class="r2-section r2-fingerprint"><div class="r2-kicker">HOW YOU ACTUALLY WORK WITH AI</div><h2>YOUR AI CAPABILITY SIGNATURE</h2><p>This is your AI fingerprint — the shape created by your five core capabilities working together.</p><div class="r2-fingerprint-svg">${fingerprint(ds)}</div><div class="r2-cap-grid"><article class="r2-cap"><div class="cap-line"></div><small>YOUR NATURAL ADVANTAGE</small><h3>${esc(strongest.name)}</h3><span class="score">${Math.round(strongest.score)} / 100</span><p>${esc(adv[strongest.name]||'This is a capability you can continue to leverage.')}</p></article><article class="r2-cap opportunity"><div class="cap-line"></div><small>YOUR HIGHEST-LEVERAGE OPPORTUNITY</small><h3>${esc(weakest.name)}</h3><span class="score">${Math.round(weakest.score)} / 100</span><p>${esc(opp[weakest.name]||'This is a capability where focused improvement may create useful leverage.')}</p></article></div></section><section class="r2-section"><div class="r2-editorial"><div class="r2-kicker">HOW TO WORK WITH AI</div><h2>The simple operating system.</h2><p class="lead">Exceptional AI results become repeatable when you know what you want, communicate it clearly, judge what comes back, and improve it deliberately.</p><div class="rf-process-line">${process.map((x,i)=>`<div class="rf-step"><div class="rf-gem ${x[2]}">${i+1}</div><strong>${x[0]}</strong><span>${x[1]}</span></div>`).join('')}</div></div></section><section class="r2-section r2-insight"><div class="r2-kicker">THE DISCOVERY</div><div class="orbital"></div><blockquote>OH… THAT’S WHY.</blockquote><p>${esc(insight)}</p><p>${esc('This is where the assessment becomes useful: not because of the number itself, but because you can see what to do with it.')}</p></section><section class="r2-section"><div class="r2-report-artifact"><div class="r2-doc" aria-hidden="true"><div class="seal">M</div><h3>YOUR MAXESS<br>AI CAPABILITY REPORT</h3><p>${esc(capBand)}</p><div class="lines"><div class="line"></div><div class="line" style="width:76%"></div><div class="line" style="width:61%"></div><div class="line" style="width:84%"></div></div></div><div class="r2-report-copy"><div class="r2-kicker">KEEP YOUR DISCOVERY</div><h2>Your MAXESS report belongs to you.</h2><p>Take the discovery with you as a premium capability report.</p><div class="r2-actions"><button class="r2-primary" data-r2-save>SAVE MY RESULTS</button></div></div></div></section><section class="r2-section"><div class="r2-naya"><div class="r2-naya-photo"><img src="${NAYA_IMG}" alt="Naya" loading="lazy" onerror="this.style.display='none';"></div><div><div class="r2-kicker">NAYA · YOUR PERSONAL GUIDE</div><h2>I GOT YOU.</h2><p>You just discovered how you work with AI. Now let me show you how to turn that capability into exceptional results.</p></div></div></section><section class="r2-section r2-masters"><div class="r2-kicker">NAYA MASTER INTELLIGENCE</div><h2>Meet your AI Masters.</h2><p>A specialized intelligence team is ready to help you work in the areas that matter to you.</p><div class="r2-network"><div class="orbit o1"></div><div class="orbit o2"></div><div class="core">NAYA</div>${masters.map((m,i)=>`<div class="node n${i+1}"><div class="rf-gem ${m[2]}">${m[3]}</div><h3>Naya Master ${m[0]}</h3><span>${m[1]}</span></div>`).join('')}</div><div class="r2-actions"><button class="r2-secondary" data-r2-explore>EXPLORE ALL MASTERS</button></div></section><section class="r2-section r2-keys"><div class="r2-kicker">THE THREE-KEY SYSTEM</div><h2>It’s actually very simple.</h2><p>Use the right blueprint, choose the right specialty, and activate the right Naya Master.</p><div class="r2-key-row">${keys.map(k=>`<article class="r2-key"><div class="rf-gem ${k[3]}">${k[0]}</div><h3>${k[1]}</h3><p>${k[2]}</p></article>`).join('')}</div></section><section class="r2-section r2-cta"><div class="r2-kicker">MASTER AI</div><h2>Ready to turn capability into exceptional results?</h2><p>You know where you are. You know your leverage. Now you have a simple system and specialized Naya expertise to help you put AI to work.</p><div class="r2-actions"><button class="r2-primary" data-r2-master>START MASTER AI</button><button class="r2-secondary" data-r2-save>SAVE MY RESULTS</button></div><div class="r2-disclaimer">Your MAXESS result is a capability snapshot based on your assessment responses. It is not a diagnosis, prediction, or guarantee.</div></section></div></div>`;
    root.dataset[MARKER]='1';
    root.querySelectorAll('[data-r2-save]').forEach(btn=>btn.addEventListener('click',()=>{if(!safeClick(['pdfButton','saveResultsButton','printButton']))window.print();}));
    root.querySelector('[data-r2-master]')?.addEventListener('click',()=>{if(!safeClick(['freeTrialButton','masterAiButton','startMasterAiButton'])){const link=[...document.querySelectorAll('a')].find(a=>/master/i.test(a.textContent||a.getAttribute('href')||''));if(link)link.click();}});
    root.querySelector('[data-r2-explore]')?.addEventListener('click',()=>window.dispatchEvent(new CustomEvent('maxess:explore-masters')));
  }
  new MutationObserver(render).observe(root,{attributes:true,attributeFilter:['class']});
  render();
})();
</script>
'''

style_idx = core.rfind("</style>")
if style_idx < 0:
    raise RuntimeError("stylesheet closing tag missing")
core = core[:style_idx] + CSS + chr(10) + core[style_idx:]
core += chr(10) + JS + chr(10)
s = core + "</body>" + chr(10) + "</html>" + chr(10)

if s.count(HTML_MARK) != 1:
    raise RuntimeError("final authority HTML marker invalid")
if s.count("<script>") != 2:
    raise RuntimeError("expected one main app script plus one Results authority script")
if "MAXESS RESULTS FINAL AUTHORITY V2" not in s:
    raise RuntimeError("authority marker missing")

p.write_text(s, encoding="utf-8")
print("Applied MAXESS Results Final Authority V2")
