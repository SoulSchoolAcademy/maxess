# MAXESS V20 — APPROVED WORKING BASELINE

Date: 2026-08-16

Status: APPROVED WORKING BASELINE — preserve this state unless a future change intentionally replaces it.

## Why this baseline matters

This is the first Results-page iteration that Shawn has explicitly judged as a major success. The live Groove page is now structured, professional-looking, substantially less overwhelming, and usable as a real foundation for continued refinement.

Shawn's direct assessment: this is the best the Results page has looked so far. The large score orb at the top works visually, the duplicate/zero score problem is gone, and the page now feels structured and professional.

## What solved the major problem

The successful execution method was a full-pass transformation against the real large Groove source rather than a small replacement renderer or isolated one-at-a-time patch.

Key execution lessons:

1. Preserve the existing 7,000+ line Groove source.
2. Treat GitHub as the shared source-of-truth workspace.
3. Make multiple related edits in one controlled pass.
4. Apply the changes to the real source, not a miniature test renderer.
5. Run structural/static checks and browser QA before declaring success.
6. Keep temporary execution/repair machinery separate from the final page artifact.
7. Do not stack endless generations of competing DOM renderers.
8. When a QA assertion fails, repair the complete pass and rerun the full gate rather than stopping after a partial fix.
9. The live Groove page—not GitHub source—is the final truth for visual/publishing verification.

## Confirmed successful V20 changes

- Existing Groove architecture preserved.
- Large canonical MAXESS orb retained.
- Duplicate/zero score presentation removed.
- AI score moved into the dominant top-level orb treatment.
- The page hierarchy became substantially cleaner and more professional.
- Existing downstream report content was preserved.
- Existing Pattern, Strength, Lever, Next Move, Masters/pathway and Playground/ending content were preserved.
- Real MAXESS_RESULT data remained functional.
- Full-pass browser QA was used before the artifact was considered successful.
- The resulting HTML was committed to the working branch.

## Still intentionally open for V21+

These are improvements, not reasons to destabilize the approved baseline:

- Make the five subordinate dimension orbs true visual mirrors of the main orb.
- Restore/implement the intended five smaller orb treatment with real scores, dimension names and clickable behavior.
- Refine the exact placement of the main score number; current approved preference is to keep the orb near the top while considering a more centered score presentation inside the orb.
- Increase the primary Naya Listen button size/visual prominence.
- Continue refining Naya's role as the front-of-house guide.
- Verify and complete the exact desired narrative order where any legacy content still differs.
- Continue removing any remaining legacy/competing presentation elements only when their replacement is proven.
- Preserve the current visual quality while making further changes incrementally and safely.

## Non-negotiable preservation rule

Do NOT revert to the old strategy of replacing the page with a small renderer. Do NOT overwrite this baseline with an incomplete reconstruction. Future work must start from this approved V20 baseline and improve it surgically or through a controlled full-pass transformation.

## Working philosophy

The breakthrough was not merely a particular CSS/DOM edit. The breakthrough was the execution method: use the complete real source, batch the related changes, validate the resulting artifact, and only then publish/test it.

This baseline should be treated as the reference point for future MAXESS Results work.
