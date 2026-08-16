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

## Deployment Verification Attempt — 2026-08-16

The live target `https://results.nayanet.xyz/` was fetched after the V14 merge. It is still serving the older Results experience and does not expose the V14 Personal Profile layer.

The authoritative `GROOVE-DEPLOYMENT-CONTRACT.md` was read before attempting further action. It explicitly establishes that the connected environment has **no authenticated Groove editor/publishing integration** and therefore cannot honestly perform the external publish stage from GitHub alone.

A repository/plugin capability check was also performed for Groove deployment; no connected Groove publishing plugin/integration is available.

## Exact Blocker

**BLOCKED — EXTERNAL GROOVE PUBLISH ACTION NOT CONNECTED**

This is not a source-code failure and not a reason to alter the Results implementation. The missing capability is authenticated access to the Groove page/editor that owns `results.nayanet.xyz`.

## Required Next Action

Identify and connect the real Groove deployment path:

1. Groove site/funnel owning `results.nayanet.xyz`.
2. Exact Groove page owning the route.
3. Exact page/section element containing the Results code.
4. Whether the page uses pasted code, a URL-loaded artifact, or another source.
5. Exact publish action.
6. Any cache/CDN behavior.

Then run the minimal deployment probe before publishing the complete V14 artifact.

## Current State

**GitHub: VERIFIED**

**Live: NOT VERIFIED**

**Release gate: BLOCKED ONLY BY EXTERNAL GROOVE PUBLISH ACCESS**
