# MAXESS RESULTS V17 — EXECUTION DIRECTIVE

Status: LOCKED DESIGN / READY FOR IMPLEMENTATION
Branch: `maxess-results-v16-updated-edited`
Authoritative foundation: `MAXESS-RESULTS-10-GROOVE.html`
Runtime authority: `window.MAXESS_RESULT`
Public target: `results.nayanet.xyz`

## Mission

Transform the MAXESS results page from a collection of result sections into a remarkable personal AI mastery experience:

DATA → INSIGHT → UNDERSTANDING → ACTION → CAPABILITY

The page must feel like a personal report and guided experience, not a decorated dashboard.

## LOCKED EXPERIENCE ORDER

1. Naya orientation banner — pinned at the very top.
2. YOUR AI SCORE — the hero and visual crown jewel.
3. Five AI capability mini-Orbs — one for each dimension.
4. LISTEN TO NAYA — the primary interpretation action.
5. YOUR PATTERN.
6. HERE'S WHAT IT MEANS.
7. YOUR STRENGTH.
8. YOUR LEVER.
9. YOUR ACTION.
10. Video / YOUR MOVE / free-trial conversion area.
11. INCLUDES EVERYTHING — followed by all 18 Naya Master profiles.
12. DON'T LEARN AI. LEARN WHAT AI CAN DO FOR YOU. — Playground.
13. Naya + human / technology philosophy at the absolute bottom.

This order is authoritative for the V17 experience unless explicitly superseded by a later approved directive.

## 1. NAYA ORIENTATION BANNER

Purpose: orient the human before the score is revealed.

Concept:

“Hi. Look at your results. This isn't a judgment. It's a map.”

Requirements:
- Small, elegant, highly legible banner.
- Pinned above the Orb hero.
- Naya imagery may be used here.
- Fix any contrast/readability problems, especially white text disappearing into the background.
- Do not allow this banner to compete with the Orb.

## 2. HERO — YOUR AI SCORE

The Orb is the primary visual feature of the page.

Requirements:
- `YOUR AI SCORE` appears exactly once in the hero.
- The authoritative runtime score appears exactly once in the hero.
- Score must be sourced from `window.MAXESS_RESULT`.
- No hard-coded production score.
- No duplicate zero/score presentation.
- Preserve and refine the existing successful orbiting-ball / Orb motion.
- The score must be large, centered, immediately readable, and visually integrated into the Orb.
- The Orb must be responsive and accessible.
- Reduced-motion support must remain.

The Orb should feel like the MAXESS signature, not a generic dashboard visualization.

## 3. FIVE AI CAPABILITY MINI-ORBS

Create five smaller versions of the same Orb visual language used by the hero.

Each mini-Orb represents one result dimension and displays its live score.

Current demo dimensions:
- Direction — 86
- Communication — 91
- Evaluation — 79
- Iteration — 74
- Systems Thinking — 68

These values are development fixture examples only. Production values MUST come from `window.MAXESS_RESULT`.

Requirements:
- Five mini-Orbs on desktop, arranged as a clean single row when space permits.
- Each mini-Orb has its own score.
- Each mini-Orb has a distinct visual/color identity while remaining part of one MAXESS system.
- Use the same underlying visual concept as the hero Orb; do not create five unrelated chart styles.
- Responsive mobile layout must preserve clarity and hierarchy.
- Mini-Orbs must not become visually louder than the hero.
- Labels must remain readable and accessible.

## 4. LISTEN TO NAYA

Replace weaker “See Your Results” framing with:

LISTEN TO NAYA

This is the natural transition from:

SCORE → SNAPSHOT → INTERPRETATION

Preserve the working Naya listen functionality. Do not rebuild it unnecessarily.

## 5–9. PERSONAL INTERPRETATION NARRATIVE

The middle of the report must progressively answer the human's next natural question.

YOUR PATTERN
→ reveal something meaningful in the relationship between the user's dimensions.

HERE'S WHAT IT MEANS
→ translate data into plain-language understanding.

YOUR STRENGTH
→ identify what the user can already leverage.

YOUR LEVER
→ identify the highest-value opportunity without shaming the user.

