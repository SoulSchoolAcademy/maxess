/*
 MAXESS RESULTS V17 — FINAL DETERMINISTIC REPAIR

 Purpose:
 Repair the rendered Results experience after the accumulated V13/V18/V19/V19B
 presentation layers. This is intentionally a final deterministic DOM repair,
 not another scoring system or data source.

 Rules:
 - window.MAXESS_RESULT is the only production result source.
 - The existing Groove Results document remains the foundation.
 - One Naya introduction.
 - One primary Listen to Naya control.
 - Real overall score in the central orb.
 - Exactly five dimension mini-orbs.
 - No standalone score-zero hero label.
 - Existing lower report remains intact.
*/
(function () {
  'use strict';

  var ROOT_ID = 'maxess-results-10';
  var STYLE_ID = 'maxess-v17-final-style';
  var NAYA_IMAGE = 'https://i.postimg.cc/RF3XFWJ7/grok-image-c6a924fd-1f75-4ac8-840d-35b224fb3e52.jpg';
  var root = document.getElementById(ROOT_ID);
  if (!root || root.dataset.maxessV17Final === '1') return;

  var result = window.MAXESS_RESULT || null;
  var dims = Array.isArray(result && result.dimensions) ? result.dimensions.slice(0, 5) : [];
  var fallbackNames = ['Direction', 'Communication', 'Evaluation', 'Iteration', 'Systems Thinking'];
  while (dims.length < 5) dims.push({ name: fallbackNames[dims.length], score: 0 });

  var overall = Number(result && result.overallScore);
  if (!Number.isFinite(overall)) {
    overall = dims.reduce(function (sum, d) { return sum + (Number(d.score) || 0); }, 0) / 5;
  }
  overall = Math.max(0, Math.min(100, Math.round(overall)));

  function esc(v) {
    return String(v == null ? '' : v).replace(/[&<>\"']/g, function (c) {
      return ({ '&':'&amp;', '<':'&lt;', '>':'&gt;', '\"':'&quot;', "'":'&#39;' })[c];
    });
  }

  function score(d) {
    var n = Number(d && d.score);
    return Number.isFinite(n) ? Math.max(0, Math.min(100, Math.round(n))) : 0;
  }

  function band(s) {
    if (s < 50) return 'Building';
    if (s < 65) return 'Developing';
    if (s < 75) return 'Advancing';
    if (s < 85) return 'Strong';
    if (s < 95) return 'Mastery';
    return 'Exceptional';
  }

  function addStyle() {
    if (document.getElementById(STYLE_ID)) return;
    var s = document.createElement('style');
    s.id = STYLE_ID;
    s.textContent = `
      #${ROOT_ID} .v17-hero-naya{width:min(900px,100%);margin:0 auto 28px;display:grid;grid-template-columns:74px 1fr auto;gap:18px;align-items:center;padding:16px 18px;border:1px solid rgba(255,255,255,.13);border-radius:22px;background:linear-gradient(110deg,rgba(255,255,255,.075),rgba(166,108,255,.09),rgba(255,255,255,.025));box-shadow:0 18px 60px rgba(0,0,0,.28)}
      #${ROOT_ID} .v17-hero-naya img{width:74px;height:74px;border-radius:50%;object-fit:cover;border:2px solid rgba(255,255,255,.78);box-shadow:0 0 0 5px rgba(166,108,255,.1),0 10px 30px rgba(0,0,0,.35)}
      #${ROOT_ID} .v17-naya-kicker{font-size:10px;font-weight:900;letter-spacing:.18em;text-transform:uppercase;color:#caa6ff}
      #${ROOT_ID} .v17-naya-copy{margin-top:4px;color:rgba(255,255,255,.78);font-size:14px;line-height:1.45}
      #${ROOT_ID} .v17-naya-copy strong{color:#fff}
      #${ROOT_ID} .v17-naya-listen{display:inline-flex;align-items:center;justify-content:center;gap:9px;min-height:46px;padding:0 16px;border-radius:14px;border:1px solid rgba(255,255,255,.2);background:linear-gradient(135deg,#cda5ff,#7138c9);color:#fff;font-weight:850;white-space:nowrap;cursor:pointer;box-shadow:0 10px 30px rgba(113,56,201,.25)}
      #${ROOT_ID} .v17-naya-listen:hover{transform:translateY(-2px);filter:brightness(1.08)}
      #${ROOT_ID} .v17-play{width:22px;height:22px;border-radius:50%;display:grid;place-items:center;background:#fff;color:#35105e;font-size:9px}
      #${ROOT_ID} .v17-score-label{margin-top:12px;text-align:center;color:rgba(255,255,255,.48);font-size:10px;font-weight:900;letter-spacing:.2em;text-transform:uppercase}
      #${ROOT_ID} .v17-mini-orbs{display:grid;grid-template-columns:repeat(5,minmax(0,1fr));gap:12px;width:min(1000px,100%);margin:28px auto 0}
      #${ROOT_ID} .v17-mini-orb{position:relative;aspect-ratio:1;border-radius:50%;display:grid;place-items:center;text-align:center;padding:14px;background:radial-gradient(circle at 35% 25%,rgba(255,255,255,.16),rgba(255,255,255,.045) 35%,rgba(0,0,0,.35) 78%);border:1px solid rgba(255,255,255,.15);box-shadow:inset 0 0 30px rgba(255,255,255,.025),0 12px 34px rgba(0,0,0,.25);overflow:hidden;transition:transform .25s ease,border-color .25s ease,box-shadow .25s ease}
      #${ROOT_ID} .v17-mini-orb::before{content:"";position:absolute;inset:8%;border-radius:50%;border:2px solid var(--v17-c);opacity:.75;box-shadow:0 0 20px var(--v17-c)}
      #${ROOT_ID} .v17-mini-orb::after{content:"";position:absolute;inset:19%;border-radius:50%;background:conic-gradient(var(--v17-c) calc(var(--v17-score)*1%),rgba(255,255,255,.045) 0);mask:radial-gradient(farthest-side,transparent calc(100% - 6px),#000 calc(100% - 5px));-webkit-mask:radial-gradient(farthest-side,transparent calc(100% - 6px),#000 calc(100% - 5px));filter:drop-shadow(0 0 7px var(--v17-c));opacity:.8}
      #${ROOT_ID} .v17-mini-orb:hover{transform:translateY(-5px) scale(1.025);border-color:var(--v17-c);box-shadow:0 16px 42px rgba(0,0,0,.34),0 0 28px color-mix(in srgb,var(--v17-c) 22%,transparent)}
      #${ROOT_ID} .v17-mini-content{position:relative;z-index:3}
      #${ROOT_ID} .v17-mini-score{font-size:clamp(27px,3vw,42px);font-weight:900;line-height:.9;letter-spacing:-.07em}
      #${ROOT_ID} .v17-mini-name{margin-top:8px;font-size:9px;line-height:1.2;font-weight:900;letter-spacing:.08em;text-transform:uppercase;color:rgba(255,255,255,.72);max-width:100px}
      #${ROOT_ID} .v17-mini-dot{display:inline-block;width:6px;height:6px;border-radius:50%;background:var(--v17-c);box-shadow:0 0 12px var(--v17-c);margin-bottom:2px}
      @media(max-width:850px){#${ROOT_ID} .v17-hero-naya{grid-template-columns:58px 1fr;gap:13px}#${ROOT_ID} .v17-hero-naya img{width:58px;height:58px}#${ROOT_ID} .v17-naya-listen{grid-column:1/-1;width:100%}#${ROOT_ID} .v17-mini-orbs{grid-template-columns:repeat(5,minmax(90px,1fr));overflow-x:auto;padding:4px 2px 10px}#${ROOT_ID} .v17-mini-orb{min-width:90px}}
      @media(max-width:520px){#${ROOT_ID} .v17-hero-naya{padding:14px;border-radius:18px}#${ROOT_ID} .v17-mini-orbs{gap:9px}.v17-mini-orb{min-width:78px}#${ROOT_ID} .v17-mini-score{font-size:25px}#${ROOT_ID} .v17-mini-name{font-size:7px}}
      @media(prefers-reduced-motion:reduce){#${ROOT_ID} .v17-mini-orb,#${ROOT_ID} .v17-naya-listen{transition:none!important}}
    `;
    document.head.appendChild(s);
  }

  function findExistingListen() {
    var selectors = ['.v13-naya-listen', '.v18-naya-listen', '.v19-naya-listen', '[data-naya-listen]', 'button'];
    for (var i=0;i<selectors.length;i++) {
      var els = root.querySelectorAll(selectors[i]);
      for (var j=0;j<els.length;j++) {
        var t = (els[j].textContent || '').trim().toLowerCase();
        if (t.indexOf('listen to naya') !== -1 || els[j].getAttribute('aria-label') === 'Listen to Naya') return els[j];
      }
    }
    return null;
  }

  function removeDuplicateNayaAndListen(keep) {
    root.querySelectorAll('.v13-naya-intro,.v18-naya-intro,.v19-naya-intro,.v19b-naya-intro').forEach(function(el){el.remove();});
    root.querySelectorAll('button,a,[role="button"]').forEach(function(el){
      if (el === keep) return;
      var t=(el.textContent||'').trim().toLowerCase();
      var aria=(el.getAttribute('aria-label')||'').toLowerCase();
      if (t.indexOf('listen to naya')!==-1 || aria.indexOf('listen to naya')!==-1) el.remove();
    });
  }

  function buildHero() {
    var hero = root.querySelector('.mx-hero');
    if (!hero) return;
    var grid = hero.querySelector('.mx-hero-grid') || hero;
    var orb = hero.querySelector('.mx-score-orb');
    if (!orb) return;

    var originalListen = findExistingListen();
    var listenClone = originalListen ? originalListen.cloneNode(true) : null;
    if (originalListen) originalListen.style.display='none';

    var oldLabel = hero.querySelector('.v13-hero-label');
    if (oldLabel) oldLabel.remove();
    hero.querySelectorAll('.v13-print').forEach(function(el){el.remove();});

    var copy = hero.querySelector('.mx-hero-copy');
    if (copy) copy.remove();
    hero.querySelectorAll('.v13-naya-intro,.v18-naya-intro,.v19-naya-intro,.v19b-naya-intro').forEach(function(el){el.remove();});

    grid.style.display='flex';
    grid.style.flexDirection='column';
    grid.style.alignItems='center';
    grid.style.gap='0';
    grid.style.width='100%';
    grid.style.maxWidth='1200px';
    grid.style.margin='0 auto';

    var naya=document.createElement('div');
    naya.className='v17-hero-naya';
    naya.innerHTML='<img src="'+NAYA_IMAGE+'" alt="Naya, your MAXESS guide"><div><div class="v17-naya-kicker">Naya · Your Guide</div><div class="v17-naya-copy"><strong>Hi, I\'ve looked at your results.</strong> This isn\'t your judgment. It\'s your map.</div></div><button type="button" class="v17-naya-listen"><span class="v17-play">▶</span> Listen to Naya</button>';
    grid.insertBefore(naya, grid.firstChild);

    var btn=naya.querySelector('.v17-naya-listen');
    if (listenClone) {
      btn.addEventListener('click',function(){
        try { listenClone.click(); } catch(e) {}
      });
    }

    var scoreStrong=orb.querySelector('.mx-score strong');
    if (!scoreStrong) {
      var scoreWrap=document.createElement('div');
      scoreWrap.className='mx-score';
      scoreWrap.innerHTML='<strong></strong><span>AI SCORE</span>';
      orb.appendChild(scoreWrap);
      scoreStrong=scoreWrap.querySelector('strong');
    }
    scoreStrong.textContent=String(overall);
    var scoreSpan=orb.querySelector('.mx-score span');
    if (scoreSpan) scoreSpan.textContent='AI SCORE';
    orb.setAttribute('aria-label','Your AI Score is '+overall+' out of 100');
    orb.setAttribute('role','img');

    var label=document.createElement('div');
    label.className='v17-score-label';
    label.textContent='YOUR AI MASTERY SCORE · '+band(overall);
    orb.parentNode.insertBefore(label, orb.nextSibling);

    var oldMini=root.querySelectorAll('.v19b-dim-orbs,.v19b-orb-row,.v19-dim-orbs,.mx-aaa-gauge-grid');
    oldMini.forEach(function(el){el.remove();});

    var minis=document.createElement('div');
    minis.className='v17-mini-orbs';
    dims.forEach(function(d,i){
      var sc=score(d);
      var colors=['#ff9f0a','#34c759','#0a84ff','#af52de','#ff2d55'];
      var card=document.createElement('div');
      card.className='v17-mini-orb';
      card.style.setProperty('--v17-c',colors[i]);
      card.style.setProperty('--v17-score',sc);
      card.innerHTML='<div class="v17-mini-content"><div class="v17-mini-score">'+sc+'</div><div class="v17-mini-name"><span class="v17-mini-dot"></span> '+esc(d.name || fallbackNames[i])+'</div></div>';
      card.setAttribute('aria-label',(d.name || fallbackNames[i])+': '+sc+' out of 100');
      minis.appendChild(card);
    });
    label.after(minis);

    removeDuplicateNayaAndListen(listenClone);
    root.dataset.maxessV17Final='1';
  }

  function run() {
    addStyle();
    buildHero();
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', run, {once:true}); else run();
})();
