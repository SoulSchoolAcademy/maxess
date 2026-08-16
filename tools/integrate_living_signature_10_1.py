from pathlib import Path

TARGET = Path('MAXESS-RESULTS-10-GROOVE.html')
ENGINE = Path('MAXESS-LIVE-10-1-ENGINE.js')
MARKER = '<!-- MAXESS-LIVING-SIGNATURE-10.1 -->'

html = TARGET.read_text(encoding='utf-8')
engine = ENGINE.read_text(encoding='utf-8')

if MARKER not in html:
    block = f'{MARKER}\n<script id="maxess-live-10-1-engine">\n{engine}\n</script>\n'
    anchor = '</body>'
    if anchor not in html:
        raise SystemExit('Missing </body> anchor')
    html = html.replace(anchor, block + anchor, 1)
    TARGET.write_text(html, encoding='utf-8')

print('MAXESS Living Signature 10.1 integration applied.')
