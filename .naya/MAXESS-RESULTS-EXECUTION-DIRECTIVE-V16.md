# MAXESS RESULTS — V16 EXECUTION DIRECTIVE

Status: EXECUTION MASTER DIRECTIVE
Version: 16.0
Date: 2026-08-16
Artifact state governed by: `.naya/NAYA-LAW.md`
Results authority governed by: `.naya/RESULTS-SOURCE-REGISTRY.md`

---

# 0. PURPOSE

This document is the complete execution contract for the next MAXESS Results reconstruction.

Its job is to remove ambiguity between:

- what the human requested;
- what the AI believes it should do;
- what file is approved;
- what file is being edited;
- what was actually changed;
- what was merely tested;
- what was actually delivered;
- and what has been approved for future work.

The target is not a cosmetic refresh, wrapper, prototype, shortened replacement, or collection of labels around the existing page.

The target is a complete, self-contained, production-quality MAXESS Results experience that materially improves the product while preserving working functionality and real data contracts.

The execution must produce one explicit candidate state:

**UPDATED EDITED FILE — V16 — NOT YET AUTHORITATIVE**

That candidate is the only artifact to hand off for human review.

It becomes authoritative ONLY after explicit human approval.

---

# 1. MASTER EXECUTION PROMPT

Use the following as the internal execution instruction for the entire V16 build:

> NAYA MASTER ON.
>
> Execute MAXESS Results V16 as an engineering reconstruction, not a planning exercise and not a cosmetic patch.
>
> First read the repository law, governance, Results source registry, current approved baseline, relevant project instructions, assessment/result contract, and deployment path. Do not guess which file is authoritative.
>
> Treat the last human-approved artifact as the APPROVED/AUTHORITATIVE BASELINE. Do not call the current working file authoritative. Do not promote any new artifact automatically.
>
> Create a distinct V16 working/edit state. Perform the actual requested Results transformation against that working state.
>
> Preserve all working functionality unless the directive explicitly changes it. Preserve information even when the presentation is restructured.
>
> Build from the real `window.MAXESS_RESULT` contract. Do not invent a second scoring engine. Do not hard-code a fake personalized report when real result data is available.
>
> Reconstruct the entire Results experience from top to bottom: profile, score hero, narrative, pattern, five dimensions, strengths, biggest lever, next move, Naya/Orb relationship, 18 Naya Masters, pathway recommendations, conversion, responsive behavior, accessibility, performance, print/share behavior, and Groove-compatible deployment structure.
>
> Do not solve a large redesign by adding a small overlay, footer, wrapper, marker, or decorative layer while leaving the underlying weak architecture untouched.
>
> Map every requested feature to an implementation location before editing. Map every existing important feature to KEEP, REPAIR, RESTRUCTURE, REPLACE, ADD, REMOVE, or CONNECT.
>
> After implementation, inspect the complete artifact. Build a static inventory. Compare it against the approved baseline. Produce a requirement-by-requirement evidence map. Reject zero-change work. Reject materially incomplete work. Reject accidental regression.
>
> Test JavaScript syntax and data binding. Test the renderer with materially different result states. Test responsive behavior, accessibility, reduced motion, print/PDF, navigation, interactions, and failure/fallback states.
>
> Run Oscar as an adversarial product review. Oscar must try to prove that the result is still mediocre, incomplete, generic, disconnected from the real data, visually incoherent, slow, inaccessible, broken on mobile, or conversion-weak.
>
> Fix every material Oscar finding that is technically within scope.
>
> Re-fetch the exact written V16 artifact from GitHub after writing. Verify its exact version markers, content, hash/blob, size, required components, and diff against the approved baseline.
>
> The final handoff MUST say `UPDATED EDITED FILE — V16 — NOT YET AUTHORITATIVE`.
>
> Never call V16 authoritative until Shawn explicitly approves it.
>
> If the artifact did not materially change, STOP and report `BLOCKED — ZERO-CHANGE EXECUTION` rather than pretending progress occurred.
>
> If deployment cannot be verified, report `NOT LIVE VERIFIED`; do not claim LIVE.
>
> The only acceptable standard is: AAA, distinctive, personal, cohesive, conversion-effective, beautiful, useful, fast, reliable, accessible, and genuinely improved.

