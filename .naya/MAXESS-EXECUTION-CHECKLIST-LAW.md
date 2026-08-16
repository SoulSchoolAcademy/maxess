# MAXESS EXECUTION CHECKLIST LAW

Status: MANDATORY
Version: 2.0
Effective: 2026-08-16

## PURPOSE

Prevent false completion claims, repeated review loops, delivery of unchanged or partial artifacts, and user time being spent discovering failures that should have been caught before delivery.

This law operationalizes Naya Law and the Human Maximus Prime Directive for consequential implementation work.

## PRIME EXECUTION STANDARD

PLAN → EXECUTE → VERIFY → CHECK OFF → DELIVER

Never:

PLAN → CLAIM → LINK → USER DISCOVERS FAILURE

A plan is not execution.
A commit is not execution.
A filename is not execution.
A successful load is not proof of the requested change.
A description of a feature is not the feature.

## 1. PRE-FLIGHT: ESTABLISH TRUTH

Before changing anything, the assistant MUST:

1. Read NAYA Law, NAYA Master, relevant governance, project memory, and the applicable source registry.
2. Identify the authoritative implementation source.
3. Identify the actual production/deployment entrypoint.
4. Capture the authoritative source path and current hash when available.
5. Inventory the existing working functionality.
6. Separate known facts, assumptions, and unverified facts.
7. Identify protected functionality that must survive.
8. Establish the exact requested delta.
9. Establish acceptance criteria before implementation begins.
10. Create the numbered implementation checklist.

If authority is ambiguous, STOP and resolve authority before editing.

## 2. REQUIRED IMPLEMENTATION CHECKLIST

Every material implementation request MUST begin with a numbered checklist.

Every item MUST state:

1. WHAT will change.
2. WHERE it will change.
3. HOW it will be implemented.
4. HOW completion will be verified.
5. WHAT existing behavior is protected from regression.

The checklist must enumerate material changes individually. Broad statements such as “make it AAA” are insufficient.

For a visual/UX upgrade, the checklist must identify each major requested visual, interaction, content, responsive, accessibility, performance, data, and delivery change.

## 3. EXECUTE AGAINST THE AUTHORITATIVE SOURCE

The implementation MUST modify the authoritative implementation or an explicitly designated successor that preserves the authoritative architecture.

Never substitute a smaller renderer, wrapper, loader, mock, prototype, excerpt, minified replacement, or unrelated artifact merely because it is easier to produce.

For an existing production system, the default strategy is:

PRESERVE → UNDERSTAND → IMPROVE → INTEGRATE → TEST → SCORE → REPEAT

Replacement requires explicit authorization.

## 4. ITEM-BY-ITEM COMPLETION CONTROL

During execution, every checklist item has exactly one state:

- NOT STARTED
- IN PROGRESS
- BLOCKED
- COMPLETE — VERIFIED

Only COMPLETE — VERIFIED may receive a green checkmark.

An item cannot be marked complete because:

- a directive was written;
- a plan exists;
- a commit was created;
- a file exists;
- a filename says AAA;
- a manifest says complete;
- a test merely loaded the page;
- the intended feature is described in prose;
- the assistant expects the feature to work.

The actual implementation must contain the change and verification must prove it.

## 5. BEFORE/AFTER DIFFERENCE GATE

Every upgrade request MUST establish a before state and an after state.

The assistant MUST inspect the actual diff/change footprint before claiming completion.

The diff must contain substantive implementation changes corresponding to the requested work.

Metadata-only changes, commit messages, manifests, hashes, timestamps, filenames, whitespace-only changes, or generated labels do not satisfy the gate.

If a requested visual or functional change cannot be located in the actual source artifact, that item is NOT COMPLETE.

If an upgrade produces no meaningful source change, STOP:

**BLOCKED — ZERO MEANINGFUL IMPLEMENTATION CHANGE DETECTED.**

Do not deliver the unchanged artifact.

## 6. PRESERVATION / REGRESSION GATE

Before editing, inventory what already works.

After editing, verify that material protected behavior still exists.

For MAXESS Results this includes, where present:

- full-width architecture;
- Groove compatibility;
- real MAXESS_RESULT handoff;
- existing assessment/result functionality;
- Naya identity and behavior;
- existing media/video;
- existing icons and useful visual language;
- CTA/conversion functionality;
- responsive behavior;
- accessibility behavior;
- print behavior;
- existing NayaNET foundation.

A feature may only be marked preserved when the actual resulting artifact proves it remains present and functional.

## 7. FUNCTIONAL VERIFICATION GATE

Run appropriate static and runtime verification against the resulting artifact.

At minimum, verify where applicable:

- HTML/document integrity;
- JavaScript syntax;
- bootstrap/runtime initialization;
- authoritative result contract;
- real data propagation;
- expected dimensions;
- expected dynamic calculations;
- interactive controls;
- responsive rules;
- accessibility hooks;
- reduced-motion behavior;
- print/PDF rules;
- media preservation;
- absence of silent production fixtures;
- absence of duplicate/competing Results renderers.

A test must test the requested behavior, not merely confirm that a file exists.

