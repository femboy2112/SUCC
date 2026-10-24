#!/usr/bin/env python3
"""Independent exact group-algebra oracle for BBP mixed-source fiber moments.

This script independently constructs the authentic forced trajectory from the
common BBP forcing. It does not import cyclotomic_selected_source, evaluate
complex exponentials, read pi digits, or enumerate the exponentially large
dyadic origin grid. Equality is checked as exact rational phase-coefficient
maps, a stronger finite certificate than floating agreement of evaluations.

For Delta=B*L, the coefficient of e(h*16^n*delta) in I_p(h;delta) is
  u_s*v_(bL+s)/Delta                    at n=m+1+bL+s, s>0,
  (u_0-L*mu)*v_(bL)/Delta               at n=m+1+bL.
The maps retain the full source phases and all signed coefficients.
"""

from collections import defaultdict
from fractions import Fraction as Q
from hashlib import sha256
import json
from math import isqrt
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from observational_succ.bbp_source_memory import forcing


def _add(poly, phase, coefficient):
    """Add coefficient*e(phase), reducing only the rational phase modulo one."""
    phase %= 1
    poly[phase] += coefficient
    if not poly[phase]:
        del poly[phase]


def _product(left, right):
    result = defaultdict(Q)
    for x, a in left.items():
        for y, b in right.items():
            _add(result, x+y, a*b)
    return result


def _norm_square(poly):
    result = defaultdict(Q)
    for x, a in poly.items():
        for y, b in poly.items():
            _add(result, x-y, a*b)
    return result


def _map_record(poly):
    entries = [[str(x), str(a)] for x, a in sorted(poly.items())]
    encoded = json.dumps(entries, separators=(",", ":")).encode()
    return {"phase_terms": len(entries), "phase_coefficients": entries,
            "sha256": sha256(encoded).hexdigest()}


def _source(p):
    if p < 3 or p % 8 != 1 or any(p % d == 0 for d in range(2, isqrt(p)+1)):
        raise ValueError("prime p=1 mod8 required")
    m = (p-1)//8
    L, residue = 1, 16 % p
    while residue != 1:
        residue = residue*16 % p
        L += 1
    assert m % L == 0
    values, state = [Q()], Q()
    for n in range(1, 4*m+1):
        state = (16*state+forcing(n)) % 1
        values.append(state)
    local = [Q((4*pow(16, t, p)) % p, p) for t in range(3*m)]
    complement = [(values[m+1+t]-local[t]) % 1 for t in range(3*m)]
    assert all(x.denominator % p for x in complement)
    for t in range(3*m-1):
        assert complement[t+1] == (16*complement[t]+forcing(m+2+t)) % 1
    return m, L, values, local, complement


