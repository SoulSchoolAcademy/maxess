(() => {
  'use strict';

  /* =========================================================
     MAXESS RESULTS — DATA CONTRACT
     The assessment can hand this page a MAXESS_RESULT object.
     The Results experience remains independent from questions.
  ========================================================= */

  const DEFAULT_RESULT = {
    overall: 84,
    level: 'Advancing',
    dimensions: {
      direction: 91,
      communication: 84,
      evaluation: 78,
      iteration: 72,
      systemsThinking: 88
    },
    strongest: 'direction',
    opportunity: 'iteration',
    assessmentVersion: 'MAXESS-1.0',
    completedAt: null,
    userName: ''
  };

  const DIMENSIONS = [
    {
      key: 'direction',
      label: 'Direction',
      short: 'Direction',
      index: '01',
      description: 'Knowing what you are trying to accomplish before asking AI to act.',
      foundation: 'You can define a destination instead of merely asking for an answer.',
      advanced: 'You turn goals into clear constraints, priorities and success conditions.',
      next: 'Make the desired outcome explicit before every important AI task.'
    },
    {
      key: 'communication',
      label: 'Communication',
      short: 'Communication',
      index: '02',
      description: 'Expressing intent, context, audience and expectations clearly.',
      foundation: 'You can communicate enough context for AI to understand your intent.',
      advanced: 'You shape context and tone so the output feels deliberately directed.',
      next: 'Tell AI what matters, what to avoid and what a successful answer looks like.'
    },
    {
      key: 'evaluation',
      label: 'Evaluation',
      short: 'Evaluation',
      index: '03',
      description: 'Judging whether an AI output is accurate, useful and fit for purpose.',
      foundation: 'You notice obvious quality problems and can recognize a useful answer.',
      advanced: 'You can score an output against explicit standards rather than gut feeling alone.',
      next: 'Define three to five criteria before accepting an important output.'
    },
    {
      key: 'iteration',
      label: 'Iteration',
      short: 'Iteration',
      index: '04',
      description: 'Improving the result through deliberate cycles of feedback and revision.',
      foundation: 'You can ask AI to revise, but the process may stop too early.',
      advanced: 'You treat the first answer as a draft and deliberately improve it.',
      next: 'Never let a high-value first draft be the final draft.'
    },
    {
      key: 'systemsThinking',
      label: 'Systems Thinking',
      short: 'Systems',
      index: '05',
      description: 'Connecting prompts, tools, people, workflows and outputs into a repeatable system.',
      foundation: 'You see beyond isolated prompts and recognize useful sequences.',
      advanced: 'You build repeatable workflows that compound value over time.',
      next: 'Turn successful one-off processes into reusable systems.'
    }
  ];

  const METHOD = [
    ['KNOW', 'Understand the real goal, context, audience and constraints.'],
    ['TELL', 'Give the machine the information and direction it needs.'],
    ['ASK', 'Request the specific transformation or decision you need.'],
    ['CREATE', 'Let AI produce a useful first version.'],
    ['SCORE', 'Judge the output against clear standards.'],
    ['IMPROVE', 'Give targeted feedback and run another pass.'],
    ['REPEAT', 'Keep the loop moving until the result earns its place.']
  ];

  const AUDIO = {
    foundation: '',
    developing: '',
    advancing: '',
    mastering: ''
  };

  const state = {
    result: null,
    selectedDimension: 'direction',
    playing: false,
    observer: null
  };

  const $ = (selector, root = document) => root.querySelector(selector);
  const $$ = (selector, root = document) => [...root.querySelectorAll(selector)];

  function clamp(value, min = 0, max = 100) {
    const n = Number(value);
    if (!Number.isFinite(n)) return min;
    return Math.min(max, Math.max(min, Math.round(n)));
  }

  function normalizeResult(input) {
    const raw = input && typeof input === 'object' ? input : {};
    const dims = raw.dimensions && typeof raw.dimensions === 'object' ? raw.dimensions : {};
    const result = {
      ...DEFAULT_RESULT,
      ...raw,
      overall: clamp(raw.overall ?? DEFAULT_RESULT.overall),
      dimensions: {
        direction: clamp(dims.direction ?? DEFAULT_RESULT.dimensions.direction),
        communication: clamp(dims.communication ?? DEFAULT_RESULT.dimensions.communication),
        evaluation: clamp(dims.evaluation ?? DEFAULT_RESULT.dimensions.evaluation),
        iteration: clamp(dims.iteration ?? DEFAULT_RESULT.dimensions.iteration),
        systemsThinking: clamp(dims.systemsThinking ?? DEFAULT_RESULT.dimensions.systemsThinking)
      }
    };

    const strongest = DIMENSIONS.reduce((best, d) => {
      return result.dimensions[d.key] > result.dimensions[best] ? d.key : best;
    }, 'direction');

    const weakest = DIMENSIONS.reduce((best, d) => {
      return result.dimensions[d.key] < result.dimensions[best] ? d.key : best;
    }, 'direction');

    if (!raw.strongest || !result.dimensions[raw.strongest]) result.strongest = strongest;
    if (!raw.opportunity || !result.dimensions[raw.opportunity]) result.opportunity = weakest;
    result.level = getLevel(result.overall);
    return result;
  }

  function getLevel(score) {
    if (score >= 90) return 'Mastering';
    if (score >= 75) return 'Advancing';
    if (score >= 55) return 'Developing';
    return 'Foundation';
  }

  function getDimension(key) {
    return DIMENSIONS.find(d => d.key === key) || DIMENSIONS[0];
  }

  function getDimensionLevel(score) {
    return getLevel(score).toUpperCase();
  }

  function getStoredResult() {
    const candidates = [];

    try { candidates.push(window.MAXESS_RESULT); } catch (_) {}

    try {
      const session = sessionStorage.getItem('MAXESS_RESULT');
      if (session) candidates.push(JSON.parse(session));
    } catch (_) {}

    try {
      const local = localStorage.getItem('MAXESS_RESULT');
      if (local) candidates.push(JSON.parse(local));
    } catch (_) {}

    try {
      const params = new URLSearchParams(location.search);
      const encoded = params.get('result');
      if (encoded) candidates.push(JSON.parse(decodeURIComponent(encoded)));
    } catch (_) {}

    const candidate = candidates.find(value => value && typeof value === 'object');
    return normalizeResult(candidate || DEFAULT_RESULT);
  }

  function exposeBridge() {
    window.MAXESS_RESULTS = {
      version: '1.0',
      getResult: () => state.result,
      setResult: (next) => {
        state.result = normalizeResult(next);
        renderAll();
      },
      dimensions: DIMENSIONS.map(d => ({ ...d })),
      audio: { ...AUDIO }
    };
  }

  function scoreCopy(score) {
    if (score >= 90) return 'You are operating with a highly developed AI mastery process. The opportunity now is refinement, consistency and teaching the system to compound your strengths.';
    if (score >= 75) return 'You already know how to work with AI deliberately. Your next gains come from turning good instincts into a repeatable, measurable process.';
    if (score >= 55) return 'You have useful AI instincts. The next step is to make your thinking more deliberate so AI can become a reliable extension of your capability.';
    return 'You are building your foundation. The fastest gains will come from learning to define the goal, communicate the context and judge the result.';
  }

  function renderScore() {
    const r = state.result;
    $('#overallScore').textContent = r.overall;
    $('#overallLevel').textContent = r.level.toUpperCase();
    $('#scoreMeaning').textContent = scoreCopy(r.overall);
    $('#radarCenterScore').textContent = r.overall;
    $('#statementCopy').textContent = buildStatement(r);
  }

  function buildStatement(r) {
    const strongest = getDimension(r.strongest).label.toLowerCase();
    const opportunity = getDimension(r.opportunity).label.toLowerCase();
    return `Your profile shows a meaningful ${r.level.toLowerCase()} foundation. ${strongest.charAt(0).toUpperCase() + strongest.slice(1)} is already a natural advantage. Your next gains come from deliberately strengthening ${opportunity}, because that is where additional effort can create the greatest return.`;
  }

  function renderDimensions() {
    const r = state.result;
    const grid = $('#dimensionGrid');
    const details = $('#dimensionDetails');
    grid.innerHTML = '';
    details.innerHTML = '';

    DIMENSIONS.forEach((d, index) => {
      const score = r.dimensions[d.key];
      const card = document.createElement('button');
      card.type = 'button';
      card.className = `dimension-card${state.selectedDimension === d.key ? ' active' : ''}`;
      card.dataset.dimension = d.key;
      card.innerHTML = `
        <span class="index">${d.index} / DIMENSION</span>
        <strong class="dimension-score">${score}</strong>
        <h3>${d.label}</h3>
        <p class="desc">${d.description}</p>
        <span class="mini-gauge"><span style="width:${score}%"></span></span>
      `;
      card.addEventListener('click', () => selectDimension(d.key));
      grid.appendChild(card);

      const row = document.createElement('article');
      row.className = 'detail-row';
      row.id = `detail-${d.key}`;
      row.innerHTML = `
        <div class="detail-name">${d.label}</div>
        <div class="detail-score">${score}</div>
        <div class="detail-meter" aria-label="${d.label} score ${score} out of 100"><span style="width:${score}%"></span></div>
        <div class="detail-level">${getDimensionLevel(score)}</div>
      `;
      details.appendChild(row);
    });
  }

  function selectDimension(key) {
    state.selectedDimension = key;
    $$('.dimension-card').forEach(card => card.classList.toggle('active', card.dataset.dimension === key));
    const target = document.getElementById(`detail-${key}`);
    if (target) {
      target.scrollIntoView({ behavior: 'smooth', block: 'center' });
      target.animate([{ boxShadow: '0 0 0 rgba(139,92,255,0)' }, { boxShadow: '0 0 35px rgba(139,92,255,.18)' }, { boxShadow: '0 0 0 rgba(139,92,255,0)' }], { duration: 900 });
    }
  }

  function renderFeatureSections() {
    const r = state.result;
    const strongest = getDimension(r.strongest);
    const opportunity = getDimension(r.opportunity);
    const strongestScore = r.dimensions[r.strongest];
    const opportunityScore = r.dimensions[r.opportunity];

    $('#capabilityTitle').textContent = strongest.label;
    $('#capabilityScore').textContent = strongestScore;
    $('#capabilityBadge').textContent = strongestScore;
    $('#capabilityMeter').style.width = `${strongestScore}%`;
    $('#capabilityText').textContent = strongest.advanced;

    $('#opportunityTitle').textContent = opportunity.label;
    $('#opportunityScore').textContent = opportunityScore;
    $('#opportunityText').textContent = opportunity.next;

    $('#whyStrength').textContent = `${strongest.label} is currently your strongest dimension at ${strongestScore}. ${strongest.advanced}`;
    $('#whyGap').textContent = `${opportunity.label} is currently your lowest leverage dimension at ${opportunityScore}. That gap is not a verdict — it is an opportunity.`;
    $('#whyMove').textContent = buildWhyMove(opportunity);
  }

  function buildWhyMove(opportunity) {
    const moves = {
      direction: 'Before every important AI task, write the destination in one sentence and define what success looks like.',
      communication: 'Add context, audience, constraints and examples instead of asking AI to guess what you mean.',
      evaluation: 'Create a short scorecard before accepting an output so quality becomes visible instead of subjective.',
      iteration: 'Treat every meaningful answer as a draft. Score it, identify the largest gap and run another pass.',
      systemsThinking: 'Capture successful workflows and turn them into reusable systems instead of repeating the same work manually.'
    };
    return moves[opportunity.key] || moves.iteration;
  }

  function renderPathway() {
    const r = state.result;
    const opportunity = getDimension(r.opportunity);
    const strongest = getDimension(r.strongest);
    const path = [
      {
        n: '01',
        title: `Use ${strongest.label}`,
        text: `Make your existing strength your starting point. Before an important AI task, deliberately use your ${strongest.label.toLowerCase()} ability to establish the outcome.`,
        action: 'START WITH YOUR ADVANTAGE'
      },
      {
        n: '02',
        title: `Train ${opportunity.label}`,
        text: opportunity.next,
        action: 'BUILD THE NEW HABIT'
      },
      {
        n: '03',
        title: 'Run the loop',
        text: 'Use KNOW → TELL → ASK → CREATE → SCORE → IMPROVE → REPEAT until the result earns your approval.',
        action: 'MAKE IT REPEATABLE'
      }
    ];

    $('#pathway').innerHTML = path.map(item => `
      <article class="path-card">
        <div class="path-number">${item.n}</div>
        <h3>${item.title}</h3>
        <p>${item.text}</p>
        <span class="action">${item.action}</span>
      </article>
    `).join('');
  }

  function renderMethod() {
    $('#methodLoop').innerHTML = METHOD.map(([label]) => `<button type="button" class="method-node"><span>${label}</span></button>`).join('');
    const nodes = $$('.method-node');
    nodes.forEach((node, index) => {
      node.setAttribute('aria-label', `${METHOD[index][0]} — ${METHOD[index][1]}`);
      node.addEventListener('click', () => showMethod(index));
    });
  }

  function showMethod(index) {
    const [label, explanation] = METHOD[index];
    const existing = document.querySelector('.method-popover');
    if (existing) existing.remove();
    const pop = document.createElement('div');
    pop.className = 'method-popover';
    pop.innerHTML = `<strong>${label}</strong><span>${explanation}</span>`;
    pop.style.cssText = 'position:fixed;left:50%;bottom:28px;transform:translateX(-50%);z-index:20;max-width:min(520px,calc(100% - 30px));padding:14px 18px;border:1px solid rgba(181,140,255,.35);border-radius:14px;background:#0c0a11;color:#fff;box-shadow:0 20px 55px rgba(0,0,0,.6);display:flex;gap:12px;align-items:center;font-size:12px;line-height:1.5';
    document.body.appendChild(pop);
    setTimeout(() => pop.remove(), 3200);
  }

  function drawRadar() {
    const canvas = $('#radarCanvas');
    if (!canvas) return;
    const rect = canvas.getBoundingClientRect();
    const size = Math.max(260, Math.floor(Math.min(rect.width, rect.height)));
    const dpr = window.devicePixelRatio || 1;
    canvas.width = size * dpr;
    canvas.height = size * dpr;
    const ctx = canvas.getContext('2d');
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    const cx = size / 2;
    const cy = size / 2;
    const radius = size * .34;
    const count = DIMENSIONS.length;
    const values = DIMENSIONS.map(d => state.result.dimensions[d.key] / 100);

    ctx.clearRect(0, 0, size, size);
    for (let ring = 1; ring <= 4; ring++) {
      const rr = radius * ring / 4;
      ctx.beginPath();
      DIMENSIONS.forEach((_, i) => {
        const a = -Math.PI / 2 + i * Math.PI * 2 / count;
        const x = cx + Math.cos(a) * rr;
        const y = cy + Math.sin(a) * rr;
        if (i === 0) ctx.moveTo(x, y); else ctx.lineTo(x, y);
      });
      ctx.closePath();
      ctx.strokeStyle = ring === 4 ? 'rgba(181,140,255,.25)' : 'rgba(255,255,255,.07)';
      ctx.lineWidth = 1;
      ctx.stroke();
    }

    DIMENSIONS.forEach((d, i) => {
      const a = -Math.PI / 2 + i * Math.PI * 2 / count;
      ctx.beginPath();
      ctx.moveTo(cx, cy);
      ctx.lineTo(cx + Math.cos(a) * radius, cy + Math.sin(a) * radius);
      ctx.strokeStyle = 'rgba(255,255,255,.09)';
      ctx.stroke();
    });

    ctx.beginPath();
    values.forEach((value, i) => {
      const a = -Math.PI / 2 + i * Math.PI * 2 / count;
      const x = cx + Math.cos(a) * radius * value;
      const y = cy + Math.sin(a) * radius * value;
      if (i === 0) ctx.moveTo(x, y); else ctx.lineTo(x, y);
    });
    ctx.closePath();
    const fill = ctx.createRadialGradient(cx, cy, 10, cx, cy, radius);
    fill.addColorStop(0, 'rgba(189,157,255,.24)');
    fill.addColorStop(1, 'rgba(101,53,210,.05)');
    ctx.fillStyle = fill;
    ctx.fill();
    ctx.strokeStyle = 'rgba(193,162,255,.88)';
    ctx.lineWidth = 2;
    ctx.shadowColor = 'rgba(139,92,255,.45)';
    ctx.shadowBlur = 16;
    ctx.stroke();
    ctx.shadowBlur = 0;

    values.forEach((value, i) => {
      const a = -Math.PI / 2 + i * Math.PI * 2 / count;
      const x = cx + Math.cos(a) * radius * value;
      const y = cy + Math.sin(a) * radius * value;
      ctx.beginPath();
      ctx.arc(x, y, 5, 0, Math.PI * 2);
      ctx.fillStyle = '#d8c6ff';
      ctx.fill();
      ctx.strokeStyle = '#5d2dbb';
      ctx.lineWidth = 2;
      ctx.stroke();
    });

    DIMENSIONS.forEach((d, i) => {
      const a = -Math.PI / 2 + i * Math.PI * 2 / count;
      const x = cx + Math.cos(a) * (radius + 35);
      const y = cy + Math.sin(a) * (radius + 35);
      ctx.fillStyle = '#9f98aa';
      ctx.font = '700 9px Inter, sans-serif';
      ctx.textAlign = x < cx - 10 ? 'right' : x > cx + 10 ? 'left' : 'center';
      ctx.textBaseline = y < cy ? 'bottom' : 'top';
      ctx.fillText(d.short.toUpperCase(), x, y);
    });
  }

  function configureAudio() {
    const audio = $('#nayaAudio');
    const header = $('#nayaHeaderButton');
    const main = $('#nayaMainButton');
    const label = $('#nayaMainLabel');
    const tier = state.result.level.toLowerCase();
    const source = AUDIO[tier] || '';
    $('#nayaTier').textContent = state.result.level.toUpperCase();

    if (source) {
      audio.src = source;
      main.disabled = false;
      main.title = `Play your ${state.result.level} Naya report`;
    } else {
      main.disabled = true;
      main.title = 'Naya audio recording not connected yet';
      label.textContent = 'Naya audio coming online';
      header.title = 'Naya audio recording not connected yet';
    }

    function toggle() {
      if (!source) return;
      if (audio.paused) audio.play().catch(() => {}); else audio.pause();
    }

    main.addEventListener('click', toggle);
    header.addEventListener('click', toggle);
    audio.addEventListener('play', () => {
      state.playing = true;
      main.classList.add('playing');
      header.classList.add('playing');
      label.textContent = 'Pause Naya';
    });
    audio.addEventListener('pause', () => {
      state.playing = false;
      main.classList.remove('playing');
      header.classList.remove('playing');
      if (source) label.textContent = 'Listen to Naya';
    });
    audio.addEventListener('ended', () => {
      state.playing = false;
      main.classList.remove('playing');
      header.classList.remove('playing');
      if (source) label.textContent = 'Listen again';
    });
  }

  function setupReveal() {
    const items = $$('.reveal');
    if (!('IntersectionObserver' in window)) {
      items.forEach(item => item.classList.add('visible'));
      return;
    }
    state.observer = new IntersectionObserver(entries => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible');
          state.observer.unobserve(entry.target);
        }
      });
    }, { threshold: .12, rootMargin: '0px 0px -30px 0px' });
    items.forEach(item => state.observer.observe(item));
  }

  function setupKeyboardNavigation() {
    document.addEventListener('keydown', event => {
      if (event.key === 'Escape') {
        const pop = document.querySelector('.method-popover');
        if (pop) pop.remove();
      }
      if (event.key >= '1' && event.key <= '5' && !event.metaKey && !event.ctrlKey) {
        const index = Number(event.key) - 1;
        const dimension = DIMENSIONS[index];
        if (dimension) selectDimension(dimension.key);
      }
    });
  }

  function setupResize() {
    let frame = 0;
    window.addEventListener('resize', () => {
      cancelAnimationFrame(frame);
      frame = requestAnimationFrame(drawRadar);
    }, { passive: true });
  }

  function renderAll() {
    renderScore();
    renderDimensions();
    renderFeatureSections();
    renderPathway();
    renderMethod();
    drawRadar();
    configureAudio();
  }

  function init() {
    state.result = getStoredResult();
    exposeBridge();
    renderAll();
    setupReveal();
    setupKeyboardNavigation();
    setupResize();

    window.dispatchEvent(new CustomEvent('maxess:results-ready', {
      detail: { result: state.result }
    }));

    console.info('[MAXESS Results] Ready', {
      score: state.result.overall,
      level: state.result.level,
      dimensions: state.result.dimensions
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init, { once: true });
  } else {
    init();
  }
})();
