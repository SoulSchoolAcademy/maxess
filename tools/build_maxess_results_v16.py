from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FOUNDATION = ROOT / "nayanetpagecode"
OUTPUT = ROOT / "MAXESS-RESULTS-10-GROOVE.html"

TOWER = r'''<!-- MAXESS RESULTS V16 TOWER — UPDATED EDITED FILE — NOT YET AUTHORITATIVE -->
<section id="maxess-results-v16" class="mxv16" data-contract="MAXESS-RESULTS-CONTRACT-1" data-result-state="loading" aria-label="MAXESS personal AI mastery report">
  <div class="mxv16__status" data-status role="status" aria-live="polite">
    <div class="mxv16__status-card">
      <div class="mxv16__status-orb" aria-hidden="true"></div>
      <h1 data-status-title>Preparing your report…</h1>
      <p data-status-copy>Reading your completed MAXESS result.</p>
    </div>
  </div>

  <div class="mxv16__report" data-report hidden>
    <header class="mxv16__hero" id="mxv16-score">
      <div class="mxv16__hero-inner">
        <div class="mxv16__hero-copy">
          <span class="mxv16__eyebrow">MAXESS AI MASTERY ASSESSMENT</span>
          <h1>YOUR AI SCORE</h1>
          <p class="mxv16__hero-sub">A snapshot of how you currently direct, communicate with, evaluate, improve, and systematize AI.</p>
          <div class="mxv16__hero-meta">
            <span data-profile-name>YOUR REPORT</span>
            <span aria-hidden="true">•</span>
            <span data-assessment-name>AI MASTERY ASSESSMENT</span>
          </div>
          <a class="mxv16__button mxv16__button--primary" href="#mxv16-pattern">See my pattern <span aria-hidden="true">↓</span></a>
        </div>

        <div class="mxv16__orb-wrap" aria-label="Your validated AI score">
          <div class="mxv16__orb" data-orb role="img" aria-label="AI score visualization">
            <div class="mxv16__orb-ring mxv16__orb-ring--outer"></div>
            <div class="mxv16__orb-ring mxv16__orb-ring--inner"></div>
            <div class="mxv16__orb-core">
              <span class="mxv16__score" data-score>—</span>
              <span class="mxv16__score-label">OUT OF 100</span>
            </div>
          </div>
          <div class="mxv16__band" data-band>—</div>
          <p class="mxv16__sr-only" data-score-text></p>
        </div>

        <aside class="mxv16__hero-guide" aria-label="Naya interpretation">
          <div class="mxv16__naya-mini">
            <img data-naya-image src="https://i.postimg.cc/RF3XFWJ7/grok-image-c6a924fd-1f75-4ac8-840d-35b224fb3e52.jpg" alt="Naya, your AI guide" loading="lazy">
            <div><strong>NAYA</strong><span>YOUR AI GUIDE</span></div>
          </div>
          <p data-hero-meaning>Your score is the summary. The interesting part is what the shape of your result tells you about how you work.</p>
        </aside>
      </div>
    </header>

    <main>
      <section class="mxv16__chapter mxv16__chapter--light" id="mxv16-profile" aria-labelledby="mxv16-profile-title">
        <div class="mxv16__wide mxv16__profile-grid">
          <div>
            <span class="mxv16__chapter-number">01</span>
            <h2 id="mxv16-profile-title">YOUR REPORT</h2>
            <p class="mxv16__lead">This is not a judgment. It is a map of your current AI capability — built from the result you actually earned.</p>
          </div>
          <div class="mxv16__profile-card">
            <span class="mxv16__eyebrow mxv16__eyebrow--dark">PERSONAL PROFILE</span>
            <div class="mxv16__profile-name" data-profile-name>YOUR REPORT</div>
            <div class="mxv16__profile-role" data-profile-role>MAXESS participant</div>
            <div class="mxv16__profile-line"><span>Assessment</span><strong data-assessment-name>AI Mastery Assessment</strong></div>
            <div class="mxv16__profile-line"><span>Assessment version</span><strong data-assessment-version>—</strong></div>
          </div>
        </div>
      </section>

      <section class="mxv16__chapter mxv16__chapter--dark" id="mxv16-pattern" aria-labelledby="mxv16-pattern-title">
        <div class="mxv16__wide">
          <div class="mxv16__section-head">
            <div><span class="mxv16__chapter-number">02</span><h2 id="mxv16-pattern-title">THE PATTERN</h2></div>
            <p>The score tells you where you are. The pattern tells you how the pieces relate.</p>
          </div>
          <div class="mxv16__pattern-grid">
            <div class="mxv16__pattern-visual">
              <svg data-pattern viewBox="0 0 520 460" role="img" aria-labelledby="mxv16-pattern-svg-title mxv16-pattern-svg-desc">
                <title id="mxv16-pattern-svg-title">Your five-dimension AI capability pattern</title>
                <desc id="mxv16-pattern-svg-desc">A five-axis profile showing the relative scores of your validated MAXESS dimensions.</desc>
              </svg>
            </div>
            <div class="mxv16__pattern-copy">
              <div class="mxv16__pattern-summary"><strong data-pattern-summary>—</strong><span>YOUR CURRENT SHAPE</span></div>
              <p data-pattern-copy>—</p>
              <div class="mxv16__pattern-legend" data-pattern-legend></div>
            </div>
          </div>
        </div>
      </section>

      <section class="mxv16__chapter mxv16__chapter--light" id="mxv16-dimensions" aria-labelledby="mxv16-dimensions-title">
        <div class="mxv16__wide">
          <div class="mxv16__section-head mxv16__section-head--dark">
            <div><span class="mxv16__chapter-number">03</span><h2 id="mxv16-dimensions-title">YOUR FIVE DIMENSIONS</h2></div>
            <p>Each score is evidence. Together they explain the way you currently work with AI.</p>
          </div>
          <div class="mxv16__dimensions" data-dimensions></div>
        </div>
      </section>

      <section class="mxv16__chapter mxv16__chapter--dark" id="mxv16-meaning" aria-labelledby="mxv16-meaning-title">
        <div class="mxv16__wide">
          <div class="mxv16__section-head">
            <div><span class="mxv16__chapter-number">04</span><h2 id="mxv16-meaning-title">WHAT IT MEANS</h2></div>
            <p>Naya turns the measurement into something you can actually use.</p>
          </div>
          <div class="mxv16__naya-report">
            <div class="mxv16__naya-portrait"><img data-naya-image src="https://i.postimg.cc/d1nncN9F/Naya-and-shawn-ok-44-a.png" alt="Naya guiding your MAXESS report" loading="lazy"></div>
            <div><span class="mxv16__eyebrow">NAYA'S READ</span><p class="mxv16__naya-quote" data-naya-interpretation>—</p><p class="mxv16__naya-detail" data-naya-detail>—</p></div>
          </div>
        </div>
      </section>

      <section class="mxv16__chapter mxv16__chapter--light" id="mxv16-strength" aria-labelledby="mxv16-strength-title">
        <div class="mxv16__wide mxv16__two-col">
          <div class="mxv16__feature mxv16__feature--strength">
            <span class="mxv16__eyebrow mxv16__eyebrow--dark">05 · YOUR STRONGEST SIGNAL</span>
            <div class="mxv16__feature-score" data-strongest-score>—</div>
            <h2 id="mxv16-strength-title" data-strongest-name>—</h2>
            <p data-strongest-copy>—</p>
            <span class="mxv16__feature-note">This is an asset to build from.</span>
          </div>
          <div class="mxv16__feature mxv16__feature--lever" id="mxv16-lever">
            <span class="mxv16__eyebrow mxv16__eyebrow--dark">06 · YOUR BIGGEST LEVER</span>
            <div class="mxv16__feature-score" data-lever-score>—</div>
            <h2 data-lever-name>—</h2>
            <p data-lever-copy>—</p>
            <span class="mxv16__feature-note">Improvement here is the clearest useful opportunity.</span>
          </div>
        </div>
      </section>

      <section class="mxv16__chapter mxv16__chapter--dark" id="mxv16-next" aria-labelledby="mxv16-next-title">
        <div class="mxv16__wide">
          <div class="mxv16__section-head">
            <div><span class="mxv16__chapter-number">07</span><h2 id="mxv16-next-title">YOUR NEXT MOVE</h2></div>
            <p>One focused move beats ten scattered improvements.</p>
          </div>
          <div class="mxv16__next-card">
            <div class="mxv16__next-index">01</div>
            <div><span class="mxv16__eyebrow">START HERE</span><h3 data-next-title>—</h3><p data-next-copy>—</p></div>
          </div>
          <div class="mxv16__process" aria-label="The MAXESS improvement process">
            <span>KNOW</span><i>→</i><span>TELL</span><i>→</i><span>ASK</span><i>→</i><span>CREATE</span><i>→</i><span>SCORE</span><i>→</i><span>IMPROVE</span><i>→</i><span>REPEAT</span>
          </div>
        </div>
      </section>

      <section class="mxv16__chapter mxv16__chapter--light" id="mxv16-masters" aria-labelledby="mxv16-masters-title">
        <div class="mxv16__wide">
          <div class="mxv16__section-head mxv16__section-head--dark">
            <div><span class="mxv16__chapter-number">08</span><h2 id="mxv16-masters-title">18 NAYA MASTERS</h2></div>
            <p>These are capability pathways — not a list of tools. Your result determines where the strongest next connections are.</p>
          </div>
          <div class="mxv16__masters" data-masters></div>
        </div>
      </section>

      <section class="mxv16__chapter mxv16__chapter--dark" id="mxv16-system" aria-labelledby="mxv16-system-title">
        <div class="mxv16__wide mxv16__system-grid">
          <div>
            <span class="mxv16__chapter-number">09</span>
            <h2 id="mxv16-system-title">THE SYSTEM</h2>
            <p class="mxv16__lead">Your assessment is the beginning of a development system. Measure → understand → practice → improve → repeat.</p>
          </div>
          <div class="mxv16__system-stack">
            <div><strong>YOUR RESULT</strong><span>Where you are now.</span></div>
            <div><strong>YOUR PATH</strong><span>What deserves attention next.</span></div>
            <div><strong>YOUR PRACTICE</strong><span>How capability becomes repeatable.</span></div>
          </div>
        </div>
      </section>

      <section class="mxv16__chapter mxv16__chapter--light" id="mxv16-video" aria-labelledby="mxv16-video-title">
        <div class="mxv16__wide mxv16__video-grid">
          <div>
            <span class="mxv16__eyebrow mxv16__eyebrow--dark">THE NEXT CHAPTER</span>
            <h2 id="mxv16-video-title">Turn the insight into capability.</h2>
            <p class="mxv16__lead">The report tells you where to focus. The larger MAXESS/Naya system is where you can practice, build, and compound that capability.</p>
          </div>
          <div class="mxv16__video-shell">
            <div class="mxv16__video-placeholder">
              <span>YOUR RESULT COMES FIRST</span>
              <strong>The existing NayaNET foundation remains directly below this Results tower.</strong>
              <small>Any foundation video continues to work independently.</small>
            </div>
          </div>
        </div>
      </section>

      <section class="mxv16__chapter mxv16__chapter--final" id="mxv16-final" aria-labelledby="mxv16-final-title">
        <div class="mxv16__final-inner">
          <span class="mxv16__eyebrow">10 · YOUR NEXT CHAPTER</span>
          <h2 id="mxv16-final-title">You know where you are. Now build from it.</h2>
          <p>Use the result as a starting point, not a ceiling. Choose one useful capability, apply the process, and let the next result teach you what to improve.</p>
          <div class="mxv16__final-actions">
            <a class="mxv16__button mxv16__button--primary" href="#mxv16-masters">Explore my pathways <span aria-hidden="true">→</span></a>
            <button class="mxv16__button mxv16__button--quiet" type="button" data-print>Save / print my report</button>
          </div>
        </div>
      </section>
    </main>
  </div>
</section>

<style id="maxess-results-v16-css">
#maxess-results-v16.mxv16{--mxv16-bg:#050507;--mxv16-ink:#0a0a0e;--mxv16-white:#fff;--mxv16-muted:#a9a7b2;--mxv16-purple:#9a62ff;--mxv16-cyan:#45e5ff;--mxv16-green:#39df91;--mxv16-gold:#ffd45a;--mxv16-orange:#ff9d3d;--mxv16-blue:#4c9dff;--mxv16-magenta:#ef4bc8;display:block;position:relative;isolation:isolate;width:100%;overflow:clip;background:var(--mxv16-bg);color:#fff;font-family:Inter,ui-sans-serif,system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif}
#maxess-results-v16.mxv16 *{box-sizing:border-box}
#maxess-results-v16.mxv16 a,#maxess-results-v16.mxv16 button{font:inherit}
#maxess-results-v16.mxv16 a{color:inherit;text-decoration:none}
#maxess-results-v16.mxv16 button{border:0}
#maxess-results-v16.mxv16 :focus-visible{outline:3px solid #fff;outline-offset:4px}
#maxess-results-v16 .mxv16__sr-only{position:absolute!important;width:1px!important;height:1px!important;padding:0!important;margin:-1px!important;overflow:hidden!important;clip:rect(0,0,0,0)!important;white-space:nowrap!important;border:0!important}
#maxess-results-v16 .mxv16__wide{width:min(1440px,92vw);margin-inline:auto}
#maxess-results-v16 .mxv16__hero{background:radial-gradient(circle at 50% 45%,rgba(122,74,236,.19),transparent 28%),radial-gradient(circle at 78% 20%,rgba(69,229,255,.08),transparent 25%),linear-gradient(180deg,#020204,#07040c 72%,#050507);padding:clamp(48px,7vw,100px) 0 clamp(58px,7vw,104px)}
#maxess-results-v16 .mxv16__hero-inner{width:min(1540px,94vw);margin:auto;display:grid;grid-template-columns:minmax(0,1fr) minmax(330px,560px) minmax(260px,.75fr);align-items:center;gap:clamp(28px,5vw,80px)}
#maxess-results-v16 .mxv16__eyebrow{display:inline-block;color:#cbb7ff;font-size:11px;font-weight:900;letter-spacing:.19em;text-transform:uppercase}
#maxess-results-v16 .mxv16__eyebrow--dark{color:#6f43ae}
#maxess-results-v16 .mxv16__hero h1{margin:14px 0 0;font-size:clamp(54px,7vw,112px);line-height:.88;letter-spacing:-.065em;font-weight:950}
#maxess-results-v16 .mxv16__hero-sub{max-width:660px;margin:24px 0 0;color:rgba(255,255,255,.72);font-size:clamp(16px,1.45vw,20px);line-height:1.55}
#maxess-results-v16 .mxv16__hero-meta{display:flex;flex-wrap:wrap;gap:10px;margin-top:18px;color:#aaa7b3;font-size:10px;font-weight:850;letter-spacing:.08em;text-transform:uppercase}
#maxess-results-v16 .mxv16__button{display:inline-flex;align-items:center;justify-content:center;gap:10px;min-height:54px;padding:0 21px;border-radius:17px;cursor:pointer;font-weight:900;transition:transform .2s ease,box-shadow .2s ease,border-color .2s ease;background:transparent;color:inherit}
#maxess-results-v16 .mxv16__button:hover{transform:translateY(-2px)}
#maxess-results-v16 .mxv16__button--primary{margin-top:28px;color:#09070e;background:linear-gradient(135deg,#fff,#e9dcff 40%,#c4a0ff 72%,#fff0a8);border:1px solid #f0e4ff;box-shadow:0 14px 35px rgba(0,0,0,.4),0 0 38px rgba(154,98,255,.2)}
#maxess-results-v16 .mxv16__button--quiet{color:#16121d;background:#fff;border:1px solid #cfc4dc}
#maxess-results-v16 .mxv16__orb-wrap{display:grid;place-items:center;text-align:center}
#maxess-results-v16 .mxv16__orb{--score-progress:0%;--score-a:#9a62ff;--score-b:#45e5ff;position:relative;width:min(560px,42vw);aspect-ratio:1;border-radius:50%;display:grid;place-items:center;background:radial-gradient(circle at 32% 22%,rgba(255,255,255,.26),rgba(255,255,255,.03) 17%,transparent 33%),radial-gradient(circle at 50% 50%,rgba(69,229,255,.13),rgba(154,98,255,.1) 42%,#030308 72%);box-shadow:0 0 0 1px rgba(255,255,255,.18),inset 0 0 80px rgba(69,229,255,.12),0 45px 120px rgba(0,0,0,.72),0 0 120px color-mix(in srgb,var(--score-a) 18%,transparent);transform:translateZ(0)}
#maxess-results-v16 .mxv16__orb::before{content:"";position:absolute;inset:-7%;border-radius:50%;background:conic-gradient(from -90deg,var(--score-a) 0 var(--score-progress),rgba(255,255,255,.06) var(--score-progress) 100%);-webkit-mask:radial-gradient(farthest-side,transparent calc(100% - 4px),#000 calc(100% - 3px));mask:radial-gradient(farthest-side,transparent calc(100% - 4px),#000 calc(100% - 3px));filter:drop-shadow(0 0 12px color-mix(in srgb,var(--score-a) 55%,transparent))}
#maxess-results-v16 .mxv16__orb::after{content:"";position:absolute;inset:7%;border-radius:50%;border:1px solid color-mix(in srgb,var(--score-b) 34%,transparent);box-shadow:0 0 50px color-mix(in srgb,var(--score-b) 12%,transparent)}
#maxess-results-v16 .mxv16__orb-ring{position:absolute;border-radius:50%;border:1px solid rgba(255,255,255,.08);pointer-events:none}
#maxess-results-v16 .mxv16__orb-ring--outer{inset:13%;border-left-color:color-mix(in srgb,var(--score-b) 45%,transparent);transform:rotate(18deg)}
#maxess-results-v16 .mxv16__orb-ring--inner{inset:25%;border-right-color:color-mix(in srgb,var(--score-a) 50%,transparent);transform:rotate(-23deg)}
#maxess-results-v16 .mxv16__orb-core{position:relative;z-index:2;width:54%;aspect-ratio:1;border-radius:50%;display:grid;place-items:center;align-content:center;background:radial-gradient(circle at 32% 24%,rgba(255,255,255,.16),rgba(13,12,20,.82) 42%,#020207 76%);border:1px solid rgba(255,255,255,.14);box-shadow:inset 0 0 50px rgba(154,98,255,.15)}
#maxess-results-v16 .mxv16__score{font-size:clamp(72px,9vw,138px);line-height:.82;letter-spacing:-.08em;font-weight:950;background:linear-gradient(115deg,var(--score-a),var(--score-b));-webkit-background-clip:text;background-clip:text;color:transparent}
#maxess-results-v16 .mxv16__score-label{margin-top:12px;color:#8d8995;font-size:9px;font-weight:900;letter-spacing:.2em}
#maxess-results-v16 .mxv16__band{margin-top:22px;min-height:36px;padding:9px 16px;border:1px solid color-mix(in srgb,var(--score-a) 55%,white 8%);border-radius:999px;background:color-mix(in srgb,var(--score-a) 8%,#050507);font-size:12px;font-weight:900;letter-spacing:.08em;text-transform:uppercase}
#maxess-results-v16 .mxv16__hero-guide{align-self:center;padding:24px;border:1px solid rgba(255,255,255,.11);border-radius:26px;background:linear-gradient(145deg,rgba(255,255,255,.06),rgba(255,255,255,.015));box-shadow:inset 0 1px rgba(255,255,255,.08),0 25px 65px rgba(0,0,0,.3)}
#maxess-results-v16 .mxv16__naya-mini{display:flex;align-items:center;gap:13px}.mxv16__naya-mini img{width:52px;height:52px;border-radius:50%;object-fit:cover;border:1px solid rgba(255,255,255,.5);box-shadow:0 0 25px rgba(154,98,255,.22)}
#maxess-results-v16 .mxv16__naya-mini strong,#maxess-results-v16 .mxv16__naya-mini span{display:block}.mxv16__naya-mini strong{font-size:15px;letter-spacing:.14em}.mxv16__naya-mini span{margin-top:4px;color:#8f8a97;font-size:9px;font-weight:800;letter-spacing:.1em}
#maxess-results-v16 .mxv16__hero-guide p{margin:18px 0 0;color:#d8d4df;font-size:15px;line-height:1.55}
#maxess-results-v16 .mxv16__chapter{padding:clamp(64px,8vw,116px) 0;scroll-margin-top:18px}.mxv16__chapter--light{background:#fff;color:#09090d}.mxv16__chapter--dark{background:#050507;color:#fff}.mxv16__chapter--final{background:radial-gradient(circle at 50% 0,rgba(154,98,255,.25),transparent 38%),linear-gradient(180deg,#0b0612,#020204);color:#fff}
#maxess-results-v16 .mxv16__chapter-number{display:block;color:#8f62d4;font-size:12px;font-weight:950;letter-spacing:.18em;margin-bottom:8px}.mxv16__chapter--dark .mxv16__chapter-number{color:#b996ff}
#maxess-results-v16 .mxv16__section-head{display:grid;grid-template-columns:minmax(0,1.2fr) minmax(260px,.8fr);gap:40px;align-items:end;margin-bottom:42px}.mxv16__section-head h2,.mxv16__section-head p{margin:0}.mxv16__section-head h2{font-size:clamp(40px,5.3vw,76px);line-height:.94;letter-spacing:-.06em;font-weight:950}.mxv16__section-head p{color:rgba(255,255,255,.66);font-size:16px;line-height:1.6}.mxv16__section-head--dark p{color:#4b4850}
#maxess-results-v16 .mxv16__lead{max-width:760px;color:rgba(255,255,255,.72);font-size:clamp(17px,1.6vw,21px);line-height:1.6}.mxv16__chapter--light .mxv16__lead{color:#46434a}
#maxess-results-v16 .mxv16__profile-grid{display:grid;grid-template-columns:minmax(0,1fr) minmax(320px,.72fr);gap:clamp(30px,7vw,100px);align-items:center}.mxv16__profile-grid h2{margin:0;font-size:clamp(52px,6.5vw,92px);line-height:.9;letter-spacing:-.065em;font-weight:950}.mxv16__profile-card{padding:30px;border:1px solid #ded9e4;border-radius:28px;background:#fbfafc;box-shadow:0 22px 60px rgba(20,10,30,.08)}.mxv16__profile-name{margin-top:18px;font-size:28px;font-weight:950;letter-spacing:-.03em}.mxv16__profile-role{margin-top:5px;color:#6e6875;font-size:14px}.mxv16__profile-line{display:flex;justify-content:space-between;gap:20px;padding-top:15px;margin-top:15px;border-top:1px solid #e9e5ec;font-size:12px}.mxv16__profile-line span{color:#77727c}.mxv16__profile-line strong{text-align:right}
#maxess-results-v16 .mxv16__pattern-grid{display:grid;grid-template-columns:minmax(360px,1fr) minmax(280px,.72fr);gap:clamp(28px,7vw,100px);align-items:center}.mxv16__pattern-visual{min-width:0;padding:18px;border:1px solid rgba(255,255,255,.08);border-radius:30px;background:radial-gradient(circle at 50% 50%,rgba(154,98,255,.12),transparent 55%),#08080d}.mxv16__pattern-visual svg{display:block;width:100%;height:auto}.mxv16__pattern-visual .grid{fill:none;stroke:rgba(255,255,255,.12);stroke-width:1}.mxv16__pattern-visual .axis{stroke:rgba(255,255,255,.08);stroke-width:1}.mxv16__pattern-visual .shape{fill:rgba(154,98,255,.18);stroke:#c2a2ff;stroke-width:3;filter:drop-shadow(0 0 10px rgba(154,98,255,.25))}.mxv16__pattern-visual .node{fill:#fff;stroke:#c2a2ff;stroke-width:3}.mxv16__pattern-visual text{fill:#c8c3ce;font-size:12px;font-weight:800}.mxv16__pattern-summary strong{display:block;font-size:clamp(42px,5vw,72px);line-height:.95;letter-spacing:-.06em}.mxv16__pattern-summary span{display:block;margin-top:9px;color:#8f8997;font-size:10px;font-weight:900;letter-spacing:.17em}.mxv16__pattern-copy>p{margin:22px 0 0;color:#c4becb;font-size:17px;line-height:1.65}.mxv16__pattern-legend{display:grid;gap:8px;margin-top:26px}.mxv16__legend-row{display:grid;grid-template-columns:10px 1fr auto;gap:10px;align-items:center;font-size:12px}.mxv16__legend-dot{width:10px;height:10px;border-radius:50%;background:var(--dot);box-shadow:0 0 10px color-mix(in srgb,var(--dot) 40%,transparent)}.mxv16__legend-row strong{font-weight:850}.mxv16__legend-row span:last-child{color:#a7a1ae;font-weight:900}
#maxess-results-v16 .mxv16__dimensions{display:grid;grid-template-columns:repeat(5,minmax(0,1fr));gap:16px}.mxv16__dimension{min-width:0;padding:24px 16px 22px;border:1px solid #e2dee6;border-radius:28px;background:#fff;box-shadow:0 18px 45px rgba(20,10,30,.07)}.mxv16__gauge{--gauge:#9a62ff;--value:0%;width:116px;aspect-ratio:1;margin:0 auto 20px;display:grid;place-items:center;border-radius:50%;background:conic-gradient(var(--gauge) var(--value),#eeeaf1 var(--value));position:relative}.mxv16__gauge::after{content:"";position:absolute;inset:9px;border-radius:50%;background:#fff;border:1px solid #eeeaf1}.mxv16__gauge-score{position:relative;z-index:1;font-size:28px;font-weight:950;letter-spacing:-.05em}.mxv16__dimension h3{margin:0;font-size:17px;line-height:1.15;text-align:center}.mxv16__dimension-level{margin-top:7px;text-align:center;color:#76717b;font-size:9px;font-weight:900;letter-spacing:.12em;text-transform:uppercase}.mxv16__dimension p{margin:15px 0 0;color:#55515a;font-size:12px;line-height:1.5}.mxv16__dimension-lever{margin-top:12px;padding-top:12px;border-top:1px solid #eeeaf1;color:#6a356f;font-size:11px;line-height:1.45}.mxv16__dimension-lever strong{display:block;margin-bottom:4px;color:#19151d;font-size:9px;letter-spacing:.1em;text-transform:uppercase}
#maxess-results-v16 .mxv16__naya-report{display:grid;grid-template-columns:220px 1fr;gap:clamp(28px,6vw,76px);align-items:center;padding:clamp(28px,5vw,58px);border:1px solid rgba(255,255,255,.11);border-radius:34px;background:radial-gradient(circle at 15% 50%,rgba(154,98,255,.18),transparent 34%),linear-gradient(145deg,#15101d,#08080c);box-shadow:0 30px 90px rgba(0,0,0,.35)}.mxv16__naya-portrait img{width:100%;aspect-ratio:1;object-fit:cover;border-radius:50%;border:1px solid rgba(255,255,255,.25);box-shadow:0 0 60px rgba(154,98,255,.18)}.mxv16__naya-quote{margin:16px 0 0;max-width:850px;color:#fff;font-size:clamp(28px,4.2vw,58px);line-height:1.03;letter-spacing:-.045em;font-weight:900}.mxv16__naya-detail{max-width:820px;margin:20px 0 0;color:#bbb4c5;font-size:16px;line-height:1.65}
#maxess-results-v16 .mxv16__two-col{display:grid;grid-template-columns:1fr 1fr;gap:18px}.mxv16__feature{min-height:360px;padding:34px;border-radius:32px;display:flex;flex-direction:column;justify-content:flex-end;border:1px solid #e1dce5;background:#fff;box-shadow:0 22px 60px rgba(20,10,30,.08)}.mxv16__feature--strength{background:linear-gradient(145deg,#f4fff9,#fff)}.mxv16__feature--lever{background:linear-gradient(145deg,#fffaf0,#fff)}.mxv16__feature-score{font-size:84px;line-height:.85;letter-spacing:-.08em;font-weight:950;color:#1b171f}.mxv16__feature h2{margin:14px 0 0;font-size:clamp(30px,4vw,52px);line-height:.96;letter-spacing:-.05em}.mxv16__feature p{max-width:600px;margin:16px 0 0;color:#4f4a54;font-size:16px;line-height:1.55}.mxv16__feature-note{margin-top:20px;color:#766f7b;font-size:10px;font-weight:900;letter-spacing:.08em;text-transform:uppercase}
#maxess-results-v16 .mxv16__next-card{display:grid;grid-template-columns:90px 1fr;gap:24px;align-items:center;padding:30px;border-radius:30px;border:1px solid rgba(255,255,255,.12);background:linear-gradient(145deg,#15101d,#08080c)}.mxv16__next-index{width:76px;aspect-ratio:1;display:grid;place-items:center;border-radius:50%;background:linear-gradient(145deg,#fff,#c6a1ff);color:#120b1c;font-size:28px;font-weight:950;box-shadow:0 0 35px rgba(154,98,255,.18)}.mxv16__next-card h3{margin:8px 0 0;font-size:clamp(27px,4vw,46px);line-height:1;letter-spacing:-.04em}.mxv16__next-card p{max-width:820px;margin:12px 0 0;color:#bbb4c4;font-size:15px;line-height:1.6}.mxv16__process{display:flex;flex-wrap:wrap;justify-content:center;align-items:center;gap:9px;margin-top:28px;color:#c9c3d0;font-size:10px;font-weight:950;letter-spacing:.08em}.mxv16__process span{padding:9px 11px;border:1px solid rgba(255,255,255,.11);border-radius:999px;background:rgba(255,255,255,.035)}.mxv16__process i{font-style:normal;color:#6e6777}
#maxess-results-v16 .mxv16__masters{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:14px}.mxv16__master{min-width:0;min-height:220px;padding:22px;border:1px solid #e2dee6;border-radius:26px;background:#fff;box-shadow:0 16px 40px rgba(20,10,30,.06);position:relative;overflow:hidden}.mxv16__master::after{content:"";position:absolute;width:130px;height:130px;right:-55px;top:-55px;border-radius:50%;background:var(--master-color);opacity:.12;filter:blur(12px)}.mxv16__master-top{display:flex;justify-content:space-between;gap:12px;align-items:start}.mxv16__master-icon{width:44px;height:44px;display:grid;place-items:center;border-radius:14px;color:#fff;background:radial-gradient(circle at 30% 20%,#fff,var(--master-color) 45%,#130c1d);border:1px solid #fff;box-shadow:0 0 22px color-mix(in srgb,var(--master-color) 24%,transparent);font-size:18px}.mxv16__master-score{font-size:24px;font-weight:950}.mxv16__master h3{margin:18px 0 0;font-size:17px;line-height:1.1}.mxv16__master p{margin:9px 0 0;color:#5e5962;font-size:12px;line-height:1.5}.mxv16__master-reason{margin-top:14px;padding-top:12px;border-top:1px solid #eeeaf1;color:#6f4c7d;font-size:10px;font-weight:800;line-height:1.45}.mxv16__master-reason strong{display:block;margin-bottom:3px;color:#1d1720;font-size:9px;letter-spacing:.08em;text-transform:uppercase}
#maxess-results-v16 .mxv16__system-grid{display:grid;grid-template-columns:1fr 1fr;gap:60px;align-items:center}.mxv16__system-grid h2{margin:0;font-size:clamp(52px,6vw,86px);line-height:.9;letter-spacing:-.065em}.mxv16__system-stack{display:grid;gap:10px}.mxv16__system-stack div{padding:21px;border:1px solid rgba(255,255,255,.1);border-radius:22px;background:rgba(255,255,255,.035)}.mxv16__system-stack strong,.mxv16__system-stack span{display:block}.mxv16__system-stack strong{font-size:11px;letter-spacing:.13em}.mxv16__system-stack span{margin-top:6px;color:#a9a1b0;font-size:13px}
#maxess-results-v16 .mxv16__video-grid{display:grid;grid-template-columns:1fr 1fr;gap:60px;align-items:center}.mxv16__video-grid h2{margin:12px 0 0;font-size:clamp(42px,5vw,72px);line-height:.95;letter-spacing:-.06em}.mxv16__video-shell{min-height:340px;border-radius:30px;border:1px solid #ddd7e2;background:linear-gradient(145deg,#fbfafc,#f2eef6);display:grid;place-items:center;padding:30px}.mxv16__video-placeholder{text-align:center;max-width:430px}.mxv16__video-placeholder span,.mxv16__video-placeholder strong,.mxv16__video-placeholder small{display:block}.mxv16__video-placeholder span{color:#7040a6;font-size:10px;font-weight:950;letter-spacing:.16em}.mxv16__video-placeholder strong{margin-top:12px;font-size:22px;line-height:1.15}.mxv16__video-placeholder small{margin-top:10px;color:#6c6670;font-size:11px;line-height:1.45}
#maxess-results-v16 .mxv16__final-inner{width:min(920px,92vw);margin:auto;text-align:center}.mxv16__final-inner h2{margin:14px 0 0;font-size:clamp(44px,6vw,86px);line-height:.92;letter-spacing:-.065em}.mxv16__final-inner p{max-width:720px;margin:20px auto 0;color:#bbb2c4;font-size:17px;line-height:1.6}.mxv16__final-actions{display:flex;flex-wrap:wrap;justify-content:center;gap:12px;margin-top:28px}.mxv16__final-actions .mxv16__button{margin-top:0}
#maxess-results-v16 .mxv16__status{min-height:240px;display:grid;place-items:center;padding:60px 20px;background:#050507}.mxv16__status-card{width:min(560px,92vw);padding:34px;text-align:center;border:1px solid rgba(255,255,255,.11);border-radius:28px;background:#0d0b12}.mxv16__status-card h1{margin:16px 0 0;font-size:28px;letter-spacing:-.03em}.mxv16__status-card p{margin:10px 0 0;color:#aaa4b1;line-height:1.5}.mxv16__status-orb{width:58px;height:58px;margin:auto;border-radius:50%;background:radial-gradient(circle at 30% 20%,#fff,#9a62ff 40%,#160b27);box-shadow:0 0 40px rgba(154,98,255,.25)}
#maxess-results-v16[data-result-state="error"] .mxv16__status-orb,#maxess-results-v16[data-result-state="missing"] .mxv16__status-orb{background:radial-gradient(circle at 30% 20%,#fff,#ff9d3d 40%,#2b1105)}
@media(max-width:1120px){#maxess-results-v16 .mxv16__hero-inner{grid-template-columns:1fr minmax(310px,480px);grid-template-areas:"copy orb" "guide orb"}.mxv16__hero-copy{grid-area:copy}.mxv16__orb-wrap{grid-area:orb}.mxv16__hero-guide{grid-area:guide}.mxv16__dimensions{grid-template-columns:repeat(3,minmax(0,1fr))}.mxv16__masters{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media(max-width:820px){#maxess-results-v16 .mxv16__hero-inner,#maxess-results-v16 .mxv16__profile-grid,#maxess-results-v16 .mxv16__pattern-grid,#maxess-results-v16 .mxv16__two-col,#maxess-results-v16 .mxv16__system-grid,#maxess-results-v16 .mxv16__video-grid{grid-template-columns:1fr;grid-template-areas:none}.mxv16__orb-wrap,.mxv16__hero-copy,.mxv16__hero-guide{grid-area:auto}.mxv16__orb{width:min(500px,78vw)}.mxv16__section-head{grid-template-columns:1fr}.mxv16__dimensions{grid-template-columns:repeat(2,minmax(0,1fr))}.mxv16__naya-report{grid-template-columns:150px 1fr}}
@media(max-width:560px){#maxess-results-v16 .mxv16__wide{width:min(100% - 32px,720px)}#maxess-results-v16 .mxv16__hero-inner{width:min(100% - 28px,720px)}#maxess-results-v16 .mxv16__hero h1{font-size:clamp(48px,15vw,70px)}#maxess-results-v16 .mxv16__orb{width:min(390px,88vw)}#maxess-results-v16 .mxv16__dimensions,#maxess-results-v16 .mxv16__masters{grid-template-columns:1fr}.mxv16__naya-report{grid-template-columns:1fr}.mxv16__naya-portrait{width:min(180px,55vw)}.mxv16__next-card{grid-template-columns:1fr}.mxv16__process{justify-content:flex-start}.mxv16__process i{display:none}.mxv16__button{width:100%}}
@media(prefers-reduced-motion:reduce){#maxess-results-v16 .mxv16__button{transition:none}.mxv16__orb,.mxv16__orb::before{animation:none!important}}
@media print{#maxess-results-v16 .mxv16__hero,#maxess-results-v16 .mxv16__chapter--dark,#maxess-results-v16 .mxv16__chapter--final{background:#fff!important;color:#111!important}.mxv16__hero-sub,.mxv16__hero-meta,.mxv16__section-head p,.mxv16__lead,.mxv16__pattern-copy>p,.mxv16__naya-detail,.mxv16__feature p,.mxv16__next-card p,.mxv16__final-inner p{color:#333!important}.mxv16__hero h1,.mxv16__section-head h2,.mxv16__feature h2,.mxv16__next-card h3,.mxv16__system-grid h2,.mxv16__video-grid h2,.mxv16__final-inner h2{color:#111!important}.mxv16__orb{width:260px!important}.mxv16__masters{grid-template-columns:repeat(3,1fr)!important}.mxv16__master,.mxv16__feature,.mxv16__profile-card,.mxv16__pattern-visual,.mxv16__naya-report,.mxv16__next-card,.mxv16__video-shell,.mxv16__system-stack div{box-shadow:none!important;break-inside:avoid}.mxv16__button{display:none!important}.mxv16__chapter{padding:38px 0!important;break-inside:auto}.mxv16__status{display:none!important}}
</style>

<script id="maxess-results-v16-js">
(function(){
  'use strict';

  var root=document.getElementById('maxess-results-v16');
  if(!root || root.dataset.initialized==='1') return;
  root.dataset.initialized='1';

  var CONFIG={
    assessmentIds:['ai-mastery'],
    expectedDimensions:5,
    dimensionMeta:[
      {id:'direction',name:'Direction',color:'#ffd45a'},
      {id:'communication',name:'Communication',color:'#39df91'},
      {id:'evaluation',name:'Evaluation',color:'#4c9dff'},
      {id:'iteration',name:'Iteration',color:'#9a62ff'},
      {id:'systems',name:'Systems Thinking',color:'#ef4bc8'}
    ],
    bands:[
      {min:0,max:59.999,label:'Foundation',copy:'You are building the habits that make AI genuinely useful.'},
      {min:60,max:74.999,label:'Developing',copy:'You have a useful foundation and clear leverage ahead.'},
      {min:75,max:89.999,label:'Advancing',copy:'You have meaningful AI capability and a strong platform to build on.'},
      {min:90,max:100,label:'Mastering',copy:'You have developed a highly capable way of working with AI.'}
    ],
    masters:[
      ['writing','Writing & Communication','Write, rewrite, explain, persuade and communicate better.','#ffd45a','W'],
      ['research','Research & Information','Find, understand, compare and organize information.','#39df91','R'],
      ['brainstorming','Brainstorming & Ideas','Generate possibilities, concepts, angles and solutions.','#4c9dff','B'],
      ['content','Content Creation','Turn ideas into posts, scripts, stories and content systems.','#9a62ff','C'],
      ['business','Business & Strategy','Think through decisions, opportunities, models and growth.','#ef4bc8','B'],
      ['marketing','Marketing & Sales','Create offers, messaging, campaigns and customer journeys.','#8a5cff','M'],
      ['learning','Learning & Education','Learn faster, teach better and build educational experiences.','#ffd45a','L'],
      ['coding','Coding & Software','Build, debug, automate and understand technology.','#39df91','C'],
      ['images','Images & Visual Creation','Create concepts, graphics, visuals and design directions.','#4c9dff','I'],
      ['video','Video & Media','Develop videos, stories, edits, concepts and production workflows.','#9a62ff','V'],
      ['audio','Audio & Music','Work with voice, audio, narration, sound and music.','#ef4bc8','A'],
      ['data','Data & Analysis','Analyze information, patterns, numbers and decisions.','#8a5cff','D'],
      ['productivity','Productivity & Organization','Save time and build smarter repeatable workflows.','#ffd45a','P'],
      ['career','Career & Professional Growth','Improve skills, opportunities, work and professional value.','#39df91','C'],
      ['decision','Decision Making','Clarify options, trade-offs, uncertainty and choices.','#4c9dff','D'],
      ['creative','Creative Development','Explore concepts, aesthetics, invention and creative direction.','#9a62ff','C'],
      ['systems','Systems & Automation','Turn successful work into repeatable intelligent systems.','#ef4bc8','S'],
      ['orchestration','AI Orchestration','Coordinate AI capabilities into larger, coherent workflows.','#8a5cff','O']
    ]
  };

  var state={phase:'loading',model:null};

  function $(selector){return root.querySelector(selector)}
  function $$(selector){return Array.prototype.slice.call(root.querySelectorAll(selector))}
  function clamp(n){return Math.max(0,Math.min(100,n))}
  function number(value){var n=Number(value);return Number.isFinite(n)?n:null}
  function text(value){return value===null||value===undefined?'':String(value)}
  function escape(value){return text(value).replace(/[&<>\"']/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;','\"':'&quot;',"'":'&#039;'}[c]})}
  function bandFor(score){for(var i=0;i<CONFIG.bands.length;i++){if(score>=CONFIG.bands[i].min&&score<=CONFIG.bands[i].max)return CONFIG.bands[i]}return null}
  function status(title,copy,type){root.dataset.resultState=type||'error';root.querySelector('[data-status-title]').textContent=title;root.querySelector('[data-status-copy]').textContent=copy;root.querySelector('[data-status]').hidden=false;root.querySelector('[data-report]').hidden=true}
  function fail(code,title,copy){state.phase=code;status(title,copy,'error')}

  function demoResult(){return {assessmentId:'ai-mastery',assessmentVersion:'2.0.0',resultVersion:'demo-v16',completionState:'completed',participant:{name:'Demo Participant',role:'AI Explorer'},overallScore:82,band:'Advancing',dimensions:[{id:'direction',name:'Direction',score:86},{id:'communication',name:'Communication',score:91},{id:'evaluation',name:'Evaluation',score:79},{id:'iteration',name:'Iteration',score:74},{id:'systems',name:'Systems Thinking',score:80}]}}

  function input(){
    var production=window.MAXESS_RESULT;
    var fixture=new URLSearchParams(window.location.search).get('fixture')==='demo';
    if(production && typeof production==='object') return {value:production,source:'production'};
    if(fixture) return {value:demoResult(),source:'development-fixture'};
    return {value:null,source:'missing'};
  }

  function validate(raw){
    if(!raw || typeof raw!=='object' || Array.isArray(raw)) return {ok:false,code:'malformed',message:'The result contract exists but is not a valid object.'};
    var assessmentId=text(raw.assessmentId||raw.assessment?.id);
    if(!assessmentId || CONFIG.assessmentIds.indexOf(assessmentId)<0) return {ok:false,code:'unsupported',message:'This Results page does not support the supplied assessment identity.'};
    var completion=text(raw.completionState||raw.status).toLowerCase();
    if(['completed','complete','finished'].indexOf(completion)<0) return {ok:false,code:'incomplete',message:'Your assessment result is not marked complete yet.'};
    var overall=number(raw.overallScore);
    if(overall===null || overall<0 || overall>100) return {ok:false,code:'malformed',message:'The overall score is missing or outside the valid 0–100 range.'};
    var dims=Array.isArray(raw.dimensions)?raw.dimensions:[];
    if(dims.length!==CONFIG.expectedDimensions) return {ok:false,code:'incomplete',message:'The result contract does not contain all five required dimensions.'};
    var seen={};
    var normalized=[];
    for(var i=0;i<dims.length;i++){
      var d=dims[i]||{};var id=text(d.id);var score=number(d.score??d.value??d.normalizedScore);
      if(!id || seen[id]) return {ok:false,code:'malformed',message:'A dimension identifier is missing or duplicated.'};
      if(score===null || score<0 || score>100) return {ok:false,code:'malformed',message:'A dimension contains an invalid score.'};
      seen[id]=true;
      var meta=CONFIG.dimensionMeta.find(function(m){return m.id===id})||{};
      normalized.push({id:id,name:text(d.name||d.label||meta.name||id),score:Math.round(score*10)/10,color:text(d.color||meta.color||'#9a62ff'),description:text(d.description||d.insight),metadata:d.metadata||{}})
    }
    var band=bandFor(overall);
    if(!band) return {ok:false,code:'malformed',message:'The score cannot be mapped to a supported result band.'};
    return {ok:true,model:{assessmentId:assessmentId,assessmentVersion:text(raw.assessmentVersion||raw.assessment?.version||'unknown'),resultVersion:text(raw.resultVersion||raw.result?.version||raw.assessmentVersion||'unknown'),completionState:'completed',participant:{name:text(raw.participant?.name||raw.participantName||raw.name),role:text(raw.participant?.role||raw.role)},overall:Math.round(overall*10)/10,band:band,dimensions:normalized,rawAnswers:Array.isArray(raw.rawAnswers)?raw.rawAnswers:null,weighting:raw.weighting||null,recommendations:Array.isArray(raw.recommendations)?raw.recommendations:null,pathway:raw.pathway||null,timestamp:text(raw.completedAt||raw.timestamp)}}
  }

  function derive(model){
    var sorted=model.dimensions.slice().sort(function(a,b){return b.score-a.score});
    var strongest=sorted[0];
    var lowest=sorted[sorted.length-1];
    var spread=strongest.score-lowest.score;
    var leverage=lowest;
    var opportunities=model.dimensions.map(function(d){return {d:d,leverage:100-d.score}}).sort(function(a,b){return b.leverage-a.leverage});
    if(opportunities.length) leverage=opportunities[0].d;
    var ties=model.dimensions.filter(function(d){return Math.abs(d.score-strongest.score)<0.05}).length>1;
    var pattern=spread<8?'balanced':spread<20?'defined':'high-contrast';
    return {strongest:strongest,lever:leverage,spread:spread,pattern:pattern,strongestTied:ties}
  }

  function copyFor(id,kind,score){
    var messages={
      direction:{strong:'You are good at giving AI a destination. That helps the system aim before it starts producing.',lever:'Your next lift comes from defining the destination more precisely before the work begins.'},
      communication:{strong:'You translate intent into language AI can actually use. That is a high-value human skill.',lever:'Give AI richer context, audience, constraints, and outcomes so less energy is spent correcting misunderstandings.'},
      evaluation:{strong:'You have a useful quality filter. You are more likely to ask whether an answer deserves trust, not merely whether it sounds good.',lever:'Make “Why is this not a 10?” a normal part of important AI work.'},
      iteration:{strong:'You understand that strong work gets refined. That turns AI from an answer machine into an improvement partner.',lever:'Diagnose the weakness, preserve what works, improve what does not, and repeat.'},
      systems:{strong:'You are thinking beyond one-off outputs and toward reusable capability. That is the bridge from using AI to building with it.',lever:'Capture what works so successful workflows become reusable assets instead of discoveries you have to recreate.'}
    };
    var m=messages[id]||{strong:'This is an established part of your current capability.',lever:'Deliberate practice here can create useful lift.'};return m[kind]
  }

  function nextMove(model,derived){
    var d=derived.lever;
    return {title:'Strengthen '+d.name,copy:copyFor(d.id,'lever',d.score)+' Then apply the full process: KNOW → TELL → ASK → CREATE → SCORE → IMPROVE → REPEAT.'}
  }

  function pathwayReason(master,model,derived){
    var scoreMap={writing:['communication','iteration'],research:['evaluation','direction'],brainstorming:['direction','iteration'],content:['communication','iteration'],business:['direction','evaluation'],marketing:['communication','direction'],learning:['communication','iteration'],coding:['systems','iteration'],images:['creative','communication'],video:['creative','systems'],audio:['communication','creative'],data:['evaluation','systems'],productivity:['systems','iteration'],career:['communication','direction'],decision:['evaluation','direction'],creative:['iteration','brainstorming'],systems:['systems','iteration'],orchestration:['systems','direction']};
    var ids=scoreMap[master[0]]||[];var relevant=model.dimensions.filter(function(d){return ids.indexOf(d.id)>=0});var avg=relevant.length?relevant.reduce(function(s,d){return s+d.score},0)/relevant.length:model.overall;return avg<70?'High relevance to your current development opportunity.':avg<82?'Useful bridge from your current pattern to a stronger capability.':'Strong fit with capabilities you can already leverage.'
  }

  function colorFor(score){if(score<50)return ['#ff4b55','#ff9d3d'];if(score<65)return ['#ff9d3d','#ffd45a'];if(score<75)return ['#ffd45a','#39df91'];if(score<85)return ['#39df91','#45e5ff'];if(score<90)return ['#45e5ff','#4c9dff'];if(score<95)return ['#4c9dff','#9a62ff'];return ['#9a62ff','#ef4bc8']}

  function renderPattern(model){
    var svg=$('[data-pattern]');var cx=260,cy=230,rad=165;var pts=[];var labels=[];var five=model.dimensions.slice(0,5);var out='';
    function point(i,scale){var angle=-Math.PI/2+i*2*Math.PI/5;var r=rad*scale;return [cx+Math.cos(angle)*r,cy+Math.sin(angle)*r]}
    [0.25,0.5,0.75,1].forEach(function(scale){out+='<polygon class="grid" points="'+five.map(function(_,i){return point(i,scale).join(',')}).join(' ')+'" />'});
    five.forEach(function(_,i){var p=point(i,1);out+='<line class="axis" x1="'+cx+'" y1="'+cy+'" x2="'+p[0]+'" y2="'+p[1]+'" />'});
    var nodes=five.map(function(d,i){return point(i,Math.max(.08,d.score/100))});out+='<polygon class="shape" points="'+nodes.map(function(p){return p.join(',')}).join(' ')+'" />';nodes.forEach(function(p){out+='<circle class="node" cx="'+p[0]+'" cy="'+p[1]+'" r="7" />'});
    five.forEach(function(d,i){var p=point(i,1.17);out+='<text x="'+p[0]+'" y="'+p[1]+'" text-anchor="middle">'+escape(d.name)+'</text>'});svg.innerHTML=out;
    $('[data-pattern-summary]').textContent=derivedPattern(model.dimensions);
    $('[data-pattern-copy]').textContent=patternCopy(model);
    $('[data-pattern-legend]').innerHTML=five.map(function(d){return '<div class="mxv16__legend-row"><span class="mxv16__legend-dot" style="--dot:'+escape(d.color)+'"></span><strong>'+escape(d.name)+'</strong><span>'+Math.round(d.score)+'</span></div>'}).join('')
  }

  function derivedPattern(dims){var s=dims.slice().sort(function(a,b){return b.score-a.score});var spread=s[0].score-s[s.length-1].score;if(spread<8)return 'Balanced capability';if(spread<20)return 'Defined capability';return 'High-contrast capability'}
  function patternCopy(model){var d=model.dimensions.slice().sort(function(a,b){return b.score-a.score});var spread=d[0].score-d[d.length-1].score;if(spread<8)return 'Your five dimensions are close together. That suggests a relatively balanced capability profile: no single area is doing all the work.';if(spread<20)return 'Your profile has a clear shape. One or two capabilities are carrying more weight, while another area gives you a useful place to focus.';return 'Your profile has strong contrast. That is useful information: you already have meaningful capability to leverage, and the gap shows where focused improvement can create a visible change.'}

  function render(model,source){
    state.model=model;state.phase='ready';root.dataset.resultState='ready';root.dataset.source=source;root.querySelector('[data-status]').hidden=true;root.querySelector('[data-report]').hidden=false;
    var derived=derive(model);var palette=colorFor(model.overall);var profile=model.participant.name||'YOUR REPORT';
    $$('[data-score]').forEach(function(el){el.textContent=Math.round(model.overall)});$('[data-score-text]').textContent='Your validated MAXESS AI score is '+Math.round(model.overall)+' out of 100, in the '+model.band.label+' band.';$('[data-band]').textContent=model.band.label+' · '+Math.round(model.overall)+'/100';
    $('[data-orb]').style.setProperty('--score-progress',model.overall+'%');$('[data-orb]').style.setProperty('--score-a',palette[0]);$('[data-orb]').style.setProperty('--score-b',palette[1]);
    $$('[data-profile-name]').forEach(function(el){el.textContent=profile});$('[data-profile-role]').textContent=model.participant.role||'MAXESS participant';$$('[data-assessment-name]').forEach(function(el){el.textContent=model.assessmentId==='ai-mastery'?'AI Mastery Assessment':model.assessmentId});$('[data-assessment-version]').textContent=model.assessmentVersion;
    $('[data-hero-meaning]').textContent=model.band.copy+' '+(derived.pattern==='balanced'?'Your five dimensions are working in a relatively even relationship.':'Your five dimensions create a '+derived.pattern+' profile, which gives us a clear place to focus.');
    renderPattern(model);
    $('[data-dimensions]').innerHTML=model.dimensions.map(function(d){var desc=d.description||copyFor(d.id,d.score>=75?'strong':'lever',d.score);var level=d.score>=90?'Mastery':d.score>=75?'Advancing':d.score>=60?'Developing':'Foundation';return '<article class="mxv16__dimension"><div class="mxv16__gauge" style="--gauge:'+escape(d.color)+';--value:'+d.score+'%"><span class="mxv16__gauge-score">'+Math.round(d.score)+'</span></div><h3>'+escape(d.name)+'</h3><div class="mxv16__dimension-level">'+level+'</div><p>'+escape(desc)+'</p><div class="mxv16__dimension-lever"><strong>Actionable lever</strong>'+escape(copyFor(d.id,'lever',d.score))+'</div></article>'}).join('');
    $('[data-naya-interpretation]').textContent=derived.strongest.name+' is giving you something valuable to build from.';$('[data-naya-detail]').textContent='If I were helping you improve one thing first, I would start with '+derived.lever.name+'. It is not a deficiency. It is the clearest useful opportunity visible in your current scores.';
    $('[data-strongest-score]').textContent=Math.round(derived.strongest.score);$('[data-strongest-name]').textContent=derived.strongest.name;$('[data-strongest-copy]').textContent=copyFor(derived.strongest.id,'strong',derived.strongest.score);$('[data-lever-score]').textContent=Math.round(derived.lever.score);$('[data-lever-name]').textContent=derived.lever.name;$('[data-lever-copy]').textContent=copyFor(derived.lever.id,'lever',derived.lever.score);
    var next=nextMove(model,derived);$('[data-next-title]').textContent=next.title;$('[data-next-copy]').textContent=next.copy;
    $('[data-masters]').innerHTML=CONFIG.masters.map(function(m){var primary=pathwayReason(m,model,derived);var score=masterRelevance(m,model,derived);return '<article class="mxv16__master" style="--master-color:'+m[3]+'"><div class="mxv16__master-top"><span class="mxv16__master-icon" aria-hidden="true">'+escape(m[4])+'</span><span class="mxv16__master-score">'+score+'%</span></div><h3>'+escape(m[1])+'</h3><p>'+escape(m[2])+'</p><div class="mxv16__master-reason"><strong>Why this pathway</strong>'+escape(primary)+'</div></article>'}).join('');
    root.dispatchEvent(new CustomEvent('maxess:results-ready',{detail:{overall:model.overall,dimensions:model.dimensions}}));
  }

  function masterRelevance(m,model,derived){var r=pathwayReason(m,model,derived);if(r.indexOf('High relevance')===0)return 92;if(r.indexOf('Useful bridge')===0)return 82;return 70}

  function init(){
    try{
      var incoming=input();
      if(incoming.source==='missing'){state.phase='missing';status('Your result is not available yet','This Results renderer is waiting for the authoritative window.MAXESS_RESULT contract. No score has been invented. If you are testing the page, use the explicit development fixture.','missing');return}
      var checked=validate(incoming.value);
      if(!checked.ok){state.phase=checked.code;status(checked.code==='unsupported'?'Unsupported assessment':checked.code==='incomplete'?'Your result is incomplete':'We could not validate this result',checked.message+' No production score has been manufactured.','error');return}
      render(checked.model,incoming.source)
    }catch(error){console.error('MAXESS Results V16 render failure',error);fail('rendering','We could not render this report safely','The result contract was present, but the Results renderer encountered an unexpected error. No replacement score was shown.')}
  }

  $('[data-print]').addEventListener('click',function(){window.print()});
  root.addEventListener('error',function(event){if(event.target && event.target.tagName==='IMG'){event.target.style.visibility='hidden'}},true);
  if(document.readyState==='loading') document.addEventListener('DOMContentLoaded',init,{once:true}); else init();
})();
</script>
'''


def build() -> None:
    source = FOUNDATION.read_text(encoding="utf-8")
    if "<body" not in source.lower() or "</body>" not in source.lower():
        raise SystemExit("BLOCKED: nayanetpagecode does not contain a complete body boundary")
    if "MAXESS RESULTS V16 TOWER" in source:
        raise SystemExit("BLOCKED: V16 tower already exists in foundation")
    body_index = source.lower().find("<body")
    body_end = source.find(">", body_index)
    if body_end < 0:
        raise SystemExit("BLOCKED: malformed body tag in foundation")
    candidate = source[:body_end + 1] + "\n\n" + TOWER + "\n\n" + source[body_end + 1:]
    OUTPUT.write_text(candidate, encoding="utf-8", newline="\n")
    print(f"BUILT {OUTPUT} bytes={OUTPUT.stat().st_size}")


if __name__ == "__main__":
    build()
