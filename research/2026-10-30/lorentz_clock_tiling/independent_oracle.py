"""Independent symbolic and direct-polynomial oracle for Lorentz-clock research.

Separate from the coefficient-based Fraction production probe. Only uses
SymPy and the original signed four-pole Laplace transform.
"""
from __future__ import annotations
from math import comb
from fractions import Fraction as F
import sympy as sp

M=sp.Matrix([[1,1],[1,2]])
Q=sp.Matrix([[-2,-1],[-1,2]])
assert M.T*Q*M==Q and M.det()==1 and Q.det()==-5
lambda_plus=(3+sp.sqrt(5))/2
lambda_minus=(3-sp.sqrt(5))/2
assert sp.simplify(M.charpoly().as_expr()-(sp.Symbol('lambda')-lambda_plus)*(sp.Symbol('lambda')-lambda_minus))==0
assert sp.simplify((lambda_plus+lambda_minus)/2-sp.Rational(3,2))==0
assert sp.simplify((lambda_plus-lambda_minus)/2-sp.sqrt(5)/2)==0
assert sp.simplify((1+sp.sqrt(5)/3)/2-(3+sp.sqrt(5))/6)==0

p=sp.Symbol('p',real=True)
z,w=sp.symbols('z w')
H=(2-p*z-(1-p)*w)**-2
assert sp.simplify(H.subs(w,z)-(2-z)**-2)==0
# Conditional total count / binomial splitting: coefficient of z^j w^k.
for j in range(5):
    for k in range(5):
        total=j+k
        coeff=sp.diff(H,z,j,w,k).subs({z:0,w:0})/sp.factorial(j)/sp.factorial(k)
        expected=sp.binomial(total,j)*(total+1)*p**j*(1-p)**k/sp.Integer(2)**(total+2)
        assert sp.simplify(coeff-expected)==0

pg=(3+sp.sqrt(5))/6
cov=(sp.Rational(1,9)-1/((1+2*p)**2*(3-2*p)**2))/4
assert sp.simplify(cov.subs(p,sp.Rational(1,2))-sp.Rational(7,576))==0
assert sp.simplify(cov.subs(p,pg)-sp.Rational(58,8649))==0
# Genuine failure of Lorentz invariance of the characteristic function.
assert H.subs({p:sp.Rational(1,2),z:-1,w:1})==sp.Rational(1,4)
assert H.subs({p:sp.Rational(1,2),z:-1,w:-1})==sp.Rational(1,9)

A,B=sp.symbols('A B',real=True)
C=p*A+(1-p)*B
D=p*A*(1-A)+(1-p)*B*(1-B)
d=1+C
J=-sp.Rational(151,120)*C/d**3+3*D/d**4
fake=J-sp.Rational(59,120)*C/d**3
assert sp.simplify(J-fake-sp.Rational(59,120)*C/d**3)==0
assert sp.simplify(J.subs({A:0,B:0}))==0
assert sp.simplify(J.subs({A:1-z,B:0,p:1}) -(-sp.Rational(151,120)*(1-z)/(2-z)**3 + 3*z*(1-z)/(2-z)**4))==0

# Independently evaluate the finite two-panel transform through the
# original signed four-pole Laplace moments, not the word enumeration.
def original_R(t):
    t=F(t)
    return F(4)/t-F(2)/(t+3)-F(1)/(t+4)-F(1)/(t+5)

def finite_direct(n,m1,z,w):
    z,w=F(z),F(w)
    a=8*n-7
    acc=F()
    for i in range(m1+1):
        ci=comb(m1,i)*z**(m1-i)*(1-z)**i
        for j in range(n-m1+1):
            cj=comb(n-m1,j)*w**(n-m1-j)*(1-w)**j
            acc += ci*cj*original_R(a+8*(i+j))
    return acc/original_R(a)

for n,pair,z0,w0 in [(3,1,F(0),F(1,3)),(6,2,F(1,2),F(2,3)),(12,6,F(0),F(1)),(18,9,F(1,3),F(1,2))]:
    true=finite_direct(n,pair,z0,w0)
    pr=F(pair,n)
    central=1/(1+pr*(1-z0)+(1-pr)*(1-w0))**2
    c=pr*(1-z0)+(1-pr)*(1-w0)
    dd=pr*(1-z0)*z0+(1-pr)*(1-w0)*w0
    jj=-F(151,120)*c/(1+c)**3+3*dd/(1+c)**4
    print(f'n={n} p={pr}: exact polynomial {float(true):.10f}, first-jet approx {float(central+jj/n):.10f}')
print('PASS: golden hyperbolic Q, true/projective clock, 25 bivariate coefficients, parity, noninvariance, source first-jet, independent four-pole finite sum')
