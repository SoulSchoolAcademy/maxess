from pathlib import Path
import re

PATH = Path('MAXESS-RESULTS-10-GROOVE.html')
s = PATH.read_text(encoding='utf-8')

# 1. Remove the silent production-looking result fixture. Real data is authoritative.
s = re.sub(
    r"window\.MAXESS_RESULT\s*=\s*result\s*\|\|\s*\{.*?\};\n",
    "window.MAXESS_RESULT = result || null;\n",
    s,
    count=1,
    flags=re.S,
)
s = s.replace('data-mode="development-fixture"', 'data-mode="live-result-contract"')

# 2. Remove the bridge that reconstructed fake results from static DOM values.
s = re.sub(
    r'<script id="maxess-result-live-bridge">.*?</script>\s*',
    '''<script id="maxess-result-live-bridge">\n(function(){\n  'use strict';\n  // Naya Law: Results never manufacture production data from presentation markup.\n  // This bridge only announces a real authoritative result when one exists.\n  function boot(){\n    var r=window.MAXESS_RESULT;\n    if(!r) return;\n    window.dispatchEvent(new CustomEvent('maxess:result-ready',{detail:r}));\n  }\n  if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',boot,{once:true});else boot();\n})();\n</script>\n''',
    s,
    count=1,
    flags=re.S,
)

# 3. Remove the known malformed 10.4 script. Its CSS was accidentally emitted as raw JS.
s = re.sub(
    r'<script id="maxess-recognition-flow-10-4-js">.*?</script>\s*',
    '''<script id="maxess-recognition-flow-10-4-js">\n(function(){\n  'use strict';\n  var root=document.getElementById('maxess-results-10');\n  if(!root) return;\n  root.dataset.recognitionFlow104='1';\n})();\n</script>\n''',
    s,
    count=1,
    flags=re.S,
)

# 4. Align the Living Signature engine with the authoritative five dimensions.
s = s.replace(
    "{ key: 'direction', label: 'Direction', short: 'DIR', hue: 274 },\n    { key: 'context', label: 'Context', short: 'CTX', hue: 252 },\n    { key: 'collaboration', label: 'Collaboration', short: 'COL', hue: 218 },\n    { key: 'evaluation', label: 'Evaluation', short: 'EVA', hue: 300 },\n    { key: 'iteration', label: 'Iteration', short: 'ITR', hue: 186 }",
    "{ key: 'direction', label: 'Direction', short: 'DIR', hue: 24 },\n    { key: 'communication', label: 'Communication', short: 'COM', hue: 52 },\n    { key: 'evaluation', label: 'Evaluation', short: 'EVA', hue: 142 },\n    { key: 'iteration', label: 'Iteration', short: 'ITR', hue: 198 },\n    { key: 'systemsThinking', label: 'Systems Thinking', short: 'SYS', hue: 274 }",
)

# 5. Remove hard-coded presentation scores from the five dimension cards.
s = re.sub(r'(<article class="mx-dim mx-reveal") data-score="\d+"', r'\1', s)
# Only replace score values inside mx-dim cards, preserving other page numbers.
def neutralize_dim(match):
    block = match.group(0)
    block = re.sub(r'<strong>\d+<small>/100</small>', '<strong>—<small>/100</small>', block, count=1)
    block = re.sub(r'<span style="--w:\d+%">', '<span style="--w:0%">', block, count=1)
    return block
s = re.sub(r'<article class="mx-dim mx-reveal".*?</article>', neutralize_dim, s, flags=re.S)

# 6. Replace the fallback data in the recognition-flow source with a real-data-only path.
s = s.replace(
    "const fallback=[['Presence',82],['Clarity',78],['Power',74],['Grace',86],['Execution',71]];\n    return entries.length===5?entries:fallback;",
    "return entries;",
)

