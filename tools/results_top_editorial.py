from pathlib import Path

p=Path('code')
s=p.read_text(encoding='utf-8')
marker='MAXESS RESULTS TOP EDITORIAL'
if marker in s:
    print('top editorial already present')
    raise SystemExit(0)

CSS=r'''
/* =========================================================
   MAXESS RESULTS TOP EDITORIAL
   Replace the old signal card with a premium editorial opening.
========================================================= */
.maxess-signal{display:none!important}
.maxess-top-editorial{
  max-width:900px;
  margin:34px auto 0;
  padding:0 10px;
  text-align:center;
}
.maxess-top-editorial .kicker{
  color:#b895ff;
  font-size:10px;
  line-height:1;
  letter-spacing:.22em;
  text-transform:uppercase;
  font-weight:950;
}
.maxess-top-editorial h2{
  margin:12px auto 0;
  max-width:820px;
  color:#fff;
  font-size:clamp(30px,5vw,54px);
  line-height:1.02;
  letter-spacing:-.045em;
  font-weight:950;
}
.maxess-top-editorial .score-story{
  max-width:760px;
  margin:16px auto 0;
  color:#d8d2df;
  font-size:clamp(15px,1.8vw,18px);
  line-height:1.62;
}
.maxess-top-editorial .score-story strong{color:#fff}
.maxess-top-editorial .analysis-rule{
  width:72px;
  height:1px;
  margin:28px auto 25px;
  background:linear-gradient(90deg,transparent,#b895ff,transparent);
  box-shadow:0 0 18px rgba(138,92,255,.24);
}
.maxess-top-editorial .analysis-label{
  color:#fff;
  font-size:12px;
  letter-spacing:.08em;
  text-transform:uppercase;
  font-weight:950;
}
.maxess-top-editorial .analysis-copy{
  max-width:780px;
  margin:10px auto 0;
  color:#aaa4b3;
  font-size:15px;
  line-height:1.7;
}
.maxess-top-editorial .work-bridge{
  display:inline-flex;
  align-items:center;
  justify-content:center;
  gap:8px;
  margin-top:23px;
  color:#cfc6dc;
  font-size:10px;
  font-weight:900;
  letter-spacing:.12em;
  text-transform:uppercase;
}
.maxess-top-editorial .work-bridge::before{
  content:"";
  width:6px;
  height:6px;
  border-radius:50%;
  background:#8a5cff;
  box-shadow:0 0 12px rgba(138,92,255,.65);
}
@media(max-width:700px){
  .maxess-top-editorial{margin-top:24px;padding:0 2px}
  .maxess-top-editorial h2{font-size:31px}
  .maxess-top-editorial .score-story{font-size:14px}
  .maxess-top-editorial .analysis-copy{font-size:14px;line-height:1.62}
}
'''
if '</style>' not in s:
    raise RuntimeError('style closing tag missing')
s=s.replace('</style>',CSS+'\n</style>',1)

js=r'''
/* MAXESS RESULTS TOP EDITORIAL */
(function(){
  const root=document.getElementById('resultsView');
  if(!root) return;
  const hero=root.querySelector('.result-hero');
  if(!hero || root.dataset.maxessTopEditorial==='1') return;
  root.dataset.maxessTopEditorial='1';

  const overall=Number(document.getElementById('overallScore')?.textContent||0);
  const dims=[...root.querySelectorAll('#dimensionConstellation .dimension-orb')].map(el=>({
    name:el.querySelector('.dimension-name')?.textContent?.trim()||'capability',
    score:Number(el.querySelector('.dimension-score')?.textContent||0)
  }));
  const strongest=[...dims].sort((a,b)=>b.score-a.score)[0];
  const opportunity=[...dims].sort((a,b)=>a.score-b.score)[0];
  const evidence=document.getElementById('resultsMasterV2Evidence')?.textContent?.trim()||'';

  const section=document.createElement('section');
  section.className='maxess-top-editorial';
  section.setAttribute('aria-labelledby','maxessTopEditorialTitle');
  section.innerHTML=`
    <div class="kicker">YOUR PERSONALIZED ANALYSIS</div>
    <h2 id="maxessTopEditorialTitle">What your score tells the story.</h2>
    <p class="score-story">Your <strong>${Math.round(overall)}/100</strong> is not a grade. It is a snapshot of how you currently work with AI — where you already have momentum, and where the next improvement could create the most leverage.</p>
    <div class="analysis-rule" aria-hidden="true"></div>
    <div class="analysis-label">How you work with AI</div>
    <p class="analysis-copy">Your strongest current capability is <strong>${escapeHtml(strongest?.name||'your strongest dimension')}</strong>${strongest?` at ${Math.round(strongest.score)}/100`:''}. Your clearest opportunity is <strong>${escapeHtml(opportunity?.name||'your next area for growth')}</strong>${opportunity?` at ${Math.round(opportunity.score)}/100`:''}. That gives you a practical place to begin — build from the strength you already have instead of trying to improve everything at once.</p>
    <div class="work-bridge">Explore the evidence behind your result</div>
  `;
  hero.insertAdjacentElement('afterend',section);

  function escapeHtml(v){return String(v).replace(/[&<>'"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;',"'":'&#39;','"':'&quot;'}[c]));}
})();
'''
if '</script>' not in s:
    raise RuntimeError('script closing tag missing')
s=s.replace('</script>', '<script>\n'+js+'\n</script>',1)
p.write_text(s,encoding='utf-8')
print('MAXESS top editorial refinement applied')
