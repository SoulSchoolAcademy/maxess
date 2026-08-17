from pathlib import Path

p=Path('MAXESS-RESULTS-10-GROOVE.html')
s=p.read_text(encoding='utf-8')
if 'MAXESS_RESULTS_V19_EXACT_EXECUTION' in s:
    raise SystemExit('V19 already applied')

layer=r'''<!-- MAXESS_RESULTS_V19_EXACT_EXECUTION -->
<style id="maxess-results-v19-exact">
#maxess-results-10{overflow-x:hidden!important}
#maxess-results-10.v19-ready{display:flex!important;flex-direction:column!important}
#maxess-results-10.v19-ready>.v19-naya{order:1!important}
#maxess-results-10.v19-ready>.v19-hero{order:2!important}
#maxess-results-10.v19-ready>.v19-dims{order:3!important}
#maxess-results-10.v19-ready>.v19-listen{order:4!important}
#maxess-results-10.v19-ready>.v19-pattern{order:5!important}
#maxess-results-10.v19-ready>.v19-meaning{order:6!important}
#maxess-results-10.v19-ready>.v19-strength{order:7!important}
#maxess-results-10.v19-ready>.v19-lever{order:8!important}
#maxess-results-10.v19-ready>.v19-action{order:9!important}
#maxess-results-10.v19-ready>.v19-video{order:10!important}
#maxess-results-10.v19-ready>.v19-trial{order:11!important}
#maxess-results-10.v19-ready>.v19-masters{order:12!important}
#maxess-results-10.v19-ready>.v19-playground{order:13!important}
#maxess-results-10.v19-ready>.v19-tech{order:14!important}
.v19-orbs{display:grid!important;grid-template-columns:repeat(5,minmax(0,1fr));gap:12px!important}
.v19-orb{position:relative;min-height:165px;display:grid!important;place-items:center!important;text-align:center!important;border-radius:50%!important;background:radial-gradient(circle,#27153c 0,#0a060f 64%,#030205 100%)!important;border:1px solid rgba(210,170,255,.35)!important;box-shadow:inset 0 0 35px rgba(166,108,255,.18),0 15px 40px rgba(0,0,0,.3)!important}
.v19-orb:before{content:"";position:absolute;inset:10%;border:1px solid rgba(208,168,255,.4);border-radius:50%}
.v19-orb .v19-n{position:relative;font-size:38px;font-weight:900;color:#fff}
.v19-orb .v19-l{position:relative;margin-top:7px;font-size:9px;font-weight:900;letter-spacing:.1em;text-transform:uppercase;color:rgba(255,255,255,.7)}
.v19-hero .mx-score-orb{width:min(520px,80vw)!important}
.v19-hero .mx-score strong{font-size:clamp(110px,15vw,190px)!important}
.v19-label{display:block!important;text-align:center!important;margin-bottom:20px!important;color:#fff!important;font-size:16px!important;font-weight:900!important;letter-spacing:.28em!important}
.v19-lever{text-align:center!important}
.v19-lever *{max-width:100%!important}
.v19-tech{text-align:center!important}
@media(max-width:900px){.v19-orbs{grid-template-columns:repeat(2,minmax(0,1fr))!important}}
@media(max-width:520px){.v19-orb{min-height:140px}.v19-orb .v19-n{font-size:32px}}
</style>
<script id="maxess-results-v19-exact">
(function(){
function run(){
 var r=document.getElementById('maxess-results-10');if(!r)return;
 var t=function(x){return(x&&x.textContent||'').replace(/\s+/g,' ').trim().toLowerCase()};
 var top=function(x){while(x&&x.parentElement!==r)x=x.parentElement;return x};
 var find=function(words){var a=r.querySelectorAll('section,article,div');for(var i=0;i<a.length;i++){var z=t(a[i]);for(var j=0;j<words.length;j++)if(z.indexOf(words[j])>=0){var b=top(a[i]);if(b)return b}}return null};
 var hero=r.querySelector('.mx-hero');if(hero)hero=top(hero);
 var dims=r.querySelector('.mx-dim-grid,.v13-dim-grid,.v17-dimensions,#v13-dimensions');if(dims)dims=top(dims);
 var naya=find(['hi, look at your results','you have seen your patterns','you\'ve seen your patterns']);
 var pattern=find(['your pattern']);
 var meaning=find(['what it means','meaning']);
 var strength=find(['your strength']);
 var lever=find(['biggest lever']);
 var action=find(['your move']);
 var video=find(['watch the video']);
 var trial=find(['free trial']);
 var masters=find(['18 naya masters','18 masters']);
 var play=find(['learn what ai can do for you','don\'t learn ai']);
 var tech=find(['technology should amplify the human']);
 if(!naya){naya=document.createElement('section');naya.innerHTML='<div style="text-align:center;padding:28px 20px"><div style="font-weight:900;letter-spacing:.2em">NAYA</div><h1>Hi. Look at your results.</h1><p>This is not a judgment. It is a map — with Naya.</p></div>';r.insertBefore(naya,r.firstChild)}
 var add=function(x,c){if(x){x.classList.add(c);r.appendChild(x)}};
 add(naya,'v19-naya');add(hero,'v19-hero');add(dims,'v19-dims');
 if(dims){var g=dims.querySelector('.mx-dim-grid,.v13-dim-grid,.v17-dim-grid');if(g){g.classList.add('v19-orbs');var names=['Direction','Communication','Evaluation','Iteration','Systems Thinking'];var d=(window.MAXESS_RESULT&&window.MAXESS_RESULT.dimensions)||[];for(var i=0;i<5;i++){var c=g.children[i]||document.createElement('div');c.className='v19-orb';c.innerHTML='<div><div class="v19-n">'+((d[i]&&d[i].score)||'')+'</div><div class="v19-l">'+((d[i]&&d[i].name)||names[i])+'</div></div>';g.appendChild(c)}while(g.children.length>5)g.removeChild(g.lastChild)}}
 if(hero){var lab=document.createElement('div');lab.className='v19-label';lab.textContent='YOUR AI SCORE';hero.insertBefore(lab,hero.firstChild);var sc=hero.querySelector('.mx-score strong');if(sc)sc.textContent=(window.MAXESS_RESULT&&window.MAXESS_RESULT.overallScore)||'';var ss=hero.querySelectorAll('.mx-score strong');for(var q=1;q<ss.length;q++)ss[q].textContent=''}
 var listen=find(['listen to naya']);if(listen&&listen!==hero) add(listen,'v19-listen');
 add(pattern,'v19-pattern');add(meaning,'v19-meaning');add(strength,'v19-strength');add(lever,'v19-lever');add(action,'v19-action');add(video,'v19-video');add(trial,'v19-trial');add(masters,'v19-masters');add(play,'v19-playground');add(tech,'v19-tech');
 r.classList.add('v19-ready');r.setAttribute('data-maxess-v19-order','NAYA|ORB|MINI_ORBS|LISTEN|PATTERN|MEANING|STRENGTH|LEVER|ACTION|VIDEO|TRIAL|MASTERS|PLAYGROUND|TECH');
}
if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',run);else run();
})();
</script>
'''
i=s.lower().rfind('</body>')
if i<0: raise SystemExit('No body closing tag')
p.write_text(s[:i]+layer+s[i:],encoding='utf-8')
print('V19 layer inserted into actual Groove file')
