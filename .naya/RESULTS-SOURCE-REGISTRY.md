# MAXESS RESULTS — SOURCE REGISTRY

Status: AUTHORITATIVE CONTROL DOCUMENT
Version: 2.2
Updated: 2026-08-16

## PURPOSE

This registry is the single source-of-truth map for the MAXESS Results surface AND the state machine governing Results artifacts.

The repository contains many historical Results files. Their names are not authority. Their role is determined here.

## CRITICAL STATE MODEL

### APPROVED / AUTHORITATIVE BASELINE
The last Results artifact explicitly approved by Shawn Vibert, or the initial approved project baseline when no prior user approval exists.

### UPDATED EDITED FILE
The newly modified artifact produced by the current execution. It is the candidate upgrade being handed to Shawn for review.

The Updated Edited File is NOT authoritative merely because it is newer, larger, committed, pushed, statically verified, called FINAL/MASTER/AAA, or successfully deployed.

## CURRENT APPROVED BASELINE

Repository: `SoulSchoolAcademy/maxess`

Branch: `main`

Current approved Results artifact:

`MAXESS-RESULTS-10-GROOVE.html`

Current presentation layer associated with the approved artifact:

`MAXESS-RESULTS-EXPERIENCE.js`

Current approved Results source SHA:

`9036c27a58f1a8552ea86c6ce598883a3dc12bd7`

This remains the recovery/approval baseline until Shawn explicitly approves a candidate.

## CURRENT EDIT STATE

**UPDATED EDITED FILE — V16 — NOT YET AUTHORITATIVE**

Candidate artifact:

`MAXESS-RESULTS-NEW-GROOVE.html`

Branch:

`feat/maxess-results-new-experience`

Candidate commit:

`56eae9cf22cb6af1dc56689492f012dcf7c5c6e7`

Candidate purpose: a new self-contained Groove-ready Results experience using the real `window.MAXESS_RESULT` boundary, the strongest verified MAXESS/NayaNET presentation patterns, and the approved Naya assets from commit `362cfa156428a8cb5d2aa01ebd1561ab65bcf477`.

The candidate is NOT live and NOT authoritative.

## DEPLOYMENT STATUS

Public target:

`https://results.nayanet.xyz/`

**LIVE-VERIFIED = FALSE**

The external Groove publishing channel is not authenticated in this environment. GitHub changes are not deployment proof.

## ARCHITECTURE

```text
MAXESS Assessment
      ↓
Result Contract
      ↓
window.MAXESS_RESULT
      ↓
APPROVED BASELINE / V16 WORKING CANDIDATE
      ↓
Groove deployment artifact / publisher
      ↓
https://results.nayanet.xyz/
      ↓
Independent live verification
      ↓
Explicit human approval
```

`nayanetpagecode` is preserved foundation/reference material, not a competing Results scoring source.

## FILE CLASSIFICATIONS

### APPROVED / AUTHORITATIVE

- `MAXESS-RESULTS-10-GROOVE.html`
- `MAXESS-RESULTS-EXPERIENCE.js`

### UPDATED EDITED FILE — V16 — NOT YET AUTHORITATIVE

- `MAXESS-RESULTS-NEW-GROOVE.html`

### DEPLOYMENT ARTIFACTS / MIRRORS

- `MAXESS-RESULTS-FINAL-GROOVE.html`
- `MAXESS-RESULTS-GROOVE-EMBED.html`
- `MAXESS-RESULTS-FINAL-GROOVE-EMBED.html`
- `MAXESS-RESULTS-GROOVE-EMBED-9.95.html`

Do not edit these independently unless the release architecture explicitly requires reassembly.

### HISTORICAL / REFERENCE

- `MAXESS-RESULTS-10-10-EXECUTABLE.html`
- `MAXESS-RESULTS-10-10-FULL-BUILD.html`
- `MAXESS-RESULTS-10-6-NORTH-STAR-FULL-READABLE.html`
- `MAXESS-RESULTS-10-6-NORTH-STAR-PREVIEW.html`
- `MAXESS-RESULTS-9-5-GROOVE.html`
- `MAXESS-RESULTS-9-5-COMPLETE-GROOVE.html`
- `MAXESS-RESULTS-9-0-FULL-GROOVE.html`
- `MAXESS-RESULTS-9-0-GROOVE-EMBED.html`

### UPSTREAM ASSESSMENT

- `CURRENT WORKING FILE`
- `RESULTS PAGE CODE`

These remain upstream of the Results Contract boundary.

## DEVELOPMENT DATA RULE

Development fixture data may exist only behind explicit developer opt-in such as `?fixture=demo`.

Production architecture remains:

`Assessment → Result Contract → Results renderer`

The Results renderer must not become a second scoring engine.

## REQUIRED EXECUTION

Every consequential Results implementation must:

1. Read Naya governance and V16 Results instructions.
2. Identify the approved baseline.
3. Freeze the baseline as recovery state.
4. Create an explicit Updated Edited File state.
5. Map requirements to implementation and verification.
6. Preserve working functionality and real data contracts.
7. Re-fetch the exact edited artifact.
8. Diff against the approved baseline.
9. Reject zero-change or materially insufficient work.
10. Run deterministic QA and regression checks.
11. Reassemble the real Groove artifact when promotion is authorized.
12. Verify the public target for any live-release claim.
13. Run adversarial Oscar review.
14. Fix material findings and retest.
15. Hand off only the Updated Edited File for human review.
16. Promote to authority only after explicit human approval.

## AUTHORITY PROMOTION RULE

Valid promotion requires clear human approval such as:

- “Approved.”
- “Thumbs up.”
- “Make this the new authoritative version.”

Do not infer approval from silence, continued work, or testing.

## ZERO-CHANGE RULE

If an implementation request produces no material change compared with the approved baseline:

**BLOCKED — ZERO-CHANGE EXECUTION**

## PUBLIC PARITY RULE

If GitHub and the public target disagree:

**BLOCKED — DEPLOYMENT PARITY FAILURE**

## FINAL TEST

Another AI must be able to determine without guessing:

- the approved baseline;
- the current Updated Edited File;
- where real result data comes from;
- which files must not be modified;
- how Groove consumes the artifact;
- how live parity is proven;
- what event promotes the candidate to authority.
