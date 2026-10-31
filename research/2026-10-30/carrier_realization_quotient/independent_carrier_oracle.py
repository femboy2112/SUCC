"""Independent Machin interval and Fourier/entropy oracle for SUCC raw-state quotient.

Uses source arithmetic independently of carrier_quotient_probe.py; not blind referee.
"""
from fractions import Fraction as F
from collections import Counter
from math import log, pi, sqrt
import math
import mpmath as mp
import sympy as sy

BASE=16

def atan_interval_den(q,nterms):
    partial=sum((F((-1)**j, (2*j+1)*q**(2*j+1)) for j in range(nterms)),F(0))
    error=F(1,(2*nterms+1)*q**(2*nterms+1))
    return ((partial,partial+error) if nterms%2==0
            else (partial-error,partial))

def machin_alpha_interval():
    # pi/16=atan(1/5)-(1/4)atan(1/239), fully rational series bounds.
    a,b=atan_interval_den(5,85)
    c,d=atan_interval_den(239,24)
    return a-d/4,b-c/4

def independent_bbp_alpha_interval(M):
    c=(4,-2,-1,-1);delta=(0,3,4,5)
    total=F(0)
    for n in range(1,M+1):
        a=8*n-7
        r=sum((F(z,a+u) for z,u in zip(c,delta)),F(0))
        total+=r/F(BASE**n)
    n=M+1
    a=8*n-7
    r=sum((F(z,a+u) for z,u in zip(c,delta)),F(0))
    return total, total+r/(F(15)*BASE**M)


def root_cert_interval(lo,hi,K):
    assert int(lo*16**K)==int(hi*16**K),('interval straddles grid',K)
    return int(lo*16**K)

mach=machin_alpha_interval()
bbp=independent_bbp_alpha_interval(96)
assert mach[0]<mach[1] and bbp[0]<bbp[1]
assert max(mach[0],bbp[0])<min(mach[1],bbp[1])
for K in (1,16,40,64,80):
    a=root_cert_interval(*mach,K)
    b=root_cert_interval(*bbp,K)
    assert a==b
print('independent rational Machin / original BBP first 80 hex digits MATCH')
print('first 32 hex:', format(root_cert_interval(*mach,80),'080x')[:32])

# Independent original Green tail budget: digamma from Laplace/source and direct sum.
mp.mp.dps=80
rmp=lambda n: 4/mp.mpf(8*n-7)-2/mp.mpf(8*n-4)-1/mp.mpf(8*n-3)-1/mp.mpf(8*n-2)
S=- (4*mp.digamma(mp.mpf(1)/8)-2*mp.digamma(mp.mpf(1)/2)-mp.digamma(mp.mpf(5)/8)-mp.digamma(mp.mpf(3)/4))/8
memory=(S-mp.pi)/15
assert memory>0 and memory<mp.mpf(1)/32
sum_m=mp.fsum(mp.fsum(rmp(n+j)/mp.power(16,j) for j in range(1,30)) for n in range(1,1500))
print('finite Green residual',mp.nstr(memory-sum_m,30))
assert abs(sum_m-memory)<mp.mpf('0.000012')
print('Green total Wasserstein coupling budget M=',mp.nstr(memory,50),'direct finite sum=',mp.nstr(sum_m,35))

# Mean-word entropy rigidity: exact biased vector + pressure control.
p0=mp.mpf(2)/17
p1=mp.mpf(1)/17
H=-p0*mp.log(p0)-15*p1*mp.log(p1)
D=mp.log(16)-H
assert D>0
for k in (1,5,25,100):
    M=p0**k
    assert mp.log(16**k*M)>=k*D
print('biased full-support entropy deficit nats=',mp.nstr(D,40))

# Exact independent source-atom first angular jet and scalar-product no-go.
a=sy.symbols('a',positive=True)
atoms=((2,3),(1,4),(1,5))
rd=[sy.Rational(c*d)/(a*(a+d)) for c,d in atoms]
ref=[sy.Rational(c*d,15) for c,d in atoms]
for (c,d),r,beta in zip(atoms,rd,ref):
    p=sy.factor(r/sum(rd))
    coeff=sy.limit(a*(p-beta),a,sy.oo)
    assert sy.simplify(coeff-beta*(sy.Rational(59,15)-d))==0
variance=sum(beta*(d-sy.Rational(59,15))**2 for beta,(_,d) in zip(ref,atoms))
assert variance==sy.Rational(164,225)
print('source marks beta=',ref,'angular variance=',variance,'first mark jets exact PASS')

# Finite original arithmetic readout at 4096 digits from independent BBP series,
# with a separate verification of 64 digits from Machin exact interval.
lo,hi=independent_bbp_alpha_interval(4102)
K=4099
m=root_cert_interval(lo,hi,K)
digits=tuple((m>>(4*(K-1-j)))&15 for j in range(K))
for N in (128,512,2048,4096):
    for k in (1,2,3):
        counts=Counter(tuple(digits[j:j+k]) for j in range(N))
        pmax=max(counts.values())
        Hblock=-sum((mp.mpf(n)/N)*mp.log(mp.mpf(n)/N) for n in counts.values())
        print('selected prefix N=',N,'k=',k,'max_count=',pmax,'max/canonical=',mp.nstr(mp.mpf(pmax)*16**k/N,9),'KL_to_uniform=',mp.nstr(k*mp.log(16)-Hblock,12))
print('Independent carrier oracle PASS')
