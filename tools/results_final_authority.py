from pathlib import Path

p = Path("code")
s = p.read_text(encoding="utf-8")
MARK = "MAXESS RESULTS FRESH AUTHORITY V3"
HTML_MARK = "<!-- " + MARK + " -->"

# Remove this authority from any prior generated source.
while HTML_MARK in s:
    start = s.find(HTML_MARK)
    body_end = s.find("</body>", start)
    if start < 0 or body_end < 0:
        break
    s = s[:start] + s[body_end:]

body_idx = s.rfind("</body>")
if body_idx < 0:
    raise RuntimeError("body closing tag missing")

first_script_end = s.find("</script>")
if first_script_end < 0 or first_script_end > body_idx:
    raise RuntimeError("main application script closing tag missing")
first_script_end += len("</script>")
core = s[:first_script_end].rstrip()

CSS = r'''
/* =========================================================
   MAXESS RESULTS — FRESH AUTHORITY V3
   Results presentation only. Assessment engine remains intact.
========================================================= */
#resultsView{display:none!important;width:100%!important;max-width:none!important;margin:0!important;}
#resultsView.visible{display:block!important;}
.board-wrap:has(#resultsView.visible){display:block!important;min-height:0!important;}
.board-wrap:has(#resultsView.visible) .board{display:block!important;min-height:0!important;overflow:visible!important;border:0!important;border-radius:0!important;background:transparent!important;box-shadow:none!important;}
.board-wrap:has(#resultsView.visible) .board::before,.board-wrap:has(#resultsView.visible) .board::after{display:none!important;}
.board-wrap:has(#resultsView.visible) .board-content{display:block!important;min-height:0!important;padding:0!important;}

.mxr{--ink:#f8f6fb;--muted:#aaa3b1;--line:rgba(184,149,255,.13);--purple:#8a5cff;--light:#b895ff;--blue:#3ca8ff;--green:#35e39b;--magenta:#ed42c4;--sapphire:#4e8cff;position:relative;isolation:isolate;overflow:hidden;color:var(--ink);background:radial-gradient(circle at 50% -8%,rgba(128,78,255,.2),transparent 32%),radial-gradient(circle at 5% 40%,rgba(60,168,255,.05),transparent 24%),radial-gradient(circle at 95% 76%,rgba(53,227,155,.05),transparent 22%),linear-gradient(180deg,#050507 0%,#020204 38%,#030305 100%);}
.mxr::before{content:"";position:absolute;inset:0;pointer-events:none;z-index:-1;background:radial-gradient(circle at 50% 20%,rgba(255,255,255,.02),transparent 35%),linear-gradient(115deg,transparent 16%,rgba(255,255,255,.014) 50%,transparent 84%);}
.mxr *{box-sizing:border-box}
.mxr-wrap{width:min(1180px,100%);margin:0 auto;padding:clamp(24px,5vw,72px) clamp(16px,4vw,48px) 120px}
.mxr-kicker{font-size:10px;font-weight:950;letter-spacing:.21em;text-transform:uppercase;color:var(--light)}
.mxr-title{margin:8px 0 0;font-size:clamp(42px,7vw,84px);font-weight:950;line-height:.92;letter-spacing:-.065em}
.mxr-copy{margin:17px 0 0;max-width:820px;color:#bcb6c4;font-size:clamp(16px,2vw,20px);line-height:1.58}
.mxr-center{text-align:center}.mxr-center .mxr-copy{margin-left:auto;margin-right:auto}
.mxr-hero{padding-bottom:64px}
.mxr-gauge{width:min(680px,100%);margin:26px auto 0}.mxr-gauge svg{display:block;width:100%;height:auto;overflow:visible}
.mxr-gauge .track{fill:none;stroke:rgba(255,255,255,.075);stroke-width:23;stroke-linecap:round}.mxr-gauge .fill{fill:none;stroke:url(#mxrGauge);stroke-width:23;stroke-linecap:round;filter:drop-shadow(0 0 14px rgba(138,92,255,.38))}.mxr-gauge .tick{stroke:rgba(255,255,255,.13);stroke-width:2}.mxr-gauge .tick.major{stroke:rgba(184,149,255,.35);stroke-width:3}.mxr-gauge .tick-label{fill:#898392;font:800 11px system-ui,sans-serif}.mxr-gauge .needle{stroke:#fff;stroke-width:5;stroke-linecap:round;filter:drop-shadow(0 0 8px rgba(255,255,255,.48))}.mxr-gauge .hub{fill:#09070d;stroke:#b895ff;stroke-width:3;filter:drop-shadow(0 0 12px rgba(138,92,255,.45))}.mxr-gauge .score{fill:#fff;font:1000 76px system-ui,sans-serif;letter-spacing:-.065em}.mxr-gauge .label{fill:#98919f;font:900 10px system-ui,sans-serif;letter-spacing:.17em}
.mxr-band{margin-top:-3px;font-size:11px;font-weight:950;letter-spacing:.16em;text-transform:uppercase;color:#d9d0e7}
.mxr-rule{height:1px;background:linear-gradient(90deg,transparent,var(--line),transparent)}
.mxr-section{padding:clamp(68px,8vw,110px) 0;border-top:1px solid var(--line)}
.mxr-editorial{max-width:960px;margin:0 auto}.mxr-editorial h2{margin:8px 0 0;font-size:clamp(34px,5vw,62px);line-height:.98;letter-spacing:-.045em}.mxr-lead{margin:16px 0 0;max-width:900px;color:#ddd7e4;font-size:clamp(18px,2.2vw,22px);line-height:1.58}
.mxr-facts{display:flex;flex-wrap:wrap;gap:28px;margin-top:26px}.mxr-fact{min-width:145px;padding-top:12px;border-top:1px solid rgba(255,255,255,.09)}.mxr-fact small{display:block;color:#7f7888;font-size:9px;font-weight:950;letter-spacing:.16em;text-transform:uppercase}.mxr-fact strong{display:block;margin-top:7px;font-size:24px}
.mxr-spectrum{max-width:900px;margin:28px auto 0;text-align:left}.mxr-spectrum-track{position:relative;height:16px;border-radius:999px;background:linear-gradient(90deg,#312043 0%,#5b3c87 36%,#7a5cff 64%,#8ce7c5 100%);box-shadow:inset 0 1px 3px rgba(255,255,255,.14),0 12px 28px rgba(0,0,0,.24)}.mxr-spectrum-marker{position:absolute;top:50%;width:28px;height:28px;border-radius:50%;transform:translate(-50%,-50%);background:radial-gradient(circle at 30% 20%,#fff 0,#e8ddff 14%,#b895ff 35%,#7048ef 64%,#14101c 100%);border:1px solid #f1ebff;box-shadow:0 0 0 6px rgba(138,92,255,.08),0 0 25px rgba(138,92,255,.4)}.mxr-spectrum-labels{display:flex;justify-content:space-between;margin-top:11px;color:#7f7888;font-size:10px;font-weight:900;letter-spacing:.06em;text-transform:uppercase}
.mxr-fingerprint{text-align:center}.mxr-fingerprint h2{margin:8px 0 0;font-size:clamp(36px,5vw,64px);line-height:.96;letter-spacing:-.045em}.mxr-fingerprint p{max-width:820px;margin:16px auto 0;color:#aaa3b1;font-size:15px;line-height:1.65}
.mxr-constellation{max-width:900px;margin:28px auto 0}.mxr-constellation svg{display:block;width:100%;height:auto}.mxr-constellation .grid{fill:none;stroke:rgba(255,255,255,.075)}.mxr-constellation .axis{stroke:rgba(184,149,255,.1)}.mxr-constellation .shape{fill:rgba(138,92,255,.14);stroke:#b895ff;stroke-width:3;filter:drop-shadow(0 0 18px rgba(138,92,255,.22))}.mxr-constellation .point{fill:#fff;stroke:#b895ff;stroke-width:2.5}.mxr-constellation .label{fill:#b6afbe;font:900 11px system-ui,sans-serif}
.mxr-cap-list{display:grid;grid-template-columns:repeat(5,1fr);gap:10px;margin-top:25px}.mxr-cap-btn{appearance:none;border:0;background:transparent;color:#fff;padding:0;text-align:center;cursor:pointer}.mxr-jewel{width:64px;height:64px;margin:0 auto;border-radius:21px;display:grid;place-items:center;border:1px solid rgba(255,255,255,.66);box-shadow:inset 0 2px 5px rgba(255,255,255,.7),0 0 28px rgba(138,92,255,.15),0 9px 18px rgba(0,0,0,.42)}.mxr-cap-btn:nth-child(1) .mxr-jewel{background:radial-gradient(circle at 28% 17%,#fff 0,#ddd4ff 13%,#8a5cff 43%,#09050f 100%)}.mxr-cap-btn:nth-child(2) .mxr-jewel{background:radial-gradient(circle at 28% 17%,#fff 0,#d9ecff 13%,#3ca8ff 43%,#06101a 100%)}.mxr-cap-btn:nth-child(3) .mxr-jewel{background:radial-gradient(circle at 28% 17%,#fff 0,#d8fff0 13%,#35e39b 43%,#06110b 100%)}.mxr-cap-btn:nth-child(4) .mxr-jewel{background:radial-gradient(circle at 28% 17%,#fff 0,#ddd8ff 13%,#765cff 43%,#0a0710 100%)}.mxr-cap-btn:nth-child(5) .mxr-jewel{background:radial-gradient(circle at 28% 17%,#fff 0,#ffd8f5 13%,#ed42c4 43%,#12050f 100%)}.mxr-cap-btn span{display:block;margin-top:10px;font-size:11px;font-weight:950;line-height:1.2}.mxr-cap-detail{max-width:760px;margin:24px auto 0;padding-top:15px;border-top:1px solid rgba(184,149,255,.12);color:#b7b0bd;font-size:14px;line-height:1.68}.mxr-cap-btn:focus-visible{outline:2px solid #fff;outline-offset:6px;border-radius:12px}
.mxr-two{display:grid;grid-template-columns:1fr 1fr;gap:48px}.mxr-story{padding-top:16px;border-top:1px solid rgba(184,149,255,.16)}.mxr-story .accent{width:36px;height:3px;border-radius:999px;background:var(--green);box-shadow:0 0 18px rgba(53,227,155,.25);margin-bottom:15px}.mxr-story.opportunity .accent{background:var(--purple);box-shadow:0 0 18px rgba(138,92,255,.24)}.mxr-story small{display:block;color:#7f7888;font-size:9px;font-weight:950;letter-spacing:.16em;text-transform:uppercase}.mxr-story h3{margin:8px 0 0;font-size:clamp(30px,4vw,42px);line-height:1.02;letter-spacing:-.035em}.mxr-story .story-score{margin-top:9px;color:var(--light);font-size:14px;font-weight:950}.mxr-story p{margin:10px 0 0;color:#aaa3b1;font-size:14px;line-height:1.68}.mxr-story details{margin-top:18px}.mxr-story summary{cursor:pointer;color:#d7d1df;font-size:11px;font-weight:950;letter-spacing:.1em;text-transform:uppercase}.mxr-story details p{margin-top:10px}
.mxr-insight{padding:clamp(82px,12vw,150px) 0}.mxr-orbit{width:112px;height:112px;border-radius:50%;border:1px solid rgba(234,226,255,.7);background:radial-gradient(circle at 30% 20%,#fff 0,#e4d8ff 11%,#a079ff 33%,#5429aa 61%,#08050e 100%);box-shadow:inset 0 2px 7px rgba(255,255,255,.72),0 0 54px rgba(138,92,255,.31),0 20px 34px rgba(0,0,0,.4);position:relative;margin-bottom:24px}.mxr-orbit::after{content:"";position:absolute;inset:-18px;border:1px solid rgba(184,149,255,.08);border-radius:50%;transform:rotate(-12deg) scaleX(1.46)}.mxr-insight blockquote{margin:0;max-width:1000px;font-size:clamp(34px,5.7vw,70px);font-weight:950;line-height:.98;letter-spacing:-.05em}.mxr-insight p{max-width:790px;margin:18px 0 0;color:#aaa3b1;font-size:15px;line-height:1.66}
.mxr-report{display:grid;grid-template-columns:330px minmax(0,1fr);gap:48px;align-items:center;max-width:980px;margin:0 auto}.mxr-doc{aspect-ratio:.74;border-radius:27px;padding:20px;background:linear-gradient(145deg,#17131f,#08080b);border:1px solid rgba(184,149,255,.25);box-shadow:inset 0 2px 6px rgba(255,255,255,.07),0 28px 65px rgba(0,0,0,.42),0 0 34px rgba(138,92,255,.1);transform:rotate(-3deg)}.mxr-seal{width:44px;height:44px;border-radius:50%;display:grid;place-items:center;background:radial-gradient(circle,#d8c9ff,#7954ff 58%,#291054);border:1px solid rgba(255,255,255,.5);font-weight:1000}.mxr-doc h3{margin:20px 0 0;font-size:28px;line-height:1.02;letter-spacing:-.03em}.mxr-doc .line{height:6px;border-radius:99px;background:linear-gradient(90deg,#8a5cff,#292430);margin-top:9px}.mxr-report-copy h2{margin:0;font-size:clamp(32px,4.7vw,54px);line-height:.98;letter-spacing:-.04em}.mxr-report-copy p{margin:12px 0 0;color:#aaa3b1;font-size:15px;line-height:1.64}.mxr-actions{display:flex;gap:11px;flex-wrap:wrap;margin-top:22px}.mxr-btn{min-height:56px;padding:0 23px;border-radius:18px;border:1px solid rgba(255,255,255,.15);background:#08080b;color:#fff;font-weight:950;cursor:pointer}.mxr-btn.primary{border-color:rgba(231,220,255,.72);background:linear-gradient(180deg,#c8afff,#805cff);color:#0a0610;box-shadow:0 17px 42px rgba(138,92,255,.21)}.mxr-btn:hover{transform:translateY(-2px)}.mxr-btn:focus-visible{outline:2px solid #fff;outline-offset:4px}
.mxr-naya{display:grid;grid-template-columns:190px minmax(0,1fr);gap:34px;align-items:center;max-width:1000px;margin:0 auto;padding:18px 0}.mxr-naya-photo{width:190px;height:190px;border-radius:50%;overflow:hidden;border:1px solid rgba(240,233,255,.7);background:radial-gradient(circle at 30% 20%,#fff,#a27aff 38%,#341774 72%,#06040a);box-shadow:inset 0 2px 8px rgba(255,255,255,.72),0 0 55px rgba(138,92,255,.32),0 20px 32px rgba(0,0,0,.42)}.mxr-naya-photo img{width:100%;height:100%;object-fit:cover;display:block}.mxr-naya h2{margin:8px 0 0;font-size:clamp(38px,5.2vw,62px);line-height:.94;letter-spacing:-.05em}.mxr-naya p{margin:14px 0 0;color:#b6b0bb;font-size:16px;line-height:1.65;max-width:760px}
.mxr-network{text-align:center}.mxr-network h2{margin:8px 0 0;font-size:clamp(36px,5.1vw,62px);line-height:.96;letter-spacing:-.045em}.mxr-network>p{max-width:760px;margin:15px auto 0;color:#aaa3b1;font-size:14px;line-height:1.65}.mxr-network-art{position:relative;width:min(960px,100%);height:430px;margin:30px auto 0}.mxr-net-orbit{position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);border:1px solid rgba(184,149,255,.14);border-radius:50%}.mxr-net-orbit.one{width:250px;height:250px}.mxr-net-orbit.two{width:450px;height:280px;transform:translate(-50%,-50%) rotate(-9deg)}.mxr-net-center{position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);width:122px;height:122px;border-radius:50%;display:grid;place-items:center;background:radial-gradient(circle at 30% 20%,#fff 0,#e5d9ff 10%,#9c78ff 34%,#4f2ba8 63%,#08050e 100%);border:1px solid rgba(240,233,255,.7);box-shadow:inset 0 2px 8px rgba(255,255,255,.74),0 0 58px rgba(138,92,255,.42),0 20px 34px rgba(0,0,0,.44);font-size:24px;font-weight:1000}.mxr-net-node{position:absolute;width:150px;transform:translate(-50%,-50%)}.mxr-net-node .mxr-jewel{width:72px;height:72px;border-radius:23px}.mxr-net-node strong{display:block;margin-top:10px;font-size:13px}.mxr-net-node span{display:block;margin-top:5px;color:#8f8799;font-size:9px;line-height:1.3}.mxr-net-node.n1{left:16%;top:50%}.mxr-net-node.n2{left:34%;top:12%}.mxr-net-node.n3{left:66%;top:12%}.mxr-net-node.n4{left:84%;top:50%}.mxr-net-node.n5{left:50%;top:90%}
.mxr-all-masters{margin:22px auto 0;max-width:930px}.mxr-master-list{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;margin-top:14px;text-align:left}.mxr-master-list span{padding:12px 14px;border-top:1px solid rgba(184,149,255,.12);color:#aaa3b1;font-size:11px}.mxr-master-list[hidden]{display:none}
.mxr-keys{text-align:center}.mxr-keys h2{margin:8px 0 0;font-size:clamp(34px,4.9vw,60px);line-height:.97;letter-spacing:-.045em}.mxr-keys>p{max-width:760px;margin:15px auto 0;color:#aaa3b1;font-size:14px;line-height:1.64}.mxr-key-row{display:grid;grid-template-columns:repeat(3,1fr);gap:20px;max-width:960px;margin:34px auto 0;position:relative}.mxr-key-row::before{content:"";position:absolute;left:18%;right:18%;top:60px;height:2px;background:linear-gradient(90deg,transparent,rgba(184,149,255,.48),transparent)}.mxr-key{position:relative;z-index:1;text-align:center}.mxr-key button{width:120px;height:120px;border-radius:50%;border:1px solid rgba(255,255,255,.65);background:radial-gradient(circle at 30% 18%,#fff 0,#ded4ff 13%,#8a5cff 42%,#0a0710 100%);box-shadow:inset 0 2px 8px rgba(255,255,255,.72),0 0 38px rgba(138,92,255,.2),0 18px 30px rgba(0,0,0,.42);color:#fff;font-size:20px;font-weight:1000;cursor:pointer}.mxr-key:nth-child(2) button{background:radial-gradient(circle at 30% 18%,#fff 0,#d9ecff 13%,#3ca8ff 42%,#06101a 100%)}.mxr-key:nth-child(3) button{background:radial-gradient(circle at 30% 18%,#fff 0,#d8fff0 13%,#35e39b 42%,#06110b 100%)}.mxr-key h3{margin:15px 0 0;font-size:16px}.mxr-key p{max-width:220px;margin:7px auto 0;color:#8f8798;font-size:11px;line-height:1.45}.mxr-key-detail{max-width:700px;margin:22px auto 0;color:#b9b1c0;font-size:14px;line-height:1.65;min-height:24px}
.mxr-cta{text-align:center;padding:clamp(86px,12vw,155px) 0 32px}.mxr-cta h2{margin:8px auto 0;max-width:900px;font-size:clamp(42px,6.4vw,78px);line-height:.94;letter-spacing:-.06em}.mxr-cta p{max-width:690px;margin:16px auto 0;color:#b3acbb;font-size:16px;line-height:1.65}.mxr-cta .mxr-actions{justify-content:center}.mxr-note{margin-top:20px;color:#6b6471;font-size:10px;line-height:1.5}
.mxr-print-only{display:none}
@media(max-width:820px){.mxr-two,.mxr-report{grid-template-columns:1fr}.mxr-report{max-width:520px}.mxr-doc{max-width:330px;margin:0 auto}.mxr-naya{grid-template-columns:100px minmax(0,1fr)}.mxr-naya-photo{width:100px;height:100px}.mxr-cap-list{gap:6px}.mxr-network-art{height:480px}.mxr-net-node.n1{left:17%;top:45%}.mxr-net-node.n2{left:35%;top:12%}.mxr-net-node.n3{left:65%;top:12%}.mxr-net-node.n4{left:83%;top:45%}.mxr-net-node.n5{left:50%;top:88%}}
@media(max-width:600px){.mxr-wrap{padding-inline:15px}.mxr-section{padding:58px 0}.mxr-cap-list{grid-template-columns:repeat(5,1fr)}.mxr-jewel{width:52px;height:52px;border-radius:17px}.mxr-cap-btn span{font-size:9px}.mxr-network-art{height:500px}.mxr-network h2{font-size:34px}.mxr-key-row{grid-template-columns:1fr;gap:18px}.mxr-key-row::before{display:none}.mxr-key button{width:98px;height:98px}.mxr-naya{grid-template-columns:1fr;text-align:center}.mxr-naya-photo{margin:0 auto}.mxr-master-list{grid-template-columns:1fr 1fr}.mxr-spectrum-labels{font-size:8px}}
@media print{html,body{background:#fff!important;color:#111!important}body{overflow:visible!important}.maxess-app{background:#fff!important;min-height:auto!important}.topbar,.footer,.command-row,.interest-actions,.result-actions,.interstitial{display:none!important}.app-inner,.board-wrap,.board,.board-content{display:block!important;min-height:auto!important;padding:0!important;margin:0!important;border:0!important;box-shadow:none!important;background:#fff!important;overflow:visible!important}.mxr{background:#fff!important;color:#111!important}.mxr::before{display:none}.mxr-wrap{width:100%!important;padding:0!important}.mxr-section,.mxr-hero,.mxr-insight,.mxr-cta{break-inside:avoid}.mxr-title,.mxr-editorial h2,.mxr-fingerprint h2,.mxr-story h3,.mxr-insight blockquote,.mxr-report-copy h2,.mxr-naya h2,.mxr-network h2,.mxr-keys h2,.mxr-cta h2,.mxr-network strong,.mxr-key h3{color:#111!important}.mxr-copy,.mxr-lead,.mxr-fingerprint p,.mxr-story p,.mxr-insight p,.mxr-report-copy p,.mxr-naya p,.mxr-network>p,.mxr-keys>p,.mxr-key p,.mxr-key-detail,.mxr-cta p{color:#333!important}.mxr-doc{transform:none;background:#fafafa;border-color:#ddd;box-shadow:none}.mxr-orbit,.mxr-net-orbit,.mxr-spectrum-track{print-color-adjust:exact;-webkit-print-color-adjust:exact}.mxr-actions{display:none!important}.mxr-print-only{display:block!important;color:#111!important;margin-bottom:20px}}
@media(prefers-reduced-motion:reduce){.mxr-btn:hover{transform:none}}
'''

