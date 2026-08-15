from pathlib import Path

PATH = Path('code')
s = PATH.read_text(encoding='utf-8')
original = s
MARKER = 'MAXESS RESULTS EXPERIENCE 9.9 — PERSONAL SIGNAL'

CSS = r'''
/* =========================================================
   MAXESS RESULTS EXPERIENCE 9.9 — PERSONAL SIGNAL
   Purpose: give the Results Experience one clear human spine
   before the deeper layers appear.
========================================================= */
.maxess-signal{position:relative;margin:24px auto 0;max-width:980px;padding:clamp(28px,4vw,42px);border:1px solid rgba(184,149,255,.30);border-radius:32px;background:radial-gradient(circle at 50% 0,rgba(138,92,255,.18),transparent 48%),linear-gradient(145deg,rgba(255,255,255,.055),rgba(255,255,255,.018));box-shadow:0 25px 70px rgba(0,0,0,.38),inset 0 1px 0 rgba(255,255,255,.10);text-align:center}
.maxess-signal::before{content:"";position:absolute;left:12%;right:12%;top:0;height:1px;background:linear-gradient(90deg,transparent,rgba(216,192,255,.68),transparent);box-shadow:0 0 22px rgba(138,92,255,.25)}
.maxess-signal-kicker{color:#b895ff;font-size:10px;line-height:1;letter-spacing:.20em;text-transform:uppercase;font-weight:950}
.maxess-signal h3{max-width:760px;margin:12px auto 0;color:#fff;font-size:clamp(25px,4vw,40px);line-height:1.06;letter-spacing:-.035em;font-weight:950}
.maxess-signal-lead{max-width:680px;margin:13px auto 0;color:#aaa5b3;font-size:14px;line-height:1.58;font-weight:600}
.maxess-signal-grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:12px;max-width:720px;margin:24px auto 0}
.maxess-signal-item{min-width:0;padding:19px 20px;border:1px solid rgba(255,255,255,.09);border-radius:22px;background:rgba(255,255,255,.025);text-align:left}
.maxess-signal-item span{display:block;font-size:9px;letter-spacing:.16em;text-transform:uppercase;font-weight:950}
.maxess-signal-item strong{display:block;margin-top:7px;color:#fff;font-size:14px;line-height:1.4;font-weight:850}
.maxess-signal-keep span{color:#35e39b}.maxess-signal-build span{color:#ffd45a}
.maxess-signal-note{max-width:650px;margin:16px auto 0;color:#8f8997;font-size:11px;line-height:1.55}
.maxess-signal-note b{color:#c9c2d1}
.maxess-signal-next{display:inline-flex;align-items:center;justify-content:center;gap:8px;margin-top:16px;padding:10px 14px;border:1px solid rgba(184,149,255,.20);border-radius:999px;background:rgba(138,92,255,.06);color:#d6cee4;font-size:10px;font-weight:900}
.maxess-signal-next .dot{width:6px;height:6px;border-radius:50%;background:#35e39b;box-shadow:0 0 10px rgba(53,227,155,.7)}
@media(max-width:760px){.maxess-signal{padding:25px 19px;border-radius:28px}.maxess-signal h3{font-size:27px}.maxess-signal-lead{font-size:13px}.maxess-signal-grid{grid-template-columns:1fr;gap:9px;margin-top:20px}.maxess-signal-item{padding:16px 17px}}
@media(prefers-reduced-motion:reduce){.maxess-signal{animation:none}}
'''

if MARKER not in s:
    if '</style>' not in s:
        raise RuntimeError('style closing tag not found')
    s = s.replace('</style>', CSS + '\n</style>', 1)

