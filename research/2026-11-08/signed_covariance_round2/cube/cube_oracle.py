"""Exact algebra oracles for local-source Gowers cubes.

No floating point, numerical BK exponent, or claim of asymptotic certification.
The two root-of-unity identities are compared before evaluation, as integer
coefficient histograms. Rational complex checks use independent finite arrays.
"""
from collections import Counter
from fractions import Fraction
from hashlib import sha256
from itertools import combinations, product
from math import isqrt, prod
from pathlib import Path
import argparse
import json

Q = Fraction
ZERO = (Q(0), Q(0))
ONE = (Q(1), Q(0))


def add(z, w):
    return z[0] + w[0], z[1] + w[1]


def conj(z):
    return z[0], -z[1]


def mul(z, w):
    return z[0]*w[0]-z[1]*w[1], z[0]*w[1]+z[1]*w[0]


def avg(values):
    values = list(values)
    if not values:
        raise ValueError("a finite average needs a nonempty domain")
    return (sum(z[0] for z in values)/len(values),
            sum(z[1] for z in values)/len(values))


def abs2(z):
    return z[0]*z[0]+z[1]*z[1]


def is_prime(p):
    return isinstance(p, int) and p >= 2 and all(p % q for q in range(2, isqrt(p)+1))


def clock(p):
    if not is_prime(p) or p == 2:
        raise ValueError("an odd prime is required")
    residues = [1]
    x = 16 % p
    while x != 1:
        residues.append(x)
        x = (16*x) % p
    return tuple(residues)


def vertices(shifts, m):
    """Enumerate literal cube vertices and their alternating signs."""
    d = len(shifts)
    return [(sum(shifts[j] for j in range(d) if (mask >> j) & 1) % m,
             -1 if mask.bit_count() % 2 else 1)
            for mask in range(1 << d)]


def direct_histogram(p, xi, depth, unsigned=False):
    """Enumerate every cube, summing its literal signed vertices."""
    if depth < 1:
        raise ValueError("positive cube depth required")
    gpow = clock(p)
    m = len(gpow)
    hist = Counter()
    for shifts in product(range(m), repeat=depth):
        corners = vertices(shifts, m)
        for r in range(m):
            exponent = sum((1 if unsigned else sign)*gpow[(r+off) % m]
                           for off, sign in corners)
            hist[(xi*exponent) % p] += 1
    return hist


def squared_sum_histogram(p, xi, depth):
    """Independently expand squared subgroup sums after the last shift."""
    if depth < 1:
        raise ValueError("positive cube depth required")
    gpow = clock(p)
    m = len(gpow)
    hist = Counter()
    degenerate = 0
    for shifts in product(range(m), repeat=depth-1):
        c = (xi*prod(1-pow(16, shift, p) for shift in shifts)) % p
        if c == 0:
            degenerate += 1
        for x in gpow:
            for y in gpow:
                hist[(c*(x-y)) % p] += 1
    return hist, degenerate


def fourth_moment_histogram(p, xi):
    """Fourier orthogonality: enumerate three free indices, then solve the fourth."""
    gpow = clock(p)
    m = len(gpow)
    histogram = Counter()
    for r1 in range(m):
        for r2 in range(m):
            for r3 in range(m):
                r4 = (r1-r2+r3) % m
                exponent = xi*(gpow[r1]-gpow[r2]+gpow[r3]-gpow[r4])
                histogram[exponent % p] += 1
    return histogram


def dft4(values):
    if len(values) != 4:
        raise ValueError("this independent exact Fourier oracle is a four-cycle")
    roots = (ONE, (Q(0), Q(1)), (Q(-1), Q(0)), (Q(0), Q(-1)))
    return [avg(mul(z, roots[(-k*r) % 4]) for r, z in enumerate(values))
            for k in range(4)]


