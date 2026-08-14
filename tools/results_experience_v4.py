from pathlib import Path
import re

PATH = Path('code')
s = PATH.read_text(encoding='utf-8')
original = s

s = re.sub(r'<meta name="maxess-build" content="[^"]+">', '<meta name="maxess-build" content="AAA-2026-08-14-v4-results">', s, count=1)
s = re.sub(r'<meta name="maxess-aaa-pass" content="[^"]+">', '<meta name="maxess-aaa-pass" content="2026-08-14-v4-results">', s, count=1)

CSS = r'''
/* =========================================================
   MAXESS RESULTS EXPERIENCE V4 — REWARD / TRUST / CLARITY
========================================================= */
.results-v4-intro{display:grid;grid-template-columns:minmax(0,1.35fr) minmax(280px,.8fr);gap:16px;margin-top:30px;align-items:stretch}
.results-v4-card{position:relative;padding:27px 28px;border:1px solid rgba(184,149,255,.18);border-radius:30px;background:linear-gradient(145deg,rgba(138,92,255,.10),rgba(255,255,255,.025) 48%,rgba(237,66,196,.035));box-shadow:inset 0 1px 0 rgba(255,255,255,.07),0 18px 45px rgba(0,0,0,.28)}
.results-v4-card h4{margin:0;font-size:12px;letter-spacing:.18em;text-transform:uppercase;color:#b895ff;font-weight:950}.results-v4-card p{margin:11px 0 0;color:#ddd8e6;font-size:15px;line-height:1.58;font-weight:600}
.results-v4-truth{display:flex;flex-direction:column;justify-content:center}.results-v4-truth strong{font-size:18px;color:#fff}.results-v4-truth>span{display:block;margin-top:8px;color:#aaa5b3;font-size:12px;line-height:1.5}
.results-v4-method{margin-top:14px;display:flex;flex-wrap:wrap;gap:7px}.results-v4-chip{padding:7px 10px;border:1px solid rgba(255,255,255,.10);border-radius:999px;background:rgba(255,255,255,.035);color:#c8c1d4;font-size:10px;font-weight:850}
.results-v4-delta{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-top:14px}.results-v4-delta-card{padding:20px 21px;border-radius:24px;border:1px solid rgba(255,255,255,.09);background:rgba(255,255,255,.025)}.results-v4-delta-card strong{display:block;font-size:11px;letter-spacing:.14em;text-transform:uppercase;font-weight:950}.results-v4-delta-card p{margin:8px 0 0;font-size:13px;line-height:1.5;color:#bcb7c3}.results-v4-strength strong{color:#35e39b}.results-v4-opportunity strong{color:#ffd45a}
.results-v4-masterkey{margin-top:58px;padding:38px 30px;border-radius:40px;border:1px solid rgba(184,149,255,.26);background:radial-gradient(circle at 50% 0,rgba(138,92,255,.16),transparent 48%),linear-gradient(145deg,#14101b,#08080c);box-shadow:0 24px 65px rgba(0,0,0,.42),inset 0 1px 0 rgba(255,255,255,.08);text-align:center}.results-v4-masterkey h3{margin:8px 0 0;font-size:clamp(27px,4.5vw,43px);line-height:1.03;letter-spacing:-.04em;font-weight:950}.results-v4-masterkey .mk-intro{max-width:690px;margin:13px auto 0;color:#bdb7c5;font-size:15px;line-height:1.55}
.results-v4-steps{display:grid;grid-template-columns:repeat(7,1fr);gap:7px;margin-top:25px}.results-v4-step{min-height:92px;padding:13px 8px;border:1px solid rgba(255,255,255,.09);border-radius:18px;background:rgba(255,255,255,.025);display:flex;flex-direction:column;justify-content:center;align-items:center}.results-v4-step b{font-size:14px;color:#fff}.results-v4-step span{margin-top:5px;font-size:8px;line-height:1.25;color:#8f8999;letter-spacing:.08em;text-transform:uppercase;font-weight:850}.results-v4-arrow{align-self:center;color:#8a5cff;font-size:14px}
.results-v4-cta-note{margin:16px auto 0;max-width:560px;color:#8f8997;font-size:11px;line-height:1.5}.results-v4-cta-note strong{color:#c8c1d0}.results-v4-method-toggle{margin-top:14px;border:0;background:transparent;color:#a892c9;font-size:11px;font-weight:850;cursor:pointer;text-decoration:underline;text-underline-offset:3px}.results-v4-method-detail{display:none;margin-top:12px;color:#9d97a6;font-size:11px;line-height:1.55;text-align:left}.results-v4-method-detail.open{display:block}
.results-v4-reveal{animation:resultsV4Reveal .8s cubic-bezier(.2,.8,.2,1) both}@keyframes resultsV4Reveal{from{opacity:0;transform:translateY(14px)}to{opacity:1;transform:none}}
@media(max-width:760px){.results-v4-intro{grid-template-columns:1fr}.results-v4-delta{grid-template-columns:1fr}.results-v4-masterkey{padding:29px 17px;border-radius:30px}.results-v4-steps{grid-template-columns:repeat(2,1fr)}.results-v4-step:last-child{grid-column:1/-1}.results-v4-card{padding:23px 20px}.results-v4-cta-note{font-size:10px}}
@media(prefers-reduced-motion:reduce){.results-v4-reveal{animation:none}}
'''
if 'MAXESS RESULTS EXPERIENCE V4' not in s:
    s = s.replace('</style>', CSS + '\n</style>', 1)

