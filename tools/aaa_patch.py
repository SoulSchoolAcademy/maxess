from pathlib import Path
import re

PATH = Path('code')
BUILD = 'AAA-2026-08-14-v3'
MARKER = '<meta name="maxess-aaa-pass" content="2026-08-14-v3">'

def replace_once(text, old, new):
    if new in text:
        return text, False
    if old not in text:
        raise RuntimeError(f'Anchor not found: {old[:120]!r}')
    return text.replace(old, new, 1), True

s = PATH.read_text(encoding='utf-8')
original = s

# RELEASE IDENTITY
for old in [
    '<meta name="maxess-build" content="AAA-2026-08-14">',
    '<meta name="maxess-aaa-pass" content="2026-08-14-v2">',
]:
    s = s.replace(old, '')
s, _ = replace_once(s, '<title>MAXESS — AI Mastery Assessment</title>', '<title>MAXESS — AI Mastery Assessment</title>\n<meta name="maxess-build" content="AAA-2026-08-14-v3">\n' + MARKER)

# V3 visible design pass.
v3_css = r'''
/* =========================================================
   MAXESS AAA V3 — VISIBLE CRAFT PASS
========================================================= */
:root{
  --aaa-glass:rgba(255,255,255,.045);
  --aaa-glass-strong:rgba(255,255,255,.075);
  --aaa-purple-glow:rgba(138,92,255,.28);
  --aaa-border:rgba(184,149,255,.22);
}
.maxess-app{
  background:
    radial-gradient(circle at 50% -8%,rgba(138,92,255,.24),transparent 32%),
    radial-gradient(circle at 88% 42%,rgba(237,66,196,.07),transparent 28%),
    radial-gradient(circle at 12% 76%,rgba(60,168,255,.06),transparent 26%),
    #020204;
}
.topbar{padding-top:7px;}
.brand{
  position:relative;padding:10px 13px;border:1px solid rgba(184,149,255,.16);
  border-radius:14px;background:linear-gradient(180deg,rgba(255,255,255,.055),rgba(255,255,255,.015));
  box-shadow:inset 0 1px 0 rgba(255,255,255,.08),0 8px 24px rgba(0,0,0,.28);
}
.brand::after{
  content:"AI MASTERY";position:absolute;left:14px;bottom:-7px;padding:2px 6px;
  border:1px solid rgba(184,149,255,.20);border-radius:999px;background:#08070d;color:#8876a8;
  font-size:6px;line-height:1;font-weight:950;letter-spacing:.18em;
}
.progress-hud{
  border-color:rgba(184,149,255,.24);background:linear-gradient(180deg,rgba(255,255,255,.09),rgba(255,255,255,.028));
  box-shadow:inset 0 1px 0 rgba(255,255,255,.11),0 14px 38px rgba(0,0,0,.38),0 0 40px rgba(138,92,255,.12);
}
.progress-fill{background:linear-gradient(90deg,#5e2bd2,#8a5cff 48%,#d1b7ff 100%);}
.question-count-chip{border-color:rgba(184,149,255,.30);background:linear-gradient(180deg,rgba(138,92,255,.11),rgba(138,92,255,.035));color:#d5c9e7;}
.board{
  border-color:rgba(171,126,255,.62);border-radius:34px;
  box-shadow:0 0 0 1px rgba(255,255,255,.035),0 40px 100px rgba(0,0,0,.76),0 0 95px rgba(80,38,190,.14),inset 0 1px 0 rgba(255,255,255,.13);
}
.board-content{padding:clamp(24px,3.3vw,40px);}
.command-row{margin-bottom:18px;}
.naya-button{border-color:rgba(255,255,255,.27);background:linear-gradient(180deg,rgba(255,255,255,.085),rgba(255,255,255,.025));}
.naya-orb{box-shadow:inset 0 2px 4px rgba(255,255,255,.78),0 0 28px rgba(116,76,255,.48),0 7px 15px rgba(0,0,0,.6);}
.continue-button:not(:disabled){border-color:#c4a4ff;box-shadow:inset 0 1px 0 rgba(255,255,255,.12),0 14px 32px rgba(0,0,0,.62),0 0 38px rgba(138,92,255,.22);}
.aaa-status-rail{
  width:min(940px,100%);margin:0 auto 20px;padding:10px 14px;border-color:rgba(184,149,255,.18);
  border-radius:14px;background:linear-gradient(90deg,rgba(138,92,255,.075),rgba(255,255,255,.025),rgba(237,66,196,.045));
  box-shadow:inset 0 1px 0 rgba(255,255,255,.055),0 10px 26px rgba(0,0,0,.18);
}
.question-area{padding:2px 12px 0;}
.question-label{padding:7px 11px;border:1px solid rgba(184,149,255,.18);border-radius:999px;background:rgba(138,92,255,.055);box-shadow:0 0 22px rgba(138,92,255,.08);}
.question-label::before,.question-label::after{display:none;}
.question-title{max-width:900px;font-size:clamp(28px,3.7vw,48px);line-height:1.055;text-shadow:0 3px 24px rgba(0,0,0,.55),0 0 40px rgba(138,92,255,.08);}
.question-rule{width:220px;margin-top:20px;}
.answers{width:min(900px,100%);margin-top:22px;gap:11px;}
.answer{
  min-height:68px;grid-template-columns:58px minmax(0,1fr) 34px;border-color:rgba(255,255,255,.12);border-radius:22px;
  background:linear-gradient(105deg,rgba(255,255,255,.055),rgba(255,255,255,.018) 48%,rgba(138,92,255,.025));
  box-shadow:0 10px 24px rgba(0,0,0,.34),inset 0 1px 0 rgba(255,255,255,.06);
}
.answer::before{
  content:"";position:absolute;left:0;top:12px;bottom:12px;width:2px;border-radius:2px;background:var(--accent);opacity:.35;
  box-shadow:0 0 14px color-mix(in srgb,var(--accent) 45%,transparent);transition:opacity .22s ease,width .22s ease;
}
.answer:hover::before,.answer.selected::before{width:4px;opacity:.9;}
.answer:hover{transform:translateY(-3px) scale(1.003);}
.answer.selected{background:linear-gradient(105deg,rgba(255,255,255,.075),rgba(138,92,255,.045) 55%,rgba(255,255,255,.02));}
.answer-title{font-size:clamp(15px,1.65vw,18px);}
.answer-sub{color:#cbc6d4;}
.jewel{width:54px;height:54px;border-radius:18px;}
.chevron{width:32px;height:32px;}
.footer{color:#716b7c;}
.aaa-guidance{margin:12px auto 0;color:#85808f;font-size:11px;line-height:1.4;font-weight:700;letter-spacing:.01em;text-align:center;}
@media(max-width:760px){
  .topbar{padding-top:4px}.brand{padding:8px 10px}.brand::after{display:none}.board-content{padding:15px 9px 13px}
  .aaa-status-rail{margin-bottom:13px;padding:8px 9px}.question-area{padding:0 5px}.question-label{padding:6px 9px;font-size:8px}
  .question-title{font-size:clamp(24px,6.5vw,34px)}.question-rule{width:130px;margin-top:13px}.answers{width:100%;margin-top:15px;gap:8px}
  .answer{min-height:63px;grid-template-columns:47px minmax(0,1fr) 27px;gap:9px;padding:6px;border-radius:18px}
  .jewel{width:45px;height:45px;border-radius:14px}.answer-title{font-size:13.6px}.answer-sub{font-size:12.6px}.chevron{width:26px;height:26px}
  .aaa-guidance{font-size:10px;margin-top:9px;padding:0 12px}
}
@media(prefers-reduced-motion:reduce){.answer:hover{transform:none;}}
'''
s, _ = replace_once(s, '</style>', v3_css + '\n</style>')

