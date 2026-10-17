"""Exact hostile checks; no synthetic result is a claim about original Weil."""
from __future__ import annotations
import unittest
from fractions import Fraction as F
from observational_succ.source_jump_spectral import (
    JumpSpectralError, rat, matrix, eye, zero, add, mul, transpose, dot, apply,
    witness, is_psd, exact_spectral_projectors, exact_polar_schur,
    effective_gamma_rank_budget, authenticate_original_jump_rank_budget,
    authentic_primitive_ritz_packet, canonical_cycle_control,
    source_fourier_band_certificate_budget, exact_feature_gram_decision, exact_gamma_prefix_multiplier,
)


class MatrixModelTests(unittest.TestCase):
    def test_exact_positive_cycle(self):
        result=canonical_cycle_control()
        self.assertTrue(result['positive_certified_in_finite_model'])
        self.assertFalse(result['RH_proved'])
        self.assertEqual(result['low_spectral_rank'],3)
        self.assertEqual(result['cosh_high_resolvent'],F(1,39))
        self.assertEqual(result['sinh_high_resolvent'],0)
        self.assertEqual(result['cosh_effective_strength'],F(78,41))
        self.assertEqual(result['sinh_effective_strength'],2)
        self.assertTrue(is_psd(result['full_signed_operator']))

    def test_negative_contact_mutant(self):
        result=canonical_cycle_control(potential=3)
        self.assertFalse(result['positive_certified_in_finite_model'])
        w=result['negative_witness']
        self.assertTrue(w is not None)
        self.assertLess(dot(w,apply(result['full_signed_operator'],w)),0)
        self.assertFalse(result['original_signed_Weil_certified'])

    def test_missing_positive_polar_mutant(self):
        result=canonical_cycle_control(pole_mutation=True)
        self.assertFalse(result['positive_certified_in_finite_model'])
        self.assertLess(dot(result['negative_witness'],apply(result['full_signed_operator'],result['negative_witness'])),0)

    def test_both_polar_renormalizations(self):
        # Exact spectral control in parity-adapted coordinates, with both
        # even/odd pole vectors having a genuine low and high component.
        L=((0,0,0,0,0),(0,20,0,0,0),(0,0,20,0,0),(0,0,0,40,0),(0,0,0,0,40))
        reflection=((1,0,0,0,0),(0,1,0,0,0),(0,0,-1,0,0),(0,0,0,1,0),(0,0,0,0,-1))
        result=exact_polar_schur(L,(0,20,40),1,(1,0,0,1,0),(0,0,1,0,1),25,reflection)
        self.assertEqual(result['low_spectral_rank'],3)
        self.assertEqual(result['cosh_high_resolvent'],F(1,39))
        self.assertEqual(result['sinh_high_resolvent'],F(1,39))
        self.assertEqual(result['cosh_effective_strength'],F(78,41))
        self.assertEqual(result['sinh_effective_strength'],F(78,37))
        self.assertTrue(result['positive_certified_in_finite_model'])

    def test_not_all_positive_jump_sources_are_signed_positive(self):
        L=((0,0,0,0,0),(0,20,0,0,0),(0,0,20,0,0),(0,0,0,40,0),(0,0,0,0,40))
        reflection=tuple(tuple(F(int(i==j))*F(-1 if i in (2,4) else 1) for j in range(5)) for i in range(5))
        r=exact_polar_schur(L,(0,20,40),3,(1,0,0,1,0),(0,0,1,0,1),25,reflection)
        self.assertFalse(r['positive_certified_in_finite_model'])

    def test_exact_polynomial_projectors(self):
        L=((0,0,0),(0,1,0),(0,0,3))
        p=exact_spectral_projectors(L,(0,1,3))
        self.assertEqual(p[0][0][0],1)
        self.assertEqual(sum((sum(p[z][i][i] for i in range(3)) for z in p)),3)
        for z,P in p.items():
            self.assertEqual(mul(P,P),P)
            self.assertEqual(mul(P,L),mul(L,P))

    def test_reject_untrue_spectral_claim(self):
        with self.assertRaises(JumpSpectralError):
            exact_spectral_projectors(((0,0),(0,3)),(0,2))

    def test_reject_negative_eigenspectrum(self):
        with self.assertRaises(JumpSpectralError):
            exact_spectral_projectors(((-1,0),(0,3)),(-1,3))

    def test_reject_duplicate_eigenvalues(self):
        with self.assertRaises(JumpSpectralError):
            exact_spectral_projectors(((0,0),(0,3)),(0,0,3))

    def test_reject_false_cutoff(self):
        with self.assertRaises(JumpSpectralError):
            canonical_cycle_control(potential=22)

    def test_reject_fake_parity(self):
        L=((0,0),(0,20))
        false_ref=((0,1),(1,0))
        with self.assertRaises(JumpSpectralError):
            exact_polar_schur(L,(0,20),1,(1,0),(0,1),10,false_ref)

    def test_reject_mixed_pole_eigenspace_even_if_orthogonal_globally(self):
        # c and s are orthogonal but mix within eigenspaces; such a model
        # cannot use the two independent Woodbury scalar denominators.
        L=((1,0),(0,10))
        with self.assertRaises(JumpSpectralError):
            exact_polar_schur(L,(1,10),0,(1,1),(1,-1),8)

    def test_exact_psd_witness_negative_diagonal(self):
        A=((1,0),(0,-1))
        w=witness(A)
        self.assertLess(dot(w,apply(A,w)),0)

    def test_exact_psd_witness_zero_diagonal(self):
        A=((0,1),(1,3))
        w=witness(A)
        self.assertLess(dot(w,apply(A,w)),0)

    def test_exact_psd_witness_negative_schur(self):
        A=((1,2),(2,1))
        w=witness(A)
        self.assertLess(dot(w,apply(A,w)),0)

    def test_psd_semidefinite_rank_one(self):
        self.assertTrue(is_psd(((1,1),(1,1))))
        self.assertTrue(is_psd(((0,0),(0,0))))

    def test_source_ranks_exact(self):
        r=effective_gamma_rank_budget()
        self.assertEqual(r['frequency_band_radius'],76)
        self.assertEqual(r['cell_rank_upper'],453)
        self.assertEqual(r['original_real_Gamma_prefix_rungs'],256)
        self.assertEqual(r['band_Gamma_energy_floor'],F(3927,500))
        self.assertGreater(exact_gamma_prefix_multiplier(76,256),F(3927,500))
        self.assertEqual(r['high_cell_complement_energy_floor'],F(3927,500)*(1-F(76,3*453))**2)
        self.assertEqual(r['full_negative_budget_upper'],F(103,16))
        self.assertEqual(r['high_signed_spectral_gap_lower'],F(9,16))
        self.assertEqual(r['odd_polar_effective_strength_upper'],F(20,9))
        self.assertFalse(r['spectral_projector_explicitly_computed'])

    def test_constructive_fourier_band_budget(self):
        r=source_fourier_band_certificate_budget(16,F(1,4))
        self.assertEqual(r['R'],65536)
        self.assertEqual(r['mu_gamma_lower'],F(1104,125))
        self.assertEqual(r['two_sided_midpoint_frequency_nodes'],184683593729)
        self.assertLess(r['absolute_operator_quadrature_error_certified_upper'],F(1,4))
        self.assertFalse(r['actual_source_frequency_coefficients_sampled'])

    def test_fourier_band_budget_shrinks_with_accuracy(self):
        fine=source_fourier_band_certificate_budget(10,F(1,100))
        coarse=source_fourier_band_certificate_budget(10,F(1,2))
        self.assertGreater(fine['two_sided_midpoint_frequency_nodes'],coarse['two_sided_midpoint_frequency_nodes'])

    def test_exact_feature_gram_positive_signed(self):
        a=exact_feature_gram_decision(1,((1,F(1,2)),(F(1,2),1)),(-F(1,4),-F(1,4)))
        self.assertTrue(a['positive_certified_in_finite_feature_model'])
        self.assertFalse(a['original_signed_Weil_certified'])

    def test_exact_feature_gram_negative_mutant(self):
        a=exact_feature_gram_decision(1,((1,F(1,2)),(F(1,2),1)),(-3,0))
        self.assertFalse(a['positive_certified_in_finite_feature_model'])
        w=a['negative_coefficient_witness']
        self.assertLess(dot(w,apply(a['finite_restricted_matrix'],w)),0)

    def test_feature_gram_must_be_psd(self):
        with self.assertRaises(JumpSpectralError):
            exact_feature_gram_decision(1,((1,2),(2,1)),(1,-1))

    def test_feature_base_must_be_strict(self):
        with self.assertRaises(JumpSpectralError):
            exact_feature_gram_decision(0,((1,0),(0,1)),(1,1))

    def test_original_source_adapter(self):
        try:
            from observational_succ import source_weil_hierarchy
        except ImportError:
            self.skipTest('original SUCC source package absent in isolated testing fixture')
        r=authenticate_original_jump_rank_budget()
        self.assertEqual(r['source_contract']['source_git_blob'],'0cc8510b71d178fc79e8d410a86d8b6014cf9178')
        self.assertFalse(r['original_signed_Weil_certified'])
        self.assertEqual(r['cell_rank_upper'],453)
        self.assertEqual(r['negative_jump_baseline_index_upper'],5)
        self.assertEqual(r['negative_even_jump_baseline_index_upper'],3)
        self.assertEqual(r['negative_odd_jump_baseline_index_upper'],2)

    def test_authentic_primitive_ritz(self):
        try:
            from observational_succ import suzuki_legendre_source
        except ImportError:
            self.skipTest('original SUCC source package absent in isolated testing fixture')
        records={k:authentic_primitive_ritz_packet(k,12) for k in (1,2)}
        for k,r in records.items():
            self.assertEqual(r['original_source_blob'],'0cc8510b71d178fc79e8d410a86d8b6014cf9178')
            self.assertGreater(r['primitive_K_norm_squared'],0)
            self.assertLessEqual(*r['positive_jump_ritz_rayleigh_interval'])
            self.assertFalse(r['source_generated_jump_eigenfunction_claimed'])
        # A REAL original-source strictly negative baseline EVEN direction,
        # despite the inherited WB4 original signed low A4 > 0.
        self.assertTrue(records[1]['baseline_rigorously_negative_on_this_trial'])
        self.assertLess(records[1]['polar_free_baseline_energy_interval'][1],F(-56,1000))
        # One strictly positive ODD baseline test does NOT certify the sector.
        self.assertGreater(records[2]['polar_free_baseline_energy_interval'][0],F(0))


if __name__=='__main__':
    unittest.main()
