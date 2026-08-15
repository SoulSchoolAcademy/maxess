# 16 — MAXESS GROOVE ENGINEERING LAWS

Status: LOCKED ENGINEERING MEMORY
Version: 1.0

## Core physical architecture

MAXESS Assessment and MAXESS Results are distinct experience modes.

Assessment = contained, focused, question-by-question experience.
Results = long-form, flowing, scrollable, personalized document.

Entering Results must release any assessment-specific viewport/container constraints rather than forcing the Results experience into the assessment's fixed board.

## Single-embed principle

When the target environment requires a single Groove embed, the deliverable must be self-contained enough to survive that environment. Do not use redirects, external loaders, hidden replacement pages, or separate app deployments as substitutes for a complete embed unless explicitly approved.

## Data boundary

The assessment engine produces the authoritative Result Contract.
The Results engine consumes and validates it.

Conceptual flow:
MAXESS ASSESSMENT → RESULT CONTRACT → MAXESS RESULTS.

Do not rely on localStorage/sessionStorage as a cross-origin handoff between `maxess.nayanet.xyz` and `results.nayanet.xyz`.

## State architecture

Use explicit experience modes/states rather than one giant ambiguous screen state. Core modes may include:
- assessment
- interests
- results

Results can have internal reveal stages such as:
- reveal
- overview
- capability
- insight
- master-key
- pathways
- cta

These are experience states, not necessarily separate pages.

## Result renderer

The Results renderer should consume structured data such as:
- overall score
- mastery band
- dimension scores
- strongest dimension
- opportunity dimension
- response pattern
- profile/archetype
- interests
- pathways
- recommendations
- narrative
- next step

Separate truth-producing engine logic from presentation/meaning-making logic.

## Determinism

Same assessment inputs should produce the same underlying score and dimension result. Optional presentation variation must never alter the underlying assessment truth.

## QA profiles

At minimum test:
- minimum responses
- maximum responses
- balanced responses
- one very high dimension
- one very low dimension
- score-band boundaries
- ties for strongest/opportunity dimensions
- multiple interest combinations
- missing/invalid result payload
- repeated submission
- refresh/back behavior
- audio/speech failure
- visualization failure
- offline/optional-service failure when applicable

## Personalization verification

Create at least three fictional profiles. Their reports should differ materially enough that a reviewer can tell which profile produced which interpretation. Generic copy must not masquerade as personalization.

## Graceful degradation

Optional layers must fail without destroying the core product:
- Naya speech → text fallback
- motion → static content fallback
- charts → accessible textual equivalent
- optional external service → useful local experience where possible

## Groove delivery gate

Before a Groove artifact is called final:
1. Confirm current authoritative source.
2. Confirm the artifact actually contains the requested changes.
3. Confirm it is self-contained to the required degree.
4. Confirm assessment state still works.
5. Confirm transition into Results works.
6. Confirm Results can scroll through its entire document.
7. Confirm Results does not inherit accidental assessment constraints.
8. Confirm end-to-end result data flow.
9. Confirm mobile behavior.
10. Confirm no known critical regression.
11. Compare against the previous approved baseline.
12. Score against the MAXIS/AAA release gate.

## Hard engineering rule

Do not substitute a large old file, a loader, a redirect, or a wrapper for the requested current implementation.

A file being large proves only that it is large. A file being reachable proves only that it is reachable. Neither proves that the current product transformation is present.
