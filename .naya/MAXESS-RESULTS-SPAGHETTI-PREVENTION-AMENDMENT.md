# MAXESS RESULTS — SPAGHETTI PREVENTION AMENDMENT

Status: MANDATORY EXECUTION AMENDMENT
Version: 1.0
Applies to: Every MAXESS Results reconstruction, refactor, Groove embed, and deployable artifact.

## WHY THIS EXISTS

The previous V16 candidate failed the user's most basic acceptance test: it looked like a compressed, difficult-to-audit block of code and was not presented as a trustworthy complete source artifact.

The failure was not merely visual. The execution process optimized for producing a compact candidate quickly instead of proving that the candidate was a complete, maintainable, source-level implementation of the requested experience.

The failure mechanism was:

1. A large Results request was translated into a feature checklist.
2. The implementation was generated as a dense single-expression renderer.
3. Large amounts of markup and behavior were packed into one JavaScript template string.
4. Static checks confirmed syntax and presence of keywords, but did not prove architecture quality, maintainability, complete component boundaries, or visual/source readability.
5. The handoff treated static correctness as sufficient evidence of AAA quality.

That door is now closed.

## NEW HARD RULE — NO COMPRESSED MONOLITHIC RENDERERS

A consequential MAXESS Results artifact MUST NOT implement the entire page as one giant `root.innerHTML = \`...\`` expression, one minified function, or one opaque immediately-invoked block containing all markup, data logic, styles, and interactions.

The artifact must have explicit source-level architecture:

```text
BOOTSTRAP / DATA CONTRACT
        ↓
NORMALIZATION
        ↓
DERIVED INSIGHTS
        ↓
COMPONENT RENDERERS
        ↓
PAGE ASSEMBLY
        ↓
BEHAVIOR / INTERACTION BINDING
        ↓
QA / READY EVENT
```

Each major Results component must have a named renderer or clearly bounded implementation section.

## REQUIRED COMPONENT BOUNDARIES

The source must contain separately identifiable implementation for:

- data bootstrap
- result normalization
- profile
- score hero / Orb
- score interpretation
- five dimensions
- pattern
- strongest signal
- biggest lever
- next move
- Naya
- 18 Masters
- continuation / CTA
- accessibility helpers
- responsive behavior
- print behavior
- interaction binding
- initialization

## READABILITY GATE

The source must be understandable by a competent engineer opening the file for the first time.

Reject:

- giant one-line functions;
- giant template literals containing the whole page;
- unexplained numeric constants scattered through rendering code;
- repeated inline logic that should be a function;
- cryptic one-letter variables for major state;
- mixed data, markup, styling, and event binding in the same expression;
- generated-looking code that cannot be safely edited by hand.

## COMPLETE SOURCE GATE

The handoff artifact MUST be the complete source file, not:

- a fragment;
- a patch without the base file;
- a shortened replacement;
- a snippet;
- a pseudo-code representation;
- a wrapper around an unseen file;
- a loader that fetches the real implementation from somewhere else;
- or a file that depends on an undocumented missing companion.

If the requested deliverable is a Groove embed, the delivered artifact must be directly usable as the Groove embed source or explicitly include every required companion dependency with exact integration instructions.

## TOP-TO-BOTTOM COMPONENT CHECK

Review the actual source and the rendered experience in this order:

1. document/bootstrap
2. hero
3. profile
4. report interpretation
5. dimensions
6. pattern
7. strongest signal
8. biggest lever
9. next move
10. Naya
11. 18 Masters
12. system/continuation
13. CTA
14. footer/closing behavior

Do not skip from code generation to final handoff.

## VISUAL QA GATE

Static source inspection is NOT visual QA.

The evaluator must inspect the rendered page top-to-bottom and ask:

- Is the hierarchy obvious?
- Does each section feel intentional?
- Are components visually related without becoming repetitive cards?
- Does the page feel premium rather than assembled?
- Is the Orb meaningful?
- Does Naya feel present rather than pasted on?
- Are there awkward gaps, cramped areas, excessive borders, weak typography, or generic dashboard patterns?
- Does the page remain coherent at mobile widths?

If visual inspection cannot be performed in the available environment, the status must be `VISUAL QA NOT VERIFIED`; do not call the page AAA.

## COMPLETENESS PROOF

Before handoff, record:

- source byte size;
- line count;
- major section count;
- named renderer/component count;
- all 18 Master names;
- data contract markers;
- event handlers;
- external dependencies;
- runtime fallback behavior;
- responsive breakpoints;
- print rules;
- accessibility hooks;
- exact file SHA/blob SHA;
- exact commit SHA.

## MINIMUM ACCEPTANCE STANDARD

A candidate cannot be called AAA if it is merely:

- syntactically valid;
- feature-rich on paper;
- different from the baseline;
- or visually plausible from a screenshot.

AAA requires:

**COMPLETE + STRUCTURED + READABLE + FUNCTIONAL + PERSONALIZED + RESPONSIVE + ACCESSIBLE + PERFORMANT + DEPLOYABLE + VERIFIED.**

## FAILURE RESPONSE

If a candidate fails this amendment:

1. reject the candidate;
2. record the failure mechanism;
3. do not relabel it;
4. do not promote it;
5. rebuild from the approved baseline or clean working state;
6. re-run the complete gate.

This amendment exists specifically to prevent repeating the V16 failure mode.