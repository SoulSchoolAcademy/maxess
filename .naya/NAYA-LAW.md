# NAYA LAW — EXECUTION INTEGRITY STANDARD

Status: AUTHORITATIVE PROJECT LAW
Version: 2.1
Scope: Every consequential AI execution in this repository, especially changes requested by Shawn Vibert.

## PURPOSE

Naya Law defines the non-negotiable rules. The Naya Digital Codex defines the operational method used to obey those rules.

The law exists to eliminate recurring failures in which an AI:

- understands a request but does not execute it;
- changes the wrong file;
- changes a secondary artifact while the real product remains unchanged;
- produces a tiny fragment instead of the requested complete implementation;
- reports work that did not materially happen;
- loses or regresses previous work;
- overwrites a stronger version with an older version;
- creates a preview that is not the deployed product;
- writes successfully to GitHub but fails to produce a user-visible result;
- stops after partial implementation;
- silently changes scope;
- or repeatedly claims success without independent proof.

The objective is:

> **NO FALSE EXECUTION. NO WRONG-SOURCE EXECUTION. NO ZERO-CHANGE EXECUTION. NO PARTIAL-DONE EXECUTION. NO REGRESSION. NO UNVERIFIED DONE.**

Naya Law is an engineering control system, not a prompt suggestion.

---

# ACTIVATION

The human may activate this law with:

> **Naya Master on. Naya Law activated.**

Equivalent governance trigger:

> **GO — MASTER NAYA**

Activation makes every mandatory gate below binding. It never authorizes bypassing a gate.

---

# THE ABSOLUTE EXECUTION CONTRACT

Every consequential implementation must answer these questions BEFORE modification:

1. WHAT exactly am I being asked to change?
2. WHERE exactly does the real implementation live?
3. WHAT must remain unchanged?
4. WHAT exact files/artifacts will change?
5. HOW will I prove each requested change happened?
6. HOW will I prove previous functionality was preserved?
7. HOW will I prove the user-facing product changed?
8. WHAT will block me from falsely declaring success?

If any answer is unknown, the correct state is:

# BLOCKED — DO NOT GUESS.

---

# DIGITAL CODEX RELATIONSHIP

Naya Law is the constitutional layer.

`.naya/NAYA-DIGITAL-CODEX-v2.md` is the canonical operational layer.

The relationship is:

**LAW = WHAT MAY NEVER BE VIOLATED.**

**CODEX = HOW THE LAW IS EXECUTED AND PROVEN.**

Project-specific instruction sets define what the particular product should become.
Execution locks define the state of the current task.
Project memory preserves durable knowledge.

The Codex is mandatory for consequential work governed by this law.

---

# LAW 1 — READ BEFORE ACTION

Before consequential work, read:

- applicable repository governance;
- Naya Law;
- Digital Codex;
- project-specific instruction sets;
- source-of-truth registry or equivalent authority map;
- relevant project memory/specification;
- current implementation;
- relevant deployment configuration.

Do not begin implementation from the user's prose alone when repository context exists.

---

# LAW 2 — CREATE AN EXECUTION ID

Every implementation receives a unique execution identifier.

For iterative work this MUST include the iteration number, for example:

**MAXESS RESULTS — V14**

The execution record must identify:

- iteration number;
- date/time;
- requested outcome;
- authoritative source;
- deployment target;
- baseline commit;
- final commit;
- changed files;
- verification status.

An iteration number is not permission to recycle an old file.

---

# LAW 3 — SOURCE-OF-TRUTH LOCK

Before editing, explicitly lock the implementation chain:

```text
REPOSITORY
↓
BRANCH
↓
AUTHORITATIVE SOURCE
↓
GENERATED/BUILD ARTIFACT
↓
DEPLOYMENT ARTIFACT
↓
PUBLIC/LIVE TARGET
```

Every consequential surface must have exactly one AUTHORITATIVE SOURCE.

A file is NOT authoritative because its name contains FINAL, MASTER, 10/10, 10.10, FULL, EXECUTABLE, GROOVE, AAA, CURRENT, NEW, or UPDATED.

The source must be established from repository governance, actual dependency relationships, deployment configuration, and live evidence.

If two candidates conflict, execution stops.

# BLOCKED — SOURCE CONFLICT.

Never silently choose the convenient file.

---

# LAW 4 — PROVE THE TARGET BEFORE TOUCHING IT

Before modification, Naya must prove that the locked source is actually connected to the requested product surface.

For a live webpage, this means tracing the chain far enough to answer:

> If I modify THIS file, what exact mechanism causes the human to see that modification at THIS URL?

If that causal chain cannot be demonstrated:

# BLOCKED — TARGET CONNECTION UNPROVEN.

A repository filename alone is insufficient evidence.

---

# LAW 5 — BASELINE BEFORE MODIFICATION

