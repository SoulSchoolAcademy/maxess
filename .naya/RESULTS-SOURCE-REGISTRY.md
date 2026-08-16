# MAXESS RESULTS — SOURCE REGISTRY

Status: AUTHORITATIVE CONTROL DOCUMENT
Updated: 2026-08-16

## PURPOSE

This registry exists to eliminate ambiguity between source files, previews, generated artifacts, Groove content, and the public Results experience.

## CURRENT AUTHORITATIVE RESULTS SOURCE

**Repository:** `SoulSchoolAcademy/maxess`

**Branch:** `main`

**Authoritative Results artifact currently designated by project memory:**

`MAXESS-RESULTS-10-GROOVE.html`

**Current file SHA:** `524e14a31df7da958adf8090c3220a26adea7056`

**Public verification target:**

`https://results.nayanet.xyz/`

## CRITICAL DEPLOYMENT FINDING — 2026-08-16

The public verification target has been documented as serving a materially different Results implementation from the authoritative GitHub artifact.

Therefore:

**GitHub source = authoritative engineering artifact.**

**Public URL = verification target, not an independent source of truth.**

The public experience is NOT considered live-verified until it demonstrably matches the authoritative artifact after publication.

## FILE CLASSIFICATION RULE

Files with names such as `FULL-BUILD`, `EXECUTABLE`, `PREVIEW`, `NORTH-STAR`, `10-10`, `9-0`, `CURRENT WORKING FILE`, `FINAL`, or similar are not authoritative merely because of their names.

Every candidate must be classified as one of:

- AUTHORITATIVE SOURCE
- GENERATED ARTIFACT
- GROOVE DEPLOYMENT ARTIFACT
- PREVIEW
- PROTOTYPE
- LEGACY
- SPECIFICATION
- BACKUP
- UNKNOWN

Unknown candidates must not be edited for a consequential release.

## REQUIRED EXECUTION BEHAVIOR

For a Results implementation request:

1. Read Naya Law.
2. Read this registry.
3. Fetch the authoritative source.
4. Record its current SHA/baseline.
5. Inspect its architecture and protected functionality.
6. Implement the requested delta in the authoritative path.
7. Re-fetch the exact written artifact.
8. Prove the requested delta exists.
9. Reassemble/build the actual Groove/public artifact when required.
10. Verify the public target.
11. Compare public output against the authoritative source.
12. Block delivery if parity fails.

## ZERO-CHANGE RULE

If a requested implementation produces no material change to the authoritative source or required deployment artifact, the task is automatically:

**BLOCKED — ZERO-CHANGE EXECUTION.**

## DUPLICATE FILE RULE

Do not create another competing Results master without an explicit architectural reason and an update to this registry.

A new candidate becomes authoritative only after:
- architectural justification;
- preservation assessment;
- explicit registry update;
- verification;
- deployment parity confirmation when applicable.

## CURRENT STATUS

Engineering source is identifiable.

Public deployment parity is a known unresolved issue and therefore live verification remains blocked until the deployment source is connected and confirmed.

## FINAL TEST

> Can another AI open this registry, identify exactly which Results artifact it is supposed to modify, prove that it changed, and determine whether the human-facing public experience actually received that change?

If not, this registry is incomplete and must be repaired before consequential Results work proceeds.
