# MAXESS RESULTS — SOURCE REGISTRY

Status: AUTHORITATIVE CONTROL DOCUMENT
Version: 2.0
Updated: 2026-08-16

## PURPOSE

This registry is the single source-of-truth map for the MAXESS Results surface. Historical files are reference material only unless explicitly promoted here.

## CURRENT AUTHORITATIVE ENGINEERING SOURCE

Repository: `SoulSchoolAcademy/maxess`

Execution branch for this AAA v2 release: `naya/results-aaa-v2`

Foundation:

`MAXESS-RESULTS-10-GROOVE.html`

Presentation layer:

`MAXESS-RESULTS-EXPERIENCE.js`

Presentation-layer content SHA for this release:

`648c7908d093052b956c3c879af1dea05768659f`

Complete Groove delivery artifact:

`MAXESS-RESULTS-10.10-GROOVE-EMBED-COMPLETE.html`

Complete artifact content SHA for this release:

`74cc12718cadd7673b3c313398c91ea30f027d91`

The complete Groove artifact is the preferred delivery file. It is self-contained and MUST NOT require a GitHub-hosted Results renderer.

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

Legacy alternate dimension names are not part of the current Results contract.

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
MAXESS-RESULTS-10.10-GROOVE-EMBED-COMPLETE.html
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

It must contain:

- markup;
- CSS;
- JavaScript behavior;
- result decoding/handoff;
- responsive behavior;
- accessibility behavior;
- requested Results sections;
- Naya interactions;
- print/PDF behavior;
- no external GitHub Results renderer dependency;
- no iframe/loader shortcut used as the Results implementation.

## DEVELOPMENT DATA RULE

The complete artifact contains a deterministic fixture only when the explicit `fixture=demo` query parameter is supplied. Production URLs without that parameter do not receive fixture data.

Production remains:

`Assessment → window.MAXESS_RESULT → Results renderer`

## PRESERVATION RULE

The presentation layer must preserve pre-existing media when it exists inside the Results root before runtime rendering. It must also preserve the surrounding NayaNET foundation and later conversion architecture outside the Results root.

Do not invent a media URL or replace missing real media with a fake production video.

## DELIVERY GATE

Before Groove publication, prove:

1. The branch contains the intended source and presentation changes.
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
