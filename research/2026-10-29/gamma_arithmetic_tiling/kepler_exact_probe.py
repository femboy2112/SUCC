"""Exact standalone SUCC Operation Kepler probe; run with SymPy installed.
Checks algebraic identities only. Universal claims follow from the documented
positive polynomial formulas, not from finite sampling; pi normality OPEN.
"""
from fractions import Fraction as F
from math import gcd
import sympy as s

a=s.symbols('a',positive=True,real=True)
R=lambda z:4/z-2/(z+3)-1/(z+4)-1/(z+5)
P=s.cancel(R(a*(1-s.I))/R(a))
D=(a*a+4*a+8)*(2*a*a+6*a+9)*(2*a*a+10*a+25)*(15*a*a+121*a+240)
P4=118*a**4+930*a**3+3707*a**2+7260*a+7200
P5=60*a**5+602*a**4+2904*a**3+7667*a**2+11280*a+7200
P9=(3540*a**9+91318*a**8+1059000*a**7+7300703*a**6+33156378*a**5+
    103207249*a**4+220620060*a**3+312831000*a**2+266976000*a+103680000)
RE=s.factor(s.re(s.expand_complex(P)))
IM=s.factor(s.im(s.expand_complex(P)))
RAD=s.factor(s.expand_complex(P*s.conjugate(P))-s.Rational(1,4))
assert s.cancel(RE-(a+3)*(a+4)*(a+5)*P4/(2*D))==0
assert s.cancel(IM-(a+3)*(a+4)*(a+5)*P5/(2*D))==0
assert s.cancel(RAD-P9/(4*D*(15*a*a+121*a+240)))==0
for poly in (P4,P5,P9):
    assert all(c>0 for c in s.Poly(poly,a).all_coeffs())
assert s.simplify(s.limit(P,a,s.oo)-s.I/2)==0
assert s.simplify(s.limit(a*(P-s.I/2),a,s.oo)-s.Rational(59,60)*(1+s.I))==0
assert s.simplify((1-s.I)**(-1)-(1+s.I)/2)==0
assert s.simplify((1-s.I)**(-2)-s.I/2)==0

B=s.Matrix([[1,1],[1,2]]); v=s.Matrix([1,0])
def T(i,j):return (B**i*v).dot(B**j*v)
for i in range(-7,8):
    for j in range(-7,8):
        assert T(i,j)*T(i+1,j+1)-T(i,j+1)*T(i+1,j)==1
assert gcd(0,6)!=1 and gcd(2,6)!=1
assert gcd(1,6)==1 and gcd(3,6)!=1
assert s.sqrt(2).is_integer is False

r=lambda k:F(4,8*k-7)-F(2,8*k-4)-F(1,8*k-3)-F(1,8*k-2)
for n in (1,2,3,8,25):
    lower=sum((r(n+j)/16**j for j in range(1,22)),F())
    upper=lower+r(n+22)/(15*16**21)
    assert 0<lower<upper<=F(1,(8*n+1)**2)
print('KEPLER_EXACT_PASS; 3 positive polynomial identities; 225 SL2 cells; BBP tail bounds')
