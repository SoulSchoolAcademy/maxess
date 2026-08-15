# 25 — GROOVE EMBED ENGINEERING LAW

Status: AUTHORITATIVE MASTER PROJECT MEMORY  
Version: 1.0  
Date: 2026-08-15  
Scope: All NayaNET / MAXESS / Human Maximus pages and app-like experiences currently intended for publication through Groove.cm custom embed/code blocks.

> **PRIMARY PURPOSE**
> Teach Naya how to design for the Groove embed environment itself rather than designing a generic webpage and hoping Groove will reproduce it.
>
> Groove embed code is not merely a delivery format. It is the current runtime architecture for our public experiences.

---

# 1. NON-NEGOTIABLE OPERATING LAW

For current Groove publishing, the design target is:

**A complete, self-contained, responsive, production-quality page fragment that is intentionally engineered for insertion into Groove's Code Embed / Custom Code environment.**

GitHub is the source-control, memory, inspection, versioning, QA, and delivery-link system. Groove is the deployment/runtime environment.

Never confuse:

- the standalone source page;
- the Groove-native embed artifact;
- the public Groove deployment;
- the live verified result.

These are four different states.

The authoritative pipeline is:

**DISCOVER → INVENTORY → DESIGN FOR GROOVE → BUILD NATIVE EMBED → STATIC QA → OSCAR → RETEST → COMMIT → RAW LINK → PASTE INTO GROOVE → PUBLISH → LIVE VERIFY**

---

# 2. WHAT WE KNOW ABOUT GROOVE TODAY

Groove's current public site describes GroovePages as a responsive drag-and-drop website/page builder and explicitly lists custom code integration, unlimited pages, custom domains, analytics, and integration with other Groove apps. [GroovePages](https://groove.cm/groove-pages)

Groove's current public transition page says Groove.cm is transitioning to Scale.gg. Existing Groove members can continue using their Groove tools during the phased transition, while new Groove enrollment has closed. [Official transition update](https://www.groove.cm/)

