from pathlib import Path

BASE = Path('MAXESS-RESULTS-9-5-GROOVE.html')
NAYA = Path('nayanetpagecode')
MARKER = '<!-- MAXESS NAYANET MERGED EXPERIENCE v10 -->'

if not BASE.exists():
    raise SystemExit('MAXESS-RESULTS-9-5-GROOVE.html not found')
if not NAYA.exists():
    raise SystemExit('nayanetpagecode not found')

page = BASE.read_text(encoding='utf-8')
source = NAYA.read_text(encoding='utf-8')

if MARKER in page:
    print('MAXESS NAYANET MERGE ALREADY PRESENT')
    raise SystemExit(0)

closing = page.lower().rfind('</body>')
if closing < 0:
    raise SystemExit('Results file has no closing </body>')

source = source.replace('</script', '<\\/script')
manifest = '''<script type="application/json" id="maxess-build-manifest">
{
  "product": "MAXESS AI Mastery Results",
  "release": "9.5",
  "architecture": "Results -> NayaNET",
  "results": "complete personalized results experience",
  "score": "overall MAXESS score and mastery band",
  "profile": "five-dimension visual fingerprint",
  "insight": "strongest capability and next opportunity",
  "pathway": "personalized three-step improvement path",
  "method": "KNOW -> TELL -> ASK -> CREATE -> SCORE -> IMPROVE -> REPEAT",
  "naya": "personalized report entry point",
  "nayanet": "original cinematic experience preserved",
  "video": "existing NayaNET cinematic video",
  "destinations": "Free Gifts, ProMax Player, AI Masterclass, Take Your Power Back",
  "membership": "One Membership / Everything Included",
  "responsive": true,
  "accessible": true,
  "reducedMotion": true,
  "sourceOfTruth": "repository master NayaNET source"
}
</script>
'''
bridge = f'''\n{MARKER}\n{manifest}<section id="maxess-nayanet-bridge" aria-label="NayaNET experience">\n  <div id="maxess-nayanet-shadow-host"></div>\n</section>\n<script>\n(function(){{\n  const SOURCE = {source!r};\n  const host = document.getElementById('maxess-nayanet-shadow-host');\n  if (!host) return;\n  const root = host.attachShadow ? host.attachShadow({{mode:'open'}}) : host;\n  root.innerHTML = SOURCE;\n  root.querySelectorAll('script').forEach(function(oldScript){{\n    const script = document.createElement('script');\n    for (const attr of oldScript.attributes) script.setAttribute(attr.name, attr.value);\n    script.textContent = oldScript.textContent;\n    oldScript.replaceWith(script);\n  }});\n}})();\n</script>\n'''

page = page[:closing] + bridge + page[closing:]
BASE.write_text(page, encoding='utf-8')

lines = len(page.splitlines())
bytes_ = len(page.encode('utf-8'))
if lines < 5000:
    raise SystemExit(f'AAA build rejected: {lines} lines / {bytes_} bytes; expected 5000+ complete source')

print(f'MAXESS NAYANET MERGED BUILD: {lines} lines / {bytes_} bytes')