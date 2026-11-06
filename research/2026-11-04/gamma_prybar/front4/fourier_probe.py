"""Replay the preregistered rational transport and interval character checks."""
from fractions import Fraction as F
from functools import lru_cache
from itertools import combinations
import json
from mpmath import iv

iv.dps = 35


@lru_cache(maxsize=None)
def source(n):
    return 4*F(1, 8*n-7) - 2*F(1, 8*n-4) - F(1, 8*n-3) - F(1, 8*n-2)


def orbit(end, seed):
    values = [seed]
    for n in range(1, end+1):
        values.append(16*values[-1] + source(n))
    return values


def point_character(x):
    x %= 1
    angle = (2*iv.pi*x.numerator)/x.denominator
    return iv.mpc(iv.cos(angle), iv.sin(angle))


def outward_millionths(x):
    # endpoints first converted outward to integer millionths
    # iv endpoints have substantially greater precision than this report.
    scaled = x*1000000
    import math
    return [math.floor(float(scaled.a))-1, math.ceil(float(scaled.b))+1]


def run_epoch(A, h):
    available = [0]
    j = 1
    while h*16**j <= A**3:
        if h*16**j >= A**2:
            available.append(j)
        j += 1
    zero = orbit(2*A, F(0))
    moved = orbit(2*A, F(1,7))
    aligned = 0
    blocks = {}
    means = {}
    for j in available:
        blocks[j] = []
        for m in range(A, 2*A+1):
            b = sum((16**ell)*source(m-ell) for ell in range(j))
            for values in (zero, moved):
                assert values[m] - b == 16**j*values[m-j]
                aligned += 1
            blocks[j].append(b)
        means[j] = sum(point_character(h*16**j*x) for x in zero[A:2*A])/A
    min_pair_checks = 0
    for j,k in combinations(available, 2):
        d = [h*(v-u) for u,v in zip(blocks[j], blocks[k])]
        increments = [u-v for u,v in zip(d,d[1:])]
        bound = F(h*16**k, 8192*A**3)
        assert all(0 < bound <= v < F(1,2) for v in increments)
        assert all(u>v for u,v in zip(increments,increments[1:]))
        assert F(0) < bound  # zero forcing has zero increments and fails
        min_pair_checks += len(increments)
    return dict(epoch=A, h=h, depths=available, exact_alignments=aligned,
                increments_checked=min_pair_checks,
                normalized_energy_millionths=outward_millionths(
                    sum(abs(v)**2 for v in means.values())),
                modulus_millionths={j:outward_millionths(abs(v)) for j,v in means.items()})


if __name__ == '__main__':
    print(json.dumps([run_epoch(A,h) for A in (73,149,281) for h in (1,3)],
                     sort_keys=True, indent=2))
