from pathlib import Path

p = Path('tools/results_experience_v4.py')
s = p.read_text(encoding='utf-8')
lines = s.splitlines()
new_anchor = 'ANCHOR = ' + repr('    </div>\n\n  </div>\n\n\n  <!-- ==================================================\n       DIMENSIONS')
for i, line in enumerate(lines):
    if line.startswith('ANCHOR = '):
        lines[i] = new_anchor
        break
else:
    raise RuntimeError('Expected V4 ANCHOR assignment not found')
p.write_text('\n'.join(lines) + '\n', encoding='utf-8')
print('fixed V4 results insertion anchor')
