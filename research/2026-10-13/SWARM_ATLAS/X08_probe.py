#!/usr/bin/env python3
"""Exact bounded X08 controls; no imported helpers or floating arithmetic."""
from __future__ import annotations

import argparse
from dataclasses import dataclass
from fractions import Fraction
import hashlib
import itertools
import json
import math
from pathlib import Path
import resource
import subprocess
import sys
import time

if not __debug__:
    raise RuntimeError("optimized Python would disable regression checks")
resource.setrlimit(resource.RLIMIT_AS, (256 * 1024 * 1024,) * 2)
resource.setrlimit(resource.RLIMIT_CPU, (25, 25))


@dataclass(frozen=True)
class QI:
    re: Fraction = Fraction(0)
    im: Fraction = Fraction(0)

    def __post_init__(self):
        object.__setattr__(self, "re", Fraction(self.re))
        object.__setattr__(self, "im", Fraction(self.im))

    def __add__(self, other):
        return QI(self.re + other.re, self.im + other.im)

    def __neg__(self):
        return QI(-self.re, -self.im)

    def __sub__(self, other):
        return self + -other

    def __mul__(self, other):
        return QI(self.re * other.re - self.im * other.im,
                  self.re * other.im + self.im * other.re)

    def norm(self):
        return self.re ** 2 + self.im ** 2

    def inv(self):
        n = self.norm()
        if not n:
            raise ZeroDivisionError("zero Gaussian rational")
        return QI(self.re / n, -self.im / n)

    def __truediv__(self, other):
        return self * other.inv()

    def power(self, exponent):
        if exponent < 0:
            return self.inv().power(-exponent)
        result = ONE
        for _ in range(exponent):
            result = result * self
        return result


ZERO, ONE, I = QI(), QI(1), QI(0, 1)
PI = {"1+i": QI(1, 1), "3": QI(3)}


def vp_integer(n, p):
    if n <= 0:
        raise ValueError("positive integer required")
    k = 0
    while n % p == 0:
        k += 1
        n //= p
    return k


def valuation(z, place="1+i"):
    """None denotes infinity. Norm formula is exact for these two places."""
    if z == ZERO:
        return None
    n = z.norm()
    p, e = (2, 1) if place == "1+i" else (3, 2)
    value = vp_integer(n.numerator, p) - vp_integer(n.denominator, p)
    assert value % e == 0
    return value // e


def valuation_by_division(z, place="1+i"):
    if z == ZERO:
        return None
    d = math.lcm(z.re.denominator, z.im.denominator)
    a, b = int(z.re * d), int(z.im * d)
    k = 0
    if place == "1+i":
        while (a + b) % 2 == 0:
            a, b = (a + b) // 2, (b - a) // 2
            k += 1
        return k - 2 * vp_integer(d, 2)
    while a % 3 == 0 and b % 3 == 0:
        a, b = a // 3, b // 3
        k += 1
    return k - vp_integer(d, 3)


def capped(z, cap, place):
    t = valuation(z, place)
    return cap if t is None else min(t, cap)


def separation_depth(z, cap, place):
    t = valuation(z, place)
    return cap if t is None else min(t + 1, cap)


@dataclass(frozen=True)
class Affine:
    a: QI
    b: QI

    def __post_init__(self):
        if self.a == ZERO:
            raise ValueError("a groupoid label must be invertible")

    def apply(self, z):
        return self.a * z + self.b

    def after(self, other):
        return Affine(self.a * other.a, self.a * other.b + self.b)

    def inverse(self):
        return Affine(self.a.inv(), -(self.b / self.a))


IDENTITY = Affine(ONE, ZERO)


def prefixes(word):
    result = [IDENTITY]
    for step in word:  # chronological order, products act rightmost first
        result.append(step.after(result[-1]))
    return result


def trace(word, z, cap, place):
    return [capped(g.apply(z), cap, place) for g in prefixes(word)]


def demand(word, z, cap, place):
    return max(separation_depth(g.apply(z), cap, place) - valuation(g.a, place)
               for g in prefixes(word))


def below_bound_witness(word, z, cap, place):
    req = demand(word, z, cap, place)
    r = req - 1
    for j, g in enumerate(prefixes(word)):
        y = g.apply(z)
        target = separation_depth(y, cap, place) - valuation(g.a, place)
        if target != req:
            continue
        t = valuation(y, place)
        s = r + valuation(g.a, place)
        yp = ZERO if t is not None and t < cap else PI[place].power(s)
        zp = (yp - g.b) / g.a
        delta_v = valuation(zp - z, place)
        assert delta_v is None or delta_v >= r
        assert capped(g.apply(zp), cap, place) != capped(y, cap, place)
        return {"prefix": j, "depth": r, "z": z, "witness": zp,
                "difference_valuation": delta_v,
                "original_trace": trace(word, z, cap, place),
                "witness_trace": trace(word, zp, cap, place)}
    raise AssertionError("sharpness witness not found")


