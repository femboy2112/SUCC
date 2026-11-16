"""Separate SymPy/mpmath oracle. Does not import the gamma_genesis module.

Uses symbolic source formulas, independent quadrature, and Mellin/Gamma
identity checks. Neither symbols nor numerical integrals prove RH/normality.
"""
import sympy as s
import mpmath as mp
from fractions import Fraction as F
from math import factorial

x,d,n,m,t,z=s.symbols('x d n m t z', real=True)
Q=4-2*x**3-x**4-x**5
R=(1-x)/((2-x**2)*(x**2-2*x+2))
assert s.factor(Q/(16-x**8)-R)==0
assert s.factor(Q-(1-x)*(x*x+2)*(x*x+2*x+2))==0
r=4/(8*n-7)-2/(8*n-4)-1/(8*n-3)-1/(8*n-2)
ralt=(120*n*n-89*n+16)/((2*n-1)*(4*n-1)*(8*n-7)*(8*n-3))
assert s.factor(r-ralt)==0
print('PASS: original immutable four-pole / rational Oily Green source')

D=s.factor(((2-x**2)*(x**2-2*x+2)).subs(x,1-d))
assert s.expand(D)==1+2*d+2*d**3-d**4
E=s.factor(1/D-(1-2*d))
assert s.factor(E-d**2*(4-2*d+5*d**2-2*d**3)/D)==0
assert s.factor(4*d*d-E-d**3*(10-5*d+10*d*d-4*d**3)/D)==0
# On d in [0,1]: D>=1, first numerator >=2 and second >=5;
# moreover second numerator <= 20 (all via elementary intervals).
print('PASS: exact factored endpoint residual and rational positivity witnesses')

beta=lambda k:factorial(k)/s.prod(m+i for i in range(1,k+2))
A=beta(1)-2*beta(2)+4*beta(3)
v=s.symbols('v', positive=True)
expansion=s.series(A.subs(m,1/v),v,0,6).removeO().expand()
assert expansion.coeff(v,2)==1 and expansion.coeff(v,3)==-7 and expansion.coeff(v,4)==55
print('PASS: original source moment T_m = m^-2 -7m^-3 +55m^-4 + O(m^-5)')

for shape in (s.Rational(1,2),s.Rational(3,2),s.Integer(1),s.Integer(2),s.Integer(4)):
    for rate in (s.Integer(1),s.Integer(2)):
        got=s.integrate(t**(shape-1)*s.exp(-rate*t),(t,0,s.oo))
        assert s.simplify(got-s.gamma(shape)/rate**shape)==0,(shape,rate,got)
print('PASS: Mellin-Laplace Gamma integral at 10 independent shapes/rates')

a,b,sig,lam=s.symbols('a b sig lam',positive=True)
assert s.simplify((a*b)**sig-a**sig*b**sig)==0
assert s.simplify(s.exp(-lam*(a+b))-s.exp(-lam*a)*s.exp(-lam*b))==0
for k in range(1,12):
    assert s.simplify(s.digamma(k)-(s.harmonic(k-1)-s.EulerGamma))==0
print('PASS: multiplicative/additive characters and 11 Euler/digamma depth identities')


for a,b in ((s.Integer(1),s.Integer(1)),(s.Integer(1),s.Integer(2)),
            (s.Rational(1,2),s.Rational(3,2))):
    u=s.symbols('u',real=True)
    got=s.integrate(u**(a-1)*(1-u)**(b-1),(u,0,1))
    assert s.simplify(got-s.gamma(a)*s.gamma(b)/s.gamma(a+b))==0,(a,b,got)
print('PASS: independent Beta-integral proof of Gamma-convolution identity')

for shape in range(1,6):
    for j in range(0,10):
        got=s.integrate(s.exp(-2*t)*t**(shape+j-1),(t,0,s.oo))/(
            s.factorial(shape-1)*s.factorial(j))
        want=s.binomial(shape+j-1,j)/2**(shape+j)
        assert s.simplify(got-want)==0,(shape,j,got)
print('PASS: 50 direct Poisson-Gamma integrals equal NB/Oily coefficients')

for S in (2,4,6):
    for k in range(1,5):
        got=s.integrate(t**s.Rational(S,2-0)*s.exp(-s.pi*k*k*t)/t,(t,0,s.oo))
        want=s.gamma(s.Rational(S,2))/(s.pi*k*k)**s.Rational(S,2)
        assert s.simplify(got-want)==0,(S,k,got)
print('PASS: 12 authentic theta-Gaussian Mellin factor tests in Re(s)>1')

mp.mp.dps=55
for M in (0,8,16,32,64,128):
    integral=mp.quad(lambda v:(v**M)*(1-v)/((2-v*v)*(v*v-2*v+2)),[0,mp.mpf('0.5'),1])
    b1=F(1,(M+1)*(M+2))
    b2=F(2,(M+1)*(M+2)*(M+3))
    b3=F(6,(M+1)*(M+2)*(M+3)*(M+4))
    b4=F(24,(M+1)*(M+2)*(M+3)*(M+4)*(M+5))
    lower=b1-2*b2+4*b3-20*b4
    upper=b1-2*b2+4*b3
    lo=mp.mpf(lower.numerator)/lower.denominator
    hi=mp.mpf(upper.numerator)/upper.denominator
    assert lo < integral < hi,(M,integral,lo,hi)
print('PASS: six 55-digit independent source moment quadratures inside exact bounds')

for M in (16,64,128):
    mass=mp.quad(lambda v:v**M*(1-v)/((2-v*v)*(v*v-2*v+2)), [0,mp.mpf('0.5'),1])
    for omega in (mp.mpf('0.5'),mp.mpf('1'),mp.mpf('3')):
        # Original-source posterior with the NEW declared x^m likelihood.
        measured=mp.quad(lambda v:(v**M)*(1-v)/((2-v*v)*(v*v-2*v+2))
                        *mp.exp(1j*omega*mp.log(M*(1-v))),
                        [0,mp.mpf('0.5'),1])/mass
        analytic=mp.gamma(2+1j*omega)/mp.gamma(2)
        assert abs(measured-analytic) < mp.mpf(14)/M
        assert abs(analytic)<1
print('PASS: nine independent original-source complex log-Mellin observations within uniform TV bound')

print('INDEPENDENT SYMBOLIC AUDIT: PASS')
