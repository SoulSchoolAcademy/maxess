(() => {
  'use strict';

  const RESULT_QUERY_KEY = 'result';
  const PREVIEW_QUERY_KEY = 'preview';
  const REQUIRED = ['direction','communication','evaluation','iteration','systemsThinking'];
  const app = document.getElementById('app');

  const clamp = (value) => {
    const n = Number(value);
    return Number.isFinite(n) ? Math.max(0, Math.min(100, Math.round(n))) : null;
  };

  const normalize = (raw) => {
    if (!raw || typeof raw !== 'object' || Array.isArray(raw)) return null;
    const dims = raw.dimensions;
    if (!dims || typeof dims !== 'object') return null;
    const normalized = {};
    for (const key of REQUIRED) {
      const value = clamp(dims[key]);
      if (value === null) return null;
      normalized[key] = value;
    }
    const overall = clamp(raw.overall ?? raw.overallScore ?? raw.score);
    if (overall === null) return null;
    return {
      ...raw,
      overall,
      level: typeof raw.level === 'string' ? raw.level : undefined,
      dimensions: normalized,
      strongest: typeof raw.strongest === 'string' ? raw.strongest : undefined,
      opportunity: typeof raw.opportunity === 'string' ? raw.opportunity : undefined,
      version: typeof raw.version === 'string' ? raw.version : 'MAXESS-RESULTS-CONTRACT-1'
    };
  };

  const decode = (encoded) => {
    try {
      return JSON.parse(decodeURIComponent(encoded));
    } catch (_) {}
    try {
      const bytes = Uint8Array.from(atob(encoded.replace(/-/g,'+').replace(/_/g,'/')), c => c.charCodeAt(0));
      return JSON.parse(new TextDecoder().decode(bytes));
    } catch (_) {}
    return null;
  };

  const setVisibility = (visible) => {
    if (!app) return;
    app.style.visibility = visible ? 'visible' : 'hidden';
  };

  const showGate = (message) => {
    setVisibility(true);
    if (document.getElementById('maxessProductionGate')) return;
    const gate = document.createElement('div');
    gate.id = 'maxessProductionGate';
    gate.setAttribute('role','alert');
    gate.style.cssText = 'position:fixed;inset:0;z-index:9999;display:grid;place-items:center;padding:24px;background:#030305;color:#fff;font-family:Inter,system-ui,sans-serif';
    gate.innerHTML = `<div style="width:min(640px,100%);padding:42px;border:1px solid rgba(216,180,255,.24);border-radius:28px;background:linear-gradient(145deg,rgba(255,255,255,.06),rgba(255,255,255,.015));box-shadow:0 28px 90px rgba(0,0,0,.55);text-align:center"><div style="font-size:10px;font-weight:900;letter-spacing:.2em;color:#d8b4ff;text-transform:uppercase">MAXESS RESULTS</div><h1 style="font-size:clamp(38px,7vw,64px);line-height:.92;letter-spacing:-.06em;margin:16px 0">Your completed assessment<br>result is required.</h1><p style="color:rgba(255,255,255,.72);line-height:1.7;margin:0 auto 22px;max-width:540px">${message}</p><a href="https://maxess.nayanet.xyz/" style="display:inline-flex;align-items:center;justify-content:center;padding:14px 20px;border-radius:14px;background:linear-gradient(135deg,#fff,#d7b2ff);color:#160a24;text-decoration:none;font-weight:950">Return to MAXESS Assessment</a></div>`;
    document.body.appendChild(gate);
  };

  const accept = (payload, source) => {
    const result = normalize(payload);
    if (!result) return false;
    try {
      sessionStorage.setItem('MAXESS_RESULT', JSON.stringify(result));
      localStorage.setItem('MAXESS_RESULT', JSON.stringify(result));
    } catch (_) {}
    if (window.MAXESS_RESULTS?.setResult) window.MAXESS_RESULTS.setResult(result);
    setVisibility(true);
    const gate = document.getElementById('maxessProductionGate');
    if (gate) gate.remove();
    window.dispatchEvent(new CustomEvent('maxess:real-result-accepted',{detail:{result,source}}));
    return true;
  };

  const params = new URLSearchParams(location.search);
  let result = null;
  const encoded = params.get(RESULT_QUERY_KEY);
  if (encoded) result = decode(encoded);

  try {
    if (!result) {
      const saved = sessionStorage.getItem('MAXESS_RESULT') || localStorage.getItem('MAXESS_RESULT');
      if (saved) result = JSON.parse(saved);
    }
  } catch (_) {}

  if (result && accept(result,'url-or-storage')) {
    // Real result accepted.
  } else if (params.get(PREVIEW_QUERY_KEY) === '1') {
    // Explicit development-only preview. Never used implicitly in production.
    setVisibility(true);
  } else {
    // The core app may have already rendered its development fixture. Keep it hidden
    // and replace it with a truthful production gate until a real result arrives.
    setVisibility(false);
    showGate('The Results page is intentionally refusing to invent a score. Complete the MAXESS assessment first, then return here with its result.');
  }

  window.addEventListener('message', (event) => {
    if (!event.data || event.data.type !== 'MAXESS_ASSESSMENT_COMPLETE') return;
    if (accept(event.data.result,'postMessage')) window.scrollTo({top:0,behavior:'smooth'});
  });

  window.addEventListener('maxess:assessment-complete', (event) => {
    if (event.detail?.result) accept(event.detail.result,'custom-event');
  });

  window.MAXESS_RESULTS_PRODUCTION = {
    version: '1.0',
    accept,
    normalize,
    requiredDimensions: REQUIRED.slice()
  };
})();
