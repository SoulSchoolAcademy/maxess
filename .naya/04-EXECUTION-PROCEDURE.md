# 04 — NAYA EXECUTION PROCEDURE

READ FIRST: `.naya/00-UNDERSTANDING-FIRST.md`
READ NEXT: `.naya/05-QUALITY-AND-OSCAR.md`

## PHASE 0 — UNDERSTANDING GATE
Before consequential implementation, read `.naya/00-UNDERSTANDING-FIRST.md` and complete its Understanding-First protocol.

The executor must first inspect the repository, establish the source of truth, understand the current architecture and working behavior, verify the production/deployment path when relevant, reconcile contradictions, and formulate the implementation/verification plan.

**No implementation begins until the Understanding Gate passes.**

If material uncertainty remains, status is `BLOCKED — UNDERSTANDING INCOMPLETE`.

`GO — MASTER NAYA` activates this sequence; it does not bypass the gate.

## PHASE 1 — GOVERNANCE
Read the Naya Governance Entrypoint and linked rule chain. Identify applicable project-memory files.

## PHASE 2 — DISCOVERY
Inspect repository structure, current source, current deployment path, dependencies, assets, data contracts, release workflows, and known working versions.

## PHASE 3 — OBJECTIVE
Restate the actual human/product outcome internally. Identify what must change and what must remain untouched.

## PHASE 4 — RECONCILIATION
Distinguish authoritative source files from generated artifacts, legacy/prototype files, specifications, and release infrastructure. Resolve material conflicts before editing.

## PHASE 5 — DESIGN
Choose architecture before implementation when the change affects multiple components. Define data flow, component boundaries, state, failure modes, and acceptance criteria.

## PHASE 6 — BUILD
Implement the smallest architecture that fully satisfies the requirements. Do not underbuild merely to save code. Do not inflate code merely to hit a line count.

## PHASE 7 — INTEGRATE
Connect real data, real navigation, real contracts, and real existing components. Test the complete journey, not just the isolated page.

## PHASE 8 — VERIFY
Check static structure, runtime logic, data integrity, responsive behavior, accessibility, links, assets, error states, persistence/transport, and deployment wiring.

## PHASE 9 — OSCAR
Attack the result. Look specifically for missing requirements, stale code, duplicated UI, disconnected sections, weak language, empty states, regressions, user confusion, growth friction, and visual inconsistency.

## PHASE 10 — FIX
Every material finding is either fixed or explicitly blocks release. Do not paper over problems.

## PHASE 11 — RETEST
Run the same checks again after fixes. Verify the final artifact, not an intermediate version.

## PHASE 12 — RELEASE
Only release when applicable gates pass. Record commit, source path, release status, and known limitations honestly.

## CHANGE DISCIPLINE
For every significant change ask:
- What existing behavior could this break?
- What new behavior does it create?
- How will I verify both?
- Does the final artifact actually contain the requested change?
- Am I modifying the authoritative source or merely an artifact?

## MULTI-AGENT DISCIPLINE
Any downstream AI/agent must receive the relevant mission, authoritative sources, protected functionality, architecture, requested delta, constraints, acceptance criteria, verification requirements, and known risks before it executes. No agent may guess through missing project context.

## DELIVERY RULE
Never send a user-facing link until the artifact behind that link has been verified to be the intended current source.
