from pathlib import Path

HTML = Path('MAXESS-RESULTS-10-GROOVE.html')
FRAGMENT = Path('.naya/MAXESS-RESULTS-NAYA-EXPERIENCE-FRAGMENT.html')
FIX_V2 = Path('.naya/MAXESS-RESULTS-NAYA-EXPERIENCE-FIX-V2.html')
FIX_V3 = Path('.naya/MAXESS-RESULTS-NAYA-EXPERIENCE-FIX-V3.html')
FIX_V4 = Path('.naya/MAXESS-RESULTS-NAYA-EXPERIENCE-FIX-V4.html')
FIX_V5 = Path('.naya/MAXESS-RESULTS-NAYA-EXPERIENCE-FIX-V5.html')
MARKER_V1 = 'naya-results-experience-v1'
MARKER_V2 = 'naya-results-experience-v1-fix'
MARKER_V3 = 'naya-results-experience-v3'
MARKER_V4 = 'maxess-results-v4-refinement'
MARKER_V5 = 'maxess-results-v5-guard'

html = HTML.read_text(encoding='utf-8')
fragment = FRAGMENT.read_text(encoding='utf-8')
fix_v2 = FIX_V2.read_text(encoding='utf-8')
fix_v3 = FIX_V3.read_text(encoding='utf-8')
fix_v4 = FIX_V4.read_text(encoding='utf-8')
fix_v5 = FIX_V5.read_text(encoding='utf-8')

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

if '</body>' not in html or '</html>' not in html:
    raise SystemExit('BLOCKED — Results artifact has no canonical closing tags.')

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
if MARKER_V5 not in updated:
    updated = updated.replace('</body>', '\n<!-- MAXESS RESULTS V5 DATA INTEGRITY -->\n' + fix_v5 + '\n</body>', 1)
    changed = True

# Canonicalize the HTML document. Older execution passes appended style/script
# blocks after </html>. Preserve those bytes, but move them inside <body> so the
# authoritative artifact has exactly one valid document boundary.
close_html = updated.find('</html>')
if close_html == -1:
    raise SystemExit('BLOCKED — missing </html>.')
tail = updated[close_html + len('</html>'):]
if tail.strip():
    body_close = updated.find('</body>', 0, close_html)
    if body_close == -1:
        raise SystemExit('BLOCKED — missing </body> before post-document content.')
    core = updated[:close_html + len('</html>')]
    core_before_body = core[:body_close]
    core_after_body = core[body_close:close_html]
    body_content = core_before_body + tail + '\n' + core_after_body
    updated = body_content
    changed = True

# Remove any accidental duplicate document boundaries introduced by malformed
# historical fragments. Do not remove protected body content.
if updated.count('<html') != 1 or updated.count('</html>') != 1 or updated.count('<body') != 1 or updated.count('</body>') != 1:
    raise SystemExit('BLOCKED — canonical document boundary count failed.')

if not changed:
    print('MAXESS Results experience already applied through V5; no-op.')
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
    'maxess-results-v5-guard',
    'THE HUMAN + AI SYSTEM',
]:
    if required_fragment not in updated:
        raise SystemExit('BLOCKED — distinctive change proof missing: ' + required_fragment)

# Production data integrity: hard-coded demo scores may exist only in the
# explicit fixture branch of the bootstrap. The V5 runtime synchronizer is the
# sole renderer-side bridge from MAXESS_RESULT to displayed scores.
if 'fixtureMode = new URLSearchParams(window.location.search).get("fixture") === "demo"' not in updated:
    raise SystemExit('BLOCKED — explicit fixture boundary missing.')
if 'data-result-state' not in updated:
    raise SystemExit('BLOCKED — result-state guard missing.')

HTML.write_text(updated, encoding='utf-8')
print(f'Applied MAXESS Results patch: {len(html)} -> {len(updated)} bytes')
print('Protected data boundary:', 'window.MAXESS_RESULT' in updated)
print('Protected video:', 'ny-youtube-player' in updated)
print('Protected CTA:', 'Start Your Free Trial' in updated)
print('Canonical document:', updated.count('<html') == 1 and updated.count('</html>') == 1 and updated.count('<body') == 1 and updated.count('</body>') == 1)
print('Distinctive hero:', 'YOUR AI SCORE' in updated)
print('Naya presence:', 'naya-presence' in updated)
print('Human + AI bridge:', 'naya-human-bridge' in updated)
print('V4 refinement:', 'maxess-results-v4-refinement' in updated)
print('V5 data guard:', 'maxess-results-v5-guard' in updated)