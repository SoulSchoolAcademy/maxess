# MAXESS RESULTS — SOURCE REGISTRY

Status: AUTHORITATIVE CONTROL DOCUMENT
Version: 2.1
Updated: 2026-08-16

## CURRENT AUTHORITATIVE ENGINEERING SOURCE

Repository: `SoulSchoolAcademy/maxess`

Execution branch: `naya/results-aaa-v2`

Foundation:

`MAXESS-RESULTS-10-GROOVE.html`

Presentation layer:

`MAXESS-RESULTS-EXPERIENCE.js`

Current presentation content SHA:

`9ba5ce3a5763a25b6ebbaff66a1b1343d9074c23`

Complete Groove delivery artifact:

`MAXESS-RESULTS-10.10-GROOVE-EMBED-COMPLETE.html`

Current complete artifact content SHA:

`74cc12718cadd7673b3c313398c91ea30f027d91`

The complete Groove artifact is a self-contained compiled delivery snapshot. It must not depend on a GitHub-hosted Results renderer at runtime.

Public verification target:

`https://results.nayanet.xyz/`

## RELEASE STATUS

GitHub implementation status:

**AAA V2 IMPLEMENTED ON EXECUTION BRANCH**

Public deployment status:

**LIVE-VERIFIED = FALSE**

The public URL must not be called live, verified, 9.5+, or AAA until the external Groove publishing source is updated and the actual public URL is independently re-fetched and compared.

## AUTHORITATIVE DATA BOUNDARY

`window.MAXESS_RESULT` is authoritative.

The Results presentation layer reads and interprets that contract. It does not calculate assessment scoring and must not manufacture production data from DOM content.

Authoritative dimensions:

1. Direction
2. Communication
3. Evaluation
4. Iteration
5. Systems Thinking

## ARCHITECTURE

```text
MAXESS Assessment
      ↓
window.MAXESS_RESULT
      ↓
MAXESS-RESULTS-10-GROOVE.html
      ↓
MAXESS-RESULTS-EXPERIENCE.js
      ↓
COMPLETE GROOVE EMBED
      ↓
Groove deployment
      ↓
https://results.nayanet.xyz/
      ↓
Independent live verification
```

`nayanetpagecode` remains the preserved NayaNET foundation. It is not a competing Results renderer.

## AAA V2 EXPERIENCE CONTRACT

The Results layer must present:

- score-first hero;
- large score-reactive MAXESS Orb;
- Naya ↔ Orb resonance;
- personal report framing;
- five premium circular dimension gauges;
- real five-dimension relationship visualization;
- strongest dimension;
- dynamically determined biggest lever;
- one clear next move;
- current KNOW → TELL → ASK → CREATE → SCORE → IMPROVE → FREEZE method;
- all 18 Naya Masters;
- solution/conversion after personal value;
- responsive/mobile behavior;
- accessibility and reduced motion;
- print/PDF treatment.

“Pattern” is reserved primarily for the relationship visualization. It must not dominate the hero.

## COMPLETE EMBED RULE

The preferred Groove delivery is exactly one complete file:

`MAXESS-RESULTS-10.10-GROOVE-EMBED-COMPLETE.html`

It must contain markup, CSS, JavaScript behavior, result decoding/handoff, responsive behavior, accessibility behavior, requested Results sections, Naya interactions, print/PDF behavior, and no external GitHub Results renderer dependency.

A snippet, bootstrap, loader, or partial file is not acceptable delivery.

## DEVELOPMENT DATA RULE

The complete artifact contains a deterministic fixture only when the explicit `fixture=demo` query parameter is supplied. Production URLs without that parameter do not receive fixture data.

Production remains:

`Assessment → window.MAXESS_RESULT → Results renderer`

## PRESERVATION RULE

The presentation layer captures pre-existing video/iframe media inside the Results root before runtime replacement and reattaches it to the solution chapter. It does not invent a replacement media URL when no authoritative media exists.

The surrounding NayaNET foundation and later conversion architecture remain outside the Results renderer and are not rebuilt by the presentation layer.

## DELIVERY GATE

Before Groove publication, prove:

1. The intended source and presentation files changed.
2. The complete artifact is self-contained.
3. The complete artifact does not load a second Results renderer.
4. `window.MAXESS_RESULT` remains the production data boundary.
5. All five authoritative dimensions are present.
6. All 18 Naya Masters are present.
7. No silent production fixture exists.
8. Static JavaScript syntax passes.
9. Runtime bootstrap smoke test passes.
10. Reduced-motion and print rules exist.
11. Existing media/foundation/conversion behavior is preserved where present.
12. The public URL is re-fetched after Groove publication.

If any deployment-parity proof is missing:

**BLOCKED — DEPLOYMENT PARITY FAILURE**
