# MAXESS RESULTS — MASTER INSTRUCTION SET

Status: AUTHORITATIVE PRODUCT / DESIGN / EXECUTION SPECIFICATION
Version: 1.0
Date: 2026-08-16
Scope: The complete MAXESS Results experience, including its visual design, information architecture, UX, Naya presence, data integrity, responsive behavior, print/PDF experience, performance, accessibility, and implementation/verification process.

This document is the execution blueprint for the MAXESS Results experience. It converts the MAXESS Results North Star into explicit product logic, psychology, visual language, section architecture, component behavior, acceptance criteria, and QA requirements.

It is not a suggestion list.
It is not a mood board.
It is not a collection of optional ideas.
It is the specification against which the Results experience is to be built and judged.

---

# 1. NORTH STAR

MAXESS Results is a PERSONAL AI MASTERY REPORT.

The user has just completed an assessment. The Results experience must make the person feel that the system has listened to them, measured them, understood them, interpreted the result, and given them a clear path forward.

The desired reaction is:

> “Holy shit. This is actually my AI Mastery Report.”

Not:

> “Here is another webpage with my score.”

The page must therefore behave like a report and an experience, not like a generic SaaS dashboard or sales page.

The emotional journey is:

ME
→ MY SCORE
→ MY REPORT
→ MY FIVE DIMENSIONS
→ MY PATTERN
→ WHAT IT MEANS
→ MY STRENGTHS
→ MY BIGGEST LEVER
→ MY NEXT MOVE
→ NAYA MASTERS
→ THE SYSTEM
→ MY NEXT CHAPTER

The page must answer, in order:

1. Where am I?
2. What does that mean?
3. What am I made of?
4. How do my strengths relate?
5. What does Naya see?
6. What am I already good at?
7. Where could improvement create the greatest return?
8. What should I do next?
9. What specialists can help me?
10. Where can I go from here?

The user receives value before being asked to buy, join, or continue.

---

# 2. PRODUCT PSYCHOLOGY

The Results experience should move through five psychological states:

## REVEAL

The score creates curiosity, emotion, and recognition.

## UNDERSTAND

Naya helps the user interpret the result.

## RECOGNIZE

The user sees strengths and capability instead of being framed as deficient.

## FOCUS

The user discovers a high-leverage improvement opportunity.

## ACT

The user leaves knowing what to do next and why the larger MAXESS/Naya system can help.

Do not reverse this order.

Do not introduce heavy commercial material before the user has received meaningful interpretation.

Do not overwhelm the user with all 18 pathways before they understand why they matter.

Do not make the report feel like a funnel wearing report clothing.

---

# 3. THE CENTRAL EXPERIENCE MODEL

MAXESS measures.

The Orb reveals.

Naya interprets.

The report explains.

The dimensions provide evidence.

The pattern provides connection.

The lever provides focus.

The next move provides action.

The 18 Naya Masters provide capability.

The final system provides continuation.

Each element has a distinct job. Do not make two elements compete for the same job.

---

# 4. GLOBAL DESIGN PRINCIPLE

Use this hierarchy everywhere:

# VISUAL → NAYA → TEXT

The visual communicates the primary idea.

Naya provides human interpretation and personality.

Text provides supporting detail.

Do not design a text-heavy page and decorate it afterward.

If a concept can be understood visually, prefer the visual.

If a paragraph can become a number, diagram, gauge, icon, relationship, image, or spatial composition, investigate that option first.

If a sentence does not clarify, deepen, personalize, orient, or move the user forward, remove it.

---

# 5. THE RUTHLESS EDITORIAL RULE

Every element must pass these questions:

1. Why does this exist?
2. Why is it here?
3. Why is it here now?
4. What should the user understand?
5. What should the user feel?
6. Could the visual communicate this better?
7. Is this the strongest possible presentation?
8. Is it duplicating another element?
9. Does it advance the report story?
10. Would the page become stronger if it were removed?

If an element cannot justify its existence, remove or redesign it.

Extraordinary does not mean adding more.

Extraordinary means every surviving element is intentional.

---

# 6. PRESERVATION RULE

This is an upgrade of the existing MAXESS Results product, not permission to throw away working functionality.

Before modification, inventory and preserve:

- complete Results functionality;
- real MAXESS result handoff;
- `window.MAXESS_RESULT` data boundary;
- existing video;
- NayaNET branding;
- Naya identity;
- existing useful icons;
- existing CTA behavior;
- working assessment flow;
- responsive behavior;
- accessibility behavior;
- print/PDF behavior that already works;
- Groove/embed compatibility;
- existing valuable content;
- any integration required by the public Results experience.