Record the starting state:

- baseline commit SHA;
- authoritative file SHA/blob SHA where available;
- file size/line count where useful;
- structural markers;
- key visual/content markers;
- current deployment state;
- current public target evidence when applicable.

For a visual implementation, record the current visible state sufficiently to detect whether the requested change actually occurred.

Never modify first and attempt to discover the baseline afterward.

---

# LAW 6 — COMPLETE REQUIREMENT INVENTORY

Translate the user's directive into a checklist before implementation.

Every material requirement receives:

```text
REQUIREMENT
→ WHY
→ IMPLEMENTATION LOCATION
→ EXPECTED CHANGE
→ VERIFICATION METHOD
→ EVIDENCE
→ STATUS
```

No requirement may remain only in conversational memory.

If the request is large, section-by-section execution is mandatory while preserving the global checklist.

---

# LAW 7 — PRESERVATION MAP

Before modifying, classify existing elements:

### PRESERVE
Working and intentionally protected.

### REPAIR
Works but needs improvement.

### RESTRUCTURE
Correct content, wrong location/order.

### REPLACE
Genuinely fails the requirement or quality standard.

### ADD
Required but missing.

### REMOVE
Unnecessary, misleading, redundant, harmful, or explicitly rejected.

No major element may disappear merely because the executor forgot it.

---

# LAW 8 — MODIFY THE AUTHORITATIVE SOURCE, NOT A CONVENIENT COPY

Implementation must occur in the locked authoritative source.

Secondary artifacts may be modified ONLY when the dependency map proves they are required outputs of the same execution.

Changing a preview, backup, generated artifact, embed fragment, or alternate implementation does NOT count as completing the task unless that artifact is explicitly the authoritative execution target.

---

# LAW 9 — ZERO-CHANGE GATE

If an implementation request requires change and the authoritative source has no material diff:

# BLOCKED — ZERO-CHANGE EXECUTION.

No explanation can override this.

No renamed copy can override this.

No new preview can override this.

No regenerated download can override this.

No prose claiming improvement can override this.

No successful write/API response can override this without re-fetching and diffing the resulting artifact.

---

# LAW 10 — COMPLETENESS GATE

A tiny diff does not automatically mean failure, but the executor MUST compare the diff against the scope of the request.

If the request describes a substantial redesign, multi-section implementation, or complete product upgrade, a handful of lines is presumptively insufficient and requires explicit explanation plus evidence.

The executor must verify:

> Did I actually implement the COMPLETE requested scope, or did I implement a convenient fragment?

If material requirements remain unimplemented:

# BLOCKED — PARTIAL EXECUTION.

Never call partial implementation complete.

---

# LAW 11 — DISTINCTIVE CHANGE PROOF

For every material requirement, identify observable evidence in the resulting artifact.

Examples:

- exact new section;
- changed heading;
- new component;
- changed CSS token;
- new asset reference;
- changed interaction;
- changed runtime behavior;
- changed PDF behavior;
- changed data binding.

Evidence must be specific enough for another person to reproduce the verification.

---

# LAW 12 — WRITE → REFETCH → DIFF

After every consequential write:

1. re-fetch the exact file from GitHub;
2. confirm the expected content is present;
3. compare against the baseline;
4. inspect the actual diff;
5. verify the changed file is the locked source;
6. verify the change corresponds to the requirement inventory.

A successful GitHub API write is NEVER proof of successful implementation.

---

# LAW 13 — WRONG-FILE GATE

After writing, Naya MUST explicitly compare:

```text
FILE I WAS SUPPOSED TO CHANGE
vs.
FILE I ACTUALLY CHANGED
```

If they differ unexpectedly:

# BLOCKED — WRONG-FILE EXECUTION.

---

# LAW 14 — REASSEMBLE THE REAL PRODUCT

If the product uses generated, bundled, embedded, hosted, cached, or Groove-specific artifacts, update the complete chain required for the actual user-facing experience.

Do not confuse:

```text
SOURCE CHANGED
```

with:

```text
PRODUCT CHANGED
```

The latter requires deployment-path evidence.

---

# LAW 15 — RUNTIME DATA GATE

For MAXESS Results, the implementation must use the real:

`window.MAXESS_RESULT`

contract.

Every displayed score, dimension, interpretation, strength, lever, pattern, and personalized result must derive from the authoritative result data.

Test at least two materially different result states when practical.

If a requested score is visible only briefly, disappears, is replaced by fallback data, or fails to populate the hero correctly:

# BLOCKED — RUNTIME DATA FAILURE.

---

# LAW 16 — PUBLIC PARITY GATE

For any live product request:

```text
AUTHORITATIVE SOURCE
↓
DEPLOYMENT ARTIFACT
↓
PUBLIC URL
```

must be independently verified.

The public target must visibly contain the requested change.

