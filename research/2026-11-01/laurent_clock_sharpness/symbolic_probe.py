"""Optional independent symbolic derivatives and limits; not Lean proof authority."""
from __future__ import annotations
import json
from fractions import Fraction as F
import sympy as sp
import sharpness as exact


def run():
    x=sp.symbols('x',positive=True)
    poles=[(4,sp.Rational(7,8)),(-2,sp.Rational(1,2)),(-1,sp.Rational(3,8)),(-1,sp.Rational(1,4))]
    cnt=0
    for d,k in ((1,1),(1,2),(2,1),(2,2),(2,3),(3,1),(3,2),(4,1)):
        source=sum(sp.Rational(w,8)/(x+j-p)*16**(k-j) for j in range(1,k+1) for w,p in poles)
        coeff=sum(sp.Rational(w,8)*(p-j)**a/ x**(a+1)*16**(k-j)
                  for j in range(1,k+1) for a in range(1,d) for w,p in poles)
        r=sp.cancel(source-coeff)
        c=sp.Rational(exact.finite_leading(k,d).numerator,exact.finite_leading(k,d).denominator)
        assert sp.simplify(sp.limit(x**(d+1)*r/16**k,x,sp.oo)-c)==0
        cnt+=1
        assert sp.simplify(sp.limit(x**(d+2)*sp.diff(r,x)/16**k,x,sp.oo)+(d+1)*c)==0
        cnt+=1
        assert sp.simplify(sp.limit(x**(d+3)*sp.diff(r,x,2)/16**k,x,sp.oo)-(d+1)*(d+2)*c)==0
        cnt+=1
    assert sp.factor(sum(sp.Rational(w,8)/(x-p) for w,p in poles)) == sp.factor((120*x**2-89*x+16)/((2*x-1)*(4*x-1)*(8*x-7)*(8*x-3)))
    cnt+=1
    return {'status':'EXACT_SYMBOLIC_PASS','identities':cnt,'order_pairs':8,'method':'sympy derivative+limit, independent of Fraction derivative oracle'}


if __name__=='__main__':print(json.dumps(run(),indent=2,sort_keys=True))
