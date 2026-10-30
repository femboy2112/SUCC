"""Independent SymPy/Fraction research oracle; does NOT import minimal_pole_gamma.
Tests identities and finite witnesses, not universal proof by enumeration.
"""
from fractions import Fraction as F
from math import factorial
import sympy as s

m,d,p,q,r,a,n,z=s.symbols('m d p q r a n z', positive=True)
W=p+q+r
u,v,w=m-d,m,m+d
R=W/a-p/(a+u)-q/(a+v)-r/(a+w)
S=p*u+q*v+r*w
L=W*(u*v+u*w+v*w)-p*v*w-q*u*w-r*u*v
C=W*u*v*w
checks=0

def check(cond, label):
    global checks
    if cond is not True and cond != s.true:
        raise AssertionError(f'{label}: {cond}')
    checks+=1

check(s.cancel(R*a*(a+u)*(a+v)*(a+w)-(S*a*a+L*a+C))==0,'all-weight source numerator')
check(s.factor(C-S*m*m-m*d*(m*(p-r)-d*W))==0,'selfduality exact residual')
check(s.factor(S-(m*W+d*(r-p)))==0,'rank two coefficient')
check(s.simplify((C/S).subs({p:2,q:1,r:1})-m*m-m*d*(m-4*d)/(4*m-d))==0,'unique geometric center')

for mm in range(2,9):
    for dd in range(1,mm):
        for pp,qq,rr in ((2,1,1),(2,2,1),(3,2,1),(4,1,1)):
            check((S.subs({m:mm,d:dd,p:pp,q:qq,r:rr})>0) == True,'source first moment')
            check((C.subs({m:mm,d:dd,p:pp,q:qq,r:rr})>0) == True,'source constant')
            rho=s.factor((C/S).subs({m:mm,d:dd,p:pp,q:qq,r:rr}))
            match=(mm*(pp-rr)==dd*(pp+qq+rr))
            check(bool(rho==mm*mm)==match,'reciprocal center equivalence')

for M in range(3,13):
    for pp in range(1,M-1):
        for qq in range(1,M-pp):
            rr=M-pp-qq
            if pp<=rr: continue
            mm=F(M,pp-rr)
            if mm<=1: continue
            if M==4: check((pp,qq,rr,mm)==(2,1,1,F(4)),'unique positive minimal')
            else:check(M>4,'higher-weight only')

original=s.cancel(R.subs({m:4,d:1,p:2,q:1,r:1}))
ref=(15*a*a+121*a+240)/(a*(a+3)*(a+4)*(a+5))
check(s.cancel(original-ref)==0,'original unchanged')
check(s.discriminant(15*a*a+121*a+240,a)==241,'original real roots')
check(s.factor((15*a*a+121*a+240).subs(a,0)/15)==16,'root product 16')
D=16*(a+3)*(a+5)/((3*a+16)*(5*a+16))
check(s.cancel(D-1-(a*a-16)/((3*a+16)*(5*a+16)))==0,'inversion sign')
check(s.cancel(D*D.subs(a,16/a)-1)==0,'reciprocity involution')
check(s.cancel(D.subs(a,1)-s.Rational(128,133))==0,'cross first')
check(s.cancel(D.subs(a,9)-s.Rational(2688,2623))==0,'cross second')
clock=s.factor(D.subs(a,8*n-7)*s.Rational(15,16))
f=(24*n-6)*(40*n-20)/((24*n-5)*(40*n-19))
check(s.cancel(clock-f)==0,'exact two-channel split')

x=s.symbols('x',positive=True)
eta=s.log((24/x-5)/(24/x-6))+s.log((40/x-19)/(40/x-20))
series=s.series(eta,x,0,5).removeO().expand()
check(s.factor(series.coeff(x,1)-s.Rational(1,15))==0,'harmonic log exponent')
check(s.factor(series.coeff(x,2)-s.Rational(313,14400))==0,'second source correction')
check(s.factor(series.coeff(x,3)-s.Rational(21091,2592000))==0,'third source correction')

for N in range(0,150):
    P=s.prod(s.Rational((24*j-6)*(40*j-20),(24*j-5)*(40*j-19)) for j in range(1,N+1))
    # Independent factorial / Pochhammer implementation.
    Cgamma=s.rf(s.Rational(1,2),N)*s.rf(s.Rational(3,4),N)/(
        s.rf(s.Rational(19,24),N)*s.rf(s.Rational(21,40),N))
    check(P==Cgamma,'finite Gamma product')

# A direct rational comparison with the actual signed BBP forcing for many clocks.
for k in range(1,151):
    ak=8*k-7
    forcing=s.Rational(4,ak)-s.Rational(2,ak+3)-s.Rational(1,ak+4)-s.Rational(1,ak+5)
    check(forcing==ref.subs(a,ak),'authentic forcing passport')
    uk=s.Rational(16,15)*s.Rational((24*k-6)*(40*k-20),(24*k-5)*(40*k-19))
    check(uk==D.subs(a,ak),'native reciprocal path')

# The quadratic weights can move without preserving the center; exact controls.
for args in [(4,1,2,2,1),(5,1,2,1,1),(4,2,2,1,1),(3,1,3,2,1),(5,1,2,2,1)]:
    mm,dd,pp,qq,rr=args
    rho=s.factor((C/S).subs({m:mm,d:dd,p:pp,q:qq,r:rr}))
    check(bool(rho==mm*mm)==(mm*(pp-rr)==dd*(pp+qq+rr)),'hostile selfduality')

# The ORIGINAL source has the historically cited degree-(2,4) rational-map
# passport.  Independent polynomial invariants expose 2,3,5 (no digit theorem).
X=s.symbols('X')
Apoly=120*X*X-89*X+16
Dpoly=(2*X-1)*(4*X-1)*(8*X-7)*(8*X-3)
check(s.cancel(ref.subs(a,8*X-7)-Apoly/Dpoly)==0,'authentic x-polynomial passport')
check(s.resultant(Apoly,Dpoly,X)==-(2**15)*(3**2)*(5**2),'exceptional resultant 2 3 5')
check(s.discriminant(Dpoly,X)==(2**24)*(3**2)*(5**2),'exceptional discriminant 2 3 5')

print('INDEPENDENT_EXACT_ORACLE_PASS assertions='+str(checks))
