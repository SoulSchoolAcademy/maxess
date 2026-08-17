from pathlib import Path

path = Path('MAXESS-RESULTS-10-GROOVE.html')
text = path.read_text(encoding='utf-8')
if 'MAXESS_RESULTS_V17_EXECUTION' in text:
    print('V17 already present; nothing to do.')
    raise SystemExit(0)

css = '''<style id="maxess-results-v17-css">
#maxess-results-10.v17-results .mx-hero{min-height:min(820px,92vh)!important;padding-top:34px!important;padding-bottom:54px!important}
#maxess-results-10.v17-results .mx-hero-grid{display:flex!important;flex-direction:column!important;align-items:center!important;gap:18px!important;width:min(980px,100%)!important;text-align:center!important}
#maxess-results-10.v17-results .mx-hero-grid>div:first-child{order:2!important;display:flex!important;flex-direction:column!important;align-items:center!important;max-width:900px!important}
#maxess-results-10.v17-results .mx-hero-grid>.mx-score-orb{order:1!important;width:min(620px,80vw)!important;min-width:300px!important;margin:0 auto!important}
#maxess-results-10.v17-results .mx-hero .mx-eyebrow{display:none!important}
#maxess-results-10.v17-results .mx-hero .mx-title{font-size:0!important;line-height:1!important;margin:0!important}
#maxess-results-10.v17-results .mx-hero .mx-title::after{content:'YOUR AI SCORE';font-size:clamp(15px,1.35vw,18px);font-weight:950;letter-spacing:.25em;color:#fff}
#maxess-results-10.v17-results .mx-hero .mx-title em{display:none!important}
#maxess-results-10.v17-results .mx-hero .mx-copy,#maxess-results-10.v17-results .mx-hero .mx-proof,#maxess-results-10.v17-results .mx-hero .mx-hero-actions{display:none!important}
#maxess-results-10.v17-results .mx-score-orb{background:conic-gradient(from 205deg,#ff4545,#ff9e4a,#ffe56b,#58e18b,#50ddff,#6472ff,#a75bff,#ff4fb7,#ff4545)!important;box-shadow:0 0 100px rgba(166,108,255,.34),0 0 210px rgba(80,220,255,.12)!important;animation:v17Orb 28s linear infinite!important}
#maxess-results-10.v17-results .mx-score-orb::before{inset:3.5%!important;background:radial-gradient(circle at 30% 20%,rgba(255,255,255,.98),transparent 5%,rgba(255,255,255,.15) 12%,transparent 29%),radial-gradient(circle at 48% 54%,#28153f 0%,#0b0712 57%,#020207 100%)!important;box-shadow:inset 0 -70px 90px rgba(0,0,0,.72),inset 0 0 75px rgba(255,255,255,.09)!important}
#maxess-results-10.v17-results .mx-score-orb::after{inset:9%!important;border:1px solid rgba(255,255,255,.32)!important;box-shadow:0 0 35px rgba(255,255,255,.12),inset 0 0 40px rgba(255,255,255,.1)!important}
#maxess-results-10.v17-results .mx-score strong{font-size:clamp(112px,17vw,205px)!important;line-height:.78!important;font-weight:900!important;color:#fff!important;-webkit-text-fill-color:#fff!important;text-shadow:0 0 45px rgba(166,108,255,.22)!important}
#maxess-results-10.v17-results .mx-score span{margin-top:20px!important;color:#d0a8ff!important;font-size:12px!important;font-weight:900!important;letter-spacing:.25em!important}
#maxess-results-10.v17-results .mx-band{display:none!important}
#maxess-results-10.v17-results .v17-naya-banner{display:grid;grid-template-columns:58px minmax(0,1fr);align-items:center;gap:14px;width:min(1120px,calc(100% - 28px));margin:12px auto 0;padding:12px 16px;border-radius:18px;background:linear-gradient(105deg,#fff,#f7f3fc 62%,#eef9f8);color:#111;border:1px solid rgba(0,0,0,.10);box-shadow:0 18px 48px rgba(0,0,0,.20);position:relative;z-index:4}
#maxess-results-10.v17-results .v17-naya-banner img{width:58px;height:58px;border-radius:50%;object-fit:cover;border:2px solid #fff;box-shadow:0 0 0 5px rgba(150,93,255,.10),0 10px 25px rgba(0,0,0,.16)}
#maxess-results-10.v17-results .v17-naya-kicker{font-size:9px;font-weight:950;letter-spacing:.18em;color:#7042aa;text-transform:uppercase}
#maxess-results-10.v17-results .v17-naya-title{margin:3px 0 0;font-size:clamp(17px,2vw,24px);line-height:1.05;letter-spacing:-.03em;font-weight:850}
#maxess-results-10.v17-results .v17-naya-copy{margin:4px 0 0;color:#444;font-size:12px;line-height:1.4}
#maxess-results-10.v17-results .v17-dimensions{padding-top:42px!important;padding-bottom:46px!important}
#maxess-results-10.v17-results .v17-dimensions .mx-section-head{text-align:center;display:block!important;margin-bottom:22px!important}
#maxess-results-10.v17-results .v17-dimensions .mx-section-head h2{font-size:clamp(28px,4vw,52px)!important}
#maxess-results-10.v17-results .v17-dimensions .mx-section-head p{margin:10px auto 0;max-width:720px}
#maxess-results-10.v17-results .v17-mini-orb-grid{display:grid;grid-template-columns:repeat(5,minmax(0,1fr));gap:14px;max-width:1180px;margin:0 auto}
#maxess-results-10.v17-results .v17-mini-orb{position:relative;min-width:0;padding:16px 8px 18px;border-radius:24px;background:linear-gradient(160deg,rgba(255,255,255,.055),rgba(255,255,255,.012));border:1px solid rgba(255,255,255,.10);text-align:center;overflow:hidden;box-shadow:0 18px 48px rgba(0,0,0,.18)}
#maxess-results-10.v17-results .v17-mini-orb .orb{--g:#a66cff;position:relative;width:min(128px,100%);aspect-ratio:1;margin:0 auto 13px;border-radius:50%;background:conic-gradient(from 210deg,var(--g) calc(var(--score)*1%),rgba(255,255,255,.08) 0);box-shadow:0 0 28px color-mix(in srgb,var(--g) 28%,transparent),0 0 0 1px rgba(255,255,255,.12);animation:v17MiniFloat 5.5s ease-in-out infinite}
#maxess-results-10.v17-results .v17-mini-orb .orb::before{content:"";position:absolute;inset:7%;border-radius:50%;background:radial-gradient(circle at 30% 20%,rgba(255,255,255,.9),transparent 7%,rgba(255,255,255,.08) 18%,transparent 32%),radial-gradient(circle at 50% 52%,color-mix(in srgb,var(--g) 16%,#09070d),#05040a 70%);box-shadow:inset 0 -18px 26px rgba(0,0,0,.65)}
#maxess-results-10.v17-results .v17-mini-orb .orb::after{content:"";position:absolute;inset:15%;border-radius:50%;border:1px solid color-mix(in srgb,var(--g) 55%,white 5%);box-shadow:0 0 16px color-mix(in srgb,var(--g) 25%,transparent)}
#maxess-results-10.v17-results .v17-mini-orb .score{position:absolute;inset:0;display:grid;place-items:center;font-size:34px;font-weight:900;color:#fff;z-index:2;text-shadow:0 0 18px rgba(0,0,0,.55)}
#maxess-results-10.v17-results .v17-mini-orb h3{margin:0;font-size:13px;line-height:1.1;color:#fff}
#maxess-results-10.v17-results .v17-mini-orb p{margin:5px 0 0;color:rgba(255,255,255,.48);font-size:9px;letter-spacing:.12em;text-transform:uppercase}
#maxess-results-10.v17-results .v17-listen{display:flex;justify-content:center;margin:24px auto 0}
#maxess-results-10.v17-results .v17-listen .mx-cta{min-width:min(360px,100%)}
#maxess-results-10.v17-results .v17-meaning-card,#maxess-results-10.v17-results .v17-story-card{padding:28px;border:1px solid rgba(255,255,255,.12);border-radius:24px;background:linear-gradient(145deg,rgba(255,255,255,.055),rgba(255,255,255,.012));box-shadow:0 18px 50px rgba(0,0,0,.18)}
#maxess-results-10.v17-results .v17-meaning-grid,#maxess-results-10.v17-results .v17-story-grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:14px}
#maxess-results-10.v17-results .v17-meaning-card h3,#maxess-results-10.v17-results .v17-story-card h3{margin:6px 0 0;font-size:clamp(24px,3vw,38px);letter-spacing:-.04em}
#maxess-results-10.v17-results .v17-meaning-card p,#maxess-results-10.v17-results .v17-story-card p{margin:10px 0 0;color:rgba(255,255,255,.64);font-size:14px;line-height:1.55}
#maxess-results-10.v17-results .v17-meaning-card .lever{margin-top:15px;padding-top:12px;border-top:1px solid rgba(255,255,255,.10);color:#d0a8ff;font-size:11px;font-weight:800}
#maxess-results-10.v17-results .v17-action-section .mx-step{border-color:rgba(166,108,255,.32);box-shadow:0 18px 55px rgba(0,0,0,.24)}
#maxess-results-10.v17-results .v17-conversion{padding:36px 16px 46px!important}
#maxess-results-10.v17-results .v17-your-move{text-align:center;margin:22px auto 0}
#maxess-results-10.v17-results .v17-your-move h2{margin:0;font-size:clamp(30px,4vw,54px);letter-spacing:-.045em}
#maxess-results-10.v17-results .v17-your-move p{margin:8px 0 16px;color:rgba(255,255,255,.60);font-size:14px}
#maxess-results-10.v17-results .v17-your-move .ny-primary-zone{padding:0;display:flex;gap:12px;flex-wrap:wrap}
#maxess-results-10.v17-results .v17-your-move .ny-primary{width:auto;min-width:260px;min-height:58px}
#maxess-results-10.v17-results .v17-masters-section{padding-top:46px!important}
#maxess-results-10.v17-results .v17-masters-section .ny-membership{margin:0 auto 26px;padding:0 10px 12px}
#maxess-results-10.v17-results .v17-masters-section .ny-membership-inner{padding:28px 22px 30px}
#maxess-results-10.v17-results .v17-masters-grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:14px;margin-top:20px}
#maxess-results-10.v17-results .v17-master-profile{padding:20px;border:1px solid rgba(255,255,255,.12);border-radius:22px;background:linear-gradient(145deg,rgba(255,255,255,.055),rgba(255,255,255,.012));box-shadow:0 16px 44px rgba(0,0,0,.18)}
#maxess-results-10.v17-results .v17-master-profile h3{margin:0;font-size:16px}
#maxess-results-10.v17-results .v17-master-profile .profile-kicker{margin-top:5px;color:#cdb6ff;font-size:9px;font-weight:950;letter-spacing:.16em;text-transform:uppercase}
#maxess-results-10.v17-results .v17-master-profile p{margin:9px 0 0;color:rgba(255,255,255,.60);font-size:12px;line-height:1.5}
#maxess-results-10.v17-results .v17-master-profile .profile-meter{height:5px;margin-top:13px;border-radius:999px;background:rgba(255,255,255,.07);overflow:hidden}
#maxess-results-10.v17-results .v17-master-profile .profile-meter i{display:block;height:100%;width:var(--w);background:linear-gradient(90deg,#8d4de7,#61d8ff)}
#maxess-results-10.v17-results .v17-playground{padding-top:44px!important}
#maxess-results-10.v17-results .v17-philosophy{text-align:center;padding-top:68px!important;padding-bottom:86px!important}
#maxess-results-10.v17-results .v17-philosophy h2{margin:12px auto 0;max-width:900px;font-size:clamp(30px,4.8vw,68px);line-height:1;letter-spacing:-.055em}
#maxess-results-10.v17-results .v17-philosophy p{margin:16px auto 0;max-width:650px;color:rgba(255,255,255,.60);font-size:15px;line-height:1.6}
@keyframes v17Orb{to{transform:rotate(360deg)}}
@keyframes v17MiniFloat{0%,100%{transform:translateY(0)}50%{transform:translateY(-3px)}}
@media(max-width:900px){#maxess-results-10.v17-results .v17-mini-orb-grid{grid-template-columns:repeat(2,minmax(0,1fr));max-width:620px}#maxess-results-10.v17-results .v17-meaning-grid,#maxess-results-10.v17-results .v17-story-grid{grid-template-columns:1fr}#maxess-results-10.v17-results .v17-masters-grid{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media(max-width:620px){#maxess-results-10.v17-results .v17-naya-banner{grid-template-columns:46px minmax(0,1fr);padding:10px 12px}#maxess-results-10.v17-results .v17-naya-banner img{width:46px!important;height:46px!important}#maxess-results-10.v17-results .v17-mini-orb-grid{grid-template-columns:repeat(2,minmax(0,1fr));gap:9px}#maxess-results-10.v17-results .v17-mini-orb{padding:12px 5px 14px}#maxess-results-10.v17-results .v17-mini-orb .orb{width:104px}.v17-mini-orb .score{font-size:28px!important}#maxess-results-10.v17-results .v17-masters-grid{grid-template-columns:1fr}#maxess-results-10.v17-results .v17-your-move .ny-primary{width:100%}}
@media(prefers-reduced-motion:reduce){#maxess-results-10.v17-results .mx-score-orb,#maxess-results-10.v17-results .v17-mini-orb .orb{animation:none!important}}
</style>'''

