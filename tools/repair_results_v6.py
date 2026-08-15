from pathlib import Path
import re, subprocess, tempfile
p=Path('code'); s=p.read_text(encoding='utf-8')
MARK='MAXESS RESULTS — FRESH FLAGSHIP 2026-08-15'
if MARK not in s: raise SystemExit('fresh Results build not present')
# The fresh CSS was inserted inside the original <style>; flatten it back into that stylesheet.
s=s.replace('<style id="fresh-results-style">','',1)
m=s.find(MARK); close=s.find('</style>',m)
if close>=0: s=s[:close]+s[close+8:]
# Normalize accidental invalid shorthand alpha values.
for a,b in {'#fff.045':'rgba(255,255,255,.045)','#fff.012':'rgba(255,255,255,.012)','#fff.022':'rgba(255,255,255,.022)','#fff0.07':'rgba(255,255,255,.07)','#fff1':'rgba(255,255,255,.1)','#fff2':'rgba(255,255,255,.2)','#fff9':'rgba(255,255,255,.6)'}.items(): s=s.replace(a,b)
# Preserve every DOM contract used by the original assessment engine.
if 'class="fresh-compat"' not in s:
    compat='''<div class="fresh-compat" aria-hidden="true"><div id="scoreStage"></div><span id="overallScore"></span><div id="resultLevel"><span id="resultLevelText"></span></div><span id="resultSubtitle"></span><div id="dimensionConstellation"></div><span id="strongestName"></span><span id="strongestScore"></span><span id="strongestText"></span><span id="opportunityName"></span><span id="opportunityScore"></span><span id="opportunityText"></span><div id="analysisCloud"></div><div id="nextPath"></div><div id="selectedInterests"></div><span id="interestReportIntro"></span><div id="interestReportSection"></div><button id="enterNayaButton" type="button"></button><button id="freeTrialButton" type="button"></button><button id="pdfButton" type="button"></button><button id="restartButton" type="button"></button></div>'''
    end=s.rfind('</div></section>')
    if end<0: raise SystemExit('fresh Results closing boundary missing')
    s=s[:end]+compat+s[end:]
# Add compatibility CSS without touching the assessment styles.
if '.fresh-compat{display:none' not in s:
    s=s.replace('</style>','.fresh-compat{display:none!important}\n</style>',1)
# Validate both original and fresh scripts.
scripts=re.findall(r'<script(?:\s[^>]*)?>([\s\S]*?)</script>',s,re.I)
if len(scripts)<2: raise SystemExit(f'expected at least two script blocks, found {len(scripts)}')
for i,x in enumerate(scripts,1):
    f=Path(tempfile.gettempdir())/f'maxess-v6-{i}.js'; f.write_text(x,encoding='utf-8'); subprocess.run(['node','--check',str(f)],check=True)
assert s.count('id="resultsView"')==1
assert 'MAXESS_ASSESSMENT' in s and 'questionId' in s
p.write_text(s,encoding='utf-8')
print('RESULTS INTEGRATION REPAIRED',len(s.splitlines()),'lines',len(scripts),'scripts')
