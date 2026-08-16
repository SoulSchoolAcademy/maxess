# MAXESS Results — Master Naya Execution Instruction Set V11

## Execution identity
- Iteration: 11
- Role: **Master Naya** — master of all masters; accountable for strategy, architecture, UX, visual design, engineering, accessibility, QA, preservation, and verification.
- Standard: Naya Law.
- North Star: **ME → MY SCORE → NAYA → MY REPORT → MY INSIGHTS → MY OPPORTUNITY → MY NEXT MOVE → NAYA MASTERS → MY PLAYGROUND → MY SOLUTION → ACTION.**
- Release principle: **The live user-facing outcome is the product. Code changes are evidence, not completion.**

## Why this iteration exists
Previous iterations accumulated additive patches, competing layout rules, duplicate V6 profile blocks, and multiple visual overrides. The repository contains a functioning Result Contract but the experience has drifted into a report/dashboard rather than a personal, emotionally compelling Results journey. V11 therefore uses the existing authoritative result architecture but gives the presentation layer one coherent experience owner.

## Absolute preservation
Never replace or recalculate the assessment engine. Preserve `window.MAXESS_RESULT`, real result handoff, five dimensions, 18 AI pathways, existing video/NayaNET continuation, CTA destinations, Groove compatibility, responsive behavior, accessibility, and print support. Development fixture data is permitted only when `?fixture=demo` is explicitly present. No fabricated production score may appear.

## Hero — MY SCORE
Purpose: create the first emotional reaction: **“This is my result.”**
- Headline: **YOUR AI SCORE**.
- Huge score and living Orb; the Orb is the dominant visual.
- No radar chart beside the Orb in the first viewport.
- No sales copy, generic mini-cards, or “Your AI capability has shape.”
- Score band may be a restrained secondary signal, never the focal point.
- Add Print / Save PDF in the hero action area.
- Orb color continuously interpolates by score: 0–49 red/orange; 50–64 orange/yellow; 65–74 yellow/green; 75–84 green/teal; 85–89 teal/blue; 90–94 blue/purple; 95–100 purple/magenta.
- Orb must be sharp, luminous, dimensional, performant, reduced-motion safe, and data-driven.

## Naya — MY GUIDE
Purpose: convert the product from a dashboard into a personal report experience.
- Introduce Naya immediately after the score reveal.
- Use the supplied Naya profile asset as a circular portrait; use dark/light treatment according to background.
- Voice and face must feel like one character.
- Copy must be short, warm, direct, and personal.
- Primary action: **Listen to your results**.
- Naya interprets; the Orb represents the user's AI signature; the report provides evidence.

## Report architecture
Every section must answer: What does this mean? Why does it matter? What should I do next?

### 03 — YOUR FIVE DIMENSIONS
Purpose: reveal the capability profile at a glance.
- Use five premium circular gauges/instruments.
- Score is visually dominant.
- Each dimension has distinct color identity and a concise plain-language interpretation.
- Do not use generic square card walls.
- Visuals communicate before text.

### YOUR PATTERN
Purpose: explain relationships between dimensions, not repeat the word “pattern” everywhere.
- One meaningful visual relationship between the five dimensions.
- Use “See the pattern” intentionally.
- Highlight relationships and the user's strongest signal and largest opportunity.

### YOUR STRENGTHS
Purpose: create earned pride.
- Lead with the user's actual strongest dimensions.
- Use visual symbols and benefit language.
- Never invent psychological claims unsupported by the result contract.

### YOUR BIGGEST LEVER
Purpose: frame the lowest/highest-opportunity dimension as upside, never shame.
- Identify dynamically from actual data.
- Show a visual before/after or current → potential relationship where it can be truthful.
- Avoid “weakness” framing.

### WHAT IT MEANS
Purpose: turn measurement into understanding.
- Keep copy concise.
- Naya's interpretation is the human layer.

### YOUR NEXT MOVE
Purpose: leave the user knowing exactly what to do next.
- Concrete, personalized action tied to the result.
- No generic motivational filler.

### 18 NAYA MASTERS
Purpose: introduce the ecosystem only after self-understanding has been earned.
- Show the six most relevant pathways first, derived deterministically from the result where possible.
- Progressive disclosure for all 18.
- Each pathway: icon/visual, name, one-line benefit, action.
- Never invent pathway names outside the authoritative registry.

