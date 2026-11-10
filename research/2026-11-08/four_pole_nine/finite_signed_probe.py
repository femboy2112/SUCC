"""Finite exploratory three-channel signed cumulants on frozen original BBP.

Predeclared epochs A=17,31,61,127; h=1,2. Uses reduced exact Fractions
and float circular characters for display only. NOT interval certified.
"""
import cmath
import json
from fractions import Fraction
from pathlib import Path
from math import pi

CLOCKS=(17,31,61,127)
HARMONICS=(1,2)


def r_channels(n):
    a=8*n-7
    return (Fraction(6,a*(a+3)),Fraction(4,a*(a+4)),Fraction(5,a*(a+5)))


def centered_cubic(rows):
    N=len(rows)
    mean=lambda f:sum(map(f,rows))/N
    m=[mean(lambda x:x[i]) for i in range(3)]
    p={(i,j):mean(lambda x:x[i]*x[j]) for i,j in ((0,1),(0,2),(1,2))}
    third=mean(lambda x:x[0]*x[1]*x[2])
    kappa=third-m[0]*p[1,2]-m[1]*p[0,2]-m[2]*p[0,1]+2*m[0]*m[1]*m[2]
    recon=kappa + m[0]*(p[1,2]-m[1]*m[2]) +m[1]*(p[0,2]-m[0]*m[2]) +m[2]*(p[0,1]-m[0]*m[1]) + m[0]*m[1]*m[2]
    assert abs(recon-third)<5e-13
    return dict(W_abs=abs(third), kappa_abs=abs(kappa), max_marginal_abs=max(map(abs,m)),
                max_pairwise_moment_abs=max(map(abs,p.values())), max_covariance_abs=max(abs(p[i,j]-m[i]*m[j]) for i,j in p),
                signed_triple_re=third.real,signed_triple_im=third.imag)


def phases():
    v=[Fraction(0)]*3
    for n in range(1,2*max(CLOCKS)):
        for i,r in enumerate(r_channels(n)):
            v[i]=16*v[i]+r
        yield n,tuple(float(x%1) for x in v)


def run():
    history=dict(phases())
    out=[]
    for A in CLOCKS:
        for h in HARMONICS:
            rows=[tuple(cmath.exp(2j*pi*h*x) for x in history[n]) for n in range(A,2*A)]
            d=centered_cubic(rows)
            out.append(dict(A=A,h=h,**{k:round(v,13) for k,v in d.items()}))
    return {'scope':'FINITE_FLOAT_DIAGNOSTIC_NOT_CERTIFICATE',
            'original_source':'six, four, five first-difference forcing, U0=0',
            'predeclared_epochs':list(CLOCKS),'predeclared_harmonics':list(HARMONICS),
            'results':out}

if __name__=='__main__':
    o=run()
    dest=Path(__file__).with_name('FINITE_SIGNED_DIAGNOSTIC.json')
    dest.write_text(json.dumps(o,indent=2,sort_keys=True)+'\n',encoding='utf8')
    print(json.dumps(o,indent=2,sort_keys=True))
