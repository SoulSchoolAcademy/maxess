#!/usr/bin/env python3
"""Build the self-optimized MAXESS Results experience.

This builder is intentionally a new presentation layer. It does not promote an
old 9.x/9.95/10 artifact to final authority. It consumes deterministic
assessment fixtures for development and appends the real NayaNET Page Code as
the immutable final chapter/foundation.
"""
from pathlib import Path
import html
import json
import re

ROOT = Path(__file__).resolve().parents[1]
NAYA = ROOT / "nayanetpagecode"
OUT_FULL = ROOT / "MAXESS-RESULTS-FINAL-GROOVE.html"
OUT_EMBED = ROOT / "MAXESS-RESULTS-FINAL-GROOVE-EMBED.html"
ALIASES = [
    ROOT / "MAXESS-RESULTS-10-GROOVE.html",
    ROOT / "MAXESS-RESULTS-GROOVE-EMBED.html",
    ROOT / "MAXESS-RESULTS-GROOVE-EMBED-9.95.html",
]

FIXTURE = {
    "contract": "MAXESS-RESULTS-CONTRACT-1",
    "mode": "development-fixture",
    "score": 82,
    "band": "Advancing",
    "dimensions": [
        ("Direction", 86, "You usually know what you want AI to help you accomplish.", "Define the outcome and success test before asking AI to work."),
        ("Communication", 91, "You are strong at expressing context, intent, and the human outcome behind a request.", "Turn that strength into reusable instructions, briefs, and decision frameworks."),
        ("Evaluation", 79, "You can recognize useful work, with a major opportunity in deliberate judgment.", "Use a visible scorecard before accepting an answer or artifact."),
        ("Iteration", 74, "You understand that quality improves through refinement rather than one-shot prompting.", "Make improvement loops explicit: create, score, improve, repeat."),
        ("Systems Thinking", 68, "You can see the bigger system, with an opportunity to connect repeated work.", "Turn repeated work into reusable systems, components, and operating rules."),
    ],
    "areas": [
        ("Writing & Communication", "Turn ideas into clear instructions, messages, stories, and decisions."),
        ("Research & Information", "Find, compare, synthesize, and explain useful information."),
        ("Brainstorming & Ideas", "Expand possibilities without losing the goal."),
        ("Content Creation", "Create useful, human content faster and better."),
        ("Business & Strategy", "Turn insight into positioning, offers, decisions, and plans."),
        ("Marketing & Sales", "Make value understandable and action easier."),
        ("Learning & Education", "Use AI as a tutor, curriculum designer, and thinking partner."),
        ("Coding & Software", "Build, debug, explain, and improve software with AI."),
        ("Images & Visual Creation", "Turn concepts into visual communication and creative assets."),
        ("Video & Media", "Plan, script, edit, package, and distribute media."),
        ("Documents & Presentations", "Transform raw thinking into polished deliverables."),
        ("Data & Analysis", "Use evidence, structure, and models to make better decisions."),
        ("Productivity & Planning", "Turn intention into organized execution."),
        ("Career & Professional Development", "Build skills, positioning, confidence, and opportunity."),
        ("Personal Decision-Making", "Think through choices with more clarity and less noise."),
        ("Creative Work", "Explore, shape, and finish original creative work."),
        ("Automation & Systems", "Connect repeatable work into reliable systems."),
        ("Advanced AI Work", "Orchestrate models, agents, tools, context, and evaluation."),
    ],
}
BANDS = ((0,50,"Foundation"),(51,75,"Developing"),(76,90,"Advancing"),(91,100,"Mastering"))

def esc(v): return html.escape(str(v), quote=True)
def band(score):
    for lo, hi, name in BANDS:
        if lo <= score <= hi: return name
    raise ValueError(score)

def dim_cards():
    out=[]
    for i,(name,score,meaning,action) in enumerate(FIXTURE["dimensions"],1):
        out.append(f'''<article class="mx-dim mx-reveal" data-score="{score}">
          <div class="mx-dim-head"><span class="mx-kicker">0{i}</span><h3>{esc(name)}</h3><strong>{score}<small>/100</small></strong></div>
          <div class="mx-track"><span style="--w:{score}%"></span></div>
          <p>{esc(meaning)}</p>
          <div class="mx-lever"><span>LEVER</span><b>{esc(action)}</b></div>
        </article>''')
    return ''.join(out)

