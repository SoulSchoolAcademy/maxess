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

# Keep the NayaNET source physically inside the finished artifact while
# isolating its CSS from the MAXESS Results application with Shadow DOM.
source = source.replace('</script', '<\\/script')
bridge = f'''\n{MARKER}\n<section id="maxess-nayanet-bridge" aria-label="NayaNET experience">\n  <div id="maxess-nayanet-shadow-host"></div>\n</section>\n<script>\n(function(){{\n  const SOURCE = {source!r};\n  const host = document.getElementById('maxess-nayanet-shadow-host');\n  if (!host) return;\n  const root = host.attachShadow ? host.attachShadow({{mode:'open'}}) : host;\n  root.innerHTML = SOURCE;\n  root.querySelectorAll('script').forEach(function(oldScript){{\n    const script = document.createElement('script');\n    for (const attr of oldScript.attributes) script.setAttribute(attr.name, attr.value);\n    script.textContent = oldScript.textContent;\n    oldScript.replaceWith(script);\n  }});\n}})();\n</script>\n'''

page = page[:closing] + bridge + page[closing:]
BASE.write_text(page, encoding='utf-8')

lines = len(page.splitlines())
bytes_ = len(page.encode('utf-8'))
if lines < 5000:
    raise SystemExit(f'AAA build rejected: {lines} lines / {bytes_} bytes; expected 5000+ complete source')

print(f'MAXESS NAYANET MERGED BUILD: {lines} lines / {bytes_} bytes')