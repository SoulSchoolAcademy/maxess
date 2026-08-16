# MAXESS RESULTS — SOURCE REGISTRY

Status: AUTHORITATIVE CONTROL DOCUMENT
Version: 2.0
Updated: 2026-08-16

## PURPOSE

This registry is the single source-of-truth map for the MAXESS Results surface AND the state machine governing Results artifacts.

The repository contains many historical Results files. Their names are not authority. Their role is determined here.

## CRITICAL STATE MODEL

There are two different concepts that MUST NEVER be conflated:

### APPROVED / AUTHORITATIVE BASELINE
The last Results artifact explicitly approved by Shawn Vibert, or the initial approved project baseline when no prior user approval exists.

### UPDATED EDITED FILE
The newly modified artifact produced by the current execution. It is the candidate upgrade being handed to Shawn for review.

The Updated Edited File is NOT authoritative merely because it is:

- newer;
- larger;
- committed;
- pushed to GitHub;
- statically verified;
- called FINAL, MASTER, 10/10, 10.10, AAA, CURRENT, NEW, UPDATED, V15, or similar;
- or successfully deployed.

Authority is a human approval state, not a filename or timestamp.

## HANDOFF RULE

Before approval, all Results implementation handoffs MUST be labeled:

> **UPDATED EDITED FILE — V<N> — NOT YET AUTHORITATIVE**

The review link must point to that exact version/commit.

Only after Shawn explicitly approves the candidate may it be promoted:

> **AUTHORITATIVE / APPROVED — V<N>**

The exact approved commit/hash is then recorded here as the new baseline.

## CURRENT APPROVED BASELINE

Repository: `SoulSchoolAcademy/maxess`

Branch: `main`

Current approved Results artifact:

`MAXESS-RESULTS-10-GROOVE.html`

Current presentation layer associated with the approved artifact:

`MAXESS-RESULTS-EXPERIENCE.js`

Current approved Results source SHA recorded before the V15 execution cycle:

`9036c27a58f1a8552ea86c6ce598883a3dc12bd7`

IMPORTANT: This registry entry identifies the approved baseline state. It must not be silently replaced merely because a later edit exists.

Public verification target:

`https://results.nayanet.xyz/`

## CURRENT EDIT STATE

As of this registry revision, no newly edited Results artifact is promoted to approved status by this governance change alone.

The previous V15 execution must NOT be treated as human-approved authority merely because it produced a commit or passed static gates.

Any next Results implementation must create an explicit:

`UPDATED EDITED FILE — V<N> — NOT YET AUTHORITATIVE`

state and hand off that exact artifact for human review.

## DEPLOYMENT STATUS

As of 2026-08-16, the public target is NOT in parity with the approved engineering artifact.

Therefore:

**LIVE-VERIFIED = FALSE**

**DELIVERY STATUS = BLOCKED — DEPLOYMENT PARITY FAILURE**

GitHub acceptance is not deployment proof.

The actual deployment owner/source for `results.nayanet.xyz` still needs to be identified and connected to the approved Results artifact. Repository inspection indicates the target is Groove-hosted, but GitHub alone does not provide sufficient evidence of the external Groove publishing source or credentials.

## AUTHORITATIVE ARCHITECTURE

```text
MAXESS Assessment
      ↓
Result Contract
      ↓
APPROVED / AUTHORITATIVE RESULTS BASELINE
      ↓
CURRENT UPDATED EDITED FILE
      ↓
Groove deployment artifact / publisher
      ↓
https://results.nayanet.xyz/
      ↓
Independent live verification
```

`nayanetpagecode` is the preserved NayaNET foundation appended to the Results experience. It is not a competing Results source.

The presentation layer is not a second scoring engine. It consumes `window.MAXESS_RESULT` and is responsible for the user-facing Results experience only.

## FILE CLASSIFICATIONS

### APPROVED / AUTHORITATIVE ENGINEERING SOURCE

- `MAXESS-RESULTS-10-GROOVE.html` — approved Results deployment source/foundation.
- `MAXESS-RESULTS-EXPERIENCE.js` — approved Results presentation layer associated with that source.

These labels describe the approved baseline state. During an active execution, the newly modified candidate must be labeled UPDATED EDITED FILE until human approval.

### DEPLOYMENT ARTIFACTS / MIRRORS

- `MAXESS-RESULTS-FINAL-GROOVE.html` — currently identical to the approved source; do not edit independently.
- `MAXESS-RESULTS-GROOVE-EMBED.html` — Groove-oriented deployment artifact.
- `MAXESS-RESULTS-FINAL-GROOVE-EMBED.html` — deployment artifact/mirror.
- `MAXESS-RESULTS-GROOVE-EMBED-9.95.html` — historical deployment artifact; not current.

