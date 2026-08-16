# MAXESS — CURRENT TRUTH

Last updated: 2026-08-15
Status: Active build — authentic Results tower

## North Star

MAXESS must take a person from finishing an assessment to genuinely understanding how they currently work with AI, recognizing their strengths and leverage points, knowing exactly what to do next, and wanting to continue that growth with Naya.

The Results experience should feel like a cinematic revelation, not a static report or dashboard.

## Current architecture

The Results page is one continuous document.

MAXESS Results tower → recognition → AI fingerprint → five dimensions → advantage/leverage → clear growth path → Naya handoff → canonical NayaNET ground floor.

The NayaNET page code in `nayanetpagecode` is the ground floor. It is NOT an iframe, separate page, visual reference, or replacement target. The production build physically inlines that source beneath the MAXESS Results experience.

## Current source of truth

- Results source: `MAXESS-RESULTS-AUTHENTIC-TOWER.html`
- NayaNET ground floor source: `nayanetpagecode`
- Results enhancement design: `knowledge/results-experience-aaa-enhancements.css`
- Results enhancement runtime: `knowledge/results-experience-aaa-enhancements.js`
- Production build script: `scripts/build-authentic-results.js`
- Latest canonical UI output: `current-ui/MAXESS-RESULTS.html`

## Design DNA

The entire page must feel like one premium system. Reuse the NayaNET language for:

- black / deep-purple atmosphere
- jewel-tone gradients
- luminous metallic highlights
- premium rounded geometry
- layered borders and shadows
- circular luminous icons
- premium CTA buttons
- typography hierarchy
- responsive spacing and sizing
- hover/focus behavior
- restrained motion

New elements may be innovative, but they must feel native to the same visual world.

## Results experience requirements

1. Make the emotional reveal special: large typography, breathing room, slow reveal, score animation, and a unique-pattern moment.
2. Make the score understandable, not merely visible.
3. Make the five-dimensional fingerprint visually memorable and data-driven.
4. Explain what the pattern means.
5. Separate strengths from leverage opportunities.
6. Give exactly one clear next move per relevant dimension/archetype rather than overwhelming the user with a long task list.
7. Connect to Naya quickly and prominently after the user understands the result.
8. Carry the user's authoritative assessment context forward so Naya can begin with the profile rather than asking the user to repeat it.
9. Preserve the canonical NayaNET ground floor.
10. Never fabricate a result when authoritative result data is unavailable.

## Data rule

`window.MAXESS_RESULT` (or the supported equivalent result object) is authoritative. The renderer may interpret it, visualize it, and generate guidance from it, but must not invent a user's score or assessment outcome.

## Learning rule

Use the compounding loop:

DO → OBSERVE → SCORE → QUESTION → LEARN → UPDATE → APPLY → VERIFY → TEACH

Every meaningful correction should be examined for a reusable principle and added to the knowledge bank when valuable.

## Quality rule

Do not call a build 9.5, 10, or AAA because a filename says so. The finished experience earns its score through evidence, testing, and honest scorecarding.

## Current known priorities

- Complete the emotional reveal and progressive disclosure.
- Make the next action unmistakable.
- Make the Naya handoff immediate and context-aware.
- Keep one coherent design system across the full page.
- Reduce root-level prototype clutter by establishing the current-ui / knowledge / notes / archive structure.
- Verify the rendered experience before claiming AAA.
