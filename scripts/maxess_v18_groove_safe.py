from pathlib import Path
import re

path=Path('MAXESS-RESULTS-10-GROOVE.html')
text=path.read_text(encoding='utf-8')
marker='MAXESS_RESULTS_V18_2_GROOVE_SAFE'
if marker in text:
    raise SystemExit(0)
block=r'''<style id="maxess-results-v18-2-groove-safe">
html,body{width:100%!important;margin:0!important;padding:0!important;overflow-x:hidden!important}
#maxess-results-10{display:flex!important;flex-direction:column!important;width:100%!important}
#maxess-results-10>#naya-report{order:1!important}
#maxess-results-10>.mx-hero,#maxess-results-10>#v13-hero{order:2!important}
#maxess-results-10>#v13-dimensions{order:3!important}
#maxess-results-10>#v18-listen-static{order:4!important}
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
#maxess-results-10>#v13-masters .v13-master::before{content:'AI PROFILE';display:block;margin-bottom:7px;color:#cdb6ff;font-size:9px;font-weight:950;letter-spacing:.16em}
@media(max-width:900px){#maxess-results-10>#v13-dimensions .v13-dim-grid{grid-template-columns:repeat(2,minmax(0,1fr))!important}}
@media(max-width:520px){#maxess-results-10>#v13-dimensions .v13-dim-grid{grid-template-columns:1fr 1fr!important}}
</style>
<section id="v18-listen-static" aria-label="Listen to Naya" style="order:4!important;padding:28px 20px;text-align:center;background:linear-gradient(180deg,#050507,#09040f);">
<div style="max-width:760px;margin:auto"><div style="font-size:clamp(28px,4vw,48px);font-weight:950;letter-spacing:-.045em;color:#fff">LISTEN TO NAYA</div><p style="margin:8px auto 16px;color:rgba(255,255,255,.58)">Let Naya walk you through your results.</p><button type="button" data-maxess-listen="1" style="min-width:min(360px,100%);padding:15px 22px;border-radius:999px;border:0;cursor:pointer;font-weight:900">Listen to Naya</button></div>
</section>'''

matches=list(re.finditer(r'<[^>]+\bid=["\']v13-final["\'][^>]*>',text,re.I))
if not matches:
    raise SystemExit('V18.2 BLOCKED: could not locate the actual v13-final element')
anchor=matches[0]
text=text[:anchor.start()]+block+'\n'+text[anchor.start():]
path.write_text(text,encoding='utf-8')
print('V18.2 inserted inside the actual results root before the real v13-final element')
