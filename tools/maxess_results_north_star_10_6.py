from pathlib import Path

ARTIFACTS = [
    "MAXESS-RESULTS-10-GROOVE.html",
    "MAXESS-RESULTS-FINAL-GROOVE.html",
    "MAXESS-RESULTS-GROOVE-EMBED.html",
    "MAXESS-RESULTS-FINAL-GROOVE-EMBED.html",
    "MAXESS-RESULTS-GROOVE-EMBED-9.95.html",
]

MARKER = "MAXESS-NORTH-STAR-10.6"

CSS = r'''
/* MAXESS-NORTH-STAR-10.6 */
#maxess-results-10 .mx-hero{min-height:min(900px,96vh);padding-left:clamp(16px,5vw,88px);padding-right:clamp(16px,5vw,88px)}
#maxess-results-10 .mx-hero-grid{display:flex;flex-direction:column;gap:22px;width:100%;max-width:1500px;margin:0 auto;text-align:center}
#maxess-results-10 .mx-hero-grid > *{width:100%}
#maxess-results-10 .mx-score-orb{width:min(520px,72vw);margin:0 auto;filter:saturate(1.18);animation:mx106orb 7s ease-in-out infinite}
@keyframes mx106orb{0%,100%{transform:scale(1);box-shadow:0 0 0 1px rgba(255,255,255,.16),inset 0 0 70px rgba(174,92,255,.2),0 35px 100px rgba(0,0,0,.62),0 0 100px rgba(148,74,255,.24)}50%{transform:scale(1.018);box-shadow:0 0 0 1px rgba(255,255,255,.22),inset 0 0 90px rgba(174,92,255,.28),0 38px 115px rgba(0,0,0,.62),0 0 145px rgba(148,74,255,.34)}}
#maxess-results-10 .mx-hero-grid .mx-hero-actions{justify-content:center;margin-top:8px}
#maxess-results-10 .mx-hero-grid .mx-proof{display:none}
#maxess-results-10 .mx-hero-grid .mx-title{font-size:clamp(34px,5vw,72px);margin-top:8px}
#maxess-results-10 .mx-hero-grid .mx-copy{margin-left:auto;margin-right:auto;max-width:780px}
#maxess-results-10 .mx-report-tools{display:flex;justify-content:center;flex-wrap:wrap;gap:10px;margin:18px auto 0}
#maxess-results-10 .mx-report-tools button{min-height:50px;padding:0 20px;border-radius:999px;border:1px solid rgba(255,255,255,.18);background:linear-gradient(135deg,rgba(255,255,255,.12),rgba(166,108,255,.13));color:#fff;font-weight:850;cursor:pointer;box-shadow:0 12px 30px rgba(0,0,0,.22),inset 0 1px rgba(255,255,255,.22)}
#maxess-results-10 .mx-report-tools button:hover{transform:translateY(-2px);background:linear-gradient(135deg,rgba(255,255,255,.17),rgba(166,108,255,.2))}
#maxess-results-10 .mx-report-naya{max-width:900px;margin:8px auto 0;padding:20px 24px;border:1px solid rgba(81,226,173,.2);border-radius:24px;background:linear-gradient(135deg,rgba(81,226,173,.07),rgba(166,108,255,.08));text-align:left;box-shadow:0 18px 55px rgba(0,0,0,.22)}
#maxess-results-10 .mx-report-naya strong{display:block;font-size:12px;letter-spacing:.14em;text-transform:uppercase;color:#51e2ad;margin-bottom:7px}
#maxess-results-10 .mx-report-naya span{display:block;color:rgba(255,255,255,.84);font-size:16px;line-height:1.55}
#maxess-results-10 .mx-section.mx-pattern-section{background:linear-gradient(180deg,#fff 0,#f7f5fb 100%);color:#08070b}
#maxess-results-10 .mx-section.mx-pattern-section .mx-eyebrow{color:#6940a8}
#maxess-results-10 .mx-section.mx-pattern-section .mx-eyebrow::before{background:linear-gradient(90deg,#6940a8,transparent)}
#maxess-results-10 .mx-section.mx-pattern-section .mx-section-head h2{color:#08070b}
#maxess-results-10 .mx-section.mx-pattern-section .mx-section-head p{color:rgba(8,7,11,.62)}
#maxess-results-10 .mx-section.mx-pattern-section .mx-dim{background:linear-gradient(160deg,#fff,#f0edf6);border-color:rgba(8,7,11,.1);box-shadow:0 15px 40px rgba(37,17,62,.08);border-radius:28px}
#maxess-results-10 .mx-section.mx-pattern-section .mx-dim-head h3,#maxess-results-10 .mx-section.mx-pattern-section .mx-dim-head strong,#maxess-results-10 .mx-section.mx-pattern-section .mx-dim p,#maxess-results-10 .mx-section.mx-pattern-section .mx-lever b{color:#08070b}
#maxess-results-10 .mx-section.mx-pattern-section .mx-dim-head strong small,#maxess-results-10 .mx-section.mx-pattern-section .mx-kicker{color:rgba(8,7,11,.5)}
#maxess-results-10 .mx-section.mx-pattern-section .mx-track{background:rgba(8,7,11,.09)}
#maxess-results-10 .mx-section.mx-pattern-section .mx-track span{background:linear-gradient(90deg,#5f2ca5,#a66cff,#1fbf91)}
#maxess-results-10 .mx-report-chapter{position:relative}
#maxess-results-10 .mx-report-chapter + .mx-report-chapter{border-top:1px solid rgba(255,255,255,.08)}
#maxess-results-10 .mx-report-chapter .mx-section-head h2{max-width:900px}
#maxess-results-10 .mx-sales-start{margin-top:20px;padding-top:18px;border-top:1px solid rgba(255,255,255,.12)}
#maxess-results-10 .mx-sales-start::before{content:'YOUR REPORT IS COMPLETE';display:block;color:#51e2ad;font-size:10px;font-weight:900;letter-spacing:.2em;margin-bottom:9px}
#maxess-results-10 .mx-print-only{display:none}
@media(max-width:900px){#maxess-results-10 .mx-hero{min-height:auto;padding-top:60px}#maxess-results-10 .mx-score-orb{width:min(430px,82vw)}#maxess-results-10 .mx-dim-grid{grid-template-columns:1fr 1fr}#maxess-results-10 .mx-section-head{display:block}#maxess-results-10 .mx-section-head p{margin-top:14px}}
@media(max-width:560px){#maxess-results-10 .mx-dim-grid{grid-template-columns:1fr}#maxess-results-10 .mx-score-orb{width:min(360px,86vw)}#maxess-results-10 .mx-hero-actions{flex-direction:column;align-items:stretch}#maxess-results-10 .mx-hero-actions .mx-cta{width:100%}}
@media(prefers-reduced-motion:reduce){#maxess-results-10 .mx-score-orb{animation:none!important}#maxess-results-10 *{scroll-behavior:auto!important;transition:none!important}}
@media print{
  body{background:#fff!important}
  #maxess-results-10{background:#fff!important;color:#08070b!important;overflow:visible!important}
  #maxess-results-10::before,#maxess-results-10::after{display:none!important}
  #maxess-results-10 .mx-hero{min-height:auto!important;padding:34px 30px 42px!important;background:#08070b!important;color:#fff!important;page-break-after:always}
  #maxess-results-10 .mx-hero-grid{display:block!important}
  #maxess-results-10 .mx-score-orb{width:300px!important;margin:25px auto!important;animation:none!important;box-shadow:none!important;print-color-adjust:exact;-webkit-print-color-adjust:exact}
  #maxess-results-10 .mx-report-tools,#maxess-results-10 .mx-hero-actions,#maxess-results-10 .mx-proof,#maxess-results-10 button,#maxess-results-10 video,#maxess-results-10 audio{display:none!important}
  #maxess-results-10 .mx-report-naya{background:#f5f1fa!important;color:#08070b!important;border:1px solid #ddd!important;box-shadow:none!important;page-break-inside:avoid}
  #maxess-results-10 .mx-report-naya span{color:#202027!important}
  #maxess-results-10 .mx-section{padding:42px 30px!important;background:#fff!important;color:#08070b!important;page-break-inside:avoid}
  #maxess-results-10 .mx-section-head h2,#maxess-results-10 .mx-title,#maxess-results-10 .mx-dim-head h3,#maxess-results-10 .mx-dim-head strong,#maxess-results-10 .mx-dim p,#maxess-results-10 .mx-lever b{color:#08070b!important}
  #maxess-results-10 .mx-copy,#maxess-results-10 .mx-section-head p{color:#33343a!important}
  #maxess-results-10 .mx-dim-grid{grid-template-columns:repeat(5,1fr)!important;gap:8px!important}
  #maxess-results-10 .mx-dim{min-height:240px!important;padding:14px!important;background:#faf9fc!important;border-color:#ddd!important;box-shadow:none!important}
  #maxess-results-10 .mx-track span{print-color-adjust:exact;-webkit-print-color-adjust:exact}
  #maxess-results-10 .mx-sales-start,#maxess-results-10 [data-mx-sales]{display:none!important}
  #maxess-results-10 .mx-print-only{display:block!important}
}
'''

