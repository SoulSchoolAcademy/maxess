from pathlib import Path

p = Path('MAXESS-RESULTS-10-GROOVE.html')
s = p.read_text(encoding='utf-8')

MARKER = '<!-- MAXESS_RESULTS_V18_PRESERVATION_EXECUTION -->'
if MARKER in s:
    raise SystemExit('V18 preservation layer already present')

layer = r'''<!-- MAXESS_RESULTS_V18_PRESERVATION_EXECUTION -->
<style id="maxess-results-v18-preservation-css">
#maxess-results-10.v18-preservation{--v18-purple:#9b63ff;--v18-violet:#d8c0ff;--v18-cyan:#55e6ff;--v18-white:#fff;--v18-soft:rgba(255,255,255,.72);--v18-line:rgba(255,255,255,.13);background:#030305!important;color:#fff!important;overflow-x:hidden!important}
#maxess-results-10.v18-preservation .v18-flow{display:flex!important;flex-direction:column!important;width:100%!important}
#maxess-results-10.v18-preservation .v18-flow>*{order:initial!important}
#maxess-results-10.v18-preservation .v18-naya-top{order:1!important;position:relative;width:100%;padding:28px 18px 22px;text-align:center;background:radial-gradient(circle at 50% 0,rgba(155,99,255,.20),transparent 58%),linear-gradient(180deg,#10071a,#050308);border-bottom:1px solid rgba(255,255,255,.08);z-index:5}
#maxess-results-10.v18-preservation .v18-naya-inner{width:min(900px,100%);margin:auto;display:flex;flex-direction:column;align-items:center;gap:11px}
#maxess-results-10.v18-preservation .v18-naya-avatar{width:76px;height:76px;border-radius:50%;object-fit:cover;border:2px solid rgba(255,255,255,.70);box-shadow:0 0 0 6px rgba(155,99,255,.08),0 16px 38px rgba(0,0,0,.30)}
#maxess-results-10.v18-preservation .v18-naya-kicker{font-size:10px;font-weight:950;letter-spacing:.20em;color:#cdb5ff;text-transform:uppercase}
#maxess-results-10.v18-preservation .v18-naya-title{margin:0;color:#fff;font-size:clamp(25px,3.6vw,43px);line-height:1.02;letter-spacing:-.045em;font-weight:850}
#maxess-results-10.v18-preservation .v18-naya-copy{margin:0;max-width:700px;color:rgba(255,255,255,.70);font-size:clamp(14px,1.4vw,17px);line-height:1.5}
#maxess-results-10.v18-preservation .v18-naya-copy strong{color:#fff}
#maxess-results-10.v18-preservation .v18-listen{min-height:48px;padding:0 22px;border-radius:999px;border:1px solid rgba(255,255,255,.25);background:linear-gradient(135deg,#d8b8ff,#7540d2 55%,#35105f);color:#fff;font:inherit;font-weight:900;cursor:pointer;box-shadow:0 14px 35px rgba(86,35,153,.30),inset 0 1px rgba(255,255,255,.55)}
#maxess-results-10.v18-preservation .v18-score-section{order:2!important;position:relative;display:flex!important;flex-direction:column!important;align-items:center!important;justify-content:center!important;text-align:center!important;min-height:min(760px,82vh)!important;padding:48px 18px 58px!important;background:radial-gradient(circle at 50% 45%,rgba(85,230,255,.045),rgba(155,99,255,.15) 22%,transparent 48%),linear-gradient(180deg,#050308,#020204)!important}
#maxess-results-10.v18-preservation .v18-score-section .mx-hero-grid{display:flex!important;flex-direction:column!important;align-items:center!important;gap:18px!important;width:min(1000px,100%)!important;text-align:center!important}
#maxess-results-10.v18-preservation .v18-score-section .mx-hero-grid>div:first-child{display:flex!important;flex-direction:column!important;align-items:center!important;width:100%!important;max-width:900px!important;order:2!important}
#maxess-results-10.v18-preservation .v18-score-section .v13-score-orb{order:1!important;width:min(520px,76vw)!important;min-width:280px!important;margin:0 auto!important}
#maxess-results-10.v18-preservation .v18-score-label{display:block!important;margin:0;color:#fff!important;font-size:clamp(18px,2vw,26px)!important;font-weight:950!important;letter-spacing:.22em!important;text-transform:uppercase!important}
#maxess-results-10.v18-preservation .v18-score-section .v13-score-label{display:none!important}
#maxess-results-10.v18-preservation .v18-score-section .v13-score-number,#maxess-results-10.v18-preservation .v18-score-section .v13-score-caption,#maxess-results-10.v18-preservation .v18-score-section .v13-band{display:none!important}
#maxess-results-10.v18-preservation .v18-score-section .v13-score-orb .v13-score-number{display:block!important}
#maxess-results-10.v18-preservation .v18-score-section .v13-score-orb{background:radial-gradient(circle at 31% 23%,rgba(255,255,255,.28),rgba(57,223,145,.16) 20%,rgba(76,157,255,.09) 40%,#07060b 73%,#020205 100%)!important;border:1px solid rgba(196,181,253,.38)!important;box-shadow:0 0 0 1px rgba(255,255,255,.15),inset 0 0 100px rgba(57,223,145,.18),0 40px 115px rgba(0,0,0,.70),0 0 135px rgba(155,99,255,.20)!important}
#maxess-results-10.v18-preservation .v18-score-section .v13-score-orb::before{border-color:rgba(85,230,255,.42)!important;box-shadow:0 0 55px rgba(85,230,255,.14)!important}
#maxess-results-10.v18-preservation .v18-score-section .v13-score-orb::after{border-color:rgba(57,223,145,.22)!important}
#maxess-results-10.v18-preservation .v18-score-section .v13-score-orb .v13-score-number{font-size:clamp(100px,13vw,178px)!important;line-height:.78!important;background:linear-gradient(110deg,#39df91,#55e6ff,#9b63ff)!important;-webkit-background-clip:text!important;background-clip:text!important;color:transparent!important}
#maxess-results-10.v18-preservation .v18-dim-section{order:3!important;padding:58px clamp(16px,4vw,72px)!important;background:#fff!important;color:#0b0b10!important}
#maxess-results-10.v18-preservation .v18-dim-section .v18-section-head{width:min(1400px,100%);margin:0 auto 28px;display:flex;align-items:end;justify-content:space-between;gap:30px}
#maxess-results-10.v18-preservation .v18-dim-section h2{margin:0;color:#0b0b10;font-size:clamp(34px,5vw,68px);line-height:.94;letter-spacing:-.055em}
#maxess-results-10.v18-preservation .v18-dim-section p{max-width:620px;margin:0;color:#3d3d45;font-size:15px;line-height:1.6}
#maxess-results-10.v18-preservation .v18-orbs{display:grid!important;grid-template-columns:repeat(5,minmax(130px,1fr));gap:18px;width:min(1400px,100%);margin:auto}
#maxess-results-10.v18-preservation .v18-dim-orb{position:relative;min-width:0;aspect-ratio:1;border-radius:50%;border:1px solid rgba(0,0,0,.13);background:radial-gradient(circle at 34% 25%,#fff,#f4effb 42%,#ddd5e8 100%);color:#111;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;cursor:pointer;box-shadow:inset 0 1px rgba(255,255,255,.95),0 22px 55px rgba(24,12,38,.12);transition:transform .25s ease,box-shadow .25s ease,border-color .25s ease}
#maxess-results-10.v18-preservation .v18-dim-orb:hover,#maxess-results-10.v18-preservation .v18-dim-orb:focus-visible{transform:translateY(-7px) scale(1.025);border-color:rgba(115,61,190,.42);box-shadow:inset 0 1px rgba(255,255,255,.95),0 30px 70px rgba(24,12,38,.18),0 0 35px rgba(155,99,255,.12);outline:none}
#maxess-results-10.v18-preservation .v18-dim-orb::before{content:"";position:absolute;inset:9%;border-radius:50%;border:1px solid color-mix(in srgb,var(--dim-color) 45%,#fff 25%);pointer-events:none}
#maxess-results-10.v18-preservation .v18-dim-score{font-size:clamp(34px,4vw,54px);line-height:1;font-weight:950;color:var(--dim-color)}
#maxess-results-10.v18-preservation .v18-dim-name{margin-top:8px;max-width:105px;font-size:11px;line-height:1.2;font-weight:900;letter-spacing:.06em;text-transform:uppercase}
#maxess-results-10.v18-preservation .v18-dim-detail{width:min(1400px,100%);margin:24px auto 0;padding:22px 24px;border-radius:20px;background:#f5f3f8;border:1px solid rgba(0,0,0,.08);color:#111;min-height:86px}
#maxess-results-10.v18-preservation .v18-dim-detail b{color:#6637a8;font-size:10px;letter-spacing:.15em;text-transform:uppercase}
#maxess-results-10.v18-preservation .v18-dim-detail p{margin:7px 0 0;color:#333;font-size:14px}
#maxess-results-10.v18-preservation .v18-existing-section{order:4!important}
#maxess-results-10.v18-preservation .v18-hidden{display:none!important}
#maxess-results-10.v18-preservation .v13-shell>.v18-flow{margin:0!important}
#maxess-results-10.v18-preservation .v18-flow .v13-report,#maxess-results-10.v18-preservation .v18-flow .v13-dimensions,#maxess-results-10.v18-preservation .v18-flow .v13-pattern,#maxess-results-10.v18-preservation .v18-flow .v13-strengths,#maxess-results-10.v18-preservation .v18-flow .v13-lever,#maxess-results-10.v18-preservation .v18-flow .v13-next,#maxess-results-10.v18-preservation .v18-flow .v13-masters,#maxess-results-10.v18-preservation .v18-flow .v13-video,#maxess-results-10.v18-preservation .v18-flow .v13-final{width:100%!important}
#maxess-results-10.v18-preservation .v13-report{order:4!important}
#maxess-results-10.v18-preservation .v13-pattern{order:5!important}
#maxess-results-10.v18-preservation .v13-strengths{order:6!important}
#maxess-results-10.v18-preservation .v13-lever{order:7!important}
#maxess-results-10.v18-preservation .v13-next{order:8!important}
#maxess-results-10.v18-preservation .v13-masters{order:9!important}
#maxess-results-10.v18-preservation .v13-video{order:10!important}
#maxess-results-10.v18-preservation .v13-playground,#maxess-results-10.v18-preservation #naya-playground{order:11!important}
#maxess-results-10.v18-preservation .v13-final{order:12!important}
#maxess-results-10.v18-preservation .v18-listen-secondary,#maxess-results-10.v18-preservation #mx-naya-listen,#maxess-results-10.v18-preservation #v11-naya-listen,#maxess-results-10.v18-preservation #v13-listen{display:none!important}
@media(max-width:950px){#maxess-results-10.v18-preservation .v18-orbs{grid-template-columns:repeat(3,minmax(130px,1fr))}#maxess-results-10.v18-preservation .v18-dim-section .v18-section-head{display:block}#maxess-results-10.v18-preservation .v18-dim-section p{margin-top:14px}}
@media(max-width:620px){#maxess-results-10.v18-preservation .v18-score-section{min-height:auto!important;padding:38px 14px 48px!important}#maxess-results-10.v18-preservation .v18-score-section .v13-score-orb{width:min(390px,86vw)!important;min-width:260px!important}#maxess-results-10.v18-preservation .v18-orbs{grid-template-columns:repeat(2,minmax(120px,1fr));gap:12px}#maxess-results-10.v18-preservation .v18-dim-orb{min-height:0}#maxess-results-10.v18-preservation .v18-dim-name{font-size:10px}}
@media(max-width:390px){#maxess-results-10.v18-preservation .v18-orbs{grid-template-columns:1fr}#maxess-results-10.v18-preservation .v18-dim-orb{width:min(220px,76vw);margin:auto}}
@media(prefers-reduced-motion:reduce){#maxess-results-10.v18-preservation .v18-dim-orb{transition:none}}
</style>
<script id="maxess-results-v18-preservation-js">
(function(){
'use strict';
function boot(){
 var root=document.getElementById('maxess-results-10');if(!root||root.dataset.v18Preservation==='1')return;
 root.dataset.v18Preservation='1';root.classList.add('v18-preservation');
 var result=window.MAXESS_RESULT||{};
 var score=Number(result.overallScore!=null?result.overallScore:result.score);
 if(!Number.isFinite(score))score=0;score=Math.round(Math.max(0,Math.min(100,score)));
 var dims=Array.isArray(result.dimensions)?result.dimensions.slice(0,5):[];
 var shell=root.querySelector('.v13-shell')||root;
 function first(selectors,scope){scope=scope||shell;for(var i=0;i<selectors.length;i++){var e=scope.querySelector(selectors[i]);if(e)return e}return null}
 function directSection(selector){var e=shell.querySelector(selector);if(!e)return null;return e}
 function removeBy(selectors){selectors.forEach(function(sel){root.querySelectorAll(sel).forEach(function(e){if(!e.closest('.v18-naya-top'))e.remove()})})}
 removeBy(['#v13-naya','#v12-naya','#v11-naya-report','#v11-naya-welcome','#v13-naya-introduction','.v11-naya-welcome','.v12-naya-intro']);
 var oldFlow=shell.querySelector('.v18-flow');if(oldFlow)oldFlow.remove();
 var flow=document.createElement('div');flow.className='v18-flow';shell.appendChild(flow);
 var hero=first(['#v13-score','#v13-hero','.v13-hero']);
 if(!hero)hero=first(['.v13-hero']);
 var scoreSection=hero;
 if(scoreSection){scoreSection.classList.add('v18-score-section');var title=first(['.v13-score-label','.v13-score-value','.v13-score-caption'],scoreSection);var oldCopy=scoreSection.querySelector('.v13-hero-copy');if(oldCopy)oldCopy.classList.add('v18-hidden');var orb=scoreSection.querySelector('.v13-score-orb');if(orb){var sn=orb.querySelector('.v13-score-number');if(sn)sn.textContent=String(score);var label=scoreSection.querySelector('.v13-score-label');if(label)label.textContent='YOUR AI SCORE';var oldBand=orb.querySelector('.v13-band');if(oldBand)oldBand.remove();}var existingGrid=scoreSection.querySelector('.v13-hero-inner')||scoreSection.querySelector('.mx-hero-grid');if(existingGrid){var labelEl=existingGrid.querySelector('.v13-score-label');if(!labelEl){labelEl=document.createElement('div');labelEl.className='v18-score-label';labelEl.textContent='YOUR AI SCORE';existingGrid.insertBefore(labelEl,existingGrid.firstChild)}existingGrid.querySelectorAll('.v13-score-value,.v13-score-caption,.v13-overline,.v13-band,.v13-hero-actions').forEach(function(e){e.classList.add('v18-hidden')})}}
 var naya=document.createElement('section');naya.className='v18-naya-top';naya.innerHTML='<div class="v18-naya-inner"><img class="v18-naya-avatar" src="https://raw.githubusercontent.com/SoulSchoolAcademy/maxess/main/Naya%20Profile%20Black.jpg" alt="Naya, your AI guide"><div class="v18-naya-kicker">NAYA · YOUR GUIDE</div><h2 class="v18-naya-title">Hi. I’ve looked at your results.</h2><p class="v18-naya-copy">This isn’t your judgment. <strong>It’s your map.</strong> I’m here to help you understand what you already do well, where your biggest opportunity is, and what to do next.</p><button class="v18-listen" type="button" aria-label="Listen to Naya walk through your MAXESS results">Listen to Naya <span aria-hidden="true">▶</span></button></div>';
 naya.querySelector('.v18-listen').addEventListener('click',function(){var candidates=root.querySelectorAll('#mx-naya-listen,#v11-naya-listen,#v13-listen,.mx-naya-listen');for(var i=0;i<candidates.length;i++){if(candidates[i].style.display!=='none'){candidates[i].click();return}}root.dispatchEvent(new CustomEvent('maxess:naya-listen',{bubbles:true,detail:{result:window.MAXESS_RESULT||null}}));});
 flow.appendChild(naya);
 if(scoreSection)flow.appendChild(scoreSection);
 var dimSection=first(['#v13-dimensions','#v12-dimensions','.v13-dimensions']);
 if(dimSection){var wrapper=document.createElement('section');wrapper.className='v18-dim-section';wrapper.innerHTML='<div class="v18-section-head"><div><span style="display:block;color:#6637a8;font-size:10px;font-weight:950;letter-spacing:.18em;text-transform:uppercase">YOUR FIVE DIMENSIONS</span><h2>See the shape of your capability.</h2></div><p>These are the five real dimensions from your MAXESS result. Tap one to explore what it means and where its leverage lives.</p></div><div class="v18-orbs" role="list" aria-label="Your five MAXESS dimensions"></div><div class="v18-dim-detail" id="v18-dimension-detail"><b>SELECT A DIMENSION</b><p>Choose one of the five orbs to see its score, meaning, and next lever.</p></div>';
 var grid=wrapper.querySelector('.v18-orbs');
 var sourceCards=Array.prototype.slice.call(dimSection.querySelectorAll('.v13-dim,.v15-dim,.mx-dim')).slice(0,5);
 for(var i=0;i<5;i++){var d=dims[i]||{};var card=sourceCards[i];var name=d.name||(card&&card.querySelector('h3,.v15-dim-name')?.textContent)||['Direction','Communication','Evaluation','Iteration','Systems Thinking'][i];var v=Number(d.score);if(!Number.isFinite(v))v=Number(card&&card.getAttribute('data-score'))||0;v=Math.round(Math.max(0,Math.min(100,v)));var btn=document.createElement('button');btn.type='button';btn.className='v18-dim-orb';btn.style.setProperty('--dim-color',['#ff9d3d','#ffd84a','#39df91','#4c9dff','#965dff'][i]);btn.setAttribute('role','listitem');btn.setAttribute('aria-label',name+' score '+v+' out of 100');btn.innerHTML='<span class="v18-dim-score">'+v+'</span><span class="v18-dim-name">'+name+'</span>';btn.addEventListener('click',(function(nm,sc,idx){return function(){var detail=wrapper.querySelector('#v18-dimension-detail');detail.innerHTML='<b>'+nm+' · '+sc+' / 100</b><p>'+dimensionCopy(nm,sc,idx)+'</p>';detail.scrollIntoView({behavior:'smooth',block:'nearest'});root.dispatchEvent(new CustomEvent('maxess:dimension',{bubbles:true,detail:{name:nm,score:sc,index:idx}}));}})(name,v,i));grid.appendChild(btn)}
 dimSection.classList.add('v18-hidden');flow.appendChild(wrapper);
 }
 var report=first(['#v13-report','#v12-report','#v11-naya-report']);if(report){report.classList.add('v18-existing-section');flow.appendChild(report)}
 var pattern=first(['#v15-pattern','#v13-pattern','#v12-pattern','#v11-pattern']);if(pattern){pattern.classList.add('v18-existing-section');flow.appendChild(pattern)}
 var strength=first(['#v13-strengths','#v11-strengths','#v12-strengths']);if(strength){strength.classList.add('v18-existing-section');flow.appendChild(strength)}
 var lever=first(['#v13-lever','#v11-lever','#v12-lever']);if(lever){lever.classList.add('v18-existing-section');flow.appendChild(lever)}
 var next=first(['#v13-next','#v11-next','#v12-next']);if(next){next.classList.add('v18-existing-section');flow.appendChild(next)}
 var masters=first(['#v13-masters','#v11-masters','#v12-masters']);if(masters){masters.classList.add('v18-existing-section');flow.appendChild(masters)}
 var video=first(['#v13-video','#v11-video','#v12-video']);if(video){video.classList.add('v18-existing-section');flow.appendChild(video)}
 var playground=root.querySelector('#naya-playground');if(playground){playground.classList.add('v18-existing-section');flow.appendChild(playground)}
 var final=first(['#v13-final','#v11-final','#v12-final']);if(final){final.classList.add('v18-existing-section');flow.appendChild(final)}
 root.querySelectorAll('#mx-naya-listen,#v11-naya-listen,#v13-listen').forEach(function(e){e.classList.add('v18-listen-secondary')});
 root.setAttribute('data-results-version','18-preservation');root.setAttribute('data-results-data-source','window.MAXESS_RESULT');root.setAttribute('data-v18-score',String(score));root.setAttribute('data-v18-dimension-count',String(dims.length));
 function dimensionCopy(name,sc,i){var n=String(name).toLowerCase();if(n.indexOf('communication')>=0)return'Your communication signal is '+sc+'. Use this strength to turn context, intent, and desired outcomes into reusable instructions and briefs.';if(n.indexOf('direction')>=0)return'Your direction signal is '+sc+'. Define the outcome and success test before asking AI to work.';if(n.indexOf('evaluation')>=0)return'Your evaluation signal is '+sc+'. Make judgment visible: score important AI output before accepting it.';if(n.indexOf('iteration')>=0)return'Your iteration signal is '+sc+'. Build the habit of create → score → improve → repeat.';if(n.indexOf('system')>=0)return'Your systems signal is '+sc+'. Turn one repeated workflow into a reusable system instead of solving it from scratch each time.';return'Your '+name+' signal is '+sc+'. Use this dimension as a focused area for your next improvement.'}
}
if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',function(){setTimeout(boot,350)},{once:true});else setTimeout(boot,350);
})();
</script>
'''

body = s.lower().rfind('</body>')
if body < 0:
    raise SystemExit('No closing body tag')
s = s[:body] + layer + '\n' + s[body:]
p.write_text(s, encoding='utf-8')
print('MAXESS V18 preservation layer appended to canonical Groove source')
