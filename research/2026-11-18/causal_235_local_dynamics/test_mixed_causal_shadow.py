"""Exact mixed 2/3 causal-history controls; no pi-value oracle.

This extends SUCC's 2026-11-15 A-FS witness. It is a finite control,
not a counterexample to the fixed zero-seed pi-normality problem.
"""

from fractions import Fraction
from itertools import product
import json
import unittest


def source(n):
    return (Fraction(4, 8*n-7) - Fraction(2, 8*n-4)
            - Fraction(1, 8*n-3) - Fraction(1, 8*n-2))


def prefix(n):
    return sum((source(j) / 16**j for j in range(1, n+1)), Fraction())


def states(seed, n):
    out = [Fraction(seed)]
    for j in range(1, n+1):
        out.append(16*out[-1] + source(j))
    return out


def valuation(q, p):
    q = Fraction(q)
    if not q:
        return float('inf')
    a, b = abs(q.numerator), q.denominator
    v = 0
    while a % p == 0:
        a //= p
        v += 1
    while b % p == 0:
        b //= p
        v -= 1
    return v


def local_report(q, p, depth):
    """Canonical representative of q+p**depth Z_p, including polar part."""
    q = Fraction(q)
    e = max(0, -valuation(Fraction(1, q.denominator), p))
    e = int(e)
    unit_den = q.denominator // p**e
    modulus = p**(depth+e)
    a = q.numerator * pow(unit_den, -1, modulus) % modulus
    return (e, a)


def shadow(word, a=2, b=1):
    if not word or a < 2 or b < 1 or any(c not in range(4) for c in word):
        raise ValueError('Require a nonempty 0..3 word, a>=2 and b>=1')
    n = len(word)
    digit_integer = 0
    for c in word:
        digit_integer = 16*digit_integer + 4+c
    beta = Fraction(digit_integer, 16**n-1)
    modulus = 2**a * 3**b
    denominator = 256*modulus*16**n+1
    target = (beta-prefix(n+1))*denominator/modulus
    rounded = (target+Fraction(1, 2)).__floor__()
    seed = Fraction(modulus*rounded, denominator)
    return seed, beta, denominator


def local_transcript(seed, n):
    """Adaptive finite policy: next depths depend only on previous reports."""
    out = []
    depth2, depth3 = 4, 3
    for j, u in enumerate(states(seed, n)):
        r2 = local_report(u, 2, depth2)
        r3 = local_report(u, 3, depth3)
        out.append((j, depth2, depth3, r2, r3))
        depth2 = 2 + (r2[1] + j) % 11
        depth3 = 1 + (r3[1] + 2*j) % 7
    return out


class MixedCausalShadow(unittest.TestCase):
    def test_every_word_through_depth_five(self):
        for n in range(1, 6):
            original = states(0, n)
            for word in product(range(4), repeat=n):
                seed, _, height_bound = shadow(word)
                changed = states(seed, n)
                self.assertTrue(0 < seed < 1)
                self.assertLessEqual(max(abs(seed.numerator), seed.denominator), height_bound)
                self.assertEqual(tuple(x.__floor__() % 4 for x in changed[1:]), word)
                for j, (u, v) in enumerate(zip(original, changed)):
                    self.assertEqual(v-u, 16**j*seed)
                    self.assertGreaterEqual(valuation(v-u, 2), 2+4*j)
                    self.assertGreaterEqual(valuation(v-u, 3), 1)

    def test_fresh_long_patterns_and_polar_reports(self):
        for n, a, b in [(7, 5, 3), (19, 11, 7), (48, 17, 9)]:
            word = tuple((j*j + 3*j + n) % 4 for j in range(n))
            seed, beta, _ = shadow(word, a, b)
            original, changed = states(0, n), states(seed, n)
            for j in range(n+1):
                self.assertEqual(local_report(original[j], 2, a+4*j),
                                 local_report(changed[j], 2, a+4*j))
                self.assertEqual(local_report(original[j], 3, b),
                                 local_report(changed[j], 3, b))
                if j:
                    self.assertEqual(changed[j].__floor__() % 4, word[j-1])
                    self.assertEqual(changed[j].__floor__(), (16**j*beta).__floor__())

    def test_finite_adaptive_memory_policy(self):
        n = 33
        reference = local_transcript(0, n)
        a = max(2, max(d2-4*j for j, d2, _, _, _ in reference))
        b = max(1, max(d3 for _, _, d3, _, _ in reference))
        seed, _, _ = shadow((0,)*n, a, b)
        self.assertEqual(local_transcript(seed, n), reference)
        self.assertTrue(all(x.__floor__() % 4 == 0 for x in states(seed, n)[1:]))
        # The exact seed predicate discriminates; it is not a finite residue query.
        self.assertNotEqual(seed == 0, True)
        # A real carry report discriminates: no false all-observer claim.
        self.assertTrue(any(x.__floor__() % 4 != 0 for x in states(0, n)[1:]))

    def test_controls_and_reconstruction_boundary(self):
        word = (0, 0, 0, 0)
        seed, _, _ = shadow(word, 8, 6)
        # One unauthorized local perturbation breaks an observed congruence.
        mutated = seed + Fraction(1, 2**9)
        self.assertNotEqual(local_report(seed, 2, 8), local_report(mutated, 2, 8))
        # Existing bounded-height CRT theorem, also valid with explicit pole parts.
        h = 5
        candidates = {Fraction(a, b) for a in range(-h, h+1) for b in range(1, h+1)}
        reports = {}
        self.assertGreater(2**3*3**2, 2*h*h)
        for q in candidates:
            key = (local_report(q, 2, 3), local_report(q, 3, 2))
            self.assertNotIn(key, reports)
            reports[key] = q
        # Dropping height admits arbitrarily different real values in the same fibers.
        self.assertEqual(local_report(0, 2, 3), local_report(72, 2, 3))
        self.assertEqual(local_report(0, 3, 2), local_report(72, 3, 2))


if __name__ == '__main__':
    unittest.main(verbosity=2)