def _case(p, h, fourth):
    m, L, values, local, complement = _source(p)
    Delta, B = 3*m, 3*m//L
    v2, odd = 0, abs(h)
    if odd == 0:
        raise ValueError("nonzero harmonic required")
    while odd % 2 == 0:
        odd //= 2
        v2 += 1
    K = 4*m+v2//4+1
    modulus = 16**K

    # Nonzero/distinct temporal characters and nonaliasing unordered pair sums.
    frequencies = [h*16**n for n in range(m+1, 4*m+1)]
    assert all(f % modulus for f in frequencies)
    assert len({f % modulus for f in frequencies}) == Delta
    pairs = {frequencies[j]+frequencies[k]
             for j in range(Delta) for k in range(j, Delta)}
    assert len(pairs) == Delta*(Delta+1)//2
    assert len({f % modulus for f in pairs}) == len(pairs)

    # Direct I = full normalized window minus its block-anchored term.
    coefficients = {}
    for t in range(Delta):
        n, nb = m+1+t, m+1+(t//L)*L
        frequency, anchor_frequency = h*16**n % modulus, h*16**nb % modulus
        direct = coefficients.setdefault(frequency, defaultdict(Q))
        _add(direct, h*values[n], Q(1, Delta))
        anchor = coefficients.setdefault(anchor_frequency, defaultdict(Q))
        _add(anchor, h*(local[t % L]+complement[(t//L)*L]), -Q(1, Delta))

    # Independently verify the displayed block-start/non-start coefficient law.
    for t in range(Delta):
        b, s = divmod(t, L)
        expected_coefficient = defaultdict(Q)
        if s:
            _add(expected_coefficient, h*(local[s]+complement[t]), Q(1, Delta))
        else:
            _add(expected_coefficient, h*(local[0]+complement[t]), Q(1, Delta))
            for r in range(L):
                _add(expected_coefficient, h*(local[r]+complement[t]), -Q(1, Delta))
        assert coefficients[frequencies[t] % modulus] == expected_coefficient

    exact2 = defaultdict(Q)
    for coefficient in coefficients.values():
        for phase, weight in _norm_square(coefficient).items():
            _add(exact2, phase, weight)

    # u0-L*mu = -sum_(s=1)^(L-1)u_s, so V is its exact squared modulus.
    remainder = defaultdict(Q)
    for s in range(1, L):
        _add(remainder, h*local[s], Q(1))
    V = _norm_square(remainder)
    expected2 = defaultdict(Q)
    _add(expected2, Q(), Q(L-1, B*L**2))
    for phase, weight in V.items():
        _add(expected2, phase, weight/Q(B*L**2))
    assert exact2 == expected2

    fourth_result = {"status": "NOT_REQUESTED"}
    if fourth:
        # Direct fourth moment: square the response polynomial, then use only
        # exact grid-character orthogonality and exact conjugate coefficients.
        squared_coefficients = {}
        for f, a in coefficients.items():
            for g, b in coefficients.items():
                target = squared_coefficients.setdefault((f+g) % modulus, defaultdict(Q))
                for phase, weight in _product(a, b).items():
                    _add(target, phase, weight)
        exact4 = defaultdict(Q)
        for coefficient in squared_coefficients.values():
            for phase, weight in _norm_square(coefficient).items():
                _add(exact4, phase, weight)

        # Independently assemble 2*M2^2 - (L-1+V^2)/(B^3*L^4).
        expected4 = defaultdict(Q)
        for phase, weight in _product(expected2, expected2).items():
            _add(expected4, phase, 2*weight)
        _add(expected4, Q(), -Q(L-1, B**3*L**4))
        for phase, weight in _product(V, V).items():
            _add(expected4, phase, -weight/Q(B**3*L**4))
        assert exact4 == expected4
        fourth_result = {"status": "EXACT_PHASE_MAP_EQUALITY", "direct": _map_record(exact4),
                         "formula": _map_record(expected4)}

    source_rows = [[str(values[m+1+t]), str(local[t]), str(complement[t])]
                   for t in range(Delta)]
    return {
        "p": p, "h": h, "m": m, "L": L, "B": B, "Delta": Delta,
        "dyadic_depth": K, "grid_size": str(modulus), "grid_enumerated": False,
        "source_selected_initial": "0", "complement_recurrence_verified": True,
        "nonzero_distinct_frequencies": True,
        "unordered_pair_sums_distinct": True,
        "coefficient_formula_verified": True,
        "mean_zero": True,
        "source_rows_sha256": sha256(json.dumps(source_rows, separators=(",", ":")).encode()).hexdigest(),
        "second_moment": {"status": "EXACT_PHASE_MAP_EQUALITY", "direct": _map_record(exact2),
                          "formula": _map_record(expected2)},
        "fourth_moment": fourth_result,
    }


def run():
    """Return deterministic exact finite certificates; no infinite claim."""
    return {
        "schema": "cyclotomic-fiber-moment-oracle-v1",
        "status": "EXACT_FINITE_GROUP_ALGEBRA_NOT_POINTWISE_CANCELLATION",
        "pi_normality_proved": False,
        "source": "common BBP forcing with selected initial state zero",
        "dependencies": {
            "observational_succ/bbp_source_memory.py": sha256(
                (ROOT/"observational_succ/bbp_source_memory.py").read_bytes()).hexdigest(),
            "scripts/cyclotomic_fiber_moment_oracle.py": sha256(Path(__file__).read_bytes()).hexdigest(),
        },
        "cases": [_case(17, 1, True), _case(17, -2, True), _case(41, 1, False)],
    }


if __name__ == "__main__":
    print(json.dumps(run(), indent=2, sort_keys=True))
