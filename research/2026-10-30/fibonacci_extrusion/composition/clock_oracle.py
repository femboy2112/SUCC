"""Separate exact symbolic check of FIC05 clock defects; no producer import."""
import json
from pathlib import Path
import sympy as s
root=Path(__file__).resolve().parent
x=s.symbols('x',positive=True)
R=(15*x*x+121*x+240)/(x*(x+3)*(x+4)*(x+5))
m=-s.diff(s.log(R),x)
rows=[]
for row in json.loads((root/'clock_receipt.json').read_text())['rows']:
    a=s.Rational(row['a']);z=s.Rational(row['s']);c=row['c'];d=row['d']
    val=s.cancel((c+d)*m.subs(x,a+z)-c*m.subs(x,a+c*z)-d*m.subs(x,a+d*z))
    assert val==s.Rational(row['mean_defect'])
    gamma=2*(c+d)/(a+z)-2*c/(a+c*z)-2*d/(a+d*z)
    assert gamma>0
    rows.append({'n':row['n'],'a':row['a'],'source_mean_defect':str(val),'gamma_control_defect':str(gamma),'status':'PASS'})
p=root/'clock_oracle_receipt.json'
if p.exists():raise SystemExit('refusing overwrite')
record={'status':'PASS','sympy':s.__version__,'method':'logarithmic derivative of factored rational transform','rows':rows}
p.write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
