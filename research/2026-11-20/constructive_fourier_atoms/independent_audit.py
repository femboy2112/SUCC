"""Independent SymPy/mpmath reconstruction, no import of causal_fourier.py.

This reproduces exact BBP source identities, exact finite clock arithmetic,
nonlinear source-mellin Fourier transform and source-specific coefficients.
No universal π shell estimate or hosted CI is claimed.
"""
from fractions import Fraction
from math import isqrt
import json
import sympy as S
import mpmath as mp

n,t,z=S.symbols('n t z')
Q=4-2*t**3-t**4-t**5
H=4+4*t+4*t**2+2*t**3+t**4
assert S.expand((1-t)*H-Q)==0
r=4/(8*n-7)-2/(8*n-4)-1/(8*n-3)-1/(8*n-2)
r_bbp=(120*n*n-89*n+16)/((2*n-1)*(4*n-1)*(8*n-7)*(8*n-3))
assert S.factor(r-r_bbp)==0
r2=lambda j:S.together(r.subs(n,j))
c1=S.Rational(1,16)*r2(1);c2=S.Rational(1,256)*r2(2)
assert c1==S.Rational(47,240)
assert c2==S.Rational(53,104832)
assert 2*c1*c2==S.Rational(2491,12579840)

# Integer clock isometry and complement-adic phase resolution without
# importing the production module or its unit tests.
clock=lambda k:(16**k-1)//15
count=0
for p in (3,5):
    for k in range(1,6 if p==3 else 5):
        m=p**k
        states=[clock(j)%m for j in range(m)]
        assert len(set(states))==m
        assert states[0]==clock(m)%m==0
        count+=m
for p in (3,5):
    for a in range(0,65):
        for b in range(a+1,65):
            d=abs(clock(a)-clock(b));e=b-a
            v0=v1=0
            while d%p==0:d//=p;v0+=1
            while e%p==0:e//=p;v1+=1
            assert v0==v1
            count+=1

# Exact first-prime-square signatures of original and matched source mutant.
prime_checks=0
for p in list(S.primerange(7,700)):
    j=(p*p+7)//8
    rr=r2(j)
    a=p*p*rr
    mutant=S.cancel(rr+S.Rational(2,(8*j-7)*(8*j-6)*(8*j-5)))
    am=p*p*mutant
    assert S.denom(a)%p and S.denom(am)%p
    assert (S.numer(a)*pow(int(S.denom(a)), -1, int(p)))%p==4
    assert (S.numer(am)*pow(int(S.denom(am)),-1,int(p)))%p==5
    prime_checks+=2

mp.mp.dps=75
ferr=[]
for omega in (mp.mpf('0'), mp.mpf('0.31'),mp.mpf('1.12'),mp.pi/3):
    w=mp.e**(1j*omega)
    integrand=lambda v: (4-2*v**3-v**4-v**5)*w/(16-w*v**8)
    integ=mp.quad(integrand,[0,1])
    summ=mp.mpc(0)
    for j in range(1,68):
        rv=4/mp.mpf(8*j-7)-2/mp.mpf(8*j-4)-1/mp.mpf(8*j-3)-1/mp.mpf(8*j-2)
        summ+=rv/16**j*w**j
    err=abs(integ-summ)
    ferr.append(mp.nstr(err,8))
    assert err<mp.mpf('1e-70'), (omega,err)
    if omega==0:
        assert abs(integ-mp.pi/16)<mp.mpf('1e-70')

receipt={
 'suite':'independent_sympy_mpmath',
 'status':'PASS',
 'sympy_version':S.__version__, 'mpmath_version':mp.__version__,
 'finite_clock_and_valuation_assertions':count,
 'exact_prime_square_mutant_residue_assertions':prime_checks,
 'exact_source_gap_coefficient':'2491/12579840',
 'four_mellin_fourier_integral_vs_67_term_errors':ferr,
 'scope':'finite algebra and numerical integral; no asymptotic π Weyl proof',
}
print(json.dumps(receipt,indent=2))