def fourth_moment_checks():
    records = []
    instances = 0
    for split, ps, xis in (("development", (17, 41, 73, 89, 97, 113), (1, 2)),
                          ("holdout", (137, 193, 241), (3, 5))):
        for p in ps:
            for xi in xis:
                fourth = fourth_moment_histogram(p, xi)
                cube = direct_histogram(p, xi, 2)
                assert fourth == cube
                m = len(clock(p))
                instances += m**3
                records.append({"split": split, "p": p, "m": m, "xi": xi,
                                "free_fourier_index_triples": m**3,
                                "histogram": [fourth[k] for k in range(p)]})
    arrays = ((ONE, ONE, ONE, (Q(-1), Q(0))),
              (ONE, (Q(0), Q(1)), (Q(-1), Q(0)), (Q(0), Q(-1))),
              (ONE, (Q(3, 5), Q(4, 5)), (Q(1, 2), Q(0)), ZERO))
    subsets = 0
    flat_equalities = 0
    for array_id, values in enumerate(arrays):
        energies = [abs2(z) for z in dft4(values)]
        fourth_sum = sum(t*t for t in energies)
        assert cube_average([values]*4, 2) == (fourth_sum, Q(0))
        for s in range(5):
            for support in combinations(range(4), s):
                energy = sum(energies[k] for k in support)
                assert energy*energy <= s*fourth_sum
                if array_id == 0:
                    # The all-four-modes bound is sharp on its complete flat spectrum.
                    if s == 4:
                        assert energy*energy == s*fourth_sum
                        flat_equalities += 1
                    assert energies == [Q(1, 4)]*4
                subsets += 1
    return {"cases": len(records), "free_fourier_index_triples": instances,
            "records": records, "exact_support_checks": subsets,
            "flat_full_support_equalities": flat_equalities}


def forcing(n, first_coefficient=4):
    return (Q(first_coefficient, 8*n-7)-Q(2, 8*n-4)
            -Q(1, 8*n-3)-Q(1, 8*n-2))


def unwrapped_history(N, seed=Q(0), first_coefficient=4):
    states = [Q(seed)]
    for n in range(1, N+1):
        states.append(16*states[-1]+forcing(n, first_coefficient))
    return states


def principal_part(value, p):
    denominator = value.denominator
    power = 1
    while denominator % p == 0:
        denominator //= p
        power *= p
    if power == 1:
        return Q(0)
    return Q((value.numerator*pow(denominator, -1, power)) % power, power)


def authentic(states):
    return bool(states) and states[0] == 0 and all(
        states[n] == 16*states[n-1]+forcing(n) for n in range(1, len(states)))


def source_checks():
    records = []
    checks = 0
    for p in (41, 73, 97, 137, 193, 241):
        L = (p-1)//4
        birth = (p+7)//8
        states = unwrapped_history(2*L)
        assert authentic(states)
        assert not authentic(unwrapped_history(2*L, Q(1, p)))
        assert not authentic(unwrapped_history(2*L, first_coefficient=5))
        first = []
        for n in range(L+1, 2*L+1):
            actual = principal_part(states[n], p)
            expected = Q((4*pow(16, n-birth, p)) % p, p)
            assert actual == expected
            first.append(actual.numerator)
            checks += 1
        payload = [f"{v.numerator}/{v.denominator}" for v in states]
        records.append({"p": p, "L": L, "m": len(clock(p)),
                        "clean_principal_numerators": first,
                        "unwrapped_history_sha256": sha256(
                            json.dumps(payload, separators=(",", ":")).encode()).hexdigest()})
        checks += 3
    return {"checks": checks, "records": records}


def cube_average(functions, depth):
    """Literal multilinear alternating cube average on one cyclic group."""
    if depth < 1 or len(functions) != 1 << depth:
        raise ValueError("one function for each cube vertex is required")
    m = len(functions[0])
    if not m or any(len(f) != m for f in functions):
        raise ValueError("all functions need the same nonempty cyclic domain")
    values = []
    for r in range(m):
        for shifts in product(range(m), repeat=depth):
            z = ONE
            for mask, (off, sign) in enumerate(vertices(shifts, m)):
                value = functions[mask][(r+off) % m]
                z = mul(z, value if sign == 1 else conj(value))
            values.append(z)
    return avg(values)


def cube_atom(functions, depth):
    """Compute the nonzero-corner atom without reading vertex zero."""
    if depth < 2 or len(functions) != (1 << depth)-1:
        raise ValueError("one bounded function per nonzero corner is required")
    m = len(functions[0])
    if not m or any(len(f) != m for f in functions):
        raise ValueError("all atom functions need the same nonempty domain")
    if any(abs2(z) > 1 for f in functions for z in f):
        raise ValueError("cube atom factors must be one-bounded")
    out = []
    for r in range(m):
        values = []
        for shifts in product(range(m), repeat=depth):
            z = ONE
            for mask in range(1, 1 << depth):
                index = (r+sum(shifts[j] for j in range(depth)
                               if (mask >> j) & 1)) % m
                factor = functions[mask-1][index]
                z = mul(z, conj(factor) if mask.bit_count() % 2 else factor)
            values.append(z)
        out.append(avg(values))
    return out