ANCHOR = '''    </div>\n\n\n    <!-- ==================================================\n       DIMENSIONS'''
BLOCK = '''    </div>\n\n    <div class="results-v4-intro results-v4-reveal">\n      <article class="results-v4-card">\n        <h4>What this score actually tells you</h4>\n        <p id="resultsV4Opening">Your score is a map of how you currently direct, communicate with, evaluate, improve, and systematize AI. It is not a judgment of your intelligence or potential.</p>\n        <div class="results-v4-method"><span class="results-v4-chip">Current capability</span><span class="results-v4-chip">Self-reported patterns</span><span class="results-v4-chip">Actionable direction</span></div>\n        <button class="results-v4-method-toggle" id="resultsV4MethodToggle" type="button" aria-expanded="false">How did you calculate this?</button>\n        <div class="results-v4-method-detail" id="resultsV4MethodDetail">Each answer carries a defined capability value. Responses are grouped into five dimensions, each dimension is averaged, and the five dimension scores are combined using the configured dimension weights. MAXESS is a capability discovery tool, not a clinical, IQ, or scientifically validated psychological test.</div>\n      </article>\n      <article class="results-v4-card results-v4-truth">\n        <strong>Your score is a starting point — not a ceiling.</strong>\n        <span>The useful question is not “Am I good enough?” It is “What would make my next result better?”</span>\n        <div class="results-v4-delta">\n          <div class="results-v4-delta-card results-v4-strength"><strong>Keep</strong><p id="resultsV4Keep">Your strongest capability.</p></div>\n          <div class="results-v4-delta-card results-v4-opportunity"><strong>Build</strong><p id="resultsV4Build">Your highest-leverage opportunity.</p></div>\n        </div>\n      </article>\n    </div>\n\n    <!-- ==================================================\n       DIMENSIONS'''
if 'id="resultsV4Opening"' not in s:
    if ANCHOR not in s: raise RuntimeError('Results insertion anchor not found')
    s = s.replace(ANCHOR, BLOCK, 1)

ANCHOR2 = '''  <!-- ==================================================\n       NEXT LEVEL\n  ================================================== -->'''
MASTER = '''  <section class="results-v4-masterkey results-v4-reveal" aria-labelledby="resultsV4MasterKeyTitle">\n    <div class="report-kicker">THE MAXESS MASTER KEY</div>\n    <h3 id="resultsV4MasterKeyTitle">Exceptional AI output is a process.</h3>\n    <p class="mk-intro">You do not need a magical prompt. You need a repeatable way to direct intelligence, judge the result, and improve it until the work deserves to be finished.</p>\n    <div class="results-v4-steps" aria-label="MAXESS Master Key process">\n      <div class="results-v4-step"><b>KNOW</b><span>Goal</span></div><span class="results-v4-arrow" aria-hidden="true">→</span><div class="results-v4-step"><b>TELL</b><span>Context</span></div><span class="results-v4-arrow" aria-hidden="true">→</span><div class="results-v4-step"><b>ASK</b><span>Direction</span></div><span class="results-v4-arrow" aria-hidden="true">→</span><div class="results-v4-step"><b>LOOK</b><span>Result</span></div><span class="results-v4-arrow" aria-hidden="true">→</span><div class="results-v4-step"><b>SCORE</b><span>Quality</span></div><span class="results-v4-arrow" aria-hidden="true">→</span><div class="results-v4-step"><b>IMPROVE</b><span>Refine</span></div><span class="results-v4-arrow" aria-hidden="true">→</span><div class="results-v4-step"><b>REPEAT</b><span>Mastery</span></div>\n    </div>\n  </section>\n\n  <!-- ==================================================\n       NEXT LEVEL\n  ================================================== -->'''
if 'resultsV4MasterKeyTitle' not in s:
    if ANCHOR2 not in s: raise RuntimeError('Next level anchor not found')
    s = s.replace(ANCHOR2, MASTER, 1)

