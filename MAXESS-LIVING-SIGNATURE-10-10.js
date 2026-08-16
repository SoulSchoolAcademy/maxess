/* MAXESS 10.10 — Living Signature + Resonance Orb
 *
 * Presentation-only renderer.
 * Sole source of truth: window.MAXESS_RESULT.
 * No DOM score scraping. No remote HTML replacement. No external libraries.
 *
 * Required result shape:
 * {
 *   overallScore: 0..100,
 *   band: string,
 *   dimensions: [{id,name,score,description?,insight?} x 5]
 * }
 */
(function () {
  'use strict';

  var ROOT_ID = 'maxess-results-10';
  var ORB_SELECTOR = '.mx-score-orb';
  var STYLE_ID = 'maxess-living-signature-10-10-style';
  var MOUNT_ID = 'maxess-living-signature-10-10';
  var DIMENSION_FALLBACK = [
    { id: 'direction', name: 'Direction' },
    { id: 'communication', name: 'Communication' },
    { id: 'evaluation', name: 'Evaluation' },
    { id: 'iteration', name: 'Iteration' },
    { id: 'systems-thinking', name: 'Systems Thinking' }
  ];

  function clamp(n) {
    n = Number(n);
    if (!isFinite(n)) return 0;
    return Math.max(0, Math.min(100, n));
  }

  function getResult() {
    var source = window.MAXESS_RESULT;
    if (!source || !Array.isArray(source.dimensions) || source.dimensions.length < 5) return null;

    var dimensions = source.dimensions.slice(0, 5).map(function (d, i) {
      var fallback = DIMENSION_FALLBACK[i];
      return {
        id: String(d && (d.id || fallback.id)),
        name: String(d && d.name || fallback.name),
        score: clamp(d && d.score),
        description: String(d && d.description || ''),
        insight: String(d && d.insight || '')
      };
    });

    return {
      overallScore: clamp(source.overallScore),
      band: String(source.band || ''),
      dimensions: dimensions
    };
  }

  function css() {
    if (document.getElementById(STYLE_ID)) return;
    var style = document.createElement('style');
    style.id = STYLE_ID;
    style.textContent = '\
#' + ROOT_ID + ' .mx-ls-stage{position:relative;width:min(610px,92vw);aspect-ratio:1;margin:auto;display:grid;place-items:center;isolation:isolate;--mx-energy:.6;--mx-speaking:0}\
#' + ROOT_ID + ' .mx-ls-stage:before{content:"";position:absolute;inset:7%;border-radius:50%;background:radial-gradient(circle,rgba(181,92,255,.25),rgba(73,37,132,.08) 40%,transparent 72%);filter:blur(26px);opacity:calc(.35 + var(--mx-energy)*.55);z-index:-3}\
#' + ROOT_ID + ' .mx-ls-stage:after{content:"";position:absolute;inset:1%;border-radius:50%;border:1px solid rgba(255,255,255,.045);box-shadow:0 0 100px rgba(141,66,255,.1),inset 0 0 90px rgba(111,48,208,.06);pointer-events:none;z-index:-2}\
#' + ROOT_ID + ' .mx-ls-svg{position:absolute;inset:0;width:100%;height:100%;overflow:visible;z-index:1}\
#' + ROOT_ID + ' .mx-ls-orbit{fill:none;stroke:rgba(225,204,255,.11);stroke-width:1;stroke-dasharray:2 13;transform-origin:50% 50%;animation:mxLsRotate 34s linear infinite}\
#' + ROOT_ID + ' .mx-ls-path{fill:none;stroke-linecap:round;vector-effect:non-scaling-stroke;transform-origin:50% 50%;filter:drop-shadow(0 0 8px rgba(164,85,255,.25));opacity:.65;transition:opacity .5s ease,stroke-width .5s ease}\
#' + ROOT_ID + ' .mx-ls-node{fill:#fff;stroke:#d8b8ff;stroke-width:1.2;filter:drop-shadow(0 0 8px rgba(191,106,255,.85))}\
#' + ROOT_ID + ' .mx-ls-core{position:relative;width:min(225px,37vw);aspect-ratio:1;border-radius:50%;display:grid;place-items:center;cursor:pointer;outline:none;z-index:5;transform:scale(calc(.95 + var(--mx-energy)*.065));transition:transform .45s cubic-bezier(.2,.8,.2,1),filter .35s ease}\
#' + ROOT_ID + ' .mx-ls-core:hover{filter:brightness(1.08)}\
#' + ROOT_ID + ' .mx-ls-core:focus-visible{box-shadow:0 0 0 4px rgba(223,193,255,.32),0 0 65px rgba(168,82,255,.38)}\
#' + ROOT_ID + ' .mx-ls-core:before{content:"";position:absolute;inset:6%;border-radius:50%;background:radial-gradient(circle at 30% 20%,rgba(255,255,255,.76),transparent 8%),radial-gradient(circle at 50% 47%,rgba(218,171,255,.92),rgba(126,50,224,.5) 32%,rgba(38,10,67,.96) 70%,#050208 100%);box-shadow:inset 0 4px 20px rgba(255,255,255,.15),inset 0 -30px 58px rgba(8,1,20,.82),0 0 0 1px rgba(255,255,255,.2),0 0 45px rgba(172,83,255,.42),0 0 110px rgba(127,48,222,.22)}\
#' + ROOT_ID + ' .mx-ls-core:after{content:"";position:absolute;inset:0;border-radius:50%;border:1px solid rgba(228,205,255,.28);box-shadow:inset 0 0 30px rgba(192,108,255,.18);animation:mxLsBreathe 4.4s ease-in-out infinite}\
#' + ROOT_ID + ' .mx-ls-core-copy{position:relative;z-index:4;text-align:center;pointer-events:none}\
#' + ROOT_ID + ' .mx-ls-score{display:block;font-size:clamp(58px,8vw,100px);line-height:.82;letter-spacing:-.085em;font-weight:850;text-shadow:0 4px 24px rgba(0,0,0,.65),0 0 36px rgba(207,151,255,.2)}\
#' + ROOT_ID + ' .mx-ls-label{display:block;margin-top:20px;color:rgba(239,219,255,.82);font-size:9px;font-weight:900;letter-spacing:.23em;text-transform:uppercase}\
#' + ROOT_ID + ' .mx-ls-ripple{position:absolute;inset:6%;border-radius:50%;border:1px solid rgba(216,177,255,0);pointer-events:none;opacity:0;z-index:3}\
#' + ROOT_ID + ' .mx-ls-stage.speaking .mx-ls-ripple{animation:mxLsVoice 1s ease-out infinite}\
#' + ROOT_ID + ' .mx-ls-stage.speaking .mx-ls-core:after{animation:mxLsSpeak .68s ease-in-out infinite}\
#' + ROOT_ID + ' .mx-ls-stage.excited .mx-ls-core{filter:brightness(1.18) saturate(1.1)}\
#' + ROOT_ID + ' .mx-ls-stage.excited .mx-ls-ripple{animation:mxLsVoice .72s ease-out 2}\
#' + ROOT_ID + ' .mx-ls-labels{position:absolute;inset:0;z-index:6;pointer-events:none}\
#' + ROOT_ID + ' .mx-ls-dim-label{position:absolute;min-width:92px;padding:7px 9px;border:1px solid rgba(255,255,255,.12);border-radius:999px;background:rgba(5,3,9,.7);backdrop-filter:blur(12px);-webkit-backdrop-filter:blur(12px);color:rgba(255,255,255,.74);font-size:8px;font-weight:900;letter-spacing:.11em;text-align:center;text-transform:uppercase;opacity:0;transform:translate(-50%,-50%) scale(.9);transition:opacity .3s ease,transform .3s ease}\
#' + ROOT_ID + ' .mx-ls-stage.open .mx-ls-dim-label,#' + ROOT_ID + ' .mx-ls-stage:hover .mx-ls-dim-label,#' + ROOT_ID + ' .mx-ls-stage:focus-within .mx-ls-dim-label{opacity:1;transform:translate(-50%,-50%) scale(1)}\
#' + ROOT_ID + ' .mx-ls-hint{position:absolute;left:50%;bottom:1%;transform:translateX(-50%);color:rgba(255,255,255,.32);font-size:8px;font-weight:800;letter-spacing:.12em;text-transform:uppercase;white-space:nowrap;pointer-events:none}\
@keyframes mxLsBreathe{0%,100%{transform:scale(.985);opacity:.62}50%{transform:scale(1.02);opacity:1}}\
@keyframes mxLsSpeak{0%,100%{transform:scale(.985);opacity:.5}45%{transform:scale(1.075);opacity:1}72%{transform:scale(1.03);opacity:.8}}\
@keyframes mxLsVoice{0%{transform:scale(.72);opacity:.72}100%{transform:scale(1.22);opacity:0}}\
@keyframes mxLsRotate{to{transform:rotate(360deg)}}\
@media(max-width:900px){#' + ROOT_ID + ' .mx-ls-stage{width:min(610px,94vw);order:-1}}\
@media(max-width:600px){#' + ROOT_ID + ' .mx-ls-stage{width:96vw}#' + ROOT_ID + ' .mx-ls-core{width:min(198px,43vw)}#' + ROOT_ID + ' .mx-ls-score{font-size:clamp(52px,14vw,78px)}#' + ROOT_ID + ' .mx-ls-dim-label{min-width:72px;font-size:7px;padding:6px 7px}}\
@media(prefers-reduced-motion:reduce){#' + ROOT_ID + ' .mx-ls-orbit,#' + ROOT_ID + ' .mx-ls-core:after,#' + ROOT_ID + ' .mx-ls-stage.speaking .mx-ls-ripple{animation:none!important}#' + ROOT_ID + ' .mx-ls-path,#' + ROOT_ID + ' .mx-ls-dim-label{transition:none!important}}\
';
    document.head.appendChild(style);
  }

  function polar(cx, cy, r, a) {
    var angle = a - Math.PI / 2;
    return [cx + Math.cos(angle) * r, cy + Math.sin(angle) * r];
  }

  function pathFor(score, index) {
    var points = [];
    var base = 125 + index * 7;
    var amplitude = 9 + score * .18;
    var phase = index * 1.17;
    for (var i = 0; i <= 56; i++) {
      var t = i / 56;
      var a = t * Math.PI * 2;
      var wave = Math.sin(a * (2.2 + index * .24) + phase) * amplitude;
      wave += Math.sin(a * (5 + index * .15) - phase) * amplitude * .25;
      wave += Math.cos(a * 3.1 + score * .018) * score * .045;
      points.push(polar(300, 300, base + wave, a));
    }
    var d = '';
    for (var p = 0; p < points.length - 1; p++) {
      var cur = points[p];
      var next = points[p + 1];
      if (p === 0) d += 'M ' + cur[0].toFixed(2) + ' ' + cur[1].toFixed(2) + ' ';
      d += 'L ' + next[0].toFixed(2) + ' ' + next[1].toFixed(2) + ' ';
    }
    return d + 'Z';
  }

  function hue(index) {
    return [274, 242, 212, 300, 178][index] || 274;
  }

  function render(stage, result) {
    var labels = [
      ['50%', '8%'], ['91%', '31%'], ['78%', '87%'], ['22%', '87%'], ['9%', '31%']
    ];
    var paths = result.dimensions.map(function (d, i) {
      var op = (.22 + d.score / 100 * .48).toFixed(2);
      var width = (1.1 + d.score / 100 * 2.8).toFixed(2);
      var dash = Math.round(780 - d.score * 3.1);
      var dur = (17 + i * 1.15 - d.score * .025).toFixed(2);
      return '<path class="mx-ls-path" d="' + pathFor(d.score, i) + '" stroke="hsla(' + hue(i) + ',92%,76%,' + op + ')" stroke-width="' + width + '" stroke-dasharray="' + dash + '" style="animation:mxLsOrbit' + i + ' ' + dur + 's linear infinite"/>';
    }).join('');

    var keyframes = result.dimensions.map(function (_, i) {
      return '@keyframes mxLsOrbit' + i + '{to{transform:rotate(' + (i % 2 ? '-' : '') + '360deg)}}';
    }).join('');
    var keyStyle = document.createElement('style');
    keyStyle.id = MOUNT_ID + '-motion';
    keyStyle.textContent = keyframes;
    document.head.appendChild(keyStyle);

    var nodes = result.dimensions.map(function (d, i) {
      var pos = polar(300, 300, 165 + d.score * .34, (Math.PI * 2 / 5) * i);
      return '<circle class="mx-ls-node" cx="' + pos[0].toFixed(1) + '" cy="' + pos[1].toFixed(1) + '" r="' + (3.5 + d.score / 45).toFixed(1) + '"/>';
    }).join('');

    var labelMarkup = result.dimensions.map(function (d, i) {
      return '<span class="mx-ls-dim-label" style="left:' + labels[i][0] + ';top:' + labels[i][1] + '">' + escapeHtml(d.name) + '</span>';
    }).join('');

    var energy = (0.32 + result.overallScore / 100 * .68).toFixed(3);
    stage.style.setProperty('--mx-energy', energy);
    stage.innerHTML = '<svg class="mx-ls-svg" viewBox="0 0 600 600" role="img" aria-label="Your five-dimensional MAXESS capability signature"><circle class="mx-ls-orbit" cx="300" cy="300" r="245"/><circle class="mx-ls-orbit" cx="300" cy="300" r="205" opacity=".45"/>' + paths + nodes + '</svg><div class="mx-ls-labels" aria-hidden="true">' + labelMarkup + '</div><button class="mx-ls-core" type="button" aria-label="Reveal your five MAXESS dimensions"><span class="mx-ls-core-copy"><strong class="mx-ls-score">' + Math.round(result.overallScore) + '</strong><span class="mx-ls-label">MAXESS SCORE · ' + escapeHtml(result.band || 'YOUR RESULT') + '</span></span><span class="mx-ls-ripple"></span></button><span class="mx-ls-hint">Tap or hover the core to reveal your pattern</span>';

    var core = stage.querySelector('.mx-ls-core');
    core.addEventListener('click', function () { stage.classList.toggle('open'); });
    core.addEventListener('keydown', function (event) {
      if (event.key === 'Escape') stage.classList.remove('open');
    });

    var existing = stage.querySelector('.mx-ls-motion');
    if (existing) existing.remove();
  }

  function escapeHtml(value) {
    return String(value).replace(/[&<>\"']/g, function (c) {
      return {'&':'&amp;','<':'&lt;','>':'&gt;','\"':'&quot;',"'":'&#39;'}[c];
    });
  }

  function speakPulse(stage, excited) {
    if (!stage) return;
    stage.classList.add('speaking');
    if (excited) {
      stage.classList.remove('excited');
      void stage.offsetWidth;
      stage.classList.add('excited');
      setTimeout(function () { stage.classList.remove('excited'); }, 1500);
    }
    clearTimeout(stage._mxVoiceTimer);
    stage._mxVoiceTimer = setTimeout(function () { stage.classList.remove('speaking'); }, 620);
  }

  function bindVoice(stage) {
    window.addEventListener('maxess:naya:start', function () { speakPulse(stage, false); });
    window.addEventListener('maxess:naya:word', function () { speakPulse(stage, false); });
    window.addEventListener('maxess:naya:positive', function () { speakPulse(stage, true); });
    window.addEventListener('maxess:naya:stop', function () { stage.classList.remove('speaking'); });

    document.addEventListener('play', function (event) {
      if (event.target && event.target.tagName === 'AUDIO') {
        speakPulse(stage, false);
      }
    }, true);
  }

  function boot() {
    var result = getResult();
    var root = document.getElementById(ROOT_ID);
    if (!root || !result) return;
    var orb = root.querySelector(ORB_SELECTOR);
    if (!orb || orb.querySelector('#' + MOUNT_ID)) return;
    css();
    var stage = document.createElement('div');
    stage.id = MOUNT_ID;
    stage.className = 'mx-ls-stage';
    orb.innerHTML = '';
    orb.appendChild(stage);
    render(stage, result);
    bindVoice(stage);
    root.setAttribute('data-living-signature', '10.10');
    root.setAttribute('data-result-source', 'window.MAXESS_RESULT');
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', boot, { once: true });
  } else {
    boot();
  }
})();
