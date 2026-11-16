"""Exact controls for negative-order causal and Mellin readouts."""
from fractions import Fraction as Q
from math import comb, factorial
import unittest

from observational_succ import causal_negative_orders as c
from observational_succ.bbp_dirichlet_resolvent import zeta_nonpositive
from observational_succ.euler_bbp_regulator import source_power_term


class CausalDifferenceTests(unittest.TestCase):
    def test_forward_support_and_total_variation(self):
        for m in range(9):
            for h in (Q(1), Q(1, 7), Q(3, 11)):
                atoms = c.forward_delta_difference(m, h)
                self.assertTrue(all(a.lag >= 0 for a in atoms))
                self.assertEqual(sum(abs(a.coefficient) for a in atoms),
                                 c.delta_difference_noise_gain(m, h))

    def test_polynomial_annihilation_and_orientation(self):
        for m in range(1, 10):
            atoms = c.forward_delta_difference(m, Q(2, 13))
            for degree in range(m):
                self.assertEqual(c.polynomial_atom_pairing(atoms, (0,)*degree+(1,)), 0)
            self.assertEqual(c.polynomial_atom_pairing(atoms, (0,)*m+(1,)),
                             (-1)**m*factorial(m))

    def test_next_degree_attains_error_bound(self):
        for m in range(1, 10):
            h = Q(1, 17)
            actual = abs(c.polynomial_atom_pairing(c.forward_delta_difference(m, h),
                                                   (0,)*(m+1)+(1,)))
            self.assertEqual(actual, c.delta_difference_error_bound(m, h, factorial(m+1)))

    def test_general_polynomial_error(self):
        for m in range(1, 6):
            h = Q(1, 19)
            polynomial = tuple(Q((-1)**j, j+1) for j in range(m+4))
            atoms = c.forward_delta_difference(m, h)
            observed = c.polynomial_atom_pairing(atoms, polynomial)
            target = (-1)**m*factorial(m)*polynomial[m]
            # A valid derivative bound on the complete sampled interval.
            bound = sum((abs(polynomial[j])*Q(factorial(j), factorial(j-m-1))
                         *(m*h)**(j-m-1) for j in range(m+1, len(polynomial))), Q())
            self.assertLessEqual(abs(observed-target), c.delta_difference_error_bound(m, h, bound))

    def test_independent_noise_attains_gain(self):
        eta = Q(1, 1000)
        for m in range(9):
            atoms = c.forward_delta_difference(m, Q(1, 5))
            observed_error = sum((a.coefficient*eta*(-1)**j for j, a in enumerate(atoms)), Q())
            self.assertEqual(observed_error, eta*c.delta_difference_noise_gain(m, Q(1, 5)))

    def test_zero_order_is_identity(self):
        self.assertEqual(c.forward_delta_difference(0, Q(7, 3)), (c.CausalAtom(Q(0), Q(1)),))
        self.assertEqual(c.delta_difference_error_bound(0, 1, 17), 0)
        self.assertEqual(c.negative_order_pairing(0, (9,), 11), 9)

    def test_tempered_convolution_binomial(self):
        for lam in (Q(0), Q(1), Q(3, 7)):
            for m in range(6):
                for n in range(6):
                    left, right = c.tempered_negative_coefficients(m, lam), c.tempered_negative_coefficients(n, lam)
                    product = tuple(sum((left[i]*right[k-i] for i in range(m+1)
                                         if 0 <= k-i <= n), Q()) for k in range(m+n+1))
                    self.assertEqual(product, c.tempered_negative_coefficients(m+n, lam))

    def test_exponential_test_jet(self):
        for m in range(12):
            a, lam = Q(7, 3), Q(2, 5)
            self.assertEqual(c.negative_order_pairing(m, tuple((-a)**j for j in range(m+1)), lam),
                             (a+lam)**m)

    def test_sign_mutation_and_positive_measure_mutation(self):
        atoms = c.forward_delta_difference(1, Q(1, 8))
        self.assertEqual(c.polynomial_atom_pairing(atoms, (0, 1)), -1)
        self.assertNotEqual(c.polynomial_atom_pairing(atoms, (0, 1)), 1)
        positive = tuple(c.CausalAtom(a.lag, abs(a.coefficient)) for a in atoms)
        self.assertNotEqual(c.polynomial_atom_pairing(positive, (1,)), 0)