js = '''<script id="MAXESS_RESULTS_V17_EXECUTION">
(function(){
'use strict';
var root=document.getElementById('maxess-results-10');if(!root)return;
root.classList.add('v17-results');
function sec(pred){return Array.prototype.slice.call(root.children).find(function(e){return e.tagName==='SECTION'&&pred(e)})||null}
function tx(e){return(e&&e.textContent||'').replace(/\\s+/g,' ').trim()}
function el(tag,cls){var e=document.createElement(tag);if(cls)e.className=cls;return e}
var hero=sec(function(e){return e.classList.contains('mx-hero')});
var bridge=root.querySelector('#naya-report');
if(bridge&&hero){var img=(root.querySelector('.v13-naya-intro img,.v12-naya-intro img')||{}).src||'';bridge.className='mx-section v17-naya-orientation';bridge.innerHTML='';var b=el('div','v17-naya-banner');if(img){var im=document.createElement('img');im.src=img;im.alt='Naya';b.appendChild(im)}else{var f=el('div');f.setAttribute('aria-hidden','true');f.textContent='✦';f.style.cssText='display:grid;place-items:center;width:46px;height:46px;border-radius:50%;background:linear-gradient(145deg,#d8b7ff,#6f36c6);color:#fff;font-size:22px;font-weight:900';b.appendChild(f)}var c=el('div');c.innerHTML='<div class="v17-naya-kicker">NAYA</div><div class="v17-naya-title">This isn’t a judgment. It’s a map.</div><div class="v17-naya-copy">Hi. I’ve looked at your results. I’ll help you understand what they mean — and what to do with them.</div>';b.appendChild(c);bridge.appendChild(b);root.insertBefore(bridge,hero)}
var result=window.MAXESS_RESULT||{};var hs=root.querySelector('.mx-hero .mx-score strong');if(hs&&result.overallScore!=null)hs.textContent=String(result.overallScore);
var dims=sec(function(e){return /Every score has/i.test(tx(e))||e.querySelector('.mx-dim-grid')});var meaning=null;
if(dims){dims.classList.add('v17-dimensions');var head=dims.querySelector('.mx-section-head');if(head){var eh=head.querySelector('.mx-eyebrow'),hh=head.querySelector('h2'),pp=head.querySelector('p');if(eh)eh.textContent='YOUR FIVE DIMENSIONS';if(hh)hh.textContent='YOUR AI CAPABILITIES';if(pp)pp.textContent='Five capabilities make up your overall AI score.'}var cards=Array.prototype.slice.call(dims.querySelectorAll('.mx-dim'));var data=Array.isArray(result.dimensions)?result.dimensions:[];var colors=['#55dfff','#ff4fb7','#ffd84a','#58e18b','#a75bff'];var mini=el('div','v17-mini-orb-grid');var meaningSec=el('section','mx-section v17-meaning-section');meaningSec.innerHTML='<div class="mx-wide"><div class="mx-section-head"><div><span class="mx-eyebrow">YOUR MEANING</span><h2>Now, here’s what each score tells you.</h2></div><p>The number is the signal. The explanation turns it into something you can use.</p></div><div class="v17-meaning-grid"></div></div>';var mg=meaningSec.querySelector('.v17-meaning-grid');cards.forEach(function(card,i){var name=(card.querySelector('h3')||{}).textContent||('Dimension '+(i+1));var score=(data[i]&&data[i].score!=null)?data[i].score:(card.dataset.score||0);var desc=(card.querySelector('p')||{}).textContent||'';var lever=(card.querySelector('.mx-lever b')||{}).textContent||'';var item=el('article','v17-mini-orb');item.innerHTML='<div class="orb" style="--g:'+colors[i]+';--score:'+score+'"><span class="score">'+score+'</span></div><h3>'+name+'</h3><p>AI CAPABILITY</p>';mini.appendChild(item);var mc=el('article','v17-meaning-card');mc.innerHTML='<span class="mx-eyebrow">'+name+' · '+score+'</span><h3>'+name+'</h3><p>'+desc+'</p><div class="lever">LEVER · '+lever+'</div>';mg.appendChild(mc)});dims.querySelector('.mx-dim-grid').replaceWith(mini);root.insertBefore(meaningSec,dims.nextSibling);var listen=el('div','v17-listen');listen.innerHTML='<button class="mx-cta mx-cta-primary" type="button">🎧 Listen to Naya</button>';dims.parentNode.insertBefore(listen,dims.nextSibling);listen.querySelector('button').addEventListener('click',function(){window.dispatchEvent(new CustomEvent('maxess:naya-report'));var a=document.querySelector('#nayanet-foundation-anchor');if(a)a.scrollIntoView({behavior:'smooth',block:'start'})})}
var pattern=sec(function(e){return e.id==='your-fingerprint'||/See the pattern/i.test(tx(e))});
var advantage=sec(function(e){return /What you already/i.test(tx(e))});
var action=sec(function(e){return /From capability/i.test(tx(e))});
if(pattern)pattern.classList.add('v17-pattern-section');var strength=null,lever=null;
if(advantage){var panels=Array.prototype.slice.call(advantage.querySelectorAll('.mx-panel'));if(panels[0]){strength=el('section','mx-section v17-strength-section');strength.innerHTML='<div class="mx-wide"><div class="mx-section-head"><div><span class="mx-eyebrow">YOUR STRENGTH</span><h2>What you already do well.</h2></div></div><div class="v17-story-grid"><article class="v17-story-card"></article></div></div>';strength.querySelector('.v17-story-card').innerHTML=panels[0].innerHTML}if(panels[1]){lever=el('section','mx-section v17-lever-section');lever.innerHTML='<div class="mx-wide"><div class="mx-section-head"><div><span class="mx-eyebrow">YOUR LEVER</span><h2>Where a little growth can create a lot of upside.</h2></div></div><div class="v17-story-grid"><article class="v17-story-card"></article></div></div>';lever.querySelector('.v17-story-card').innerHTML=panels[1].innerHTML}advantage.remove()}
if(action){action.classList.add('v17-action-section');var ah=action.querySelector('h2');if(ah)ah.innerHTML='YOUR ACTION';var ap=action.querySelector('.mx-section-head p');if(ap)ap.textContent='Turn what you discovered into a simple practice you can repeat.'}
var conversion=document.querySelector('.ny-page-inner');if(conversion){var theater=conversion.querySelector('.ny-theater'),primary=conversion.querySelector('.ny-primary-zone');if(theater||primary){var cv=el('section','mx-section v17-conversion');if(theater)cv.appendChild(theater);var mv=el('div','v17-your-move');mv.innerHTML='<h2>YOUR MOVE</h2><p>Watch the video. Then start your free trial.</p>';if(primary)mv.appendChild(primary);cv.appendChild(mv);root.appendChild(cv)}conversion.remove()}
var pathways=sec(function(e){return /18 AI PATHWAYS/i.test(tx(e))||e.querySelector('.mx-areas')});if(pathways){pathways.classList.add('v17-masters-section');var h=pathways.querySelector('.mx-section-head');if(h){var e=h.querySelector('.mx-eyebrow'),hh=h.querySelector('h2'),p=h.querySelector('p');if(e)e.textContent='18 NAYA MASTERS';if(hh)hh.textContent='INCLUDES EVERYTHING';if(p)p.textContent='All 18 Naya Masters are included — each one is a capability you can develop with Naya.'}var areas=pathways.querySelector('.mx-areas');var profiles=el('div','v17-masters-grid');Array.prototype.slice.call(areas.querySelectorAll('.mx-area')).forEach(function(card){var n=(card.querySelector('h3')||{}).textContent||'AI Master',d=(card.querySelector('p')||{}).textContent||'',m=(card.querySelector('.mx-area-relevance em')||{}).style&&card.querySelector('.mx-area-relevance em').style.getPropertyValue('--w')||'0%';var q=el('article','v17-master-profile');q.innerHTML='<h3>'+n+'</h3><div class="profile-kicker">AI PROFILE</div><p>'+d+'</p><div class="profile-meter"><i style="--w:'+m+'"></i></div>';profiles.appendChild(q)});areas.replaceWith(profiles);var seal=document.querySelector('.ny-membership');if(seal)pathways.insertBefore(seal,pathways.firstChild);root.appendChild(pathways)}
var playground=sec(function(e){return e.id==='naya-playground'});if(playground){playground.classList.add('v17-playground');root.appendChild(playground)}
var final=root.querySelector('.mx-final');if(final){final.classList.add('v17-philosophy');final.innerHTML='<span class="mx-eyebrow">NAYA + HUMAN</span><h2>Technology should amplify the human.</h2><p>Naya helps you understand your capability, turn insight into action, and use AI in service of what matters to you.</p>';root.appendChild(final)}
root.querySelectorAll('.mx-insight,#growth-scorecard').forEach(function(e){e.remove()});
if(pattern)root.appendChild(pattern);if(meaningSec)root.appendChild(meaningSec);if(strength)root.appendChild(strength);if(lever)root.appendChild(lever);if(action)root.appendChild(action);
root.setAttribute('data-v17-order','NAYA>SCORE>DIMENSIONS>LISTEN>PATTERN>MEANING>STRENGTH>LEVER>ACTION>VIDEO>TRIAL>MASTERS>PLAYGROUND>PHILOSOPHY');
})();
</script>'''

text = text.replace('</body>', css + '\n' + js + '\n</body>', 1)
path.write_text(text, encoding='utf-8')
print('V17 bytes:', path.stat().st_size)
