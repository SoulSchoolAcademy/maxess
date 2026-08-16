from pathlib import Path

FILES = [
    "MAXESS-RESULTS-10-GROOVE.html",
    "MAXESS-RESULTS-FINAL-GROOVE.html",
    "MAXESS-RESULTS-GROOVE-EMBED.html",
    "MAXESS-RESULTS-FINAL-GROOVE-EMBED.html",
    "MAXESS-RESULTS-GROOVE-EMBED-9.95.html",
]
MARK = "NAYA-LAW-AAA-RESULTS-PASS-3"
NAYA_IMAGE = "https://i.postimg.cc/dVXw7sRN/grok-image-f75a6f12-4e3a-4c99-a334-5684ba0f7401.jpg"

CSS = r'''
/* NAYA LAW AAA PASS 3 — report-first, data-driven, Naya visual identity */
#maxess-results-10 .nl3-report{width:min(1500px,100%);margin:0 auto;padding:clamp(34px,5vw,78px) 0}
#maxess-results-10 .nl3-report-head{text-align:center;max-width:900px;margin:0 auto 34px}
#maxess-results-10 .nl3-kicker{display:inline-block;font-size:11px;font-weight:900;letter-spacing:.18em;text-transform:uppercase;color:rgba(255,255,255,.58)}
#maxess-results-10 .nl3-report-head h2{margin:10px 0 12px;font-size:clamp(34px,4.8vw,70px);line-height:.96;letter-spacing:-.055em}
#maxess-results-10 .nl3-report-head p{margin:0;color:rgba(255,255,255,.68);font-size:clamp(16px,1.35vw,20px);line-height:1.6}
#maxess-results-10 .nl3-naya{display:grid;grid-template-columns:minmax(190px,280px) minmax(0,1fr);gap:28px;align-items:center;padding:clamp(24px,3vw,42px);border:1px solid rgba(196,181,253,.24);border-radius:32px;background:linear-gradient(135deg,rgba(155,99,255,.12),rgba(85,230,255,.045),rgba(255,255,255,.025));box-shadow:0 30px 90px rgba(0,0,0,.42),inset 0 1px rgba(255,255,255,.13);overflow:hidden}
#maxess-results-10 .nl3-naya-portrait{width:min(230px,100%);aspect-ratio:1/1;border-radius:28px;object-fit:cover;object-position:center top;border:1px solid rgba(255,255,255,.22);box-shadow:0 20px 55px rgba(0,0,0,.48),0 0 45px rgba(155,99,255,.14);background:#09070d}
#maxess-results-10 .nl3-naya-copy h3{margin:7px 0 10px;font-size:clamp(28px,3.2vw,48px);line-height:1;letter-spacing:-.045em}
#maxess-results-10 .nl3-naya-copy p{margin:0;color:rgba(255,255,255,.68);font-size:16px;line-height:1.6;max-width:720px}
#maxess-results-10 .nl3-status{display:inline-flex;align-items:center;gap:8px;margin-top:18px;padding:9px 13px;border-radius:999px;border:1px solid rgba(85,230,255,.18);background:rgba(85,230,255,.05);font-size:10px;font-weight:900;letter-spacing:.12em;text-transform:uppercase;color:rgba(255,255,255,.72)}
#maxess-results-10 .nl3-status i{width:7px;height:7px;border-radius:50%;background:#55e6ff;box-shadow:0 0 13px rgba(85,230,255,.8)}
#maxess-results-10 .nl3-gauges{display:grid;grid-template-columns:repeat(5,minmax(150px,1fr));gap:18px;margin-top:34px}
#maxess-results-10 .nl3-gauge{--nl3-g:#965dff;position:relative;min-height:320px;padding:24px 18px;border-radius:28px;border:1px solid rgba(255,255,255,.13);background:#050507;display:flex;flex-direction:column;align-items:center;text-align:center;overflow:hidden;box-shadow:inset 0 1px rgba(255,255,255,.1),0 24px 70px rgba(0,0,0,.34)}
#maxess-results-10 .nl3-ring{width:164px;height:164px;border-radius:50%;display:grid;place-items:center;background:conic-gradient(var(--nl3-g) calc(var(--nl3-score)*1%),rgba(255,255,255,.08) 0);box-shadow:0 0 25px color-mix(in srgb,var(--nl3-g) 25%,transparent);flex:none}
#maxess-results-10 .nl3-ring::after{content:"";width:134px;height:134px;border-radius:50%;background:#050507;box-shadow:inset 0 0 28px rgba(0,0,0,.72)}
#maxess-results-10 .nl3-gauge-score{position:absolute;top:76px;left:0;right:0;font-size:42px;font-weight:900;line-height:1;color:var(--nl3-g);text-shadow:0 0 20px color-mix(in srgb,var(--nl3-g) 30%,transparent);z-index:2}
#maxess-results-10 .nl3-gauge h3{margin:16px 0 6px;font-size:17px;line-height:1.15}
#maxess-results-10 .nl3-gauge p{margin:0;color:rgba(255,255,255,.62);font-size:12px;line-height:1.5}
#maxess-results-10 .nl3-meaning{margin-top:30px;padding:clamp(24px,3vw,42px);border-radius:30px;background:linear-gradient(145deg,rgba(255,255,255,.06),rgba(255,255,255,.018));border:1px solid rgba(255,255,255,.11)}
#maxess-results-10 .nl3-meaning h3{margin:0 0 10px;font-size:clamp(28px,3.2vw,48px);letter-spacing:-.045em}
#maxess-results-10 .nl3-meaning p{margin:0;color:rgba(255,255,255,.7);font-size:16px;line-height:1.65;max-width:900px}
#maxess-results-10 .nl3-missing{padding:34px;border:1px solid rgba(255,170,80,.3);border-radius:24px;background:rgba(255,170,80,.05);color:#fff;text-align:center}
#maxess-results-10 .nl3-missing h2{margin:0 0 8px;font-size:30px}
#maxess-results-10 .nl3-missing p{margin:0;color:rgba(255,255,255,.68)}
@media(max-width:980px){#maxess-results-10 .nl3-gauges{grid-template-columns:repeat(2,1fr)}#maxess-results-10 .nl3-naya{grid-template-columns:1fr;text-align:center}#maxess-results-10 .nl3-naya-portrait{margin:auto}}
@media(max-width:560px){#maxess-results-10 .nl3-report{padding-inline:0}#maxess-results-10 .nl3-gauges{grid-template-columns:1fr}#maxess-results-10 .nl3-gauge{min-height:300px}#maxess-results-10 .nl3-naya{padding:20px;border-radius:24px}#maxess-results-10 .nl3-naya-portrait{width:min(220px,72vw)}}
@media(prefers-reduced-motion:reduce){#maxess-results-10 .nl3-gauge,#maxess-results-10 .nl3-naya{transition:none!important}}
@media print{#maxess-results-10 .nl3-report{break-inside:auto}#maxess-results-10 .nl3-naya{break-inside:avoid;background:#fff;color:#111;border:1px solid #aaa;box-shadow:none}#maxess-results-10 .nl3-naya-copy p,#maxess-results-10 .nl3-meaning p{color:#222}#maxess-results-10 .nl3-gauges{grid-template-columns:repeat(5,1fr)}#maxess-results-10 .nl3-gauge{break-inside:avoid;background:#fff;color:#111;box-shadow:none;border:1px solid #aaa}#maxess-results-10 .nl3-ring{box-shadow:none}#maxess-results-10 .nl3-ring::after{background:#fff}#maxess-results-10 .nl3-gauge h3,#maxess-results-10 .nl3-gauge p{color:#111}}
'''

