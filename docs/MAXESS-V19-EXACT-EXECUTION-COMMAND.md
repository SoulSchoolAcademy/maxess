# MAXESS — V19 EXACT EXECUTION COMMAND

## MANDATORY IMPLEMENTATION + VERIFICATION CONTRACT

This document is an execution order, not a planning request. The executor must modify the actual `MAXESS-RESULTS-10-GROOVE.html` artifact on `maxess-results-v16-updated-edited`, verify the rendered result, and refuse completion if any requirement fails.

## Required rendered order

1. Naya introduction
2. YOUR AI SCORE — Big Orb
3. Five Mini-Orbs: Direction, Communication, Evaluation, Iteration, Systems Thinking
4. Listen to Naya
5. Pattern
6. Meaning
7. Strength
8. Lever
9. Action
10. Video
11. Free Trial / CTA
12. 18 Naya Masters + AI Profiles
13. Learn What AI Can Do For You / Playground
14. Technology Should Amplify The Human

## Mandatory fixes

- Naya introduction must be first.
- Big Orb must be the hero immediately after the Naya introduction.
- Hero must show exactly one visible YOUR AI SCORE label and one runtime score.
- No duplicate zero or duplicate hero score.
- Five genuine Mini-Orbs must be created and populated from `window.MAXESS_RESULT.dimensions`.
- Mini-Orbs must be five across on desktop and responsive on mobile.
- Biggest Lever must be centered, readable, unclipped, and accessible.
- Pattern → Meaning → Strength → Lever → Action must form a clear narrative.
- Technology should amplify the human must be the final substantive report section.
- Every Master must receive an AI PROFILE treatment without hard-coded production personalization.
- All production personalization must originate from `window.MAXESS_RESULT`.
- `?fixture=demo` is development-only and must never become the production fallback.

## Verification gate

The executor must verify the actual artifact and the rendered DOM at 390px and 1440px. Verify section order, score uniqueness, five Mini-Orbs, readability, no horizontal overflow, accessibility, working controls, Naya interaction, and final technology section placement.

If any item fails: BUILD = FAILED. Fix it, retest it, and continue.

Do not report Updated, Implemented, Done, Complete, Ready, Production Ready, or All Requirements Passed unless objectively verified.

## Final rule

The job is not to make the code look changed. The job is to make the MAXESS experience actually change.

EXECUTE → VERIFY → FIX → RETEST → VERIFY AGAIN → HAND OFF.

If even one required item remains incomplete, do not send the file.