class SourceMellinTests(unittest.TestCase):
    def test_original_forcing_is_preserved(self):
        for n in range(1, 35):
            a = 8*n-7
            forcing = sum((Q(c0, a+d) for c0, d in zip(c.SOURCE_COEFFICIENTS, c.SOURCE_SHIFTS)), Q())
            self.assertEqual(forcing, source_power_term(n))

    def test_tilted_source_small_values(self):
        for a in (Q(1, 9), Q(1), Q(17, 3), Q(101)):
            self.assertEqual(c.source_negative_mellin(0, a), 0)
            self.assertEqual(c.source_negative_mellin(1, a), -15)
            self.assertEqual(c.source_negative_mellin(2, a), -30*a-59)
            for m in range(1, 20):
                self.assertLess(c.source_negative_mellin(m, a), 0)

    def test_native_full_source_values(self):
        expected = (0, -16, -112, -880, -9520, -136816, -2391472)
        self.assertEqual(tuple(c.bbp_negative_mellin(m) for m in range(len(expected))), expected)

    def test_source_face_zero_block_and_first_contact(self):
        for k in range(12):
            for a in (Q(1, 7), Q(2), Q(31)):
                for m in range(k+1):
                    self.assertEqual(c.source_negative_mellin(m, a, k), 0)
                first = (-1)**(k+1)*15*8**k*factorial(k+1)
                self.assertEqual(c.source_negative_mellin(k+1, a, k), first)
                self.assertGreater((-1)**(k+1)*c.source_negative_mellin(k+5, a, k), 0)

    def test_full_face_zero_block_and_sign(self):
        for z in (Q(0), Q(1, 16), Q(2, 5), Q(9, 10)):
            for k in range(9):
                self.assertTrue(all(c.bbp_negative_mellin(m, k, z) == 0 for m in range(k+1)))
                self.assertEqual(c.bbp_negative_mellin(k+1, k, z), c.bbp_face_first_value(k, z))
                for m in (k+2, k+7):
                    self.assertGreater((-1)**(k+1)*c.bbp_negative_mellin(m, k, z), 0)

    def test_independent_heat_division_against_infinite_sum(self):
        for z in (Q(0), Q(1, 16), Q(2, 3)):
            for k in range(7):
                coefficients = c.bbp_heat_coefficients(24, k, z)
                for m in range(25):
                    self.assertEqual((-1)**m*factorial(m)*coefficients[m], c.bbp_negative_mellin(m, k, z))

    def test_geometric_moment_known_values(self):
        for z in (Q(0), Q(1, 16), Q(2, 3)):
            moments = c.geometric_power_moments(z, 3)
            expected = (1/(1-z), z/(1-z)**2, z*(1+z)/(1-z)**3,
                        z*(1+4*z+z*z)/(1-z)**4)
            self.assertEqual(moments, expected)

    def test_geometric_moment_tail_partition(self):
        z, cutoff, degree = Q(3, 7), 11, 16
        moments = c.geometric_power_moments(z, degree)
        for m in range(degree+1):
            prefix = sum((z**n*n**m for n in range(cutoff)), Q())
            tail = z**cutoff*sum((comb(m, j)*cutoff**(m-j)*moments[j] for j in range(m+1)), Q())
            self.assertEqual(moments[m], prefix+tail)

    def test_convolution_contact_from_full_kernel(self):
        for power in range(1, 9):
            for m in range(2*power-1):
                self.assertEqual(c.convolution_negative_mellin(power, m, Q(2, 7)), 0)
            self.assertEqual(c.convolution_negative_mellin(power, 2*power-1, Q(13, 5)), -15**power)
            self.assertLess(c.convolution_negative_mellin(power, 2*power+2, Q(2, 7)), 0)

    def test_no_zeta_parity_for_original_source(self):
        for n in range(1, 18):
            self.assertEqual(c.zeta_negative_from_heat(2*n), 0)
            self.assertLess(c.bbp_negative_mellin(2*n), 0)