def rational_cube_checks():
    bank = (ONE, (Q(0), Q(1)), (Q(-1), Q(0)), (Q(0), Q(-1)),
            (Q(3, 5), Q(4, 5)), (Q(4, 5), Q(-3, 5)), (Q(1, 2), Q(0)), ZERO)
    records = []
    for m in (2, 3, 4):
        for d in (2, 3):
            for seed in range(4):
                fs = [[bank[(r*r+3*w+seed*r+w*r) % len(bank)] for r in range(m)]
                      for w in range(1 << d)]
                lam = cube_average(fs, d)
                qs = [cube_average([f]*(1 << d), d) for f in fs]
                assert all(q[1] == 0 and 0 <= q[0] <= 1 for q in qs)
                lhs = abs2(lam)**(1 << (d-1))
                assert lhs <= prod(q[0] for q in qs)
                atom = cube_atom(fs[1:], d)
                atom_pairing = avg(mul(x, y) for x, y in zip(fs[0], atom))
                assert atom_pairing == lam
                assert lhs <= qs[0][0]
                records.append({"m": m, "d": d, "seed": seed,
                                "pairing": [str(v) for v in lam],
                                "Q_first": str(qs[0][0]),
                                "gcs_rhs_power": str(prod(q[0] for q in qs)),
                                "lhs_power": str(lhs)})
    # Resonant complement and genuine cyclic linear phase: all values rational complex.
    a = [ONE, (Q(0), Q(1)), (Q(-1), Q(0)), (Q(0), Q(-1))]
    assert avg(mul(z, conj(z)) for z in a) == ONE
    assert cube_atom([a]*3, 2) == [conj(z) for z in a]
    return {"cases": len(records), "records": records,
            "resonant_pairing": "1", "cyclic_phase_atom_exact": True}


def run():
    records = []
    enumerated_cubes = 0
    degenerate_checks = 0
    groups = (("development", (17, 41, 73, 89, 97, 113), range(1, 5), (1, 2)),
              ("holdout", (137, 193, 241), range(1, 4), (3, 5)))
    for split, primes, depths, xis in groups:
        for p in primes:
            m = len(clock(p))
            for d in depths:
                for xi in xis:
                    literal = direct_histogram(p, xi, d)
                    squared, degeneracies = squared_sum_histogram(p, xi, d)
                    assert literal == squared, (p, xi, d)
                    assert degeneracies == m**(d-1)-(m-1)**(d-1)
                    assert sum(literal.values()) == m**(d+1)
                    assert all(literal[k] == literal[-k % p] for k in range(p))
                    histogram = [literal[k] for k in range(p)]
                    records.append({"split": split, "p": p, "m": m, "depth": d,
                                    "xi": xi, "degenerate_preceding_tuples": degeneracies,
                                    "cube_count": m**(d+1), "histogram": histogram})
                    enumerated_cubes += m**(d+1)
                    degenerate_checks += m**(d-1)
    # Negative cases are fixed in the protocol, not selected from a numerical fit.
    unsigned_differs = direct_histogram(41, 1, 2, unsigned=True) != direct_histogram(41, 1, 2)
    assert unsigned_differs
    zero_hist = direct_histogram(41, 0, 3)
    assert zero_hist == Counter({0: len(clock(41))**4})
    m = len(clock(73))
    full_period_coefficient = (1-pow(16, m, 73)) % 73
    assert full_period_coefficient == 0
    here = Path(__file__).resolve().parent
    hashes = {p.name: sha256(p.read_bytes()).hexdigest() for p in sorted(here.glob("*.py"))}
    return {"status": "all exact checks passed", "parent": "1990b05117d84b33094c8e0f53f7d19b60f48060",
            "code_sha256": hashes, "cube_cases": len(records),
            "literal_cube_instances": enumerated_cubes,
            "preceding_shift_instances": degenerate_checks,
            "cube_records": records, "source": source_checks(),
            "rational_multilinear": rational_cube_checks(),
            "fourth_moment": fourth_moment_checks(),
            "negative_controls": {"unsigned_cube_rejected": unsigned_differs,
                                  "zero_frequency_cube_is_one": True,
                                  "full_period_shift_erases_coefficient": full_period_coefficient == 0},
            "scope": "finite exact algebra and source checks; BK/PNT and asymptotic conclusions are paper proofs"}


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    payload = run()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True)+"\n")
    print(json.dumps({k: payload[k] for k in ("status", "cube_cases", "literal_cube_instances",
                                            "preceding_shift_instances")}, sort_keys=True))