---

# 2. NON-NEGOTIABLE STATE MODEL

```text
APPROVED / AUTHORITATIVE BASELINE
        ↓
V16 WORKING COPY
        ↓
REAL IMPLEMENTATION
        ↓
UPDATED EDITED FILE — V16
        ↓
STATIC + FUNCTIONAL + REGRESSION + OSCAR QA
        ↓
HANDOFF FOR HUMAN REVIEW
        ↓
EXPLICIT HUMAN APPROVAL
        ↓
PROMOTE V16 → AUTHORITATIVE / APPROVED
```

Never reverse this order.

Never hand off the approved baseline while describing it as the new edit.

Never hand off V16 while calling it authoritative.

---

# 3. PHASE A — PRE-FLIGHT / SOURCE DISCOVERY

## A1. Read governance

- [ ] `.naya/NAYA-LAW.md`
- [ ] `.naya/RESULTS-SOURCE-REGISTRY.md`
- [ ] all applicable repository governance documents actually present in the repository
- [ ] relevant MAXESS project instructions
- [ ] relevant assessment/result architecture documentation
- [ ] deployment/Groove instructions available in the repository

## A2. Identify the approved baseline

Record:

- [ ] approved version
- [ ] exact branch
- [ ] exact commit SHA
- [ ] exact file path
- [ ] exact blob/content SHA where available
- [ ] byte count
- [ ] line count
- [ ] baseline HTML structure
- [ ] baseline CSS structure
- [ ] baseline JavaScript structure
- [ ] baseline data contract
- [ ] baseline external dependencies
- [ ] baseline deployment relationship

## A3. Identify the current candidate state

- [ ] determine whether an unapproved edit already exists
- [ ] do NOT treat it as authoritative
- [ ] identify whether it is reusable, superseded, broken, or historical
- [ ] preserve it for forensic comparison if useful

## A4. Trace the actual product path

```text
ASSESSMENT
→ RESULT CALCULATION
→ RESULT CONTRACT
→ MAXESS_RESULT
→ RESULTS RENDERER
→ GROOVE ARTIFACT
→ PUBLIC URL
```

For each arrow:

- [ ] identify the actual implementation
- [ ] identify transformations
- [ ] identify fallbacks
- [ ] identify cached/generated copies
- [ ] identify external dependencies
- [ ] identify what can diverge

## A5. Source conflict gate

- [ ] exactly one approved baseline identified
- [ ] no conflicting source silently selected
- [ ] if conflict exists: BLOCKED until resolved

---

# 4. PHASE B — COMPLETE ARCHITECTURE MAP

Create an explicit inventory before editing.

## B1. Document structure

- [ ] document/head/meta
- [ ] fonts
- [ ] global variables/tokens
- [ ] global reset
- [ ] page shell
- [ ] navigation/header
- [ ] main content container
- [ ] footer/end matter

## B2. Results components

Identify exact implementation for:

- [ ] Personal Profile
- [ ] AI Score hero
- [ ] score interpretation
- [ ] report title/subtitle
- [ ] narrative introduction
- [ ] strongest signal
- [ ] biggest lever
- [ ] five dimensions
- [ ] dimension scores
- [ ] dimension interpretation
- [ ] strengths
- [ ] improvement areas
- [ ] next move
- [ ] Naya guidance
- [ ] Orb/signature
- [ ] Naya/Orb speaking state
- [ ] 18 Naya Masters
- [ ] master cards/icons
- [ ] personalized master recommendations
- [ ] pathway/library relationship
- [ ] CTA/conversion sections
- [ ] navigation/anchors
- [ ] print/PDF behavior
- [ ] fallback/error states

