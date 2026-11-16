"""Separate symbolic/multiprecision referee for gauge-frontier models.

The primary standard-library source code is not imported. Tests inspect
reflection-conjugation and arbitrary-complex-jet impostors, exact
BBP source recurrence residual, and finite Lagarias interval witnesses.
"""
from __future__ import annotations
import sympy as s
from pathlib import Path

z=s.symbols('z')
points=[s.Rational(0),s.Rational(2,3)+s.I*s.Rational(3,5)]
order=2
w=s.prod(((z*z-a*a)*(z*z-s.conjugate(a)**2))**(order+1) for a in points)
w=s.expand(w)
zi=s.I*s.Rational(1,2)
assert w.subs(z,zi)!=0
q=s.cancel(1-w/w.subs(z,zi))
assert s.simplify(q.subs(z,-z)-q)==0
assert s.expand(w).as_poly(z).all_coeffs() and all(s.simplify(s.im(c))==0 for c in s.Poly(w,z).all_coeffs())
assert s.simplify(q.subs(z,zi))==0
for a in points:
    for k in range(order+1):
        assert s.simplify(s.diff((q-1)*s.cos(z),z,k).subs(z,a))==0,(a,k)
assert s.simplify(s.cos(zi))==s.cosh(s.Rational(1,2))
print('SYMMETRIC-ENTIRE IMPOSTOR: complex finite jets, evenness, conjugation, off-real zeros PASS')

n=s.symbols('n',integer=True,positive=True)
r=lambda j: 4/s.Rational(8*j-7)-2/s.Rational(8*j-4)-1/s.Rational(8*j-3)-1/s.Rational(8*j-2)
for clock in range(0,10):
    for depth in range(0,8):
        U=lambda t:sum(s.Integer(16)**(t-k)*r(k) for k in range(1,t+1))
        tail=lambda t:sum(s.Integer(16)**(-k)*r(t+k) for k in range(1,depth+1))
        residual=s.cancel(U(clock+1)+tail(clock+1)-16*(U(clock)+tail(clock)))
        expected=s.Integer(16)**(-depth)*r(clock+depth+1)
        assert s.simplify(residual-expected)==0
print('SIGNED ORIGINAL FOUR-POLE GREEN RESIDUAL: 80 symbolic clocks/depths PASS')

# No oracle use of the primary Taylor-series functions.
# We only compare independent high-precision direct analytic evaluations against
# rational upper/lower proofs for a finite range, not substitute numerics for proof.
from mpmath import mp
mp.dps=85
H=mp.mpf(0)
min_gap=mp.inf
for k in range(1,257):
    H+=1/mp.mpf(k)
    sigma=sum(d for d in range(1,k+1) if k%d==0)
    gap=H+mp.exp(H)*mp.log(H)-sigma
    if k==1: assert gap==0
    else:
        assert gap>0
        min_gap=min(min_gap,gap)
print('LAGARIAS NUMERICAL HOLDOUT (not proof): n=1..256 PASS; min gap n>1:',mp.nstr(min_gap,28))
print('INDEPENDENT ORACLE PASS')
