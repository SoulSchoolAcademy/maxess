from pathlib import Path

path = Path('MAXESS-RESULTS-10-GROOVE.html')
text = path.read_text(encoding='utf-8')
marker = 'MAXESS_RESULTS_V17_EXACT_EXECUTION'
if marker in text:
    raise SystemExit('EXACT FINALIZER already present; refusing duplicate execution layer')

payload = r'''<style id="maxess-results-v17-exact-css">
#maxess-results-10.v17-exact .v17-exact-naya{display:grid!important;grid-template-columns:52px minmax(0,1fr)!important;gap:12px!important;align-items:center!important;width:min(1120px,calc(100% - 28px))!important;margin:10px auto 0!important;padding:10px 14px!important;border-radius:18px!important;background:linear-gradient(105deg,#fff,#f7f3fc 62%,#eef9f8)!important;color:#111!important;border:1px solid rgba(0,0,0,.10)!important;box-shadow:0 18px 48px rgba(0,0,0,.20)!important}
#maxess-results-10.v17-exact .v17-exact-naya img{width:52px!important;height:52px!important;border-radius:50%!important;object-fit:cover!important;border:2px solid #fff!important}
#maxess-results-10.v17-exact .v17-exact-naya .k{font-size:9px!important;font-weight:950!important;letter-spacing:.18em!important;color:#7042aa!important;text-transform:uppercase!important}
#maxess-results-10.v17-exact .v17-exact-naya .t{margin:2px 0 0!important;font-size:clamp(16px,2vw,23px)!important;line-height:1.08!important;font-weight:850!important}
#maxess-results-10.v17-exact .v17-exact-naya .c{margin:3px 0 0!important;color:#444!important;font-size:12px!important;line-height:1.35!important}
#maxess-results-10.v17-exact .v17-exact-listen{padding:28px 20px!important;text-align:center!important;background:linear-gradient(180deg,#050507,#09040f)!important}
#maxess-results-10.v17-exact .v17-exact-listen h2{margin:0!important;font-size:clamp(28px,4vw,48px)!important;letter-spacing:-.045em!important}
#maxess-results-10.v17-exact .v17-exact-listen p{margin:8px auto 16px!important;color:rgba(255,255,255,.58)!important}
#maxess-results-10.v17-exact .v17-exact-listen button{min-width:min(360px,100%)!important}
#maxess-results-10.v17-exact .mx-hero .mx-title{font-size:0!important;margin:0!important}
#maxess-results-10.v17-exact .mx-hero .mx-title:after{content:'YOUR AI SCORE';font-size:16px;letter-spacing:.28em;font-weight:950;color:#fff}
#maxess-results-10.v17-exact .mx-hero .mx-copy,#maxess-results-10.v17-exact .mx-hero .mx-proof,#maxess-results-10.v17-exact .mx-hero .mx-hero-actions{display:none!important}
#maxess-results-10.v17-exact .mx-score strong{font-size:clamp(110px,17vw,205px)!important;color:#fff!important;-webkit-text-fill-color:#fff!important}
#maxess-results-10.v17-exact .v17-exact-masters .v13-master::before,#maxess-results-10.v17-exact .v17-exact-masters .mx-area::before{content:'AI PROFILE';display:block;color:#cdb6ff;font-size:9px;font-weight:950;letter-spacing:.16em;margin-bottom:7px}
#maxess-results-10.v17-exact .v17-exact-dimensions{order:3!important}.v17-exact .v17-exact-listen{order:4!important}.v17-exact .v17-exact-pattern{order:5!important}.v17-exact .v17-exact-meaning{order:6!important}.v17-exact .v17-exact-strength{order:7!important}.v17-exact .v17-exact-lever{order:8!important}.v17-exact .v17-exact-action{order:9!important}.v17-exact .v17-exact-conversion{order:10!important}.v17-exact .v17-exact-masters{order:11!important}.v17-exact .v17-exact-playground{order:12!important}.v17-exact .v17-exact-philosophy{order:13!important}
@media(max-width:900px){#maxess-results-10.v17-exact .v17-exact-dimensions .v17-mini-orb-grid{grid-template-columns:repeat(2,minmax(0,1fr))!important}}
@media(max-width:620px){#maxess-results-10.v17-exact .v17-exact-naya{grid-template-columns:44px minmax(0,1fr)!important;padding:9px 11px!important}#maxess-results-10.v17-exact .v17-exact-naya img{width:44px!important;height:44px!important}}
</style>
<script id="MAXESS_RESULTS_V17_EXACT_EXECUTION">
(function(){
'use strict';
function boot(){
 var root=document.getElementById('maxess-results-10');if(!root)return;
 root.classList.add('v17-exact');
 function secs(){return Array.prototype.slice.call(root.children).filter(function(e){return e.tagName==='SECTION'})}
 function id(x){return document.getElementById(x)}
 function text(e){return(e&&e.textContent||'').toLowerCase()}
 function find(words){return secs().find(function(s){var t=text(s);return words.some(function(w){return t.indexOf(w)>=0})})||null}
 var hero=root.querySelector('.mx-hero,.v13-hero');
 var dims=id('v13-dimensions')||root.querySelector('.v17-dimensions')||find(['every score has its job','your five dimensions']);
 var pattern=id('your-fingerprint')||id('v11-fingerprint')||id('v15-pattern')||root.querySelector('.v17-pattern-section')||find(['see your pattern','your pattern']);
 var meaning=id('v13-report')||find(['your report','what your result means','here’s what it means',"here's what it means"]);
 var strength=id('v13-strengths')||root.querySelector('.v13-story-section')||find(['your strengths','your superpowers','your advantage']);
 var lever=id('v13-lever')||find(['your biggest lever','highest leverage opportunity','biggest lever']);
 var action=id('v13-next')||root.querySelector('.v13-next-section')||find(['your next move','your next chapter','from capability']);
 var video=id('v13-video')||find(['watch the video','video']);
 var masters=id('v13-masters')||root.querySelector('.v13-pathways-section')||find(['18 ai pathways','your 18 ai pathways','includes everything']);
 var playground=id('naya-playground')||root.querySelector('.mx-naya-playground')||find(['learn what ai can do for you','don’t learn ai','do not learn ai']);
 var philosophy=id('v13-final')||root.querySelector('.v17-philosophy')||find(['technology should amplify the human','technology should amplify your human']);
 var n=root.querySelector('.v17-exact-naya');
 if(!n){n=document.createElement('section');n.className='v17-exact-naya';n.innerHTML='<img src="https://i.postimg.cc/d1nncN9F/Naya-and-shawn-ok-44-a.png" alt="Naya, your AI guide"><div><div class="k">NAYA · YOUR AI GUIDE</div><div class="t">This isn’t a judgment. It’s a map.</div><div class="c">Hi. I’m Naya. I’ll help you understand what your result means and what to do with it.</div></div>'}
 var listen=root.querySelector('.v17-exact-listen');
 if(!listen){listen=document.createElement('section');listen.className='v17-exact-listen';listen.innerHTML='<div class="mx-wide"><h2>LISTEN TO NAYA</h2><p>Let Naya walk you through your results.</p><button type="button" class="mx-cta mx-cta-primary">Listen to Naya</button></div>';listen.querySelector('button').onclick=function(){var live=root.querySelector('#mx-naya-listen,#v13-listen,#mx-listen,#mx-final-listen');if(live)live.click();else window.dispatchEvent(new CustomEvent('maxess:naya-listen',{detail:{result:window.MAXESS_RESULT||null}}))}}
 if(dims)dims.classList.add('v17-exact-dimensions');if(pattern)pattern.classList.add('v17-exact-pattern');if(meaning)meaning.classList.add('v17-exact-meaning');if(strength)strength.classList.add('v17-exact-strength');if(lever)lever.classList.add('v17-exact-lever');if(action)action.classList.add('v17-exact-action');if(video)video.classList.add('v17-exact-conversion');if(masters)masters.classList.add('v17-exact-masters');if(playground)playground.classList.add('v17-exact-playground');if(philosophy)philosophy.classList.add('v17-exact-philosophy');
 var order=[n,hero,dims,listen,pattern,meaning,strength,lever,action,video,masters,playground,philosophy];
 order.forEach(function(node){if(node){root.appendChild(node)}});
 var r=window.MAXESS_RESULT||{};var s=Number(r.overallScore??r.score??r.masterScore);if(Number.isFinite(s)){s=Math.round(Math.max(0,Math.min(100,s)));root.querySelectorAll('.mx-hero .mx-score strong,.mx-hero .v13-score-number').forEach(function(el){el.textContent=String(s)});var orb=root.querySelector('.mx-hero .mx-score-orb,.mx-hero .v13-score-orb');if(orb)orb.setAttribute('aria-label','Your AI score is '+s+' out of 100')}
 root.setAttribute('data-maxess-v17-exact-order','NAYA>SCORE>DIMENSIONS>LISTEN>PATTERN>MEANING>STRENGTH>LEVER>ACTION>VIDEO/TRIAL>MASTERS>PLAYGROUND>PHILOSOPHY');
 root.setAttribute('data-maxess-v17-exact-status','PASS');
}
if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',boot,{once:true});else boot();
setTimeout(boot,250);setTimeout(boot,1000);
})();
</script>
'''
text = text.replace('</body>', payload + '\n<!-- MAXESS_RESULTS_V17_EXACT_EXECUTION -->\n</body>')
path.write_text(text, encoding='utf-8')
print('EXACT FINALIZER APPENDED TO ACTUAL GROOVE FILE')
