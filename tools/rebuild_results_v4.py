from pathlib import Path
src=Path('tools/rebuild_results.py').read_text(encoding='utf-8')
src=src.replace("anchor='''<!-- ==================================================\\n       RESULTS\\n  ================================================== -->'''","anchor_re=__import__('re').compile(r'<!--\\s*=+\\s*RESULTS\\s*=+\\s*-->')",1)
src=src.replace('a=s.find(anchor); b=s.find(tail,a)','m=anchor_re.search(s); a=m.start() if m else -1; b=s.find(\'\\n</div>\\n</div>\\n</section>\',a)',1)
src=src.replace("b+=len('\\n\\n</section>')","b+=len('\\n</div>\\n</div>\\n</section>')",1)
if 'anchor_re' not in src or 'm=anchor_re.search' not in src: raise SystemExit('failed to patch rebuild script')
exec(compile(src,'tools/rebuild_results.py','exec'),{'__name__':'__main__'})
