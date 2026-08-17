from pathlib import Path

path = Path('MAXESS-RESULTS-10-GROOVE.html')
text = path.read_text(encoding='utf-8')
marker = 'MAXESS_RESULTS_V17_FORCE_VISUAL'
if marker in text:
    print('V17 force visual patch already present.')
    raise SystemExit(0)

patch = r'''<style id="maxess-results-v17-force-css">
#maxess-results-10.v17-force .v17-naya-banner{order:0!important;margin-top:8px!important}
#maxess-results-10.v17-force .mx-hero{order:1!important;min-height:min(760px,88vh)!important;padding-top:24px!important}
#maxess-results-10.v17-force .mx-hero-grid{display:flex!important;flex-direction:column!important;gap:8px!important;align-items:center!important}
#maxess-results-10.v17-force .mx-hero-grid>.mx-score-orb{order:1!important;width:min(560px,78vw)!important;min-width:300px!important}
#maxess-results-10.v17-force .mx-hero-grid>div:first-child{order:2!important;max-width:800px!important}
#maxess-results-10.v17-force .mx-hero .mx-title{font-size:0!important;margin:0!important}
#maxess-results-10.v17-force .mx-hero .mx-title:after{content:'YOUR AI SCORE';font-size:16px;letter-spacing:.28em;font-weight:950;color:#fff}
#maxess-results-10.v17-force .mx-hero .mx-copy,#maxess-results-10.v17-force .mx-hero .mx-proof,#maxess-results-10.v17-force .mx-hero .mx-hero-actions{display:none!important}
#maxess-results-10.v17-force .mx-score-orb{background:conic-gradient(from 205deg,#ff4545,#ff9e4a,#ffe56b,#58e18b,#50ddff,#6472ff,#a75bff,#ff4fb7,#ff4545)!important;box-shadow:0 0 100px rgba(166,108,255,.34),0 0 210px rgba(80,220,255,.12)!important}
#maxess-results-10.v17-force .mx-score strong{font-size:clamp(110px,17vw,205px)!important;color:#fff!important;-webkit-text-fill-color:#fff!important}
#maxess-results-10.v17-force .v17-dimensions{order:2!important}
#maxess-results-10.v17-force .v17-dimensions .v17-mini-orb-grid{grid-template-columns:repeat(5,minmax(0,1fr))!important}
#maxess-results-10.v17-force .v17-listen{order:3!important}
#maxess-results-10.v17-force .v17-pattern-section{order:4!important}
#maxess-results-10.v17-force .v17-meaning-section{order:5!important}
#maxess-results-10.v17-force .v17-strength-section{order:6!important}
#maxess-results-10.v17-force .v17-lever-section{order:7!important}
#maxess-results-10.v17-force .v17-action-section{order:8!important}
#maxess-results-10.v17-force .v17-conversion{order:9!important}
#maxess-results-10.v17-force .v17-masters-section{order:10!important}
#maxess-results-10.v17-force .v17-playground{order:11!important}
#maxess-results-10.v17-force .v17-philosophy{order:12!important}
#maxess-results-10.v17-force .v17-masters-section .ny-membership{margin-bottom:24px!important}
@media(max-width:900px){#maxess-results-10.v17-force .v17-dimensions .v17-mini-orb-grid{grid-template-columns:repeat(2,minmax(0,1fr))!important}}
</style>
<script id="MAXESS_RESULTS_V17_FORCE_VISUAL">
(function(){
'use strict';
function run(){
 var root=document.getElementById('maxess-results-10');if(!root)return;
 root.classList.add('v17-force');
 function text(e){return(e&&e.textContent||'').replace(/\s+/g,' ').trim()}
 function sections(){return Array.prototype.slice.call(root.children).filter(function(e){return e.tagName==='SECTION'})}
 function find(cls,rx){return sections().find(function(e){return(cls&&e.classList.contains(cls))||(rx&&rx.test(text(e)))})||null}
 var hero=find('mx-hero'),dims=find('v17-dimensions',/every score has its job|five dimensions|your ai capabilities/i),pattern=find('v17-pattern-section',/see your pattern|your pattern|pattern/i),meaning=find('v17-meaning-section',/here.?s what it means|what it means|meaning/i),strength=find('v17-strength-section',/strength/i),lever=find('v17-lever-section',/lever/i),action=find('v17-action-section',/action/i),conversion=find('v17-conversion',/watch the video|free trial|your move/i),masters=find('v17-masters-section',/includes everything|18 naya masters|18 ai pathways/i),playground=find('v17-playground',/learn what ai can do for you|playground/i),final=find('v17-philosophy',/technology should amplify the human/i);
 var banner=root.querySelector('.v17-naya-banner');
 if(banner)banner.style.display='grid';
 var ordered=[banner,hero,dims,pattern,meaning,strength,lever,action,conversion,masters,playground,final];
 ordered.forEach(function(n){if(n&&n.parentNode===root)root.appendChild(n)});
 root.setAttribute('data-maxess-v17-force-order','NAYA>SCORE>DIMENSIONS>LISTEN>PATTERN>MEANING>STRENGTH>LEVER>ACTION>VIDEO>TRIAL>MASTERS>PLAYGROUND>PHILOSOPHY');
 var orb=root.querySelector('.mx-score-orb .mx-score strong');
 if(orb){var r=window.MAXESS_RESULT||{};var score=r.overallScore!=null?r.overallScore:(r.score!=null?r.score:null);if(score!=null)orb.textContent=score}
 var scoreLabel=root.querySelector('.mx-score-orb .mx-score span');if(scoreLabel)scoreLabel.textContent='YOUR AI SCORE';
}
if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',run);else run();
setTimeout(run,50);setTimeout(run,500);
})();
</script>'''

needle='</body>'
if needle not in text: raise SystemExit('Could not locate </body> in Groove artifact')
text=text.replace(needle,patch+'\n'+needle,1)
path.write_text(text,encoding='utf-8')
print('V17 force visual patch applied directly to the working Groove file.')
