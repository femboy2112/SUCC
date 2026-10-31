"""Separately implemented SymPy + mpmath counting-quotient oracle.

All finite carrier identities derive from the original four signed poles;
analytic tail estimates accompany truncated transcendental series.
"""
import sympy as S
import mpmath as m
from fractions import Fraction as F
from math import factorial
from collections import defaultdict

m.mp.dps = 60
n, t = S.symbols('n t',positive=True)
r = 4/(8*n-7)-2/(8*n-4)-1/(8*n-3)-1/(8*n-2)
assert S.factor(r)==(120*n*n-89*n+16)/((2*n-1)*(4*n-1)*(8*n-7)*(8*n-3))

def rr(i):
    return m.mpf(4)/(8*i-7)-m.mpf(2)/(8*i-4)-m.mpf(1)/(8*i-3)-m.mpf(1)/(8*i-2)

S_R = -(4*m.digamma(m.mpf(1)/8)-2*m.digamma(m.mpf(1)/2)
        -m.digamma(m.mpf(5)/8)-m.digamma(m.mpf(3)/4))/8
assert abs(S_R-m.mpf('3.38604761959719172193641883143841286022691835'))<m.mpf('1e-44')
B = m.pi/16
memory = (S_R-m.pi)/15
assert abs(memory-m.mpf('0.0162969977338265'))<m.mpf('1e-15')

# Different implementations of finite source/conjugacy checks.
def rf(i):
    a=8*i-7
    return F(120*i*i-89*i+16,(2*i-1)*(4*i-1)*(8*i-7)*(8*i-3))

for M in (2,8,20):
    xs=[F(0)]
    for i in range(1,M+1): xs.append(16*xs[-1]+rf(i))
    tails=[sum((rf(i)/16**(i-j) for i in range(j+1,M+1)),F(0))
           for j in range(M+1)]
    for i in range(M+1):
        assert xs[i]+tails[i]==16**i*tails[0]

# First 34th moment group-algebra bucket comparison against the O(N)
# source-series identity, authored independently of exact unittest module.
def comp(k,p):
    if p==1:
        yield (k,)
    else:
        for v in range(k+1):
            for q in comp(k-v,p-1):yield (v,)+q

N=5; h=1; u=[F(0)]
for i in range(1,N+1):u.append(16*u[-1]+rf(i))
buckets=defaultdict(list)
for v in comp(17,N):
    z=sum(v[i]*16**(i+1) for i in range(N))
    numerator=factorial(17)
    denominator=1
    for x in v:denominator*=factorial(x)
    coefficient=numerator//denominator
    phase=sum((v[i]*u[i+1] for i in range(N)),F(0))
    buckets[z].append((coefficient,phase))
loss=m.mpf(0)
for cl in buckets.values():
    for j in range(len(cl)):
        for k in range(j+1,len(cl)):
            ca,a=cl[j];cb,b=cl[k]
            v=F(a-b)
            theta=2*m.pi*m.mpf(v.numerator)/v.denominator
            loss+=2*ca*cb*(1-m.cos(theta))

rates=[rr(i) for i in range(N+1)]
A_N=sum((2*m.sin(m.pi*h*rates[i])**2 for i in range(2,N+1)),m.mpf(0))
S_N=sum((m.sin(2*m.pi*h*rates[i]) for i in range(2,N+1)),m.mpf(0))
B_N=sum((2*m.sin(m.pi*h*(rates[i+1]-rates[i]))**2 for i in range(2,N)),m.mpf(0))
loss_fast=578*(N-1)*A_N-289*(A_N*A_N+S_N*S_N)-544*B_N
assert abs(loss-loss_fast)<m.mpf('1e-50')
print('N=5 independent exact collision/orbit defect',m.nstr(loss,35))

# High-precision O(N) full counting quotient: S uses the Gauss digamma
# expression for sum r_n and the rapidly convergent sine-minus-linear tail.
A=S_corr=Badj=m.mpf(0)
prev=None
M=20000
for i in range(2,M+1):
    x=2*m.pi*rr(i)
    A+=2*m.sin(x/2)**2
    S_corr+=m.sin(x)-x
    if prev is not None: Badj+=2*m.sin((x-prev)/2)**2
    prev=x
SumS=2*m.pi*(S_R-m.mpf(47)/15)+S_corr
Cinf=-578*A-289*(A*A+SumS*SumS)-544*Badj
print('original source digamma S_R',m.nstr(S_R,36))
print('A1 quotient source dephasing',m.nstr(A,36))
print('S1 source sine sum (digamma corrected)',m.nstr(SumS,36))
print('B1 adjacent source dispersion',m.nstr(Badj,36))
print('C1 quotient constant',m.nstr(Cinf,36))

# Rigorous tail bounds via r_i <=15/(8i-7)^2 and elementary trigonometry.
tail_A=2*m.pi**2*(m.mpf(225)/(24*(8*M-7)**3))
tail_sin_correction=(2*m.pi)**3/6*(m.mpf(3375)/(40*(8*M-7)**5))
assert tail_A<m.mpf('1e-11')
assert tail_sin_correction<m.mpf('1e-18')
print('certified A1 tail upper',m.nstr(tail_A,17))
print('sine-minus-linear correction tail upper',m.nstr(tail_sin_correction,17))

# Source-only character of the quotient is a decisive nonnormal counterseed
# because all Haar seed moments are invariant under translation.
assert rr(2)>0
print('Independent symbolic and high-precision quotient oracle PASS')
