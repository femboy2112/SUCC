"""Exact finite boundary filters, target witnesses, and phase-loss controls.

Public arithmetic inputs must have exact type int or Fraction; floats,
booleans and strings are rejected. Fourier calculations take place
in Q[z]/Phi_q(z).  No finite output asserts an asymptotic arithmetic theorem.
"""

from __future__ import annotations

from fractions import Fraction as F
from functools import lru_cache
import json


def rational(value):
    if type(value) not in (int, F):
        raise ValueError("exact integer or Fraction required")
    return F(value)


def _rows(rows):
    result = [[rational(x) for x in row] for row in rows]
    if not result or not result[0]:
        raise ValueError("a nonempty rectangular matrix is required")
    if any(len(row) != len(result[0]) for row in result):
        raise ValueError("ragged matrix")
    return result


def rref(rows):
    """Return exact reduced row-echelon form and pivot columns."""
    a = _rows(rows)
    pivots = []
    row = 0
    for col in range(len(a[0])):
        selected = next((i for i in range(row, len(a)) if a[i][col]), None)
        if selected is None:
            continue
        a[row], a[selected] = a[selected], a[row]
        d = a[row][col]
        a[row] = [x / d for x in a[row]]
        for i in range(len(a)):
            if i != row and a[i][col]:
                scale = a[i][col]
                a[i] = [x - scale * y for x, y in zip(a[i], a[row])]
        pivots.append(col)
        row += 1
        if row == len(a):
            break
    return a, tuple(pivots)


def nullspace(rows):
    a, pivots = rref(rows)
    n = len(a[0])
    out = []
    for free in range(n):
        if free in pivots:
            continue
        z = [F(0)] * n
        z[free] = F(1)
        for row, pivot in enumerate(pivots):
            z[pivot] = -a[row][free]
        out.append(tuple(z))
    return tuple(out)


def solve_linear(rows, rhs):
    """One exact solution, with free coordinates zero; None if inconsistent."""
    a = _rows(rows)
    if len(a) != len(rhs):
        raise ValueError("incompatible right-hand side")
    n = len(a[0])
    reduced, pivots = rref([row + [rational(y)] for row, y in zip(a, rhs)])
    if n in pivots:
        return None
    answer = [F(0)] * n
    for row, pivot in enumerate(pivots):
        answer[pivot] = reduced[row][-1]
    return tuple(answer)


def dot(x, y):
    if len(x) != len(y):
        raise ValueError("incompatible vector lengths")
    return sum((rational(a) * rational(b) for a, b in zip(x, y)), F(0))


def observations(filters, law):
    return tuple(dot(row, law) for row in filters)


def target_identifiability(filters, target):
    """Return a dual exact reconstruction or two indistinguishable laws.

    The filters must explicitly contain the constant-one row.  The result is
    universal over probability laws on this finite carrier, not conditional
    on any one observed data vector.
    """
    a = _rows(filters)
    t = tuple(rational(x) for x in target)
    n = len(t)
    if len(a[0]) != n or [F(1)] * n not in a:
        raise ValueError("matching carrier and explicit mass filter required")
    coefficients = solve_linear(list(zip(*a)), t)
    if coefficients is not None:
        return {"identified": True, "coefficients": coefficients}
    z = next(z for z in nullspace(a) if dot(t, z))
    positive_mass = sum((max(x, F(0)) for x in z), F(0))
    p = tuple(max(x, F(0)) / positive_mass for x in z)
    q = tuple(max(-x, F(0)) / positive_mass for x in z)
    return {
        "identified": False,
        "positive_law": p,
        "negative_law": q,
        "observations": observations(a, p),
        "target_gap": dot(t, p) - dot(t, q),
    }


