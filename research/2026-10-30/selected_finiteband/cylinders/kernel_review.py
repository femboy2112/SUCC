"""Complementary finite check of kernel K01/K02; no kernel-code imports."""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json
import sympy as s


def r(n):
    return F(4,8*n-7)-F(2,8*n-4)-F(1,8*n-3)-F(1,8*n-2)


def run():
    rows=[]
    for H in (3,7,19,73,239):
        moment=sum((h*h*(1-F(abs(h),H)) for h in range(-H+1,H)),F())
        assert moment==F(H*(H*H-1),6)
        rows.append(dict(H=H,weighted_second_moment=str(moment)))
    source_checks=0
    for n in (1,2,3,7,29,113,557):
        lo=sum((r(n+j)/16**j for j in range(1,15)),F())
        hi=lo+r(n+15)/(15*16**14)
        assert 0<lo<hi<1/F(64*n*n)
        assert r(n+1)/15<=1/F((8*n+1)*(8*n+4))
        source_checks+=1
    H=s.symbols('H',positive=True)
    D=2*s.pi*s.sqrt(H*(H**2-1)/6)
    A=s.sqrt(2*H)
    C2=s.pi/(8*s.sqrt(3))
    assert s.simplify(4*A*D/64-C2*H*s.sqrt(H**2-1))==0
    u=s.symbols('u',positive=True)
    integral=s.sqrt(s.pi)/16*2*s.integrate((1-u)*s.sqrt(4*s.pi*u),(u,0,1))
    assert s.simplify(integral-s.pi/15)==0
    n=s.symbols('n',positive=True)
    rational=4/(8*n-7)-2/(8*n-4)-1/(8*n-3)-1/(8*n-2)
    assert s.limit(n*n*rational,n,s.oo)==s.Rational(15,64)
    paper=Path(__file__).resolve().parent.parent/'kernel/KERNEL_TRANSPORT.md'
    return dict(status='PASS',paper_sha256=hashlib.sha256(paper.read_bytes()).hexdigest(),
                exact_moments=rows,source_tail_cases=source_checks,
                hilbert_constant_square=str(C2),mellin_value=str(integral),
                scope='same-model complementary proof review and fresh exact symbolic cases')


if __name__=='__main__':
    print(json.dumps(run(),indent=2))
