# AI Collaboration + Master Memory — 2026-08-15

## Context

Shawn introduced a higher-level operating model for MAXESS: the GitHub repository should function as a shared brain/memory and communication system between Shawn and collaborating AIs such as Naya, Ara, Grok, and future agents.

## Core insight

The problem is often not intelligence or coding ability. It is missing context.

A single conversation cannot reliably contain the entire history, decisions, failures, lessons, standards, and current state of a complex project. Therefore the project needs persistent externalized context that can be read before action and updated after meaningful work.

## Decision

Create a universal AI collaboration protocol that makes GitHub the durable shared memory and communication layer.

The protocol is now stored in:

`AI-COLLABORATION-PROTOCOL.md`

## Operating model

Before substantial work:

CURRENT TRUTH → NAYA MASTER → SCORECARDING → RELEVANT CURRENT IMPLEMENTATION → RECENT LESSONS → EXECUTE

After substantial work:

DO → OBSERVE → SCORE → QUESTION → LEARN → UPDATE → APPLY → VERIFY → TEACH

## Important principles

1. Context is a first-class dependency.
2. Current truth outranks historical artifacts.
3. Old versions should be archived, not confused with current work.
4. Filenames must never be used to claim quality.
5. Aha moments are reusable system knowledge.
6. Corrections should be converted into general principles where possible.
7. Different AIs can contribute different strengths through a shared written protocol.
8. The repository should accumulate understanding, not random files.
9. Implemented, verified, and proven-in-use are distinct states.
10. The ultimate goal is compounding collective intelligence.

## Architectural implication

The repository is not merely source control. It is simultaneously:

- source of truth
- memory system
- learning system
- decision record
- AI-to-AI communication bus
- engineering workspace
- verification history

## Future requirement

Continue improving the folder structure and source-of-truth hierarchy so a new AI can enter the repository, understand the project rapidly, identify current implementation, learn from prior failures, and make a high-quality next decision without requiring Shawn to reconstruct the history manually.

## Aha

The strongest form of collaboration is not merely multiple AIs producing outputs. It is multiple intelligences contributing to a persistent shared knowledge system where each meaningful action improves the context available to the next action.
