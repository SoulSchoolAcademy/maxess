from pathlib import Path

p=Path('MAXESS-RESULTS-10-GROOVE.html')
s=p.read_text(encoding='utf-8')
marker='MAXESS_RESULTS_V17_BROWSER_REPAIR'
if marker in s:
    raise SystemExit('V17 browser repair already present')
layer=r'''<!-- MAXESS_RESULTS_V17_BROWSER_REPAIR -->
<script id="MAXESS_RESULTS_V17_BROWSER_REPAIR">
(function(){
'use strict';
function run(){
 var root=document.getElementById('maxess-results-10');if(!root)return;
 function pull(sel,cls){var e=root.querySelector(sel);if(!e)return null;e.classList.add(cls);root.appendChild(e);return e}
 var naya=pull('#v13-naya-introduction','v17-naya-top')||pull('.v17-naya-banner','v17-naya-top')||pull('#naya-report','v17-naya-top');
 var hero=pull('#v13-hero','v17-hero')||pull('.mx-hero','v17-hero');
 var dims=pull('#v13-dimensions','v17-dims');
 var pattern=pull('#v15-pattern','v17-pattern')||pull('#your-fingerprint','v17-pattern');
 var meaning=pull('#v13-report','v17-meaning');
 var strength=pull('#v13-strengths','v17-strength');
 var lever=pull('#v13-lever','v17-lever');
 var action=pull('#v13-next','v17-action');
 var video=pull('#v13-video','v17-video');
 var masters=pull('#v13-masters','v17-masters');
 var playground=pull('#naya-playground','v17-playground');
 var tech=pull('#v13-final','v17-tech');
 if(naya){var title=naya.querySelector('.v13-naya-title,.v11-naya-title,.v17-naya-title');if(title)title.textContent='Hi. I’ve looked at your results.';var copy=naya.querySelector('.v13-naya-copy,.v11-naya-copy,.v17-naya-copy');if(copy)copy.innerHTML='This isn’t your judgment. <strong>It’s your map.</strong> I’m here to help you understand what you already do well, where your biggest opportunity is, and what to do next.';var inner=naya.querySelector('.v17-naya-inner')||naya;var b=inner.querySelector('.v17-naya-listen');if(!b){b=document.createElement('button');b.type='button';b.className='v17-naya-listen';b.textContent='Listen to Naya';b.setAttribute('aria-label','Listen to Naya walk through your MAXESS results');b.onclick=function(){var c=root.querySelectorAll('#v13-listen button,#mx-naya-listen,#mx-listen,.v17-listen button,[data-maxess-listen]');for(var i=0;i<c.length;i++){if(c[i]!==b){c[i].click();return}}root.dispatchEvent(new CustomEvent('maxess:naya-listen',{bubbles:true}))};inner.appendChild(b)}}
 var r=window.MAXESS_RESULT||{},score=Number(r.overallScore!=null?r.overallScore:r.score);if(Number.isFinite(score)){score=Math.round(Math.max(0,Math.min(100,score)));if(hero){var sn=hero.querySelectorAll('.mx-score strong');if(sn.length){sn[0].textContent=String(score);for(var q=1;q<sn.length;q++)sn[q].textContent=''}hero.querySelectorAll('.v13-score-label,.v13-score-value,.v13-score-caption').forEach(function(e){e.remove()})}}
 if(dims){var grid=dims.querySelector('.v17-orbs');if(!grid){grid=document.createElement('div');grid.className='v17-orbs';dims.appendChild(grid)}grid.innerHTML='';var ds=Array.isArray(r.dimensions)?r.dimensions:[],names=['Direction','Communication','Evaluation','Iteration','Systems Thinking'];for(var d=0;d<5;d++){var x=ds[d]||{},v=Number(x.score),name=x.name||names[d],c=document.createElement('div');c.className='v17-orb';c.setAttribute('role','listitem');c.setAttribute('aria-label',name+' score '+(Number.isFinite(v)?Math.round(v):'unavailable'));c.innerHTML='<div><div class="v17-orb-score">'+(Number.isFinite(v)?Math.round(v):'—')+'</div><div class="v17-orb-name">'+name+'</div></div>';grid.appendChild(c)}}
 root.querySelectorAll('#v18-'+'listen-static').forEach(function(e){e.remove()});
 root.setAttribute('data-results-version','17-final');root.setAttribute('data-results-data-source',Number.isFinite(score)?'window.MAXESS_RESULT':'unavailable');
}
if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',run,{once:true});else run();
})();
</script>
'''
body=s.lower().rfind('</body>')
if body<0:raise SystemExit('No body close')
p.write_text(s[:body]+layer+'\n'+s[body:],encoding='utf-8')
print('V17 browser repair appended — registered final verification trigger')
