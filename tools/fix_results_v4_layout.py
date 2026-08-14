from pathlib import Path

p=Path('code')
s=p.read_text(encoding='utf-8')
old='.results-v4-steps{display:grid;grid-template-columns:repeat(7,1fr);gap:7px;margin-top:25px}'
new='.results-v4-steps{display:flex;align-items:stretch;justify-content:center;gap:7px;margin-top:25px}.results-v4-steps .results-v4-step{flex:1;min-width:0}.results-v4-steps .results-v4-arrow{flex:0 0 auto}'
if old in s:
    s=s.replace(old,new,1)
old_mobile='.results-v4-steps{grid-template-columns:repeat(2,1fr)}.results-v4-step:last-child{grid-column:1/-1}'
new_mobile='.results-v4-steps{display:grid;grid-template-columns:repeat(2,1fr)}.results-v4-step:last-child{grid-column:1/-1}.results-v4-arrow{display:none}'
if old_mobile in s:
    s=s.replace(old_mobile,new_mobile,1)
p.write_text(s,encoding='utf-8')
print('results v4 layout normalization applied')
