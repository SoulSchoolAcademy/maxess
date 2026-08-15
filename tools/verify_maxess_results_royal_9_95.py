from pathlib import Path
import re

OUT = Path('MAXESS-RESULTS-10-GROOVE.html')
s = OUT.read_text(encoding='utf-8')
royal = s[s.find('<main id="royal-results-995"'):]
master_seed = re.findall(r"\['[^']+','[^']+','[^']+'\]", s)
checks = {
    'royal_marker': 'MAXESS_RESULTS_ROYAL_9_95' in s,
    'royal_root': '<main id="royal-results-995"' in s,
    'naya_person': 'rr-naya-avatar' in royal and 'rr-naya-halo' in royal,
    'naya_feature_language': 'Naya is not a button.' in royal,
    'master_library': 'const MASTERS=[' in s and len(master_seed) >= 18,
    'master_count_data': 'Writing & Communication' in s and 'Advanced AI Work' in s,
    'five_dimensions': all(x in s for x in ['Direction','Communication','Evaluation','Iteration','Systems Thinking']),
    'no_iframe': '<iframe' not in royal.lower(),
    'nayanet_destination': 'https://nayanet.xyz/' in royal,
    'purple_white_black': '--royal-purple:' in s and '--royal-white:' in s and '--royal-bg:' in s,
    'responsive': '@media(max-width:720px)' in s,
    'reduced_motion': 'prefers-reduced-motion' in s,
    'substantial': len(s.splitlines()) >= 3000 and len(s.encode('utf-8')) >= 90000,
}
for k, v in checks.items():
    print(f'{k}: {"PASS" if v else "FAIL"}')
print('MASTER SOURCE ENTRIES:', len(master_seed))
if not all(checks.values()):
    raise SystemExit('ROYAL 9.95 STRUCTURAL VERIFICATION FAILED')
print('ROYAL 9.95 STRUCTURAL VERIFICATION PASS')