Never replace a complete working artifact with a smaller prototype or loader because it is easier to edit.

Never delete working functionality to make the implementation easier for the AI.

---

# 7. SOURCE / IMPLEMENTATION LOCK

The authoritative readable Results artifact is:

`MAXESS-RESULTS-10-GROOVE.html`

Consequential Results upgrades must be made in that artifact or through a verified generation path that demonstrably produces the same complete working artifact.

Do not treat filenames such as FINAL, MASTER, 10/10, FULL BUILD, PREVIEW, or EXECUTABLE as authoritative merely because of their names.

Before every major implementation, establish:

- repository;
- branch;
- authoritative source;
- generated artifact, if any;
- deployment source;
- public verification target;
- current baseline SHA or equivalent fingerprint;
- known protected functionality.

If source authority is ambiguous, stop and resolve it.

---

# 8. COMPLETE PAGE INVENTORY REQUIREMENT

Before changing section order or styling, create an inventory of the actual current page.

Inventory at minimum:

- document structure;
- section IDs/classes;
- headings;
- body copy;
- images;
- image sources;
- Naya assets;
- logos;
- icons;
- score components;
- Orb;
- dimension components;
- pattern visualization;
- interpretation blocks;
- strength blocks;
- lever block;
- next-move block;
- 18 Naya Masters;
- video;
- CTAs;
- buttons;
- popups;
- audio behavior;
- animations;
- data parsing;
- result fallback behavior;
- print styles;
- mobile rules;
- accessibility rules;
- external dependencies;
- scripts;
- embeds;
- deployment assumptions.

Classify each current block:

KEEP / IMPROVE / MOVE / MERGE / REWRITE / REPLACE / REMOVE.

Do this before substantial redesign.

---

# 9. PAGE ARCHITECTURE

The preferred final order is:

## 01 — YOUR AI SCORE

The reveal.

## NAYA ARRIVAL

Naya becomes the guide.

## 02 — YOUR REPORT

Listen to your results.

## 03 — YOUR FIVE DIMENSIONS

See the capability profile.

## 04 — SEE THE PATTERN

Understand relationships between dimensions.

## 05 — WHAT IT MEANS

Naya interprets the profile.

## 06 — YOUR STRENGTHS

Recognize existing capability.

## 07 — YOUR BIGGEST LEVER

Identify the highest-return improvement opportunity.

## 08 — YOUR NEXT MOVE

Provide one clear next action.

## 09 — 18 NAYA MASTERS

Introduce specialists only after the user understands the need.

## 10 — HUMAN + AI / THE SYSTEM

Use Shawn + Naya imagery and philosophy to bridge from personal report to larger system.

## 11 — THE SOLUTION / VIDEO

Introduce the continuation path and commercial layer.

## FINAL — YOUR NEXT CHAPTER

One ending. One invitation. One clear CTA hierarchy.

Existing content may be retained, moved, merged, rewritten, or removed according to this story architecture.

---

# 10. SECTION 01 — YOUR AI SCORE

## Purpose

Create the emotional reveal.

## Required hierarchy

Small contextual label:

MAXESS AI MASTERY ASSESSMENT

Primary title:

# YOUR AI SCORE

Primary data:

# [ACTUAL SCORE]

Visual centerpiece:

# THE ORB

Primary action:

SEE YOUR RESULTS

## Prohibited hero clutter

Do not put unrelated cards beside the Orb.

Do not place “Your AI Capability Has Shape” as the primary hero message.

Do not use “Meaningful AI Foundation” as prime hero copy.

Do not use “Your AI Leverage” in the hero.

Do not place sales copy beside the Orb.

Do not make the hero explain the entire report.

The hero should reveal, not explain.

## Composition

The score and Orb are the dominant visual relationship.

The Orb must have enough space around it to feel magical rather than crowded.

The viewport is the canvas. Preserve full-width widescreen architecture while keeping internal reading widths sensible.

---

# 11. THE ORB — MAXESS SIGNATURE

The Orb is one of the primary identity assets of MAXESS.

It must:

- be centered in the hero;
- be substantially larger than supporting UI;
- have dimensional depth;
- use layered energy;
- support subtle particles or resonance paths where performance allows;
- respond to score;
- respond subtly to Naya speech;
- respond to interaction where useful;
- remain performant;
- respect reduced-motion settings.

## Score spectrum

0–49: red → orange