## B3. Runtime architecture

- [ ] `window.MAXESS_RESULT`
- [ ] profile source
- [ ] dimension source
- [ ] score normalization
- [ ] strongest-signal derivation
- [ ] biggest-lever derivation
- [ ] personalization logic
- [ ] master recommendations
- [ ] Naya state
- [ ] Orb state
- [ ] event listeners
- [ ] DOM mounting
- [ ] initialization order
- [ ] failure/fallback handling

## B4. Styling architecture

- [ ] typography system
- [ ] spacing system
- [ ] color tokens
- [ ] surfaces
- [ ] borders
- [ ] shadows
- [ ] radii
- [ ] gradients
- [ ] motion
- [ ] responsive breakpoints
- [ ] focus states
- [ ] print styles
- [ ] reduced-motion styles

## B5. Dependency architecture

For every external dependency:

- [ ] identify purpose
- [ ] identify failure mode
- [ ] identify whether it is necessary
- [ ] identify whether self-contained implementation is preferable
- [ ] confirm no hidden runtime loader undermines Groove reliability

---

# 5. PHASE C — BASELINE PRESERVATION MAP

Every existing material feature must be classified.

### KEEP
- [ ] working functionality that remains correct

### REPAIR
- [ ] functional but broken/weak behavior

### RESTRUCTURE
- [ ] useful content in weak hierarchy/location

### REPLACE
- [ ] implementation that prevents the required experience

### ADD
- [ ] missing requirements

### REMOVE
- [ ] redundancy, misleading content, obsolete behavior, or explicitly rejected elements

### CONNECT
- [ ] existing features that are currently disconnected from real result data or the new narrative

For every classification, record:

- [ ] current implementation
- [ ] reason
- [ ] V16 treatment
- [ ] regression test

---

# 6. PHASE D — RESULT DATA CONTRACT

This is a hard architectural boundary.

## D1. Authoritative result data

- [ ] use `window.MAXESS_RESULT`
- [ ] identify exact schema
- [ ] identify profile data
- [ ] identify total score
- [ ] identify five dimension values
- [ ] identify labels
- [ ] identify raw/normalized values where available
- [ ] identify answer-derived metadata
- [ ] identify assessment identity/version

## D2. No fake second scoring engine

- [ ] renderer does not secretly calculate a competing score
- [ ] display transformations are clearly separated from scoring
- [ ] fallback data is explicitly development-only
- [ ] no production user is silently shown a development fixture

## D3. Personalization

- [ ] personal profile is real
- [ ] strongest signal is derived from the person's actual result
- [ ] biggest lever is derived from the person's actual result
- [ ] five-dimension narrative reflects the actual score pattern
- [ ] Naya language reflects the individual's pattern
- [ ] Masters recommendations reflect actual needs/opportunities
- [ ] no generic copy masquerades as personalization

## D4. Multi-state testing

Test at least:

- [ ] high balanced profile
- [ ] high/low contrast profile
- [ ] low profile
- [ ] missing/partial data fallback
- [ ] unusual but valid score distribution

---

# 7. PHASE E — EXPERIENCE ARCHITECTURE / REPORT HIERARCHY

The page must read as a guided report, not a collection of dashboard cards.

## E1. Narrative sequence

The exact sequence must be evaluated and intentionally designed around:

1. [ ] Who you are / Personal Profile
2. [ ] Your AI Score
3. [ ] What your score means
4. [ ] See the Pattern
5. [ ] Your Five Dimensions
6. [ ] Your Strongest Signal
7. [ ] Your Biggest Lever
8. [ ] Your Strengths
9. [ ] Your Next Move
10. [ ] Naya's personalized interpretation/guidance
11. [ ] 18 Naya Masters / personalized pathway
12. [ ] Your Next Chapter / conversion

This is a target architecture, not permission to blindly preserve wording if evidence shows a stronger hierarchy. Any change must improve comprehension and conversion.

## E2. Information hierarchy

