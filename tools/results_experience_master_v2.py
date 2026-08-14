from pathlib import Path

p = Path('code')
s = p.read_text(encoding='utf-8')
original = s

MARKER = 'MAXESS RESULTS EXPERIENCE MASTER V2'

CSS = r'''
/* =========================================================
   MAXESS RESULTS EXPERIENCE MASTER V2 — PERSONAL INTELLIGENCE
   Purpose: deepen meaning without replacing existing MAXESS DNA.
========================================================= */
.results-master-v2{margin-top:18px;padding:28px;border:1px solid rgba(184,149,255,.22);border-radius:30px;background:radial-gradient(circle at 92% 0,rgba(78,140,255,.10),transparent 42%),linear-gradient(145deg,rgba(138,92,255,.075),rgba(255,255,255,.018));box-shadow:inset 0 1px 0 rgba(255,255,255,.07),0 18px 45px rgba(0,0,0,.26)}
.results-master-v2-kicker{margin:0;color:#b895ff;font-size:10px;line-height:1;letter-spacing:.18em;text-transform:uppercase;font-weight:950}
.results-master-v2-title{margin:8px 0 0;font-size:clamp(25px,3.6vw,38px);line-height:1.05;letter-spacing:-.035em;font-weight:950;color:#fff}
.results-master-v2-intro{max-width:760px;margin:11px 0 0;color:#bdb7c5;font-size:14px;line-height:1.58;font-weight:600}
.results-master-v2-grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:10px;margin-top:20px}
.results-master-v2-card{min-width:0;padding:18px;border:1px solid rgba(255,255,255,.09);border-radius:22px;background:rgba(255,255,255,.025)}
.results-master-v2-card strong{display:block;color:#fff;font-size:10px;letter-spacing:.14em;text-transform:uppercase;font-weight:950}
.results-master-v2-card p{margin:8px 0 0;color:#bcb7c4;font-size:12px;line-height:1.55;font-weight:600}
.results-master-v2-evidence strong{color:#b895ff}.results-master-v2-meaning strong{color:#3ca8ff}.results-master-v2-next strong{color:#35e39b}
.results-master-v2-disclosure{margin-top:14px;padding-top:13px;border-top:1px solid rgba(255,255,255,.07);color:#8f8997;font-size:10px;line-height:1.55}
.results-master-v2-disclosure b{color:#c9c2d1}
.results-master-v2-territories{margin-top:14px;display:flex;flex-wrap:wrap;gap:7px}
.results-master-v2-territory{padding:7px 10px;border:1px solid rgba(184,149,255,.20);border-radius:999px;background:rgba(138,92,255,.07);color:#d6cee4;font-size:10px;font-weight:850}
@media(max-width:760px){.results-master-v2{padding:23px 20px}.results-master-v2-grid{grid-template-columns:1fr}.results-master-v2-card{padding:16px}.results-master-v2-intro{font-size:13px}}
@media(prefers-reduced-motion:reduce){.results-master-v2{animation:none}}
'''

if MARKER not in s:
    if '</style>' not in s:
        raise RuntimeError('style closing tag not found')
    s = s.replace('</style>', CSS + '\n</style>', 1)

HTML_ANCHOR = '  <section class="results-v4-masterkey results-v4-reveal" aria-labelledby="resultsV4MasterKeyTitle">'
HTML = '''  <section class="results-master-v2 results-v4-reveal" aria-labelledby="resultsMasterV2Title">
    <p class="results-master-v2-kicker">YOUR PERSONAL INTELLIGENCE</p>
    <h3 class="results-master-v2-title" id="resultsMasterV2Title">Here is what your pattern may be telling you.</h3>
    <p class="results-master-v2-intro" id="resultsMasterV2Intro">This section connects your score, dimension pattern, and selected AI territories into one practical interpretation. It is an evidence-based reading of this assessment—not a claim about who you are as a person.</p>
    <div class="results-master-v2-grid">
      <article class="results-master-v2-card results-master-v2-evidence">
        <strong>Evidence</strong>
        <p id="resultsMasterV2Evidence">Your strongest and lowest dimensions will appear here.</p>
      </article>
      <article class="results-master-v2-card results-master-v2-meaning">
        <strong>Interpretation</strong>
        <p id="resultsMasterV2Meaning">Your assessment pattern will be translated into plain language here.</p>
      </article>
      <article class="results-master-v2-card results-master-v2-next">
        <strong>Next move</strong>
        <p id="resultsMasterV2Next">Your highest-leverage learning direction will appear here.</p>
      </article>
    </div>
    <div class="results-master-v2-disclosure"><b>How to read this:</b> Evidence comes directly from your assessment responses. Interpretation is a reasonable inference from that evidence. Recommendations are suggested actions—not predictions or guarantees.</div>
    <div class="results-master-v2-territories" id="resultsMasterV2Territories" aria-label="AI territories that matter to you"></div>
  </section>

'''
if 'id="resultsMasterV2Title"' not in s:
    if HTML_ANCHOR not in s:
        raise RuntimeError('master key anchor not found')
    s = s.replace(HTML_ANCHOR, HTML + HTML_ANCHOR, 1)