50–64: orange → yellow

65–74: yellow → green

75–84: green → teal

85–89: teal → blue

90–94: blue → purple

95–100: purple → magenta

Interpolate smoothly. Do not hard-switch colors at score boundaries.

The score should affect the visual energy as well as color where appropriate.

Higher scores should feel more luminous and energized without becoming gaudy.

90+ must feel like a clear achievement.

95–100 must feel extraordinary.

---

# 12. NAYA ARRIVAL

Naya appears after the initial score reveal so that she does not compete with the first emotional moment.

The user should experience:

MY SCORE → ORB → NAYA

This creates a reveal followed by companionship.

Naya can say a short line such as:

> “I've looked at your results. Let's see what they're telling us.”

Copy may change based on the actual result and approved product voice, but it must remain short, warm, human, and interpretive.

---

# 13. NAYA PRESENCE SYSTEM

Naya is not decorative photography.

Naya is the guide character of the experience.

Her presence should feel coherent because the user has already heard her voice during the assessment.

Use a reusable component system:

### Naya Profile

Circular or softly masked portrait.

### Naya Speech

Short contextual interpretation.

### Naya Guidance

Instructional popup / next-step moment.

### Naya Transition

Chapter introduction.

### Naya Master

Specialist introduction.

### Naya Audio State

Visual indication when her voice is actively speaking.

The portrait should subtly respond when speech is active through restrained glow, ring, pulse, or resonance. Avoid mechanical looping animation.

---

# 14. NAYA ASSESSMENT PRESENCE

The assessment should use Naya strategically before Results.

Do not place a giant portrait on every question.

Use Naya at:

- introduction;
- important transitions;
- selected contextual moments;
- completion;
- handoff to Results.

The purpose is continuity.

The user should finish the assessment thinking:

> “I was listening to Naya.”

Then arrive at Results and see the same Naya.

Voice + face + timing + context creates the character experience.

---

# 15. NAYA IMAGE SYSTEM

Available Naya portrait treatments should support both light and dark environments.

### Naya on white

Use for light report chapters, clarity, explanation, strengths, and next-move moments.

### Naya on black

Use for dark cinematic chapters, interpretation, pattern, transformation, and system moments.

Portraits may be:

- circular;
- softly masked;
- cut out;
- surrounded by a subtle energy ring;
- placed beside a short speech block;
- used as a larger emotional chapter image.

Do not use the same treatment repetitively just because it is available.

Every image must have a narrative job.

---

# 16. SECTION 02 — YOUR REPORT

Purpose: transition from reveal into interpretation.

Preferred structure:

# YOUR REPORT

## LISTEN TO YOUR RESULTS

Supporting copy should establish that Naya is turning the assessment into a practical interpretation.

The section should feel like the beginning of a personal report, not a marketing card.

Use strong typography and generous whitespace.

Naya should be present here or immediately adjacent to the interpretation.

---

# 17. SECTION 03 — YOUR FIVE DIMENSIONS

Purpose: reveal the composition of the score.

Primary visual:

Five premium circular gauges.

Each gauge contains:

- large score;
- dimension name;
- circular progress;
- distinct color identity;
- subtle glow;
- restrained energy movement;
- short plain-language descriptor.

The score must be visually dominant.

Do not bury the score in small text.

Do not use weak square cards when a circular visualization communicates the concept better.

The five gauges must feel like one system, not five unrelated widgets.

---

# 18. DIMENSION COLOR LANGUAGE

Use the MAXESS spectrum intentionally.

Possible dimension colors may draw from:

red / orange / yellow / green / teal / blue / indigo / purple / magenta.

Do not make every dimension purple.

Color is information and energy, not decoration.

Each dimension should be distinguishable without relying on color alone.

---

# 19. SECTION 04 — SEE THE PATTERN

“Pattern” earns its place here because the user can now see five dimensions and is ready to understand their relationships.

The section must provide an actual visual relationship:

- connecting paths;
- subtle energy lines;
- central Orb relationship;
- selected-dimension highlighting;
- related-path illumination;
- restrained interaction.

When a dimension is selected:

- it becomes visually dominant;
- related relationships illuminate;
- other elements gently recede;
- Naya can provide a short contextual insight.

Do not overwhelm the user with a technical diagram.

The visual must remain immediately understandable.

---

# 20. SECTION 05 — WHAT IT MEANS

Purpose: translate measurement into human meaning.

Heading:

# WHAT IT MEANS

The user should understand that the score is a starting point, not a verdict.

