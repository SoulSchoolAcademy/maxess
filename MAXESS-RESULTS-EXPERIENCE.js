/*
 * MAXESS RESULTS — WHOLE-SYSTEM AAA PRESENTATION ENGINE
 *
 * Purpose:
 *   Render the complete Results interpretation experience from one
 *   authoritative MAXESS_RESULT payload while preserving the downstream
 *   NayaNET foundation that follows this Results surface.
 *
 * Architecture:
 *   Result Contract → normalize → interpret → render → interact
 *
 * Hard rules:
 *   - Never calculate a new assessment score.
 *   - Never invent production personalization.
 *   - Never scrape the DOM for result data.
 *   - Never require animation, audio, or hover for meaning.
 *   - Preserve the NayaNET foundation outside this Results root.
 */
(function MAXESSResultsAAA(window, document) {
  'use strict';

  var ROOT_ID = 'maxess-results-10';
  var VERSION = 'MAXESS-RESULTS-WHOLE-SYSTEM-AAA-1.0';

  var DIMENSIONS = [
    'Direction',
    'Communication',
    'Evaluation',
    'Iteration',
    'Systems Thinking'
  ];

  var DIMENSION_META = {
    'Direction': {
      color: '#ff9d3d',
      icon: '↗',
      archetype: 'The Director',
      meaning: 'Knowing what you want AI to accomplish and defining the outcome before the work begins.',
      action: 'Define the outcome, audience, constraints and success test before asking AI to create.'
    },
    'Communication': {
      color: '#f4d34f',
      icon: '◌',
      archetype: 'The Translator',
      meaning: 'Turning intent, context and human nuance into information AI can actually use.',
      action: 'Give AI the context, audience, examples and constraints that shape a useful answer.'
    },
    'Evaluation': {
      color: '#39df91',
      icon: '✓',
      archetype: 'The Judge',
      meaning: 'Knowing whether an AI result is actually good, useful, accurate and fit for purpose.',
      action: 'Score important outputs against explicit criteria instead of accepting the first plausible answer.'
    },
    'Iteration': {
      color: '#46b7ff',
      icon: '↻',
      archetype: 'The Refiner',
      meaning: 'Improving a result deliberately rather than treating the first version as the finished version.',
      action: 'Create a deliberate create → score → improve loop and preserve what already works.'
    },
    'Systems Thinking': {
      color: '#a66cff',
      icon: '⌘',
      archetype: 'The Architect',
      meaning: 'Seeing how individual AI interactions can become repeatable systems, workflows and leverage.',
      action: 'Turn repeated work into reusable structures, rules, workflows and connected capabilities.'
    }
  };

  var PATHWAYS = [
    ['Writing & Communication', 'Direction, Communication', 'Turn ideas into clear words, instructions and decisions.'],
    ['Research & Information', 'Direction, Evaluation', 'Find, compare and synthesize useful information.'],
    ['Brainstorming & Ideas', 'Direction, Iteration', 'Expand possibilities without losing the real goal.'],
    ['Content Creation', 'Communication, Iteration', 'Create useful human content faster and better.'],
    ['Business & Strategy', 'Direction, Evaluation, Systems Thinking', 'Turn insight into positioning, offers and plans.'],
    ['Marketing & Sales', 'Communication, Evaluation', 'Make value understandable and action easier.'],
    ['Learning & Education', 'Communication, Iteration', 'Use AI as tutor, teacher and thinking partner.'],
    ['Coding & Software', 'Direction, Iteration, Systems Thinking', 'Build, debug and improve software with AI.'],
    ['Images & Visual Creation', 'Direction, Communication', 'Turn concepts into visual communication.'],
    ['Video & Media', 'Communication, Iteration', 'Plan, script and package media.'],
    ['Documents & Presentations', 'Communication, Evaluation', 'Transform raw thinking into polished deliverables.'],
    ['Data & Analysis', 'Evaluation, Systems Thinking', 'Use evidence and models to make better decisions.'],
    ['Productivity & Planning', 'Direction, Systems Thinking', 'Turn intention into organized execution.'],
    ['Career & Professional Development', 'Direction, Communication', 'Build skills, positioning and opportunity.'],
    ['Personal Decision-Making', 'Evaluation, Communication', 'Think through choices with more clarity.'],
    ['Creative Work', 'Direction, Iteration', 'Explore, shape and finish original work.'],
    ['Automation & Systems', 'Systems Thinking, Iteration', 'Connect repeated work into reliable systems.'],
    ['Advanced AI Work', 'Evaluation, Systems Thinking, Iteration', 'Orchestrate models, agents, tools and evaluation.' ]
  ];

  var NAYA_MASTERS = [
    ['Naya Director', 'Turns goals into clear outcomes, plans and instructions.', 'Direction'],
    ['Naya Oscar', 'Challenges quality, assumptions, weaknesses and blind spots.', 'Evaluation'],
    ['Naya Architect', 'Connects individual tasks into intelligent systems.', 'Systems Thinking'],
    ['Naya Writer', 'Shapes ideas into clear, human communication.', 'Communication'],
    ['Naya Researcher', 'Finds, compares and synthesizes useful information.', 'Evaluation'],
    ['Naya Ideator', 'Expands possibilities while protecting the objective.', 'Iteration'],
    ['Naya Strategist', 'Turns information into decisions and direction.', 'Direction'],
    ['Naya Marketer', 'Makes value understandable and action easier.', 'Communication'],
    ['Naya Teacher', 'Turns complexity into learning and understanding.', 'Communication'],
    ['Naya Developer', 'Builds, debugs and improves software.', 'Iteration'],
    ['Naya Designer', 'Turns concepts into useful visual experiences.', 'Communication'],
    ['Naya Media', 'Plans, scripts and packages media.', 'Communication'],
    ['Naya Publisher', 'Transforms thinking into polished deliverables.', 'Evaluation'],
    ['Naya Analyst', 'Uses evidence to reveal useful patterns.', 'Evaluation'],
    ['Naya Planner', 'Converts intention into organized execution.', 'Direction'],
    ['Naya Automator', 'Connects repeated work into reliable workflows.', 'Systems Thinking'],
    ['Naya Advanced', 'Coordinates advanced models, agents and evaluation.', 'Systems Thinking'],
    ['Naya Growth', 'Connects capability to adoption, action and sustainable value.', 'Direction']
  ];

  var COLORS = ['#ff9d3d', '#f4d34f', '#39df91', '#46b7ff', '#a66cff'];

  function esc(value) {
    return String(value == null ? '' : value).replace(/[&<>\"']/g, function (char) {
      return {
        '&': '&amp;',
        '<': '&lt;',
        '>': '&gt;',
        '\"': '&quot;',
        "'": '&#39;'
      }[char];
    });
  }

  function clamp(value) {
    var n = Number(value);
    if (!Number.isFinite(n)) return 0;
    return Math.max(0, Math.min(100, n));
  }

  function band(score) {
    if (score <= 50) return 'Foundation';
    if (score <= 75) return 'Developing';
    if (score <= 90) return 'Advancing';
    return 'Mastering';
  }

  function bandDescription(score) {
    if (score <= 50) return 'You are building the foundations that make strong AI work possible.';
    if (score <= 75) return 'You have useful capability in place and a clear path to strengthen it.';
    if (score <= 90) return 'You are operating beyond the basics and can now compound your capability.';
    return 'You are operating at a high level and are ready to turn capability into mastery.';
  }

  function normalizeResult(raw) {
    if (!raw || typeof raw !== 'object') return null;

    var rawDimensions = Array.isArray(raw.dimensions) ? raw.dimensions : [];
    var byName = {};

    rawDimensions.forEach(function (dimension) {
      if (!dimension) return;
      byName[String(dimension.name || '').toLowerCase()] = dimension;
    });

    var dimensions = DIMENSIONS.map(function (name) {
      var source = byName[name.toLowerCase()] || rawDimensions[DIMENSIONS.indexOf(name)] || {};
      return {
        id: source.id || name.toLowerCase().replace(/\s+/g, '-'),
        name: name,
        score: clamp(source.score != null ? source.score : source.value),
        description: source.description || '',
        evidence: source.evidence || ''
      };
    });

    var overall = raw.overallScore != null ? raw.overallScore : raw.score;
    if (overall == null && dimensions.some(function (d) { return d.score > 0; })) {
      overall = dimensions.reduce(function (sum, d) { return sum + d.score; }, 0) / dimensions.length;
    }

    var strongest = dimensions.slice().sort(function (a, b) { return b.score - a.score; })[0];
    var opportunity = dimensions.slice().sort(function (a, b) { return a.score - b.score; })[0];
    var spread = strongest && opportunity ? strongest.score - opportunity.score : 0;

    return {
      raw: raw,
      overall: clamp(overall),
      band: band(clamp(overall)),
      dimensions: dimensions,
      strongest: strongest,
      opportunity: opportunity,
      spread: spread,
      profile: raw.profile || raw.archetype || null,
      narrative: raw.narrative || raw.interpretation || null,
      responses: Array.isArray(raw.responses) ? raw.responses : [],
      version: raw.assessmentVersion || raw.version || null,
      date: raw.completedAt || raw.date || null
    };
  }

  function getRoot() {
    return document.getElementById(ROOT_ID);
  }

  function getRawResult() {
    return window.MAXESS_RESULT || null;
  }

  function evidenceDescription(dimension) {
    var meta = DIMENSION_META[dimension.name];
    return dimension.description || meta.meaning;
  }

  function opportunityLanguage(result) {
    var d = result.opportunity;
    var m = DIMENSION_META[d.name];
    return 'Your clearest leverage point is ' + d.name + '. Strengthening this does not mean starting over — it gives the capabilities you already have a stronger structure to work with.';
  }

  function patternLanguage(result) {
    var high = result.strongest;
    var low = result.opportunity;
    var spread = Math.round(result.spread);

    if (spread <= 8) {
      return 'Your five dimensions are relatively balanced. That matters because your next gains can come from sharpening the whole system rather than rescuing one weak point.';
    }
    if (spread <= 20) {
      return high.name + ' leads your profile while ' + low.name + ' has the most room to catch up. That gives you a clear place to focus without losing the advantage you already have.';
    }
    return 'There is a meaningful gap between ' + high.name + ' and ' + low.name + '. That imbalance is useful information: your fastest progress may come from strengthening the capability that lets your strongest capability travel further.';
  }

  function nextMove(result) {
    var d = result.opportunity;
    var meta = DIMENSION_META[d.name];
    return {
      title: 'Practice ' + d.name + ' on one real task this week.',
      body: meta.action,
      dimension: d.name
    };
  }

  function relevanceFor(pathway, result) {
    var names = pathway[1].split(',').map(function (x) { return x.trim(); });
    var total = 0;
    names.forEach(function (name) {
      var d = result.dimensions.find(function (item) { return item.name === name; });
      if (d) total += d.score;
    });
    var average = names.length ? total / names.length : 0;
    var opportunityBoost = names.indexOf(result.opportunity.name) >= 0 ? 8 : 0;
    var strengthBoost = names.indexOf(result.strongest.name) >= 0 ? 5 : 0;
    return Math.round(Math.min(100, average + opportunityBoost + strengthBoost));
  }

  function sortedPathways(result) {
    return PATHWAYS.map(function (item, index) {
      return {
        index: index,
        name: item[0],
        dimensions: item[1],
        description: item[2],
        relevance: relevanceFor(item, result)
      };
    }).sort(function (a, b) { return b.relevance - a.relevance; });
  }

  function svgFingerprint(result) {
    var cx = 300;
    var cy = 300;
    var radius = 210;

    function point(score, index, scale) {
      var angle = -Math.PI / 2 + index * (Math.PI * 2 / 5);
      var r = radius * (score / 100) * (scale || 1);
      return [cx + Math.cos(angle) * r, cy + Math.sin(angle) * r];
    }

    function outerPoint(index, scale) {
      var angle = -Math.PI / 2 + index * (Math.PI * 2 / 5);
      var r = radius * (scale || 1);
      return [cx + Math.cos(angle) * r, cy + Math.sin(angle) * r];
    }

    function pointsToString(points) {
      return points.map(function (p) { return p[0].toFixed(1) + ',' + p[1].toFixed(1); }).join(' ');
    }

    var outer = DIMENSIONS.map(function (_, i) { return outerPoint(i, 1); });
    var mid = DIMENSIONS.map(function (_, i) { return outerPoint(i, .66); });
    var inner = DIMENSIONS.map(function (_, i) { return outerPoint(i, .33); });
    var data = result.dimensions.map(function (d, i) { return point(d.score, i, 1); });

    var axes = outer.map(function (p) {
      return '<line x1="300" y1="300" x2="' + p[0].toFixed(1) + '" y2="' + p[1].toFixed(1) + '" />';
    }).join('');

    var dots = data.map(function (p, i) {
      return '<circle cx="' + p[0].toFixed(1) + '" cy="' + p[1].toFixed(1) + '" r="8" fill="' + COLORS[i] + '" stroke="#fff" stroke-width="3" />';
    }).join('');

    return '<svg class="mx-signature-svg" viewBox="0 0 600 600" role="img" aria-labelledby="mx-signature-title mx-signature-desc">' +
      '<title id="mx-signature-title">Your five-dimension AI capability signature</title>' +
      '<desc id="mx-signature-desc">A visual fingerprint of Direction, Communication, Evaluation, Iteration and Systems Thinking scores.</desc>' +
      '<polygon points="' + pointsToString(outer) + '" class="mx-grid-line" />' +
      '<polygon points="' + pointsToString(mid) + '" class="mx-grid-line" />' +
      '<polygon points="' + pointsToString(inner) + '" class="mx-grid-line" />' +
      axes +
      '<polygon points="' + pointsToString(data) + '" class="mx-signature-shape" />' +
      dots +
      '</svg>';
  }

  function orb(score) {
    var size = Math.round(420 + score * 1.35);
    var hue = score <= 50 ? '#ff4b55' : score <= 64 ? '#ff9d3d' : score <= 74 ? '#f4d34f' : score <= 84 ? '#39df91' : score <= 89 ? '#46b7ff' : score <= 94 ? '#a66cff' : '#ef4bc8';
    var second = score <= 50 ? '#ff9d3d' : score <= 64 ? '#f4d34f' : score <= 74 ? '#39df91' : score <= 84 ? '#46b7ff' : score <= 94 ? '#a66cff' : '#ef4bc8';
    return '<div class="mx-orb" style="--orb-size:' + size + 'px;--orb-a:' + hue + ';--orb-b:' + second + '" aria-hidden="true">' +
      '<span class="mx-orbit mx-orbit-a"></span>' +
      '<span class="mx-orbit mx-orbit-b"></span>' +
      '<span class="mx-orbit mx-orbit-c"></span>' +
      '<span class="mx-orb-core"></span>' +
      '<span class="mx-orb-energy e1"></span>' +
      '<span class="mx-orb-energy e2"></span>' +
      '<span class="mx-orb-energy e3"></span>' +
      '<span class="mx-orb-score">' + Math.round(score) + '<small>/100</small></span>' +
      '</div>';
  }

  function styles() {
    return '<style id="maxess-results-whole-system-aaa-css">' +
      ':root{--mx-black:#030305;--mx-ink:#fff;--mx-soft:rgba(255,255,255,.72);--mx-muted:rgba(255,255,255,.48);--mx-purple:#a66cff;--mx-blue:#46b7ff;--mx-green:#39df91;--mx-gold:#f4d34f;--mx-max:1680px;--mx-read:900px;--mx-ease:cubic-bezier(.2,.8,.2,1)}' +
      '#maxess-results-10{width:100vw!important;max-width:none!important;margin-left:calc(50% - 50vw)!important;overflow:hidden!important;color:#fff!important;background:#030305!important;font-family:Inter,ui-sans-serif,system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif!important;line-height:1.5;isolation:isolate}' +
      '#maxess-results-10 *{box-sizing:border-box}' +
      '#maxess-results-10 a,#maxess-results-10 button{font:inherit}' +
      '#maxess-results-10 button{cursor:pointer}' +
      '#maxess-results-10 .mx-wrap{width:min(var(--mx-max),100%);margin:auto;padding-inline:clamp(22px,4vw,74px)}' +
      '#maxess-results-10 .mx-read{width:min(var(--mx-read),100%);margin:auto}' +
      '#maxess-results-10 .mx-section{position:relative;padding:clamp(76px,8vw,132px) 0;scroll-margin-top:30px}' +
      '#maxess-results-10 .mx-eyebrow{display:inline-flex;align-items:center;gap:10px;font-size:11px;font-weight:900;letter-spacing:.18em;text-transform:uppercase;color:#bfa5ff}' +
      '#maxess-results-10 .mx-eyebrow:before{content:"";width:30px;height:1px;background:linear-gradient(90deg,currentColor,transparent)}' +
      '#maxess-results-10 h1,#maxess-results-10 h2,#maxess-results-10 h3,#maxess-results-10 p{margin-top:0}' +
      '#maxess-results-10 h2{font-size:clamp(38px,5.5vw,78px);line-height:.95;letter-spacing:-.055em;margin:12px 0 18px}' +
      '#maxess-results-10 h3{letter-spacing:-.025em}' +
      '#maxess-results-10 .mx-copy{max-width:820px;color:var(--mx-soft);font-size:clamp(17px,1.45vw,21px);line-height:1.62}' +
      '#maxess-results-10 .mx-center{text-align:center}' +
      '#maxess-results-10 .mx-dark{background:#030305;color:#fff}' +
      '#maxess-results-10 .mx-violet{background:radial-gradient(circle at 50% 0,rgba(166,108,255,.16),transparent 46%),#0b0611;color:#fff}' +
      '#maxess-results-10 .mx-light{background:#fff;color:#111}' +
      '#maxess-results-10 .mx-light .mx-copy{color:#555}' +
      '#maxess-results-10 .mx-cream{background:#f5f0e6;color:#171317}' +
      '#maxess-results-10 .mx-emerald{background:linear-gradient(180deg,#03110d,#071b16);color:#fff}' +
      '#maxess-results-10 .mx-gold{background:linear-gradient(180deg,#181205,#f4d34f0a),#171109;color:#fff}' +
      '#maxess-results-10 .mx-blue{background:radial-gradient(circle at 50% 0,rgba(70,183,255,.15),transparent 48%),#040b13;color:#fff}' +
      '#maxess-results-10 .mx-hero{min-height:min(900px,96vh);display:flex;align-items:center;background:radial-gradient(circle at 50% 34%,rgba(166,108,255,.22),transparent 32%),radial-gradient(circle at 20% 80%,rgba(70,183,255,.08),transparent 30%),linear-gradient(180deg,#020204,#09050e 72%,#030305);overflow:hidden}' +
      '#maxess-results-10 .mx-hero-grid{display:grid;grid-template-columns:1fr minmax(380px,620px) 1fr;align-items:center;gap:clamp(20px,4vw,70px)}' +
      '#maxess-results-10 .mx-hero-copy{align-self:center}' +
      '#maxess-results-10 .mx-hero-copy h1{font-size:clamp(40px,5vw,76px);line-height:.95;letter-spacing:-.06em;margin:14px 0}' +
      '#maxess-results-10 .mx-hero-copy p{max-width:520px;color:var(--mx-soft);font-size:clamp(17px,1.4vw,20px);line-height:1.55}' +
      '#maxess-results-10 .mx-hero-center{text-align:center}' +
      '#maxess-results-10 .mx-orb{position:relative;width:min(var(--orb-size),46vw);min-width:380px;aspect-ratio:1;margin:auto;border-radius:50%;display:grid;place-items:center;background:radial-gradient(circle at 34% 25%,rgba(255,255,255,.34),transparent 9%),radial-gradient(circle at 50% 48%,color-mix(in srgb,var(--orb-a) 55%,#12091d),#10071a 45%,#030205 76%);box-shadow:0 0 0 1px rgba(255,255,255,.18),inset 0 0 110px color-mix(in srgb,var(--orb-a) 22%,transparent),0 40px 120px rgba(0,0,0,.68),0 0 130px color-mix(in srgb,var(--orb-a) 25%,transparent);transition:filter .5s ease,transform .5s ease}' +
      '#maxess-results-10 .mx-orb:before{content:"";position:absolute;inset:5%;border-radius:50%;border:1px solid color-mix(in srgb,var(--orb-a) 60%,transparent);box-shadow:0 0 60px color-mix(in srgb,var(--orb-a) 18%,transparent)}' +
      '#maxess-results-10 .mx-orbit{position:absolute;border-radius:50%;pointer-events:none}' +
      '#maxess-results-10 .mx-orbit-a{inset:-5%;border:1px solid color-mix(in srgb,var(--orb-a) 55%,transparent);animation:mx-orbit-a 8s ease-in-out infinite}' +
      '#maxess-results-10 .mx-orbit-b{inset:10%;border:1px solid color-mix(in srgb,var(--orb-b) 42%,transparent);animation:mx-orbit-b 12s linear infinite}' +
      '#maxess-results-10 .mx-orbit-c{inset:18%;border:1px dashed rgba(255,255,255,.13);animation:mx-orbit-c 18s linear infinite reverse}' +
      '#maxess-results-10 .mx-orb-core{position:absolute;inset:26%;border-radius:50%;background:radial-gradient(circle at 36% 30%,rgba(255,255,255,.3),transparent 8%),radial-gradient(circle,color-mix(in srgb,var(--orb-a) 45%,#fff0),transparent 62%);filter:blur(2px)}' +
      '#maxess-results-10 .mx-orb-energy{position:absolute;left:50%;top:50%;width:4px;height:44%;transform-origin:50% 0;border-radius:99px;background:linear-gradient(180deg,color-mix(in srgb,var(--orb-a) 80%,white),transparent);opacity:.55;animation:mx-energy 4s ease-in-out infinite}' +
      '#maxess-results-10 .mx-orb-energy.e1{transform:translate(-50%,-5%) rotate(15deg)}' +
      '#maxess-results-10 .mx-orb-energy.e2{transform:translate(-50%,-5%) rotate(137deg);animation-delay:1.2s}' +
      '#maxess-results-10 .mx-orb-energy.e3{transform:translate(-50%,-5%) rotate(255deg);animation-delay:2.1s}' +
      '#maxess-results-10 .mx-orb-score{position:relative;z-index:4;font-size:clamp(100px,12vw,176px);font-weight:900;letter-spacing:-.1em;line-height:.75;background:linear-gradient(110deg,#fff,color-mix(in srgb,var(--orb-a) 70%,white),var(--orb-b));-webkit-background-clip:text;background-clip:text;color:transparent;text-shadow:0 0 45px color-mix(in srgb,var(--orb-a) 22%,transparent)}' +
      '#maxess-results-10 .mx-orb-score small{font-size:.16em;letter-spacing:.03em;margin-left:8px;vertical-align:baseline}' +
      '#maxess-results-10 .mx-hero-center .mx-mastery{display:inline-flex;margin-top:34px;padding:10px 16px;border-radius:999px;border:1px solid rgba(255,255,255,.18);background:rgba(255,255,255,.05);font-size:12px;font-weight:900;letter-spacing:.14em;text-transform:uppercase}' +
      '#maxess-results-10 .mx-action-row{display:flex;flex-wrap:wrap;gap:12px;margin-top:26px}' +
      '#maxess-results-10 .mx-center .mx-action-row{justify-content:center}' +
      '#maxess-results-10 .mx-btn{display:inline-flex;align-items:center;justify-content:center;gap:9px;min-height:54px;padding:0 20px;border-radius:15px;border:1px solid rgba(255,255,255,.18);background:rgba(255,255,255,.06);color:inherit;text-decoration:none;font-weight:900;transition:transform .2s var(--mx-ease),box-shadow .2s ease,border-color .2s ease,background .2s ease}' +
      '#maxess-results-10 .mx-btn:hover,#maxess-results-10 .mx-btn:focus-visible{transform:translateY(-3px);border-color:rgba(255,255,255,.48);box-shadow:0 16px 38px rgba(0,0,0,.2);outline:none}' +
      '#maxess-results-10 .mx-btn-primary{background:linear-gradient(135deg,#d9bcff,#7a3ed0 52%,#34105d);color:#fff;border-color:rgba(230,210,255,.7);box-shadow:0 14px 34px rgba(99,42,175,.28),inset 0 1px rgba(255,255,255,.6)}' +
      '#maxess-results-10 .mx-light .mx-btn{border-color:rgba(0,0,0,.15);background:#111;color:#fff}' +
      '#maxess-results-10 .mx-light .mx-btn-primary{background:linear-gradient(135deg,#a66cff,#5b2fa8);border-color:#7040b4}' +
      '#maxess-results-10 .mx-hero-side{padding:24px;border-left:1px solid rgba(255,255,255,.12)}' +
      '#maxess-results-10 .mx-hero-side strong{display:block;font-size:clamp(22px,2vw,32px);letter-spacing:-.035em;margin-bottom:8px}' +
      '#maxess-results-10 .mx-hero-side p{margin:0;color:var(--mx-muted);line-height:1.6}' +
      '#maxess-results-10 .mx-score-strip{display:grid;grid-template-columns:repeat(5,1fr);gap:8px;margin-top:34px}' +
      '#maxess-results-10 .mx-score-chip{padding:15px 10px;border:1px solid rgba(255,255,255,.1);border-radius:15px;background:rgba(255,255,255,.04);text-align:center}' +
      '#maxess-results-10 .mx-score-chip b{display:block;font-size:26px}' +
      '#maxess-results-10 .mx-score-chip span{display:block;margin-top:5px;color:var(--mx-muted);font-size:9px;font-weight:800;letter-spacing:.08em;text-transform:uppercase}' +
      '#maxess-results-10 .mx-signature-layout{display:grid;grid-template-columns:minmax(340px,1fr) minmax(360px,1fr);gap:clamp(35px,7vw,110px);align-items:center}' +
      '#maxess-results-10 .mx-signature-wrap{padding:20px}' +
      '#maxess-results-10 .mx-signature-svg{display:block;width:min(620px,100%);margin:auto}' +
      '#maxess-results-10 .mx-grid-line{fill:none;stroke:rgba(0,0,0,.12);stroke-width:2}' +
      '#maxess-results-10 .mx-signature-svg line{stroke:rgba(0,0,0,.1);stroke-width:2}' +
      '#maxess-results-10 .mx-signature-shape{fill:rgba(125,68,215,.15);stroke:#7d44d7;stroke-width:6;filter:drop-shadow(0 12px 22px rgba(125,68,215,.15))}' +
      '#maxess-results-10 .mx-dimension-list{display:grid;gap:11px}' +
      '#maxess-results-10 .mx-dimension-row{padding:18px 20px;border-radius:17px;background:#f6f4f8;border:1px solid rgba(0,0,0,.08)}' +
      '#maxess-results-10 .mx-dimension-row-top{display:flex;justify-content:space-between;gap:20px;align-items:baseline}' +
      '#maxess-results-10 .mx-dimension-row-top strong{font-size:19px;color:#3c275c}' +
      '#maxess-results-10 .mx-dimension-row-top b{font-size:20px}' +
      '#maxess-results-10 .mx-bar{height:7px;margin-top:11px;border-radius:99px;background:#ddd9e5;overflow:hidden}' +
      '#maxess-results-10 .mx-bar i{display:block;height:100%;width:var(--w);background:linear-gradient(90deg,var(--c),#7d44d7);border-radius:inherit}' +
      '#maxess-results-10 .mx-dimension-row p{margin:10px 0 0;color:#666;font-size:12px;line-height:1.5}' +
      '#maxess-results-10 .mx-chapter-head{max-width:880px}' +
      '#maxess-results-10 .mx-five-grid{display:grid;grid-template-columns:repeat(5,1fr);gap:13px;margin-top:34px}' +
      '#maxess-results-10 .mx-dimension-card{min-height:370px;padding:22px 18px;border-radius:27px;border:1px solid rgba(255,255,255,.12);background:linear-gradient(160deg,rgba(255,255,255,.07),rgba(255,255,255,.018));box-shadow:inset 0 1px rgba(255,255,255,.09),0 26px 70px rgba(0,0,0,.25);transition:transform .2s ease,border-color .2s ease,opacity .2s ease}' +
      '#maxess-results-10 .mx-dimension-card:hover,#maxess-results-10 .mx-dimension-card:focus-within{transform:translateY(-5px);border-color:color-mix(in srgb,var(--c) 50%,transparent)}' +
      '#maxess-results-10 .mx-ring{position:relative;width:156px;height:156px;margin:0 auto 20px;border-radius:50%;background:conic-gradient(var(--c) calc(var(--v)*1%),rgba(255,255,255,.08) 0);filter:drop-shadow(0 0 16px color-mix(in srgb,var(--c) 25%,transparent))}' +
      '#maxess-results-10 .mx-ring:after{content:"";position:absolute;inset:12px;border-radius:50%;background:#0c0911;box-shadow:inset 0 0 30px rgba(0,0,0,.6)}' +
      '#maxess-results-10 .mx-ring b{position:absolute;inset:0;display:grid;place-items:center;z-index:1;font-size:43px;color:var(--c)}' +
      '#maxess-results-10 .mx-dimension-card h3{text-align:center;font-size:20px;margin:0 0 7px}' +
      '#maxess-results-10 .mx-archetype{text-align:center;color:var(--c);font-size:10px;font-weight:900;letter-spacing:.14em;text-transform:uppercase}' +
      '#maxess-results-10 .mx-dimension-card p{color:#aaa;font-size:12px;line-height:1.55;text-align:center}' +
      '#maxess-results-10 .mx-lever{margin-top:18px;padding-top:15px;border-top:1px solid rgba(255,255,255,.1)}' +
      '#maxess-results-10 .mx-lever small{display:block;color:var(--c);font-size:9px;font-weight:900;letter-spacing:.14em}' +
      '#maxess-results-10 .mx-lever b{display:block;margin-top:6px;font-size:11px;line-height:1.45}' +
      '#maxess-results-10 .mx-meaning-grid{display:grid;grid-template-columns:repeat(2,1fr);gap:14px;margin-top:34px}' +
      '#maxess-results-10 .mx-meaning-card{padding:28px;border-radius:24px;border:1px solid rgba(0,0,0,.1);background:#fff}' +
      '#maxess-results-10 .mx-meaning-card .mx-number{display:inline-grid;place-items:center;width:34px;height:34px;border-radius:50%;color:#fff;background:var(--c);font-weight:900}' +
      '#maxess-results-10 .mx-meaning-card h3{font-size:26px;margin:18px 0 8px}' +
      '#maxess-results-10 .mx-meaning-card p{color:#555;line-height:1.6;font-size:14px}' +
      '#maxess-results-10 .mx-two-up{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-top:34px}' +
      '#maxess-results-10 .mx-feature{padding:clamp(30px,4vw,52px);border-radius:31px;border:1px solid rgba(255,255,255,.13);background:rgba(255,255,255,.045);box-shadow:0 30px 80px rgba(0,0,0,.25)}' +
      '#maxess-results-10 .mx-feature h3{font-size:clamp(30px,3.5vw,54px);line-height:.98;margin:12px 0}' +
      '#maxess-results-10 .mx-feature p{color:var(--mx-soft);line-height:1.65;max-width:650px}' +
      '#maxess-results-10 .mx-feature.advantage{border-color:rgba(57,223,145,.28)}' +
      '#maxess-results-10 .mx-feature.opportunity{border-color:rgba(244,211,79,.3)}' +
      '#maxess-results-10 .mx-reveal-box{max-width:1120px;margin:36px auto 0;padding:clamp(35px,6vw,76px);border-radius:34px;background:radial-gradient(circle at 50% 0,rgba(166,108,255,.25),transparent 52%),rgba(255,255,255,.04);border:1px solid rgba(166,108,255,.25);text-align:center;box-shadow:0 35px 100px rgba(0,0,0,.4)}' +
      '#maxess-results-10 .mx-reveal-box h3{font-size:clamp(30px,4vw,60px);margin:10px 0 16px}' +
      '#maxess-results-10 .mx-reveal-box p{max-width:820px;margin:0 auto;color:var(--mx-soft);font-size:clamp(17px,1.5vw,21px);line-height:1.65}' +
      '#maxess-results-10 .mx-next{display:grid;grid-template-columns:1.1fr .9fr;gap:30px;align-items:stretch;margin-top:34px}' +
      '#maxess-results-10 .mx-next-main{padding:clamp(30px,5vw,60px);border-radius:31px;background:#111;border:1px solid rgba(0,0,0,.08)}' +
      '#maxess-results-10 .mx-next-main h3{font-size:clamp(30px,4vw,56px);line-height:1;margin:10px 0 14px}' +
      '#maxess-results-10 .mx-next-main p{color:#555;line-height:1.65}' +
      '#maxess-results-10 .mx-next-action{padding:30px;border-radius:31px;background:linear-gradient(145deg,#111,#231638);color:#fff;display:flex;flex-direction:column;justify-content:center;border:1px solid rgba(166,108,255,.25)}' +
      '#maxess-results-10 .mx-next-action strong{font-size:25px}' +
      '#maxess-results-10 .mx-next-action p{color:#bbb;line-height:1.55}' +
      '#maxess-results-10 .mx-path-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin-top:32px}' +
      '#maxess-results-10 .mx-path-card{position:relative;display:flex;flex-direction:column;min-height:190px;padding:22px;border-radius:22px;background:#0a1018;border:1px solid rgba(255,255,255,.11);color:#fff;text-decoration:none;transition:transform .2s ease,border-color .2s ease,box-shadow .2s ease}' +
      '#maxess-results-10 .mx-path-card:hover,#maxess-results-10 .mx-path-card:focus-visible{transform:translateY(-4px);border-color:rgba(70,183,255,.45);box-shadow:0 18px 45px rgba(0,0,0,.25);outline:none}' +
      '#maxess-results-10 .mx-path-card.recommended{border-color:rgba(166,108,255,.48);box-shadow:inset 0 0 0 1px rgba(166,108,255,.1)}' +
      '#maxess-results-10 .mx-path-card small{color:#bda8ff;font-weight:900;letter-spacing:.12em}' +
      '#maxess-results-10 .mx-path-card h3{font-size:18px;margin:13px 0 7px}' +
      '#maxess-results-10 .mx-path-card p{margin:0;color:#9ca7b5;font-size:12px;line-height:1.5}' +
      '#maxess-results-10 .mx-path-score{margin-top:auto;padding-top:16px;color:#6fc7ff;font-size:10px;font-weight:900;letter-spacing:.12em;text-transform:uppercase}' +
      '#maxess-results-10 .mx-more{display:flex;justify-content:center;margin-top:18px}' +
      '#maxess-results-10 .mx-hidden-path{display:none}' +
      '#maxess-results-10 .mx-hidden-path.is-visible{display:flex}' +
      '#maxess-results-10 .mx-master-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin-top:32px}' +
      '#maxess-results-10 .mx-master-card{min-height:170px;padding:23px;border-radius:23px;background:rgba(255,255,255,.045);border:1px solid rgba(255,255,255,.12);transition:transform .2s ease,border-color .2s ease}' +
      '#maxess-results-10 .mx-master-card:hover{transform:translateY(-4px);border-color:rgba(255,255,255,.3)}' +
      '#maxess-results-10 .mx-master-icon{width:48px;height:48px;display:grid;place-items:center;border-radius:14px;background:linear-gradient(145deg,#c6a7ff,#552b99);font-size:22px;box-shadow:inset 0 1px rgba(255,255,255,.55)}' +
      '#maxess-results-10 .mx-master-card h3{font-size:20px;margin:18px 0 6px}' +
      '#maxess-results-10 .mx-master-card p{margin:0;color:#aaa;font-size:12px;line-height:1.5}' +
      '#maxess-results-10 .mx-craft-grid{display:grid;grid-template-columns:repeat(7,1fr);gap:8px;margin-top:32px}' +
      '#maxess-results-10 .mx-craft-step{padding:20px 10px;text-align:center;border-radius:17px;border:1px solid rgba(0,0,0,.09);background:#fff}' +
      '#maxess-results-10 .mx-craft-step b{display:block;font-size:12px;letter-spacing:.08em}' +
      '#maxess-results-10 .mx-craft-step span{display:block;margin-top:7px;color:#666;font-size:10px;line-height:1.35}' +
      '#maxess-results-10 .mx-naya{display:grid;grid-template-columns:1fr .8fr;gap:30px;align-items:center}' +
      '#maxess-results-10 .mx-naya-card{padding:clamp(30px,5vw,60px);border-radius:34px;background:radial-gradient(circle at 30% 25%,rgba(255,255,255,.18),transparent 16%),linear-gradient(145deg,#29133d,#0c0612);border:1px solid rgba(255,255,255,.15);box-shadow:0 35px 100px rgba(0,0,0,.4)}' +
      '#maxess-results-10 .mx-naya-orb{width:170px;aspect-ratio:1;border-radius:50%;margin:auto;background:radial-gradient(circle at 35% 28%,#fff,transparent 9%),radial-gradient(circle,#b57dff,#30104e 52%,#050208 78%);box-shadow:0 0 70px rgba(166,108,255,.45),inset 0 0 50px rgba(255,255,255,.14);animation:mx-breathe 5s ease-in-out infinite}' +
      '#maxess-results-10 .mx-report{background:#fff;color:#111}' +
      '#maxess-results-10 .mx-report-card{max-width:1120px;margin:auto;padding:clamp(34px,6vw,76px);border-radius:34px;border:1px solid rgba(0,0,0,.1);box-shadow:0 30px 90px rgba(0,0,0,.09);text-align:center}' +
      '#maxess-results-10 .mx-report-card p{max-width:760px;margin:18px auto;color:#555;line-height:1.65;font-size:17px}' +
      '#maxess-results-10 .mx-final{background:radial-gradient(circle at 50% 0,rgba(166,108,255,.28),transparent 50%),#030305;text-align:center}' +
      '#maxess-results-10 .mx-final h2{max-width:1000px;margin-inline:auto}' +
      '#maxess-results-10 .mx-final p{color:#aaa;font-size:18px}' +
      '#maxess-results-10 .mx-error{min-height:70vh;display:grid;place-items:center;background:#030305;color:#fff;text-align:center}' +
      '#maxess-results-10 .mx-error-box{max-width:680px;padding:40px;border:1px solid rgba(255,255,255,.13);border-radius:28px;background:rgba(255,255,255,.04)}' +
      '#maxess-results-10 .mx-error-box h1{font-size:42px;letter-spacing:-.04em}' +
      '#maxess-results-10 .mx-error-box p{color:#aaa;line-height:1.6}' +
      '@keyframes mx-breathe{50%{transform:scale(1.018);filter:saturate(1.12)}}' +
      '@keyframes mx-orbit-a{0%,100%{transform:scale(.98) rotate(0deg);opacity:.35}50%{transform:scale(1.025) rotate(180deg);opacity:.8}}' +
      '@keyframes mx-orbit-b{to{transform:rotate(360deg)}}' +
      '@keyframes mx-orbit-c{to{transform:rotate(360deg)}}' +
      '@keyframes mx-energy{0%,100%{opacity:.15;filter:blur(1px)}50%{opacity:.75;filter:blur(3px)}}' +
      '@media(max-width:1180px){#maxess-results-10 .mx-hero-grid{grid-template-columns:1fr;max-width:850px;margin:auto;text-align:center}#maxess-results-10 .mx-hero-copy{order:2}#maxess-results-10 .mx-hero-center{order:1}#maxess-results-10 .mx-hero-side{order:3;border-left:0;border-top:1px solid rgba(255,255,255,.12);padding-top:25px}#maxess-results-10 .mx-hero-copy p{margin-inline:auto}#maxess-results-10 .mx-five-grid{grid-template-columns:repeat(3,1fr)}#maxess-results-10 .mx-path-grid,#maxess-results-10 .mx-master-grid{grid-template-columns:repeat(2,1fr)}#maxess-results-10 .mx-craft-grid{grid-template-columns:repeat(4,1fr)}}' +
      '@media(max-width:820px){#maxess-results-10 .mx-signature-layout,#maxess-results-10 .mx-two-up,#maxess-results-10 .mx-next,#maxess-results-10 .mx-naya{grid-template-columns:1fr}#maxess-results-10 .mx-five-grid{grid-template-columns:repeat(2,1fr)}#maxess-results-10 .mx-meaning-grid{grid-template-columns:1fr}#maxess-results-10 .mx-craft-grid{grid-template-columns:repeat(2,1fr)}}' +
      '@media(max-width:600px){#maxess-results-10 .mx-section{padding:66px 0}#maxess-results-10 .mx-wrap{padding-inline:18px}#maxess-results-10 .mx-orb{min-width:0;width:min(88vw,480px)}#maxess-results-10 .mx-hero{min-height:auto;padding:74px 0}#maxess-results-10 .mx-score-strip{grid-template-columns:repeat(2,1fr)}#maxess-results-10 .mx-five-grid,#maxess-results-10 .mx-path-grid,#maxess-results-10 .mx-master-grid{grid-template-columns:1fr}#maxess-results-10 .mx-action-row{flex-direction:column}#maxess-results-10 .mx-btn{width:100%}#maxess-results-10 .mx-dimension-card{text-align:left;min-height:auto}#maxess-results-10 .mx-ring{margin-left:0}#maxess-results-10 .mx-dimension-card h3,#maxess-results-10 .mx-dimension-card p{text-align:left}#maxess-results-10 .mx-archetype{text-align:left}#maxess-results-10 .mx-craft-grid{grid-template-columns:1fr 1fr}}' +
      '@media(prefers-reduced-motion:reduce){#maxess-results-10 *,#maxess-results-10 *:before,#maxess-results-10 *:after{animation:none!important;transition:none!important;scroll-behavior:auto!important}}' +
      '@media print{#maxess-results-10{width:100%!important;margin:0!important;background:#fff!important;color:#111!important}#maxess-results-10 .mx-section{padding:30px 0;background:#fff!important;color:#111!important;break-inside:avoid}#maxess-results-10 .mx-hero{min-height:auto}#maxess-results-10 .mx-orbit,#maxess-results-10 .mx-orb-energy,#maxess-results-10 .mx-naya-orb{animation:none!important}#maxess-results-10 .mx-action-row,#maxess-results-10 .mx-more,#maxess-results-10 .mx-final .mx-action-row{display:none!important}#maxess-results-10 .mx-dimension-card,#maxess-results-10 .mx-feature,#maxess-results-10 .mx-path-card,#maxess-results-10 .mx-master-card,#maxess-results-10 .mx-report-card{break-inside:avoid;box-shadow:none;background:#fff!important;color:#111!important;border:1px solid #aaa}#maxess-results-10 .mx-copy,#maxess-results-10 .mx-dimension-card p,#maxess-results-10 .mx-feature p{color:#333!important}#maxess-results-10 .mx-orb{width:260px;min-width:0;box-shadow:none;background:#eee;color:#111}#maxess-results-10 .mx-orb-score{background:none;color:#111}#maxess-results-10 .mx-orb-core{display:none}}' +
      '</style>';
  }

  function dimensionRows(result) {
    return result.dimensions.map(function (d, index) {
      var meta = DIMENSION_META[d.name];
      return '<div class="mx-dimension-row" style="--c:' + meta.color + '">' +
        '<div class="mx-dimension-row-top"><strong>' + esc(d.name) + '</strong><b>' + Math.round(d.score) + '</b></div>' +
        '<div class="mx-bar"><i style="--w:' + d.score + '%;--c:' + meta.color + '"></i></div>' +
        '<p>' + esc(evidenceDescription(d)) + '</p>' +
        '</div>';
    }).join('');
  }

  function dimensionCards(result) {
    return result.dimensions.map(function (d, index) {
      var meta = DIMENSION_META[d.name];
      return '<article class="mx-dimension-card" tabindex="0" style="--v:' + d.score + ';--c:' + meta.color + '" aria-label="' + esc(d.name + ' score ' + Math.round(d.score) + ' out of 100') + '">' +
        '<div class="mx-ring"><b>' + Math.round(d.score) + '</b></div>' +
        '<div class="mx-archetype">' + esc(meta.icon + ' ' + meta.archetype) + '</div>' +
        '<h3>' + esc(d.name) + '</h3>' +
        '<p>' + esc(evidenceDescription(d)) + '</p>' +
        '<div class="mx-lever"><small>YOUR PRACTICAL LEVER</small><b>' + esc(meta.action) + '</b></div>' +
        '</article>';
    }).join('');
  }

  function meaningCards(result) {
    return result.dimensions.map(function (d, index) {
      var meta = DIMENSION_META[d.name];
      return '<article class="mx-meaning-card" style="--c:' + meta.color + '">' +
        '<span class="mx-number">' + (index + 1) + '</span>' +
        '<h3>' + esc(d.name) + '</h3>' +
        '<p><strong>What it is:</strong> ' + esc(meta.meaning) + '</p>' +
        '<p><strong>What your score says:</strong> ' + Math.round(d.score) + '/100 places this capability in the ' + esc(band(d.score).toLowerCase()) + ' range.</p>' +
        '<p><strong>What to do:</strong> ' + esc(meta.action) + '</p>' +
        '</article>';
    }).join('');
  }

  function pathwayCards(result) {
    var ranked = sortedPathways(result);
    return ranked.map(function (pathway, index) {
      var hidden = index >= 6 ? ' mx-hidden-path' : '';
      var recommended = index < 3 ? ' recommended' : '';
      return '<a class="mx-path-card' + hidden + recommended + '" href="#" data-pathway="' + esc(pathway.name) + '">' +
        '<small>' + String(index + 1).padStart(2, '0') + ' · ' + pathway.relevance + '% RELEVANCE</small>' +
        '<h3>' + esc(pathway.name) + '</h3>' +
        '<p>' + esc(pathway.description) + '</p>' +
        '<span class="mx-path-score">' + (index < 3 ? 'Recommended starting point' : 'Explore pathway') + ' →</span>' +
        '</a>';
    }).join('');
  }

  function masterCards(result) {
    return NAYA_MASTERS.map(function (master) {
      var meta = DIMENSION_META[master[2]];
      return '<article class="mx-master-card" tabindex="0" style="--c:' + meta.color + '">' +
        '<div class="mx-master-icon" aria-hidden="true">' + esc(meta.icon) + '</div>' +
        '<h3>' + esc(master[0]) + '</h3>' +
        '<p>' + esc(master[1]) + '</p>' +
        '</article>';
    }).join('');
  }

  function craftSteps() {
    var steps = [
      ['KNOW', 'Define the real outcome.'],
      ['TELL', 'Give AI the context and standard.'],
      ['ASK', 'Direct the work intelligently.'],
      ['CREATE', 'Make something useful.'],
      ['SCORE', 'Judge the result.'],
      ['IMPROVE', 'Fix the gap and preserve strengths.'],
      ['FREEZE', 'Keep the version that works.']
    ];
    return steps.map(function (step, index) {
      return '<div class="mx-craft-step"><b>' + esc(step[0]) + '</b><span>' + esc(step[1]) + '</span></div>';
    }).join('');
  }

  function renderMissingState() {
    var root = getRoot();
    if (!root) return;
    root.innerHTML = styles() +
      '<section class="mx-error mx-section"><div class="mx-error-box">' +
      '<span class="mx-eyebrow">MAXESS RESULT</span>' +
      '<h1>Your result is not available yet.</h1>' +
      '<p>The Results experience received no valid assessment result. Nothing has been invented or guessed. Return to the assessment and complete it again.</p>' +
      '</div></section>';
    root.dataset.resultsState = 'missing-result';
  }

  function render(result) {
    var root = getRoot();
    if (!root || !result) return;

    root.dataset.built = '1';
    root.dataset.resultsVersion = VERSION;
    root.dataset.resultsState = 'valid-result';

    var next = nextMove(result);
    var pathways = sortedPathways(result);

    root.innerHTML = styles() +
      '<section id="mx-result-arrival" class="mx-section mx-hero">' +
        '<div class="mx-wrap mx-hero-grid">' +
          '<div class="mx-hero-copy">' +
            '<span class="mx-eyebrow">YOUR MAXESS RESULT</span>' +
            '<h1>Your AI Mastery Report</h1>' +
            '<p>Your score is the beginning. This report shows what your result says about the way you work with AI — and where your next improvement can create the most leverage.</p>' +
            '<div class="mx-action-row"><a class="mx-btn mx-btn-primary" href="#mx-signature">Explore your report ↓</a><button class="mx-btn" type="button" data-naya-read>◉ Listen to Naya</button></div>' +
          '</div>' +
          '<div class="mx-hero-center">' +
            orb(result.overall) +
            '<div class="mx-mastery">' + esc(result.band) + ' · ' + esc(bandDescription(result.overall)) + '</div>' +
            '<div class="mx-score-strip">' + result.dimensions.map(function (d) { return '<div class="mx-score-chip"><b>' + Math.round(d.score) + '</b><span>' + esc(d.name) + '</span></div>'; }).join('') + '</div>' +
          '</div>' +
          '<aside class="mx-hero-side"><strong>What matters most</strong><p>' + esc(result.strongest.name) + ' is currently your strongest signal. ' + esc(result.opportunity.name) + ' is your clearest opportunity to create leverage.</p></aside>' +
        '</div>' +
      '</section>' +

      '<section id="mx-signature" class="mx-section mx-light">' +
        '<div class="mx-wrap mx-signature-layout">' +
          '<div><span class="mx-eyebrow">01 · RECOGNITION</span><h2>What AI Really Says About You</h2><p class="mx-copy">One number tells you where you are. Your five-dimensional signature shows how you got there. The shape is the useful part.</p><div class="mx-dimension-list">' + dimensionRows(result) + '</div></div>' +
          '<div class="mx-signature-wrap">' + svgFingerprint(result) + '</div>' +
        '</div>' +
      '</section>' +

      '<section id="mx-dimensions" class="mx-section mx-violet">' +
        '<div class="mx-wrap">' +
          '<div class="mx-chapter-head"><span class="mx-eyebrow">02 · YOUR FIVE DIMENSIONS</span><h2>Five capabilities. One pattern.</h2><p class="mx-copy">Each dimension is a different part of the way you work with AI. Together they form your current capability profile.</p></div>' +
          '<div class="mx-five-grid">' + dimensionCards(result) + '</div>' +
        '</div>' +
      '</section>' +

      '<section id="mx-meaning" class="mx-section mx-cream">' +
        '<div class="mx-wrap">' +
          '<span class="mx-eyebrow">03 · WHAT IT MEANS</span><h2>Your scores, translated into real life.</h2><p class="mx-copy">A score is useful only when you understand what it changes. Here is the practical meaning of each capability.</p>' +
          '<div class="mx-meaning-grid">' + meaningCards(result) + '</div>' +
        '</div>' +
      '</section>' +

      '<section id="mx-advantage" class="mx-section mx-emerald">' +
        '<div class="mx-wrap">' +
          '<span class="mx-eyebrow">04 · YOUR NATURAL ADVANTAGE</span>' +
          '<div class="mx-feature advantage"><span class="mx-archetype">' + esc(DIMENSION_META[result.strongest.name].archetype) + '</span><h3>' + esc(result.strongest.name) + '</h3><p>' + esc(evidenceDescription(result.strongest)) + ' Your highest current capability can become the foundation for the next level of your AI practice.</p></div>' +
        '</div>' +
      '</section>' +

      '<section id="mx-opportunity" class="mx-section mx-gold">' +
        '<div class="mx-wrap">' +
          '<span class="mx-eyebrow">05 · YOUR HIGHEST-LEVERAGE OPPORTUNITY</span>' +
          '<div class="mx-feature opportunity"><span class="mx-archetype">' + esc(DIMENSION_META[result.opportunity.name].archetype) + '</span><h3>' + esc(result.opportunity.name) + '</h3><p>' + esc(opportunityLanguage(result)) + '</p></div>' +
        '</div>' +
      '</section>' +

      '<section id="mx-revelation" class="mx-section mx-dark">' +
        '<div class="mx-wrap mx-center">' +
          '<span class="mx-eyebrow">06 · OH... THAT’S WHY</span>' +
          '<h2>The shape tells the story.</h2>' +
          '<div class="mx-reveal-box"><h3>' + esc(result.strongest.name) + ' leads. ' + esc(result.opportunity.name) + ' is the lever.</h3><p>' + esc(patternLanguage(result)) + '</p><div class="mx-action-row"><button class="mx-btn mx-btn-primary" type="button" data-naya-read>◉ Hear Naya interpret this</button></div></div>' +
        '</div>' +
      '</section>' +

      '<section id="mx-next" class="mx-section mx-light">' +
        '<div class="mx-wrap">' +
          '<span class="mx-eyebrow">07 · YOUR NEXT MOVE</span><h2>One clear move beats ten vague ones.</h2><p class="mx-copy">Your report should not leave you wondering what to do. Start with the capability that gives your current profile the most leverage.</p>' +
          '<div class="mx-next"><div class="mx-next-main"><span class="mx-eyebrow">FOCUS</span><h3>' + esc(next.title) + '</h3><p>' + esc(next.body) + '</p></div><div class="mx-next-action"><strong>' + esc(next.dimension) + '</strong><p>Use this capability on one real task. Then score the result and improve it.</p><button class="mx-btn mx-btn-primary" type="button" data-naya-read>Ask Naya to help you start →</button></div></div>' +
        '</div>' +
      '</section>' +

      '<section id="mx-pathways" class="mx-section mx-blue">' +
        '<div class="mx-wrap">' +
          '<span class="mx-eyebrow">08 · PERSONALIZED AI MASTERY LIBRARY</span><h2>18 doors. Your result tells us where to start.</h2><p class="mx-copy">These are not 18 products to buy. They are 18 kinds of capability you can build. The first three are the strongest starting signals for this result.</p>' +
          '<div class="mx-path-grid">' + pathwayCards(result) + '</div>' +
          '<div class="mx-more"><button class="mx-btn" type="button" data-show-pathways>Show all 18 pathways ↓</button></div>' +
        '</div>' +
      '</section>' +

      '<section id="mx-masters" class="mx-section mx-violet">' +
        '<div class="mx-wrap">' +
          '<span class="mx-eyebrow">09 · NAYA MASTERS</span><h2>Meet the intelligence behind the next level.</h2><p class="mx-copy">Naya is one coherent intelligence with specialist modes. These Masters help you turn a result into action.</p>' +
          '<div class="mx-master-grid">' + masterCards(result) + '</div>' +
        '</div>' +
      '</section>' +

      '<section id="mx-craftsmanship" class="mx-section mx-light">' +
        '<div class="mx-wrap">' +
          '<span class="mx-eyebrow">10 · AI CRAFTSMANSHIP</span><h2>You do not need a better prompt. You need a better loop.</h2><p class="mx-copy">The reusable skill is knowing what you want, directing AI clearly, judging the result, improving it and preserving what works.</p>' +
          '<div class="mx-craft-grid">' + craftSteps() + '</div>' +
        '</div>' +
      '</section>' +

      '<section id="mx-master-ai" class="mx-section mx-dark">' +
        '<div class="mx-wrap mx-center">' +
          '<span class="mx-eyebrow">11 · MASTER AI</span><h2>Now you know where you are. You can build from here.</h2><p class="mx-copy" style="margin-inline:auto">The purpose of this report is not to label you. It is to give you a useful starting point for becoming more capable, more deliberate and more effective with AI.</p>' +
        '</div>' +
      '</section>' +

      '<section id="mx-naya" class="mx-section mx-violet">' +
        '<div class="mx-wrap mx-naya">' +
          '<div><span class="mx-eyebrow">12 · NAYA</span><h2>Your result should become a conversation.</h2><p class="mx-copy">Naya already has the context of this result. You do not need to start over explaining yourself. Ask her to help you work on the next move.</p><div class="mx-action-row"><button class="mx-btn mx-btn-primary" type="button" data-naya-read>◉ Listen to your personalized reading</button></div></div>' +
          '<div class="mx-naya-card"><div class="mx-naya-orb" aria-hidden="true"></div><p class="mx-center" style="margin:28px 0 0;color:#bbb">Naya interprets. You decide. Together, you improve.</p></div>' +
        '</div>' +
      '</section>' +

      '<section id="mx-report" class="mx-section mx-report">' +
        '<div class="mx-wrap"><div class="mx-report-card"><span class="mx-eyebrow">13 · YOUR REPORT</span><h2>Your result is worth keeping.</h2><p>Save or print this personalized report so the insight does not disappear when you close the browser.</p><div class="mx-action-row" style="justify-content:center"><button class="mx-btn mx-btn-primary" type="button" data-print>Print / Save PDF ↗</button><button class="mx-btn" type="button" data-naya-read>◉ Listen to Naya</button></div></div></div>' +
      '</section>' +

      '<section id="mx-transition" class="mx-section mx-final">' +
        '<div class="mx-wrap">' +
          '<span class="mx-eyebrow">14 · YOUR NEXT CHAPTER</span><h2>You know where you are.<br>Now build what comes next.</h2><p>Continue into the NayaNET experience when you are ready.</p>' +
          '<div class="mx-action-row" style="justify-content:center"><a class="mx-btn mx-btn-primary" href="https://nayanet.xyz/" target="_blank" rel="noopener">Continue with Naya →</a></div>' +
        '</div>' +
      '</section>';

    bindInteractions(root, result, pathways);
  }

  function playNaya() {
    var candidates = [
      'maxessNayaPlayOriginal',
      'maxessNayaPlay'
    ];

    for (var i = 0; i < candidates.length; i += 1) {
      var button = document.getElementById(candidates[i]);
      if (button && button !== document.activeElement) {
        try { button.click(); return true; } catch (error) { /* graceful */ }
      }
    }

    if (typeof window.playMaxessNaya === 'function') {
      try { window.playMaxessNaya(); return true; } catch (error) { /* graceful */ }
    }

    if (typeof window.MAXESS_NAYA_PLAY === 'function') {
      try { window.MAXESS_NAYA_PLAY(); return true; } catch (error) { /* graceful */ }
    }

    return false;
  }

  function bindInteractions(root, result, pathways) {
    root.querySelectorAll('[data-naya-read]').forEach(function (button) {
      button.addEventListener('click', function () {
        var played = playNaya();
        if (!played) {
          button.setAttribute('aria-label', 'Naya audio is not currently available. Your written interpretation remains available above.');
          button.textContent = 'Naya audio unavailable — read the interpretation above';
        }
      });
    });

    var printButton = root.querySelector('[data-print]');
    if (printButton) {
      printButton.addEventListener('click', function () { window.print(); });
    }

    var moreButton = root.querySelector('[data-show-pathways]');
    if (moreButton) {
      moreButton.addEventListener('click', function () {
        root.querySelectorAll('.mx-hidden-path').forEach(function (card) { card.classList.add('is-visible'); });
        moreButton.remove();
      });
    }

    root.querySelectorAll('[data-pathway]').forEach(function (link) {
      link.addEventListener('click', function (event) {
        event.preventDefault();
        var name = link.getAttribute('data-pathway');
        if (typeof window.MAXESS_PATHWAY_OPEN === 'function') {
          window.MAXESS_PATHWAY_OPEN(name);
          return;
        }
        window.dispatchEvent(new CustomEvent('maxess:pathway-request', { detail: { name: name, result: result.raw } }));
      });
    });

    var observer = 'IntersectionObserver' in window ? new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) entry.target.dataset.revealed = 'true';
      });
    }, { threshold: .08 }) : null;

    if (observer) {
      root.querySelectorAll('.mx-section').forEach(function (section) { observer.observe(section); });
    }

    root.querySelectorAll('.mx-dimension-card').forEach(function (card) {
      card.addEventListener('focus', function () { card.scrollIntoView({ block: 'nearest', behavior: 'smooth' }); });
    });
  }

  function boot() {
    var root = getRoot();
    if (!root) return;

    var raw = getRawResult();
    var result = normalizeResult(raw);

    if (!result || !Array.isArray(result.raw.dimensions) || result.raw.dimensions.length < 5) {
      renderMissingState();
      return;
    }

    render(result);
  }

  window.MAXESS_RESULTS_AAA = {
    version: VERSION,
    normalize: normalizeResult,
    render: function () {
      var result = normalizeResult(getRawResult());
      if (result) render(result);
      else renderMissingState();
    }
  };

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', boot, { once: true });
  } else {
    boot();
  }

  window.addEventListener('maxess:result-ready', boot);

})(window, document);