def area_cards():
    out=[]
    for i,(name,desc) in enumerate(FIXTURE["areas"],1):
        relevance=[91,86,84,82,79][i%5]
        out.append(f'''<article class="mx-area mx-reveal" data-index="{i}" data-name="{esc(name)}">
          <div class="mx-area-num">{i:02d}</div>
          <div class="mx-area-main"><h3>{esc(name)}</h3><p>{esc(desc)}</p></div>
          <div class="mx-area-relevance"><span>PATHWAY</span><i><em style="--w:{relevance}%"></em></i></div>
          <button class="mx-mini" type="button" data-area="{esc(name)}">Explore <span aria-hidden="true">↗</span></button>
        </article>''')
    return ''.join(out)

def css():
    return r'''<style id="maxess-results-10-system">
:root{--mx-bg:#040307;--mx-ink:#fff;--mx-soft:rgba(255,255,255,.72);--mx-muted:rgba(255,255,255,.48);--mx-line:rgba(255,255,255,.12);--mx-purple:#a66cff;--mx-violet:#d0a8ff;--mx-gold:#f7d58c;--mx-green:#51e2ad;--mx-max:1500px;--mx-read:960px;--mx-ease:cubic-bezier(.2,.8,.2,1)}
#maxess-results-10{position:relative;width:100%;overflow:hidden;color:var(--mx-ink);background:#040307;font-family:Inter,ui-sans-serif,system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;line-height:1.5;isolation:isolate}
#maxess-results-10,#maxess-results-10 *{box-sizing:border-box}#maxess-results-10 button{font:inherit}
#maxess-results-10::before{content:"";position:absolute;inset:0;z-index:-3;background:radial-gradient(ellipse 80% 30% at 50% 0,rgba(171,92,255,.36),transparent 70%),radial-gradient(ellipse 42% 26% at 4% 18%,rgba(100,50,255,.13),transparent 72%),radial-gradient(ellipse 42% 26% at 96% 38%,rgba(45,155,255,.09),transparent 72%),linear-gradient(180deg,#12071b 0,#09050d 22%,#050408 56%,#030204 100%)}
#maxess-results-10::after{content:"";position:absolute;inset:0;z-index:-2;pointer-events:none;opacity:.18;background-image:radial-gradient(rgba(255,255,255,.2) .55px,transparent .7px);background-size:5px 5px;mask-image:linear-gradient(#000,transparent 72%)}
.mx-wrap{width:100%;margin:0 auto}.mx-reading{width:min(var(--mx-read),100%);margin:0 auto}.mx-wide{width:min(var(--mx-max),100%);margin:0 auto}
.mx-section{position:relative;width:100%;padding:clamp(64px,7vw,116px) clamp(20px,4vw,72px)}
.mx-reveal{opacity:0;transform:translateY(22px);transition:opacity .8s var(--mx-ease),transform .8s var(--mx-ease)}.mx-reveal.is-visible{opacity:1;transform:none}
.mx-eyebrow{display:inline-flex;align-items:center;gap:10px;color:var(--mx-violet);font-size:11px;font-weight:800;letter-spacing:.18em;text-transform:uppercase}.mx-eyebrow::before{content:"";width:28px;height:1px;background:linear-gradient(90deg,var(--mx-purple),transparent)}
.mx-title{margin:14px 0 0;font-size:clamp(40px,6.1vw,92px);line-height:.94;letter-spacing:-.055em;font-weight:780}.mx-title em{font-style:normal;background:linear-gradient(110deg,#fff 12%,#d9b7ff 48%,#9b5cff 82%);-webkit-background-clip:text;background-clip:text;color:transparent}.mx-copy{max-width:760px;margin:20px 0 0;color:var(--mx-soft);font-size:clamp(16px,1.5vw,21px);line-height:1.55}
.mx-hero{min-height:min(850px,92vh);display:flex;align-items:center;padding-top:clamp(72px,8vw,130px);padding-bottom:clamp(60px,7vw,100px)}.mx-hero::before{content:"";position:absolute;width:min(800px,85vw);height:520px;left:50%;top:7%;transform:translateX(-50%);background:radial-gradient(circle,rgba(166,108,255,.22),transparent 68%);filter:blur(12px);z-index:-1}
.mx-hero-grid{display:grid;grid-template-columns:minmax(0,1.05fr) minmax(340px,.7fr);gap:clamp(36px,7vw,110px);align-items:center}.mx-score-orb{position:relative;aspect-ratio:1;border-radius:50%;width:min(430px,76vw);margin:auto;display:grid;place-items:center;background:radial-gradient(circle at 32% 25%,rgba(255,255,255,.28),transparent 10%),radial-gradient(circle at 50% 48%,#2b1645 0,#13091e 42%,#08050c 72%,#030205 100%);box-shadow:0 0 0 1px rgba(255,255,255,.16),inset 0 0 70px rgba(174,92,255,.17),0 35px 100px rgba(0,0,0,.62),0 0 100px rgba(148,74,255,.2)}.mx-score-orb::before{content:"";position:absolute;inset:10%;border:1px solid rgba(208,168,255,.28);border-radius:50%;box-shadow:0 0 45px rgba(166,108,255,.16)}.mx-score-orb::after{content:"";position:absolute;inset:17%;border:1px solid rgba(255,255,255,.08);border-radius:50%}.mx-score{position:relative;text-align:center;z-index:2}.mx-score strong{display:block;font-size:clamp(88px,11vw,150px);line-height:.78;letter-spacing:-.08em;font-weight:800}.mx-score span{display:block;margin-top:24px;color:var(--mx-violet);font-size:12px;font-weight:900;letter-spacing:.22em;text-transform:uppercase}.mx-band{display:inline-flex;margin-top:16px;padding:9px 14px;border:1px solid rgba(208,168,255,.28);border-radius:999px;background:rgba(166,108,255,.08);color:#fff;font-size:12px;font-weight:800;letter-spacing:.1em;text-transform:uppercase}
.mx-hero-actions{display:flex;flex-wrap:wrap;gap:12px;margin-top:30px}.mx-cta{display:inline-flex;align-items:center;justify-content:center;gap:11px;min-height:56px;padding:0 22px;border-radius:16px;border:1px solid rgba(255,255,255,.18);color:#fff;text-decoration:none;font-weight:800;cursor:pointer;transition:transform .2s var(--mx-ease),filter .2s ease,background .2s ease}.mx-cta:hover{transform:translateY(-3px);filter:brightness(1.08)}.mx-cta-primary{background:linear-gradient(135deg,#d7b2ff,#8244e7 45%,#42117e);box-shadow:0 14px 34px rgba(101,43,180,.3),inset 0 1px rgba(255,255,255,.6)}.mx-cta-ghost{background:rgba(255,255,255,.055)}
.mx-proof{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin-top:42px}.mx-proof div{padding:16px 18px;border-left:1px solid rgba(208,168,255,.3)}.mx-proof b{display:block;font-size:13px}.mx-proof span{display:block;color:var(--mx-muted);font-size:12px;margin-top:3px}
.mx-divider{height:1px;background:linear-gradient(90deg,transparent,var(--mx-line),transparent);margin:0 auto;width:min(1400px,88%)}
.mx-section-head{display:flex;align-items:end;justify-content:space-between;gap:28px;margin-bottom:34px}.mx-section-head h2{margin:8px 0 0;font-size:clamp(30px,4vw,62px);line-height:.98;letter-spacing:-.045em}.mx-section-head p{max-width:540px;margin:0;color:var(--mx-muted);font-size:15px;line-height:1.6}
.mx-insight{padding-top:clamp(70px,7vw,110px);padding-bottom:clamp(56px,6vw,92px)}.mx-insight-card{position:relative;overflow:hidden;padding:clamp(28px,4vw,56px);border:1px solid rgba(208,168,255,.18);border-radius:32px;background:linear-gradient(135deg,rgba(174,92,255,.12),rgba(255,255,255,.035) 44%,rgba(0,0,0,.18));box-shadow:0 35px 100px rgba(0,0,0,.3)}.mx-insight-card::after{content:"";position:absolute;width:280px;height:280px;right:-100px;top:-120px;border-radius:50%;background:radial-gradient(circle,rgba(166,108,255,.3),transparent 68%);filter:blur(10px)}.mx-quote{position:relative;z-index:1;max-width:1050px;margin:0;font-size:clamp(27px,3.6vw,52px);line-height:1.08;letter-spacing:-.04em}.mx-quote strong{color:#d6b3ff}.mx-note{position:relative;z-index:1;margin:22px 0 0;max-width:760px;color:var(--mx-soft);font-size:16px}
.mx-dim-grid{display:grid;grid-template-columns:repeat(5,minmax(0,1fr));gap:12px}.mx-dim{min-height:330px;padding:22px;border:1px solid var(--mx-line);border-radius:24px;background:linear-gradient(160deg,rgba(255,255,255,.065),rgba(255,255,255,.018));transition:transform .25s var(--mx-ease),border-color .25s ease,background .25s ease}.mx-dim:hover{transform:translateY(-5px);border-color:rgba(208,168,255,.3);background:linear-gradient(160deg,rgba(166,108,255,.1),rgba(255,255,255,.02))}.mx-dim-head{display:grid;grid-template-columns:auto 1fr auto;gap:12px;align-items:start}.mx-dim-head h3{margin:0;font-size:17px;line-height:1.1}.mx-dim-head strong{font-size:24px;line-height:1}.mx-dim-head strong small{font-size:9px;color:var(--mx-muted);font-weight:500}.mx-kicker{color:var(--mx-muted);font-size:10px;font-weight:900;letter-spacing:.12em}.mx-track{height:5px;margin:25px 0 18px;border-radius:99px;background:rgba(255,255,255,.08);overflow:hidden}.mx-track span{display:block;width:var(--w);height:100%;border-radius:inherit;background:linear-gradient(90deg,#7540ca,#d1a5ff);box-shadow:0 0 16px rgba(166,108,255,.35)}.mx-dim p{color:var(--mx-soft);font-size:13px;line-height:1.55;margin:0}.mx-lever{margin-top:22px;padding-top:16px;border-top:1px solid var(--mx-line)}.mx-lever span{display:block;color:var(--mx-violet);font-size:9px;font-weight:900;letter-spacing:.15em}.mx-lever b{display:block;margin-top:6px;color:#fff;font-size:12px;line-height:1.4}
.mx-fingerprint{display:grid;grid-template-columns:minmax(320px,.8fr) minmax(0,1.2fr);gap:clamp(34px,7vw,100px);align-items:center}.mx-radar{position:relative;width:min(560px,90vw);aspect-ratio:1;margin:auto;display:grid;place-items:center}.mx-radar svg{width:100%;height:100%;overflow:visible}.mx-radar-center{position:absolute;text-align:center}.mx-radar-center b{display:block;font-size:54px;letter-spacing:-.06em}.mx-radar-center span{color:var(--mx-muted);font-size:10px;letter-spacing:.16em;text-transform:uppercase}.mx-list{display:grid;gap:10px}.mx-list-row{display:grid;grid-template-columns:32px 1fr auto;gap:14px;align-items:center;padding:15px 16px;border:1px solid var(--mx-line);border-radius:16px;background:rgba(255,255,255,.03)}.mx-list-row b{font-size:13px}.mx-list-row span{color:var(--mx-muted);font-size:11px}.mx-list-row strong{font-size:16px}.mx-bar{height:4px;grid-column:2/-1;margin-top:-4px;border-radius:99px;background:rgba(255,255,255,.07);overflow:hidden}.mx-bar i{display:block;width:var(--w);height:100%;background:linear-gradient(90deg,#7a42d2,#d0a7ff)}
.mx-contrast{display:grid;grid-template-columns:1fr 1fr;gap:14px}.mx-panel{position:relative;min-height:300px;padding:32px;border-radius:28px;border:1px solid var(--mx-line);overflow:hidden}.mx-panel::after{content:"";position:absolute;width:260px;height:260px;border-radius:50%;right:-100px;bottom:-130px;filter:blur(4px)}.mx-panel-power{background:linear-gradient(135deg,rgba(81,226,173,.1),rgba(255,255,255,.025))}.mx-panel-power::after{background:radial-gradient(circle,rgba(81,226,173,.18),transparent 68%)}.mx-panel-lever{background:linear-gradient(135deg,rgba(166,108,255,.13),rgba(255,255,255,.025))}.mx-panel-lever::after{background:radial-gradient(circle,rgba(166,108,255,.2),transparent 68%)}.mx-panel .mx-eyebrow{color:var(--mx-gold)}.mx-panel h3{position:relative;z-index:1;font-size:clamp(28px,3vw,46px);line-height:1;letter-spacing:-.04em;margin:16px 0}.mx-panel p{position:relative;z-index:1;max-width:520px;color:var(--mx-soft);font-size:15px}
.mx-path{display:grid;grid-template-columns:repeat(4,1fr);gap:12px}.mx-step{padding:22px;border:1px solid var(--mx-line);border-radius:22px;background:rgba(255,255,255,.03)}.mx-step strong{display:block;color:var(--mx-violet);font-size:11px;letter-spacing:.14em}.mx-step h3{font-size:19px;margin:12px 0 7px}.mx-step p{margin:0;color:var(--mx-muted);font-size:13px}
.mx-areas{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:10px}.mx-area{display:grid;grid-template-columns:42px 1fr 90px auto;gap:15px;align-items:center;padding:17px 18px;border:1px solid var(--mx-line);border-radius:18px;background:rgba(255,255,255,.027);transition:transform .22s var(--mx-ease),background .22s ease,border-color .22s ease}.mx-area:hover{transform:translateX(4px);background:rgba(166,108,255,.065);border-color:rgba(208,168,255,.26)}.mx-area-num{color:var(--mx-muted);font-size:10px;font-weight:900}.mx-area-main h3{font-size:14px;margin:0}.mx-area-main p{font-size:11px;color:var(--mx-muted);margin:4px 0 0;line-height:1.35}.mx-area-relevance span{display:block;color:var(--mx-muted);font-size:8px;letter-spacing:.12em}.mx-area-relevance i{display:block;height:4px;margin-top:6px;border-radius:99px;background:rgba(255,255,255,.08);overflow:hidden}.mx-area-relevance em{display:block;width:var(--w);height:100%;background:linear-gradient(90deg,#7740d0,#d0a6ff)}.mx-mini{padding:9px 11px;border:1px solid rgba(255,255,255,.14)!important;border-radius:10px;background:rgba(255,255,255,.05);color:#fff;cursor:pointer;font-size:10px;font-weight:800}.mx-mini:hover{background:rgba(166,108,255,.16)}
.mx-naya-bridge{padding-top:clamp(78px,9vw,130px);padding-bottom:clamp(60px,7vw,100px);text-align:center}.mx-bridge-card{position:relative;overflow:hidden;padding:clamp(34px,6vw,82px) 22px;border-radius:36px;border:1px solid rgba(208,168,255,.2);background:radial-gradient(circle at 50% 0,rgba(166,108,255,.22),transparent 50%),linear-gradient(180deg,rgba(255,255,255,.055),rgba(255,255,255,.018));box-shadow:0 45px 120px rgba(0,0,0,.42)}.mx-bridge-card h2{font-size:clamp(36px,5vw,70px);line-height:.96;letter-spacing:-.055em;margin:12px auto;max-width:850px}.mx-bridge-card p{max-width:670px;margin:18px auto 28px;color:var(--mx-soft);font-size:16px}.mx-audio-label{display:inline-flex;align-items:center;gap:8px;color:var(--mx-gold);font-size:11px;font-weight:900;letter-spacing:.14em;text-transform:uppercase}.mx-audio-label::before{content:"◉";font-size:9px}.mx-key{display:grid;grid-template-columns:repeat(7,1fr);gap:8px;margin:32px auto 0;max-width:1080px}.mx-key div{position:relative;padding:18px 10px;border:1px solid var(--mx-line);border-radius:15px;background:rgba(255,255,255,.035);font-size:12px;font-weight:900}.mx-key div:not(:last-child)::after{content:"→";position:absolute;right:-10px;top:50%;transform:translateY(-50%);color:var(--mx-violet);z-index:2}.mx-final{padding-bottom:20px}.mx-final-note{margin:0 auto 18px;text-align:center;color:var(--mx-muted);font-size:11px;letter-spacing:.1em;text-transform:uppercase}
@media(max-width:1050px){.mx-hero-grid,.mx-fingerprint{grid-template-columns:1fr}.mx-score-orb{width:min(360px,72vw)}.mx-dim-grid{grid-template-columns:repeat(2,1fr)}.mx-dim:last-child{grid-column:1/-1}.mx-path{grid-template-columns:repeat(2,1fr)}.mx-areas{grid-template-columns:1fr}.mx-area-relevance{display:none}}
@media(max-width:720px){.mx-section{padding:58px 16px}.mx-hero{min-height:auto;padding-top:74px}.mx-title{font-size:clamp(42px,13vw,66px)}.mx-copy{font-size:15px}.mx-hero-grid{gap:42px}.mx-score-orb{width:min(290px,78vw)}.mx-score strong{font-size:90px}.mx-proof{grid-template-columns:1fr;gap:0}.mx-proof div{border-left:0;border-top:1px solid rgba(208,168,255,.22)}.mx-section-head{display:block}.mx-section-head p{margin-top:14px}.mx-dim-grid{grid-template-columns:1fr}.mx-dim:last-child{grid-column:auto}.mx-contrast{grid-template-columns:1fr}.mx-panel{min-height:260px}.mx-path{grid-template-columns:1fr}.mx-area{grid-template-columns:32px 1fr auto}.mx-area-main p{display:none}.mx-key{grid-template-columns:1fr 1fr;gap:8px}.mx-key div:not(:last-child)::after{display:none}.mx-hero-actions{flex-direction:column}.mx-cta{width:100%}}
@media(prefers-reduced-motion:reduce){#maxess-results-10 *{scroll-behavior:auto!important;animation:none!important;transition:none!important}.mx-reveal{opacity:1;transform:none}}
</style>'''

