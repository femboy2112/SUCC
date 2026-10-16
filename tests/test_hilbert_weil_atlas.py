"""Exact Hilbert-curve geometry, genuine source adapter and hostile sign tests."""
from __future__ import annotations
import importlib.util
import json
import unittest
from fractions import Fraction as F
from observational_succ.hilbert_weil_atlas import (
    HilbertAtlasError, _prime_power,
    authenticated_first_window_range_certificate, classical_first_window_carleman_range_budget,
    original_source_cross_derivative_tail_budget,
    authentic_hilbert_rayleigh,
    authentic_hilbert_shifted_schur_budget, finite_schur_control,
    compressed_prime_trace_blindspot, geometry_receipt, hilbert_average, hilbert_cells, hilbert_index,
    hilbert_diagonal_completion_budget, hilbert_lipschitz_enclosure, hilbert_martingale_l2_error_bound,
    hilbert_point_enclosure, hilbert_prime_index_mutation,
    hilbert_xy, invisible_negative_to_level, log_integer_interval,
    prime_wavefront_tiles, q, receipt, shift_projection_defect,
)


class HilbertExactGeometryTests(unittest.TestCase):
    def test_full_adjacency_and_prefix_refinement(self):
        for d in range(0,7):
            r=geometry_receipt(d)
            self.assertTrue(r['unique'])
            self.assertTrue(r['adjacent'])
            self.assertTrue(r['parent_refinement'])
            self.assertFalse(r['physical_infinity_actualized'])
            self.assertEqual(r['uniform_area_per_tile'],str(F(1,4**d)))

    def test_forward_inverse_no_holes(self):
        for d in range(1,6):
            for j in range(4**d):
                x,y=hilbert_xy(d,j)
                self.assertEqual(hilbert_index(d,x,y),j)

    def test_quadrant_children_contiguous(self):
        for d in range(1,5):
            cells=hilbert_cells(d)
            for k in range(4**(d-1)):
                self.assertEqual({(x//2,y//2) for x,y in cells[4*k:4*k+4]},
                                 {hilbert_xy(d-1,k)})

    def test_normalized_area_exact(self):
        for d in range(0,6):
            self.assertEqual(hilbert_average(d,lambda x,y:F(1)),1)
            self.assertEqual(hilbert_average(d,lambda x,y:x+y),1)
            self.assertEqual(hilbert_average(d,lambda x,y:x-y),0)

    def test_signed_quadrature_lipschitz(self):
        # f=x²-y. Coordinate Lipschitz upper constants 2 and 1 on the unit square.
        target=F(1,3)-F(1,2)
        for d in range(1,6):
            r=hilbert_lipschitz_enclosure(d,lambda x,y:x*x-y,2,1)
            self.assertTrue(r['lower']<=target<=r['upper'])
            self.assertEqual(r['error_bound'],F(3,2**(d+1)))
            self.assertLessEqual(abs(r['center']-target),r['error_bound'])

    def test_finite_zeno_prefix_nested_limit_point(self):
        for t in (F(1,5),F(17,59),F(1,4),F(1)):
            older=None
            for d in range(0,7):
                r=hilbert_point_enclosure(t,d)
                self.assertEqual(r['l_infinity_error_radius'],F(1,2**d))
                if older is not None:
                    self.assertTrue(older['x_interval'][0]<=r['x_interval'][0]<=r['x_interval'][1]<=older['x_interval'][1])
                    self.assertTrue(older['y_interval'][0]<=r['y_interval'][0]<=r['y_interval'][1]<=older['y_interval'][1])
                older=r

    def test_hilbert_martingale_observer_rate_contract(self):
        for d in range(0,7):
            r=hilbert_martingale_l2_error_bound(d,F(3,2))
            self.assertEqual(r['rigorous_l2_error_upper'],F(3,2**d))
            self.assertTrue(r['requires_external_source_lipschitz_proof'])
        with self.assertRaises(HilbertAtlasError):
            hilbert_martingale_l2_error_bound(3,-1)

    def test_midpoint_exact_symmetric_pair_integrals(self):
        # f(x,y)=-(x-y)² (indefinite-sign *kernel* geometry toy, not original Weil).
        for d in range(1,6):
            v=hilbert_average(d,lambda x,y:-(x-y)**2)
            self.assertTrue(-F(1,6)<=v<=0)

    def test_invalid_depth_index_and_float_types(self):
        cases=(lambda:hilbert_xy(-1,0),lambda:hilbert_xy(3,64),
               lambda:hilbert_xy(1,False),lambda:hilbert_index(2,4,0),
               lambda:q(.5),lambda:hilbert_average(1,lambda x,y:.5),
               lambda:hilbert_lipschitz_enclosure(1,lambda x,y:x,-1,0))
        for f in cases:
            with self.subTest(f=f),self.assertRaises(HilbertAtlasError):f()


class GenuinePrimeWavefrontTests(unittest.TestCase):
    def test_primitive_prime_source_gate(self):
        for n,expected in ((2,(2,1)),(3,(3,1)),(4,(2,2)),(8,(2,3)),
                           (9,(3,2)),(25,(5,2))):
            self.assertEqual(_prime_power(n),expected)
        for n in (6,10,12,15,18,21,30):
            self.assertIsNone(_prime_power(n))
            with self.assertRaises(HilbertAtlasError):
                prime_wavefront_tiles(3,F(1,2),n)

    def test_source_log_interval(self):
        lo,hi=log_integer_interval(2)
        self.assertTrue(F(69,100)<lo<hi<F(70,100))
        lo,hi=log_integer_interval(3)
        self.assertTrue(F(109,100)<lo<hi<F(11,10))
        self.assertEqual(log_integer_interval(4),
                         tuple(2*x for x in log_integer_interval(2)))

    def test_true_prime2_wavefront_occupancy_sparse(self):
        for d in range(2,7):
            r=prime_wavefront_tiles(d,F(1,2),2)
            v=r['counts']
            self.assertEqual(sum(v.values()),4**d)
            self.assertTrue(v['threshold']<=8*(2**d))
            self.assertGreater(v['threshold'],0)
            self.assertEqual(len(r['ordered_labels']),4**d)
        self.assertEqual(prime_wavefront_tiles(4,F(1,2),2)['counts'],
                         {'inactive':226,'active':12,'threshold':18})

    def test_prime_power_four_not_yet_activated(self):
        r=prime_wavefront_tiles(5,F(1,2),4)
        self.assertEqual(r['counts']['inactive'],4**5)
        self.assertEqual(r['counts']['active'],0)

    def test_hilbert_index_prime_action_is_not_natural(self):
        r=hilbert_prime_index_mutation(2,2,3)
        self.assertTrue(r['invertible_on_index_clock'])
        self.assertFalse(r['refinement_square_commutes'])
        self.assertEqual((r['actual_parent'],r['naive_parent']),(1,0))
        self.assertTrue(r['toy_index_action_not_authenticated_original_FUCC'])

    def test_naive_compressed_trace_is_blind_to_genuine_prime2(self):
        r=compressed_prime_trace_blindspot(4,F(1,2),2)
        self.assertEqual(r['naive_step_basis_translation_trace_interval'],(F(),F()))
        self.assertTrue(r['actual_shift_nonzero_on_interval'])
        self.assertTrue(r['the_prime_term_is_offdiagonal_not_trace_visible'])
        self.assertFalse(r['Connes_trace_distribution_identified'])
        with self.assertRaises(HilbertAtlasError):
            compressed_prime_trace_blindspot(4,F(1,2),6)

    def test_low_resolution_prime_trace_interval_outward(self):
        r=compressed_prime_trace_blindspot(0,F(1,2),2)
        self.assertFalse(r['trace_identically_zero'])
        self.assertLess(r['naive_step_basis_translation_trace_interval'][0],
                        r['naive_step_basis_translation_trace_interval'][1])

    def test_even_prime_loses_2_adic_clock_units(self):
        r=hilbert_prime_index_mutation(2,2,2)
        self.assertFalse(r['invertible_on_index_clock'])
        self.assertEqual(r['image_count'],8)
        self.assertTrue(hilbert_prime_index_mutation(2,2,6)['toy_index_action_not_authenticated_original_FUCC'])

    def test_fixed_prime_log_binary_nonuniform_control(self):
        lo,hi=log_integer_interval(2)
        # The exact fraction 2^n log 2, for n=3,6, has a phase in [1/4,3/4].
        for depth in (3,6):
            x,y=2**depth*lo,2**depth*hi
            self.assertEqual(x.numerator//x.denominator,y.numerator//y.denominator)
            frac_lo=x-(x.numerator//x.denominator)
            frac_hi=y-(y.numerator//y.denominator)
            self.assertGreaterEqual(frac_lo,F(1,4))
            self.assertLessEqual(frac_hi,F(3,4))
            self.assertGreaterEqual(shift_projection_defect(frac_lo),F(3,8))

    def test_source_threshold_rejects_invalid_radii(self):
        with self.assertRaises(HilbertAtlasError):prime_wavefront_tiles(3,0,2)
        with self.assertRaises(HilbertAtlasError):prime_wavefront_tiles(3,.5,2)


class SignedOperatorFirewalls(unittest.TestCase):
    def test_authentic_carleman_smoothing_zero_shift_range_paper_bound(self):
        r=classical_first_window_carleman_range_budget()
        self.assertEqual(r['original_screw_derivative_L1_strict_upper'],24)
        self.assertEqual(r['original_screw_kernel_Linfty_strict_upper'],12)
        self.assertEqual(r['legendre_30_derivative_HS_norm_squared'],922560)
        self.assertEqual(r['original_low_to_high_H1_gain_strict_upper'],11556)
        self.assertEqual(r['uniform_lambda_to_zero_cross_resolvent_upper'],
                         F(11556**2)*F(10000,369))
        self.assertTrue(r['range_condition_proved_conditional_on_original_high_theorem'])
        self.assertFalse(r['shorted_low_sign_proved'])
        self.assertFalse(r['RH_proved'])

    def test_original_Gamma_rungs_converge_in_cross_H1_source_metric(self):
        vals=[]
        for J in (1,2,8,32,128,512):
            r=original_source_cross_derivative_tail_budget(J)
            self.assertEqual(r['omitted_original_Gamma_derivative_L1_upper'],
                             2*r['omitted_original_Gamma_kernel_Linfty_upper'])
            self.assertEqual(r['source_high_cross_derivative_gain_upper'],
                             963*r['omitted_original_Gamma_kernel_Linfty_upper'])
            self.assertFalse(r['finite_J_true_derivative_Gram_computed'])
            vals.append(r['source_high_cross_derivative_gain_upper'])
        self.assertEqual(vals,sorted(vals,reverse=True))
        with self.assertRaises(HilbertAtlasError):
            original_source_cross_derivative_tail_budget(0)

    def test_exact_hidden_negative_even_toeplitz(self):
        for d in range(1,6):
            w=invisible_negative_to_level(d)
            self.assertTrue(w['coarse_block_zero'])
            self.assertEqual(w['quadratic_unit_alternating'],-1)
            self.assertFalse(w['original_arithmetic_source'])
            self.assertTrue(w['signed_even_difference_kernel'])

    def test_source_diagonal_schedule_has_vanishing_shifted_cost(self):
        vals=[]
        for n in (4,8,12,16,24,32):
            r=hilbert_diagonal_completion_budget(n)
            self.assertEqual(r['J'],2**n)
            self.assertEqual(r['lambda'],F(1,2**n))
            self.assertFalse(r['all_test_low_schur_sign_verified'])
            self.assertFalse(r['unshifted_zero_lambda_verified'])
            self.assertFalse(r['RH_proved'])
            vals.append(r['shifted_cross_penalty_upper_conditional'])
        self.assertEqual(vals,sorted(vals,reverse=True))
        self.assertLess(vals[-1],F(1,100000))

    def test_source_diagonal_schedule_requires_proven_rounding(self):
        r=hilbert_diagonal_completion_budget(16)
        self.assertFalse(r['current_source_stage_software_supports_this_level'])
        self.assertEqual(r['source_rounding_precision_assumption'],F(1,2**32))
        for invalid in (0,65,2.0,True):
            with self.assertRaises(HilbertAtlasError):hilbert_diagonal_completion_budget(invalid)

    def test_shift_cell_variance(self):
        self.assertEqual(shift_projection_defect(F(1,2)),F(1,2))
        self.assertEqual(shift_projection_defect(F(1,4)),F(3,8))
        self.assertEqual(shift_projection_defect(0),0)
        self.assertEqual(shift_projection_defect(1),0)

    def test_shifted_schur_penalty_never_certifies_zero_shift(self):
        a=finite_schur_control(1,F(1,2),F(1,16),F(1,4),F(1,2))
        self.assertEqual(a['exact_coupling_penalty'],F(4,5))
        self.assertEqual(a['upper_coupling_penalty'],F(1))
        self.assertFalse(a['zero_shift_verified'])
        b=finite_schur_control(1,F(1,2),F(1,16),F(1,16),F(1,2))
        self.assertGreater(b['upper_coupling_penalty'],a['upper_coupling_penalty'])

    def test_wrong_high_sign_and_fake_bound(self):
        for f in (lambda:finite_schur_control(1,1,-1,1,1),
                  lambda:finite_schur_control(1,1,1,1,F(1,2)),
                  lambda:finite_schur_control(1,1,1,0,1)):
            with self.assertRaises(HilbertAtlasError):f()

    def test_receipt_deterministic_and_firewall(self):
        a,b=receipt(),receipt()
        self.assertEqual(a,b)
        self.assertEqual(json.loads(json.dumps(a)),a)
        self.assertTrue(a['no_source_Weil_sign_or_RH_proof'])
        self.assertEqual(a['hidden_negative_level_3']['quadratic_unit_alternating'],'-1')


class AuthenticSuzukiAdapterTests(unittest.TestCase):
    """These run only in an authentic SUCC repo checkout with source blob available."""
    @unittest.skipUnless(importlib.util.find_spec('observational_succ.source_weil_hierarchy'),
                         'requires integrated original source module on GitHub CI')
    def test_actual_original_signed_source_rational_hilbert_rayleigh(self):
        from observational_succ.source_weil_hierarchy import stage
        r=authentic_hilbert_rayleigh(2,(F(1),F(-1),F(),F()),J=2)
        st=stage(F(1,2),2,4)
        self.assertEqual(r['source'],st.source)
        self.assertEqual(r['rational_center'],
                         st.center[0][0]-2*st.center[0][1]+st.center[1][1])
        self.assertLessEqual(r['rayleigh_lower'],r['rayleigh_upper'])
        self.assertFalse(r['positive_on_whole_space_certified'])
        self.assertFalse(r['RH_proved'])

    @unittest.skipUnless(importlib.util.find_spec('observational_succ.source_weil_hierarchy'),
                         'requires integrated original source module on GitHub CI')
    def test_actual_original_zero_shift_range_source_authenticated(self):
        r=authenticated_first_window_range_certificate()
        self.assertTrue(r['original_source_prime_tape_authenticated'])
        self.assertEqual(r['high_source_proof_replay'],'AMW-06B')
        self.assertFalse(r['shorted_low_sign_proved'])
        self.assertFalse(r['RH_proved'])

    @unittest.skipUnless(importlib.util.find_spec('observational_succ.source_weil_hierarchy'),
                         'requires integrated original source module on GitHub CI')
    def test_actual_original_source_high_schur_budget(self):
        r=authentic_hilbert_shifted_schur_budget(2,F(1,8),J=3)
        self.assertEqual(r['shifted_high_resolvent_penalty_upper'],
                         8*r['cross_operator_norm_upper']**2)
        self.assertTrue(r['high_sign_from_authentic_AMW_06B'])
        self.assertEqual(r['high_relative_K_gap'],F(369,10000))
        self.assertFalse(r['unshifted_lambda_zero_certified'])
        self.assertFalse(r['RH_proved'])

    @unittest.skipUnless(importlib.util.find_spec('observational_succ.source_weil_hierarchy'),
                         'requires integrated original source module on GitHub CI')
    def test_coupling_costs_more_as_shift_shrinks(self):
        a=authentic_hilbert_shifted_schur_budget(2,F(1,4),J=2)
        b=authentic_hilbert_shifted_schur_budget(2,F(1,16),J=2)
        self.assertEqual(b['shifted_high_resolvent_penalty_upper'],
                         4*a['shifted_high_resolvent_penalty_upper'])

    @unittest.skipUnless(importlib.util.find_spec('observational_succ.source_weil_hierarchy'),
                         'requires integrated original source module on GitHub CI')
    def test_forged_source_vector_float_refused(self):
        with self.assertRaises(HilbertAtlasError):
            authentic_hilbert_rayleigh(2,(1.,-1.,0.,0.),J=2)

if __name__=='__main__':
    unittest.main()
