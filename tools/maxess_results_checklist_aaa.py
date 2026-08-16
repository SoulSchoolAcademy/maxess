from pathlib import Path
import re

SOURCE = Path('MAXESS-RESULTS-10-GROOVE.html')
MARKER = 'MAXESS-AAA-CHECKLIST-V1'

AAA_CSS = r'''
<!-- MAXESS-AAA-CHECKLIST-V1 -->
<style id="maxess-aaa-checklist-css">
#maxess-results-10{width:100vw!important;max-width:none!important;margin-left:calc(50% - 50vw)!important;margin-right:calc(50% - 50vw)!important;overflow:hidden!important}
#maxess-results-10 .mx-section{width:100%!important}
#maxess-results-10 .mx-wide{width:min(1760px,100%)!important;margin-inline:auto!important}
#maxess-results-10 .mx-hero{min-height:min(920px,95vh)!important;background:radial-gradient(circle at 50% 42%,rgba(150,93,255,.22),transparent 31%),linear-gradient(180deg,#020205,#09040d)!important}
#maxess-results-10 .mx-hero-grid{grid-template-columns:minmax(0,1fr) minmax(360px,680px) minmax(0,1fr)!important;grid-template-areas:"copy orb side"!important;gap:clamp(24px,4vw,76px)!important;width:min(1660px,100%)!important;margin:auto!important;text-align:center!important}
#maxess-results-10 .mx-hero-grid>.mx-score-orb{grid-area:orb!important;width:min(650px,48vw)!important;min-width:340px!important}
#maxess-results-10 .mx-hero-grid>div:first-child{grid-area:copy!important;display:flex!important;flex-direction:column!important;align-items:center!important}
#maxess-results-10 .mx-score-orb{--aaa-a:#965dff;--aaa-b:#ef4bc8;transition:filter .45s ease,box-shadow .45s ease!important;box-shadow:0 0 0 1px rgba(255,255,255,.22),inset 0 0 110px color-mix(in srgb,var(--aaa-a) 30%,transparent),0 40px 130px rgba(0,0,0,.7),0 0 150px color-mix(in srgb,var(--aaa-a) 22%,transparent)!important}
#maxess-results-10 .mx-score strong{font-size:clamp(110px,13vw,190px)!important;background:linear-gradient(110deg,var(--aaa-a),var(--aaa-b))!important;-webkit-background-clip:text!important;background-clip:text!important;color:transparent!important}
#maxess-results-10 .mx-aaa-resonance{position:absolute;inset:-10%;border-radius:50%;pointer-events:none;border:1px solid color-mix(in srgb,var(--aaa-a) 38%,transparent);opacity:.55;animation:aaa-resonance 5s ease-in-out infinite}
#maxess-results-10 .mx-aaa-resonance.r2{inset:-17%;opacity:.28;animation-delay:1.2s}
#maxess-results-10 .mx-dim-grid{grid-template-columns:repeat(5,minmax(150px,1fr))!important;gap:18px!important}
#maxess-results-10 .mx-dim{--g:#965dff;position:relative!important;min-height:350px!important;border-radius:30px!important;padding:24px 18px!important;text-align:center!important;background:#050507!important;border:1px solid rgba(255,255,255,.13)!important;box-shadow:inset 0 1px rgba(255,255,255,.08),0 28px 80px rgba(0,0,0,.38)!important;overflow:hidden!important}
#maxess-results-10 .mx-dim:nth-child(1){--g:#ff9d3d}#maxess-results-10 .mx-dim:nth-child(2){--g:#ffd84a}#maxess-results-10 .mx-dim:nth-child(3){--g:#38df91}#maxess-results-10 .mx-dim:nth-child(4){--g:#3c9cff}#maxess-results-10 .mx-dim:nth-child(5){--g:#965dff}
#maxess-results-10 .mx-dim::before{content:"";position:absolute;top:22px;left:50%;width:158px;height:158px;transform:translateX(-50%);border-radius:50%;background:conic-gradient(var(--g) calc(var(--score,0)*1%),rgba(255,255,255,.08) 0);filter:drop-shadow(0 0 14px color-mix(in srgb,var(--g) 40%,transparent));transition:background .5s ease}
#maxess-results-10 .mx-dim::after{content:"";position:absolute;top:34px;left:50%;width:134px;height:134px;transform:translateX(-50%);border-radius:50%;background:#050507;box-shadow:inset 0 0 28px rgba(0,0,0,.7),0 0 0 1px color-mix(in srgb,var(--g) 35%,transparent)}
#maxess-results-10 .mx-dim-head{position:relative!important;z-index:2!important;margin-top:54px!important;display:flex!important;flex-direction:column!important;align-items:center!important;gap:7px!important}
#maxess-results-10 .mx-dim-head strong{font-size:44px!important;color:var(--g)!important;text-shadow:0 0 20px color-mix(in srgb,var(--g) 28%,transparent)!important}
#maxess-results-10 .mx-dim .mx-track{position:relative!important;z-index:2!important;width:84%!important;height:7px!important;margin:17px 0 12px!important}
#maxess-results-10 .mx-dim .mx-track span{background:var(--g)!important;box-shadow:0 0 16px color-mix(in srgb,var(--g) 42%,transparent)!important}
#maxess-results-10 .mx-dim p,#maxess-results-10 .mx-lever{position:relative!important;z-index:2!important}
#maxess-results-10 .mx-lever span{color:var(--g)!important}
#maxess-results-10 .mx-aaa-chapter{margin-top:26px;padding:clamp(28px,4vw,54px);border-radius:30px;border:1px solid rgba(150,93,255,.25);background:linear-gradient(145deg,rgba(150,93,255,.1),rgba(255,255,255,.025));box-shadow:0 30px 90px rgba(0,0,0,.3)}
#maxess-results-10 .mx-aaa-chapter h2{margin:8px 0 12px;font-size:clamp(32px,4.2vw,62px);letter-spacing:-.045em}
#maxess-results-10 .mx-aaa-chapter p{max-width:850px;color:rgba(255,255,255,.76);font-size:clamp(16px,1.35vw,20px);line-height:1.6}
#maxess-results-10 .mx-aaa-actions{display:flex;flex-wrap:wrap;gap:10px;margin-top:22px}
#maxess-results-10 .mx-aaa-print{min-height:52px;padding:0 18px;border-radius:15px;border:1px solid rgba(255,255,255,.18);background:#08080c;color:#fff;font-weight:900;cursor:pointer}
#maxess-results-10 .mx-aaa-print:hover,#maxess-results-10 .mx-aaa-print:focus-visible{transform:translateY(-2px);border-color:#b895ff;box-shadow:0 0 28px rgba(150,93,255,.18)}
#maxess-results-10 .mx-aaa-masters{display:grid;grid-template-columns:repeat(6,minmax(0,1fr));gap:12px;margin-top:24px}
#maxess-results-10 .mx-aaa-master{min-height:125px;padding:18px;border:1px solid rgba(255,255,255,.11);border-radius:18px;background:rgba(255,255,255,.035);transition:transform .2s ease,border-color .2s ease,background .2s ease}
#maxess-results-10 .mx-aaa-master:hover,#maxess-results-10 .mx-aaa-master:focus-visible{transform:translateY(-4px);border-color:rgba(180,145,255,.45);background:rgba(150,93,255,.08)}
#maxess-results-10 .mx-aaa-master b{display:block;font-size:13px}#maxess-results-10 .mx-aaa-master span{display:block;margin-top:7px;color:rgba(255,255,255,.58);font-size:11px;line-height:1.4}
#maxess-results-10 .mx-aaa-lever{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-top:24px}
#maxess-results-10 .mx-aaa-lever>div{padding:26px;border-radius:24px;border:1px solid rgba(255,255,255,.11);background:rgba(255,255,255,.035)}
#maxess-results-10 .mx-aaa-lever strong{display:block;margin-top:8px;font-size:clamp(24px,2.5vw,40px);letter-spacing:-.035em}
@keyframes aaa-resonance{0%,100%{transform:scale(.98);opacity:.25}50%{transform:scale(1.03);opacity:.65}}
@media(max-width:1100px){#maxess-results-10 .mx-hero-grid{grid-template-columns:1fr!important;grid-template-areas:"copy" "orb" "side"!important}.mx-aaa-masters{grid-template-columns:repeat(3,1fr)!important}}
@media(max-width:760px){#maxess-results-10 .mx-hero-grid>.mx-score-orb{width:min(88vw,520px)!important;min-width:0!important}.mx-aaa-masters{grid-template-columns:repeat(2,1fr)!important}.mx-aaa-lever{grid-template-columns:1fr!important}.mx-dim-grid{grid-template-columns:1fr!important}}
@media(prefers-reduced-motion:reduce){#maxess-results-10 .mx-aaa-resonance{animation:none!important}#maxess-results-10 *{scroll-behavior:auto!important}}
@media print{#maxess-results-10{width:100%!important;margin:0!important;background:#fff!important;color:#111!important}#maxess-results-10 .mx-aaa-print,#maxess-results-10 .mx-hero-actions,#maxess-results-10 button{display:none!important}#maxess-results-10 .mx-section{break-inside:avoid}#maxess-results-10 .mx-aaa-chapter{background:#fff!important;color:#111!important;box-shadow:none!important;border-color:#ddd!important}#maxess-results-10 .mx-aaa-chapter p,#maxess-results-10 .mx-aaa-master span{color:#333!important}}
</style>
'''

