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

# Release patch: preserve the baseline, remove accidental duplicate responsive blocks,
# and add one visible status rail that communicates progress without replacing existing UI.
s, _ = replace_once(s, '<meta name="maxess-build" content="AAA-2026-08-14">', '<meta name="maxess-build" content="AAA-2026-08-14">\n' + MARKER)

block = '''@media(max-height:820px) and (min-width:761px){\n  .app-inner{padding-top:8px;padding-bottom:10px;}\n  .topbar{padding-bottom:9px;}\n  .board-content{padding-top:22px;padding-bottom:20px;}\n  .command-row{margin-bottom:16px;}\n  .question-title{font-size:36px;}\n  .answers{gap:7px;margin-top:15px;}\n  .answer{min-height:56px;}\n  .jewel{width:45px;height:45px;}\n}\n'''
if s.count(block) > 1:
    first = s.find(block)
    s = s[:first + len(block)] + s[first + len(block):].replace(block, '')

rail_css = '''\n/* =========================================================\n   AAA STATUS RAIL\n========================================================= */\n.aaa-status-rail{width:min(860px,100%);margin:0 auto 14px;display:flex;align-items:center;justify-content:space-between;gap:12px;padding:8px 12px;border:1px solid rgba(255,255,255,.075);border-radius:12px;background:rgba(255,255,255,.025);color:#918d9b;font-size:9px;font-weight:850;letter-spacing:.10em;text-transform:uppercase;}\n.aaa-status-rail strong{color:#d7c9f6;font-weight:950;}\n.aaa-status-rail .aaa-live{display:inline-flex;align-items:center;gap:6px;white-space:nowrap;}\n.aaa-status-rail .aaa-live::before{content:"";width:6px;height:6px;border-radius:50%;background:#35e39b;box-shadow:0 0 10px rgba(53,227,155,.7);}\n'''
s, _ = replace_once(s, '/* =========================================================\n   QUESTION\n========================================================= */', rail_css + '\n\n/* =========================================================\n   QUESTION\n========================================================= */')

s, _ = replace_once(s, '<div class="question-area"', '<div class="aaa-status-rail" aria-live="polite">\n  <span><strong id="aaaStepLabel">STEP 01</strong> · BUILDING YOUR AI PROFILE</span>\n  <span class="aaa-live">ASSESSMENT ACTIVE</span>\n</div>\n\n<div class="question-area"')

s, _ = replace_once(s, '@media(max-width:760px){\n', '@media(max-width:760px){\n\n  .aaa-status-rail{margin-bottom:10px;padding:7px 9px;font-size:8px;}\n\n')

s, _ = replace_once(s, '  questionCountChip:\n    document.getElementById("questionCountChip"),', '  questionCountChip:\n    document.getElementById("questionCountChip"),\n\n  aaaStepLabel:\n    document.getElementById("aaaStepLabel"),')

s, _ = replace_once(s, '  DOM.questionCountChip.textContent=\n    `QUESTION ${current} OF ${total}`;', '  DOM.questionCountChip.textContent=\n    `QUESTION ${current} OF ${total}`;\n\n  if(DOM.aaaStepLabel){\n    DOM.aaaStepLabel.textContent=\n      `STEP ${String(current).padStart(2,"0")}`;\n  }')

s, _ = replace_once(s, '  if(DOM.questionCountChip) DOM.questionCountChip.textContent="FINAL STEP";', '  if(DOM.questionCountChip) DOM.questionCountChip.textContent="FINAL STEP";\n  if(DOM.aaaStepLabel) DOM.aaaStepLabel.textContent="STEP 16 · COMPLETE";')

if s == original:
    print('No changes required; AAA v2 is already applied.')
else:
    PATH.write_text(s, encoding='utf-8')
    print('AAA v2 visible UX pass applied.')
