from pathlib import Path
import re, subprocess, tempfile
src=Path('tools/rebuild_results_v4.py').read_text(encoding='utf-8')
exec(compile(src,'tools/rebuild_results_v4.py','exec'),{'__name__':'__main__'})
p=Path('code'); s=p.read_text(encoding='utf-8')
repl={'#fff.045':'rgba(255,255,255,.045)','#fff.012':'rgba(255,255,255,.012)','#fff.022':'rgba(255,255,255,.022)','#fff0.07':'rgba(255,255,255,.07)','#fff1':'rgba(255,255,255,.1)','#fff2':'rgba(255,255,255,.2)','#fff9':'rgba(255,255,255,.6)'}
for a,b in repl.items(): s=s.replace(a,b)
scripts=re.findall(r'<script(?:\s[^>]*)?>([\s\S]*?)</script>',s,re.I)
if len(scripts)<2: raise SystemExit(f'expected assessment + Results scripts, found {len(scripts)}')
for i,x in enumerate(scripts,1):
    f=Path(tempfile.gettempdir())/f'maxess-{i}.js'; f.write_text(x,encoding='utf-8'); subprocess.run(['node','--check',str(f)],check=True)
p.write_text(s,encoding='utf-8')
print('RESULTS BUILD VERIFIED',len(s.splitlines()),'lines',len(s),'bytes',len(scripts),'scripts')
