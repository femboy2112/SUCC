"""Independent finite checks on the two complementary genuine BBP channels."""
from fractions import Fraction as Q
from math import isqrt
import json

ORIGINAL = (4, 0, 0, -2, -1, -1, 0, 0)
SECOND = (0, 8, 4, 4, 0, 0, -1, 0)
RADIAL = tuple(Q(2 * a - b, 4) for a, b in zip(ORIGINAL, SECOND))


def state_path(horizon):
    radial = [Q(0)]
    u = v = Q(0)
    for block in range(horizon):
        prefix = 16 * radial[-1]
        for j, weight in enumerate(RADIAL, 1):
            prefix += weight / (8 * block + j)
            assert prefix < 0 if j == 6 else prefix > 0
        radial.append(prefix)
        u = 16 * u + sum(Q(a, 8 * block + j) for j, a in enumerate(ORIGINAL, 1))
        v = 16 * v + sum(Q(b, 8 * block + j) for j, b in enumerate(SECOND, 1))
        assert prefix == (2 * u - v) / 4
        assert 0 < prefix < Q(1, 32 * (block + 1) + 16)
    return radial


def primes(bound):
    return [p for p in range(3, bound + 1, 2)
            if all(p % d for d in range(3, isqrt(p) + 1, 2))]


def residue(x, p):
    assert x.denominator % p
    return x.numerator * pow(x.denominator, -1, p) % p


def run():
    radial = state_path(166)
    horizons = []
    for n in (41, 79, 127):
        top = [p for p in primes(8*n) if p > 4*n]
        assert all(radial[n].denominator % p == 0 for p in top)
        horizons.append({"n": n, "surviving_top_primes": len(top),
                         "denominator_bits": radial[n].denominator.bit_length()})
    inert = []
    for p in (11, 19, 23, 31):
        lhs = residue(p * radial[p], p)
        rhs = residue(radial[1], p)
        assert lhs == rhs
        if rhs:
            assert lhs != (-rhs) % p
            inert.append(p)
    assert inert
    energies = []
    for a in (31, 47, 83):
        epoch = radial[a:2*a]
        signed_order = sorted(epoch)
        distance_sum = 2 * sum((2*i-a+1) * x for i, x in enumerate(signed_order))
        for q in (8, 16):
            # All distances < 1/q and < 1/2, verified independently by the max range.
            assert max(epoch) - min(epoch) < min(Q(1, q), Q(1, 2))
            exact = sum(max(Q(0), 1-q*abs(x-y)) for x in epoch for y in epoch) / a**2
            assert exact == 1 - Q(q, a*a) * distance_sum
            assert 1 - Q(q, 32*a+16) < exact < 1
            scale = 10**9
            energies.append({"a": a, "q": q, "floor_1e9_J_over_q": int(scale * exact)})
    return {"horizons": horizons, "sixth_negative_prefixes": len(radial)-1,
            "inert_primes_rejecting_angular_sign": inert, "energy": energies}


if __name__ == "__main__":
    print(json.dumps(run(), indent=2))
