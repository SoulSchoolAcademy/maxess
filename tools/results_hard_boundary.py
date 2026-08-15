from pathlib import Path

p = Path('code')
s = p.read_text(encoding='utf-8')
MARK = 'MAXESS RESULTS HARD BOUNDARY'
if MARK in s:
    print('Hard boundary already present')
    raise SystemExit(0)

CSS = r'''
/* =========================================================
   MAXESS RESULTS HARD BOUNDARY
   The live Results surface owns the presentation.
========================================================= */
/* Fail-safe: old Results UI is invisible even before JS mounts. */
#resultsView > :not(.result-hero):not(.results-hard-output){
  display:none !important;
}
#resultsView .result-hero{
  position:relative;
  background:transparent !important;
  border:0 !important;
  box-shadow:none !important;
  overflow:visible !important;
  isolation:isolate;
}
#resultsView .result-hero::before,
#resultsView .result-hero::after,
#resultsView .result-hero .score-stage::before,
#resultsView .result-hero .score-stage::after{
  display:none !important;
  content:none !important;
}
#resultsView .results-hard-output{display:block !important;}
'''

JS = r'''
/* =========================================================
   MAXESS RESULTS HARD BOUNDARY
========================================================= */
(function(){
  const root=document.getElementById('resultsView');
  if(!root) return;

  const scrubCodeText=()=>{
    const rx=/function\s*\(|document\.getElementById|const\s+[A-Za-z_$][\w$]*\s*=|querySelector\s*\(/;
    const walker=document.createTreeWalker(document.body,NodeFilter.SHOW_TEXT);
    const kill=[];
    while(walker.nextNode()){
      const node=walker.currentNode;
      const parent=node.parentElement;
      if(parent && /^(SCRIPT|STYLE|NOSCRIPT)$/i.test(parent.tagName)) continue;
      if(rx.test(node.nodeValue||'')) kill.push(node);
    }
    kill.forEach(n=>n.remove());
  };

  const mount=()=>{
    if(!root.classList.contains('visible') || root.dataset.resultsHardBoundary==='1') return;
    const hero=root.querySelector(':scope > .result-hero');
    if(!hero) return;

    root.classList.add('results-hard-boundary');
    root.dataset.resultsHardBoundary='1';

    [...root.children].forEach(child=>{
      if(child!==hero) child.remove();
    });

    const score=Math.round(Number(document.getElementById('overallScore')?.textContent||0));
    const dims=[...root.querySelectorAll('#dimensionConstellation .dimension-orb')].map((el,i)=>({
      name:el.querySelector('.dimension-name')?.textContent?.trim()||['Direction','Communication','Evaluation','Iteration','Systems Thinking'][i]||'Dimension',
      score:Number(el.querySelector('.dimension-score')?.textContent||0)
    }));
    dims.sort((a,b)=>b.score-a.score);
    const hi=dims[0]||{name:'Direction',score:score};
    const lo=dims[dims.length-1]||hi;
    const escape=(v)=>String(v==null?'':v).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));

    const out=document.createElement('section');
    out.className='results-hard-output';
    out.innerHTML=`
      <section class="rr-clean-intro">
        <div class="rr-kicker">YOUR PERSONALIZED ANALYSIS</div>
        <h3>What your score tells your story.</h3>
        <p>You already have a real advantage in <em>${escape(hi.name)}</em>. Your next meaningful lift is in <em>${escape(lo.name).toLowerCase()}</em>.</p>
      </section>

      <section class="rr-clean-fingerprint">
        <div class="rr-kicker">YOUR AI FINGERPRINT</div>
        <h3>The shape underneath your score.</h3>
        <div class="rr-fingerprint-grid">
          ${dims.map(d=>`<div class="rr-fingerprint-point"><span>${escape(d.name)}</span><strong>${Math.round(d.score)}</strong></div>`).join('')}
        </div>
      </section>

      <section class="rr-clean-system">
        <div class="rr-kicker">HOW YOU WORK WITH AI</div>
        <h3>AI is the engine.<br><em>You are the director.</em></h3>
        <div class="rr-clean-sequence">${['KNOW','TELL','ASK','LOOK','SCORE','IMPROVE','REPEAT'].map(x=>`<span>${x}</span>`).join('<b>→</b>')}</div>
      </section>

      <section class="rr-clean-naya">
        <div class="rr-clean-orb">N</div>
        <div>
          <div class="rr-kicker">NAYA · PERSONAL GUIDE</div>
          <h3>“Okay. Now we know where to look.”</h3>
          <p>Keep the capability that's already working. Practice the one that creates the most leverage. Then use that combination to make something real.</p>
        </div>
      </section>

      <section class="rr-clean-master">
        <div class="rr-kicker">NAYA · MASTER INTELLIGENCE</div>
        <h3>Specific work deserves specific mastery.</h3>
        <div class="rr-master-focus">
          <div class="rr-jewel rr-purple">✦</div><div><strong>Naya Master ${escape(hi.name)}</strong><span>Your natural advantage</span></div>
          <div class="rr-jewel rr-blue">◆</div><div><strong>Naya Master ${escape(lo.name)}</strong><span>Your leverage opportunity</span></div>
          <div class="rr-jewel rr-green">△</div><div><strong>Naya Master Strategist</strong><span>Turn intent into action</span></div>
        </div>
      </section>

      <section class="rr-clean-final">
        <div class="rr-kicker">YOUR NEXT CHAPTER</div>
        <h3>Now make the capability real.</h3>
        <p>Your result shows you where you are. The next step is choosing what you want to build with it.</p>
        <div class="rr-clean-actions"><button type="button" data-rh-go>MASTER AI</button><button type="button" data-rh-save>SAVE MY RESULTS</button></div>
      </section>
    `;

    hero.insertAdjacentElement('afterend',out);
    out.querySelector('[data-rh-go]')?.addEventListener('click',()=>document.getElementById('freeTrialButton')?.click());
    out.querySelector('[data-rh-save]')?.addEventListener('click',()=>document.getElementById('pdfButton')?.click());
    scrubCodeText();
  };

  const observer=new MutationObserver(()=>mount());
  observer.observe(root,{attributes:true,attributeFilter:['class']});
  mount();
})();
'''

if '</style>' not in s:
    raise RuntimeError('style closing tag missing')
s=s.replace('</style>',CSS+'\n</style>',1)
if '</script>' not in s:
    raise RuntimeError('script closing tag missing')
pos=s.rfind('</script>')
s=s[:pos]+'\n'+JS+'\n'+s[pos:]
p.write_text(s,encoding='utf-8')
print('Applied MAXESS Results hard boundary')
