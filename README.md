# MAXESS

MAXESS is the AI Mastery assessment and Results system.

## Start here

Before changing the project, read:

1. `.naya/NAYA-MASTER.md` or `NAYA-MASTER.md` when invoking the Master operating context.
2. `.naya/NAYA-GOVERNANCE.md`
3. `.naya/NAYA-LAW.md`
4. `.naya/REPOSITORY-OPERATING-MAP.md`
5. `.naya/RESULTS-SOURCE-REGISTRY.md` for Results work

## Current Results source of truth

`MAXESS-RESULTS-10-GROOVE.html`

Public verification target:

`https://results.nayanet.xyz/`

The public target is currently blocked from release verification because it does not yet demonstrate parity with the authoritative GitHub artifact.

## Architecture

```text
Assessment
  → Result Contract
  → Results renderer
  → Groove deployment
  → Public Results URL
  → Live verification
```

The assessment owns response collection and scoring. Results owns presentation and interpretation. Results must not create a second scoring engine.

## Important rule

The repository contains historical builds, previews, prototypes, deployment artifacts, and duplicate files. A filename containing `FINAL`, `MASTER`, `10/10`, `FULL BUILD`, or similar language does not make a file authoritative.

Use the registry and operating map to determine the correct path.

## Working standard

Understand first. Preserve what works. Change the authoritative path. Prove the change. Verify the live outcome. If the evidence is missing, it is not done.
