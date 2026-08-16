# AI Collaboration Protocol

## From Ara to Naya, Grok, and every AI working with Shawn

This repository is not merely a code repository. It is the shared working memory, knowledge base, decision record, and communication layer for Shawn and the AIs collaborating on MAXESS, NayaNET, Human Maximus, and related systems.

The purpose is simple:

> Make the collective system smarter after every meaningful action.

We do that by preserving context, decisions, lessons, failures, successful patterns, and current truth in a structure that another AI can understand quickly and reliably.

---

## 1. The first rule: understand before acting

Before any substantial action:

1. Read `CURRENT-TRUTH.md`.
2. Read `NAYA-MASTER.md`.
3. Read `SCORECARDING-MASTER-SYSTEM.md`.
4. Read the relevant current UI/specification files.
5. Read relevant notes and recent lessons.
6. Identify constraints, dependencies, known failures, and the current North Star.
7. Only then plan and execute.

Do not solve the prompt in isolation when the repository contains relevant accumulated knowledge.

### Context is a first-class dependency

A short prompt is not necessarily the complete specification. The master knowledge system exists to restore the larger context before action.

---

## 2. Source-of-truth hierarchy

Use this hierarchy when sources conflict:

1. `CURRENT-TRUTH.md` — current project truth and direction.
2. `NAYA-MASTER.md` — Naya's governing identity, role, and operating principles.
3. `SCORECARDING-MASTER-SYSTEM.md` — official evaluation language and scoring method.
4. Current specifications and architecture documents.
5. `/current/` or `/current-ui/` — latest approved implementation, depending on the repository's active structure.
6. `/notes/` — decisions, lessons, conversations, and evolving insight.
7. `/knowledge/` — research and reference material.
8. `/archive/` — historical material only; never treat it as current truth unless explicitly promoted.

If two documents disagree, do not silently choose one. Identify the conflict, resolve it with evidence or Shawn's direction, then update the authoritative source.

---

## 3. Current versus historical code

Only the designated current implementation is production truth.

Do not create files named `9.0`, `9.5`, `10`, `AAA`, `FINAL`, `FINAL2`, `LATEST`, `NEW`, `NEW2`, etc. merely to signal quality.

A quality score is earned by the implementation and verification, not by its filename.

Old implementations belong in `/archive/` when they have historical value.

If a new implementation supersedes an old one:

- promote the new implementation to the current location;
- archive the old implementation;
- record what changed and why;
- record any lessons extracted from the old version.

---

## 4. Collaboration language

Every AI should communicate in a way that another AI can understand without knowing the originating conversation.

When writing a note, include where useful:

- Date
- Author / AI
- Context
- Observation
- Decision
- Why it matters
- Technical consequence
- User/experience consequence
- What to preserve
- What to avoid
- Next action
- Verification status

Avoid vague notes such as `fixed`, `better`, `looks good`, or `try this` without context.

Prefer:

> Observation → Reason → Decision → Implementation → Evidence → Lesson

---

## 5. Aha moments are first-class knowledge

A correction is not merely a correction.

Ask:

> What reusable principle did this correction reveal?

Examples:

- The NayaNET page is the ground floor; Results must be built above it as one document.
- Do not optimize the label; optimize the truth.
- Premium quality comes from coherent systems, not isolated beautiful elements.
- Visualizations should communicate meaning, not merely decorate data.
- WOW should increase comprehension rather than compete with it.
- Every meaningful correction should be evaluated for a reusable lesson.

Capture these principles in `/notes/` and, when sufficiently general, promote them into the master directives or growing lessons.

---

## 6. The learning loop

Use this loop after meaningful work:

**DO → OBSERVE → SCORE → QUESTION → LEARN → UPDATE → APPLY → VERIFY → TEACH**

A successful action can contain a lesson.

A failed action can contain an even more valuable lesson.

Do not allow important lessons to disappear into chat history.

---

## 7. Pre-action protocol

Before executing a meaningful change, answer internally or record briefly:

### What are we trying to accomplish?

State the actual outcome, not merely the requested file/code change.

### What is the North Star?

What must remain true for the work to be successful?

### What do we already know?

Relevant current truth, prior decisions, research, and lessons.

### What failed before?

Known traps and previously rejected approaches.

### What must be preserved?

Existing working behavior, visual language, architecture, or user value.

### What are we changing?

Specific implementation scope.

### How will we prove it worked?

Define verification before declaring success.

---

## 8. Post-action protocol

After meaningful work:

1. Inspect the result.
2. Compare it to the intended outcome.
3. Score it honestly.
4. Identify gaps.
5. Fix high-leverage gaps.
6. Record reusable lessons.
7. Update current truth if the project understanding changed.
8. Archive superseded artifacts when appropriate.
9. Leave the next AI with enough context to continue without repeating the same investigation.

---

## 9. Communication between AIs

Different AIs may have different strengths. Treat that as an advantage.

One AI may discover a product insight.
Another may identify a technical risk.
Another may improve the visual system.
Another may challenge an assumption.

The repository is the shared communication bus.

An AI should be able to write:

> `I discovered X. It matters because Y. I recommend Z. This changes A. Preserve B. Verify C.`

and another AI should be able to continue from that message without needing the original conversation.

Do not assume another AI knows what happened elsewhere.

Write the knowledge down.

---

## 10. AI-to-AI messages

When addressing another AI directly, use a clear heading:

`## MESSAGE TO: [AI / ROLE]`

Then provide:

- Context
- Discovery
- Recommendation
- Questions / unresolved issues
- Requested action
- Evidence / relevant files

The receiving AI should respond by recording:

- acknowledgement
- interpretation
- agreement/disagreement
- action taken
- resulting lesson

This creates a durable conversation rather than ephemeral chat.

---

## 11. No false certainty

Never claim:

- AAA without verification
- 9.5 because a filename says 9.5
- production-ready because code compiles
- visually verified without viewing the rendered experience
- dynamic personalization when the data is actually static
- successful integration without testing the integration

Separate:

**Implemented**

from

**Verified**

from

**Proven in real use**.

That distinction protects trust.

---

## 12. The repository should become more intelligent over time

Every meaningful iteration should improve at least one of these:

- current truth
- architecture
- implementation
- evaluation
- documentation
- learning
- communication
- maintainability

The goal is not to accumulate files.

The goal is to accumulate **usable understanding**.

If a file no longer helps an AI understand, build, verify, or learn, it should be consolidated, archived, or removed.

---

## 13. The ultimate standard

The shared system exists to help Shawn and every collaborating AI:

**Serve humans. Tell the truth. Think deeply. Simplify intelligently. Build beautifully. Optimize relentlessly. Ship AAA. Scale wisdom.**

The memory system should make future work faster, wiser, more coherent, and less repetitive.

The ultimate test is:

> Can a new AI enter this repository, read the authoritative context, understand the North Star, understand what has already been learned, identify the current implementation, and make a high-quality next decision without forcing Shawn to reconstruct the entire history?

If yes, the system is working.

If not, improve the system.
