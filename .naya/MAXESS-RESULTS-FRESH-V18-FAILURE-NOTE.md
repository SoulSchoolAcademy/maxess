# MAXESS RESULTS — V17 FAILURE NOTE / V18 FRESH-BUILD RULE

Status: ACTIVE GOVERNANCE AMENDMENT
Version: 18.0

## What failed

The V17 candidate was rejected because it did not meet the user's requirement for a complete, working, professional Results artifact. The implementation became a shortened reconstruction rather than a faithful complete experience. Its reduced scope created the appearance of a replacement/prototype instead of a finished MAXESS Results page.

## Root cause

The execution optimized for architectural cleanliness and static feature coverage before proving preservation of the complete user experience. In other words, it solved the wrong optimization problem:

`cleaner code + fewer lines + named components`

was incorrectly treated as evidence of:

`complete Results experience + functional parity + AAA quality`.

That is not acceptable.

## Permanent rules

1. Never equate fewer lines with better engineering.
2. Never shorten a large working artifact simply to make it easier to reason about.
3. Never replace a complete experience with a prototype while claiming reconstruction.
4. Never remove functionality merely because it is inconvenient to preserve.
5. When starting fresh, explicitly state that the new artifact is a fresh build and independently implement the full required surface.
6. A fresh build must still satisfy the complete Results directive: profile, authoritative MAXESS_RESULT, personalization, strongest signal, five dimensions, pattern, biggest lever, report hierarchy, Naya, Orb, all 18 Masters, responsive behavior, accessibility, performance, conversion, Groove compatibility, and complete self-contained deployment.
7. Static checks must include completeness and preservation evidence, not merely syntax and keyword presence.
8. A candidate is not acceptable if any visible section says or implies that MAXESS is "not ready" unless that state is a deliberate, production-safe data-loading error state with a clear recovery path. Demo/fixture language must never appear in the normal user experience.
9. Development fixtures must be isolated from the production presentation. They may be used for engineering verification but must not become the visible default copy.
10. The final candidate must be opened/re-fetched and inspected from top to bottom before handoff.
11. If the candidate looks like a prototype, dashboard skeleton, compressed demo, or partial rebuild, reject it and rebuild before handoff.
12. The human question remains: `Why is this not a 10?` Material answers require another build pass.

## Fresh-build strategy

V18 intentionally begins as a new self-contained artifact rather than another patch to the failed V17 candidate. It is a candidate only. It is not authoritative.

The approved baseline remains protected on `main`.

## Authority state

`MAXESS-RESULTS-FRESH-V18-GROOVE.html` = UPDATED EDITED FILE — NOT YET AUTHORITATIVE.

Only explicit human approval can promote V18 to authoritative status.
