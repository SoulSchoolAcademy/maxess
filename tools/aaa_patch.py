from pathlib import Path

PATH = Path('code')
MARKER = '<meta name="maxess-aaa-pass" content="2026-08-14-v2">'

def replace_once(text, old, new):
    if new in text:
        return text, False
    if old not in text:
        raise RuntimeError(f'Anchor not found: {old[:80]!r}')
    return text.replace(old, new, 1), True

s = PATH.read_text(encoding='utf-8')
original = s

# 1. Make the release state visible and unambiguous.
s, _ = replace_once(
    s,
    '<meta name="maxess-build" content="AAA-2026-08-14">',
    '<meta name="maxess-build" content="AAA-2026-08-14">\n' + MARKER
)

# 2. Remove accidental repeated short-screen media blocks from prior automated passes.
block = '''@media(max-height:820px) and (min-width:761px){\n  .app-inner{padding-top:8px;padding-bottom:10px;}\n  .topbar{padding-bottom:9px;}\n  .board-content{padding-top:22px;padding-bottom:20px;}\n  .command-row{margin-bottom:16px;}\n  .question-title{font-size:36px;}\n  .answers{gap:7px;margin-top:15px;}\n  .answer{min-height:56px;}\n  .jewel{width:45px;height:45px;}\n}\n'''
count = s.count(block)
if count > 1:
    first = s.find(block)
    before = s[:first + len(block)]
    after = s[first + len(block):].replace(block, '')
    s = before + after

# 3. Add a clearly visible, compact assessment-status rail without replacing the existing HUD.
rail_css = '''\n/* =========================================================\n   AAA STATUS RAIL\n========================================================= */\n\n.aaa-status-rail{\n  width:min(860px,100%);\n  margin:0 auto 14px;\n  display:flex;\n  align-items:center;\n  justify-content:space-between;\n  gap:12px;\n  padding:8px 12px;\n  border:1px solid rgba(255,255,255,.075);\n  border-radius:12px;\n  background:rgba(255,255,255,.025);\n  color:#918d9b;\n  font-size:9px;\n  font-weight:850;\n  letter-spacing:.10em;\n  text-transform:uppercase;\n}\n\n.aaa-status-rail strong{\n  color:#d7c9f6;\n  font-weight:950;\n}\n\n.aaa-status-rail .aaa-live{\n  display:inline-flex;\n  align-items:center;\n  gap:6px;\n  white-space:nowrap;\n}\n\n.aaa-status-rail .aaa-live::before{\n  content:"";\n  width:6px;\n  height:6px;\n  border-radius:50%;\n  background:#35e39b;\n  box-shadow:0 0 10px rgba(53,227,155,.7);\n}\n'''
s, _ = replace_once(s, '/* =========================================================\n   QUESTION\n========================================================= */', rail_css + '\n\n/* =========================================================\n   QUESTION\n========================================================= */')

# 4. Add a semantic status rail to the question stage. This is intentionally additive.
html_anchor = '<div class="question-area"'
html_new = '''<div class="aaa-status-rail" aria-live="polite">\n  <span><strong id="aaaStepLabel">STEP 01</strong> · BUILDING YOUR AI PROFILE</span>\n  <span class="aaa-live">ASSESSMENT ACTIVE</span>\n</div>\n\n<div class="question-area"'''
s, _ = replace_once(s, html_anchor, html_new)

# 5. Give the rail enough room on small screens while keeping it quiet.
mobile_anchor = '@media(max-width:760px){\n'
mobile_css = '''@media(max-width:760px){\n\n  .aaa-status-rail{\n    margin-bottom:10px;\n    padding:7px 9px;\n    font-size:8px;\n  }\n\n'''
s, _ = replace_once(s, mobile_anchor, mobile_css)

# 6. Wire the rail to the same question state as the existing progress system.
s, _ = replace_once(
    s,
    '  questionCountChip:\n    document.getElementById("questionCountChip"),',
    '  questionCountChip:\n    document.getElementById("questionCountChip"),\n\n  aaaStepLabel:\n    document.getElementById("aaaStepLabel"),'
)

s, _ = replace_once(
    s,
    '  DOM.questionCountChip.textContent=\n    `QUESTION ${current} OF ${total}`;',
    '  DOM.questionCountChip.textContent=\n    `QUESTION ${current} OF ${total}`;\n\n  if(DOM.aaaStepLabel){\n    DOM.aaaStepLabel.textContent=\n      `STEP ${String(current).padStart(2,"0")}`;\n  }'
)

# 7. Ensure the final personalization state also communicates completion cleanly.
s, _ = replace_once(
    s,
    '  if(DOM.questionCountChip) DOM.questionCountChip.textContent="FINAL STEP";',
    '  if(DOM.questionCountChip) DOM.questionCountChip.textContent="FINAL STEP";\n  if(DOM.aaaStepLabel) DOM.aaaStepLabel.textContent="STEP 16 · COMPLETE";'
)

if s == original:
    print('No changes required; AAA pass already applied.')
else:
    PATH.write_text(s, encoding='utf-8')
    print('AAA v2 pass applied.')
