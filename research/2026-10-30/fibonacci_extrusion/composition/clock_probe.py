from pathlib import Path
from fractions import Fraction as F
from fib_composition import *
import json
rows=[]
for a in [F(17),F(97,3),F(233)]:
    for n in [4,5,8,13]:
        d=clock_defect(a,F(3,7),n);b=clock_defect_lower(a,F(3,7),n)
        assert d>b>0
        rows.append({'a':str(a),'s':'3/7','n':n,'c':fib(n-2),'d':fib(n-1),
                     'mean_defect':str(d),'lower_bound':str(b),'status':'PASS'})
record={'status':'PASS','authority':'exact rational mean defects; paper law-classification proof separate','rows':rows}
p=Path(__file__).with_name('clock_receipt.json')
if p.exists():raise SystemExit('refusing overwrite')
p.write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