# Replace the prior status rail copy with clearer human-facing copy.
old_rail='''<div class="aaa-status-rail" aria-live="polite">\n  <span><strong id="aaaStepLabel">STEP 01</strong> · BUILDING YOUR AI PROFILE</span>\n  <span class="aaa-live">ASSESSMENT ACTIVE</span>\n</div>'''
new_rail='''<div class="aaa-status-rail" aria-live="polite">\n  <span><strong id="aaaStepLabel">STEP 01</strong> · BUILDING YOUR AI PROFILE</span>\n  <span class="aaa-live">LIVE · NO WRONG ANSWERS</span>\n</div>'''
if old_rail in s:
    s=s.replace(old_rail,new_rail,1)

# Add guidance once, immediately before the answer grid.
needle='<div\n  class="answers"'
guidance='<div class="aaa-guidance" id="aaaGuidance" aria-live="polite">Choose the answer that feels most like you. You can change your mind before continuing.</div>\n\n'
if 'id="aaaGuidance"' not in s:
    s,n=re.subn(needle,guidance+'<div\n  class="answers"',s,count=1)
    if n!=1: raise RuntimeError('Answer grid insertion anchor not found.')

# Progress-aware guidance.
old_update='''  DOM.questionCountChip.textContent=\n    `QUESTION ${current} OF ${total}`;\n\n  if(DOM.aaaStepLabel){'''
new_update='''  DOM.questionCountChip.textContent=\n    `QUESTION ${current} OF ${total}`;\n\n  const guidance=document.getElementById("aaaGuidance");\n  if(guidance){\n    guidance.textContent = window.innerWidth <= 760\n      ? "Choose the answer that feels most like you."\n      : "Choose the answer that feels most like you · click or use ↑ ↓ to explore · Enter to continue.";\n  }\n\n  if(DOM.aaaStepLabel){'''
s,_=replace_once(s,old_update,new_update)