- [ ] one dominant hero message
- [ ] clear score hierarchy
- [ ] clear subheadline
- [ ] strong section rhythm
- [ ] progressive disclosure
- [ ] no competing hero elements
- [ ] no excessive card grid feeling
- [ ] no unexplained visual ornaments

## E3. Narrative quality

- [ ] user sees themselves in the report
- [ ] score is explained rather than merely displayed
- [ ] pattern is visually obvious
- [ ] strengths feel specific
- [ ] biggest lever feels actionable
- [ ] next move feels achievable
- [ ] Naya feels like a guide, not a decorative chatbot
- [ ] conversion is earned by value delivered

---

# 8. PHASE F — PERSONAL PROFILE

- [ ] use real profile information available to the Results contract
- [ ] show identity clearly without overloading the hero
- [ ] visually connect profile to assessment outcome
- [ ] handle missing profile fields gracefully
- [ ] no fake name/avatar/profile data
- [ ] accessible semantics
- [ ] mobile-safe layout

---

# 9. PHASE G — AI SCORE HERO

- [ ] score is the primary hero metric
- [ ] score uses authoritative result data
- [ ] no misleading score duplication
- [ ] clear interpretation band/level
- [ ] concise explanatory copy
- [ ] visually premium
- [ ] responsive typography
- [ ] animation is restrained and accessible
- [ ] reduced-motion alternative
- [ ] no score flicker during initialization

---

# 10. PHASE H — PATTERN / FIVE DIMENSIONS

- [ ] five dimensions are clearly identified
- [ ] exact scores are visible
- [ ] labels are understandable
- [ ] pattern is visually interpretable without technical knowledge
- [ ] strongest dimension is distinguishable
- [ ] weakest/opportunity dimension is distinguishable
- [ ] relationships between dimensions are explained
- [ ] no misleading ranking if scores are effectively tied
- [ ] responsive visualization
- [ ] accessible text equivalent
- [ ] print-friendly representation

The pattern section should answer:

> “What does the shape of my result tell me about how I currently use AI?”

---

# 11. PHASE I — STRONGEST SIGNAL

- [ ] derive from actual five-dimension result
- [ ] identify why it is strong
- [ ] connect strength to practical behavior
- [ ] avoid generic praise
- [ ] show evidence from the person's result
- [ ] connect to future opportunity
- [ ] allow tied scores gracefully

---

# 12. PHASE J — BIGGEST LEVER

This is not simply “lowest score.”

- [ ] identify the most strategically important opportunity
- [ ] consider score and leverage, not only rank
- [ ] explain why it matters
- [ ] explain what improvement would unlock
- [ ] give a concrete next action
- [ ] connect to relevant Naya Master(s)
- [ ] avoid shame/deficit framing
- [ ] personalize the language

---

# 13. PHASE K — NAYA EXPERIENCE

Naya must be an integrated intelligence layer.

## K1. Naya role

- [ ] interpret the report
- [ ] connect sections
- [ ] explain patterns
- [ ] identify opportunity
- [ ] recommend next actions
- [ ] connect user to relevant Masters

## K2. Orb

- [ ] Orb has clear purpose
- [ ] Orb is visually distinctive
- [ ] Orb is not redundant decoration
- [ ] Orb has stable idle state
- [ ] Orb has speaking/thinking/active state
- [ ] Orb state is connected to Naya state
- [ ] no fake animation implying speech when Naya is not speaking
- [ ] reduced-motion behavior
- [ ] mobile behavior
- [ ] keyboard/focus behavior if interactive

## K3. Naya/Orb relationship

The experience must communicate:

**Naya = intelligence/voice/guide**

**Orb = visible signature/presence/state**

They must feel like one system rather than two unrelated widgets.

---

# 14. PHASE L — 18 NAYA MASTERS

Preserve all 18 canonical Masters:

