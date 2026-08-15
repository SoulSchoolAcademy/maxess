/**
 * MAX ASSESSMENT FAMILY
 *
 * Canonical product-family definition for the reusable MAX assessment engine.
 * The flagship implementation is AI MAX. MAX LIFE and MAX PERCEPTION use
 * the same engine/result contract with assessment-specific configuration.
 *
 * Product language:
 *   AI MAX         = How effectively am I working with AI?
 *   MAX LIFE       = How effectively am I operating my life?
 *   MAX PERCEPTION = How deeply and accurately am I perceiving life?
 *
 * Brand reading:
 *   MAX + AI         -> AI MAX
 *   MAX + LIFE       -> MAX LIFE
 *   MAX + PERCEPTION -> MAX PERCEPTION
 *   Together: AI • LIFE • PERCEPTION under the MAX umbrella.
 */

(function(root){
  'use strict';

  const FAMILY = Object.freeze({
    version: '1.0.0',
    umbrella: 'MAX',
    sequence: Object.freeze(['AI MAX', 'MAX LIFE', 'MAX PERCEPTION']),
    sharedEngine: 'MAX Assessment Engine',
    resultContract: 'MAX Assessment Result v1',

    assessments: Object.freeze({
      ai: Object.freeze({
        id: 'ai-max',
        slug: 'ai-max',
        name: 'AI MAX',
        displayName: 'AI MAX Score',
        shortName: 'AI MAX',
        category: 'AI',
        questionCount: 15,
        purpose: 'Measure how effectively a person directs, communicates with, evaluates, iterates and systematizes AI.',
        productRole: 'Most immediately useful: turns AI frustration into a measurable capability profile and a practical next step.',
        resultsPath: 'https://results.nayanet.xyz/'
      }),

      life: Object.freeze({
        id: 'max-life',
        slug: 'max-life',
        name: 'MAX LIFE',
        displayName: 'MAX Life Score',
        shortName: 'MAX LIFE',
        category: 'LIFE',
        questionCount: 15,
        purpose: 'Measure how effectively a person is operating their life, including direction, choices, habits, relationships, growth and agency.',
        productRole: 'Most revealing of oneself: helps a person see the patterns shaping the life they are actually living.',
        resultsPath: 'https://results.nayanet.xyz/'
      }),

      perception: Object.freeze({
        id: 'max-perception',
        slug: 'max-perception',
        name: 'MAX PERCEPTION',
        displayName: 'MAX Perception Score',
        shortName: 'MAX PERCEPTION',
        category: 'PERCEPTION',
        questionCount: 15,
        purpose: 'Measure how deeply and accurately a person perceives, interprets, questions and expands their understanding of life.',
        productRole: 'Most mind-opening: the questions themselves are designed to reveal assumptions, filters and the willingness to reconsider perception.',
        resultsPath: 'https://results.nayanet.xyz/'
      })
    })
  });

  // Explicit export for browsers, test runners and the reusable assessment engine.
  root.MAX_ASSESSMENT_FAMILY = FAMILY;
})(typeof window !== 'undefined' ? window : globalThis);
