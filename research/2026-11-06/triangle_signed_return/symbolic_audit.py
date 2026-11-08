"""Optional independent SymPy oracle of original-pole and digamma mass identities."""
import sympy as sp
n=sp.symbols('n'); rt=sp.Rational
r=(120*n*n-89*n+16)/((2*n-1)*(4*n-1)*(8*n-7)*(8*n-3))
four=4/(8*n-7)-2/(8*n-4)-1/(8*n-3)-1/(8*n-2)
assert sp.factor(r-four)==0
psi=sp.digamma
D=(-4*psi(rt(1,8))+2*psi(rt(1,2))+psi(rt(5,8))+psi(rt(3,4)))/8
s=sp.sqrt(2)
unsimplified=(4+5*s)*sp.pi/16+rt(5,8)*sp.log(2)+5*s/16*(sp.log(2+s)-sp.log(2-s))
assert sp.simplify(sp.expand_func(D)-unsimplified)==0
assert sp.simplify((2+s)/(2-s)-(1+s)**2)==0
# Thus the log ratio equals 2log(1+sqrt2) over R with positive arguments.
print('PASS exact pole partial fractions')
print('PASS exact Gauss/digamma reduction to real silver-ratio source mass')
print('PASS algebraic positive-log ratio simplification')
print('MASS=',sp.N(D,40))
