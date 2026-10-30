"""Independent exact arithmetic for the Stoneham-to-BBP transfer audit.

No parent research implementation is imported. Finite execution verifies the
listed instances; universal assertions are proved in TRANSFER_DOSSIER.md.
"""
from collections import Counter
from fractions import Fraction as F
from math import comb, gcd, isqrt, prod

OFFSETS = (1, 4, 5, 6)
BBP = (4, -2, -1, -1)


def primes_to(limit):
    return [p for p in range(2, limit + 1)
            if all(p % d for d in range(2, isqrt(p) + 1))]


def forcing(n, coefficients=BBP):
    if n < 1 or len(coefficients) != 4:
        raise ValueError("positive source time, four coefficients")
    return sum((F(c, 8 * (n - 1) + d)
                for c, d in zip(coefficients, OFFSETS)), F())


def bbp_orbit(last, coefficients=BBP, seed=F()):
    u = F(seed)
    result = [u]
    for n in range(1, last + 1):
        u = 16 * u + forcing(n, coefficients)
        result.append(u)
    return result


def direct_bbp(n, coefficients=BBP):
    """Independent summation order: pole first, then time, no recurrence."""
    return sum((F(c * 16 ** (n - j), 8 * (j - 1) + d)
                for c, d in zip(coefficients, OFFSETS)
                for j in range(1, n + 1)), F())


def valuation(value, p):
    value = F(value)
    if not value:
        return None
    num, den = abs(value.numerator), value.denominator
    result = 0
    while num % p == 0:
        num //= p
        result += 1
    while den % p == 0:
        den //= p
        result -= 1
    return result


def grid_witness_primes(n):
    """Two disjoint, uniformly safe first-pole windows; theorem domain n>=3."""
    if n < 3:
        raise ValueError("n>=3")
    plus, minus = [], []
    for p in primes_to(8 * n - 7):
        if p <= 5:
            continue
        if p % 4 == 1 and 2 * n + 2 < p <= 8 * n - 7:
            plus.append(p)
        if p % 4 == 3 and 8 * n + 8 < 3 * p and p <= 4 * n - 1:
            minus.append(p)
    return plus, minus


