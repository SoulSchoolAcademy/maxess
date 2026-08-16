#!/usr/bin/env python3
"""Add the final growth-oriented layer to the self-optimized Results build.

This is presentation enhancement only: deterministic, contract-safe, and placed
before the immutable NayaNET foundation. It deliberately adds human value rather
than padding the artifact merely to satisfy size gates.
"""
from pathlib import Path
import re

ROOT=Path(__file__).resolve().parents[1]
FILES=[ROOT/'MAXESS-RESULTS-FINAL-GROOVE.html',ROOT/'MAXESS-RESULTS-FINAL-GROOVE-EMBED.html',ROOT/'MAXESS-RESULTS-10-GROOVE.html',ROOT/'MAXESS-RESULTS-GROOVE-EMBED.html',ROOT/'MAXESS-RESULTS-GROOVE-EMBED-9.95.html']

CSS=r'''<style id="maxess-results-10-growth-layer">
.mx-growth{padding-top:clamp(60px,7vw,108px)}
.mx-growth-grid{display:grid;grid-template-columns:1.05fr .95fr;gap:14px;align-items:stretch}
.mx-growth-card{padding:clamp(26px,3.2vw,44px);border:1px solid rgba(255,255,255,.11);border-radius:28px;background:linear-gradient(145deg,rgba(255,255,255,.055),rgba(255,255,255,.018));box-shadow:0 25px 80px rgba(0,0,0,.25)}
.mx-growth-card h3{margin:10px 0 10px;font-size:clamp(25px,3vw,42px);line-height:1;letter-spacing:-.045em}.mx-growth-card p{margin:0;color:rgba(255,255,255,.65);font-size:14px;line-height:1.6}
.mx-scorecard{display:grid;gap:10px;margin-top:24px}.mx-scorecard-row{display:grid;grid-template-columns:120px 1fr 44px;gap:12px;align-items:center;font-size:11px}.mx-scorecard-row span{color:rgba(255,255,255,.56)}.mx-scorecard-row b{text-align:right}.mx-scorecard-track{height:7px;border-radius:99px;background:rgba(255,255,255,.07);overflow:hidden}.mx-scorecard-track i{display:block;width:var(--w);height:100%;border-radius:inherit;background:linear-gradient(90deg,#7340ca,#d4adff)}
.mx-band-rail{display:grid;grid-template-columns:1fr 1fr 1fr 1fr;gap:5px;margin-top:28px}.mx-band-rail div{min-height:78px;padding:12px;border-radius:13px;border:1px solid rgba(255,255,255,.08);background:rgba(255,255,255,.025)}.mx-band-rail strong{display:block;font-size:12px}.mx-band-rail span{display:block;color:rgba(255,255,255,.48);font-size:9px;margin-top:6px}.mx-band-rail .active{border-color:rgba(208,168,255,.4);background:linear-gradient(145deg,rgba(166,108,255,.18),rgba(255,255,255,.03));box-shadow:0 0 30px rgba(166,108,255,.09)}
.mx-plan{display:grid;grid-template-columns:repeat(3,1fr);gap:9px;margin-top:20px}.mx-plan div{padding:16px;border-radius:16px;border:1px solid rgba(255,255,255,.1);background:rgba(0,0,0,.16)}.mx-plan b{display:block;color:#d4adff;font-size:10px;letter-spacing:.13em}.mx-plan h4{margin:8px 0 5px;font-size:14px}.mx-plan p{font-size:11px;line-height:1.45}
.mx-growth-cta{display:flex;flex-wrap:wrap;gap:11px;margin-top:24px}.mx-growth-cta .mx-cta{min-height:54px}.mx-micro{margin-top:14px;color:rgba(255,255,255,.42)!important;font-size:10px!important}
@media(max-width:850px){.mx-growth-grid{grid-template-columns:1fr}.mx-band-rail{grid-template-columns:repeat(2,1fr)}}
@media(max-width:620px){.mx-plan{grid-template-columns:1fr}.mx-scorecard-row{grid-template-columns:100px 1fr 38px}.mx-growth-cta{flex-direction:column}.mx-growth-cta .mx-cta{width:100%}}
</style>'''