JS = r'''<!-- MAXESS RESULTS FRESH AUTHORITY V3 -->
<script>
(function(){
  'use strict';
  const root=document.getElementById('resultsView');
  if(!root) return;
  const KEY='maxessFreshResultsV3';
  const NAYA_IMG='https://i.postimg.cc/593L5r04/Naya-and-shawn-ok-0.png';
  let legacyTemplate=root.innerHTML;
  let lastWasVisible=false;
  let timer=0;
  const esc=v=>String(v==null?'':v).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
  const clamp=(n,a,b)=>Math.max(a,Math.min(b,n));
  const dims=()=>{const found=[...root.querySelectorAll('#dimensionConstellation .dimension-orb')].map((el,i)=>({name:el.querySelector('.dimension-name')?.textContent?.trim()||['Direction','Communication','Evaluation','Iteration','Systems Thinking'][i]||'Dimension',score:clamp(Math.round(Number(el.querySelector('.dimension-score')?.textContent||0)),0,100)}));return found.length===5?found:['Direction','Communication','Evaluation','Iteration','Systems Thinking'].map(name=>({name,score:0}));};
  const scoreFrom=ds=>{const el=document.getElementById('overallScore');const n=Number((el?.textContent||'').replace(/[^\d.]/g,''));if(Number.isFinite(n)&&n>=0)return clamp(Math.round(n),0,100);return clamp(Math.round(ds.reduce((a,d)=>a+d.score,0)/5),0,100)};
  const band=score=>score>=80?'MASTERING':score>=65?'ADVANCING':score>=45?'DEVELOPING':'EMERGING';
  const scoreMeaning=score=>score>=80?'You already have a strong working relationship with AI. The opportunity now is consistency, depth, and turning good results into repeatable exceptional results.':score>=65?'You have a useful working foundation with AI. The next leap is learning to make your intent, evaluation, and improvement more deliberate.':score>=45?'You are developing the habits that make AI genuinely useful. A clearer process will make the quality of your results much more consistent.':'You are at the beginning of your AI capability journey. The biggest opportunity is building a simple repeatable way to direct, evaluate, and improve AI.';
  const advText={Direction:'You tend to give AI a destination instead of leaving the work completely open-ended.',Communication:'You tend to shape the interaction with useful context, intent, examples, or constraints.',Evaluation:'You tend to notice whether an answer is useful, accurate, complete, or good enough.',Iteration:'You tend to improve an answer rather than assuming the first result is the final result.','Systems Thinking':'You tend to connect successful AI work into repeatable methods instead of treating every task as isolated.'};
  const oppText={Direction:'Your next leverage point is making the desired destination even clearer before AI begins.',Communication:'Your next leverage point is giving AI richer context, constraints, examples, and standards when the outcome matters.',Evaluation:'Your next leverage point is turning quality judgment into a deliberate habit every time the result matters.',Iteration:'Your next leverage point is turning revision into a repeatable improve-and-check loop.', 'Systems Thinking':'Your next leverage point is capturing what works so you can reuse and improve it instead of starting from zero.'};
  const icon=k=>{const paths={Direction:'M4 17 20 4 13 20 10 13 4 10Z',Communication:'M4 5h16v10H9l-5 4V5Z',Evaluation:'M12 3 20 7v5c0 5-3.4 8-8 9-4.6-1-8-4-8-9V7l8-4Z M8 12l2.5 2.5L16 9',Iteration:'M6 7a7 7 0 0 1 12 2M18 17a7 7 0 0 1-12-2 M7 4v4h4M17 20v-4h-4','Systems Thinking':'M12 3v4M12 17v4M3 12h4M17 12h4M5.6 5.6l2.8 2.8M15.6 15.6l2.8 2.8M18.4 5.6l-2.8 2.8M8.4 15.6l-2.8 2.8'};return `<svg viewBox="0 0 24 24" width="22" height="22" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="${paths[k]||paths.Direction}"/></svg>`;};
  const jewel=(k,label)=>`<div class="mxr-jewel" aria-hidden="true">${icon(k)}</div>`;
  const gauge=score=>{const cx=300,cy=260,r=180,a0=-2.46,a1=2.46,a=a0+(a1-a0)*score/100,pt=(ang,rr)=>[cx+rr*Math.cos(ang),cy+rr*Math.sin(ang)],arc=(s,e)=>{const A=pt(s,r),B=pt(e,r);return `M ${A[0]} ${A[1]} A ${r} ${r} 0 0 1 ${B[0]} ${B[1]}`};let ticks='',labels='';for(let i=0;i<=10;i++){const t=a0+(a1-a0)*i/10,u=pt(t,r-14),v=pt(t,r+10);ticks+=`<line class="tick ${i%5===0?'major':''}" x1="${u[0]}" y1="${u[1]}" x2="${v[0]}" y2="${v[1]}"/>`;if(i%2===0){const q=pt(t,r+35);labels+=`<text class="tick-label" x="${q[0]}" y="${q[1]}" text-anchor="middle" dominant-baseline="middle">${i*10}</text>`}}const needle=pt(a,126);return `<svg viewBox="0 0 600 395" role="img" aria-label="MAXESS score ${score} out of 100"><defs><linearGradient id="mxrGauge" x1="0" x2="1"><stop offset="0" stop-color="#5b2bb6"/><stop offset=".58" stop-color="#8a5cff"/><stop offset="1" stop-color="#c8afff"/></linearGradient></defs><path class="track" d="${arc(a0,a1)}"/><path class="fill" d="${arc(a0,a)}"/>${ticks}${labels}<line class="needle" x1="${cx}" y1="${cy}" x2="${needle[0]}" y2="${needle[1]}"/><circle class="hub" cx="${cx}" cy="${cy}" r="16"/><text class="score" x="${cx}" y="${cy-3}" text-anchor="middle">${score}</text><text class="label" x="${cx}" y="${cy+27}" text-anchor="middle">YOUR MAXESS SCORE</text></svg>`};
  const constellation=ds=>{const cx=300,cy=220,r=154,n=5,p=(i,rr)=>{const a=-Math.PI/2+i*2*Math.PI/n;return[cx+rr*Math.cos(a),cy+rr*Math.sin(a)]};const poly=f=>ds.map((_,i)=>p(i,r*f).join(',')).join(' ');let grid='';[1,.75,.5,.25].forEach(f=>grid+=`<polygon class="grid" points="${poly(f)}"/>`);let axes='',points='',labels='';ds.forEach((d,i)=>{const q=p(i,r),l=p(i,r+38);axes+=`<line class="axis" x1="${cx}" y1="${cy}" x2="${q[0]}" y2="${q[1]}"/>`;const v=p(i,r*clamp(d.score,0,100)/100);points+=`<circle class="point" cx="${v[0]}" cy="${v[1]}" r="6"/>`;labels+=`<text class="label" x="${l[0]}" y="${l[1]}" text-anchor="middle" dominant-baseline="middle">${esc(d.name)}</text>`});const shape=ds.map((d,i)=>p(i,r*clamp(d.score,0,100)/100).join(',')).join(' ');return `<svg viewBox="0 0 600 440" role="img" aria-label="AI capability fingerprint">${grid}${axes}<polygon class="shape" points="${shape}"/>${points}${labels}</svg>`};
  const ctaHref=()=>{const links=[...root.querySelectorAll('a[href]')];const hit=links.find(a=>/master ai|start master|masterclass|start now/i.test((a.textContent||'').trim()));return hit?.href||''};
  const report=()=>window.print();
  function render(){
    if(!root.classList.contains('visible')) return;
    if(root.dataset[KEY]==='1') return;
    const ds=dims();
    if(ds.every(d=>d.score===0)&&!document.getElementById('overallScore')) return;
    const score=scoreFrom(ds),sorted=[...ds].sort((a,b)=>b.score-a.score),strong=sorted[0],opp=sorted[4],gap=Math.max(0,strong.score-opp.score),capBand=band(score),href=ctaHref();
    const masters=[['Writing','Words & Communication','Direction'],['Research','Evidence & Discovery','Evaluation'],['Strategy','Direction & Decisions','Direction'],['Creation','Ideas & Media','Iteration'],['Systems','Automation & Leverage','Systems Thinking']];
    const master18=['Writing & Communication','Research & Information','Brainstorming & Ideas','Content Creation','Business & Strategy','Marketing & Sales','Learning & Education','Coding & Software','Images & Visual Creation','Video & Media','Audio & Music','Automation & Workflows','Data & Analysis','Productivity & Organization','Personal Growth & Life','Health & Wellness','Money & Finance','Community & Relationships'];
    const keys=[['01','MASTER KEY','The universal blueprint.'],['02','SPECIALIZED KEY','Choose the territory.'],['03','ACTIVATION ROLODEX','Activate the right Naya Master.']];
    const analysis=`Your result shows a clear capability pattern: ${strong.name} is currently your strongest dimension at ${strong.score}, while ${opp.name} is the largest leverage point at ${opp.score}. That means you already have something real to build on. Your next gains are less about “learning AI” in the abstract and more about strengthening the specific part of your working process that will improve the rest.`;
    const insight=gap<=9?`Your profile is remarkably balanced. The interesting part is that your next level is unlikely to come from fixing one obvious gap — it will come from making the whole way you work with AI more deliberate.`:`Your profile is more uneven. That matters because your strongest capability can help carry the opportunity forward. ${strong.name} is the strength to lean on while you deliberately develop ${opp.name}.`;
    const nodes=ds.map((d,i)=>`<button class="mxr-cap-btn" data-cap="${i}" aria-label="${esc(d.name)} capability, ${d.score} out of 100">${jewel(d.name)}<span>${esc(d.name)}</span></button>`).join('');
    const netNodes=masters.map((m,i)=>`<div class="mxr-net-node n${i+1}">${jewel(m[2],m[0])}<strong>${esc(m[0])}</strong><span>${esc(m[1])}</span></div>`).join('');
    root.innerHTML=`<div class="mxr"><div class="mxr-wrap">
      <section class="mxr-hero mxr-center"><div class="mxr-kicker">Your MAXESS Result</div><h1 class="mxr-title">${score}%</h1><div class="mxr-band">${capBand} AI CAPABILITY</div><p class="mxr-copy">${esc(scoreMeaning(score))}</p><div class="mxr-gauge">${gauge(score)}</div></section>

      <section class="mxr-section"><div class="mxr-editorial"><div class="mxr-kicker">Your Personalized Analysis</div><h2>Here’s what your result tells us about you.</h2><p class="mxr-lead">${esc(analysis)}</p><div class="mxr-facts"><div class="mxr-fact"><small>Strongest</small><strong>${esc(strong.name)}</strong></div><div class="mxr-fact"><small>Leverage</small><strong>${esc(opp.name)}</strong></div><div class="mxr-fact"><small>Profile spread</small><strong>${gap} pts</strong></div></div></div></section>

      <section class="mxr-section mxr-center"><div class="mxr-kicker">What Your Score Tells You</div><h2 class="mxr-title" style="font-size:clamp(34px,5vw,62px)">${score} / 100</h2><div class="mxr-spectrum" aria-label="Capability spectrum"><div class="mxr-spectrum-track"><div class="mxr-spectrum-marker" style="left:${score}%"></div></div><div class="mxr-spectrum-labels"><span>Emerging</span><span>Developing</span><span>Advancing</span><span>Mastering</span></div></div><p class="mxr-copy" style="max-width:760px">${esc(scoreMeaning(score))}</p></section>

      <section class="mxr-section mxr-fingerprint"><div class="mxr-kicker">How You Actually Work With AI</div><h2>AI Capability Signature</h2><p>Five dimensions. One pattern. Tap a capability and make it the focus.</p><div class="mxr-constellation">${constellation(ds)}</div><div class="mxr-cap-list">${nodes}</div><div class="mxr-cap-detail" id="mxrCapDetail" aria-live="polite"></div></section>

      <section class="mxr-section"><div class="mxr-two"><article class="mxr-story"><div class="accent"></div><small>Your Natural Advantage</small><h3>${esc(strong.name)}</h3><div class="story-score">${strong.score} / 100</div><p>${esc(advText[strong.name]||'This is currently the clearest strength in your capability profile.')}</p><details><summary>Why it matters</summary><p>This strength gives you something to build from. Use it deliberately when you enter areas where AI results are less consistent.</p></details></article><article class="mxr-story opportunity"><div class="accent"></div><small>Your Highest-Leverage Opportunity</small><h3>${esc(opp.name)}</h3><div class="story-score">${opp.score} / 100</div><p>${esc(oppText[opp.name]||'This is the capability with the clearest room to create additional leverage.')}</p><details><summary>Open the opportunity</summary><p>The point is not to become “perfect.” It is to strengthen this capability enough that the quality of your overall AI work rises with it.</p></details></article></div></section>

      <section class="mxr-section mxr-insight"><div class="mxr-orbit" aria-hidden="true"></div><div class="mxr-kicker">The “OH… THAT’S WHY” Discovery</div><blockquote>${esc(insight)}</blockquote><p>That observation comes directly from the relationship between your measured strengths and opportunities — not from a generic personality label.</p></section>

      <section class="mxr-section"><div class="mxr-report"><div class="mxr-doc"><div class="mxr-seal">M</div><h3>YOUR MAXESS<br>AI CAPABILITY REPORT</h3><p>Your score, capability fingerprint, advantage, opportunity, and discovery.</p><div class="line"></div><div class="line" style="width:78%"></div><div class="line" style="width:64%"></div><div class="line" style="width:86%"></div></div><div class="mxr-report-copy"><div class="mxr-kicker">Your MAXESS Report</div><h2>Keep what you discovered.</h2><p>Save a clean version of this experience to revisit, print, or keep offline.</p><div class="mxr-actions"><button class="mxr-btn primary" id="mxrSave">SAVE MY RESULTS</button></div></div></div></section>

      <section class="mxr-section"><div class="mxr-naya"><div class="mxr-naya-photo"><img src="${NAYA_IMG}" alt="Naya and Shawn" onerror="this.style.display='none';this.parentElement.classList.add('image-fallback')"></div><div><div class="mxr-kicker">Naya</div><h2>I GOT YOU.</h2><p>You just discovered how you work with AI. Now let me show you how to turn that capability into exceptional results.</p></div></div></section>

      <section class="mxr-section mxr-network"><div class="mxr-kicker">Naya Master Intelligence</div><h2>A whole intelligence team around you.</h2><p>Five major territories create the front door. The specialized Masters stay behind the doorway so the experience never becomes a catalogue.</p><div class="mxr-network-art"><div class="mxr-net-orbit one"></div><div class="mxr-net-orbit two"></div><div class="mxr-net-center">NAYA</div>${netNodes}</div><div class="mxr-all-masters"><button class="mxr-btn" id="mxrMasters">MEET ALL MASTERS</button><div class="mxr-master-list" id="mxrMasterList" hidden>${master18.map(x=>`<span>${esc(x)}</span>`).join('')}</div></div></section>

      <section class="mxr-section mxr-keys"><div class="mxr-kicker">The Three-Key System</div><h2>It’s actually very simple.</h2><p>One universal blueprint. One specialized blueprint. One activated expert.</p><div class="mxr-key-row">${keys.map((k,i)=>`<div class="mxr-key"><button data-key="${i}" aria-label="${esc(k[1])}">${k[0]}</button><h3>${esc(k[1])}</h3><p>${esc(k[2])}</p></div>`).join('')}</div><div id="mxrKeyDetail" class="mxr-key-detail" aria-live="polite">The Master Key gives you the universal way to work. The Specialized Key gives the work a territory. The Activation Rolodex puts the right Naya Master beside you.</div></section>

      <section class="mxr-section mxr-cta mxr-center"><div class="mxr-kicker">Master AI / Start Now</div><h2>Ready to master AI?</h2><p>You’re not happy with mediocre AI results. You want exceptional results. MAXESS gives you a simple, repeatable system to help you get there.</p><div class="mxr-actions"><button class="mxr-btn primary" id="mxrStart">START MASTER AI</button></div><div class="mxr-note">The invitation begins after you’ve received the value of your assessment.</div></section>

      <section class="mxr-section mxr-cta mxr-center" style="padding-top:80px"><div class="mxr-kicker">Your Next Move</div><h2>What will you do with what you now know?</h2><p>You know where you are. You know where your leverage is. Now decide what you’ll do with it.</p><div class="mxr-actions"><button class="mxr-btn primary" id="mxrFinalStart">MASTER AI →</button><button class="mxr-btn" id="mxrFinalSave">SAVE MY RESULTS</button></div></section>
      <div class="mxr-print-only">YOUR MAXESS AI CAPABILITY REPORT · Score ${score}/100 · Strongest: ${esc(strong.name)} · Opportunity: ${esc(opp.name)}</div>
    </div></div>`;
    root.dataset[KEY]='1';

    const detail=root.querySelector('#mxrCapDetail');
    const capExplain=i=>{const d=ds[i];return `<strong>${esc(d.name)} · ${d.score}/100</strong><br>${esc(advText[d.name]||'This capability contributes directly to how effectively you direct, evaluate, and improve AI work.')}`};
    const first=Math.max(0,ds.findIndex(d=>d.name===strong.name));
    detail.innerHTML=capExplain(first);
    root.querySelectorAll('[data-cap]').forEach(btn=>btn.addEventListener('click',()=>{detail.innerHTML=capExplain(Number(btn.dataset.cap));}));
    root.querySelector('#mxrSave')?.addEventListener('click',report);
    root.querySelector('#mxrFinalSave')?.addEventListener('click',report);
    root.querySelector('#mxrMasters')?.addEventListener('click',()=>{const list=root.querySelector('#mxrMasterList');list.hidden=!list.hidden;root.querySelector('#mxrMasters').textContent=list.hidden?'MEET ALL MASTERS':'HIDE SPECIALIZED MASTERS';});
    const keyCopy=['The universal blueprint: KNOW → TELL → ASK → LOOK → SCORE → IMPROVE → REPEAT.','The specialized blueprint: choose the territory, language, standards, and context for the work.','The activated expert: bring the right Naya Master into the work when specialized judgment or execution matters.'];
    root.querySelectorAll('[data-key]').forEach(btn=>btn.addEventListener('click',()=>{root.querySelector('#mxrKeyDetail').textContent=keyCopy[Number(btn.dataset.key)];}));
    const go=()=>{if(href)window.location.href=href;else window.scrollTo({top:document.body.scrollHeight,behavior:'smooth'});};
    root.querySelector('#mxrStart')?.addEventListener('click',go);root.querySelector('#mxrFinalStart')?.addEventListener('click',go);
  }
  function watch(){
    const visible=root.classList.contains('visible');
    if(!visible){
      if(lastWasVisible){root.innerHTML=legacyTemplate;delete root.dataset[KEY];}
      lastWasVisible=false;
      return;
    }
    lastWasVisible=true;
    if(root.dataset[KEY]==='1') return;
    window.clearTimeout(timer);timer=window.setTimeout(render,80);
  }
  const mo=new MutationObserver(watch);mo.observe(root,{attributes:true,childList:true,subtree:true});
  window.setInterval(watch,180);
  watch();
})();
</script>
'''

style_idx = core.rfind("</style>")
if style_idx < 0:
    raise RuntimeError("stylesheet closing tag missing")
core = core[:style_idx] + CSS + chr(10) + core[style_idx:]
core += chr(10) + JS + chr(10)
s = core + "</body>" + chr(10) + "</html>" + chr(10)

if s.count(HTML_MARK) != 1:
    raise RuntimeError("fresh authority HTML marker invalid")
if s.count("<script>") != 2:
    raise RuntimeError("expected one main app script plus one Results authority script")
if "MAXESS RESULTS FRESH AUTHORITY V3" not in s:
    raise RuntimeError("fresh authority marker missing")

p.write_text(s, encoding="utf-8")
print("Applied MAXESS Results Fresh Authority V3")