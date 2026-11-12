import unittest
from fractions import Fraction as Q
from math import isqrt
import sympy as sp

import cylinder as cy
import prime_observer as po


class CylinderTests(unittest.TestCase):
    def test_omega_and_commutator_arithmetic(self):
        flags = po.sieve_mask(10000)
        for n in range(1, 10001):
            self.assertEqual(cy.omega(n) == 1, bool(flags[n]))
        for a in range(1, 65):
            for b in range(1, 65):
                self.assertEqual(cy.omega(a * b) - cy.omega(b), cy.omega(a))

    def test_character_average_independent_cyclotomic_remainders(self):
        z = sp.Symbol("z")
        for clock in range(1, 13):
            modulus = sp.Poly(sp.cyclotomic_poly(clock, z), z, domain=sp.QQ)
            for charge in range(0, 3 * clock + 1):
                for target in (0, 1, 2):
                    exponent = (charge - target) % clock
                    polynomial = sp.Poly(sum(z ** ((j * exponent) % clock)
                                             for j in range(clock)), z, domain=sp.QQ)
                    remainder = polynomial.rem(modulus)
                    self.assertEqual(remainder.as_expr(),
                                     clock * cy.character_average(charge, clock, target))

    def test_finite_clock_alias_and_adaptive_resolution(self):
        for clock in range(2, 21):
            n = 2 ** (clock + 1)
            self.assertGreater(cy.omega(n), 1)
            self.assertEqual(cy.character_average(cy.omega(n), clock, 1), 1)
            self.assertEqual(cy.character_average(cy.omega(n), clock + 1, 1), 0)
        for window in (2, 3, 4, 16, 31, 64, 1000, 10000):
            flags = po.sieve_mask(window)
            clock = cy.single_clock_bound(window)
            for n in range(1, window + 1):
                self.assertEqual(cy.character_average(cy.omega(n), clock, 1), flags[n])

    def test_same_and_opposite_pair_twists(self):
        for N in tuple(range(4, 258, 2)) + (1000, 2048):
            row = cy.pair_twist_receipt(N)
            flags = po.sieve_mask(N)
            expected = sum(flags[k] * flags[N - k] for k in range(2, N - 1))
            self.assertEqual(row["same_orientation_exact_pairs"], expected)
            self.assertEqual(row["same_orientation_clock_survivors"], expected)
        self.assertEqual(cy.omega(4) - cy.omega(4), 0)  # false opposite-twist survivor
        self.assertEqual(cy.omega(4) + cy.omega(4), 4)  # rejected by degree-2 projection
        self.assertGreater(cy.pair_twist_receipt(8)["opposite_orientation_survivors"], 2)
        # A match in the proper-divisor grading need not match Omega.
        self.assertEqual(po.factor_energy(6), po.factor_energy(8))
        self.assertNotEqual(cy.omega(6), cy.omega(8))

    def test_unit_sector_must_be_excluded_for_pairs(self):
        self.assertEqual(cy.omega(1) + cy.omega(9), 2)
        self.assertEqual(po.factor_energy(9), 1)

    def test_wiggle_conjugation_is_not_prime_projection(self):
        self.assertIn((14, 15), cy.wiggle_edges(100, 1))
        self.assertIn((33, 35), cy.wiggle_edges(100, 2))
        self.assertNotIn((33, 35), cy.wiggle_edges(100, 2, prime_only=True))
        self.assertEqual(cy.wiggle_edges(1000, 1, prime_only=True), [(2, 3)])
        self.assertIn((11, 13), cy.wiggle_edges(100, 2, prime_only=True))

    def test_prime_transfer_needs_intermediate_sectors(self):
        for p, q in ((2, 3), (3, 5), (5, 11)):
            for r in (2, 3, 5, 7, 11, 13):
                state = {r: 1}
                self.assertEqual(cy.prime_compress(cy.multiplicative_wiggle(state, p)), {})
                result = cy.prime_compress(cy.multiplicative_wiggle(cy.multiplicative_wiggle(state, q), p))
                expected = {p: 1} if r == q else ({q: 1} if r == p else {})
                self.assertEqual(result, expected)
                matrix_unit = cy.prime_compress(cy.multiplier(cy.multiplier(state, q, adjoint=True), p))
                self.assertEqual(matrix_unit, {p: 1} if r == q else {})
        self.assertEqual(cy.multiplier({5: 1}, 5, adjoint=True), {1: 1})
        self.assertEqual(cy.multiplier({5: 1}, 3), {15: 1})
        self.assertEqual(cy.prime_compress(cy.multiplicative_wiggle(cy.multiplicative_wiggle({3: 1}, 3), 3)), {3: 2})
        self.assertEqual(cy.prime_compress(cy.multiplicative_wiggle(cy.multiplicative_wiggle({5: 1}, 3), 3)), {5: 1})

    def test_full_operator_fixed_space_is_larger_than_prime_multipliers(self):
        self.assertEqual(cy.omega(8) - cy.omega(4), 1)
        self.assertNotEqual(cy.omega(8), 1)
        self.assertNotEqual(cy.omega(4), 1)

    def test_additive_shear_lower_bound_on_power_of_two_seams(self):
        for k in range(2, 17):
            previous = cy.omega(2 ** k - 1)
            self.assertLessEqual(3 ** previous, 2 ** k - 1)
            self.assertEqual(cy.omega(2 ** k), k)

    def test_undersampled_pair_alias(self):
        self.assertGreater(cy.pair_twist_receipt(32, clock=6)["alias_count"], 0)

    def test_interposed_twist_resolves_vacuum_and_semiprime_routes(self):
        for p, q in ((2, 3), (3, 5), (5, 11)):
            self.assertEqual(cy.twisted_transfer_charges(p, q, q), {p: {0: 1}})
            self.assertEqual(cy.twisted_transfer_charges(p, q, p), {q: {2: 1}})
        z = sp.Symbol('z', nonzero=True)
        block = sp.Matrix([[0, 1/z], [z, 0]])
        self.assertEqual(block ** 2, sp.eye(2))
        self.assertEqual(sp.expand(block.det()), -1)

    def test_fejer_weights_and_integer_diophantine_certificate(self):
        for steps in range(1, 33):
            expected = {}
            for j in range(steps):
                for k in range(steps):
                    expected[j-k] = expected.get(j-k, Q()) + Q(1, steps*steps)
            self.assertEqual(cy.fejer_weights(steps), expected)
            self.assertEqual(sum(expected.values()), 1)
        for c in range(1, 1001):
            lower = isqrt(2*c*c)
            for m in (lower, lower+1):
                self.assertGreaterEqual(abs(2*c*c - m*m), 1)
                self.assertLessEqual(m, 2*c)
        self.assertEqual(cy.fejer_window_error(10000, 256), Q(9, 1024))
        self.assertEqual(cy.fejer_window_error(3, 1), 0)

    def test_complete_single_cylinder_spectrum_does_not_fix_pairs(self):
        from collections import Counter
        self.assertEqual(Counter(cy.omega(n) for n in range(2, 99)),
                         Counter(cy.omega(po.relabel(n)) for n in range(2, 99)))
        actual = sum(cy.omega(k)+cy.omega(100-k)==2 for k in range(2, 99))
        fake = sum(cy.omega(po.relabel(k))+cy.omega(po.relabel(100-k))==2
                   for k in range(2, 99))
        self.assertEqual((actual, fake), (12, 0))

    def test_invalid_inputs(self):
        for n in (True, 1.0, "2", 0, -1):
            with self.assertRaises(ValueError):
                cy.omega(n)
        with self.assertRaises(ValueError):
            cy.character_average(1, 0)
        with self.assertRaises(ValueError):
            cy.pair_twist_receipt(5)


if __name__ == "__main__":
    unittest.main()