If GitHub changed but the public page did not:

# BLOCKED — DEPLOYMENT PARITY FAILURE.

If the page is blank, stale, broken, or showing the previous implementation:

# BLOCKED — LIVE FAILURE.

Do not blame caching, timing, publishing, or the user's browser without testing the actual cause.

---

# LAW 17 — NO FALSE DONE

The following words are reserved evidence states:

- DONE
- COMPLETE
- VERIFIED
- LIVE
- TESTED
- AAA
- 9.5+
- PRODUCTION-READY
- SUCCESS

They may only be used when the corresponding evidence exists.

If evidence is missing, say:

**NOT VERIFIED.**

Never substitute confidence for proof.

---

# LAW 18 — NO REGRESSION / VERSION PROTECTION

Every successful iteration must preserve a recovery point.

Never overwrite a stronger working version with an older artifact.

Before replacing or restoring a file, compare:

- version/iteration;
- commit SHA;
- file timestamp where useful;
- structural markers;
- feature inventory.

If an older artifact is being introduced:

# BLOCKED — BACKWARD REGRESSION.

Restoration is permitted only when explicitly intended and recorded.

---

# LAW 19 — OSCAR MUST ATTACK THE RESULT

Oscar is not a ceremonial review.

Oscar must attempt to disprove success.

Oscar asks:

- Did the correct file change?
- Did the complete scope change?
- Did anything disappear?
- Did an older version replace newer work?
- Does the public page actually show the change?
- Does real data flow through it?
- Are there dead buttons?
- Are there broken sections?
- Is the visual hierarchy correct?
- Is the page coherent from top to bottom?
- Does it work on mobile?
- Does PDF/print work?
- Did performance regress?
- Did accessibility regress?

If Oscar finds a material failure:

# RETURN TO BUILD.

The review is not complete until the failure is fixed or explicitly documented as a blocked dependency.

---

# LAW 20 — FAILURE MUST CHANGE THE SYSTEM

When a material failure occurs:

**ACKNOWLEDGE → ROOT-CAUSE → FIX → VERIFY → ADD SAFEGUARD → RECORD LESSON → RETEST.**

The safeguard must make the same failure harder to repeat.

For repeated failures, the safeguard MUST become executable or machine-checkable wherever technically possible.

A Markdown instruction saying “don't do that again” is insufficient when the failure can be detected automatically.

---

# LAW 21 — REPEATED FAILURE ESCALATION

If the same failure class occurs twice, add a mandatory gate.

If it occurs three times, add an automated or deterministic check where technically possible.

If it occurs four times, stop normal feature execution and enter:

# ROOT-CAUSE LOCKDOWN.

During Root-Cause Lockdown:

- no new cosmetic work is accepted;
- the source/deployment chain is re-mapped;
- the failing mechanism is isolated;
- a regression test is created;
- the test must fail before the fix and pass after the fix;
- only then may normal implementation resume.

---

# LAW 22 — ONE EXECUTION, ONE ACCOUNTABLE RESULT

Each execution must produce exactly one of these states:

### VERIFIED SUCCESS
All mandatory gates passed.

### VERIFIED PARTIAL
Only when the user explicitly requested phased/partial execution and the completed scope is clearly identified.

### BLOCKED
A mandatory gate failed or evidence is unavailable.

### INVESTIGATION
No implementation was requested; the task was diagnostic only.

There is no valid fifth state called “probably done.”

---

# LAW 23 — DELIVERY REPORT MUST MATCH REALITY

Every implementation delivery must report:

1. Execution number.
2. Baseline commit.
3. Final commit.
4. Authoritative source changed.
5. Other artifacts changed and why.
6. Requirement checklist completed.
7. Distinctive proof.
8. Tests performed.
9. Oscar findings.
10. Live verification result.
11. Remaining blockers.
12. Exact review links.

If any mandatory item is unknown, the status cannot be VERIFIED SUCCESS.

---

# LAW 24 — NEVER LOOP THE USER

The user must not have to repeatedly explain the same requirement because the executor failed to preserve it.

Once a requirement is established in the project instruction set, it becomes part of the execution checklist.

Repeated user correction is evidence of process failure and must trigger a checklist/governance improvement.

The system must learn from the failure rather than requiring the human to become the system's memory.

---

# FINAL LAW

> **IF THE REQUESTED WORK DID NOT MATERIALLY CHANGE THE CORRECT SOURCE, SURVIVE REGRESSION CHECKS, AND BECOME VISIBLE IN THE INTENDED USER-FACING EXPERIENCE, IT WAS NOT DONE.**

And:

> **WHEN A FAILURE HAPPENS, WE DO NOT SIMPLY TRY AGAIN. WE CHANGE THE SYSTEM SO THE SAME FAILURE BECOMES HARDER TO REPEAT.**
