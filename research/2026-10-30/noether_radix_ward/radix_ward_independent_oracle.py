"""Independent high-precision combinatorial Fourier oracle: no imports from probes."""
import mpmath as mp
from math import factorial
from collections import defaultdict
from fractions import Fraction as F

mp.mp.dps=90
b=16
pol=((4,0),(-2,3),(-1,4),(-1,5))
R=lambda a:sum((F(c,a+d) for c,d in pol),F(0))
N=4;h=1
U=[F(0)]
for n in range(1,N+1):U.append(b*U[-1]+R(8*n-7))

def compositions(k,length):
    if length==1:yield (k,)
    else:
        for i in range(k+1):
            for tail in compositions(k-i,length-1):yield (i,)+tail

def integer_phase(z):
    v=z-z.numerator//z.denominator
    return mp.exp(2*mp.pi*1j*mp.mpf(v.numerator)/v.denominator)

def multinomial(m):
    num=factorial(sum(m))
    for j in m:num//=1
    den=1
    for j in m:den*=factorial(j)
    return num//den

k=17
buckets=defaultdict(list)
for mm in compositions(k,N):
    f=sum(mm[j]*b**(j+1) for j in range(N))
    amp=multinomial(mm)
    phi=sum((mm[j]*U[j+1] for j in range(N)),F(0))
    buckets[f].append((mm,amp,phi))

left=mp.mpf(0)
diag=0
for a in buckets.values():
    diag+=sum(t[1]**2 for t in a)
    z=sum((amp*integer_phase(ph) for _,amp,ph in a),mp.mpc(0))
    left+=abs(z)**2

right=mp.mpf(diag)
for p in range(2,N+1):
    for q in range(p+1,N+1):
        coeff=17 if q==p+1 else 289
        right+=2*coeff*mp.re(integer_phase(R(8*q-7)-R(8*p-7)))
assert abs(left-right)<mp.mpf('1e-58'),mp.nstr(left-right,15)

# Verify first 16-vs-1 mixed moment independently from character projection.
source=sum(integer_phase(-R(8*(n+1)-7)) for n in range(1,N))
# 16 copies of each source phase, 1 negative frequency at next index.
third=sum(integer_phase(16*U[n]-U[n+1]) for n in range(1,N))
assert abs(source-third)<mp.mpf('1e-70')

# Localized selection is a different, exponentially narrowing measurement.
f=lambda n:integer_phase(U[n])
W=sum(f(n) for n in range(1,N+1))
K=lambda z:(mp.exp(2*mp.pi*1j*z)-1)/(2*mp.pi*1j*z)
local=sum(f(n)*K(mp.mpf(16)**(n-N)) for n in range(1,N+1))
assert abs(local-W)<mp.mpf(32)*mp.pi/15

print('N',N,'first 34th balanced moment value:',mp.nstr(left,25))
print('34th moment minus its diagonal:',mp.nstr(left-diag,25))
print('17-factor unbalanced source Ward moment:',mp.nstr(source,25))
print('localized seed cylinder vs exact selected sum:',mp.nstr(local,19),mp.nstr(W,19))
print('Independent 90-digit first-collision / source-resonance oracle PASS')
