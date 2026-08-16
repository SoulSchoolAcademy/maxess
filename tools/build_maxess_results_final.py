#!/usr/bin/env python3
"""
MAXESS FINAL RESULTS BUILDER
============================

This is the new final Results build path.

It does NOT select an old 9.x/9.95/10 Results artifact as the final source.
It constructs a new Results experience from:
  1. the locked MAXESS product/result architecture,
  2. a deterministic development Result Contract fixture,
  3. the NayaNET Page Code as the immutable foundation for the final chapter.

The real assessment Result Contract can replace the fixture later without
changing the presentation architecture.

Outputs:
  - MAXESS-RESULTS-FINAL-GROOVE.html
  - MAXESS-RESULTS-FINAL-GROOVE-EMBED.html
  - MAXESS-RESULTS-10-GROOVE.html (deployment alias)
  - MAXESS-RESULTS-GROOVE-EMBED.html (deployment alias)
  - MAXESS-RESULTS-GROOVE-EMBED-9.95.html (deployment alias)
"""

from __future__ import annotations

from pathlib import Path
import html
import re

ROOT = Path(__file__).resolve().parents[1]
NAYANET_PATH = ROOT / "nayanetpagecode"
FULL_OUT = ROOT / "MAXESS-RESULTS-FINAL-GROOVE.html"
EMBED_OUT = ROOT / "MAXESS-RESULTS-FINAL-GROOVE-EMBED.html"
# Deployment aliases: these are the canonical artifacts consumed by the
# existing Groove handoff. They are generated from the same final source.
DEPLOY_FULL_OUT = ROOT / "MAXESS-RESULTS-10-GROOVE.html"
DEPLOY_EMBED_OUT = ROOT / "MAXESS-RESULTS-GROOVE-EMBED.html"
DEPLOY_EMBED_995_OUT = ROOT / "MAXESS-RESULTS-GROOVE-EMBED-9.95.html"

