"""Independent high-precision ORIGINAL Oily endpoint KL experiment (mpmath).

This is a numerical observation of the authentic R=(1-x)L versus a declared
order-zero L deflation. Mathematical asymptotic derivation is in research note.
"""
from __future__ import annotations
import json
import mpmath as mp
mp.mp.dps=55

def L(x):
    return 1/((2-x*x)*(x*x-2*x+2))

def experiment(a):
    a=mp.mpf(a)
    cuts=[mp.mpf(v) for v in (0,1,4,12,30) if mp.mpf(v)<a]+[a]
    cuts=sorted(set(cuts))
    def i(power,logy=False):
        def f(y):
            if y==0:
                return mp.mpf(0)
            x=1-y/a
            z=(x**a)*L(x)*y**power
            return z*mp.log(y) if logy else z
        return mp.quad(f,cuts)
    I0,I1,J0,J1=i(0),i(1),i(0,True),i(1,True)
    d01=mp.log(I1/I0)-J0/I0
    d10=mp.log(I0/I1)+J1/I1
    return {'a':int(a),'kl_deflated_to_authentic':mp.nstr(d01,26),
            'kl_authentic_to_deflated':mp.nstr(d10,26),
            'symmetric_J':mp.nstr(d01+d10,26),
            'error_to_gamma':mp.nstr(d01-mp.euler,17),
            'error_to_one_minus_gamma':mp.nstr(d10-(1-mp.euler),17)}

def main():
    rows=[experiment(i) for i in (8,16,64,256)]
    assert abs(mp.mpf(rows[-1]['kl_deflated_to_authentic'])-mp.euler)<mp.mpf('.02')
    assert abs(mp.mpf(rows[-1]['kl_authentic_to_deflated'])-(1-mp.euler))<mp.mpf('.02')
    print(json.dumps({'scope':'High precision numerical quadrature, not universal proof',
                      'Euler_gamma':mp.nstr(mp.euler,30),'rows':rows},indent=2))

if __name__=='__main__':main()