YOUR ACTION
→ provide a clear, practical next step.

Every section must earn its existence. Remove or merge redundant material rather than decorating it.

The middle must feel personalized, insightful, and human.

## 10. VIDEO / YOUR MOVE / FREE TRIAL

“YOUR MOVE” is intentionally minimal.

Remove unnecessary boxes and explanatory clutter.

The conversion area should visually connect:

YOUR MOVE
→ WATCH THE VIDEO
→ START YOUR FREE TRIAL

Do not let additional copy dilute the decision point.

## 11. INCLUDES EVERYTHING / 18 NAYA MASTERS

The 18 Naya Masters belong BELOW the video and free-trial conversion area.

They are not part of the initial results reveal.

“INCLUDES EVERYTHING” introduces the depth of the product, followed by all 18 Naya Master profiles.

Each Master should eventually have an AI profile rather than being merely a catalogue tile.

A Master profile should be capable of communicating:
- Master name
- AI capability/profile
- What this Master helps the human do
- User's relationship/status with the Master
- Why it matters to this user
- Appropriate practice/development direction

Do not overwhelm the primary report narrative with all 18 Masters before the conversion point.

## 12. PLAYGROUND

The Playground follows the 18 Masters.

Core message:

DON'T LEARN AI.
LEARN WHAT AI CAN DO FOR YOU.

Purpose: move from understanding the report into experiencing AI capability.

## 13. FINAL PHILOSOPHY

The Naya + technology ending remains at the absolute bottom.

Preserve the approved ending concept:

“Technology should amplify the human.”

Do not turn the ending into another sales block.

It is the final philosophical thought of the experience.

## PERSONALIZATION LAW

All production personalization MUST derive from:

`window.MAXESS_RESULT`

Never hard-code:
- score
- participant
- band
- dimensions
- strengths
- opportunities
- recommendations
- pathways
- Master personalization

`?fixture=demo` is development-only and must never become the production fallback.

## PRESERVATION LAW

Preserve:
- complete Groove foundation
- Result Contract
- NayaNET integration
- working result architecture
- working Naya functionality
- approved ending
- existing working functionality

Do not replace working architecture merely to make the redesign easier.

## EDITORIAL RULE

Before adding anything, inspect the existing 28-section report and classify each section:

KEEP — already earns its place.
MOVE — valuable but incorrectly positioned.
REWRITE — valuable idea with weak communication.
MERGE — duplicates another experience.
REMOVE — does not earn its space.

V17 must not become “V16 plus more sections.”

The goal is a clearer, stronger, more human experience using the best existing material.

## VISUAL SYSTEM RULE

The Orb is the core MAXESS visual language.

Hierarchy:

BIG ORB = overall AI score
MINI-ORBS = five measured AI capabilities
MASTER PROFILES = deeper capability map

Do not turn every element into an Orb. Use the visual language where it communicates score/capability and preserve hierarchy.

## QA GATES

Before claiming completion:

1. Static verification.
2. Browser verification at 390px.
3. Browser verification at 1440px.
4. Visual inspection.
5. No horizontal overflow.
6. Score is runtime-bound.
7. No duplicate score / duplicate YOUR AI SCORE.
8. Hero Orb is visually dominant.
9. Five mini-Orbs render correctly and responsively.
10. Accessibility labels and contrast verified.
11. Reduced-motion behavior verified.
12. Complete section order verified.
13. Naya functionality verified.
14. Performance sanity check.
15. Oscar review.
16. WHY IS THIS NOT A 10?
17. Fix actual failures and retest.
18. Independently verify public parity.

Do not claim LIVE, PRODUCTION VERIFIED, AUTHORITATIVE, or HUMAN APPROVED unless those gates have actually passed.

## RELEASE BOUNDARY

GitHub source, deployment, and public experience are separate states.

Human approval remains required for promotion to authoritative/live status.

## NORTH STAR

The person should leave thinking:

“This isn't just a score. It actually helped me understand how I work with AI, what I'm capable of, where I can improve, and what I should do next.”

AAA is not a label.
AAA is what survives inspection.