1. Writing & Communication
2. Research & Information
3. Brainstorming & Ideas
4. Content Creation
5. Business & Strategy
6. Marketing & Sales
7. Learning & Education
8. Coding & Software
9. Images & Visual Creation
10. Video & Media
11. Audio & Music
12. Data & Analysis
13. Productivity & Organization
14. Career & Professional Growth
15. Decision Making
16. Creative Development
17. Systems & Automation
18. AI Orchestration

For each:

- [ ] canonical name preserved
- [ ] icon/visual identity
- [ ] short useful description
- [ ] connection to user's result
- [ ] relevance indicator or reason
- [ ] actionable next step where appropriate
- [ ] mobile layout
- [ ] keyboard/accessibility support
- [ ] no duplicate or missing Master

The library must feel like a personalized pathway, not an arbitrary catalogue.

---

# 15. PHASE M — VISUAL DESIGN SYSTEM

The target visual standard is premium digital product/report, not generic dashboard.

## M1. Brand

- [ ] MAXESS visual identity
- [ ] Naya signature
- [ ] intentional purple/black/white/gold relationship where appropriate
- [ ] consistent visual language

## M2. Typography

- [ ] display hierarchy
- [ ] body hierarchy
- [ ] labels
- [ ] numeric score typography
- [ ] readable line lengths
- [ ] mobile scaling

## M3. Layout

- [ ] generous spacing
- [ ] intentional section transitions
- [ ] controlled content width
- [ ] clear alignment system
- [ ] visual rhythm
- [ ] no accidental empty space
- [ ] no cramped sections

## M4. Components

- [ ] reusable component patterns
- [ ] consistent states
- [ ] consistent spacing
- [ ] consistent interaction language
- [ ] no unnecessary one-off decoration

## M5. Visual storytelling

- [ ] score feels important
- [ ] pattern feels discoverable
- [ ] strongest signal feels rewarding
- [ ] biggest lever feels motivating
- [ ] Naya feels present
- [ ] Masters feel like an exciting next chapter

---

# 16. PHASE N — RESPONSIVE / MOBILE

Explicitly test:

- [ ] 320px
- [ ] 375px
- [ ] 390px
- [ ] 430px
- [ ] tablet portrait
- [ ] tablet landscape
- [ ] desktop
- [ ] wide desktop

Check:

- [ ] no horizontal overflow
- [ ] no clipped text
- [ ] no broken charts
- [ ] no inaccessible controls
- [ ] no giant dead zones
- [ ] no microscopic text
- [ ] no broken Orb
- [ ] no broken profile
- [ ] Masters remain usable
- [ ] CTA remains visible and logical

---

# 17. PHASE O — ACCESSIBILITY

- [ ] semantic headings
- [ ] logical heading hierarchy
- [ ] landmark regions
- [ ] keyboard navigation
- [ ] visible focus
- [ ] sufficient contrast
- [ ] meaningful alt text where needed
- [ ] decorative graphics hidden appropriately
- [ ] accessible score text
- [ ] accessible chart/pattern alternative
- [ ] form/control labels
- [ ] reduced motion
- [ ] no color-only meaning
- [ ] touch targets appropriate

---

# 18. PHASE P — PERFORMANCE / RELIABILITY

- [ ] minimize unnecessary dependencies
- [ ] avoid duplicate render passes
- [ ] avoid layout thrashing
- [ ] avoid blocking initialization
- [ ] no unnecessary network fetch for core Results rendering
- [ ] self-contained critical renderer where architecture permits
- [ ] graceful dependency failure
- [ ] no console errors
- [ ] no unhandled promise rejection
- [ ] no runaway animation
- [ ] no memory-heavy repeated listeners

---

# 19. PHASE Q — GROOVE COMPATIBILITY

- [ ] complete self-contained artifact
- [ ] no accidental dependency on local development paths
- [ ] no inaccessible filesystem assumptions
- [ ] no build step required unless Groove explicitly provides it
- [ ] scripts execute in the intended embedding context
- [ ] CSS does not leak dangerously into surrounding page
- [ ] surrounding page does not unintentionally break Results
- [ ] initialization works when loaded in Groove
- [ ] result contract is available at initialization time or safely awaited
- [ ] fallback behavior is explicit
- [ ] external scripts are minimized and justified

