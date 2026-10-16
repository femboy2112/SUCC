"""Round II source interval, ansatz quantifier and distinct-response controls."""
from fractions import Fraction as F
import importlib.util
import unittest

from observational_succ import observer_schur_source as S
from observational_succ import one_object_relative_residual as R
from observational_succ import suzuki_legendre_source as L


class ExactSourceAnsatzTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.strong = S.certify_degree_eight_family(F(1, 5), 512)

    def test_all_coefficients_excluded_not_just_frozen_trials(self):
        z = self.strong
        self.assertTrue(z['all_coefficients_criterion_fails'])
        self.assertLess(z['criterion_uniform_upper_for_P2'], -F(3, 100000))
        self.assertFalse(z['this_kappa_certified_as_source_high_bound'])
        self.assertFalse(z['source_original_negative_direction'])
        self.assertEqual(z['source_original_sign'], 'OPEN')
        self.assertIn('ALL', z['coefficients_quantified'])

    def test_independent_principal_minor_check_of_majorant(self):
        neg = R.scale(-1, self.strong['criterion_Loewner_upper'])
        product = F(1)
        for k, pivot in enumerate(self.strong['minus_upper_LDL_pivots'], 1):
            product *= pivot
            minor = tuple(tuple(neg[i][j] for j in range(k)) for i in range(k))
            self.assertEqual(R.det(minor), product)
            self.assertGreater(R.det(minor), 0)

    def test_exact_maximum_square_completion_for_complex_coefficients(self):
        upper = self.strong['criterion_Loewner_upper']
        a, b = self.strong['upper_majorant_maximizer']
        maximum = self.strong['criterion_uniform_upper_for_P2']
        self.assertEqual(R.quadratic(upper, (1, a, b)), maximum)
        for u, v in ((0, 0), (1, -2), (100, 100), (F(1, 17), -F(12, 7))):
            self.assertLessEqual(R.quadratic(upper, (1, a+u, b+v)), maximum)
            self.assertLessEqual(R.quadratic(upper, (1, a, b))+R.quadratic(upper, (0, u, v)), maximum)

    def test_interval_matrix_really_is_dominated_by_upper(self):
        boxes = self.strong['criterion_interval_matrix']
        upper = self.strong['criterion_Loewner_upper']
        # Every corner of its six independent entries is below the majorant.
        from itertools import product
        pairs = ((0, 0), (0, 1), (0, 2), (1, 1), (1, 2), (2, 2))
        for choices in product((0, 1), repeat=6):
            a = [[F()]*3 for _ in range(3)]
            for (i, j), select in zip(pairs, choices):
                a[i][j] = a[j][i] = boxes[i][j][select]
            self.assertTrue(R.psd(R.add(upper, tuple(map(tuple, a)), -1)))

    def test_inherited_kappa_also_excludes_family(self):
        r = S.certify_degree_eight_family()
        self.assertTrue(r['all_coefficients_criterion_fails'])
        self.assertLess(r['criterion_uniform_upper_for_P2'], -F(1, 1000))
        self.assertTrue(r['this_kappa_certified_as_source_high_bound'])

    def test_insufficient_interval_budget_stays_unresolved(self):
        r = S.certify_degree_eight_family(F(1, 5), 128)
        self.assertFalse(r['all_coefficients_criterion_fails'])
        self.assertEqual(r['status'], 'UNRESOLVED')
        self.assertIsNone(r['criterion_uniform_upper_for_P2'])

    def test_gamma_extension_preserves_parent_intervals(self):
        z = S.polynomial_source_entry(2, 6, 64)
        old = L.authentic_full_low_entry(2, 6, J=64)
        self.assertLessEqual(z.lo, old.lo)
        self.assertGreaterEqual(z.hi, old.hi)
        self.assertEqual((S.polynomial_source_entry(1, 2).lo,
                          S.polynomial_source_entry(1, 2).hi), (0, 0))

    def test_source_kappa_ceiling_does_not_manufacture_no_go(self):
        r = S.certified_high_kappa_ceiling()
        self.assertLess(r['every_valid_kappa_upper'], F(83, 100))
        self.assertGreater(r['every_valid_kappa_upper'], F(4, 5))
        self.assertFalse(r['does_this_exclude_kappa_above_one_fifth'])
        self.assertFalse(r['this_is_a_source_high_lower_bound'])

    def test_certified_upper_short_uses_coordinate_metric_and_never_promotes_sign(self):
        r = S.certified_polynomial_upper_short()
        self.assertEqual(r['source_original_sign'], 'OPEN')
        self.assertFalse(r['source_sign_proved_by_positive_upper'])
        for sector in r['parity_operator_upper_caps'].values():
            c, metric = sector['operator_eigenvalue_upper'], sector['low_coordinate_metric']
            self.assertTrue(R.psd(R.add(R.scale(c, metric), sector['upper_form_matrix'], -1)))
            self.assertLess(c, F(1, 100))

    def test_proof_inputs_reject_bool_float_and_unsupported_budget(self):
        for bad in (True, .2, 0, -1):
            with self.assertRaises(ValueError):
                S.certify_degree_eight_family(bad)
        for bad in (True, 0, 769, 512.0):
            with self.assertRaises(ValueError):
                S.certify_degree_eight_family(gamma_modes=bad)


