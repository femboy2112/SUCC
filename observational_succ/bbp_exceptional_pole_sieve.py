"""Exact BBP forcing denominator sieve, including 3/5 pole collisions.

Theorem is about reduced rational *forcing denominators*, NOT selected phases.
Original four poles, zero-origin recurrence are not modified. No normality.
"""
from __future__ import annotations

from math import isqrt
from fractions import Fraction as Q
from .succ_internal_matrix_walk import authentic_r

SOURCE='Q:Coherent-Main-X-four-pole-BBP'
_HIT3=(0,1,2,3,4,5,6,7)
_HIT5=(1,3,4,6,8,9,11,13,14,16,18,19,21,23)


def prime_period(p):
    if type(p) is not int or p<3 or p>101 or any(p%d==0 for d in range(2,isqrt(p)+1)):
        raise ValueError('odd prime <=101 required')
    return 9 if p==3 else 25 if p==5 else p


def hit_classes(p):
    """All n residue classes where p divides denominator of reduced BBP r(n)."""
    if p==3:return _HIT3
    if p==5:return _HIT5
    m=prime_period(p)
    classes=tuple(n for n in range(m) if ((2*n-1)*(4*n-1)*(8*n-7)*(8*n-3))%p==0)
    if len(classes)!=4:raise ArithmeticError('four distinct generic pole roots')
    return classes


def _vp(n,p):
    if type(n) is not int or n<1:raise ValueError('positive integer')
    v=0
    while n%p==0:
        v+=1;n//=p
    return v


def forcing_denominator_depth(n,p):
    """Exact odd-prime valuation of reduced den(r(n)), all p-power levels.

    At 3/5 shared poles cancel in the numerator. Else all four pole roots
    are distinct and numerator is a p-unit whenever a pole is present.
    """
    if type(n) is not int or n<1:raise ValueError('positive n')
    prime_period(p)
    if p==3:
        if n%3==0:return _vp(8*n-3,3)
        if n%3==1:return _vp(4*n-1,3)
        t=(n-2)//3
        if t%3==2:return 0
        return 1+_vp(2*t+1,3)+_vp(8*t+3,3)
    if p==5:
        if n%5==1:return _vp(8*n-3,5)
        if n%5==3:return _vp(2*n-1,5)
        if n%5!=4:return 0
        t=(n-4)//5
        if t%5==4:return 0
        return 1+_vp(4*t+3,5)+_vp(8*t+5,5)
    return sum(_vp(a,p) for a in (2*n-1,4*n-1,8*n-7,8*n-3))


def denominator_depth_transition(old_state,force,p):
    """Odd-prime SUCC ultrametric law including equal-depth cancellations.

    Distinct nonzero denominator depths: next depth is their maximum.
    At tied positive depth, cancellation can lower next depth. This is a
    source-independent identity; source authentication belongs to the caller.
    """
    if type(old_state) is not Q or type(force) is not Q:
        raise ValueError('exact rational state and forcing required')
    prime_period(p)
    a=_vp(old_state.denominator,p)
    b=_vp(force.denominator,p)
    next_state=16*old_state+force
    c=_vp(next_state.denominator,p)
    if c>max(a,b) or (a!=b and c!=max(a,b)) or (a==b and c>a):
        raise ArithmeticError('odd-prime depth transition failed')
    return {'old_depth':a,'force_depth':b,'new_depth':c,
            'tie':a==b and a>0,'depth_drop':c<a,
            'new_state':next_state}


def source_depth_drops(N,primes):
    """Actual zero-anchored BBP tie cancellations, not a Weyl bound."""
    if type(N) is not int or not 1<=N<=512:raise ValueError('bounded N')
    P=tuple(primes)
    if not P or P!=tuple(sorted(set(P))):raise ValueError('distinct sorted primes')
    for p in P:prime_period(p)
    u=Q(0);drops=[];ties=[]
    for n in range(1,N+1):
        r=authentic_r(n)
        for p in P:
            event=denominator_depth_transition(u,r,p)
            if event['tie']:ties.append((n,p,event['old_depth'],event['new_depth']))
            if event['depth_drop']:drops.append((n,p,event['old_depth'],event['new_depth']))
        u=16*u+r
    return {'source':SOURCE,'N':N,'primes':P,'ties':tuple(ties),
            'drops':tuple(drops),'weyl_cancellation_proved':False}


def occupancy(N,p):
    if type(N) is not int or not 1<=N<=100000:
        raise ValueError('bounded N required')
    m=prime_period(p)
    classes=hit_classes(p)
    q,r=divmod(N,m)
    n=q*len(classes)+sum(1 for c in classes if 1<=c<=r)
    if N<=256:
        direct=sum(authentic_r(j).denominator%p==0 for j in range(1,N+1))
        if direct!=n:raise ArithmeticError('source pole arithmetic disagreement')
    return {'p':p,'period':m,'hit_classes':classes,'hits':n,'avoids':N-n,
            'density_numerator':len(classes),'density_denominator':m,
            'error_numerator':m*n-N*len(classes),
            'error_denominator':m,'source':SOURCE,'phase_cancellation_proved':False}


def combined_sieve(N,primes):
    """CRT exact count and Weyl deletion bound; phase correlations untouched."""
    if type(N) is not int or not 1<=N<=100000:
        raise ValueError('bounded N required')
    P=tuple(primes)
    if not P or len(P)>4 or P!=tuple(sorted(set(P))):
        raise ValueError('sorted nonempty distinct prime set (max 4)')
    periods={p:prime_period(p) for p in P}
    hits={p:set(hit_classes(p)) for p in P}
    M=1;survivor_count=1
    for p in P:
        M*=periods[p]
        survivor_count*=periods[p]-len(hits[p])
    if M>250000:raise ValueError('explicit CRT period budget')
    q,r=divmod(N,M)
    tail=sum(all(n%periods[p] not in hits[p] for p in P) for n in range(1,r+1))
    safe=q*survivor_count+tail
    if N<=256 and safe!=sum(all(authentic_r(n).denominator%p for p in P) for n in range(1,N+1)):
        raise ArithmeticError('CRT source mismatch')
    return {'source':SOURCE,'N':N,'primes':P,'period':M,
            'survivors_per_period':survivor_count,'safe':safe,'deleted':N-safe,
            'max_weyl_deletion_error':N-safe,'phase_cancellation_proved':False}
