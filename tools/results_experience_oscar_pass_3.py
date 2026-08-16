#!/usr/bin/env python3
"""Growing Lesson 003: literal 10-star composition pass.

The override is inserted before </body> so generated Groove artifacts remain
valid HTML. It never appends executable markup after </html>.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FILES = [
    ROOT / "MAXESS-RESULTS-FINAL-GROOVE.html",
    ROOT / "MAXESS-RESULTS-FINAL-GROOVE-EMBED.html",
    ROOT / "MAXESS-RESULTS-10-GROOVE.html",
    ROOT / "MAXESS-RESULTS-GROOVE-EMBED.html",
    ROOT / "MAXESS-RESULTS-GROOVE-EMBED-9.95.html",
]

OVERRIDE = r'''
<style id="maxess-oscar-pass-3">
#maxess-results-10{--mx-space:clamp(34px,4vw,64px);--mx-glow:rgba(171,105,255,.13)}
#maxess-results-10 .mx-section{padding-block:var(--mx-space);position:relative;isolation:isolate}
#maxess-results-10 .mx-section::after{content:"";position:absolute;inset:0;z-index:-1;pointer-events:none;background:radial-gradient(ellipse 75% 55% at 50% 0,var(--mx-glow),transparent 70%);opacity:.7}
#maxess-results-10 .mx-hero{min-height:min(700px,82vh);padding-block:clamp(44px,5vw,76px)}
#maxess-results-10 .mx-hero-grid{width:min(1420px,94vw);gap:clamp(26px,4vw,64px)}
#maxess-results-10 .mx-title{font-size:clamp(46px,6.2vw,92px);line-height:.91;letter-spacing:-.055em}
#maxess-results-10 .mx-copy{font-size:clamp(16px,1.35vw,19px);line-height:1.55;max-width:640px}
#maxess-results-10 .mx-hero-actions{margin-top:24px;gap:10px}
#maxess-results-10 .mx-proof{margin-top:24px;max-width:760px}
#maxess-results-10 .mx-proof div{background:linear-gradient(145deg,rgba(255,255,255,.055),rgba(255,255,255,.012));border:1px solid rgba(255,255,255,.09);border-left-color:rgba(205,165,255,.4);box-shadow:0 12px 30px rgba(0,0,0,.16)}
#maxess-results-10 .mx-score-orb{filter:saturate(1.08);transform:translateZ(0)}
#maxess-results-10 .mx-score strong{font-size:clamp(74px,10vw,132px);letter-spacing:-.07em}
#maxess-results-10 .mx-insight{padding-block:clamp(28px,3vw,44px)}
#maxess-results-10 .mx-insight-card{max-width:1120px;margin-inline:auto;padding:clamp(26px,4vw,52px);border-radius:30px;background:linear-gradient(145deg,rgba(255,255,255,.065),rgba(255,255,255,.018));border:1px solid rgba(255,255,255,.1);box-shadow:0 30px 90px rgba(0,0,0,.25)}
#maxess-results-10 .mx-quote{font-size:clamp(30px,4.2vw,60px);line-height:1.02;letter-spacing:-.045em}
#maxess-results-10 .mx-section-head{max-width:1420px;margin-inline:auto;gap:28px}
#maxess-results-10 .mx-section-head h2{font-size:clamp(34px,4.5vw,68px);line-height:.98;letter-spacing:-.05em}
#maxess-results-10 .mx-section-head p{font-size:15px;line-height:1.65}
#maxess-results-10 .mx-fingerprint{width:min(1420px,94vw);margin-inline:auto;gap:clamp(18px,4vw,58px)}
#maxess-results-10 .mx-radar{filter:drop-shadow(0 24px 45px rgba(0,0,0,.28))}
#maxess-results-10 .mx-dim-grid{gap:10px}
#maxess-results-10 .mx-dim{min-height:250px;padding:22px;border-radius:20px}
#maxess-results-10 .mx-dim h3{font-size:20px}
#maxess-results-10 .mx-panel{border-radius:26px}
#maxess-results-10 .mx-contrast{width:min(1420px,94vw);margin-inline:auto}
#maxess-results-10 .mx-contrast>*{min-height:0}
#maxess-results-10 .mx-list-row{transition:transform .18s ease,border-color .18s ease,background .18s ease}
#maxess-results-10 .mx-list-row:hover{transform:translateX(4px);border-color:rgba(205,165,255,.3)}
#maxess-results-10 .mx-area{transition:transform .18s ease,background .18s ease,border-color .18s ease}
#maxess-results-10 .mx-area:hover{transform:translateY(-2px)}
#maxess-results-10 .mx-naya-bridge{padding-block:clamp(54px,6vw,90px);background:radial-gradient(ellipse 70% 85% at 50% 45%,rgba(167,96,255,.12),transparent 68%)}
#maxess-results-10 .mx-bridge-card{width:min(1180px,94vw);margin-inline:auto;padding:clamp(38px,6vw,72px) clamp(20px,5vw,70px);border-radius:36px;background:radial-gradient(ellipse 65% 100% at 50% 0,rgba(193,126,255,.22),transparent 64%),linear-gradient(145deg,rgba(255,255,255,.075),rgba(255,255,255,.015));border:1px solid rgba(225,205,255,.16);box-shadow:0 45px 120px rgba(0,0,0,.45),0 0 100px rgba(145,75,230,.13)}
#maxess-results-10 .mx-key{gap:10px}
#maxess-results-10 .mx-key div{border-radius:18px;padding:18px;background:linear-gradient(145deg,rgba(255,255,255,.07),rgba(255,255,255,.018));border:1px solid rgba(255,255,255,.08)}
#maxess-results-10 .mx-cta{min-height:58px;border-radius:17px;letter-spacing:-.01em}
#maxess-results-10 .mx-cta-primary{box-shadow:0 16px 38px rgba(91,34,160,.42),0 0 32px rgba(166,108,255,.1),inset 0 1px rgba(255,255,255,.72),inset 0 -2px rgba(20,4,42,.5)}
#maxess-results-10 .mx-cta-ghost{box-shadow:0 12px 30px rgba(0,0,0,.28),inset 0 1px rgba(255,255,255,.25)}
@media(max-width:900px){
#maxess-results-10 .mx-hero{min-height:auto}
#maxess-results-10 .mx-hero-grid{width:min(720px,92vw)}
#maxess-results-10 .mx-section-head{display:block;width:min(720px,92vw)}
#maxess-results-10 .mx-section-head p{margin-top:14px}
#maxess-results-10 .mx-fingerprint{width:min(720px,92vw)}
#maxess-results-10 .mx-contrast{width:min(720px,92vw)}
}
@media(max-width:620px){
#maxess-results-10{--mx-space:34px}
#maxess-results-10 .mx-section{padding-inline:16px}
#maxess-results-10 .mx-hero{padding-top:44px;padding-bottom:38px}
#maxess-results-10 .mx-title{font-size:clamp(42px,13vw,62px)}
#maxess-results-10 .mx-copy{font-size:15px}
#maxess-results-10 .mx-proof{grid-template-columns:1fr;margin-top:20px}
#maxess-results-10 .mx-proof div{padding:10px 0;border-radius:0;border-width:0 0 1px}
#maxess-results-10 .mx-score-orb{margin-inline:auto}
#maxess-results-10 .mx-insight-card{border-radius:24px}
#maxess-results-10 .mx-dim{padding:18px;min-height:0}
#maxess-results-10 .mx-bridge-card{border-radius:28px}
#maxess-results-10 .mx-cta{width:100%}
}
@media(prefers-reduced-motion:reduce){#maxess-results-10 .mx-list-row,#maxess-results-10 .mx-area,#maxess-results-10 .mx-cta{transition:none!important}}
</style>
'''


def apply(path: Path):
    text = path.read_text(encoding='utf-8')
    if 'id="maxess-oscar-pass-3"' in text:
        return False
    if '</body>' in text:
        text = text.replace('</body>', OVERRIDE + '</body>', 1)
    elif '</html>' in text:
        text = text.replace('</html>', OVERRIDE + '</html>', 1)
    else:
        text += OVERRIDE
    path.write_text(text, encoding='utf-8')
    return True

changed = sum(1 for f in FILES if f.exists() and apply(f))
print(f'Oscar Pass 3 applied to {changed} canonical Results artifacts')
