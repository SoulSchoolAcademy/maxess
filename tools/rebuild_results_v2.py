from pathlib import Path
src=Path('tools/rebuild_results.py').read_text(encoding='utf-8')
old="tail='''\\n\\n</section>\\n\\n\\n</div>\\n</div>\\n</section>'''"
new="tail='''\\n\\n</div>\\n</div>\\n</section>'''"
if old not in src: raise SystemExit('rebuild script boundary pattern not found')
src=src.replace(old,new,1)
exec(compile(src,'tools/rebuild_results.py','exec'),{'__name__':'__main__'})
