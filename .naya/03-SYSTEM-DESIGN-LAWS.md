# 03 — SYSTEM DESIGN LAWS FOR NAYA

READ NEXT: `.naya/04-EXECUTION-PROCEDURE.md`

## ARCHITECTURE LAW
Design the system before modifying implementation when changes cross components.

## CONFIGURATION-DRIVEN LAW
Prefer reusable engines driven by configuration/data over hard-coded one-off implementations when the product is intended to support multiple assessments, profiles, dimensions, customers, or white-label variants.

## SEPARATION OF CONCERNS
Assessment measures. Results interprets. Naya reasons/assists. NayaNET provides ecosystem experiences. Infrastructure transports and persists data.

## CONTRACT-FIRST LAW
Every boundary needs a stable, documented contract. A Results page must consume an authoritative result object rather than reconstructing truth from presentation state.

## PRESERVATION RULE
Do not rewrite working modules just because a clean-room rewrite is easier to author. Preserve proven behavior and change only what is required.

## SOURCE-OF-TRUTH RULE
At project start, establish current source, deployment source, data source, and release pipeline. Record them in project memory when they are not obvious.

## STATE INTEGRITY
The same real input should produce the same deterministic result unless the specification explicitly includes randomness.

## FAIL-CLOSED RULE
Missing or invalid result data must produce a clear failure state or safe recovery path. Never silently manufacture a result.

## CROSS-DOMAIN RULE
Different origins must use an explicit transport mechanism. Never assume localStorage/sessionStorage is shared across subdomains.

## RELEASE INTEGRITY
A release pipeline must not silently regenerate production output from an obsolete source. The authoritative source must be explicit and guarded by structural gates.

## OBSERVABILITY
For important builds expose evidence: version, source, status, validation result, and meaningful diagnostics. Do not rely on memory or intuition.

## MODULARITY
Reusable concerns should be separable: data model, engine, renderer, integration, QA, content, and deployment.

## HUMAN-FIRST ENGINEERING
Technical elegance exists to serve the human outcome. Favor clarity, maintainability, accessibility, performance, resilience, and understandable behavior.
