from pathlib import Path

TARGETS = [
    Path('MAXESS-RESULTS-FINAL-GROOVE.html'),
    Path('MAXESS-RESULTS-FINAL-GROOVE-EMBED.html'),
    Path('MAXESS-RESULTS-10-GROOVE.html'),
    Path('MAXESS-RESULTS-GROOVE-EMBED.html'),
    Path('MAXESS-RESULTS-GROOVE-EMBED-9.95.html'),
]
PATCH = Path('MAXESS-LIVING-SIGNATURE-10-PATCH.js')
AUDIO = Path('MAXESS-NAYA-RESULT-AUDIO-9.js')
MARKER = '<!-- MAXESS-LIVING-SIGNATURE-10.1 -->'

patch = PATCH.read_text(encoding='utf-8')
audio = AUDIO.read_text(encoding='utf-8')

bridge = r'''<script id="maxess-result-live-bridge">\
(function(){\
  function boot(){\
    var root=document.getElementById('maxess-results-10');\
    if(!root)return;\
    if(window.MAXESS_RESULT&&Array.isArray(window.MAXESS_RESULT.dimensions)&&window.MAXESS_RESULT.dimensions.length>=5)return;\
    var score=root.querySelector('.mx-score strong');\
    var rows=[].slice.call(root.querySelectorAll('.mx-list-row')).slice(0,5);\
    if(!score||rows.length<5)return;\
    var dims=rows.map(function(row,i){var n=row.querySelector('b'),s=row.querySelector('strong');return {id:String(i+1),name:n?n.textContent.trim():'Dimension '+(i+1),score:s?Number(s.textContent):0};});\
    window.MAXESS_RESULT={overallScore:Number(score.textContent)||0,band:'',dimensions:dims};\
  }\
  if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',function(){setTimeout(boot,0)},{once:true});else boot();\
})();\
</script>'''

anchor = r'''<script id="maxess-live-anchor">\
(function(){\
  function boot(){var el=document.querySelector('.ny-page-inner');if(el&&!el.classList.contains('naya-end'))el.classList.add('naya-end');}\
  if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',boot,{once:true});else boot();\
})();\
</script>'''

no_external_loader = '<script id="maxessLivingSignatureScript"></script>'

block = ('\n' + MARKER + '\n' + bridge + '\n' + no_external_loader + '\n'
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
    target.write_text(html.replace('</body>', block + '</body>', 1), encoding='utf-8')
    changed += 1

if changed == 0:
    raise SystemExit('No Results artifacts were changed; integration marker may already exist or artifacts are missing.')

print(f'MAXESS Living Signature 10.1 integration applied to {changed} artifact(s).')