### MY PLAYGROUND
Purpose: turn curiosity into useful action.
- Feature a small number of strong doors such as Naya Writer, Naya Brainstormer, and Talk to Naya.
- Benefit before feature.
- Strong, tactile CTAs.

### MY SOLUTION / NAYANET CONTINUATION
Purpose: conversion earned by value.
- Commercial material comes late.
- Preserve the existing video and NayaNET Page Code/continuation.
- Never let conversion interrupt the personal report too early.

## Visual system
- Desktop is full widescreen/full viewport. Never create a narrow phone-like central page.
- Use black for authority, white for clarity/breathing room, purple for energy, and the broader score/dimension spectrum for meaning.
- Avoid endless purple and avoid low-contrast decorative text.
- Use editorial spacing: generous at chapter boundaries, tighter inside information groups.
- Every visual has a job. If it does not improve comprehension, emotion, navigation, or action, remove it.
- Prefer circles, gauges, constellations, portraits, energy paths, and strong imagery over repetitive rectangles.

## Naya asset rules
Authoritative supplied assets include the repository Naya photos and the four user-provided image sources. Prefer the dedicated profile images for recurring Naya portrait UI. Use Shawn + Naya imagery only when it strengthens the Human + AI story. Do not use every supplied image merely because it exists. Sharpness, crop quality, contrast, and contextual fit are mandatory.

## Technical rules
- One authoritative result source: `window.MAXESS_RESULT`.
- Renderer reads the Result Contract; it does not create a second scoring engine.
- No DOM scraping as the primary score source.
- No production fixture fallback.
- No fake result values.
- No external library dependency for core rendering.
- CSS/SVG/vanilla JS preferred.
- `prefers-reduced-motion` required.
- Keyboard focus and semantic labels required.
- Print stylesheet must produce a readable black-on-white premium report.
- Do not allow duplicate execution to create duplicate visible components.
- The external Results experience renderer is the presentation-layer authority; legacy inline rules must not be allowed to create competing visible copies.

## Execution protocol
READ → MAP → BASELINE → SOURCE-LOCK → PLAN → MODIFY → REASSEMBLE → BUILD → REFETCH → DIFF → TEST → OSCAR → FIX → RETEST → LIVE-CHECK → VERIFY → DELIVER.

### Baseline
Before modification record:
- authoritative artifact SHA
- external renderer SHA
- relevant governance/instruction files
- current visible section inventory
- protected behavior inventory
- public target: `https://results.nayanet.xyz/`

### Zero-change gate
If an execution claims a material change but the authoritative source does not change, block the execution.

### Distinctive proof
For every material request record:
1. requested outcome
2. implementation mechanism
3. exact evidence in final artifact
4. runtime/public verification

### Live parity
GitHub changed ≠ product changed. The execution is not VERIFIED until the real public target reflects the authoritative implementation.

## Oscar challenge
Oscar must attack:
- wrong section order
- duplicated content
- fake/fallback data leakage
- weak visual hierarchy
- excessive text
- poor scanability
- competing focal points
- sales too early
- missing personalization
- broken buttons
- mobile overflow
- accessibility failures
- unreadable PDF
- performance regressions
- regression of protected functionality

If Oscar finds a major issue, fix and retest. Do not rationalize it.

## 100/100 scorecard
- Emotional impact / awe: 20
- Personal report clarity: 15
- Naya presence/personality: 15
- Orb/signature: 15
- Information hierarchy: 10
- Visual communication: 10
- Flow/UX: 5
- PDF/print: 5
- Technical reliability: 5

Release target: 95+ overall; no critical category below 90; zero critical regressions; live parity verified.

## Iteration learning record
At the end of every execution append:
- Iteration number
- What improved
- What remained weak
- What failed
- Root cause
- Corrective rule
- Evidence
- New permanent rule, if any

The next iteration must read the previous record before acting. Known mistakes become constraints, not recurring experiments.

## Definition of done
DONE means the user can open the real Results experience and immediately understand: **this is my score, Naya is here, this is what my result means, this is where I am strongest, this is my biggest opportunity, this is my next move, and these are the tools/pathways that can help me.**

If that cannot be proven on the live user-facing experience: **NOT DONE.**
