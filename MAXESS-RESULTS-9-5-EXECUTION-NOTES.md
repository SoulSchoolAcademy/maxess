# MAXESS Results 9.5+ Execution Notes

## Status

The repository has now received the first coherent 9.5+ execution pass as additive production assets.

Commits:
- `498db83d405c119629f9d01f407b94b56fcec466` — MAXESS 9.5+ execution CSS pass
- `ccfe5ef09dd2c673f51f5998c62626d2589ab4eb` — executable Groove insert

## North Star

`RESULT -> RECOGNITION -> PATTERN -> LEVERAGE -> PATH -> NAYA -> ACTION`

The Results experience is not a report. It is a personalized revelation that turns the assessment into a clear next move.

## What this pass changes

### 1. Full-page composition

Use the available viewport width intelligently. Wide containers are used for visual systems, fingerprint graphics, dimension grids, and pathway composition. Reading remains constrained where prose benefits from it.

### 2. Hero hierarchy

The score remains the dominant object. The first screen answers what the user got, what it means, and where to go next without competing CTA clutter.

### 3. MAXESS action language

Primary and secondary controls receive stronger hierarchy, consistent 58px touch targets, deliberate icon treatment, focus states, depth, hover behavior, and mobile full-width behavior.

### 4. Recognition before information density

The short-version insight is treated as a major emotional beat. The page should make the user recognize themselves before asking them to process the complete data set.

### 5. Fingerprint as signature product visual

The five-dimensional visualization receives more breathing room and visual emphasis. It is treated as the user's capability pattern, not merely a chart.

### 6. Strength + leverage

The page's contrast section is treated as a decision system: where the user already has power and where improvement creates the most leverage.

### 7. Pathway as payoff

The growth/path section is visually connected to the preceding diagnosis. The next action should feel earned by the result rather than appended as a marketing CTA.

### 8. Naya transition

The Naya bridge is strengthened as the handoff from self-understanding to guidance. Existing NayaNET/video/membership behavior remains preserved rather than replaced.

### 9. Mobile

The experience uses the full available width, removes cramped multi-column controls at small sizes, keeps action targets thumb-friendly, and prevents the desktop hierarchy from collapsing into tiny text.

### 10. Reduced motion and accessibility

Focus visibility and reduced-motion preservation remain part of the pass. The patch is additive and does not remove existing semantic/accessible markup.

## Preservation rule

Do not rewrite the assessment engine, scoring model, NayaNET endpoint, video, membership presentation, or other proven behavior merely for visual polish.

The ideal architecture remains:

`ASSESSMENT ENGINE -> AUTHORITATIVE MAXESS_RESULT -> RESULTS RENDERER -> NAYA -> NAYANET`

## Release gate

The pass is not considered finally scored 9.5+ until the live Groove-rendered experience is visually and functionally verified at:

- desktop wide
- desktop standard
- tablet
- 320px mobile
- lowest plausible score
- highest plausible score
- mixed dimensions
- tied dimensions
- optional personalization absent
- refresh after completion
- back navigation
- keyboard navigation
- reduced motion
- slow/failing Results source
- Naya endpoint
- video/buttons/membership endpoint

## Important implementation note

Because the repository's existing Results/Groove file is a mature large embed, this pass is deliberately stored as an additive insert rather than destroying or replacing the established build. `MAXESS-RESULTS-9-5-GROOVE-INSERT.html` is the executable Groove insertion; `MAXESS-RESULTS-9-5-EXECUTION-PASS.css` is the canonical source for the styling rules.

The next score should be earned from the actual rendered experience, not assumed from the existence of the code.
