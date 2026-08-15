from pathlib import Path

p = Path('code')
s = p.read_text(encoding='utf-8')
MARKER = 'MAXESS NAYA MASTERS GALLERY'
if MARKER in s:
    print('Naya Masters gallery already present')
    raise SystemExit(0)

CSS = r'''
/* =========================================================
   MAXESS NAYA MASTERS GALLERY
   Premium intelligence presentation. No card soup.
========================================================= */
.maxess-naya-gallery{
  margin:82px auto 0;
  max-width:1080px;
  padding:54px 0 10px;
  border-top:1px solid rgba(184,149,255,.11);
  text-align:center;
}
.maxess-naya-gallery .ng-kicker{
  color:#b895ff;
  font-size:10px;
  font-weight:950;
  letter-spacing:.20em;
  text-transform:uppercase;
}
.maxess-naya-gallery h3{
  max-width:860px;
  margin:10px auto 0;
  font-size:clamp(34px,5vw,58px);
  line-height:.98;
  letter-spacing:-.045em;
  font-weight:950;
}
.maxess-naya-gallery .ng-lead{
  max-width:720px;
  margin:16px auto 0;
  color:#aaa3b2;
  font-size:15px;
  line-height:1.65;
}
.ng-stage{
  position:relative;
  margin:38px auto 0;
  display:grid;
  grid-template-columns:repeat(5,minmax(0,1fr));
  gap:12px;
  align-items:stretch;
}
.ng-stage::before{
  content:"";
  position:absolute;
  left:7%;
  right:7%;
  top:55px;
  height:1px;
  background:linear-gradient(90deg,transparent,rgba(184,149,255,.42),transparent);
  box-shadow:0 0 20px rgba(138,92,255,.12);
}
.ng-master{
  position:relative;
  z-index:1;
  min-width:0;
  padding:0 8px 6px;
  text-align:center;
}
.ng-jewel{
  position:relative;
  width:92px;
  height:92px;
  margin:0 auto;
  border-radius:28px;
  display:grid;
  place-items:center;
  border:1px solid rgba(255,255,255,.72);
  box-shadow:
    inset 0 2px 6px rgba(255,255,255,.74),
    0 0 36px rgba(138,92,255,.16),
    0 16px 24px rgba(0,0,0,.42);
}
.ng-jewel::after{
  content:"";
  position:absolute;
  inset:10px;
  border-radius:20px;
  border:1px solid rgba(255,255,255,.16);
  box-shadow:inset 0 0 18px rgba(255,255,255,.08);
}
.ng-jewel svg{width:46px;height:46px;position:relative;z-index:2;filter:drop-shadow(0 4px 7px rgba(0,0,0,.34))}
.ng-jewel.purple{background:radial-gradient(circle at 28% 18%,#fff 0,#e4d7ff 12%,#8a5cff 42%,#2c1463 74%,#09050f 100%)}
.ng-jewel.blue{background:radial-gradient(circle at 28% 18%,#fff 0,#d9ecff 12%,#3ca8ff 42%,#08376d 74%,#050c15 100%)}
.ng-jewel.green{background:radial-gradient(circle at 28% 18%,#fff 0,#d7fff0 12%,#35e39b 42%,#096642 74%,#03100a 100%)}
.ng-jewel.violet{background:radial-gradient(circle at 28% 18%,#fff 0,#ded7ff 12%,#765cff 42%,#27106c 74%,#09060f 100%)}
.ng-jewel.magenta{background:radial-gradient(circle at 28% 18%,#fff 0,#ffd8f5 12%,#ed42c4 42%,#71114f 74%,#10050d 100%)}
.ng-master .ng-name{
  margin-top:16px;
  color:#fff;
  font-size:14px;
  line-height:1.15;
  font-weight:950;
  letter-spacing:-.01em;
}
.ng-master .ng-role{
  margin-top:6px;
  color:#9991a3;
  font-size:10px;
  line-height:1.42;
}
.ng-master .ng-brand{
  display:block;
  margin-top:8px;
  color:#b895ff;
  font-size:9px;
  font-weight:950;
  letter-spacing:.14em;
  text-transform:uppercase;
}
.ng-foot{
  margin-top:34px;
  color:#77707f;
  font-size:11px;
  line-height:1.6;
}

@media(max-width:860px){
  .ng-stage{grid-template-columns:repeat(3,minmax(0,1fr));gap:24px 10px}
  .ng-stage::before{display:none}
}
@media(max-width:560px){
  .maxess-naya-gallery{margin-top:62px;padding-top:42px}
  .ng-stage{grid-template-columns:repeat(2,minmax(0,1fr));gap:26px 8px}
  .ng-jewel{width:78px;height:78px;border-radius:24px}
  .ng-jewel svg{width:40px;height:40px}
  .ng-master .ng-name{font-size:13px}
}
'''

