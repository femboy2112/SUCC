# Is "admissible" a strict extension of #521 CT-03's domain 16^d<(8A+1)(8A+2)? Exact rational enclosures.
from fractions import Fraction as F
import sympy as sp
def r(n): return F(4,8*n-7)-F(2,8*n-4)-F(1,8*n-3)-F(1,8*n-2)
m=sp.symbols('m',positive=True)
rm=sp.Rational(4)/(8*m-7)-sp.Rational(2)/(8*m-4)-sp.Rational(1)/(8*m-3)-sp.Rational(1)/(8*m-2)
num=sp.factor(sp.numer(sp.together(sp.diff(rm,m))))
print("numerator of r'(m):",sp.expand(num))
# r decreasing for m>=2 => T_n decreasing (T_n-T_{n+1}=sum 16^-j (r(n+j)-r(n+j+1)))
print("r'(m)<0 checked symbolically for m>=2:", all(sp.Poly(sp.expand(-num.subs(m,m+2)),m).all_coeffs()[i]>=0 for i in range(sp.degree(num,m)+1)) )
def Tenc(n,D=40):
    lo=sum((r(n+j)/F(16)**j for j in range(1,D+1)),F(0))
    # r(q) < 15/(64q^2)+1/q^3 (CT1, q>=2) <= (15/64+1/n)/n^2 for q>n
    hi=lo+F(1,16**D)*(F(15,64)+F(1,n))/(F(n)**2*15)
    return lo,hi
bad=[]
for d in range(2,201):
    N0=2**(2*d-3)
    ct03=lambda A:16**d<(8*A+1)*(8*A+2)
    assert ct03(N0) and not ct03(N0-1)
    lo_prev,_=Tenc(N0-1,D=d+12); _,hi0=Tenc(N0,D=d+12)
    adm_N0 = 16**d*hi0<=1          # with T decreasing => whole window [N0,2N0) admissible
    nonadm_prev = 16**d*lo_prev>1  # A=N0-1 fails at n=N0-1
    if not(adm_N0 and nonadm_prev): bad.append(d)
print("d in [2,200] where admissible-threshold != CT-03 threshold (=2^(2d-3)):",bad)
