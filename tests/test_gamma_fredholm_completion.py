"""Hostile exact algebra and real frozen-source Gamma/FUCC completion tests."""
import unittest
from fractions import Fraction as F
from observational_succ import gamma_fredholm_completion as C


class StandaloneAlgebra(unittest.TestCase):
    def test_gamma_tail_lower_rational(self):
        w=C.odd_legendre_135_witness()
        self.assertEqual(w['norm_sq'],F(2136,77))
        self.assertEqual(w['derivative_norm_sq'],F(1296))
        self.assertEqual(C.gamma_tail_H01_lower(64,w['norm_sq'],w['derivative_norm_sq']),
          2*F(2136,77)/257**2 - (F(4,257**4)+F(64,257**5))*1296)
    def test_tail_geometric_sign(self):
        low=C.gamma_tail_H01_lower(64,F(2136,77),F(1296))
        self.assertGreater(low,F(838,1000000))
        self.assertLess(low,F(840,1000000))
        self.assertGreater(C.gamma_tail_source_upper(64,F(2136,77)),low)
    def test_mutant_large_derivative_loses_lower(self):
        self.assertLess(C.gamma_tail_H01_lower(64,1,10000000),0)
    def test_tail_refinement_is_valid_only_H01(self):
        self.assertTrue(C.odd_legendre_135_witness()['endpoints_zero'])
        self.assertTrue(C.odd_legendre_135_witness()['meanzero'])
    def test_polynomial_identity(self):
        coeff=C.odd_legendre_135_witness()['u_polynomial_ascending']
        self.assertEqual(coeff,(0,57,0,-480,0,1008))
        for x in (F(-1,2),F(1,2),F(0)):
            self.assertEqual(sum(v*x**i for i,v in enumerate(coeff)),0)
    def test_exact_gamma_bounds_ordered(self):
        for J in (8,16,64,128):
            self.assertLess(C.gamma_tail_H01_lower(J,F(2136,77),F(1296)),C.gamma_tail_source_upper(J,F(2136,77)))
    def test_interval_signed_mult(self):
        self.assertEqual(C.IV(F(-2),F(3))*C.IV(F(4),F(5)),C.IV(F(-10),F(15)))
    def test_interval_sub(self):
        self.assertEqual(C.IV(F(1),F(2))-C.IV(F(3),F(4)),C.IV(F(-3),F(-1)))
    def test_non_Fraction_types_rejected(self):
        for invalid in (0.5,True,'1/2'):
            with self.assertRaises(C.CompletionError):C.rat(invalid)
    def test_inverted_interval(self):
        with self.assertRaises(C.CompletionError):C.IV(F(3),F(2))
    def test_bad_Gamma_depth(self):
        for j in (0,-1,1.0):
            with self.assertRaises(C.CompletionError):C.gamma_tail_H01_lower(j,1,0)
    def test_bad_source_scoped_depth(self):
        with self.assertRaises(C.CompletionError):C.authentic_fifth_mode_completion(63)
    def test_fraction_round_outward(self):
        for x in (F(-1,7),F(1,7),F(5,8),F(0)):
            self.assertLessEqual(C.divround(x),x)
            self.assertGreaterEqual(C.divround(x,upper=True),x)
    def test_exact_cubic_formula_coefficients(self):
        g=F(13,3);w=F(2)
        a,b,c=C.cubic_baseline_inverse_coeff(g,w)
        for eigen in (-1,0,1):
            self.assertEqual((g-w*eigen)*(a+b*eigen+c*eigen**2),1)
    def test_cubic_nonpositive_rejected(self):
        with self.assertRaises(C.CompletionError):C.cubic_baseline_inverse_coeff(1,2)
    def test_cell_overlap_exact_odd(self):
        self.assertEqual(C._overlap(F(0),F(1,2),F(1,3),F(1)),F(1,6))
    def test_fraction_fixed_rational_model_math(self):
        # A source-independent two-feature mixed signed model.
        q=C.IV(F(1),F(2));self.assertEqual(C.interval_abs_hi(q),2)


class CompleteSource(unittest.TestCase):
    @staticmethod
    def _has_source():
        try:import observational_succ.tate_suzuki_shorting
        except ImportError:return False
        return True
    def test_fifth_mode_strict_Gamma_sign_reversal(self):
        if not self._has_source():self.skipTest('Isolated fixture lacks original protected Suzuki module')
        p=C.authentic_fifth_mode_completion(64)
        self.assertTrue(p['truncated_negative_strict'])
        self.assertTrue(p['fully_completed_same_vector_positive_strict'])
        self.assertLess(F(p['J64_full_signed_source_energy'][1]),0)
        self.assertGreater(F(p['complete_true_gamma_energy_lower']),0)
        self.assertFalse(p['original_S4_positive_proved'])
    def test_true_fredholm_feature_gram_J8(self):
        if not self._has_source():self.skipTest('Isolated fixture lacks original protected Suzuki module')
        p=C.authentic_fredholm_feature_gram(8,16)
        self.assertEqual(p['dimension'],18)
        self.assertEqual(len(p['closed_source_W_interval']),18)
        self.assertGreater(F(p['positive_baseline_gap_rational']),0)
        self.assertEqual(p['result'],'INCONCLUSIVE_FINITE_GAMMA_SUFFICIENT_TEST')
    def test_nonpositive_reference_rejected_at_eight_cells(self):
        if not self._has_source():self.skipTest('Isolated fixture lacks original protected Suzuki module')
        with self.assertRaises(C.CompletionError):C.authentic_fredholm_feature_gram(8,8)
    def test_full_Gamma_endpoint_zero_four_dimensional_positivity(self):
        if not self._has_source():self.skipTest('Isolated fixture lacks original protected Suzuki module')
        x=C.authentic_endpoint_zero_four_dimensional_compensation(64)
        self.assertTrue(x['strict_completed_original_source_positive_on_four_dimensional_subspace'])
        self.assertFalse(x['original_first_window_S4_proved'])
        self.assertEqual(tuple(sorted(x['source_complete_two_parity_blocks'])),('even_u_odd_primitive','odd_u_even_primitive'))
    def test_authentic_fake_composite_rejected(self):
        if not self._has_source():self.skipTest('Isolated fixture lacks original protected Suzuki module')
        from observational_succ import source_weil_hierarchy as s
        self.assertEqual(s.authenticated_prime_wavefront(F(1,2)),((2,2),))
        self.assertIsNone(s.real_prime_power(6))
    def test_unchanged_original_source_blob(self):
        if not self._has_source():self.skipTest('Isolated fixture lacks original protected Suzuki module')
        from observational_succ.tate_suzuki_shorting import verify_original_suzuki_source
        self.assertEqual(verify_original_suzuki_source()['source_git_blob'],'0cc8510b71d178fc79e8d410a86d8b6014cf9178')


if __name__=='__main__':unittest.main()