class ExactParityAndResponseTests(unittest.TestCase):
    def test_two_sector_test_needs_both_diagonals_and_determinant(self):
        good = ((2, 0, 1, 0), (0, 3, 0, 1), (1, 0, 2, 0), (0, 1, 0, 3))
        self.assertTrue(S.parity_psd_test(good)['PSD'])
        indefinite = ((1, 0, 2, 0), (0, 1, 0, 0), (2, 0, 1, 0), (0, 0, 0, 1))
        self.assertFalse(S.parity_psd_test(indefinite)['PSD'])
        negative = tuple(tuple(-int(i == j) for j in range(4)) for i in range(4))
        self.assertFalse(S.parity_psd_test(negative)['PSD'])
        singular = ((0, 0, 0, 0), (0, 1, 0, 1), (0, 0, 0, 0), (0, 1, 0, 1))
        self.assertTrue(S.parity_psd_test(singular)['PSD'])
        wrong = [list(row) for row in good]; wrong[0][1] = wrong[1][0] = 1
        with self.assertRaises(ValueError):
            S.parity_psd_test(wrong)

    def test_threshold_basis_has_exact_Q_moments_and_parity(self):
        basis = S.threshold_response_basis()
        self.assertEqual(len(basis), 9)
        for c in basis:
            for n, coef in enumerate(c['P0_to_P4_projection']):
                p = L.legendre_polynomial(n, F(1, 2))
                moment = L.poly_integral(p, c['left'], c['right'])+c['reflection_eigenvalue']*L.poly_integral(p, -c['right'], -c['left'])
                self.assertEqual(moment-coef/F(2*n+1), 0)
                if (-1)**n != c['reflection_eigenvalue']:
                    self.assertEqual(coef, 0)
            self.assertGreater(c['L2_norm_squared'], 0)
        with self.assertRaises(ValueError):
            S.threshold_response_basis((0, .25, F(1, 2)))

    def test_finite_positive_blocks_do_not_guarantee_positive_short(self):
        # G=[[1,2],[2,1]], positive A,D but S=-3. Ordinary input is synthetic.
        self.assertEqual(F(1)-F(2)**2/F(1), -3)
        # Negative lower sufficient certificate does not refute positive G.
        # D=2, K=1, A=1, B=1, U=0, kappa=1/2: S=1/2, lower=-1.
        self.assertEqual(F(1)-F(1)/F(2), F(1, 2))
        self.assertEqual(F(1)-F(1)/F(1, 2), -1)


@unittest.skipUnless(all(importlib.util.find_spec(p) for p in ('scipy', 'numpy', 'mpmath')),
                     'source numerical experiment requires research dependencies')
class DifferentSourceResponseTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.basis = S.threshold_response_basis((F(0), F(193147, 10**6), F(1, 3), F(1, 2)))
        cls.grid = S.numerical_threshold_grid(cls.basis, 8)

    def test_new_response_is_whole_source_and_not_a_sign_certificate(self):
        from observational_succ.four_low_schur_proof_teeth import numerical_full_source_matrix
        import numpy as np
        reference = np.array(numerical_full_source_matrix(4, 40)['matrix_decimal'], dtype=float)
        self.assertLess(np.max(abs(reference-self.grid['source_matrix'][:4, :4])), 2e-8)
        fit = S.numerical_threshold_trial(self.basis, self.grid, 'relative_optimal')
        fresh = S.numerical_threshold_trial(self.basis, self.grid, 'relative_optimal', fit['frozen_rational_U'])
        self.assertEqual(fit['lower_unnormalized'], fresh['lower_unnormalized'])
        self.assertFalse(fit['original_sign_certified'])
        self.assertFalse(fit['continuum_Gram_error_certified'])
        self.assertLess(fit['sectors']['even']['lower_operator_eigenvalues'][0], 0)
        bad = [list(row) for row in fit['frozen_rational_U']]
        bad[0][0] = F(1)  # first high cell even, first low mode odd
        with self.assertRaises(ValueError):
            S.numerical_threshold_trial(self.basis, self.grid, frozen=bad)

    def test_mod_four_gamma_filter_derivative_matches_real_gamma(self):
        import numpy as np
        from scipy.integrate import quad
        for r in (.125, .375, .875):
            value = S._numerical_kernel_channels(np.array([r]))['gamma'][0]
            def d(x):
                z = np.exp(-x/2)
                return -(np.log1p(z)-np.log(-np.expm1(-x/2)))/2-np.arctan(z)
            target = quad(d, 0, r, epsabs=2e-12)[0]
            self.assertAlmostEqual(value, target, places=11)

    def test_mutated_channels_cannot_hide_behind_parity(self):
        r = S.numerical_channel_mutations()
        self.assertTrue(r['all_mutations_preserve_reflection'])
        self.assertTrue(r['fake_composite6_tape_rejected'])
        self.assertTrue(r['fake6_invisible_at_this_radius'])
        self.assertTrue(all(v > 0 for v in r['mutation_max_abs_changes'].values()))
        self.assertEqual(r['mutation_authentication'], 'REJECTED_NOT_ALTERNATIVE_ZETA_SOURCES')

    def test_wrong_basis_cannot_borrow_a_source_matrix(self):
        other = S.threshold_response_basis()
        with self.assertRaises(S.ObserverSourceError):
            S.numerical_threshold_trial(other, self.grid)
        forged = tuple(dict(c) for c in self.basis)
        forged[0]['P0_to_P4_projection'] = (F(),)*5
        with self.assertRaises(S.ObserverSourceError):
            S.numerical_threshold_trial(forged, self.grid)


if __name__ == '__main__':
    unittest.main()
