from pathlib import Path

path = Path('MAXESS-RESULTS-10-GROOVE.html')
text = path.read_text(encoding='utf-8')
marker = 'MAXESS_RESULTS_V18_GROOVE_SAFE'
if marker in text:
    print('V18 already present; refusing duplicate insertion.')
    raise SystemExit(0)

block = r'''<style id="maxess-results-v18-groove-safe">
/* V18: Groove-safe presentation order. CSS-first so the intended hierarchy survives environments that suppress dynamic DOM reordering. */
html,body{width:100%!important;margin:0!important;padding:0!important;overflow-x:hidden!important}
#maxess-results-10{display:flex!important;flex-direction:column!important;width:100%!important}
#maxess-results-10>#naya-report{order:1!important}
#maxess-results-10>.mx-hero,#maxess-results-10>#v13-hero{order:2!important}
#maxess-results-10>#v13-dimensions{order:3!important}
#maxess-results-10>#v18-listen-static,#maxess-results-10>.v17-listen,#maxess-results-10>#v17-listen,#maxess-results-10>#v13-listen{order:4!important}
#maxess-results-10>#v15-pattern,#maxess-results-10>#your-fingerprint{order:5!important}
#maxess-results-10>#v13-report{order:6!important}
#maxess-results-10>#v13-strengths{order:7!important}
#maxess-results-10>#v13-lever{order:8!important}
#maxess-results-10>#v13-next{order:9!important}
#maxess-results-10>#v13-video{order:10!important}
#maxess-results-10>#v13-masters{order:11!important}
#maxess-results-10>#naya-playground{order:12!important}
#maxess-results-10>#v13-final{order:13!important}
#maxess-results-10>.v17-naya-banner{order:1!important}
#maxess-results-10>.v17-conversion{order:10!important}
#maxess-results-10>.v17-masters-section{order:11!important}
#maxess-results-10>.v17-playground{order:12!important}
#maxess-results-10>.v17-philosophy{order:13!important}
#maxess-results-10>.v17-pattern-section{order:5!important}
#maxess-results-10>.v17-meaning-section{order:6!important}
#maxess-results-10>.v17-strength-section{order:7!important}
#maxess-results-10>.v17-lever-section{order:8!important}
#maxess-results-10>.v17-action-section{order:9!important}
#maxess-results-10>.v17-dimensions{order:3!important}
#maxess-results-10>.v17-listen{order:4!important}
#maxess-results-10>.mx-final{order:13!important}
#maxess-results-10>.mx-hero{min-height:min(760px,88vh)!important}
#maxess-results-10>.mx-hero .mx-title{font-size:0!important}
#maxess-results-10>.mx-hero .mx-title:after{content:'YOUR AI SCORE';font-size:16px;letter-spacing:.28em;font-weight:950;color:#fff}
#maxess-results-10>.mx-hero .mx-copy,#maxess-results-10>.mx-hero .mx-proof,#maxess-results-10>.mx-hero .mx-hero-actions{display:none!important}
#maxess-results-10>.mx-hero .mx-score strong{font-size:clamp(110px,17vw,205px)!important;color:#fff!important;-webkit-text-fill-color:#fff!important}
#maxess-results-10>#v13-dimensions .v13-dim-grid{grid-template-columns:repeat(5,minmax(0,1fr))!important}
#maxess-results-10>#v13-dimensions .v13-dim{min-width:0!important}
#maxess-results-10>#v13-masters .v13-master::before{content:'AI PROFILE';display:block;margin-bottom:7px;color:#cdb6ff;font-size:9px;font-weight:950;letter-spacing:.16em}
@media(max-width:900px){#maxess-results-10>#v13-dimensions .v13-dim-grid{grid-template-columns:repeat(2,minmax(0,1fr))!important}}
@media(max-width:520px){#maxess-results-10>#v13-dimensions .v13-dim-grid{grid-template-columns:1fr 1fr!important}}
</style>
<section id="v18-listen-static" aria-label="Listen to Naya" style="order:4!important;padding:28px 20px;text-align:center;background:linear-gradient(180deg,#050507,#09040f);">
<div style="max-width:760px;margin:auto"><div style="font-size:clamp(28px,4vw,48px);font-weight:950;letter-spacing:-.045em;color:#fff">LISTEN TO NAYA</div><p style="margin:8px auto 16px;color:rgba(255,255,255,.58)">Let Naya walk you through your results.</p><button type="button" data-maxess-listen="1" style="min-width:min(360px,100%);padding:15px 22px;border-radius:999px;border:0;cursor:pointer;font-weight:900">Listen to Naya</button></div>
</section>
<script id="MAXESS_RESULTS_V18_GROOVE_SAFE">
(function(){function run(){var r=document.getElementById('maxess-results-10');if(!r)return;var s=document.getElementById('v18-listen-static');if(s&&s.parentNode!==r)r.appendChild(s);var b=s&&s.querySelector('[data-maxess-listen]');if(b)b.onclick=function(){var x=r.querySelector('#mx-naya-listen,#v13-listen,#mx-listen,#mx-final-listen,.v17-listen button');if(x&&x!==b)x.click();else window.dispatchEvent(new CustomEvent('maxess:naya-listen',{detail:{result:window.MAXESS_RESULT||null}}))};var R=window.MAXESS_RESULT||{};var v=Number(R.overallScore??R.score??R.masterScore);if(Number.isFinite(v)){v=Math.round(Math.max(0,Math.min(100,v)));r.querySelectorAll('.mx-hero .mx-score strong,.mx-hero .v13-score-number').forEach(function(e){e.textContent=v})}}if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',run);else run();setTimeout(run,300);})();
</script>
'''

if '</body>' not in text:
    raise SystemExit('V18 BLOCKED: no closing body tag found')
text = text.replace('</body>', block + '</body>', 1)
path.write_text(text, encoding='utf-8')
print('V18 GROOVE-SAFE BLOCK INSERTED INTO ACTUAL WORKING GROOVE FILE')
