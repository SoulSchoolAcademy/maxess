# MAXESS — REPOSITORY OPERATING MAP

Status: AUTHORITATIVE CONTROL DOCUMENT
Version: 1.0
Updated: 2026-08-16

## PURPOSE

This document is the fast operational map for Naya and any downstream AI working in the MAXESS repository.

The repository contains historical experiments, duplicate artifacts, assessment code, Results renderers, build scripts, release triggers, and deployment notes. Those files are valuable history, but they are not interchangeable.

The rule is simple:

> One task → one authoritative path → one proof chain.

## CURRENT PRODUCT BOUNDARY

### MAXESS Assessment

The assessment collects responses and owns scoring/state.

Current working assessment artifact:

`CURRENT WORKING FILE`

Assessment/result rendering source used by the assessment project:

`RESULTS PAGE CODE`

These files are upstream assessment work. They are NOT the public MAXESS Results deployment source.

### MAXESS Results

The Results experience consumes a Result Contract and renders the user's result. It must not become a second scoring engine.

Current authoritative engineering artifact:

`MAXESS-RESULTS-10-GROOVE.html`

Public verification target:

`https://results.nayanet.xyz/`

Deployment status as of 2026-08-16:

**BLOCKED — DEPLOYMENT PARITY UNKNOWN / FAILED**

The public target is currently demonstrably different from the authoritative GitHub artifact.

## AUTHORITATIVE RESULTS PATH

```text
Assessment
  ↓
Result Contract
  ↓
MAXESS-RESULTS-10-GROOVE.html
  ↓
Groove deployment artifact / publisher
  ↓
https://results.nayanet.xyz/
  ↓
Live verification
```

The Results page is not considered shipped until the final two stages are proven.

## RESULTS FILE CLASSIFICATION

| Path | Classification | Rule |
| --- | --- | --- |
| `MAXESS-RESULTS-10-GROOVE.html` | AUTHORITATIVE SOURCE | Only authoritative Results implementation path for consequential visual/functional changes unless registry is deliberately changed. |
| `MAXESS-RESULTS-FINAL-GROOVE.html` | DUPLICATE MIRROR | Currently identical to the authoritative artifact. Do not edit independently. |
| `MAXESS-RESULTS-FINAL-GROOVE-EMBED.html` | GROOVE DEPLOYMENT ARTIFACT / DUPLICATE | Deployment-oriented artifact. Must not become a competing source. |
| `MAXESS-RESULTS-GROOVE-EMBED.html` | GROOVE DEPLOYMENT ARTIFACT / DUPLICATE | Keep aligned with the authoritative source when a deployment package is required. |
| `MAXESS-RESULTS-GROOVE-EMBED-9.95.html` | LEGACY / DUPLICATE | Historical artifact; never use for new work. |
| `MAXESS-RESULTS-10-10-EXECUTABLE.html` | HISTORICAL BUILD ARTIFACT | Reference only. Never edit for current release work. |
| `MAXESS-RESULTS-10-10-FULL-BUILD.html` | HISTORICAL BUILD ARTIFACT | Reference only. Never edit for current release work. |
| `MAXESS-RESULTS-10-6-NORTH-STAR-FULL-READABLE.html` | REFERENCE / HISTORICAL | Reference only. |
| `MAXESS-RESULTS-10-6-NORTH-STAR-PREVIEW.html` | PREVIEW | Reference only. |
| `MAXESS-RESULTS-9-5-GROOVE.html` | LEGACY | Historical reference only. |
| `MAXESS-RESULTS-9-5-COMPLETE-GROOVE.html` | LEGACY | Historical reference only. |
| `MAXESS-RESULTS-9-0-FULL-GROOVE.html` | LEGACY | Historical reference only. |
| `MAXESS-RESULTS-9-0-GROOVE-EMBED.html` | LEGACY | Historical reference only. |
| `results` | LEGACY STANDALONE RENDERER | Separate older Results implementation. Do not edit for the current public Results release. |
| `results-v5-prototype.html` | PROTOTYPE | Reference only. |
| `RESULTS PAGE CODE` | UPSTREAM ASSESSMENT RESULT VIEW | Not the public Results deployment source. |
| `CURRENT WORKING FILE` | UPSTREAM ASSESSMENT | Not the public Results deployment source. |

## FOUNDATION RULE

`nayanetpagecode` is the preserved NayaNET foundation appended to the Results experience.

It supplies validated video, button/icon, CTA, membership, responsive, accessibility, and interaction patterns.

Do not recreate weaker substitutes when the real Page Code can be reused.

## DATA RULE

Development fixtures may exist for deterministic visual development, but they must be explicitly marked as fixtures.

Production Results must receive real Result Contract data.

Never use a fake score, fake personality, fake status, or fake user result as a silent production fallback.

## WORKFLOW RULE

The repository may contain historical GitHub Actions workflows. A workflow name is not proof of the current deployment path.

Before using an action:

1. identify what file it reads;
2. identify what file it writes;
3. identify whether it commits/pushes;
4. identify whether it produces a deployment artifact;
5. identify whether it actually publishes to the public target;
6. verify its current relationship to the registry.

No workflow may silently create a new competing Results source.

## CHANGE RULE

For a Results request:

1. Read governance.
2. Read this map and `.naya/RESULTS-SOURCE-REGISTRY.md`.
3. Baseline the authoritative source SHA.
4. Map the requested delta to concrete locations.
5. Modify only the authoritative path.
6. Re-fetch and diff.
7. Run deterministic checks.
8. Build/reassemble the actual Groove artifact when applicable.
9. Verify the public target.
10. Run Oscar.
11. Fix material findings.
12. Retest.
13. Only then deliver.

## HARD BLOCKS

- Unknown Results source of truth.
- Zero material diff for an implementation request.
- Fake production result data.
- Public target not matching the release artifact.
- A legacy artifact being edited as if it were current.
- A workflow producing an unregistered competing master.
- Critical regression.

## OPERATING PRINCIPLE

> The repository is memory. The registry is the map. The authoritative artifact is the thing we change. The public target is the thing the human judges.