HTML_ANCHOR = '''    <div class="results-v4-intro results-v4-reveal">'''
HTML = '''    <section class="maxess-signal results-v4-reveal" aria-labelledby="maxessSignalTitle">
      <div class="maxess-signal-kicker">YOUR PERSONAL SIGNAL</div>
      <h3 id="maxessSignalTitle">Here's the most important thing I see in your result.</h3>
      <p class="maxess-signal-lead" id="maxessSignalLead">Your strongest capability is the foundation. Your clearest opportunity is where your next improvement can create the most leverage.</p>
      <div class="maxess-signal-grid">
        <article class="maxess-signal-item maxess-signal-keep"><span>KEEP</span><strong id="maxessSignalKeep">Your strongest capability.</strong></article>
        <article class="maxess-signal-item maxess-signal-build"><span>BUILD</span><strong id="maxessSignalBuild">Your highest-leverage opportunity.</strong></article>
      </div>
      <div class="maxess-signal-note"><b>How to read this:</b> MAXESS is showing you a current capability pattern from your assessment choices. It is a starting signal, not a judgment or prediction.</div>
      <div class="maxess-signal-next"><span class="dot" aria-hidden="true"></span><span id="maxessSignalNext">Next: see the evidence behind this pattern.</span></div>
    </section>

'''
if 'id="maxessSignalTitle"' not in s:
    if HTML_ANCHOR not in s:
        raise RuntimeError('Results intro anchor not found')
    s = s.replace(HTML_ANCHOR, HTML + HTML_ANCHOR, 1)

# Reorder: move leverage insights immediately after the score/signal area,
# so the user sees their opportunity before the detailed dimension report.
REORDER_MARKER = 'MAXESS RESULTS EXPERIENCE 9.9 — REORDER'
if REORDER_MARKER not in s:
    js_reorder = r'''

  /* MAXESS RESULTS EXPERIENCE 9.9 — REORDER */
  const maxessResultView=document.getElementById("resultsView");
  if(maxessResultView){
    const signal=maxessResultView.querySelector(".maxess-signal");
    const insightFlow=maxessResultView.querySelector(".insight-flow");
    const reportSections=[...maxessResultView.querySelectorAll(":scope > .report-section")];
    const dimensionsSection=reportSections.find(section=>section.querySelector("#dimensionConstellation"));
    if(signal && insightFlow && dimensionsSection){
      const insightSection=insightFlow.closest(".report-section");
      if(insightSection){ signal.insertAdjacentElement("afterend", insightSection); }
    }
  }

'''
    anchor = '  const resultsV4NayaText=document.getElementById("resultsV4NayaText");'
    if anchor not in s:
        raise RuntimeError('Results render anchor not found')
    s = s.replace(anchor, js_reorder + anchor, 1)

# Populate the signal with the already-computed personalization values.
JS_ANCHOR = '''  if(resultsV4Build){
    resultsV4Build.textContent=`${opportunity.name} is your lowest dimension at ${Math.round(opportunity.score)}/100, making it the clearest place to look for leverage.`;
  }'''
JS = '''  if(resultsV4Build){
    resultsV4Build.textContent=`${opportunity.name} is your lowest dimension at ${Math.round(opportunity.score)}/100, making it the clearest place to look for leverage.`;
  }
  const maxessSignalKeep=document.getElementById("maxessSignalKeep");
  const maxessSignalBuild=document.getElementById("maxessSignalBuild");
  const maxessSignalLead=document.getElementById("maxessSignalLead");
  const maxessSignalNext=document.getElementById("maxessSignalNext");
  if(maxessSignalKeep){maxessSignalKeep.textContent=`${strongest.name} · ${Math.round(strongest.score)}/100 — your strongest current capability.`;}
  if(maxessSignalBuild){maxessSignalBuild.textContent=`${opportunity.name} · ${Math.round(opportunity.score)}/100 — your clearest leverage opportunity.`;}
  if(maxessSignalLead){maxessSignalLead.textContent=`Your ${Math.round(results.overall)}/100 is a capability snapshot. The fastest path forward is not to fix everything — it is to keep your strength and deliberately build the area with the most room to improve.`;}
  if(maxessSignalNext){maxessSignalNext.textContent=`Next: see the evidence behind your ${opportunity.name} opportunity.`;}
'''
if 'maxessSignalKeep=document' not in s:
    if JS_ANCHOR not in s:
        raise RuntimeError('Signal population anchor not found')
    s = s.replace(JS_ANCHOR, JS, 1)

PATH.write_text(s, encoding='utf-8')
print('MAXESS 9.9 personal signal + hierarchy refinement applied' if s != original else 'no changes required')
