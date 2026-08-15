/*
  MAXESS RESULT HANDOFF ADAPTER
  Include this after the assessment calculates its final result.

  Usage:
    MAXESS_RESULTS_HANDOFF(result);

  The adapter deliberately does not calculate scores. The assessment owns
  truth. It serializes the authoritative result and opens the independent
  Results product with a validated result payload.
*/
(function () {
  'use strict';

  const RESULTS_URL = 'https://results.nayanet.xyz/';
  const REQUIRED = ['direction','communication','evaluation','iteration','systemsThinking'];

  function validResult(result) {
    if (!result || typeof result !== 'object' || !result.dimensions) return false;
    const score = Number(result.overall ?? result.overallScore ?? result.score);
    if (!Number.isFinite(score) || score < 0 || score > 100) return false;
    return REQUIRED.every(key => Number.isFinite(Number(result.dimensions[key])));
  }

  function normalize(result) {
    const dimensions = {};
    REQUIRED.forEach(key => {
      dimensions[key] = Math.max(0, Math.min(100, Math.round(Number(result.dimensions[key]))));
    });
    return {
      version: result.version || 'MAXESS-RESULTS-CONTRACT-1',
      assessmentId: result.assessmentId || 'ai-max',
      assessmentVersion: result.assessmentVersion || '1.0',
      completed: true,
      overall: Math.max(0, Math.min(100, Math.round(Number(result.overall ?? result.overallScore ?? result.score)))),
      level: result.level || '',
      dimensions,
      strongest: result.strongest || '',
      opportunity: result.opportunity || '',
      profile: result.profile || null,
      answers: Array.isArray(result.answers) ? result.answers : [],
      aiAreas: Array.isArray(result.aiAreas) ? result.aiAreas : [],
      recommendations: Array.isArray(result.recommendations) ? result.recommendations : [],
      narrative: result.narrative || result.insight || null,
      completedAt: result.completedAt || new Date().toISOString()
    };
  }

  function encode(value) {
    const json = JSON.stringify(value);
    return encodeURIComponent(json);
  }

  function openResults(result) {
    if (!validResult(result)) {
      throw new Error('MAXESS_RESULTS_HANDOFF requires a completed result with an overall score and all five configured dimensions.');
    }
    const normalized = normalize(result);
    try {
      sessionStorage.setItem('MAXESS_RESULT', JSON.stringify(normalized));
      localStorage.setItem('MAXESS_RESULT', JSON.stringify(normalized));
    } catch (_) {}
    const url = `${RESULTS_URL}?result=${encode(normalized)}`;
    window.location.assign(url);
  }

  window.MAXESS_RESULTS_HANDOFF = openResults;
})();
