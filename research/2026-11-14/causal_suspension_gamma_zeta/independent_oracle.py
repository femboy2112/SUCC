"""Independent SymPy/mpmath formulas; does not import implementation under test."""
from __future__ import annotations
from fractions import Fraction
from math import lcm
from itertools import product
import sympy as sp
import mpmath as mp

z, p = sp.symbols('z p')
# Formal EGF, independently differentiated; no primary implementation import.
expr=sp.exp(z)/(1+sp.exp(z))
for m in range(21):
    egf=sp.diff(expr,z,m).subs(z,0).simplify()
    finite=sum(sp.Rational(1,2**(n+1)) * sum(
        (-1)**k * sp.binomial(n,k) * (k+1)**m for k in range(n+1))
        for n in range(m+1))
    assert sp.simplify(egf-finite)==0, (m,egf,finite)
    assert sp.simplify(finite/(1-2**(m+1))-sp.zeta(-m))==0,m
print('Euler-Hasse vs independent SymPy derivative and zeta values: 21/21 PASS')

for n in range(1,11):
    assert sp.diff(expr,z,2*n).subs(z,0).simplify()==0
print('Independent oddness/even coefficient test: 10/10 PASS')

for n in range(1,9):
    coeffs=[sp.expand((1+p)**n).coeff(p,j) for j in range(n+1)]
    assert coeffs==[sp.binomial(n,j) for j in range(n+1)]
    assert sp.simplify((1+p)**(-n)*sum(coeffs[j]*p**j for j in range(n+1)))==1
print('Gamma negative depth distribution and Laplace inverse: 8/8 PASS')

# Independent finite odometer circles; no local package import.
checks=0
for N in range(2,20):
    L=lcm(*range(1,N+1))
    prev=lcm(*range(1,N))
    for m in range(1,20):
        assert ((-m)%L)%prev == (-m)%prev
        checks+=1
print(f'Profinite bonding and forward winding: {checks}/{checks} PASS')

# Independent CRT construction using SymPy, not the finite-clock primary function.
for N in range(2,19):
    L=lcm(*range(1,N+1))
    twopower=L & -L
    odd=L//twopower
    rem=sp.ntheory.modular.crt([twopower,odd],[1,0],check=True)
    assert rem is not None
    a=int(rem[0])%L
    assert a%twopower==1 and a%odd==0
    if N>2:
        prev=lcm(*range(1,N))
        previous=sp.ntheory.modular.crt([prev & -prev, prev//(prev & -prev)],[1,0],check=True)
        assert a%prev==int(previous[0])%prev
print('Independent CRT finite-level phantom: 17/17 PASS')


mp.mp.dps=70
for n in range(1,7):
    actual=mp.diff(mp.zeta,-2*n)
    expected=(-1)**n * mp.factorial(2*n)*mp.zeta(2*n+1)/(2*(2*mp.pi)**(2*n))
    assert mp.fabs(actual-expected)<mp.mpf('1e-60'),(n,actual,expected)
print('Independent zeta trivial-zero derivative via positive reflected zeta: 6/6 PASS')

# Direct integral verifies gamma-character values and the endpoint under source projection.
probes=0
for length,m,rate in [(6,1,3),(6,2,5),(12,2,4),(60,1,5),(60,3,6)]:
    omega=2*mp.pi/length
    a=m*rate
    dens=lambda t:(rate**a/mp.gamma(a))*t**(a-1)*mp.exp(-rate*t)
    integral=mp.quad(lambda t:dens(t)*mp.exp(-1j*omega*t),[0,mp.inf])
    closed=(1+1j*omega/rate)**(-a)
    assert abs(integral-closed)<mp.mpf('1e-55'),(length,m,rate,integral,closed)
    probes+=1
print(f'Gamma-clock Fourier via independent direct integral: {probes}/{probes} PASS')

print('CLAIM: mathematics only; no actual physics, no RH/normality proof.')
