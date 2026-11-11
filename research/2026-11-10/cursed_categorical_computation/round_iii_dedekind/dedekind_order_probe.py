#!/usr/bin/env python3
"""Exact finite regression controls for DEDEKIND_YONEDA.md.

Uses integers and fractions only. These checks calibrate finite examples;
they do not prove an infinite completion theorem or any digit statistic.
No external dependencies and no repository mutation.
"""

from dataclasses import dataclass
from fractions import Fraction
from itertools import combinations
from math import gcd, isqrt
from hashlib import sha256
from pathlib import Path
import json
import platform


@dataclass(frozen=True)
class FinitePoset:
    elements: tuple
    leq: object

    def upper(self, subset):
        return frozenset(
            y for y in self.elements if all(self.leq(x, y) for x in subset)
        )

    def lower(self, subset):
        return frozenset(
            x for x in self.elements if all(self.leq(x, y) for y in subset)
        )

    def closure(self, subset):
        return self.lower(self.upper(subset))


def powerset(elements):
    return tuple(
        frozenset(s)
        for size in range(len(elements) + 1)
        for s in combinations(elements, size)
    )


def completion_controls():
    models = {
        "chain_six": FinitePoset(tuple(range(6)), lambda x, y: x <= y),
        "diamond_four": FinitePoset(
            tuple(range(4)), lambda x, y: x == y or x == 0 or y == 3
        ),
        "antichain_three": FinitePoset(tuple(range(3)), lambda x, y: x == y),
    }
    expected_fixed = {"chain_six": 6, "diamond_four": 4, "antichain_three": 5}
    results = {}
    for name, poset in models.items():
        subsets = powerset(poset.elements)
        for a in subsets:
            closed = poset.closure(a)
            assert a <= closed
            assert poset.closure(closed) == closed
            for b in subsets:
                assert (a <= poset.lower(b)) == (b <= poset.upper(a))
                if a <= b:
                    assert poset.closure(a) <= poset.closure(b)
        fixed = tuple(a for a in subsets if poset.closure(a) == a)
        assert len(fixed) == expected_fixed[name]
        for a in fixed:
            for b in fixed:
                meet = a & b
                join = poset.closure(a | b)
                assert meet in fixed and join in fixed
                for c in fixed:
                    if c <= a and c <= b:
                        assert c <= meet
                    if a <= c and b <= c:
                        assert join <= c
        results[name] = {
            "subsets": len(subsets),
            "galois_pairs": len(subsets) ** 2,
            "fixed_cuts": len(fixed),
            "lattice_pairs": len(fixed) ** 2,
        }

    # A calibrated mutation: replacing closure(union) by union fails.
    antichain = models["antichain_three"]
    a, b = frozenset({0}), frozenset({1})
    assert antichain.closure(a) == a and antichain.closure(b) == b
    assert antichain.closure(a | b) != a | b
    assert antichain.closure(a | b) == frozenset({0, 1, 2})
    results["union_without_closure_mutation"] = "REJECTED"
    return results


def pair(a, b):
    assert a >= 0 and b >= 0
    return (a + b) * (a + b + 1) // 2 + b


def unpair(n):
    assert n >= 0
    w = (isqrt(8 * n + 1) - 1) // 2
    b = n - w * (w + 1) // 2
    return w - b, b


def zigzag(p):
    return 2 * p if p >= 0 else -2 * p - 1


def unzigzag(n):
    return n // 2 if n % 2 == 0 else -(n + 1) // 2


def encode_rational(q):
    return pair(zigzag(q.numerator), q.denominator - 1)


def decode_rational(code):
    a, b = unpair(code)
    p, s = unzigzag(a), b + 1
    if gcd(p, s) != 1:
        raise ValueError("Not a canonical reduced rational code")
    return Fraction(p, s)


def natural_coding_controls():
    rationals = {
        Fraction(p, s) for p in range(-40, 41) for s in range(1, 25)
    }
    codes = {encode_rational(q) for q in rationals}
    assert len(codes) == len(rationals)
    for q in rationals:
        assert decode_rational(encode_rational(q)) == q
    small = {Fraction(p, s) for p in range(-6, 7) for s in range(1, 7)}
    for q in small:
        for r in small:
            left = q.numerator * r.denominator
            right = r.numerator * q.denominator
            assert (left <= right) == (q <= r)
    nonreduced_code = pair(zigzag(2), 2 - 1)
    try:
        decode_rational(nonreduced_code)
    except ValueError:
        pass
    else:
        raise AssertionError("A duplicate nonreduced rational code was accepted")
    return {
        "roundtrips": len(rationals),
        "integer_order_comparisons": len(small) ** 2,
        "nonreduced_code_mutation": "REJECTED",
    }


def below_sqrt_two(q):
    p, s = q.numerator, q.denominator
    return p < 0 or p * p < 2 * s * s


def above_sqrt_two(q):
    p, s = q.numerator, q.denominator
    return p > 0 and p * p > 2 * s * s


def locator(p, q, prefer_lower):
    assert p < q
    if prefer_lower:
        if below_sqrt_two(p):
            return "lower"
        assert above_sqrt_two(q)
        return "upper"
    if above_sqrt_two(q):
        return "upper"
    assert below_sqrt_two(p)
    return "lower"


def sqrt_two_controls():
    last = None
    for n in range(128):
        k = isqrt(2 * 4**n)
        a, b = Fraction(k, 2**n), Fraction(k + 1, 2**n)
        assert below_sqrt_two(a) and above_sqrt_two(b)
        assert b - a == Fraction(1, 2**n)
        if last is not None:
            assert last[0] <= a < b <= last[1]
        last = a, b

    locator_paths = []
    for prefer_lower in (True, False):
        a, b = Fraction(1), Fraction(2)
        for n in range(80):
            old_a, old_b = a, b
            p = a + (b - a) / 3
            q = a + 2 * (b - a) / 3
            verdict = locator(p, q, prefer_lower)
            if verdict == "lower":
                a = p
            else:
                b = q
            assert old_a <= a < b <= old_b
            assert below_sqrt_two(a) and above_sqrt_two(b)
            assert b - a == Fraction(2, 3) ** (n + 1)
        locator_paths.append({"prefer_lower": prefer_lower, "steps": 80})

    delta = Fraction(1, 1024)
    fixed_probes = [Fraction(k, 8) for k in range(-32, 33)]
    first_profile = [below_sqrt_two(q) for q in fixed_probes]
    second_profile = [below_sqrt_two(q - delta) for q in fixed_probes]
    assert first_profile == second_profile
    separating_probe = Fraction(1449, 1024)
    assert above_sqrt_two(separating_probe)
    assert below_sqrt_two(separating_probe - delta)
    assert not below_sqrt_two(separating_probe)
    return {
        "dyadic_enclosures": 128,
        "locator_paths": locator_paths,
        "indistinguishable_fixed_probes": len(fixed_probes),
        "fresh_separating_probe": str(separating_probe),
        "finite_profile_implies_equality_mutation": "REJECTED",
    }


def main():
    result = {
        "status": "PASS",
        "python": platform.python_version(),
        "script_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
        "arithmetic": "exact integers and fractions; no floating point",
        "completion": completion_controls(),
        "coding": natural_coding_controls(),
        "sqrt_two": sqrt_two_controls(),
        "boundary": "Finite regressions only; no asymptotic or normality claim",
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