def radar():
    vals=[d[1] for d in FIXTURE["dimensions"]]; cx=250;cy=250;r=170
    pts=[]
    for i,v in enumerate(vals):
        import math
        a=-math.pi/2+i*(2*math.pi/5); rr=r*v/100; pts.append(f"{cx+math.cos(a)*rr:.1f},{cy+math.sin(a)*rr:.1f}")
    grid=[]
    for level in (25,50,75,100):
        import math
        p=[]
        for i in range(5):
            a=-math.pi/2+i*(2*math.pi/5); rr=r*level/100;p.append(f"{cx+math.cos(a)*rr:.1f},{cy+math.sin(a)*rr:.1f}")
        grid.append(f'<polygon points="{" ".join(p)}" fill="none" stroke="rgba(255,255,255,.09)" stroke-width="1"/>')
    axes=[]
    for i in range(5):
        import math
        a=-math.pi/2+i*(2*math.pi/5); axes.append(f'<line x1="{cx}" y1="{cy}" x2="{cx+math.cos(a)*r}" y2="{cy+math.sin(a)*r}" stroke="rgba(255,255,255,.08)"/>')
    return '<svg viewBox="0 0 500 500" role="img" aria-label="Five-dimension capability fingerprint">'+''.join(grid)+''.join(axes)+f'<polygon points="{" ".join(pts)}" fill="rgba(166,108,255,.2)" stroke="#cda5ff" stroke-width="3" stroke-linejoin="round"/>'+''.join(f'<circle cx="{p.split(",")[0]}" cy="{p.split(",")[1]}" r="5" fill="#fff" stroke="#a66cff" stroke-width="3"/>' for p in pts)+'</svg>'