def rational_prime(n):
    return n >= 2 and all(n % d for d in range(2, math.isqrt(n) + 1))


def gaussian_prime(z):
    if z.re.denominator != 1 or z.im.denominator != 1:
        return False
    a, b = int(z.re), int(z.im)
    if a and b:
        return rational_prime(a * a + b * b)
    c = abs(a or b)
    return rational_prime(c) and c % 4 == 3


def prime_by_gaussian_divisors(z):
    """Independent finite Gaussian-divisor search, not the classification rule."""
    if z.re.denominator != 1 or z.im.denominator != 1 or z.norm() <= 1:
        return False
    n = int(z.norm())
    bound = math.isqrt(n)
    for a in range(-bound, bound + 1):
        for b in range(-bound, bound + 1):
            d = QI(a, b)
            if 1 < d.norm() < n:
                q = z / d
                if q.re.denominator == q.im.denominator == 1:
                    return False
    return True


def source_path(word, z, bound):
    if not gaussian_prime(z):
        return False
    current = z
    for step in word:
        target = step.apply(current)
        distance = (target - current).norm()
        if not gaussian_prime(target) or not (0 < distance <= bound):
            return False
        current = target
    return True


def encode(value):
    if isinstance(value, QI):
        return {"re": str(value.re), "im": str(value.im)}
    if isinstance(value, Affine):
        return {"a": encode(value.a), "b": encode(value.b)}
    if isinstance(value, dict):
        return {k: encode(v) for k, v in value.items()}
    if isinstance(value, (tuple, list)):
        return [encode(v) for v in value]
    return value


