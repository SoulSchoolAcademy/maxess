# MAXESS AAA DELIVERY MANIFEST — PRODUCTION SOURCE LOCK

Status: ACTIVE
Date: 2026-08-17

## Single authoritative Groove embed

- Production repository: `SoulSchoolAcademy/maxess`
- Production branch: `main`
- Production embed artifact: `MAXESS-RESULTS-AAA-GROOVE-EMBED.html`
- Main baseline: `33537b05a8ec6bea65004ee7f7ed3d3b33b13f2e`
- Production data boundary: `window.MAXESS_RESULT`

## Explicit deployment model

GitHub and Groove are NOT connected.

GitHub is the engineering/source repository only.
Groove is the production publishing environment.
The production workflow is manual:

GitHub `main`
→ retrieve `MAXESS-RESULTS-AAA-GROOVE-EMBED.html`
→ replace the existing MAXESS Results Groove code/embed element
→ publish Groove
→ open `https://results.nayanet.xyz/`
→ visually verify the public result.

No GitHub workflow, commit, branch, or trigger is considered a Groove deployment.

## Source-of-truth law

Do not use `MAXESS-RESULTS-10-GROOVE.html`, `MAXESS-RESULTS-V17-CLEAN-REBUILD-GROOVE.html`, `MAXESS-RESULTS-FINAL-GROOVE-EMBED.html`, `RESULTS PAGE CODE`, or any other historical/candidate artifact as the production embed unless this manifest is explicitly changed first.

Historical/candidate files may be used for research, comparison, or recovery only.

## Branch law

All production candidate work must begin from `main` or be explicitly reconciled with the current `main` commit before being called production-ready.

A stale/diverged execution branch is never production source by implication.

## Live verification law

`LIVE-VERIFIED` is false until the public Groove URL visibly matches the artifact after manual Groove publication.

A GitHub commit is not a deployment.
A successful GitHub workflow is not a deployment.
A generated HTML file is not a deployment.
Only the published Groove page is the live product.
