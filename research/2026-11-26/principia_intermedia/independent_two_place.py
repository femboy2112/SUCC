"""Independent Fraction oracle for the BBP rational seam and place budgets."""
from fractions import Fraction as F
from random import Random
import json


def vp(x, p):
    if not x:
        raise ValueError("zero has no finite valuation")
    a, b = abs(x.numerator), x.denominator
    v = 0
    while a % p == 0:
        a //= p
        v += 1
    while b % p == 0:
        b //= p
        v -= 1
    return v


def residual(k, cuts, sign=1):
    # Integrate factored source interval by interval, not the four-pole primitive.
    z = F(0)
    ends = [F(0), *cuts, F(1)]
    for a, b in zip(ends, ends[1:]):
        for j, c in enumerate((4, 4, 4, 2, 1)):
            m = 8 * k + j + 1
            z += sign * c * ((b**m - a**m) / m - (b**(m+1) - a**(m+1)) / (m+1))
        sign = -sign
    return z


def scaled_mod(x, modulus):
    assert x.denominator % 2
    return x.numerator * pow(x.denominator, -1, modulus) % modulus


def test_mixed_partitions():
    rng = Random(20261126)
    counts = {"partitions": 0, "moment_checks": 0, "odd_depth_cases": 0,
              "even_depth_cases": 0, "single_even_moments": 0}
    for trial in range(360):
        size = 1 + trial % 6
        cuts = sorted({F(rng.randrange(1, b), b) for b in
                       [rng.randrange(2, 90) for _ in range(size + 3)]})[:size]
        sign = (-1)**trial
        e = max(0, max(-vp(t, 2) for t in cuts))
        counts["partitions"] += 1
        for k in range(7):
            z = residual(k, cuts, sign)
            counts["moment_checks"] += 1
            if not e:
                assert scaled_mod(z, 2) == (k + 1) % 2
                continue
            d = 8*k + 6
            a = [t * 2**e for t in cuts]
            deepest = sum(vp(t, 2) == -e for t in cuts)
            normalized = z * 2**(e*d)
            expected = -sign * sum(((-1)**i * t**d for i, t in enumerate(a)), F(0)) / (4*k + 3)
            mod = 2**(e+1)
            assert scaled_mod(normalized, mod) == scaled_mod(expected, mod)
            if deepest % 2:
                assert z and vp(z, 2) == -e*d
                counts["odd_depth_cases"] += 1
            else:
                counts["even_depth_cases"] += 1
    for B in range(2, 35):
        for a in range(1, B):
            t = F(a, B)
            for k in (0, 2, 4):
                z = residual(k, [t])
                assert z
                assert vp(z, 2) == min(0, vp(t, 2)) * (8*k + 6)
                counts["single_even_moments"] += 1
    return counts


def test_prime_grid():
    rows = []
    for p in (2, 3, 7, 11):
        for depth in range(1, 7):
            B = p**depth
            lo, hi = 0, B
            while hi-lo > 1:
                m = (lo+hi)//2
                if residual(0, [F(m,B)]) < 0:
                    lo = m
                else:
                    hi = m
            a = min((a for a in (lo,hi) if 0 < a < B),
                    key=lambda a: abs(residual(0, [F(a,B)])))
            t = F(a,B)
            z = residual(0,[t])
            polynomial = (120*t - 15*t**4 - 6*t**5 - 5*t**6 - 47)/15
            assert z == polynomial and 0 < abs(z) <= F(8,B)
            e = -vp(t,p)
            assert e > 0
            assert vp(z,p) == -6*e - (1 if p == 3 else 0)
            if p != 2:
                assert vp(z,2) == 0
            # Check denominator support, not full numerator factorization.
            denominator = z.denominator
            for ell in {3,5,p}:
                while denominator % ell == 0:
                    denominator //= ell
            assert denominator == 1
            # Denominator support bounds growth in the other places.
            if p == 3:
                assert F(3)**(-vp(z,3)) >= B/F(40)
            rows.append({"prime":p,"grid_depth":depth,"reduced_depth":e,
                         "cut":str(t),"residual":str(z),"vp":vp(z,p)})
    return rows


if __name__ == "__main__":
    print(json.dumps({"mixed":test_mixed_partitions(),"prime_grids":test_prime_grid()}, indent=2))
