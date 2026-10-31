"""Exact finite arithmetic plus numerical calibration for K01--K05.

Universal claims come from KERNEL_TRANSPORT.md, not these finite calculations.
"""
from collections import Counter
from fractions import Fraction as F
from math import cos, log, pi, sin, sqrt
import cmath


def source(n):
    assert n >= 1
    return 4*F(1,8*n-7)-2*F(1,8*n-4)-F(1,8*n-3)-F(1,8*n-2)


def positive_source(n):
    a=8*n-7
    return 6*F(1,a*(a+3))+4*F(1,a*(a+4))+5*F(1,a*(a+5))


def tail_interval(n, terms=24):
    lo=sum((source(n+j)/16**j for j in range(1,terms+1)), F(0))
    hi=lo+source(n+terms+1)/(15*16**terms)
    return lo,hi


def rational_states(N,seed=F(0)):
    u=seed
    out=[]
    for n in range(1,N+1):
        u=(16*u+source(n))%1
        out.append(u)
    return out


def coefficient_moments(H):
    return tuple(sum((F(H-abs(h),H)*h**j for h in range(1-H,H)),F(0))
                 for j in (0,1,2))


def fejer(t,H):
    t=float(t)%1
    if t>0.5: t-=1
    if t==0: return float(H)
    return sin(pi*H*t)**2/(H*sin(pi*t)**2)


def energy(points,H):
    N=len(points)
    total=1.0
    for h in range(1,H):
        z=sum(cmath.exp(2j*pi*h*float(x)) for x in points)/N
        total+=2*(1-h/H)*abs(z)**2
    return total


def hard(points,q):
    counts=Counter(int(q*(x%1)) for x in points)
    return F(q*sum(v*v for v in counts.values()),len(points)**2)


def transport_budget(N,H):
    return sqrt(pi/(8*sqrt(3)))*sqrt(H)*(H*H-1)**0.25/N


def pointwise_budget(tails,H):
    D=2*pi*sqrt(H*(H*H-1)/6)
    return sum(min(sqrt(2*H),D*float(t)) for t in tails)/len(tails)


def block_counts(digits,N,m):
    assert len(digits)>=N+m-1
    return Counter(tuple(digits[n:n+m]) for n in range(N))


def entropy_bound_check(digits,N,m,k,base=2):
    cm=block_counts(digits,N,m)
    ck=block_counts(digits,N,k)
    Q=F(base**m*sum(v*v for v in cm.values()),N*N)
    l1=sum(abs(F(v,N)-F(1,base**k)) for v in ck.values())
    l1+=(base**k-len(ck))*F(1,base**k)
    bound=sqrt(2*log(float(Q))/(m//k))+2*m/N
    return l1,Q,bound


def surgery_counts(j,c_num=1,c_den=3):
    M=16**(j*j)
    L=M//j
    N=M+L
    # Integer comparison avoids numerical log rounding at enormous horizons.
    q=1; m=0
    while 16**((m+1)*c_den)<=N**c_num:
        m+=1; q*=16
    count=max(0,L-m+1)
    return {'j':j,'N':N,'m':m,'zero_starts':count,
            'Q_lower':F(q*count*count,N*N),'density':F(L,N)}


def probe():
    rows=[]
    for N,H in ((11,8),(32,16),(61,32),(128,64)):
        states=rational_states(N)
        tails=[sum(tail_interval(n),F(0))/2 for n in range(1,N+1)]
        completed=[(x+t)%1 for x,t in zip(states,tails)]
        gap=abs(sqrt(energy(states,H))-sqrt(energy(completed,H)))
        first=pointwise_budget(tails,H)
        bound=transport_budget(N,H)
        assert gap<=first+1e-11 and first<=bound+1e-11
        rows.append({'N':N,'H':H,'sqrt_energy_gap':gap,'point_budget':first,
                     'global_budget':bound,'status':'numerical calibration PASS'})
    surgery=[]
    for j in (2,3,5,8,13,21):
        v=surgery_counts(j)
        surgery.append({'j':j,'m':v['m'],'density':str(v['density']),
                        'log_Q_lower_over_m':log(float(v['Q_lower']))/v['m']
                        if v['m']<200 else
                        log(16)+2*(log(v['zero_starts'])-log(v['N']))/v['m']})
    return {'status':'PASS','authority':'finite calibration, proofs in dossier',
            'transport_rows':rows,'slow_normal_surgery':surgery}


if __name__=='__main__':
    import json
    print(json.dumps(probe(),indent=2))