Public third-party GroovePages integration guides confirm that GroovePages supports Code Embed / HTML-style embeds and that external services commonly provide snippets intended to be pasted into a GroovePages embed/code element. [Prefinery example](https://help.prefinery.com/article/273-how-to-install-the-signup-form-on-groovepages-groove-cm) [POWR example](https://www.powr.io/tabs-for-groovepages-how-to-add-to-your-site)

A third-party technical article documents that Groove's custom-HTML implementation may itself execute the custom code inside an iframe in some contexts. This is important because it means the parent Groove page and the embedded document can have separate layout contexts. Treat this as an observed implementation detail, not as an immutable official platform contract. [Technical example](https://thegroovepreneur.com/blog/post/start-a-blog-with-grooveblog)

## 2.1 WHAT WE COULD NOT ESTABLISH AS A PUBLIC PLATFORM LIMIT

As of 2026-08-15, we did **not** find an authoritative public Groove document stating a hard maximum for:

- HTML characters/bytes in a Code Embed element;
- JavaScript characters/bytes;
- CSS characters/bytes;
- number of DOM nodes;
- maximum single-embed height;
- maximum script execution time;
- maximum number of script tags;
- maximum number of embedded code blocks per page;
- maximum file size for an inline custom-code artifact.

Therefore Naya MUST NOT invent a numeric Groove maximum and present it as fact.

Use **tested practical budgets** instead of fake platform limits.

---

# 3. OUR PRACTICAL GROOVE LIMITS

These are engineering budgets, not claimed vendor limits.

## GREEN — preferred

- One self-contained page experience per embed block.
- Inline CSS and JavaScript when practical.
- No dependency on a build step for Shawn.
- No external frontend framework unless the runtime need is proven.
- No unnecessary network requests.
- Keep the DOM intentionally structured.
- Prefer one root container with namespaced classes/IDs.
- Use CSS variables for the design system.
- Keep assets compressed and intentionally loaded.
- Prefer vector/SVG/CSS visuals over large raster assets when practical.
- Use lazy-loading for below-the-fold heavy media.
- Use `defer`-style or end-of-fragment execution patterns when applicable.
- Keep runtime initialization deterministic and idempotent.

## YELLOW — possible but requires testing

- Large inline artifacts approaching or exceeding 100 KB.
- Many animations running simultaneously.
- Large SVGs.
- Multiple canvases.
- Complex charts.
- Large embedded JSON datasets.
- Several third-party scripts.
- Multiple Code Embed blocks coordinating with one another.
- Global selectors affecting the parent page.
- Long-running timers, observers, or event loops.

## RED — avoid unless there is a demonstrated reason

- A complete `<!doctype html><html><head><body>` document pasted into a native fragment slot when a fragment is the intended target.
- Nested iframes as a substitute for native rendering.
- Full-page legacy DOM hidden with CSS instead of removing it from the delivered artifact.
- Multiple unrelated page engines in one embed.
- Framework runtimes loaded from multiple CDNs without necessity.
- Repeating global IDs/classes that may collide.
- Reliance on browser behavior that has not been tested on the actual Groove page.
- Huge unoptimized images or video assets inside the code artifact.
- Code that depends on editor-preview-only behavior.
- Code that assumes direct control of the parent document when the embed may execute in an isolated context.

---

# 4. THE BIG GROOVE PRINCIPLE: DESIGN FOR THE EMBED RUNTIME

A generic web page asks:

> "How would I build this website?"

A Groove-native build asks:

> "What is the exact runtime context in which this code will be injected, and how do I get the maximum possible experience inside that context?"

This changes architecture.

## 4.1 Start with the embed contract

Every Groove page should define:

- root element ID;
- namespace prefix;
- expected width behavior;
- expected height behavior;
- background ownership;
- data input contract;
- initialization trigger;
- navigation model;
- asset strategy;
- error state;
- mobile behavior;
- cleanup/reinitialization behavior;
- version marker.

## 4.2 Use a single application root

Preferred:

```html
<div id="maxess-groove-embed">
  ...experience...
</div>
```

Then scope CSS to that root whenever possible.

## 4.3 Make the fragment self-contained

A production artifact should ideally contain everything required to render:

- structure;
- styles;
- interaction logic;
- data/config;
- accessibility labels;
- responsive rules;
- error/empty states;
- version/build markers.

The goal is copy/paste → publish → works.

---

# 5. GROOVE EMBED CODE DOS

## DO 1 — Namespace everything

Use a strong prefix such as:

- `rr-` for Results;
- `nx-` for Naya;
- `mx-` for MAXESS;
- one unique root ID.

This minimizes collision with Groove's own CSS and any other page elements.

## DO 2 — Build full-bleed intentionally

When the experience should visually occupy the page, use an explicit full-bleed strategy rather than assuming the embed container will naturally span the viewport.

Typical pattern:

```css
#maxess-groove-embed{
  position:relative;
  width:100%;
  max-width:100%;
  min-height:100vh;
}
```

Where the parent environment introduces side gutters, test a controlled viewport breakout technique only when necessary.

Do not apply viewport breakout blindly; it must be verified on the actual Groove page.

## DO 3 — Make the page responsive from the first line of CSS

Do not build desktop first and bolt mobile on later.

Use:

- `clamp()`;
- fluid grids;
- responsive typography;
- min/max widths;
- CSS Grid/Flexbox;
- media queries;
- touch-friendly controls.

## DO 4 — Use deterministic initialization

The page must survive:

- initial load;
- delayed script execution;
- editor preview quirks;
- repeated rendering where applicable;
- resize events;
- missing result data.

Initialization should be safe to run more than once or should explicitly prevent double initialization.

## DO 5 — Separate data from presentation

For MAXESS, use the Result Contract and configuration-driven dimensions/Master library rather than hard-coding a single person's result into the UI.

## DO 6 — Build graceful empty/error states

A missing result should produce a helpful state, not a blank page and not fabricated scores.

## DO 7 — Preserve accessibility

Use:

- semantic headings;
- buttons for actions;
- links for navigation;
- visible focus states;
- sufficient text contrast;
- reduced-motion support;
- descriptive labels;
- keyboard-accessible controls.

## DO 8 — Optimize assets

Do not embed 15 MB images merely because Groove accepts the file.

Prefer:

- compressed WebP/AVIF where supported;
- properly sized images;
- SVG for logos/icons;
- lazy loading;
- poster images before video;
- hosted assets only when the dependency is deliberate and reliable.

## DO 9 — Keep animation purposeful

Motion should communicate hierarchy, state, or delight.

Do not animate everything.

## DO 10 — Test the live published page

Builder preview is not enough.

The actual Groove URL is the deployment truth.

---

# 6. GROOVE EMBED CODE DON'TS

## DON'T 1 — Do not confuse a standalone HTML document with an embed fragment

A standalone source file may legitimately contain:

```html
<!doctype html>
<html>
<head>...</head>
<body>...</body>
</html>
```

A Groove-native fragment should normally not include that document shell.

## DON'T 2 — Do not hide legacy code instead of removing it

This caused the recent MAXESS Results failure.

A hidden legacy iframe/DOM can still:

- affect layout;
- execute JavaScript;
- add network traffic;
- create duplicate IDs;
- interfere with selectors;
- confuse the builder;
- increase runtime complexity.

The release artifact should contain only the code the current experience needs.

## DON'T 3 — Do not use iframe as the architecture unless the product actually needs an iframe

An iframe creates another browsing context and adds isolation, but also creates:

- sizing complexity;
- communication complexity;
- navigation complexity;
- accessibility complexity;
- performance overhead;
- debugging friction.

For our current single-page MAXESS Results experience, the preferred architecture is native embed code without a nested iframe.

## DON'T 4 — Do not rely on global CSS

Bad:

```css
body{...}
h1{...}
button{...}
```

Preferred:

```css
#maxess-groove-embed h1{...}
#maxess-groove-embed .mx-button{...}
```

Global selectors can collide with the Groove host page.

## DON'T 5 — Do not depend on editor-only DOM behavior

A page that works only inside the Groove editor but fails after publishing is not complete.

## DON'T 6 — Do not create fake numeric limits

There is no evidence for a public hard Groove Code Embed byte/line maximum. Record measured practical limits instead.

## DON'T 7 — Do not inflate code to hit an arbitrary line count

More lines do not equal better engineering.

The correct objective is:

**maximum capability + minimum unnecessary code + maximum clarity + maximum reliability.**

## DON'T 8 — Do not create multiple engines for the same page

One page should have one authoritative renderer/runtime.

## DON'T 9 — Do not assume an external library will always load

Every external dependency introduces:

- availability risk;
- latency;
- version drift;
- privacy/security considerations;
- possible CSP/runtime issues.

Use dependency-free HTML/CSS/JS whenever practical.

## DON'T 10 — Do not claim LIVE VERIFIED until the actual Groove URL has been checked

GitHub passing only proves source-level gates.

---

# 7. WHAT EMBED CODE ENABLES US TO DO EXTREMELY WELL

When the Groove Code Embed environment accepts HTML/CSS/JS, it becomes a compact application runtime inside the Groove page.

That lets us build far more than a static block.

## 7.1 Application-like interfaces

We can build:

- dashboards;
- assessment result experiences;
- calculators;
- interactive scorecards;
- quizzes;
- tab systems;
- accordions;
- charts;
- radar graphs;
- progress systems;
- animated storytelling;
- personalization;
- local state/persistence where browser storage is appropriate;
- copy/share/print utilities;
- conditional rendering;
- data-driven cards;
- custom navigation;
- client-side filtering and sorting.

## 7.2 Data-driven personalization

A single embed can render different output based on:

- URL parameters;
- `sessionStorage` / `localStorage` where appropriate;
- serialized result contracts;
- page state;
- controlled API responses if external requests are deliberately used.

This is especially powerful for MAXESS because the same visual engine can render different people's scores without rebuilding the page.

## 7.3 Custom visual systems

Embed code lets us escape ordinary builder widgets and create:

- custom SVG illustrations;
- CSS-based visual identities;
- animated score rings;
- radar charts;
- energy fields/glows;
- custom iconography;
- premium motion;
- unconventional layouts;
- responsive storytelling.

The builder becomes the host; our code becomes the experience engine.

## 7.4 Direct control over the user journey

Instead of forcing the user through generic builder components, the embed can orchestrate:

**attention → explanation → result → interpretation → action → next experience**

That is the correct model for MAXESS Results.

---

# 8. WHERE EMBED CODE IS STRONGER THAN ORDINARY BUILDER ELEMENTS

## Stronger in

### Visual uniqueness
We can design exact geometry, typography, spacing, gradients, motion, SVG, and responsive behavior rather than accept the builder's generic component shapes.

### Interaction density
A single embed can behave like a miniature application.

### Reusable engines
One renderer can serve many assessments and datasets.

### Deterministic rendering
Configuration + data → consistent result.

### Faster iteration for a code-capable team
One source file can change the whole experience without manually adjusting dozens of builder elements.

### Advanced visualization
Canvas/SVG/CSS-based charts and diagrams are practical.

### Portability
A well-designed fragment can potentially be moved to another HTML-capable host with fewer changes than a page built from proprietary builder widgets.

---

# 9. WHERE EMBED CODE IS WEAKER

Embed code is not automatically better for everything.

It is weaker when we need:

- deep server-side logic;
- secure secrets;
- private API credentials;
- long-running background processes;
- complex backend databases;
- server-side rendering;
- large build pipelines;
- package ecosystems that depend on compilation;
- enterprise-scale application state.

For those jobs, keep the backend/service external and make Groove the presentation/runtime host.

**Never place secrets in browser-delivered embed code.**

---

# 10. THE IDEAL MAXESS/GROOVE ARCHITECTURE

The preferred architecture is:

```text
MAXESS ASSESSMENT ENGINE
        ↓
RESULT CONTRACT
        ↓
GROOVE RESULTS EMBED ROOT
        ↓
DATA NORMALIZER
        ↓
RESULTS UI ENGINE
        ↓
VISUALIZATION ENGINE
        ↓
NAYA PERSONA / MASTER LIBRARY
        ↓
ACTION / NEXT EXPERIENCE
```

The embed should be a reusable presentation engine, not a one-off page.

## 10.1 Recommended file roles

### Source
`MAXESS-RESULTS-10-GROOVE.html`

Full standalone development/reference artifact.

### Delivery
`MAXESS-RESULTS-GROOVE-EMBED.html`

The exact Groove-native paste artifact.

### Build tool
`tools/build_maxess_results_groove_embed.py`

Generates the delivery artifact from the authoritative source.

### Verification
Royal and Groove-specific QA scripts verify:

- required structures;
- dimensions;
- Masters;
- Result Contract;
- no legacy iframe/DOM;
- responsive/accessibility signals;
- full-bleed behavior;
- delivery integrity.

---

# 11. PERFORMANCE LAW

There is no virtue in a huge file.

The quality target is:

**rich experience / minimal unnecessary payload**

## Recommended performance priorities

1. Remove dead code.
2. Remove duplicate CSS.
3. Remove unused JS.
4. Avoid giant images.
5. Avoid duplicate libraries.
6. Avoid layout thrashing.
7. Minimize repeated DOM queries when practical.
8. Debounce/throttle expensive resize/scroll handlers.
9. Prefer CSS transforms for animation.
10. Render only what is needed.
11. Lazy-load heavy below-the-fold assets.
12. Keep first-screen content fast.

## Performance budget philosophy

Use this as a working target, not a Groove vendor limit:

- **<50 KB:** excellent for a substantial interactive fragment.
- **50–100 KB:** comfortable for a rich page if runtime is efficient.
- **100–250 KB:** acceptable for a highly interactive experience; test carefully.
- **250–500 KB:** yellow zone; justify the payload.
- **>500 KB:** red zone for inline embed unless the capability genuinely requires it.

These are engineering heuristics, not Groove's published limits.

Our latest MAXESS Royal Groove fragment measured approximately **39 KB / 188 lines** at build time while still passing the complete structural release gate. That is evidence that a compact native artifact can contain the entire intended experience without dragging legacy code into Groove.

---

# 12. FULL-BLEED LAW

Groove can provide a host container whose width is not identical to the viewport.

For immersive pages we therefore define a deliberate full-bleed contract.

Preferred approach:

1. unique root;
2. root width contract;
3. responsive internal shell;
4. controlled breakout only when necessary;
5. verify against the real published Groove page.

Do not assume `width:100vw` is always safe. It can create horizontal overflow depending on scrollbar/host layout behavior.

The correct solution is **tested full bleed**, not ideological full bleed.

---

# 13. DATA AND STATE LAW

For personalized MAXESS pages:

### Preferred priority

1. Explicit Result Contract from the assessment flow.
2. Controlled URL result payload when necessary.
3. Controlled session storage/local storage where appropriate.
4. Safe empty state when data is missing.

### Never

- invent scores;
- silently use fake defaults as though they were real;
- overwrite real results with preview data;
- assume a browser storage value is trustworthy without validation.

Normalize every incoming value before rendering.

---

# 14. SECURITY LAW

The embed runs in the user's browser.

Therefore:

- never ship API keys;
- never ship secret tokens;
- never put private credentials in JavaScript;
- validate data before using it in the DOM;
- escape user-controlled text when inserting into HTML;
- minimize third-party scripts;
- use HTTPS resources;
- avoid unnecessary external requests;
- never trust query parameters as authenticated data.

A public embed is public code.

---

# 15. SEO LAW

Do not assume an embed fragment provides the same SEO behavior as native page content.

Important page-level SEO elements should remain in Groove's page settings where possible:

- title;
- meta description;
- Open Graph metadata;
- canonical strategy;
- crawl/index settings.

Use embed code primarily for the experience layer.

GroovePages publicly advertises built-in SEO optimization and custom code integration, so the strongest architecture uses Groove's page-level SEO capabilities plus our custom embedded experience. [GroovePages](https://groove.cm/groove-pages)

---

# 16. ACCESSIBILITY LAW

A premium visual experience must remain usable.

Required checks:

- keyboard navigation;
- focus visibility;
- readable type sizes;
- meaningful heading hierarchy;
- action labels;
- reduced-motion behavior;
- mobile touch targets;
- no color-only meaning;
- no text embedded only inside images;
- screen-reader sensible structure where practical.

The goal is **AAA visual quality without sacrificing human accessibility.**

---

# 17. RELEASE ARTIFACT LAW

The exact code Shawn pastes into Groove is itself a release artifact.

Therefore:

- store it in GitHub;
- version it;
- test it;
- inspect it;
- provide a raw GitHub link;
- never require Shawn to merge files manually;
- never tell Shawn to paste a development-only source file when the release artifact is different.

The raw link must point to the actual current Groove delivery artifact.

---

# 18. MASTER + OSCAR BUILD LOOP FOR GROOVE

Every significant Groove page follows this cycle:

### MASTER
Understand the entire system, laws, source, user goal, and deployment environment.

### INVENTORY
List:

- source files;
- current version;
- dependencies;
- data contracts;
- assets;
- runtime states;
- known bugs;
- current release status;
- current public URL.

### BUILD
Create the strongest version that fits the Groove runtime.

### SCORE
Score every material area from 0–10.

### OSCAR
Attack every score below 10.

### FIX
Fix the highest-impact weaknesses first.

### RETEST
Repeat the same tests.

### RELEASE
Only after the source and delivery artifact both pass.

### LIVE VERIFY
The Groove URL must actually be opened/tested before claiming the page is live/verified.

This directly follows the Naya execution procedure and Oscar quality gate. See `.naya/04-EXECUTION-PROCEDURE.md` and `.naya/05-QUALITY-AND-OSCAR.md`.

---

# 19. GROOVE 10/10 SCORECARD

The following scorecard is the default evaluation framework for a major Groove embed page.

| Area | Current Score | Why it is not yet a 10 | 10/10 action |
|---|---:|---|---|
| Runtime compatibility | 8.5 | Source is verified; actual public Groove rendering still requires human live verification | Paste the current raw artifact into the real Groove page, publish, and inspect desktop/tablet/mobile behavior |
| Embed architecture | 9.5 | Architecture is now correct, but it must remain regression-protected | Keep a dedicated native fragment generator and forbid shell/legacy DOM/iframe leakage |
| Visual quality | 9.0 | Royal system is strong, but pixel-level live validation can reveal spacing/scale differences caused by Groove's host container | Compare rendered public page against the design target and tune only from real evidence |
| Responsive quality | 8.5 | Static responsive rules pass, but actual Groove breakpoints and container behavior need live testing | Test real published page across mobile/tablet/desktop and fix breakpoint-specific issues |
| Performance | 9.0 | Current fragment is compact, but browser runtime and asset behavior are not fully measured on live Groove | Profile first render, long-page scroll, animation cost, and network activity; remove any avoidable work |
| Data integrity | 9.5 | Contract validation is strong; full end-to-end assessment→Groove test remains necessary | Run a real assessment, pass a real Result Contract, refresh, and verify the exact user result remains correct |
| Interaction | 8.5 | Static source confirms controls, but live behavior has not yet been exhaustively tested | Exercise every button, link, share/copy/print action, missing-data state, and resize path on the published page |
| Accessibility | 8.5 | Structural support exists, but live keyboard/screen-reader testing remains incomplete | Perform keyboard-only and reduced-motion checks on the live Groove page |
| Maintainability | 9.0 | Delivery is generated correctly, but the repo contains historical workflow complexity that should be simplified | Keep one authoritative release path and archive/deactivate obsolete competing workflows |
| Release confidence | 8.0 | GitHub release gate passes, but Groove deployment itself has not been confirmed by live testing in this build cycle | Publish, open the real URL, compare source→render, and record LIVE VERIFIED only after evidence |

### CURRENT OVERALL

**8.8 / 10 pre-live engineering confidence**

This is intentionally not a 10.

The missing points are not because the source artifact is weak. They are mostly because the final runtime is Groove's published environment and that requires actual live verification.

---

# 20. HOW WE TURN THE 8.8 INTO 10

## Step 1 — Live runtime verification

Publish the current native fragment in the real Groove page.

## Step 2 — Render inventory

Check:

- outer width;
- page gutters;
- hero height;
- section spacing;
- typography;
- overflow;
- scroll height;
- button alignment;
- cards;
- Naya section;
- 18 Masters;
- final CTA.

## Step 3 — Functional inventory

Exercise:

- result loading;
- missing result state;
- query payload;
- session state;
- copy;
- share;
- print;
- navigation;
- responsive resize.

## Step 4 — Oscar attack

Ask:

- What is confusing?
- What feels dead?
- What feels repetitive?
- What is too centered?
- What is too narrow?
- What is too small?
- What is too decorative?
- What is missing?
- What feels like a builder rather than a product?
- Where does the page lose emotional momentum?

## Step 5 — Fix the highest-impact failures

Do not randomly polish everything.

Use impact order:

**broken > confusing > visually weak > inefficient > merely imperfect**

## Step 6 — Re-run the exact same checks

A 10 requires evidence after the fix, not confidence before the fix.

---

# 21. THE MAXIMUM-OUTPUT GROOVE BUILD STANDARD

When the goal is an extraordinary page, use this architecture:

```text
GROOVE PAGE
└── ONE PRIMARY CODE EMBED
    ├── release marker
    ├── unique application root
    ├── tokenized design system
    ├── responsive layout system
    ├── semantic content structure
    ├── data contract
    ├── runtime normalizer
    ├── presentation engine
    ├── visual engine
    ├── interaction engine
    ├── accessibility layer
    ├── failure states
    └── lightweight diagnostics
```

Then use Groove itself for the parts Groove is better at:

- domain;
- page/funnel structure;
- page-level SEO;
- native Groove integrations;
- publishing;
- platform-level analytics where appropriate.

Use our embed for the parts where custom code gives us leverage:

- brand experience;
- interaction;
- personalization;
- visualization;
- custom storytelling;
- app-like behavior.

This is the strongest division of labor.

---

# 22. BUILD FOR EXTRAORDINARY OUTPUT, NOT MINIMUM COMPLIANCE

A Groove embed is allowed to be sophisticated.

The fact that it is inserted into a page builder does **not** mean it should look like a page-builder widget.

Our target is:

> **The user should feel that they entered a premium product, not that they encountered a chunk of custom code inside a funnel builder.**

That means:

- visual continuity;
- edge-to-edge confidence;
- intentional pacing;
- strong hierarchy;
- alive motion;
- excellent typography;
- meaningful data visualization;
- human language;
- no unexplained boxes;
- no dead space;
- no accidental chrome;
- no obvious implementation artifacts.

---

# 23. REGRESSION LESSONS LOCKED FROM THE RECENT RESULTS FAILURE

The recent MAXESS Results issue produced the following permanent lessons:

1. A standalone HTML document is not automatically a correct Groove embed artifact.
2. Hidden legacy content is still technical debt inside the delivered artifact.
3. A nested iframe is an architectural choice, not a harmless implementation detail.
4. Code-size expectations must never replace functional verification.
5. A smaller artifact can be better engineering when dead code is removed.
6. The release gate must test the exact artifact that Shawn will paste.
7. The raw GitHub link must point to the exact release artifact, not merely a development source file.
8. GitHub Actions success proves source-level checks, not Groove live deployment.
9. Final quality requires actual public Groove verification.
10. When a live page fails, trace the source→artifact→Groove handoff before rewriting good product code.

---

# 24. NAYA'S DEFAULT GROOVE DECISION TREE

When asked to build something for Groove:

### A. Is it a page-level experience?

Yes → prefer one authoritative native embed artifact.

### B. Does it need server-side secrets or secure processing?

Yes → move that logic to a backend/service; never ship secrets in the embed.

### C. Does it need advanced visual/interactive behavior?

Yes → use custom HTML/CSS/JS aggressively but deliberately.

### D. Does it need Groove-native marketing functionality?

Yes → let Groove handle the relevant platform feature and let the embed handle the custom experience layer.

### E. Does it need an iframe?

Only if there is a real isolation/integration reason.

### F. Is there a documented Groove limit?

Use it.

### G. Is there no documented limit?

Do not invent one. Establish a tested engineering budget and record the evidence.

---

# 25. MASTER RULE

**Know the runtime. Design for the runtime. Build for the runtime. Test the runtime.**

Do not build a generic website and hope Groove can contain it.

Build a Groove-native application experience from the beginning.

That is how we get the highest possible output from the platform.

---

# 26. CURRENT RELEASE STATUS

For the current MAXESS Results experience:

- Standalone Royal source: release-gated.
- Groove-native artifact: release-gated.
- Native artifact measured approximately 39 KB / 188 lines at build time.
- No iframe tag in the native artifact.
- No legacy Results root in the native artifact.
- No legacy NayaNET frame in the native artifact.
- Royal Results structure present.
- Five dimensions present.
- 18 Naya Masters present.
- Result Contract marker present.
- Full-bleed contract present.
- Actual Groove live deployment still requires human publication and live verification.

Never describe the final public page as LIVE VERIFIED until that last step has actually occurred.

---

# 27. SOURCE NOTES

Primary/current:

- [GroovePages official product page](https://groove.cm/groove-pages)
- [Groove.cm → Scale.gg transition announcement](https://www.groove.cm/)

Supporting implementation evidence:

- [Prefinery: installing a JavaScript/embed signup form in GroovePages](https://help.prefinery.com/article/273-how-to-install-the-signup-form-on-groovepages-groove-cm)
- [POWR: adding an embed snippet to GroovePages](https://www.powr.io/tabs-for-groovepages-how-to-add-to-your-site)
- [Technical article documenting Groove custom-HTML iframe behavior](https://thegroovepreneur.com/blog/post/start-a-blog-with-grooveblog)

Source discipline:

- Official Groove material is preferred for current product capabilities and platform status.
- Third-party material is used only as implementation evidence where official public documentation is sparse.
- Unsupported numeric limits are not presented as vendor facts.
