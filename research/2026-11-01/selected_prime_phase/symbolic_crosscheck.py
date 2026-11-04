"""Optional independent SymPy symbolic checks; not Lean/kernel proof authority."""
from __future__ import annotations
import json
import sympy as s

x=s.symbols('x',positive=True)
source=4/(8*x-7)-2/(8*x-4)-1/(8*x-3)-1/(8*x-2)
combined=(120*x*x-89*x+16)/((2*x-1)*(4*x-1)*(8*x-7)*(8*x-3))
a=8*x-7
edges=2*(1/a-1/(a+3))+(1/a-1/(a+4))+(1/a-1/(a+5))
assert s.factor(source-combined)==0
assert s.factor(source-edges)==0
assert s.limit(x**2*source,x,s.oo)==s.Rational(15,64)
assert s.factor(source-s.Rational(15,64)/x**2).subs(x,4)>0
r1=source.subs(x,1)
r2=source.subs(x,2)
assert r1==s.Rational(47,15) and r2==s.Rational(106,819)
p=s.Integer(257)
assert pow(16,2,257)==256 and pow(16,4,257)==1
assert (s.Rational(1,2)-(s.Rational(176,1799)**2)/4)>s.Rational(49,100)
assert s.factor((s.Integer(1)+(p-2)*p)-(p-1)**2)==0
print(json.dumps({'sympy_version':s.__version__,'exact_checks':8,'status':'PASS',
 'source_leading_curvature':'15/64','original_r1':str(r1),'original_r2':str(r2)},indent=2))
