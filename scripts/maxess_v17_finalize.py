from pathlib import Path
import re

path = Path('MAXESS-RESULTS-10-GROOVE.html')
text = path.read_text(encoding='utf-8')
marker = 'MAXESS_RESULTS_V17_FINALIZE'
if marker in text:
    print('V17 finalizer already present.')
    raise SystemExit(0)
if 'MAXESS_RESULTS_V17_EXECUTION' not in text:
    raise SystemExit('V17 execution was not applied to the working file.')

finalizer = r'''<script id="MAXESS_RESULTS_V17_FINALIZE">
(function(){
  'use strict';
  var root=document.getElementById('maxess-results-10');
  if(!root) return;
  var text=function(e){return (e&&e.textContent||'').replace(/\s+/g,' ').trim()};
  var section=function(fn){return Array.prototype.slice.call(root.children).find(function(e){return e.tagName==='SECTION'&&fn(e)})||null};
  var hero=section(function(e){return e.classList.contains('mx-hero')});
  var dims=section(function(e){return e.classList.contains('v17-dimensions')||/YOUR FIVE DIMENSIONS|YOUR AI CAPABILITIES/i.test(text(e))});
  var listen=root.querySelector('.v17-listen');
  var pattern=section(function(e){return e.classList.contains('v17-pattern-section')||e.id==='your-fingerprint'||/See the pattern/i.test(text(e))});
  var meaning=section(function(e){return e.classList.contains('v17-meaning-section')});
  var strength=section(function(e){return e.classList.contains('v17-strength-section')});
  var lever=section(function(e){return e.classList.contains('v17-lever-section')});
  var action=section(function(e){return e.classList.contains('v17-action-section')});
  var conversion=section(function(e){return e.classList.contains('v17-conversion')});
  var masters=section(function(e){return e.classList.contains('v17-masters-section')});
  var playground=section(function(e){return e.classList.contains('v17-playground')||e.id==='naya-playground'});
  var final=section(function(e){return e.classList.contains('v17-philosophy')||e.classList.contains('mx-final')});
  var banner=document.querySelector('.v17-naya-banner');
  var bridge=document.getElementById('naya-report');
  if(bridge) bridge.style.display='contents';
  var order=[bridge,hero,dims,listen,pattern,meaning,strength,lever,action,conversion,masters,playground,final];
  order.forEach(function(node){if(node&&node.parentNode===root)root.appendChild(node)});
  root.setAttribute('data-maxess-v17-final-order','NAYA>SCORE>DIMENSIONS>LISTEN>PATTERN>MEANING>STRENGTH>LEVER>ACTION>VIDEO>TRIAL>MASTERS>PLAYGROUND>PHILOSOPHY');
  if(banner) banner.setAttribute('aria-label','Naya introduction to your MAXESS results');
})();
</script>'''

needle = '</body>'
if needle not in text:
    raise SystemExit('Could not locate document body close.')
text = text.replace(needle, finalizer + '\n' + needle, 1)
path.write_text(text, encoding='utf-8')
print('V17 finalizer applied directly to MAXESS-RESULTS-10-GROOVE.html')
