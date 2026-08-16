/* MAXESS 10.10 dynamic renderer
 * Reads only window.MAXESS_RESULT. Never reads score text back from the DOM.
 */
(function(){
  'use strict';
  var ROOT_ID='maxess-results-10';
  var META=[
    ['direction','Direction'],['communication','Communication'],['evaluation','Evaluation'],['iteration','Iteration'],['systems-thinking','Systems Thinking']
  ];
  function clamp(n){n=Number(n);return isFinite(n)?Math.max(0,Math.min(100,n)):0;}
  function band(score){if(score<=50)return 'Foundation';if(score<=75)return 'Developing';if(score<=90)return 'Advancing';return 'Mastering';}
  function normalize(){
    var r=window.MAXESS_RESULT;if(!r)return null;
    var dims=(r.dimensions||[]).slice(0,5).map(function(d,i){return {id:String(d.id||META[i][0]),name:String(d.name||META[i][1]),score:clamp(d.score),description:String(d.description||''),insight:String(d.insight||'')};});
    if(dims.length<5)return null;
    return {overallScore:clamp(r.overallScore),band:String(r.band||band(r.overallScore)),dimensions:dims};
  }
  function setText(el,v){if(el)el.textContent=v;}
  function render(){
    var root=document.getElementById(ROOT_ID),r=normalize();if(!root||!r)return;
    setText(root.querySelector('.mx-score strong'),Math.round(r.overallScore));
    setText(root.querySelector('.mx-band'),r.band);
    setText(root.querySelector('.mx-radar-center b'),Math.round(r.overallScore));
    root.querySelectorAll('.mx-list-row').forEach(function(row,i){var d=r.dimensions[i];if(!d)return;setText(row.querySelector('b'),d.name);setText(row.querySelector('strong'),Math.round(d.score));var bar=row.querySelector('.mx-bar span');if(bar)bar.style.setProperty('--w',d.score+'%');});
    root.querySelectorAll('.mx-scorecard-row').forEach(function(row,i){var d=r.dimensions[i];if(!d)return;setText(row.querySelector('span'),d.name);setText(row.querySelector('b'),Math.round(d.score));var bar=row.querySelector('i');if(bar)bar.style.setProperty('--w',d.score+'%');});
    var rails=root.querySelectorAll('.mx-band-rail div');rails.forEach(function(el){el.classList.remove('active');var t=(el.textContent||'').trim();if(t.indexOf(r.band)!==-1)el.classList.add('active');});
    var ranked=r.dimensions.slice().sort(function(a,b){return b.score-a.score;});
    var strength=ranked[0],opportunity=ranked[ranked.length-1];
    var quote=root.querySelector('.mx-quote');
    if(quote)quote.innerHTML='Your strongest signal is <strong>'+escapeHtml(strength.name)+'</strong> — and your biggest leverage opportunity is <strong>'+escapeHtml(opportunity.name)+'</strong>.';
    var note=root.querySelector('.mx-note');
    if(note)note.textContent='Your result is not a judgment. It is a pattern: '+strength.name+' is currently carrying more of your AI capability, while '+opportunity.name+' offers the clearest place to create additional leverage.';
    var growth=root.querySelector('.mx-growth-card h3');if(growth)growth.innerHTML='You\'re in<br>'+escapeHtml(r.band)+'.';
    root.setAttribute('data-result-source','window.MAXESS_RESULT');
  }
  function escapeHtml(v){return String(v).replace(/[&<>"']/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c];});}
  if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',render,{once:true});else render();
})();
