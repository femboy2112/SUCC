#!/usr/bin/env python3
"""Finite exact checks for rational compilers; theorem proofs are in the note.

The pi name is imported from computation_probe.py. This is a shared dependency,
not independent evidence for the BBP identity or pi's transcendence.
"""
from __future__ import annotations

import argparse
from dataclasses import dataclass
from fractions import Fraction as Q
from hashlib import sha256
import json
from pathlib import Path
import platform

from computation_probe import bbp_interval, bbp_table, machin_interval


def trim(p):
    p = tuple(map(Q, p))
    while p and not p[-1]:
        p = p[:-1]
    return p


def add(p, q):
    return trim(tuple((p[i] if i < len(p) else Q(0)) +
                      (q[i] if i < len(q) else Q(0))
                      for i in range(max(len(p), len(q)))))


def mul(p, q):
    if not p or not q:
        return ()
    r = [Q(0)] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            r[i+j] += a*b
    return trim(r)


def divmod_poly(p, q):
    p, q = trim(p), trim(q)
    if not q:
        raise ZeroDivisionError("zero polynomial divisor")
    quotient = [Q(0)] * max(0, len(p)-len(q)+1)
    while p and len(p) >= len(q):
        k, a = len(p)-len(q), p[-1]/q[-1]
        quotient[k] += a
        p = add(p, (Q(0),)*k + tuple(-a*b for b in q))
    return trim(quotient), p


def gcd_poly(p, q):
    while q:
        p, q = q, divmod_poly(p, q)[1]
    return tuple(a/p[-1] for a in p) if p else ()


@dataclass(frozen=True)
class RF:
    num: tuple
    den: tuple = (Q(1),)

    def __post_init__(self):
        p, q = trim(self.num), trim(self.den)
        if not q:
            raise ZeroDivisionError("zero rational-function denominator")
        if not p:
            p, q = (), (Q(1),)
        else:
            g = gcd_poly(p, q)
            p, rp = divmod_poly(p, g)
            q, rq = divmod_poly(q, g)
            assert not rp and not rq
            leading = q[-1]
            p, q = tuple(a/leading for a in p), tuple(a/leading for a in q)
        object.__setattr__(self, "num", p)
        object.__setattr__(self, "den", q)

    def __add__(self, other):
        return RF(add(mul(self.num, other.den), mul(other.num, self.den)),
                  mul(self.den, other.den))

    def __neg__(self):
        return RF(tuple(-a for a in self.num), self.den)

    def __sub__(self, other):
        return self + (-other)

    def __mul__(self, other):
        return RF(mul(self.num, other.num), mul(self.den, other.den))

    def inverse(self):
        return RF(self.den, self.num)

    def __pow__(self, k):
        if k < 0:
            return self.inverse() ** (-k)
        result = RF((1,))
        for _ in range(k):
            result = result*self
        return result


def poly_at(p, x):
    result = Q(0)
    for a in reversed(p):
        result = result*x + a
    return result


def interval_mul(x, y):
    products = tuple(a*b for a in x for b in y)
    return min(products), max(products)


def poly_interval(p, interval):
    result = (Q(0), Q(0))
    for a in reversed(p):
        lo, hi = interval_mul(result, interval)
        result = lo+a, hi+a
    return result


def rf_interval(f, interval):
    p, q = poly_interval(f.num, interval), poly_interval(f.den, interval)
    if q[0] <= 0 <= q[1]:
        return None
    return interval_mul(p, (1/q[1], 1/q[0]))


def sign_interval(interval):
    if interval is None:
        return None
    lo, hi = interval
    return 1 if lo > 0 else (-1 if hi < 0 else None)


def sign_certificate(f, table):
    if not f.num:
        return {"sign": 0, "terms": 0, "method": "exact polynomial identity"}
    for n in range(1, len(table)):
        interval = rf_interval(f, bbp_interval(n, table))
        sign = sign_interval(interval)
        if sign is not None:
            return {"sign": sign, "terms": n,
                    "interval": [str(x) for x in interval]}
    raise AssertionError("finite regression budget exhausted; no theorem inferred")


def floor_certificate(f, table):
    for n in range(1, len(table)):
        interval = rf_interval(f, bbp_interval(n, table))
        if interval is not None:
            lo, hi = (x.numerator//x.denominator for x in interval)
            if lo == hi:
                return {"floor": lo, "terms": n}
    raise AssertionError("finite regression budget exhausted")


def matrix(a, b):
    return ((a, 2*b), (b, a))


def matrix_mul(a, b):
    return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(2))
                       for j in range(2)) for i in range(2))


