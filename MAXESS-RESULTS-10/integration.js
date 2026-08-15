/* =========================================================
   MAXESS RESULTS — ASSESSMENT HANDOFF
   This file is the seam between the questionnaire product and
   the independent Results product. It deliberately contains
   no question rendering and no assessment scoring.
========================================================= */
(function () {
  'use strict';

  const CONTRACT_VERSION = 'MAXESS-RESULTS-CONTRACT-1';
  const REQUIRED_DIMENSIONS = [
    'direction',
    'communication',
    'evaluation',
    'iteration',
    'systemsThinking'
  ];

  const clamp = (value) => {
    const number = Number(value);
    if (!Number.isFinite(number)) return 0;
    return Math.max(0, Math.min(100, Math.round(number)));
  };

  function validObject(value) {
    return value !== null && typeof value === 'object' && !Array.isArray(value);
  }

  function validateDimensions(dimensions) {
    if (!validObject(dimensions)) return false;
    return REQUIRED_DIMENSIONS.every(key => Number.isFinite(Number(dimensions[key])));
  }

  function normalize(payload) {
    if (!validObject(payload)) return null;
    if (!validateDimensions(payload.dimensions)) return null;

    const dimensions = {};
    REQUIRED_DIMENSIONS.forEach(key => {
      dimensions[key] = clamp(payload.dimensions[key]);
    });

    const calculated = Math.round(
      REQUIRED_DIMENSIONS.reduce((sum, key) => sum + dimensions[key], 0) /
      REQUIRED_DIMENSIONS.length
    );

    return {
      version: payload.version || CONTRACT_VERSION,
      overall: clamp(payload.overall ?? calculated),
      level: payload.level || '',
      dimensions,
      strongest: payload.strongest || '',
      opportunity: payload.opportunity || '',
      assessmentVersion: payload.assessmentVersion || 'MAXESS-1.0',
      completedAt: payload.completedAt || new Date().toISOString(),
      userName: typeof payload.userName === 'string' ? payload.userName.slice(0, 120) : ''
    };
  }

  function receive(payload, source) {
    const normalized = normalize(payload);
    if (!normalized) {
      console.warn('[MAXESS Results] Ignored invalid assessment payload from', source);
      return false;
    }

    try {
      sessionStorage.setItem('MAXESS_RESULT', JSON.stringify(normalized));
    } catch (_) {}

    try {
      localStorage.setItem('MAXESS_RESULT', JSON.stringify(normalized));
    } catch (_) {}

    if (window.MAXESS_RESULTS && typeof window.MAXESS_RESULTS.setResult === 'function') {
      window.MAXESS_RESULTS.setResult(normalized);
    }

    window.dispatchEvent(new CustomEvent('maxess:result-received', {
      detail: { result: normalized, source }
    }));

    return true;
  }

  function listenForAssessment() {
    window.addEventListener('maxess:assessment-complete', event => {
      receive(event.detail && event.detail.result, 'custom-event');
    });

    window.addEventListener('message', event => {
      const data = event.data;
      if (!validObject(data)) return;
      if (data.type !== 'MAXESS_ASSESSMENT_COMPLETE') return;
      receive(data.result, 'postMessage');
    });
  }

  function publishReady() {
    window.dispatchEvent(new CustomEvent('maxess:results-contract-ready', {
      detail: {
        version: CONTRACT_VERSION,
        dimensions: REQUIRED_DIMENSIONS.slice()
      }
    }));
  }

  function diagnostics() {
    const result = window.MAXESS_RESULTS && window.MAXESS_RESULTS.getResult
      ? window.MAXESS_RESULTS.getResult()
      : null;

    return {
      contract: CONTRACT_VERSION,
      ready: Boolean(result),
      result: result ? {
        overall: result.overall,
        level: result.level,
        dimensions: { ...result.dimensions }
      } : null,
      url: location.href,
      timestamp: new Date().toISOString()
    };
  }

  window.MAXESS_RESULTS_INTEGRATION = {
    contractVersion: CONTRACT_VERSION,
    receive,
    normalize,
    diagnostics,
    requiredDimensions: REQUIRED_DIMENSIONS.slice()
  };

  listenForAssessment();

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', publishReady, { once: true });
  } else {
    publishReady();
  }
})();
