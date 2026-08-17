/* MAXESS RESULTS — V17.1 PRESERVATION FINISH PASS
   Purpose:
   - Preserve the existing Groove Results experience.
   - Do NOT remove or replace the V13/V15 rendered experience.
   - Do NOT create a second Results renderer.
   - Normalize the final visible hierarchy in place.
   - Use only window.MAXESS_RESULT for score/dimension data.
*/
(function () {
  'use strict';

  function esc(value) {
    return String(value == null ? '' : value).replace(/[&<>"']/g, function (c) {
      return ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'})[c];
    });
  }

  function clamp(n) {
    return Math.max(0, Math.min(100, Number(n) || 0));
  }

  function boot() {
    var root = document.getElementById('maxess-results-10');
    if (!root || root.dataset.v171FinishPass === '1') return;
    root.dataset.v171FinishPass = '1';

    var result = window.MAXESS_RESULT || {};
    var scoreValue = clamp(result.overallScore != null ? result.overallScore :
                           (result.score != null ? result.score : result.masterScore));

    var dimensions = Array.isArray(result.dimensions)
      ? result.dimensions.slice(0, 5).map(function (d, i) {
          return {
            name: d && (d.name || d.label) || ('Dimension ' + (i + 1)),
            score: clamp(d && (d.score != null ? d.score : d.value))
          };
        })
      : [];

    /* The rendered V13/V15 shell is the existing experience. Preserve it. */
    var shell = root.querySelector('.v13-shell') || root;

    /* ---------- HERO: preserve the real orb, remove competing hero copy ---------- */
    var hero = shell.querySelector('.v13-hero') || shell.querySelector('.mx-hero');
    if (!hero) return;

    var orb = hero.querySelector('.v13-score-orb') || hero.querySelector('.mx-score-orb');
    if (!orb) return;

    /* Remove duplicate/competing hero presentation elements only. */
    hero.querySelectorAll(
      '.v13-hero-tools, .v15-print, .v12-print, .hero-score-whisper, .mx-proof'
    ).forEach(function (el) { el.remove(); });

    var heroCopy = hero.querySelector('.v13-hero-copy') ||
                   hero.querySelector('.mx-hero-grid > div:first-child');

    if (heroCopy) {
      heroCopy.querySelectorAll('.mx-copy, .mx-proof, .hero-score-whisper, .mx-band').forEach(function (el) {
        el.remove();
      });

      var title = heroCopy.querySelector('h1, .mx-title');
      if (title) title.textContent = 'YOUR AI SCORE';

      var eyebrow = heroCopy.querySelector('.mx-eyebrow, .v13-overline');
      if (eyebrow) eyebrow.textContent = 'MAXESS AI MASTERY ASSESSMENT';

      /* No giant competing paragraph/title stack. */
      heroCopy.querySelectorAll('.v13-sub, .v13-score-label, .v13-score-value, .v13-score-caption').forEach(function (el) {
        if (!el.closest('.v13-orb-wrap')) el.remove();
      });

      /* Keep one primary hero action only if one already exists. */
      var actions = heroCopy.querySelector('.mx-hero-actions, .v13-hero-actions');
      if (actions) {
        var links = Array.prototype.slice.call(actions.querySelectorAll('a,button'));
        links.slice(1).forEach(function (el) { el.remove(); });
        if (links[0]) {
          links[0].textContent = 'See Your Results ↓';
          links[0].setAttribute('href', '#v171-naya');
        }
      }
    }

    /* Sync the authoritative score into the existing orb. */
    var orbScore = orb.querySelector('.mx-score strong, .v13-score-number');
    if (orbScore) orbScore.textContent = String(Math.round(scoreValue));

    var orbLabel = orb.querySelector('.mx-score span, .v13-score-caption');
    if (orbLabel) orbLabel.textContent = 'AI SCORE';

    orb.setAttribute('role', 'img');
    orb.setAttribute('aria-label', 'Your AI Score is ' + Math.round(scoreValue) + ' out of 100');

    /* ---------- NAYA: exactly one visible welcome card ---------- */
    var nayaCandidates = Array.prototype.slice.call(shell.querySelectorAll(
      '.v11-naya-welcome, #v12-naya, .v13-naya, .v13-naya-intro, #v13-naya-introduction, #v12-naya, .mx-recognition-naya'
    ));

    var naya = shell.querySelector('.v11-naya-welcome') ||
               shell.querySelector('#v13-naya-introduction') ||
               shell.querySelector('.v13-naya-intro');

    if (!naya) {
      /* Reuse an existing Naya report card if the prior pass renamed it. */
      naya = shell.querySelector('#v11-naya-report .v11-naya-panel, #v12-report .v12-naya-intro');
    }

    if (naya) {
      naya.id = 'v171-naya';

      var kicker = naya.querySelector('.v11-naya-kicker, .v13-naya-kicker, .v12-naya-kicker');
      if (kicker) kicker.textContent = 'NAYA · YOUR AI GUIDE';

      var title = naya.querySelector('.v11-naya-title, .v13-naya-title, .v12-naya-title, h2');
      if (title) title.textContent = "Hi. I've looked at your results.";

      var copy = naya.querySelector('.v11-naya-copy, .v13-naya-copy, .v12-naya-copy, p');
      if (copy) copy.innerHTML = "This isn't your judgment.<br>It's your map.";

      var avatar = naya.querySelector('img');
      if (avatar) {
        avatar.alt = 'Naya, your AI guide';
        avatar.loading = 'eager';
      }

      var listen = naya.querySelector('button, a');
      if (listen) {
        listen.textContent = 'Listen to Naya ▶';
        listen.setAttribute('aria-label', 'Listen to Naya interpret your results');
      }

      /* Remove every other Naya intro card, but never remove the actual report section. */
      nayaCandidates.forEach(function (candidate) {
        if (candidate !== naya && candidate !== naya.closest('section')) {
          candidate.remove();
        }
      });

      /* Place Naya first inside the hero, above the score. */
      if (naya.parentNode) naya.parentNode.removeChild(naya);
      var heroGrid = hero.querySelector('.v13-hero-grid, .mx-hero-grid') || hero;
      heroGrid.insertBefore(naya, heroGrid.firstChild);
    }

    /* ---------- EXACTLY FIVE subordinate dimension mini-orbs ---------- */
    if (dimensions.length === 5) {
      var mini = document.getElementById('v171-five-dimensions');

      if (!mini) {
        mini = document.createElement('div');
        mini.id = 'v171-five-dimensions';
        mini.setAttribute('aria-label', 'Your five AI capability dimensions');
        orb.insertAdjacentElement('afterend', mini);
      }

      mini.innerHTML = dimensions.map(function (d) {
        var safe = clamp(d.score);
        return (
          '<button class="v171-mini-orb" type="button" aria-label="' +
          esc(d.name) + ', ' + Math.round(safe) + ' out of 100">' +
            '<span class="v171-mini-ring" style="--score:' + safe + '%">' +
              '<b>' + Math.round(safe) + '</b>' +
            '</span>' +
            '<span class="v171-mini-name">' + esc(d.name) + '</span>' +
          '</button>'
        );
      }).join('');

      mini.querySelectorAll('.v171-mini-orb').forEach(function (button) {
        button.addEventListener('click', function () {
          var target =
            shell.querySelector('#v15-pattern, #v13-pattern, #v11-fingerprint, #v12-dimensions') ||
            Array.prototype.slice.call(shell.querySelectorAll('section')).find(function (section) {
              return /five dimensions|fingerprint/i.test(section.textContent || '');
            });

          if (target) target.scrollIntoView({ behavior: 'smooth', block: 'start' });
        });
      });
    }

    /* ---------- NARRATIVE ORDER: reorder existing sections, do not rebuild them ---------- */
    function findSection(selectors, terms) {
      for (var i = 0; i < selectors.length; i++) {
        var direct = shell.querySelector(selectors[i]);
        if (direct) return direct;
      }

      var sections = Array.prototype.slice.call(shell.querySelectorAll(':scope > section'));
      return sections.find(function (section) {
        var text = (section.textContent || '').toLowerCase();
        return terms.some(function (term) { return text.indexOf(term) !== -1; });
      });
    }

    var report = findSection(
      ['#v15-report', '#v13-report', '#v12-report', '#v11-naya-report'],
      ['your report', 'listen to your results']
    );

    var pattern = findSection(
      ['#v15-pattern', '#v13-pattern', '#v12-pattern', '#v11-pattern', '#v11-fingerprint'],
      ['see the pattern', 'your fingerprint']
    );

    var dimSection = findSection(
      ['#v13-dimensions', '#v12-dimensions', '#v11-dimensions'],
      ['five dimensions', 'every score has']
    );

    var strength = findSection(
      ['#v13-strengths', '#v12-strengths', '#v11-strengths'],
      ['your strengths', 'natural advantage']
    );

    var lever = findSection(
      ['#v13-lever', '#v12-lever', '#v11-lever'],
      ['your biggest lever', 'highest-leverage opportunity']
    );

    var next = findSection(
      ['#v13-next', '#v12-next', '#v11-next'],
      ['your next move', 'your next chapter']
    );

    var masters = findSection(
      ['#v13-masters', '#v12-masters', '#v11-masters'],
      ['18 naya masters', '18 ai pathways', 'your naya masters']
    );

    var playground = shell.querySelector('#naya-playground');
    var video = shell.querySelector('#v13-video');
    var ending = shell.querySelector('#v13-final, .mx-final');

    [
      hero,
      report,
      dimSection,
      pattern,
      strength,
      lever,
      next,
      masters,
      playground,
      video,
      ending
    ].filter(Boolean).forEach(function (section) {
      shell.appendChild(section);
    });

    /* Required final order:
       Naya → Listen → Score → Five dimensions → Report → Pattern → Strength
       → Lever → Next Move → 18 Masters → Playground/ending.
    */
    if (naya && hero) {
      var heroGrid2 = hero.querySelector('.v13-hero-grid, .mx-hero-grid') || hero;
      heroGrid2.insertBefore(naya, heroGrid2.firstChild);
    }

    /* ---------- FINAL CSS: presentation only; no new renderer ---------- */
    if (!document.getElementById('v171-finish-pass-style')) {
      var style = document.createElement('style');
      style.id = 'v171-finish-pass-style';
      style.textContent = `
#maxess-results-10 .v13-hero,
#maxess-results-10 .mx-hero{
  padding-top:clamp(40px,5vw,72px)!important;
  padding-bottom:clamp(44px,5vw,76px)!important;
}
#maxess-results-10 .v13-hero-grid,
#maxess-results-10 .mx-hero-grid{
  display:flex!important;
  flex-direction:column!important;
  align-items:center!important;
  justify-content:center!important;
  gap:20px!important;
  width:min(1120px,100%)!important;
  text-align:center!important;
}
#maxess-results-10 #v171-naya{
  order:1!important;
  width:min(820px,100%)!important;
  margin:0 auto 2px!important;
}
#maxess-results-10 .mx-score-orb,
#maxess-results-10 .v13-orb-wrap{
  order:2!important;
}
#maxess-results-10 #v171-five-dimensions{
  order:3!important;
  display:grid!important;
  grid-template-columns:repeat(5,minmax(0,1fr))!important;
  gap:12px!important;
  width:min(940px,100%)!important;
  margin:5px auto 0!important;
}
#maxess-results-10 .v171-mini-orb{
  appearance:none!important;
  border:1px solid rgba(255,255,255,.10)!important;
  border-radius:18px!important;
  padding:10px 5px!important;
  background:rgba(255,255,255,.025)!important;
  color:#fff!important;
  cursor:pointer!important;
  transition:transform .2s ease,background .2s ease,border-color .2s ease!important;
}
#maxess-results-10 .v171-mini-orb:hover,
#maxess-results-10 .v171-mini-orb:focus-visible{
  transform:translateY(-3px)!important;
  background:rgba(155,99,255,.09)!important;
  border-color:rgba(196,181,253,.32)!important;
}
#maxess-results-10 .v171-mini-ring{
  display:grid!important;
  place-items:center!important;
  width:68px!important;
  height:68px!important;
  margin:0 auto 8px!important;
  border-radius:50%!important;
  background:conic-gradient(#9b63ff var(--score),rgba(255,255,255,.08) 0)!important;
  position:relative!important;
  box-shadow:0 0 22px rgba(139,92,246,.15)!important;
}
#maxess-results-10 .v171-mini-ring::after{
  content:""!important;
  position:absolute!important;
  inset:6px!important;
  border-radius:50%!important;
  background:#09070d!important;
  box-shadow:inset 0 0 15px rgba(139,92,246,.16)!important;
}
#maxess-results-10 .v171-mini-ring b{
  position:relative!important;
  z-index:1!important;
  font-size:15px!important;
}
#maxess-results-10 .v171-mini-name{
  display:block!important;
  max-width:130px!important;
  margin:auto!important;
  color:rgba(255,255,255,.68)!important;
  font-size:10px!important;
  line-height:1.2!important;
}
#maxess-results-10 #v171-naya .v11-naya-title,
#maxess-results-10 #v171-naya .v13-naya-title,
#maxess-results-10 #v171-naya h2{
  font-size:clamp(20px,2.7vw,30px)!important;
  line-height:1.06!important;
}
#maxess-results-10 #v171-naya .v11-naya-copy,
#maxess-results-10 #v171-naya .v13-naya-copy,
#maxess-results-10 #v171-naya p{
  font-size:14px!important;
  line-height:1.5!important;
}
#maxess-results-10 #v171-naya .v11-naya-avatar,
#maxess-results-10 #v171-naya img{
  border-radius:50%!important;
  object-fit:cover!important;
}
@media(max-width:760px){
  #maxess-results-10 #v171-five-dimensions{
    grid-template-columns:repeat(3,1fr)!important;
  }
}
@media(max-width:480px){
  #maxess-results-10 #v171-five-dimensions{
    grid-template-columns:repeat(2,1fr)!important;
  }
}
@media(prefers-reduced-motion:reduce){
  #maxess-results-10 .v171-mini-orb{
    transition:none!important;
  }
}
`;
      document.head.appendChild(style);
    }

    console.log('%cMAXESS RESULTS V17.1 FINISH PASS ACTIVE', 'color:#c6a3ff;font-weight:900;font-size:16px');
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', function () {
      setTimeout(boot, 180);
    }, { once: true });
  } else {
    setTimeout(boot, 180);
  }
})();
