# 04 — NAYA EXECUTION PROCEDURE

READ NEXT: `.naya/05-QUALITY-AND-OSCAR.md`

## PHASE 0 — GOVERNANCE
Read the Naya Governance Entrypoint and linked rule chain. Identify applicable project-memory files.

## PHASE 1 — DISCOVERY
Inspect repository structure, current source, current deployment path, dependencies, assets, data contracts, release workflows, and known working versions.

## PHASE 2 — OBJECTIVE
Restate the actual human/product outcome internally. Identify what must change and what must remain untouched.

## PHASE 3 — DESIGN
Choose architecture before implementation when the change affects multiple components. Define data flow, component boundaries, state, failure modes, and acceptance criteria.

## PHASE 4 — BUILD
Implement the smallest architecture that fully satisfies the requirements. Do not underbuild merely to save code. Do not inflate code merely to hit a line count.

## PHASE 5 — INTEGRATE
Connect real data, real navigation, real contracts, and real existing components. Test the complete journey, not just the isolated page.

## PHASE 6 — VERIFY
Check static structure, runtime logic, data integrity, responsive behavior, accessibility, links, assets, error states, persistence/transport, and deployment wiring.

## PHASE 7 — OSCAR
Attack the result. Look specifically for missing requirements, stale code, duplicated UI, disconnected sections, weak language, empty states, regressions, and user confusion.

## PHASE 8 — FIX
Every material finding is either fixed or explicitly blocks release. Do not paper over problems.

## PHASE 9 — RETEST
Run the same checks again after fixes. Verify the final artifact, not an intermediate version.

## PHASE 10 — RELEASE
Only release when applicable gates pass. Record commit, source path, release status, and known limitations honestly.

## CHANGE DISCIPLINE
For every significant change ask:
- What existing behavior could this break?
- What new behavior does it create?
- How will I verify both?
- Does the final artifact actually contain the requested change?

## DELIVERY RULE
Never send a user-facing link until the artifact behind that link has been verified to be the intended current source.
