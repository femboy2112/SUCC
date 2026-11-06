"""Arithmetic oracle for the silent-prime automorphism obstruction."""
from fractions import Fraction as F
from math import ceil, floor, gcd, lcm, prod
import hashlib
import json
from cofactor_probe import four_poles, primes_up_to, split_rational


def probe(A):
    L = A//4
    S = [p for p in primes_up_to(8*A-11) if p%8==5 and p>4*A]
    H = prod(S)
    Q = 1
    numerator = 0
    states = []
    x = F(0)
    for n in range(1,2*A):
        g = split_rational(n)
        q = lcm(Q,g.denominator)
        numerator = 16*numerator*(q//Q)+g.numerator*(q//g.denominator)
        Q = q
        x = 16*x+four_poles(n)
        assert numerator==Q*x
        if n>=A:
            states.append(x)
            assert gcd(H,g.denominator)==1
    assert Q%H==0 and gcd(H,Q//H)==1
    assert all(states[0].denominator%p==0 for p in S)
    # Rational center from source through A+L, computed by plain recurrence.
    center = H*((-states[L]/16**L)%1)
    radius = F(H,16*A*A*16**L)
    lo,hi = ceil(center-radius),floor(center+radius)
    report = {"A":A,"L":L,"S":S,"H_bits":H.bit_length(),
              "interval_size_bits":max(0,hi-lo+1).bit_length()}
    for z in range(lo,hi+1):
        delta = F(z,H)
        if (states[0]+delta).denominator!=states[0].denominator:
            continue
        b = z*pow(16**A,-1,H)%H
        seed = F(b,H)
        y = states[0]+16**A*seed
        # CRT multiplier w=1 mod Q/H and w X_A=Y_A mod H on common clock.
        X,Y=int(Q*states[0]),int(Q*y)
        u = Y*pow(X,-1,H)%H
        w = 1+(Q//H)*((u-1)*pow(Q//H,-1,H)%H)
        assert gcd(w,Q)==1
        mutants = []
        carry_digest = hashlib.sha256()
        for i,x in enumerate(states):
            g = four_poles(A+i)
            assert (w*g-g)%1==0
            assert (y-w*x)%1==0
            assert x.denominator==y.denominator
            mutants.append(y)
            g_next = four_poles(A+i+1)
            carry = floor(16*(y%1)+g_next)
            carry_digest.update(bytes([carry]))
            assert 16*(y%1)+g_next-carry==(16*y+g_next)%1
            y = 16*y+g_next
        assert (S[0]*w*states[0]).denominator != states[0].denominator
        for i in range(A-3):
            gap = 2*states[i]-3*states[i+2]+states[i+3]
            other = 2*mutants[i]-3*mutants[i+2]+mutants[i+3]
            assert gap.denominator==other.denominator and (w*gap-other)%1==0
        center_lifts = [(v+F(1,2))%1-F(1,2) for v in mutants[:L]]
        diam = max(center_lifts)-min(center_lifts)
        assert diam<F(1,32*A*A)
        return {**report,"success":True,"offset":z-lo,
                "floor_inverse_diameter":floor(1/diam),"common_multiplier_checked_states":A,
                "carry_sha256":carry_digest.hexdigest(),
                "seed_sha256":hashlib.sha256(str(seed).encode()).hexdigest()}
    return {**report,"success":False}


if __name__=="__main__":
    print(json.dumps([probe(A) for A in [89,197,401,647]],indent=2))
