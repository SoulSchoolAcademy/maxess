from pathlib import Path

p = Path('code')
s = p.read_text(encoding='utf-8')
MARKER = 'MAXESS RESULTS EXPERIENCE CANONICAL CLEANUP'

CSS = r'''
/* =========================================================
   MAXESS RESULTS EXPERIENCE CANONICAL CLEANUP
   One experience. One hierarchy. No legacy pile-up.
========================================================= */
.maxess-canonical-hide{display:none!important}
.maxess-canonical-spacer{height:0!important;margin:0!important;padding:0!important;border:0!important}

/* Preserve the premium core; remove report/dashboard residue. */
#resultsView .results-v4-intro,
#resultsView .results-master-v2,
#resultsView .results-v4-naya,
#resultsView .results-v4-masterkey,
#resultsView .final-cta,
#resultsView .maxess-signal,
#resultsView .maxess-meaning,
#resultsView .maxess-ohwhy,
#resultsView .maxess-naya-guide,
#resultsView .maxess-masterkey-10,
#resultsView .maxess-opportunities,
#resultsView .maxess-naya-masters,
#resultsView .maxess-threshold,
#resultsView .maxess-results-journey,
#resultsView .results-v4-playground,
#resultsView .results-v4-treasure,
#resultsView .results-v4-pathway,
#resultsView .results-v4-cta,
#resultsView .results-v4-method,
#resultsView .results-v4-evidence,
#resultsView .results-v4-recommendation,
#resultsView .results-v4-next,
#resultsView .results-master-v2-next,
#resultsView .results-master-v2-evidence,
#resultsView .results-master-v2-meaning{
  display:none!important;
}

/* Let the canonical sections breathe instead of behaving like nested cards. */
#resultsView .maxess-personal-editorial{
  margin-top:30px;
  margin-bottom:14px;
}
#resultsView .maxess-signature-shell{
  margin-top:58px;
}
#resultsView .maxess-oscar-finale{
  margin-top:68px;
}

/* Remove accidental empty vertical gaps left by deleted legacy sections. */
#resultsView > .report-section:empty,
#resultsView > .results-v4-reveal:empty{
  display:none!important;
}

@media(max-width:760px){
  #resultsView .maxess-signature-shell{margin-top:42px}
  #resultsView .maxess-oscar-finale{margin-top:44px}
}
'''

if f'/* {MARKER}' not in s:
    s = s.replace('</style>', CSS + '\n</style>', 1)

JS = r'''

(function(){
  const CANONICAL_CLASSES = [
    '.results-v4-intro','.results-master-v2','.results-v4-naya','.results-v4-masterkey','.final-cta',
    '.maxess-signal','.maxess-meaning','.maxess-ohwhy','.maxess-naya-guide','.maxess-masterkey-10',
    '.maxess-opportunities','.maxess-naya-masters','.maxess-threshold','.maxess-results-journey',
    '.results-v4-playground','.results-v4-treasure','.results-v4-pathway','.results-v4-cta',
    '.results-v4-method','.results-v4-evidence','.results-v4-recommendation','.results-v4-next',
    '.results-master-v2-next','.results-master-v2-evidence','.results-master-v2-meaning'
  ];

  function cleanup(root){
    if(!root || !root.classList.contains('visible')) return;
    root.classList.add('maxess-canonical-clean');

    /* Remove legacy/generated duplicate sections from the actual DOM. */
    CANONICAL_CLASSES.forEach(selector=>{
      root.querySelectorAll(selector).forEach(el=>el.remove());
    });

    /* Remove empty report containers created by removed sections. */
    root.querySelectorAll(':scope > .report-section').forEach(section=>{
      const text=(section.textContent||'').replace(/\s+/g,'').trim();
      const visibleChild=[...section.children].some(c=>getComputedStyle(c).display!=='none');
      if(!text || !visibleChild) section.remove();
    });

    /* The result page has one canonical emotional sequence. */
    const hero=root.querySelector('.result-hero');
    const editorial=root.querySelector('.maxess-personal-editorial');
    const signature=root.querySelector('.maxess-signature-shell');
    const finale=root.querySelector('.maxess-oscar-finale');

    if(hero) hero.dataset.canonical='hero';
    if(editorial) editorial.dataset.canonical='personal-analysis';
    if(signature) signature.dataset.canonical='capability-signature';
    if(finale) finale.dataset.canonical='next-chapter';

    /* Remove stray standalone text blocks that are not part of the canonical composition. */
    root.querySelectorAll(':scope > p').forEach(p=>{
      if(!p.closest('.result-hero,.maxess-personal-editorial,.maxess-signature-shell,.maxess-oscar-finale')) p.remove();
    });
  }

  const root=document.getElementById('resultsView');
  if(!root) return;
  const apply=()=>cleanup(root);
  const obs=new MutationObserver(()=>apply());
  obs.observe(root,{attributes:true,attributeFilter:['class'],childList:true,subtree:true});
  apply();
})();
'''

if MARKER not in s:
    idx = s.lower().rfind('</script>')
    if idx < 0:
        raise RuntimeError('script closing tag not found')
    s = s[:idx] + JS + s[idx:]

s = s.replace('</head>', f'\n<!-- {MARKER} -->\n</head>', 1) if f'<!-- {MARKER} -->' not in s else s
p.write_text(s, encoding='utf-8')
print('Canonical Results cleanup applied')
