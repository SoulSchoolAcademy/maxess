# 24 — GROOVE DEPLOYMENT & DELIVERY LAW

Status: AUTHORITATIVE
Scope: All current NayaNET / MAXESS web builds intended for Shawn's current public publishing workflow.

## 1. CORE RULE

**GitHub is the source-control, memory, storage, inspection, versioning, and delivery-link system. It is NOT the current deployment platform.**

For the current workflow, public pages are deployed through **Groove.cm**, normally by copying the complete self-contained HTML/JS/CSS artifact into Groove's embed/code environment.

Do not assume GitHub Pages, Vercel, Netlify, or another hosting service is the deployment destination unless Shawn explicitly changes this law.

## 2. REQUIRED DELIVERY FORMAT

When Shawn asks for a finished Groove page, the final deliverable must be:

1. A complete self-contained Groove-compatible embed/code artifact.
2. Stored in GitHub for version control and retrieval.
3. Provided to Shawn through a **raw GitHub link** whenever practical so he can open/copy the exact source in a code-friendly format.
4. Optimized for Groove.cm's actual embed environment.
5. Ready to paste into Groove without requiring Shawn to reconstruct files, merge snippets, install packages, run a build, or deploy another service.

Preferred response format:

**RAW GITHUB SOURCE:** <raw GitHub URL>

Do not substitute a hosted deployment URL for the raw source link when the requested deliverable is Groove embed code.

## 3. WHAT GITHUB IS FOR

Use GitHub to:

- store authoritative source files;
- preserve working versions;
- maintain Naya memory and doctrine;
- inspect current source;
- compare versions and diffs;
- run source-level QA and release gates;
- preserve deployment-ready artifacts;
- provide Shawn a raw copy/paste delivery link.

GitHub is the project's durable technical memory and source-of-truth archive.

## 4. WHAT GITHUB IS NOT FOR

Do not treat a successful GitHub commit or GitHub Actions run as proof that a Groove page is publicly deployed.

Do not automatically create or rely on Vercel/Netlify/GitHub Pages deployment merely because it is technically convenient.

Do not move a Groove task onto another hosting platform without explicit authorization.

## 5. GROOVE-FIRST BUILD RULE

For Groove work, design the artifact around the actual embed environment from the beginning.

Assume:

- one self-contained HTML document where practical;
- inline CSS and JavaScript when needed;
- no build step for Shawn;
- no dependency on a separate frontend server;
- no iframe architecture unless explicitly requested;
- no external app shell merely to make the page work;
- graceful handling of browser limitations;
- responsive desktop/mobile behavior inside Groove;
- no assumptions about control over the parent page beyond what the embed actually provides.

## 6. SOURCE → DELIVERY PIPELINE

The authoritative flow is:

**CURRENT SOURCE → INSPECT → PRESERVE → BUILD → QA → GROOVE-COMPATIBILITY CHECK → COMMIT TO GITHUB → RE-FETCH RAW SOURCE → VERIFY → SEND RAW GITHUB LINK → SHAWN PASTES INTO GROOVE → LIVE HUMAN TEST**

The live Groove page is the final deployment environment.

## 7. RESULTS-SPECIFIC RULE

For MAXESS Results:

**MAXESS Assessment → Result Contract → Standalone Results HTML → Groove embed → NayaNET destination/continuation**

The Results page itself must remain a standalone flowing experience.

Do not silently combine the Results page with a NayaNET page or place it inside an iframe merely because a legacy workflow did so.

The bottom NayaNET/video/CTA experience belongs in the intended final sequence, but it must be integrated directly into the source when the specification calls for a single Groove page—not nested as an external iframe.

## 8. DEPLOYMENT STATE DISCIPLINE

Always distinguish:

**SOURCE READY** — GitHub artifact is complete and verified.

**GROOVE READY** — artifact has been checked for Groove compatibility and is ready to paste.

**GROOVE DEPLOYED** — Shawn or an authorized operator has pasted/published it in Groove.

**LIVE VERIFIED** — the deployed Groove URL has been opened and the actual rendered behavior has been tested.

Never claim GROOVE DEPLOYED or LIVE VERIFIED from a GitHub Actions success alone.

## 9. WHEN A LIVE URL DOES NOT MATCH THE SOURCE

Do not immediately rewrite the page.

First trace:

1. Is the GitHub source correct?
2. Is the raw file correct?
3. Did the correct artifact reach Shawn?
4. Did Groove receive the correct artifact?
5. Is the Groove page using an old embed/code block?
6. Is there caching?
7. Is the URL pointing to the intended Groove page?
8. Is another embedded layer or iframe masking the new source?

Fix the actual handoff/deployment failure before modifying good source code.

## 10. MASTER MEMORY RULE

This deployment law overrides stale assumptions that another hosting platform is the default.

If a future Naya session starts to reach for Vercel or another deployment provider for a Groove task, Naya should stop and check this document first.

Ask only if the current user explicitly wants to change the deployment strategy.

## 11. FINAL GROOVE RELEASE GATE

Do not deliver the final Groove code unless:

- required functionality is present;
- source is complete;
- Groove compatibility has been checked;
- no iframe is present unless explicitly required;
- mobile and desktop CSS are included;
- essential assets are correctly referenced or embedded;
- no required package/build step exists for Shawn;
- the file is the intended current version;
- the raw GitHub artifact has been re-fetched and verified after the final write;
- release status is honestly labeled.

## 12. COMMUNICATION RULE

For a finished Groove build, lead with the actionable deliverable, not deployment theory:

**NAYA MASTER / GROOVE READY**

**RAW SOURCE:** <raw GitHub URL>

Then provide the concise status and any verified limitation.

Do not send Shawn an ordinary GitHub webpage URL when a raw source link is requested.

Do not send fragments when a complete embed is required.

## 13. MEMORY LESSON

The project has previously lost context by confusing:

**source storage** with **deployment**.

This file exists specifically to prevent that regression.

**GitHub stores and delivers the code. Groove deploys the code.**

That distinction is now a permanent NayaNET law unless Shawn explicitly changes it.
