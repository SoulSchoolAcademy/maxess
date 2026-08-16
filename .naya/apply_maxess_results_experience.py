from pathlib import Path

HTML = Path('MAXESS-RESULTS-10-GROOVE.html')
FRAGMENT = Path('.naya/MAXESS-RESULTS-NAYA-EXPERIENCE-FRAGMENT.html')
MARKER = 'naya-results-experience-v1'

html = HTML.read_text(encoding='utf-8')
fragment = FRAGMENT.read_text(encoding='utf-8')

if MARKER in html:
    print('MAXESS Results Naya experience already applied; no-op.')
    raise SystemExit(0)

required = [
    'window.MAXESS_RESULT',
    'MAXESS-RESULTS-CONTRACT-1',
    'ny-page-inner',
    'ny-youtube-player',
    'Start Your Free Trial',
]
missing = [item for item in required if item not in html]
if missing:
    raise SystemExit('BLOCKED — expected protected functionality missing: ' + ', '.join(missing))

if '</body>' not in html:
    raise SystemExit('BLOCKED — Results artifact has no closing body tag.')

updated = html.replace('</body>', '\n<!-- NAYA RESULTS EXPERIENCE V1 -->\n' + fragment + '\n</body>', 1)

if len(updated) <= len(html):
    raise SystemExit('BLOCKED — zero-change execution.')

for required_fragment in [
    'YOUR AI SCORE',
    'naya-report',
    'your-dimensions',
    'biggest-lever',
    'naya-masters',
    'naya-human-bridge',
    'naya-final-solution',
]:
    if required_fragment not in updated:
        raise SystemExit('BLOCKED — distinctive change proof missing: ' + required_fragment)

HTML.write_text(updated, encoding='utf-8')
print(f'Applied Naya Results experience fragment: {len(html)} -> {len(updated)} bytes')
print('Protected data boundary:', 'window.MAXESS_RESULT' in updated)
print('Protected video:', 'ny-youtube-player' in updated)
print('Protected CTA:', 'Start Your Free Trial' in updated)
print('Distinctive hero:', 'YOUR AI SCORE' in updated)
print('Naya presence:', 'naya-presence' in updated)
print('Human + AI bridge:', 'naya-human-bridge' in updated)
