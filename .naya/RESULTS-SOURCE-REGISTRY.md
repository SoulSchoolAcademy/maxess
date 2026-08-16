# MAXESS RESULTS — SOURCE REGISTRY

Status: AUTHORITATIVE CONTROL DOCUMENT
Version: 1.1
Updated: 2026-08-16

## PURPOSE

This registry is the single source-of-truth map for the MAXESS Results surface.

The repository contains many historical Results files. Their names are not authority. Their role is determined here.

## CURRENT AUTHORITATIVE ENGINEERING SOURCE

Repository: `SoulSchoolAcademy/maxess`

Branch: `main`

Current authoritative Results artifact:

`MAXESS-RESULTS-10-GROOVE.html`

Current baseline SHA:

`524e14a31df7da958adf8090c3220a26adea7056`

Public verification target:

`https://results.nayanet.xyz/`

## DEPLOYMENT STATUS

As of 2026-08-16, the public target is NOT in parity with the authoritative engineering artifact.

The public page currently exposes an older/different Results implementation, including different visible section structure and copy. Therefore:

**LIVE-VERIFIED = FALSE**

**DELIVERY STATUS = BLOCKED — DEPLOYMENT PARITY FAILURE**

GitHub acceptance is not deployment proof.

The actual deployment owner/source for `results.nayanet.xyz` still needs to be identified and connected to the authoritative Results artifact. Repository inspection indicates the target is Groove-hosted, but GitHub alone does not provide sufficient evidence of the external Groove publishing source or credentials.

## AUTHORITATIVE ARCHITECTURE

```text
MAXESS Assessment
      ↓
Result Contract
      ↓
MAXESS-RESULTS-10-GROOVE.html
      ↓
Groove deployment artifact / publisher
      ↓
https://results.nayanet.xyz/
      ↓
Independent live verification
```

`nayanetpagecode` is the preserved NayaNET foundation appended to the Results experience. It is not a competing Results source.

## FILE CLASSIFICATIONS

### AUTHORITATIVE SOURCE

- `MAXESS-RESULTS-10-GROOVE.html`

### DEPLOYMENT ARTIFACTS / MIRRORS

- `MAXESS-RESULTS-FINAL-GROOVE.html` — currently identical to the authoritative source; do not edit independently.
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

The authoritative Results artifact currently contains a deterministic development fixture so visual engineering can be exercised before the production Result Contract is wired.

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
6. Inspect the current authoritative artifact.
7. Record baseline SHA and relevant structural markers.
8. Map every material user requirement to an implementation location and proof method.
9. Modify only the authoritative engineering path.
10. Re-fetch the exact artifact.
11. Diff against the baseline.
12. Run deterministic QA and regression checks.
13. Reassemble the Groove/deployment artifact when required.
14. Verify the actual public target.
15. Run Oscar against the final experience.
16. Fix material findings.
17. Retest.
18. Deliver only when the evidence chain passes.

## ZERO-CHANGE RULE

If an implementation request produces no material change to the authoritative source, status is:

**BLOCKED — ZERO-CHANGE EXECUTION**

## DUPLICATE-SOURCE RULE

No new Results master may be created without:

- architectural justification;
- explicit classification;
- registry update;
- preservation assessment;
- verification;
- deployment parity confirmation when applicable.

## PUBLIC PARITY RULE

The public target is the human-facing truth for release verification.

If GitHub and the public target disagree:

**BLOCKED — DEPLOYMENT PARITY FAILURE**

## FINAL TEST

Another AI must be able to open this registry and answer, without guessing:

- Which Results file do I modify?
- Which files must I not modify?
- Where does the result data come from?
- What does the public target need to consume?
- How do I prove my change reached the human?

If any answer is ambiguous, the registry is not finished.