JS_ANCHOR = '''  const resultsV4NayaText=document.getElementById("resultsV4NayaText");'''
JS = '''  const resultsMasterV2Evidence=document.getElementById("resultsMasterV2Evidence");
  const resultsMasterV2Meaning=document.getElementById("resultsMasterV2Meaning");
  const resultsMasterV2Next=document.getElementById("resultsMasterV2Next");
  const resultsMasterV2Territories=document.getElementById("resultsMasterV2Territories");
  const strongestScore=Math.round(strongest.score);
  const opportunityScore=Math.round(opportunity.score);
  const strongestTies=results.dimensions.filter(d=>Math.round(d.score)===strongestScore);
  const opportunityTies=results.dimensions.filter(d=>Math.round(d.score)===opportunityScore);
  const strongestNames=strongestTies.map(d=>d.name).join(" and ");
  const opportunityNames=opportunityTies.map(d=>d.name).join(" and ");
  if(resultsMasterV2Evidence){
    resultsMasterV2Evidence.textContent=`Your overall capability snapshot is ${Math.round(results.overall)}/100. Your strongest dimension${strongestTies.length>1?'s':''} ${strongestTies.length>1?'are':'is'} ${strongestNames} at ${strongestScore}/100, while your clearest leverage opportunity${opportunityTies.length>1?'s':''} ${opportunityTies.length>1?'are':'is'} ${opportunityNames} at ${opportunityScore}/100.`;
  }
  if(resultsMasterV2Meaning){
    resultsMasterV2Meaning.textContent=`The useful signal is the pattern, not a single number. ${opportunityMessage(opportunity,opportunity.score)} Your strongest capability can become the foundation you use while developing this next layer.`;
  }
  if(resultsMasterV2Next){
    resultsMasterV2Next.textContent=`Start with ${opportunityNames}: practice one repeatable improvement habit, use the Master Key to evaluate the next result, and turn what works into a reusable method.`;
  }
  if(resultsMasterV2Territories){
    resultsMasterV2Territories.innerHTML="";
    if(state.selectedInterests.size){
      AI_AREAS.filter(a=>state.selectedInterests.has(a.id)).forEach(area=>{
        const tag=document.createElement("span");
        tag.className="results-master-v2-territory";
        tag.textContent=`Matters to you: ${area.name}`;
        resultsMasterV2Territories.appendChild(tag);
      });
    }else{
      const tag=document.createElement("span");
      tag.className="results-master-v2-territory";
      tag.textContent="No AI territory selected — report remains assessment-driven";
      resultsMasterV2Territories.appendChild(tag);
    }
  }

'''
if 'resultsMasterV2Evidence=document' not in s:
    if JS_ANCHOR not in s:
        raise RuntimeError('Naya personalization anchor not found')
    s = s.replace(JS_ANCHOR, JS + JS_ANCHOR, 1)

# Make the existing Naya language explicitly evidence-bounded and interest-safe.
s = s.replace(
    'If I were sitting beside you looking at this report, I’d focus first on ${opportunity.name}. You already have ${strongest.name} working for you. The opportunity is to use that strength while deliberately building the capability that currently gives you the most room to improve.',
    'Looking at the pattern in this assessment, I’d focus first on ${opportunity.name}. You already have ${strongest.name} working for you. The opportunity is to use that strength while deliberately building the capability that currently gives you the most room to improve.'
)

p.write_text(s, encoding='utf-8')
print('MAXESS Results Experience Master V2 applied' if s != original else 'no changes required')