def html_body():
    score=FIXTURE["score"]
    rows=''.join(f'<div class="mx-list-row"><span>{i:02d}</span><b>{esc(name)}</b><strong>{v}</strong><div class="mx-bar"><i style="--w:{v}%"></i></div></div>' for i,(name,v,_,_) in enumerate(FIXTURE["dimensions"],1))
    return f'''<main id="maxess-results-10" data-contract="{esc(FIXTURE["contract"])}" data-mode="{esc(FIXTURE["mode"])}">
      <section class="mx-section mx-hero"><div class="mx-wide mx-hero-grid">
        <div><span class="mx-eyebrow">MAXESS AI MASTERY ASSESSMENT</span><h1 class="mx-title">Your AI capability<br><em>has a shape.</em></h1><p class="mx-copy">You didn't just receive a number. You created a picture of how you currently think, direct, evaluate, iterate, and build with AI.</p><div class="mx-hero-actions"><a class="mx-cta mx-cta-primary" href="#your-fingerprint">Explore Your Results <span aria-hidden="true">↓</span></a><a class="mx-cta mx-cta-ghost" href="#naya-report">Meet Naya <span aria-hidden="true">→</span></a></div><div class="mx-proof"><div><b>5 dimensions</b><span>Your capability fingerprint</span></div><div><b>18 pathways</b><span>Where you can grow</span></div><div><b>1 next move</b><span>Turn insight into action</span></div></div></div>
        <div class="mx-score-orb mx-reveal"><div class="mx-score"><strong>{score}</strong><span>MAXESS SCORE</span><div class="mx-band">{band(score)}</div></div></div>
      </div></section>
      <div class="mx-divider"></div>
      <section class="mx-section mx-insight"><div class="mx-reading"><span class="mx-eyebrow">THE SHORT VERSION</span><div class="mx-insight-card mx-reveal"><p class="mx-quote">You already have a meaningful AI foundation. <strong>Your next leap is leverage.</strong></p><p class="mx-note">The highest-value move is not simply learning more tools. It is becoming better at directing the work, judging the result, and turning what works into a repeatable system.</p></div></div></section>
      <section class="mx-section" id="your-fingerprint"><div class="mx-wide"><div class="mx-section-head"><div><span class="mx-eyebrow">01 · YOUR FINGERPRINT</span><h2>See the pattern,<br>not just the score.</h2></div><p>Five dimensions show where your current capability is strong, where it is developing, and where a small improvement can create disproportionate upside.</p></div><div class="mx-fingerprint"><div class="mx-radar mx-reveal">{radar()}<div class="mx-radar-center"><b>{score}</b><span>overall</span></div></div><div class="mx-list">{rows}</div></div></div></section>
      <section class="mx-section"><div class="mx-wide"><div class="mx-section-head"><div><span class="mx-eyebrow">02 · WHAT IT MEANS</span><h2>Every score has<br>a job.</h2></div><p>A result becomes useful when you know what it means and what to do with it. These are your current strengths and levers.</p></div><div class="mx-dim-grid">{dim_cards()}</div></div></section>
      <section class="mx-section"><div class="mx-wide"><div class="mx-section-head"><div><span class="mx-eyebrow">03 · YOUR ADVANTAGE</span><h2>What you already<br>have working for you.</h2></div></div><div class="mx-contrast"><article class="mx-panel mx-panel-power mx-reveal"><span class="mx-eyebrow">NATURAL ADVANTAGE</span><h3>Communication</h3><p>Your strongest dimension is the ability to express context, intent, and the human outcome behind a request. That's a powerful directing skill.</p></article><article class="mx-panel mx-panel-lever mx-reveal"><span class="mx-eyebrow">HIGHEST-LEVERAGE OPPORTUNITY</span><h3>Systems Thinking</h3><p>Your largest upside is turning good individual interactions into connected, reusable systems that keep producing value after the first conversation.</p></article></div></div></section>
      <section class="mx-section"><div class="mx-wide"><div class="mx-section-head"><div><span class="mx-eyebrow">04 · YOUR NEXT CHAPTER</span><h2>From capability<br>to compounding.</h2></div><p>Mastery is not a finish line. It is the ability to make your strengths repeatable, measurable, and increasingly valuable.</p></div><div class="mx-path"><article class="mx-step mx-reveal"><strong>01 · DIRECT</strong><h3>Know the outcome</h3><p>Define what success looks like before AI begins.</p></article><article class="mx-step mx-reveal"><strong>02 · CREATE</strong><h3>Build the first version</h3><p>Give AI enough context and direction to do useful work.</p></article><article class="mx-step mx-reveal"><strong>03 · SCORE</strong><h3>Judge the work</h3><p>Use criteria instead of accepting the first answer.</p></article><article class="mx-step mx-reveal"><strong>04 · COMPOUND</strong><h3>Make it reusable</h3><p>Turn successful work into a system you can repeat.</p></article></div></div></section>
      <section class="mx-section"><div class="mx-wide"><div class="mx-section-head"><div><span class="mx-eyebrow">05 · YOUR 18 AI PATHWAYS</span><h2>Don't learn AI.<br>Learn what AI can do for you.</h2></div><p>These are 18 capability doors. Explore the ones that matter most to your goals, then build depth instead of collecting tools.</p></div><div class="mx-areas">{area_cards()}</div></div></section>
      <section class="mx-section mx-naya-bridge" id="naya-report"><div class="mx-reading"><div class="mx-bridge-card mx-reveal"><span class="mx-audio-label">PERSONALIZED REPORT</span><h2>You've seen the pattern.<br><em>Now hear what it means.</em></h2><p>Naya is the next layer: turning your result into a practical conversation about where you are, where you can go, and what to do next.</p><button class="mx-cta mx-cta-primary" type="button" id="mx-naya-listen">Naya — Listen to Your Report <span aria-hidden="true">▶</span></button><div class="mx-key" aria-label="AI Master Key"><div>KNOW</div><div>TELL</div><div>ASK</div><div>CREATE</div><div>SCORE</div><div>IMPROVE</div><div>REPEAT</div></div></div></div></section>
      <section class="mx-section mx-final"><p class="mx-final-note">The Results chapter is complete. The next chapter is NayaNET.</p><div id="nayanet-foundation-anchor"></div></section>
    </main>'''

