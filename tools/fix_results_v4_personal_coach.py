from pathlib import Path

p=Path('code')
s=p.read_text(encoding='utf-8')

css='''\n/* MAXESS RESULTS V4 — CONTEXTUAL NAYA / PERSONAL PLAYGROUND */\n.results-v4-naya{margin-top:18px;padding:27px 28px;border:1px solid rgba(184,149,255,.22);border-radius:30px;background:radial-gradient(circle at 8% 0,rgba(138,92,255,.15),transparent 42%),linear-gradient(145deg,rgba(255,255,255,.045),rgba(255,255,255,.018));box-shadow:inset 0 1px 0 rgba(255,255,255,.07),0 18px 45px rgba(0,0,0,.26);display:grid;grid-template-columns:auto minmax(0,1fr);gap:17px;align-items:start}\n.results-v4-naya-orb{width:52px;height:52px;border-radius:50%;background:radial-gradient(circle at 30% 20%,#fff 0%,#dfd1ff 12%,#946dff 38%,#3b1b83 70%,#09050f 100%);border:1px solid #ddd1ff;box-shadow:inset 0 2px 4px rgba(255,255,255,.75),0 0 22px rgba(116,76,255,.38),0 7px 15px rgba(0,0,0,.6)}\n.results-v4-naya h4{margin:0;color:#b895ff;font-size:10px;letter-spacing:.18em;text-transform:uppercase;font-weight:950}.results-v4-naya p{margin:8px 0 0;color:#e2ddea;font-size:15px;line-height:1.58;font-weight:650}.results-v4-playground{margin-top:14px;display:flex;flex-wrap:wrap;gap:7px}.results-v4-playground span{padding:7px 10px;border:1px solid rgba(184,149,255,.20);border-radius:999px;background:rgba(138,92,255,.07);color:#d6cee4;font-size:10px;font-weight:850}\n@media(max-width:760px){.results-v4-naya{grid-template-columns:1fr;padding:23px 20px}.results-v4-naya-orb{width:44px;height:44px}.results-v4-naya p{font-size:13px}}\n'''
if 'CONTEXTUAL NAYA / PERSONAL PLAYGROUND' not in s:
    s=s.replace('</style>',css+'\n</style>',1)

anchor='''  <section class="results-v4-masterkey results-v4-reveal" aria-labelledby="resultsV4MasterKeyTitle">'''
block='''  <section class="results-v4-naya results-v4-reveal" aria-labelledby="resultsV4NayaTitle">\n    <div class="results-v4-naya-orb" aria-hidden="true"></div>\n    <div>\n      <h4 id="resultsV4NayaTitle">Naya's read on your result</h4>\n      <p id="resultsV4NayaText">Your results are not a verdict. They are a useful signal about where your next improvement can create the most leverage.</p>\n      <div class="results-v4-playground" id="resultsV4Playground" aria-label="Your selected AI territories"></div>\n    </div>\n  </section>\n\n  <section class="results-v4-masterkey results-v4-reveal" aria-labelledby="resultsV4MasterKeyTitle">'''
if 'resultsV4NayaTitle' not in s:
    if anchor not in s: raise RuntimeError('Master Key anchor missing')
    s=s.replace(anchor,block,1)

anchor_js='''  if(resultsV4Build){\n    resultsV4Build.textContent=`${opportunity.name} is your lowest dimension at ${Math.round(opportunity.score)}/100, making it the clearest place to look for leverage.`;\n  }'''
patch_js='''  if(resultsV4Build){\n    resultsV4Build.textContent=`${opportunity.name} is your lowest dimension at ${Math.round(opportunity.score)}/100, making it the clearest place to look for leverage.`;\n  }\n  const resultsV4NayaText=document.getElementById("resultsV4NayaText");\n  if(resultsV4NayaText){\n    resultsV4NayaText.textContent=`If I were sitting beside you looking at this report, I’d focus first on ${opportunity.name}. You already have ${strongest.name} working for you. The opportunity is to use that strength while deliberately building the capability that currently gives you the most room to improve.`;\n  }\n  const resultsV4Playground=document.getElementById("resultsV4Playground");\n  if(resultsV4Playground && state.selectedInterests.size){\n    AI_AREAS.filter(a=>state.selectedInterests.has(a.id)).slice(0,6).forEach(area=>{\n      const tag=document.createElement("span");\n      tag.textContent=area.name;\n      resultsV4Playground.appendChild(tag);\n    });\n  }'''
if 'resultsV4NayaText=document' not in s:
    if anchor_js not in s: raise RuntimeError('Results V4 personalization anchor missing')
    s=s.replace(anchor_js,patch_js,1)

p.write_text(s,encoding='utf-8')
print('contextual Naya and personal playground applied')
