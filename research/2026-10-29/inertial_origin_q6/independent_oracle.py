"""Independent SymPy/mpmath/numpy checks of the inertial-origin carry formulas.
Numerical observations are not substitutes for the paper proofs.
"""
from __future__ import annotations
import json
from pathlib import Path
from fractions import Fraction as F
from math import gcd
import mpmath as mp
import numpy as np
import sympy as sp

mp.mp.dps = 76

def rt(n):
    # Independent reduced polynomial source, rather than four partial fractions.
    n=sp.Integer(n)
    return sp.Rational(120*n*n-89*n+16, (2*n-1)*(4*n-1)*(8*n-7)*(8*n-3))

def to_mp(r):
    return mp.mpf(int(sp.numer(r)))/int(sp.denom(r))

def compare_signed_carry_integral(n,k,h):
    r=to_mp(rt(n))
    if k==0:low,hi=mp.mpf(0),(1-r)/16
    elif k==16:low,hi=(16-r)/16,mp.mpf(1)
    else:low,hi=(k-r)/16,(k+1-r)/16
    observed=mp.quad(lambda x:mp.exp(2j*mp.pi*h*(16*x+r-k)),[low,hi])
    jf=(mp.exp(2j*mp.pi*h*r)-1)/(2j*mp.pi*h)
    predicted=-jf/16 if k==0 else jf/16 if k==16 else mp.mpc(0)
    return abs(observed-predicted)


def check_four_poles():
    n=sp.symbols('n',positive=True,integer=True)
    a=8*n-7
    raw=4/a-2/(a+3)-1/(a+4)-1/(a+5)
    reduced=(120*n*n-89*n+16)/((2*n-1)*(4*n-1)*(8*n-7)*(8*n-3))
    assert sp.simplify(raw-reduced)==0
    lower=15/(a*(a+5))
    # manifest positivity as 6/(a(a+3))+4/(a(a+4))+5/(a(a+5)).
    identity=sp.simplify(raw-(6/(a*(a+3))+4/(a*(a+4))+5/(a*(a+5))))
    assert identity==0
    return {'exact_partial_fraction_to_reduced':True,'exact_positive_decomposition':True}


def calc_fft_average(N=3,K=5):
    # Discrete Haar quadrature is exact for all frequency differences when
    # 16^K exceeds the largest |16^n-16^m|, up to floating evaluation.
    M=16**K
    x=np.arange(M,dtype=np.float64)/M
    phase=np.zeros(M,dtype=np.complex128)
    base=0.0
    for n in range(1,N+1):
        rn=float(rt(n))
        base=16*base+rn
        phase +=np.exp((2j*np.pi)*(16**n*x+base))
    observed=float(np.mean(abs(phase/N)**2))
    return {'N':N,'M':M,'observed':observed,'exact_prediction':1/N,'error':abs(observed-1/N)}

def calc_coherent_seed(n):
    # Independent high precision π expression for initial advanced seed.
    seed=-mp.pi/16
    u=seed
    for t in range(1,n+1): u=16*u+to_mp(rt(t))
    tail=mp.nsum(lambda j:mp.power(16,-j)*to_mp(rt(n+int(j))),[1,100])
    # No exact rational arithmetic in this oracle, unlike source probe.
    return {'n':n,'tail_error':float(abs(u+tail)),
            'fractional_phase':float(u-mp.floor(u)),
            'last_carry':int(mp.floor(16*( (u-to_mp(rt(n)))/16 - mp.floor((u-to_mp(rt(n)))/16)) + to_mp(rt(n))))}

def boundary_condition(n):
    return float(1-16*to_mp(rt(n))-to_mp(rt(n+1)))

def main():
    results={'symbolic':check_four_poles(), 'integrals':[], 'fft':[], 'coherent':[], 'transition_margin':{}}
    for n in (2,3,5,9):
        for h in (1,3):
            for k in (0,1,7,15,16):
                error=compare_signed_carry_integral(n,k,h)
                assert error<mp.mpf('1e-65'),(n,k,h,error)
                results['integrals'].append({'n':n,'h':h,'carry':k,'error':float(error)})
    for N,K in ((2,4),(3,5)):
        r=calc_fft_average(N,K)
        assert r['error']<1e-12,r
        results['fft'].append(r)
    for n in (2,4,8,13):
        r=calc_coherent_seed(n)
        assert r['tail_error']<1e-50,r
        assert r['last_carry']==15,r
        results['coherent'].append(r)
    for n in (3,4,5,8,30):
        margin=boundary_condition(n)
        assert margin>0
        results['transition_margin'][n]=margin
    out=Path(__file__).with_name('independent_receipt.json')
    out.write_text(json.dumps(results,indent=2,sort_keys=True)+'\n')
    print('Independent original-source symbolic, carry-integral, FFT and coherent-seed checks: PASS')
    print('carry integral checks',len(results['integrals']),'max error',max(x['error'] for x in results['integrals']))
    print('FFT checks',results['fft'])
    print('coherent checks',results['coherent'])
    print('transition strict margin min',min(results['transition_margin'].values()))

if __name__=='__main__':main()