def main():
    quadratic_products = 0
    values = tuple(Q(i, j) for j in (1, 2) for i in range(-2, 3))
    for a in values:
        for b in values:
            for c in values:
                for d in values:
                    assert matrix_mul(matrix(a, b), matrix(c, d)) == \
                           matrix(a*c+2*b*d, a*d+b*c)
                    quadratic_products += 1
    j = matrix(0, 1)
    assert matrix_mul(j, j) == matrix(2, 0)
    # Mutation: replacing 2b by b changes the represented field.
    wrong = ((0, 1), (1, 0))
    assert matrix_mul(wrong, wrong) != matrix(2, 0)

    one, t = RF((1,)), RF((0, 1))
    assert (t*t-one)*(t-one).inverse() == t+one
    assert (t*t-one)*(t-one).inverse() != t-one
    assert RF((0, 0)) == RF(())
    try:
        RF((1,), ())
    except ZeroDivisionError:
        pass
    else:
        raise AssertionError("zero denominator accepted")

    expressions = [RF((a, b), (c, 1))
                   for a in (-2, 0, 3) for b in (1, 2) for c in (-1, 1, 4)]
    evaluations = 0
    for f in expressions:
        for g in expressions:
            for x in (Q(2), Q(5, 2), Q(7, 2)):
                def ev(h):
                    return poly_at(h.num, x)/poly_at(h.den, x)
                assert ev(f+g) == ev(f)+ev(g)
                assert ev(f*g) == ev(f)*ev(g)
                evaluations += 2

    # Test the non-thin categorical bridge on actual vector-space maps,
    # including zero dimensions and rational-function coefficients.
    zero = RF(())
    coefficient_bank = (zero, one, t, (t-one).inverse(), t*t)

    def typed_matrix(rows, columns, offset=0):
        return tuple(tuple(coefficient_bank[(offset+3*i+j) % len(coefficient_bank)]
                           for j in range(columns)) for i in range(rows))

    def linear_map(a, vector):
        return tuple(sum((c*x for c, x in zip(row, vector)), zero) for row in a)

    def tau(a, vectors, dimension):
        return tuple(tuple(sum((c*v[k] for c, v in zip(row, vectors)), zero)
                           for k in range(dimension)) for row in a)

    def compose(b, a, columns):
        return tuple(tuple(sum((row[k]*a[k][j] for k in range(len(a))), zero)
                           for j in range(columns)) for row in b)

    family_cases = 0
    for d, e, n, m in ((1, 1, 2, 3), (2, 3, 2, 2), (3, 2, 1, 2),
                       (0, 2, 2, 3), (2, 0, 2, 3), (2, 3, 0, 2), (2, 3, 2, 0)):
        a, h = typed_matrix(m, n, 1), typed_matrix(e, d, 2)
        vectors = typed_matrix(n, d, 3)
        left = tuple(linear_map(h, v) for v in tau(a, vectors, d))
        right = tau(a, tuple(linear_map(h, v) for v in vectors), e)
        assert left == right  # h^m tau_A = tau_A h^n
        b = typed_matrix(2, m, 4)
        assert tau(b, tau(a, vectors, d), d) == tau(compose(b, a, n), vectors, d)
        family_cases += 1

    table = bbp_table(80)
    independent_name = machin_interval(100)
    cases = {
        "pi_minus_3": t-RF((3,)),
        "22_over_7_minus_pi": RF((Q(22, 7),))-t,
        "355_over_113_minus_pi": RF((Q(355, 113),))-t,
        "pi_minus_333_over_106": t-RF((Q(333, 106),)),
        "squared_close_difference": (t-RF((Q(22, 7),)))**2,
        "rational_function": (t*t-one)*(t-one).inverse(),
        "exact_zero": (t*t-one)-(t-one)*(t+one),
    }
    signs = {}
    for name, f in cases.items():
        receipt = sign_certificate(f, table)
        if f.num:
            assert receipt["sign"] == sign_interval(rf_interval(f, independent_name))
        signs[name] = receipt
    assert signs["22_over_7_minus_pi"]["sign"] == 1
    assert signs["355_over_113_minus_pi"]["sign"] == 1
    assert signs["exact_zero"]["sign"] == 0

    floors = {}
    for exponent in (0, 1, 2, 4, 8, 16, 32):
        f = RF((16**exponent,))*t
        result = floor_certificate(f, table)
        interval = rf_interval(f, independent_name)
        assert interval is not None
        a, b = (x.numerator//x.denominator for x in interval)
        assert result["floor"] == a == b
        floors[str(exponent)] = result

    # A finite rational probe set is not the full Yoneda profile.
    probes = (Q(0), Q(1), Q(2))
    assert tuple(q < Q(4, 3) for q in probes) == tuple(q < Q(3, 2) for q in probes)
    assert (Q(7, 5) < Q(4, 3)) != (Q(7, 5) < Q(3, 2))
    # Forgetting the relation between repeated variables loses exactness.
    interval = (Q(1), Q(2))
    naive_difference = interval[0]-interval[1], interval[1]-interval[0]
    assert naive_difference == (Q(-1), Q(1))
    assert t-t == RF(())
    # A semidecision procedure must not wait for a zero value to become positive.
    assert sign_interval((Q(-1, 10), Q(1, 10))) is None

    return {
        "status": "VERIFIED_FINITE",
        "python": platform.python_version(),
        "arithmetic": "integers and fractions.Fraction only",
        "script_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
        "shared_pi_name_sha256": sha256(Path(__file__).with_name("computation_probe.py").read_bytes()).hexdigest(),
        "counts": {"quadratic_matrix_products": quadratic_products,
                   "rational_function_evaluations": evaluations,
                   "sign_cases": len(signs), "floor_cases": len(floors),
                   "family_naturality_and_composition_cases": family_cases},
        "sign_certificates": signs,
        "floor_certificates": floors,
        "mutation_controls": ["wrong quadratic relation", "wrong factor cancellation",
                              "zero denominator", "finite probe collision",
                              "lost variable correlation", "unresolved sign interval"],
        "scope": "Finite implementation checks; algebraic and termination theorems require the note's proofs and pi transcendence. No normality claim.",
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    receipt = main()
    text = json.dumps(receipt, indent=2, sort_keys=True)+"\n"
    if args.output:
        args.output.write_text(text, encoding="utf-8")
    print(json.dumps({"status": receipt["status"], "counts": receipt["counts"]}, sort_keys=True))
