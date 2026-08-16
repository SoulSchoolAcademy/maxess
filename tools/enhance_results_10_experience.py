#!/usr/bin/env python3
"""Add growth, personality, dimensionality, and Naya experience layers safely.

This is a presentation pass only. It does not alter assessment scoring or the
canonical Result Contract. It inserts additive layers before the existing Naya
chapter and leaves the underlying Results engine intact.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FILES = [
    ROOT / 'MAXESS-RESULTS-FINAL-GROOVE.html',
    ROOT / 'MAXESS-RESULTS-FINAL-GROOVE-EMBED.html',
    ROOT / 'MAXESS-RESULTS-10-GROOVE.html',
    ROOT / 'MAXESS-RESULTS-GROOVE-EMBED.html',
    ROOT / 'MAXESS-RESULTS-GROOVE-EMBED-9.95.html',
]

CSS = """<style id=\"maxess-results-10-growth-layer\">
.mx-growth{padding-top:clamp(60px,7vw,108px)}
.mx-growth-grid{display:grid;grid-template-columns:1.05fr .95fr;gap:14px;align-items:stretch}
.mx-growth-card{padding:clamp(26px,3.2vw,44px);border:1px solid rgba(255,255,255,.11);border-radius:28px;background:linear-gradient(145deg,rgba(255,255,255,.055),rgba(255,255,255,.018));box-shadow:0 25px 80px rgba(0,0,0,.25)}
.mx-growth-card h3{margin:10px 0;font-size:clamp(25px,3vw,42px);line-height:1;letter-spacing:-.045em}.mx-growth-card p{margin:0;color:rgba(255,255,255,.65);font-size:14px;line-height:1.6}
.mx-scorecard{display:grid;gap:10px;margin-top:24px}.mx-scorecard-row{display:grid;grid-template-columns:120px 1fr 44px;gap:12px;align-items:center;font-size:11px}.mx-scorecard-row span{color:rgba(255,255,255,.56)}.mx-scorecard-row b{text-align:right}.mx-scorecard-track{height:7px;border-radius:99px;background:rgba(255,255,255,.07);overflow:hidden}.mx-scorecard-track i{display:block;width:var(--w);height:100%;border-radius:inherit;background:linear-gradient(90deg,#7340ca,#d4adff)}
.mx-band-rail{display:grid;grid-template-columns:repeat(4,1fr);gap:5px;margin-top:28px}.mx-band-rail div{min-height:78px;padding:12px;border-radius:13px;border:1px solid rgba(255,255,255,.08);background:rgba(255,255,255,.025)}.mx-band-rail strong{display:block;font-size:12px}.mx-band-rail span{display:block;color:rgba(255,255,255,.48);font-size:9px;margin-top:6px}.mx-band-rail .active{border-color:rgba(208,168,255,.4);background:linear-gradient(145deg,rgba(166,108,255,.18),rgba(255,255,255,.03));box-shadow:0 0 30px rgba(166,108,255,.09)}
.mx-plan{display:grid;grid-template-columns:repeat(3,1fr);gap:9px;margin-top:20px}.mx-plan div{padding:16px;border-radius:16px;border:1px solid rgba(255,255,255,.1);background:rgba(0,0,0,.16)}.mx-plan b{display:block;color:#d4adff;font-size:10px;letter-spacing:.13em}.mx-plan h4{margin:8px 0 5px;font-size:14px}.mx-plan p{font-size:11px;line-height:1.45}.mx-growth-cta{display:flex;flex-wrap:wrap;gap:11px;margin-top:24px}.mx-growth-cta .mx-cta{min-height:54px}.mx-micro{margin-top:14px!important;color:rgba(255,255,255,.42)!important;font-size:10px!important}

/* MAXESS 10.0 visual language: additive, reusable, and deliberately restrained. */
#maxess-results-10 .mx-wide{width:min(1680px,100%);margin-left:auto;margin-right:auto}
#maxess-results-10 .mx-section{padding-left:clamp(18px,3.5vw,64px);padding-right:clamp(18px,3.5vw,64px)}
#maxess-results-10 .mx-growth-card,#maxess-results-10 .mx-dim,#maxess-results-10 .mx-area,#maxess-results-10 .mx-panel,#maxess-results-10 .mx-step{position:relative;overflow:hidden;backdrop-filter:blur(18px);-webkit-backdrop-filter:blur(18px)}
#maxess-results-10 .mx-growth-card::before,#maxess-results-10 .mx-dim::before,#maxess-results-10 .mx-area::before,#maxess-results-10 .mx-panel::before{content:"";position:absolute;inset:0;pointer-events:none;background:linear-gradient(135deg,rgba(255,255,255,.10),transparent 32%,transparent 70%,rgba(166,108,255,.05));opacity:.7}
#maxess-results-10 .mx-dim:nth-child(1){box-shadow:inset 0 1px rgba(255,255,255,.12),0 24px 60px rgba(72,24,126,.12)}
#maxess-results-10 .mx-dim:nth-child(2){box-shadow:inset 0 1px rgba(255,255,255,.12),0 24px 60px rgba(42,145,189,.10)}
#maxess-results-10 .mx-dim:nth-child(3){box-shadow:inset 0 1px rgba(255,255,255,.12),0 24px 60px rgba(206,148,46,.09)}
#maxess-results-10 .mx-dim:nth-child(4){box-shadow:inset 0 1px rgba(255,255,255,.12),0 24px 60px rgba(56,191,151,.09)}
#maxess-results-10 .mx-dim:nth-child(5){box-shadow:inset 0 1px rgba(255,255,255,.12),0 24px 60px rgba(199,74,190,.10)}
#maxess-results-10 .mx-score-orb{animation:mx-orb-breathe 5.5s ease-in-out infinite}
#maxess-results-10 .mx-score-orb::before{animation:mx-orb-ring 12s linear infinite}
#maxess-results-10 .mx-cta-primary{position:relative;overflow:hidden}
#maxess-results-10 .mx-cta-primary::after{content:"";position:absolute;top:-60%;left:-30%;width:28%;height:220%;transform:rotate(22deg);background:linear-gradient(90deg,transparent,rgba(255,255,255,.34),transparent);animation:mx-sheen 4.8s ease-in-out infinite}
#maxess-results-10 .mx-mini{transition:transform .22s cubic-bezier(.2,.8,.2,1),background .22s ease,border-color .22s ease;position:relative;z-index:1}
#maxess-results-10 .mx-mini:hover,#maxess-results-10 .mx-mini:focus-visible{transform:translateY(-2px) scale(1.02);background:linear-gradient(135deg,rgba(166,108,255,.26),rgba(42,211,238,.12));border-color:rgba(208,168,255,.42)!important}

.mx-naya-playground{padding-top:clamp(72px,8vw,118px);padding-bottom:clamp(70px,8vw,118px)}
.mx-naya-playground-head{display:flex;justify-content:space-between;align-items:end;gap:30px;margin-bottom:30px}.mx-naya-playground-head h2{margin:9px 0 0;font-size:clamp(34px,4.7vw,72px);line-height:.94;letter-spacing:-.055em}.mx-naya-playground-head p{max-width:560px;margin:0;color:rgba(255,255,255,.62);font-size:15px;line-height:1.6}
.mx-naya-doors{display:grid;grid-template-columns:1fr 1fr 1fr;gap:14px}
.mx-naya-door{position:relative;min-height:310px;padding:30px;border-radius:30px;border:1px solid rgba(255,255,255,.13);overflow:hidden;text-decoration:none;color:#fff;background:linear-gradient(145deg,rgba(255,255,255,.07),rgba(255,255,255,.018));box-shadow:inset 0 1px rgba(255,255,255,.10),0 30px 80px rgba(0,0,0,.24);transition:transform .28s cubic-bezier(.2,.8,.2,1),border-color .28s ease,box-shadow .28s ease}
.mx-naya-door:hover,.mx-naya-door:focus-visible{transform:translateY(-8px);border-color:rgba(255,255,255,.30);box-shadow:inset 0 1px rgba(255,255,255,.18),0 38px 100px rgba(0,0,0,.40),0 0 55px rgba(166,108,255,.10)}
.mx-naya-door::before{content:"";position:absolute;width:260px;height:260px;right:-100px;top:-110px;border-radius:50%;filter:blur(4px);background:radial-gradient(circle,rgba(166,108,255,.28),transparent 68%)}
.mx-naya-door:nth-child(2)::before{background:radial-gradient(circle,rgba(42,211,238,.25),transparent 68%)}
.mx-naya-door:nth-child(3)::before{background:radial-gradient(circle,rgba(247,213,140,.25),transparent 68%)}
.mx-naya-icon{position:relative;display:grid;place-items:center;width:68px;height:68px;border-radius:21px;font-size:30px;background:linear-gradient(145deg,rgba(255,255,255,.20),rgba(255,255,255,.055));border:1px solid rgba(255,255,255,.20);box-shadow:inset 0 1px rgba(255,255,255,.3),0 15px 35px rgba(0,0,0,.25);margin-bottom:48px}
.mx-naya-door:nth-child(1) .mx-naya-icon{background:linear-gradient(145deg,rgba(188,112,255,.42),rgba(86,37,170,.18))}.mx-naya-door:nth-child(2) .mx-naya-icon{background:linear-gradient(145deg,rgba(42,211,238,.34),rgba(46,88,180,.16))}.mx-naya-door:nth-child(3) .mx-naya-icon{background:linear-gradient(145deg,rgba(247,213,140,.38),rgba(191,95,212,.15))}
.mx-naya-door h3{position:relative;margin:0;font-size:clamp(24px,2.4vw,38px);letter-spacing:-.045em}.mx-naya-door p{position:relative;max-width:360px;margin:10px 0 25px;color:rgba(255,255,255,.66);font-size:14px;line-height:1.55}.mx-naya-open{position:relative;display:inline-flex;align-items:center;gap:9px;color:#fff;font-size:11px;font-weight:900;letter-spacing:.10em;text-transform:uppercase}.mx-naya-open span{display:grid;place-items:center;width:25px;height:25px;border-radius:50%;background:rgba(255,255,255,.10);border:1px solid rgba(255,255,255,.16)}
.mx-naya-note{margin:18px 0 0;color:rgba(255,255,255,.42);font-size:11px;letter-spacing:.04em}

@keyframes mx-orb-breathe{0%,100%{transform:scale(1);filter:saturate(1)}50%{transform:scale(1.018);filter:saturate(1.12)}}
@keyframes mx-orb-ring{to{transform:rotate(360deg)}}
@keyframes mx-sheen{0%,72%{left:-35%}88%,100%{left:125%}}
@media(max-width:1050px){.mx-naya-doors{grid-template-columns:1fr 1fr}.mx-naya-door:last-child{grid-column:1/-1}.mx-naya-playground-head{display:block}.mx-naya-playground-head p{margin-top:14px}}
@media(max-width:850px){.mx-growth-grid{grid-template-columns:1fr}.mx-band-rail{grid-template-columns:repeat(2,1fr)}}
@media(max-width:620px){.mx-plan{grid-template-columns:1fr}.mx-scorecard-row{grid-template-columns:100px 1fr 38px}.mx-growth-cta{flex-direction:column}.mx-growth-cta .mx-cta{width:100%}.mx-naya-doors{grid-template-columns:1fr}.mx-naya-door:last-child{grid-column:auto}.mx-naya-door{min-height:280px}.mx-naya-icon{margin-bottom:40px}}
@media(prefers-reduced-motion:reduce){#maxess-results-10 .mx-score-orb,#maxess-results-10 .mx-score-orb::before,#maxess-results-10 .mx-cta-primary::after{animation:none!important}#maxess-results-10 .mx-naya-door,#maxess-results-10 .mx-mini{transition:none!important}}
</style>"""

HTML = """<section class=\"mx-section mx-growth\" id=\"growth-scorecard\">
<div class=\"mx-wide\">
<div class=\"mx-section-head\"><div><span class=\"mx-eyebrow\">06 · TURN INSIGHT INTO GROWTH</span><h2>Know where you are.<br>Know what moves you.</h2></div><p>A useful assessment should not leave you staring at a score. This chapter turns the result into practical direction: protect the strength, build the lever, and make progress repeatable.</p></div>
<div class=\"mx-growth-grid\">
<article class=\"mx-growth-card mx-reveal\"><span class=\"mx-eyebrow\">YOUR SCORECARD</span><h3>Strong enough to leverage.<br>Honest enough to improve.</h3><p>Your profile is not a judgment. It is a starting position. Make your strongest capability more useful and your biggest gap less limiting.</p><div class=\"mx-scorecard\">
<div class=\"mx-scorecard-row\"><span>Direction</span><div class=\"mx-scorecard-track\"><i style=\"--w:86%\"></i></div><b>86</b></div>
<div class=\"mx-scorecard-row\"><span>Communication</span><div class=\"mx-scorecard-track\"><i style=\"--w:91%\"></i></div><b>91</b></div>
<div class=\"mx-scorecard-row\"><span>Evaluation</span><div class=\"mx-scorecard-track\"><i style=\"--w:79%\"></i></div><b>79</b></div>
<div class=\"mx-scorecard-row\"><span>Iteration</span><div class=\"mx-scorecard-track\"><i style=\"--w:74%\"></i></div><b>74</b></div>
<div class=\"mx-scorecard-row\"><span>Systems Thinking</span><div class=\"mx-scorecard-track\"><i style=\"--w:68%\"></i></div><b>68</b></div>
</div></article>
<article class=\"mx-growth-card mx-reveal\"><span class=\"mx-eyebrow\">YOUR MASTERY RANGE</span><h3>You're in<br>Advancing.</h3><p>The next jump is not about collecting more AI tools. It is about directing better work, evaluating it deliberately, and turning wins into systems.</p><div class=\"mx-band-rail\" aria-label=\"MAXESS score bands\"><div><strong>Foundation</strong><span>0–50</span></div><div><strong>Developing</strong><span>51–75</span></div><div class=\"active\"><strong>Advancing</strong><span>76–90</span></div><div><strong>Mastering</strong><span>91–100</span></div></div><div class=\"mx-growth-cta\"><a class=\"mx-cta mx-cta-primary\" href=\"https://takeyourpowerback.xyz/services\">Start Free <span aria-hidden=\"true\">→</span></a><a class=\"mx-cta mx-cta-ghost\" href=\"#naya-report\">Listen with Naya <span aria-hidden=\"true\">↓</span></a></div><p class=\"mx-micro\">Zero Cost Start / Free Trial · Continue into the NayaNET experience.</p></article>
</div>
<div class=\"mx-plan\"><div class=\"mx-reveal\"><b>NEXT 01</b><h4>Protect your strength</h4><p>Use Communication as your directing advantage.</p></div><div class=\"mx-reveal\"><b>NEXT 02</b><h4>Build your lever</h4><p>Practice Systems Thinking on one repeated workflow.</p></div><div class=\"mx-reveal\"><b>NEXT 03</b><h4>Make quality visible</h4><p>Score every meaningful AI output before accepting it.</p></div></div>
</div></section><div class=\"mx-divider\"></div>

<section class=\"mx-section mx-naya-playground\" id=\"naya-playground\">
<div class=\"mx-wide\">
<div class=\"mx-naya-playground-head\"><div><span class=\"mx-eyebrow\">YOUR AI PLAYGROUND</span><h2>Don't learn AI.<br><em style=\"font-style:normal;background:linear-gradient(110deg,#fff,#d7b2ff,#63d9ff);-webkit-background-clip:text;background-clip:text;color:transparent\">Learn what AI can do for you.</em></h2></div><p>These aren't random tools. They're doors into what your capability can become when Naya helps you turn thinking into action.</p></div>
<div class=\"mx-naya-doors\">
<a class=\"mx-naya-door mx-reveal\" href=\"#naya-writer\" aria-label=\"Open Naya Writer\"><span class=\"mx-naya-icon\" aria-hidden=\"true\">✍️</span><h3>Naya Writer</h3><p>Turn thoughts, rough ideas, and half-finished sentences into clear words that sound like you.</p><span class=\"mx-naya-open\">Open Naya Writer <span aria-hidden=\"true\">↗</span></span></a>
<a class=\"mx-naya-door mx-reveal\" href=\"#naya-brainstormer\" aria-label=\"Open Naya Brainstormer\"><span class=\"mx-naya-icon\" aria-hidden=\"true\">💡</span><h3>Naya Brainstormer</h3><p>Turn one thought into possibilities, angles, strategies, names, stories, and next moves.</p><span class=\"mx-naya-open\">Open Naya Brainstormer <span aria-hidden=\"true\">↗</span></span></a>
<a class=\"mx-naya-door mx-reveal\" href=\"#naya\" aria-label=\"Talk to Naya\"><span class=\"mx-naya-icon\" aria-hidden=\"true\">✦</span><h3>Naya</h3><p>Ask anything. Build anything. Think out loud with an AI companion designed around what you want to accomplish.</p><span class=\"mx-naya-open\">Talk to Naya <span aria-hidden=\"true\">↗</span></span></a>
</div>
<p class=\"mx-naya-note\">These are doors, not products. The goal is simple: make AI useful to you.</p>
</div></section><div class=\"mx-divider\"></div>"""

for path in FILES:
    if not path.exists():
        continue
    text = path.read_text(encoding='utf-8')
    changed = False
    if 'id="growth-scorecard"' not in text:
        marker = '<section class="mx-section mx-naya-bridge" id="naya-report">'
        if marker not in text:
            raise SystemExit(f'Missing insertion marker: {path.name}')
        if '</head>' in text:
            text = text.replace('</head>', CSS + '</head>', 1)
        else:
            text = CSS + text
        text = text.replace(marker, HTML + marker, 1)
        changed = True
    elif 'id="naya-playground"' not in text:
        marker = '<section class="mx-section mx-naya-bridge" id="naya-report">'
        if marker not in text:
            raise SystemExit(f'Missing Naya insertion marker: {path.name}')
        if 'maxess-results-10-growth-layer' not in text and '</head>' in text:
            text = text.replace('</head>', CSS + '</head>', 1)
        text = text.replace(marker, HTML.split('<section class="mx-section mx-naya-playground"',1)[1].split('</section><div class="mx-divider"></div>',1)[0].join(['<section class="mx-section mx-naya-playground"','</section><div class="mx-divider"></div>']), 1)
        changed = True
    if changed:
        path.write_text(text, encoding='utf-8')
        print(path.name, 'enhanced', len(text.encode()))
    else:
        print(path.name, 'already enhanced')
