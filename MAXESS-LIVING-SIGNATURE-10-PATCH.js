/*
 MAXESS — LIVING SIGNATURE 10.0

 Purpose
 -------
 Upgrade the existing MAXESS results hero from a conventional score orb into
 the signature MAXESS visual language:

   Living Signature + Resonance Orb + five-dimensional energy + Naya reactivity

 Design rules
 ------------
 - Preserve the existing MAXESS result architecture and authoritative data.
 - Never recalculate assessment scores here.
 - No external libraries.
 - SVG for the generative signature; CSS for the atmosphere and motion.
 - Responsive and reduced-motion friendly.
 - Graceful fallback when MAXESS_RESULT is unavailable.
 - Naya playback can drive the visual through a shared CustomEvent contract.
 - If a real audio element is available, Web Audio can drive pulse intensity.

 Integration
 -----------
 Load this file after the existing MAXESS results markup/scripts.
 It looks for #maxess-results-10 .mx-score-orb and upgrades that hero in place.
*/
(function () {
  'use strict';

  const ROOT_ID = 'maxess-results-10';
  const SIGNATURE_ID = 'maxessLivingSignature';
  const STYLE_ID = 'maxessLivingSignatureStyles';

  const DIMENSION_META = [
    { key: 'direction', label: 'Direction', short: 'DIR', hue: 274 },
    { key: 'context', label: 'Context', short: 'CTX', hue: 252 },
    { key: 'collaboration', label: 'Collaboration', short: 'COL', hue: 218 },
    { key: 'evaluation', label: 'Evaluation', short: 'EVA', hue: 300 },
    { key: 'iteration', label: 'Iteration', short: 'ITR', hue: 186 }
  ];

  const clamp = (n, min, max) => Math.max(min, Math.min(max, n));
  const num = (v, fallback = 0) => {
    const n = Number(v);
    return Number.isFinite(n) ? n : fallback;
  };

  function readResult() {
    const r = window.MAXESS_RESULT || {};
    const rawDims = Array.isArray(r.dimensions) ? r.dimensions : [];
    const byName = new Map(rawDims.map(d => [String(d.name || d.id || '').toLowerCase(), d]));
    const dimensions = DIMENSION_META.map((meta, i) => {
      const source = rawDims[i] || byName.get(meta.label.toLowerCase()) || {};
      return {
        ...meta,
        score: clamp(num(source.score, 0), 0, 100),
        name: source.name || meta.label,
        insight: source.insight || '',
        description: source.description || ''
      };
    });
    const overall = clamp(num(r.overallScore, dimensions.reduce((a, d) => a + d.score, 0) / Math.max(1, dimensions.length)), 0, 100);
    return { ...r, overallScore: overall, dimensions };
  }

  function addStyles() {
    if (document.getElementById(STYLE_ID)) return;
    const style = document.createElement('style');
    style.id = STYLE_ID;
    style.textContent = `
      #${ROOT_ID} .mx-hero-grid{position:relative}
      #${ROOT_ID} .mx-ls-stage{
        position:relative;
        width:min(620px,92vw);
        aspect-ratio:1;
        margin:auto;
        display:grid;
        place-items:center;
        isolation:isolate;
      }
      #${ROOT_ID} .mx-ls-stage::before{
        content:"";
        position:absolute;
        inset:8%;
        border-radius:50%;
        background:radial-gradient(circle,rgba(176,86,255,.24),rgba(96,42,168,.08) 35%,transparent 70%);
        filter:blur(24px);
        z-index:-3;
        opacity:calc(.35 + var(--mx-energy, .6) * .65);
      }
      #${ROOT_ID} .mx-ls-stage::after{
        content:"";
        position:absolute;
        inset:2%;
        border-radius:50%;
        border:1px solid rgba(255,255,255,.035);
        box-shadow:0 0 80px rgba(142,64,255,.08), inset 0 0 80px rgba(110,50,210,.05);
        pointer-events:none;
      }
      #${ROOT_ID} .mx-ls-svg{
        position:absolute;
        inset:0;
        width:100%;
        height:100%;
        overflow:visible;
      }
      #${ROOT_ID} .mx-ls-path{
        fill:none;
        stroke-linecap:round;
        vector-effect:non-scaling-stroke;
        transform-origin:50% 50%;
        transition:opacity .7s ease,filter .7s ease;
      }
      #${ROOT_ID} .mx-ls-orbit{
        fill:none;
        stroke:rgba(225,199,255,.13);
        stroke-width:1;
        stroke-dasharray:2 12;
        transform-origin:50% 50%;
      }
      #${ROOT_ID} .mx-ls-node{
        fill:#fff;
        stroke:rgba(224,193,255,.9);
        stroke-width:1;
        filter:drop-shadow(0 0 7px rgba(191,106,255,.8));
      }
      #${ROOT_ID} .mx-ls-label{
        position:absolute;
        left:50%;
        top:50%;
        min-width:72px;
        padding:7px 10px;
        border:1px solid rgba(255,255,255,.12);
        border-radius:999px;
        background:rgba(5,3,9,.68);
        backdrop-filter:blur(12px);
        -webkit-backdrop-filter:blur(12px);
        color:rgba(255,255,255,.76);
        font-size:9px;
        font-weight:900;
        letter-spacing:.13em;
        text-align:center;
        text-transform:uppercase;
        opacity:0;
        transform:translate(-50%,-50%) scale(.92);
        pointer-events:none;
        transition:opacity .35s ease,transform .35s ease;
      }
      #${ROOT_ID} .mx-ls-stage:hover .mx-ls-label,
      #${ROOT_ID} .mx-ls-stage:focus-within .mx-ls-label,
      #${ROOT_ID} .mx-ls-stage.mx-ls-open .mx-ls-label{
        opacity:1;
        transform:translate(-50%,-50%) scale(1);
      }
      #${ROOT_ID} .mx-ls-core{
        position:relative;
        width:min(235px,38vw);
        aspect-ratio:1;
        border-radius:50%;
        display:grid;
        place-items:center;
        cursor:pointer;
        outline:none;
        transform:scale(calc(.94 + var(--mx-energy,.6) * .07));
        transition:transform .5s cubic-bezier(.2,.8,.2,1),filter .5s ease;
      }
      #${ROOT_ID} .mx-ls-core:hover{filter:brightness(1.08)}
      #${ROOT_ID} .mx-ls-core:focus-visible{box-shadow:0 0 0 4px rgba(220,188,255,.35),0 0 60px rgba(170,80,255,.35)}
      #${ROOT_ID} .mx-ls-core::before{
        content:"";
        position:absolute;
        inset:7%;
        border-radius:50%;
        background:
          radial-gradient(circle at 31% 22%,rgba(255,255,255,.72) 0,rgba(255,255,255,.18) 7%,transparent 18%),
          radial-gradient(circle at 50% 47%,rgba(207,150,255,.85) 0,rgba(126,48,220,.48) 31%,rgba(36,11,66,.94) 69%,#050208 100%);
        box-shadow:
          inset 0 4px 18px rgba(255,255,255,.14),
          inset 0 -30px 55px rgba(12,2,25,.8),
          0 0 0 1px rgba(255,255,255,.2),
          0 0 40px rgba(168,83,255,.38),
          0 0 95px rgba(132,52,225,.22);
      }
      #${ROOT_ID} .mx-ls-core::after{
        content:"";
        position:absolute;
        inset:0;
        border-radius:50%;
        border:1px solid rgba(225,197,255,.24);
        box-shadow:inset 0 0 28px rgba(185,105,255,.16);
        animation:mxLsBreathe 4.2s ease-in-out infinite;
      }
      #${ROOT_ID} .mx-ls-core-copy{
        position:relative;
        z-index:3;
        text-align:center;
        pointer-events:none;
      }
      #${ROOT_ID} .mx-ls-score{
        display:block;
        font-size:clamp(60px,8vw,104px);
        line-height:.8;
        letter-spacing:-.085em;
        font-weight:850;
        text-shadow:0 4px 22px rgba(0,0,0,.62),0 0 34px rgba(198,135,255,.18);
      }
      #${ROOT_ID} .mx-ls-core-label{
        display:block;
        margin-top:22px;
        color:rgba(235,214,255,.82);
        font-size:9px;
        font-weight:900;
        letter-spacing:.22em;
        text-transform:uppercase;
      }
      #${ROOT_ID} .mx-ls-ripple{
        position:absolute;
        inset:7%;
        border-radius:50%;
        border:1px solid rgba(215,170,255,0);
        pointer-events:none;
        opacity:0;
      }
      #${ROOT_ID} .mx-ls-stage.mx-ls-speaking .mx-ls-ripple{animation:mxLsVoice 1.15s ease-out infinite}
      #${ROOT_ID} .mx-ls-stage.mx-ls-speaking .mx-ls-core::after{animation:mxLsSpeak .72s ease-in-out infinite}
      #${ROOT_ID} .mx-ls-stage.mx-ls-excited .mx-ls-core{filter:brightness(1.16)}
      #${ROOT_ID} .mx-ls-stage.mx-ls-excited .mx-ls-ripple{animation:mxLsVoice .72s ease-out 2}
      #${ROOT_ID} .mx-ls-hint{
        position:absolute;
        left:50%;
        bottom:2%;
        transform:translateX(-50%);
        color:rgba(255,255,255,.36);
        font-size:9px;
        font-weight:700;
        letter-spacing:.11em;
        text-transform:uppercase;
        white-space:nowrap;
      }
      @keyframes mxLsBreathe{0%,100%{transform:scale(.985);opacity:.62}50%{transform:scale(1.018);opacity:1}}
      @keyframes mxLsSpeak{0%,100%{transform:scale(.985);opacity:.5}45%{transform:scale(1.065);opacity:1}70%{transform:scale(1.025);opacity:.8}}
      @keyframes mxLsVoice{0%{transform:scale(.72);opacity:.75}100%{transform:scale(1.22);opacity:0}}
      @media(max-width:900px){
        #${ROOT_ID} .mx-hero-grid{grid-template-columns:1fr;}
        #${ROOT_ID} .mx-ls-stage{order:-1;width:min(620px,94vw);}
        #${ROOT_ID} .mx-hero-copy{text-align:center;margin:auto;}
        #${ROOT_ID} .mx-hero-copy .mx-eyebrow{justify-content:center;}
        #${ROOT_ID} .mx-hero-copy .mx-copy{margin-left:auto;margin-right:auto;}
        #${ROOT_ID} .mx-hero-actions,#${ROOT_ID} .mx-proof{justify-content:center;}
      }
      @media(max-width:600px){
        #${ROOT_ID} .mx-ls-stage{width:96vw;}
        #${ROOT_ID} .mx-ls-core{width:min(205px,43vw);}
        #${ROOT_ID} .mx-ls-score{font-size:clamp(54px,14vw,78px);}
        #${ROOT_ID} .mx-ls-label{font-size:8px;min-width:62px;padding:6px 8px;}
        #${ROOT_ID} .mx-ls-hint{bottom:0;font-size:8px;}
      }
      @media(prefers-reduced-motion:reduce){
        #${ROOT_ID} .mx-ls-core::after,#${ROOT_ID} .mx-ls-stage.mx-ls-speaking .mx-ls-ripple{animation:none!important}
        #${ROOT_ID} .mx-ls-path{transition:none!important}
      }
    `;
    document.head.appendChild(style);
  }

  function polar(cx, cy, r, angle) {
    const a = angle - Math.PI / 2;
    return [cx + Math.cos(a) * r, cy + Math.sin(a) * r];
  }

  function makePath(score, index, points = 48) {
    const baseR = 118 + index * 7;
    const amp = 13 + score * .19;
    const phase = index * 1.31;
    const pts = [];
    for (let i = 0; i <= points; i++) {
      const t = i / points;
      const angle = t * Math.PI * 2;
      const wave1 = Math.sin(angle * (2 + index * .33) + phase) * amp;
      const wave2 = Math.sin(angle * (5 + index * .17) - phase * .7) * (amp * .32);
      const wave3 = Math.cos(angle * 3.1 + score * .02) * (score * .06);
      const r = baseR + wave1 + wave2 + wave3;
      pts.push(polar(300, 300, r, angle));
    }
    let d = '';
    pts.forEach((p, i) => {
      const prev = pts[(i - 1 + pts.length) % pts.length];
      const next = pts[(i + 1) % pts.length];
      const cx = (prev[0] + p[0]) / 2;
      const cy = (prev[1] + p[1]) / 2;
      if (i === 0) d += `M ${cx.toFixed(2)} ${cy.toFixed(2)} `;
      d += `Q ${p[0].toFixed(2)} ${p[1].toFixed(2)} ${(p[0] + next[0]) / 2} ${(p[1] + next[1]) / 2} `;
    });
    d += 'Z';
    return d;
  }

  function signatureMarkup(result) {
    const paths = result.dimensions.map((d, i) => {
      const hue = DIMENSION_META[i].hue;
      const score = d.score;
      const width = (1.2 + score / 100 * 2.4).toFixed(2);
      const opacity = (.16 + score / 100 * .42).toFixed(2);
      const dash = (650 - score * 2.1).toFixed(0);
      const dur = (18 - score * .055 + i * .7).toFixed(2);
      return `<path class="mx-ls-path" data-index="${i}" d="${makePath(score, i)}" stroke="hsla(${hue},92%,76%,${opacity})" stroke-width="${width}" style="filter:drop-shadow(0 0 ${Math.round(5 + score/16)}px hsla(${hue},90%,70%,.34));stroke-dasharray:${dash};stroke-dashoffset:0;animation:mxLsOrbit${i} ${dur}s linear infinite"/>`;
    }).join('');

    const labelPositions = [
      ['50%', '10%'], ['88%', '34%'], ['76%', '83%'], ['24%', '83%'], ['12%', '34%']
    ];
    const labels = result.dimensions.map((d, i) => `<span class="mx-ls-label" style="left:${labelPositions[i][0]};top:${labelPositions[i][1]}">${d.name}</span>`).join('');
    const nodes = result.dimensions.map((d, i) => {
      const p = polar(300, 300, 171, i * (Math.PI * 2 / 5));
      const size = 2.4 + d.score / 35;
      return `<circle class="mx-ls-node" cx="${p[0].toFixed(1)}" cy="${p[1].toFixed(1)}" r="${size.toFixed(1)}" opacity="${(.35 + d.score/160).toFixed(2)}"/>`;
    }).join('');
    return `
      <div class="mx-ls-stage" id="${SIGNATURE_ID}" tabindex="0" role="button" aria-label="MAXESS Living Signature. Tap or hover to reveal the five dimensions.">
        <svg class="mx-ls-svg" viewBox="0 0 600 600" aria-hidden="true">
          <defs>
            <radialGradient id="mxLsField" cx="50%" cy="50%" r="50%">
              <stop offset="0%" stop-color="#d9b4ff" stop-opacity=".22"/>
              <stop offset="35%" stop-color="#7e36d7" stop-opacity=".08"/>
              <stop offset="100%" stop-color="#000" stop-opacity="0"/>
            </radialGradient>
            <filter id="mxLsGlow"><feGaussianBlur stdDeviation="5" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
          </defs>
          <circle cx="300" cy="300" r="238" fill="url(#mxLsField)"/>
          <circle class="mx-ls-orbit" cx="300" cy="300" r="207"/>
          <circle class="mx-ls-orbit" cx="300" cy="300" r="185" opacity=".55"/>
          <g filter="url(#mxLsGlow)">${paths}</g>
          ${nodes}
        </svg>
        ${labels}
        <div class="mx-ls-core" id="mxLsCore" tabindex="0" aria-label="Overall MAXESS score ${Math.round(result.overallScore)} out of 100">
          <div class="mx-ls-ripple"></div>
          <div class="mx-ls-core-copy">
            <strong class="mx-ls-score">${Math.round(result.overallScore)}</strong>
            <span class="mx-ls-core-label">MAXESS SCORE</span>
          </div>
        </div>
        <div class="mx-ls-hint">Your intelligence signature · hover or tap</div>
      </div>`;
  }

  function installKeyframes() {
    if (document.getElementById('mxLsDynamicKeyframes')) return;
    const s = document.createElement('style');
    s.id = 'mxLsDynamicKeyframes';
    let css = '';
    for (let i = 0; i < 5; i++) {
      css += `@keyframes mxLsOrbit${i}{from{transform:rotate(0deg)}to{transform:rotate(${i % 2 ? -360 : 360}deg)}}`;
    }
    s.textContent = css;
    document.head.appendChild(s);
  }

  function upgradeHero() {
    const root = document.getElementById(ROOT_ID);
    if (!root || document.getElementById(SIGNATURE_ID)) return false;
    const orb = root.querySelector('.mx-score-orb');
    if (!orb) return false;

    const result = readResult();
    const stage = document.createElement('div');
    stage.innerHTML = signatureMarkup(result);
    const signature = stage.firstElementChild;
    orb.replaceWith(signature);

    root.style.setProperty('--mx-energy', String(result.overallScore / 100));
    installKeyframes();
    bindInteraction(signature, result);
    return true;
  }

  function bindInteraction(stage, result) {
    const core = stage.querySelector('#mxLsCore');
    const paths = [...stage.querySelectorAll('.mx-ls-path')];
    const orbEnergy = result.overallScore / 100;

    const setSpeaking = (on, excited = false) => {
      stage.classList.toggle('mx-ls-speaking', !!on);
      stage.classList.toggle('mx-ls-excited', !!excited);
    };

    core.addEventListener('click', () => stage.classList.toggle('mx-ls-open'));
    core.addEventListener('keydown', e => {
      if (e.key === 'Enter' || e.key === ' ') {
        e.preventDefault();
        stage.classList.toggle('mx-ls-open');
      }
    });

    // Public Naya visual contract. Any Naya player can dispatch these events.
    window.addEventListener('maxess:naya:start', () => setSpeaking(true, false));
    window.addEventListener('maxess:naya:word', e => {
      const energy = clamp(num(e.detail && e.detail.energy, .72), 0, 1);
      stage.style.setProperty('--mx-energy', String(Math.max(orbEnergy, energy)));
      setSpeaking(true, energy > .82);
      paths.forEach((p, i) => {
        p.style.opacity = String(.3 + energy * .55);
        p.style.strokeWidth = String(1.2 + energy * 2.8 + i * .06);
      });
    });
    window.addEventListener('maxess:naya:positive', () => {
      setSpeaking(true, true);
      window.setTimeout(() => setSpeaking(true, false), 700);
    });
    window.addEventListener('maxess:naya:stop', () => {
      setSpeaking(false, false);
      stage.style.setProperty('--mx-energy', String(orbEnergy));
      paths.forEach(p => { p.style.opacity = ''; p.style.strokeWidth = ''; });
    });

    // If a compatible audio element exists, sample its energy with Web Audio.
    // This is deliberately optional: the visual still works without it.
    const audio = document.querySelector('#maxessNayaAudioElement, audio[data-maxess-naya], .mx-naya-audio audio');
    if (audio && window.AudioContext && window.AnalyserNode) {
      try {
        const AudioCtx = window.AudioContext || window.webkitAudioContext;
        const ctx = new AudioCtx();
        const source = ctx.createMediaElementSource(audio);
        const analyser = ctx.createAnalyser();
        analyser.fftSize = 256;
        source.connect(analyser);
        analyser.connect(ctx.destination);
        const data = new Uint8Array(analyser.frequencyBinCount);
        const tick = () => {
          if (!audio.paused && !audio.ended) {
            if (ctx.state === 'suspended') ctx.resume().catch(() => {});
            analyser.getByteFrequencyData(data);
            let sum = 0;
            for (let i = 0; i < data.length; i++) sum += data[i];
            const energy = clamp(sum / (data.length * 255), 0, 1);
            stage.style.setProperty('--mx-energy', String(Math.max(orbEnergy, .5 + energy * .5)));
            setSpeaking(true, energy > .68);
            paths.forEach((p, i) => {
              p.style.opacity = String(.24 + energy * .66);
              p.style.strokeWidth = String(1.2 + energy * 3 + i * .04);
            });
          } else if (stage.classList.contains('mx-ls-speaking')) {
            setSpeaking(false, false);
            stage.style.setProperty('--mx-energy', String(orbEnergy));
          }
          requestAnimationFrame(tick);
        };
        tick();
      } catch (err) {
        // Cross-origin media or browser policy may prevent analysis. Event sync remains available.
      }
    }
  }

  function boot() {
    addStyles();
    upgradeHero();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => setTimeout(boot, 60), { once: true });
  } else {
    setTimeout(boot, 60);
  }
})();
