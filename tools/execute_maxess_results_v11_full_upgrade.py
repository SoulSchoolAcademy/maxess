#!/usr/bin/env python3
"""MAXESS Results V11 — preservation-first full-artifact upgrade.

This executor deliberately modifies the authoritative MAXESS-RESULTS-10-GROOVE.html
in place. It never creates a replacement Results implementation and never owns
assessment scoring. The existing 274KB+ artifact remains intact; this pass adds a
final, scoped presentation layer and runtime orchestration above the existing
components.

Naya Law requirements enforced here:
- preserve the existing artifact
- require a material source change
- keep window.MAXESS_RESULT authoritative
- no production fake result
- section order is explicit
- print mode is explicit
- reduced motion is explicit
- supplied Naya profile assets are used
- the public page remains the verification target
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TARGET = ROOT / "MAXESS-RESULTS-10-GROOVE.html"
MARKER = "<!-- MAXESS_RESULTS_V11_FULL_UPGRADE_EXECUTED -->"

CSS = r'''<style id="maxess-results-v11-full-upgrade">
/* ================================================================
   MAXESS RESULTS V11 — FINAL PRESENTATION LAYER
   Preservation-first. Scoped to #maxess-results-10.
   ================================================================ */
#maxess-results-10.v11-full-upgrade,
#maxess-results-10{
  --v11-black:#030307;
  --v11-white:#fff;
  --v11-soft:rgba(255,255,255,.74);
  --v11-muted:rgba(255,255,255,.48);
  --v11-line:rgba(255,255,255,.12);
  --v11-purple:#965dff;
  --v11-magenta:#ef4bc8;
  --v11-blue:#459cff;
  --v11-teal:#39d9cc;
  --v11-green:#42df98;
  --v11-yellow:#ffd84a;
  --v11-orange:#ff9d3d;
  --v11-red:#ff4b55;
  width:100vw!important;
  max-width:none!important;
  margin-left:calc(50% - 50vw)!important;
  margin-right:calc(50% - 50vw)!important;
  overflow-x:hidden!important;
  background:var(--v11-black)!important;
}
#maxess-results-10 .v11-wide{width:min(1760px,100%);margin-inline:auto}
#maxess-results-10 .v11-hidden{display:none!important}

/* HERO: score first, orb second, almost nothing else competing. */
#maxess-results-10 .mx-hero{
  min-height:min(900px,94vh)!important;
  display:grid!important;
  place-items:center!important;
  padding:clamp(54px,7vw,105px) clamp(18px,4vw,76px) clamp(52px,6vw,90px)!important;
  background:
    radial-gradient(circle at 50% 46%,rgba(150,93,255,.20),transparent 32%),
    radial-gradient(circle at 20% 55%,rgba(57,217,204,.045),transparent 30%),
    linear-gradient(180deg,#020205,#07040c 72%,#030307)!important;
}
#maxess-results-10 .mx-hero-grid{
  display:flex!important;
  flex-direction:column!important;
  align-items:center!important;
  justify-content:center!important;
  gap:24px!important;
  width:min(1250px,100%)!important;
  text-align:center!important;
}
#maxess-results-10 .mx-hero-grid>div:first-child{
  order:1!important;
  display:flex!important;
  flex-direction:column!important;
  align-items:center!important;
  width:100%!important;
  max-width:920px!important;
}
#maxess-results-10 .mx-hero-grid>.mx-score-orb{
  order:2!important;
  width:min(570px,72vw)!important;
  min-width:300px!important;
  margin:0 auto!important;
}
#maxess-results-10 .mx-hero .mx-eyebrow{color:rgba(255,255,255,.58)!important}
#maxess-results-10 .mx-hero .mx-title{
  margin:12px 0 0!important;
  font-size:clamp(42px,5.8vw,82px)!important;
  line-height:.92!important;
  letter-spacing:-.06em!important;
  color:#fff!important;
}
#maxess-results-10 .mx-hero .mx-title em{display:none!important}
#maxess-results-10 .mx-hero .mx-copy,
#maxess-results-10 .mx-hero .mx-proof,
#maxess-results-10 .mx-hero .hero-score-whisper{display:none!important}
#maxess-results-10 .mx-hero .mx-hero-actions{order:3!important;margin-top:4px!important;justify-content:center!important}
#maxess-results-10 .mx-hero .mx-cta-ghost{display:none!important}
#maxess-results-10 .mx-hero .mx-score-orb{
  --v11-a:#42df98;
  --v11-b:#459cff;
  background:
    radial-gradient(circle at 31% 24%,rgba(255,255,255,.30),transparent 10%),
    radial-gradient(circle at 50% 48%,color-mix(in srgb,var(--v11-a) 22%,transparent) 0,color-mix(in srgb,var(--v11-b) 13%,transparent) 34%,#0c0913 70%,#020205 100%)!important;
  border:1px solid color-mix(in srgb,var(--v11-b) 50%,white 12%)!important;
  box-shadow:
    0 0 0 1px rgba(255,255,255,.13),
    inset 0 0 100px color-mix(in srgb,var(--v11-a) 24%,transparent),
    inset 0 -30px 70px rgba(0,0,0,.65),
    0 42px 120px rgba(0,0,0,.70),
    0 0 150px color-mix(in srgb,var(--v11-a) 22%,transparent)!important;
  animation:v11Orb 5.4s ease-in-out infinite;
  will-change:transform,filter;
}
#maxess-results-10 .mx-hero .mx-score-orb::before{
  border-color:color-mix(in srgb,var(--v11-b) 58%,white 10%)!important;
  box-shadow:0 0 60px color-mix(in srgb,var(--v11-a) 30%,transparent)!important;
  animation:v11Ring 18s linear infinite;
}
#maxess-results-10 .mx-hero .mx-score-orb::after{
  border-color:color-mix(in srgb,var(--v11-b) 28%,white 5%)!important;
  animation:v11RingReverse 25s linear infinite;
}
#maxess-results-10 .mx-hero .mx-score strong{
  font-size:clamp(105px,13vw,188px)!important;
  background:linear-gradient(110deg,var(--v11-a),var(--v11-b),var(--v11-magenta))!important;
  -webkit-background-clip:text!important;
  background-clip:text!important;
  color:transparent!important;
  text-shadow:none!important;
  animation:v11Score 4s ease-in-out infinite;
}
#maxess-results-10 .mx-hero .mx-score span{color:rgba(255,255,255,.76)!important}
#maxess-results-10 .mx-hero .mx-band{display:none!important}
@keyframes v11Orb{0%,100%{transform:scale(1);filter:saturate(1) brightness(1)}50%{transform:scale(1.022);filter:saturate(1.18) brightness(1.06)}}
@keyframes v11Ring{to{transform:rotate(360deg)}}
@keyframes v11RingReverse{to{transform:rotate(-360deg)}}
@keyframes v11Score{0%,100%{transform:translateY(0)}50%{transform:translateY(-4px)}}

/* HERO CTA */
#maxess-results-10 .mx-hero .mx-cta-primary{
  min-height:56px!important;
  padding-inline:25px!important;
  border-radius:17px!important;
  background:linear-gradient(145deg,#e4d0ff 0%,#9860e8 32%,#52218f 68%,#180a2d 100%)!important;
  border:1px solid rgba(255,255,255,.45)!important;
  box-shadow:0 18px 42px rgba(0,0,0,.42),0 0 30px rgba(150,93,255,.14),inset 0 1px rgba(255,255,255,.72)!important;
}

/* NAYA WELCOME: immediately after score/orb. */
#maxess-results-10 .v11-naya-welcome{
  width:min(1120px,calc(100% - 30px));
  margin:0 auto;
  display:grid;
  grid-template-columns:88px minmax(0,1fr) auto;
  align-items:center;
  gap:22px;
  padding:22px 24px;
  border:1px solid rgba(150,93,255,.22);
  border-radius:28px;
  background:linear-gradient(110deg,rgba(150,93,255,.10),rgba(255,255,255,.035),rgba(57,217,204,.05));
  box-shadow:0 24px 70px rgba(0,0,0,.26),inset 0 1px rgba(255,255,255,.10);
}
#maxess-results-10 .v11-naya-avatar{
  width:88px;height:88px;border-radius:50%;object-fit:cover;
  border:2px solid rgba(255,255,255,.66);
  box-shadow:0 0 0 7px rgba(150,93,255,.08),0 14px 34px rgba(0,0,0,.30);
}
#maxess-results-10 .v11-naya-kicker{display:block;color:#c9a9ff;font-size:10px;font-weight:950;letter-spacing:.19em;text-transform:uppercase}
#maxess-results-10 .v11-naya-title{margin:5px 0 0;font-size:clamp(20px,2.3vw,31px);line-height:1.05;letter-spacing:-.035em;font-weight:820}
#maxess-results-10 .v11-naya-copy{margin:8px 0 0;color:rgba(255,255,255,.64);font-size:14px;line-height:1.5}
#maxess-results-10 .v11-naya-welcome .mx-cta{white-space:nowrap;min-height:50px}

/* CHAPTER SYSTEM */
#maxess-results-10 .v11-chapter{
  display:flex;align-items:center;gap:13px;margin-bottom:18px;
}
#maxess-results-10 .v11-chapter-num{
  display:grid;place-items:center;width:40px;height:40px;flex:0 0 40px;border-radius:50%;
  border:1px solid rgba(150,93,255,.32);background:rgba(150,93,255,.08);color:#d2b8ff;
  font-size:10px;font-weight:950;letter-spacing:.08em;
}
#maxess-results-10 .v11-chapter-label{display:block;color:rgba(255,255,255,.48);font-size:9px;font-weight:950;letter-spacing:.18em;text-transform:uppercase}
#maxess-results-10 .v11-chapter-sub{display:block;margin-top:3px;color:rgba(255,255,255,.42);font-size:11px}

/* ORDER + RHYTHM */
#maxess-results-10 .v11-white-chapter{background:#fff!important;color:#0b0a0f!important}
#maxess-results-10 .v11-white-chapter .mx-section-head h2{color:#0b0a0f!important}
#maxess-results-10 .v11-white-chapter .mx-section-head p{color:#3c3c43!important}
#maxess-results-10 .v11-white-chapter .v11-chapter-label{color:#5d5d65!important}
#maxess-results-10 .v11-white-chapter .v11-chapter-sub{color:#777!important}
#maxess-results-10 .v11-white-chapter .v11-chapter-num{color:#6637a8;background:#f0e9fa;border-color:#d9c8f0}

/* FIVE DIMENSIONS: premium circular gauge instruments. */
#maxess-results-10 .mx-dim-grid{grid-template-columns:repeat(5,minmax(150px,1fr))!important;gap:18px!important}
#maxess-results-10 .v11-dimension-card{
  --v11-g:#965dff;
  position:relative!important;min-height:330px!important;border-radius:30px!important;
  background:linear-gradient(160deg,#0a0a0f,#14101b)!important;
  border:1px solid rgba(255,255,255,.13)!important;
  box-shadow:inset 0 1px rgba(255,255,255,.13),0 28px 76px rgba(0,0,0,.40)!important;
  display:flex!important;flex-direction:column!important;align-items:center!important;text-align:center!important;
  padding:22px 17px!important;overflow:hidden!important;
  transition:transform .28s ease,border-color .28s ease,box-shadow .28s ease!important;
}
#maxess-results-10 .v11-dimension-card:hover,#maxess-results-10 .v11-dimension-card:focus-within{
  transform:translateY(-7px)!important;border-color:color-mix(in srgb,var(--v11-g) 52%,white 5%)!important;
  box-shadow:inset 0 1px rgba(255,255,255,.18),0 38px 100px rgba(0,0,0,.52),0 0 38px color-mix(in srgb,var(--v11-g) 12%,transparent)!important;
}
#maxess-results-10 .v11-dimension-card::before{
  content:"";position:absolute;top:19px;left:50%;width:156px;height:156px;transform:translateX(-50%);border-radius:50%;
  background:conic-gradient(var(--v11-g) calc(var(--v11-score,0)*1%),rgba(255,255,255,.075) 0);
  filter:drop-shadow(0 0 16px color-mix(in srgb,var(--v11-g) 35%,transparent));
}
#maxess-results-10 .v11-dimension-card::after{
  content:"";position:absolute;top:31px;left:50%;width:132px;height:132px;transform:translateX(-50%);border-radius:50%;
  background:#09090e;box-shadow:inset 0 0 26px rgba(0,0,0,.78),0 0 0 1px color-mix(in srgb,var(--v11-g) 22%,transparent);
}
#maxess-results-10 .v11-dimension-head{position:relative;z-index:2;margin-top:52px;display:flex;flex-direction:column;align-items:center;gap:5px}
#maxess-results-10 .v11-dimension-number{font-size:43px;line-height:1;font-weight:850;color:var(--v11-g);text-shadow:0 0 22px color-mix(in srgb,var(--v11-g) 30%,transparent)}
#maxess-results-10 .v11-dimension-name{font-size:16px;font-weight:800;color:#fff}
#maxess-results-10 .v11-dimension-card .mx-track{position:relative;z-index:2;width:82%;height:7px;margin:17px 0 12px;background:rgba(255,255,255,.08)}
#maxess-results-10 .v11-dimension-card .mx-track span{background:var(--v11-g)!important;box-shadow:0 0 16px color-mix(in srgb,var(--v11-g) 45%,transparent)!important}
#maxess-results-10 .v11-dimension-copy{position:relative;z-index:2;margin:0;color:rgba(255,255,255,.68);font-size:12px;line-height:1.5}
#maxess-results-10 .v11-dimension-lever{position:relative;z-index:2;width:100%;margin-top:auto;padding-top:12px;border-top:1px solid rgba(255,255,255,.08)}
#maxess-results-10 .v11-dimension-lever span{display:block;color:var(--v11-g);font-size:9px;font-weight:950;letter-spacing:.16em}
#maxess-results-10 .v11-dimension-lever b{display:block;margin-top:5px;color:#fff;font-size:11px;line-height:1.4}

/* RADAR / FINGERPRINT becomes an editorial white chapter. */
#maxess-results-10 #v11-fingerprint{background:#fff!important;color:#0b0a0f!important}
#maxess-results-10 #v11-fingerprint .mx-section-head h2{color:#0b0a0f!important}
#maxess-results-10 #v11-fingerprint .mx-section-head p{color:#38383f!important}
#maxess-results-10 #v11-fingerprint .mx-eyebrow{color:#6438a7!important}
#maxess-results-10 #v11-fingerprint .mx-list-row{background:#f4f3f7!important;color:#111!important;border-color:rgba(0,0,0,.08)!important}
#maxess-results-10 #v11-fingerprint .mx-list-row b,#maxess-results-10 #v11-fingerprint .mx-list-row span{color:#18181d!important}
#maxess-results-10 #v11-fingerprint .mx-list-row strong{color:#6637a8!important}
#maxess-results-10 #v11-fingerprint .mx-bar{background:#dddde4!important}
#maxess-results-10 #v11-fingerprint .mx-bar i{background:linear-gradient(90deg,#6738ad,#45c0dc)!important}

/* NAYA REPORT — personal, light, visual, not salesy. */
#maxess-results-10 #v11-naya-report{background:linear-gradient(180deg,#f7f7fa,#fff)!important;color:#0b0a0f!important}
#maxess-results-10 #v11-naya-report .mx-section-head h2{color:#0b0a0f!important}
#maxess-results-10 #v11-naya-report .mx-section-head p{color:#38383f!important}
#maxess-results-10 #v11-naya-report .v11-naya-panel{
  width:min(1180px,100%);margin:0 auto;border:1px solid rgba(0,0,0,.09);border-radius:32px;padding:clamp(28px,4vw,52px);
  background:#fff;box-shadow:0 30px 90px rgba(24,11,42,.10);display:grid;grid-template-columns:100px 1fr;gap:22px;align-items:center;
}
#maxess-results-10 #v11-naya-report .v11-naya-avatar{width:100px;height:100px;border-radius:50%;object-fit:cover;border:3px solid #fff;box-shadow:0 0 0 7px rgba(150,93,255,.08),0 14px 34px rgba(0,0,0,.18)}
#maxess-results-10 #v11-naya-report .v11-naya-name{color:#6738ad;font-size:10px;font-weight:950;letter-spacing:.18em}
#maxess-results-10 #v11-naya-report .v11-naya-speech{margin:7px 0 0;color:#111;font-size:clamp(20px,2.3vw,32px);line-height:1.12;letter-spacing:-.03em;font-weight:780}
#maxess-results-10 #v11-naya-report .v11-naya-sub{margin:9px 0 0;color:#4a4a51;font-size:14px;line-height:1.55}
#maxess-results-10 #v11-naya-report .mx-cta{margin-top:17px}

/* PATTERN */
#maxess-results-10 #v11-pattern{background:linear-gradient(180deg,#050308,#0c0712)!important}
#maxess-results-10 .v11-pattern-visual{position:relative;width:min(1100px,100%);margin:0 auto;display:grid;grid-template-columns:repeat(5,1fr);gap:14px;align-items:center;padding:28px 0}
#maxess-results-10 .v11-pattern-visual::before{content:"";position:absolute;left:7%;right:7%;top:50%;height:1px;background:linear-gradient(90deg,transparent,rgba(150,93,255,.42),rgba(69,156,255,.45),rgba(57,217,204,.42),transparent);box-shadow:0 0 25px rgba(150,93,255,.16)}
#maxess-results-10 .v11-pattern-node{position:relative;z-index:2;aspect-ratio:1;border-radius:50%;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;background:radial-gradient(circle at 34% 25%,rgba(255,255,255,.14),rgba(150,93,255,.08) 36%,#07070c 76%);border:1px solid rgba(255,255,255,.14);box-shadow:inset 0 1px rgba(255,255,255,.16),0 22px 60px rgba(0,0,0,.42);transition:transform .25s ease,border-color .25s ease}
#maxess-results-10 .v11-pattern-node:hover{transform:translateY(-7px) scale(1.03);border-color:rgba(150,93,255,.45)}
#maxess-results-10 .v11-pattern-node .dot{width:9px;height:9px;border-radius:50%;background:linear-gradient(135deg,#46e5ff,#965dff);box-shadow:0 0 17px rgba(70,229,255,.55);margin-bottom:10px}
#maxess-results-10 .v11-pattern-node b{font-size:12px;line-height:1.15}
#maxess-results-10 .v11-pattern-node strong{font-size:31px;line-height:1;margin-top:8px}
#maxess-results-10 .v11-pattern-node small{margin-top:7px;color:rgba(255,255,255,.45);font-size:8px;max-width:110px}

/* STRENGTHS / LEVER: white and dark contrast, not sales cards. */
#maxess-results-10 #v11-strengths,#maxess-results-10 #v11-lever{background:#fff!important;color:#0b0a0f!important}
#maxess-results-10 #v11-strengths .mx-section-head h2,#maxess-results-10 #v11-lever .mx-section-head h2{color:#0b0a0f!important}
#maxess-results-10 #v11-strengths .mx-section-head p,#maxess-results-10 #v11-lever .mx-section-head p{color:#3b3b42!important}
#maxess-results-10 #v11-strengths .v11-story-card,#maxess-results-10 #v11-lever .v11-story-card{border:1px solid rgba(0,0,0,.09);border-radius:30px;padding:clamp(26px,4vw,48px);background:#fff;box-shadow:0 26px 80px rgba(20,10,35,.10)}
#maxess-results-10 .v11-story-kicker{display:block;color:#6738ad;font-size:10px;font-weight:950;letter-spacing:.17em;text-transform:uppercase}
#maxess-results-10 .v11-story-title{margin:10px 0;font-size:clamp(30px,4vw,55px);line-height:.98;letter-spacing:-.05em;color:#111;font-weight:820}
#maxess-results-10 .v11-story-copy{max-width:820px;color:#444;font-size:16px;line-height:1.6}
#maxess-results-10 .v11-story-metric{display:inline-flex;align-items:baseline;gap:7px;margin-top:20px;font-weight:900;color:#6738ad}
#maxess-results-10 .v11-story-metric strong{font-size:62px;line-height:1;color:#111}
#maxess-results-10 .v11-lever-accent{border-left:5px solid #965dff!important}

/* NEXT MOVE: visual journey */
#maxess-results-10 #v11-next{background:linear-gradient(180deg,#060409,#12081a)!important}
#maxess-results-10 .v11-next-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:12px}
#maxess-results-10 .v11-next-step{position:relative;padding:24px;border-radius:24px;border:1px solid rgba(255,255,255,.11);background:linear-gradient(145deg,rgba(255,255,255,.055),rgba(255,255,255,.015));box-shadow:inset 0 1px rgba(255,255,255,.09),0 20px 50px rgba(0,0,0,.25)}
#maxess-results-10 .v11-next-step::after{content:"→";position:absolute;right:-13px;top:50%;transform:translateY(-50%);width:25px;height:25px;display:grid;place-items:center;border-radius:50%;background:#0b0711;border:1px solid rgba(150,93,255,.35);color:#cdb3ff;z-index:3}
#maxess-results-10 .v11-next-step:last-child::after{display:none}
#maxess-results-10 .v11-next-num{color:#c7a9ff;font-size:10px;font-weight:950;letter-spacing:.15em}
#maxess-results-10 .v11-next-step h3{margin:12px 0 6px;font-size:19px}
#maxess-results-10 .v11-next-step p{margin:0;color:rgba(255,255,255,.58);font-size:12px;line-height:1.5}

/* 18 NAYA MASTERS */
#maxess-results-10 #v11-masters{background:linear-gradient(180deg,#07050b,#14091d)!important}
#maxess-results-10 .v11-masters-lead{max-width:760px;margin:0 auto 28px;text-align:center;color:rgba(255,255,255,.62);font-size:16px;line-height:1.6}
#maxess-results-10 .v11-masters-grid{display:grid;grid-template-columns:repeat(6,minmax(0,1fr));gap:10px}
#maxess-results-10 .v11-master{position:relative;min-height:145px;padding:18px 14px;border:1px solid rgba(255,255,255,.11);border-radius:22px;background:linear-gradient(145deg,rgba(255,255,255,.055),rgba(255,255,255,.012));display:flex;flex-direction:column;justify-content:flex-end;overflow:hidden;transition:transform .22s ease,border-color .22s ease}
#maxess-results-10 .v11-master:hover{transform:translateY(-4px);border-color:rgba(150,93,255,.38)}
#maxess-results-10 .v11-master::before{content:"";position:absolute;width:70px;height:70px;right:-25px;top:-25px;border-radius:50%;background:radial-gradient(circle,rgba(150,93,255,.22),transparent 70%)}
#maxess-results-10 .v11-master-num{color:rgba(255,255,255,.38);font-size:9px;font-weight:950;letter-spacing:.12em}
#maxess-results-10 .v11-master-name{margin-top:7px;font-size:13px;font-weight:800;line-height:1.18}
#maxess-results-10 .v11-master-benefit{margin-top:6px;color:rgba(255,255,255,.45);font-size:10px;line-height:1.35}

/* PLAYGROUND = conversion zone, but after report. */
#maxess-results-10 #naya-playground{background:linear-gradient(135deg,#160a24,#050507 72%)!important;border-top:1px solid rgba(255,255,255,.10);border-bottom:1px solid rgba(255,255,255,.10)}
#maxess-results-10 .mx-naya-door{min-height:300px!important;border-radius:30px!important}

/* HUMAN + AI */
#maxess-results-10 #v11-human{background:linear-gradient(135deg,#09050e,#190923 52%,#040306)!important}
#maxess-results-10 .v11-human-grid{display:grid;grid-template-columns:minmax(300px,.8fr) minmax(0,1.2fr);align-items:center;gap:clamp(30px,7vw,100px)}
#maxess-results-10 .v11-human-image{position:relative;max-width:600px;margin:auto}
#maxess-results-10 .v11-human-image img{display:block;width:100%;border-radius:30px;border:1px solid rgba(255,255,255,.16);box-shadow:0 35px 100px rgba(0,0,0,.55)}
#maxess-results-10 .v11-human-copy h2{font-size:clamp(38px,5vw,72px);line-height:.94;letter-spacing:-.055em;margin:12px 0}
#maxess-results-10 .v11-human-copy p{max-width:650px;color:rgba(255,255,255,.68);font-size:17px;line-height:1.6}

/* REMOVE EARLY SALES INTERRUPTION */
#maxess-results-10 .v11-remove-commercial{display:none!important}

/* PRINT / PDF: black text on white paper. */
@media print{
  @page{size:letter;margin:.55in}
  html,body{background:#fff!important;color:#111!important}
  #maxess-results-10{width:100%!important;margin:0!important;background:#fff!important;color:#111!important}
  #maxess-results-10 .mx-section,#maxess-results-10 #v11-naya-report,#maxess-results-10 #v11-fingerprint,#maxess-results-10 #v11-strengths,#maxess-results-10 #v11-lever,#maxess-results-10 #v11-next,#maxess-results-10 #v11-masters,#maxess-results-10 #naya-playground,#maxess-results-10 #v11-human{background:#fff!important;color:#111!important;break-inside:avoid!important;padding:26px 0!important}
  #maxess-results-10 h1,#maxess-results-10 h2,#maxess-results-10 h3,#maxess-results-10 h4,#maxess-results-10 strong,#maxess-results-10 b{color:#111!important;-webkit-text-fill-color:#111!important;text-shadow:none!important}
  #maxess-results-10 p,#maxess-results-10 .mx-copy,#maxess-results-10 .mx-section-head p,#maxess-results-10 .v11-dimension-copy,#maxess-results-10 .v11-dimension-lever b,#maxess-results-10 .v11-human-copy p{color:#333!important}
  #maxess-results-10 .mx-hero{min-height:auto!important;background:#fff!important;padding:18px 0 30px!important}
  #maxess-results-10 .mx-hero .mx-score-orb{width:230px!important;min-width:0!important;background:#f3f3f5!important;box-shadow:none!important;animation:none!important}
  #maxess-results-10 .mx-hero .mx-score strong{font-size:90px!important;background:none!important;color:#111!important;-webkit-text-fill-color:#111!important;animation:none!important}
  #maxess-results-10 .mx-hero .mx-hero-actions,#maxess-results-10 .v11-naya-welcome .mx-cta,#maxess-results-10 .mx-cta,#maxess-results-10 .mx-mini{display:none!important}
  #maxess-results-10 .v11-dimension-card{background:#fff!important;color:#111!important;box-shadow:none!important;border:1px solid #bbb!important;break-inside:avoid!important}
  #maxess-results-10 .v11-dimension-card::before,#maxess-results-10 .v11-dimension-card::after{display:none!important}
  #maxess-results-10 .v11-dimension-number,#maxess-results-10 .v11-dimension-name,#maxess-results-10 .v11-dimension-lever b{color:#111!important}
  #maxess-results-10 .v11-pattern-node,#maxess-results-10 .v11-next-step,#maxess-results-10 .v11-master,#maxess-results-10 .v11-story-card,#maxess-results-10 .v11-naya-panel{background:#fff!important;color:#111!important;border:1px solid #bbb!important;box-shadow:none!important;break-inside:avoid!important}
  #maxess-results-10 .v11-pattern-node b,#maxess-results-10 .v11-pattern-node strong,#maxess-results-10 .v11-master-name,#maxess-results-10 .v11-story-title{color:#111!important}
  #maxess-results-10 .v11-naya-copy,#maxess-results-10 .v11-naya-sub{color:#333!important}
  #maxess-results-10 .v11-human-image img{box-shadow:none!important}
  .ny-page-inner{break-before:page!important}
}

@media(max-width:1150px){
  #maxess-results-10 .mx-dim-grid{grid-template-columns:repeat(3,minmax(0,1fr))!important}
  #maxess-results-10 .v11-masters-grid{grid-template-columns:repeat(4,minmax(0,1fr))}
  #maxess-results-10 .v11-next-grid{grid-template-columns:repeat(2,1fr);gap:14px}
  #maxess-results-10 .v11-next-step:nth-child(2)::after{display:none}
}
@media(max-width:800px){
  #maxess-results-10 .v11-naya-welcome{grid-template-columns:72px minmax(0,1fr);gap:15px}
  #maxess-results-10 .v11-naya-avatar{width:72px;height:72px}
  #maxess-results-10 .v11-naya-welcome .mx-cta{grid-column:1/-1;width:100%}
  #maxess-results-10 .v11-pattern-visual{grid-template-columns:repeat(2,1fr)}
  #maxess-results-10 .v11-pattern-visual::before{display:none}
  #maxess-results-10 .v11-pattern-node{width:min(220px,100%);margin:auto}
  #maxess-results-10 .v11-pattern-node:last-child{grid-column:1/-1}
  #maxess-results-10 .v11-human-grid{grid-template-columns:1fr}
  #maxess-results-10 .v11-human-copy{text-align:center}
  #maxess-results-10 .v11-human-copy p{margin-inline:auto}
}
@media(max-width:680px){
  #maxess-results-10 .mx-hero{min-height:auto!important;padding-top:50px!important;padding-bottom:48px!important}
  #maxess-results-10 .mx-hero-grid>.mx-score-orb{width:min(410px,84vw)!important}
  #maxess-results-10 .mx-dim-grid{grid-template-columns:1fr!important;gap:12px!important}
  #maxess-results-10 .v11-dimension-card{min-height:315px!important}
  #maxess-results-10 .v11-masters-grid{grid-template-columns:repeat(2,minmax(0,1fr))}
  #maxess-results-10 .v11-next-grid{grid-template-columns:1fr}
  #maxess-results-10 .v11-next-step::after{display:none}
  #maxess-results-10 .v11-naya-panel{grid-template-columns:1fr;text-align:center}
  #maxess-results-10 .v11-naya-panel .v11-naya-avatar{margin-inline:auto}
}
@media(prefers-reduced-motion:reduce){
  #maxess-results-10 .mx-score-orb,#maxess-results-10 .mx-score-orb::before,#maxess-results-10 .mx-score-orb::after,#maxess-results-10 .mx-score strong{animation:none!important}
  #maxess-results-10 .v11-dimension-card,#maxess-results-10 .v11-pattern-node,#maxess-results-10 .v11-master,#maxess-results-10 .mx-cta{transition:none!important}
}
</style>'''

JS = r'''<script id="maxess-results-v11-full-upgrade-js">
(function(){
  'use strict';
  const root=document.getElementById('maxess-results-10');
  if(!root || root.dataset.v11FullUpgrade==='1') return;
  root.dataset.v11FullUpgrade='1';

  const NAYA_WHITE='https://raw.githubusercontent.com/SoulSchoolAcademy/maxess/main/Naya%20Profile%20white.jpg';
  const NAYA_BLACK='https://raw.githubusercontent.com/SoulSchoolAcademy/maxess/main/Naya%20Profile%20Black.jpg';
  const SHAWN_NAYA='https://i.postimg.cc/d1nncN9F/Naya-and-shawn-ok-44-a.png';
  const scoreBand=s=>s>=91?'Mastering':s>=76?'Advancing':s>=51?'Developing':'Foundation';
  const clamp=n=>Math.max(0,Math.min(100,n));
  const getResult=()=>window.MAXESS_RESULT||null;
  const getScore=()=>{const r=getResult();const n=Number(r&&((r.overallScore??r.score??r.masterScore)));return Number.isFinite(n)?clamp(n):null};
  const getDims=()=>{
    const r=getResult();
    if(!r)return [];
    const raw=Array.isArray(r.dimensions)?r.dimensions:[];
    return raw.slice(0,5).map((d,i)=>({id:d.id||String(i+1),name:d.name||d.label||`Dimension ${i+1}`,score:clamp(Number(d.score??d.value??0)||0),description:d.description||d.insight||''}));
  };
  const esc=s=>String(s).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
  const palette=s=>{
    if(s<50)return['#ff4b55','#ff9d3d'];
    if(s<65)return['#ff9d3d','#ffd84a'];
    if(s<75)return['#ffd84a','#39df91'];
    if(s<85)return['#39df91','#46e5ff'];
    if(s<90)return['#46e5ff','#4c9dff'];
    if(s<95)return['#4c9dff','#965dff'];
    return['#965dff','#ef4bc8'];
  };
  const dimColors=['#ff9d3d','#ffd84a','#39df91','#4c9dff','#965dff'];

  function scoreDrivenOrb(){
    const s=getScore(); if(s===null)return;
    const orb=root.querySelector('.mx-score-orb'); if(!orb)return;
    const [a,b]=palette(s);
    orb.style.setProperty('--v11-a',a);orb.style.setProperty('--v11-b',b);
    const strong=orb.querySelector('.mx-score strong');if(strong)strong.textContent=Math.round(s);
    const label=orb.querySelector('.mx-score span');if(label)label.textContent='YOUR AI SCORE';
    orb.setAttribute('role','img');orb.setAttribute('aria-label',`Your MAXESS AI score is ${Math.round(s)} out of 100`);
  }

  function heroCopy(){
    const hero=root.querySelector('.mx-hero'); if(!hero)return;
    const first=hero.querySelector('.mx-hero-grid>div:first-child'); if(!first)return;
    const s=getScore();
    const h=first.querySelector('.mx-title');if(h)h.innerHTML='YOUR AI SCORE';
    const e=first.querySelector('.mx-eyebrow');if(e)e.textContent='MAXESS AI MASTERY ASSESSMENT';
    first.querySelectorAll('.mx-copy,.mx-proof,.hero-score-whisper,.mx-band').forEach(x=>x.remove());
    const actions=first.querySelector('.mx-hero-actions');
    if(actions){
      actions.innerHTML=`<a class="mx-cta mx-cta-primary" href="#v11-naya-report">See Your Results <span aria-hidden="true">↓</span></a>`;
    }
  }

  function nayaWelcome(){
    if(root.querySelector('.v11-naya-welcome'))return;
    const hero=root.querySelector('.mx-hero');if(!hero)return;
    const s=getScore();
    const welcome=document.createElement('aside');welcome.className='v11-naya-welcome';
    welcome.innerHTML=`<img class="v11-naya-avatar" src="${NAYA_BLACK}" alt="Naya" loading="eager"><div><span class="v11-naya-kicker">NAYA · YOUR AI GUIDE</span><h2 class="v11-naya-title">Hi. I'm Naya. Let's make sense of your result.</h2><p class="v11-naya-copy">You just created a picture of how you work with AI. I'll help you understand it, see what matters, and choose your next move.</p></div><button class="mx-cta mx-cta-primary" type="button" id="v11-naya-listen">Listen to Naya <span aria-hidden="true">▶</span></button>`;
    hero.insertAdjacentElement('afterend',welcome);
    welcome.querySelector('#v11-naya-listen').addEventListener('click',()=>{
      const b=root.querySelector('#mx-naya-listen');if(b)b.click();
      else window.dispatchEvent(new CustomEvent('maxess:naya-report'));
    });
  }

  function removeShortVersion(){
    root.querySelectorAll('section').forEach(sec=>{
      const t=(sec.textContent||'').replace(/\s+/g,' ').trim().toLowerCase();
      if(t.includes('the short version') && t.includes('meaningful ai foundation'))sec.remove();
    });
  }

  function chapter(sec,num,label,sub){
    if(!sec)return;
    const head=sec.querySelector('.mx-section-head');if(!head)return;
    if(head.querySelector('.v11-chapter'))return;
    const c=document.createElement('div');c.className='v11-chapter';c.innerHTML=`<span class="v11-chapter-num">${num}</span><div><span class="v11-chapter-label">${label}</span><span class="v11-chapter-sub">${sub}</span></div>`;
    head.prepend(c);
  }

  function locate(){
    const sections=[...root.querySelectorAll(':scope>section')];
    const find=(terms)=>sections.find(s=>terms.some(t=>(s.textContent||'').toLowerCase().includes(t)));
    return {
      hero:root.querySelector('.mx-hero'),
      report:find(['listen to your results','personalized report','naya · your personal report']),
      fingerprint:root.querySelector('#your-fingerprint')||find(['your fingerprint','see the pattern']),
      dimensions:find(['every score has','five dimensions','what it means']),
      strengths:root.querySelector('#your-strengths')||find(['natural advantage','what you already']),
      lever:root.querySelector('#biggest-lever')||find(['highest-leverage opportunity','biggest lever']),
      next:root.querySelector('#your-next-move')||find(['your next chapter','from capability','your next move']),
      masters:root.querySelector('#naya-masters')||find(['your 18 ai pathways','18 ai pathways']),
      playground:root.querySelector('#naya-playground'),
      media:root.querySelector('.ny-page-inner')
    };
  }

  function rebuildDimensions(sec){
    if(!sec)return;
    const dims=getDims();if(dims.length!==5)return;
    let cards=[...sec.querySelectorAll('.mx-dim')].slice(0,5);
    if(cards.length!==5)return;
    cards.forEach((card,i)=>{
      const d=dims[i],color=dimColors[i];
      card.classList.add('v11-dimension-card');
      card.style.setProperty('--v11-g',color);card.style.setProperty('--v11-score',d.score);
      card.setAttribute('data-score',d.score);card.setAttribute('tabindex','0');
      card.innerHTML=`<div class="v11-dimension-head"><span class="v11-dimension-name">${esc(d.name)}</span><strong class="v11-dimension-number">${Math.round(d.score)}</strong></div><div class="mx-track"><span style="--w:${d.score}%"></span></div><p class="v11-dimension-copy">${esc(d.description||defaultDimensionCopy(d.name,d.score))}</p><div class="v11-dimension-lever"><span>LEVER</span><b>${esc(defaultLever(d.name,d.score))}</b></div>`;
    });
    const grid=sec.querySelector('.mx-dim-grid');if(grid){grid.innerHTML='';cards.forEach(c=>grid.appendChild(c));}
  }
  function defaultDimensionCopy(name,score){
    const n=name.toLowerCase();
    if(n.includes('communication'))return 'You can express context, intent and the human outcome behind a request.';
    if(n.includes('direction'))return 'You usually know what you want AI to help you accomplish.';
    if(n.includes('evaluation'))return 'You can recognize useful work and are ready to make judgment more deliberate.';
    if(n.includes('iteration'))return 'You understand that quality improves through refinement rather than one-shot prompting.';
    if(n.includes('system'))return 'You can see the bigger system and can turn repeated work into leverage.';
    return score>=85?'A strong capability you can turn into repeatable advantage.':score>=70?'A useful capability with room to sharpen.':'A high-value area for focused growth.';
  }
  function defaultLever(name,score){
    const n=name.toLowerCase();
    if(n.includes('communication'))return 'Turn your strength into reusable briefs, instructions and decision frameworks.';
    if(n.includes('direction'))return 'Define the outcome and success test before asking AI to work.';
    if(n.includes('evaluation'))return 'Score meaningful AI output before accepting it.';
    if(n.includes('iteration'))return 'Make the improvement loop explicit: create, score, improve, repeat.';
    if(n.includes('system'))return 'Turn one repeated workflow into a reusable system.';
    return score>=85?'Protect and compound this strength.':'Practice this capability on one real workflow this week.';
  }

  function fingerprint(sec){
    if(!sec)return;
    sec.id='v11-fingerprint';
    const h=sec.querySelector('.mx-section-head h2');if(h)h.innerHTML='SEE THE PATTERN,<br>NOT JUST THE SCORE.';
    const p=sec.querySelector('.mx-section-head p');if(p)p.textContent='Your score tells you where you are. Your pattern shows how your strengths work together.';
    chapter(sec,'03','YOUR FINGERPRINT','The shape of your current capability');
  }

  function nayaReport(sec){
    if(!sec)return;
    sec.id='v11-naya-report';
    sec.classList.add('v11-white-chapter');
    const head=sec.querySelector('.mx-section-head');
    if(head){
      const h=head.querySelector('h2');if(h)h.innerHTML='LISTEN TO<br>YOUR RESULTS';
      const p=head.querySelector('p');if(p)p.textContent='Naya turns your assessment into a personal conversation about where you are, what it means, and what to do next.';
      chapter(sec,'02','YOUR REPORT','Your result, interpreted by Naya');
    }
    if(!sec.querySelector('.v11-naya-panel')){
      const panel=document.createElement('div');panel.className='v11-naya-panel';
      panel.innerHTML=`<img class="v11-naya-avatar" src="${NAYA_WHITE}" alt="Naya" loading="lazy"><div><span class="v11-naya-name">NAYA · YOUR AI GUIDE</span><div class="v11-naya-speech">“You have a result. Now let's turn it into something useful.”</div><p class="v11-naya-sub">Listen to your report, then keep exploring below.</p><button class="mx-cta mx-cta-primary" type="button" id="v11-report-listen">Naya — Listen to Your Report <span aria-hidden="true">▶</span></button></div>`;
      sec.querySelector('.mx-wide')?.appendChild(panel);
      panel.querySelector('#v11-report-listen').addEventListener('click',()=>{const b=root.querySelector('#mx-naya-listen');if(b)b.click();else window.dispatchEvent(new CustomEvent('maxess:naya-report'));});
    }
  }

  function buildPattern(dims){
    if(root.querySelector('#v11-pattern'))return;
    const sec=document.createElement('section');sec.id='v11-pattern';sec.className='mx-section';
    sec.innerHTML=`<div class="mx-wide"><div class="mx-section-head"><div><div class="v11-chapter"><span class="v11-chapter-num">04</span><div><span class="v11-chapter-label">YOUR PATTERN</span><span class="v11-chapter-sub">How your dimensions work together</span></div></div><h2>SEE THE PATTERN.</h2></div><p>Your five dimensions are not five separate scores. Together they form your AI working signature.</p></div><div class="v11-pattern-visual">${dims.map((d,i)=>`<div class="v11-pattern-node"><span class="dot" aria-hidden="true"></span><b>${esc(d.name)}</b><strong>${Math.round(d.score)}</strong><small>${esc(patternCopy(d.name))}</small></div>`).join('')}</div></div>`;
    return sec;
  }
  function patternCopy(name){const n=name.toLowerCase();if(n.includes('communication'))return 'Express';if(n.includes('direction'))return 'Direct';if(n.includes('evaluation'))return 'Judge';if(n.includes('iteration'))return 'Improve';if(n.includes('system'))return 'Connect';return 'Build';}

  function strengths(sec){
    if(!sec)return;
    sec.id='v11-strengths';
    const h=sec.querySelector('.mx-section-head h2');if(h)h.innerHTML='YOUR<br>STRENGTHS';
    const p=sec.querySelector('.mx-section-head p');if(p)p.textContent='The abilities you already have are not just nice scores. They are assets you can build on.';
    chapter(sec,'06','YOUR STRENGTHS','What you already have working for you');
    const panels=[...sec.querySelectorAll('.mx-panel')];
    panels.forEach((panel,i)=>{
      panel.classList.add('v11-story-card');
      const h3=panel.querySelector('h3');if(h3)h3.classList.add('v11-story-title');
    });
  }

  function lever(sec){
    if(!sec)return;
    sec.id='v11-lever';
    const h=sec.querySelector('.mx-section-head h2');if(h)h.innerHTML='YOUR BIGGEST<br>LEVER';
    const p=sec.querySelector('.mx-section-head p');if(p)p.textContent='The one area where focused improvement can create the greatest return.';
    chapter(sec,'07','YOUR BIGGEST LEVER','Where improvement can create disproportionate upside');
    sec.querySelectorAll('.mx-panel').forEach(p=>p.classList.add('v11-story-card','v11-lever-accent'));
  }

  function nextMove(sec){
    if(!sec)return;
    sec.id='v11-next';
    const h=sec.querySelector('.mx-section-head h2');if(h)h.innerHTML='YOUR<br>NEXT MOVE';
    const p=sec.querySelector('.mx-section-head p');if(p)p.textContent='One focused move beats ten scattered improvements. Start where your leverage is highest.';
    chapter(sec,'08','YOUR NEXT MOVE','Turn insight into one concrete action');
    const path=sec.querySelector('.mx-path');
    if(path){path.classList.add('v11-next-grid');[...path.children].forEach((el,i)=>{el.classList.add('v11-next-step');const title=el.querySelector('h3');if(title){title.textContent=['Direct with intention','Build the first version','Score the result','Make the win reusable'][i]||title.textContent}const strong=el.querySelector('strong');if(strong)strong.classList.add('v11-next-num')});}
  }

  const pathwayBenefits=[
    'Turn thoughts into clear words.','Find and synthesize useful information.','Expand ideas without losing the goal.','Create useful human content faster.','Turn insight into strategy and decisions.','Make value understandable and actionable.','Learn with an always-available thinking partner.','Build, debug and improve software.','Turn concepts into visual communication.','Plan and produce video and media.','Create polished deliverables from rough thinking.','Use evidence to make better decisions.','Turn intention into organized execution.','Build skills, positioning and opportunity.','Think through choices with more clarity.','Explore and finish original creative work.','Connect repeated work into reliable systems.','Orchestrate models, tools, context and evaluation.'
  ];
  function masters(sec){
    if(!sec)return;
    sec.id='v11-masters';
    const h=sec.querySelector('.mx-section-head h2');if(h)h.innerHTML='18 NAYA<br>MASTERS';
    const p=sec.querySelector('.mx-section-head p');if(p)p.textContent='Specialist AI Masters designed to help you turn a capability into an exceptional result.';
    chapter(sec,'09','YOUR NAYA MASTERS','18 specialist pathways');
    const areas=[...sec.querySelectorAll('.mx-area')].slice(0,18);if(!areas.length)return;
    const grid=document.createElement('div');grid.className='v11-masters-grid';
    areas.forEach((a,i)=>{
      const name=a.querySelector('h3')?.textContent.trim()||`Naya Master ${i+1}`;
      const card=document.createElement('article');card.className='v11-master';
      card.innerHTML=`<span class="v11-master-num">${String(i+1).padStart(2,'0')}</span><span class="v11-master-name">Naya ${esc(name.replace(/^Naya\s+/i,''))}</span><span class="v11-master-benefit">${pathwayBenefits[i]}</span>`;
      grid.appendChild(card);
    });
    const existing=sec.querySelector('.mx-areas');
    if(existing)existing.replaceWith(grid);
  }

  function human(media){
    if(root.querySelector('#v11-human'))return;
    const sec=document.createElement('section');sec.id='v11-human';sec.className='mx-section';
    sec.innerHTML=`<div class="mx-wide v11-human-grid"><div class="v11-human-image"><img src="${SHAWN_NAYA}" alt="Shawn and Naya" loading="lazy"></div><div class="v11-human-copy"><span class="mx-eyebrow">HUMAN + AI</span><h2>Technology should amplify the human.</h2><p>The goal is not to become more machine-like. It is to become more capable — with Naya helping you turn your own strengths into exceptional results.</p></div></div>`;
    const anchor=media||root.querySelector('#naya-playground');
    if(anchor)anchor.insertAdjacentElement('afterend',sec);else root.appendChild(sec);
  }

  function reorder(){
    const x=locate();
    const pattern=buildPattern(getDims());
    const order=[x.hero, x.report, x.fingerprint, pattern, x.dimensions, x.strengths, x.lever, x.next, x.masters, x.playground];
    order.filter(Boolean).forEach(sec=>root.appendChild(sec));
    human(x.media);
    if(x.media)root.appendChild(x.media);
    root.querySelectorAll('section').forEach(sec=>{
      const t=(sec.textContent||'').toLowerCase();
      if(t.includes('short version')&&t.includes('meaningful ai foundation'))sec.remove();
    });
  }

  function apply(){
    const s=getScore(); if(s===null)return;
    scoreDrivenOrb();heroCopy();nayaWelcome();removeShortVersion();
    const x=locate();
    fingerprint(x.fingerprint);nayaReport(x.report);rebuildDimensions(x.dimensions);strengths(x.strengths);lever(x.lever);nextMove(x.next);masters(x.masters);reorder();
    root.setAttribute('data-v11-result-score',String(Math.round(s)));
    root.setAttribute('data-v11-band',scoreBand(s));
  }

  function waitForResult(){
    let tries=0;
    const run=()=>{tries++;if(getScore()!==null){apply();return}if(tries<40)setTimeout(run,100);};
    run();
  }
  if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',waitForResult,{once:true});else waitForResult();
  window.addEventListener('maxess:result-ready',apply);
})();
</script>'''


def execute():
    if not TARGET.exists():
        raise SystemExit(f"Missing authoritative artifact: {TARGET}")
    source = TARGET.read_text(encoding='utf-8')
    if MARKER in source:
        print('V11 already executed; refusing duplicate mutation.')
        return
    if 'id="maxess-results-10"' not in source:
        raise SystemExit('BLOCKED — authoritative Results root not found.')
    if 'window.MAXESS_RESULT' not in source:
        raise SystemExit('BLOCKED — MAXESS_RESULT contract not found.')
    before = len(source)
    # Insert CSS before </head>, JS before </body>; existing artifact is otherwise byte-for-byte preserved.
    if '</head>' not in source or '</body>' not in source:
        raise SystemExit('BLOCKED — malformed HTML boundary.')
    upgraded = source.replace('</head>', CSS + '\n</head>', 1)
    upgraded = upgraded.replace('</body>', JS + '\n</body>', 1)
    upgraded = upgraded.replace('</html>', MARKER + '\n</html>', 1)
    after = len(upgraded)
    if after <= before:
        raise SystemExit('BLOCKED — ZERO-CHANGE EXECUTION')
    if 'YOUR AI SCORE' not in upgraded or 'v11-naya-welcome' not in upgraded or 'v11-masters-grid' not in upgraded:
        raise SystemExit('BLOCKED — distinctive change proof missing.')
    TARGET.write_text(upgraded, encoding='utf-8')
    print(f'V11 upgrade executed: {before} -> {after} bytes; +{after-before} bytes')


if __name__ == '__main__':
    execute()
