#!/usr/bin/env python3
"""MAXESS Results V12 — section-by-section execution engine.

This pass fixes the failure of V11: V11 was primarily a CSS/runtime overlay.
V12 makes the visual story explicit, removes competing early content, creates a
score-first hero, introduces Naya as the report guide, and rebuilds the report
rhythm from the real MAXESS_RESULT contract. It remains inside the authoritative
Groove artifact and never changes scoring.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TARGET = ROOT / "MAXESS-RESULTS-10-GROOVE.html"
MARKER = "<!-- MAXESS_RESULTS_V12_SECTION_EXECUTION -->"

CSS = r'''<style id="maxess-results-v12-css">
/* MAXESS V12 — intentional editorial system */
#maxess-results-10.v12-results{
  --v12-bg:#050507;--v12-ink:#fff;--v12-soft:rgba(255,255,255,.70);--v12-muted:rgba(255,255,255,.46);
  --v12-purple:#965dff;--v12-magenta:#ef4bc8;--v12-blue:#4c9dff;--v12-teal:#39d9cc;--v12-green:#39df91;
  --v12-yellow:#ffd84a;--v12-orange:#ff9d3d;--v12-red:#ff4b55;--v12-max:1680px;
  width:100vw!important;max-width:none!important;margin-left:calc(50% - 50vw)!important;margin-right:calc(50% - 50vw)!important;
  background:#050507!important;color:var(--v12-ink)!important;overflow-x:clip!important;
}
#maxess-results-10.v12-results .mx-section{padding:clamp(56px,6vw,96px) clamp(20px,4vw,72px)!important}
#maxess-results-10.v12-results .mx-wide{width:min(var(--v12-max),100%)!important;margin-inline:auto!important}
#maxess-results-10.v12-results .mx-section-head{margin-bottom:30px!important;align-items:end!important}
#maxess-results-10.v12-results .mx-section-head h2{font-size:clamp(34px,4.8vw,68px)!important;letter-spacing:-.055em!important;line-height:.94!important}
#maxess-results-10.v12-results .mx-section-head p{max-width:560px!important;font-size:15px!important;line-height:1.55!important}

/* 01 — score is the first thing the eye sees */
#maxess-results-10.v12-results .mx-hero{min-height:min(880px,94vh)!important;padding:58px 20px 70px!important;display:grid!important;place-items:center!important;background:
 radial-gradient(circle at 50% 44%,rgba(150,93,255,.20),transparent 30%),radial-gradient(circle at 20% 70%,rgba(57,217,204,.06),transparent 30%),linear-gradient(180deg,#020205,#09050d 70%,#050507)!important}
#maxess-results-10.v12-results .mx-hero-grid{display:flex!important;flex-direction:column!important;align-items:center!important;gap:26px!important;width:min(980px,100%)!important;text-align:center!important}
#maxess-results-10.v12-results .mx-hero-grid>div:first-child{order:1!important;display:flex!important;flex-direction:column!important;align-items:center!important;max-width:900px!important}
#maxess-results-10.v12-results .mx-hero-grid>.mx-score-orb{order:2!important;width:min(620px,78vw)!important;min-width:300px!important;margin:0 auto!important}
#maxess-results-10.v12-results .mx-hero .mx-eyebrow{font-size:11px!important;letter-spacing:.22em!important;color:rgba(255,255,255,.50)!important}
#maxess-results-10.v12-results .mx-hero .mx-title{font-size:clamp(46px,6.5vw,94px)!important;line-height:.88!important;letter-spacing:-.07em!important;margin:10px 0 0!important;color:#fff!important}
#maxess-results-10.v12-results .mx-hero .mx-title em{display:none!important}
#maxess-results-10.v12-results .mx-hero .mx-copy,#maxess-results-10.v12-results .mx-hero .mx-proof,#maxess-results-10.v12-results .hero-score-whisper{display:none!important}
#maxess-results-10.v12-results .mx-hero .mx-score-orb{--v12-a:#39df91;--v12-b:#4c9dff;background:radial-gradient(circle at 31% 23%,rgba(255,255,255,.30),transparent 10%),radial-gradient(circle at 50% 48%,color-mix(in srgb,var(--v12-a) 28%,transparent),color-mix(in srgb,var(--v12-b) 18%,transparent) 32%,#0b0910 70%,#020205 100%)!important;border:1px solid color-mix(in srgb,var(--v12-b) 65%,white 8%)!important;box-shadow:0 0 0 1px rgba(255,255,255,.12),inset 0 0 120px color-mix(in srgb,var(--v12-a) 28%,transparent),0 45px 130px rgba(0,0,0,.75),0 0 170px color-mix(in srgb,var(--v12-a) 22%,transparent)!important;animation:v12Orb 5.5s ease-in-out infinite!important}
#maxess-results-10.v12-results .mx-score-orb::before{border-color:color-mix(in srgb,var(--v12-b) 70%,white 10%)!important;box-shadow:0 0 70px color-mix(in srgb,var(--v12-a) 32%,transparent)!important;animation:v12Ring 18s linear infinite!important}
#maxess-results-10.v12-results .mx-score-orb::after{border-color:color-mix(in srgb,var(--v12-b) 35%,white 5%)!important;animation:v12RingReverse 26s linear infinite!important}
#maxess-results-10.v12-results .mx-score strong{font-size:clamp(116px,15vw,210px)!important;line-height:.78!important;background:linear-gradient(110deg,var(--v12-a),var(--v12-b),var(--v12-magenta))!important;-webkit-background-clip:text!important;background-clip:text!important;color:transparent!important;text-shadow:none!important}
#maxess-results-10.v12-results .mx-score span{margin-top:28px!important;color:rgba(255,255,255,.78)!important;letter-spacing:.25em!important}
#maxess-results-10.v12-results .mx-band{display:none!important}
#maxess-results-10.v12-results .mx-hero-actions{order:3!important;margin-top:0!important;justify-content:center!important}
#maxess-results-10.v12-results .mx-hero .mx-cta-ghost{display:none!important}
#maxess-results-10.v12-results .v12-print{position:absolute;right:clamp(18px,4vw,70px);top:22px;z-index:5}
#maxess-results-10.v12-results .v12-print button{border:1px solid rgba(255,255,255,.18);background:rgba(255,255,255,.06);color:#fff;border-radius:13px;padding:11px 15px;font-weight:800;cursor:pointer;backdrop-filter:blur(14px)}
@keyframes v12Orb{0%,100%{transform:scale(1);filter:saturate(1)}50%{transform:scale(1.022);filter:saturate(1.22) brightness(1.06)}}
@keyframes v12Ring{to{transform:rotate(360deg)}}@keyframes v12RingReverse{to{transform:rotate(-360deg)}}

/* 02 — Naya is a guide, not an advertisement */
#maxess-results-10.v12-results .v12-naya-intro{width:min(1120px,calc(100% - 32px));margin:0 auto 8px;display:grid;grid-template-columns:112px 1fr auto;gap:24px;align-items:center;padding:24px 28px;border-radius:30px;background:linear-gradient(105deg,#fff,#f7f3fc 65%,#f0f9f8);color:#111;border:1px solid rgba(0,0,0,.08);box-shadow:0 25px 80px rgba(0,0,0,.16)}
#maxess-results-10.v12-results .v12-naya-intro img{width:112px;height:112px;border-radius:50%;object-fit:cover;border:3px solid #fff;box-shadow:0 0 0 7px rgba(150,93,255,.10),0 15px 35px rgba(0,0,0,.18)}
#maxess-results-10.v12-results .v12-naya-kicker{font-size:10px;font-weight:950;letter-spacing:.18em;color:#7042aa;text-transform:uppercase}
#maxess-results-10.v12-results .v12-naya-title{margin:6px 0 0;font-size:clamp(24px,3vw,40px);line-height:1;letter-spacing:-.045em;font-weight:850}
#maxess-results-10.v12-results .v12-naya-copy{margin:10px 0 0;color:#444;font-size:15px;line-height:1.55;max-width:720px}
#maxess-results-10.v12-results .v12-naya-intro .mx-cta{white-space:nowrap;background:linear-gradient(135deg,#7c43d8,#4b1c89)!important;border:0!important}

/* editorial rhythm: black / white / black / white */
#maxess-results-10.v12-results .v12-light{background:#fff!important;color:#111!important}
#maxess-results-10.v12-results .v12-light .mx-section-head h2{color:#111!important}
#maxess-results-10.v12-results .v12-light .mx-section-head p{color:#444!important}
#maxess-results-10.v12-results .v12-dark{background:linear-gradient(180deg,#050507,#100817)!important}
#maxess-results-10.v12-results .v12-chapter{display:flex;align-items:center;gap:12px;margin-bottom:18px}
#maxess-results-10.v12-results .v12-chapter b{display:grid;place-items:center;width:38px;height:38px;border-radius:50%;font-size:10px;letter-spacing:.08em;border:1px solid rgba(150,93,255,.28);background:rgba(150,93,255,.08);color:#cbb1ff}
#maxess-results-10.v12-results .v12-chapter span{font-size:9px;font-weight:950;letter-spacing:.18em;color:rgba(255,255,255,.45);text-transform:uppercase}
#maxess-results-10.v12-results .v12-light .v12-chapter span{color:#666}

/* Dimensions — instruments, not five little boxes */
#maxess-results-10.v12-results .mx-dim-grid{grid-template-columns:repeat(5,minmax(145px,1fr))!important;gap:18px!important}
#maxess-results-10.v12-results .v12-dim{position:relative!important;min-height:340px!important;border-radius:30px!important;padding:24px 16px!important;display:flex!important;flex-direction:column!important;align-items:center!important;text-align:center!important;overflow:hidden!important;background:linear-gradient(160deg,#0b0a10,#15101c)!important;border:1px solid rgba(255,255,255,.12)!important;box-shadow:inset 0 1px rgba(255,255,255,.10),0 25px 75px rgba(0,0,0,.38)!important}
#maxess-results-10.v12-results .v12-dim::before{content:"";position:absolute;top:20px;left:50%;width:164px;height:164px;transform:translateX(-50%);border-radius:50%;background:conic-gradient(var(--v12-g) calc(var(--v12-score)*1%),rgba(255,255,255,.08) 0);filter:drop-shadow(0 0 18px color-mix(in srgb,var(--v12-g) 35%,transparent))}
#maxess-results-10.v12-results .v12-dim::after{content:"";position:absolute;top:33px;left:50%;width:138px;height:138px;transform:translateX(-50%);border-radius:50%;background:#08080d;box-shadow:inset 0 0 30px rgba(0,0,0,.8)}
#maxess-results-10.v12-results .v12-dim-head{position:relative;z-index:2;margin-top:58px;display:flex;flex-direction:column;gap:4px;align-items:center}
#maxess-results-10.v12-results .v12-dim-score{font-size:45px;font-weight:900;line-height:1;color:var(--v12-g)}
#maxess-results-10.v12-results .v12-dim-name{font-size:16px;font-weight:850}
#maxess-results-10.v12-results .v12-dim-desc{position:relative;z-index:2;margin:20px 0 0;color:rgba(255,255,255,.68);font-size:12px;line-height:1.45}
#maxess-results-10.v12-results .v12-dim-lever{position:relative;z-index:2;margin-top:auto;padding-top:13px;border-top:1px solid rgba(255,255,255,.08);width:100%;color:var(--v12-g);font-size:9px;font-weight:950;letter-spacing:.15em;text-transform:uppercase}

/* Pattern is a visual chapter */
#maxess-results-10.v12-results .v12-pattern{background:linear-gradient(180deg,#050507,#0d0716)!important}
#maxess-results-10.v12-results .v12-pattern-grid{position:relative;display:grid;grid-template-columns:repeat(5,1fr);gap:18px;padding:30px 0}
#maxess-results-10.v12-results .v12-pattern-grid::before{content:"";position:absolute;left:8%;right:8%;top:50%;height:2px;background:linear-gradient(90deg,transparent,#ff9d3d,#ffd84a,#39df91,#4c9dff,#965dff,transparent);opacity:.5;filter:blur(.2px)}
#maxess-results-10.v12-results .v12-pattern-node{position:relative;z-index:2;aspect-ratio:1;border-radius:50%;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;background:radial-gradient(circle at 35% 25%,rgba(255,255,255,.16),rgba(150,93,255,.08) 38%,#07070b 76%);border:1px solid rgba(255,255,255,.14);box-shadow:inset 0 1px rgba(255,255,255,.15),0 24px 65px rgba(0,0,0,.4)}
#maxess-results-10.v12-results .v12-pattern-node strong{font-size:36px;line-height:1;margin-top:8px}.v12-pattern-node b{font-size:12px;line-height:1.15}.v12-pattern-node small{margin-top:7px;color:rgba(255,255,255,.45);font-size:8px}

/* Narrative cards */
#maxess-results-10.v12-results .v12-story{display:grid;grid-template-columns:minmax(160px,.35fr) minmax(0,1fr);gap:28px;align-items:center;padding:32px;border-radius:30px;background:#fff;border:1px solid rgba(0,0,0,.09);box-shadow:0 25px 80px rgba(20,10,35,.10)}
#maxess-results-10.v12-results .v12-story-score{font-size:clamp(72px,9vw,130px);font-weight:900;letter-spacing:-.08em;line-height:.8;color:#111}.v12-story-score small{font-size:12px;letter-spacing:.12em;color:#7042aa;display:block;margin-top:20px}
#maxess-results-10.v12-results .v12-story h3{font-size:clamp(28px,3.8vw,54px);line-height:.98;letter-spacing:-.05em;margin:0;color:#111}.v12-story p{margin:14px 0 0;color:#444;line-height:1.6;max-width:760px}

/* Next move: one path, not four unrelated boxes */
#maxess-results-10.v12-results .v12-next-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:0;border:1px solid rgba(255,255,255,.12);border-radius:30px;overflow:hidden}
#maxess-results-10.v12-results .v12-next-step{min-height:220px;padding:26px 24px;background:linear-gradient(160deg,rgba(255,255,255,.06),rgba(255,255,255,.015));border-right:1px solid rgba(255,255,255,.09);position:relative}.v12-next-step:last-child{border-right:0}
#maxess-results-10.v12-results .v12-next-step b{font-size:10px;color:#cbb1ff;letter-spacing:.16em}.v12-next-step h3{margin:12px 0 8px;font-size:21px}.v12-next-step p{margin:0;color:rgba(255,255,255,.56);font-size:12px;line-height:1.5}

/* Masters — colorful, clean, scannable */
#maxess-results-10.v12-results .v12-masters-grid{display:grid;grid-template-columns:repeat(6,1fr);gap:12px}
#maxess-results-10.v12-results .v12-master{min-height:150px;padding:18px;border-radius:22px;border:1px solid rgba(255,255,255,.11);background:linear-gradient(145deg,rgba(255,255,255,.06),rgba(255,255,255,.015));position:relative;overflow:hidden}.v12-master::before{content:"";position:absolute;inset:auto -20px -35px auto;width:95px;height:95px;border-radius:50%;background:radial-gradient(circle,var(--v12-master-color),transparent 68%);opacity:.34}.v12-master b{position:relative;z-index:2;display:block;font-size:10px;color:rgba(255,255,255,.42);letter-spacing:.12em}.v12-master strong{position:relative;z-index:2;display:block;margin-top:8px;font-size:14px}.v12-master span{position:relative;z-index:2;display:block;margin-top:6px;color:rgba(255,255,255,.46);font-size:10px;line-height:1.35}

/* Remove commercial language from the report body; keep final conversion assets. */
#maxess-results-10.v12-results .v12-early-commercial{display:none!important}

/* PDF: readable, black-on-white, intentional breaks */
@media print{
 @page{size:letter;margin:.55in}
 #maxess-results-10.v12-results,#maxess-results-10.v12-results .mx-section{background:#fff!important;color:#111!important}
 #maxess-results-10.v12-results .v12-print,#maxess-results-10.v12-results .mx-hero-actions,#maxess-results-10.v12-results .mx-cta{display:none!important}
 #maxess-results-10.v12-results .mx-hero{min-height:auto!important;padding:10px 0 30px!important}
 #maxess-results-10.v12-results .mx-score-orb{width:250px!important;box-shadow:none!important;background:#f3f3f5!important;animation:none!important}
 #maxess-results-10.v12-results .mx-score strong{font-size:95px!important;background:none!important;color:#111!important;-webkit-text-fill-color:#111!important}
 #maxess-results-10.v12-results .v12-naya-intro,#maxess-results-10.v12-results .v12-story,#maxess-results-10.v12-results .v12-dim,#maxess-results-10.v12-results .v12-pattern-node,#maxess-results-10.v12-results .v12-master,#maxess-results-10.v12-results .v12-next-step{background:#fff!important;color:#111!important;box-shadow:none!important;border-color:#bbb!important;break-inside:avoid!important}
 #maxess-results-10.v12-results h1,#maxess-results-10.v12-results h2,#maxess-results-10.v12-results h3,#maxess-results-10.v12-results strong,#maxess-results-10.v12-results b{color:#111!important;-webkit-text-fill-color:#111!important}
 #maxess-results-10.v12-results p,#maxess-results-10.v12-results span,#maxess-results-10.v12-results small{color:#333!important}
}
@media(max-width:1100px){#maxess-results-10.v12-results .mx-dim-grid{grid-template-columns:repeat(3,1fr)!important}#maxess-results-10.v12-results .v12-masters-grid{grid-template-columns:repeat(4,1fr)}}
@media(max-width:760px){#maxess-results-10.v12-results .v12-naya-intro{grid-template-columns:78px 1fr}.v12-naya-intro img{width:78px!important;height:78px!important}.v12-naya-intro .mx-cta{grid-column:1/-1;width:100%}#maxess-results-10.v12-results .mx-dim-grid{grid-template-columns:1fr!important}.v12-pattern-grid{grid-template-columns:repeat(2,1fr)!important}.v12-pattern-node:last-child{grid-column:1/-1}.v12-next-grid{grid-template-columns:1fr!important}.v12-next-step{border-right:0!important;border-bottom:1px solid rgba(255,255,255,.09)}#maxess-results-10.v12-results .v12-masters-grid{grid-template-columns:repeat(2,1fr)}}
@media(prefers-reduced-motion:reduce){#maxess-results-10.v12-results .mx-score-orb,#maxess-results-10.v12-results .mx-score-orb::before,#maxess-results-10.v12-results .mx-score-orb::after{animation:none!important}}
</style>'''

JS = r'''<script id="maxess-results-v12-js">
(function(){
'use strict';
const root=document.getElementById('maxess-results-10');if(!root||root.dataset.v12==='1')return;root.dataset.v12='1';root.classList.add('v12-results');
const esc=s=>String(s??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const result=()=>window.MAXESS_RESULT||null;
const score=()=>{const r=result();const n=Number(r?.overallScore??r?.score??r?.masterScore);return Number.isFinite(n)?Math.max(0,Math.min(100,n)):null};
const dims=()=>{const r=result();return Array.isArray(r?.dimensions)?r.dimensions.slice(0,5).map((d,i)=>({name:d.name||d.label||`Dimension ${i+1}`,score:Number(d.score??d.value??0)||0,description:d.description||d.insight||''})):[]};
const colors=['#ff9d3d','#ffd84a','#39df91','#4c9dff','#965dff'];
const palette=s=>s<50?['#ff4b55','#ff9d3d']:s<65?['#ff9d3d','#ffd84a']:s<75?['#ffd84a','#39df91']:s<85?['#39df91','#4c9dff']:s<90?['#4c9dff','#4c9dff']:s<95?['#4c9dff','#965dff']:['#965dff','#ef4bc8'];
function allSections(){return [...root.querySelectorAll('section')]}
function find(...terms){return allSections().find(s=>{const t=(s.textContent||'').toLowerCase();return terms.some(x=>t.includes(x))})}
function removeNoise(){allSections().forEach(s=>{const t=(s.textContent||'').toLowerCase();if((t.includes('short version')&&t.includes('meaningful ai foundation'))||t.includes('technology should amplify your human')||t.includes('your ai capability has shape'))s.classList.add('v12-early-commercial')});}
function addPrint(){if(root.querySelector('.v12-print'))return;const b=document.createElement('div');b.className='v12-print';b.innerHTML='<button type="button" aria-label="Print or save this report as PDF">Print / Save PDF</button>';b.querySelector('button').onclick=()=>window.print();root.querySelector('.mx-hero')?.appendChild(b)}
function hero(){const h=root.querySelector('.mx-hero');if(!h)return;const s=score();const [a,b]=palette(s??82);const orb=h.querySelector('.mx-score-orb');if(orb){orb.style.setProperty('--v12-a',a);orb.style.setProperty('--v12-b',b);orb.setAttribute('aria-label',`Your AI score is ${Math.round(s??0)} out of 100`);const n=orb.querySelector('.mx-score strong');if(n)n.textContent=Math.round(s??0);const lab=orb.querySelector('.mx-score span');if(lab)lab.textContent='YOUR AI SCORE'}const title=h.querySelector('.mx-title');if(title)title.textContent='YOUR AI SCORE';const e=h.querySelector('.mx-eyebrow');if(e)e.textContent='MAXESS AI MASTERY ASSESSMENT';h.querySelectorAll('.mx-copy,.mx-proof,.hero-score-whisper,.mx-band').forEach(x=>x.remove());const actions=h.querySelector('.mx-hero-actions');if(actions){actions.innerHTML='<a class="mx-cta mx-cta-primary" href="#v12-report">See Your Results ↓</a>'}}
function naya(){if(root.querySelector('#v12-naya'))return;const hero=root.querySelector('.mx-hero');if(!hero)return;const s=score()??0;const box=document.createElement('section');box.id='v12-naya';box.className='mx-section';box.innerHTML=`<div class="v12-naya-intro"><img src="https://raw.githubusercontent.com/SoulSchoolAcademy/maxess/main/Naya%20Profile%20white.jpg" alt="Naya, your AI guide"><div><span class="v12-naya-kicker">NAYA · YOUR AI GUIDE</span><h2 class="v12-naya-title">Hi. I'm Naya. I'm here to help you understand your result.</h2><p class="v12-naya-copy">You just created a picture of how you work with AI. I'll walk you through what your score reveals, where your strengths are, and the one move that can create the most leverage next.</p></div><button class="mx-cta" type="button">Listen to Naya ▶</button></div>`;hero.insertAdjacentElement('afterend',box);box.querySelector('button').onclick=()=>root.querySelector('#mx-naya-listen')?.click()}
function chapter(sec,num,label,sub){const head=sec?.querySelector('.mx-section-head');if(!head||head.querySelector('.v12-chapter'))return;const c=document.createElement('div');c.className='v12-chapter';c.innerHTML=`<b>${num}</b><div><span>${label}</span><small>${sub}</small></div>`;head.prepend(c)}
function dimsBlock(sec){if(!sec)return;sec.id='v12-dimensions';const ds=dims();const grid=sec.querySelector('.mx-dim-grid');if(!grid||ds.length!==5)return;grid.innerHTML='';ds.forEach((d,i)=>{const card=document.createElement('article');card.className='v12-dim';card.style.setProperty('--v12-g',colors[i]);card.style.setProperty('--v12-score',Math.max(0,Math.min(100,d.score)));card.innerHTML=`<div class="v12-dim-head"><strong class="v12-dim-score">${Math.round(d.score)}</strong><span class="v12-dim-name">${esc(d.name)}</span></div><p class="v12-dim-desc">${esc(d.description||dimensionCopy(d.name,d.score))}</p><div class="v12-dim-lever">LEVER · ${esc(lever(d.name,d.score))}</div>`;grid.appendChild(card)});chapter(sec,'04','YOUR FIVE DIMENSIONS','Five capabilities. One connected profile.');const h=sec.querySelector('.mx-section-head h2');if(h)h.textContent='YOUR FIVE DIMENSIONS';const p=sec.querySelector('.mx-section-head p');if(p)p.textContent='See the five capabilities that shape how you work with AI.'}
function dimensionCopy(n,s){n=n.toLowerCase();if(n.includes('communication'))return'Express context, intent and the human outcome clearly.';if(n.includes('direction'))return'Know the destination before asking AI to build the route.';if(n.includes('evaluation'))return'Judge whether an answer is actually useful before accepting it.';if(n.includes('iteration'))return'Improve quality through deliberate cycles instead of one-shot prompting.';if(n.includes('system'))return'Turn repeated work into connected, reusable leverage.';return s>=85?'A strength you can compound.':s>=70?'A capable area ready to sharpen.':'A valuable area for focused growth.'}
function lever(n,s){n=n.toLowerCase();if(n.includes('communication'))return'REUSABLE BRIEFS';if(n.includes('direction'))return'DEFINE THE OUTCOME';if(n.includes('evaluation'))return'SCORE THE OUTPUT';if(n.includes('iteration'))return'IMPROVE DELIBERATELY';if(n.includes('system'))return'BUILD THE SYSTEM';return s>=85?'COMPOUND IT':'PRACTICE IT'}
function pattern(){if(root.querySelector('#v12-pattern'))return;const ds=dims();const anchor=root.querySelector('#v12-dimensions')||find('five dimensions');if(!anchor)return;const sec=document.createElement('section');sec.id='v12-pattern';sec.className='mx-section v12-pattern';sec.innerHTML=`<div class="mx-wide"><div class="mx-section-head"><div><div class="v12-chapter"><b>05</b><div><span>YOUR PATTERN</span><small>How your dimensions work together</small></div></div><h2>SEE THE PATTERN.</h2></div><p>Your scores are not five separate boxes. Together they form the shape of your AI working style.</p></div><div class="v12-pattern-grid">${ds.map((d,i)=>`<div class="v12-pattern-node"><b>${esc(d.name)}</b><strong>${Math.round(d.score)}</strong><small>${['Direct','Express','Judge','Improve','Connect'][i]||'Build'}</small></div>`).join('')}</div></div>`;anchor.insertAdjacentElement('afterend',sec)}
function report(){const sec=find('listen to your results','personalized report');if(!sec)return;sec.id='v12-report';sec.classList.add('v12-light');chapter(sec,'03','YOUR REPORT','Naya interprets what your result means');const h=sec.querySelector('.mx-section-head h2');if(h)h.textContent='YOUR REPORT';const p=sec.querySelector('.mx-section-head p');if(p)p.textContent='Your score is the beginning. Now turn it into understanding.'}
function story(sec,id,num,title){if(!sec)return;sec.id=id;sec.classList.add('v12-light');chapter(sec,num,title.toUpperCase(),'A clear interpretation of what your result means');const panel=sec.querySelector('.mx-panel');if(panel&&!panel.classList.contains('v12-story')){const s=score()??0;const old=panel.innerHTML;panel.innerHTML=`<div class="v12-story-score">${Math.round(s)}<small>MAXESS SCORE</small></div><div><h3>${title}</h3><p>${esc((old.replace(/\s+/g,' ').trim()).slice(0,420))}</p></div>`;panel.classList.add('v12-story')}}
function next(sec){if(!sec)return;sec.id='v12-next';sec.classList.add('v12-dark');chapter(sec,'08','YOUR NEXT MOVE','Turn insight into one concrete action');const path=sec.querySelector('.mx-path');if(path){path.classList.add('v12-next-grid');[...path.children].slice(0,4).forEach((el,i)=>{el.classList.add('v12-next-step');el.innerHTML=`<b>0${i+1}</b>${el.innerHTML}`})}}
function masters(sec){if(!sec)return;sec.id='v12-masters';sec.classList.add('v12-dark');chapter(sec,'09','YOUR NAYA MASTERS','18 specialist pathways');const areas=[...sec.querySelectorAll('.mx-area')].slice(0,18);const old=sec.querySelector('.mx-areas');if(!old||!areas.length)return;const names=['Writing','Research','Brainstorming','Content','Business','Marketing','Learning','Coding','Images','Video','Audio','Data','Productivity','Career','Decision','Creative','Systems','AI Orchestration'];const benefits=['Write with clarity.','Find the signal.','Expand possibilities.','Create faster.','Think strategically.','Turn value into action.','Learn intelligently.','Build and debug.','Make ideas visible.','Create media.','Shape sound.','Work with evidence.','Organize execution.','Grow capability.','Choose with clarity.','Create original work.','Build reusable systems.','Coordinate AI at scale.'];const grid=document.createElement('div');grid.className='v12-masters-grid';areas.forEach((a,i)=>{const c=document.createElement('article');c.className='v12-master';c.style.setProperty('--v12-master-color',colors[i%colors.length]);c.innerHTML=`<b>${String(i+1).padStart(2,'0')}</b><strong>Naya ${names[i]}</strong><span>${benefits[i]}</span>`;grid.appendChild(c)});old.replaceWith(grid)}
function reorder(){const hero=root.querySelector('.mx-hero'), n=root.querySelector('#v12-naya'), report=root.querySelector('#v12-report'), pattern=root.querySelector('#v12-pattern'), dim=root.querySelector('#v12-dimensions'), strength=find('your strengths','your superpowers'), leverSec=find('biggest lever','highest leverage opportunity'), nextSec=root.querySelector('#v12-next'), mastersSec=root.querySelector('#v12-masters'), playground=root.querySelector('#naya-playground');const ordered=[hero,n,report,pattern,dim,strength,leverSec,nextSec,mastersSec,playground].filter(Boolean);ordered.forEach(x=>root.appendChild(x));allSections().forEach(s=>{if(ordered.includes(s))return;const t=(s.textContent||'').toLowerCase();if(t.includes('short version')||t.includes('meaningful ai foundation'))s.classList.add('v12-early-commercial')})}
function apply(){if(score()===null)return;hero();addPrint();removeNoise();naya();report();dimsBlock(find('five dimensions','every score has'));pattern();story(find('your strengths','your superpowers'),'v12-strengths','06','YOUR STRENGTHS');story(find('biggest lever','highest leverage opportunity'),'v12-lever','07','YOUR BIGGEST LEVER');next(find('your next move','your next chapter'));masters(find('18 ai pathways','your 18 ai pathways'));reorder();root.setAttribute('data-v12-score',String(Math.round(score())))}
let tries=0;function wait(){if(score()!==null){apply();return}if(++tries<60)setTimeout(wait,150)}
if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',wait,{once:true});else wait();window.addEventListener('maxess:result-ready',apply);
})();
</script>'''

def execute():
    if not TARGET.exists(): raise SystemExit('BLOCKED — authoritative artifact missing')
    source=TARGET.read_text(encoding='utf-8')
    if MARKER in source: raise SystemExit('BLOCKED — V12 already executed')
    if 'id="maxess-results-10"' not in source or 'window.MAXESS_RESULT' not in source: raise SystemExit('BLOCKED — result contract/root missing')
    if '</head>' not in source or '</body>' not in source: raise SystemExit('BLOCKED — malformed artifact')
    before=len(source)
    out=source.replace('</head>',CSS+'\n</head>',1).replace('</body>',JS+'\n</body>',1).replace('</html>',MARKER+'\n</html>',1)
    if len(out)<=before: raise SystemExit('BLOCKED — ZERO-CHANGE EXECUTION')
    TARGET.write_text(out,encoding='utf-8')
    print(f'V12 executed: {before} -> {len(out)} bytes; +{len(out)-before} bytes')

if __name__=='__main__': execute()
