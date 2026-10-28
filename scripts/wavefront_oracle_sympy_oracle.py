#!/usr/bin/env python3
"""Independent SymPy derivation of WEO characteristic and source identities."""
import sympy as s

x,z = s.symbols('x z', real=True)
u = x-x*x/s.Integer(2)
v = x*x/s.Integer(2)
D=s.expand((1-u*z)*(1-v*z))
assert s.simplify((u+v)-x)==0
assert s.simplify(u*v-x**3*(2-x)/4)==0
assert s.factor((u+v)**2-4*u*v)==x**2*(x-1)**2
assert s.factor(D.subs(x,1))==(z-2)**2/4
R=(1-x)/(4*(1-u)*(1-v))
assert s.simplify(R-(1-x)/((2-x*x)*(x*x-2*x+2)))==0
G=(1-u)*(1-v)/D
assert s.simplify(G.subs(z,1)-1)==0
assert s.simplify(G.subs(x,1)-(2-z)**(-2))==0
for j in range(16):
    q=s.expand((1-u)*(1-v)*sum(u**k*v**(j-k) for k in range(j+1)))
    assert s.simplify(q.subs(x,1)-s.Rational(j+1,2**(j+2)))==0
    if j>=2:
        prev=s.expand((1-u)*(1-v)*sum(u**k*v**(j-1-k) for k in range(j)))
        prev2=s.expand((1-u)*(1-v)*sum(u**k*v**(j-2-k) for k in range(j-1)))
        assert s.simplify(q-x*prev+u*v*prev2)==0

# Independent formal z transform: H2/W = z^2 (1-u)(1-v)/D.
# Evaluate coefficient j of the continuous Oily packet via finite power series.
series=s.series(G,z,0,10).removeO().expand()
for j in range(10):
    exact=(1-u)*(1-v)*sum(u**k*v**(j-k) for k in range(j+1))
    assert s.simplify(series.coeff(z,j)-exact)==0

# Demonstrate a deformation in *success probability* epsilon, distinct from source x=1.
e,svar=s.symbols('eps s',positive=True)
G_eps=(e/(1-(1-e)*s.exp(-e*svar)))**2
assert s.limit(G_eps,e,0,dir='+')==(1+svar)**(-2)
print('WEO_INDEPENDENT_SYMPY_PASS: recurrence/discriminant/double pole/16 packets/10 z-series/Gamma-limit control')
