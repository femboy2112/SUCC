"""Independent exact arithmetic checks for the cloud ABC paper proof."""
import unittest
from fractions import Fraction
from math import gcd

from observational_succ.cloud_abc_correlations import (
    density_upper, divisors, g_integer, inner_expansion, low_ris_divisor_gate,
    mobius, moment_budget, packing_upper, powerful, powerful_singleton_witness,
    primitive_divisor_count, primitive_pair_count, progression_count,
    primitive_density_multiplier,
    triple_expansion,
)


def independent_rad(n):
    # Trial division implemented here, independently of repository factor helpers.
    p, result = 2, 1
    while p*p <= n:
        if n % p == 0:
            result *= p
            while n % p == 0:
                n //= p
        p += 1
    return result * n


def independent_ris(n):
    return n // independent_rad(n)


def brute_triples(X, d=1, e=1, f=1):
    return [(a, b, a+b) for a in range(1, X) for b in range(1, X-a+1)
            if gcd(a, b) == 1 and a % d == 0 and b % e == 0 and (a+b) % f == 0]


class CloudABCCorrelationsTests(unittest.TestCase):
    def test_divisor_expansion_vs_independent_radical(self):
        for n in range(1, 351):
            for t in (0, 1, 2):
                self.assertEqual(sum(g_integer(d, t) for d in divisors(n)), independent_ris(n)**t)
                self.assertGreaterEqual(g_integer(n, t), 0)
                if g_integer(n, t):
                    self.assertTrue(powerful(n))

    def test_mobius_calibration(self):
        for n in range(1, 101):
            self.assertEqual(sum(mobius(d) for d in divisors(n)), int(n == 1))

    def test_general_crt_floor_count_exhaustive(self):
        for c in range(1, 46):
            for d in range(1, 14):
                for e in range(1, 14):
                    expected = sum(a % d == 0 and (c-a) % e == 0 for a in range(1, c))
                    self.assertEqual(progression_count(c, d, e), expected)

    def test_global_primitive_mobius_count_exhaustive(self):
        for c in range(1, 46):
            for d in range(1, 12):
                for e in range(1, 12):
                    expected = sum(a % d == 0 and (c-a) % e == 0 and gcd(a, c) == 1
                                   for a in range(1, c))
                    self.assertEqual(primitive_pair_count(c, d, e), expected)

    def test_inner_expansion_both_domains(self):
        for c in range(2, 36):
            for t in (0, 1, 2):
                for primitive in (False, True):
                    expected = sum(independent_ris(a)**t * independent_ris(c-a)**t
                                   for a in range(1, c) if not primitive or gcd(a, c) == 1)
                    self.assertEqual(inner_expansion(c, t, primitive=primitive), expected)

    def test_three_divisor_expansion_independent_route(self):
        for X in (2, 9, 17, 24, 31):
            for t in (0, 1, 2):
                expected = sum(independent_ris(a*b*c)**t for a, b, c in brute_triples(X))
                self.assertEqual(triple_expansion(X, t), expected)

    def test_packing_count_and_determinants(self):
        X = 43  # fresh cutoff, not used to choose the theorem
        for d in (1, 2, 4, 8, 9):
            for e in (1, 3, 5, 7, 25):
                for f in (1, 2, 5, 11, 49):
                    points = brute_triples(X, d, e, f)
                    self.assertEqual(primitive_divisor_count(X, d, e, f), len(points))
                    if any(gcd(x, y) != 1 for x, y in ((d, e), (d, f), (e, f))):
                        self.assertEqual(points, [])
                        continue
                    self.assertLessEqual(len(points), packing_upper(X, d, e, f))
                    slopes = sorted(Fraction(a, c) for a, b, c in points)
                    self.assertEqual(len(slopes), len(set(slopes)))
                    for left, right in zip(slopes, slopes[1:]):
                        self.assertGreaterEqual(right-left, Fraction(d*e*f, X*X))
                    if d*e*f <= X*X:
                        self.assertLessEqual(len(points), density_upper(X, d, e, f))

    def test_powerful_gate_with_unbalanced_and_deep_inputs(self):
        triples = brute_triples(48) + [(1, 2**k-1, 2**k) for k in range(2, 11)]
        triples += [(441, 400, 841), (32, 49, 81), (169, 343, 512)]
        for a, b, c in triples:
            ds = [d for d in divisors(a) if powerful(d)]
            es = [e for e in divisors(b) if powerful(e)]
            fs = [f for f in divisors(c) if powerful(f)]
            H = independent_ris(a*b*c)
            for d in ds:
                for e in es:
                    for f in fs:
                        self.assertTrue(low_ris_divisor_gate(a, b, d, e, f))
                        if H <= c:
                            self.assertLessEqual(d*e*f, c*c)

    def test_high_determinant_singleton_negative_control(self):
        w = powerful_singleton_witness()
        self.assertTrue(w["all_powerful"])
        self.assertTrue(w["refutes_density_only"])
        self.assertEqual(w["primitive_count"], 1)
        with self.assertRaises(ValueError):
            density_upper(841, 441, 400, 841)

    def test_primitivity_is_load_bearing(self):
        # (n,n,2n) all has slope 1/2; its ris(abc)>=n² for EVERY n.
        slopes = [Fraction(n, 2*n) for n in range(1, 101)]
        self.assertEqual(len(set(slopes)), 1)
        for n in range(1, 101):
            self.assertGreaterEqual(independent_ris(2*n**3), n*n)
        X, d, e, f = 34, 8, 9, 17
        raw = [(a, b, a+b) for a in range(1, X) for b in range(1, X-a+1)
               if a % d == 0 and b % e == 0 and (a+b) % f == 0]
        self.assertEqual(raw, [(8, 9, 17), (16, 18, 34)])
        self.assertGreater(len(raw), packing_upper(X, d, e, f))
        self.assertEqual(primitive_divisor_count(X, d, e, f), 1)

    def test_radical_pair_tail_pigeonhole_exact(self):
        for a, b, c in brute_triples(70):
            ra, rb, rc = map(independent_rad, (a, b, c))
            R = ra*rb*rc
            minimum = min(ra*rb, ra*rc, rb*rc)
            self.assertLessEqual(minimum**3, R**2)
            self.assertEqual(R*independent_ris(a*b*c), a*b*c)
            self.assertLessEqual(a*b*c, c**3)

    def test_rankin_euler_factor_by_finite_geometric_identity(self):
        # eta=1 makes everything rational. Independent finite coprime pair
        # enumeration over powers is compared with the elementary local sum.
        for p in (2, 3, 7):
            for depth in (1, 3, 7):
                vals = [p**k for k in range(depth+1)]
                direct = sum(Fraction(1, m*n*independent_rad(m)*independent_rad(n))
                             for m in vals for n in vals if gcd(m, n) == 1)
                local = 1 + 2*sum(Fraction(1, p**(k+1)) for k in range(1, depth+1))
                self.assertEqual(direct, local)
                self.assertLess(direct, 1+Fraction(2, p*(p-1)))

    def test_explicit_constant_scope_and_exact_exponent_balance(self):
        for t in (0, Fraction(1, 2), Fraction(3, 5), Fraction(13, 20)):
            budget = moment_budget(t)
            self.assertEqual(2 + 2*budget.eta + budget.t - Fraction(2, 3), 2)
            self.assertGreater(budget.low_power, 0)
            self.assertGreater(budget.tail_power, 0)
        for t in (Fraction(2, 3), 1, Fraction(-1, 10), 0.5, True):
            with self.assertRaises(ValueError):
                moment_budget(t)

    def test_fixed_divisor_local_density_independent_residue_census(self):
        for p in (2, 3, 5):
            for k in (1, 2, 3):
                q = p**k
                total = q*q
                for slot in (0, 1, 2):
                    count = sum((a, b, a+b)[slot] % q == 0 and not (a % p == b % p == 0)
                                for a in range(q) for b in range(q))
                    self.assertEqual(Fraction(count, total), Fraction(p-1, p*q))
                    moduli = [1, 1, 1]
                    moduli[slot] = q
                    conditional = Fraction(count, total) / (1-Fraction(1, p*p))
                    self.assertEqual(conditional, primitive_density_multiplier(*moduli))
        self.assertEqual(primitive_density_multiplier(4, 9, 25), Fraction(1, 2160))
        self.assertEqual(primitive_density_multiplier(2, 4, 1), 0)

    def test_input_controls(self):
        for args in ((0, 1, 1), (4, 0, 1), (4, 1, False)):
            with self.assertRaises(ValueError):
                progression_count(*args)
        with self.assertRaises(ValueError):
            packing_upper(10, 2, 4, 1)
        with self.assertRaises(ValueError):
            low_ris_divisor_gate(2, 3, 2, 1, 1)
        with self.assertRaises(ValueError):
            g_integer(4, Fraction(1, 2))


if __name__ == "__main__":
    unittest.main()
