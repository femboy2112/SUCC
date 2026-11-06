"""Verify finite pair-height control witnesses by one-prime event streams."""
from collections import defaultdict
from fractions import Fraction as F
from math import gcd
import json

from checkpoint_probe import certify, four, prime


def pulses(p, horizon):
    residue = 0
    cell = 0
    out = [(cell, residue)]
    for i in range(1,horizon+1):
        residue = residue*16%p
        for offset, weight in ((7,4),(4,-2),(3,-1),(2,-1)):
            den = 8*i-offset
            if den%p == 0:
                cell += 1
                residue = (residue+weight*pow(den//p,-1,p))%p
        out.append((cell, residue))
    return out


def rectangle_check(p):
    end = min(5*p,(p*p-1)//8)
    stream = pulses(p,end)
    grouped = defaultdict(set)
    for t, (ct, rt) in enumerate(stream):
        for n, (cn, rn) in enumerate(stream[:t]):
            if rt and rt == rn:
                grouped[cn,ct].add(t-n)
    checks = 0
    for lags in grouped.values():
        seen = list(lags)
        for d in seen[1:]:
            assert pow(16,abs(d-seen[0]),p)==1
            checks += 1
    return dict(p=p,end=end,distinct_lag_checks=checks)


def height_check(a):
    captured = {}
    certify(a, witness=captured)
    q, seed = captured['clock'], captured['seed']
    losses = defaultdict(lambda: 1)
    worst_count = defaultdict(int)
    for p in range(2*a+1,8*a-7,2):
        if q%p or not prime(p):
            continue
        old = pulses(p,2*a-1)
        seen = defaultdict(list)
        shift = seed.numerator*pow(seed.denominator//p,-1,p)%p if seed.denominator%p==0 else 0
        shift = shift*pow(16,a,p)%p
        for i in range(a,2*a):
            original = old[i][1]
            cooked = (original+shift)%p
            for t, previous in seen[cooked]:
                if original != previous:
                    losses[t,i] *= p
                    worst_count[t,i] += 1
            seen[cooked].append((i,original))
            shift=shift*16%p
    original = F(0)
    selected = {}
    for i in range(1,a+24):
        original=16*original+four(i)
        if i>=a:
            selected[i] = original
    for i in range(12):
        m,n = a+i,a+2*i+1
        den=(selected[n]-selected[m]).denominator
        changed=(selected[n]-selected[m]+(16**n-16**m)*seed).denominator
        assert den//gcd(den,changed)==losses.get((m,n),1)
    return dict(A=a, unordered_pairs=a*(a-1)//2,
                pairs_losing_some_native_factor=len(losses),
                max_distinct_lost=max(worst_count.values(),default=0),
                maximum_lost_product=str(max(losses.values(),default=1)))


if __name__ == '__main__':
    print(json.dumps(dict(rectangles=[rectangle_check(p) for p in (17,31,73,127,257)],
                          height=[height_check(a) for a in (251,509,1024)]),indent=2))
