# Smart Note — MAXESS Results V14 Personalization

**Date:** 2026-08-16
**Project:** MAXESS Results
**Protocol:** Digital Codex / Naya Law / Scorecarding Master Key

## Lesson

A MAXESS Results page must be treated as a **personal profile system**, not merely a score-report page. The score is one signal inside a larger identity-and-capability model.

## Permanent Rule

Never invent personal information. Personalization must consume only authoritative Result Contract data and preserve the score as a separate authoritative value.

## Architecture Pattern

`window.MAXESS_RESULT` → `window.MAXESS_PROFILE` → personalized presentation → downstream Naya/personalization components.

The profile layer should support, when actually supplied by the Result Contract:

- name / display name
- role / profession
- goal / objective
- experience level
- organization / company
- location
- bio / about
- overall score
- dimension scores
- strongest signal
- biggest lever

## Execution Learning

1. Read the authoritative artifact before changing anything.
2. Preserve the existing Results architecture.
3. Add personalization as a layer rather than replacing working systems.
4. Make the personalization contract explicit and consumable by downstream systems.
5. Validate that the artifact materially changed.
6. Verify the live URL separately; GitHub implementation is not live verification.
7. Never say the live result is updated until the public URL visibly matches.

## V14 Result

The authoritative `MAXESS-RESULTS-10-GROOVE.html` was materially modified and merged to `main` with a dedicated V14 personalization layer. GitHub Actions validated the mutation and the merged artifact was re-fetched and confirmed to contain the V14 marker.

## Remaining Gate

The public Groove-hosted Results URL is still serving a different live artifact. V14 therefore remains **GitHub-verified / NOT LIVE-VERIFIED** until the Groove deployment path consumes the new authoritative artifact and the public URL passes the live gate.
