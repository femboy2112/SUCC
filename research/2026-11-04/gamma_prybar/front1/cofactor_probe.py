"""Exact counterseed on a fiber with fixed reduced denominators. Standard library."""
import argparse
import hashlib
import json
from fractions import Fraction as F
from math import ceil, floor, isqrt, lcm, prod


def four_poles(n):
    return 4*F(1,8*n-7)-2*F(1,8*n-4)-F(1,8*n-3)-F(1,8*n-2)


def split_rational(n):
    return F(120*n*n-89*n+16, (2*n-1)*(4*n-1)*(8*n-7)*(8*n-3))


def primes_up_to(n):
    sieve = [True]*(n+1)
    sieve[:2] = [False, False]
    for p in range(2,isqrt(n)+1):
        if sieve[p]:
            sieve[p*p:n+1:p] = [False]*((n-p*p)//p+1)
    return [i for i in range(2,n+1) if sieve[i]]


def pulse_prefixes():
    """Normalize by 16^(-j) at each pole 8j-b=mp. See paper."""
    res = {}
    weights = {7:4, 4:-2, 3:-1, 2:-1}
    for a in [1,3,5,7]:
        c = F()
        pulses = []
        chi = 1 if a in [1,7] else -1
        for m in range(1,257):
            b = (-m*a)%8
            if b in weights:
                c += F(weights[b]*chi**m, m*2**((m+b)//2))
                assert c != 0
                pulses.append(c)
        res[a] = {"nonzero_prefixes":len(pulses),
                  "sha256":hashlib.sha256(repr(pulses).encode()).hexdigest()}
    return res


def epoch(A):
    states, clocks = [F(0)], [1]
    full_num = 0
    for n in range(1,2*A+1):
        forcing = four_poles(n)
        u = 16*states[-1]+forcing
        g = split_rational(n)
        Q = lcm(clocks[-1],g.denominator)
        full_num = 16*full_num*(Q//clocks[-1])+g.numerator*(Q//g.denominator)
        assert full_num==u*Q
        states.append(u)
        clocks.append(Q)
    U = states[A:2*A]
    band = [p for p in primes_up_to(3*A) if 16*p>A and p>5]
    # At finite A exclude exceptions that fail the asymptotic hypotheses.
    H = prod(p for p in band if p*p>16*A and all(x.denominator%p==0 for x in U))
    assert clocks[A]%H==0
    excepted = [p for p in band if H%p]
    # Set z/H + 16^A alpha_(2A) approximately integral.
    center = H*((-states[-1]/16**A)%1)
    radius = F(H,16*A*A*16**A)
    lo, hi = ceil(center-radius),floor(center+radius)
    baseline = {"A":A, "band_size":len(band), "H_bits":H.bit_length(),
                "excepted":excepted, "candidate_bits":max(0,hi-lo+1).bit_length()}
    # z and b label the same grid but at A and zero respectively.
    forbidden = {}
    if lo<=hi:
        for p in band:
            if H%p:
                continue
            # The normalized primary (at epoch entry) is constant between p-events.
            c = U[0].numerator*pow(U[0].denominator//p,-1,p)%p
            bad = {-(H//p)*c%p}
            for m in range(1, 16*A//p+1):
                t = m*p
                for pole,w in ((7,4),(4,-2),(3,-1),(2,-1)):
                    j,rem = divmod(t+pole,8)
                    if rem==0 and A<j<2*A:
                        c = (c+w*pow(m,-1,p)*pow(16,A-j,p))%p
                        bad.add(-(H//p)*c%p)
            forbidden[p] = bad
    for z in range(lo,hi+1):
        if any(z%p in bad for p,bad in forbidden.items()):
            continue
        b = z*pow(16**A,-1,H)%H
        seed = F(b,H)
        changed = 16**A*seed+U[0]
        previous = 16**(A-1)*seed+states[A-1]
        centered = []
        for i,x in enumerate(U):
            if changed.denominator!=x.denominator:
                break
            assert changed==16*previous+four_poles(A+i)
            carry = floor(16*(previous%1)+four_poles(A+i))
            assert changed%1 == 16*(previous%1)+four_poles(A+i)-carry
            assert (clocks[A+i]*(changed-x))%(clocks[A+i]//H)==0
            centered.append((changed+F(1,2))%1-F(1,2))
            previous,changed = changed,16*changed+four_poles(A+i+1)
        else:
            diam = max(centered)-min(centered)
            assert diam<F(1,32*A*A)
            return {**baseline, "success":True, "denominators_matched":len(U),
                    "offset_in_interval":z-lo,
                    "seed_sha256":hashlib.sha256(str(seed).encode()).hexdigest(),
                    "floor_inverse_diameter":floor(1/diam)}
    return {**baseline,"success":False}


if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("epochs",nargs="*",type=int,default=[192,384,768,127,251])
    args=parser.parse_args()
    print(json.dumps({"pulse_check":pulse_prefixes(),"epochs":[epoch(n) for n in args.epochs]},indent=2))