AAA_JS = r'''
<script id="maxess-aaa-checklist-js">
(function(){
'use strict';
var root=document.getElementById('maxess-results-10');
if(!root||root.dataset.aaaChecklistV1==='1')return;
root.dataset.aaaChecklistV1='1';
var names=['Direction','Communication','Evaluation','Iteration','Systems Thinking'];
var colors=['#ff9d3d','#ffd84a','#38df91','#3c9cff','#965dff'];
function clamp(n){return Math.max(0,Math.min(100,Number(n)||0));}
function result(){return window.MAXESS_RESULT||{};}
function dims(){var r=result(),a=Array.isArray(r.dimensions)?r.dimensions:[],map={};a.forEach(function(d){map[String(d.name||'').toLowerCase()]=d;});return names.map(function(name,i){var d=a[i]||map[name.toLowerCase()]||{};return{name:d.name||name,score:clamp(d.score!=null?d.score:d.value)};});}
function overall(ds){var r=result();return clamp(r.overallScore!=null?r.overallScore:r.overall!=null?r.overall:r.score!=null?r.score:(ds.reduce(function(s,d){return s+d.score},0)/(ds.length||1)));}
function palette(v){var stops=[[0,'#ff4b55'],[50,'#ff9d3d'],[65,'#ffd84a'],[75,'#38df91'],[85,'#36d9d1'],[90,'#3c9cff'],[95,'#965dff'],[100,'#ef4bc8']];for(var i=0;i<stops.length-1;i++){var a=stops[i],b=stops[i+1];if(v<=b[0]){var t=(v-a[0])/(b[0]-a[0]);return [a[1],b[1],t];}}return ['#965dff','#ef4bc8',1];}
function applyScore(ds){var v=overall(ds),p=palette(v),orb=root.querySelector('.mx-score-orb'),score=root.querySelector('.mx-score strong'),band=root.querySelector('.mx-band');if(score)score.textContent=Math.round(v);if(band)band.textContent=v<=50?'Foundation':v<=64?'Developing':v<=84?'Advancing':v<=94?'Mastering':'Pinnacle';if(orb){orb.style.setProperty('--aaa-a',p[0]);orb.style.setProperty('--aaa-b',p[1]);orb.style.filter='drop-shadow(0 0 '+Math.round(24+v*.32)+'px '+p[0]+'66)';if(!orb.querySelector('.mx-aaa-resonance')){var r1=document.createElement('i'),r2=document.createElement('i');r1.className='mx-aaa-resonance';r2.className='mx-aaa-resonance r2';orb.appendChild(r1);orb.appendChild(r2);}}var radar=root.querySelector('.mx-radar-center b');if(radar)radar.textContent=Math.round(v);}
function applyDimensions(ds){var cards=Array.prototype.slice.call(root.querySelectorAll('.mx-dim')).slice(0,5);cards.forEach(function(card,i){var d=ds[i];card.style.setProperty('--score',d.score);card.setAttribute('data-score',String(d.score));var strong=card.querySelector('.mx-dim-head strong');if(strong)strong.innerHTML=Math.round(d.score)+'<small>/100</small>';var track=card.querySelector('.mx-track span');if(track)track.style.setProperty('--w',d.score+'%');var h=card.querySelector('.mx-dim-head h3');if(h)h.textContent=d.name;card.setAttribute('aria-label',d.name+' score '+Math.round(d.score)+' out of 100');});}
function strongestLever(ds){var sorted=ds.slice().sort(function(a,b){return b.score-a.score;});return{strongest:sorted[0],lever:sorted[sorted.length-1]};}
function addChapter(ds){var pair=strongestLever(ds),host=root.querySelector('.mx-insight')||root.querySelector('.mx-section');if(!host||root.querySelector('.mx-aaa-chapter'))return;var s=document.createElement('section');s.className='mx-section mx-aaa-chapter';s.innerHTML='<div class="mx-wide"><span class="mx-eyebrow">06 · YOUR BIGGEST LEVER</span><h2>'+pair.lever.name+' is your clearest growth lever.</h2><p>Your strongest signal is <strong>'+pair.strongest.name+'</strong> at '+Math.round(pair.strongest.score)+'/100. Your biggest opportunity is <strong>'+pair.lever.name+'</strong> at '+Math.round(pair.lever.score)+'/100. Focused improvement here can create the greatest return across the rest of your AI practice.</p><div class="mx-aaa-lever"><div><span class="mx-eyebrow">STRONGEST SIGNAL</span><strong>'+pair.strongest.name+' · '+Math.round(pair.strongest.score)+'</strong></div><div><span class="mx-eyebrow">BIGGEST LEVER</span><strong>'+pair.lever.name+' · '+Math.round(pair.lever.score)+'</strong></div></div><div class="mx-aaa-actions"><button class="mx-aaa-print" type="button">Print / Save PDF ↗</button></div></div></section>';host.parentNode.insertBefore(s,host.nextSibling);s.querySelector('.mx-aaa-print').addEventListener('click',function(){window.print();});}
function addMasters(){if(root.querySelector('.mx-aaa-masters'))return;var source=Array.prototype.slice.call(root.querySelectorAll('.mx-area,.mx-naya-door')).slice(0,18);if(!source.length)return;var section=document.createElement('section');section.className='mx-section mx-aaa-chapter';section.innerHTML='<div class="mx-wide"><span class="mx-eyebrow">08 · YOUR NAYA MASTERS</span><h2>18 specialist AI Masters.</h2><p>One connected pathway for turning your result into capability. Each Master is a focused territory you can develop next.</p><div class="mx-aaa-masters"></div></div>';var grid=section.querySelector('.mx-aaa-masters');source.forEach(function(el,i){var title=(el.querySelector('h3')||el.querySelector('b')||el).textContent.trim().replace(/\s+/g,' ');var card=document.createElement('div');card.className='mx-aaa-master';card.tabIndex=0;card.innerHTML='<b>'+String(i+1).padStart(2,'0')+' · '+title.slice(0,48)+'</b><span>Specialist pathway for focused AI mastery.</span>';grid.appendChild(card);});root.appendChild(section);}
function init(){var ds=dims();applyScore(ds);applyDimensions(ds);addChapter(ds);addMasters();}
if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',init,{once:true});else init();
window.addEventListener('maxess:result-ready',init);
})();
</script>
'''

source = SOURCE.read_text(encoding='utf-8')
# Remove the external Results renderer. The complete Groove artifact must be self-contained.
source = re.sub(r'<!-- MAXESS_RESULTS_EXPERIENCE_LOADER -->\s*<script[^>]+MAXESS-RESULTS-EXPERIENCE\.js[^>]*></script>', '', source, flags=re.I)
# Remove previous copies of this exact layer so the build is idempotent.
source = re.sub(r'<!-- MAXESS-AAA-CHECKLIST-V1 -->.*?</script>\s*', '', source, flags=re.S)
# Preserve the complete existing master and append the upgrade layer in-place.
source = source.replace('</body>', AAA_CSS + AAA_JS + '\n</body>', 1)
# Make the final artifact visibly identifiable and auditable.
source = source.replace('<main id="maxess-results-10"', '<main id="maxess-results-10" data-aaa-execution="MAXESS-AAA-CHECKLIST-V1"', 1)
SOURCE.write_text(source, encoding='utf-8')
print('MAXESS AAA checklist layer applied:', SOURCE)