---

# 20. PHASE R — FUNCTIONAL INTERACTIONS

Inventory every interactive element.

For each:

- [ ] click/tap works
- [ ] keyboard works
- [ ] visible state changes correctly
- [ ] destination/action is correct
- [ ] no dead buttons
- [ ] no placeholder links
- [ ] no misleading controls
- [ ] no duplicate event listeners
- [ ] mobile interaction works

Include:

- [ ] navigation
- [ ] anchors
- [ ] Naya/Orb interaction if present
- [ ] Master actions
- [ ] conversion CTA
- [ ] print/save
- [ ] share/copy if present

---

# 21. PHASE S — CONVERSION FLOW

Conversion must follow demonstrated value.

- [ ] user understands result before CTA
- [ ] CTA is connected to next logical action
- [ ] CTA copy is specific
- [ ] value proposition is clear
- [ ] relevant Master pathway is visible
- [ ] no premature hard sell
- [ ] no misleading claims
- [ ] no broken destination
- [ ] mobile CTA behavior
- [ ] final CTA provides a clear next chapter

---

# 22. PHASE T — CONTENT / COPY REVIEW

For every major text block:

- [ ] specific to MAXESS
- [ ] specific to the user where data permits
- [ ] understandable without technical expertise
- [ ] concise
- [ ] emotionally intelligent
- [ ] useful
- [ ] no generic AI filler
- [ ] no unsupported claims
- [ ] no repetitive explanation
- [ ] strong headings
- [ ] clear CTA

Tone:

- intelligent
- warm
- direct
- encouraging
- premium
- human
- never corporate sludge
- never generic AI prose

---

# 23. PHASE U — COMPLETE ARTIFACT REASSEMBLY

Before final write:

- [ ] all required sections exist
- [ ] all required scripts exist
- [ ] all required styles exist
- [ ] all dependencies accounted for
- [ ] all IDs/classes are internally consistent
- [ ] no duplicate IDs
- [ ] no orphaned event handlers
- [ ] no missing function definitions
- [ ] no broken references
- [ ] no accidental truncation
- [ ] file closes correctly
- [ ] complete artifact is deployable

The final candidate must be a complete file, not a patch fragment.

---

# 24. PHASE V — STATIC INVENTORY

Produce a machine-readable inventory covering:

- [ ] byte count
- [ ] line count
- [ ] HTML sections
- [ ] IDs
- [ ] classes
- [ ] CSS blocks
- [ ] JS blocks
- [ ] functions
- [ ] event listeners
- [ ] external resources
- [ ] data bindings
- [ ] required section markers
- [ ] 18 Masters
- [ ] accessibility markers
- [ ] responsive rules
- [ ] print rules
- [ ] Naya/Orb state hooks

Compare V16 inventory to baseline.

---

# 25. PHASE W — REQUIREMENT EVIDENCE MATRIX

For every directive item record:

```text
REQUIREMENT
STATUS: PASS / FAIL / BLOCKED
IMPLEMENTATION LOCATION
EVIDENCE
REGRESSION RISK
TEST PERFORMED
```

No material requirement may be marked PASS without evidence.

---

# 26. PHASE X — DIFF / NO-OP / REGRESSION GATES

## X1. Diff

- [ ] compare candidate against approved baseline
- [ ] inspect actual diff
- [ ] classify every changed region

## X2. Zero-change

- [ ] candidate hash differs
- [ ] file content materially differs
- [ ] requested components materially differ
- [ ] not merely metadata/markers

## X3. Regression

- [ ] required old functionality remains
- [ ] required data remains
- [ ] existing integrations remain
- [ ] no accidental deletion
- [ ] no older artifact reintroduced

If any gate fails:

**BLOCKED — DO NOT HAND OFF AS SUCCESS.**