def approximate_target_certificate(filters, target, coefficients, readings, errors):
    """Exact certified center/radius from a user-supplied dual coefficient list."""
    a = _rows(filters)
    if not (len(a) == len(coefficients) == len(readings) == len(errors)):
        raise ValueError("one coefficient, reading and error per filter required")
    if len(a[0]) != len(target) or any(rational(x) < 0 for x in errors):
        raise ValueError("bad target dimension or negative uncertainty")
    residual = max(
        abs(rational(t) - dot(coefficients, column))
        for t, column in zip(target, zip(*a))
    )
    amplification = sum(
        (abs(rational(c)) * rational(e) for c, e in zip(coefficients, errors)), F(0)
    )
    center = dot(coefficients, readings)
    return {
        "center": center,
        "radius": residual + amplification,
        "approximation_error": residual,
        "measurement_error": amplification,
        "coefficient_l1": sum((abs(rational(c)) for c in coefficients), F(0)),
    }


def cyclic_correlation(signal):
    q = len(signal)
    if not q:
        raise ValueError("empty signal")
    return tuple(
        sum((rational(signal[x]) * rational(signal[(x + s) % q]) for x in range(q)), F(0))
        for s in range(q)
    )


def cyclic_triple(signal):
    q = len(signal)
    if not q:
        raise ValueError("empty signal")
    return tuple(
        tuple(
            sum(
                (rational(signal[x]) * rational(signal[(x + s) % q]) * rational(signal[(x + t) % q])
                 for x in range(q)), F(0)
            )
            for t in range(q)
        )
        for s in range(q)
    )


def cyclic_convolution(signal):
    q = len(signal)
    if not q:
        raise ValueError("empty signal")
    return tuple(
        sum((rational(signal[x]) * rational(signal[(s - x) % q]) for x in range(q)), F(0))
        for s in range(q)
    )


def shift(signal, amount):
    q = len(signal)
    if not q:
        raise ValueError("empty signal")
    return tuple(signal[(x - amount) % q] for x in range(q))


def _trim(poly):
    out = list(poly)
    while len(out) > 1 and not out[-1]:
        out.pop()
    return out or [F(0)]


def _poly_divmod(numerator, denominator):
    a, b = _trim(numerator), _trim(denominator)
    if b == [0]:
        raise ValueError("zero polynomial divisor")
    out = [F(0)] * max(1, len(a) - len(b) + 1)
    while len(a) >= len(b) and a != [0]:
        k, c = len(a) - len(b), F(a[-1]) / F(b[-1])
        out[k] += c
        for j in range(len(b)):
            a[j + k] -= c * b[j]
        a = _trim(a)
    return tuple(_trim(out)), tuple(a)


@lru_cache(None)
def cyclotomic_polynomial(q):
    if type(q) is not int or q < 1:
        raise ValueError("positive integral order required")
    poly = tuple([F(-1)] + [F(0)] * (q - 1) + [F(1)])
    for d in range(1, q):
        if q % d == 0:
            poly, remainder = _poly_divmod(poly, cyclotomic_polynomial(d))
            if remainder != (F(0),):
                raise ArithmeticError("inexact cyclotomic division")
    return poly


def cyclotomic_reduce(poly, q):
    poly = tuple(rational(x) for x in poly)
    modulus = cyclotomic_polynomial(q)
    _, remainder = _poly_divmod(poly, modulus)
    return tuple(remainder) + (F(0),) * (len(modulus) - 1 - len(remainder))


