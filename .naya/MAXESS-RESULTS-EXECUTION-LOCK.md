# MAXESS RESULTS — EXECUTION LOCK

Status: ACTIVE
Date: 2026-08-16

## Purpose

This lock exists because the Results release path previously violated Naya Law by replacing the complete readable Groove artifact with a tiny external-script loader.

That failure class is now explicitly prohibited.

## HARD RULE

For MAXESS Results:

> **A complete requested Groove embed means the complete working Results implementation must be contained in the delivered embed artifact.**

Never substitute the complete artifact with:

- a loader;
- a bootstrap that fetches the renderer from GitHub;
- a 30–100 line wrapper around another Results file;
- a minified replacement when the authoritative source is a readable full artifact;
- a mock;
- a demo-only implementation;
- a partial excerpt.

## SOURCE PRESERVATION

The authoritative readable Results artifact is:

`MAXESS-RESULTS-10-GROOVE.html`

The artifact must preserve the existing complete implementation and be modified in place for consequential Results upgrades.

## PRODUCTION DATA

`window.MAXESS_RESULT` is authoritative.

A development fixture may exist only behind an explicit development flag such as `?fixture=demo`.

Production must never silently manufacture a result.

## RELEASE GATE

Before a Groove link is delivered, verify all of the following:

1. The link points to the complete HTML artifact.
2. The artifact is materially larger than a loader/wrapper.
3. The artifact contains the Results markup, styles, and behavior required for the experience.
4. It does not dynamically fetch the primary Results renderer from GitHub at runtime.
5. `window.MAXESS_RESULT` remains the production data boundary.
6. Existing video, NayaNET foundation, CTA architecture, and responsive behavior remain present.
7. The requested AAA changes are actually present in the artifact.
8. The artifact is re-fetched after the final write.
9. The artifact is independently inspected before being presented to Shawn.
10. If live deployment cannot be verified, status must be `LIVE — UNVERIFIED`.

## INCIDENT SAFEGUARD

If a future execution produces a tiny wrapper where a complete artifact was required:

**STOP → REVERT → RESTORE THE COMPLETE ARTIFACT → INSPECT → VERIFY → ONLY THEN CONTINUE.**

Do not ask Shawn to paste or test a known-invalid replacement.

## OPERATING STANDARD

**READ → MAP → FREEZE → MODIFY IN PLACE → REASSEMBLE → REFETCH → DIFF → TEST → OSCAR → LIVE-CHECK → DELIVER THE COMPLETE ARTIFACT.**
