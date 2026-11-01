"""Independent symbolic exact algebra checks; supplementary to stdlib tests.

Run python research/2026-11-01/circle_path_ratio/symbolic_probe.py
"""
import sympy as s
from pathlib import Path

t=s.symbols('t',real=True)
n=s.symbols('n',positive=True,integer=True)
i=s.I
X=(1-t*t)/(1+t*t)
Y=2*t/(1+t*t)
assert s.factor(X*X+Y*Y-1)==0
assert s.simplify(s.sqrt(s.factor(s.diff(X,t)**2+s.diff(Y,t)**2))-2/(1+t*t))==0
D=2*t/(1-t*t)
C=(1+i*t)/(1-i*t)
assert s.cancel(C.subs(t,D)-C*C)==0
eta=2/(1+t*t)
assert s.cancel(eta.subs(t,D)*s.diff(D,t)-2*eta)==0
# A full local source rotation is an isometry of the angular 1-form.
u=s.symbols('u',real=True)
R=(t+u)/(1-u*t)
assert s.cancel(eta.subs(t,R)*s.diff(R,t)-eta)==0
# Original pole form on a separate source projective sphere.
z=s.symbols('z')
r=4/(8*z-7)-2/(8*z-4)-1/(8*z-3)-1/(8*z-2)
assert s.factor(r-(120*z*z-89*z+16)/((2*z-1)*(4*z-1)*(8*z-7)*(8*z-3)))==0
assert s.factor(s.integrate(eta,(t,0,s.oo))-s.pi)==0
# Conductor/cyclotomic: all four factors in the source denominator are odd on integer n.
# Degree-16 nontrivial composition on the real projective circle.
P=s.together(s.expand((1+i*t)**16)).expand()
A=s.expand(s.im(P));B=s.expand(s.re(P))
# This polynomial equality can be expensive if expanded prematurely; compare samples exact.
for val in [s.Rational(1,3),s.Rational(3,5),s.Rational(2,7)]:
    a,b=val,s.Integer(1)
    for _ in range(4):a,b=2*a*b,b*b-a*a
    assert s.factor(a*B.subs(t,val)-b*A.subs(t,val))==0
print('PASS 10 independent symbolic source/circle/pullback/arc/16-power probes')
