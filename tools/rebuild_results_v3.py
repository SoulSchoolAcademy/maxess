from pathlib import Path
src=Path('tools/rebuild_results.py').read_text(encoding='utf-8')
old="a=s.find(anchor); b=s.find(tail,a)\nif a<0 or b<0: raise SystemExit('results boundary not found')\nb+=len('\\n\\n</section>')"
new="a=s.find(anchor); b=s.find('\\n</div>\\n</div>\\n</section>',a)\nif a<0 or b<0: raise SystemExit('results boundary not found')\nb+=len('\\n</div>\\n</div>\\n</section>')"
if old not in src: raise SystemExit('boundary code not found in rebuild script')
exec(compile(src.replace(old,new,1),'tools/rebuild_results.py','exec'),{'__name__':'__main__'})
