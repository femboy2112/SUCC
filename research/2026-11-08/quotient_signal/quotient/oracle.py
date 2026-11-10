"""Exact Gaussian-rational quotient and refinement oracles.

Independent of the source and interval implementations. No float, random
sample, pi approximation or special-function library is used by this file.
"""
from __future__ import annotations

import argparse
from dataclasses import dataclass
from fractions import Fraction as F
import json
from pathlib import Path


@dataclass(frozen=True)
class Z:
    re: F = F(0)
    im: F = F(0)

    def __post_init__(self):
        object.__setattr__(self, "re", F(self.re))
        object.__setattr__(self, "im", F(self.im))

    @staticmethod
    def coerce(other):
        return other if isinstance(other, Z) else Z(other)

    def __add__(self, other):
        other = self.coerce(other)
        return Z(self.re + other.re, self.im + other.im)

    __radd__ = __add__

    def __neg__(self):
        return Z(-self.re, -self.im)

    def __sub__(self, other):
        return self + (-self.coerce(other))

    def __rsub__(self, other):
        return self.coerce(other) - self

    def __mul__(self, other):
        other = self.coerce(other)
        return Z(self.re * other.re - self.im * other.im,
                 self.re * other.im + self.im * other.re)

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = self.coerce(other)
        return self * other.conj() * Z(1 / other.abs2())

    def conj(self):
        return Z(self.re, -self.im)

    def abs2(self):
        return self.re**2 + self.im**2

    def serial(self):
        return [str(self.re), str(self.im)]


def unit(t):
    """Rational parametrization of the unit circle, exact for rational t."""
    t = F(t)
    return Z((1-t*t)/(1+t*t), 2*t/(1+t*t))


def validated(values, weights):
    if not values or len(values) != len(weights):
        raise ValueError("positive-length values and weights must agree")
    if any(not isinstance(x, Z) for x in values):
        raise TypeError("exact Gaussian rationals required")
    if any(not isinstance(w, (int, F)) or isinstance(w, bool) or w <= 0
           for w in weights):
        raise ValueError("positive exact rational weights required")


def mean(values, weights):
    validated(values, weights)
    return sum((w*x for x, w in zip(values, weights)), Z()) / sum(weights)


def norm2(values, weights):
    validated(values, weights)
    return sum(w*x.abs2() for x, w in zip(values, weights)) / F(sum(weights))


def inner(x, y, weights):
    return mean([u.conj()*v for u, v in zip(x, y)], weights)


def mul(x, y):
    if len(x) != len(y):
        raise ValueError("equal dimensions required")
    return [u*v for u, v in zip(x, y)]


def sub(x, y):
    if len(x) != len(y):
        raise ValueError("equal dimensions required")
    return [u-v for u, v in zip(x, y)]


def project(values, labels, weights):
    validated(values, weights)
    if len(labels) != len(values):
        raise ValueError("one transcript label per atom required")
    sums, masses = {}, {}
    for x, label, w in zip(values, labels, weights):
        sums[label] = sums.get(label, Z()) + w*x
        masses[label] = masses.get(label, F(0)) + w
    return [sums[label]/masses[label] for label in labels]


def quotient(values, a, labels, weights):
    if len(a) != len(values) or any(x.abs2() != 1 for x in a):
        raise ValueError("one exact unit carrier phase per atom required")
    return mul(a, project(mul([x.conj() for x in a], values), labels, weights))


def covariance(a, b, weights):
    return mean(mul(a, b), weights)-mean(a, weights)*mean(b, weights)