---

# 27. PHASE Y — FUNCTIONAL QA

Run:

- [ ] JavaScript syntax check
- [ ] HTML structural check
- [ ] CSS sanity check
- [ ] data-binding checks
- [ ] result-state checks
- [ ] interaction checks
- [ ] responsive checks
- [ ] accessibility checks
- [ ] print/PDF checks
- [ ] console-error check
- [ ] dependency/load check
- [ ] regression checks

Where browser automation is available, use it. Where it is unavailable, explicitly identify the unverified browser behavior instead of claiming it passed.

---

# 28. PHASE Z — OSCAR ADVERSARIAL REVIEW

Oscar must attempt to fail the product.

Ask:

### PRODUCT
- [ ] Is this genuinely better?
- [ ] Does it feel distinctive?
- [ ] Does it feel premium?
- [ ] Does it feel like MAXESS rather than a template?

### UX
- [ ] Can a first-time user understand it?
- [ ] Is the narrative obvious?
- [ ] Is the next action obvious?
- [ ] Is there cognitive overload?

### DATA
- [ ] Are all personalized claims real?
- [ ] Is `MAXESS_RESULT` actually driving the experience?
- [ ] Can two different result states visibly produce different reports?

### DESIGN
- [ ] Does the page look cohesive?
- [ ] Are sections visually related?
- [ ] Is there too much card-grid repetition?
- [ ] Is the Orb meaningful?
- [ ] Does Naya feel integrated?

### TECHNICAL
- [ ] Any broken JS?
- [ ] Any dead interaction?
- [ ] Any race condition?
- [ ] Any dependency failure?
- [ ] Any regression?

### ACCESSIBILITY
- [ ] Can keyboard users navigate?
- [ ] Is the score understandable without the graphic?
- [ ] Is motion optional?

### PERFORMANCE
- [ ] Is initialization efficient?
- [ ] Is there unnecessary network work?
- [ ] Are animations restrained?

### MOBILE
- [ ] Is the mobile experience intentionally designed?
- [ ] Does anything overflow or collapse badly?

### CONVERSION
- [ ] Does the report naturally lead to a next step?
- [ ] Is the CTA earned?
- [ ] Is the pathway compelling?

Any material FAIL returns the artifact to BUILD.

---

# 29. PHASE AA — FINAL WRITE

Only after all upstream checks:

- [ ] write the complete V16 candidate
- [ ] commit with explicit V16 message
- [ ] record commit SHA
- [ ] record content/blob SHA
- [ ] record byte count

The final candidate remains:

**UPDATED EDITED FILE — V16 — NOT YET AUTHORITATIVE**

---

# 30. PHASE AB — RE-FETCH / ACTUAL FILE PROOF

Immediately after writing:

- [ ] re-fetch exact file from exact commit/branch
- [ ] confirm file exists
- [ ] confirm complete content
- [ ] confirm V16 implementation markers
- [ ] confirm no truncation
- [ ] confirm hash/content SHA
- [ ] confirm expected byte count
- [ ] confirm actual changed regions
- [ ] compare re-fetched artifact to the candidate used for verification

If fetched content differs:

**BLOCKED — WRITE/READ PARITY FAILURE.**

---

# 31. PHASE AC — FINAL HANDOFF

The handoff MUST state:

```text
UPDATED EDITED FILE — V16
STATUS: NOT YET AUTHORITATIVE
BASELINE: APPROVED V14 / exact recorded SHA
CANDIDATE: V16 / exact commit + file SHA
LIVE: VERIFIED or NOT VERIFIED
OSCAR: PASS or BLOCKED
REGRESSION: PASS or BLOCKED
```

The link MUST point to the exact Updated Edited File version.

Do NOT call it authoritative.

Do NOT call it approved.

Do NOT call it live unless public verification actually occurred.

---

# 32. PHASE AD — HUMAN PROMOTION

Only after Shawn explicitly approves V16:

- [ ] record approval
- [ ] promote exact V16 commit/hash to approved baseline
- [ ] update Results Source Registry
- [ ] mark V16 authoritative/approved
- [ ] preserve previous baseline as recoverable history
- [ ] use V16 as baseline for V17

Approval language must be explicit.

Silence is not approval.

Continued work is not approval.

Technical test success is not approval.

---

# 33. DEFINITION OF SUCCESS

V16 is successful only if ALL of the following are true:

- [ ] real approved baseline was used
- [ ] actual working edit was created
- [ ] candidate materially differs from baseline
- [ ] complete requested scope was implemented
- [ ] working functionality was preserved
- [ ] result data is real and authoritative
- [ ] personalization is genuine
- [ ] report hierarchy is coherent
- [ ] visual system is premium
- [ ] Naya is integrated
- [ ] Orb is integrated
- [ ] all 18 Masters are preserved
- [ ] responsive behavior is intentionally designed
- [ ] accessibility requirements are addressed
- [ ] performance is acceptable
- [ ] Groove compatibility is preserved
- [ ] conversion flow is coherent
- [ ] complete artifact exists
- [ ] static inventory passes
- [ ] functional checks pass
- [ ] regression checks pass
- [ ] Oscar finds no material unresolved issue
- [ ] exact candidate was re-fetched
- [ ] live status is honestly reported
- [ ] handoff is explicitly labeled UPDATED EDITED FILE
- [ ] no authority promotion occurs without Shawn's approval

---

# 34. FINAL SELF-QUESTION

Before handoff, the executor MUST ask:

> **WHY IS THIS NOT A 10?**

Then divide the answer into:

### MUST FIX NOW
Material deficiency that can be fixed within scope.

### BLOCKED DEPENDENCY
Requires something unavailable externally.

### ACCEPTABLE TRADEOFF
Conscious decision with a documented reason.

No material MUST FIX NOW item may remain unresolved while declaring success.

---

# 35. FAILURE RESPONSE

If execution fails:

```text
STOP
↓
IDENTIFY FAILURE CLASS
↓
ROOT CAUSE
↓
FIX THE MECHANISM
↓
ADD A MACHINE-CHECKABLE SAFEGUARD
↓
RETEST
↓
RESUME ONLY AFTER THE SAFEGUARD PASSES
```

Never simply rerun the same failed process.

---

# 36. EXECUTION LOG TEMPLATE

```text
EXECUTION: MAXESS RESULTS V16

APPROVED BASELINE:
Version:
Commit:
File SHA:
Bytes:

UPDATED EDITED FILE:
Version: V16
Commit:
File SHA:
Bytes:

REQUIREMENTS:
Passed:
Failed:
Blocked:

MAJOR CHANGES:
1.
2.
3.

PRESERVED:
1.
2.
3.

REPAIRED:
1.
2.
3.

RESTRUCTURED:
1.
2.
3.

ADDED:
1.
2.
3.

OSCAR:
Pass/Fail:
Findings:
Fixes:

FUNCTIONAL QA:
Pass/Fail:

REGRESSION:
Pass/Fail:

PUBLIC/LIVE:
Verified/Not Verified:

PROMOTION:
NOT YET AUTHORITATIVE / APPROVED

HANDOFF:
Exact Updated Edited File link:
```

---

# FINAL DIRECTIVE

Do not optimize for producing a response that sounds complete.

Optimize for producing an artifact that is actually complete.

Do not optimize for preserving the current implementation merely because it exists.

Preserve what works; reconstruct what does not.

Do not optimize for avoiding change.

Optimize for meaningful improvement.

Do not optimize for passing superficial checks.

Optimize for the real human experience.

Do not call the newest file authoritative.

The newest candidate is the UPDATED EDITED FILE.

Authority belongs to the last human-approved baseline.

**BUILD THE THING. PROVE THE THING. HAND OFF THE UPDATED EDITED FILE. WAIT FOR APPROVAL. THEN PROMOTE IT.**