### HISTORICAL / REFERENCE RESULTS

- `MAXESS-RESULTS-10-10-EXECUTABLE.html`
- `MAXESS-RESULTS-10-10-FULL-BUILD.html`
- `MAXESS-RESULTS-10-6-NORTH-STAR-FULL-READABLE.html`
- `MAXESS-RESULTS-10-6-NORTH-STAR-PREVIEW.html`
- `MAXESS-RESULTS-9-5-GROOVE.html`
- `MAXESS-RESULTS-9-5-COMPLETE-GROOVE.html`
- `MAXESS-RESULTS-9-0-FULL-GROOVE.html`
- `MAXESS-RESULTS-9-0-GROOVE-EMBED.html`

These are reference material only. New consequential work must not be written into them.

### LEGACY / SEPARATE RENDERER

- `results` — older standalone Results renderer. It has its own hard-coded development defaults and is not the current public Results source.
- `results-v5-prototype.html` — prototype.

### UPSTREAM ASSESSMENT FILES

- `CURRENT WORKING FILE` — assessment application/source.
- `RESULTS PAGE CODE` — assessment-side Results rendering logic that consumes `calculateResults()`.

These files are upstream of the Result Contract boundary. They are not the public Groove Results deployment source.

## DEVELOPMENT DATA RULE

The approved Results artifact may contain a deterministic development fixture so visual engineering can be exercised before the production Result Contract is wired.

That fixture MUST be explicitly marked as development-only and MUST NOT silently masquerade as production user data.

Production architecture remains:

`Assessment → Result Contract → Results renderer`

The Results renderer must not become a second scoring engine.

## REQUIRED EXECUTION

For every consequential Results implementation:

1. Read `NAYA-MASTER.md`.
2. Read `.naya/NAYA-GOVERNANCE.md`.
3. Read `.naya/NAYA-LAW.md`.
4. Read `.naya/00-UNDERSTANDING-FIRST.md`.
5. Read this registry and `.naya/REPOSITORY-OPERATING-MAP.md`.
6. Identify the APPROVED / AUTHORITATIVE BASELINE.
7. Freeze/record baseline SHA, hash, and relevant structural markers.
8. Create a uniquely identified UPDATED EDITED FILE state for the current execution.
9. Map every material user requirement to an implementation location and proof method.
10. Modify the working/edit path, preserving the approved baseline as a recovery point.
11. Re-fetch the exact UPDATED EDITED FILE.
12. Diff against the approved baseline.
13. Reject zero-change or materially insufficient changes.
14. Run deterministic QA and regression checks.
15. Reassemble the Groove/deployment artifact when required.
16. Verify the actual public target when release verification is requested.
17. Run Oscar against the candidate final experience.
18. Fix material findings.
19. Retest.
20. Hand off ONLY the UPDATED EDITED FILE for Shawn's review.
21. Promote to APPROVED / AUTHORITATIVE only after explicit human approval.
22. Record the exact approved commit/hash as the new baseline.

## ZERO-CHANGE RULE

If an implementation request produces no material change to the UPDATED EDITED FILE compared with the approved baseline, status is:

**BLOCKED — ZERO-CHANGE EXECUTION**

A new filename, marker, commit, workflow run, or regenerated download does not count as a material change.

## DUPLICATE-SOURCE RULE

No new Results master may be created without:

- architectural justification;
- explicit classification;
- registry update;
- preservation assessment;
- verification;
- deployment parity confirmation when applicable.

Versioned candidate files are permitted when they exist specifically to protect the approved baseline and make the Updated Edited File unambiguous. They are not automatically authoritative.

## PUBLIC PARITY RULE

The public target is the human-facing truth for release verification.

If GitHub and the public target disagree:

**BLOCKED — DEPLOYMENT PARITY FAILURE**

## AUTHORITY PROMOTION RULE

Promotion requires explicit human acceptance.

Valid promotion evidence is a clear user instruction such as:

- “Approved.”
- “Thumbs up.”
- “Make this the new authoritative version.”
- equivalent unambiguous approval.

Do not infer approval from silence, continued conversation, testing requests, or a request to keep working.

## FINAL TEST

Another AI must be able to open this registry and answer, without guessing:

- Which artifact is the approved baseline?
- Which artifact is the current Updated Edited File?
- Which file do I modify for the current execution?
- Which files must I not modify?
- Where does the result data come from?
- What does the public target need to consume?
- How do I prove my change reached the human?
- What exact event promotes a candidate to authority?

If any answer is ambiguous, the registry is not finished.