def run():
    started = time.monotonic_ns()
    counts = {}
    # Positive and hostile calibrations, before the sweep.
    assert valuation(QI(1, 1)) == 1
    assert valuation(QI(2)) == 2
    assert valuation(QI(Fraction(1, 2))) == -2
    assert valuation(ZERO) is None and capped(ZERO, 4, "1+i") == 4
    assert gaussian_prime(QI(3)) and not gaussian_prime(QI(5))
    assert gaussian_prime(QI(1, 2)) and not gaussian_prime(QI(3, 4))

    points = [QI(a, b) for a in range(-3, 4) for b in range(-3, 4)]
    fractions = [QI(Fraction(a, d), Fraction(b, d))
                 for d in (1, 2, 3, 5) for a in range(-3, 4) for b in range(-3, 4)]
    for place in PI:
        for z in fractions:
            assert valuation(z, place) == valuation_by_division(z, place)
    counts["independent_valuation_checks"] = len(fractions) * len(PI)
    for z in points:
        assert gaussian_prime(z) == prime_by_gaussian_divisors(z)
    counts["independent_prime_checks"] = len(points)

    base = [Affine(QI(1), QI(1)), Affine(QI(2), QI(-1)),
            Affine(QI(1), I), Affine(QI(1, 1), QI(-1, 2)),
            Affine(QI(Fraction(1, 3)), QI(2, -1))]
    steps = base + [g.inverse() for g in base]
    for g, h, k in itertools.product(steps, repeat=3):
        assert g.after(h).after(k) == g.after(h.after(k))
    counts["associativity_triples"] = len(steps) ** 3
    for place, g, h in itertools.product(PI, steps, steps):
        assert valuation(g.after(h).a, place) == valuation(g.a, place) + valuation(h.a, place)
        assert g.after(g.inverse()) == IDENTITY
    counts["slope_cocycle_and_inverse_cases"] = len(PI) * len(steps) ** 2

    words = [[g] for g in steps] + [[g, h] for g, h in itertools.product(steps, repeat=2)]
    centers = [QI(0), QI(1), QI(1, 1), QI(-1, 2), QI(Fraction(1, 2), Fraction(1, 3))]
    units = [QI(1), QI(-1), I, QI(1, 2)]
    sharp = []
    stable = concatenation = 0
    for place, word, z, cap in itertools.product(PI, words, centers, range(1, 5)):
        req = demand(word, z, cap, place)
        expected = trace(word, z, cap, place)
        # Fresh exact rational perturbations at and above the derived bound.
        for extra, unit in itertools.product(range(3), units):
            zp = z + PI[place].power(req + extra) * unit
            assert trace(word, zp, cap, place) == expected
            stable += 1
        witness = below_bound_witness(word, z, cap, place)
        if len(sharp) < 8 or (place == "3" and len(sharp) < 16):
            sharp.append({"place": place, "cap": cap, "word": word, **witness})
        for split in range(len(word) + 1):
            beta, gamma = word[:split], word[split:]
            total_beta = prefixes(beta)[-1]
            rhs = max(demand(beta, z, cap, place),
                      demand(gamma, total_beta.apply(z), cap, place) - valuation(total_beta.a, place))
            assert req == rhs
            concatenation += 1
    counts["whole_path_models"] = len(PI) * len(words) * len(centers) * 4
    counts["stable_rational_perturbations"] = stable
    counts["constructive_below_bound_falsifiers"] = counts["whole_path_models"]
    counts["max_plus_concatenation_checks"] = concatenation

    z0, y = QI(1, 1), QI(1, 2)
    g, h = Affine(QI(2), QI(-1)), Affine(ONE, I)
    assert source_path([h, g], z0, 4)
    assert not source_path([g, h], z0, 4)
    assert g.after(h).apply(z0) == QI(1, 4)
    assert h.after(g).apply(z0) == QI(1, 3)
    assert g.after(h).b - h.after(g).b == I
    dropped_cross_term = Affine(g.a * h.a, g.b + h.b)
    assert dropped_cross_term.apply(z0) != g.after(h).apply(z0)
    hidden_composite_word = [g, h, h]
    assert gaussian_prime(prefixes(hidden_composite_word)[-1].apply(z0))
    assert not source_path(hidden_composite_word, z0, 4)
    # Complete ambient toggles; source enabledness is measured after every prefix.
    factorial = {}
    for order_name, both in (("h_then_g", [h, g]), ("g_then_h", [g, h])):
        cells = {"00": [], "10": [g], "01": [h], "11": both}
        addresses = {key: prefixes(word)[-1].apply(z0) for key, word in cells.items()}
        membership = {key: int(source_path(word, z0, 4)) for key, word in cells.items()}
        factorial[order_name] = {
            "addresses": addresses, "source_enabledness": membership,
            "address_mixed_difference": addresses["11"] - addresses["10"] - addresses["01"] + addresses["00"],
            "enabledness_mixed_difference": membership["11"] - membership["10"] - membership["01"] + membership["00"],
        }
    assert factorial["h_then_g"]["address_mixed_difference"] == I
    assert factorial["g_then_h"]["address_mixed_difference"] == ZERO
    assert factorial["h_then_g"]["enabledness_mixed_difference"] == 0
    assert factorial["g_then_h"]["enabledness_mixed_difference"] == -1

    excursion = Affine(PI["1+i"].power(-3), y - PI["1+i"].power(-3) * z0)
    excursion_word = [excursion, excursion.inverse()]
    assert source_path(excursion_word, z0, 1)
    assert prefixes(excursion_word)[-1] == IDENTITY
    empty_req, excursion_req = demand([], z0, 3, "1+i"), demand(excursion_word, z0, 3, "1+i")
    assert (empty_req, excursion_req) == (2, 4)
    cancellation_receipt = below_bound_witness(excursion_word, z0, 3, "1+i")

    # Exact valuation-only no-go and fixed-depth successor witnesses.
    successor = Affine(ONE, ONE)
    fixed_depth = []
    for place, r in itertools.product(PI, range(1, 6)):
        x, xp = PI[place].power(r) - ONE, PI[place].power(r + 1) - ONE
        assert valuation(x, place) == valuation(xp, place) == 0
        assert valuation(xp - x, place) >= r
        assert valuation(successor.apply(x), place) == r
        assert valuation(successor.apply(xp), place) == r + 1
        fixed_depth.append({"place": place, "depth": r, "x": x, "xp": xp,
                            "successor_valuations": [r, r + 1]})

    # Authentic source adjacency is rechecked, never inferred from residues.
    prime_path = [QI(1, 1), QI(1, 2), QI(0, 3), QI(-1, 2),
                  QI(-2, 1), QI(-3, 0), QI(-4, 1)]
    translation_word = [Affine(ONE, v - u) for u, v in zip(prime_path, prime_path[1:])]
    assert source_path(translation_word, prime_path[0], 2)
    displacement = prime_path[-1] - prime_path[0]
    assert displacement == QI(-5)
    fake_repeat = prime_path[1] + displacement
    assert fake_repeat == QI(-4, 2) and not gaussian_prime(fake_repeat)
    assert not source_path(translation_word, prime_path[-1], 2)

    # Small complete window, including all legitimate graph translations.
    window = [QI(a, b) for a in range(-5, 6) for b in range(-5, 6)]
    primes = [z for z in window if gaussian_prime(z)]
    edges = [(u, v) for u, v in itertools.product(primes, repeat=2)
             if 0 < (v - u).norm() <= 2]
    for u, v in edges:
        e = Affine(ONE, v - u)
        assert source_path([e], u, 2)
        assert source_path([e.inverse()], v, 2)
        for place in PI:
            r = demand([e], u, 3, place)
            assert valuation(e.a, place) == 0
            assert trace([e], u + PI[place].power(r), 3, place) == trace([e], u, 3, place)
    counts["complete_window_points"] = len(window)
    counts["complete_window_primes"] = len(primes)
    counts["actual_directed_prime_adjacencies"] = len(edges)

    root = Path(__file__).resolve().parents[3]
    source_paths = ["AGENTS.md", "docs/METHOD.md", "provenance/IMPORT_MANIFEST.json",
                    "research/2026-10-13/SWARM_ATLAS/PROTOCOL.md",
                    "research/2026-10-13/SWARM_ATLAS/E33.md",
                    "research/2026-10-13/SWARM_ATLAS/E34.md",
                    "research/2026-10-13/SWARM_ATLAS/E35.md",
                    "research/2026-10-13/E36_DIRICHLET_LOG_MULTIPLICATIVITY.md",
                    "research/2026-10-13/E39_GAUSSIAN_ARITHMETIC_CUT_AND_TRANSPORT.md",
                    "research/2026-10-13/SWARM_ATLAS/X08.md"]
    hashes = {p: hashlib.sha256((root / p).read_bytes()).hexdigest() for p in source_paths}
    hashes[str(Path(__file__).relative_to(root))] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    current = subprocess.run(["git", "rev-parse", "HEAD"], cwd=root, check=True,
                             text=True, capture_output=True).stdout.strip()
    return encode({
        "schema": "SUCC.X08.exact.v1", "status": "TESTED MODEL",
        "base_commit": "dc23cf405fa432b717ca84018ab86d78ef08edde",
        "execution_head": current, "branch": "research/swm-x08-2026-10-13",
        "limits": {"cpu_seconds": 25, "address_space_bytes": 268435456},
        "elapsed_milliseconds": (time.monotonic_ns() - started) // 1000000,
        "source_sha256": hashes, "counts": counts,
        "retained_sharpness_examples": sharp,
        "factorial": factorial,
        "order_witness": {"start": z0, "g": g, "h": h,
                          "h_then_g_trace": [z0, h.apply(z0), g.after(h).apply(z0)],
                          "g_then_h_trace": [z0, g.apply(z0), h.after(g).apply(z0)],
                          "source_paths": [True, False]},
        "inverse_excursion": {"start": z0, "middle": y, "label": excursion,
                              "empty_demand": empty_req, "excursion_demand": excursion_req,
                              "below_bound_witness": cancellation_receipt},
        "hidden_composite_intermediate": {
            "trace": [q.apply(z0) for q in prefixes(hidden_composite_word)],
            "final_prime": True, "itinerary_valid": False},
        "fixed_depth_no_go": fixed_depth,
        "periodic_source_no_go": {"actual_path": prime_path, "displacement": displacement,
                                   "translated_second_vertex": fake_repeat,
                                   "translated_second_norm": int(fake_repeat.norm()),
                                   "repeated_source_path_valid": False},
        "controls_rejected": ["drop_scaled_affine_offset", "commute_affine_order",
                              "fixed_depth_unbounded_valuation_decoder",
                              "ignore_intermediate_prime_membership",
                              "repeat_residue_loop_as_prime_cover",
                              "cancel_observed_inverse_excursion",
                              "lower_ambient_precision_bound_by_one"],
        "nonclaims": ["ambient sharpness is not sparse-source sharpness",
                      "no periodic Gaussian-prime cover", "no physical authentication",
                      "no formal logarithm of noncommutative actions",
                      "no analytic completion or RH progress", "no zero-position inputs",
                      "no kernel proof, full suite, CI, compiler or network execution"],
    })


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--receipt", type=Path, required=True)
    args = parser.parse_args()
    result = run()
    args.receipt.write_text(json.dumps(result, sort_keys=True, indent=2) + "\n")
    print(json.dumps({"status": result["status"], "counts": result["counts"],
                      "elapsed_milliseconds": result["elapsed_milliseconds"]}, sort_keys=True))


if __name__ == "__main__":
    main()
