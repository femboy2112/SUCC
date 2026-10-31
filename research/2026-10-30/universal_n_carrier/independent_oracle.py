"""Independent symbolic/integral checks for SUCC's universal N bridge.

Requires sympy and mpmath. The classical analytic proofs are in the dossier.
"""
from fractions import Fraction as F
import sympy as sp
import mpmath as mp

mp.mp.dps=65
a,x=sp.symbols("a x",positive=True)
c=(4,-2,-1,-1)
d=(0,3,4,5)
R=sum(sp.Integer(ci)/(a+di) for ci,di in zip(c,d))
V=a**4/((a+3)**2*(a+4)*(a+5))
Q=sum(sp.Integer(ci)*sp.exp(-di*x) for ci,di in zip(c,d))
assert sp.simplify(sp.diff(sp.log(V),a)-R)==0
assert sp.factor(R)==(15*a*a+121*a+240)/(a*(a+3)*(a+4)*(a+5))
assert [sp.diff(Q,x,j).subs(x,0) for j in (1,2,3)]==[15,-59,243]

def positive_q(y):
    return -2*mp.expm1(-3*y)-mp.expm1(-4*y)-mp.expm1(-5*y)

def rational_r(A):
    return mp.mpf(4)/A-mp.mpf(2)/(A+3)-1/(mp.mpf(A)+4)-1/(mp.mpf(A)+5)

for A in (1,9,17,73,257):
    actual=mp.quad(lambda y:mp.exp(-A*y)*positive_q(y),[0,1,mp.inf])
    assert abs(actual-rational_r(A))<mp.mpf('1e-58')

q=(mp.mpf(1)/8,mp.mpf(1)/2,mp.mpf(5)/8,mp.mpf(3)/4)
C0=mp.fprod(mp.gamma(z)**(-ci) for ci,z in zip(c,q))
S_R=-mp.fsum(ci*mp.digamma(z) for ci,z in zip(c,q))/8
for N in (1,7,25,90):
    product=F(1)
    for n in range(1,N+1):
        A=8*n-7
        product*=F(A**4,(A+3)**2*(A+4)*(A+5))
    via_gamma=mp.fprod(mp.gamma(N+z)**ci/mp.gamma(z)**ci
                       for ci,z in zip(c,q))
    assert abs(mp.mpf(product.numerator)/product.denominator-via_gamma)<mp.mpf('1e-55')
    N2=product.denominator;v2=0
    while N2%2==0:
        N2//=2;v2+=1
    assert v2==5*N

for N in (100,1000,10000):
    gamma_value=mp.fprod(mp.gamma(N+z)**ci/mp.gamma(z)**ci
                         for ci,z in zip(c,q))
    assert abs(gamma_value*N**(mp.mpf(15)/8)/C0-1)<mp.mpf('0.003')

# Lerch relation: numerical Hurwitz differentiation at q=1/8 can be unstable
# at high precision. This is calibration only, not its proof.
lerch=-mp.fsum(ci*mp.diff(lambda s,q0=z:mp.zeta(s,q0),0)
              for ci,z in zip(c,q))
assert abs(lerch-mp.log(C0))<mp.mpf('1e-8')
assert abs(mp.zeta(-1)+mp.zeta(2)/(2*mp.pi**2))<mp.mpf('1e-58')

for rank in (2,3,4):
    for j in range(4):
        prob=mp.quad(
            lambda y:y**(rank-1)*mp.exp(-y)/mp.gamma(rank)
              *mp.exp(-y)*y**j/mp.factorial(j),
            [0,1,mp.inf])
        pascal=mp.binomial(rank+j-1,j)*mp.mpf(2)**(-rank-j)
        assert abs(prob-pascal)<mp.mpf('1e-55')

assert sum(c)==0
assert sum(ci*di for ci,di in zip(c,d))==-15
assert sum(ci*di**2 for ci,di in zip(c,d))==-59
assert sum(ci*di for ci,di in zip((5,-5,0,0),d))==-15
print("Independent symbolic/direct-integral/Gamma/Hurwitz oracle PASS")
print("C_BBP =",mp.nstr(C0,32))
print("S_R =",mp.nstr(S_R,32))
print("Green memory =",mp.nstr((S_R-mp.pi)/15,32))
