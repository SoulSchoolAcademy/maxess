from pathlib import Path
p=Path('tools/results_experience_v4.py')
s=p.read_text(encoding='utf-8')
old='''ANCHOR = ''' + "'''    </div>\\n\\n\\n    <!-- ==================================================\\n       DIMENSIONS'''
new='''ANCHOR = ''' + "'''    </div>\\n\\n  </div>\\n\\n\\n  <!-- ==================================================\\n       DIMENSIONS'''
if old not in s:
    raise RuntimeError('Expected V4 results anchor definition not found')
s=s.replace(old,new,1)
p.write_text(s,encoding='utf-8')
print('fixed V4 results insertion anchor')
