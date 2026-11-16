import unittest
from fractions import Fraction as Q
from math import gcd, isqrt, lcm

import sympy as sp

import cylinder as cy
import prime_observer as po
import prime_waves as pw


def cyclotomic_value(spectrum, modulus, n):
    """Independent symbolic root-of-unity evaluation; no complex tolerance."""
    z = sp.Symbol("z")
    polynomial = sp.Poly(sum(sp.Rational(value.numerator, value.denominator) *
                             z ** ((a * n) % modulus)
                             for a, value in spectrum.items()), z, domain=sp.QQ)
    return polynomial.rem(sp.Poly(sp.cyclotomic_poly(modulus, z), z,
                                  domain=sp.QQ)).as_expr()


class PrimeWaveTests(unittest.TestCase):
    def test_circle_projectors_against_cyclotomic_remainders(self):
        for modulus in range(1, 17):
            spectrum = {j: Q(1, modulus) for j in range(modulus)}
            for n in range(-2, 2 * modulus + 1):
                self.assertEqual(cyclotomic_value(spectrum, modulus, n),
                                 pw.divisor_pulse(modulus, n))

    def test_ramanujan_prime_against_primitive_roots(self):
        for p in (2, 3, 5, 7, 11, 13):
            spectrum = {j: Q(1) for j in range(1, p)}
            for n in range(-1, 2 * p + 1):
                self.assertEqual(cyclotomic_value(spectrum, p, n),
                                 pw.ramanujan_prime(p, n))

    def test_range_projector_and_anchored_braid(self):
        for m in range(1, 13):
            for n in range(1, 97):
                state = cy.multiplier(cy.multiplier({n: 1}, m, adjoint=True), m)
                expected = {n: 1} if pw.divisor_pulse(m, n) else {}
                self.assertEqual(state, expected)
                self.assertEqual(cy.multiplier({n + 1: 1}, m), {m * n + m: 1})
        for m, k in ((4, 6), (2, 3), (3, 9)):
            for n in range(1, 151):
                self.assertEqual(pw.divisor_pulse(m, n) * pw.divisor_pulse(k, n),
                                 pw.divisor_pulse(lcm(m, k), n))

    def test_prime_power_channels_recover_multiplicity(self):
        primes = pw.primes_through(200)
        for n in range(1, 201):
            self.assertEqual(sum(pw.valuation_from_pulses(p, n) for p in primes),
                             cy.omega(n))
        self.assertEqual([pw.divisor_pulse(p, 2) for p in primes],
                         [pw.divisor_pulse(p, 4) for p in primes])
        self.assertNotEqual(pw.valuation_from_pulses(2, 2),
                            pw.valuation_from_pulses(2, 4))

    def test_crt_wave_spectrum_is_the_declared_periodic_field(self):
        for primes in ((), (2,), (3,), (2, 3), (2, 3, 5), (3, 7)):
            modulus, spectrum = pw.survivor_spectrum(primes)
            phi = sum(gcd(n, modulus) == 1 for n in range(modulus))
            for n in range(modulus):
                expected = Q(modulus, phi) if gcd(n, modulus) == 1 else Q(0)
                value = cyclotomic_value(spectrum, modulus, n)
                self.assertEqual(value, sp.Rational(expected.numerator,
                                                    expected.denominator))
            # A reflected correlation has coefficients c_a*c_a, not an
            # unmentioned random-phase average or a sign-free assumption.
            reflected = {a: c * c for a, c in spectrum.items()}
            for target in (-1, 0, 1, 4, 7, 16, 30, 32, 100):
                expected = pw.periodic_pair_receipt(primes, target)[
                    "normalized_correlation"]
                self.assertEqual(cyclotomic_value(reflected, modulus, target),
                                 sp.Rational(expected.numerator, expected.denominator))

    def test_local_pair_correlation_directly(self):
        for p in (2, 3, 5, 7, 11, 13):
            self.assertEqual(sum(pw.survivor_wave(p, n) for n in range(p)), p)
            for target in range(2 * p):
                direct = sum(pw.survivor_wave(p, n) *
                             pw.survivor_wave(p, target - n)
                             for n in range(p)) / p
                self.assertEqual(direct, pw.local_pair_factor(p, target))
        self.assertEqual(pw.local_pair_factor(3, 30), Q(3, 2))
        self.assertEqual(pw.local_pair_factor(3, 32), Q(3, 4))

    def test_complete_period_product_and_finite_interval_are_distinct(self):
        for primes in ((), (2, 3), (2, 3, 5), (2, 3, 5, 7)):
            for target in range(4, 80):
                result = pw.periodic_pair_receipt(primes, target)
                self.assertEqual(result["count"], result["crt_count"])
                self.assertEqual(result["normalized_correlation"],
                                 result["factor_product"])
        result = pw.periodic_pair_receipt((2, 3, 5), 16)
        self.assertEqual(result["residues"], (17, 23, 29))
        self.assertEqual(result["normalized_correlation"], Q(45, 32))
        self.assertEqual(pw.endpoint_decomposition(16, 5)["bulk_pairs"], 0)

    def test_corrected_wave_sieve_against_marking_sieve(self):
        for window in tuple(range(2, 80)) + (257, 1024, 4096):
            self.assertEqual(pw.corrected_prime_mask(window), po.sieve_mask(window))
        self.assertEqual(pw.corrected_prime_mask(49, 5)[49], 1)
        self.assertEqual(pw.corrected_prime_mask(49, 7)[49], 0)
        self.assertEqual(pw.corrected_prime_mask(5, 5)[5], 1)
        self.assertEqual(pw.divisor_pulse(5, 5), 1)

    def test_endpoint_and_odd_target_corrections(self):
        for target in tuple(range(4, 200)) + (514, 997, 1024):
            flags = po.sieve_mask(target - 2)
            for cutoff in (isqrt(target - 2), isqrt(target) + 3):
                row = pw.endpoint_decomposition(target, cutoff)
                self.assertTrue(row["exact_prime_cutoff"])
                self.assertEqual(row["total"], pw.pair_count(flags, target))
        self.assertEqual(pw.endpoint_decomposition(4, 2)["small_pairs"], 1)
        self.assertEqual(pw.endpoint_decomposition(7, 2)["total"], 2)
        self.assertEqual(pw.periodic_pair_receipt((2,), 7)["count"], 0)
        self.assertEqual(pw.endpoint_decomposition(16, 5)["mixed_pairs"], 4)

    def test_homometric_intensity_has_different_sum_fibers(self):
        a, b = pw.HOMOMETRIC_A, pw.HOMOMETRIC_B
        self.assertEqual(pw.difference_histogram(a), pw.difference_histogram(b))
        self.assertEqual((min(a), max(a)), (min(b), max(b)))
        self.assertNotEqual(a, b)
        self.assertNotEqual(tuple(sorted(min(a) + max(a) - x for x in a)), b)
        self.assertEqual(pw.sum_histogram(a).get(8, 0), 2)
        self.assertEqual(pw.sum_histogram(b).get(8, 0), 0)

    def test_finite_phase_bank_counterfeit_and_authentic_braid(self):
        for window in (713, 1024, 2048):
            self.assertEqual(pw.residue_degree_histogram(window, 30),
                             pw.residue_degree_histogram(window, 30, transported=True))
        for n in range(1, 2501):
            self.assertEqual(pw.mod30_relabel(pw.mod30_relabel(n)), n)
            self.assertEqual(pw.mod30_relabel(n) % 30, n % 30)
            for p in (2, 3, 5):
                self.assertEqual(pw.divisor_pulse(p, n),
                                 pw.divisor_pulse(p, pw.mod30_relabel(n)))
        genuine = po.sieve_mask(28)
        fake = (0, 0) + tuple(int(cy.omega(pw.mod30_relabel(n)) == 1)
                             for n in range(2, 29))
        self.assertEqual((pw.pair_count(genuine, 30), pw.pair_count(fake, 30)), (6, 0))
        self.assertEqual(pw.mod30_product(2, 1), 2)
        self.assertEqual(pw.mod30_product(2, 7), 434)
        self.assertEqual(pw.mod30_product(2, 6) + 2, 14)

    def test_coherent_phase_reference_recovers_amplitude(self):
        for real in range(-5, 6):
            for imag in range(-5, 6):
                self.assertEqual(((real + 1) ** 2 + imag ** 2 -
                                  (real - 1) ** 2 - imag ** 2) // 4, real)
                self.assertEqual((real ** 2 + (imag + 1) ** 2 -
                                  real ** 2 - (imag - 1) ** 2) // 4, imag)

    def test_finite_fourier_sampling_alias_and_safe_resolution(self):
        labels = (2, 3, 5, 7)
        ordinary = pw.sum_histogram(labels)
        for modulus in (15, 17, 31):
            cyclic = pw.cyclic_product({p: Q(1) for p in labels},
                                      {p: Q(1) for p in labels}, modulus)
            for target in range(15):
                self.assertEqual(cyclic.get(target, 0), ordinary.get(target, 0))
        aliased = pw.cyclic_product({p: Q(1) for p in labels},
                                   {p: Q(1) for p in labels}, 5)
        self.assertEqual(ordinary.get(4, 0), 1)
        self.assertEqual(aliased[4], 4)  # 2+2, 2+7, 7+2, 7+7.

    def test_prime_modulus_and_exact_input_guards(self):
        for bad in ((2, 2), (4,), (True,), (2.0,)):
            with self.assertRaises(ValueError):
                pw.survivor_spectrum(bad)
        for bad in (0, True, 2.0):
            with self.assertRaises(ValueError):
                pw.divisor_pulse(bad, 10)
        with self.assertRaises(ValueError):
            pw.valuation_from_pulses(2, 0)
        with self.assertRaises(ValueError):
            pw.cyclic_product({0: 0.1}, {0: Q(1)}, 2)
        with self.assertRaises(ValueError):
            pw.cyclic_product({}, {0: 0.1}, 2)
        with self.assertRaises(ValueError):
            pw.pair_count((0, 0, 1), 8)
        for invalid in (0.5, True, 2, Q(1)):
            with self.assertRaises(ValueError):
                pw.pair_count((0, 0, invalid), 4)


if __name__ == "__main__":
    unittest.main()
