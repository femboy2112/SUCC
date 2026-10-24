#!/usr/bin/env python3
"""Independent exact polynomial-filter calibration from the translator lane."""
from fractions import Fraction as Q
from math import comb
from collections import Counter
import json, hashlib
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from observational_succ.bbp_source_memory import forcing
from observational_succ.pi_pascal_kernel import tail_pascal_interval
checks=Counter()
def check(name, cond):
    assert cond, name
    checks[name]+=1

def vp2(x):
    x=Q(x)
    assert x
    a,b=abs(x.numerator),x.denominator
    return ((a&-a).bit_length()-1)-((b&-b).bit_length()-1)
def nu(j): return 2*j-j.bit_count()-1
U=[Q()]
for n in range(1,210): U.append(16*U[-1]+forcing(n))
def mul(p,q):
    z=[Q()]*(len(p)+len(q)-1)
    for i,a in enumerate(p):
        for j,b in enumerate(q): z[i+j]+=a*b
    return z
def filt(poly,k,start=0):
    out=[Q(1)]
    for _ in range(k): out=mul(out,poly)
    return sum((a*U[start+i] for i,a in enumerate(out)),Q())
def delta(seq,k,n=0):
    return sum(((-1)**(k-j)*comb(k,j)*seq[n+j] for j in range(k+1)),Q())
for b in (1,2,3):
    check('no_base3_denominator_below4',not any((a-3*b)%16==0 for a in range(-b,b+1)))
for m in range(1,161):
    for b in (1,2):
        check('no_power3_denominator_below3',not any((a-b*3**m)%15==0 for a in range(-b,b+1)))
    feasible=all(any((a-3**(m+1))%mod==0 for a in range(-3,4)) for mod in (15,16))
    check('denominator3_power_condition',feasible==(m%4==0))
P4=[-Q(1),Q(1,4)]
P81=[Q(1),-Q(1,3),Q(1,3)]
P31=[-Q(1),Q(2),Q(),Q(),-Q(16),Q(17),-Q(1)]
for k in range(1,81):
    h=filt([-Q(4),Q(1)],k)
    check('denominator4_dyadic_value',vp2(h)==vp2(k))
    check('denominator4_scaled_value',vp2(h/4**k)==vp2(k)-2*k)
Z=[filt(P81,k) for k in range(49)]
for j in range(1,33):
    bj=delta(U,j,j)/3**j
    check('base81_origin_newton',delta(Z,j)==bj)
    check('base81_origin_valuation',vp2(bj)==nu(j))
for k in range(17):
    for j in range(1,17): check('base81_full_grid_valuation',vp2(delta(Z,j,k))==nu(j))
for n in [2,3,7]:
    S=[filt(P81,k,n)-81**k*U[n] for k in range(34)]
    check('base81_reset_zero',S[0]==0)
    for j in range(1,17):
        bj=delta(U,j,n+j)/3**j-80**j*U[n]
        check('base81_reset_newton',delta(S,j)==bj)
    for k in range(17):
        for j in range(1,17): check('base81_reset_grid_valuation',vp2(delta(S,j,k))==nu(j))
    s=[S[k+1]-81*S[k] for k in range(33)]
    for k in range(13):
        for j in range(13): check('base81_reset_cm_forcing',(-1)**j*delta(s,j,k)>0)
V=[filt(P31,k) for k in range(25)]
for k in range(9):
    for j in range(1,9): check('base31_profile_repair',vp2(delta(V,j,k))==nu(j))
for n in range(65):
    check('base81_local_transport',(U[n+2]-U[n+1]+3*U[n])/3==81*U[n]+5*forcing(n+1)+forcing(n+2)/3)
for j in range(1001):
    t=Q(j,1000)
    p=1-t*(1-t)/3
    check('base81_kernel_positive',Q(11,12)<=p<=1)
    check('base81_eighth_power_bound',p**8<=max(t,1-t))
    p31=sum(c*t**i for i,c in enumerate(P31))
    check('base31_kernel_norm',-1<=p31<=1)
check('eighth_power_sharp_integer',2*11**7>12**7 and 2*11**8<12**8)
check('weak_symmetry_control',(16*Q(1,5))%1==Q(1,5) and (81*Q(1,5))%1==Q(1,5) and (3*Q(1,5))%1!=Q(1,5))
# Independent Machin interval; 200 terms is far more precision than needed here.
def atan_interval(b,n=200):
    a=sum((Q((-1)**j,(2*j+1)*b**(2*j+1)) for j in range(n)),Q())
    nxt=a+Q((-1)**n,(2*n+1)*b**(2*n+1))
    return min(a,nxt),max(a,nxt)
a,b=atan_interval(5),atan_interval(239)
alpha=(a[0]-b[1]/4,a[1]-b[0]/4)
for n in [0,1,2,7]:
    for k in [1,2,7,8,16,31,40]:
        z=filt(P81,k,n)
        lo,hi=(81**k*16**n*e-z for e in alpha)
        m=k//8
        bound=tail_pascal_interval(n,m,5)[1]+tail_pascal_interval(n+m,0,5)[1]
        check('base81_machin_positive_remainder',0<lo<hi<bound)
result={'status':'PASS','assertions':sum(checks.values()),'categories':dict(checks),'sample':{'U2':str(U[2]),'Z1':str(Z[1]),'Z1_dropped_carry':str(((3*Z[1])%1)/3)},'boundaries':['Finite exact checks only; universal claims have paper proofs.','No real collision or same-law invariance estimate is asserted.']}
print(json.dumps(result,indent=2))