Naya should interpret the most important result patterns.

Use short insights, visual emphasis, and progressive disclosure rather than walls of prose.

Do not use repeated “pattern” language in every heading.

“Pattern” is reserved primarily for the dedicated pattern chapter.

---

# 21. SECTION 06 — YOUR STRENGTHS

Purpose: create recognition and confidence.

The experience must not imply that the user's score is a judgment of worth.

Highlight strong dimensions dynamically.

Use:

- large scores;
- clear names;
- concise insights;
- visual celebration;
- Naya interpretation where useful.

Desired feeling:

> “I already have something valuable here.”

---

# 22. SECTION 07 — YOUR BIGGEST LEVER

Purpose: identify the one area where focused improvement can create disproportionate upside.

This is where “leverage” belongs, not in the hero.

The result must be dynamic and derived from the actual assessment.

Never use generic filler.

Naya can frame it as a recommendation rather than a deficiency:

> “If I were helping you improve one thing first, I'd start here.”

The section must be visually important without becoming a generic card.

---

# 23. SECTION 08 — YOUR NEXT MOVE

Purpose: convert understanding into one clear action.

The user should leave this section knowing:

> “Here's what I should do next.”

Do not give ten competing actions.

Do not introduce a giant product catalog here.

Use Naya to make the recommendation feel personal.

---

# 24. SECTION 09 — 18 NAYA MASTERS

Only introduce the specialist pathway after the user understands themselves.

Position the 18 Masters as capability extensions, not generic software features.

Each Master should have:

- name;
- distinct icon;
- visual identity;
- color treatment;
- short benefit;
- clear capability.

Naya is the host/guide.

The 18 Masters are specialists.

Do not make all 18 visually identical beyond their shared system language.

Do not make them feel like an app store.

They should feel like a coherent collection of specialist intelligences.

---

# 25. SECTION 10 — HUMAN + AI

The Shawn + Naya imagery belongs here or in an equivalent later system/mission transition.

It should not interrupt the user's personal report near the beginning.

Its job is philosophical:

# HUMAN + AI

The message should reinforce that AI is intended to amplify human capability rather than erase human identity.

The image should therefore have meaning, not simply fill space.

---

# 26. SECTION 11 — THE SOLUTION / VIDEO

The existing strong video is protected.

Do not remove it.

Do not replace it with a placeholder.

Do not reduce it to an insignificant thumbnail.

Its job is to transition the user from:

MY REPORT

to:

THE SYSTEM THAT CAN HELP ME IMPROVE.

Commercial language becomes appropriate here because the user has already received meaningful personal value.

---

# 27. FINAL CHAPTER — YOUR NEXT CHAPTER

There must be one ending.

Do not create a chain of competing endings.

Avoid structures like:

Threshold → Next Chapter → Master AI → Explore → CTA → another CTA.

Instead:

# YOUR NEXT CHAPTER

Then a concise emotional bridge, the final solution/context, and a clear CTA hierarchy.

The user should finish feeling invited, not pressured.

---

# 28. BUTTON SYSTEM

Buttons must feel premium, tactile, accessible, and intentional.

The seven-stage AI process uses semantic color language:

NO → RED
TELL → ORANGE
ASK → YELLOW
CREATE → LIGHT BLUE
SCORE → INDIGO / DARK BLUE
IMPROVE → PURPLE
REPEAT → MAGENTA

Buttons should have:

- strong contrast;
- dimensional depth;
- restrained gradient;
- icon consistency;
- tactile hover/focus state;
- smooth transition;
- touch-friendly target size;
- keyboard accessibility.

Do not make every button purple.

Do not use decorative color that conflicts with semantic meaning.

---

# 29. PAGE COLOR RHYTHM

Use deliberate chapter contrast.

A recommended rhythm is:

BLACK → WHITE → DARK → WHITE → PURPLE → BLACK → WHITE / CINEMATIC

Black = depth.

White = clarity.

Purple = possibility / Naya.

Spectrum = capability / energy.

Photography = humanity.

Orb = transformation.

Data = truth.

Background changes should feel like turning pages in a premium report.

---

# 30. TYPOGRAPHY

Hierarchy must remain obvious during a fast scan.

Priority:

1. Score
2. Chapter title
3. Section title
4. Supporting explanation
5. Detail / microcopy

Never reverse this hierarchy.

Important information must not be tiny, low contrast, or decorative-looking.

---

# 31. SCANABILITY

A user should be able to scroll rapidly and understand:

MY SCORE
→ MY FIVE DIMENSIONS
→ MY PATTERN
→ WHAT IT MEANS
→ MY STRENGTHS
→ MY LEVER
→ MY NEXT MOVE
→ MY AI MASTERS
→ MY NEXT CHAPTER

without reading every paragraph.

Use visual anchors, chapter numbers, large titles, scores, icons, and deliberate spacing.

---

# 32. IMAGE STORYTELLING

Images are narrative components.

Before using an image ask:

> What does this image communicate that the interface cannot communicate as effectively?

Possible jobs:

- warmth;
- humanity;
- relationship;
- possibility;
- identity;
- transformation;
- aspiration;
- personality.

If an image does not have a clear job, do not use it merely to fill space.

---

# 33. AUDIO / FACE / PRESENCE SYNCHRONIZATION

When Naya speaks:

- portrait may subtly pulse;
- a soft ring may animate;
- Orb may respond subtly;
- resonance paths may breathe;
- selected dimensions may illuminate where contextually appropriate.

When Naya stops:

- the system settles naturally.

Do not create noisy or mechanical visualizations.

The desired subconscious impression is:

> “Naya is actually interpreting my results.”

---

# 34. DATA INTEGRITY

`window.MAXESS_RESULT` is authoritative.

All visible result values must ultimately derive from the authoritative result object.

Do not scrape the DOM for scores.

Do not replace real results with a fixture.

A development fixture may exist only behind an explicit development mechanism and must never silently run in production.

Never hard-code a user's score, dimensions, labels, or interpretation into production markup.

Never manufacture missing result data merely to make the page look complete.

If required production data is missing, fail safely and visibly rather than fabricate.

---

# 35. PDF / PRINT EXPERIENCE

The PDF is a separate product surface.

Default print/report treatment:

# WHITE BACKGROUND
# BLACK TEXT
# MAXESS COLOR ACCENTS

Structure:

Cover
→ Score
→ Orb / Signature
→ Five Dimensions
→ Interpretation
→ Strengths
→ Biggest Lever
→ Next Move
→ Naya Masters / Pathway
→ Optional final CTA

Remove or hide:

- navigation;
- hover controls;
- unnecessary web buttons;
- animation-only elements;
- web chrome.

Control page breaks intentionally.

Do not allow important sections to split awkwardly.

The PDF must be readable without depending on the web page's dark cinematic styling.

---

# 36. RESPONSIVE DESIGN

Desktop:

Full widescreen cinematic experience.

Tablet:

Preserve hierarchy and visual impact.

Mobile:

Recompose rather than merely shrink.

The Orb remains prominent.

Gauges remain readable.

Naya remains recognizable.

Buttons remain touch-friendly.

No cramped miniature desktop layouts.

---

# 37. ACCESSIBILITY

Maintain:

- semantic headings;
- keyboard navigation;
- visible focus;
- sufficient contrast;
- screen-reader labels;
- accessible controls;
- reduced-motion support;
- touch-friendly targets.

Color must never be the only means of communicating score state or meaning.

---

# 38. PERFORMANCE

Premium visual quality must not require wasteful rendering.

Prefer:

- CSS transforms;
- opacity;
- efficient SVG;
- restrained particles;
- requestAnimationFrame only where justified;
- progressive enhancement;
- reduced complexity on lower-powered devices.

Avoid unnecessary heavy 3D libraries when CSS/SVG can achieve the result.

---

# 39. NAYA COPY RULES

Naya speaks like a highly intelligent, warm human guide.

She should be:

- concise;
- conversational;
- insightful;
- encouraging;
- honest;
- personal;
- never salesy too early;
- never repetitive.

Naya should interpret rather than narrate what the screen already says.

Bad:

> “Your score is 82 and your communication score is 87.”

Better:

> “Your communication strength gives you something valuable to build on.”

The visual already provides the numbers.

Naya provides meaning.

---

# 40. COPY ELIMINATION RULE

Specific language currently suspected of being weak or misplaced must be challenged rather than preserved automatically.

Examples:

- “Your AI Capability Has Shape” should not occupy the hero merely because the phrase sounds sophisticated.
- “Meaningful AI Foundation” should not occupy prime space unless it provides a genuine user insight.
- “Your AI Leverage” belongs conceptually with the Biggest Lever chapter if retained.
- Repeated use of “pattern” should be eliminated outside the dedicated pattern concept.

A phrase survives only if it performs a meaningful job.

---

# 41. COMPONENT ARCHITECTURE

Prefer reusable components over one-off visual hacks.

