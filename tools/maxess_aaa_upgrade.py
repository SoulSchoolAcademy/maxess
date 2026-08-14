from pathlib import Path

p = Path('code')
s = p.read_text(encoding='utf-8')
orig = s

def sub(a, b, n=1):
    global s
    s = s.replace(a, b, n)

# Normalize repeated generated fragments so this patch remains idempotent.
marker = '<meta name="maxess-build" content="AAA-2026-08-14">'
while s.count(marker) > 1:
    s = s.replace(marker, '', 1)

chip = '''.question-count-chip{
  justify-self:end;
  min-width:128px;
  padding:9px 12px;
  border:1px solid rgba(181,140,255,.24);
  border-radius:999px;
  background:rgba(138,92,255,.055);
  color:#bdb4ce;
  font-size:9px;
  font-weight:950;
  letter-spacing:.10em;
  text-align:center;
  white-space:nowrap;
}'''
while s.count(chip) > 1:
    s = s.replace(chip, '', 1)

sub('button{\n  font:inherit;\n}', 'button{\n  font:inherit;\n  -webkit-tap-highlight-color:transparent;\n}\n\nbutton,.answer,.interest-area{\n  touch-action:manipulation;\n  user-select:none;\n  -webkit-user-select:none;\n}')
sub('.command-row{\n  display:flex;', '.command-row{\n  position:relative;\n  z-index:4;\n  display:flex;')
sub('.question-title{\n  margin:0;\n  color:#fff;\n  font-size:clamp(26px,4vw,48px);', '.question-title{\n  margin:0 auto;\n  color:#fff;\n  max-width:860px;\n  font-size:clamp(25px,3.35vw,42px);')
sub('.answers{\n  width:min(860px,100%);\n  margin:clamp(18px,2.4vw,28px) auto 0;', '.answers{\n  width:min(860px,100%);\n  margin:clamp(16px,2vw,23px) auto 0;')
sub('  min-height:66px;\n  display:grid;\n  grid-template-columns:52px minmax(0,1fr) 30px;', '  min-height:62px;\n  display:grid;\n  grid-template-columns:52px minmax(0,1fr) 30px;')
sub('  <div></div>\n\n</header>', '  <div class="question-count-chip" id="questionCountChip" aria-live="polite">QUESTION 1 OF 15</div>\n\n</header>')
sub('.brand-ess{\n  color:#b58cff;\n}', '.brand-ess{\n  color:#b58cff;\n}\n\n'+chip)
sub('  progressPercent:\n    document.getElementById("progressPercent"),\n\n  nayaButton:', '  progressPercent:\n    document.getElementById("progressPercent"),\n\n  questionCountChip:\n    document.getElementById("questionCountChip"),\n\n  nayaButton:')
sub('  DOM.progressPercent.textContent=\n    `${percentage}%`;\n\n}', '  DOM.progressPercent.textContent=\n    `${percentage}%`;\n\n  if(DOM.questionCountChip){\n    DOM.questionCountChip.textContent=`QUESTION ${current} OF ${total}`;\n  }\n\n}')
sub('  .brand{\n    font-size:16px;\n  }\n\n  .progress-hud{', '  .brand{\n    font-size:16px;\n  }\n\n  .question-count-chip{display:none;}\n\n  .progress-hud{')
sub('@media(max-width:420px){', '@media(max-height:820px) and (min-width:761px){\n  .app-inner{padding-top:8px;padding-bottom:10px;}\n  .topbar{padding-bottom:9px;}\n  .board-content{padding-top:22px;padding-bottom:20px;}\n  .command-row{margin-bottom:16px;}\n  .question-title{font-size:36px;}\n  .answers{gap:7px;margin-top:15px;}\n  .answer{min-height:56px;}\n  .jewel{width:45px;height:45px;}\n}\n\n@media(max-width:420px){')
sub('  if(!("speechSynthesis" in window)){\n    return;\n  }', '  if(!("speechSynthesis" in window)){\n    DOM.nayaPrimary.textContent="Audio unavailable";\n    DOM.nayaSecondary.textContent="Speech is not supported here";\n    setTimeout(stopNaya,2200);\n    return;\n  }')
sub('  DOM.interestsView.classList.add(\n    "visible"\n  );\n\n  state.interestBoard=0;', '  DOM.interestsView.classList.add(\n    "visible"\n  );\n\n  DOM.progressLabel.textContent="PERSONALIZE YOUR REPORT";\n  DOM.progressFill.style.width="100%";\n  DOM.progressPercent.textContent="100%";\n  if(DOM.questionCountChip) DOM.questionCountChip.textContent="FINAL STEP";\n\n  state.interestBoard=0;')
sub('<title>MAXESS — AI Mastery Assessment</title>', '<title>MAXESS — AI Mastery Assessment</title>\n<meta name="maxess-build" content="AAA-2026-08-14">')

# Final normalization.
while s.count(marker) > 1:
    s = s.replace(marker, '', 1)
while s.count(chip) > 1:
    s = s.replace(chip, '', 1)

if s != orig:
    p.write_text(s, encoding='utf-8')
    print('MAXESS AAA upgrade applied')
else:
    print('MAXESS AAA upgrade already applied or no matching baseline found')
