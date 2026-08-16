#!/usr/bin/env python3
"""Growing Lesson 002: Oscar Pass 2.

Post-build refinement for the canonical MAXESS Results experience. The pass is
scoped to #maxess-results-10 so the immutable NayaNET Page Code remains intact.
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
<style id="maxess-oscar-pass-2">
/* GROWING LESSON 002 — composition, rhythm, illumination, tactile controls */
#maxess-results-10 .mx-section{padding-top:clamp(48px,5.2vw,82px);padding-bottom:clamp(48px,5.2vw,82px)}
#maxess-results-10 .mx-hero{min-height:min(760px,88vh);padding-top:clamp(62px,6vw,96px);padding-bottom:clamp(52px,5.5vw,84px)}
#maxess-results-10 .mx-hero-grid{gap:clamp(32px,5vw,82px)}
#maxess-results-10 .mx-hero::before{width:min(1050px,90vw);height:620px;top:0;opacity:.9}
#maxess-results-10 .mx-title{max-width:920px}
#maxess-results-10 .mx-copy{max-width:690px}
#maxess-results-10 .mx-proof{margin-top:30px;gap:8px}
#maxess-results-10 .mx-proof div{padding:13px 16px;background:rgba(255,255,255,.018);border-radius:12px;border-left:1px solid rgba(208,168,255,.34)}
#maxess-results-10 .mx-score-orb{box-shadow:0 0 0 1px rgba(255,255,255,.18),inset 0 0 90px rgba(174,92,255,.2),0 32px 90px rgba(0,0,0,.58),0 0 130px rgba(148,74,255,.25)}
#maxess-results-10 .mx-divider{width:min(1500px,92%);background:linear-gradient(90deg,transparent,rgba(208,168,255,.25),transparent)}

/* Scene rhythm: alternate atmosphere instead of stacking identical cards. */
#maxess-results-10 > .mx-section:nth-of-type(2){padding-top:42px;padding-bottom:52px}
#maxess-results-10 > .mx-section:nth-of-type(3),
#maxess-results-10 > .mx-section:nth-of-type(5),
#maxess-results-10 > .mx-section:nth-of-type(7){background:linear-gradient(180deg,rgba(166,108,255,.025),transparent 28%,rgba(255,255,255,.012) 72%,transparent)}
#maxess-results-10 > .mx-section:nth-of-type(4){background:radial-gradient(ellipse 55% 65% at 15% 50%,rgba(166,108,255,.07),transparent 72%)}
#maxess-results-10 > .mx-section:nth-of-type(6){background:radial-gradient(ellipse 55% 65% at 85% 50%,rgba(81,226,173,.045),transparent 72%)}

/* Less box, more composition. */
#maxess-results-10 .mx-panel{background:linear-gradient(145deg,rgba(255,255,255,.065),rgba(255,255,255,.012));box-shadow:0 26px 80px rgba(0,0,0,.22)}
#maxess-results-10 .mx-dim{min-height:300px;background:linear-gradient(160deg,rgba(255,255,255,.055),rgba(255,255,255,.012));box-shadow:0 18px 50px rgba(0,0,0,.12)}
#maxess-results-10 .mx-area{background:linear-gradient(100deg,rgba(255,255,255,.045),rgba(255,255,255,.012));box-shadow:0 10px 30px rgba(0,0,0,.12)}
#maxess-results-10 .mx-area:hover{transform:translateY(-2px) translateX(3px)}

/* Black Diamond Royal button standard — tactile, obvious, premium. */
#maxess-results-10 .mx-cta{min-height:58px;padding:0 24px;border-radius:17px;border:1px solid rgba(230,218,255,.34);position:relative;overflow:hidden;isolation:isolate;box-shadow:0 12px 28px rgba(0,0,0,.3),inset 0 1px rgba(255,255,255,.34),inset 0 -1px rgba(0,0,0,.4)}
#maxess-results-10 .mx-cta::before{content:"";position:absolute;inset:1px;border-radius:16px;border:1px solid rgba(255,255,255,.1);pointer-events:none;z-index:-1}
#maxess-results-10 .mx-cta::after{content:"";position:absolute;left:8%;right:8%;top:1px;height:34%;border-radius:999px;background:linear-gradient(180deg,rgba(255,255,255,.28),transparent);opacity:.55;pointer-events:none}
#maxess-results-10 .mx-cta-primary{background:linear-gradient(145deg,#e2c9ff 0%,#a968f4 28%,#6e2bc0 65%,#32105d 100%);border-color:rgba(239,225,255,.65);box-shadow:0 16px 34px rgba(91,34,160,.36),inset 0 1px rgba(255,255,255,.72),inset 0 -2px rgba(20,4,42,.5)}
#maxess-results-10 .mx-cta-ghost{background:linear-gradient(145deg,rgba(255,255,255,.12),rgba(255,255,255,.035));border-color:rgba(255,255,255,.22)}
#maxess-results-10 .mx-cta:hover{transform:translateY(-2px);filter:brightness(1.08);box-shadow:0 20px 38px rgba(0,0,0,.36),0 0 28px rgba(166,108,255,.16),inset 0 1px rgba(255,255,255,.7)}
#maxess-results-10 .mx-cta:active{transform:translateY(1px) scale(.985);filter:brightness(.98);box-shadow:0 8px 18px rgba(0,0,0,.36),inset 0 2px 4px rgba(0,0,0,.34)}
#maxess-results-10 .mx-cta:focus-visible,#maxess-results-10 .mx-mini:focus-visible{outline:2px solid #fff;outline-offset:3px}
#maxess-results-10 .mx-mini{min-height:44px;padding:0 13px;border-radius:12px;background:linear-gradient(145deg,rgba(255,255,255,.11),rgba(255,255,255,.035));border-color:rgba(208,168,255,.3)!important;box-shadow:inset 0 1px rgba(255,255,255,.2),0 7px 18px rgba(0,0,0,.2)}
#maxess-results-10 .mx-mini:hover{transform:translateY(-1px);background:linear-gradient(145deg,rgba(166,108,255,.24),rgba(255,255,255,.055))}
#maxess-results-10 .mx-mini:active{transform:translateY(1px) scale(.98)}

/* Naya transition is the emotional climax, not merely another card. */
#maxess-results-10 .mx-naya-bridge{padding-top:clamp(68px,7vw,108px);padding-bottom:clamp(50px,5vw,78px)}
#maxess-results-10 .mx-bridge-card{padding:clamp(40px,6vw,76px) 24px;border-radius:40px;background:radial-gradient(ellipse 75% 90% at 50% 0,rgba(177,100,255,.24),transparent 62%),linear-gradient(180deg,rgba(255,255,255,.07),rgba(255,255,255,.018));box-shadow:0 45px 120px rgba(0,0,0,.44),0 0 90px rgba(141,70,220,.11)}
#maxess-results-10 .mx-key div{background:linear-gradient(145deg,rgba(255,255,255,.075),rgba(255,255,255,.02));box-shadow:inset 0 1px rgba(255,255,255,.1),0 10px 28px rgba(0,0,0,.16)}

@media(max-width:1050px){#maxess-results-10 .mx-section{padding-top:54px;padding-bottom:54px}}
@media(max-width:720px){
 #maxess-results-10 .mx-section{padding:44px 16px}
 #maxess-results-10 .mx-hero{padding-top:58px;padding-bottom:46px}
 #maxess-results-10 .mx-proof{margin-top:24px}
 #maxess-results-10 .mx-proof div{border-radius:0;background:transparent;padding:12px 2px}
 #maxess-results-10 .mx-cta{min-height:58px;width:100%}
 #maxess-results-10 .mx-score-orb{width:min(285px,76vw)}
 #maxess-results-10 .mx-naya-bridge{padding-top:52px;padding-bottom:42px}
 #maxess-results-10 .mx-bridge-card{padding:38px 18px;border-radius:30px}
}
@media(prefers-reduced-motion:reduce){#maxess-results-10 .mx-cta,#maxess-results-10 .mx-mini{transition:none}}
</style>
'''

def apply(path: Path):
    text = path.read_text(encoding="utf-8")
    if 'id="maxess-oscar-pass-2"' in text:
        return False
    marker = "</body>"
    if marker not in text:
        raise RuntimeError(f"No body close marker in {path}")
    text = text.replace(marker, OVERRIDE + marker, 1)
    path.write_text(text, encoding="utf-8")
    return True

changed = 0
for f in FILES:
    if f.exists() and apply(f):
        changed += 1
print(f"Oscar Pass 2 applied to {changed} canonical Results artifacts")