def first_pole_events(p, through):
    """Literal denominator enumeration, independently testing window geometry."""
    return [(j, d, (8 * (j - 1) + d) // p, c)
            for j in range(1, through + 1)
            for c, d in zip(BBP, OFFSETS)
            if (8 * (j - 1) + d) % p == 0]


def rational_mod(value, modulus):
    value = F(value)
    return value.numerator * pow(value.denominator, -1, modulus) % modulus


def primary(value, p):
    """Canonical p-primary projection Q/Z -> Z[1/p]/Z, arbitrary exponent."""
    value = F(value)
    power, complement = 1, value.denominator
    while complement % p == 0:
        power *= p
        complement //= p
    if power == 1:
        return F()
    return F(value.numerator * pow(complement, -1, power) % power, power)


def walsh(digit, mask):
    return (-1) ** ((digit & mask).bit_count())


def stage_residues(c, stage):
    """Exact circle pulse recurrence; retain all earlier impulses."""
    if c not in (3, 5) or stage < 1:
        raise ValueError("c=3 or5, stage>=1")
    start, stop = c ** stage, c ** (stage + 1)
    z, next_pulse = F(), c
    out = []
    for n in range(1, stop):
        z *= 16
        if n == next_pulse:
            z += F(1, n)
            next_pulse *= c
        z %= 1
        if n >= start:
            out.append(z)
    return out


def stage_residues_oracle(c, stage):
    """Direct modular sum, independent of pulse recurrence."""
    q = c ** stage
    return [F(sum(c ** (stage - k) * pow(16, n - c ** k, q)
                  for k in range(1, stage + 1)) % q, q)
            for n in range(q, c * q)]


def prime_power_character_remainder(residues, h, c, stage):
    """Exact polynomial residue modulo Phi_(c^stage), no complex floats."""
    q, r = c ** stage, c ** (stage - 1)
    coeff = [0] * q
    for x in residues:
        index = h * int(q * x) % q
        coeff[index] += 1
    degree = (c - 1) * r
    for i in range(q - 1, degree - 1, -1):
        a = coeff[i]
        if a:
            for j in range(c):
                coeff[i - degree + j * r] -= a
    return tuple(coeff[:degree])


def distance_to_arc(x, start, length):
    if not 0 <= length <= 1:
        raise ValueError("circle arc length in [0,1]")
    z = (x - start) % 1
    return F() if z <= length else min(z - length, 1 - z)


def stage_tail_bound(c, stage):
    return F(1, 16 * (c - 1) * c ** stage)


def stage_tail_partial(c, stage, n, extra=2):
    return sum((F(1, c ** k * 16 ** (c ** k - n))
                for k in range(stage + 1, stage + extra + 1)), F())


def stoneham_certified_upper(c, N, start, length):
    """Upper count for the infinite orbit from exact rational stage enclosures."""
    hits, stage = min(c, N), 1
    while c ** stage < N:
        q = c ** stage
        eps = stage_tail_bound(c, stage)
        for j, z in enumerate(stage_residues(c, stage)):
            if q + j >= N:
                break
            hits += distance_to_arc(z, start, length) <= eps
        stage += 1
    return hits


def stoneham_hotspot_bound(c, N, length):
    if N <= c:
        return F(N)
    stage = 0
    while c ** (stage + 1) < N:
        stage += 1
    return c * N * length + 3 * c * (c - 1) * stage + c


def sparse_two_pulses(K):
    return [(2 ** k + (k + 3) // 4, 2 ** (4 * ((k + 3) // 4) - k))
            for k in range(1, K + 1)]


def smallest_covering_arc(points):
    """Exact minimum circle-arc length over every translation."""
    vals = sorted({F(x) % 1 for x in points})
    if len(vals) <= 1:
        return F()
    gaps = [vals[j + 1] - vals[j] for j in range(len(vals) - 1)]
    gaps.append(1 + vals[0] - vals[-1])
    return 1 - max(gaps)


def approximate_grid_search(states, q_limit, radius):
    """Exhaustive q and exact all-translation test, no fitted phase."""
    if not states or q_limit < 1 or radius < 0:
        raise ValueError("nonempty states, positive q limit, nonnegative radius")
    feasible, best = [], None
    for q in range(1, q_limit + 1):
        arc = smallest_covering_arc([q * x for x in states])
        needed = arc / (2 * q)
        if best is None or needed < best[0]:
            best = needed, q
        if needed <= radius:
            feasible.append(q)
    return dict(feasible_q=feasible, minimum_radius=str(best[0]),
                minimum_radius_q=best[1], declared_radius=str(radius))


def digits(value, N):
    value %= 1
    out = []
    for _ in range(N):
        value *= 16
        digit = value.numerator // value.denominator
        out.append(digit)
        value -= digit
    return out


def positive_word_mass(n, failures, successes):
    """Whole retained-posterior mass before normalization, exact finite shifts."""
    return sum(((-1) ** j * comb(successes, j)
                * forcing(n + failures + j)
                for j in range(successes + 1)), F())


def debruijn_cycle(base=16, order=2):
    a, out = [0] * (base * order + 1), []

    def rec(t, period):
        if t > order:
            if order % period == 0:
                out.extend(a[1:period + 1])
            return
        a[t] = a[t - period]
        rec(t + 1, period)
        for digit in range(a[t - period] + 1, base):
            a[t] = digit
            rec(t + 1, t)

    rec(1, 1)
    return out


def receipt():
    orbit = bbp_orbit(258)
    grids = []
    for n in (7, 23, 64, 97, 127, 211, 257):
        plus, minus = grid_witness_primes(n)
        difference = orbit[n + 1] - orbit[n]
        product = prod(plus + minus)
        assert difference.denominator % product == 0
        grids.append(dict(n=n, plus=plus, minus=minus, product=str(product),
                          product_bits=product.bit_length(),
                          difference_numerator=str(difference.numerator),
                          difference_denominator=str(difference.denominator),
                          every_valuation_minus_one=all(
                              valuation(difference, p) == -1 for p in plus + minus)))
    stages = []
    for c, levels in ((3, (2, 3, 5)), (5, (2, 3, 4))):
        for level in levels:
            vals = stage_residues(c, level)
            count = Counter(vals)
            assert vals == stage_residues_oracle(c, level)
            assert set(count.values()) == {c * (c - 1)}
            stages.append(dict(c=c, stage=level, length=len(vals),
                               distinct=len(count), multiplicity=c * (c - 1),
                               character_h1_zero=not any(prime_power_character_remainder(
                                   vals, 1, c, level))))
    stale_transfer = []
    for c, level in ((3, 2), (3, 3), (5, 2)):
        q = c ** (level - 1)
        vals = [int(q * (orbit[n] % 1))
                for n in range(c ** level, c ** (level + 1))]
        counts = [vals.count(j) for j in range(q)]
        stale_transfer.append(dict(c=c, stage=level, bbp_bins=counts,
                                   stoneham_exact_multiplicity=c * (c - 1)))
    return dict(status="PASS", authority="finite exact checks, paper proofs separate",
                source="original four poles; U_0=0", grid_witnesses=grids,
                stoneham_stages=stages, rejected_naive_transfer=stale_transfer,
                sparse_two_pulses=sparse_two_pulses(10),
                pi_normality="OPEN", rh="OPEN")


def approximate_receipt():
    orbit = bbp_orbit(386)
    rows = []
    for n in (97, 127, 211, 257, 383):
        radius = F(1, (8 * n + 1) ** 2)
        row = approximate_grid_search(orbit[n:n + 4], n, radius)
        needed = F(row['minimum_radius'])
        rows.append(dict(n=n, length=4, q_limit=n,
                         minimum_over_tail_radius_floor=int(needed / radius),
                         exceeds_twice_tail_radius=needed > 2 * radius, **row))
    return dict(scope="Exact finite all-translations search; asymptotic approximate-grid question OPEN",
                source="zero-seeded original rational BBP; positive Green tail", rows=rows)


if __name__ == "__main__":
    import json
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--approximate', action='store_true')
    args = parser.parse_args()
    print(json.dumps(approximate_receipt() if args.approximate else receipt(), indent=2))
