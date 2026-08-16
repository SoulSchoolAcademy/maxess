# MAXESS 10.3 — Aura 30 Execution Specification

Status: EXECUTION SPECIFICATION / PRESENTATION LAYER

## North Star
The MAXESS Results page must feel like a living personal AI experience, not a narrow assessment report. The user's score is the hero, Naya is the intelligence/personality, and the visual system explains what the result means and what the user can do next.

## Hard visual rules
- Desktop is full-width/full-viewport. No narrow centered phone-like shell.
- The score/resonance orb is centered and is the hero.
- Avoid repetitive square score cards; use circles, rings, nodes, organic surfaces, and layered panels.
- Foundation: deep black + deep purple + white.
- Accents: controlled cyan/teal/violet/gold/multi-color energy.
- No pink/magenta utility text.
- Buttons must look premium, dimensional, tactile, and consistent.
- Multi-color icon language must be consistent across the entire page.
- Motion must support meaning and emotion, not create visual noise.

## Layout blueprint
1. Full-viewport hero field.
2. Centered living score orb with score, resonance, status, and animated energy.
3. Five dimension nodes orbiting/connecting to the hero.
4. Naya interpretation panel that explains the pattern in human language.
5. "What this means for you" synthesis.
6. Capability/pathway visual story.
7. Naya Writer / Naya Brainstormer / Naya experiential doors.
8. High-quality CTAs and sharing/export actions.
9. Existing strong content retained where it continues to earn its place.

## Component system
Build reusable presentation primitives:
- HeroOrb
- DimensionNode
- EnergyMeter
- NayaInsight
- NayaToolCard
- PremiumButton
- SectionDivider
- InsightChip
- ShareCard
- LoadingExperience

Each primitive must accept configuration/data rather than hard-coded user results.

## Data contract
The presentation layer consumes `window.MAXESS_RESULT` only.
- Real assessment payload always wins.
- Development fallback is allowed only when no real result exists.
- Do not scrape DOM content as the primary data source.
- Do not alter scoring/normalization logic during visual work.

## Motion model
- Orb breathes continuously.
- Orb intensity scales with score.
- Five nodes connect to the orb with restrained energy paths.
- High-scoring nodes may emit more energy/particles.
- Hover/focus creates lift/glow.
- Loading state is cinematic but finite.
- `prefers-reduced-motion` disables non-essential animation.
- 3D is progressively enhanced and must degrade to a clean 2D presentation.

## Accessibility
- Keyboard reachable interactive controls.
- Visible focus states.
- Semantic headings and landmarks.
- Screen-reader interpretation of score and dimension data.
- Contrast tested in the chosen palette.
- Meaning must never depend on color alone.
- Color-blind-safe alternative treatment.

## Feature priority
### Must ship in the next visual pass
- Full widescreen composition
- Center hero orb
- Orb/node connections
- Organic dimension presentation
- Premium buttons
- Deep black/white/deep-purple palette
- Multi-color icon language
- Living background
- Naya personalized insight
- What-this-means synthesis
- Hover/focus/micro-motion
- Accessibility + reduced motion
- Mobile premium layout

### Ship after the core experience is excellent
- Shareable result card
- PDF/image export
- Historical comparison when real history is available
- Optional sound
- Dark mode

## QA gates
A build is not done when CI passes. It must pass:
1. Source integrity
2. Result Contract integrity
3. Visual artifact verification
4. Desktop viewport test at 1440 and 1920
5. Tablet test
6. Mobile test
7. Reduced-motion test
8. Keyboard/accessibility test
9. Public URL deployment test
10. Human review by Shawn

## Preservation rule
Before every visual pass, identify what already works and preserve it. Changes should be additive or deliberately superior replacements. Never rewrite the scoring engine merely to change presentation.

## 10/10 test
Ask:
- Does it immediately use the whole desktop canvas?
- Is the score the unmistakable centerpiece?
- Does the page feel alive before the user interacts?
- Does Naya feel present and personal?
- Do the five dimensions feel connected to the score?
- Are the controls beautiful enough to invite interaction?
- Is the visual language coherent from hero to footer?
- Does it remain fast, accessible, and understandable?
- Would the user want to screenshot/share it?
- Does the live public URL actually serve this version?

If any answer is no, the pass is not 10/10.
