from pathlib import Path

p = Path('MAXESS-RESULTS-10-GROOVE.html')
s = p.read_text(encoding='utf-8')

# MAXESS V17 deterministic execution: remove obsolete presentation tails before installing the clean final layer.
markers = [
    '<!-- MAXESS_RESULTS_V17_EXACT_EXECUTION -->',
    '<!-- MAXESS_RESULTS_V18_GROOVE_SAFE',
    '<!-- MAXESS_RESULTS_V19_EXACT_EXECUTION -->',
    '<!-- MAXESS_RESULTS_V19B_EXECUTION -->',
]
found = [s.find(m) for m in markers if s.find(m) >= 0]
if found:
    cut = min(found)
    body = s.lower().rfind('</body>')
    if body < cut:
        raise SystemExit('Invalid presentation-tail markers')
    s = s[:cut] + '\n' + s[body:]

layer = r'''<!-- MAXESS_RESULTS_V17_CLEAN_EXECUTION -->
<style id="maxess-results-v17-clean">
#maxess-results-10.v17-clean{display:flex!important;flex-direction:column!important;overflow-x:hidden!important}
#maxess-results-10.v17-clean>.v17-naya-top{order:1!important}
#maxess-results-10.v17-clean>.v17-hero{order:2!important}
#maxess-results-10.v17-clean>.v17-dims{order:3!important}
#maxess-results-10.v17-clean>.v17-pattern{order:5!important}
#maxess-results-10.v17-clean>.v17-meaning{order:6!important}
#maxess-results-10.v17-clean>.v17-strength{order:7!important}
#maxess-results-10.v17-clean>.v17-lever{order:8!important}
#maxess-results-10.v17-clean>.v17-action{order:9!important}
#maxess-results-10.v17-clean>.v17-video{order:10!important}
#maxess-results-10.v17-clean>.v17-masters{order:11!important}
#maxess-results-10.v17-clean>.v17-playground{order:12!important}
#maxess-results-10.v17-clean>.v17-tech{order:13!important}
#maxess-results-10 .v17-naya-top{position:relative;padding:30px 20px 22px;text-align:center;background:linear-gradient(180deg,#12071b,#08050d);z-index:2}
#maxess-results-10 .v17-naya-inner{width:min(920px,100%);margin:auto;display:flex;flex-direction:column;align-items:center;gap:12px}
#maxess-results-10 .v17-naya-avatar{width:76px;height:76px;border-radius:50%;object-fit:cover;display:block;box-shadow:0 0 0 2px rgba(255,255,255,.18),0 0 32px rgba(166,108,255,.28)}
#maxess-results-10 .v17-naya-kicker{font-size:10px;font-weight:900;letter-spacing:.2em;color:#d0a8ff;text-transform:uppercase}
#maxess-results-10 .v17-naya-title{margin:0;color:#fff;font-size:clamp(28px,4vw,48px);line-height:1;letter-spacing:-.045em;font-weight:850}
#maxess-results-10 .v17-naya-copy{margin:0;max-width:680px;color:rgba(255,255,255,.72);font-size:clamp(15px,1.5vw,18px);line-height:1.5}
#maxess-results-10 .v17-naya-copy strong{color:#fff}
#maxess-results-10 .v17-naya-listen{display:inline-flex;align-items:center;justify-content:center;min-height:48px;padding:0 22px;border:1px solid rgba(255,255,255,.18);border-radius:999px;background:linear-gradient(135deg,#d7b2ff,#8244e7 48%,#42117e);color:#fff;font:inherit;font-weight:900;cursor:pointer;box-shadow:0 12px 30px rgba(101,43,180,.28)}
#maxess-results-10.v17-clean>.v17-hero{min-height:min(760px,86vh)!important;padding-top:46px!important;padding-bottom:58px!important}
#maxess-results-10.v17-clean>.v17-hero .mx-title{font-size:0!important;text-align:center!important;margin:0!important}
#maxess-results-10.v17-clean>.v17-hero .mx-title:after{content:'YOUR AI SCORE';font-size:16px;letter-spacing:.28em;font-weight:950;color:#fff}
#maxess-results-10.v17-clean>.v17-hero .mx-copy,#maxess-results-10.v17-clean>.v17-hero .mx-proof,#maxess-results-10.v17-clean>.v17-hero .mx-hero-actions{display:none!important}
#maxess-results-10.v17-clean>.v17-hero .mx-score strong{font-size:clamp(108px,15vw,190px)!important;color:#fff!important;-webkit-text-fill-color:#fff!important}
#maxess-results-10.v17-clean>.v17-hero .v13-score-label,#maxess-results-10.v17-clean>.v17-hero .v13-score-value,#maxess-results-10.v17-clean>.v17-hero .v13-score-caption{display:none!important}
#maxess-results-10 .v17-orbs{display:grid!important;grid-template-columns:repeat(5,minmax(0,1fr))!important;gap:14px!important;width:min(1120px,100%);margin:auto}
#maxess-results-10 .v17-orb{position:relative;min-height:150px;border-radius:50%;display:grid!important;place-items:center;text-align:center;background:radial-gradient(circle at 35% 28%,rgba(255,255,255,.18),transparent 9%),radial-gradient(circle,#2b1645 0,#0b0611 68%,#030205 100%);border:1px solid rgba(208,168,255,.42);box-shadow:inset 0 0 40px rgba(166,108,255,.2),0 16px 40px rgba(0,0,0,.28);transition:transform .25s ease,box-shadow .25s ease}
#maxess-results-10 .v17-orb:before{content:"";position:absolute;inset:10%;border:1px solid rgba(255,255,255,.12);border-radius:50%;pointer-events:none}
#maxess-results-10 .v17-orb:hover{transform:translateY(-5px);box-shadow:inset 0 0 45px rgba(166,108,255,.28),0 22px 52px rgba(0,0,0,.34)}
#maxess-results-10 .v17-orb-score{position:relative;font-size:36px;line-height:1;font-weight:950;color:#fff}
#maxess-results-10 .v17-orb-name{position:relative;margin-top:7px;font-size:9px;line-height:1.25;font-weight:900;letter-spacing:.1em;text-transform:uppercase;color:rgba(255,255,255,.72)}
@media(max-width:900px){#maxess-results-10 .v17-orbs{grid-template-columns:repeat(2,minmax(0,1fr))!important;max-width:620px}}
@media(max-width:520px){#maxess-results-10 .v17-naya-top{padding:26px 18px 20px}#maxess-results-10 .v17-naya-avatar{width:64px;height:64px}#maxess-results-10 .v17-naya-title{font-size:28px}#maxess-results-10 .v17-naya-copy{font-size:14px}#maxess-results-10.v17-clean>.v17-hero{min-height:auto!important;padding-top:34px!important;padding-bottom:42px!important}#maxess-results-10 .v17-orbs{gap:10px!important}#maxess-results-10 .v17-orb{min-height:132px}#maxess-results-10 .v17-orb-score{font-size:32px}}
@media(prefers-reduced-motion:reduce){#maxess-results-10 .v17-orb{transition:none!important}#maxess-results-10 .v17-orb:hover{transform:none!important}}
</style>
<script id="MAXESS_RESULTS_V17_CLEAN_EXECUTION">
(function(){
'use strict';
function run(){
 var root=document.getElementById('maxess-results-10');if(!root)return;
 var result=window.MAXESS_RESULT||{};
 var score=Number(result.overallScore!=null?result.overallScore:result.score);
 if(Number.isFinite(score))score=Math.round(Math.max(0,Math.min(100,score)));
 function top(el){while(el&&el.parentElement!==root)el=el.parentElement;return el}
 function move(el,cls){if(!el)return null;el.classList.add(cls);root.appendChild(el);return el}
 function one(s){return root.querySelector(s)}
 function textFind(words){var els=root.querySelectorAll('section,article,div');for(var i=0;i<els.length;i++){var t=(els[i].textContent||'').replace(/\s+/g,' ').trim().toLowerCase();for(var j=0;j<words.length;j++)if(t.indexOf(words[j])>-1)return top(els[i])}return null}
 root.classList.add('v17-clean');
 var naya=one('#v13-naya-introduction')||one('.v17-naya-banner')||one('#naya-report')||one('.v11-naya-welcome');
 naya=top(naya);
 if(!naya){naya=document.createElement('section');naya.innerHTML='<div class="v17-naya-inner"><img class="v17-naya-avatar" src="https://raw.githubusercontent.com/SoulSchoolAcademy/maxess/main/Naya%20Profile%20Black.jpg" alt="Naya, your AI guide"><div class="v17-naya-kicker">NAYA · YOUR GUIDE</div><h2 class="v17-naya-title">Hi. I’ve looked at your results.</h2><p class="v17-naya-copy">This isn’t your judgment. <strong>It’s your map.</strong> I’m here to help you understand what you already do well, where your biggest opportunity is, and what to do next.</p></div>')}
 naya.classList.add('v17-naya-top');
 var nt=one.call(naya,'.v13-naya-title,.v11-naya-title');if(nt)nt.textContent='Hi. I’ve looked at your results.';
 var nc=one.call(naya,'.v13-naya-copy,.v11-naya-copy');if(nc)nc.innerHTML='This isn’t your judgment. <strong>It’s your map.</strong> I’m here to help you understand what you already do well, where your biggest opportunity is, and what to do next.';
 var ni=naya.querySelector('img');if(ni){ni.classList.add('v17-naya-avatar');ni.alt='Naya, your AI guide'}
 root.appendChild(naya);
 root.querySelectorAll('#v18-'+'listen-static,#v13-listen,.v17-listen').forEach(function(x){x.style.display='none'});
 var btn=document.createElement('button');btn.type='button';btn.className='v17-naya-listen';btn.textContent='Listen to Naya';btn.setAttribute('aria-label','Listen to Naya walk through your MAXESS results');
 btn.onclick=function(){var c=root.querySelectorAll('#v13-listen button,#mx-naya-listen,#mx-listen,.v17-listen button,[data-maxess-listen]');for(var i=0;i<c.length;i++){if(c[i]!==btn){c[i].click();return}}root.dispatchEvent(new CustomEvent('maxess:naya-listen',{bubbles:true,detail:{result:window.MAXESS_RESULT||null}}))};
 var niw=naya.querySelector('.v17-naya-inner');if(niw)niw.appendChild(btn);else naya.appendChild(btn);
 var hero=top(one('.mx-hero'))||top(one('#v13-hero'));
 if(hero){hero.classList.add('v17-hero');var title=hero.querySelector('.mx-title');if(title)title.textContent='YOUR AI SCORE';hero.querySelectorAll('.v13-score-label,.v13-score-value,.v13-score-caption').forEach(function(x){x.remove()});var nodes=hero.querySelectorAll('.mx-score strong');if(nodes.length&&Number.isFinite(score)){nodes[0].textContent=String(score);for(var q=1;q<nodes.length;q++)nodes[q].textContent=''}move(hero,'v17-hero')}
 var dim=top(one('#v13-dimensions'))||top(one('.v17-dimensions'))||textFind(['five dimensions','your fingerprint']);
 if(dim){dim.classList.add('v17-dims');var grid=dim.querySelector('.v13-dim-grid,.mx-dim-grid');if(!grid){grid=document.createElement('div');dim.appendChild(grid)}grid.className='v17-orbs';grid.setAttribute('role','list');grid.innerHTML='';var ds=Array.isArray(result.dimensions)?result.dimensions:[],names=['Direction','Communication','Evaluation','Iteration','Systems Thinking'];for(var d=0;d<5;d++){var x=ds[d]||{},v=Number(x.score),name=x.name||names[d],card=document.createElement('div');card.className='v17-orb';card.setAttribute('role','listitem');card.setAttribute('aria-label',name+' score '+(Number.isFinite(v)?Math.round(v):'unavailable'));card.innerHTML='<div><div class="v17-orb-score">'+(Number.isFinite(v)?Math.round(v):'—')+'</div><div class="v17-orb-name">'+name+'</div></div>';grid.appendChild(card)}move(dim,'v17-dims')}
 var map=[['v17-pattern',['#v15-pattern','#your-fingerprint'],['your pattern','see the pattern']],['v17-meaning',['#v13-report'],['what it means','every score has']],['v17-strength',['#v13-strengths'],['your advantage','what you already']],['v17-lever',['#v13-lever'],['biggest lever','your lever']],['v17-action',['#v13-next'],['your next chapter','your next move']],['v17-video',['#v13-video'],['watch the video']],['v17-masters',['#v13-masters'],['18 ai pathways','18 naya masters']],['v17-playground',['#naya-playground'],['ai playground','learn what ai can do for you']],['v17-tech',['#v13-final'],['technology should amplify the human']]];
 for(var m=0;m<map.length;m++){var e=null;for(var z=0;z<map[m][1].length&&!e;z++)e=one(map[m][1][z]);if(!e)e=textFind(map[m][2]);if(e)move(e,map[m][0])}
 root.querySelectorAll('#v18-'+'listen-static').forEach(function(x){x.remove()});
 root.setAttribute('data-results-version','17-clean');root.setAttribute('data-results-data-source',Number.isFinite(score)?'window.MAXESS_RESULT':'unavailable');
}
if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',run,{once:true});else run();
})();
</script>
'''
body = s.lower().rfind('</body>')
if body < 0:
    raise SystemExit('No closing body tag')
s = s[:body] + layer + '\n' + s[body:]
p.write_text(s, encoding='utf-8')
print('MAXESS V17 clean presentation layer prepared')
