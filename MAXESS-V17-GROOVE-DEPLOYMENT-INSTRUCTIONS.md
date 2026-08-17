# MAXESS V17 — GROOVE DEPLOYMENT PACKAGE

## Why this package exists

The previous execution flow changed GitHub engineering artifacts but did not change the live Groove page. That is a deployment-source failure, not a design failure.

V17 therefore uses a different rule:

**REPLACE THE GROOVE RESULTS CODE WITH ONE AUTHORITATIVE RENDERER. DO NOT APPEND ANOTHER PRESENTATION PATCH.**

## Authoritative payload

`MAXESS-RESULTS-V17-FINAL-GROOVE-PAYLOAD.html`

## Required Groove action

1. Open the Groove page that owns `results.nayanet.xyz`.
2. Locate the existing MAXESS Results custom-code element.
3. Replace the existing Results HTML/code in that element with the contents of `MAXESS-RESULTS-V17-FINAL-GROOVE-PAYLOAD.html`.
4. Do not append it after the old Results renderer.
5. Do not keep the old hero renderer active beside it.
6. Publish the Groove page.
7. Open `https://results.nayanet.xyz/` in a fresh/private browser window.
8. Confirm the public page changed before evaluating visual details.

## V17 release invariants

- One Results renderer.
- One primary Naya introduction.
- One primary Listen to Naya control.
- Naya portrait at the top.
- Real `window.MAXESS_RESULT` is authoritative.
- No fabricated production score.
- Actual score appears inside the main orb.
- Exactly five active mini-orbs.
- Five dimensions are data-driven.
- All 18 AI pathways are present.
- No duplicated V18/V19/V19B presentation layers.
- No horizontal overflow.
- Reduced-motion support.
- Honest empty state when a result is unavailable.

## Demo preview

Use `?fixture=demo` only for visual QA. Production must supply `window.MAXESS_RESULT` or the encoded `result` query payload.

## Zero-change gate

If the public Groove page still shows the old opening — `Your AI capability has a shape.` — the new payload has not been published. Do not diagnose that as a CSS/JavaScript failure. The deployment action has not occurred.

## Final proof

The release is successful only when the public URL visibly shows:

Naya + portrait + Listen to Naya
→ actual AI score inside the main orb
→ five mini-orbs
→ personal map
→ five dimensions
→ strengths / leverage
→ 18 pathways
→ next actions
→ Naya ending

GitHub success alone is not live success.
