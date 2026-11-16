"""Independent symbolic source and probability calculations (no weaving_probe imports)."""
from fractions import Fraction
import sympy as sp

x=sp.symbols('x',real=True)
a,b,c=(1-x),(2+x*x),(2+2*x+x*x)
q=4-2*x**3-x**4-x**5
assert sp.expand(a*b*c-q)==0
E=lambda f:sp.integrate(f,(x,0,1))
a0,b0,c0=E(a),E(b),E(c)
ab,ac,bc,abc=E(a*b),E(a*c),E(b*c),E(a*b*c)
assert (a0,b0,c0)==(sp.Rational(1,2),sp.Rational(7,3),sp.Rational(10,3))
assert (ab,ac,bc)==(sp.Rational(13,12),sp.Rational(17,12),sp.Rational(241,30))
assert abc==sp.Rational(47,15)
assert abc-a0*b0*c0==-sp.Rational(34,45)
third=sp.factor(abc-ab*c0-ac*b0-bc*a0+2*a0*b0*c0)
assert third==-sp.Rational(1,45)
print('Source factorization Q=(1-t)(2+t^2)(2+2t+t^2): exact')
print('Weighted source r(1):',abc)
print('Three-variable cumulant:',third)
K0=1/(16-x**8)
K1=(16+x**8)/(256+x**16)
Kd=2*x**16/((16-x**8)*(256+x**16))
assert sp.factor(K0-K1-Kd)==0
assert sp.expand(sp.factor(q)-(1-x)*(2+x*x)*(2+2*x+x*x))==0
for n in range(1,30):
    moment=4*sp.Rational(1,8*n-7)-2*sp.Rational(1,8*n-4)-sp.Rational(1,8*n-3)-sp.Rational(1,8*n-2)
    assert sp.integrate(x**(8*n-8)*q,(x,0,1))==moment
print('Original four-pole source moments: 29 exact checks')
print('Difference of π/16 and χ kernels: exact positive rational form')
# An independent measure-theoretic Jacobian: for each ordering branch
# (u1,u2)=(m,mv) or (mv,m), its square Lebesgue density is m dm dv.
# r=m^2 => dr=2m dm => each branch has density (1/2) dr dv;
# the pair of branches makes dr dv, independent of bit.
m,v,r=sp.symbols('m v r',positive=True)
J=sp.det(sp.Matrix([[sp.diff(m,m),sp.diff(m,v)],[sp.diff(m*v,m),sp.diff(m*v,v)]]))
assert J==m
assert sp.simplify(J/(2*m))==sp.Rational(1,2)
print('2D square-to-disk transfer Jacobian: branch density (1/2) dr dv')
# Independent positive-moment finite difference and endpoint coefficient audit.
from math import factorial,comb
assert sp.diff(q,x).subs(x,1)==-15
for n in range(5):
    for k in range(5):
        source_poly=sp.integrate(x**(16*n)*(1-x**16)**(2*k)*q,(x,0,1))
        signed=sum((-1)**j*comb(2*k,j)*(4*sp.Rational(1,16*n+16*j+1)-2*sp.Rational(1,16*n+16*j+4)-sp.Rational(1,16*n+16*j+5)-sp.Rational(1,16*n+16*j+6)) for j in range(2*k+1))
        assert sp.simplify(source_poly-signed)==0
        assert source_poly>0
for k in range(5):
    coefficient=sp.Rational(15*factorial(2*k+1),256)
    assert coefficient>0
print('Source signed finite-difference Gamma hierarchy: 25 exact moments, 5 positive coefficients')