def js():
    return r'''<script id="maxess-results-10-behavior">(()=>{const root=document.getElementById('maxess-results-10');if(!root)return;const reveal=()=>{const io=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('is-visible');io.unobserve(e.target)}}),{threshold:.12});root.querySelectorAll('.mx-reveal').forEach((el,i)=>{el.style.transitionDelay=Math.min(i*35,280)+'ms';io.observe(el)})};reveal();root.querySelectorAll('.mx-mini').forEach(b=>b.addEventListener('click',()=>{const name=b.dataset.area||'this pathway';window.dispatchEvent(new CustomEvent('maxess:pathway',{detail:{name}}));b.blur()}));const n=document.getElementById('mx-naya-listen');if(n)n.addEventListener('click',()=>{const target=document.querySelector('#nayanet-foundation-anchor');if(target)target.scrollIntoView({behavior:'smooth',block:'start'});window.dispatchEvent(new CustomEvent('maxess:naya-report'))});})();</script>'''

def build():
    naya=NAYA.read_text(encoding='utf-8')
    # The Page Code is intentionally appended verbatim. The Results layer owns
    # everything above this point; NayaNET owns its final chapter controls.
    page='''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover"><meta name="theme-color" content="#040307"><meta name="color-scheme" content="dark"><title>MAXESS — Your AI Mastery Results</title>'''+css()+'''</head><body>'''+html_body()+naya+js()+'''</body></html>'''
    OUT_FULL.write_text(page,encoding='utf-8')
    # Groove embed: remove document wrapper but preserve every presentation and script layer.
    embed=re.sub(r'<!doctype html>','',page,flags=re.I)
    embed=re.sub(r'</?html[^>]*>','',embed,flags=re.I)
    embed=re.sub(r'<head>.*?</head>','',embed,flags=re.I|re.S)
    embed=re.sub(r'</?body[^>]*>','',embed,flags=re.I)
    OUT_EMBED.write_text(embed,encoding='utf-8')
    for p in ALIASES:
        p.write_text(page if p.name.endswith('.html') and 'EMBED' not in p.name and 'GROOVE-EMBED' not in p.name else embed,encoding='utf-8')
    print(f'Built {OUT_FULL.name}: {len(page.splitlines())} lines / {len(page.encode())} bytes')
    print(f'Built {OUT_EMBED.name}: {len(embed.splitlines())} lines / {len(embed.encode())} bytes')
    print('Contract:',FIXTURE['contract'],'Mode:',FIXTURE['mode'],'Band:',band(FIXTURE['score']))
if __name__=='__main__': build()
