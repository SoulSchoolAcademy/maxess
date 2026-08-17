#!/usr/bin/env python3
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
TARGET=ROOT/"MAXESS-RESULTS-10-GROOVE.html"
MARKER="<!-- MAXESS_RESULTS_V16_AAA_EXECUTION -->"

CSS=r'''<style id="maxess-results-v16-aaa-css">
/* V16: preserve the authoritative Results foundation; refine the experience in place. */
#maxess-results-10.v16-results .mx-hero{min-height:min(900px,94vh)!important;background:radial-gradient(circle at 50% 34%,rgba(166,108,255,.27),transparent 31%),radial-gradient(circle at 20% 75%,rgba(85,223,255,.09),transparent 25%),radial-gradient(circle at 82% 68%,rgba(255,79,183,.08),transparent 23%),#07050d!important}
#maxess-results-10.v16-results .mx-hero-grid{gap:22px!important}
#maxess-results-10.v16-results .mx-title{font-size:clamp(48px,7vw,100px)!important;line-height:.88!important;letter-spacing:-.075em!important}
#maxess-results-10.v16-results .mx-copy,#maxess-results-10.v16-results .mx-proof,.hero-score-whisper{display:none!important}
#maxess-results-10.v16-results .mx-score-orb{width:min(620px,78vw)!important;min-width:300px!important;background:conic-gradient(from 205deg,#ff4545 0deg,#ff9e4a 42deg,#ffe56b 86deg,#58e18b 132deg,#50ddff 176deg,#6472ff 225deg,#a75bff 275deg,#ff4fb7 320deg,#ff4545 360deg)!important;border:0!important;box-shadow:0 0 100px rgba(166,108,255,.34),0 0 210px rgba(80,220,255,.12)!important;animation:v16Orb 28s linear infinite!important}
#maxess-results-10.v16-results .mx-score-orb:before{inset:3.5%!important;border-radius:50%!important;background:radial-gradient(circle at 30% 20%,rgba(255,255,255,.98),transparent 5%,rgba(255,255,255,.15) 12%,transparent 29%),radial-gradient(circle at 48% 54%,#28153f 0%,#0b0712 57%,#020207 100%)!important;box-shadow:inset 0 -70px 90px rgba(0,0,0,.72),inset 0 0 75px rgba(255,255,255,.09)!important}
#maxess-results-10.v16-results .mx-score-orb:after{inset:9%!important;border:1px solid rgba(255,255,255,.32)!important;box-shadow:0 0 35px rgba(255,255,255,.12),inset 0 0 40px rgba(255,255,255,.1)!important}
#maxess-results-10.v16-results .mx-score strong{font-size:clamp(112px,17vw,205px)!important;line-height:.78!important}
#maxess-results-10.v16-results .mx-score span{letter-spacing:.25em!important;margin-top:20px!important}
#maxess-results-10.v16-results .mx-band{font-size:21px!important;font-weight:900!important}
#maxess-results-10.v16-results .mx-hero-actions{margin-top:2px!important}
#maxess-results-10.v16-results .v16-chapter{display:flex;align-items:center;gap:12px;margin-bottom:14px}
#maxess-results-10.v16-results .v16-chapter b{display:grid;place-items:center;width:36px;height:36px;border-radius:50%;font-size:10px;border:1px solid rgba(166,108,255,.28);background:rgba(166,108,255,.08);color:#cdb6ff}
#maxess-results-10.v16-results .v16-chapter span{font-size:9px;font-weight:950;letter-spacing:.18em;text-transform:uppercase;color:#777}
#maxess-results-10.v16-results .v16-master{transition:transform .2s ease,box-shadow .2s ease}
#maxess-results-10.v16-results .v16-master:hover{transform:translateY(-4px)}
@keyframes v16Orb{to{transform:rotate(360deg)}}
@media(prefers-reduced-motion:reduce){#maxess-results-10.v16-results .mx-score-orb{animation:none!important}}
@media(max-width:760px){#maxess-results-10.v16-results .mx-score-orb{width:min(88vw,500px)!important;min-width:0!important}#maxess-results-10.v16-results .mx-title{font-size:clamp(44px,14vw,70px)!important}}
</style>'''

JS=r'''<script id="maxess-results-v16-aaa-js">
(function(){
'use strict';
const root=document.getElementById('maxess-results-10');if(!root||root.dataset.v16aaa==='1')return;root.dataset.v16aaa='1';root.classList.add('v16-results');
const get=()=>window.MAXESS_RESULT||null;
const score=()=>{const r=get(),n=Number(r?.overallScore??r?.score??r?.masterScore);return Number.isFinite(n)?Math.max(0,Math.min(100,n)):null};
function apply(){
 const r=get(),s=score();if(!r||s===null)return false;
 const orb=root.querySelector('.mx-score-orb');if(orb){orb.setAttribute('aria-label',`Your AI score is ${Math.round(s)} out of 100`);const n=orb.querySelector('.mx-score strong');if(n)n.textContent=Math.round(s);const lab=orb.querySelector('.mx-score span');if(lab)lab.textContent='YOUR AI SCORE'}
 const title=root.querySelector('.mx-hero .mx-title');if(title)title.textContent='YOUR AI SCORE';
 const meta=root.querySelector('.mx-top-meta');if(meta)meta.textContent=`${r.participant||'Your'} · ${r.assessment||'AI Mastery Assessment'}`;
 root.querySelectorAll('.v16-chapter').forEach(x=>x.remove());
 [...root.querySelectorAll('section')].forEach((sec,i)=>{const h=sec.querySelector('.mx-section-head');if(!h||h.querySelector('.v16-chapter'))return;const c=document.createElement('div');c.className='v16-chapter';c.innerHTML=`<b>${String(i+1).padStart(2,'0')}</b><span>MAXESS RESULTS</span>`;h.prepend(c)});
 const listen=()=>{const t=document.getElementById('mx-naya-listen');if(t)t.click();else window.dispatchEvent(new CustomEvent('maxess:naya-listen',{detail:{result:r}}))};
 root.querySelectorAll('#mx-listen,#mx-final-listen').forEach(b=>b.onclick=listen);
 return true;
}
let tries=0;function boot(){if(apply())return;if(++tries<80)setTimeout(boot,125)}
if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',boot,{once:true});else boot();
window.addEventListener('maxess:result-ready',apply);
})();
</script>'''

def execute():
    if not TARGET.exists(): raise SystemExit("BLOCKED — authoritative artifact missing")
    source=TARGET.read_text(encoding="utf-8")
    if MARKER in source: raise SystemExit("BLOCKED — V16 already executed")
    if 'id="maxess-results-10"' not in source or 'window.MAXESS_RESULT' not in source: raise SystemExit("BLOCKED — result contract/root missing")
    if '</head>' not in source or '</body>' not in source: raise SystemExit("BLOCKED — malformed artifact")
    out=source.replace('</head>',CSS+'</head>',1).replace('</body>',JS+'</body>',1).replace('</html>',MARKER+'</html>',1)
    if len(out)<=len(source): raise SystemExit("BLOCKED — ZERO-CHANGE EXECUTION")
    TARGET.write_text(out,encoding="utf-8")
    print(f"V16 executed: {len(source)} -> {len(out)} bytes")
if __name__=="__main__": execute()

# V16 trigger touch: intentionally unchanged execution logic; used to activate the candidate workflow.