s = s.replace("""      You don't need more information.\n      You need a better way to use what you already have.""", """      Now you know where you are.\n      Let’s build where you can go.""", 1)
s = s.replace("""      MAXESS shows you where you are.\n      The next step is learning how to turn AI into a real capability\n      you can use, improve, repeat, and eventually build on.""", """      Your report is the map. The next step is learning the repeatable methods that turn AI from something you occasionally use into a capability you can direct, evaluate, improve, and build on.""", 1)
if 'No pressure.' not in s:
    s = s.replace('    <div class="cta-actions">', '    <div class="results-v4-cta-note"><strong>No pressure.</strong> Keep your report. Explore when you are ready. The invitation below is simply the next chapter if you want help turning these insights into capability.</div>\n\n    <div class="cta-actions">', 1)

ANCHOR3 = '''  DOM.resultSubtitle.textContent=\n    results.band.description;'''
PATCH3 = '''  DOM.resultSubtitle.textContent=\n    results.band.description;\n\n  const resultsV4Opening=document.getElementById("resultsV4Opening");\n  const resultsV4Keep=document.getElementById("resultsV4Keep");\n  const resultsV4Build=document.getElementById("resultsV4Build");\n  if(resultsV4Opening){\n    resultsV4Opening.textContent=`Your ${Math.round(results.overall)}/100 is a capability snapshot based on the choices you made here. It shows how your current patterns line up across five practical dimensions of working with AI.`;\n  }\n  if(resultsV4Keep){\n    resultsV4Keep.textContent=`${strongest.name} is currently your strongest dimension at ${Math.round(strongest.score)}/100. Keep using this strength while you build the next layer.`;\n  }\n  if(resultsV4Build){\n    resultsV4Build.textContent=`${opportunity.name} is your lowest dimension at ${Math.round(opportunity.score)}/100, making it the clearest place to look for leverage.`;\n  }'''
if 'resultsV4Opening=document' not in s:
    if ANCHOR3 not in s: raise RuntimeError('Result copy anchor not found')
    s = s.replace(ANCHOR3, PATCH3, 1)

ANCHOR4 = '''  renderInterests();\n\n\n  if(results.overall>=90){'''
PATCH4 = '''  renderInterests();\n\n  if(state.selectedInterests.size){\n    const intro=DOM.interestReportIntro;\n    if(intro) intro.textContent=`These are the AI territories you told us matter to you. They do not change your score; they make the direction after your report more relevant to you.`;\n  }\n\n  if(results.overall>=90){'''
if 'They do not change your score' not in s:
    if ANCHOR4 not in s: raise RuntimeError('Interest anchor not found')
    s = s.replace(ANCHOR4, PATCH4, 1)

ANCHOR5 = '''DOM.freeTrialButton.addEventListener(\n  "click",\n  openFreeTrial\n);'''
PATCH5 = '''DOM.freeTrialButton.addEventListener(\n  "click",\n  openFreeTrial\n);\n\nconst resultsV4MethodToggle=document.getElementById("resultsV4MethodToggle");\nif(resultsV4MethodToggle){\n  resultsV4MethodToggle.addEventListener("click",()=>{\n    const detail=document.getElementById("resultsV4MethodDetail");\n    if(!detail) return;\n    const open=detail.classList.toggle("open");\n    resultsV4MethodToggle.setAttribute("aria-expanded",String(open));\n    resultsV4MethodToggle.textContent=open?"Hide scoring method":"How did you calculate this?";\n  });\n}'''
if 'resultsV4MethodToggle.addEventListener' not in s:
    if ANCHOR5 not in s: raise RuntimeError('Method event anchor not found')
    s = s.replace(ANCHOR5, PATCH5, 1)

PATH.write_text(s, encoding='utf-8')
print('results-v4 patch applied' if s != original else 'no changes required')