Required conceptual components include:

- HeroScore;
- MAXESSOrb;
- NayaPresence;
- NayaSpeech;
- NayaGuidance;
- DimensionGauge;
- DimensionRelationship;
- PatternVisualization;
- StrengthHighlight;
- BiggestLever;
- NextMove;
- NayaMaster;
- VideoSection;
- FinalCTA;
- PrintReportLayer.

Names may differ in implementation, but responsibilities must remain modular.

Do not duplicate logic unnecessarily.

---

# 42. IMPLEMENTATION ORDER

Do not redesign everything at once.

Use this sequence:

PHASE 0 — INVENTORY

PHASE 1 — ARCHITECTURE / SECTION ORDER

PHASE 2 — HERO + ORB

PHASE 3 — NAYA PRESENCE

PHASE 4 — FIVE DIMENSIONS

PHASE 5 — PATTERN

PHASE 6 — INTERPRETATION / STRENGTHS / LEVER

PHASE 7 — NEXT MOVE

PHASE 8 — 18 NAYA MASTERS

PHASE 9 — HUMAN + AI / SYSTEM / VIDEO

PHASE 10 — FINAL CTA

PHASE 11 — PDF / PRINT

PHASE 12 — MOBILE / ACCESSIBILITY / PERFORMANCE

PHASE 13 — WHOLE-PAGE OSCAR REVIEW

PHASE 14 — REGRESSION / LIVE VERIFICATION

Each phase must be independently testable.

A successfully completed phase becomes a protected baseline for the next phase.

---

# 43. REQUIREMENT TRACEABILITY

Every material requirement must map to:

REQUIREMENT → IMPLEMENTATION → VERIFICATION → EVIDENCE → STATUS

Example:

| Requirement | Implementation | Verification | Evidence | Status |
|---|---|---|---|---|
| Hero says YOUR AI SCORE | HeroScore heading | source + visual inspection | exact heading present | PASS |
| Orb responds to score | MAXESSOrb logic | result fixtures / runtime | score-to-color behavior | PASS |
| Naya portrait appears | NayaPresence | source + runtime | image rendered | PASS |
| PDF is readable | print stylesheet | print/PDF inspection | black text on white | PASS |

No material requirement may silently disappear.

---

# 44. BASELINE AND ZERO-CHANGE GATE

Before modification record the baseline artifact fingerprint, size, and relevant structural inventory.

After modification:

REFETCH → DIFF → INSPECT.

If a material implementation was requested and the authoritative artifact has no material change:

# BLOCKED — ZERO-CHANGE EXECUTION

Do not explain it away.

Do not claim the work was conceptually completed.

Do not deliver a placeholder.

---

# 45. DISTINCTIVE CHANGE PROOF

For every major request, document what changed in concrete terms.

Example:

REQUEST: simplify hero.

IMPLEMENTATION: removed competing hero copy and side content; centered score and Orb; retained primary CTA.

PROOF: final artifact contains the new hero structure and no prohibited hero copy.

VERIFICATION: static inventory + rendered inspection.

Claims must be tied to observable evidence.

---

# 46. REGRESSION PROTECTION

Before modification, identify protected functionality.

After modification, verify at minimum:

- result handoff;
- score rendering;
- dimension rendering;
- CTA behavior;
- Naya audio;
- video;
- responsive layout;
- print/PDF;
- accessibility;
- existing integrations;
- external links;
- loading behavior.

Any critical regression blocks release.

---

# 47. OSCAR REVIEW

Oscar is the adversarial quality role.

Oscar does not ask whether the implementation is “pretty good.”

Oscar asks:

> Why is this not a 10?

Oscar must inspect:

- hierarchy;
- visual impact;
- emotional experience;
- clarity;
- redundancy;
- section order;
- whitespace;
- typography;
- color rhythm;
- Naya presence;
- Orb quality;
- interactions;
- mobile;
- PDF;
- data integrity;
- performance;
- accessibility;
- preservation;
- technical reliability.

Oscar must identify the highest-impact remaining weaknesses, not merely praise the implementation.

If Oscar identifies a material weakness, fix it and retest.

---

# 48. RELEASE SCORECARD

Score the final experience:

Visual impact — 20%

Report clarity — 15%

Naya personality / presence — 15%

Orb / signature — 15%

Information hierarchy — 10%

Buttons / interactions — 10%

Widescreen composition — 5%

PDF / print — 5%

Technical reliability — 5%

Release target:

# 9.5+ OVERALL

No major category below:

# 9.0

