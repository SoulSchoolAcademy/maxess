#!/usr/bin/env python3
"""Growing Lesson 001 visual optimization pass for the definitive Results experience.

This pass is deliberately additive: it preserves the Results content, scoring,
Naya architecture, and immutable NayaNET foundation while correcting the main
4.2 failure modes: excessive whitespace, weak visual rhythm, flat hierarchy,
excessive darkness, and generic-looking interaction surfaces.
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

POLISH = r'''<style id="maxess-growing-lesson-001-polish">
/* Growing Lesson 001: compose the page as one experience, not isolated sections. */
#maxess-results-10 .mx-section{padding-top:clamp(46px,5vw,78px);padding-bottom:clamp(46px,5vw,78px)}
#maxess-results-10 .mx-hero{min-height:min(780px,88vh);padding-top:clamp(56px,6vw,92px);padding-bottom:clamp(50px,6vw,82px)}
#maxess-results-10 .mx-insight{padding-top:clamp(44px,4.5vw,70px);padding-bottom:clamp(40px,4.5vw,68px)}
#maxess-results-10 .mx-section-head{margin-bottom:24px;align-items:center}
#maxess-results-10 .mx-section-head p{font-size:14px;max-width:500px}
#maxess-results-10 .mx-section-head h2{font-size:clamp(29px,3.7vw,56px)}
#maxess-results-10 .mx-dim-grid{grid-template-columns:repeat(3,minmax(0,1fr));gap:14px}
#maxess-results-10 .mx-dim{min-height:285px;padding:20px;border-radius:22px}
#maxess-results-10 .mx-dim:nth-child(4),#maxess-results-10 .mx-dim:nth-child(5){min-height:250px}
#maxess-results-10 .mx-dim:nth-child(4){grid-column:1 / span 1}
#maxess-results-10 .mx-dim:nth-child(5){grid-column:2 / span 1}
#maxess-results-10 .mx-contrast{gap:14px}
#maxess-results-10 .mx-panel{border-radius:28px;padding:clamp(24px,3vw,42px)}
#maxess-results-10 .mx-fingerprint{gap:clamp(24px,5vw,72px)}
#maxess-results-10 .mx-radar{max-width:560px}
#maxess-results-10 .mx-list{gap:7px}
#maxess-results-10 .mx-list-row{padding:13px 15px;border-radius:14px}
#maxess-results-10 .mx-area{padding:17px 18px;border-radius:18px}
#maxess-results-10 .mx-area-main h3{font-size:15px}
#maxess-results-10 .mx-area-main p{font-size:11px;line-height:1.45}
#maxess-results-10 .mx-mini{min-height:38px;padding:0 13px;border-radius:12px;border:1px solid rgba(208,168,255,.22);background:rgba(166,108,255,.08);color:#fff;font-weight:800;transition:transform .2s ease,background .2s ease,border-color .2s ease}
#maxess-results-10 .mx-mini:hover{transform:translateY(-2px);background:rgba(166,108,255,.16);border-color:rgba(208,168,255,.42)}
#maxess-results-10 .mx-cta{min-height:54px;border-radius:15px;position:relative;overflow:hidden}
#maxess-results-10 .mx-cta::after{content:"";position:absolute;inset:1px;border-radius:14px;pointer-events:none;background:linear-gradient(110deg,rgba(255,255,255,.18),transparent 32%,transparent 68%,rgba(255,255,255,.06));opacity:.7}
#maxess-results-10 .mx-cta>*{position:relative;z-index:1}
#maxess-results-10 .mx-growth{padding-top:clamp(48px,5vw,76px)}
#maxess-results-10 .mx-growth-grid{gap:14px}
#maxess-results-10 .mx-growth-card{padding:clamp(24px,3vw,38px);border-radius:24px}
#maxess-results-10 .mx-plan{margin-top:14px;gap:10px}
#maxess-results-10 .mx-plan div{padding:14px;border-radius:15px}
#maxess-results-10 .mx-divider{opacity:.75}
/* Light architecture: black remains the canvas, purple illumination creates hierarchy. */
#maxess-results-10 .mx-section:nth-of-type(3)::before,#maxess-results-10 .mx-section:nth-of-type(6)::before,#maxess-results-10 .mx-section:nth-of-type(8)::before{content:"";position:absolute;inset:0;pointer-events:none;background:radial-gradient(ellipse 60% 70% at 50% 30%,rgba(132,62,210,.075),transparent 72%)}
@media(max-width:980px){
  #maxess-results-10 .mx-hero-grid{grid-template-columns:1fr;gap:38px}
  #maxess-results-10 .mx-score-orb{width:min(360px,70vw)}
  #maxess-results-10 .mx-dim-grid{grid-template-columns:repeat(2,minmax(0,1fr))}
  #maxess-results-10 .mx-dim:nth-child(4),#maxess-results-10 .mx-dim:nth-child(5){grid-column:auto}
}
@media(max-width:700px){
  #maxess-results-10 .mx-section{padding-left:18px;padding-right:18px;padding-top:42px;padding-bottom:42px}
  #maxess-results-10 .mx-hero{min-height:auto;padding-top:54px;padding-bottom:48px}
  #maxess-results-10 .mx-section-head{display:block;margin-bottom:20px}
  #maxess-results-10 .mx-section-head p{margin-top:15px}
  #maxess-results-10 .mx-dim-grid{grid-template-columns:1fr;gap:10px}
  #maxess-results-10 .mx-dim,#maxess-results-10 .mx-dim:nth-child(4),#maxess-results-10 .mx-dim:nth-child(5){min-height:0}
  #maxess-results-10 .mx-proof{grid-template-columns:1fr;gap:8px;margin-top:28px}
  #maxess-results-10 .mx-proof div{padding:12px 15px}
  #maxess-results-10 .mx-hero-actions{flex-direction:column}
  #maxess-results-10 .mx-hero-actions .mx-cta{width:100%}
  #maxess-results-10 .mx-quote{font-size:clamp(26px,8vw,38px)}
}
@media(prefers-reduced-motion:reduce){#maxess-results-10 .mx-reveal{opacity:1;transform:none;transition:none}#maxess-results-10 .mx-cta,#maxess-results-10 .mx-mini{transition:none}}
</style>'''

for path in FILES:
    text = path.read_text(encoding="utf-8")
    if "maxess-growing-lesson-001-polish" in text:
        continue
    if "</head>" in text:
        text = text.replace("</head>", POLISH + "\n</head>", 1)
    elif "</style>" in text:
        text = text.replace("</style>", "</style>\n" + POLISH, 1)
    else:
        text = POLISH + text
    path.write_text(text, encoding="utf-8")
    print(f"optimized {path.name}: {len(text)} bytes")
