# MAXESS — REPOSITORY OPERATING MAP

Status: AUTHORITATIVE CONTROL DOCUMENT
Version: 1.1
Updated: 2026-08-16

## PURPOSE

This is the fast operational map for Naya and any downstream AI working in the MAXESS repository.

The repository contains historical experiments, duplicate Results artifacts, assessment code, renderers, build scripts, release history, and deployment notes. Those files are valuable history, but they are not interchangeable.

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

Current deployment status:

**BLOCKED — EXTERNAL GROOVE EDITOR/PUBLISH SOURCE NOT CONNECTED TO THIS REPOSITORY**

The public target is demonstrably different from the authoritative GitHub artifact. GitHub can verify source bytes, but this environment has no connected Groove editor/publishing action and therefore cannot truthfully claim to have published into Groove.

## AUTHORITATIVE RESULTS PATH

```text
Assessment
  ↓
Result Contract
  ↓
MAXESS-RESULTS-10-GROOVE.html
  ↓
Canonical verification
  ↓
EXTERNAL GROOVE EDITOR / PUBLISH ACTION
  ↓
https://results.nayanet.xyz/
  ↓
Independent live verification
```

The Results page is not considered shipped until the external publish stage and the final live verification stage are proven.

## RESULTS FILE CLASSIFICATION

| Path | Classification | Rule |
| --- | --- | --- |
| `MAXESS-RESULTS-10-GROOVE.html` | AUTHORITATIVE SOURCE | Only authoritative Results implementation path for consequential visual/functional changes unless the registry is deliberately changed. |
| `MAXESS-RESULTS-FINAL-GROOVE.html` | DUPLICATE MIRROR | Do not edit independently. |
| `MAXESS-RESULTS-FINAL-GROOVE-EMBED.html` | GROOVE DEPLOYMENT ARTIFACT / DUPLICATE | Do not treat as a source of truth. |
| `MAXESS-RESULTS-GROOVE-EMBED.html` | GROOVE DEPLOYMENT ARTIFACT / DUPLICATE | Do not treat as a source of truth. |
| `MAXESS-RESULTS-GROOVE-EMBED-9.95.html` | LEGACY / DUPLICATE | Historical artifact; never use for new work. |
| `MAXESS-RESULTS-10-10-EXECUTABLE.html` | HISTORICAL BUILD ARTIFACT | Reference only. |
| `MAXESS-RESULTS-10-10-FULL-BUILD.html` | HISTORICAL BUILD ARTIFACT | Reference only. |
| `MAXESS-RESULTS-10-6-NORTH-STAR-FULL-READABLE.html` | REFERENCE / HISTORICAL | Reference only. |
| `MAXESS-RESULTS-10-6-NORTH-STAR-PREVIEW.html` | PREVIEW | Reference only. |
| `MAXESS-RESULTS-9-5-GROOVE.html` | LEGACY | Historical reference only. |
| `MAXESS-RESULTS-9-5-COMPLETE-GROOVE.html` | LEGACY | Historical reference only. |
| `MAXESS-RESULTS-9-0-FULL-GROOVE.html` | LEGACY | Historical reference only. |
| `MAXESS-RESULTS-9-0-GROOVE-EMBED.html` | LEGACY | Historical reference only. |
| `results` | LEGACY STANDALONE RENDERER | Separate older Results implementation. Do not edit for the current public release. |
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

## ACTIVE AUTOMATION RULE

Historical workflows have accumulated in this repository. They are not independent authorities.

The intended active Results automation set is now:

1. `.github/workflows/build-final-results-groove.yml` — read-only canonical source/structure/live-parity verification.
2. `.github/workflows/maxess-qa.yml` — general repository QA.
3. `.github/workflows/naya-law-results-pass.yml` — manual Naya Law audit.
4. `.github/workflows/harden-results-fixture-boundary.yml` — explicit fixture-boundary hardening.
5. `.github/workflows/patch-assessment-results-handoff.yml` — read-only assessment → Results contract audit.

Legacy mutation/release trigger workflows are being removed from the active path. No workflow is allowed to silently generate or publish a competing Results master.

Before using any remaining workflow:

1. identify what file it reads;
2. identify what file it writes;
3. identify whether it commits/pushes;
4. identify whether it produces a deployment artifact;
5. identify whether it actually publishes to the public target;
6. verify its current relationship to this map and the Results registry.

## EXTERNAL DEPLOYMENT RULE

GitHub is not Groove.

A successful GitHub write or GitHub Actions run proves repository state only.

The external Groove deployment must have an explicitly identified:

- Groove site/funnel;
- page;
- page/section code element;
- exact content source;
- publish action;
- live URL;
- cache behavior, if any.

If any of those are unknown, status is:

**BLOCKED — EXTERNAL SOURCE UNKNOWN**

The connected GitHub environment currently has no Groove editor/publisher integration, so it cannot perform or verify an authenticated Groove edit by itself.

## CHANGE RULE

For every consequential Results request:

1. Read governance.
2. Read this map and `.naya/RESULTS-SOURCE-REGISTRY.md`.
3. Baseline the authoritative source SHA.
4. Map every requested delta to a concrete implementation location.
5. Identify what must be preserved.
6. Modify only the authoritative engineering path.
7. Re-fetch and diff.
8. Run deterministic checks.
9. Assemble the exact external deployment payload if required.
10. Publish through the identified external source.
11. Fetch the actual public target.
12. Compare live markers and structure against the release artifact.
13. Run Oscar.
14. Fix material findings.
15. Retest.
16. Only then deliver.

## HARD BLOCKS

- Unknown Results source of truth.
- Unknown external deployment source.
- Zero material diff for an implementation request.
- Fake production result data.
- Public target not matching the release artifact.
- A legacy artifact being edited as if it were current.
- A workflow producing an unregistered competing master.
- Critical regression.

## OPERATING PRINCIPLE

> The repository is memory. The registry is the map. The authoritative artifact is the thing we change. The external publisher is the delivery mechanism. The public target is the thing the human judges.
