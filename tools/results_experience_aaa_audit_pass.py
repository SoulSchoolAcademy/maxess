from pathlib import Path

p = Path('code')
s = p.read_text(encoding='utf-8')
original = s
MARKER = 'MAXESS RESULTS EXPERIENCE AAA AUDIT PASS'
if MARKER in s:
    print('AAA audit pass already present')
    raise SystemExit(0)

CSS = r'''
/* =========================================================
   MAXESS RESULTS EXPERIENCE AAA AUDIT PASS
   Presentation-density correction after live visual review.
   Rule: if a section reads like a dashboard, simplify it.
========================================================= */
.maxess-oscar-finale{
  border-color:rgba(184,149,255,.24);
  background:
    radial-gradient(circle at 50% -10%,rgba(138,92,255,.17),transparent 42%),
    linear-gradient(145deg,#09070e,#020204 76%);
}
.maxess-oscar-spine .j{
  background:rgba(255,255,255,.012);
  border-color:rgba(184,149,255,.11);
}
.maxess-oscar-spine .gem,
.maxess-oscar-door .door .gem{
  box-shadow:inset 0 2px 4px rgba(255,255,255,.72),0 0 22px rgba(138,92,255,.17),0 8px 15px rgba(0,0,0,.38);
}
.maxess-oscar-spine .t,
.maxess-oscar-door .door span{
  color:#aaa4b3;
  font-size:10px;
  letter-spacing:.05em;
}
.maxess-oscar-path .way h4{font-size:16px}
.maxess-oscar-path .way p{font-size:13px;max-width:390px}
.maxess-oscar-door{background:linear-gradient(145deg,rgba(138,92,255,.055),rgba(255,255,255,.01));}
.maxess-oscar-door p{font-size:14px;color:#b9b2c0}
.maxess-oscar-door .door{
  min-width:165px;
  padding:20px 18px;
  background:rgba(255,255,255,.012);
  border-color:rgba(184,149,255,.14);
}
.maxess-oscar-door .door strong{font-size:14px}
.maxess-oscar-naya{
  background:
    radial-gradient(circle at 9% 0,rgba(138,92,255,.15),transparent 36%),
    linear-gradient(145deg,#0c0911,#030306);
}
.maxess-oscar-final{
  background:
    radial-gradient(circle at 50% 0,rgba(138,92,255,.20),transparent 54%),
    linear-gradient(145deg,#0d0914,#030305);
}

/* Remove the “small text inside lots of boxes” feeling from redundant legacy pieces. */
.maxess-10star-results .maxess-signature-table,
.maxess-10star-results .maxess-aaa-practical,
.maxess-10star-results .maxess-keyline{
  display:none!important;
}
.maxess-10star-results .maxess-meaning,
.maxess-10star-results .maxess-ohwhy,
.maxess-10star-results .maxess-naya-guide{
  border:0;
  box-shadow:none;
  background:transparent;
  padding-left:0;
  padding-right:0;
}
.maxess-10star-results .maxess-meaning h4,
.maxess-10star-results .maxess-ohwhy blockquote{
  max-width:900px;
  font-size:clamp(28px,4vw,48px);
}
.maxess-10star-results .maxess-meaning p,
.maxess-10star-results .maxess-ohwhy p{
  max-width:800px;
  font-size:15px;
  line-height:1.68;
}

/* Eliminate accidental gold dominance in the hero-to-finale path. */
.maxess-oscar-finale .maxess-oscar-spine .gem,
.maxess-oscar-finale .maxess-oscar-door .door .gem{
  background:radial-gradient(circle at 30% 20%,#fff 0,#d9d3ff 13%,#8a5cff 42%,#0a0710 100%) !important;
}
.maxess-oscar-finale .maxess-oscar-spine .j:nth-child(2) .gem,
.maxess-oscar-finale .maxess-oscar-door .door:nth-child(2) .gem{background:radial-gradient(circle at 30% 20%,#fff 0,#d9d3ff 13%,#3ca8ff 42%,#07101a 100%) !important}
.maxess-oscar-finale .maxess-oscar-spine .j:nth-child(3) .gem,
.maxess-oscar-finale .maxess-oscar-door .door:nth-child(3) .gem{background:radial-gradient(circle at 30% 20%,#fff 0,#d9d3ff 13%,#35e39b 42%,#06110b 100%) !important}
.maxess-oscar-finale .maxess-oscar-spine .j:nth-child(4) .gem,
.maxess-oscar-finale .maxess-oscar-door .door:nth-child(4) .gem{background:radial-gradient(circle at 30% 20%,#fff 0,#d9d3ff 13%,#765cff 42%,#0a0710 100%) !important}
.maxess-oscar-finale .maxess-oscar-spine .j:nth-child(5) .gem,
.maxess-oscar-finale .maxess-oscar-door .door:nth-child(5) .gem{background:radial-gradient(circle at 30% 20%,#fff 0,#d9d3ff 13%,#ed42c4 42%,#12050f 100%) !important}

@media(max-width:760px){
  .maxess-oscar-finale .lead{font-size:14px}
  .maxess-oscar-path .way p{font-size:12.5px}
  .maxess-oscar-door .door{min-width:0;width:100%}
}
'''

if '</style>' not in s:
    raise RuntimeError('style closing tag not found')
s = s.replace('</style>', CSS + '\n</style>', 1)

JS = r'''

(function(){
  const root=document.getElementById('resultsView');
  if(!root) return;
  const apply=()=>{
    if(!root.classList.contains('visible')) return;
    root.classList.add('maxess-aaa-audited');
    root.querySelectorAll('.maxess-aaa-pass-placeholder').forEach(el=>el.remove());
    /* Final Oscar composition is the canonical continuation. Hide duplicate legacy
       “opportunity catalogue” and invitation surfaces when present. */
    root.querySelectorAll('.maxess-opportunities,.maxess-naya-masters,.maxess-threshold').forEach(el=>el.remove());
  };
  const obs=new MutationObserver(apply);
  obs.observe(root,{attributes:true,attributeFilter:['class'],childList:true,subtree:true});
  apply();
})();
'''

# Append once inside the last script block.
idx=s.lower().rfind('</script>')
if idx < 0:
    raise RuntimeError('script closing tag not found')
s=s[:idx] + JS + s[idx:]

# Make the audit traceable inside generated source.
s=s.replace('</head>', '\n<!-- ' + MARKER + ' -->\n</head>', 1)

p.write_text(s,encoding='utf-8')
print('AAA presentation-density audit pass applied')
