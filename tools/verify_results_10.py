#!/usr/bin/env python3
"""Verify the self-optimized Results artifacts with explicit diagnostics."""
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
full=ROOT/'MAXESS-RESULTS-FINAL-GROOVE.html'
embed=ROOT/'MAXESS-RESULTS-FINAL-GROOVE-EMBED.html'
checks=[]
def check(label,ok):
    checks.append((label,bool(ok)))

for p in [full,embed,ROOT/'MAXESS-RESULTS-10-GROOVE.html',ROOT/'MAXESS-RESULTS-GROOVE-EMBED.html',ROOT/'MAXESS-RESULTS-GROOVE-EMBED-9.95.html']:
    check(f'exists:{p.name}',p.exists())

text=full.read_text(encoding='utf-8'); emb=embed.read_text(encoding='utf-8')
check('full-lines>=3000',len(text.splitlines())>=3000)
check('full-bytes>=80000',len(text.encode())>=80000)
check('embed-lines>=3000',len(emb.splitlines())>=3000)
check('embed-bytes>=65000',len(emb.encode())>=65000)
for token in ['MAXESS-RESULTS-CONTRACT-1','Foundation','Developing','Advancing','Mastering','Writing & Communication','Advanced AI Work','Naya — Listen to Your Report','nayanet-foundation-anchor','ny-primary','https://takeyourpowerback.xyz/services','growth-scorecard','maxess-results-experience-manifest']:
    check('full-token:'+token,token in text)
for token in ['nayanet-foundation-anchor','ny-primary','MAXESS-RESULTS-CONTRACT-1','growth-scorecard','maxess-results-experience-manifest']:
    check('embed-token:'+token,token in emb)
for token in ['<!doctype','<html','<head','<body']:
    check('embed-no:'+token,token.lower() not in emb.lower())
check('foundation-button-system',emb.count('ny-button')>=4)
check('foundation-video',('ny-screen-frame' in emb or 'ny-screen' in emb))
failed=[x for x in checks if not x[1]]
for label,ok in checks: print(('PASS ' if ok else 'FAIL ')+label)
if failed:
    raise SystemExit(f'{len(failed)} verification checks failed')
print('DEFINITIVE MAXESS RESULTS RELEASE GATE: PASS')
