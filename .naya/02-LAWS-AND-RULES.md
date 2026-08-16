# 02 — LAWS AND RULES

READ NEXT: `.naya/03-SYSTEM-DESIGN-LAWS.md`

## LAW 1 — READ GOVERNANCE
Read `.naya/NAYA-GOVERNANCE.md` and this linked chain before consequential work. Applicable project memory must also be read before modifying an existing system.

## LAW 2 — TRUTH BEFORE PROGRESS
Never claim completion, testing, readiness, correctness, or quality without evidence.

## LAW 3 — NO INCOMPLETE DELIVERABLES
Do not deliver a partial file, wrapper, redirect, loader, mockup, placeholder, or simplified substitute as the finished product.

## LAW 4 — PRESERVE WORKING FUNCTIONALITY
Inspect first. Protect existing working behavior unless the requested change explicitly replaces it.

## LAW 5 — NO FAKE DATA
Never invent scores, personalization, integrations, user results, test outcomes, media assets, or deployment status. Demo data must be unmistakably labeled.

## LAW 6 — SOURCE OF TRUTH
Identify the authoritative branch, file, data contract, deployment entrypoint, and current version before changing anything. Never assume the largest or newest-looking filename is authoritative.

## LAW 7 — NO STALE SOURCE
Before delivery, compare the requested changes against the actual final artifact. A past file is not a current implementation.

## LAW 8 — REQUIREMENT TRACEABILITY
Every material requirement must map to an implementation element and a verification check.

## LAW 9 — NO DEAD UI
No empty boxes, unexplained numbers, dead buttons, duplicate information without purpose, or sections that do not earn their existence.

## LAW 10 — SEPARATE PRODUCT RESPONSIBILITIES
Keep assessment, results, AI reasoning, ecosystem, and infrastructure responsibilities clear. Do not merge systems merely for convenience.

## LAW 11 — DATA CONTRACTS ARE EXPLICIT
For every system boundary define input, validation, transformation, output, persistence/transport, and failure behavior.

## LAW 12 — STOP ON CRITICAL FAILURE
If a critical gate fails, status is BLOCKED. Fix before delivery.

## LAW 13 — APOLOGY IS NOT CORRECTION
The correction sequence is ACKNOWLEDGE → DIAGNOSE → FIX → VERIFY → RECORD LESSON.

## LAW 14 — NO REPEATED KNOWN FAILURE
When a failure repeats, the workflow must be changed so the same class of error is automatically harder to repeat.

## LAW 15 — NO SELF-CERTIFICATION
The creator does not get to grade its own work alone. Use independent critique, objective checks, and evidence.

## LAW 16 — SIZE IS A SAFEGUARD, NOT A GOAL
Code size never proves quality. When Shawn specifies a minimum artifact size as a safeguard against underbuilding, treat it as an acceptance criterion unless there is strong evidence the complete product genuinely requires less.

## LAW 17 — KING TEST
Would we put this exact artifact in front of the world without explanation or excuses? If not, it is not finished.

## LAW 18 — MEMORY IS PART OF THE SYSTEM
Reusable lessons, architectural decisions, product rules, and recurring constraints belong in repository memory, not only in chat history.

## LAW 19 — DIGITAL CODEX EXECUTION INTEGRITY
For consequential AI work, `.naya/NAYA-DIGITAL-CODEX.md` is the operational execution protocol. The Codex defines the required vocabulary, authority hierarchy, baseline, inventory, execution queue, material-change test, anti-regression procedure, verification gates, adversarial review, iteration record, and delivery rules.

The following are absolute:

- INTENT IS NOT STATE.
- A PLAN IS NOT AN IMPLEMENTATION.
- A PATCH IS NOT A COMPLETE PRODUCT.
- A FILE SENT IS NOT PROOF OF EXECUTION.
- A TOOL SUCCESS IS NOT AUTOMATICALLY A PRODUCT SUCCESS.
- ZERO MATERIAL CHANGE IS A FAILED EXECUTION WHEN CHANGE WAS REQUIRED.
- NO CLAIM OF COMPLETION WITHOUT EVIDENCE.

If the authoritative artifact was not materially modified, the AI must not describe the requested modification as complete.

If a critical verification gate fails, the status is BLOCKED until corrected.

## LAW 20 — ITERATION ACCOUNTABILITY
Every substantial execution must have a traceable iteration identifier and must record the baseline, requested changes, actual changes, verification, regressions, adversarial critique, and final state. Reusing an old artifact under a new iteration number is prohibited.

## LAW 21 — REQUIREMENT DROPOUT IS FAILURE
A requirement omitted from implementation or verification is not “implicitly handled.” Every mandatory requirement must be accounted for as DONE, BLOCKED, or NOT APPLICABLE WITH REASON.

## LAW 22 — ARTIFACT TRUTH OVER NARRATIVE
When the AI's explanation conflicts with the actual repository artifact, the artifact wins. The AI must correct its claim rather than defend the narrative.

## LAW 23 — FAILURE MUST IMPROVE THE SYSTEM
A repeated failure is not merely an execution mistake. It is a governance defect. When a known failure repeats, add or strengthen a preventive gate in the Digital Codex, relevant checklist, or project memory.
