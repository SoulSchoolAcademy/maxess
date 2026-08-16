# MAXESS Results — Naya Profile Asset Registry

Status: authoritative visual asset map for the Results experience.

## Primary Naya profile assets

Use the profile portraits as the default Naya visual language. Prefer the circular crop treatment; do not distort the source image.

### Naya Profile — Black
- Repository filename: `Naya Profile Black.jpg`
- Intended use: dark/black/purple report chapters, hero-adjacent Naya presence, dark cards and overlays.
- Source: `https://raw.githubusercontent.com/SoulSchoolAcademy/maxess/main/Naya%20Profile%20Black.jpg`

### Naya Profile — White
- Repository filename: `Naya Profile white.jpg`
- Intended use: white/light report chapters, interpretation sections, conversational callouts.
- Source: `https://raw.githubusercontent.com/SoulSchoolAcademy/maxess/main/Naya%20Profile%20white.jpg`

## Secondary optional assets

These are available for use only when they improve the visual story. They are not mandatory.

- `Naya Assitant.png`
- `Naya Bc.png`
- `Naya Full Kelowna.png`
- `Naya Kelowna 2.png`

## Selection rule

The profile portraits are the primary identity assets because the Results experience is a personal report and Naya is the guide interpreting the user's results. Secondary images should only be introduced when they materially improve warmth, storytelling, or brand recognition. Never add an image merely to fill space.

## Quality rules

- Preserve source sharpness; never upscale unnecessarily.
- Use `object-fit: cover` for circular portraits.
- Preserve facial proportions.
- Provide meaningful alt text.
- Keep image loading performant with explicit dimensions and lazy loading where appropriate.
- Respect light/dark chapter contrast.
- Do not allow imagery to compete with the user's score or result data.

## Execution state

V6 profile layer is registered in `.naya/MAXESS-RESULTS-NAYA-EXPERIENCE-FIX-V6.html` and is required to pass the deterministic Results execution pipeline before it can be considered part of the authoritative artifact.