## 8. VISUAL VERIFICATION GATE

For visual/UX work, code inspection alone is insufficient.

The assistant MUST verify the rendered result whenever the available tooling permits.

Verification should include:

- desktop/widescreen composition;
- tablet behavior;
- mobile behavior;
- hierarchy and spacing;
- actual visual presence of requested components;
- interactions and states;
- typography readability;
- contrast;
- Orb/animation behavior;
- button/icon quality;
- section ordering;
- absence of unintended clipping, overlap, or cramped layouts.

If live visual verification is unavailable, state that limitation explicitly. Do not claim visual verification occurred.

## 9. ADVERSARIAL QA / OSCAR GATE

Before delivery, challenge the implementation as if trying to prove it is NOT complete.

Ask:

- Did the requested change actually happen?
- Did I accidentally preserve the old presentation instead?
- Did I create a wrapper instead of upgrading the source?
- Did I lose existing functionality?
- Did I hard-code anything that should be dynamic?
- Did I introduce a fixture into production behavior?
- Did I change terminology or architecture incorrectly?
- Did I optimize one section while damaging the whole experience?
- Does the result work outside the exact happy path?
- Would the user immediately see the claimed improvement?

Any material failure returns the relevant checklist item to IN PROGRESS or BLOCKED.

## 10. DATA-INTEGRITY GATE

Where a result contract exists, verify the actual authoritative data boundary.

Do not scrape DOM content as a substitute for authoritative data.
Do not replace production data with a fixture.
Do not create a second scoring engine in the presentation layer.

Development fixtures must be explicit, deterministic, and impossible to silently masquerade as production data.

## 11. DEPLOYMENT-PARITY GATE

Repository completion and public deployment are separate states.

The assistant MUST distinguish:

- SOURCE VERIFIED
- ARTIFACT VERIFIED
- DEPLOYMENT VERIFIED
- LIVE USER-FACING VERIFIED

GitHub success does not prove Groove success.
A generated embed does not prove public deployment.
A public URL existing does not prove it serves the intended artifact.

Before claiming LIVE, independently inspect the actual public target and verify it matches the intended artifact.

If deployment ownership/source is unknown, status is BLOCKED — DEPLOYMENT PARITY UNKNOWN.

## 12. ARTIFACT COMPLETENESS GATE

When the user requests complete embed code, the delivered artifact MUST be:

- complete;
- readable where source readability is part of the requirement;
- self-contained when specified;
- ready for the stated deployment environment;
- free of omitted sections;
- free of placeholder/mock content unless explicitly requested;
- free of instructions requiring the user to reconstruct the application from multiple hidden pieces.

A partial file is never “the full embed.”

## 13. ROLLBACK / SAFETY GATE

Before material edits, preserve the known-good authoritative state.

If an implementation damages the source or produces an invalid artifact:

1. preserve evidence of the failure;
2. restore the known-good state where necessary;
3. diagnose the failure;
4. re-execute from the protected baseline;
5. never hand the user the damaged artifact as a review candidate.

## 14. COMPLETION REPORT

Before giving any review, deployment, or embed link, the response MUST contain a numbered completion checklist corresponding to the implementation plan.

Example:

1. 🟢 COMPLETE — Score-first hero — verified in resulting artifact and rendered output.
2. 🟢 COMPLETE — Five circular gauges — verified by source and runtime structure.
3. 🔴 NOT COMPLETE — Public Groove deployment — blocked because deployment source is unavailable.

Every green item must have evidence.
Every red item must state:

- what was not completed;
- why it was not completed;
- what is required to complete it;
- whether the overall delivery is blocked.

## 15. NO PREMATURE DELIVERY

The assistant MUST NOT make the user inspect a link to discover whether work was actually performed.

The assistant must inspect the artifact first, prove the checklist, then provide the link.

If the checklist is incomplete, the link is withheld unless the user explicitly asks to inspect an incomplete work-in-progress.

## 16. EVIDENCE LEDGER

For consequential builds, retain enough evidence to reconstruct what happened:

- authoritative source path;
- before hash/version;
- after hash/version;
- implementation diff/change footprint;
- checklist status;
- tests performed;
- runtime/visual verification performed;
- known limitations;
- deployment status.

The evidence ledger is part of the quality system, not optional decoration.

## 17. STOP CONDITIONS

STOP and do not claim completion when:

- authoritative source is unclear;
- requested changes are absent from the diff;
- the artifact is only a wrapper/loader when a complete artifact was required;
- critical protected functionality is lost;
- tests fail materially;
- live deployment cannot be distinguished from source completion;
- visual verification is required but unavailable and the response would otherwise claim visual success;
- any material checklist item remains unverified.

## 18. TRUTH RULE

If execution failed, say it failed.
If only some items were completed, say exactly which ones.
If all items were completed, prove them.
If something cannot be verified, label it UNVERIFIED rather than implying success.

The standard is:

**PLAN → EXECUTE → VERIFY → CHECK OFF → DELIVER.**

The goal is not to sound productive.
The goal is to produce the requested result correctly, prove it, preserve what works, and minimize the user's need to discover failures manually.
