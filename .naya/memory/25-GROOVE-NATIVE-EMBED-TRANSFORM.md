# 25 — GROOVE-NATIVE EMBED TRANSFORM

## Purpose
Prevent standalone HTML documents and legacy hidden DOM from being copied into Groove embeds.

## Canonical rule
A Groove embed is a native HTML fragment, not a standalone webpage document.

The authoritative source page may contain:
- `<!doctype>`
- `<html>`
- `<head>`
- `<body>`
- legacy fallback/rollback DOM

Those must NOT be copied into the Groove embed artifact.

## Groove artifact architecture
Extract only the authoritative current experience:

1. Required component CSS.
2. Required current `<main>` / root markup.
3. Required controller/data JavaScript.
4. A small Groove preflight wrapper that forces full-bleed width and neutralizes container constraints.

Do not include:
- old hidden Results DOM;
- legacy iframes;
- old NayaNET page frames;
- standalone document shells;
- unused scripts or duplicated controllers.

## Verification gates
Every Groove-native Results fragment must prove:
- no `<!doctype>` tag;
- no document-level `<html>`, `<head>`, or `<body>` tag;
- no actual `<iframe>` tag;
- authoritative Results root exists;
- Result Contract marker exists;
- five current MAXESS dimensions exist;
- 18 Naya Master definitions exist;
- Naya experience exists;
- full-bleed wrapper exists;
- legacy Results root is absent;
- legacy NayaNET frame is absent;
- responsive and accessibility requirements remain in the extracted CSS/experience.

## Delivery law
The raw Groove-native artifact is the preferred copy/paste deliverable:
`MAXESS-RESULTS-GROOVE-EMBED.html`

The standalone page source remains available for development/reference but is NOT the default Groove paste artifact.

## Key lesson
A smaller Groove fragment is not incomplete when it is a deliberate extraction of the complete current experience. Completeness is proved by required architecture and behavior, not by preserving dead wrapper markup or inflating line count.
