from pathlib import Path

HTML = Path('MAXESS-RESULTS-10-GROOVE.html')
FRAGMENT = Path('.naya/MAXESS-RESULTS-NAYA-EXPERIENCE-FRAGMENT.html')
FIX_V2 = Path('.naya/MAXESS-RESULTS-NAYA-EXPERIENCE-FIX-V2.html')
FIX_V3 = Path('.naya/MAXESS-RESULTS-NAYA-EXPERIENCE-FIX-V3.html')
FIX_V4 = Path('.naya/MAXESS-RESULTS-NAYA-EXPERIENCE-FIX-V4.html')
MARKER_V1 = 'naya-results-experience-v1'
MARKER_V2 = 'naya-results-experience-v1-fix'
MARKER_V3 = 'naya-results-experience-v3'
MARKER_V4 = 'maxess-results-v4-refinement'

html = HTML.read_text(encoding='utf-8')
fragment = FRAGMENT.read_text(encoding='utf-8')
fix_v2 = FIX_V2.read_text(encoding='utf-8')
fix_v3 = FIX_V3.read_text(encoding='utf-8')
fix_v4 = FIX_V4.read_text(encoding='utf-8')

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

updated = html
changed = False

if MARKER_V1 not in updated:
    updated = updated.replace('</body>', '\n<!-- NAYA RESULTS EXPERIENCE V1 -->\n' + fragment + '\n</body>', 1)
    changed = True

if MARKER_V2 not in updated:
    updated = updated.replace('</body>', '\n<!-- NAYA RESULTS EXPERIENCE FIX V2 -->\n' + fix_v2 + '\n</body>', 1)
    changed = True

if MARKER_V3 not in updated:
    updated = updated.replace('</body>', '\n<!-- NAYA RESULTS EXPERIENCE FIX V3 -->\n' + fix_v3 + '\n</body>', 1)
    changed = True

if MARKER_V4 not in updated:
    updated = updated.replace('</body>', '\n<!-- MAXESS RESULTS V4 REFINEMENT -->\n' + fix_v4 + '\n</body>', 1)
    changed = True

if not changed:
    print('MAXESS Results Naya experience already applied through V4; no-op.')
    raise SystemExit(0)

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
    'naya-results-experience-v1-fix',
    'naya-results-experience-v3',
    'maxess-results-v4-refinement',
    'THE HUMAN + AI SYSTEM',
]:
    if required_fragment not in updated:
        raise SystemExit('BLOCKED — distinctive change proof missing: ' + required_fragment)

HTML.write_text(updated, encoding='utf-8')
print(f'Applied MAXESS Results experience patch: {len(html)} -> {len(updated)} bytes')
print('Protected data boundary:', 'window.MAXESS_RESULT' in updated)
print('Protected video:', 'ny-youtube-player' in updated)
print('Protected CTA:', 'Start Your Free Trial' in updated)
print('Distinctive hero:', 'YOUR AI SCORE' in updated)
print('Naya presence:', 'naya-presence' in updated)
print('Human + AI bridge:', 'naya-human-bridge' in updated)
print('Naya asset correction:', 'grok-image-f75a6f12-4e3a-4c99-a334-5684ba0f7401.jpg' in updated and 'grok-image-c6a924fd-1f75-4ac8-840d-35b224fb3e52.jpg' in updated)
print('Hero purity:', 'naya-results-experience-v3' in updated)
print('V4 refinement:', 'maxess-results-v4-refinement' in updated)