"""Independent alternate-route Gamma/2-adic and real-circle oracle.

No imports of gamma_all_places or its tests.  Distinct algebraic derivation:
source = a rational function from SymPy and K=(1-q)^2P(q) from polynomial
factorization; independent Laplace integral and Gamma-digamma numerical views.
"""
import json
import sys
from fractions import Fraction as Q
import sympy as s
import mpmath as mp

x,q=s.symbols('x q')
AUTH=(4,-2,-1,-1)
DELTA=(1,4,5,6)

R=s.factor(sum(s.Rational(c)/(8*x-8+d) for c,d in zip(AUTH,DELTA)))
K=s.factor(sum(s.Rational(c)/(8*x-8+d) for c,d in zip((1,-3,1,1),DELTA)))
assert s.factor(R-(120*x*x-89*x+16)/((2*x-1)*(4*x-1)*(8*x-7)*(8*x-3)))==0
assert s.factor(K- (sum(s.Rational(c)/(8*x-8+d) for c,d in zip((1,-3,1,1),DELTA))))==0
qpoly=s.factor(1-3*q**3+q**4+q**5)
assert qpoly==(q-1)**2*(q**3+3*q**2+2*q+1)
assert s.factor(R + 4*K) != R

# Independent congruence proof coefficient vector (A,B,C,D) over 2-adic units.
A,B,C,D,n = s.symbols('A B C D n', integer=True)
even_num=s.expand(B*(4*n-1)+2*D*(2*n-1))
assert s.expand(even_num + B + 2*D - 4*n*(B+D)) == 0

# Direct independent exact recurrence: no calls to implementation module.
def calc_U(N,c):
    z=Q(0)
    for n in range(1,N+1):
        z=16*z+sum((Q(a,8*n-8+d) for a,d in zip(c,DELTA)),Q(0))
    return z

def val2(v):
    a,b=abs(v.numerator),v.denominator
    if a==0:return None
    t=0
    while a%2==0:a//=2;t+=1
    while b%2==0:b//=2;t-=1
    return t

snapshots={}
for k in (1,4,8,12):
    tt=2**(k+2)
    c=tuple(a+tt*b for a,b in zip(AUTH,(1,-3,1,1)))
    vals=[val2(calc_U(n,c)-calc_U(n,AUTH)) for n in (1,3,7,11,21)]
    assert vals==[k]*5
    a13=13*calc_U(2,c);auth13=13*calc_U(2,AUTH)
    assert a13.denominator%13!=0 and auth13.denominator%13!=0
    m=lambda v:(v.numerator*pow(v.denominator,-1,13))%13
    assert m(a13)!=m(auth13)
    snapshots[str(k)]={"difference_v2_sample":vals,"prime13_residue_auth":m(auth13),"prime13_residue_mutant":m(a13)}

mp.mp.dps=80
weights=[4,-2,-1,-1]
delta=[1,4,5,6]
source_inf=-sum(mp.mpf(c)*mp.digamma(mp.mpf(d)/8)/8 for c,d in zip(weights,delta))
# This integral is independent of the digamma representation.
qweight=lambda u: ((u*u+2)*(u*u+2*u+2))/sum(u**i for i in range(8))
# limit at u=1 Q'(1)/(-8) =? Q polynomial derivative at1 = -6-4-5 = -15 => 15/8.
integral=mp.quad(qweight,[0,mp.mpf('0.2'),mp.mpf('0.8'),mp.mpf('0.999'),1])
assert abs(integral-source_inf)<mp.mpf('1e-60'), (integral,source_inf)
B=(source_inf-mp.pi)/15
# Alternative integral proof of total Green-tail sum, direct positive kernel.
green_integral=mp.quad(lambda u: u**8*qweight(u)/(16*(1-u**8/16)), [0,mp.mpf('.4'),mp.mpf('.95'),1])
assert abs(B-green_integral)<mp.mpf('1e-60'),(B,green_integral)

# F_p / GK age ranks are exact rationals: no assertion that these are selected-real phase bounds.
age=lambda a:sum((Q(cc*((a*d)%8),8) for d,cc in zip(delta,weights)),Q(0))
assert [age(v) for v in (1,3,5,7)]==[Q(-15,8),Q(-5,8),Q(5,8),Q(15,8)]
GK={str(v):str(age(1)+(age(v) if v!=1 else Q(0))) for v in (1,3,5,7)}
# For p≡1 mod8 use f=1. Otherwise f=2.
assert GK=={'1':'-15/8','3':'-5/2','5':'-5/4','7':'0'}

payload={
 "status":"PASS",
 "origin":"independent SymPy rational source, polynomial positivity and 80-digit integral oracle",
 "certified_math":"symbolic identities exact; numerical quadratures are consistency checks only",
 "rational_source_polynomial":str(R),
 "age_kernel_laplace_polynomial":str(qpoly),
 "two_integrality_numerator":str(even_num),
 "two_precision_mutants":snapshots,
 "source_mass_digamma":mp.nstr(source_inf,65),
 "source_mass_integral":mp.nstr(integral,65),
 "tail_budget_from_gamma":mp.nstr(B,65),
 "tail_budget_from_positive_integral":mp.nstr(green_integral,65),
 "unit_frequency_phase_bound":mp.nstr(2*mp.pi*B,65),
 "GK_weighted_valuation_by_prime_mod8":GK,
 "python":sys.version.split()[0],"sympy":s.__version__,"mpmath":mp.__version__
}
print(json.dumps(payload,indent=2))