JS = r'''
(function(){
  const root=document.getElementById('resultsView');
  if(!root) return;
  const mount=()=>{
    if(!root.classList.contains('visible') || root.querySelector('.maxess-naya-gallery')) return;
    const shell=root.querySelector('.maxess-clean-results');
    if(!shell) return;

    root.querySelectorAll('.maxess-expert-grid,.maxess-expert-header,.maxess-treasure').forEach(el=>el.remove());

    const section=document.createElement('section');
    section.className='maxess-naya-gallery';
    section.innerHTML=`
      <div class="ng-kicker">NAYA · MASTERS</div>
      <h3>A specialized intelligence team, designed around what you want to do.</h3>
      <p class="ng-lead">One Naya. Many forms of mastery. Each Master is a focused way of turning AI capability into real-world work.</p>
      <div class="ng-stage">
        <article class="ng-master"><div class="ng-jewel purple">${gem('✦')}</div><div class="ng-name">Naya Master Writer</div><div class="ng-role">Words · Communication · Persuasion</div><span class="ng-brand">Naya Intelligence</span></article>
        <article class="ng-master"><div class="ng-jewel blue">${gem('⌁')}</div><div class="ng-name">Naya Master Researcher</div><div class="ng-role">Evidence · Discovery · Clarity</div><span class="ng-brand">Naya Intelligence</span></article>
        <article class="ng-master"><div class="ng-jewel green">${gem('◆')}</div><div class="ng-name">Naya Master Strategist</div><div class="ng-role">Business · Direction · Decisions</div><span class="ng-brand">Naya Intelligence</span></article>
        <article class="ng-master"><div class="ng-jewel violet">${gem('✧')}</div><div class="ng-name">Naya Master Creator</div><div class="ng-role">Ideas · Visuals · Media</div><span class="ng-brand">Naya Intelligence</span></article>
        <article class="ng-master"><div class="ng-jewel magenta">${gem('◈')}</div><div class="ng-name">Naya Master Systems Architect</div><div class="ng-role">Automation · Agents · Leverage</div><span class="ng-brand">Naya Intelligence</span></article>
      </div>
      <div class="ng-foot">Your assessment helps determine which doors deserve your attention first.</div>
    `;
    const anchor=shell.querySelector('.cr-naya') || shell.querySelector('.cr-masterkey') || shell.lastElementChild;
    if(anchor) anchor.insertAdjacentElement('afterend',section); else shell.appendChild(section);
  };
  function gem(symbol){
    return `<svg viewBox="0 0 48 48" aria-hidden="true"><circle cx="24" cy="24" r="17" fill="none" stroke="rgba(255,255,255,.75)" stroke-width="1.5"/><path d="M14 24h20M24 14v20M17 17l14 14M31 17L17 31" stroke="rgba(255,255,255,.78)" stroke-width="1.2" stroke-linecap="round"/><text x="24" y="29" text-anchor="middle" font-family="system-ui,sans-serif" font-size="16" font-weight="900" fill="#fff">${symbol}</text></svg>`;
  }
  new MutationObserver(mount).observe(root,{attributes:true,attributeFilter:['class'],childList:true,subtree:true});
  mount();
})();
'''

if '</style>' not in s:
    raise RuntimeError('style closing tag missing')
s=s.replace('</style>',CSS+'\n</style>',1)

idx=s.lower().rfind('</script>')
if idx<0:
    raise RuntimeError('script closing tag missing')
s=s[:idx]+JS+s[idx:]
s=s.replace('</head>', '\n<!-- '+MARKER+' -->\n</head>',1)
p.write_text(s,encoding='utf-8')
print('Naya Masters gallery applied')