def cyclotomic_multiply(a, b, q):
    a, b = tuple(map(rational, a)), tuple(map(rational, b))
    out = [F(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return cyclotomic_reduce(out, q)


def cyclotomic_conjugate(a, q):
    a = tuple(map(rational, a))
    out = [F(0)] * q
    for exponent, coefficient in enumerate(a):
        out[(-exponent) % q] += coefficient
    return cyclotomic_reduce(out, q)


def exact_fourier(signal):
    """Unnormalized DFT, z=exp(2*pi*i/q), stored in the cyclotomic basis."""
    q = len(signal)
    if not q:
        raise ValueError("empty signal")
    out = []
    for h in range(q):
        poly = [F(0)] * q
        for x, value in enumerate(signal):
            poly[(-h * x) % q] += rational(value)
        out.append(cyclotomic_reduce(poly, q))
    return tuple(out)


def exact_power(signal):
    q = len(signal)
    return tuple(
        cyclotomic_multiply(a, cyclotomic_conjugate(a, q), q)
        for a in exact_fourier(signal)
    )


def exact_bispectrum(signal):
    q = len(signal)
    transformed = exact_fourier(signal)
    return tuple(
        tuple(
            cyclotomic_multiply(
                cyclotomic_multiply(transformed[h], transformed[k], q),
                cyclotomic_conjugate(transformed[(h + k) % q], q), q
            )
            for k in range(q)
        )
        for h in range(q)
    )


def exact_triple_fourier(signal):
    """Independent direct double DFT of the integer/rational triple table."""
    q = len(signal)
    triple = cyclic_triple(signal)
    out = []
    for h in range(q):
        row = []
        for k in range(q):
            poly = [F(0)] * q
            for s in range(q):
                for t in range(q):
                    poly[(-h * s - k * t) % q] += triple[s][t]
            row.append(cyclotomic_reduce(poly, q))
        out.append(tuple(row))
    return tuple(out)


def support_relation_rank(support, q):
    """Rank of additive triangle constraints on formal phase variables.

    A deficient rank proves a continuous unobserved phase family.  Full rank
    alone is NOT a completeness certificate: torsion still needs checking.
    """
    if type(q) is not int or q < 1:
        raise ValueError("positive integral order required")
    support = tuple(sorted(set(support)))
    if any(type(h) is not int or not 0 <= h < q for h in support):
        raise ValueError("support indices must lie in Z/q")
    index = {h: i for i, h in enumerate(support)}
    if not support:
        return 0
    relations = []
    for h in support:
        for k in support:
            s = (h + k) % q
            if s in index:
                row = [0] * len(support)
                row[index[h]] += 1
                row[index[k]] += 1
                row[index[s]] -= 1
                relations.append(row)
    if not relations:
        return 0
    return len(rref(relations)[1])


def control_report():
    a = tuple(int(x in {0, 1, 4, 6}) for x in range(12))
    b = tuple(int(x in {0, 1, 3, 7}) for x in range(12))
    f = (28, 21, 7, 0, 7, 21)
    g = (16, 3, 1, 12, 25, 27)
    u, v = (14, -7, -7), (2, 11, -13)
    triple_u, triple_v = cyclic_triple(u), cyclic_triple(v)
    support_f = [h for h, value in enumerate(exact_fourier(f)) if any(value)]
    return {
        "scope": "EXACT_FINITE_CONTROLS; no asymptotic arithmetic estimate",
        "homometric": {
            "equal_autocorrelation": cyclic_correlation(a) == cyclic_correlation(b),
            "equal_exact_power": exact_power(a) == exact_power(b),
            "same_triples": cyclic_triple(a) == cyclic_triple(b),
            "sum_at_3": [int(cyclic_convolution(a)[3]), int(cyclic_convolution(b)[3])],
            "sum_at_5": [int(cyclic_convolution(a)[5]), int(cyclic_convolution(b)[5])],
        },
        "support_zero": {
            "equal_autocorrelation": cyclic_correlation(f) == cyclic_correlation(g),
            "equal_triples": cyclic_triple(f) == cyclic_triple(g),
            "equal_exact_bispectrum": exact_bispectrum(f) == exact_bispectrum(g),
            "translations": [s for s in range(6) if shift(f, s) == g],
            "support": support_f,
            "triangle_relation_rank": support_relation_rank(support_f, 6),
        },
        "near_haar": {
            "equal_autocorrelation": cyclic_correlation(u) == cyclic_correlation(v),
            "minimum_l1_over_translations_coefficient": int(min(
                sum(abs(x - y) for x, y in zip(u, shift(v, s)))
                for s in range(3)
            )),
            "maximum_triple_difference_coefficient": int(max(
                abs(triple_u[s][t] - triple_v[s][t])
                for s in range(3) for t in range(3)
            )),
        },
    }


if __name__ == "__main__":
    print(json.dumps(control_report(), indent=2, sort_keys=True))
