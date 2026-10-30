"""Independent high-precision analytic oracle, NOT proof / interval arithmetic.

Run with mpmath >=1.3, sympy optional; no full repository checkout needed.
"""
from __future__ import annotations
from fractions import Fraction
from math import gcd
from pathlib import Path
from mpmath import mp
from sympy import mobius as sp_mobius, totient as sp_totient

mp.dps=45

def sigma_minus3(h):
    return sum(mp.mpf(d)**(-3) for d in range(1,h+1) if h%d==0)

def coeff(h,y):
    h=abs(h)
    assert h>=1 and y>0
    return mp.pi/(2*mp.zeta(4)*y)*(1+2*mp.pi*y*h)*mp.exp(-2*mp.pi*y*h)*sigma_minus3(h)

def const_term(y):
    return y*y+mp.pi*mp.zeta(3)/(2*mp.zeta(4)*y)

def E(x,y,H=24):
    return const_term(y)+2*sum(coeff(h,y)*mp.cos(2*mp.pi*h*x) for h in range(1,H+1))

def L(t,cutoff=11):
    return sum(int(sp_mobius(d))*mp.exp(-t*d)/(4*(1-mp.exp(-t*d))**2) for d in range(1,cutoff+1,2))

def M(s):
    return mp.gamma(s)*mp.zeta(s-1)/(4*(1-mp.power(2,-s))*mp.zeta(s))

def assert_close(label,got,expected,atol='1e-25'):
    error=abs(got-expected)
    if error>=mp.mpf(atol):
        raise AssertionError(f'{label}: {mp.nstr(got,30)} vs {mp.nstr(expected,30)}, error={mp.nstr(error)}')
    print(f'PASS {label} error={mp.nstr(error,5)}')