class BoseAndDomainTests(unittest.TestCase):
    def test_universal_pascal_face_contacts(self):
        for m in range(17):
            self.assertEqual(c.pascal_face_negative_mellin(m, m), (-1)**m*factorial(m))
            for grade in range(m+1, 22):
                self.assertEqual(c.pascal_face_negative_mellin(m, grade), 0)

    def test_causal_face_zeta_against_independent_heat_inverse(self):
        for m in range(49):
            self.assertEqual(c.zeta_negative_from_causal_faces(m), c.zeta_negative_from_heat(m))
        self.assertEqual(c.eta_negative_from_causal_faces(0), Q(1, 2))
        self.assertEqual(c.eta_negative_from_causal_faces(1), Q(1, 4))

    def test_same_grade_mixture_keeps_source_distinction(self):
        self.assertEqual(c.native_negative_face_mixture(0), 0)
        self.assertEqual(c.native_negative_face_mixture(1), -8)
        self.assertEqual(c.native_negative_face_mixture(2), 8)
        self.assertEqual(c.eta_negative_from_causal_faces(2), 0)
        self.assertEqual(c.zeta_negative_from_causal_faces(2), 0)

    def test_new_mixture_budget_guards(self):
        for bad in (-1, True, 1.0, 65):
            with self.assertRaises((TypeError, ValueError)):
                c.eta_negative_from_causal_faces(bad)
            with self.assertRaises((TypeError, ValueError)):
                c.pascal_face_negative_mellin(1, bad)
        with self.assertRaises(ValueError):
            c.native_negative_face_mixture(26)

    def test_bose_known_jet(self):
        self.assertEqual(c.bose_regular_coefficients(7),
                         (Q(-1, 2), Q(1, 12), 0, Q(-1, 720), 0, Q(1, 30240), 0, Q(-1, 1209600)))

    def test_zeta_values_against_inherited_bernoulli_recurrence(self):
        for m in range(49):
            self.assertEqual(c.zeta_negative_from_heat(m), zeta_nonpositive(m))

    def test_same_leading_pole_positive_mutant_breaks_parity(self):
        # K_eps = K + eps*t^(2n)*exp(-t) is positive for all positive t.
        eps = Q(1, 11)
        for n in range(1, 10):
            coefficients = c.bose_regular_coefficients(2*n)
            mutated = coefficients[2*n]+eps
            self.assertEqual(factorial(2*n)*mutated, factorial(2*n)*eps)
            self.assertNotEqual(factorial(2*n)*mutated, 0)

    def test_order_and_face_bounds(self):
        for bad in (-1, 65, True, Q(1), 1.0):
            with self.assertRaises((TypeError, ValueError)):
                c.forward_delta_difference(bad, 1)
            with self.assertRaises((TypeError, ValueError)):
                c.bbp_negative_mellin(bad)
        for bad in (-1, 25, True, 1.0):
            with self.assertRaises((TypeError, ValueError)):
                c.bbp_negative_mellin(2, bad)

    def test_regulator_cannot_cross_convergence_boundary(self):
        for z in (-1, 1, 2, True, 0.5):
            with self.assertRaises((TypeError, ValueError)):
                c.bbp_negative_mellin(2, regulator=z)
            with self.assertRaises((TypeError, ValueError)):
                c.bbp_heat_coefficients(2, regulator=z)

    def test_causal_and_exact_input_guards(self):
        for bad in (-1, 0, True, 0.1):
            with self.assertRaises((TypeError, ValueError)):
                c.forward_delta_difference(1, bad)
            with self.assertRaises((TypeError, ValueError)):
                c.source_negative_mellin(2, bad)
        with self.assertRaises(ValueError):
            c.CausalAtom(Q(-1), Q(1))
        with self.assertRaises(ValueError):
            c.negative_order_pairing(2, (1, 2))
        with self.assertRaises(ValueError):
            c.tempered_negative_coefficients(1, -1)
        with self.assertRaises(ValueError):
            c.delta_difference_error_bound(1, 1, -1)

    def test_extreme_implemented_grades(self):
        self.assertLess(c.bbp_negative_mellin(64), 0)
        self.assertEqual(c.bbp_negative_mellin(24, 24), 0)
        self.assertEqual(c.bbp_negative_mellin(25, 24), c.bbp_face_first_value(24))
        coefficient = c.bbp_heat_coefficients(64)[64]
        self.assertEqual(factorial(64)*coefficient, c.bbp_negative_mellin(64))


if __name__ == "__main__":
    unittest.main()
