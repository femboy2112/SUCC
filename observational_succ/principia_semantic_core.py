"""Principia prototype: typed computational paths and exact arithmetic null certificates.

This module proves no RH statements and imports no RH axioms. It checks finite
instances of two universal elementary theorems proved in THEOREMS.md.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import isqrt
from typing import Sequence


class InvalidCertificate(ValueError):
    """A claimed source, computational path, or arithmetic proof is invalid."""


@dataclass(frozen=True)
class Edge:
    kind: str
    start: int
    finish: int
    parameter: int = 1


def check_edge(e: Edge) -> None:
    if e.start < 1:
        raise InvalidCertificate("path left the positive integer source")
    if e.kind == "S" and e.parameter == 1 and e.finish == e.start + 1:
        return
    if e.kind == "V" and e.parameter >= 2 and e.finish == e.parameter * e.start:
        return
    raise InvalidCertificate("illegal source-labelled transition")


def path_endpoint(path: Sequence[Edge]) -> tuple[int, int]:
    if not path:
        raise InvalidCertificate("empty path requires an explicit identity source")
    for i, e in enumerate(path):
        check_edge(e)
        if i and path[i - 1].finish != e.start:
            raise InvalidCertificate("noncomposable computational path")
    return path[0].start, path[-1].finish


def is_prime(p: int) -> bool:
    if p < 2:
        return False
    for k in range(2, isqrt(p) + 1):
        if p % k == 0:
            return False
    return True


@dataclass(frozen=True)
class CycleCertificate:
    source: str
    p: int
    n: int
    via_successor: tuple[Edge, ...]
    via_prime: tuple[Edge, ...]


def make_cycle(n: int, p: int) -> CycleCertificate:
    if n < 1 or not is_prime(p):
        raise InvalidCertificate("cycle requires n >= 1 and an authentic prime")
    left = (Edge("S", n, n + 1), Edge("V", n + 1, p * (n + 1), p))
    right = (Edge("V", n, p * n, p),) + tuple(
        Edge("S", p * n + k, p * n + k + 1) for k in range(p)
    )
    return CycleCertificate("positive-integer-SUCC-FUCC", p, n, left, right)


def verify_cycle(c: CycleCertificate) -> tuple[int, int]:
    if c.source != "positive-integer-SUCC-FUCC" or not is_prime(c.p) or c.n < 1:
        raise InvalidCertificate("unrecognized arithmetic source")
    if c != make_cycle(c.n, c.p):
        raise InvalidCertificate("cycle does not encode the authenticated affine square")
    if path_endpoint(c.via_successor) != path_endpoint(c.via_prime):
        raise InvalidCertificate("not an endpoint-null path difference")
    # Source cochain: omega(S at a)=a, omega(V)=0.
    omega = lambda path: sum(e.start for e in path if e.kind == "S")
    response = omega(c.via_successor) - omega(c.via_prime)
    expected = (1 - c.p * c.p) * c.n - c.p * (c.p - 1) // 2
    if response != expected or response == 0:
        raise InvalidCertificate("no authenticated nonzero path-cochain witness")
    # Every exact gradient dg telescopes and is zero on the same cycle.
    exact_gradient = lambda path: sum(e.finish**2 - e.start**2 for e in path)
    if exact_gradient(c.via_successor) != exact_gradient(c.via_prime):
        raise InvalidCertificate("exact cochain must vanish on a boundary-null cycle")
    return 0, response  # (endpoint boundary, path-sensitive response)


def trim(poly: Sequence[int]) -> tuple[int, ...]:
    if not poly:
        return (0,)
    a = list(poly)
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return tuple(a)


def multiply(a: Sequence[int], b: Sequence[int]) -> tuple[int, ...]:
    result = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            result[i + j] += x * y
    return trim(result)


def evaluate(poly: Sequence[int], x: Fraction) -> Fraction:
    out = Fraction(0)
    for a in reversed(poly):
        out = out * x + a
    return out


def divide_by_root(poly: tuple[int, ...], q: int) -> tuple[int, ...]:
    """Find Q in Z[z] with poly=(q*z-1)*Q; fail if impossible."""
    if q < 2 or len(poly) < 2:
        raise InvalidCertificate("missing polynomial degree or invalid radix root")
    quotient = [-poly[0]]
    for j in range(1, len(poly) - 1):
        quotient.append(q * quotient[-1] - poly[j])
    if q * quotient[-1] != poly[-1]:
        raise InvalidCertificate("required integral root is absent")
    return trim(quotient)


@dataclass(frozen=True)
class NullHeightCertificate:
    source: str
    coeffs: tuple[int, ...]  # ascending, nonzero polynomial
    radix: int
    depth: int
    prime: int
    valuation: int
    stages: tuple[tuple[int, ...], ...]  # F/p^m, /z, then / (radix^j z-1)


def compile_null_height(
    coeffs: Sequence[int], *, depth: int, prime: int, valuation: int,
    radix: int = 16,
) -> NullHeightCertificate:
    f = trim(coeffs)
    if f == (0,):
        raise InvalidCertificate("zero source has no nonvanishing witness")
    if radix < 2 or depth < 0 or valuation < 0 or not is_prime(prime):
        raise InvalidCertificate("ill-typed radix/prime/multiplicity inputs")
    pm = prime**valuation
    if any(a % pm for a in f):
        raise InvalidCertificate("p-adic Hasse coefficient condition failed")
    current = trim([a // pm for a in f])
    stages = [current]
    if current[0] != 0 or len(current) < 2:
        raise InvalidCertificate("source-zero null relation is absent")
    current = trim(current[1:])
    stages.append(current)
    for j in range(1, depth + 1):
        current = divide_by_root(current, radix**j)
        stages.append(current)
    return NullHeightCertificate("auxiliary-integer-polynomial", f, radix, depth, prime, valuation, tuple(stages))


def verify_null_height(c: NullHeightCertificate) -> dict[str, int]:
    """Independent exact checker: rebuild multiplications, do not call compiler division."""
    if c.source != "auxiliary-integer-polynomial" or c.radix < 2 or c.depth < 0:
        raise InvalidCertificate("unlicensed source or radix")
    if not is_prime(c.prime) or c.valuation < 0 or c.coeffs == (0,):
        raise InvalidCertificate("bad nonvanishing / local valuation claim")
    if trim(c.coeffs) != c.coeffs or len(c.stages) != c.depth + 2:
        raise InvalidCertificate("noncanonical source or missing proof path")
    pm = c.prime**c.valuation
    if any(type(a) is not int for a in c.coeffs):
        raise InvalidCertificate("coefficients must be ordinary integers")
    if any(a % pm for a in c.coeffs):
        raise InvalidCertificate("claimed local Hasse jets are not p-integral")
    steps = c.stages
    if any(not poly or trim(poly) != poly or any(type(a) is not int for a in poly) for poly in steps):
        raise InvalidCertificate("forged quotient or nonintegral factor")
    if tuple(pm * a for a in steps[0]) != c.coeffs:
        raise InvalidCertificate("local divisibility step not transported")
    if multiply((0, 1), steps[1]) != steps[0]:
        raise InvalidCertificate("zero-origin source factorization false")
    for j in range(1, c.depth + 1):
        if multiply((-1, c.radix**j), steps[j + 1]) != steps[j]:
            raise InvalidCertificate("finite null factor not source-multiplicative")
    if steps[-1] == (0,):
        raise InvalidCertificate("null field zero: cannot infer a capacity obstruction")
    # Independent root-evaluation controls catch a purported factor path that is
    # valid algebraically but not what the claimed observer readings say.
    if evaluate(c.coeffs, Fraction(0)) != 0:
        raise InvalidCertificate("source origin not null")
    for j in range(1, c.depth + 1):
        if evaluate(c.coeffs, Fraction(1, c.radix**j)) != 0:
            raise InvalidCertificate("claimed observational null is absent")
    minimum = pm * c.radix ** (c.depth * (c.depth + 1) // 2)
    leading = abs(c.coeffs[-1]); norm = sum(abs(a) for a in c.coeffs)
    if leading < minimum or norm < minimum:
        raise InvalidCertificate("arithmetic capacity theorem violated")
    return {"capacity_lower_bound": minimum, "leading_abs": leading, "l1_norm": norm,
            "independent_null_roots": c.depth + 1, "remaining_degree": len(steps[-1]) - 1}