JS = r'''
<script id="naya-law-aaa-pass-3-js">
(function(){
  'use strict';
  var ROOT='maxess-results-10';
  var NAYA_IMAGE='__NAYA_IMAGE__';
  var DIM_COLORS=['#ff9d3d','#ffd84a','#38df91','#3c9cff','#965dff'];
  var DIM_NAMES=['Direction','Communication','Evaluation','Iteration','Systems Thinking'];
  var root=document.getElementById(ROOT); if(!root)return;
  function num(v){var n=Number(v);return Number.isFinite(n)?Math.max(0,Math.min(100,n)):null;}
  function isFixture(r){return !!r && Number(r.resonance)===10.10 && r.signature==='LIVING' && r.naya==='AWAKENED' && r.groove==='MAXIMAL' && r.status==='FULL_ACTIVATION';}
  function read(){
    var r=window.MAXESS_RESULT;
    if(!r || isFixture(r))return null;
    var overall=num(r.masterScore??r.overallScore??r.overall??r.score);
    var raw=Array.isArray(r.dimensions)?r.dimensions:(r.dimensionScores&&typeof r.dimensionScores==='object'?r.dimensionScores:null);
    var dims=[];
    if(Array.isArray(raw)){
      raw.forEach(function(d,i){if(d){var s=num(d.score??d.value);if(s!==null)dims.push({name:d.name||d.label||DIM_NAMES[i]||('Dimension '+(i+1)),score:s,insight:d.insight||d.description||''});}});
    }else if(raw){Object.keys(raw).forEach(function(k){var v=raw[k];var s=num(v&&typeof v==='object'?(v.score??v.value):v);if(s!==null)dims.push({name:k,score:s,insight:v&&v.insight||v&&v.description||''});});}
    if(overall===null && dims.length===5)overall=Math.round(dims.reduce(function(a,d){return a+d.score},0)/5);
    if(overall===null || dims.length<5)return null;
    return {overall:overall,band:overall>=91?'MASTERING':overall>=76?'ADVANCING':overall>=51?'DEVELOPING':'FOUNDATION',dims:dims.slice(0,5)};
  }
  function hideOld(){
    root.querySelectorAll('.mx-proof').forEach(function(e){e.style.display='none'});
    var old=root.querySelector('.mx-score-orb');
    if(old)old.style.display='none';
  }
  function hero(data){
    var title=root.querySelector('.mx-hero .mx-title');
    var copy=root.querySelector('.mx-hero .mx-copy');
    if(title)title.innerHTML='Your MAXESS AI<br><em>Assessment Score.</em>';
    if(copy)copy.textContent='This is your personal AI Mastery Report — where you are now, what it means, and what to do next.';
    var score=root.querySelector('.mx-hero .mx-score strong');
    if(score)score.textContent=Math.round(data.overall);
    var band=root.querySelector('.mx-hero .mx-band'); if(band)band.textContent=data.band;
  }
  function report(data){
    if(root.querySelector('.nl3-report'))return;
    var sec=document.createElement('section');sec.className='mx-section nl3-report';
    var strongest=data.dims.slice().sort(function(a,b){return b.score-a.score})[0];
    var weakest=data.dims.slice().sort(function(a,b){return a.score-b.score})[0];
    var gauges=data.dims.map(function(d,i){return '<article class="nl3-gauge" style="--nl3-g:'+DIM_COLORS[i]+';--nl3-score:'+d.score+'"><div class="nl3-ring"></div><strong class="nl3-gauge-score">'+Math.round(d.score)+'</strong><h3>'+esc(d.name)+'</h3><p>'+esc(d.insight||defaultInsight(d.name))+'</p></article>'}).join('');
    sec.innerHTML='<div class="nl3-report-head"><span class="nl3-kicker">PERSONALIZED REPORT</span><h2>Listen to your results.<br>Hear what they mean.</h2><p>Naya turns your assessment into a practical understanding of where you are, where you can grow, and what you can do next.</p></div><div class="nl3-naya"><img class="nl3-naya-portrait" src="'+NAYA_IMAGE+'" alt="Naya — your AI guide" loading="lazy"><div class="nl3-naya-copy"><span class="nl3-kicker">NAYA · YOUR AI GUIDE</span><h3>I'm here to help you understand the result — not just display it.</h3><p>Your strongest signal is <strong>'+esc(strongest.name)+'</strong> at <strong>'+Math.round(strongest.score)+'</strong>. Your highest-leverage growth signal is <strong>'+esc(weakest.name)+'</strong> at <strong>'+Math.round(weakest.score)+'</strong>. The goal is not to judge you. It is to show you where focused improvement can create the greatest return.</p><span class="nl3-status"><i></i> '+data.band+' · '+Math.round(data.overall)+'/100</span></div></div><div class="nl3-gauges" aria-label="Your five MAXESS dimensions">'+gauges+'</div><div class="nl3-meaning"><h3>What your score means</h3><p>Your score is the starting point. Your pattern is the story. Your next move is where the value begins. Use the strongest capability as leverage, strengthen the biggest opportunity, and turn what works into a repeatable system.</p></div>';
    var anchor=root.querySelector('#your-fingerprint')||root.querySelector('.mx-insight')||root.querySelector('.mx-section:nth-of-type(2)');
    if(anchor)anchor.parentNode.insertBefore(sec,anchor);else root.appendChild(sec);
  }
  function missing(){
    hideOld();
    var old=root.querySelector('.nl3-missing');if(old)return;
    var sec=document.createElement('section');sec.className='mx-section';sec.innerHTML='<div class="nl3-missing"><h2>Your MAXESS result is not available yet.</h2><p>Complete the assessment and return with a valid MAXESS_RESULT payload. No score or personalization is invented here.</p></div>';
    var hero=root.querySelector('.mx-hero');if(hero)hero.parentNode.insertBefore(sec,hero.nextSibling);else root.prepend(sec);
  }
  function esc(v){return String(v).replace(/[&<>"']/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]})}
  function defaultInsight(n){var x=String(n).toLowerCase();if(x.indexOf('direction')>=0)return'How clearly you know what you want AI to accomplish.';if(x.indexOf('commun')>=0)return'How well you express context, intent, and the human outcome.';if(x.indexOf('evalu')>=0)return'How deliberately you judge whether AI work is actually good.';if(x.indexOf('iter')>=0)return'How consistently you refine useful work into something better.';return'How well you connect individual AI interactions into reusable systems.'}
  function init(){var data=read();root.setAttribute('data-naya-law-pass','3');if(!data){missing();return;}hero(data);report(data);root.querySelectorAll('.mx-score-orb').forEach(function(o){o.setAttribute('aria-label','MAXESS score '+Math.round(data.overall)+' out of 100')});}
  if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',init,{once:true});else init();
})();
</script>
'''.replace('__NAYA_IMAGE__',NAYA_IMAGE)


def patch(path: Path):
    text=path.read_text(encoding='utf-8')
    if MARK in text:
        return False
    if 'MAXESS-MASTER-BASELINE-PRESERVATION-10-10' not in text:
        raise RuntimeError(f'preservation baseline missing: {path}')
    if 'window.MAXESS_RESULT' not in text:
        raise RuntimeError(f'MAXESS_RESULT contract missing: {path}')
    block=f'\n<style id="{MARK}-css">{CSS}</style>\n{JS}\n<!-- {MARK} -->\n'
    insert_at=text.lower().rfind('</body>')
    if insert_at < 0:
        text += block
    else:
        text=text[:insert_at]+block+text[insert_at:]
    path.write_text(text,encoding='utf-8')
    return True

changed=[]
for name in FILES:
    p=Path(name)
    if not p.exists(): raise RuntimeError(f'missing artifact: {name}')
    if patch(p): changed.append(name)
print(f'{MARK}: changed {len(changed)} artifacts')
if len(changed)!=len(FILES):
    raise RuntimeError('zero-change or partial-change gate failed')
