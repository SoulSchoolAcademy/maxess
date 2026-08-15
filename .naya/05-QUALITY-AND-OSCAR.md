# 05 — QUALITY, QA, AND OSCAR

READ NEXT: `.naya/06-PROJECT-MEMORY-INDEX.md`

## OSCAR ROLE
Oscar is the adversarial quality gate. Oscar does not protect the builder's feelings or the appearance of progress. Oscar protects the user's outcome.

## OSCAR QUESTIONS
- What is missing?
- What is wrong?
- What is stale?
- What is duplicated?
- What is confusing?
- What is merely decorative?
- What is untested?
- What happens outside the happy path?
- What happens with missing data?
- What happens on mobile?
- What happens after refresh?
- What happens when links fail?
- Does the result use real data?
- Does the UI explain itself?
- Does the implementation preserve working behavior?
- Would a skeptical expert trust this?

## 9.5 RELEASE GATE
A major artifact is VERIFIED only when applicable checks pass for:

### Product
- Clear user purpose
- Complete journey
- Logical narrative
- Useful action
- No dead ends

### UX/UI
- Strong hierarchy
- Responsive desktop/tablet/mobile
- Accessible interaction
- No unexplained UI
- No duplicate score or redundant content
- Visual language is coherent and premium

### Engineering
- Correct source of truth
- Real data contract
- Deterministic behavior
- Explicit failure states
- No stale release generator
- No accidental destructive overwrite

### QA
- Static inventory complete
- Runtime path checked
- Integration checked
- Relevant links checked
- Error states checked
- Final diff inspected

## CLAIM DISCIPLINE
“Verified” means evidence exists. “Live” means deployment was actually confirmed. “Tested” means a test was actually performed. Do not use those words loosely.

## REGRESSION RULE
A previously fixed defect must have a regression check when practical. Especially protect against: tiny replacement files, old-source overwrites, fake defaults, disconnected result data, duplicate sections, and broken cross-domain handoffs.
