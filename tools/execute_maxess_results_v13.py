#!/usr/bin/env python3
"""MAXESS Results V13 — visible redesign execution layer.

V13 exists because V11/V12 changed the artifact but did not reliably produce a
materially different, clearly inspectable user-facing composition. This pass
creates an explicit editorial presentation shell inside the authoritative
Groove artifact while preserving the real MAXESS_RESULT contract and reusing
existing video/conversion content where available.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TARGET = ROOT / "MAXESS-RESULTS-10-GROOVE.html"
MARKER = "<!-- MAXESS_RESULTS_V13_VISIBLE_EXECUTION -->"

CSS = r'''<style id="maxess-results-v13-css">
/* ================================================================
   MAXESS V13 — VISIBLE EXECUTION SYSTEM
   Purpose: make the report unmistakably personal, visual, ordered,
   scannable and materially different from the V12 presentation.
   ================================================================ */
#maxess-results-10.v13-active{--v13-bg:#050507;--v13-white:#fff;--v13-ink:#111;--v13-soft:rgba(255,255,255,.68);--v13-muted:rgba(255,255,255,.42);--v13-purple:#8b4dff;--v13-magenta:#ee43c8;--v13-blue:#45a4ff;--v13-teal:#2ed8c5;--v13-green:#36dd91;--v13-yellow:#ffd447;--v13-orange:#ff9638;--v13-red:#ff4c55;background:#050507!important;color:#fff!important}
#maxess-results-10.v13-active .v13-shell{display:block;min-height:100vh;background:#050507;color:#fff;overflow:hidden}
#maxess-results-10.v13-active .v13-wrap{width:min(1580px,calc(100% - 40px));margin:0 auto}
#maxess-results-10.v13-active .v13-chapter{display:flex;align-items:center;gap:11px;margin:0 0 20px;color:rgba(255,255,255,.48);font-size:10px;font-weight:900;letter-spacing:.2em;text-transform:uppercase}
#maxess-results-10.v13-active .v13-chapter i{font-style:normal;display:grid;place-items:center;width:32px;height:32px;border-radius:50%;border:1px solid rgba(255,255,255,.15);background:rgba(139,77,255,.1);color:#cdb8ff;letter-spacing:0}
#maxess-results-10.v13-active .v13-h2{margin:0;max-width:1000px;font-size:clamp(38px,5.2vw,78px);line-height:.93;letter-spacing:-.065em;font-weight:850}
#maxess-results-10.v13-active .v13-sub{max-width:690px;margin:18px 0 0;color:#555;font-size:16px;line-height:1.55}

/* HERO: score first, orb second, nothing competing with it */
#maxess-results-10.v13-active .v13-hero{position:relative;min-height:min(920px,100vh);display:flex;align-items:center;padding:56px 0 70px;background:radial-gradient(circle at 50% 44%,rgba(139,77,255,.18),transparent 27%),radial-gradient(circle at 12% 76%,rgba(46,216,197,.08),transparent 26%),radial-gradient(circle at 90% 22%,rgba(238,67,200,.07),transparent 24%),linear-gradient(180deg,#020204 0,#08050b 70%,#050507 100%)}
#maxess-results-10.v13-active .v13-hero-tools{position:absolute;top:22px;right:22px;display:flex;gap:10px}
#maxess-results-10.v13-active .v13-tool{border:1px solid rgba(255,255,255,.18);background:rgba(255,255,255,.055);color:#fff;border-radius:13px;padding:11px 15px;font-weight:800;cursor:pointer;backdrop-filter:blur(16px)}
#maxess-results-10.v13-active .v13-hero-inner{width:min(980px,100%);margin:auto;text-align:center;display:flex;flex-direction:column;align-items:center}
#maxess-results-10.v13-active .v13-overline{color:rgba(255,255,255,.48);font-size:11px;font-weight:900;letter-spacing:.24em;text-transform:uppercase}
#maxess-results-10.v13-active .v13-score-label{margin-top:13px;font-size:clamp(42px,5.2vw,76px);line-height:.9;letter-spacing:-.065em;font-weight:900}
#maxess-results-10.v13-active .v13-score-orb{--a:#36dd91;--b:#45a4ff;position:relative;width:min(590px,76vw);aspect-ratio:1;margin:38px auto 0;border-radius:50%;display:grid;place-items:center;background:radial-gradient(circle at 30% 21%,rgba(255,255,255,.33),transparent 9%),radial-gradient(circle at 50% 48%,color-mix(in srgb,var(--a) 28%,transparent),color-mix(in srgb,var(--b) 19%,transparent) 31%,#0b0910 67%,#020204 100%);border:1px solid color-mix(in srgb,var(--b) 58%,white 12%);box-shadow:0 0 0 1px rgba(255,255,255,.1),inset 0 0 120px color-mix(in srgb,var(--a) 25%,transparent),0 50px 130px rgba(0,0,0,.72),0 0 170px color-mix(in srgb,var(--a) 18%,transparent);animation:v13Orb 5.5s ease-in-out infinite}
#maxess-results-10.v13-active .v13-score-orb:before{content:"";position:absolute;inset:8%;border-radius:50%;border:1px solid color-mix(in srgb,var(--b) 62%,white 10%);box-shadow:0 0 65px color-mix(in srgb,var(--a) 27%,transparent);animation:v13Spin 20s linear infinite}
#maxess-results-10.v13-active .v13-score-orb:after{content:"";position:absolute;inset:16%;border-radius:50%;border:1px solid rgba(255,255,255,.08);animation:v13SpinReverse 28s linear infinite}
#maxess-results-10.v13-active .v13-score-number{position:relative;z-index:2;font-size:clamp(120px,17vw,230px);line-height:.75;letter-spacing:-.09em;font-weight:900;background:linear-gradient(110deg,var(--a),var(--b),#ee43c8);-webkit-background-clip:text;background-clip:text;color:transparent}
#maxess-results-10.v13-active .v13-score-caption{position:relative;z-index:2;margin-top:32px;color:rgba(255,255,255,.76);font-size:11px;font-weight:900;letter-spacing:.25em;text-transform:uppercase}
#maxess-results-10.v13-active .v13-band{margin-top:14px;padding:7px 12px;border-radius:999px;border:1px solid rgba(255,255,255,.17);background:rgba(255,255,255,.05);font-size:11px;font-weight:850;letter-spacing:.12em;text-transform:uppercase}
#maxess-results-10.v13-active .v13-hero-actions{display:flex;justify-content:center;gap:12px;margin-top:30px}
#maxess-results-10.v13-active .v13-btn{min-height:52px;padding:0 20px;border-radius:15px;border:1px solid rgba(255,255,255,.15);font-weight:850;text-decoration:none;display:inline-flex;align-items:center;justify-content:center;cursor:pointer}
#maxess-results-10.v13-active .v13-btn-primary{background:linear-gradient(135deg,#c99cff,#7438d3 52%,#3b126f);color:#fff;box-shadow:0 14px 38px rgba(103,47,180,.28),inset 0 1px rgba(255,255,255,.55)}
#maxess-results-10.v13-active .v13-btn-ghost{background:rgba(255,255,255,.055);color:#fff}
@keyframes v13Orb{0%,100%{transform:scale(1);filter:saturate(1)}50%{transform:scale(1.018);filter:saturate(1.22) brightness(1.05)}}
@keyframes v13Spin{to{transform:rotate(360deg)}}@keyframes v13SpinReverse{to{transform:rotate(-360deg)}}

/* NAYA: personal guide, immediately after the user's score */
#maxess-results-10.v13-active .v13-naya{padding:68px 0;background:#fff;color:#111}
#maxess-results-10.v13-active .v13-naya-card{display:grid;grid-template-columns:150px minmax(0,1fr) auto;gap:30px;align-items:center;padding:28px;border:1px solid rgba(0,0,0,.09);border-radius:32px;background:linear-gradient(110deg,#fff,#f7f2fc 64%,#effaf8);box-shadow:0 30px 90px rgba(30,10,55,.12)}
#maxess-results-10.v13-active .v13-naya-photo{width:150px;height:150px;border-radius:50%;object-fit:cover;object-position:center;border:4px solid #fff;box-shadow:0 0 0 7px rgba(139,77,255,.1),0 18px 40px rgba(0,0,0,.18)}
#maxess-results-10.v13-active .v13-naya-kicker{font-size:10px;font-weight:950;letter-spacing:.18em;color:#7042aa;text-transform:uppercase}
#maxess-results-10.v13-active .v13-naya h2{margin:7px 0 0;font-size:clamp(28px,3.4vw,48px);line-height:.98;letter-spacing:-.055em}
#maxess-results-10.v13-active .v13-naya p{max-width:720px;margin:12px 0 0;color:#4c4c4c;font-size:15px;line-height:1.55}
#maxess-results-10.v13-active .v13-naya .v13-btn{background:#111;color:#fff;border:0;white-space:nowrap}

/* REPORT CHAPTER: one idea per screen */
#maxess-results-10.v13-active .v13-report{padding:92px 0;background:#fff;color:#111}
#maxess-results-10.v13-active .v13-report-head{display:grid;grid-template-columns:minmax(0,1fr) minmax(300px,.55fr);gap:60px;align-items:end}
#maxess-results-10.v13-active .v13-report .v13-chapter{color:#777}
#maxess-results-10.v13-active .v13-report .v13-chapter i{border-color:#ddd;background:#f7f2ff;color:#7042aa}
#maxess-results-10.v13-active .v13-report .v13-sub{color:#555}
#maxess-results-10.v13-active .v13-report-quote{margin-top:58px;padding:42px 0 0;border-top:1px solid #ddd;font-size:clamp(28px,4vw,60px);line-height:1.02;letter-spacing:-.055em;max-width:1100px}
#maxess-results-10.v13-active .v13-report-quote em{font-style:normal;color:#7042aa}

/* DIMENSIONS: large circular instruments */
#maxess-results-10.v13-active .v13-dimensions{padding:94px 0;background:linear-gradient(180deg,#050507,#0c0714);color:#fff}
#maxess-results-10.v13-active .v13-dim-head{display:flex;justify-content:space-between;gap:30px;align-items:end;margin-bottom:38px}
#maxess-results-10.v13-active .v13-dim-head p{max-width:520px;color:rgba(255,255,255,.52);margin:0;line-height:1.55}
#maxess-results-10.v13-active .v13-dim-grid{display:grid;grid-template-columns:repeat(5,minmax(145px,1fr));gap:16px}
#maxess-results-10.v13-active .v13-dim{position:relative;min-height:370px;padding:26px 18px 22px;border-radius:30px;background:linear-gradient(155deg,#0c0b11,#171020);border:1px solid rgba(255,255,255,.12);display:flex;flex-direction:column;align-items:center;text-align:center;overflow:hidden;box-shadow:inset 0 1px rgba(255,255,255,.09),0 28px 75px rgba(0,0,0,.34)}
#maxess-results-10.v13-active .v13-ring{width:188px;height:188px;border-radius:50%;display:grid;place-items:center;background:conic-gradient(var(--g) calc(var(--score)*1%),rgba(255,255,255,.07) 0);filter:drop-shadow(0 0 18px color-mix(in srgb,var(--g) 27%,transparent));position:relative}
#maxess-results-10.v13-active .v13-ring:after{content:"";position:absolute;inset:13px;border-radius:50%;background:#09090e;box-shadow:inset 0 0 35px rgba(0,0,0,.8)}
#maxess-results-10.v13-active .v13-ring b{position:relative;z-index:2;font-size:52px;letter-spacing:-.07em;line-height:1;color:var(--g)}
#maxess-results-10.v13-active .v13-dim h3{margin:22px 0 0;font-size:17px}
#maxess-results-10.v13-active .v13-dim p{margin:9px 0 0;color:rgba(255,255,255,.54);font-size:12px;line-height:1.45}
#maxess-results-10.v13-active .v13-lever{margin-top:auto;width:100%;padding-top:13px;border-top:1px solid rgba(255,255,255,.09);color:var(--g);font-size:9px;font-weight:950;letter-spacing:.15em;text-transform:uppercase}

/* PATTERN: connect the five dimensions visually */
#maxess-results-10.v13-active .v13-pattern{padding:94px 0;background:#fff;color:#111}
#maxess-results-10.v13-active .v13-pattern .v13-chapter{color:#777}.v13-pattern .v13-chapter i{background:#f7f2ff;border-color:#ddd;color:#7042aa}
#maxess-results-10.v13-active .v13-pattern p{color:#555}
#maxess-results-10.v13-active .v13-pattern-map{position:relative;display:grid;grid-template-columns:repeat(5,1fr);gap:22px;margin-top:54px;padding:35px 0}
#maxess-results-10.v13-active .v13-pattern-map:before{content:"";position:absolute;left:7%;right:7%;top:50%;height:2px;background:linear-gradient(90deg,#ff9638,#ffd447,#36dd91,#45a4ff,#8b4dff);opacity:.55}
#maxess-results-10.v13-active .v13-node{position:relative;z-index:2;aspect-ratio:1;border-radius:50%;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;background:radial-gradient(circle at 35% 22%,#fff,#f5f1fa 42%,#e7e1ef 100%);border:1px solid #d8d0e1;box-shadow:0 25px 55px rgba(45,20,65,.13)}
#maxess-results-10.v13-active .v13-node b{font-size:12px;line-height:1.15}.v13-node strong{margin-top:9px;font-size:38px;line-height:1;letter-spacing:-.06em}.v13-node small{margin-top:7px;color:#777;font-size:8px;letter-spacing:.1em;text-transform:uppercase}

/* INSIGHT / LEVER: turn weakness into a visual opportunity */
#maxess-results-10.v13-active .v13-insight{padding:94px 0;background:linear-gradient(145deg,#5d2aa5,#2b1251 54%,#0a0710);color:#fff}
#maxess-results-10.v13-active .v13-insight-grid{display:grid;grid-template-columns:.8fr 1.2fr;gap:70px;align-items:center}
#maxess-results-10.v13-active .v13-lever-score{font-size:clamp(100px,13vw,190px);line-height:.75;letter-spacing:-.1em;font-weight:900;color:#fff}
#maxess-results-10.v13-active .v13-lever-score small{display:block;margin-top:30px;font-size:10px;line-height:1;letter-spacing:.2em;color:rgba(255,255,255,.5);text-transform:uppercase}
#maxess-results-10.v13-active .v13-insight h2{font-size:clamp(38px,5vw,72px);line-height:.92;letter-spacing:-.06em;margin:0}
#maxess-results-10.v13-active .v13-insight p{color:rgba(255,255,255,.68);font-size:16px;line-height:1.6;max-width:700px}
#maxess-results-10.v13-active .v13-before-after{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-top:28px}
#maxess-results-10.v13-active .v13-ba{padding:22px;border-radius:22px;border:1px solid rgba(255,255,255,.14);background:rgba(0,0,0,.16)}
#maxess-results-10.v13-active .v13-ba b{display:block;font-size:9px;letter-spacing:.16em;color:rgba(255,255,255,.48)}.v13-ba span{display:block;margin-top:12px;font-size:15px;font-weight:800}.v13-ba small{display:block;margin-top:7px;color:rgba(255,255,255,.52);line-height:1.45}

/* NEXT MOVE: one clean journey */
#maxess-results-10.v13-active .v13-next{padding:94px 0;background:#050507;color:#fff}
#maxess-results-10.v13-active .v13-steps{display:grid;grid-template-columns:repeat(4,1fr);margin-top:44px;border:1px solid rgba(255,255,255,.12);border-radius:28px;overflow:hidden}
#maxess-results-10.v13-active .v13-step{min-height:220px;padding:27px;border-right:1px solid rgba(255,255,255,.1);background:linear-gradient(155deg,rgba(255,255,255,.065),rgba(255,255,255,.015))}.v13-step:last-child{border-right:0}
#maxess-results-10.v13-active .v13-step b{font-size:10px;letter-spacing:.18em;color:#cdb8ff}.v13-step h3{margin:14px 0 8px;font-size:21px}.v13-step p{margin:0;color:rgba(255,255,255,.5);font-size:12px;line-height:1.5}

/* 18 MASTERS: colorful but not cluttered */
#maxess-results-10.v13-active .v13-masters{padding:94px 0;background:#fff;color:#111}
#maxess-results-10.v13-active .v13-masters .v13-chapter{color:#777}.v13-masters .v13-chapter i{background:#f7f2ff;border-color:#ddd;color:#7042aa}
#maxess-results-10.v13-active .v13-masters p{color:#555}
#maxess-results-10.v13-active .v13-master-grid{display:grid;grid-template-columns:repeat(6,1fr);gap:12px;margin-top:42px}
#maxess-results-10.v13-active .v13-master{position:relative;min-height:148px;padding:18px;border-radius:22px;border:1px solid #ddd;background:linear-gradient(150deg,#fff,#f7f5fa);overflow:hidden}
#maxess-results-10.v13-active .v13-master:after{content:"";position:absolute;right:-30px;bottom:-35px;width:110px;height:110px;border-radius:50%;background:radial-gradient(circle,var(--g),transparent 68%);opacity:.23}
#maxess-results-10.v13-active .v13-master b{font-size:9px;letter-spacing:.15em;color:#999}.v13-master strong{display:block;margin-top:9px;font-size:14px}.v13-master span{display:block;margin-top:6px;color:#666;font-size:10px;line-height:1.35}

/* Preserve the original video/conversion content, but make the transition explicit. */
#maxess-results-10.v13-active .v13-video{padding:90px 0;background:#050507;color:#fff}
#maxess-results-10.v13-active .v13-video-frame{border-radius:30px;overflow:hidden;border:1px solid rgba(255,255,255,.12);box-shadow:0 35px 100px rgba(0,0,0,.5)}
#maxess-results-10.v13-active .v13-video-frame>*{width:100%!important}
#maxess-results-10.v13-active .v13-final{padding:90px 0 110px;background:linear-gradient(135deg,#fff,#f7f2fb);color:#111;text-align:center}
#maxess-results-10.v13-active .v13-final h2{font-size:clamp(42px,6vw,84px);line-height:.9;letter-spacing:-.07em;margin:0 auto;max-width:900px}.v13-final p{max-width:620px;margin:18px auto 28px;color:#555;line-height:1.55}
#maxess-results-10.v13-active .v13-original{display:none!important}

/* responsive */
@media(max-width:1120px){#maxess-results-10.v13-active .v13-dim-grid{grid-template-columns:repeat(3,1fr)}#maxess-results-10.v13-active .v13-master-grid{grid-template-columns:repeat(4,1fr)}#maxess-results-10.v13-active .v13-report-head,#maxess-results-10.v13-active .v13-insight-grid{grid-template-columns:1fr;gap:28px}}
@media(max-width:760px){#maxess-results-10.v13-active .v13-wrap{width:min(100% - 28px,1580px)}#maxess-results-10.v13-active .v13-hero{min-height:auto;padding:90px 0 70px}#maxess-results-10.v13-active .v13-score-orb{width:min(470px,88vw);margin-top:30px}#maxess-results-10.v13-active .v13-hero-tools{top:12px;right:12px}.v13-tool{padding:9px 11px!important;font-size:11px}#maxess-results-10.v13-active .v13-naya-card{grid-template-columns:76px 1fr;gap:18px;padding:20px}.v13-naya-photo{width:76px!important;height:76px!important}.v13-naya .v13-btn{grid-column:1/-1;width:100%}#maxess-results-10.v13-active .v13-dim-grid{grid-template-columns:1fr 1fr}#maxess-results-10.v13-active .v13-pattern-map{grid-template-columns:repeat(2,1fr)}#maxess-results-10.v13-active .v13-pattern-map:before{display:none}#maxess-results-10.v13-active .v13-node:last-child{grid-column:1/-1;max-width:48%;margin:auto}#maxess-results-10.v13-active .v13-before-after{grid-template-columns:1fr}#maxess-results-10.v13-active .v13-steps{grid-template-columns:1fr}#maxess-results-10.v13-active .v13-step{border-right:0;border-bottom:1px solid rgba(255,255,255,.1)}#maxess-results-10.v13-active .v13-master-grid{grid-template-columns:repeat(2,1fr)}}
@media(max-width:480px){#maxess-results-10.v13-active .v13-dim-grid{grid-template-columns:1fr}#maxess-results-10.v13-active .v13-master-grid{grid-template-columns:1fr}#maxess-results-10.v13-active .v13-hero-actions{flex-direction:column;width:100%}#maxess-results-10.v13-active .v13-btn{width:100%}}
@media(prefers-reduced-motion:reduce){#maxess-results-10.v13-active .v13-score-orb,#maxess-results-10.v13-active .v13-score-orb:before,#maxess-results-10.v13-active .v13-score-orb:after{animation:none!important}}
@media print{#maxess-results-10.v13-active{background:#fff!important;color:#111!important}#maxess-results-10.v13-active .v13-shell{background:#fff!important;color:#111!important}#maxess-results-10.v13-active .v13-hero,#maxess-results-10.v13-active .v13-dimensions,#maxess-results-10.v13-active .v13-next,#maxess-results-10.v13-active .v13-video{background:#fff!important;color:#111!important}#maxess-results-10.v13-active .v13-hero-tools,#maxess-results-10.v13-active .v13-hero-actions{display:none!important}#maxess-results-10.v13-active .v13-score-orb{width:250px!important;box-shadow:none!important;background:#f2f2f4!important;animation:none!important}#maxess-results-10.v13-active .v13-score-number{font-size:95px!important;background:none!important;color:#111!important;-webkit-text-fill-color:#111!important}#maxess-results-10.v13-active .v13-naya-card,#maxess-results-10.v13-active .v13-dim,#maxess-results-10.v13-active .v13-node,#maxess-results-10.v13-active .v13-master,#maxess-results-10.v13-active .v13-step{break-inside:avoid;box-shadow:none!important}#maxess-results-10.v13-active .v13-final{background:#fff!important}#maxess-results-10.v13-active .v13-original{display:none!important}}
</style>'''

JS = r'''<script id="maxess-results-v13-js">
(function(){
'use strict';
const root=document.getElementById('maxess-results-10');if(!root||root.dataset.v13==='1')return;root.dataset.v13='1';root.classList.add('v13-active');
const esc=s=>String(s??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const getResult=()=>window.MAXESS_RESULT||null;
const getScore=()=>{const r=getResult();const n=Number(r?.overallScore??r?.score??r?.masterScore);return Number.isFinite(n)?Math.max(0,Math.min(100,n)):null};
const getDims=()=>{const r=getResult();return Array.isArray(r?.dimensions)?r.dimensions.slice(0,5).map((d,i)=>({name:d.name||d.label||`Dimension ${i+1}`,score:Math.max(0,Math.min(100,Number(d.score??d.value??0)||0)),insight:d.description||d.insight||''})):[]};
const colors=['#ff9638','#ffd447','#36dd91','#45a4ff','#8b4dff'];
const scoreColors=s=>s<50?['#ff4c55','#ff9638']:s<65?['#ff9638','#ffd447']:s<75?['#ffd447','#36dd91']:s<85?['#36dd91','#45a4ff']:s<90?['#45a4ff','#45a4ff']:s<95?['#45a4ff','#8b4dff']:['#8b4dff','#ee43c8'];
const copyFor=(n,s)=>{const x=n.toLowerCase();if(x.includes('communication'))return'You can express intent, context and outcomes clearly. That is a powerful foundation for working with AI.';if(x.includes('direction'))return'You know where you are trying to go. Clear outcomes give AI a better route to follow.';if(x.includes('evaluation'))return'You can judge useful work from merely impressive work. That is how quality compounds.';if(x.includes('iteration'))return'You are building the habit of improving instead of settling for the first answer.';if(x.includes('system'))return'You have an opportunity to turn repeated effort into reusable leverage.';return s>=85?'A strength you can compound.':s>=70?'A capable area ready for another level.':'A focused opportunity for growth.'};
const leverFor=(n,s)=>{const x=n.toLowerCase();if(x.includes('communication'))return'Create reusable briefs';if(x.includes('direction'))return'Define the outcome first';if(x.includes('evaluation'))return'Score every important output';if(x.includes('iteration'))return'Build an improvement loop';if(x.includes('system'))return'Turn repetition into a system';return s>=85?'Compound this strength':'Practice this deliberately'};
const nayaImg='https://i.postimg.cc/d1nncN9F/Naya-and-shawn-ok-44-a.png';
function findSection(...words){return [...root.querySelectorAll('section')].find(s=>{const t=(s.textContent||'').toLowerCase();return words.some(w=>t.includes(w))})}
function findVideo(){return [...root.querySelectorAll('section')].find(s=>s.querySelector('iframe,video'))}
function findConversion(){const arr=[...root.querySelectorAll('section')];return arr.reverse().find(s=>{const t=(s.textContent||'').toLowerCase();return t.includes('get started')||t.includes('take action')||t.includes('learn ai')||t.includes('your ai path')})}
function scoreHero(){const s=getScore();if(s===null)return;const [a,b]=scoreColors(s);const label=s>=90?'Exceptional':s>=75?'Advancing':s>=60?'Building':'Beginning';return `<section class="v13-hero" id="v13-score"><div class="v13-hero-tools"><button class="v13-tool" id="v13-print" type="button">Print / Save PDF</button></div><div class="v13-wrap v13-hero-inner"><div class="v13-overline">MAXESS AI MASTERY ASSESSMENT</div><div class="v13-score-label">YOUR AI SCORE</div><div class="v13-score-orb" style="--a:${a};--b:${b}" role="img" aria-label="Your AI score is ${Math.round(s)} out of 100"><div class="v13-score-number">${Math.round(s)}</div><div class="v13-score-caption">OUT OF 100</div></div><div class="v13-band">${label}</div><div class="v13-hero-actions"><a class="v13-btn v13-btn-primary" href="#v13-report">See Your Results ↓</a></div></div></section>`}
function nayaBlock(){return `<section class="v13-naya" id="v13-naya"><div class="v13-wrap"><div class="v13-naya-card"><img class="v13-naya-photo" src="${nayaImg}" alt="Naya, your AI guide"><div><div class="v13-naya-kicker">NAYA · YOUR AI GUIDE</div><h2>Hi. I'm Naya. Let me walk you through your report.</h2><p>This isn't a generic AI score. It's a picture of how you work with AI right now. I'll help you see what is already strong, where your biggest leverage is, and what to do next.</p></div><button class="v13-btn" id="v13-listen" type="button">Listen to Naya ▶</button></div></div></section>`}
function reportBlock(){const s=getScore()??0;return `<section class="v13-report" id="v13-report"><div class="v13-wrap"><div class="v13-report-head"><div><div class="v13-chapter"><i>02</i> YOUR REPORT</div><h2 class="v13-h2">Your score is the beginning. Your report is the meaning.</h2></div><p class="v13-sub">See the story behind the number — what you already have, what matters most, and where one improvement can change everything.</p></div><div class="v13-report-quote">You are not trying to become “good at AI.” You are learning how to make <em>AI work better for you.</em></div></div></section>`}
function dimensionsBlock(ds){return `<section class="v13-dimensions" id="v13-dimensions"><div class="v13-wrap"><div class="v13-dim-head"><div><div class="v13-chapter"><i>03</i> YOUR FIVE DIMENSIONS</div><h2 class="v13-h2">Your capability has shape.</h2></div><p>Five capabilities show where your AI practice is strong, developing, and ready for leverage. Scan the circles first. Read the detail second.</p></div><div class="v13-dim-grid">${ds.map((d,i)=>`<article class="v13-dim"><div class="v13-ring" style="--score:${d.score};--g:${colors[i]}"><b>${Math.round(d.score)}</b></div><h3>${esc(d.name)}</h3><p>${esc(d.insight||copyFor(d.name,d.score))}</p><div class="v13-lever">LEVER · ${esc(leverFor(d.name,d.score))}</div></article>`).join('')}</div></div></section>`}
function patternBlock(ds){return `<section class="v13-pattern" id="v13-pattern"><div class="v13-wrap"><div class="v13-chapter"><i>04</i> YOUR PATTERN</div><div class="v13-report-head"><h2 class="v13-h2">See the pattern.</h2><p class="v13-sub">Your dimensions are not five separate scores. Together they describe how you naturally work with AI.</p></div><div class="v13-pattern-map">${ds.map((d,i)=>`<div class="v13-node"><b>${esc(d.name)}</b><strong>${Math.round(d.score)}</strong><small>${['Direct','Express','Judge','Improve','Connect'][i]||'Build'}</small></div>`).join('')}</div></div></section>`}
function strengthsBlock(ds){const top=[...ds].sort((a,b)=>b.score-a.score)[0]||{name:'Your strengths',score:getScore()??0};return `<section class="v13-report" id="v13-strengths"><div class="v13-wrap"><div class="v13-chapter"><i>05</i> YOUR STRENGTH</div><div class="v13-report-head"><div><h2 class="v13-h2">Start with what you already do well.</h2></div><p class="v13-sub">${esc(top.name)} is currently your strongest visible dimension at ${Math.round(top.score)}. Don't merely admire it — use it as the foundation for everything else.</p></div><div class="v13-report-quote"><em>${Math.round(top.score)}</em> in ${esc(top.name)} is something to build on.</div></div></section>`}
function leverBlock(ds){const low=[...ds].sort((a,b)=>a.score-b.score)[0]||{name:'Your next lever',score:0};return `<section class="v13-insight" id="v13-lever"><div class="v13-wrap"><div class="v13-insight-grid"><div><div class="v13-chapter"><i>06</i> YOUR BIGGEST LEVER</div><div class="v13-lever-score">${Math.round(low.score)}<small>${esc(low.name)}</small></div></div><div><h2>Turn the gap into leverage.</h2><p>${esc(low.name)} is not a weakness to be embarrassed by. It is the clearest place where focused improvement can create a return across the rest of your AI practice.</p><div class="v13-before-after"><div class="v13-ba"><b>BEFORE</b><span>More effort than necessary</span><small>Repeated work, unclear handoffs, or inconsistent results.</small></div><div class="v13-ba"><b>AFTER</b><span>Reusable advantage</span><small>A deliberate process that makes better results easier to repeat.</small></div></div></div></div></div></section>`}
function nextBlock(){return `<section class="v13-next" id="v13-next"><div class="v13-wrap"><div class="v13-chapter"><i>07</i> YOUR NEXT MOVE</div><h2 class="v13-h2">One clear path forward.</h2><div class="v13-steps"><div class="v13-step"><b>01 · KNOW</b><h3>Know the outcome</h3><p>Decide what “better” actually means before asking AI to act.</p></div><div class="v13-step"><b>02 · TELL</b><h3>Give it the context</h3><p>Share the information, constraints and standards that matter.</p></div><div class="v13-step"><b>03 · CREATE</b><h3>Make the first version</h3><p>Let AI produce something real enough to judge.</p></div><div class="v13-step"><b>04 · SCORE</b><h3>Verify the outcome</h3><p>Check the actual result. Improve it. Repeat until it earns the score.</p></div></div></div></section>`}
function mastersBlock(){const names=['Writing & Communication','Research & Information','Brainstorming & Ideas','Content Creation','Business & Strategy','Marketing & Sales','Learning & Education','Coding & Software','Images & Visual Creation','Video & Media','Audio & Music','Data & Analysis','Productivity & Organization','Career & Professional Growth','Decision Making','Creative Development','Systems & Automation','AI Orchestration'];const benefits=['Write clearly.','Find the signal.','Generate better possibilities.','Create content faster.','Think strategically.','Turn value into action.','Learn intelligently.','Build and debug.','Make ideas visible.','Create media.','Shape sound.','Work with evidence.','Organize execution.','Build capability.','Choose with clarity.','Create original work.','Build reusable systems.','Coordinate AI at scale.'];return `<section class="v13-masters" id="v13-masters"><div class="v13-wrap"><div class="v13-chapter"><i>08</i> YOUR NAYA MASTERS</div><div class="v13-report-head"><h2 class="v13-h2">18 specialist paths. One personalized direction.</h2><p class="v13-sub">Your report points toward the areas where specialized AI help can turn capability into real-world results.</p></div><div class="v13-master-grid">${names.map((n,i)=>`<article class="v13-master" style="--g:${colors[i%colors.length]}"><b>${String(i+1).padStart(2,'0')}</b><strong>Naya ${esc(n)}</strong><span>${benefits[i]}</span></article>`).join('')}</div></div></section>`}
function preserveMedia(){const video=findVideo();const conversion=findConversion();let media='';if(video){const clone=video.cloneNode(true);clone.classList.add('v13-video-frame');clone.classList.add('v13-original-preserved');media=`<section class="v13-video" id="v13-video"><div class="v13-wrap"><div class="v13-chapter"><i>09</i> THE SYSTEM</div><h2 class="v13-h2">Now turn insight into action.</h2><div class="v13-video-frame">${clone.innerHTML}</div></div></section>`}let final='<section class="v13-final" id="v13-final"><div class="v13-wrap"><div class="v13-chapter" style="justify-content:center;color:#777"><i style="background:#fff;border-color:#ddd;color:#7042aa">10</i> YOUR NEXT CHAPTER</div><h2>Understand your result. Then master it.</h2><p>Your score is not the destination. It is your starting point.</p><a class="v13-btn v13-btn-primary" href="#v13-masters" style="background:#111;color:#fff">Explore Your Naya Masters ↓</a></div></section>';if(conversion){const clone=conversion.cloneNode(true);clone.classList.add('v13-original-preserved');final=`<section class="v13-final" id="v13-final"><div class="v13-wrap"><div class="v13-chapter" style="justify-content:center;color:#777"><i style="background:#fff;border-color:#ddd;color:#7042aa">10</i> YOUR NEXT CHAPTER</div><h2>Understand your result. Then master it.</h2><p>Your report has shown you where you are. Now choose what you want to build next.</p><div class="v13-preserved-cta">${clone.innerHTML}</div></div></section>`}return media+final}
function build(){const s=getScore();if(s===null)return false;const ds=getDims();if(ds.length!==5)return false;const shell=document.createElement('div');shell.className='v13-shell';shell.innerHTML=scoreHero()+nayaBlock()+reportBlock()+dimensionsBlock(ds)+patternBlock(ds)+strengthsBlock(ds)+leverBlock(ds)+nextBlock()+mastersBlock()+preserveMedia();const original=[...root.children];original.forEach(el=>{if(el.tagName==='SCRIPT'||el.tagName==='STYLE')return;if(el.id==='maxess-v13')return;el.classList.add('v13-original')});root.insertBefore(shell,root.firstElementChild);root.querySelector('#v13-print').onclick=()=>window.print();const listen=root.querySelector('#v13-listen');if(listen)listen.onclick=()=>{const candidates=[...root.querySelectorAll('button,a')];const b=candidates.find(x=>/listen|naya/i.test(x.textContent||''));if(b&&b!==listen)b.click();else root.dispatchEvent(new CustomEvent('maxess:naya-listen',{bubbles:true}))};return true}
let attempts=0;function start(){if(root.dataset.v13Built==='1')return;if(build()){root.dataset.v13Built='1';return}if(++attempts<80)setTimeout(start,150)}
if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',start,{once:true});else start();window.addEventListener('maxess:result-ready',start);
})();
</script>'''

def execute():
    if not TARGET.exists(): raise SystemExit('BLOCKED — authoritative artifact missing')
    source=TARGET.read_text(encoding='utf-8')
    if MARKER in source: raise SystemExit('BLOCKED — V13 already executed')
    if 'window.MAXESS_RESULT' not in source or 'id="maxess-results-10"' not in source: raise SystemExit('BLOCKED — result contract/root missing')
    if '</head>' not in source or '</body>' not in source: raise SystemExit('BLOCKED — malformed artifact')
    before=len(source)
    out=source.replace('</head>',CSS+'\n</head>',1).replace('</body>',JS+'\n</body>',1).replace('</html>',MARKER+'\n</html>',1)
    if len(out)<=before: raise SystemExit('BLOCKED — ZERO-CHANGE EXECUTION')
    TARGET.write_text(out,encoding='utf-8')
    print(f'V13 visible execution: {before} -> {len(out)} bytes; +{len(out)-before} bytes')

if __name__=='__main__': execute()
