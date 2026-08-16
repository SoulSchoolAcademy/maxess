from pathlib import Path

TARGETS = [
    Path('MAXESS-RESULTS-FINAL-GROOVE.html'),
    Path('MAXESS-RESULTS-FINAL-GROOVE-EMBED.html'),
    Path('MAXESS-RESULTS-10-GROOVE.html'),
    Path('MAXESS-RESULTS-GROOVE-EMBED.html'),
    Path('MAXESS-RESULTS-GROOVE-EMBED-9.95.html'),
]
PATCH = Path('MAXESS-LIVING-SIGNATURE-10-10.js')
AUDIO = Path('MAXESS-NAYA-RESULT-AUDIO-9.js')
MARKER = '<!-- MAXESS-LIVING-SIGNATURE-10.10 -->'

patch = PATCH.read_text(encoding='utf-8')
audio = AUDIO.read_text(encoding='utf-8')

fallback_css = r'''<style id="maxess-10-10-fallback-style">
#maxess-results-10 .mx-ls-loading{position:absolute;inset:0;display:grid;place-items:center;text-align:center;color:rgba(255,255,255,.68);font-size:11px;font-weight:800;letter-spacing:.14em;text-transform:uppercase;pointer-events:none}
#maxess-results-10 .mx-ls-loading span{display:block;margin-top:8px;color:rgba(255,255,255,.38);font-size:9px;font-weight:600;letter-spacing:.08em;text-transform:none}
#maxess-results-10[data-result-source="window.MAXESS_RESULT"] .mx-ls-loading{display:none}
</style>'''

fallback = r'''<div class="mx-ls-loading" aria-live="polite">Preparing your MAXESS signature<span>Your result is loading</span></div>'''

legacy_gate = r'''<script id="maxess-modern-browser-gate">\
(function(){\
  'use strict';\
  var modern = !!(window.Promise && window.CustomEvent && document.querySelector && window.requestAnimationFrame);\
  document.documentElement.setAttribute('data-maxess-browser', modern ? 'modern' : 'limited');\
  function neutralize(){\
    var nodes=document.querySelectorAll('body *');\
    for(var i=0;i<nodes.length;i++){\
      var el=nodes[i];\
      if(el.children.length===0){\
        var t=(el.textContent||'').replace(/\\s+/g,' ').trim().toLowerCase();\
        if(t.indexOf("this site doesn't support internet explorer")!==-1 || t.indexOf('this site does not support internet explorer')!==-1){\
          el.style.display='none';\
          if(el.parentElement && el.parentElement.children.length===1) el.parentElement.style.display='none';\
        }\
      }\
    }\
  }\
  if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',neutralize,{once:true});else neutralize();\
  if(window.MutationObserver){new MutationObserver(neutralize).observe(document.documentElement,{childList:true,subtree:true});}\
})();\
</script>'''

anchor = r'''<script id="maxess-live-anchor">\
(function(){\
  function boot(){var el=document.querySelector('.ny-page-inner');if(el&&!el.classList.contains('naya-end'))el.classList.add('naya-end');}\
  if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',boot,{once:true});else boot();\
})();\
</script>'''

no_external_loader = '<script id="maxessLivingSignatureScript"></script>'

block = ('\n' + MARKER + '\n' + fallback_css + '\n' + legacy_gate + '\n'
         + '<div id="maxess-10-10-loading-template" hidden>' + fallback + '</div>\n'
         + no_external_loader + '\n'
         + '<script id="maxess-live-living-signature-engine">\n' + patch + '\n</script>\n'
         + anchor + '\n' + '<script id="maxess-live-naya-audio">\n' + audio + '\n</script>\n')

changed = 0
for target in TARGETS:
    if not target.exists():
        continue
    html = target.read_text(encoding='utf-8')
    if MARKER in html:
        continue
    if '</body>' not in html:
        raise SystemExit(f'Missing </body> anchor in {target}')
    html = html.replace('</body>', block + '</body>', 1)
    changed += 1
    target.write_text(html, encoding='utf-8')

if changed == 0:
    raise SystemExit('No Results artifacts were changed; integration marker may already exist or artifacts are missing.')

print(f'MAXESS Living Signature 10.10 integration applied to {changed} artifact(s).')