And:

# ZERO CRITICAL REGRESSIONS

A score is earned through inspection and evidence.

---

# 49. LIVE PARITY

The repository is not the user.

The public product is the user.

The complete chain is:

SOURCE
→ BUILD / ASSEMBLY
→ GROOVE / PUBLISHER
→ DEPLOYMENT
→ PUBLIC URL
→ PUBLIC VERIFICATION

GitHub success alone is not product success.

If the public target does not reflect the authoritative artifact:

# BLOCKED — DEPLOYMENT PARITY FAILURE

If live deployment cannot be independently verified, status must explicitly say:

# LIVE — UNVERIFIED

Never imply verified live success when it was not checked.

---

# 50. GROOVE DELIVERY LOCK

A complete Results embed means the complete working Results implementation is contained in the delivered artifact.

Never deliver:

- a loader;
- a bootstrap that fetches the renderer from GitHub;
- a tiny wrapper around the Results file;
- a mock;
- a demo-only implementation;
- a partial excerpt;
- a broken external dependency path.

Before providing a Groove-ready artifact, verify that it contains the required markup, styles, scripts, data boundary, visual system, and behavior.

---

# 51. FAILURE STATES

Use explicit states:

DRAFT

PROTOTYPE

INTEGRATION

QA

BLOCKED — UNDERSTANDING INCOMPLETE

BLOCKED — SOURCE UNKNOWN

BLOCKED — ZERO-CHANGE EXECUTION

BLOCKED — DEPLOYMENT PARITY FAILURE

BLOCKED — REGRESSION

LIVE — UNVERIFIED

VERIFIED

PRODUCTION

Do not use “DONE” as a substitute for verification.

---

# 52. FINAL WHOLE-PAGE CHECKLIST

Before release, verify all of the following.

## Strategy

[ ] The page behaves like a personal report.
[ ] The user is the protagonist.
[ ] Naya is the guide.
[ ] The commercial layer is delayed until value has been delivered.
[ ] There is one coherent story.
[ ] There is one ending.

## Hero

[ ] “YOUR AI SCORE” is the primary hero message.
[ ] The real score is displayed.
[ ] The Orb is the visual centerpiece.
[ ] No competing side cards crowd the Orb.
[ ] Unnecessary hero copy has been removed.
[ ] Orb color responds to score.
[ ] Orb energy is premium and restrained.
[ ] Hero works on desktop and mobile.

## Naya

[ ] Naya portrait appears intentionally.
[ ] White/black portrait treatments are used according to chapter context.
[ ] Naya voice and visual identity feel continuous.
[ ] Naya speaks only where interpretation adds value.
[ ] Naya speech states are visually coherent.
[ ] Guidance popups use Naya where appropriate.
[ ] Naya does not become repetitive decoration.

## Five Dimensions

[ ] Five dimensions are clearly visible.
[ ] Scores are dominant.
[ ] Gauges are visually strong.
[ ] Dimensions feel connected.
[ ] Color is meaningful.
[ ] Color is not the only information channel.
[ ] Interaction is useful rather than ornamental.

## Pattern

[ ] Pattern appears in the correct place.
[ ] It visually demonstrates relationships.
[ ] It does not become a technical diagram.
[ ] Naya can interpret the visual.

## Interpretation

[ ] What It Means is clear.
[ ] Strengths create confidence.
[ ] Biggest Lever is dynamic.
[ ] Next Move is concrete.
[ ] No generic filler remains.

## Naya Masters

[ ] All required pathways exist.
[ ] Names are consistent.
[ ] Icons are visually coherent.
[ ] Each Master has a clear benefit.
[ ] They appear after the user understands the need.

## Human / Brand

[ ] Shawn + Naya imagery has a narrative purpose.
[ ] Brand imagery adds warmth rather than clutter.
[ ] Logo use is restrained.
[ ] MAXESS identity is consistent.

## Video / CTA

[ ] Existing video is preserved.
[ ] Video is prominent enough to matter.
[ ] Commercial material appears at the correct stage.
[ ] Final CTA is clear.
[ ] There is one final chapter.

## Visual quality

[ ] Every block earns its existence.
[ ] Visuals communicate before text.
[ ] Typography hierarchy is obvious.
[ ] Important text is readable.
[ ] Background rhythm creates chapter distinction.
[ ] Black/white/purple/spectrum balance is intentional.
[ ] No section feels flat, generic, crowded, or unfinished.
[ ] No section exists merely because space was available.

## Technical

