from pathlib import Path
import re

HTML = Path('MAXESS-RESULTS-10-GROOVE.html')
FRAGMENT = Path('.naya/MAXESS-RESULTS-NAYA-EXPERIENCE-FRAGMENT.html')
FIX_V2 = Path('.naya/MAXESS-RESULTS-NAYA-EXPERIENCE-FIX-V2.html')
FIX_V3 = Path('.naya/MAXESS-RESULTS-NAYA-EXPERIENCE-FIX-V3.html')
FIX_V4 = Path('.naya/MAXESS-RESULTS-NAYA-EXPERIENCE-FIX-V4.html')
FIX_V5 = Path('.naya/MAXESS-RESULTS-NAYA-EXPERIENCE-FIX-V5.html')
FIX_V6 = Path('.naya/MAXESS-RESULTS-NAYA-EXPERIENCE-FIX-V6.html')
MARKER_V1 = 'naya-results-experience-v1'
MARKER_V2 = 'naya-results-experience-v1-fix'
MARKER_V3 = 'naya-results-experience-v3'
MARKER_V4 = 'maxess-results-v4-refinement'
MARKER_V5 = 'maxess-results-v5-guard'
MARKER_V6 = 'maxess-results-v6-naya-profile'

html = HTML.read_text(encoding='utf-8')
fragment = FRAGMENT.read_text(encoding='utf-8')
fix_v2 = FIX_V2.read_text(encoding='utf-8')
fix_v3 = FIX_V3.read_text(encoding='utf-8')
fix_v4 = FIX_V4.read_text(encoding='utf-8')
fix_v5 = FIX_V5.read_text(encoding='utf-8')
fix_v6 = FIX_V6.read_text(encoding='utf-8')

required = ['window.MAXESS_RESULT','MAXESS-RESULTS-CONTRACT-1','ny-page-inner','ny-youtube-player','Start Your Free Trial']
missing = [item for item in required if item not in html]
if missing: raise SystemExit('BLOCKED — expected protected functionality missing: ' + ', '.join(missing))
if '</body>' not in html or '</html>' not in html: raise SystemExit('BLOCKED — Results artifact has no canonical closing tags.')

updated = html
changed = False
for marker, fragment_text in [
    (MARKER_V1, fragment),
    (MARKER_V2, fix_v2),
    (MARKER_V3, fix_v3),
    (MARKER_V4, fix_v4),
    (MARKER_V5, fix_v5),
    (MARKER_V6, fix_v6),
]:
    if marker not in updated:
        updated = updated.replace('</body>', f'\n<!-- {marker.upper()} -->\n{fragment_text}\n</body>', 1)
        changed = True

body_open = updated.find('<body')
body_close = updated.find('</body>', body_open)
html_close = updated.find('</html>', body_close)
if body_open < 0 or body_close < 0 or html_close < 0:
    raise SystemExit('BLOCKED — unable to locate canonical body/html boundaries.')
tail = updated[html_close + len('</html>'):]
if tail.strip():
    tail = re.sub(r'<html[^>]*>', '', tail, flags=re.I)
    tail = re.sub(r'</html\s*>', '', tail, flags=re.I)
    tail = re.sub(r'<body[^>]*>', '', tail, flags=re.I)
    tail = re.sub(r'</body\s*>', '', tail, flags=re.I)
    updated = updated[:body_close] + '\n' + tail.strip() + '\n</body>\n</html>\n'
    changed = True
else:
    updated = updated[:html_close + len('</html>')] + '\n'

positions = {
    'html_open': updated.lower().find('<html'),
    'body_open': updated.lower().find('<body'),
    'body_close': updated.lower().find('</body>'),
    'html_close': updated.lower().find('</html>'),
}
if not (positions['html_open'] >= 0 and positions['body_open'] > positions['html_open'] and positions['body_close'] > positions['body_open'] and positions['html_close'] > positions['body_close']):
    raise SystemExit('BLOCKED — canonical document ordering failed.')

if not changed:
    print('MAXESS Results experience already applied through V6; no-op.')
    raise SystemExit(0)
if len(updated) <= len(html): raise SystemExit('BLOCKED — zero-change execution.')

for required_fragment in ['YOUR AI SCORE','naya-report','your-dimensions','biggest-lever','naya-masters','naya-human-bridge','naya-final-solution','THE HUMAN + AI SYSTEM',MARKER_V2,MARKER_V3,MARKER_V4,MARKER_V5,MARKER_V6.upper(),'maxess-naya-profile-v6','Naya%20Profile%20white.jpg']:
    if required_fragment not in updated: raise SystemExit('BLOCKED — distinctive change proof missing: ' + required_fragment)
if 'fixtureMode = new URLSearchParams(window.location.search).get("fixture") === "demo"' not in updated: raise SystemExit('BLOCKED — explicit fixture boundary missing.')
if 'data-result-state' not in updated: raise SystemExit('BLOCKED — result-state guard missing.')

HTML.write_text(updated, encoding='utf-8')
print(f'Applied MAXESS Results patch: {len(html)} -> {len(updated)} bytes')
print('Protected data boundary:', 'window.MAXESS_RESULT' in updated)
print('Protected video:', 'ny-youtube-player' in updated)
print('Protected CTA:', 'Start Your Free Trial' in updated)
print('Canonical document ordering:', positions)
print('Distinctive hero:', 'YOUR AI SCORE' in updated)
print('Naya presence:', 'naya-presence' in updated)
print('V5 data guard:', MARKER_V5 in updated)
print('V6 Naya profile:', MARKER_V6.upper() in updated and 'maxess-naya-profile-v6' in updated)