def verify_case(a, b, weights, partitions):
    """Return exact check count, raising on the first identity failure."""
    checks = 0

    def check(condition):
        nonlocal checks
        assert condition
        checks += 1

    n = len(a)
    z = mul(a, b)
    W = mean(z, weights)
    old = None
    signed = Z()
    for labels in partitions:
        pa, pb = project(a, labels, weights), project(b, labels, weights)
        pz = project(z, labels, weights)
        qz = quotient(z, a, labels, weights)
        ra, rb = sub(a, pa), sub(b, pb)
        va, vb = norm2(ra, weights), norm2(rb, weights)
        check(qz == mul(a, pb))
        check(quotient(qz, a, labels, weights) == qz)
        check(inner(qz, sub(z, qz), weights) == Z())
        check(norm2(z, weights) == norm2(qz, weights)+norm2(sub(z, qz), weights))
        check(norm2(sub(z, qz), weights) == vb)
        check(mean(pz, weights) == W)
        defect = mean(mul(ra, rb), weights)
        check(W-mean(qz, weights) == defect)
        check(mean(qz, weights) == mean(mul(pa, pb), weights))
        check(covariance(a, b, weights) == covariance(pa, pb, weights)+defect)
        check(defect.abs2() <= va*vb)
        check(norm2(sub(pz, qz), weights) <= va)

        # A separately chosen cell-measurable candidate tests optimality.
        candidate = project([Z(F(i-3, 7), F((i*i)%9-4, 11)) for i in range(n)],
                            labels, weights)
        check(norm2(sub(z, mul(a, candidate)), weights)
              == vb+norm2(sub(pb, candidate), weights))

        # Exact operator polynomial and sharp input, cell by cell.
        for label in set(labels):
            ids = [i for i in range(n) if labels[i] == label]
            ac = [a[i] for i in ids]
            wc = [weights[i] for i in ids]
            lc = [0]*len(ids)
            one = [Z(1)]*len(ids)
            variance = 1-mean(ac, wc).abs2()

            def diff(v):
                return sub(project(v, lc, wc), quotient(v, ac, lc, wc))

            check(norm2(diff(one), wc) == variance)
            probe = [Z(F(i+2, 5), F(3*i-1, 7)) for i in ids]
            dp, dddp = diff(probe), diff(diff(diff(probe)))
            check(dddp == [variance*x for x in dp])
            check(norm2(dp, wc) <= variance*norm2(probe, wc))

        # Gauge transport is lawful only when the gauge is transcript measurable.
        ordered = {label: i for i, label in enumerate(dict.fromkeys(labels))}
        gauge = [unit(F(ordered[label]+1, 5)) for label in labels]
        ap = mul(a, gauge)
        bp = mul(b, [g.conj() for g in gauge])
        check(mul(ap, bp) == z)
        check(quotient(z, ap, labels, weights) == qz)
        check(mul(project(ap, labels, weights), project(bp, labels, weights))
              == mul(pa, pb))

        if old is not None:
            oa, ob, oq, ocov = old
            da, db = sub(pa, oa), sub(pb, ob)
            inc = mean(mul(da, db), weights)
            check(covariance(pa, pb, weights)-ocov == inc)
            check(inc.abs2() <= norm2(da, weights)*norm2(db, weights))
            check(norm2(sub(z, oq), weights)
                  == norm2(sub(z, qz), weights)+norm2(sub(qz, oq), weights))
            check(norm2(qz, weights)-norm2(oq, weights) == norm2(db, weights))
            signed += inc
        old = pa, pb, qz, covariance(pa, pb, weights)
    check(covariance(a, b, weights) == signed+defect)
    return checks


def control_receipts():
    # Two-point arbitrary gauge changes the finite instrument, while z stays 1.
    a, b, weights, trivial = [Z(1), Z(-1)], [Z(1), Z(-1)], [1, 1], [0, 0]
    z = mul(a, b)
    before = mean(quotient(z, a, trivial, weights), weights)
    after = mean(quotient(z, [Z(1), Z(1)], trivial, weights), weights)
    assert before == Z() and after == Z(1)

    # Refinement signed increments can oppose each other exactly.
    a = [Z(1), Z(-1), Z(1), Z(-1)]
    b = [Z(1), Z(1), Z(-1), Z(-1)]
    labels, weights = [0, 0, 0, 1], [1]*4
    coarse = covariance(project(a, labels, weights), project(b, labels, weights), weights)
    total = covariance(a, b, weights)
    assert coarse == Z(F(1, 3)) and total == Z()

    # Same magnitudes, opposite signed signals.
    a = [unit(F(j, 4)) for j in range(6)]
    plus, minus = [x.conj() for x in a], [-x.conj() for x in a]
    labels, weights = [0, 0, 1, 1, 2, 2], [1]*6
    qp, qm = project(plus, labels, weights), project(minus, labels, weights)
    assert [x.abs2() for x in qp] == [x.abs2() for x in qm]
    sp, sm = mean(mul(a, qp), weights), mean(mul(a, qm), weights)
    assert sp == -sm and sp.re > 0 and sp.im == 0

    # Exact mean recovery does not imply trajectory recovery.
    a, b = [Z(1), Z(1), Z(-1), Z(-1)], [Z(1), Z(-1), Z(1), Z(-1)]
    labels, weights = [0, 0, 1, 1], [1]*4
    z, s = mul(a, b), quotient(mul(a, b), a, labels, weights)
    assert mean(z, weights) == mean(s, weights) == Z()
    assert norm2(sub(z, s), weights) == 1
    return {
        "arbitrary_gauge_mean_before": before.serial(),
        "arbitrary_gauge_mean_after": after.serial(),
        "signed_refinement_increments": [coarse.serial(), (-coarse).serial()],
        "phase_blind_opposite_means": [sp.serial(), sm.serial()],
        "zero_mean_error_unit_reconstruction_error": True,
    }


def run():
    checks, cases = 0, 0
    for n in (4, 8, 12, 16):
        partitions = [[0]*n, [i//4 for i in range(n)],
                      [i//2 for i in range(n)], list(range(n))]
        for shift in range(7):
            a = [unit(F(((i+shift)*5)%17-8, 9)) for i in range(n)]
            b = [unit(F((i*i+3*shift)%19-9, 11)) for i in range(n)]
            weights = [F(1+(i+shift)%5, 1+i%3) for i in range(n)]
            checks += verify_case(a, b, weights, partitions)
            cases += 1
    return {"schema": "quotient-signal-exact-v1",
            "arithmetic": "Gaussian rational; exact positive rational weights",
            "source_scope": "universal finite algebra, no selected-source asymptotic",
            "cases": cases, "exact_checks": checks,
            "controls": control_receipts(),
            "status": "PASS; pi base-16 normality OPEN; RH OPEN"}


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = run()
    rendered = json.dumps(result, indent=2, sort_keys=True)+"\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered)
    print(rendered, end="")
