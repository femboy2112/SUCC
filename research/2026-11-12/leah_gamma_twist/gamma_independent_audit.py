"""Independent integer-LCM and raw-denominator audit of GP-I. Standard library."""
from fractions import Fraction as F
from math import gcd, lcm, isqrt
import json


def primes_to(n):
    flags = bytearray(b'\x01') * (n + 1)
    flags[:2] = b'\x00\x00'
    for p in range(2, isqrt(n) + 1):
        if flags[p]:
            flags[p*p:n+1:p] = b'\x00' * (((n-p*p)//p) + 1)
    return [p for p in range(2, n+1) if flags[p]]


def raw_multipliers(p, stop):
    return [m for m in range(1, stop+1)
            if any((m*p+c) % 8 == 0 for c in (7,4,3,2))]


def bands(residue, stop):
    ms = raw_multipliers(residue, stop)
    return list(zip(ms, ms[1:]))


def envelope(x):
    stop = int(3/x) + 10
    pairs = bands(1, stop) + bands(3, stop)
    return 6*x + 4*sum(max(F(1,a)-(1+x)/b, 0) for a,b in pairs)


def complete_integer_states(N):
    states = [(0, 1)]
    for j in range(1, N+1):
        A,L = states[-1]
        new_L = lcm(L, *(8*j-c for c in (7,4,3,2)))
        new_A = 16*A*(new_L//L)
        new_A += sum(w*(new_L//(8*j-c))
                     for c,w in ((7,4),(4,-2),(3,-1),(2,-1)))
        states.append((new_A,new_L))
    return states


def reduced_den(state):
    A,L=state
    return L//gcd(A,L)


windows=[(31,39),(83,110),(137,205),(211,422)]
states=complete_integer_states(max(t for n,t in windows))
passport_checks=0
for p in [29,31,37,41,43,47,53,59,61,67,71,73]:
    expected=raw_multipliers(1 if p%4==1 else 3, 25)
    assert raw_multipliers(p,25)==expected
    passport_checks+=1

ratios=[F(1,4),F(1,3),F(3,7),F(1,2),F(3,4),F(1)]
wanted=[F(1301,252),F(4951,945),F(2405,441),F(79,14),F(27,4),F(8)]
for x,y in zip(ratios,wanted):
    assert envelope(x)==y
# All breakpoints in [1/100,1] are obtained from the raw residue lists.
pairs=bands(1,310)+bands(3,310)
breakpoints={F(1,100),F(1)} | {F(b-a,a) for a,b in pairs if F(1,100)<=F(b-a,a)<=1}
# Convex piecewise linear C(x) has minimum at x=1/2: compare exact rational
# parts and certify log16 within [2.77,2.78]. This interval follows from the
# positive atanh series below, not a floating logarithm.
log2_lo=2*sum(F(1,(2*j+1)*3**(2*j+1)) for j in range(20))
log2_hi=log2_lo+F(9,4*(41)*3**41)
assert F(277,100) <4*log2_lo<4*log2_hi<F(278,100)
base=envelope(F(1,2))
for x in breakpoints:
    slope=x-F(1,2)
    bound=4*log2_hi if slope>=0 else 4*log2_lo
    assert envelope(x)-base-slope*bound>=0

rows=[]
for n,t in windows:
    d=t-n;An,Ln=states[n];At,Lt=states[t]
    difference_num=At-An*(Lt//Ln)
    difference_den=Lt//gcd(difference_num,Lt)
    Dn=reduced_den(states[n]);Dt=reduced_den(states[t])
    fresh=old=exception=non_survival=0;exception_product=1
    selected=[]
    for p in primes_to(8*t):
        if p<=5 or p*p<=8*t:continue
        progression=1 if p%4==1 else 3
        is_fresh=(8*n<p<=8*t-7) if progression==1 else (4*n<p<=4*t-1)
        if is_fresh:
            assert Dn%p!=0
            if Dt%p==0:
                assert difference_den%p==0;fresh+=1
            else:non_survival+=1
        memberships=[]
        for a,b in bands(progression, int(3/F(d,n))+10):
            if 8*t<b*p and a*p+7<=8*n:
                memberships.append((a,b))
        assert len(memberships)<=1
        if not memberships:continue
        assert not is_fresh
        a,b=memberships[0]
        raw_events=[j for j in range(1,t+1)
                    if any((8*j-c)%p==0 for c in (7,4,3,2))]
        assert raw_events and raw_events[-1]<=n
        assert any((a*p+c)%8==0 and (a*p+c)//8<=n for c in (7,4,3,2))
        if Dn%p:
            non_survival+=1;continue
        if pow(16,d,p)==1:
            assert difference_den%p!=0
            exception+=1;exception_product*=p
        else:
            assert difference_den%p==0;old+=1
        selected.append(p)
    assert (16**d-1)%exception_product==0
    rows.append({'n':n,'t':t,'fresh_survivors':fresh,'old_survivors':old,
                 'excluded_divisors':exception,'finite_source_cancellations':non_survival,
                 'distinct_selected_old_primes':len(selected)})
print(json.dumps({'passport_checks':passport_checks,'ratio_checks':len(ratios),
                  'exact_convex_breakpoint_checks':len(breakpoints),'windows':rows},indent=2))
