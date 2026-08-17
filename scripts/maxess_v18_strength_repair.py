from pathlib import Path

p=Path('MAXESS-RESULTS-10-GROOVE.html')
s=p.read_text(encoding='utf-8')
marker='<!-- MAXESS_RESULTS_V18_STRENGTH_REPAIR -->'
if marker in s:
    print('V18 strength repair already present')
    raise SystemExit(0)
layer=r'''<!-- MAXESS_RESULTS_V18_STRENGTH_REPAIR -->
<style id="maxess-results-v18-strength-css">
#maxess-results-10.v18-preservation .v18-strength-section{order:6!important;width:100%;padding:clamp(58px,7vw,108px) clamp(16px,4vw,72px);background:#fff;color:#111}
#maxess-results-10.v18-preservation .v18-strength-wrap{width:min(1200px,100%);margin:auto}
#maxess-results-10.v18-preservation .v18-strength-kicker{color:#6637a8;font-size:10px;font-weight:950;letter-spacing:.18em;text-transform:uppercase}
#maxess-results-10.v18-preservation .v18-strength-section h2{margin:8px 0 0;color:#111;font-size:clamp(36px,5vw,68px);line-height:.94;letter-spacing:-.055em}
#maxess-results-10.v18-preservation .v18-strength-card{display:grid;grid-template-columns:minmax(150px,.34fr) 1fr;gap:28px;align-items:center;margin-top:28px;padding:34px;border-radius:30px;background:linear-gradient(135deg,#f5f1fb,#fff);border:1px solid rgba(0,0,0,.09);box-shadow:0 25px 80px rgba(30,10,50,.10)}
#maxess-results-10.v18-preservation .v18-strength-score{font-size:clamp(74px,9vw,132px);font-weight:950;line-height:.78;letter-spacing:-.08em;color:#111}
#maxess-results-10.v18-preservation .v18-strength-score small{display:block;margin-top:18px;font-size:10px;letter-spacing:.16em;color:#7042aa}
#maxess-results-10.v18-preservation .v18-strength-card h3{margin:0;color:#111;font-size:clamp(28px,3.6vw,52px);line-height:.98;letter-spacing:-.05em}
#maxess-results-10.v18-preservation .v18-strength-card p{margin:14px 0 0;color:#444;line-height:1.6}
@media(max-width:620px){#maxess-results-10.v18-preservation .v18-strength-card{grid-template-columns:1fr;text-align:center;padding:26px 20px}}
</style>
<script id="maxess-results-v18-strength-js">
(function(){
'use strict';
function run(){
 var root=document.getElementById('maxess-results-10');if(!root)return;
 var flow=root.querySelector('.v18-flow');if(!flow)return;
 if(flow.querySelector('.v18-strength-section'))return;
 var r=window.MAXESS_RESULT||{};var ds=Array.isArray(r.dimensions)?r.dimensions.slice(0,5):[];if(ds.length!==5)return;
 var sorted=ds.slice().sort(function(a,b){return Number(b.score)-Number(a.score)}),top=sorted[0]||{};
 var score=Math.round(Math.max(0,Math.min(100,Number(top.score)||0))),name=top.name||'Your strongest signal';
 var sec=document.createElement('section');sec.className='v18-strength-section';sec.innerHTML='<div class="v18-strength-wrap"><div class="v18-strength-kicker">YOUR STRENGTH</div><h2>Recognize what is already working.</h2><div class="v18-strength-card"><div class="v18-strength-score">'+score+'<small>STRONGEST SIGNAL</small></div><div><h3>'+escapeHtml(name)+'</h3><p>You already have meaningful capability here. Use '+escapeHtml(name)+' as a foundation, then compound it through deliberate practice rather than trying to improve everything at once.</p></div></div></div></section>';
 var lever=flow.querySelector('#v13-lever,.v13-lever');if(lever)flow.insertBefore(sec,lever);else flow.appendChild(sec);
 root.setAttribute('data-v18-strength','verified');
}
function escapeHtml(v){return String(v).replace(/[&<>'"]/g,function(c){return({'&':'&amp;','<':'&lt;','>':'&gt;',"'":'&#39;','"':'&quot;'})[c]})}
if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',function(){setTimeout(run,450)},{once:true});else setTimeout(run,450);
})();
</script>
'''
body=s.lower().rfind('</body>')
if body<0:raise SystemExit('No closing body tag')
p.write_text(s[:body]+layer+'\n'+s[body:],encoding='utf-8')
print('V18 strength repair appended')
