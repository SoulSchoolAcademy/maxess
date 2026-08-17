from pathlib import Path
TARGET=Path('MAXESS-RESULTS-AAA-GROOVE-EMBED.html')
START='<!-- MAXESS-V17-PRESERVATION-PATCH:START -->'
END='<!-- MAXESS-V17-PRESERVATION-PATCH:END -->'
STYLE=r'''<style id="maxess-v17-preservation-style">
#maxess-results-10 .v17-hero-naya{width:min(980px,100%);margin:0 auto 24px;padding:20px 24px;display:grid;grid-template-columns:78px minmax(0,1fr) auto;gap:18px;align-items:center;border:1px solid rgba(201,166,255,.24);border-radius:26px;background:linear-gradient(105deg,rgba(150,93,255,.12),rgba(255,255,255,.045),rgba(70,229,255,.045));box-shadow:0 24px 70px rgba(0,0,0,.28),inset 0 1px rgba(255,255,255,.11)}
#maxess-results-10 .v17-hero-naya img{width:78px;height:78px;border-radius:50%;object-fit:cover;border:2px solid rgba(255,255,255,.78);box-shadow:0 0 0 6px rgba(150,93,255,.09),0 14px 34px rgba(0,0,0,.3)}
#maxess-results-10 .v17-naya-kicker{display:block;color:#d0b4ff;font-size:9px;font-weight:950;letter-spacing:.18em;text-transform:uppercase}
#maxess-results-10 .v17-naya-title{margin:5px 0 0;color:#fff;font-size:clamp(19px,2.3vw,29px);line-height:1.05;letter-spacing:-.035em;font-weight:820}
#maxess-results-10 .v17-naya-copy{margin:7px 0 0;color:rgba(255,255,255,.66);font-size:13px;line-height:1.5}
#maxess-results-10 .v17-hero-naya .mx-cta{min-height:48px;white-space:nowrap}
#maxess-results-10 .v17-mini-orbs{width:min(980px,100%);margin:22px auto 0;display:grid;grid-template-columns:repeat(5,1fr);gap:12px}
#maxess-results-10 .v17-mini-orb{position:relative;aspect-ratio:1;border-radius:50%;display:grid;place-items:center;overflow:hidden;border:1px solid color-mix(in srgb,var(--c) 42%,white 8%);background:radial-gradient(circle at 33% 24%,rgba(255,255,255,.20),color-mix(in srgb,var(--c) 18%,transparent) 22%,#0b0810 68%,#030205 100%);box-shadow:inset 0 1px rgba(255,255,255,.13),0 18px 42px rgba(0,0,0,.38),0 0 28px color-mix(in srgb,var(--c) 12%,transparent);transition:transform .25s ease,border-color .25s ease,filter .25s ease}
#maxess-results-10 .v17-mini-orb:hover,#maxess-results-10 .v17-mini-orb:focus-visible{transform:translateY(-5px) scale(1.035);filter:brightness(1.08);border-color:color-mix(in srgb,var(--c) 62%,white 16%);outline:none}
#maxess-results-10 .v17-mini-orb::before{content:"";position:absolute;inset:10%;border-radius:50%;border:1px solid color-mix(in srgb,var(--c) 28%,white 4%);opacity:.75}
#maxess-results-10 .v17-mini-inner{position:relative;z-index:2;text-align:center}
#maxess-results-10 .v17-mini-score{display:block;font-size:clamp(25px,3vw,39px);line-height:.9;font-weight:900;letter-spacing:-.06em;color:var(--c);text-shadow:0 0 18px color-mix(in srgb,var(--c) 30%,transparent)}
#maxess-results-10 .v17-mini-name{display:block;margin-top:8px;color:#fff;font-size:10px;font-weight:800;line-height:1.1;max-width:110px}
#maxess-results-10 .v17-mini-tag{display:block;margin-top:5px;color:rgba(255,255,255,.40);font-size:7px;letter-spacing:.12em;text-transform:uppercase}
#maxess-results-10 .v17-hidden-legacy{display:none!important}
#maxess-results-10 .v17-hero-clean{display:flex!important;flex-direction:column!important;align-items:center!important;gap:0!important;text-align:center!important}
#maxess-results-10 .v17-hero-clean>.mx-score-orb{order:2!important}
#maxess-results-10 .v17-hero-clean>.v17-hero-naya{order:1!important}
#maxess-results-10 .v17-hero-clean>.v17-mini-orbs{order:3!important}
#maxess-results-10 .v17-hero-clean>.mx-score-orb{width:min(590px,72vw)!important;min-width:300px!important;margin:0 auto!important}
#maxess-results-10 .v17-hero-clean>.mx-score-orb .mx-score strong{font-size:clamp(105px,13vw,188px)!important}
@media(max-width:900px){#maxess-results-10 .v17-hero-naya{grid-template-columns:64px minmax(0,1fr);padding:17px 18px}.v17-hero-naya img{width:64px!important;height:64px!important}.v17-hero-naya .mx-cta{grid-column:1/-1;width:100%}#maxess-results-10 .v17-mini-orbs{grid-template-columns:repeat(5,1fr);gap:8px}}
@media(max-width:620px){#maxess-results-10 .v17-hero-naya{grid-template-columns:54px minmax(0,1fr);gap:12px;border-radius:21px;padding:15px}.v17-hero-naya img{width:54px!important;height:54px!important}.v17-naya-copy{font-size:12px!important}.v17-mini-orbs{gap:6px!important}.v17-mini-name{font-size:8px!important}.v17-mini-tag{display:none!important}.v17-mini-score{font-size:24px!important}}
@media(max-width:460px){#maxess-results-10 .v17-mini-orbs{grid-template-columns:repeat(5,1fr)}.v17-mini-name{font-size:7px!important}.v17-mini-score{font-size:20px!important}}
@media(prefers-reduced-motion:reduce){#maxess-results-10 .v17-mini-orb{transition:none!important}}
</style>'''
SCRIPT=r'''<script id="maxess-v17-preservation-script">
(function(){
'use strict';
var root=document.getElementById('maxess-results-10');if(!root||root.dataset.v17PreservationApplied==='1')return;root.dataset.v17PreservationApplied='1';
var R=function(){return window.MAXESS_RESULT||null},clamp=function(n){return Math.max(0,Math.min(100,Number(n)||0))};
var esc=function(v){return String(v==null?'':v).replace(/[&<>"']/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]})};
var dims=function(){var r=R()||{},raw=Array.isArray(r.dimensions)?r.dimensions:[];return raw.slice(0,5).map(function(d,i){return{name:d.name||d.label||('Dimension '+(i+1)),score:clamp(d.score??d.value??0)}})};
var colors=['#ff9d3d','#ffd84a','#39df91','#4c9dff','#965dff'],imgSrc='https://raw.githubusercontent.com/SoulSchoolAcademy/maxess/main/Naya%20Profile%20white.jpg';
function score(){var r=R()||{},n=Number(r.overallScore??r.masterScore??r.score??r.overall);return Number.isFinite(n)?clamp(n):null}
function build(){
 var hero=root.querySelector('.mx-hero'),grid=hero&&hero.querySelector('.mx-hero-grid'),orb=hero&&hero.querySelector('.mx-score-orb');if(!hero||!grid||!orb||score()===null)return false;var ds=dims();if(ds.length!==5)return false;
 Array.prototype.slice.call(grid.children).forEach(function(el){if(el!==orb&&!el.classList.contains('v17-hero-naya')&&!el.classList.contains('v17-mini-orbs'))el.classList.add('v17-hidden-legacy')});grid.classList.add('v17-hero-clean');
 Array.prototype.slice.call(root.querySelectorAll('.v11-naya-welcome,.v12-naya-intro,.v13-naya-intro,#maxess-naya-profile-v6,.v13-naya')).forEach(function(el){el.remove()});
 var listen=root.querySelector('#mx-naya-listen'),welcome=document.createElement('div');welcome.className='v17-hero-naya';welcome.innerHTML='<img src="'+imgSrc+'" alt="Naya, your AI guide" loading="eager"><div><span class="v17-naya-kicker">NAYA · YOUR GUIDE</span><div class="v17-naya-title">Hi. I’ve looked at your results.</div><p class="v17-naya-copy">This isn’t your judgment. It’s your map. Let’s look at what your result is telling you.</p></div><button class="mx-cta mx-cta-primary" type="button" id="v17-listen">Listen to Naya <span aria-hidden="true">▶</span></button>';
 grid.insertBefore(welcome,orb);if(listen){welcome.querySelector('#v17-listen').addEventListener('click',function(){listen.click()});listen.classList.add('v17-hidden-legacy')}
 else welcome.querySelector('#v17-listen').addEventListener('click',function(){root.dispatchEvent(new CustomEvent('maxess:naya-listen',{bubbles:true}));window.dispatchEvent(new CustomEvent('maxess:naya-report'))});
 var strong=orb.querySelector('.mx-score strong');if(strong)strong.textContent=String(Math.round(score()));var label=orb.querySelector('.mx-score span');if(label)label.textContent='AI SCORE';
 var band=orb.querySelector('.mx-band');if(band)band.textContent=(R().band||(score()>=91?'Mastering':score()>=76?'Advancing':score()>=51?'Developing':'Foundation'));
 var mini=document.createElement('div');mini.className='v17-mini-orbs';mini.setAttribute('aria-label','Your five AI capability dimensions');ds.forEach(function(d,i){var card=document.createElement('button');card.type='button';card.className='v17-mini-orb';card.style.setProperty('--c',colors[i]);card.innerHTML='<span class="v17-mini-inner"><span class="v17-mini-score">'+Math.round(d.score)+'</span><span class="v17-mini-name">'+esc(d.name)+'</span><span class="v17-mini-tag">DIMENSION '+(i+1)+'</span></span>';card.addEventListener('click',function(){var target=root.querySelector('#your-fingerprint')||root.querySelector('#v13-dimensions');if(target)target.scrollIntoView({behavior:'smooth',block:'start'})});mini.appendChild(card)});grid.appendChild(mini);
 Array.prototype.slice.call(root.querySelectorAll('#naya-report .mx-cta,#v13-report .v13-btn,#v11-naya-report .mx-cta')).forEach(function(el){if(el!==listen)el.classList.add('v17-hidden-legacy')});
 root.setAttribute('data-v17-preservation','applied');root.setAttribute('data-v17-score',String(Math.round(score())));return true;
}
function start(){if(build())return;setTimeout(start,150)}
if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',start,{once:true});else start();
})();
</script>'''
PATCH=f"{START}\n{STYLE}\n{SCRIPT}\n{END}"
text=TARGET.read_text(encoding='utf-8')
if START in text and END in text:
 a=text.index(START);b=text.index(END)+len(END);text=text[:a]+text[b:]
if '</body>' not in text: raise SystemExit('no body')
text=text.replace('</body>',PATCH+'\n</body>',1)
TARGET.write_text(text,encoding='utf-8')
print('patched',TARGET)
