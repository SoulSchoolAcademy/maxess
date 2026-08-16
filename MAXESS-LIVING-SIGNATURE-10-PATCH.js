/*
 MAXESS V13 — EXECUTION PATCH

 Purpose:
 Turn the existing MAXESS Results experience into a personal AI mastery report
 without replacing the authoritative result architecture.

 Preservation:
 - window.MAXESS_RESULT remains authoritative.
 - Existing markup, video, CTAs, audio, assessment handoff and conversion assets remain.
 - This patch upgrades/reorders existing sections in place.
 - No external libraries.
 - Reduced-motion and keyboard-safe behavior are retained.

 North Star:
 SCORE -> NAYA -> REPORT -> DIMENSIONS -> PATTERN -> MEANING -> STRENGTHS -> LEVER -> NEXT MOVE -> MASTERS -> SOLUTION -> ACTION

 Iteration: V13
*/
(function () {
  'use strict';

  const ROOT_ID = 'maxess-results-10';
  const PATCH_ID = 'maxessV13Execution';
  const NAYA_IMAGE_BLACK = 'https://i.postimg.cc/RF3XFWJ7/grok-image-c6a924fd-1f75-4ac8-840d-35b224fb3e52.jpg';
  const NAYA_IMAGE_WHITE = 'https://i.postimg.cc/dVXw7sRN/grok-image-f75a6f12-4e3a-4c99-a334-5684ba0f7401.jpg';
  const LOGO_IMAGE = 'https://i.postimg.cc/Twqw14vv/ICON-LOGO.png';

  const clamp = (n, a, b) => Math.max(a, Math.min(b, n));
  const scoreOf = (d) => clamp(Number(d && d.score) || 0, 0, 100);
  const result = window.MAXESS_RESULT || {};
  const dimensions = Array.isArray(result.dimensions) ? result.dimensions.map((d, i) => ({
    ...d,
    score: scoreOf(d),
    index: i
  })) : [];
  const overall = clamp(Number(result.overallScore) || (dimensions.length ? dimensions.reduce((s, d) => s + d.score, 0) / dimensions.length : 0), 0, 100);

  function esc(value) {
    return String(value == null ? '' : value).replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
  }

  function bandFor(score) {
    if (score < 50) return 'Building';
    if (score < 65) return 'Developing';
    if (score < 75) return 'Advancing';
    if (score < 85) return 'Strong';
    if (score < 95) return 'Mastery';
    return 'Exceptional';
  }

  function colorFor(score) {
    const stops = [
      [0, [255, 62, 62]],
      [50, [255, 148, 42]],
      [65, [247, 215, 77]],
      [75, [81, 226, 173]],
      [85, [57, 190, 218]],
      [90, [77, 112, 255]],
      [95, [181, 77, 255]],
      [100, [255, 62, 198]]
    ];
    for (let i = 1; i < stops.length; i++) {
      if (score <= stops[i][0]) {
        const a = stops[i - 1], b = stops[i];
        const t = (score - a[0]) / (b[0] - a[0]);
        return b[1].map((v, j) => Math.round(a[1][j] + (v - a[1][j]) * t));
      }
    }
    return stops[stops.length - 1][1];
  }

  function setVars(root) {
    const [r,g,b] = colorFor(overall);
    root.style.setProperty('--v13-r', r);
    root.style.setProperty('--v13-g', g);
    root.style.setProperty('--v13-b', b);
    root.style.setProperty('--v13-rgb', `${r},${g},${b}`);
    root.style.setProperty('--v13-band', `'${bandFor(overall)}'`);
  }

  function addStyles() {
    if (document.getElementById('maxessV13Styles')) return;
    const style = document.createElement('style');
    style.id = 'maxessV13Styles';
    style.textContent = `
      #${ROOT_ID}{
        --v13-rgb:166,108,255;
        --v13-r:166;--v13-g:108;--v13-b:255;
        --v13-accent:rgb(var(--v13-rgb));
        --v13-soft:rgba(var(--v13-rgb),.16);
        --v13-line:rgba(255,255,255,.11);
      }
      #${ROOT_ID} .v13-hidden{display:none!important}
      #${ROOT_ID} .v13-kicker{
        display:inline-flex;align-items:center;gap:9px;margin-bottom:13px;
        color:rgba(255,255,255,.54);font-size:10px;font-weight:900;letter-spacing:.2em;text-transform:uppercase;
      }
      #${ROOT_ID} .v13-kicker:before{content:"";width:26px;height:1px;background:linear-gradient(90deg,var(--v13-accent),transparent)}
      #${ROOT_ID} .v13-chapter{
        position:relative;display:grid;grid-template-columns:auto 1fr;gap:15px;align-items:start;
        margin-bottom:25px;
      }
      #${ROOT_ID} .v13-number{
        display:grid;place-items:center;width:42px;height:42px;border-radius:13px;
        background:linear-gradient(145deg,rgba(255,255,255,.12),rgba(var(--v13-rgb),.14));
        border:1px solid rgba(255,255,255,.14);font-size:10px;font-weight:950;letter-spacing:.08em;
        box-shadow:0 8px 28px rgba(0,0,0,.2);
      }
      #${ROOT_ID} .v13-subtitle{margin:5px 0 0;color:rgba(255,255,255,.54);font-size:15px;line-height:1.55;max-width:760px}

      /* HERO: score first, everything else second. */
      #${ROOT_ID} .mx-hero{min-height:min(900px,94vh)!important;padding-top:52px!important;padding-bottom:66px!important}
      #${ROOT_ID} .mx-hero-grid{gap:24px!important}
      #${ROOT_ID} .mx-hero-copy{max-width:1000px!important;text-align:center!important;order:3}
      #${ROOT_ID} .mx-hero-copy .mx-eyebrow{justify-content:center}
      #${ROOT_ID} .mx-hero-copy .mx-title{font-size:clamp(34px,5vw,68px)!important;margin-top:8px!important}
      #${ROOT_ID} .mx-hero-copy .mx-title em{background:linear-gradient(110deg,#fff,#fff 40%,rgb(var(--v13-rgb)) 100%);-webkit-background-clip:text;background-clip:text}
      #${ROOT_ID} .mx-hero-copy .mx-copy{max-width:640px!important;margin:14px auto 0!important;font-size:16px!important;color:rgba(255,255,255,.62)!important}
      #${ROOT_ID} .mx-score-orb,#${ROOT_ID} .mx-ls-stage{order:1!important}
      #${ROOT_ID} .mx-hero-actions{order:4;margin-top:22px!important}
      #${ROOT_ID} .mx-proof{order:5;margin-top:16px!important;max-width:760px;width:100%;margin-left:auto;margin-right:auto}
      #${ROOT_ID} .v13-hero-label{order:2;display:flex;align-items:center;justify-content:center;gap:10px;margin-top:-10px;color:#fff;font-size:clamp(22px,2.6vw,36px);font-weight:850;letter-spacing:-.035em}
      #${ROOT_ID} .v13-score-status{display:inline-flex;align-items:center;gap:8px;margin-left:5px;padding:7px 11px;border:1px solid rgba(255,255,255,.16);border-radius:999px;background:rgba(255,255,255,.055);color:rgba(255,255,255,.72);font-size:10px;font-weight:900;letter-spacing:.13em;text-transform:uppercase;vertical-align:middle}
      #${ROOT_ID} .v13-score-status:before{content:"";width:7px;height:7px;border-radius:50%;background:rgb(var(--v13-rgb));box-shadow:0 0 15px rgb(var(--v13-rgb))}
      #${ROOT_ID} .v13-print{position:absolute;right:clamp(20px,4vw,72px);top:24px;z-index:10}
      #${ROOT_ID} .v13-print button{display:inline-flex;align-items:center;gap:9px;padding:10px 14px;border-radius:12px;border:1px solid rgba(255,255,255,.15);background:rgba(255,255,255,.055);color:#fff;font-size:11px;font-weight:800;cursor:pointer;backdrop-filter:blur(12px)}
      #${ROOT_ID} .v13-print button:hover{background:rgba(255,255,255,.1);transform:translateY(-1px)}
      #${ROOT_ID} .v13-print svg{width:15px;height:15px}

      /* NAYA: person, not advertisement. */
      #${ROOT_ID} .v13-naya-intro{position:relative;overflow:hidden;margin:0 auto clamp(20px,3vw,45px);width:min(1200px,100%);border:1px solid rgba(255,255,255,.13);border-radius:30px;background:linear-gradient(115deg,rgba(255,255,255,.07),rgba(var(--v13-rgb),.09) 52%,rgba(255,255,255,.025));box-shadow:0 30px 90px rgba(0,0,0,.32)}
      #${ROOT_ID} .v13-naya-inner{display:grid;grid-template-columns:180px 1fr auto;gap:28px;align-items:center;padding:28px 32px}
      #${ROOT_ID} .v13-naya-photo{width:148px;height:148px;border-radius:50%;object-fit:cover;object-position:center;border:3px solid rgba(255,255,255,.75);box-shadow:0 0 0 7px rgba(var(--v13-rgb),.09),0 18px 50px rgba(0,0,0,.4)}
      #${ROOT_ID} .v13-naya-copy h2{margin:0;font-size:clamp(25px,3vw,42px);line-height:1;letter-spacing:-.045em}
      #${ROOT_ID} .v13-naya-copy p{margin:10px 0 0;max-width:680px;color:rgba(255,255,255,.68);font-size:15px;line-height:1.6}
      #${ROOT_ID} .v13-naya-name{display:block;margin-bottom:7px;color:rgb(var(--v13-rgb));font-size:10px;font-weight:950;letter-spacing:.18em;text-transform:uppercase}
      #${ROOT_ID} .v13-naya-listen{display:inline-flex;align-items:center;gap:10px;min-height:52px;padding:0 18px;border-radius:15px;border:1px solid rgba(255,255,255,.18);background:linear-gradient(135deg,rgba(255,255,255,.12),rgba(var(--v13-rgb),.18));color:#fff;font-weight:850;cursor:pointer;white-space:nowrap}
      #${ROOT_ID} .v13-naya-listen:hover{filter:brightness(1.1);transform:translateY(-2px)}
      #${ROOT_ID} .v13-naya-listen .play{display:grid;place-items:center;width:25px;height:25px;border-radius:50%;background:#fff;color:#13091e;font-size:10px}

      /* Section rhythm: report chapters breathe, but do not drift apart. */
      #${ROOT_ID} .v13-report-section{padding-top:clamp(54px,6vw,88px)!important;padding-bottom:clamp(54px,6vw,88px)!important}
      #${ROOT_ID} .v13-report-section.v13-light{background:#f8f7fb;color:#0b0910}
      #${ROOT_ID} .v13-report-section.v13-light .v13-kicker{color:rgba(15,12,20,.5)}
      #${ROOT_ID} .v13-report-section.v13-light .v13-subtitle{color:rgba(15,12,20,.58)}
      #${ROOT_ID} .v13-report-section.v13-light .mx-section-head p{color:rgba(15,12,20,.58)}
      #${ROOT_ID} .v13-report-section.v13-light .mx-section-head h2{color:#0b0910}

      /* Dimension cards: score and meaning are seen before microcopy. */
      #${ROOT_ID} .mx-dim-grid{gap:16px!important}
      #${ROOT_ID} .mx-dim{position:relative;overflow:hidden;min-height:310px!important;border-radius:27px!important;background:linear-gradient(160deg,rgba(255,255,255,.085),rgba(255,255,255,.018))!important}
      #${ROOT_ID} .mx-dim:before{content:"";position:absolute;left:0;right:0;top:0;height:4px;background:linear-gradient(90deg,transparent,rgb(var(--v13-rgb)),transparent);opacity:.85}
      #${ROOT_ID} .mx-dim-head strong{font-size:34px!important;text-shadow:0 0 22px rgba(var(--v13-rgb),.25)}
      #${ROOT_ID} .mx-track{height:7px!important;background:rgba(255,255,255,.07)!important}
      #${ROOT_ID} .mx-track span{background:linear-gradient(90deg,rgba(var(--v13-rgb),.55),rgb(var(--v13-rgb)))!important}
      #${ROOT_ID} .mx-lever b{font-size:13px!important}

      /* Strength / lever cards become visual statements. */
      #${ROOT_ID} .v13-visual-card{position:relative;overflow:hidden;border-radius:28px;border:1px solid rgba(255,255,255,.12);background:linear-gradient(145deg,rgba(255,255,255,.08),rgba(255,255,255,.018));padding:28px;min-height:190px}
      #${ROOT_ID} .v13-visual-card:after{content:"";position:absolute;width:180px;height:180px;right:-90px;top:-90px;border-radius:50%;background:radial-gradient(circle,rgba(var(--v13-rgb),.28),transparent 70%)}
      #${ROOT_ID} .v13-card-score{font-size:clamp(46px,5vw,72px);font-weight:900;line-height:.9;letter-spacing:-.07em}
      #${ROOT_ID} .v13-card-name{margin-top:12px;font-size:18px;font-weight:850}
      #${ROOT_ID} .v13-card-copy{margin-top:7px;color:rgba(255,255,255,.58);font-size:13px;line-height:1.5;max-width:460px}

      /* Pattern visualization: connect the five dimensions. */
      #${ROOT_ID} .v13-pattern{position:relative;display:grid;grid-template-columns:minmax(0,1fr) 360px;gap:30px;align-items:center;padding:clamp(24px,4vw,50px);border:1px solid rgba(255,255,255,.12);border-radius:32px;background:radial-gradient(circle at 50% 50%,rgba(var(--v13-rgb),.1),transparent 48%),rgba(255,255,255,.025);overflow:hidden}
      #${ROOT_ID} .v13-pattern-map{position:relative;min-height:380px;display:grid;place-items:center}
      #${ROOT_ID} .v13-pattern-map svg{width:min(520px,100%);height:380px;overflow:visible}
      #${ROOT_ID} .v13-pattern-center{position:absolute;display:grid;place-items:center;width:115px;height:115px;border-radius:50%;background:radial-gradient(circle at 35% 25%,#fff,rgba(var(--v13-rgb),.95) 22%,rgba(var(--v13-rgb),.22) 68%,transparent 100%);box-shadow:0 0 55px rgba(var(--v13-rgb),.35)}
      #${ROOT_ID} .v13-pattern-center b{font-size:30px;line-height:1;color:#fff;text-shadow:0 2px 12px #000}
      #${ROOT_ID} .v13-pattern-center span{font-size:8px;font-weight:900;letter-spacing:.14em;text-transform:uppercase;color:rgba(255,255,255,.78)}
      #${ROOT_ID} .v13-pattern-copy h3{margin:0;font-size:clamp(27px,3.5vw,46px);line-height:.98;letter-spacing:-.05em}
      #${ROOT_ID} .v13-pattern-copy p{margin:14px 0 0;color:rgba(255,255,255,.62);line-height:1.6;font-size:15px}
      #${ROOT_ID} .v13-pattern-list{display:grid;gap:8px;margin-top:22px}
      #${ROOT_ID} .v13-pattern-item{display:flex;align-items:center;justify-content:space-between;gap:15px;padding:11px 13px;border:1px solid rgba(255,255,255,.08);border-radius:13px;background:rgba(255,255,255,.025)}
      #${ROOT_ID} .v13-pattern-item span{font-size:12px;color:rgba(255,255,255,.58)}
      #${ROOT_ID} .v13-pattern-item b{font-size:13px}

      /* Pathways: personalized first, complete library remains accessible. */
      #${ROOT_ID} .v13-path-grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:14px}
      #${ROOT_ID} .v13-path{position:relative;overflow:hidden;min-height:190px;padding:22px;border-radius:23px;border:1px solid rgba(255,255,255,.11);background:linear-gradient(145deg,rgba(255,255,255,.075),rgba(255,255,255,.018));transition:transform .2s ease,border-color .2s ease}
      #${ROOT_ID} .v13-path:hover{transform:translateY(-4px);border-color:rgba(var(--v13-rgb),.42)}
      #${ROOT_ID} .v13-path-icon{width:46px;height:46px;border-radius:15px;display:grid;place-items:center;background:linear-gradient(145deg,rgba(255,255,255,.16),rgba(var(--v13-rgb),.22));font-size:20px;box-shadow:inset 0 1px rgba(255,255,255,.35)}
      #${ROOT_ID} .v13-path h3{margin:16px 0 0;font-size:17px}
      #${ROOT_ID} .v13-path p{margin:6px 0 0;color:rgba(255,255,255,.54);font-size:12px;line-height:1.45}
      #${ROOT_ID} .v13-path-badge{position:absolute;right:13px;top:13px;color:rgb(var(--v13-rgb));font-size:8px;font-weight:950;letter-spacing:.14em;text-transform:uppercase}
      #${ROOT_ID} .v13-view-all{display:flex;justify-content:center;margin-top:20px}
      #${ROOT_ID} .v13-view-all button{border:0;background:none;color:rgba(255,255,255,.58);font-weight:800;cursor:pointer;padding:10px 14px}
      #${ROOT_ID} .v13-view-all button:hover{color:#fff}

      /* Action plan: a visual journey rather than a paragraph. */
      #${ROOT_ID} .v13-journey{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;position:relative}
      #${ROOT_ID} .v13-step{position:relative;padding:24px 20px;border:1px solid rgba(255,255,255,.11);border-radius:22px;background:rgba(255,255,255,.035);min-height:180px}
      #${ROOT_ID} .v13-step:after{content:"";position:absolute;right:-17px;top:38px;width:32px;height:1px;background:linear-gradient(90deg,rgba(var(--v13-rgb),.6),transparent)}
      #${ROOT_ID} .v13-step:last-child:after{display:none}
      #${ROOT_ID} .v13-step-no{color:rgb(var(--v13-rgb));font-size:10px;font-weight:950;letter-spacing:.16em}
      #${ROOT_ID} .v13-step h3{margin:12px 0 0;font-size:19px}
      #${ROOT_ID} .v13-step p{margin:7px 0 0;color:rgba(255,255,255,.53);font-size:12px;line-height:1.5}

      /* Keep the commercial message at the end of the story. */
      #${ROOT_ID} .v13-deprioritize{opacity:.94}

      @media(max-width:1000px){
        #${ROOT_ID} .v13-naya-inner{grid-template-columns:120px 1fr}
        #${ROOT_ID} .v13-naya-listen{grid-column:2;justify-self:start}
        #${ROOT_ID} .v13-pattern{grid-template-columns:1fr}
        #${ROOT_ID} .v13-path-grid{grid-template-columns:repeat(2,minmax(0,1fr))}
        #${ROOT_ID} .v13-journey{grid-template-columns:repeat(2,1fr)}
        #${ROOT_ID} .v13-step:nth-child(2):after{display:none}
      }
      @media(max-width:700px){
        #${ROOT_ID} .v13-print{position:relative;right:auto;top:auto;display:flex;justify-content:flex-end;margin-bottom:10px}
        #${ROOT_ID} .v13-hero-label{font-size:25px}
        #${ROOT_ID} .v13-naya-inner{grid-template-columns:1fr;text-align:center;padding:24px}
        #${ROOT_ID} .v13-naya-photo{margin:auto}
        #${ROOT_ID} .v13-naya-listen{grid-column:auto;justify-self:center}
        #${ROOT_ID} .v13-path-grid,#${ROOT_ID} .v13-journey{grid-template-columns:1fr}
        #${ROOT_ID} .v13-step:after{display:none!important}
        #${ROOT_ID} .v13-pattern-map{min-height:300px}
        #${ROOT_ID} .v13-pattern-map svg{height:300px}
      }
      @media(prefers-reduced-motion:reduce){
        #${ROOT_ID} .v13-path,#${ROOT_ID} .v13-naya-listen,#${ROOT_ID} .v13-print button{transition:none!important}
      }

      /* PRINT: white paper, black text, no web chrome. */
      @media print{
        #${ROOT_ID}{background:#fff!important;color:#111!important;overflow:visible!important}
        #${ROOT_ID} *{box-shadow:none!important;text-shadow:none!important}
        #${ROOT_ID} .v13-print,#${ROOT_ID} button,#${ROOT_ID} .mx-hero-actions,#${ROOT_ID} .mx-proof,#${ROOT_ID} .mx-band{display:none!important}
        #${ROOT_ID} .mx-section,#${ROOT_ID} .v13-report-section{background:#fff!important;color:#111!important;padding:36px 24px!important}
        #${ROOT_ID} .mx-title,#${ROOT_ID} .mx-section-head h2,#${ROOT_ID} .v13-pattern-copy h3,#${ROOT_ID} .v13-naya-copy h2{color:#111!important}
        #${ROOT_ID} .mx-copy,#${ROOT_ID} .mx-section-head p,#${ROOT_ID} .mx-dim p,#${ROOT_ID} .v13-naya-copy p,#${ROOT_ID} .v13-pattern-copy p,#${ROOT_ID} .v13-path p,#${ROOT_ID} .v13-step p{color:#333!important}
        #${ROOT_ID} .v13-naya-intro,#${ROOT_ID} .mx-dim,#${ROOT_ID} .v13-pattern,#${ROOT_ID} .v13-path,#${ROOT_ID} .v13-step{border-color:#ddd!important;background:#fff!important}
        #${ROOT_ID} .mx-score-orb,#${ROOT_ID} .mx-ls-stage{break-inside:avoid;page-break-inside:avoid}
        #${ROOT_ID} .mx-dim,#${ROOT_ID} .v13-path,#${ROOT_ID} .v13-step{break-inside:avoid;page-break-inside:avoid}
        #${ROOT_ID} .v13-naya-photo{border-color:#222!important}
      }
    `;
    document.head.appendChild(style);
  }

  function printButton(root) {
    if (root.querySelector('.v13-print')) return;
    const hero = root.querySelector('.mx-hero');
    if (!hero) return;
    const wrap = document.createElement('div');
    wrap.className = 'v13-print';
    wrap.innerHTML = '<button type="button" aria-label="Print or save your MAXESS report as PDF"><svg viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M6 9V3h12v6M6 18H4a2 2 0 0 1-2-2v-5a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v5a2 2 0 0 1-2 2h-2M6 14h12v7H6z" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/></svg> Print / Save PDF</button>';
    wrap.querySelector('button').addEventListener('click', () => window.print());
    hero.appendChild(wrap);
  }

  function heroLabel(root) {
    if (root.querySelector('.v13-hero-label')) return;
    const orb = root.querySelector('.mx-score-orb, .mx-ls-stage');
    if (!orb || !orb.parentNode) return;
    const label = document.createElement('div');
    label.className = 'v13-hero-label';
    label.innerHTML = 'Your AI Score <span class="v13-score-status">' + esc(bandFor(overall)) + '</span>';
    orb.parentNode.insertBefore(label, orb.nextSibling);
  }

  function nayaIntro(root) {
    if (root.querySelector('.v13-naya-intro')) return;
    const hero = root.querySelector('.mx-hero');
    if (!hero) return;
    const section = document.createElement('section');
    section.className = 'mx-section v13-report-section';
    section.setAttribute('aria-label','Naya introduction to your personalized report');
    section.innerHTML = `
      <div class="mx-wide">
        <div class="v13-naya-intro">
          <div class="v13-naya-inner">
            <picture><img class="v13-naya-photo" src="${NAYA_IMAGE_BLACK}" alt="Naya, your AI report guide" loading="eager"></picture>
            <div class="v13-naya-copy">
              <span class="v13-naya-name">Naya · Your AI Report Guide</span>
              <h2>Hi. I'm Naya. Let's make sense of your results.</h2>
              <p>I’ve taken your MAXESS result and turned it into a personal report. I’ll help you see what you already do well, where your biggest leverage is, and what your next move can be.</p>
            </div>
            <button class="v13-naya-listen" type="button" aria-label="Listen to Naya explain your results"><span class="play">▶</span><span>Listen to your results</span></button>
          </div>
        </div>
      </div>`;
    hero.parentNode.insertBefore(section, hero.nextSibling);
    const button = section.querySelector('.v13-naya-listen');
    button.addEventListener('click', () => {
      const existing = root.querySelector('#maxessNayaPlay');
      if (existing) existing.click();
      else if ('speechSynthesis' in window) {
        const strongest = dimensions.slice().sort((a,b)=>b.score-a.score)[0];
        const weakest = dimensions.slice().sort((a,b)=>a.score-b.score)[0];
        const text = `Hi. I'm Naya. Your MAXESS AI score is ${Math.round(overall)}. Your current level is ${bandFor(overall)}. Your strongest area is ${strongest ? strongest.name : 'your current strengths'}, and your biggest opportunity is ${weakest ? weakest.name : 'your next area of growth'}. This report will help you turn that insight into action.`;
        window.speechSynthesis.cancel();
        window.speechSynthesis.speak(new SpeechSynthesisUtterance(text));
      }
    });
  }

  function findSections(root) {
    const all = [...root.querySelectorAll('section')];
    return all.map((el, i) => {
      const text = (el.innerText || '').replace(/\s+/g,' ').trim().toLowerCase();
      return { el, i, text };
    });
  }

  function scoreSection(text, words) {
    return words.reduce((n,w)=>n + (text.includes(w) ? 1 : 0), 0);
  }

  function reorderReport(root) {
    const sections = findSections(root);
    if (sections.length < 3) return;
    const main = root.querySelector('.mx-wrap') || root;
    const hero = root.querySelector('.mx-hero');
    const naya = root.querySelector('.v13-naya-intro') && root.querySelector('.v13-naya-intro').closest('section');
    if (!hero || !main) return;

    const candidates = sections.filter(s => s.el !== hero.parentElement && s.el !== naya);
    const patterns = [
      ['dimensions','five dimensions','capability profile'],
      ['pattern','capability signature','fingerprint'],
      ['strength','superpower','already have'],
      ['leverage','highest leverage','biggest lever','opportunity'],
      ['next move','next chapter','action plan','next step'],
      ['18 naya','18 ai','pathways','masters'],
      ['playground','open now','naya writer','brainstormer'],
      ['solution','technology should','amplify your human']
    ];
    const chosen = [];
    patterns.forEach(words => {
      const hit = candidates.filter(s => !chosen.includes(s.el)).sort((a,b)=>scoreSection(b.text,words)-scoreSection(a.text,words))[0];
      if (hit && scoreSection(hit.text,words) > 0) chosen.push(hit.el);
    });
    if (!chosen.length) return;

    const anchors = [hero.parentElement, naya].filter(Boolean);
    let cursor = naya || hero.parentElement;
    chosen.forEach((el, idx) => {
      if (!el || el === cursor || el.contains(cursor)) return;
      cursor.parentNode.appendChild(el);
      el.classList.add('v13-report-section');
      cursor = el;
    });
  }

  function enhanceDimensions(root) {
    const cards = [...root.querySelectorAll('.mx-dim')];
    if (!cards.length) return;
    cards.forEach((card, i) => {
      card.dataset.v13Dimension = 'true';
      const score = dimensions[i] ? dimensions[i].score : Number((card.querySelector('strong') || {}).textContent) || 0;
      const [r,g,b] = colorFor(score);
      card.style.setProperty('--dim-rgb', `${r},${g},${b}`);
      card.style.setProperty('--w', `${score}%`);
      const heading = card.querySelector('h3');
      if (heading) heading.setAttribute('aria-label', `${heading.textContent.trim()}, score ${Math.round(score)} out of 100`);
    });
  }

  function addPatternVisualization(root) {
    if (root.querySelector('.v13-pattern')) return;
    const candidates = findSections(root);
    const target = candidates.find(s => scoreSection(s.text,['pattern','capability signature','fingerprint']) > 0 && s.el !== root.querySelector('.mx-hero'));
    if (!target) return;
    const sorted = dimensions.slice().sort((a,b)=>b.score-a.score);
    const points = dimensions.map((d,i)=>{
      const a = i * Math.PI * 2 / Math.max(1,dimensions.length) - Math.PI/2;
      const r = 135 + d.score * .55;
      const x = 260 + Math.cos(a)*r, y = 190 + Math.sin(a)*r;
      return {x,y,d};
    });
    const poly = points.map(p=>`${p.x},${p.y}`).join(' ');
    const rings = [55,95,135,175].map(r=>`<circle cx="260" cy="190" r="${r}" fill="none" stroke="rgba(255,255,255,.09)"/>`).join('');
    const lines = points.map(p=>`<line x1="260" y1="190" x2="${p.x}" y2="${p.y}" stroke="rgba(255,255,255,.08)"/>`).join('');
    const nodes = points.map((p,i)=>`<circle cx="${p.x}" cy="${p.y}" r="${5 + p.d.score/35}" fill="rgb(${colorFor(p.d.score).join(',')})" filter="url(#v13Glow)"/>`).join('');
    const panel = document.createElement('div');
    panel.className = 'v13-pattern';
    panel.innerHTML = `<div class="v13-pattern-map"><svg viewBox="0 0 520 380" role="img" aria-label="Five-dimensional MAXESS capability pattern"><defs><filter id="v13Glow"><feGaussianBlur stdDeviation="4" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter></defs>${rings}${lines}<polygon points="${poly}" fill="rgba(var(--v13-rgb),.12)" stroke="rgb(var(--v13-rgb))" stroke-width="2" stroke-linejoin="round"/>${nodes}</svg><div class="v13-pattern-center"><b>${Math.round(overall)}</b><span>MAXESS</span></div></div><div class="v13-pattern-copy"><span class="v13-kicker">04 · YOUR PATTERN</span><h3>See how your strengths work together.</h3><p>Your score tells you where you are. Your pattern shows how your capabilities combine. That relationship is where the most useful insight lives.</p><div class="v13-pattern-list">${sorted.slice(0,5).map(d=>`<div class="v13-pattern-item"><span>${esc(d.name)}</span><b>${Math.round(d.score)}</b></div>`).join('')}</div></div>`;
    target.el.querySelector('.mx-wide,.mx-reading')?.appendChild(panel) || target.el.appendChild(panel);
  }

  function addJourney(root) {
    if (root.querySelector('.v13-journey')) return;
    const target = findSections(root).find(s=>scoreSection(s.text,['next move','next chapter','action plan','next step'])>0);
    if (!target) return;
    const lever = dimensions.slice().sort((a,b)=>a.score-b.score)[0];
    const strong = dimensions.slice().sort((a,b)=>b.score-a.score)[0];
    const journey = document.createElement('div');
    journey.className='v13-journey';
    journey.innerHTML=`
      <div class="v13-step"><span class="v13-step-no">01 · SEE</span><h3>Know your profile</h3><p>Start with your ${Math.round(overall)} MAXESS score and the five capabilities behind it.</p></div>
      <div class="v13-step"><span class="v13-step-no">02 · USE</span><h3>Exploit your strength</h3><p>Use ${strong ? esc(strong.name) : 'your strongest dimension'} as the foundation for better AI work.</p></div>
      <div class="v13-step"><span class="v13-step-no">03 · BUILD</span><h3>Work your biggest lever</h3><p>Focus on ${lever ? esc(lever.name) : 'your next growth area'} where improvement can create the most upside.</p></div>
      <div class="v13-step"><span class="v13-step-no">04 · REPEAT</span><h3>Turn skill into advantage</h3><p>Create, score, improve and repeat until better AI work becomes your normal way of operating.</p></div>`;
    target.el.querySelector('.mx-wide,.mx-reading')?.appendChild(journey) || target.el.appendChild(journey);
  }

  function addPathways(root) {
    if (root.querySelector('.v13-path-grid')) return;
    const target = findSections(root).find(s=>scoreSection(s.text,['18 naya','18 ai','pathways','masters'])>0);
    if (!target) return;
    const names = ['Naya Writer','Naya Researcher','Naya Strategist','Naya Marketer','Naya Brainstormer','Naya Coder','Naya Designer','Naya Video','Naya Teacher','Naya Analyst','Naya Organizer','Naya Communicator','Naya Planner','Naya Creator','Naya Problem Solver','Naya Image Master','Naya Systems Master','Talk to Naya'];
    const icons = ['✍','⌕','◆','↗','✦','⌘','◈','▶','◎','◌','▦','◉','◇','✺','⊙','✧','⬡','●'];
    const ranked = dimensions.slice().sort((a,b)=>b.score-a.score);
    const six = names.slice(0,6).map((name,i)=>({name, i, basis: ranked[i % Math.max(1,ranked.length)]}));
    const grid = document.createElement('div');
    grid.className='v13-path-grid';
    grid.innerHTML=six.map((p)=>`<article class="v13-path"><span class="v13-path-badge">Recommended</span><div class="v13-path-icon">${icons[p.i]}</div><h3>${p.name}</h3><p>Build stronger ${p.basis ? esc(p.basis.name.toLowerCase()) : 'AI'} capability with a focused specialist workflow.</p></article>`).join('');
    const more = document.createElement('div');
    more.className='v13-view-all';
    more.innerHTML='<button type="button" aria-expanded="false">View all 18 Naya Masters ↓</button>';
    const all = document.createElement('div');
    all.className='v13-path-grid v13-hidden';
    all.style.marginTop='14px';
    all.innerHTML=names.slice(6).map((name,i)=>`<article class="v13-path"><div class="v13-path-icon">${icons[i+6]}</div><h3>${name}</h3><p>A specialist pathway for turning AI capability into useful results.</p></article>`).join('');
    more.querySelector('button').addEventListener('click',e=>{const open=all.classList.toggle('v13-hidden');e.currentTarget.setAttribute('aria-expanded',String(open?'false':'true'));e.currentTarget.textContent=open?'View all 18 Naya Masters ↓':'Hide the additional Naya Masters ↑';});
    const container=target.el.querySelector('.mx-wide,.mx-reading') || target.el;
    container.appendChild(grid);container.appendChild(more);container.appendChild(all);
  }

  function moveCommercialToEnd(root) {
    const all = findSections(root);
    const commercial = all.filter(s=>scoreSection(s.text,['technology should','amplify your human','meaningful ai foundation','ai path','get started','join'])>=2).map(s=>s.el);
    commercial.forEach(el=>{ if (el !== root.querySelector('.mx-hero')) root.appendChild(el); });
  }

  function addChapterMarkers(root) {
    const sections = [...root.querySelectorAll('.v13-report-section')];
    let n = 1;
    sections.forEach(section=>{
      if (section.querySelector('.v13-chapter')) return;
      const head = section.querySelector('.mx-section-head');
      if (!head) return;
      const title = head.querySelector('h2');
      if (!title) return;
      const text = title.textContent.trim().toLowerCase();
      if (/solution|technology should|playground|conversion|cta/.test(text)) return;
      const kicker = document.createElement('div');
      kicker.className='v13-chapter';
      kicker.innerHTML=`<span class="v13-number">${String(n).padStart(2,'0')}</span><div><span class="v13-kicker">MAXESS · PERSONAL REPORT</span><div class="v13-subtitle">${esc(title.textContent.trim())}</div></div>`;
      head.parentNode.insertBefore(kicker,head);
      n++;
    });
  }

  function observeNaya(root) {
    const stage = root.querySelector('.mx-score-orb,.mx-ls-stage');
    if (!stage) return;
    window.addEventListener('maxess:naya:start',()=>stage.classList.add('v13-naya-speaking'));
    window.addEventListener('maxess:naya:stop',()=>stage.classList.remove('v13-naya-speaking'));
  }

  function run() {
    if (document.getElementById(PATCH_ID)) return;
    const root = document.getElementById(ROOT_ID);
    if (!root) return;
    const marker=document.createElement('meta');marker.id=PATCH_ID;marker.name='maxess-v13-execution';marker.content='executed';document.head.appendChild(marker);
    setVars(root);
    addStyles();
    printButton(root);
    heroLabel(root);
    nayaIntro(root);
    enhanceDimensions(root);
    reorderReport(root);
    addPatternVisualization(root);
    addJourney(root);
    addPathways(root);
    moveCommercialToEnd(root);
    addChapterMarkers(root);
    observeNaya(root);
    root.dataset.maxessV13='executed';
    root.dataset.maxessV13Score=String(Math.round(overall));
    console.info('%cMAXESS V13 EXECUTED','color:#b76cff;font-weight:900;font-size:14px', {score:overall,band:bandFor(overall),dimensions:dimensions.map(d=>({name:d.name,score:d.score}))});
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded',()=>setTimeout(run,120));
  else setTimeout(run,120);
})();