JS = r'''
/* MAXESS-NORTH-STAR-10.6 */
(function(){
  'use strict';
  var root=document.getElementById('maxess-results-10');
  if(!root || root.dataset.mx106==='1') return;
  root.dataset.mx106='1';
  function all(sel){return Array.prototype.slice.call(root.querySelectorAll(sel));}
  function text(el){return (el && (el.textContent||'')).replace(/\s+/g,' ').trim().toLowerCase();}
  function closestSection(el){return el && el.closest('.mx-section');}
  function findByText(phrase){return all('h1,h2,h3,h4,p,span,button,a,div').find(function(el){return text(el)===phrase || text(el).indexOf(phrase)>=0;});}

  // Recompose the hero: the result is the hero, not a dashboard.
  var hero=root.querySelector('.mx-hero');
  if(hero){
    var grid=hero.querySelector('.mx-hero-grid');
    if(grid){
      var title=grid.querySelector('.mx-title');
      var orb=grid.querySelector('.mx-score-orb');
      var actions=grid.querySelector('.mx-hero-actions');
      var reportTools=document.createElement('div'); reportTools.className='mx-report-tools';
      var printBtn=document.createElement('button'); printBtn.type='button'; printBtn.textContent='Print / Save PDF'; printBtn.setAttribute('aria-label','Print or save your MAXESS personal report as a PDF');
      printBtn.onclick=function(){window.print();};
      reportTools.appendChild(printBtn);
      var naya=document.createElement('div'); naya.className='mx-report-naya';
      var nayaStrong=document.createElement('strong'); nayaStrong.textContent='Naya is ready';
      var nayaSpan=document.createElement('span'); nayaSpan.textContent='I have your results. Listen to your results and I’ll walk you through the pattern I see — what is strong, what can move, and what I would do next.';
      naya.appendChild(nayaStrong); naya.appendChild(nayaSpan);
      if(title) grid.appendChild(title);
      if(orb) grid.appendChild(orb);
      if(actions) grid.appendChild(actions);
      grid.appendChild(naya);
      grid.appendChild(reportTools);
    }
  }

  // Remove low-value dashboard fragments from the personal report opening.
  all('.mx-proof').forEach(function(el){el.remove();});
  all('.mx-band').forEach(function(el){if(text(el).indexOf('meet')>=0) el.textContent='MAXESS RESULT';});

  // Turn the first dimension section into the visual pattern chapter.
  var dimGrid=root.querySelector('.mx-dim-grid');
  if(dimGrid){
    var sec=closestSection(dimGrid);
    if(sec){
      sec.classList.add('mx-pattern-section','mx-report-chapter');
      var head=sec.querySelector('.mx-section-head');
      if(head){
        var h=head.querySelector('h2');
        if(h) h.textContent='See the Pattern, Not the Score';
      }
    }
  }

  // Kill known generic/sales detours when they appear in the report area.
  ['ai capability shapes your life','your ledger','every score has a job'].forEach(function(phrase){
    var el=findByText(phrase);
    if(el){
      var sec=closestSection(el);
      if(sec) sec.setAttribute('data-mx-sales','1'); else el.style.display='none';
    }
  });

  // Mark the transition into sales/mastery content only after the report.
  var salesWords=['everything\'s included','learn ai','naya writer','naya brainstormer','mastery'];
  var candidates=all('h1,h2,h3');
  var firstSales=candidates.find(function(el){return salesWords.some(function(p){return text(el).indexOf(p)>=0;});});
  if(firstSales){
    var s=closestSection(firstSales); if(s) s.classList.add('mx-sales-start');
  }

  // Preserve Naya's existing live audio UI but make it part of the hero when present.
  var live=root.querySelector('#maxess-live-naya-audio,#maxess-result-live-bridge');
  if(live && hero){
    var clone=live.cloneNode(true); clone.classList.add('mx-hero-naya-live');
    clone.style.maxWidth='900px'; clone.style.margin='12px auto 0';
    var grid=hero.querySelector('.mx-hero-grid'); if(grid) grid.appendChild(clone);
  }

  // Keyboard-friendly report shortcut.
  root.addEventListener('keydown',function(e){if((e.ctrlKey||e.metaKey)&&e.key.toLowerCase()==='p'){return;}});
})();
'''

for name in ARTIFACTS:
    p=Path(name)
    if not p.exists():
        continue
    s=p.read_text(encoding='utf-8')
    if MARKER in s:
        continue
    if '</head>' not in s or '</body>' not in s:
        raise SystemExit(f'{name}: missing closing head/body')
    s=s.replace('</head>', '<style>\n'+CSS+'\n</style>\n</head>', 1)
    s=s.replace('</body>', '<script>\n'+JS+'\n</script>\n</body>', 1)
    p.write_text(s,encoding='utf-8')
    print(f'{MARKER}: integrated {name}')
