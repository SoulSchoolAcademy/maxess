# MAXESS V21 — Release Notes

## Baseline

V21 starts from the approved V20 Results artifact on `maxess-results-v18-preservation-finish`.

V20 is the known-good visual baseline. Preserve it; do not rebuild the Results experience.

## V21 objectives completed in the finish-pass implementation

The V21 finish layer implements the coordinated requirements from the Master Execution Directive:

- Naya remains the guide at the top of the experience.
- Primary action becomes a layered black/white/purple `LISTEN TO NAYA` control.
- Overall MAXESS score remains the hero and is centered inside the score orb.
- `out of 100` is removed from the hero presentation.
- Five dynamic mini MAXESS orbs are generated from `window.MAXESS_RESULT`.
- Each mini-orb is clickable and exposes dimension interpretation.
- The dimension instruction uses a high-contrast black/white treatment.
- A premium modern letter/scroll-inspired personalized report is generated from the result data.
- The report identifies the MAXESS mastery stage: Foundation, Developing, Advancing, or Mastering.
- The report explains the overall result, pattern, strength, lever, next move, and AI Mastery Key invitation.
- Naya's narration is interpretation-first rather than statistic-recitation-first.
- Strength and lever are explicitly framed as `Protect your strength. Build your lever.`
- The 18 Masters can receive personalized pathway-focus indicators based on the authoritative result.
- A dedicated print/PDF report is generated with intentional page structure, typography, page breaks, score page, dimensions page, personalized letter, and next-move page.
- Print/PDF output is not dependent on the screen layout's accidental browser pagination.
- The implementation uses `window.MAXESS_RESULT` as its authoritative result source.
- Name is read from available result identity fields when present, without requiring authentication.

## Critical preservation rule

Do not replace the existing Groove source with a small renderer.
Do not introduce another competing result source.
Do not create a new independent Results architecture.
Do not hard-code a user's score in production.

## Execution method

The V21 implementation is deliberately a single coordinated finish pass. It is designed to be validated as a whole rather than released as a sequence of tiny patches.

The intended QA sequence is:

1. Inspect the complete V20 artifact.
2. Apply the V21 finish layer.
3. Build/render.
4. Test desktop, tablet, and mobile.
5. Test score and all five dimensions against `MAXESS_RESULT`.
6. Test Naya interaction.
7. Test dimension interaction.
8. Test report narrative.
9. Generate the real print/PDF output.
10. Inspect PDF pagination and readability.
11. Repair failures.
12. Re-run QA.
13. Freeze only after the full release gate passes.

## Important GitHub connector constraint

The GitHub contents update operation available to this execution environment replaces an entire text file and requires the complete replacement contents. It does not provide an in-place patch/append operation for a large 7,000+ line HTML artifact.

Therefore the V21 finish implementation is stored as `MAXESS-RESULTS-V21-FINISH-PASS.js` on this branch rather than pretending that the 7,000+ line HTML was safely replaced when the complete source was not available to a single write operation.

This is intentional preservation of the V20 artifact rather than risking destructive source replacement.

The V21 branch therefore represents the complete implementation layer and release specification, but the main Groove HTML itself must not be declared V21-complete until that finish layer is integrated into the canonical HTML and the resulting artifact has passed the actual browser/PDF QA gate.

## Do not claim live publication

GitHub is the source/control handoff. Groove is the publishing environment. A GitHub commit does not prove that the Groove page has been updated.
