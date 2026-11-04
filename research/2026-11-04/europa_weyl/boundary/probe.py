"""Exact rational probes. Run python3 probe.py to regenerate RECEIPT.json on stdout."""
from fractions import Fraction as F
from math import factorial, gcd, isqrt, prod
import json

TAPS = (2, 2, 1, 0, F(-1, 2), F(-1, 2), F(-1, 4), 0)


def force(n):
    return sum(F(w, 8 * (n - 1) + j) for j, w in enumerate(TAPS, 1))


def states(limit):
    ys = [F(0)]
    for n in range(1, limit + 1):
        ys.append(16 * ys[-1] + force(n))
    return ys


def circle_distance(value):
    return abs(value - round(value))


def mod(value, p):
    return value.numerator * pow(value.denominator, -1, p) % p


def dyadic(value, bits=20):
    """Lower and upper enclosure numerators, denominator 2**bits."""
    x = value * 2**bits
    return [x.__floor__(), x.__ceil__()]


def primes(lo, hi):
    return [n for n in range(lo, hi + 1)
            if n > 1 and all(n % k for k in range(2, isqrt(n) + 1))]


def beta_term(n, j):
    return F(factorial(2 * j), 4 * prod(range(8*n + 1, 8*n + 2*j + 2)))


def geometric_checks(ys):
    rows = []
    for n in (9, 37, 113):
        future = F(ys[n + 19], 16**19) - ys[n]
        upper = future + F(1, 4 * (8*(n + 19) + 1) * 16**19)
        first, second, third = [beta_term(n, j) for j in range(3)]
        assert first - second < upper and first - second + third > future
        assert 4 * (first - second) > upper
        assert upper < first and future > first - second
        rows.append({"n": n, "measured_first_error_times_n_cubed_pow2_20":
                     [dyadic((first - upper) * n**3)[0],
                      dyadic((first - future) * n**3)[1]]})
    return rows


def aligned_checks(ys, probes, s):
    count = 0
    changed = 0
    for p in probes:
        chi = 1 if p % 4 == 1 else -1
        for k in range(1, min(5, (p-1)//8) + 1):
            y = ys[k*p] + 16**(k*p)*s
            u = ys[k] + 16**k*s
            assert mod(p * y, p) == mod(chi * ys[k], p)
            defect = mod(p*y - chi*u, p)
            assert defect == mod(-chi * 16**k * s, p)
            changed += bool(defect)
            count += 1
    return {"tests": count, "failed_aligned": changed}


def local_endpoint(n):
    term = beta_term(n, 0)
    total = term
    for j in range(1, 4*n):
        term *= F((2*j-1)*(2*j), (8*n + 2*j)*(8*n + 2*j + 1))
        total += (-1)**j * term
    return total


def epoch_row(a, ps, ys, old, online=False):
    b = 2*a - 1
    pp = prod(ps)
    if old:
        d = ys[a].denominator
        for p in ps:
            while d % p == 0:
                d //= p
    else:
        d = 2 * pp * 16**b * 8192 + 1
    if online:
        h = ys[a] + local_endpoint(a)
        lift = (h - F(1, 5)).__ceil__() + 1
        center = F(lift + F(1, 5) - h, 16**a)
    else:
        center = F(1, 5) - F(ys[b], 16**b)
    seed = F(pp * round(d * center / pp), d)
    assert gcd(pp, seed.denominator) == 1 and seed.numerator % pp == 0 and seed != 0
    assert not old or ys[a].denominator % seed.denominator == 0
    phases = [ys[n] + 16**n * seed for n in range(a, b + 1)]
    maximum = max(circle_distance(v - F(1, 5)) for v in phases)
    rounding = abs((seed - center) * 16**b)
    local_error = F(16**(b-a), 4*16**(4*a)) if online else 0
    assert maximum <= F(1, 4*(8*a + 1)) + rounding + local_error
    if online:
        assert 0 < seed < F(3, 16**a)
        assert maximum < F(1, 4*(8*a + 1)) + F(1, 8192)
    passed = maximum < F(1, 4*(8*a + 1)) + F(1, 8192)
    q = 64
    lower = q * max(F(0), 1 - 2*q*maximum)
    # All points near a common center and triangle inequality imply this lower bound.
    assert old or lower > F(3*q, 4)
    return {"A": a, "B": b, "old": old, "test_prime_count": len(ps),
            "maximum_radius_pow2_20": dyadic(maximum),
            "exact_bound_passed": passed, "J_lower_bound_pow2_20": dyadic(lower),
            "D_bits": d.bit_length(), "P_bits": pp.bit_length(),
            "seed_numerator": str(seed.numerator), "seed_denominator": str(seed.denominator)}


def phase_slips(ys):
    rows = []
    for h in (1, 3, 11):
        for m in (17, 29, 61):
            jump = next(n for n in range(m, 8*m + 1)
                        if circle_distance(h*(ys[n+1] - ys[n])) >= F(1, 64))
            rows.append({"m": m, "h": h, "first_n": jump, "jump_pow2_20":
                         dyadic(circle_distance(h*(ys[jump+1] - ys[jump])))})
    assert all(circle_distance((16**(n+1)-16**n) * F(1, 5)) == 0 for n in range(60))
    positions = [3**k for k in range(6)]
    sparse = sum(F(1, 16**m) for m in positions)
    sparse_displacement = sum(circle_distance(16**n * sparse) for n in range(243))
    assert sparse_displacement <= F(len(positions), 15)
    dense = sum(F(1, 16**m) for m in range(1, 244))
    assert sum(circle_distance(16**n * dense) for n in range(243)) > 1
    return rows


def main():
    ps = [11, 19, 29, 47, 73]
    ys = states(500)
    raw_wrong = aligned_checks(ys, ps, F(1, 5))
    assert raw_wrong["failed_aligned"] == raw_wrong["tests"]
    good = aligned_checks(ys, ps, F(prod(ps), 101))
    assert good["failed_aligned"] == 0
    result = {"angle_tail": geometric_checks(ys), "fixed_seed": raw_wrong,
              "product_seed": good, "finite_epoch": epoch_row(37, ps, ys, False),
              "old_conductor_epochs": [epoch_row(a, primes(9, a), ys, True)
                                       for a in (79, 107, 149)],
              "epoch_start_only": [epoch_row(a, primes(9, a), ys, True, online=True)
                                   for a in (83, 131, 167)],
              "angular_phase_slips": phase_slips(ys),
              "scope": "finite exact rational; dyadic enclosures use denominator 1048576"}
    print(json.dumps(result, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
