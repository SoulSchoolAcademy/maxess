# MAX Assessment Family

## Product lock

The MAX ecosystem has three core assessment products under one reusable assessment architecture:

| Product | Core question | Primary value |
|---|---|---|
| AI MAX | How effectively am I working with AI? | Most immediately useful: turns AI frustration into a measurable capability profile and a practical next step. |
| MAX LIFE | How effectively am I operating my life? | Most revealing of oneself: surfaces patterns in choices, habits, relationships, direction, growth and agency. |
| MAX PERCEPTION | How deeply and accurately am I perceiving life? | Most mind-opening: reveals assumptions, filters, perspective, discernment, flexibility and willingness to reconsider. |

Together the family reads as:

**AI • LIFE • PERCEPTION**

under the shared:

**MAX**

The family promise is:

**MAX your intelligence. MAX your life. MAX your perception.**

## Architecture

```text
Assessment Entry
      ↓
Reusable MAX Assessment Engine
      ↓
Questions + Answers + Scoring + Personalization
      ↓
MAX Assessment Result Contract
      ↓
Results Experience
      ↓
Personal Insight + Pathway
      ↓
Naya
      ↓
NayaNET
```

The assessment page and Results page are separate products connected by an explicit result-data contract. The Results page must never invent a result, silently substitute a demo score in production, or require the Results UI to know how the assessment calculated the score.

## Reusable engine requirements

The underlying engine is configuration-driven and must support:

- assessment identity and versioning
- question configuration
- answer configuration
- dimensions
- weighting
- normalization
- deterministic scoring
- response persistence
- result validation
- profile/archetype configuration
- personalization rules
- pathway/area configuration
- result serialization
- Results-page handoff
- cloning for future assessments and white-label products

## Result contract requirements

Every completed assessment must produce a normalized result object that contains, at minimum:

- assessment id/version
- completion state
- overall score
- mastery/level classification
- exactly the configured dimension set with scores
- strongest capability
- opportunity capability
- profile/archetype
- answer/response data when required for interpretation
- personalized areas/pathway
- recommendations/narrative context where configured

The Results application consumes this contract and renders the appropriate Results experience.

## AI MAX

The flagship first implementation is AI MAX. Its Results experience is the primary template for the family.

Core Results journey:

1. Your Result
2. What AI Really Says About You
3. Your Five-Dimension Pattern
4. Your Five Dimensions
5. Your Leverage: Strength + Opportunity
6. Oh… That's Why
7. Your Next Move
8. Your Personalized AI Mastery Library
9. Naya Mastery Roles
10. AI Craftsmanship: KNOW → TELL → ASK → CREATE → SCORE → IMPROVE → REPEAT
11. Master AI
12. Existing NayaNET experience

## MAX LIFE

MAX LIFE reuses the engine and Results framework but receives its own dimensions, questions, interpretation model and pathway. Its job is not to become an AI quiz; it is a life-capability assessment.

Primary product promise:

**The most revealing MAX assessment — help me see patterns in how I am actually living, choosing, relating, growing and using my agency.**

## MAX PERCEPTION

MAX PERCEPTION is intentionally designed to be more than a conventional personality test. Its questions should reveal perception itself while the person is taking the assessment.

Its purpose is to explore how a person notices, interprets, filters, evaluates, reconsiders and expands their understanding of life.

The core model is:

- Awareness
- Perspective
- Discernment
- Flexibility
- Expansion

The questions should distinguish observation from interpretation, expose assumptions and filters, test perspective-taking, and measure willingness to reconsider a belief or interpretation when new evidence appears.

The assessment should not ask the user to self-label as “perceptive.” It should create ordinary human situations in which the person's perception pattern becomes visible through the choice they make.

Its Results experience should create a genuine recognition moment such as:

> “I thought I was very perceptive. I didn't realize how much of my experience was being shaped by the way I interpreted it.”

This should lead naturally toward the Human Maximus Codex and its perception-oriented transformation work.

### MAX PERCEPTION AI rules

AI may interpret response patterns, identify meaningful combinations, surface likely blind spots, explain score relationships in plain language, suggest practical reflection experiments, and generate a personalized pathway.

AI must not invent evidence, diagnose the person, claim certainty where evidence is ambiguous, or override deterministic scoring.

Every result should distinguish:

- **FACT** — what the response/scoring model actually establishes
- **INTERPRETATION** — what the pattern may suggest
- **REFLECTION** — what the person may want to explore next

## Product positioning

The assessment front door should stay simple:

> Is AI giving you the results you know it should?
>
> Discover your AI MAX Score.
>
> Take the free three-minute assessment and discover your score, strengths, blind spots and next opportunity.

Then offer the family choice:

- AI MAX SCORE
- MAX LIFE SCORE
- MAX PERCEPTION SCORE

The assessment earns attention first. The Results experience earns trust and insight. Naya and NayaNET provide the environment for action.

## Non-negotiable quality rules

- Preserve working systems.
- Never replace a complete product with a tiny prototype.
- Never fabricate production results.
- Never use URL parameters to manufacture scores.
- Never deliver an empty or unexplained Results section.
- Never call an untested handoff complete.
- Desktop must be expansive; mobile must be genuinely responsive.
- Every Results section must earn its place.
- Every score must have a meaning.
- Every opportunity must have a practical next action.
- Personalization must come from actual result data.
- The existing NayaNET ending remains the final bridge unless explicitly redesigned later.
- Oscar is the final quality critic: truth, completeness, logic, usefulness, beauty, accessibility, responsiveness and technical integrity all have to pass.

## Permanent family lock

The three-product family is now authoritative:

**AI MAX · MAX LIFE · MAX PERCEPTION**

The naming is not interchangeable with “MAX Reception.”
