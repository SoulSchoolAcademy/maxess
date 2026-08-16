# MAXESS RESULTS — SOURCE REGISTRY

Status: AUTHORITATIVE CONTROL DOCUMENT
Version: 1.3
Updated: 2026-08-16

## PURPOSE

This registry is the single source-of-truth map for the MAXESS Results surface.

The repository contains many historical Results files. Their names are not authority. Their role is determined here.

## CURRENT AUTHORITATIVE ENGINEERING SOURCE

Repository: `SoulSchoolAcademy/maxess`

Branch: `main`

Current authoritative Results artifact:

`MAXESS-RESULTS-10-GROOVE.html`

Current presentation layer:

`MAXESS-RESULTS-EXPERIENCE.js`

Current complete Groove delivery artifact:

`MAXESS-RESULTS-10.10-GROOVE-EMBED-COMPLETE.html`

The complete Groove artifact is the file Shawn copies into Groove. It is self-contained and MUST NOT require a second Results JavaScript file or a GitHub-hosted loader.

Public verification target:

`https://results.nayanet.xyz/`

## DEPLOYMENT STATUS

As of 2026-08-16, the public target is NOT in parity with the new complete Groove artifact.

Therefore:

**LIVE-VERIFIED = FALSE**

**DELIVERY STATUS = READY FOR GROOVE — LIVE PARITY NOT YET VERIFIED**

GitHub acceptance is not deployment proof.

## AUTHORITATIVE ARCHITECTURE

```text
MAXESS Assessment
      ↓
Result Contract
      ↓
MAXESS-RESULTS-10-GROOVE.html + MAXESS-RESULTS-EXPERIENCE.js
      ↓
COMPLETE GROOVE EMBED
      ↓
Groove deployment
      ↓
https://results.nayanet.xyz/
      ↓
Independent live verification
```

`nayanetpagecode` is the preserved NayaNET foundation. It is not a competing Results renderer.

The presentation layer is not a second scoring engine. It consumes `window.MAXESS_RESULT` and is responsible for the user-facing Results experience.

## FILE CLASSIFICATIONS

### AUTHORITATIVE SOURCE

- `MAXESS-RESULTS-10-GROOVE.html` — authoritative Results foundation.
- `MAXESS-RESULTS-EXPERIENCE.js` — authoritative presentation implementation.

### COMPLETE GROOVE DELIVERY

- `MAXESS-RESULTS-10.10-GROOVE-EMBED-COMPLETE.html` — **complete self-contained Groove artifact; preferred delivery file.**

### LEGACY / DEPLOYMENT MIRRORS

- `MAXESS-RESULTS-GROOVE-EMBED.html` — previously used Groove artifact; it contained only a bootstrap/loader and is NOT a valid complete delivery artifact under Naya Law 19.
- `MAXESS-RESULTS-FINAL-GROOVE-EMBED.html` — previous deployment artifact; do not use for new delivery unless independently verified as complete.
- `MAXESS-RESULTS-FINAL-GROOVE.html` — mirror of the older source.
- `MAXESS-RESULTS-GROOVE-EMBED-9.95.html` — historical artifact.

### HISTORICAL / REFERENCE RESULTS

- `MAXESS-RESULTS-10-10-EXECUTABLE.html`
- `MAXESS-RESULTS-10-10-FULL-BUILD.html`
- `MAXESS-RESULTS-10-6-NORTH-STAR-FULL-READABLE.html`
- `MAXESS-RESULTS-10-6-NORTH-STAR-PREVIEW.html`
- `MAXESS-RESULTS-9-5-GROOVE.html`
- `MAXESS-RESULTS-9-5-COMPLETE-GROOVE.html`
- `MAXESS-RESULTS-9-0-FULL-GROOVE.html`
- `MAXESS-RESULTS-9-0-GROOVE-EMBED.html`

These are reference material only.

### LEGACY / SEPARATE RENDERER

- `results` — older standalone Results renderer.
- `results-v5-prototype.html` — prototype.

### UPSTREAM ASSESSMENT FILES

- `CURRENT WORKING FILE`
- `RESULTS PAGE CODE`

These are upstream of the Result Contract boundary.

## COMPLETE EMBED RULE

The preferred Groove delivery is one complete file:

`MAXESS-RESULTS-10.10-GROOVE-EMBED-COMPLETE.html`

It must contain:

- markup;
- CSS;
- JavaScript behavior;
- result decoding/handoff;
- responsive behavior;
- accessibility behavior;
- requested Results sections;
- requested Naya interactions;
- no external GitHub Results renderer dependency.

A snippet, bootstrap, loader, or partial file is not acceptable delivery.

## DEVELOPMENT DATA RULE

The deterministic fixture inside the complete artifact is explicitly a preview fallback only. Production results must arrive through the real `window.MAXESS_RESULT` contract.

Production architecture remains:

`Assessment → Result Contract → Results renderer`

The Results renderer must not become a second scoring engine.

## DELIVERY TEST

Before a Groove link is delivered, verify:

1. The linked file is the complete artifact.
2. It does not load the Results renderer from GitHub.
3. It contains the requested experience.
4. It is materially more than a bootstrap/snippet.
5. It is the exact file intended for Groove.
6. The public target is separately checked after Groove publication.

If these cannot be proven, status is BLOCKED.
