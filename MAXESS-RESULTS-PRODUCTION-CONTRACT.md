# MAXESS RESULTS — PRODUCTION SOURCE CONTRACT

Status: ACTIVE
Canonical branch: `main`
Canonical manual Groove embed: `MAXESS-RESULTS-GROOVE-PRODUCTION.html`
Public page: `https://results.nayanet.xyz/`

## Non-negotiable deployment model

GitHub and Groove are NOT connected and must never be treated as connected.

GitHub is the engineering/source repository.
Groove is the production publishing environment.
Shawn manually copies the complete canonical HTML into the correct Groove Results code/embed element and publishes it.

A GitHub commit is NOT a deployment.
A GitHub workflow is NOT a deployment.
A successful source test is NOT a deployment.
Only the public Groove URL changing after the manual publish is a deployment.

## Single canonical artifact

For new Groove deployments use ONLY:

`MAXESS-RESULTS-GROOVE-PRODUCTION.html`

Do not select historical/candidate files merely because their names contain `FINAL`, `AAA`, `V17`, `V18`, `V19`, `GROOVE`, or `EMBED`.

The older Results artifacts remain in repository history for recovery/reference. They are not the active deployment target unless this contract is explicitly changed.

## Single production data source

`window.MAXESS_RESULT` is the production result source of truth.

The renderer must never fabricate a personalized production score, create a second scoring engine, or treat an unavailable result as score zero.

## Deployment fingerprint

A correct publication must visibly begin with:

- Naya / Naya, Your Guide
- Hi. I've looked at your results.
- This isn't your judgment. It's your map.
- one primary Listen to Naya control
- actual AI Score inside the central orb
- five mini capability orbs

If the public page still begins with the old Results hero, the canonical artifact has not been successfully published into the live Groove element.

## Change protocol

1. Modify only the canonical production artifact unless an architecture change is explicitly required.
2. Verify source structure and data binding.
3. Commit to `main`.
4. Give Shawn the exact canonical file link.
5. Shawn replaces the contents of the production Groove code/embed element; do not append the artifact underneath the old renderer.
6. Publish Groove.
7. Open `https://results.nayanet.xyz/` in a fresh browser/private window.
8. Confirm the deployment fingerprint above.
9. Only then perform visual/function/responsive QA.

## Failure rule

If the public page does not change, stop modifying presentation code. Diagnose the Groove element/public publishing path instead. Do not create another candidate renderer.
