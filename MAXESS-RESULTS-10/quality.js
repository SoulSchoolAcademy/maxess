/* =========================================================
   MAXESS RESULTS — QUALITY / RESILIENCE LAYER
========================================================= */
(function(){
  'use strict';

  const has = (selector) => Boolean(document.querySelector(selector));
  const safe = (fn) => { try { return fn(); } catch (_) { return null; } };

  function announce(message) {
    let region = document.getElementById('maxessLiveRegion');
    if (!region) {
      region = document.createElement('div');
      region.id = 'maxessLiveRegion';
      region.setAttribute('aria-live','polite');
      region.setAttribute('aria-atomic','true');
      region.style.cssText = 'position:fixed;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap';
      document.body.appendChild(region);
    }
    region.textContent = '';
    requestAnimationFrame(() => { region.textContent = message; });
  }

  function setupDimensionAccessibility() {
    const grid = document.getElementById('dimensionGrid');
    if (!grid) return;
    const cards = () => [...grid.querySelectorAll('.dimension-card')];
    grid.addEventListener('keydown', event => {
      const current = event.target.closest('.dimension-card');
      if (!current) return;
      const list = cards();
      const index = list.indexOf(current);
      let next = null;
      if (event.key === 'ArrowRight' || event.key === 'ArrowDown') next = list[(index + 1) % list.length];
      if (event.key === 'ArrowLeft' || event.key === 'ArrowUp') next = list[(index - 1 + list.length) % list.length];
      if (next) { event.preventDefault(); next.focus(); next.click(); }
    });
  }

  function makeCardsFocusable() {
    const observer = new MutationObserver(() => {
      document.querySelectorAll('.dimension-card').forEach(card => {
        if (!card.hasAttribute('tabindex')) card.tabIndex = 0;
        card.setAttribute('role','button');
      });
    });
    observer.observe(document.body,{childList:true,subtree:true});
  }

  function setupScrollProgress() {
    const bar = document.createElement('div');
    bar.className = 'reading-progress';
    bar.setAttribute('aria-hidden','true');
    bar.style.cssText = 'position:fixed;z-index:99;left:0;top:0;width:0;height:2px;background:linear-gradient(90deg,#6331d3,#c5a4ff);box-shadow:0 0 12px rgba(139,92,255,.7);pointer-events:none;transition:width .12s linear';
    document.body.appendChild(bar);
    const update = () => {
      const max = document.documentElement.scrollHeight - window.innerHeight;
      const value = max > 0 ? Math.min(100, Math.max(0, window.scrollY / max * 100)) : 0;
      bar.style.width = `${value}%`;
    };
    window.addEventListener('scroll', update,{passive:true});
    update();
  }

  function setupShare() {
    const target = document.querySelector('.nayanet-card');
    if (!target) return;
    const wrap = document.createElement('div');
    wrap.className = 'results-tools';
    wrap.innerHTML = '<button type="button" data-results-action="share">Share my Results</button><button type="button" data-results-action="print">Save / Print</button>';
    wrap.style.cssText = 'display:flex;gap:8px;flex-wrap:wrap;margin-top:25px';
    target.appendChild(wrap);

    wrap.addEventListener('click', async event => {
      const action = event.target.closest('[data-results-action]')?.dataset.resultsAction;
      if (!action) return;
      if (action === 'print') {
        window.print();
        announce('Print dialog opened.');
        return;
      }
      if (action === 'share') {
        const result = window.MAXESS_RESULTS?.getResult?.();
        const text = result ? `My MAXESS AI Mastery Score is ${result.overall} — ${result.level}.` : 'My MAXESS AI Mastery Results.';
        if (navigator.share) {
          try { await navigator.share({title:'My MAXESS Results',text,url:location.href}); announce('Share dialog opened.'); return; } catch (_) {}
        }
        safe(() => navigator.clipboard.writeText(`${text} ${location.href}`));
        announce('Results link copied to your clipboard.');
      }
    });
  }

  function setupErrorBoundary() {
    window.addEventListener('error', event => {
      console.error('[MAXESS Results] Runtime error',event.error || event.message);
    });
    window.addEventListener('unhandledrejection', event => {
      console.error('[MAXESS Results] Promise rejection',event.reason);
    });
  }

  function setupResultChangeAnnouncement() {
    window.addEventListener('maxess:result-received', event => {
      const score = event.detail?.result?.overall;
      if (Number.isFinite(score)) announce(`MAXESS Results updated. Your score is ${score}.`);
    });
  }

  function validateSurface() {
    const required = [
      '#overallScore',
      '#overallLevel',
      '#radarCanvas',
      '#dimensionGrid',
      '#dimensionDetails',
      '#capabilityTitle',
      '#opportunityTitle',
      '#whyTitle',
      '#pathway',
      '#methodLoop',
      '#nayaMainButton',
      '#nayanetBridge'
    ];
    const missing = required.filter(selector => !has(selector));
    if (missing.length) console.warn('[MAXESS Results] Missing required surface nodes:',missing);
    return missing.length === 0;
  }

  function exposeQualityApi() {
    window.MAXESS_RESULTS_QUALITY = {
      validate: validateSurface,
      announce,
      print: () => window.print(),
      share: async () => {
        const result = window.MAXESS_RESULTS?.getResult?.();
        const text = result ? `My MAXESS AI Mastery Score is ${result.overall} — ${result.level}.` : 'My MAXESS AI Mastery Results.';
        if (navigator.share) return navigator.share({title:'My MAXESS Results',text,url:location.href});
        return safe(() => navigator.clipboard.writeText(`${text} ${location.href}`));
      }
    };
  }

  function init(){
    setupErrorBoundary();
    setupScrollProgress();
    setupDimensionAccessibility();
    makeCardsFocusable();
    setupShare();
    setupResultChangeAnnouncement();
    exposeQualityApi();
    setTimeout(validateSurface,100);
  }

  if(document.readyState==='loading') document.addEventListener('DOMContentLoaded',init,{once:true});
  else init();
})();