# Keyboard navigation among answer controls.
keyboard='''\n\n/* =========================================================\n   AAA V3 KEYBOARD ANSWER NAVIGATION\n========================================================= */\ndocument.addEventListener("keydown", event=>{\n  if(state.teachingOpen || state.transitioning) return;\n  const answers=[...DOM.answers.querySelectorAll(".answer")];\n  if(!answers.length) return;\n  const active=document.activeElement;\n  const index=answers.indexOf(active);\n  if(event.key==="ArrowDown" || event.key==="ArrowRight"){\n    event.preventDefault();\n    answers[Math.min(index<0?0:index+1,answers.length-1)].focus();\n  }else if(event.key==="ArrowUp" || event.key==="ArrowLeft"){\n    event.preventDefault();\n    answers[Math.max(index<0?0:index-1,0)].focus();\n  }else if(event.key==="Enter" && index>=0){\n    event.preventDefault();\n    active.click();\n  }\n});\n'''
s,_=replace_once(s,'</script>',keyboard+'\n</script>')

# Keep exactly one compact short-screen block.
block='''@media(max-height:820px) and (min-width:761px){\n  .app-inner{padding-top:8px;padding-bottom:10px;}\n  .topbar{padding-bottom:9px;}\n  .board-content{padding-top:22px;padding-bottom:20px;}\n  .command-row{margin-bottom:16px;}\n  .question-title{font-size:36px;}\n  .answers{gap:7px;margin-top:15px;}\n  .answer{min-height:56px;}\n  .jewel{width:45px;height:45px;}\n}\n'''
if s.count(block)>1:
    first=s.find(block);s=s[:first+len(block)]+s[first+len(block):].replace(block,'')

# Remove duplicate guidance if any.
needle2='<div class="aaa-guidance" id="aaaGuidance" aria-live="polite">Choose the answer that feels most like you. You can change your mind before continuing.</div>'
while s.count(needle2)>1:
    first=s.find(needle2);second=s.find(needle2,first+len(needle2));s=s[:second]+s[second+len(needle2):]

if s==original:
    print('No changes required; MAXESS AAA v3 is already applied.')
else:
    PATH.write_text(s,encoding='utf-8')
    print('MAXESS AAA v3 substantive visual/UX pass applied.')
