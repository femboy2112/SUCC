"""Independent Gaussian-rational and literal-source checks for H1--H6.

No floating point or imported phase implementation enters this oracle.
Finite algebra checks do not establish the open signed asymptotic gate.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as Q
from hashlib import sha256
from itertools import product
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ZERO = (0, 0)
UNITS = ((1, 0), (0, 1), (-1, 0), (0, -1))


def add(x, y):
    return x[0] + y[0], x[1] + y[1]


def mul(x, y):
    return x[0]*y[0]-x[1]*y[1], x[0]*y[1]+x[1]*y[0]


def conj(x):
    return x[0], -x[1]


def norm2(x):
    return x[0]*x[0]+x[1]*x[1]


def gsum(values):
    total = ZERO
    for value in values:
        total = add(total, value)
    return total


def direct_energy(values, aperture):
    """Sum literal moving-block squares, including both endpoint fringes."""
    if not values or type(aperture) is not int or aperture < 1:
        raise ValueError("nonempty sequence and positive integer aperture required")
    length = len(values)
    total = 0
    for start in range(1-aperture, length):
        block = gsum(values[j] for j in range(max(0, start), min(length, start+aperture)))
        total += norm2(block)
    return Q(total, length*aperture*aperture)


def correlation(values, lag):
    total = gsum(mul(values[j+lag], conj(values[j]))
                 for j in range(max(0, len(values)-lag)))
    return Q(total[0], len(values)), Q(total[1], len(values))


def pair_energy(values, aperture, absolute=False):
    diagonal = Q(sum(norm2(value) for value in values), len(values)*aperture)
    total = diagonal
    for lag in range(1, aperture):
        real = correlation(values, lag)[0]
        total += Q(2*(aperture-lag), aperture*aperture) * (abs(real) if absolute else real)
    return total


def sqrt_le_sqrt_plus(x, y, t):
    """Check sqrt(x) <= sqrt(y)+t by exact rational arithmetic."""
    if min(x, y, t) < 0:
        raise ValueError("nonnegative inputs required")
    residual = x-y-t*t
    return residual <= 0 or residual*residual <= 4*t*t*y


def forcing(n):
    if type(n) is not int or n < 1:
        raise ValueError("source time must be a positive integer")
    return Q(4, 8*n-7)-Q(2, 8*n-4)-Q(1, 8*n-3)-Q(1, 8*n-2)


def literal_history(last):
    values = [Q(0)]
    for n in range(1, last+1):
        values.append(16*values[-1]+forcing(n))
    return values


def source_sum(n, lag):
    # Separate power sum, not a call to the recurrence.
    return sum((16**(lag-j)*forcing(n+j) for j in range(1, lag+1)), Q(0))


def principal(value, prime):
    power = 1
    cofactor = value.denominator
    while cofactor % prime == 0:
        power *= prime
        cofactor //= prime
    if power == 1:
        return Q(0)
    residue = value.numerator*pow(cofactor, -1, power) % power
    return Q(residue, power)


def order16(prime):
    residue = 16 % prime
    order = 1
    while residue != 1:
        residue = residue*16 % prime
        order += 1
        if order >= prime:
            raise ValueError("invalid prime order fixture")
    return order


def run():
    counts = {"gaussian_sequences": 0, "block_pair_identities": 0,
              "finite_vdc_and_contraction": 0, "blocking_inequalities": 0,
              "source_lag_identities": 0, "source_bounds": 0,
              "exact_phase_factorizations": 0, "weight_identities": 0,
              "order_degeneracies": 0, "constant_controls": 0}
    for length in range(1, 6):
        for values in product(UNITS, repeat=length):
            counts["gaussian_sequences"] += 1
            energies = {h: direct_energy(values, h) for h in range(1, 9)}
            mean2 = Q(norm2(gsum(values)), length*length)
            for h, energy in energies.items():
                assert energy == pair_energy(values, h)
                counts["block_pair_identities"] += 1
                assert 0 <= energy <= 1
                assert mean2 <= Q(length+h-1, length)*energy
                counts["finite_vdc_and_contraction"] += 1
                for k in range(1, h+1):
                    remainder = h % k
                    # Slightly weaker than qK/H times sqrt(E_K), still exact.
                    assert sqrt_le_sqrt_plus(energy, energies[k], Q(remainder, h))
                    counts["blocking_inequalities"] += 1
    for values in ((ZERO, (Q(3,5), Q(4,5)), (Q(1,3), Q(-1,4))),
                   (ZERO, ZERO), ((Q(1,2), 0),)):
        q = Q(sum(norm2(x) for x in values), len(values))
        for h in range(1, 9):
            energy = direct_energy(values, h)
            assert energy == pair_energy(values, h)
            assert 0 <= energy <= q
            counts["block_pair_identities"] += 1
            counts["finite_vdc_and_contraction"] += 1

    lags = (1, 2, 3, 5)
    windows = (1, 2, 7, 19, 41)
    history = literal_history(2*max(windows)-1+max(lags))
    for n in range(2, len(history)):
        assert 0 < forcing(n) < Q(1, n*n)
        counts["source_bounds"] += 1
    for a in windows:
        for n in range(a, 2*a):
            for lag in lags:
                increment = source_sum(n, lag)
                difference = history[n+lag]-history[n]
                assert difference == (16**lag-1)*history[n]+increment
                assert 0 < increment < Q(16**lag-1, 15*(n+1)**2)
                counts["source_lag_identities"] += 1
                counts["source_bounds"] += 1
                for h in (1, 2, 5):
                    k = h*(16**lag-1)
                    for p in (17, 41):
                        local = principal(history[n], p)
                        left_phase = k*local
                        right_phase = k*(history[n]-local)+h*increment
                        assert left_phase+right_phase == h*difference
                        counts["exact_phase_factorizations"] += 1

    for h in range(1, 32):
        assert sum((Q(2*(h-l), h*h) for l in range(1, h)), Q()) == 1-Q(1,h)
        assert sum((Q(2*(h-l)*l, h*h) for l in range(1, h)), Q()) == Q(h*h-1,3*h)
        geometric = sum((h-l)*(16**l-1) for l in range(1,h))
        assert geometric == Q(16*(16**h-16*h+h-1),225)-Q(h*(h-1),2)
        counts["weight_identities"] += 3
    for p in (17, 41, 73, 89, 137):
        m = order16(p)
        assert all((16**lag-1) % p for lag in range(1,m))
        assert (16**m-1) % p == 0
        counts["order_degeneracies"] += 1
    for a in (1, 2, 7, 19, 41):
        for h in range(1, a+1):
            assert direct_energy(((1,0),)*a, h) == 1-Q(h*h-1,3*a*h)
            counts["constant_controls"] += 1
        for h in (a+1, 2*a, a*a):
            assert direct_energy(((1,0),)*a, h) == Q(a,h)-Q(a*a-1,3*h*h)
            counts["constant_controls"] += 1

    alternating = ((1,0),(-1,0))*16
    signed = pair_energy(alternating, 8)
    absolute = pair_energy(alternating, 8, absolute=True)
    assert signed == Q(1,256)
    assert absolute == Q(235,256)
    return {
        "status": "CERTIFIED-FINITE",
        "counts": counts,
        "checks_counted": sum(v for k,v in counts.items() if k != "gaussian_sequences"),
        "signed_control": {"length": 32, "aperture": 8,
                           "signed_energy": str(signed), "absolute_replacement": str(absolute)},
        "implementation": "independent literal four-pole Fraction recurrence; exact Gaussian rationals",
        "dependencies": {name: sha256((HERE/name).read_bytes()).hexdigest()
                         for name in ("PREREGISTRATION.md", "THEOREMS.md", "exact_oracle.py")},
        "pi_base16_normality": "OPEN", "RH": "OPEN",
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    receipt = run()
    args.output.write_text(json.dumps(receipt, indent=2, sort_keys=True)+"\n")
    print(json.dumps({"output": str(args.output), "checks": receipt["checks_counted"]}))
