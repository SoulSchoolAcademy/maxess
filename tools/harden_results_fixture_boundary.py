from pathlib import Path

TARGET = Path('MAXESS-RESULTS-10-GROOVE.html')

FALLBACK_OLD = '''  window.MAXESS_RESULT = result || {
    resonance: 10.10,
    signature: "LIVING",
    naya: "AWAKENED",
    groove: "MAXIMAL",
    status: "FULL_ACTIVATION",
    timestamp: new Date().toISOString()
  };'''

FALLBACK_NEW = '''  var fixtureMode = new URLSearchParams(window.location.search).get("fixture") === "demo";
  window.MAXESS_RESULT = result || (fixtureMode ? {
    overallScore: 82,
    band: "Advancing",
    dimensions: [
      { id: "1", name: "Direction", score: 86 },
      { id: "2", name: "Communication", score: 91 },
      { id: "3", name: "Evaluation", score: 79 },
      { id: "4", name: "Iteration", score: 74 },
      { id: "5", name: "Systems Thinking", score: 68 }
    ]
  } : null);'''

BRIDGE_OLD = '''    if(window.MAXESS_RESULT&&Array.isArray(window.MAXESS_RESULT.dimensions)&&window.MAXESS_RESULT.dimensions.length>=5)return;
    var score=root.querySelector('.mx-score strong');
    var rows=[].slice.call(root.querySelectorAll('.mx-list-row')).slice(0,5);
    if(!score||rows.length<5)return;
    var dims=rows.map(function(row,i){var n=row.querySelector('b'),s=row.querySelector('strong');return {id:String(i+1),name:n?n.textContent.trim():'Dimension '+(i+1),score:s?Number(s.textContent):0};});
    window.MAXESS_RESULT={overallScore:Number(score.textContent)||0,band:'',dimensions:dims};'''

BRIDGE_NEW = '''    if(!window.MAXESS_RESULT||!Array.isArray(window.MAXESS_RESULT.dimensions)||window.MAXESS_RESULT.dimensions.length<5)return;'''

GUARD = r'''<script id="maxess-result-contract-guard">
(function(){
  'use strict';
  var root=document.getElementById('maxess-results-10');
  if(!root)return;
  var params=new URLSearchParams(window.location.search);
  var fixture=params.get('fixture')==='demo';
  if(window.MAXESS_RESULT){
    root.setAttribute('data-result-state','ready');
    root.setAttribute('data-mode',fixture?'development-fixture':'result-contract');
    return;
  }
  root.setAttribute('data-result-state','awaiting');
  root.innerHTML='<section style="min-height:70vh;display:grid;place-items:center;padding:40px;text-align:center;font-family:Inter,system-ui,sans-serif;background:#030305;color:#fff"><div style="max-width:680px"><div style="font-size:11px;letter-spacing:.18em;font-weight:900;color:#c4a6ff;text-transform:uppercase">MAXESS RESULTS</div><h1 style="font-size:clamp(34px,6vw,72px);line-height:.95;letter-spacing:-.05em;margin:14px 0">Your result is not loaded yet.</h1><p style="color:rgba(255,255,255,.65);font-size:16px;line-height:1.7">Complete the MAXESS assessment and return with your Result Contract. This page does not invent a score when real result data is unavailable.</p></div></section>';
}
})();
</script>
'''

text = TARGET.read_text(encoding='utf-8')
if FALLBACK_OLD not in text:
    raise SystemExit('Expected fake fallback block was not found; refusing blind modification.')
if BRIDGE_OLD not in text:
    raise SystemExit('Expected live-bridge fallback block was not found; refusing blind modification.')
if 'id="maxess-result-contract-guard"' in text:
    raise SystemExit('Guard already present; refusing duplicate patch.')

text = text.replace(FALLBACK_OLD, FALLBACK_NEW, 1)
text = text.replace(BRIDGE_OLD, BRIDGE_NEW, 1)
text = text.replace('<script id="maxess-results-10-behavior">', GUARD + '<script id="maxess-results-10-behavior">', 1)
text = text.replace('data-mode="development-fixture"', 'data-mode="result-contract" data-fixture-available="true"', 1)

TARGET.write_text(text, encoding='utf-8')
print('HARDENED:', TARGET)
print('Development fixture is now opt-in via ?fixture=demo.')
print('No-result production/direct load now renders an explicit awaiting state.')
print('The living-signature bridge no longer creates result data from rendered demo markup.')
