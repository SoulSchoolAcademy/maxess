# MAXESS EXECUTION CHECKLIST LAW

Status: MANDATORY
Version: 1.0
Effective: 2026-08-16

## PURPOSE

Prevent false completion claims, repeated review loops, and delivery of unchanged or partial artifacts.

## BEFORE EXECUTION

Every material implementation request MUST begin with an explicit numbered implementation checklist. Each item must state:

1. WHAT will change.
2. WHERE it will change.
3. HOW it will be implemented.
4. HOW completion will be verified.
5. WHAT existing behavior is protected from regression.

The checklist is the execution contract. It must cover every material requested upgrade, not merely broad categories.

## DURING EXECUTION

The implementation must proceed through the checklist item by item against the authoritative source.

A checklist item cannot be marked complete because:

- a directive was written;
- a commit was created;
- a file exists;
- a filename says AAA;
- a test loaded successfully;
- an intended feature is described in prose.

A checklist item is complete only when the actual implementation contains the change and an appropriate verification proves it.

## BEFORE ANY REVIEW LINK IS GIVEN

The assistant MUST NOT provide a review/deployment/embed link until all material checklist items are either:

- COMPLETE — verified in the actual artifact; or
- BLOCKED — explicitly identified with the reason and no claim of completion.

There is no implied completion.

## REQUIRED COMPLETION REPORT

Before giving the link, the response MUST contain:

### IMPLEMENTATION CHECKLIST

1. 🟢 COMPLETE — [specific change] — [verification evidence]
2. 🟢 COMPLETE — [specific change] — [verification evidence]
3. 🟢 COMPLETE — [specific change] — [verification evidence]

Any incomplete item MUST be shown as:

🔴 NOT COMPLETE — [specific change] — [exact reason]

Never use green/checkmark language for an unverified item.

## ARTIFACT DIFFERENCE GATE

For an upgrade request, the authoritative artifact MUST have a substantive code/content diff corresponding to the requested work.

A commit message, manifest, generated filename, or metadata change is not evidence of an implementation change.

If the requested visual/UX changes cannot be identified in the source diff, the work is NOT COMPLETE.

## PRESERVATION GATE

For existing systems, the checklist MUST include preservation checks for all material existing functionality identified during the audit.

The new artifact must be an actual upgrade of the authoritative existing implementation unless the user explicitly authorizes replacement.

## NO PREMATURE DELIVERY

Never make the user inspect a link to discover whether work was actually performed.

The assistant must inspect the artifact first, prove the checklist, then provide the link.

## TRUTH RULE

If execution failed, say it failed.
If only some items were completed, say exactly which ones.
If all items were completed, prove them.

The standard is:

PLAN → EXECUTE → VERIFY → CHECK OFF → DELIVER.

Never:

PLAN → CLAIM → LINK → USER DISCOVERS FAILURE.
