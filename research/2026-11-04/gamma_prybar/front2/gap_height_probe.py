"""Direct finite checks of the two-time conductor argument, using exact integers."""
from fractions import Fraction as F
from math import gcd, prod
import json

from checkpoint_probe import four, prime


def order_16(p):
    z, k = 16%p, 1
    while z != 1:
        z = (16*z)%p
        k += 1
    return k


def certify(t):
    u = [F(0)]
    for j in range(1,t+1):
        u.append(16*u[-1]+four(j))
    single = [p for p in range(7,8*t-6) if prime(p) and
              ((p%4==1 and 2*t<p) or (p%4==3 and 8*t<3*p and p<=4*t-1))]
    g = prod(single)
    den = [(u[t]-x).denominator for x in u[:t]]
    for n, q in enumerate(den):
        assert q%(g//gcd(g,16**(t-n)-1)) == 0
    retained = 0
    for p in range(max(7,t//8+1),8*t):
        if not prime(p) or p*p <= 8*t or u[t].denominator%p:
            continue
        retained += 1
        order = order_16(p)
        event_count = sum(any((8*j-c)%p==0 for c in (7,4,3,2)) for j in range(1,t+1))
        # Equality to the final nonzero p-primary residue is equivalent to
        # cancellation of p from the complete difference denominator.
        equal = sum(q%p != 0 for q in den)
        assert equal <= t//order+event_count+1
    return dict(t=t, pairs=t, single_hit_primes=len(single), checked_prime_clocks=retained,
                smallest_gap_denominator_bits=min(den).bit_length(),
                denominators_above_diagnostic=sum(q>2**(8*t) for q in den))


if __name__ == '__main__':
    print(json.dumps([certify(t) for t in (56,163,389,673)], indent=2))