# 7. Add the authoritative runtime implementation and final visual layer.
addon = r'''
<!-- NAYA-LAW-AAA-IMPLEMENTATION-10 -->
<style id="naya-law-aaa-results-final">
/*
  NAYA LAW AAA IMPLEMENTATION
  Preservation-first final layer.
  This layer improves the existing master artifact in place.
  It does not create a second Results application or scoring engine.
*/
#maxess-results-10{
  --aaa-bg:#030307; --aaa-white:#fff; --aaa-soft:rgba(255,255,255,.76); --aaa-muted:rgba(255,255,255,.52);
  --aaa-red:#ff4b55; --aaa-orange:#ff9d3d; --aaa-yellow:#ffd84a; --aaa-green:#38df91; --aaa-teal:#36d9d1;
  --aaa-blue:#3c9cff; --aaa-indigo:#586cff; --aaa-purple:#965dff; --aaa-magenta:#ef4bc8;
  width:100vw!important; max-width:none!important; margin-left:calc(50% - 50vw)!important; margin-right:calc(50% - 50vw)!important;
  background:var(--aaa-bg)!important; color:var(--aaa-white)!important;
}
#maxess-results-10 .mx-wide{width:min(1840px,100%)!important;max-width:none!important;margin-inline:auto!important}
#maxess-results-10 .mx-section{padding-inline:clamp(20px,4.5vw,88px)!important}

/* HERO: person + score + signature. */
#maxess-results-10 .mx-hero{min-height:min(940px,96vh)!important;display:grid!important;place-items:center!important;padding-block:clamp(56px,7vh,100px)!important;background:
 radial-gradient(circle at 50% 38%,rgba(150,93,255,.22),transparent 32%),
 radial-gradient(circle at 15% 55%,rgba(54,217,209,.06),transparent 26%),
 radial-gradient(circle at 85% 55%,rgba(239,75,200,.06),transparent 26%),#030307!important}
#maxess-results-10 .mx-hero-grid{width:min(1720px,100%)!important;display:grid!important;grid-template-columns:minmax(0,1fr) minmax(360px,680px) minmax(0,1fr)!important;grid-template-areas:"copy orb side"!important;align-items:center!important;gap:clamp(22px,4vw,70px)!important;text-align:center!important}
#maxess-results-10 .mx-hero-grid>.mx-score-orb{grid-area:orb!important;width:min(650px,48vw)!important;min-width:350px!important;margin:auto!important;order:0!important}
#maxess-results-10 .mx-hero-grid>div:first-child{grid-area:copy!important;text-align:right!important}
#maxess-results-10 .mx-hero-grid>div:first-child .mx-hero-actions{justify-content:flex-end!important}
#maxess-results-10 .mx-hero .mx-title{font-size:clamp(44px,5.8vw,88px)!important;line-height:.94!important;max-width:920px!important;margin-left:auto!important}
#maxess-results-10 .mx-hero .mx-copy{font-size:clamp(16px,1.4vw,21px)!important;color:var(--aaa-soft)!important;margin-left:auto!important}
#maxess-results-10 .mx-score-orb{border:1px solid rgba(255,255,255,.24)!important;background:radial-gradient(circle at 32% 24%,rgba(255,255,255,.20),rgba(150,93,255,.22) 22%,rgba(30,14,48,.92) 58%,#020205 78%)!important;box-shadow:0 0 0 1px rgba(255,255,255,.12),inset 0 0 100px rgba(150,93,255,.30),0 45px 130px rgba(0,0,0,.75),0 0 150px rgba(150,93,255,.25)!important;animation:aaaOrb 5s ease-in-out infinite!important;will-change:transform,filter}
#maxess-results-10 .mx-score-orb::before{inset:-4%!important;border-color:rgba(196,181,253,.46)!important;box-shadow:0 0 40px rgba(150,93,255,.20)!important;animation:aaaRing 18s linear infinite!important}
#maxess-results-10 .mx-score-orb::after{inset:8%!important;border-color:rgba(54,217,209,.22)!important;animation:aaaRingReverse 25s linear infinite!important}
#maxess-results-10 .mx-score strong{font-size:clamp(110px,13vw,190px)!important;letter-spacing:-.08em!important;text-shadow:0 0 35px rgba(255,255,255,.18),0 0 80px rgba(150,93,255,.30)!important}
#maxess-results-10 .mx-hero-actions .mx-cta{min-height:60px!important}
@keyframes aaaOrb{0%,100%{transform:scale(1);filter:saturate(1) brightness(1)}50%{transform:scale(1.025);filter:saturate(1.2) brightness(1.08)}}
@keyframes aaaRing{to{transform:rotate(360deg)}}
@keyframes aaaRingReverse{to{transform:rotate(-360deg)}}

/* Chapter hierarchy. */
#maxess-results-10 .mx-section-head h2{font-size:clamp(34px,4.5vw,68px)!important;letter-spacing:-.05em!important}
#maxess-results-10 .mx-section-head p{font-size:clamp(15px,1.25vw,19px)!important;color:var(--aaa-soft)!important}
#maxess-results-10 .mx-eyebrow{color:rgba(255,255,255,.68)!important}
#maxess-results-10 .mx-insight-card{max-width:1220px!important;margin-inline:auto!important}

/* Five dimensions: premium circular gauges, dynamic and score-dominant. */
#maxess-results-10 .mx-dim-grid{display:grid!important;grid-template-columns:repeat(5,minmax(160px,1fr))!important;gap:clamp(12px,1.7vw,24px)!important}
#maxess-results-10 .mx-dim{--g:var(--aaa-purple);--score:0;position:relative!important;min-height:360px!important;border-radius:30px!important;padding:26px 18px!important;display:flex!important;flex-direction:column!important;align-items:center!important;justify-content:flex-start!important;text-align:center!important;background:linear-gradient(160deg,rgba(255,255,255,.06),rgba(255,255,255,.012))!important;border:1px solid rgba(255,255,255,.13)!important;box-shadow:inset 0 1px rgba(255,255,255,.12),0 28px 80px rgba(0,0,0,.42)!important;overflow:hidden!important;transition:transform .28s ease,border-color .28s ease,box-shadow .28s ease!important}
#maxess-results-10 .mx-dim:nth-child(1){--g:var(--aaa-orange)}
#maxess-results-10 .mx-dim:nth-child(2){--g:var(--aaa-yellow)}
#maxess-results-10 .mx-dim:nth-child(3){--g:var(--aaa-green)}
#maxess-results-10 .mx-dim:nth-child(4){--g:var(--aaa-blue)}
#maxess-results-10 .mx-dim:nth-child(5){--g:var(--aaa-purple)}
#maxess-results-10 .mx-dim:hover,#maxess-results-10 .mx-dim:focus-within{transform:translateY(-8px);border-color:color-mix(in srgb,var(--g) 48%,white 8%)!important;box-shadow:inset 0 1px rgba(255,255,255,.2),0 38px 100px rgba(0,0,0,.52),0 0 45px color-mix(in srgb,var(--g) 16%,transparent)!important}
#maxess-results-10 .mx-dim-gauge{position:relative;width:min(176px,82%);aspect-ratio:1;margin:0 auto 10px;display:grid;place-items:center}
#maxess-results-10 .mx-dim-gauge svg{width:100%;height:100%;transform:rotate(-90deg);overflow:visible}
#maxess-results-10 .mx-dim-gauge .g-track{fill:none;stroke:rgba(255,255,255,.08);stroke-width:10}
#maxess-results-10 .mx-dim-gauge .g-value{fill:none;stroke:var(--g);stroke-width:10;stroke-linecap:round;filter:drop-shadow(0 0 8px color-mix(in srgb,var(--g) 42%,transparent));transition:stroke-dashoffset .9s cubic-bezier(.2,.8,.2,1)}
#maxess-results-10 .mx-dim-gauge .g-core{fill:#060609;stroke:color-mix(in srgb,var(--g) 28%,white 8%);stroke-width:1}
#maxess-results-10 .mx-dim-gauge .g-score{position:absolute;font-size:clamp(42px,4vw,60px);font-weight:900;letter-spacing:-.08em;color:#fff;line-height:1}
#maxess-results-10 .mx-dim-gauge .g-score small{font-size:10px;color:rgba(255,255,255,.48);letter-spacing:.08em;margin-left:3px}
#maxess-results-10 .mx-dim-head{position:relative;z-index:2;display:flex!important;flex-direction:column!important;align-items:center!important;gap:5px!important;margin:0!important}
#maxess-results-10 .mx-dim-head .mx-kicker{font-size:9px!important;color:rgba(255,255,255,.44)!important}
#maxess-results-10 .mx-dim-head h3{font-size:18px!important;color:#fff!important}
#maxess-results-10 .mx-dim-head>strong{display:none!important}
#maxess-results-10 .mx-dim>.mx-track{display:none!important}
#maxess-results-10 .mx-dim p{position:relative;z-index:2;font-size:12px!important;line-height:1.5!important;color:rgba(255,255,255,.70)!important;margin:10px 0 0!important;max-width:220px}
#maxess-results-10 .mx-dim .mx-lever{position:relative;z-index:2;width:100%;margin-top:auto!important;padding-top:13px!important;border-top:1px solid rgba(255,255,255,.08)!important}
#maxess-results-10 .mx-dim .mx-lever span{color:var(--g)!important;font-size:9px!important}
#maxess-results-10 .mx-dim .mx-lever b{font-size:11px!important;color:#fff!important}

/* Pattern chapter connects the five dimensions visually. */
#maxess-results-10 .aaa-pattern{padding-block:clamp(58px,7vw,104px)!important;background:#f7f7fa!important;color:#09090c!important}
#maxess-results-10 .aaa-pattern .aaa-pattern-head{text-align:center;max-width:920px;margin:0 auto 36px}
#maxess-results-10 .aaa-pattern .aaa-pattern-head .mx-eyebrow{color:#5b31a9!important}
#maxess-results-10 .aaa-pattern .aaa-pattern-head h2{font-size:clamp(38px,5vw,76px);letter-spacing:-.055em;line-height:.94;margin:10px 0}
#maxess-results-10 .aaa-pattern .aaa-pattern-head p{font-size:clamp(16px,1.35vw,20px);color:#38383f;line-height:1.55}
#maxess-results-10 .aaa-pattern-grid{position:relative;width:min(1280px,100%);margin:auto;display:grid;grid-template-columns:repeat(5,1fr);gap:16px}
#maxess-results-10 .aaa-pattern-grid::before{content:"";position:absolute;left:8%;right:8%;top:50%;height:2px;background:linear-gradient(90deg,rgba(255,157,61,.5),rgba(255,216,74,.55),rgba(56,223,145,.55),rgba(60,156,255,.55),rgba(150,93,255,.6));z-index:0}
#maxess-results-10 .aaa-pattern-node{position:relative;z-index:1;aspect-ratio:1;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;border-radius:50%;background:#fff;border:1px solid rgba(0,0,0,.08);box-shadow:0 20px 55px rgba(0,0,0,.13);transition:transform .25s ease,box-shadow .25s ease}
#maxess-results-10 .aaa-pattern-node:hover{transform:translateY(-8px);box-shadow:0 28px 70px rgba(0,0,0,.18)}
#maxess-results-10 .aaa-pattern-node i{width:10px;height:10px;border-radius:50%;background:var(--g);box-shadow:0 0 16px color-mix(in srgb,var(--g) 40%,transparent);margin-bottom:10px}
#maxess-results-10 .aaa-pattern-node b{font-size:13px;color:#111}
#maxess-results-10 .aaa-pattern-node strong{font-size:38px;letter-spacing:-.07em;color:#111;margin-top:5px}

/* Naya chapter is a report transition, not a sales interruption. */
#maxess-results-10 #naya-report{background:#08080b!important;padding-block:clamp(62px,7vw,110px)!important}
#maxess-results-10 #naya-report .mx-bridge-card{max-width:1320px!important;margin-inline:auto!important;background:radial-gradient(circle at 50% 0,rgba(150,93,255,.22),transparent 55%),linear-gradient(145deg,rgba(255,255,255,.07),rgba(255,255,255,.018))!important;border:1px solid rgba(150,93,255,.30)!important}

/* Naya Masters: retain the existing 18 pathways and strengthen their visual language. */
#maxess-results-10 .mx-areas{grid-template-columns:repeat(2,minmax(0,1fr))!important;gap:14px!important}
#maxess-results-10 .mx-area{min-height:94px;border-radius:20px!important;background:linear-gradient(145deg,rgba(255,255,255,.055),rgba(255,255,255,.012))!important;border-color:rgba(255,255,255,.12)!important}
#maxess-results-10 .mx-area-num{color:rgba(255,255,255,.38)!important}
#maxess-results-10 .mx-area-main h3{font-size:15px!important;color:#fff!important}
#maxess-results-10 .mx-area-main p{color:rgba(255,255,255,.60)!important}
#maxess-results-10 .mx-mini{min-height:44px!important;border-radius:13px!important}

/* Conversion stays later and preserves the existing NayaNET foundation. */
#maxess-results-10 .mx-growth{background:#030307!important}
#maxess-results-10 .mx-growth-grid{grid-template-columns:repeat(2,minmax(0,1fr))!important;gap:22px!important}
#maxess-results-10 .mx-growth-card{border-radius:30px!important;background:linear-gradient(145deg,rgba(255,255,255,.06),rgba(255,255,255,.015))!important}

/* Accessibility and print. */
#maxess-results-10 :focus-visible{outline:3px solid rgba(255,255,255,.96)!important;outline-offset:4px!important}
@media(max-width:1150px){#maxess-results-10 .mx-hero-grid{grid-template-columns:1fr!important;grid-template-areas:"orb" "copy" "side"!important;max-width:800px!important}#maxess-results-10 .mx-hero-grid>div:first-child{text-align:center!important}#maxess-results-10 .mx-hero-grid>div:first-child .mx-hero-actions{justify-content:center!important}#maxess-results-10 .mx-dim-grid{grid-template-columns:repeat(3,1fr)!important}#maxess-results-10 .aaa-pattern-grid{grid-template-columns:repeat(3,1fr)!important}.aaa-pattern-node:last-child{grid-column:2}}
@media(max-width:760px){#maxess-results-10 .mx-hero{min-height:auto!important;padding-block:48px!important}#maxess-results-10 .mx-hero-grid>.mx-score-orb{width:min(500px,84vw)!important;min-width:280px!important}#maxess-results-10 .mx-dim-grid{grid-template-columns:repeat(2,1fr)!important}#maxess-results-10 .mx-areas{grid-template-columns:1fr!important}#maxess-results-10 .mx-growth-grid{grid-template-columns:1fr!important}#maxess-results-10 .aaa-pattern-grid{grid-template-columns:repeat(2,1fr)!important}.aaa-pattern-node:last-child{grid-column:1/-1;width:50%;margin-inline:auto}}
@media(max-width:520px){#maxess-results-10 .mx-section{padding-inline:16px!important}#maxess-results-10 .mx-dim-grid{grid-template-columns:1fr!important}#maxess-results-10 .mx-dim{min-height:330px!important}#maxess-results-10 .aaa-pattern-grid{grid-template-columns:1fr 1fr!important;gap:10px}.aaa-pattern-node:last-child{grid-column:1/-1;width:55%}}
@media(prefers-reduced-motion:reduce){#maxess-results-10 .mx-score-orb,#maxess-results-10 .mx-score-orb::before,#maxess-results-10 .mx-score-orb::after,#maxess-results-10 .mx-dim,#maxess-results-10 .aaa-pattern-node{animation:none!important;transition:none!important}}
@media print{
 @page{size:letter;margin:.5in}
 html,body{background:#fff!important;color:#111!important}
 #maxess-results-10{width:100%!important;margin:0!important;background:#fff!important;color:#111!important}
 #maxess-results-10 .mx-hero{min-height:auto!important;background:#fff!important;padding:20px 0 28px!important}
 #maxess-results-10 .mx-hero-grid{display:block!important;text-align:center!important}
 #maxess-results-10 .mx-score-orb{width:230px!important;min-width:0!important;margin:10px auto 20px!important;animation:none!important;box-shadow:none!important}
 #maxess-results-10 .mx-hero-actions,#maxess-results-10 .mx-proof,.nl-print{display:none!important}
 #maxess-results-10 .mx-section{padding:20px 0!important;break-inside:avoid!important}
 #maxess-results-10 .mx-dim-grid{grid-template-columns:repeat(5,1fr)!important;gap:8px!important}
 #maxess-results-10 .mx-dim{min-height:190px!important;background:#fff!important;color:#111!important;box-shadow:none!important;border:1px solid #bbb!important}
 #maxess-results-10 .mx-dim-gauge{width:105px!important}
 #maxess-results-10 .mx-dim p,#maxess-results-10 .mx-lever b,#maxess-results-10 .mx-section-head p{color:#333!important}
 #maxess-results-10 .aaa-pattern{background:#fff!important;color:#111!important}
 #maxess-results-10 .aaa-pattern-grid{grid-template-columns:repeat(5,1fr)!important}
 #maxess-results-10 .aaa-pattern-node{box-shadow:none!important}
 #maxess-results-10 .mx-area,#maxess-results-10 .mx-naya-door,#maxess-results-10 .mx-growth-card{break-inside:avoid!important}
}
</style>
<script id="maxess-aaa-runtime">
(function(){
  'use strict';
  var root=document.getElementById('maxess-results-10');
  if(!root||root.dataset.aaaRuntime==='1')return;
  root.dataset.aaaRuntime='1';
  root.dataset.nayaLaw='active';
  root.dataset.nayaLawStatus='implementation-pass';

  var names=['Direction','Communication','Evaluation','Iteration','Systems Thinking'];
  var colors=['#ff9d3d','#ffd84a','#38df91','#3c9cff','#965dff'];
  var clamp=function(n){return Math.max(0,Math.min(100,n));};
  var num=function(v){var n=Number(v);return Number.isFinite(n)?n:null;};
  function read(){
    var r=window.MAXESS_RESULT;
    if(!r)return null;
    var raw=Array.isArray(r.dimensions)?r.dimensions:[];
    var dims=names.map(function(name,i){
      var d=raw[i]||{};
      return {name:d.name||name,score:clamp(num(d.score??d.value)??0),insight:d.insight||d.description||''};
    });
    var overall=num(r.overallScore??r.masterScore??r.overall??r.score);
    if(overall===null)overall=dims.reduce(function(a,d){return a+d.score},0)/5;
    return {raw:r,overall:clamp(overall),dims:dims};
  }
  function band(v){if(v<=50)return'Foundation';if(v<=75)return'Developing';if(v<=90)return'Advancing';return'Mastering';}
  function setText(el,text){if(el)el.textContent=text;}
  function update(){
    var data=read();
    if(!data){
      root.classList.add('aaa-no-result');
      var score=root.querySelector('.mx-score strong');setText(score,'—');
      var bandEl=root.querySelector('.mx-band');setText(bandEl,'Result not loaded');
      root.querySelectorAll('.mx-dim').forEach(function(card){var s=card.querySelector('.mx-dim-head strong');if(s)s.innerHTML='—<small>/100</small>';});
      return;
    }
    root.classList.remove('aaa-no-result');
    var score=root.querySelector('.mx-score strong');setText(score,String(Math.round(data.overall)));
    setText(root.querySelector('.mx-band'),band(data.overall));

    root.querySelectorAll('.mx-dim').forEach(function(card,i){
      var d=data.dims[i];if(!d)return;
      card.dataset.score=String(Math.round(d.score));
      card.style.setProperty('--score',String(d.score));
      card.style.setProperty('--g',colors[i]);
      var old=card.querySelector('.mx-dim-head strong');if(old)old.innerHTML='—<small>/100</small>';
      var gauge=card.querySelector('.mx-dim-gauge');
      if(!gauge){
        gauge=document.createElement('div');gauge.className='mx-dim-gauge';
        gauge.innerHTML='<svg viewBox="0 0 120 120" aria-hidden="true"><circle class="g-track" cx="60" cy="60" r="49"></circle><circle class="g-value" cx="60" cy="60" r="49"></circle><circle class="g-core" cx="60" cy="60" r="39"></circle></svg><span class="g-score">—<small>/100</small></span>';
        var head=card.querySelector('.mx-dim-head');card.insertBefore(gauge,head||card.firstChild);
      }
      gauge.style.setProperty('--g',colors[i]);
      var circle=gauge.querySelector('.g-value');var circumference=2*Math.PI*49;circle.style.strokeDasharray=String(circumference);circle.style.strokeDashoffset=String(circumference*(1-d.score/100));
      var gs=gauge.querySelector('.g-score');if(gs)gs.innerHTML=Math.round(d.score)+'<small>/100</small>';
      var h=card.querySelector('.mx-dim-head h3');setText(h,d.name);
      var p=card.querySelector('.mx-dim>p');if(p&&d.insight)p.textContent=d.insight;
      var tr=card.querySelector('.mx-track span');if(tr)tr.style.setProperty('--w',d.score+'%');
    });
    // Keep the existing scorecard in sync without introducing another scoring engine.
    root.querySelectorAll('.mx-scorecard-row').forEach(function(row,i){var d=data.dims[i];if(!d)return;setText(row.querySelector('span'),d.name);setText(row.querySelector('b'),String(Math.round(d.score)));var bar=row.querySelector('i');if(bar)bar.style.setProperty('--w',d.score+'%');});
    var range=root.querySelector('.mx-growth-card .mx-band-rail');if(range){range.querySelectorAll('div').forEach(function(x){x.classList.remove('active')});var idx=data.overall<=50?0:data.overall<=75?1:data.overall<=90?2:3;var active=range.querySelectorAll('div')[idx];if(active)active.classList.add('active');}
    var max=root.querySelector('#growth-scorecard .mx-growth-card:nth-child(2) h3');if(max)max.innerHTML='You\'re in<br>'+band(data.overall)+'.';
    buildPattern(data);
    root.dispatchEvent(new CustomEvent('maxess:result-rendered',{detail:data}));
  }
  function buildPattern(data){
    if(!data)return;
    var existing=root.querySelector('.aaa-pattern');if(existing)existing.remove();
    var section=document.createElement('section');section.className='mx-section aaa-pattern';section.setAttribute('aria-labelledby','aaa-pattern-title');
    section.innerHTML='<div class="mx-wide"><div class="aaa-pattern-head"><span class="mx-eyebrow">04 · YOUR PATTERN</span><h2 id="aaa-pattern-title">See how your strengths work together.</h2><p>Your score tells you where you are. Your pattern shows you how your five dimensions combine to create your current way of working with AI.</p></div><div class="aaa-pattern-grid" role="list"></div></div>';
    var grid=section.querySelector('.aaa-pattern-grid');
    data.dims.forEach(function(d,i){var n=document.createElement('div');n.className='aaa-pattern-node';n.style.setProperty('--g',colors[i]);n.setAttribute('role','listitem');n.innerHTML='<i aria-hidden="true"></i><b>'+String(d.name).replace(/[&<>]/g,'')+'</b><strong>'+Math.round(d.score)+'</strong>';grid.appendChild(n);});
    var fp=document.getElementById('your-fingerprint');if(fp)fp.parentNode.insertBefore(section,fp);
  }
  function installNoResultNotice(){
    var hero=root.querySelector('.mx-hero');if(!hero||hero.querySelector('.aaa-no-result-notice'))return;
    var notice=document.createElement('p');notice.className='aaa-no-result-notice';notice.textContent='Your MAXESS result will appear here when the assessment result is loaded.';notice.style.cssText='display:none;max-width:680px;margin:18px auto 0;color:rgba(255,255,255,.72);font-size:15px';hero.querySelector('.mx-hero-grid')?.appendChild(notice);
    var observer=new MutationObserver(function(){notice.style.display=root.classList.contains('aaa-no-result')?'block':'none';});observer.observe(root,{attributes:true,attributeFilter:['class']});
  }
  function boot(){installNoResultNotice();update();}
  if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',boot,{once:true});else boot();
  window.addEventListener('maxess:result-ready',update);
  window.addEventListener('maxess:result-updated',update);
})();
</script>
'''

# Remove any prior duplicate copy of our marker before appending (idempotence).
s = re.sub(r'\s*<!-- NAYA-LAW-AAA-IMPLEMENTATION-10 -->.*?\s*</script>\s*$', '', s, flags=re.S)
s = s.rstrip() + '\n' + addon

PATH.write_text(s, encoding='utf-8')
print('Applied Naya Law AAA implementation to', PATH)
print('Bytes:', PATH.stat().st_size)
