from pathlib import Path

p = Path('tools/results_final_authority.py')
s = p.read_text(encoding='utf-8')
if 'import re\n' not in s:
    s = s.replace('from pathlib import Path\n', 'from pathlib import Path\nimport re\n', 1)
    p.write_text(s, encoding='utf-8')
    print('Added missing re import to final authority transformer')
else:
    print('Final authority transformer already repaired')
