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
#maxess-results-10.v19-canonical .v19-naya .v18-naya-avatar{width:88px!important;height:88px!important;object-fit:cover!important;border-radius:50%!important;display:block!important}
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
 if(!stage){stage=document.createElement('div');stage.className='v19-stage';shell.appendChild(stage)} else stage.classList.add('v19-stage');
 function visible(e){return e&&getComputedStyle(e).display!=='none'&&e.getBoundingClientRect().height>0;}
 function headingMatch(re){
  var nodes=[...root.querySelectorAll('section,article,div')];
  return nodes.find(function(e){var h=e.querySelector('h1,h2,h3,.section-title,.eyebrow');return h&&re.test((h.textContent||'').trim())&&e.getBoundingClientRect().height>20;});
 }
 function findAny(sels){for(var i=0;i<sels.length;i++){var e=root.querySelector(sels[i]);if(e)return e;}return null;}
 function move(e,order){if(e&&e!==stage){e.style.order=String(order);if(e.parentElement!==stage)stage.appendChild(e);}}
 var naya=stage.querySelector('.v18-naya-top,.v19-naya');
 if(!naya){
  naya=document.createElement('section');naya.className='v19-naya';
  naya.innerHTML='<img class="v18-naya-avatar" src="https://raw.githubusercontent.com/SoulSchoolAcademy/maxess/main/Naya%20Profile%20Black.jpg" alt="Naya, your AI guide"><div class="v18-naya-kicker">NAYA · YOUR GUIDE</div><h1>Hi. I’ve looked at your results.</h1><p>This isn’t your judgment. <strong>It’s your map.</strong></p><button type="button" class="v19-listen">Listen to Naya <span aria-hidden="true">▶</span></button>';
  stage.prepend(naya);
 } else {
  naya.classList.add('v19-naya');
  var oldTitle=naya.querySelector('h1');if(oldTitle)oldTitle.textContent='Hi. I’ve looked at your results.';
  var oldCopy=naya.querySelector('p');if(oldCopy)oldCopy.innerHTML='This isn’t your judgment. <strong>It’s your map.</strong>';
 }
 naya.style.order='1';
 var listen=naya.querySelector('.v19-listen');
 if(!listen){listen=document.createElement('button');listen.type='button';listen.className='v19-listen';listen.innerHTML='Listen to Naya <span aria-hidden="true">▶</span>';naya.appendChild(listen);}
 if(!listen.dataset.bound){listen.dataset.bound='1';listen.addEventListener('click',function(){var c=[...root.querySelectorAll('#mx-naya-listen,#v11-naya-listen,#v13-listen,.mx-naya-listen')].find(visible);if(c)c.click();else root.dispatchEvent(new CustomEvent('maxess:naya-listen',{bubbles:true,detail:{result:window.MAXESS_RESULT||null}}));});}
 var scoreSec=findAny(['.v18-score-section','#v13-score','.v13-score-section','.v13-hero']);
 var orb=findAny(['.v13-score-orb']);
 if(!scoreSec&&orb){scoreSec=orb.closest('section,article')||orb.parentElement;}
 if(scoreSec){
  scoreSec.classList.add('v19-score');move(scoreSec,2);
  var n=scoreSec.querySelector('.v13-score-number');if(n)n.textContent=String(score);
  var lbl=scoreSec.querySelector('.v18-score-label,.v13-score-label,.v19-score-label');
  if(!lbl){lbl=document.createElement('div');scoreSec.prepend(lbl);}lbl.textContent='YOUR AI SCORE';lbl.classList.add('v19-score-label');
 }
 var dimSec=findAny(['.v18-dim-section','.v18-dimensions','.v13-dimensions','.v13-fingerprint']);
 if(!dimSec){dimSec=document.createElement('section');dimSec.className='v19-dims';}
 else dimSec.classList.add('v19-dims');
 var h=dimSec.querySelector('h2');
 if(!h){h=document.createElement('h2');dimSec.prepend(h);}h.textContent='Your five dimensions.';
 var grid=dimSec.querySelector('.v19-dim-orbs');
 if(!grid){grid=document.createElement('div');grid.className='v19-dim-orbs';dimSec.appendChild(grid);}
 grid.innerHTML='';
 dims.forEach(function(d,i){
  var o=document.createElement('button');o.type='button';o.className='v19-dim-orb';o.dataset.index=String(i);o.setAttribute('aria-label',d.name+' '+Math.round(Number(d.score)||0));
  o.innerHTML='<strong>'+Math.round(Number(d.score)||0)+'</strong><span>'+String(d.name||('Dimension '+(i+1)))+'</span>';
  o.addEventListener('click',function(){var targets=[...root.querySelectorAll('section,article,div')].filter(function(e){return e!==dimSec&&new RegExp(String(d.name||'').replace(/[.*+?^${}()|[\]\\]/g,'\\$&'),'i').test(e.textContent||'')&&e.getBoundingClientRect().height>80;});if(targets[0])targets[0].scrollIntoView({behavior:'smooth',block:'center'});});
  grid.appendChild(o);
 });
 move(dimSec,3);
 var report=findAny(['.v13-report'])||headingMatch(/report/i);move(report,4);
 var pattern=findAny(['.v13-pattern'])||headingMatch(/pattern|fingerprint/i);move(pattern,5);
 var strength=findAny(['.v13-strengths','.v18-strength-section'])||headingMatch(/strength|advantage/i);move(strength,6);
 var lever=findAny(['.v13-lever','.v18-lever'])||headingMatch(/biggest lever|your lever|lever/i);move(lever,7);
 var next=findAny(['.v13-next'])||headingMatch(/next move|next chapter/i);move(next,8);
 var masters=findAny(['.v13-masters'])||headingMatch(/18 (naya )?masters|18 ai pathways|pathways/i);move(masters,9);
 var playground=findAny(['.v13-playground','#naya-playground'])||headingMatch(/playground/i);move(playground,10);
 root.querySelectorAll('.mx-hero-copy,.v13-hero-copy,.v13-overline,.v13-hero-actions').forEach(function(e){e.classList.add('v19-old-hero-copy');});
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
print('V19 canonical hierarchy rebuilt:',len(s),'bytes')