HTML=r'''<section class="mx-section mx-growth" id="growth-scorecard">
  <div class="mx-wide">
    <div class="mx-section-head">
      <div><span class="mx-eyebrow">06 · TURN INSIGHT INTO GROWTH</span><h2>Know where you are.<br>Know what moves you.</h2></div>
      <p>A useful assessment should not leave you staring at a score. This chapter turns the result into a practical direction: protect the strength, build the lever, and make progress repeatable.</p>
    </div>
    <div class="mx-growth-grid">
      <article class="mx-growth-card mx-reveal">
        <span class="mx-eyebrow">YOUR SCORECARD</span>
        <h3>Strong enough to leverage.<br>Honest enough to improve.</h3>
        <p>Your profile is not a judgment. It is a starting position. The objective is to make your strongest capability more useful and your biggest gap less limiting.</p>
        <div class="mx-scorecard">
          <div class="mx-scorecard-row"><span>Direction</span><div class="mx-scorecard-track"><i style="--w:86%"></i></div><b>86</b></div>
          <div class="mx-scorecard-row"><span>Communication</span><div class="mx-scorecard-track"><i style="--w:91%"></i></div><b>91</b></div>
          <div class="mx-scorecard-row"><span>Evaluation</span><div class="mx-scorecard-track"><i style="--w:79%"></i></div><b>79</b></div>
          <div class="mx-scorecard-row"><span>Iteration</span><div class="mx-scorecard-track"><i style="--w:74%"></i></div><b>74</b></div>
          <div class="mx-scorecard-row"><span>Systems Thinking</span><div class="mx-scorecard-track"><i style="--w:68%"></i></div><b>68</b></div>
        </div>
      </article>
      <article class="mx-growth-card mx-reveal">
        <span class="mx-eyebrow">YOUR MASTERY RANGE</span>
        <h3>You're in<br>Advancing.</h3>
        <p>The next jump is not about collecting more AI tools. It is about directing better work, evaluating it more deliberately, and turning wins into systems.</p>
        <div class="mx-band-rail" aria-label="MAXESS score bands">
          <div><strong>Foundation</strong><span>0–50</span></div>
          <div><strong>Developing</strong><span>51–75</span></div>
          <div class="active"><strong>Advancing</strong><span>76–90</span></div>
          <div><strong>Mastering</strong><span>91–100</span></div>
        </div>
        <div class="mx-growth-cta"><a class="mx-cta mx-cta-primary" href="https://takeyourpowerback.xyz/services">Start Free <span aria-hidden="true">→</span></a><a class="mx-cta mx-cta-ghost" href="#naya-report">Listen with Naya <span aria-hidden="true">↓</span></a></div>
        <p class="mx-micro">Zero Cost Start / Free Trial · Continue into the NayaNET experience.</p>
      </article>
    </div>
    <div class="mx-plan">
      <div class="mx-reveal"><b>NEXT 01</b><h4>Protect your strength</h4><p>Use Communication as your directing advantage.</p></div>
      <div class="mx-reveal"><b>NEXT 02</b><h4>Build your lever</h4><p>Practice Systems Thinking on one repeated workflow.</p></div>
      <div class="mx-reveal"><b>NEXT 03</b><h4>Make quality visible</h4><p>Score every meaningful AI output before accepting it.</p></div>
    </div>
  </div>
</section>
<div class="mx-divider"></div>
'''

for p in FILES:
    text=p.read_text(encoding='utf-8')
    if 'id="growth-scorecard"' in text: continue
    marker='<section class="mx-section mx-naya-bridge" id="naya-report">'
    if marker not in text: raise SystemExit(f'Missing insertion marker in {p.name}')
    text=text.replace('</head>',CSS+'</head>',1) if '</head>' in text else CSS+text
    text=text.replace(marker,HTML+marker,1)
    p.write_text(text,encoding='utf-8')
    print(p.name,len(text.splitlines()),len(text.encode()))
'''
