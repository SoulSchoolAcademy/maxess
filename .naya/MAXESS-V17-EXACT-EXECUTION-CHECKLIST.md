# MAXESS V17 — EXACT EXECUTION CONTRACT

STATUS RULE: THIS CHECKLIST IS THE RELEASE CONTRACT. DO NOT REPORT SUCCESS OR SEND A TEST LINK UNLESS EVERY REQUIRED EXECUTION ITEM IS SATISFIED IN THE ACTUAL WORKING GROOVE FILE.

WORKING ARTIFACT
- Repository: SoulSchoolAcademy/maxess
- Branch: maxess-results-v16-updated-edited
- File: MAXESS-RESULTS-10-GROOVE.html
- Runtime personalization boundary: window.MAXESS_RESULT
- This working artifact, not a script and not the protected foundation, is the thing that must visibly change.

## 01 — PRESERVE THE FOUNDATION
- Preserve the complete Groove foundation.
- Preserve the Result Contract.
- Preserve NayaNET integration.
- Preserve working video, buttons, audio/listen behavior, and existing validated destinations.
- Do not introduce a second scoring engine.
- Do not introduce a runtime GitHub loader.
- Do not replace the page with an iframe/wrapper.
- Do not hard-code production participant, score, band, dimensions, strength, opportunity, recommendation, or pathway personalization.
- Fixture data is development-only.

## 02 — TOP OF PAGE
- Put the compact Naya introduction banner at the absolute top.
- The banner is personal and says the result is a map, not a judgment.
- The banner must not compete with the hero.

## 03 — HERO / ORB
- The first major visual feature is the Orb.
- The hero must communicate exactly: YOUR AI SCORE.
- The runtime score must appear once in the hero Orb.
- Remove competing/duplicate hero score presentations.
- The Orb must remain the approved signature visual.
- Score must come from window.MAXESS_RESULT at runtime.

## 04 — FIVE MINI-ORBS
- Immediately after the hero, present the five dimension scores.
- Each dimension gets its own mini-Orb.
- Mini-Orbs use the hero Orb visual language.
- Mini-Orbs have distinct color identities.
- Values come from window.MAXESS_RESULT.dimensions.
- Desktop: five across.
- Mobile: responsive without horizontal overflow.

## 05 — LISTEN TO NAYA
- Immediately after the five-score snapshot, place Listen to Naya.
- Reuse the existing Naya listening mechanism.
- Do not duplicate or replace the underlying Naya integration.

## 06 — PERSONAL NARRATIVE
The exact sequence is:
- Pattern
- Meaning
- Strength
- Lever
- Action

Each section must earn its existence and must remain in that order.

Pattern: reveal what the five scores mean together.
Meaning: explain the result in human language.
Strength: identify what is already working.
Lever: identify the highest-value improvement opportunity.
Action: turn the insight into a concrete next move.

Do not allow a generic “See Your Pattern” block to float to the top.
Do not duplicate these chapters.

## 07 — VIDEO / YOUR MOVE / FREE TRIAL
- Video comes after Action.
- Your Move is immediately associated with the video and conversion decision.
- Your Move is concise; do not retain unnecessary boxes/text.
- Existing free-trial CTA wiring must be preserved.

## 08 — 18 NAYA MASTERS
- The 18 Masters come BELOW the video and free-trial CTA.
- Introduce them with INCLUDES EVERYTHING.
- Every Master must have an AI PROFILE treatment.
- They are a personalized capability map, not merely a catalogue.

## 09 — PLAYGROUND
- The Playground comes BELOW the 18 Masters.
- Preserve the concept: “Don’t learn AI. Learn what AI can do for you.”

## 10 — ABSOLUTE ENDING
- The Naya + Human philosophy is the final section.
- It must be at the absolute bottom.
- Preserve the principle: “Technology should amplify the human.”
- Nothing follows it.

## 11 — ORDER VALIDATION
The rendered DOM order must resolve to:
NAYA > SCORE > DIMENSIONS > LISTEN > PATTERN > MEANING > STRENGTH > LEVER > ACTION > VIDEO/TRIAL > MASTERS > PLAYGROUND > PHILOSOPHY

The implementation must physically append/reorder the actual sections in the working artifact. CSS order alone is insufficient.

## 12 — EXECUTION GATE
The executor must:
1. Read this checklist.
2. Inspect the actual working Groove file.
3. Apply all changes to the actual working Groove file through the execution path.
4. Validate the actual file, not merely the transformation script.
5. Fail the workflow if any required marker/order condition is absent.
6. Commit the actual Groove file.
7. Re-fetch the committed actual Groove file and verify its contents.
8. Only then provide the test link.

NO CLAIM OF COMPLETE, READY, UPDATED, OR TESTABLE IS PERMITTED IF ANY ITEM ABOVE IS UNVERIFIED.
