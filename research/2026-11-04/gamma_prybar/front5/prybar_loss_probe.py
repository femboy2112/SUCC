"""Compare a p-orbit sieve with the actual reduced two-time difference."""
from fractions import Fraction as F
from math import gcd, isqrt
import json

from prybar_radial import mod_unit, prime, tap_sum


def gap_probe():
    u = v = F()
    frames = [[F()] for _ in range(3)]
    for n in range(1, 215):
        j = 8*n
        u = 16*u+F(4,j-7)-F(2,j-4)-F(1,j-3)-F(1,j-2)
        v = 16*v+F(8,j-6)+F(4,j-5)+F(4,j-4)-F(1,j-1)
        for frame,x in zip(frames,(u,(2*u+v)/4,(2*u-v)/4)):
            frame.append(x)

    rows = []
    for a in (31,61,107):
        t = 2*a-1
        large = [p for p in range(isqrt(16*a)+1,8*t+1) if prime(p)]
        checked = guards = 0
        for idx,frame in enumerate(frames):
            for p in large:
                # Independent modular recurrence at every possible pole slot
                # (outside [A,t] included to reconstruct the actual zero seed).
                b = 0
                history = [b]
                for j in range(1,t+1):
                    b = 16*b % p
                    x = 8*j
                    for l in range(1,9):
                        den = x-8+l
                        if den % p:
                            continue
                        coeff = (4,0,0,-2,-1,-1,0,0)[l-1]
                        sharp = (0,8,4,4,0,0,-1,0)[l-1]
                        w = (coeff,F(2*coeff+sharp,4),F(2*coeff-sharp,4))[idx]
                        b = (b + mod_unit(F(w,den//p),p)) % p
                    history.append(b)
                for n in range(a,t+1):
                    den = (frame[t]-frame[n]).denominator
                    lost = frame[t].denominator // gcd(frame[t].denominator,den)
                    assert (lost%p == 0) == (history[t] != 0 and history[t]==history[n])
                    checked += 1
                    if idx or n==t:
                        continue
                    split = p%4==1
                    fresh = (8*n<p<=8*t-7 if split else 4*n<p<=4*t-1)
                    carry = (2*t<p<=8*n-7 if split else 8*t<3*p and p<=4*n-1)
                    # Additional inherited bands from consecutive multipliers 6,9
                    # (split) and 4,7 (inert); all share the same order divisor.
                    second = ((8*t<9*p and 6*p<=8*n-7) if split
                              else (8*t<7*p and 4*p<=8*n-7))
                    carry = carry or second
                    if fresh or carry:
                        assert den%p == 0 or (carry and pow(16,t-n,p)==1)
                        guards += 1
        rows.append(dict(A=a,later=t,loss_checks=checked,pointwise_guards=guards))
    return rows

if __name__ == '__main__':
    print(json.dumps(gap_probe(),indent=2))
