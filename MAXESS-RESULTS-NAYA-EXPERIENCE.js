/*
 * MAXESS RESULTS — NAYA EXPERIENCE LAYER
 *
 * This layer sits on top of the authoritative Results renderer.
 * It does not score, normalize, or invent result data.
 * It changes presentation, narrative presence, section order, and interaction.
 */
(function MAXESSNayaExperience(window, document) {
  'use strict';

  var ROOT_ID = 'maxess-results-10';
  var NAYA_IMAGE = 'https://i.postimg.cc/dVXw7sRN/grok-image-f75a6f12-4e3a-4c99-a334-5684ba0f7401.jpg';

  function root() { return document.getElementById(ROOT_ID); }
  function esc(value) {
    return String(value == null ? '' : value).replace(/[&<>\"']/g, function (c) {
      return {'&':'&amp;','<':'&lt;','>':'&gt;','\"':'&quot;',"'":'&#39;'}[c];
    });
  }

  function result() {
    var raw = window.MAXESS_RESULT;
    if (!raw || !Array.isArray(raw.dimensions)) return null;
    var ds = raw.dimensions.map(function (d) { return { name: d.name, score: Number(d.score) || 0 }; });
    var strongest = ds.slice().sort(function(a,b){return b.score-a.score;})[0];
    var opportunity = ds.slice().sort(function(a,b){return a.score-b.score;})[0];
    return { strongest: strongest, opportunity: opportunity, overall: Number(raw.overallScore != null ? raw.overallScore : raw.score) || 0 };
  }

  function guide(text, tone) {
    return '<div class="ny-guide ny-guide-' + (tone || 'warm') + '">' +
      '<div class="ny-avatar-wrap"><img class="ny-avatar" src="' + NAYA_IMAGE + '" alt="Naya" loading="lazy"><span class="ny-avatar-pulse" aria-hidden="true"></span></div>' +
      '<div class="ny-guide-copy"><span class="ny-guide-name">Naya</span><p>' + esc(text) + '</p></div>' +
      '</div>';
  }

  function insertGuides(r) {
    var messages = {
      'mx-signature': 'I looked at the shape of your results first. The interesting part is not just the number — it is how your capabilities work together.',
      'mx-meaning': 'Let me translate the scores into something useful. Numbers are only valuable when you can recognize yourself in them.',
      'mx-advantage': 'Okay, this one deserves some attention. This is the capability I would build on first because you already have real strength here.',
      'mx-opportunity': 'And here is the interesting part. I do not see a weakness here. I see your biggest unlock.',
      'mx-dimensions': 'Now let’s go one level deeper. These five capabilities are different, but together they create your AI fingerprint.',
      'mx-pathways': 'You have 18 doors you can explore. I do not want you to open all of them at once — I want to show you where your result suggests you will get the most leverage.',
      'mx-next': 'You do not need twenty things to work on. You need one useful next move. Let’s make it simple.',
      'mx-masters': 'You do not have to become an expert in everything. You can call on specialist Naya Masters when you need them.',
      'mx-naya': 'This is where your report stops being a report. Bring me the next thing you actually want to accomplish, and we can work on it together.'
    };
    Object.keys(messages).forEach(function(id){
      var section = document.getElementById(id);
      if (!section || section.querySelector('.ny-guide')) return;
      var wrap = section.querySelector('.mx-wrap');
      if (!wrap) return;
      var tone = id === 'mx-opportunity' ? 'gold' : id === 'mx-advantage' ? 'green' : id === 'mx-naya' ? 'violet' : 'warm';
      var node = document.createElement('div');
      node.innerHTML = guide(messages[id], tone);
      wrap.insertBefore(node.firstChild, wrap.firstChild);
    });

    var hero = document.getElementById('mx-result-arrival');
    if (hero && !hero.querySelector('.ny-hero-presence')) {
      var center = hero.querySelector('.mx-hero-center');
      if (center) {
        var node = document.createElement('div');
        node.className = 'ny-hero-presence';
        node.innerHTML = '<img src="' + NAYA_IMAGE + '" alt="Naya" class="ny-hero-avatar"><div><strong>Hi. I’m Naya.</strong><span>I’m going to walk through this with you.</span></div>';
        center.insertBefore(node, center.firstChild);
      }
    }
  }

  function reorder() {
    var r = root(); if (!r) return;
    var order = [
      'mx-result-arrival',
      'mx-signature',
      'mx-meaning',
      'mx-advantage',
      'mx-opportunity',
      'mx-dimensions',
      'mx-revelation',
      'mx-next',
      'mx-pathways',
      'mx-playground',
      'mx-masters',
      'mx-craftsmanship',
      'mx-master-ai',
      'mx-naya',
      'mx-report',
      'mx-transition'
    ];
    order.forEach(function(id){ var node = document.getElementById(id); if(node) r.appendChild(node); });
  }

  function playground(r) {
    if (document.getElementById('mx-playground')) return;
    var sec = document.createElement('section');
    sec.id = 'mx-playground';
    sec.className = 'mx-section ny-playground';
    sec.innerHTML = '<div class="mx-wrap">' +
      '<div class="ny-section-intro">' + guide('You know your strengths. Now let’s put them to work.', 'violet') + '</div>' +
      '<span class="mx-eyebrow">AI PLAYGROUND</span><h2>Let’s make something.</h2>' +
      '<p class="mx-copy">Pick a starting point. I’ll help you turn your capability into something real.</p>' +
      '<div class="ny-play-grid">' +
        '<button class="ny-play-card" data-play="writer"><span class="ny-play-icon">✦</span><strong>Naya Writer</strong><small>Turn an idea into clear, powerful words.</small><b>Open Writer →</b></button>' +
        '<button class="ny-play-card" data-play="brainstormer"><span class="ny-play-icon">✧</span><strong>Naya Ideator</strong><small>Turn one possibility into a field of possibilities.</small><b>Start Brainstorming →</b></button>' +
        '<button class="ny-play-card" data-play="naya"><span class="ny-play-icon">◉</span><strong>Talk to Naya</strong><small>Ask me what I see in your result.</small><b>Start a Conversation →</b></button>' +
      '</div></div>';
    r.appendChild(sec);
  }

  function bindPlayground(r) {
    r.querySelectorAll('[data-play]').forEach(function(btn){
      btn.addEventListener('click', function(){
        var type = btn.getAttribute('data-play');
        var played = false;
        if (type === 'naya') {
          var candidates = ['maxessNayaPlayOriginal','maxessNayaPlay'];
          candidates.some(function(id){ var el=document.getElementById(id); if(el){try{el.click();return true;}catch(e){} } return false; });
        }
        if (typeof window.MAXESS_PLAYGROUND_OPEN === 'function') {
          try { window.MAXESS_PLAYGROUND_OPEN(type, window.MAXESS_RESULT || null); played = true; } catch(e) {}
        }
        if (!played) window.dispatchEvent(new CustomEvent('maxess:playground-request', {detail:{tool:type,result:window.MAXESS_RESULT||null}}));
      });
    });
  }

  function installStyles() {
    if (document.getElementById('maxess-naya-experience-css')) return;
    var style = document.createElement('style');
    style.id = 'maxess-naya-experience-css';
    style.textContent = '\n' +
      '#maxess-results-10{--ny-radius:42px;--ny-soft-radius:58% 42% 52% 48% / 45% 55% 45% 55%;}\n' +
      '#maxess-results-10 .ny-guide{display:flex;align-items:center;gap:16px;max-width:720px;margin:0 0 34px;padding:12px 20px 12px 12px;border-radius:999px;background:rgba(255,255,255,.72);border:1px solid rgba(0,0,0,.08);box-shadow:0 18px 55px rgba(0,0,0,.08);backdrop-filter:blur(18px);position:relative;z-index:2}\n' +
      '#maxess-results-10 .mx-dark .ny-guide,#maxess-results-10 .mx-violet .ny-guide,#maxess-results-10 .mx-emerald .ny-guide,#maxess-results-10 .mx-gold .ny-guide,#maxess-results-10 .mx-blue .ny-guide{background:rgba(255,255,255,.08);border-color:rgba(255,255,255,.14);box-shadow:0 20px 60px rgba(0,0,0,.25);color:#fff}\n' +
      '#maxess-results-10 .ny-guide-gold{background:rgba(255,247,218,.9)}\n' +
      '#maxess-results-10 .ny-guide-green{background:rgba(230,255,245,.9)}\n' +
      '#maxess-results-10 .ny-guide-violet{background:rgba(245,237,255,.9)}\n' +
      '#maxess-results-10 .ny-avatar-wrap{position:relative;flex:0 0 auto;width:58px;height:58px}\n' +
      '#maxess-results-10 .ny-avatar{width:58px;height:58px;display:block;object-fit:cover;border-radius:50%;border:2px solid rgba(255,255,255,.8);box-shadow:0 8px 25px rgba(0,0,0,.18)}\n' +
      '#maxess-results-10 .ny-avatar-pulse{position:absolute;right:0;bottom:1px;width:13px;height:13px;border-radius:50%;background:#51e2ad;border:3px solid #fff;box-shadow:0 0 0 5px rgba(81,226,173,.13)}\n' +
      '#maxess-results-10 .ny-guide-name{display:block;font-size:11px;font-weight:900;letter-spacing:.12em;text-transform:uppercase;color:#9a61dc;margin-bottom:3px}\n' +
      '#maxess-results-10 .mx-dark .ny-guide-name,#maxess-results-10 .mx-violet .ny-guide-name,#maxess-results-10 .mx-emerald .ny-guide-name,#maxess-results-10 .mx-gold .ny-guide-name,#maxess-results-10 .mx-blue .ny-guide-name{color:#d9baff}\n' +
      '#maxess-results-10 .ny-guide p{margin:0;font-size:15px;line-height:1.45;color:#444}\n' +
      '#maxess-results-10 .mx-dark .ny-guide p,#maxess-results-10 .mx-violet .ny-guide p,#maxess-results-10 .mx-emerald .ny-guide p,#maxess-results-10 .mx-gold .ny-guide p,#maxess-results-10 .mx-blue .ny-guide p{color:rgba(255,255,255,.78)}\n' +
      '#maxess-results-10 .ny-hero-presence{display:flex;align-items:center;justify-content:center;gap:13px;margin:0 auto 18px;position:relative;z-index:6}\n' +
      '#maxess-results-10 .ny-hero-avatar{width:68px;height:68px;border-radius:50%;object-fit:cover;border:2px solid rgba(255,255,255,.72);box-shadow:0 0 35px rgba(166,108,255,.4)}\n' +
      '#maxess-results-10 .ny-hero-presence div{text-align:left}\n' +
      '#maxess-results-10 .ny-hero-presence strong{display:block;font-size:17px}\n' +
      '#maxess-results-10 .ny-hero-presence span{display:block;color:rgba(255,255,255,.58);font-size:12px;margin-top:2px}\n' +
      '#maxess-results-10 .mx-dimension-card,#maxess-results-10 .mx-meaning-card,#maxess-results-10 .mx-feature,#maxess-results-10 .mx-next-main,#maxess-results-10 .mx-next-action,#maxess-results-10 .mx-path-card,#maxess-results-10 .mx-master-card,#maxess-results-10 .mx-report-card,#maxess-results-10 .mx-reveal-box{border-radius:var(--ny-radius);}\n' +
      '#maxess-results-10 .mx-dimension-card,#maxess-results-10 .mx-path-card,#maxess-results-10 .mx-master-card{position:relative;overflow:hidden}\n' +
      '#maxess-results-10 .mx-dimension-card:before,#maxess-results-10 .mx-path-card:before,#maxess-results-10 .mx-master-card:before{content:"";position:absolute;width:170px;height:170px;right:-85px;top:-85px;border-radius:50%;background:radial-gradient(circle,rgba(255,255,255,.11),transparent 68%);pointer-events:none}\n' +
      '#maxess-results-10 .ny-playground{background:radial-gradient(circle at 50% 0,rgba(166,108,255,.24),transparent 48%),#07040b;color:#fff}\n' +
      '#maxess-results-10 .ny-section-intro{margin-bottom:28px}\n' +
      '#maxess-results-10 .ny-play-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin-top:34px}\n' +
      '#maxess-results-10 .ny-play-card{position:relative;text-align:left;padding:34px;border:1px solid rgba(255,255,255,.14);border-radius:46px;background:radial-gradient(circle at 100% 0,rgba(166,108,255,.18),transparent 38%),rgba(255,255,255,.045);color:#fff;min-height:260px;display:flex;flex-direction:column;align-items:flex-start;cursor:pointer;box-shadow:0 25px 70px rgba(0,0,0,.3);transition:transform .25s cubic-bezier(.2,.8,.2,1),border-color .25s ease,box-shadow .25s ease}\n' +
      '#maxess-results-10 .ny-play-card:hover,#maxess-results-10 .ny-play-card:focus-visible{transform:translateY(-8px) rotate(-.25deg);border-color:rgba(210,177,255,.5);box-shadow:0 35px 90px rgba(72,25,130,.35);outline:none}\n' +
      '#maxess-results-10 .ny-play-icon{width:66px;height:66px;display:grid;place-items:center;border-radius:50%;background:linear-gradient(145deg,#d6b8ff,#6635a8);font-size:28px;box-shadow:0 10px 35px rgba(166,108,255,.3),inset 0 1px rgba(255,255,255,.7)}\n' +
      '#maxess-results-10 .ny-play-card strong{font-size:28px;letter-spacing:-.04em;margin-top:24px}\n' +
      '#maxess-results-10 .ny-play-card small{color:rgba(255,255,255,.64);font-size:14px;line-height:1.5;margin-top:8px;max-width:300px}\n' +
      '#maxess-results-10 .ny-play-card b{margin-top:auto;padding-top:24px;color:#d7baff;font-size:12px;letter-spacing:.08em;text-transform:uppercase}\n' +
      '#maxess-results-10 .mx-section{position:relative}\n' +
      '#maxess-results-10 .mx-section:after{content:"";position:absolute;left:5%;right:5%;bottom:0;height:1px;background:linear-gradient(90deg,transparent,rgba(166,108,255,.16),transparent);pointer-events:none}\n' +
      '@media(max-width:820px){#maxess-results-10 .ny-play-grid{grid-template-columns:1fr 1fr}}\n' +
      '@media(max-width:600px){#maxess-results-10 .ny-guide{border-radius:28px;padding:10px 14px 10px 10px;align-items:flex-start}#maxess-results-10 .ny-avatar-wrap,#maxess-results-10 .ny-avatar{width:50px;height:50px}#maxess-results-10 .ny-guide p{font-size:14px}#maxess-results-10 .ny-play-grid{grid-template-columns:1fr}#maxess-results-10 .ny-play-card{min-height:220px;padding:28px;border-radius:36px}}\n' +
      '@media(prefers-reduced-motion:reduce){#maxess-results-10 .ny-play-card{transition:none}}\n' +
      '@media print{#maxess-results-10 .ny-guide{box-shadow:none;background:#fff!important;color:#111!important}#maxess-results-10 .ny-avatar-pulse{display:none}#maxess-results-10 .ny-playground{background:#fff!important;color:#111!important}.ny-play-card{color:#111!important;background:#fff!important;border:1px solid #aaa!important;box-shadow:none!important}}\n';
    document.head.appendChild(style);
  }

  function boot() {
    var r = root(); if (!r) return;
    if (r.dataset.nayaLayer === '1') return;
    var data = result();
    if (!data) return;
    installStyles();
    reorder();
    playground(r);
    insertGuides(data);
    bindPlayground(r);
    r.dataset.nayaLayer = '1';
    r.dataset.nayaExperience = 'naya-led-organic-1.0';
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', function(){ setTimeout(boot, 0); }, {once:true});
  else setTimeout(boot, 0);
  window.addEventListener('maxess:result-ready', function(){ setTimeout(boot, 0); });
  window.MAXESS_NAYA_EXPERIENCE = { version:'naya-led-organic-1.0', boot:boot };
})(window, document);
