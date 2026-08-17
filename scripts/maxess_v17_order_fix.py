from pathlib import Path
import re

path = Path('MAXESS-RESULTS-10-GROOVE.html')
text = path.read_text(encoding='utf-8')
pattern = r'(<script id="MAXESS_RESULTS_V17_EXECUTION">)(.*?)(</script>)'
match = re.search(pattern, text, re.S)
if not match:
    raise SystemExit('V17 script not found')
js = match.group(2)
old = """var conversion=document.querySelector('.ny-page-inner');if(conversion){var theater=conversion.querySelector('.ny-theater'),primary=conversion.querySelector('.ny-primary-zone');if(theater||primary){var cv=el('section','mx-section v17-conversion');if(theater)cv.appendChild(theater);var mv=el('div','v17-your-move');mv.innerHTML='<h2>YOUR MOVE</h2><p>Watch the video. Then start your free trial.</p>';if(primary)mv.appendChild(primary);cv.appendChild(mv);root.appendChild(cv)}conversion.remove()}"""
new = """var cv=null;var membershipSeal=null;var conversion=document.querySelector('.ny-page-inner');if(conversion){var theater=conversion.querySelector('.ny-theater'),primary=conversion.querySelector('.ny-primary-zone');membershipSeal=conversion.querySelector('.ny-membership');if(theater||primary){cv=el('section','mx-section v17-conversion');if(theater)cv.appendChild(theater);var mv=el('div','v17-your-move');mv.innerHTML='<h2>YOUR MOVE</h2><p>Watch the video. Then start your free trial.</p>';if(primary)mv.appendChild(primary);cv.appendChild(mv)}if(membershipSeal)membershipSeal.remove();conversion.remove()}"""
if old not in js:
    raise SystemExit('conversion block not found')
js = js.replace(old, new)
old2 = """var pathways=sec(function(e){return /18 AI PATHWAYS/i.test(tx(e))||e.querySelector('.mx-areas')});if(pathways){pathways.classList.add('v17-masters-section');var h=pathways.querySelector('.mx-section-head');if(h){var e=h.querySelector('.mx-eyebrow'),hh=h.querySelector('h2'),p=h.querySelector('p');if(e)e.textContent='18 NAYA MASTERS';if(hh)hh.textContent='INCLUDES EVERYTHING';if(p)p.textContent='All 18 Naya Masters are included — each one is a capability you can develop with Naya.'}var areas=pathways.querySelector('.mx-areas');var profiles=el('div','v17-masters-grid');Array.prototype.slice.call(areas.querySelectorAll('.mx-area')).forEach(function(card){var n=(card.querySelector('h3')||{}).textContent||'AI Master',d=(card.querySelector('p')||{}).textContent||'',m=(card.querySelector('.mx-area-relevance em')||{}).style&&card.querySelector('.mx-area-relevance em').style.getPropertyValue('--w')||'0%';var q=el('article','v17-master-profile');q.innerHTML='<h3>'+n+'</h3><div class="profile-kicker">AI PROFILE</div><p>'+d+'</p><div class="profile-meter"><i style="--w:'+m+'"></i></div>';profiles.appendChild(q)});areas.replaceWith(profiles);var seal=document.querySelector('.ny-membership');if(seal)pathways.insertBefore(seal,pathways.firstChild);root.appendChild(pathways)}
var playground=sec(function(e){return e.id==='naya-playground'});if(playground){playground.classList.add('v17-playground');root.appendChild(playground)}
var final=root.querySelector('.mx-final');if(final){final.classList.add('v17-philosophy');final.innerHTML='<span class="mx-eyebrow">NAYA + HUMAN</span><h2>Technology should amplify the human.</h2><p>Naya helps you understand your capability, turn insight into action, and use AI in service of what matters to you.</p>';root.appendChild(final)}
root.querySelectorAll('.mx-insight,#growth-scorecard').forEach(function(e){e.remove()});
if(pattern)root.appendChild(pattern);if(meaningSec)root.appendChild(meaningSec);if(strength)root.appendChild(strength);if(lever)root.appendChild(lever);if(action)root.appendChild(action);"""
new2 = """var pathways=sec(function(e){return /18 AI PATHWAYS/i.test(tx(e))||e.querySelector('.mx-areas')});if(pathways){pathways.classList.add('v17-masters-section');var h=pathways.querySelector('.mx-section-head');if(h){var e=h.querySelector('.mx-eyebrow'),hh=h.querySelector('h2'),p=h.querySelector('p');if(e)e.textContent='18 NAYA MASTERS';if(hh)hh.textContent='INCLUDES EVERYTHING';if(p)p.textContent='All 18 Naya Masters are included — each one is a capability you can develop with Naya.'}var areas=pathways.querySelector('.mx-areas');var profiles=el('div','v17-masters-grid');Array.prototype.slice.call(areas.querySelectorAll('.mx-area')).forEach(function(card){var n=(card.querySelector('h3')||{}).textContent||'AI Master',d=(card.querySelector('p')||{}).textContent||'',m=(card.querySelector('.mx-area-relevance em')||{}).style&&card.querySelector('.mx-area-relevance em').style.getPropertyValue('--w')||'0%';var q=el('article','v17-master-profile');q.innerHTML='<h3>'+n+'</h3><div class="profile-kicker">AI PROFILE</div><p>'+d+'</p><div class="profile-meter"><i style="--w:'+m+'"></i></div>';profiles.appendChild(q)});areas.replaceWith(profiles);if(membershipSeal)pathways.insertBefore(membershipSeal,pathways.firstChild)}
var playground=sec(function(e){return e.id==='naya-playground'});if(playground)playground.classList.add('v17-playground');
var final=root.querySelector('.mx-final');if(final){final.classList.add('v17-philosophy');final.innerHTML='<span class="mx-eyebrow">NAYA + HUMAN</span><h2>Technology should amplify the human.</h2><p>Naya helps you understand your capability, turn insight into action, and use AI in service of what matters to you.</p>}
root.querySelectorAll('.mx-insight,#growth-scorecard').forEach(function(e){e.remove()});
var ordered=[bridge,hero,dims,listen,pattern,meaningSec,strength,lever,action,cv,pathways,playground,final];ordered.forEach(function(node){if(node)root.appendChild(node)});"""
if old2 not in js:
    raise SystemExit('ordering block not found')
js = js.replace(old2, new2)
text = text[:match.start(2)] + js + text[match.end(2):]
path.write_text(text, encoding='utf-8')
print('V17 order fix applied')
