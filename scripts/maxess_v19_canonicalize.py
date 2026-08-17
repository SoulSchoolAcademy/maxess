from pathlib import Path

p=Path('MAXESS-RESULTS-10-GROOVE.html')
s=p.read_text(encoding='utf-8')
MARK='<!-- MAXESS_RESULTS_V19_CANONICAL_HIERARCHY -->'
if MARK in s:
    raise SystemExit('V19 already present')
layer=r'''<!-- MAXESS_RESULTS_V19_CANONICAL_HIERARCHY -->
<style id="maxess-results-v19-css">
#maxess-results-10.v19-canonical .v19-stage{display:flex!important;flex-direction:column!important;width:100%!important}
#maxess-results-10.v19-canonical .v19-naya{order:1!important;display:flex!important;flex-direction:column!important;align-items:center!important;text-align:center!important;padding:42px 18px 30px!important;background:radial-gradient(circle at 50% 0,rgba(166,108,255,.24),transparent 62%),#07050a!important}
#maxess-results-10.v19-canonical .v19-naya h1{margin:10px 0 0!important;font-size:clamp(30px,4.5vw,56px)!important;line-height:1!important;letter-spacing:-.05em!important;color:#fff!important}
#maxess-results-10.v19-canonical .v19-naya p{max-width:700px!important;margin:14px auto 0!important;color:rgba(255,255,255,.72)!important;font-size:clamp(15px,1.5vw,19px)!important}
#maxess-results-10.v19-canonical .v19-naya button{margin-top:20px!important;min-height:52px!important;padding:0 25px!important;border-radius:999px!important;border:1px solid rgba(255,255,255,.25)!important;background:linear-gradient(135deg,#d8b8ff,#7540d2 55%,#35105f)!important;color:#fff!important;font-weight:900!important;cursor:pointer!important}
#maxess-results-10.v19-canonical .v19-score{order:2!important;display:flex!important;flex-direction:column!important;align-items:center!important;text-align:center!important;padding:30px 16px 62px!important;background:#030305!important}
#maxess-results-10.v19-canonical .v19-score-label{order:1!important;margin-bottom:18px!important;color:#fff!important;font-size:clamp(15px,2vw,24px)!important;font-weight:950!important;letter-spacing:.22em!important;text-transform:uppercase!important}
#maxess-results-10.v19-canonical .v19-score .v13-score-orb{order:2!important;width:min(540px,80vw)!important;margin:0 auto!important}
#maxess-results-10.v19-canonical .v19-score-copy{order:3!important;max-width:650px!important;margin:22px auto 0!important;color:rgba(255,255,255,.62)!important;font-size:14px!important}
#maxess-results-10.v19-canonical .v19-dims{order:3!important;padding:58px clamp(16px,4vw,72px)!important;background:#fff!important;color:#111!important}
#maxess-results-10.v19-canonical .v19-dims h2{margin:0!important;font-size:clamp(34px,5vw,68px)!important;line-height:.94!important;letter-spacing:-.055em!important}
#maxess-results-10.v19-canonical .v19-dim-orbs{display:grid!important;grid-template-columns:repeat(5,minmax(120px,1fr))!important;gap:18px!important;max-width:1400px!important;margin:30px auto 0!important}
#maxess-results-10.v19-canonical .v19-dim-orb{aspect-ratio:1!important;border-radius:50%!important;display:flex!important;flex-direction:column!important;align-items:center!important;justify-content:center!important;text-align:center!important;cursor:pointer!important;background:radial-gradient(circle at 34% 25%,#fff,#f3edf9 45%,#ddd4e7)!important;border:1px solid rgba(0,0,0,.13)!important;box-shadow:0 22px 55px rgba(24,12,38,.12)!important;transition:transform .2s ease!important}
#maxess-results-10.v19-canonical .v19-dim-orb:hover{transform:translateY(-6px) scale(1.02)!important}
#maxess-results-10.v19-canonical .v19-dim-orb strong{font-size:clamp(34px,4vw,56px)!important;line-height:1!important}
#maxess-results-10.v19-canonical .v19-dim-orb span{max-width:105px!important;margin-top:8px!important;font-size:10px!important;font-weight:900!important;text-transform:uppercase!important;letter-spacing:.06em!important;color:#111!important}
#maxess-results-10.v19-canonical .v19-detail{max-width:1400px!important;margin:22px auto 0!important;padding:20px 22px!important;border-radius:18px!important;background:#f5f3f8!important;border:1px solid rgba(0,0,0,.08)!important}
#maxess-results-10.v19-canonical .v19-detail p{margin:6px 0 0!important;color:#333!important}
#maxess-results-10.v19-canonical .v19-old-hero-copy{display:none!important}
@media(max-width:900px){#maxess-results-10.v19-canonical .v19-dim-orbs{grid-template-columns:repeat(3,minmax(120px,1fr))!important}}
@media(max-width:620px){#maxess-results-10.v19-canonical .v19-dim-orbs{grid-template-columns:repeat(2,minmax(120px,1fr))!important;gap:12px!important}}
@media(max-width:390px){#maxess-results-10.v19-canonical .v19-dim-orbs{grid-template-columns:1fr!important}.v19-canonical .v19-dim-orb{width:min(220px,76vw)!important;margin:auto!important}}
</style>
<script id="maxess-results-v19-js">
(function(){
'use strict';
function boot(){
 var root=document.getElementById('maxess-results-10'); if(!root||root.dataset.v19Canonical==='1')return;
 root.dataset.v19Canonical='1'; root.classList.add('v19-canonical');
 var result=window.MAXESS_RESULT||{};
 var dims=Array.isArray(result.dimensions)?result.dimensions.slice(0,5):[];
 var score=Number(result.overallScore!=null?result.overallScore:result.score); if(!Number.isFinite(score))score=0; score=Math.round(Math.max(0,Math.min(100,score)));
 var shell=root.querySelector('.v13-shell')||root;
 var stage=shell.querySelector('.v18-flow');
 if(!stage){stage=document.createElement('div');stage.className='v19-stage';shell.appendChild(stage)} else {stage.classList.add('v19-stage')}
 function find(sel){return root.querySelector(sel)}
 var existingNaya=stage.querySelector('.v18-naya-top');
 if(!existingNaya){
  existingNaya=document.createElement('section'); existingNaya.className='v19-naya';
  existingNaya.innerHTML='<div class="v18-naya-inner"><img class="v18-naya-avatar" src="https://raw.githubusercontent.com/SoulSchoolAcademy/maxess/main/Naya%20Profile%20Black.jpg" alt="Naya, your AI guide"><div class="v18-naya-kicker">NAYA · YOUR GUIDE</div><h1>Hi. I’ve looked at your results.</h1><p>This isn’t your judgment. <strong>It’s your map.</strong></p><button type="button" class="v19-listen">Listen to Naya <span aria-hidden="true">▶</span></button></div>';
  stage.prepend(existingNaya);
 } else { existingNaya.classList.add('v19-naya'); existingNaya.querySelector('.v18-naya-title')?.replaceWith(Object.assign(document.createElement('h1'),{className:'v19-title',textContent:'Hi. I’ve looked at your results.'})); var cp=existingNaya.querySelector('.v18-naya-copy'); if(cp)cp.innerHTML='This isn’t your judgment. <strong>It’s your map.</strong>'; }
 var listen=existingNaya.querySelector('.v19-listen')||existingNaya.querySelector('.v18-listen');
 if(listen&&!listen.dataset.bound){listen.dataset.bound='1';listen.addEventListener('click',function(){var c=[...root.querySelectorAll('#mx-naya-listen,#v11-naya-listen,#v13-listen,.mx-naya-listen')].find(e=>getComputedStyle(e).display!=='none');if(c)c.click();else root.dispatchEvent(new CustomEvent('maxess:naya-listen',{bubbles:true,detail:{result:window.MAXESS_RESULT||null}}));});}
 var scoreSec=stage.querySelector('.v18-score-section')||find('#v13-score')||find('#v13-hero')||find('.v13-hero');
 if(scoreSec){scoreSec.classList.add('v19-score'); var orb=scoreSec.querySelector('.v13-score-orb'); if(orb){var n=orb.querySelector('.v13-score-number');if(n)n.textContent=String(score);} var lbl=scoreSec.querySelector('.v18-score-label')||scoreSec.querySelector('.v13-score-label');if(lbl){lbl.textContent='YOUR AI SCORE';lbl.classList.add('v19-score-label');}else{var l=document.createElement('div');l.className='v19-score-label';l.textContent='YOUR AI SCORE';scoreSec.prepend(l);} }
 var dimSec=stage.querySelector('.v18-dim-section');
 if(dimSec){dimSec.classList.add('v19-dims'); var old=dimSec.querySelector('.v18-section-head'); if(old){var h=old.querySelector('h2');if(h)h.textContent='Your five dimensions.';} var orbs=dimSec.querySelector('.v18-orbs'); if(orbs){orbs.classList.add('v19-dim-orbs');[...orbs.querySelectorAll('.v18-dim-orb')].forEach((o,i)=>o.classList.add('v19-dim-orb'));} }
 // Guarantee downstream order inside the existing stage without deleting content.
 var selectors=['.v13-report','.v13-pattern','.v13-strengths','.v18-strength-section','.v13-lever','.v13-next','.v13-masters','.v13-playground','#naya-playground','.v13-video','.v13-final'];
 selectors.forEach(function(sel){var e=stage.querySelector(sel);if(e)e.style.order=String(4+selectors.indexOf(sel));});
 // Hide every competing old hero narrative while retaining its data-bearing orb.
 root.querySelectorAll('.mx-hero-copy,.v13-hero-copy,.v13-overline,.v13-hero-actions').forEach(function(e){e.classList.add('v19-old-hero-copy')});
 // Hide secondary listen controls; the canonical Naya button is the only visible one.
 root.querySelectorAll('#mx-naya-listen,#v11-naya-listen,#v13-listen,.mx-naya-listen,.v18-listen-secondary').forEach(function(e){if(e!==listen)e.style.display='none';});
}
if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',boot);else boot();
window.addEventListener('maxess:profile-ready',boot);
})();
</script>
'''
idx=s.rfind('</html>')
if idx<0: raise SystemExit('No closing html tag')
s=s[:idx]+layer+'\n'+s[idx:]
p.write_text(s,encoding='utf-8')
print('V19 canonical hierarchy appended:',len(s),'bytes')