# ---------------------------------------------------------------------------
# DEVELOPMENT RESULT CONTRACT
# ---------------------------------------------------------------------------
# This is deliberately a fixture, not a production result. It exists so the
# experience can be designed, reviewed, and scored before the assessment
# handoff is connected.
FIXTURE = {
    "contract": "MAXESS-RESULTS-CONTRACT-1",
    "mode": "development-fixture",
    "score": 82,
    "band": "Advancing",
    "name": "Your MAXESS Result",
    "dimensions": [
        {"key": "direction", "name": "Direction", "score": 86,
         "meaning": "You usually know what you want AI to help you accomplish.",
         "action": "Define the outcome and success test before asking AI to work."},
        {"key": "communication", "name": "Communication", "score": 91,
         "meaning": "You are strong at expressing context, intent, and the human outcome behind a request.",
         "action": "Turn that strength into reusable instructions, briefs, and decision frameworks."},
        {"key": "evaluation", "name": "Evaluation", "score": 79,
         "meaning": "You can recognize useful work, but your biggest gains come from judging it more deliberately.",
         "action": "Use a visible scorecard before accepting an answer or artifact."},
        {"key": "iteration", "name": "Iteration", "score": 74,
         "meaning": "You understand that quality improves through refinement rather than one-shot prompting.",
         "action": "Make improvement loops explicit: create, score, improve, repeat."},
        {"key": "systems", "name": "Systems Thinking", "score": 68,
         "meaning": "You can see the bigger system, with a major opportunity to make your workflows more connected.",
         "action": "Turn repeated work into reusable systems, components, and operating rules."},
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

BANDS = (
    (0, 50, "Foundation", "You are building the foundation for powerful AI work."),
    (51, 75, "Developing", "You are developing reliable AI capability and can compound it quickly."),
    (76, 90, "Advancing", "You already have meaningful AI capability. Your next gains come from leverage."),
    (91, 100, "Mastering", "You are operating at a high level and can focus on orchestration and mastery."),
)


def band_for(score: int) -> str:
    for low, high, label, _ in BANDS:
        if low <= score <= high:
            return label
    raise ValueError(f"Score outside 0-100: {score}")


def esc(value: object) -> str:
    return html.escape(str(value), quote=True)


def dimension_rows() -> str:
    rows = []
    for i, d in enumerate(FIXTURE["dimensions"], 1):
        rows.append(f"""
        <article class="mx-dimension mx-reveal" data-dimension="{esc(d['key'])}">
          <div class="mx-dimension-top">
            <span class="mx-index">0{i}</span>
            <span class="mx-dimension-name">{esc(d['name'])}</span>
            <span class="mx-dimension-score">{d['score']}<small>/100</small></span>
          </div>
          <div class="mx-meter" role="img" aria-label="{esc(d['name'])}: {d['score']} out of 100">
            <span class="mx-meter-fill" style="--value:{d['score']}%"></span>
          </div>
          <p class="mx-dimension-meaning">{esc(d['meaning'])}</p>
          <div class="mx-dimension-action">
            <span>LEVER</span>
            <strong>{esc(d['action'])}</strong>
          </div>
        </article>
        """)
    return "\n".join(rows)


def area_cards() -> str:
    cards = []
    for i, (name, desc) in enumerate(FIXTURE["areas"], 1):
        score = FIXTURE["dimensions"][i % len(FIXTURE["dimensions"])] ["score"]
        cards.append(f"""
        <article class="mx-area mx-reveal" data-area-index="{i}">
          <div class="mx-area-number">{i:02d}</div>
          <div class="mx-area-copy">
            <h3>{esc(name)}</h3>
            <p>{esc(desc)}</p>
          </div>
          <div class="mx-area-signal" aria-label="Pathway relevance {score} percent">
            <span style="--value:{score}%"></span>
          </div>
          <button class="mx-area-action" type="button" data-area="{esc(name)}">
            <span>Explore</span><span aria-hidden="true">↗</span>
          </button>
        </article>
        """)
    return "\n".join(cards)


def build_css() -> str:
    return r"""
/* ========================================================================
   MAXESS FINAL RESULTS — DESIGN SYSTEM
   ========================================================================
   Full-page cinematic editorial experience.
   The NayaNET foundation is appended after this system and remains intact.
   ======================================================================== */

:root {
  --mx-bg: #030305;
  --mx-bg-2: #08050d;
  --mx-surface: rgba(18, 11, 27, .72);
  --mx-surface-strong: rgba(11, 8, 15, .92);
  --mx-white: #fff;
  --mx-soft: rgba(255,255,255,.72);
  --mx-muted: rgba(255,255,255,.48);
  --mx-purple: #a855f7;
  --mx-purple-2: #7c3aed;
  --mx-violet: #c084fc;
  --mx-gold: #f5d28a;
  --mx-line: rgba(255,255,255,.10);
  --mx-line-bright: rgba(255,255,255,.18);
  --mx-shadow: 0 30px 90px rgba(0,0,0,.48);
  --mx-radius: 28px;
  --mx-max: 1480px;
  --mx-reading: 940px;
}

.mx-results,
.mx-results * {
  box-sizing: border-box;
}

.mx-results {
  position: relative;
  width: 100%;
  min-height: 100vh;
  overflow: clip;
  color: var(--mx-white);
  background:
    radial-gradient(ellipse 90% 35% at 50% 0%, rgba(168,85,247,.26), transparent 68%),
    radial-gradient(ellipse 45% 28% at 0% 22%, rgba(124,58,237,.12), transparent 72%),
    radial-gradient(ellipse 45% 28% at 100% 32%, rgba(56,189,248,.08), transparent 72%),
    linear-gradient(180deg,#10051a 0%,#07040b 26%,#030305 65%,#020203 100%);
  isolation: isolate;
}

.mx-results::before {
  content: "";
  position: absolute;
  inset: 0;
  pointer-events: none;
  z-index: -1;
  background:
    linear-gradient(90deg, transparent, rgba(255,255,255,.018), transparent),
    radial-gradient(circle at 50% 18%, rgba(255,255,255,.035), transparent 30%);
}

.mx-results::after {
  content: "";
  position: absolute;
  inset: 0;
  pointer-events: none;
  z-index: -1;
  opacity: .22;
  background-image: radial-gradient(rgba(255,255,255,.16) .6px, transparent .7px);
  background-size: 4px 4px;
  mask-image: linear-gradient(to bottom, #000, transparent 70%);
}

.mx-results a,
.mx-results button {
  font: inherit;
}

.mx-results button {
  border: 0;
}

.mx-section {
  position: relative;
  width: 100%;
  padding: clamp(84px, 10vw, 170px) clamp(20px, 4vw, 72px);
}

.mx-section-inner {
  width: min(var(--mx-max), 100%);
  margin-inline: auto;
}

.mx-reading {
  width: min(var(--mx-reading), 100%);
  margin-inline: auto;
}

.mx-kicker {
  display: inline-flex;
  align-items: center;
  gap: 10px;
  margin-bottom: 20px;
  color: var(--mx-violet);
  font-size: 11px;
  font-weight: 800;
  letter-spacing: .22em;
  text-transform: uppercase;
}

.mx-kicker::before {
  content: "";
  width: 30px;
  height: 1px;
  background: linear-gradient(90deg, transparent, var(--mx-violet));
}

.mx-section-title {
  margin: 0;
  max-width: 1050px;
  font-size: clamp(38px, 6vw, 88px);
  line-height: .94;
  letter-spacing: -.055em;
  font-weight: 760;
}

.mx-section-lead {
  max-width: 820px;
  margin: 24px 0 0;
  color: var(--mx-soft);
  font-size: clamp(17px, 1.5vw, 22px);
  line-height: 1.55;
}

.mx-rule {
  width: 100%;
  height: 1px;
  margin: 42px 0;
  background: linear-gradient(90deg, transparent, var(--mx-line-bright), transparent);
}

.mx-reveal {
  opacity: 0;
  transform: translateY(24px);
  transition: opacity 700ms ease, transform 700ms cubic-bezier(.2,.8,.2,1);
}

.mx-reveal.is-visible {
  opacity: 1;
  transform: none;
}

.mx-glow {
  position: absolute;
  width: 520px;
  height: 520px;
  border-radius: 50%;
  pointer-events: none;
  filter: blur(90px);
  opacity: .15;
  background: var(--mx-purple);
}

.mx-hero {
  min-height: min(920px, 100vh);
  display: grid;
  align-items: center;
  padding-top: clamp(110px, 13vw, 190px);
  padding-bottom: clamp(80px, 9vw, 130px);
}

.mx-hero .mx-glow {
  top: 8%;
  left: 50%;
  transform: translateX(-50%);
}

.mx-hero-grid {
  display: grid;
  grid-template-columns: minmax(0, 1.05fr) minmax(360px, .95fr);
  gap: clamp(40px, 7vw, 120px);
  align-items: center;
}

.mx-hero-eyebrow {
  color: rgba(255,255,255,.62);
  font-size: 12px;
  font-weight: 800;
  letter-spacing: .28em;
  text-transform: uppercase;
}

.mx-hero-title {
  margin: 18px 0 0;
  max-width: 900px;
  font-size: clamp(58px, 9vw, 150px);
  line-height: .83;
  letter-spacing: -.075em;
  font-weight: 780;
}

.mx-hero-title em {
  display: block;
  color: transparent;
  background: linear-gradient(120deg,#fff 0%,#ead8ff 24%,#a855f7 58%,#f1cfff 100%);
  background-clip: text;
  -webkit-background-clip: text;
  font-style: normal;
}

.mx-hero-copy {
  max-width: 760px;
  margin-top: 32px;
  color: var(--mx-soft);
  font-size: clamp(18px, 1.7vw, 25px);
  line-height: 1.5;
}

.mx-hero-note {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-top: 30px;
  color: rgba(255,255,255,.42);
  font-size: 12px;
}

.mx-hero-note span {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: var(--mx-purple);
  box-shadow: 0 0 20px var(--mx-purple);
}

.mx-score-orb {
  position: relative;
  width: min(460px, 82vw);
  aspect-ratio: 1;
  margin-inline: auto;
  display: grid;
  place-items: center;
  border-radius: 50%;
  background:
    radial-gradient(circle at 32% 24%, rgba(255,255,255,.16), transparent 15%),
    radial-gradient(circle, rgba(168,85,247,.18) 0 35%, transparent 67%),
    conic-gradient(from -35deg, #f6ddff 0deg, #8b3be9 80deg, #2e0b55 190deg, #c084fc 280deg, #f6ddff 360deg);
  box-shadow:
    0 0 0 1px rgba(255,255,255,.22),
    0 0 70px rgba(168,85,247,.25),
    0 40px 100px rgba(0,0,0,.58);
}

.mx-score-orb::before {
  content: "";
  position: absolute;
  inset: 10px;
  border-radius: inherit;
  background:
    radial-gradient(circle at 35% 25%, rgba(255,255,255,.09), transparent 18%),
    radial-gradient(circle, #120b18 0%, #050407 72%);
  box-shadow: inset 0 0 50px rgba(0,0,0,.92);
}

.mx-score-orb::after {
  content: "";
  position: absolute;
  inset: -24px;
  border-radius: inherit;
  border: 1px solid rgba(192,132,252,.14);
  box-shadow: 0 0 60px rgba(168,85,247,.10);
}

.mx-score-content {
  position: relative;
  z-index: 2;
  text-align: center;
}

.mx-score-number {
  font-size: clamp(92px, 12vw, 170px);
  line-height: .82;
  font-weight: 780;
  letter-spacing: -.08em;
}

.mx-score-number small {
  display: block;
  margin-top: 16px;
  color: rgba(255,255,255,.46);
  font-size: 11px;
  font-weight: 800;
  letter-spacing: .3em;
}

.mx-band-pill {
  display: inline-flex;
  margin-top: 24px;
  padding: 10px 16px;
  border: 1px solid rgba(192,132,252,.35);
  border-radius: 999px;
  background: rgba(168,85,247,.10);
  color: #ead8ff;
  font-size: 11px;
  font-weight: 800;
  letter-spacing: .18em;
  text-transform: uppercase;
}

.mx-profile {
  padding-top: 40px;
}

.mx-profile-card {
  position: relative;
  padding: clamp(30px, 5vw, 72px);
  border: 1px solid var(--mx-line);
  border-radius: var(--mx-radius);
  background:
    linear-gradient(145deg, rgba(255,255,255,.055), rgba(255,255,255,.012)),
    rgba(7,5,10,.78);
  box-shadow: var(--mx-shadow);
  overflow: hidden;
}

.mx-profile-card::before {
  content: "";
  position: absolute;
  width: 320px;
  height: 320px;
  top: -180px;
  right: -100px;
  border-radius: 50%;
  background: rgba(168,85,247,.18);
  filter: blur(70px);
}

.mx-profile-quote {
  position: relative;
  max-width: 1100px;
  margin: 0;
  font-size: clamp(30px, 4.4vw, 68px);
  line-height: 1.02;
  letter-spacing: -.045em;
  font-weight: 700;
}

.mx-profile-support {
  position: relative;
  max-width: 850px;
  margin: 28px 0 0;
  color: var(--mx-soft);
  font-size: clamp(17px, 1.5vw, 22px);
  line-height: 1.55;
}

.mx-fingerprint {
  padding-top: clamp(70px, 8vw, 130px);
}

.mx-fingerprint-layout {
  display: grid;
  grid-template-columns: minmax(300px, .8fr) minmax(0, 1.2fr);
  gap: clamp(36px, 6vw, 100px);
  align-items: start;
}

.mx-radar {
  position: relative;
  width: min(620px, 90vw);
  aspect-ratio: 1;
  margin-inline: auto;
}

.mx-radar-ring,
.mx-radar-spoke,
.mx-radar-polygon {
  position: absolute;
  inset: 8%;
  border-radius: 50%;
}

.mx-radar-ring {
  border: 1px solid rgba(255,255,255,.12);
  transform: scale(var(--scale));
}

.mx-radar-ring:nth-child(1) { --scale: 1; }
.mx-radar-ring:nth-child(2) { --scale: .78; }
.mx-radar-ring:nth-child(3) { --scale: .56; }
.mx-radar-ring:nth-child(4) { --scale: .34; }

.mx-radar-spokes {
  position: absolute;
  inset: 8%;
}

.mx-radar-spoke {
  inset: 50% auto auto 50%;
  width: 50%;
  height: 1px;
  transform-origin: left center;
  background: rgba(255,255,255,.10);
}

.mx-radar-spoke:nth-child(1) { transform: rotate(-90deg); }
.mx-radar-spoke:nth-child(2) { transform: rotate(-18deg); }
.mx-radar-spoke:nth-child(3) { transform: rotate(54deg); }
.mx-radar-spoke:nth-child(4) { transform: rotate(126deg); }
.mx-radar-spoke:nth-child(5) { transform: rotate(198deg); }

.mx-radar-polygon {
  inset: 18%;
  border-radius: 0;
  clip-path: polygon(50% 0%, 97% 35%, 79% 91%, 21% 91%, 3% 35%);
  background: rgba(168,85,247,.22);
  border: 1px solid rgba(216,180,254,.72);
  box-shadow: 0 0 60px rgba(168,85,247,.12);
}

.mx-radar-label {
  position: absolute;
  width: 130px;
  text-align: center;
  color: rgba(255,255,255,.62);
  font-size: 10px;
  font-weight: 800;
  letter-spacing: .12em;
  text-transform: uppercase;
}

.mx-radar-label strong {
  display: block;
  margin-top: 6px;
  color: #fff;
  font-size: 14px;
  letter-spacing: 0;
}

.mx-radar-label:nth-of-type(1) { top: -2%; left: 50%; transform: translateX(-50%); }
.mx-radar-label:nth-of-type(2) { top: 26%; right: -5%; }
.mx-radar-label:nth-of-type(3) { bottom: 2%; right: 5%; }
.mx-radar-label:nth-of-type(4) { bottom: 2%; left: 5%; }
.mx-radar-label:nth-of-type(5) { top: 26%; left: -5%; }

.mx-dimension-list {
  display: grid;
  gap: 14px;
}

.mx-dimension {
  padding: 24px 26px;
  border: 1px solid var(--mx-line);
  border-radius: 20px;
  background: rgba(255,255,255,.025);
  transition: border-color 220ms ease, background 220ms ease, transform 220ms ease;
}

.mx-dimension:hover {
  transform: translateY(-2px);
  border-color: rgba(192,132,252,.34);
  background: rgba(168,85,247,.045);
}

.mx-dimension-top {
  display: grid;
  grid-template-columns: 42px 1fr auto;
  align-items: center;
  gap: 14px;
}

.mx-index {
  color: rgba(255,255,255,.28);
  font-size: 11px;
  font-weight: 800;
  letter-spacing: .12em;
}

.mx-dimension-name {
  font-size: 18px;
  font-weight: 700;
}

.mx-dimension-score {
  font-size: 28px;
  font-weight: 760;
  letter-spacing: -.04em;
}

.mx-dimension-score small {
  color: rgba(255,255,255,.35);
  font-size: 10px;
  font-weight: 700;
}

.mx-meter {
  height: 5px;
  margin: 18px 0;
  border-radius: 99px;
  background: rgba(255,255,255,.08);
  overflow: hidden;
}

.mx-meter-fill {
  display: block;
  width: var(--value);
  height: 100%;
  border-radius: inherit;
  background: linear-gradient(90deg, #5b21b6, #a855f7, #e9d5ff);
  box-shadow: 0 0 18px rgba(168,85,247,.32);
}

.mx-dimension-meaning {
  margin: 0;
  color: var(--mx-soft);
  line-height: 1.55;
}

.mx-dimension-action {
  display: grid;
  grid-template-columns: 62px 1fr;
  gap: 12px;
  margin-top: 18px;
  padding-top: 15px;
  border-top: 1px solid var(--mx-line);
}

.mx-dimension-action span {
  color: var(--mx-violet);
  font-size: 9px;
  font-weight: 900;
  letter-spacing: .16em;
}

.mx-dimension-action strong {
  font-size: 12px;
  line-height: 1.45;
}

.mx-meaning-grid {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 18px;
  margin-top: 46px;
}

.mx-meaning-card {
  min-height: 250px;
  padding: 28px;
  border: 1px solid var(--mx-line);
  border-radius: 22px;
  background: linear-gradient(145deg, rgba(255,255,255,.045), rgba(255,255,255,.012));
}

.mx-meaning-card span {
  color: var(--mx-violet);
  font-size: 10px;
  font-weight: 900;
  letter-spacing: .18em;
  text-transform: uppercase;
}

.mx-meaning-card h3 {
  margin: 52px 0 14px;
  font-size: 23px;
  line-height: 1.05;
  letter-spacing: -.03em;
}

.mx-meaning-card p {
  margin: 0;
  color: var(--mx-soft);
  line-height: 1.5;
}

.mx-leverage {
  padding-top: clamp(90px, 11vw, 180px);
}

.mx-leverage-grid {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 18px;
  margin-top: 54px;
}

.mx-leverage-card {
  position: relative;
  min-height: 430px;
  padding: clamp(30px, 4vw, 54px);
  border-radius: 28px;
  overflow: hidden;
  border: 1px solid var(--mx-line);
  background: #07050a;
}

.mx-leverage-card::after {
  content: "";
  position: absolute;
  width: 280px;
  height: 280px;
  right: -80px;
  bottom: -100px;
  border-radius: 50%;
  background: rgba(168,85,247,.15);
  filter: blur(60px);
}

.mx-leverage-card.advantage {
  border-color: rgba(245,210,138,.24);
  background: linear-gradient(145deg, rgba(245,210,138,.055), rgba(255,255,255,.01));
}

.mx-leverage-label {
  color: var(--mx-violet);
  font-size: 10px;
  font-weight: 900;
  letter-spacing: .2em;
  text-transform: uppercase;
}

.mx-leverage-card.advantage .mx-leverage-label {
  color: var(--mx-gold);
}

.mx-leverage-card h3 {
  margin: 44px 0 0;
  font-size: clamp(34px, 4vw, 62px);
  line-height: .92;
  letter-spacing: -.055em;
}

.mx-leverage-score {
  position: absolute;
  right: 32px;
  top: 28px;
  color: rgba(255,255,255,.22);
  font-size: 28px;
  font-weight: 760;
}

.mx-leverage-card p {
  position: relative;
  z-index: 1;
  max-width: 590px;
  margin: 24px 0 0;
  color: var(--mx-soft);
  font-size: 17px;
  line-height: 1.55;
}

.mx-revelation {
  padding-top: clamp(100px, 12vw, 200px);
}

.mx-revelation-card {
  position: relative;
  padding: clamp(40px, 7vw, 100px);
  border-radius: 36px;
  overflow: hidden;
  border: 1px solid rgba(192,132,252,.22);
  background:
    radial-gradient(circle at 50% 0%, rgba(168,85,247,.16), transparent 52%),
    linear-gradient(145deg, rgba(255,255,255,.045), rgba(255,255,255,.01));
  box-shadow: 0 50px 120px rgba(0,0,0,.42);
}

.mx-revelation-word {
  color: #fff;
  font-size: clamp(13px, 1.1vw, 16px);
  font-weight: 900;
  letter-spacing: .26em;
  text-transform: uppercase;
}

.mx-revelation-card h2 {
  max-width: 1100px;
  margin: 30px 0 0;
  font-size: clamp(48px, 7vw, 108px);
  line-height: .88;
  letter-spacing: -.07em;
}

.mx-revelation-card p {
  max-width: 820px;
  margin: 32px 0 0;
  color: var(--mx-soft);
  font-size: clamp(18px, 1.6vw, 24px);
  line-height: 1.55;
}

.mx-next {
  padding-top: clamp(80px, 9vw, 140px);
}

.mx-next-card {
  display: grid;
  grid-template-columns: minmax(0, 1fr) auto;
  gap: 40px;
  align-items: center;
  padding: clamp(30px, 5vw, 70px);
  border: 1px solid rgba(255,255,255,.14);
  border-radius: 28px;
  background: linear-gradient(110deg, rgba(168,85,247,.10), rgba(255,255,255,.025));
}

.mx-next-number {
  color: var(--mx-violet);
  font-size: 12px;
  font-weight: 900;
  letter-spacing: .2em;
}

.mx-next-card h2 {
  margin: 16px 0 0;
  font-size: clamp(38px, 5vw, 76px);
  line-height: .95;
  letter-spacing: -.055em;
}

.mx-next-card p {
  max-width: 760px;
  margin: 22px 0 0;
  color: var(--mx-soft);
  line-height: 1.55;
}

.mx-next-button,
.mx-audio-button {
  position: relative;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-height: 58px;
  padding: 0 25px;
  border-radius: 17px;
  color: #fff;
  text-decoration: none;
  cursor: pointer;
  background: linear-gradient(145deg, #24202a, #070609);
  border: 2px solid #9b54e9;
  box-shadow:
    0 0 0 1px rgba(255,255,255,.16),
    0 12px 28px rgba(0,0,0,.48),
    0 0 30px rgba(168,85,247,.14),
    inset 0 1px 1px rgba(255,255,255,.22);
  font-size: 13px;
  font-weight: 800;
  letter-spacing: .02em;
  transition: transform 220ms ease, filter 220ms ease;
}

.mx-next-button:hover,
.mx-audio-button:hover {
  transform: translateY(-3px);
  filter: brightness(1.08);
}

.mx-next-button:active,
.mx-audio-button:active {
  transform: translateY(1px);
}

.mx-next-button:focus-visible,
.mx-audio-button:focus-visible,
.mx-area-action:focus-visible,
.mx-copy-button:focus-visible {
  outline: 3px solid rgba(222,190,255,.96);
  outline-offset: 5px;
}

.mx-path {
  padding-top: clamp(90px, 11vw, 170px);
}

.mx-path-header {
  display: flex;
  justify-content: space-between;
  gap: 30px;
  align-items: end;
}

.mx-path-count {
  flex: 0 0 auto;
  color: rgba(255,255,255,.34);
  font-size: 13px;
  font-weight: 800;
  letter-spacing: .1em;
}

.mx-area-grid {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 12px;
  margin-top: 48px;
}

.mx-area {
  position: relative;
  min-height: 250px;
  padding: 24px;
  display: flex;
  flex-direction: column;
  border: 1px solid var(--mx-line);
  border-radius: 20px;
  background: rgba(255,255,255,.022);
  overflow: hidden;
  transition: transform 220ms ease, border-color 220ms ease, background 220ms ease;
}

.mx-area:hover {
  transform: translateY(-4px);
  border-color: rgba(168,85,247,.32);
  background: rgba(168,85,247,.045);
}

.mx-area-number {
  color: rgba(255,255,255,.22);
  font-size: 11px;
  font-weight: 900;
  letter-spacing: .14em;
}

.mx-area-copy {
  margin-top: auto;
}

.mx-area-copy h3 {
  margin: 36px 0 10px;
  font-size: 20px;
  line-height: 1.05;
  letter-spacing: -.025em;
}

.mx-area-copy p {
  margin: 0;
  color: var(--mx-muted);
  font-size: 13px;
  line-height: 1.45;
}

.mx-area-signal {
  height: 3px;
  margin-top: 20px;
  border-radius: 99px;
  background: rgba(255,255,255,.07);
  overflow: hidden;
}

.mx-area-signal span {
  display: block;
  width: var(--value);
  height: 100%;
  background: linear-gradient(90deg, #6d28d9, #c084fc);
}

.mx-area-action {
  align-self: flex-start;
  margin-top: 15px;
  padding: 0;
  color: rgba(255,255,255,.70);
  background: transparent;
  cursor: pointer;
  font-size: 11px;
  font-weight: 800;
  letter-spacing: .08em;
  text-transform: uppercase;
}

.mx-area-action span + span {
  margin-left: 6px;
  color: var(--mx-violet);
}

.mx-naya {
  padding-top: clamp(110px, 13vw, 210px);
}

.mx-naya-card {
  position: relative;
  display: grid;
  grid-template-columns: 180px minmax(0,1fr);
  gap: 40px;
  align-items: center;
  padding: clamp(30px, 5vw, 72px);
  border: 1px solid rgba(192,132,252,.24);
  border-radius: 34px;
  background:
    radial-gradient(circle at 20% 50%, rgba(168,85,247,.16), transparent 35%),
    linear-gradient(145deg, rgba(255,255,255,.05), rgba(255,255,255,.012));
  box-shadow: var(--mx-shadow);
}

.mx-naya-avatar {
  position: relative;
  width: 160px;
  aspect-ratio: 1;
  border-radius: 50%;
  display: grid;
  place-items: center;
  background:
    radial-gradient(circle at 32% 20%, #fff 0%, #e8c6ff 10%, #a855f7 35%, #4c1d95 64%, #10051b 100%);
  box-shadow:
    inset 0 3px 8px rgba(255,255,255,.75),
    inset 0 -20px 30px rgba(24,4,44,.74),
    0 0 50px rgba(168,85,247,.26),
    0 20px 50px rgba(0,0,0,.55);
}

.mx-naya-avatar::after {
  content: "N";
  font-size: 68px;
  font-weight: 800;
  letter-spacing: -.08em;
  text-shadow: 0 4px 20px rgba(0,0,0,.55);
}

.mx-naya-label {
  color: var(--mx-violet);
  font-size: 10px;
  font-weight: 900;
  letter-spacing: .2em;
  text-transform: uppercase;
}

.mx-naya-card h2 {
  margin: 13px 0 0;
  font-size: clamp(36px, 5vw, 76px);
  line-height: .93;
  letter-spacing: -.06em;
}

.mx-naya-card p {
  max-width: 820px;
  margin: 22px 0 0;
  color: var(--mx-soft);
  font-size: 18px;
  line-height: 1.55;
}

.mx-naya-actions {
  display: flex;
  flex-wrap: wrap;
  gap: 12px;
  margin-top: 28px;
}

.mx-audio-status {
  margin-top: 15px;
  color: rgba(255,255,255,.40);
  font-size: 11px;
}

.mx-master-key {
  padding-top: clamp(100px, 12vw, 190px);
}

.mx-key {
  display: grid;
  grid-template-columns: repeat(7, minmax(0,1fr));
  gap: 8px;
  margin-top: 54px;
}

.mx-key-step {
  position: relative;
  min-height: 150px;
  padding: 22px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  border: 1px solid var(--mx-line);
  border-radius: 18px;
  background: rgba(255,255,255,.024);
}

.mx-key-step strong {
  font-size: 15px;
  letter-spacing: -.01em;
}

.mx-key-step span {
  color: rgba(255,255,255,.28);
  font-size: 9px;
  font-weight: 900;
  letter-spacing: .14em;
}

.mx-key-arrow {
  position: absolute;
  right: -7px;
  top: 50%;
  color: var(--mx-violet);
  font-size: 12px;
  transform: translateY(-50%);
  z-index: 2;
}

.mx-final-threshold {
  padding-top: clamp(120px, 15vw, 240px);
  padding-bottom: clamp(90px, 10vw, 150px);
}

.mx-threshold {
  position: relative;
  padding: clamp(50px, 9vw, 130px) 20px;
  text-align: center;
}

.mx-threshold::before {
  content: "";
  position: absolute;
  inset: 10% 20%;
  border-radius: 50%;
  background: rgba(168,85,247,.10);
  filter: blur(90px);
  z-index: -1;
}

.mx-threshold h2 {
  max-width: 1100px;
  margin: 0 auto;
  font-size: clamp(48px, 7vw, 108px);
  line-height: .88;
  letter-spacing: -.07em;
}

.mx-threshold p {
  max-width: 700px;
  margin: 30px auto 0;
  color: var(--mx-soft);
  font-size: 18px;
  line-height: 1.55;
}

.mx-foundation-label {
  width: min(var(--mx-max), calc(100% - 40px));
  margin: 0 auto;
  padding: 28px 0 18px;
  color: rgba(255,255,255,.30);
  border-top: 1px solid rgba(255,255,255,.08);
  font-size: 9px;
  font-weight: 900;
  letter-spacing: .25em;
  text-transform: uppercase;
}

.mx-utility-bar {
  position: fixed;
  z-index: 50;
  top: 18px;
  left: 50%;
  transform: translateX(-50%);
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 8px 10px 8px 14px;
  border: 1px solid rgba(255,255,255,.12);
  border-radius: 999px;
  background: rgba(7,5,10,.72);
  backdrop-filter: blur(18px);
  box-shadow: 0 14px 40px rgba(0,0,0,.34);
}

.mx-utility-brand {
  color: rgba(255,255,255,.78);
  font-size: 10px;
  font-weight: 900;
  letter-spacing: .18em;
}

.mx-copy-button {
  min-height: 32px;
  padding: 0 12px;
  border-radius: 999px;
  color: #fff;
  background: rgba(255,255,255,.07);
  border: 1px solid rgba(255,255,255,.12);
  cursor: pointer;
  font-size: 10px;
  font-weight: 800;
}

.mx-fixture-badge {
  position: fixed;
  z-index: 49;
  right: 14px;
  bottom: 14px;
  padding: 8px 10px;
  border: 1px solid rgba(245,210,138,.24);
  border-radius: 999px;
  color: rgba(245,210,138,.75);
  background: rgba(30,20,6,.70);
  backdrop-filter: blur(14px);
  font-size: 9px;
  font-weight: 900;
  letter-spacing: .14em;
  text-transform: uppercase;
}

@media (max-width: 1100px) {
  .mx-hero-grid,
  .mx-fingerprint-layout {
    grid-template-columns: 1fr;
  }

  .mx-hero {
    min-height: auto;
  }

  .mx-score-orb {
    width: min(420px, 72vw);
  }

  .mx-area-grid {
    grid-template-columns: repeat(2, minmax(0,1fr));
  }

  .mx-key {
    grid-template-columns: repeat(4, minmax(0,1fr));
  }
}

@media (max-width: 760px) {
  .mx-section {
    padding: 76px 18px;
  }

  .mx-hero {
    padding-top: 100px;
  }

  .mx-hero-title {
    font-size: clamp(58px, 17vw, 100px);
  }

  .mx-score-orb {
    width: min(330px, 78vw);
  }

  .mx-score-number {
    font-size: clamp(82px, 23vw, 122px);
  }

  .mx-meaning-grid,
  .mx-leverage-grid,
  .mx-area-grid {
    grid-template-columns: 1fr;
  }

  .mx-path-header {
    align-items: start;
    flex-direction: column;
  }

  .mx-next-card,
  .mx-naya-card {
    grid-template-columns: 1fr;
  }

  .mx-naya-avatar {
    width: 120px;
  }

  .mx-key {
    grid-template-columns: repeat(2, minmax(0,1fr));
  }

  .mx-key-step {
    min-height: 120px;
  }

  .mx-key-arrow {
    display: none;
  }

  .mx-utility-bar {
    max-width: calc(100% - 28px);
  }

  .mx-utility-brand {
    display: none;
  }

  .mx-fixture-badge {
    right: 10px;
    bottom: 10px;
  }
}

@media (prefers-reduced-motion: reduce) {
  .mx-reveal {
    opacity: 1;
    transform: none;
    transition: none;
  }

  .mx-next-button,
  .mx-audio-button,
  .mx-area,
  .mx-dimension {
    transition: none;
  }
}

@media print {
  .mx-utility-bar,
  .mx-fixture-badge,
  .mx-naya-actions {
    display: none !important;
  }

  .mx-results {
    background: #fff !important;
    color: #111 !important;
  }
}
"""


def build_html() -> str:
    d = FIXTURE["dimensions"]
    strongest = max(d, key=lambda x: x["score"])
    opportunity = min(d, key=lambda x: x["score"])
    score = FIXTURE["score"]
    band = band_for(score)

    radar_labels = "\n".join(
        f'<div class="mx-radar-label"><span>{esc(x["name"])}</span><strong>{x["score"]}</strong></div>'
        for x in d
    )

    key_steps = ["KNOW", "TELL", "ASK", "CREATE", "SCORE", "IMPROVE", "REPEAT"]
    key_markup = "\n".join(
        f'<div class="mx-key-step"><span>0{i}</span><strong>{step}</strong>'
        + (f'<b class="mx-key-arrow" aria-hidden="true">›</b>' if i < len(key_steps) else "")
        + "</div>"
        for i, step in enumerate(key_steps, 1)
    )

    html_doc = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="theme-color" content="#030305">
<meta name="description" content="Your MAXESS AI Mastery Results — a personalized map of how you work with AI and what to build next.">
<title>MAXESS — Your AI Mastery Results</title>
<style>
{build_css()}
</style>
</head>
<body>
<div class="mx-results" id="maxess-results" data-contract="MAXESS-RESULTS-CONTRACT-1">
  <div class="mx-utility-bar" aria-label="Results utilities">
    <span class="mx-utility-brand">MAXESS RESULTS</span>
    <button class="mx-copy-button" id="mx-copy-summary" type="button">Copy my result</button>
  </div>

  <div class="mx-fixture-badge">Development Result Preview</div>

  <section class="mx-section mx-hero" aria-labelledby="mx-hero-title">
    <div class="mx-glow"></div>
    <div class="mx-section-inner mx-hero-grid">
      <div>
        <div class="mx-hero-eyebrow">YOUR MAXESS RESULT</div>
        <h1 class="mx-hero-title" id="mx-hero-title">
          Understand<br><em>your AI.</em>
          <br>Then master it.
        </h1>
        <p class="mx-hero-copy">
          Your result is more than a score. It is a map of how you currently
          work with AI — what is already working, where your leverage is, and
          what you can build next.
        </p>
        <div class="mx-hero-note"><span></span> Built from the MAXESS Result Contract.</div>
      </div>
      <div>
        <div class="mx-score-orb" aria-label="MAXESS score {score} out of 100">
          <div class="mx-score-content">
            <div class="mx-score-number">{score}<small>MAXESS SCORE</small></div>
            <div class="mx-band-pill">{esc(band)}</div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="mx-section mx-profile" aria-labelledby="mx-profile-title">
    <div class="mx-section-inner mx-reading">
      <div class="mx-kicker">01 / THIS IS YOU</div>
      <div class="mx-profile-card mx-reveal">
        <p class="mx-profile-quote" id="mx-profile-title">
          You already have a meaningful AI capability base.
          Your biggest opportunity is not learning everything.
          It is learning how to use what you have with more leverage.
        </p>
        <p class="mx-profile-support">
          Your profile is not evenly distributed — and that is useful.
          The shape of your capability tells a more interesting story than
          the overall number alone.
        </p>
      </div>
    </div>
  </section>

  <section class="mx-section" aria-labelledby="mx-meaning-title">
    <div class="mx-section-inner">
      <div class="mx-kicker">02 / WHAT AI REALLY SAYS ABOUT YOU</div>
      <h2 class="mx-section-title" id="mx-meaning-title">
        The score is only the beginning.
      </h2>
      <p class="mx-section-lead">
        The useful question is not “How high is my number?”
        It is “What does my pattern allow me to do — and what would create
        the biggest next jump?”
      </p>
      <div class="mx-meaning-grid">
        <article class="mx-meaning-card mx-reveal">
          <span>01 / Strength</span>
          <h3>You have a capability to build on.</h3>
          <p>Your strongest dimension is an existing asset. Do not replace it. Turn it into leverage.</p>
        </article>
        <article class="mx-meaning-card mx-reveal">
          <span>02 / Opportunity</span>
          <h3>Your lowest score is not a verdict.</h3>
          <p>It identifies a place where a relatively small improvement may unlock disproportionate capability.</p>
        </article>
        <article class="mx-meaning-card mx-reveal">
          <span>03 / Direction</span>
          <h3>Your next level has a shape.</h3>
          <p>The fastest path is usually not “learn more.” It is learning the missing behavior that connects what you already do well.</p>
        </article>
      </div>
    </div>
  </section>

  <section class="mx-section mx-fingerprint" aria-labelledby="mx-fingerprint-title">
    <div class="mx-section-inner">
      <div class="mx-kicker">03 / YOUR FIVE-DIMENSION FINGERPRINT</div>
      <h2 class="mx-section-title" id="mx-fingerprint-title">How you naturally work with AI.</h2>
      <p class="mx-section-lead">
        This is your capability pattern — not a grade. The shape matters as
        much as the individual scores.
      </p>
      <div class="mx-fingerprint-layout">
        <div class="mx-radar" aria-label="Five-dimension capability fingerprint">
          <div class="mx-radar-ring"></div>
          <div class="mx-radar-ring"></div>
          <div class="mx-radar-ring"></div>
          <div class="mx-radar-ring"></div>
          <div class="mx-radar-spokes">
            <span class="mx-radar-spoke"></span>
            <span class="mx-radar-spoke"></span>
            <span class="mx-radar-spoke"></span>
            <span class="mx-radar-spoke"></span>
            <span class="mx-radar-spoke"></span>
          </div>
          <div class="mx-radar-polygon"></div>
          {radar_labels}
        </div>
        <div class="mx-dimension-list">
          {dimension_rows()}
        </div>
      </div>
    </div>
  </section>

  <section class="mx-section" aria-labelledby="mx-meaning-each-title">
    <div class="mx-section-inner">
      <div class="mx-kicker">04 / THE MEANING OF EVERY SCORE</div>
      <h2 class="mx-section-title" id="mx-meaning-each-title">Numbers become useful when they change what you do.</h2>
      <p class="mx-section-lead">
        Every dimension gives you a behavior to keep, a behavior to strengthen,
        and a practical way to turn the insight into action.
      </p>
    </div>
  </section>

  <section class="mx-section mx-leverage" aria-labelledby="mx-leverage-title">
    <div class="mx-section-inner">
      <div class="mx-kicker">05 / THE TWO THINGS THAT MATTER MOST</div>
      <h2 class="mx-section-title" id="mx-leverage-title">Strength creates leverage.</h2>
      <div class="mx-leverage-grid">
        <article class="mx-leverage-card advantage mx-reveal">
          <div class="mx-leverage-label">YOUR NATURAL ADVANTAGE</div>
          <div class="mx-leverage-score">{strongest["score"]}/100</div>
          <h3>{esc(strongest["name"])}</h3>
          <p>{esc(strongest["meaning"])} Your next move is to deliberately turn that strength into a repeatable advantage.</p>
        </article>
        <article class="mx-leverage-card mx-reveal">
          <div class="mx-leverage-label">YOUR HIGHEST-LEVERAGE OPPORTUNITY</div>
          <div class="mx-leverage-score">{opportunity["score"]}/100</div>
          <h3>{esc(opportunity["name"])}</h3>
          <p>{esc(opportunity["meaning"])} Improving this dimension can connect several of your existing strengths and raise the value of everything around it.</p>
        </article>
      </div>
    </div>
  </section>

  <section class="mx-section mx-revelation" aria-labelledby="mx-revelation-title">
    <div class="mx-section-inner">
      <div class="mx-revelation-card mx-reveal">
        <div class="mx-revelation-word">06 / THE REVELATION</div>
        <h2 id="mx-revelation-title">OH… THAT’S WHY.</h2>
        <p>
          You do not appear to have an AI knowledge problem. Your pattern suggests
          that the next leap comes from turning strong communication and direction
          into a more deliberate evaluation-and-systems loop.
        </p>
        <p>
          In plain English: you can already tell AI what you want.
          The opportunity is to become even better at judging the result,
          improving it, and building the process so the quality repeats.
        </p>
      </div>
    </div>
  </section>

  <section class="mx-section mx-next" aria-labelledby="mx-next-title">
    <div class="mx-section-inner">
      <div class="mx-next-card mx-reveal">
        <div>
          <div class="mx-next-number">07 / YOUR NEXT MOVE</div>
          <h2 id="mx-next-title">Turn judgment into a system.</h2>
          <p>
            For your next AI task, define the desired outcome, write down the
            quality test before you start, then score the result before you
            accept it. This single habit strengthens evaluation, iteration,
            and systems thinking at the same time.
          </p>
        </div>
        <a class="mx-next-button" href="#mx-path">Build my next capability →</a>
      </div>
    </div>
  </section>

  <section class="mx-section mx-path" id="mx-path" aria-labelledby="mx-path-title">
    <div class="mx-section-inner">
      <div class="mx-path-header">
        <div>
          <div class="mx-kicker">08 / YOUR PERSONALIZED AI PATH</div>
          <h2 class="mx-section-title" id="mx-path-title">These are doors, not products.</h2>
          <p class="mx-section-lead">
            Your result helps identify where exploration could become especially useful.
            You do not need to master everything. Start where leverage is highest.
          </p>
        </div>
        <div class="mx-path-count">18 AI MASTERY AREAS</div>
      </div>
      <div class="mx-area-grid">
        {area_cards()}
      </div>
    </div>
  </section>

  <section class="mx-section mx-naya" aria-labelledby="mx-naya-title">
    <div class="mx-section-inner">
      <div class="mx-kicker">09 / NAYA SEES YOUR PATTERN</div>
      <div class="mx-naya-card mx-reveal">
        <div class="mx-naya-avatar" aria-hidden="true"></div>
        <div>
          <div class="mx-naya-label">YOUR PERSONAL AI GUIDE</div>
          <h2 id="mx-naya-title">Naya noticed something interesting.</h2>
          <p>
            Your strongest opportunity is not to collect more prompts.
            It is to build a repeatable way of thinking with AI — one that
            turns your natural communication strength into better judgment,
            iteration, and systems.
          </p>
          <div class="mx-naya-actions">
            <button class="mx-audio-button" type="button" id="mx-listen">Naya — Listen to Your Report</button>
            <a class="mx-next-button" href="#mx-master-key">Show me the Master Key →</a>
          </div>
          <div class="mx-audio-status" id="mx-audio-status" role="status" aria-live="polite">
            Report tier: {esc(band)} · 91–100 Mastering · 76–90 Advancing · 51–75 Developing · 0–50 Foundation
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="mx-section mx-master-key" id="mx-master-key" aria-labelledby="mx-key-title">
    <div class="mx-section-inner">
      <div class="mx-kicker">10 / THE MASTER KEY</div>
      <h2 class="mx-section-title" id="mx-key-title">This is how you get better.</h2>
      <p class="mx-section-lead">
        You do not become powerful with AI by memorizing prompts.
        You become powerful by learning a repeatable way to think, create,
        judge, and improve.
      </p>
      <div class="mx-key">
        {key_markup}
      </div>
    </div>
  </section>

  <section class="mx-section mx-final-threshold" aria-labelledby="mx-threshold-title">
    <div class="mx-section-inner mx-threshold mx-reveal">
      <div class="mx-kicker">11 / THE THRESHOLD</div>
      <h2 id="mx-threshold-title">You know where you are. Now build from here.</h2>
      <p>
        Your result is not the end. It is the starting point for turning your
        existing strengths into real AI capability.
      </p>
    </div>
  </section>

  <div class="mx-foundation-label">
    The next chapter below is the existing NayaNET Page Code foundation.
    It is intentionally preserved as the final conversion experience.
  </div>
</div>

<script>
(function () {{
  "use strict";

  const result = {FIXTURE!r};
  const root = document.getElementById("maxess-results");
  const copyButton = document.getElementById("mx-copy-summary");
  const listenButton = document.getElementById("mx-listen");
  const audioStatus = document.getElementById("mx-audio-status");

  // Production contract hook:
  // When the assessment handoff is connected, replace the development fixture
  // with window.MAXESS_RESULT_CONTRACT. The presentation model stays the same.
  const production = window.MAXESS_RESULT_CONTRACT;
  const activeResult = production && production.contract
    ? production
    : result;

  window.MAXESS_RESULTS_STATE = {{
    contract: activeResult.contract,
    mode: activeResult.mode,
    score: activeResult.score,
    band: activeResult.band,
    dimensions: activeResult.dimensions
  }};

  function summaryText() {{
    const strongest = activeResult.dimensions.reduce((a, b) => a.score >= b.score ? a : b);
    const weakest = activeResult.dimensions.reduce((a, b) => a.score <= b.score ? a : b);
    return [
      "MAXESS RESULT",
      activeResult.score + "/100 — " + activeResult.band,
      "Natural advantage: " + strongest.name + " (" + strongest.score + "/100)",
      "Highest-leverage opportunity: " + weakest.name + " (" + weakest.score + "/100)",
      "Master Key: KNOW → TELL → ASK → CREATE → SCORE → IMPROVE → REPEAT"
    ].join("\\n");
  }}

  copyButton?.addEventListener("click", async function () {{
    try {{
      await navigator.clipboard.writeText(summaryText());
      copyButton.textContent = "Copied ✓";
      setTimeout(() => copyButton.textContent = "Copy my result", 1800);
    }} catch (_) {{
      copyButton.textContent = "Copy unavailable";
      setTimeout(() => copyButton.textContent = "Copy my result", 1800);
    }}
  }});

  listenButton?.addEventListener("click", function () {{
    const text = [
      "Your MAXESS score is " + activeResult.score + " out of 100.",
      "Your current level is " + activeResult.band + ".",
      "Your strongest capability is " + activeResult.dimensions.reduce((a,b) => a.score >= b.score ? a : b).name + ".",
      "Your highest leverage opportunity is " + activeResult.dimensions.reduce((a,b) => a.score <= b.score ? a : b).name + ".",
      "Your next move is to turn judgment into a repeatable system."
    ].join(" ");
    if ("speechSynthesis" in window) {{
      window.speechSynthesis.cancel();
      const utterance = new SpeechSynthesisUtterance(text);
      utterance.rate = .96;
      utterance.pitch = 1.0;
      window.speechSynthesis.speak(utterance);
      audioStatus.textContent = "Naya is reading your development report.";
    }} else {{
      audioStatus.textContent = "Audio is not supported in this browser.";
    }}
  }});

  const observer = new IntersectionObserver(
    entries => entries.forEach(entry => {{
      if (entry.isIntersecting) {{
        entry.target.classList.add("is-visible");
        observer.unobserve(entry.target);
      }}
    }}),
    {{ threshold: .12 }}
  );

  document.querySelectorAll(".mx-reveal").forEach(node => observer.observe(node));

  document.querySelectorAll(".mx-area-action").forEach(button => {{
    button.addEventListener("click", function () {{
      const area = this.dataset.area || "this AI mastery area";
      audioStatus && (audioStatus.textContent = "Pathway selected: " + area + ".");
      document.getElementById("mx-naya-title")?.scrollIntoView({{ behavior: "smooth", block: "center" }});
    }});
  }});

  root?.setAttribute("data-score-band", activeResult.band);
}})();
</script>
"""
    return html_doc


def load_nayanet() -> str:
    if not NAYANET_PATH.exists():
        raise FileNotFoundError(f"Missing NayaNET Page Code: {NAYANET_PATH}")
    code = NAYANET_PATH.read_text(encoding="utf-8")
    return code.lstrip("\ufeff").strip()


def build_embed(full_html: str) -> str:
    match = re.search(r"<body[^>]*>(.*)</body>", full_html, flags=re.I | re.S)
    if not match:
        raise RuntimeError("Could not extract body from final Results document.")
    body = match.group(1).strip()
    styles = "\n".join(re.findall(r"<style[^>]*>.*?</style>", full_html, flags=re.I | re.S))
    scripts = "\n".join(re.findall(r"<script[^>]*>.*?</script>", full_html, flags=re.I | re.S))
    visible = re.sub(r"<style[^>]*>.*?</style>", "", body, flags=re.I | re.S)
    visible = re.sub(r"<script[^>]*>.*?</script>", "", visible, flags=re.I | re.S)
    return "\n".join([styles, visible.strip(), scripts])


def main() -> None:
    nayanet = load_nayanet()
    full = build_html()
    final = full.replace(
        '<div class="mx-foundation-label">',
        '<div id="nayanet-foundation" class="nayanet-foundation-anchor" aria-label="NayaNET final chapter"></div>\n<div class="mx-foundation-label">'
    )
    final = final.replace("</div>\n\n<script>", "</div>\n\n" + nayanet + "\n\n<script>", 1)
    final += """
<script>
(function () {
  const SERVICE_URL = "https://takeyourpowerback.xyz/services";
  document.querySelectorAll('a[href="https://takeyourpowerback.xyz/"], a[href="https://takeyourpowerback.xyz"]').forEach(function (a) {
    const label = (a.textContent || "").toLowerCase();
    if (label.includes("trial") || label.includes("start") || label.includes("membership") || label.includes("join")) {
      a.href = SERVICE_URL;
    }
  });
})();
</script>
</body>
</html>
"""

    embed = build_embed(final)
    FULL_OUT.write_text(final, encoding="utf-8")
    EMBED_OUT.write_text(embed, encoding="utf-8")
    DEPLOY_FULL_OUT.write_text(final, encoding="utf-8")
    DEPLOY_EMBED_OUT.write_text(embed, encoding="utf-8")
    DEPLOY_EMBED_995_OUT.write_text(embed, encoding="utf-8")

    lines = final.count("\n") + 1
    bytes_ = len(final.encode("utf-8"))
    embed_lines = embed.count("\n") + 1
    embed_bytes = len(embed.encode("utf-8"))

    print(f"FINAL: {FULL_OUT} — {lines} lines / {bytes_} bytes")
    print(f"EMBED: {EMBED_OUT} — {embed_lines} lines / {embed_bytes} bytes")
    print(f"DEPLOYMENT ALIASES: {DEPLOY_FULL_OUT.name}, {DEPLOY_EMBED_OUT.name}, {DEPLOY_EMBED_995_OUT.name}")
    if lines < 3000:
        raise SystemExit("FINAL artifact is below the completeness gate (3000 lines).")
    if bytes_ < 100000:
        raise SystemExit("FINAL artifact is below the completeness gate (100 KB).")
    if embed_lines < 3000:
        raise SystemExit("Groove embed is below the completeness gate (3000 lines).")
    if embed_bytes < 100000:
        raise SystemExit("Groove embed is below the completeness gate (100 KB).")
    for marker in (
        "MAXESS-RESULTS-CONTRACT-1",
        "KNOW",
        "TELL",
        "ASK",
        "CREATE",
        "SCORE",
        "IMPROVE",
        "REPEAT",
        "Writing & Communication",
        "Advanced AI Work",
        "Naya — Listen to Your Report",
        "https://takeyourpowerback.xyz/services",
        "nayanet-foundation-anchor",
    ):
        if marker not in final:
            raise SystemExit(f"Missing required marker: {marker}")
    print("MAXESS FINAL RESULTS BUILD GATE: PASS")


if __name__ == "__main__":
    main()
