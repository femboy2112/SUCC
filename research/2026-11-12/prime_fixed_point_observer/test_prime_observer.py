"""Independent arithmetic checks and calibrated false-claim regressions."""
import copy
from fractions import Fraction as Q
from itertools import islice
from math import isqrt
import unittest

import prime_observer as po


class CategoryTests(unittest.TestCase):
    def test_fixed_objects_and_functoriality(self):
        primes = po.sieve_mask(512)
        for n in range(1, 513):
            self.assertEqual(po.divisor_functor(n) == n, n == 1 or bool(primes[n]))
        for a in range(1, 65):
            for b in range(a, 513, a):
                self.assertEqual(po.divisor_functor(b) % po.divisor_functor(a), 0)

    def test_div_retraction_obstruction(self):
        self.assertEqual(6 % 3, 0)
        self.assertEqual(po.least_divisor(6), 2)
        self.assertNotEqual(po.least_divisor(6) % po.least_divisor(3), 0)
        self.assertEqual([po.divisor_functor(n) for n in (4, 16)], [16, 65536])

    def test_prime_closure_adjunction_and_productivity(self):
        primes = po.sieve_mask(600)
        expected = [n for n in range(2, 601) if primes[n]]
        self.assertEqual(list(islice(po.prime_stream(), len(expected))), expected)
        for n in range(2, 500):
            c = po.prime_ceiling(n)
            self.assertGreaterEqual(c, n)
            self.assertEqual(po.prime_ceiling(c), c)
            self.assertEqual(c, min(p for p in expected if p >= n))
            self.assertEqual(po.least_divisor(po.least_divisor(n)), po.least_divisor(n))
            for p in expected[:25]:
                self.assertEqual(c <= p, n <= p)

    def test_factor_coalgebra_coassociativity(self):
        def divisors(n):
            return [d for d in range(1, n + 1) if n % d == 0]
        for n in range(1, 129):
            left = sorted((a, b // a, n // b) for b in divisors(n) for a in divisors(b))
            right = sorted((n // b, a, b // a) for b in divisors(n) for a in divisors(b))
            self.assertEqual(left, right)
            if n >= 2:
                self.assertEqual(po.factor_energy(n), len(divisors(n)) - 2)

    def test_not_a_bialgebra_with_usual_product(self):
        # In Delta(4), (2,2) occurs once; in Delta(2)^2, it occurs twice.
        self.assertEqual(po.proper_factorizations(4), ((2, 2),))
        products = [(a * c, b * d) for a, b in ((1, 2), (2, 1))
                    for c, d in ((1, 2), (2, 1))]
        self.assertEqual(products.count((2, 2)), 2)


class CertificateTests(unittest.TestCase):
    def test_divisor_source_receipts(self):
        for n in range(2, 257):
            self.assertTrue(po.verify_divisor_receipt(po.divisor_receipt(n)))

    def test_forged_source_rejected(self):
        r = po.divisor_receipt(49)
        for key, value in (("pairs", []), ("energy", 0), ("prime", True),
                           ("n", 1), ("n", True), ("energy", True)):
            mutated = dict(r, **{key: value})
            self.assertFalse(po.verify_divisor_receipt(mutated))
        r["pairs"].append([7, 7])
        self.assertFalse(po.verify_divisor_receipt(r))

    def test_screen_threshold_and_omitted_square(self):
        flags = po.sieve_mask(2048)
        for cutoff in range(1, 32):
            for n in range(2, (cutoff + 1) ** 2):
                self.assertEqual(po.screened(n, cutoff), flags[n])
        self.assertEqual(po.screened(49, 5), 1)
        self.assertEqual(po.screened(49, 7), 0)
        self.assertEqual(po.screened(7, 7), 1)  # only proper factors are removed

    def test_uniform_filter_error_and_sharp_squares(self):
        flags = po.sieve_mask(1000)
        for n in range(2, 1001):
            for r in (0, 1, 2, 7):
                error = Q(1, (1 + po.factor_energy(n)) ** r) - flags[n]
                self.assertLessEqual(error, Q(1, 2 ** r))
                self.assertGreaterEqual(error, 0)
        for p in (2, 3, 5, 17, 31):
            self.assertEqual(Q(1, (1 + po.factor_energy(p * p)) ** 7), Q(1, 128))

    def test_spectral_floor_against_marking_sieve(self):
        for N in tuple(range(4, 130, 2)) + (256, 512, 1000, 2048):
            primes = po.sieve_mask(N)
            expected = sum(primes[k] * primes[N - k] for k in range(2, N - 1))
            receipt = po.pair_spectral_receipt(N)
            self.assertEqual(receipt["floor"], expected)
            self.assertEqual(receipt["zero_modes"], expected)
            self.assertLess(Q(receipt["trace"]) - expected, 1)
            self.assertTrue(receipt["floor_recovery_certified"])
        for N in (4, 20, 100, 256):
            self.assertTrue(po.verify_pair_spectral_receipt(po.pair_spectral_receipt(N)))

    def test_forged_spectral_receipt_rejected(self):
        good = po.pair_spectral_receipt(100)
        for key, value in (("N", 102), ("r", True), ("trace", "13"),
                           ("zero_modes", 0), ("floor", 13),
                           ("source", "unlabelled"), ("dimension", True),
                           ("floor_recovery_certified", False),
                           ("universal_goldbach_proved", True)):
            self.assertFalse(po.verify_pair_spectral_receipt(dict(good, **{key: value})))
        changed = copy.deepcopy(good)
        changed["energy_histogram"]["0"] += 1
        self.assertFalse(po.verify_pair_spectral_receipt(changed))
        class ForgedSource:
            def __eq__(self, other):
                return True
        self.assertFalse(po.verify_pair_spectral_receipt(
            dict(po.pair_spectral_receipt(100, transported=True), source=ForgedSource())))

    def test_underresolved_positive_trace_not_a_witness(self):
        receipt = po.pair_spectral_receipt(100, 0, transported=True)
        self.assertGreater(Q(receipt["trace"]), 0)
        self.assertEqual(receipt["zero_modes"], 0)
        self.assertFalse(receipt["floor_recovery_certified"])
        resolved = po.pair_spectral_receipt(100, transported=True)
        self.assertGreater(Q(resolved["trace"]), 0)
        self.assertEqual(resolved["floor"], 0)
        self.assertTrue(po.verify_pair_spectral_receipt(resolved))


class ReflectionTests(unittest.TestCase):
    def test_reflection_commutator_for_every_small_mask(self):
        # Exhaust all binary sources of odd size through 9, not just primes.
        for length in (1, 3, 5, 7, 9):
            for bits in range(1 << length):
                a = tuple((bits >> k) & 1 for k in range(length))
                result = po.reflection_statistics(a)
                R, m = result["ordered_pairs"], sum(a)
                self.assertEqual(result["commutator_hs_squared"], 2 * (m - R))
                self.assertEqual(result["eigen_plus"] + result["eigen_minus"], R)
                self.assertEqual(result["eigen_plus"] - result["eigen_minus"], a[length // 2])
                # A=PJP sends e_k to a[k]*a[-k-1] e_(-k-1).
                for k in range(length):
                    coef = a[k] * a[length - 1 - k]
                    self.assertEqual(coef ** 3, coef)
                    # Both P and JPJ are diagonal: this commutator is vacuous.
                    self.assertEqual(a[k] * a[length - 1 - k] - a[length - 1 - k] * a[k], 0)

    def test_genuine_haar_plus_minus_blocks(self):
        primes = po.sieve_mask(100)
        stats = po.reflection_statistics(primes[2:99])
        self.assertEqual((stats["prime_sector"], stats["ordered_pairs"],
                          stats["commutator_hs_squared"]), (25, 12, 26))
        self.assertEqual((stats["eigen_plus"], stats["eigen_minus"]), (6, 6))

    def test_transported_multiplication_breaks_only_untransported_addition(self):
        for n in range(1, 300):
            self.assertEqual(po.relabel(po.relabel(n)), n)
            self.assertEqual(po.relabel(n) % 2, n % 2)
        for a in range(1, 12):
            for b in range(1, 12):
                for c in range(1, 12):
                    self.assertEqual(po.transported_product(po.transported_product(a, b), c),
                                     po.transported_product(a, po.transported_product(b, c)))
        fake = tuple(int(po.transported_energy(k) == 0) for k in range(2, 99))
        actual = po.sieve_mask(100)[2:99]
        self.assertEqual(sum(fake), sum(actual))
        self.assertEqual(sum(fake[::2]), sum(actual[::2]))  # even k
        self.assertEqual(po.reflection_statistics(fake)["ordered_pairs"], 0)
        self.assertEqual(po.transported_product(2, 9), 106)
        self.assertEqual(po.transported_product(2, 8) + 2, 18)
        # Transporting addition too restores the corresponding pair 3+97=100.
        transported_sum = po.relabel(po.relabel(3) + po.relabel(49))
        self.assertEqual(transported_sum, 100)


class HaarTests(unittest.TestCase):
    def test_haar_parseval_all_small_sources(self):
        for size in (1, 2, 3, 4):
            for x in range(1 << size):
                for y in range(1 << size):
                    a = [(x >> k) & 1 for k in range(size)]
                    b = [(y >> k) & 1 for k in range(size)]
                    r = po.haar_overlap(a, b)
                    self.assertEqual(Q(r["constant"]) + Q(r["detail"]), r["overlap"])

    def test_parity_quotient_and_finest_band(self):
        for n in range(3, 257):
            a, b = po.midpoint_masks(n)
            # Remove the singleton prime 2 before claiming a parity support law.
            a = tuple(x if (n + d) % 2 else 0 for d, x in enumerate(a))
            b = tuple(x if (n - d) % 2 else 0 for d, x in enumerate(b))
            r = po.haar_overlap(a, b)
            self.assertEqual(Q(r["bands"]["2"]), Q(r["overlap"], 2))
            q = po.haar_overlap(*po.midpoint_masks(n, quotient_parity=True))
            self.assertEqual(q["overlap"], r["overlap"])

    def test_crt_bounds_refinement_and_sharp_counterfeit(self):
        for n in (20, 100, 257, 1024):
            for z in (2, 3, 5, 7):
                prev_lo, prev_hi = 0, n
                for width in (128, 64, 32, 16, 8, 4, 2, 1):
                    c = po.crt_haar_certificate(n, z, width)
                    self.assertLessEqual(c["lower"], c["interior_actual"])
                    self.assertLessEqual(c["interior_actual"], c["upper"])
                    self.assertLessEqual(c["interior_actual"], c["full_unordered_count"])
                    self.assertGreaterEqual(c["lower"], prev_lo)
                    self.assertLessEqual(c["upper"], prev_hi)
                    self.assertEqual(po.minimum_overlap_model(c)["overlap"], c["lower"])
                    self.assertLessEqual(c["lower"], c["coherent_lower"])
                    self.assertLessEqual(c["coherent_lower"], c["interior_actual"])
                    self.assertEqual(po.minimum_overlap_model(c, preserve_center=True)["overlap"],
                                     c["coherent_lower"])
                    prev_lo, prev_hi = c["lower"], c["upper"]
                self.assertEqual(prev_lo, c["interior_actual"])
                self.assertEqual(prev_hi, c["interior_actual"])

    def test_prior_coarse_observer_counterfeit(self):
        c = po.crt_haar_certificate(1024, 2, 128)
        fake = po.minimum_overlap_model(c)
        self.assertEqual(c["interior_actual"], 25)
        self.assertEqual(fake["overlap"], 0)
        self.assertEqual(sum(r["A"] for r in c["rows"]), 137)
        self.assertEqual(sum(r["B"] for r in c["rows"]), 171)

    def test_shared_center_strengthens_the_relaxed_bound(self):
        c = po.crt_haar_certificate(9, 2, 4)
        first = c["rows"][0]
        self.assertEqual((first["capacity"], first["A"], first["B"]), (2, 1, 1))
        self.assertEqual((first["center_bit"], first["lower"], first["coherent_lower"]), (0, 0, 1))
        coherent = po.minimum_overlap_model(c, preserve_center=True)
        self.assertEqual(coherent["cells"][0]["a"][0], 0)
        self.assertEqual(coherent["cells"][0]["b"][0], 0)
        self.assertEqual(coherent["overlap"], c["coherent_lower"])

    def test_boundaries_and_invalid_types(self):
        self.assertEqual(po.pair_spectral_receipt(4)["floor"], 1)
        self.assertEqual(po.divisor_functor(1), 1)
        for x in (True, False, 1.0, -1, "7"):
            for f in (po.tau, po.factor_energy, po.least_divisor, po.prime_ceiling):
                with self.assertRaises(ValueError):
                    f(x)
        with self.assertRaises(ValueError):
            po.factor_energy(1)
        with self.assertRaises(ValueError):
            po.pair_spectral_receipt(5)
        with self.assertRaises(ValueError):
            po.crt_haar_certificate(10, 3, 3)
        with self.assertRaises(ValueError):
            po.haar_overlap([True], [1])


if __name__ == "__main__":
    unittest.main()