def run():
    # Independent calculation of primitive/cototient Oily defect at t=log 4
    t=mp.log(4)
    lost=L(t,49)
    expected=mp.mpf('0.1068199270586508730609439')
    assert_close('original two-loop Oily primitive 45-degree defect',lost,expected,'1e-24')
    totient_dual=sum((1+(n%2==0))*int(sp_totient(n))*mp.power(4,-n)/4 for n in range(1,100))
    assert_close('independent positive totient heat coefficients equal odd-Mobius source',totient_dual,lost,'1e-25')
    # Gamma Mellin, after actually rotating integration ray by +45 degrees.
    theta=mp.pi/4
    cut=5
    s=mp.mpf('3.2')
    rotated=mp.exp(1j*theta*s)*mp.quad(lambda x:x**(s-1)*L(mp.exp(1j*theta)*x,cut),[0,mp.mpf('.1'),1,10,mp.inf])
    finite_closed=mp.gamma(s)*mp.zeta(s-1)*sum(int(sp_mobius(d))*mp.power(d,-s) for d in range(1,cut+1,2))/4
    assert_close('45-degree gamma-mellin contour transfer',rotated,finite_closed,'1e-25')
    # Pole residue and renormalized derivative (Euler gamma cancels at s=2).
    eps=mp.mpf('1e-12')
    residue=2/mp.pi**2
    assert_close('Mellin pole leading coefficient', (eps*M(2+eps)), residue, '1e-11')
    expected_derivative=1-mp.log(2)/3-mp.diff(mp.zeta,2)/mp.zeta(2)
    diff=(mp.log((eps*M(2+eps))/residue))/eps
    assert_close('Gamma plus zeta Euler cancellation jet',diff,expected_derivative,'1e-10')
    # Gamma(2) one-tile original Oily golden member
    lam=(mp.sqrt(5)-1)/2
    assert_close('rank-2 oily macaroni',mp.digamma(2)-lam**2,lam-mp.euler,'1e-35')
    # The full primitive square-lattice Eisenstein has a known Gaussian-integer factorization.
    beta2=mp.dirichlet(2,[0,1,0,-1])
    expected_E_i=2*mp.zeta(2)*beta2/mp.zeta(4)
    assert_close('Eisenstein square-lattice value at i',E(0,1,20),expected_E_i,'1e-33')
    # Honest modular invariance: z -> -1/z and golden A=(1,1;1,2).
    z=mp.mpc('.18','.8'); za=-1/z; zb=(z+1)/(z+2)
    assert_close('Eisenstein S modular invariance',E(mp.re(z),mp.im(z),22),E(mp.re(za),mp.im(za),22),'1e-28')
    assert_close('Eisenstein golden hyperbolic A modular invariance',E(mp.re(z),mp.im(z),22),E(mp.re(zb),mp.im(zb),80),'1e-24')
    # E(i,s) cusp Laurent coefficient contains Euler gamma, test at s=1+eps.
    eps=mp.mpf('1e-9')
    beta1=mp.pi/4
    residue1=3/mp.pi
    beta_prime=mp.diff(lambda q: mp.dirichlet(q,[0,1,0,-1]),1)
    const=(3/mp.pi)*(mp.euler+beta_prime/beta1-2*mp.diff(mp.zeta,2)/mp.zeta(2))
    eps_E=2*mp.zeta(1+eps)*mp.dirichlet(1+eps,[0,1,0,-1])/mp.zeta(2+2*eps)
    assert_close('Eisenstein finite Laurent contains gamma',eps_E-residue1/eps,const,'1e-8')
    # Single scalar observation is non-identifying: an explicit two-atom mixture
    # reproduces the Haar scalar while failing uniformity, yet translations separate it.
    mean=const_term(mp.mpf(1))
    high=E(mp.mpf(0),mp.mpf(1))
    low=E(mp.mpf('.5'),mp.mpf(1))
    if not (low<mean<high):
        raise AssertionError('two-atom scalar alias control failed')
    w=(mean-low)/(high-low)
    assert_close('unshifted E scalar two-atom alias',w*high+(1-w)*low,mean,'1e-35')
    print('COUNTEREXAMPLE_ONLY two-atom unshifted observer weights',mp.nstr(w,15),mp.nstr(1-w,15))
    # Exact positivity for every h is analytic; finite modes are numerical positive controls.
    for h in range(1,60):
        if not coeff(h,mp.mpf('0.7'))>0:raise AssertionError('positive coefficient false')
    print('PASS 59 nonzero primitive-Eisenstein Fourier coefficients (numeric control)')
    # Source-selected original rational phase in translated Eisenstein MMD energy.
    def source(n):
        return Fraction(4,8*n-7)-Fraction(2,8*n-4)-Fraction(1,8*n-3)-Fraction(1,8*n-2)
    y=mp.mpf(1)
    coeffs=[coeff(h,y) for h in range(1,8)]
    def energy(phases):
        N=len(phases)
        return 2*sum(c**2*abs(sum(mp.exp(2j*mp.pi*h*x) for x in phases)/N)**2 for h,c in enumerate(coeffs,1))
    for N in [16,64,160]:
        u=Fraction(0,1);xs=[]
        for n in range(1,N+1):
            u=16*u+source(n)
            frac=u.numerator%u.denominator
            xs.append(mp.mpf(frac)/u.denominator)
        # numerical finite zero-seed diagnostic, not evidence for normality
        en=energy(xs)
        coherent=energy([mp.mpf(0)]*N)
        print('OBSERVED_ONLY finite actual BBP/Eisenstein energy N',N,'E_N',mp.nstr(en,20),'coherent reference',mp.nstr(coherent,20))
        if not(0<=en<=coherent+mp.mpf('1e-20')):
            raise AssertionError('spectral energy outside trivial nonnegative/tail bound')
    # A known Weyl-equidistributed orbit provides a positive control (not π).
    for N in [64,256,1024]:
        rot=mp.sqrt(2)
        kr=[mp.frac(n*rot) for n in range(1,N+1)]
        print('KNOWN_IRRATIONAL_ROTATION energy N',N,mp.nstr(energy(kr),20))
    alternating=[mp.mpf(k%2)/2 for k in range(128)]
    print('NEGATIVE_PERIODIC_CONTROL energy',mp.nstr(energy(alternating),20))
    if not energy(alternating)>0:raise AssertionError('periodic nonuniform control failed')
    print('INDEPENDENT_MPMATH_ORACLE_PASS (numerical checks do NOT certify global signed cancellation)')

if __name__=='__main__':run()
