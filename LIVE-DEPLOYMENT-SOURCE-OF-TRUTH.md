# LIVE RESULTS DEPLOYMENT — SOURCE OF TRUTH

## Current production model — 2026-08-17

### Authoritative production source

The single production Groove embed artifact is:

`MAXESS-RESULTS-AAA-GROOVE-EMBED.html`

on the repository default branch:

`main`

Current main baseline: `33537b05a8ec6bea65004ee7f7ed3d3b33b13f2e`

### Critical deployment fact

GitHub and Groove are NOT connected and must not be treated as connected.

GitHub is the engineering/source repository.
Groove is the production publishing environment.

The only valid deployment flow is:

1. Build and verify the artifact in GitHub.
2. Retrieve the complete `MAXESS-RESULTS-AAA-GROOVE-EMBED.html` from `main`.
3. Replace the existing MAXESS Results code/embed element in Groove.
4. Publish the Groove page.
5. Open `https://results.nayanet.xyz/`.
6. Verify the public page visibly matches the new artifact.

### Branch rule

Production work must be based on the current `main` branch. Candidate branches are not production unless they have been explicitly reconciled with current `main` and promoted.

The previous `maxess-results-v16-updated-edited` branch is not the production source. It diverged from `main` and must not be used as an implicit production baseline.

### Artifact rule

Do not assume similarly named files are interchangeable.

`MAXESS-RESULTS-10-GROOVE.html`
`MAXESS-RESULTS-V17-CLEAN-REBUILD-GROOVE.html`
`MAXESS-RESULTS-FINAL-GROOVE-EMBED.html`
`RESULTS PAGE CODE`
and other historical/candidate artifacts are not production source by default.

### Live gate

The public URL is not considered updated until the following visible fingerprint is confirmed after Groove publication:

- Naya introduction at the top.
- One intended primary Listen to Naya control.
- Real AI Score displayed inside the central orb.
- No competing standalone `AI Score 0` presentation.
- Exactly five mini dimension orbs.
- Existing report narrative remains intact.

`LIVE-VERIFIED` is true only after this public-page test passes.
