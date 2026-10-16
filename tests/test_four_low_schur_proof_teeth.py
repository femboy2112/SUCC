"""Regression/control checks; proofs and quantifiers live in the dossier."""
from fractions import Fraction as F
import importlib.util
import unittest

from observational_succ import four_low_schur_proof_teeth as T
from observational_succ import suzuki_legendre_source as L
from observational_succ.suzuki_moment_schur import SchurSourceError
from observational_succ.tate_suzuki_shorting import (
    PINNED_TAPE, ShortingContractError, gammas_from_prime_mutation, rational_psd,
)


class QuotientAndSourceControls(unittest.TestCase):
    def test_low_polynomial_lifts_vanish_in_exact_quotient(self):
        polys = tuple(L.legendre_polynomial(n, F(1, 2)) for n in range(1, 5))
        r = T.quotient_polynomial_gram(polys)
        self.assertEqual(r['quotient'], ((F(),)*4,)*4)
        self.assertTrue(all(r['raw'][i][i] > 0 for i in range(4)))

    def test_quotient_is_invariant_under_low_source_coordinate_lifts(self):
        high = tuple(L.legendre_polynomial(n, F(1, 2)) for n in (5, 6, 7, 8))
        altered = tuple(L.poly_add(p, L.legendre_polynomial(i+1, F(1, 2)), i+2)
                        for i, p in enumerate(high))
        a, b = T.quotient_polynomial_gram(high), T.quotient_polynomial_gram(altered)
        self.assertEqual(a['quotient'], b['quotient'])
        self.assertNotEqual(a['raw'], b['raw'])
        removed = tuple(tuple(a['raw'][i][j]-a['quotient'][i][j] for j in range(4))
                        for i in range(4))
        self.assertTrue(rational_psd(removed)[0])

    def test_parity_on_quotient_keeps_derivative_parity_reversal(self):
        r = T.quotient_polynomial_gram(tuple(L.legendre_polynomial(n, F(1, 2))
                                           for n in (5, 6, 7, 8)))
        blocks = T.exact_parity_four(r['quotient'])
        self.assertEqual((blocks['odd_rank'], blocks['even_rank']), (2, 2))
        bad = [list(row) for row in r['quotient']]
        bad[0][1] = bad[1][0] = F(1, 1000000)
        with self.assertRaises(SchurSourceError):
            T.exact_parity_four(bad)

    def test_bool_and_float_do_not_become_exact_proof_inputs(self):
        for x in (True, .5):
            with self.assertRaises(ValueError):
                T.quotient_polynomial_gram(((x,),))
        for x in (True, 8.0, 3, 13):
            with self.assertRaises(ValueError):
                T.source_low_intervals(x, 2)

    def test_real_source_pin_and_fake_primitive6_control(self):
        snapshot = T.source_snapshot()
        self.assertEqual(snapshot['source_git_blob'], '0cc8510b71d178fc79e8d410a86d8b6014cf9178')
        self.assertIn('provenance/IMPORT_MANIFEST.json', snapshot['sha256'])
        with self.assertRaises(ShortingContractError):
            gammas_from_prime_mutation(PINNED_TAPE+((6, 6),))

    def test_source_specific_zero_trial_criterion_obstruction_is_rational(self):
        r = T.certified_trial_obstruction((0, 1, 0, 0, 0, 0), (0, 0, 0, 0, 0, 1))
        self.assertTrue(r['this_trial_sufficient_criterion_certifiably_fails'])
        self.assertIs(type(r['sufficient_criterion_direction_upper']), F)
        self.assertLess(r['sufficient_criterion_direction_upper'], -F(6, 1000))
        self.assertGreater(r['quotient_residual_energy_lower'], 0)
        self.assertFalse(r['source_original_G_negative'])
        self.assertEqual(r['source_original_sign'], 'OPEN')

    def test_trial_obstruction_refuses_a_low_witness(self):
        with self.assertRaises(T.FourLowError):
            T.certified_trial_obstruction((1, 0, 0, 0, 0), (1, 0, 0, 0, 1))

    def test_frozen_real_Galerkin_trial_has_continuum_obstruction(self):
        v = (0, 1, 0, 0, 0, F(771842481, 10**9), 0, F(198849247, 10**9), 0, 0)
        q = (0, 0, 0, 0, 0, 0, 0, 0, 0, 1)
        r = T.certified_trial_obstruction(v, q)
        self.assertTrue(r['this_trial_sufficient_criterion_certifiably_fails'])
        self.assertLess(r['sufficient_criterion_direction_upper'], -F(8, 100000))
        self.assertFalse(r['source_original_G_negative'])

    def test_interval_source_blocks_keep_original_parity_and_tail(self):
        s = T.source_low_intervals(4, 3)
        a = s['matrix']
        for i in range(4):
            for j in range(4):
                self.assertEqual(a[i][j], a[j][i])
                if (i-j) % 2:
                    self.assertEqual((a[i][j].lo, a[i][j].hi), (0, 0))
        self.assertGreater(s['positive_tail_operator_upper'], 0)
        self.assertFalse(s['full_source_sign_certified'])


@unittest.skipUnless(all(importlib.util.find_spec(m) for m in ('numpy', 'mpmath', 'scipy')),
                     'optional independent numerical convolution requires host scipy')
class RealSourceNumericalRegression(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.full = T.numerical_full_source_matrix(6, 45)
        cls.grid = T.numerical_derivative_grid(6, 8)

    def test_independent_full_source_integrations_and_finite_trial(self):
        import numpy as np
        t = T.numerical_trial(self.full, self.grid, 6)
        self.assertLess(t['full_source_matrix_crosscheck_max_difference'], 3e-6)
        self.assertGreater(t['finite_high_minimum'], 0)
        self.assertLess(t['quotient_gram_trace'], t['raw_gram_trace'])
        self.assertLess(min(t['quotient_lower_eigenvalues']), 0)
        self.assertFalse(t['original_sign_certified'])
        frozen = T.numerical_trial(self.full, self.grid, 6, frozen_U=t['U'])
        np.testing.assert_allclose(frozen['C_quotient'], t['C_quotient'])
        self.assertTrue(frozen['trial_frozen_before_evaluation'])
        bad = np.array(t['U']); bad[0, 1] = 1
        with self.assertRaises(T.FourLowError):
            T.numerical_trial(self.full, self.grid, 6, frozen_U=bad)

    def test_source_mutations_are_detectable_but_parity_is_insufficient(self):
        controls = T.source_specific_controls(self.full)
        self.assertTrue(controls['fake_primitive6_tape_rejected'])
        for key in ('missing_true_prime2_low_delta_frobenius', 'duplicate_gamma_low_delta_frobenius',
                    'contact_plus_one_low_delta_frobenius', 'pole_deletion_low_delta_frobenius'):
            self.assertGreater(controls[key], 0)
        self.assertTrue(controls['all_these_mutations_preserve_parity'])
        self.assertFalse(controls['mutations_accepted_as_authentic'])


if __name__ == '__main__':
    unittest.main()