[ ] `window.MAXESS_RESULT` is authoritative.
[ ] No production fixture silently supplies scores.
[ ] No fake result values remain.
[ ] No critical JavaScript errors.
[ ] No broken interactions.
[ ] No broken video.
[ ] No broken CTA.
[ ] Responsive behavior works.
[ ] Print/PDF works.
[ ] Accessibility requirements pass.
[ ] Performance remains acceptable.

## Preservation

[ ] Existing working functionality was inventoried.
[ ] Existing working functionality remains.
[ ] No working component was silently deleted.
[ ] No smaller replacement artifact substituted for the complete product.
[ ] Source authority is documented.

## Evidence

[ ] Baseline recorded.
[ ] Final artifact re-fetched.
[ ] Material diff confirmed.
[ ] Requirements mapped to evidence.
[ ] Tests completed.
[ ] Oscar review completed.
[ ] Oscar issues fixed or explicitly blocked.
[ ] Retest completed.
[ ] Live target checked where possible.
[ ] Delivery status is truthful.

---

# 53. DEFINITION OF DONE

MAXESS Results is not complete because:

- the file changed;
- GitHub accepted a write;
- the page loads;
- it looks better than before;
- an AI says “done.”

MAXESS Results is complete only when:

1. The full product architecture is coherent.
2. Every major section has a clear purpose and correct position.
3. The user can understand the report through scanning.
4. The hero creates a genuine reveal moment.
5. Naya feels present through voice + face + contextual interpretation.
6. The Orb is a signature visual asset.
7. The five dimensions are visually compelling and connected.
8. Pattern is visually meaningful.
9. Interpretation is personal and useful.
10. Strengths create recognition.
11. The Biggest Lever is dynamically meaningful.
12. The Next Move is actionable.
13. The 18 Naya Masters are introduced at the correct moment.
14. Human + AI philosophy is represented appropriately.
15. Video and CTA are positioned after value.
16. PDF is readable and professionally structured.
17. Desktop and mobile are excellent.
18. Accessibility and performance are acceptable.
19. Production data is real.
20. Existing working functionality is preserved.
21. Oscar has challenged the work.
22. Material issues found by Oscar have been fixed or explicitly blocked.
23. The final artifact has a material diff.
24. The final artifact has been re-fetched and inspected.
25. The live/public experience has been verified where possible.
26. The final status accurately reflects evidence.

If any critical condition is false:

# NOT DONE.

---

# 54. EXECUTION COMMAND

When this specification is loaded, the AI should be able to act from the following command:

> **NAYA MASTER ON. ACTIVATE NAYA LAW. LOAD THE MAXESS RESULTS MASTER INSTRUCTION SET. READ AND INVENTORY THE COMPLETE CURRENT RESULTS EXPERIENCE. SOURCE-LOCK THE AUTHORITATIVE ARTIFACT. BASELINE IT. MAP EVERY REQUIREMENT. PRESERVE WORKING VALUE. EXECUTE THE MASTER INSTRUCTION SET SECTION BY SECTION. AFTER EACH MATERIAL PHASE, REFETCH, DIFF, TEST, AND FREEZE SUCCESSFUL WORK. PUT ON OSCAR'S HAT, RIP THE RESULT APART, FIX THE HIGHEST-IMPACT WEAKNESSES, RETEST, AND VERIFY THE REAL USER-FACING EXPERIENCE. DO NOT CLAIM DONE WITHOUT EVIDENCE.**

---

# 55. FINAL CREATIVE STANDARD

The page must feel like:

# A PERSONAL CONVERSATION WITH AN INTELLIGENT SYSTEM.

The user sees themselves in the score.

They see the score in the Orb.

They see the structure in the dimensions.

They see the relationships in the pattern.

They hear Naya interpret what it means.

They recognize their strengths.

They discover their leverage.

They receive a next move.

They meet the 18 specialists.

They see the human philosophy behind the system.

They discover the larger solution.

Then they choose what happens next.

Every visual, word, color, image, animation, interaction, and section must serve that journey.

If it does not, question it.

If it weakens the journey, change it.

If it is unnecessary, remove it.

If it is good but not extraordinary, improve it.

If it is extraordinary, preserve it.

# SERVE THE PERSON.
# TELL THE TRUTH.
# MAKE THE EXPERIENCE BEAUTIFUL.
# MAKE THE RESULT UNDERSTANDABLE.
# MAKE NAYA FEEL PRESENT.
# PROVE THE WORK.
# VERIFY THE OUTCOME.
# SHIP AAA.
