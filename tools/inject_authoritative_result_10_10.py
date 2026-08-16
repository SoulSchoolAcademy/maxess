#!/usr/bin/env python3
"""Inject the single development Result Contract before any Results renderer runs.

Production rule: the assessment/application owns window.MAXESS_RESULT. This file
only provides the repository's deterministic fixture for standalone Groove QA.
It never scrapes rendered HTML and never calculates scores.
"""
from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'tools'))
from build_maxess_results_10_self_optimized import FIXTURE  # noqa: E402

FILES = [
    ROOT / 'MAXESS-RESULTS-FINAL-GROOVE.html',
    ROOT / 'MAXESS-RESULTS-FINAL-GROOVE-EMBED.html',
    ROOT / 'MAXESS-RESULTS-10-GROOVE.html',
    ROOT / 'MAXESS-RESULTS-GROOVE-EMBED.html',
    ROOT / 'MAXESS-RESULTS-GROOVE-EMBED-9.95.html',
]
MARKER = 'MAXESS_RESULT_BOOTSTRAP_10_10'


def payload():
    dimensions = []
    for name, score, meaning, action in FIXTURE['dimensions']:
        dimensions.append({
            'id': name.lower().replace(' ', '-'),
            'name': name,
            'score': score,
            'description': meaning,
            'insight': action,
        })
    result = {
        'schema': 'MAXESS-RESULT-1',
        'mode': FIXTURE['mode'],
        'overallScore': FIXTURE['score'],
        'band': FIXTURE['band'],
        'dimensions': dimensions,
        'areas': [{'name': n, 'description': d} for n, d in FIXTURE['areas']],
    }
    return json.dumps(result, ensure_ascii=False, separators=(',', ':'))


BOOTSTRAP = '<script type="application/json" id="MAXESS_RESULT_BOOTSTRAP_10_10">' + payload() + '</script><script id="maxess-result-contract-10-10">window.MAXESS_RESULT=window.MAXESS_RESULT||JSON.parse(document.getElementById(\'MAXESS_RESULT_BOOTSTRAP_10_10\').textContent);</script>'

changed = 0
for path in FILES:
    if not path.exists():
        continue
    text = path.read_text(encoding='utf-8')
    if MARKER in text:
        continue
    if '</head>' not in text:
        raise SystemExit(f'Missing </head> anchor: {path}')
    text = text.replace('</head>', BOOTSTRAP + '\n</head>', 1)
    path.write_text(text, encoding='utf-8')
    changed += 1

if changed == 0:
    raise SystemExit('No artifacts received the Result Contract bootstrap.')
print(f'Injected authoritative MAXESS_RESULT development contract into {changed} artifacts.')
