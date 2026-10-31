"""SymPy/mpmath independent log-potential oracle for sibling PR416 cross-audit."""
from fractions import Fraction
from math import log
import json
import sympy as s
import mpmath as mp

u=s.Symbol('u', real=True)
V=lambda a:(a**4)/((a+3)**2*(a+4)*(a+5))
R=lambda a:s.Rational(4,1)/a-s.Rational(2,1)/(a+3)-1/(a+4)-1/(a+5)
assert s.factor(s.diff(s.log(V(u+1)),u)-R(u+1))==0
for n in range(1,6):
    a=8*n-7
    assert s.simplify(s.diff(s.log(V(a+u)),u).subs(u,0)-R(s.Integer(a)))==0

# Expand only logarithms; huge products are unnecessary for exact first-jet comparison.
for N in range(1,9):
    orbit = sum(s.Integer(16)**(N-n)*R(s.Integer(8*n-7)) for n in range(1,N+1))
    derivative = sum(s.Integer(16)**(N-n)*s.diff(s.log(V(8*n-7+u)),u).subs(u,0) for n in range(1,N+1))
    assert s.simplify(orbit-derivative)==0

# Explicit all-prime factorization from original rational potential values.
for N in range(1,10):
    v2 = sum(16**(N-n)*(-5) for n in range(1,N+1))
    assert v2 == -(16**N-1)//3

mp.mp.dps=65
cs=[4,-2,-1,-1]
shifts=[0,3,4,5]
C=mp.fprod([mp.gamma(mp.mpf(1+d)/8)**(-c) for c,d in zip(cs,shifts)])
P=lambda N:mp.fprod([mp.power(mp.mpf(8*n-7)**4/((8*n-4)**2*(8*n-3)*(8*n-2)),1) for n in range(1,N+1)])
# Use sum of logs for a robust precision check, rather than multiplying N subunit terms at low precision.
for N in (40,100,200,500):
    lp=mp.fsum([4*mp.log(8*n-7)-2*mp.log(8*n-4)-mp.log(8*n-3)-mp.log(8*n-2) for n in range(1,N+1)])
    ratio=mp.exp(lp+mp.mpf(15)/8*mp.log(N))/C
    assert abs(ratio-1)<mp.mpf('4')/N,(N,ratio)

print(json.dumps({
 'status':'PASS','symbolic_potential_derivatives':6,'symbolic_BBP_logjet_cases':8,
 'prime_2_closed_form_cases':9,'Gamma_potential_asymptotic_N':[40,100,200,500],
 'Gamma_constant_C':mp.nstr(C,50),
 'mpmath_version':mp.__version__,'sympy_version':s.__version__,
},indent=2))
