"""Independent SymPy oracle: no import of primary gamma_carry_probe module."""
from fractions import Fraction
from math import log, pi
import sympy as sp

x=sp.symbols('x', real=True)
Q=4-2*x**3-x**4-x**5
assert sp.expand(Q-(1-x)*(x*x+2)*(x*x+2*x+2))==0

n=sp.symbols('n', integer=True, positive=True)
a=8*n-7
r=4/a-2/(a+3)-1/(a+4)-1/(a+5)
R=(120*n*n-89*n+16)/((2*n-1)*(4*n-1)*(8*n-7)*(8*n-3))
assert sp.factor(r-R)==0

S=sp.zeros(4,4)
for c in range(4):S[c,(c+1)%4]=1
I=sp.eye(4)
sigma=sp.Matrix([1,-1,-1,1])
assert S**4==I
G1=(2*I-S).inv()
G2=G1*G1
assert G1*sigma==sp.Matrix([sp.Rational(1,5),-sp.Rational(3,5),-sp.Rational(1,5),sp.Rational(3,5)])
assert G2*sigma==sp.Matrix([-sp.Rational(1,25),-sp.Rational(7,25),sp.Rational(1,25),sp.Rational(7,25)])
G3=4*((3*I-S).inv())**2
assert G3*G2==G2*G3
z2=(2-sp.I)**(-2)
z3=4*(3-sp.I)**(-2)
assert sp.simplify(z2-sp.Rational(3,25)-sp.Rational(4,25)*sp.I)==0
assert sp.simplify(z3-sp.Rational(8,25)-sp.Rational(6,25)*sp.I)==0
assert sp.simplify(z2*z3-sp.Rational(2,25)*sp.I)==0
assert sp.simplify((1+sp.I)*z2-(-1+7*sp.I)/25)==0

# Whole group: the mod4 sign is NOT itself a character.
for c in range(4):
    for d in range(4):
        assert sigma[(c+d)%4] == sigma[c]*sigma[d]*(-1)**((c%2)*(d%2))

th=sp.symbols('theta',real=True)
q=5-4*sp.cos(th)
assert sp.limit((q-1)/th**2,th,0)==2
assert sp.limit(sp.log(q)/th**2,th,0)==2

# Original source bound and strict monotonicity checked over a finite rational audit range.
for k in range(1,501):
    raw=Fraction(4,8*k-7)-Fraction(2,8*k-4)-Fraction(1,8*k-3)-Fraction(1,8*k-2)
    if k>=2:
        assert 0<raw<Fraction(15,(8*(k-1)+1)*(8*(k-1)+2))
        old=Fraction(4,8*(k-1)-7)-Fraction(2,8*(k-1)-4)-Fraction(1,8*(k-1)-3)-Fraction(1,8*(k-1)-2)
        assert raw<old

print('INDEPENDENT AUDIT: 4x4 exact Gamma matrices, C4 cocycle, 3-4-5 quarter turn, source rational form, Fourier low-mode Taylor and 500 rational source cases: PASS')
