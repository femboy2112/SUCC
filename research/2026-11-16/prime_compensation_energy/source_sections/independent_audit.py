"""Independent symbolic and Fraction audit; does NOT import source_sections.py."""
import json
from fractions import Fraction as F
from itertools import combinations
from math import gcd, isqrt
import sympy as sp

checks=0

def verify(x):
    global checks
    assert x
    checks+=1

# Symbolic, arbitrary two-prime transports, using direct matrices (not helpers).
a,b=sp.symbols('a b', positive=True)
U,V=sp.symbols('U V')
B=lambda z:sp.Matrix([[-(z+1/z)/2,(z-1/z)/2],[(z-1/z)/2,-(z+1/z)/2]])
verify(sp.simplify(B(a)*B(b)-B(b)*B(a))==sp.zeros(2))
verify(sp.simplify(B(a).T*sp.diag(1,-1)*B(a)-sp.diag(1,-1))==sp.zeros(2))
verify(sp.simplify((B(a)*B(b))[0,0]-(B(a))[0,0]*(B(b))[0,0]-(a-1/a)*(b-1/b)/4)==0)
verify(sp.simplify((B(a)*B(b)*sp.Matrix([U,0]))[0]-(B(a)[0,0]*B(b)[0,0]*U) - ((a-1/a)*(b-1/b)/4)*U)==0)
verify(sp.simplify((B(sp.Integer(2))*B(sp.Integer(4)))[0,0]-sp.Rational(65,16))==0)
verify(sp.simplify(B(sp.Integer(2))[0,0]*B(sp.Integer(4))[0,0]-sp.Rational(85,32))==0)
verify(sp.simplify(sp.Rational(65,16)-sp.Rational(85,32)-sp.Rational(45,32))==0)
# Source hyperbola and branch reset: start authentic E=1,R=-1/12, p=3 then p=5.
v0=sp.Matrix([sp.Rational(11,24),sp.Rational(13,24)])
x=B(sp.Integer(2))*v0
verify(x==sp.Matrix([sp.Rational(-1,6),sp.Rational(-1,3)]))
verify(x[0]**2-x[1]**2==-sp.Rational(1,12))
wrong=sp.Matrix([x[0],-x[1]])
verify(wrong[0]**2-wrong[1]**2==-sp.Rational(1,12))
verify((B(sp.Integer(4))*x)[0]==-sp.Rational(13,48))
verify((B(sp.Integer(4))*wrong)[0]==sp.Rational(47,48))
verify(((B(sp.Integer(4))*(x-wrong))[0])==-sp.Rational(5,4))

# Direct Hurwitz/Bernoulli reduced-residue source (not factor-product R).
for ps in [(),(2,),(2,3),(2,3,5),(2,3,5,7)]:
    Q=sp.prod(ps)
    FQ=sp.prod([1-sp.Integer(p) for p in ps])
    RQ=-sp.Rational(Q,2)*sum((sp.bernoulli(2,sp.Rational(k,Q)) for k in range(1,Q+1) if gcd(k,Q)==1),sp.Integer(0))
    verify(sp.simplify(RQ/FQ+sp.Rational(1,12))==0)

# Direct four-pole partial source, constructed without recurrence.
def fourpole(j):return F(4,8*j-7)-F(2,8*j-4)-F(1,8*j-3)-F(1,8*j-2)
def U(n):return sum((16**(n-j)*fourpole(j) for j in range(1,n+1)),F())
for n in range(1,41):
    x=U(n)
    c=x.numerator//x.denominator
    v=x-c
    r=fourpole(n+1)
    y=U(n+1)
    cp=y.numerator//y.denominator
    yp=y-cp
    verify(cp-16*c==(16*v+r).numerator//(16*v+r).denominator)
    verify(cp-16*c +yp-16*v-r==0)
    verify((c+v)==x)
    verify(F(0)<r<1)
    # first digit needs one additional hidden branch bit for any cell
    for k in range(16):
        lo=k+r
        hi=k+1+r
        flo=lo.numerator//lo.denominator
        fhi=-((-hi).numerator//(-hi).denominator)-1
        verify(fhi-flo==1)

# Two-step compensation with independent arithmetic.
for n in range(1,41):
    c=U(n).numerator//U(n).denominator
    c2=U(n+2).numerator//U(n+2).denominator
    u=U(n)-c
    w=U(n+2)-c2
    r=16*fourpole(n+1)+fourpole(n+2)
    verify(F(c2-256*c)+w-256*u-r==0)

# 16^k quantization forecast bounds (no main module imports).
for n in range(1,25):
    u=U(n)
    c=u.numerator//u.denominator
    for k in range(1,4):
        M=16**k
        digit=(M*(u-c)).numerator//(M*(u-c)).denominator
        lo=c+F(digit,M)
        hi=c+F(digit+1,M)
        verify(lo<=u<hi)
        for h in (1,2,3):
            shift=sum((16**(h-j)*fourpole(n+j) for j in range(1,h+1)),F())
            a=16**h*lo+shift
            b=16**h*hi+shift
            minimum=a.numerator//a.denominator
            maximum=-((-b).numerator//(-b).denominator)-1
            ctrue=U(n+h).numerator//U(n+h).denominator
            verify(minimum<=ctrue<=maximum)

print(json.dumps({"symbolic_checks":13,"total_assertions":checks,"status":"PASS","claim":"finite exact and symbolic calibrations only"},indent=2))
