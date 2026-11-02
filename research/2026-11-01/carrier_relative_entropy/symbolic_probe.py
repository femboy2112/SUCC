"""Optional independent SymPy algebra audit; no floating output used as proof."""
from __future__ import annotations
import json


def main():
    import sympy as S
    n,j,k=S.symbols('n j k', integer=True, positive=True)
    r=4/(8*n-7)-2/(8*n-4)-1/(8*n-3)-1/(8*n-2)
    combined=(120*n*n-89*n+16)/((2*n-1)*(4*n-1)*(8*n-7)*(8*n-3))
    diff=S.factor(r-S.Rational(15,64)/n**2)
    den=64*n*n*(2*n-1)*(4*n-1)*(8*n-7)*(8*n-3)
    numer=9664*n**3-9656*n**2+3090*n-315
    assert S.cancel(r-combined)==0
    assert S.cancel(diff-numer/den)==0
    weights=(4,-2,-1,-1)
    poles=(S.Rational(7,8),S.Rational(1,2),S.Rational(3,8),S.Rational(1,4))
    assert sum(weights)==0
    def coeff(a):return S.expand(sum(S.Rational(w,8)*(p-j)**a for w,p in zip(weights,poles)))
    assert coeff(0)==0
    assert coeff(1)==S.Rational(15,64)
    assert coeff(2)==(151-240*j)/512
    x=S.Rational(1,16)
    v=S.symbols('v')
    f=v/(1-v)
    exact_moments=[]
    for d in range(6):
        exact_moments.append(str(S.cancel(f.subs(v,S.Rational(1,16)))))
        f=S.factor(v*S.diff(f,v))
    expected=['1/15','16/225','272/3375','1712/16875','37808/253125','201968/759375']
    assert exact_moments==expected
    print(json.dumps({'symbolic_checks':6,'status':'PASS','source_poles':list(map(str,poles)),
                      'source_leading_coefficient':'15/64','source_third_coefficient':'(151-240j)/512',
                      'exact_power_moments':exact_moments},indent=2,sort_keys=True))

if __name__=='__main__':main()
