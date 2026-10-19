"""Hostile exact controls of the hidden-memory Schur telescope.

None of these toy matrices is the unmodified original Suzuki source.
"""
import sys
import unittest
from fractions import Fraction as F
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from observational_succ import hidden_memory_schur as H


class HiddenMemoryFiniteTests(unittest.TestCase):

    def test_carrier_spectral_observer_has_no_gamma_memory(self):
        x=H.positive_jump_projection_memory(((2,0),(0,3)),((1,0),(0,0)))
        self.assertTrue(x['positive_carrier_reduces_observer'])
        self.assertEqual(x['memory_kernel_at_t0'],H.zeros(2,2))

    def test_nonreducing_observer_acquires_real_memory(self):
        x=H.positive_jump_projection_memory(((2,1),(1,2)),((1,0),(0,0)))
        self.assertFalse(x['positive_carrier_reduces_observer'])
        self.assertEqual(x['memory_kernel_at_t0'],((F(1),F()),(F(),F())))

    def test_forged_nonorthogonal_projection_rejected(self):
        with self.assertRaises(H.HiddenMemoryError):
            H.positive_jump_projection_memory(((2,0),(0,3)),((1,1),(0,0)))

    def test_exact_finite_schur_single(self):
        z=H.rational_memory_telescope(((F(3,2),),),((F(1),),),((F(1),),),3,
            step=F(1),high_gap=F(1),coupling_sq_upper=F(1))
        self.assertEqual(z['actual_finite_S'],((F(1,2),),))
        self.assertEqual(z['finite_upper_S'],((F(5,8),),))
        self.assertEqual(z['memory_response_prefix'],((F(7,8),),))
        self.assertEqual(z['Loewner_error_cap'],F(1,8))
        self.assertEqual(z['verdict'],'POSITIVE_FINITE_MODEL')

    def test_negative_eventually(self):
        z=H.rational_memory_telescope(((F(1,2),),),((1,),),((1,),),2,
             step=F(1),high_gap=F(1),coupling_sq_upper=F(1))
        self.assertEqual(z['actual_finite_S'],((-F(1,2),),))
        self.assertEqual(z['finite_upper_S'],((-F(1,4),),))
        self.assertEqual(z['verdict'],'NEGATIVE_FINITE_MODEL')

    def test_singular_never_promotes_sign(self):
        for depth in range(1,9):
            z=H.rational_memory_telescope(((1,),),((1,),),((1,),),depth,
                  step=F(1),high_gap=F(1),coupling_sq_upper=F(2))
            self.assertEqual(z['actual_finite_S'],((F(),),))
            self.assertEqual(z['finite_upper_S'],((F(1,2**depth),),))
            self.assertEqual(z['verdict'],'AMBIGUOUS')

    def test_multi_low_dimensions(self):
        A=((F(2),0),(0,F(2)))
        B=((F(1),0),(0,F(1)))
        D=((F(2),0),(0,F(3)))
        z=H.rational_memory_telescope(A,B,D,7,step=F(1),high_gap=F(2),coupling_sq_upper=1)
        self.assertEqual(z['actual_finite_S'],((F(3,2),F()),(F(),F(5,3))))
        self.assertTrue(H.is_psd(z['finite_lower_S']))

    def test_hidden_block_couplings(self):
        A=((1,0),(0,1))
        B=((F(1,2),F(1,2)),(F(1,2),-F(1,2)))
        D=((2,F(1,4)),(F(1,4),2))
        z=H.rational_memory_telescope(A,B,D,8,step=F(1),high_gap=F(7,4),coupling_sq_upper=F(1,2))
        self.assertTrue(H.is_psd(z['finite_lower_S']))
        self.assertTrue(H.psd_diff(z['finite_upper_S'],z['actual_finite_S']))

    def test_depth_monotone_upper(self):
        last=None
        for n in range(8):
            out=H.rational_memory_telescope(((2,),),((1,),),((2,),),n,step=F(1),high_gap=F(2),coupling_sq_upper=1)
            if last is not None:self.assertLessEqual(out['finite_upper_S'][0][0],last)
            last=out['finite_upper_S'][0][0]

    def test_453_cell_rational_budget(self):
        x=H.finite_cell_algebraic_budget(64)
        self.assertEqual(x['rank'],453)
        self.assertEqual(x['squared_cross_cap'],249901074)
        self.assertEqual(x['tail_upper'],F(444268576,2**64))
        self.assertLess(x['tail_upper'],F(1,10**9))
        self.assertFalse(x['source_verified'])

    def test_642_source_clock_observer_budget(self):
        x=H.finite_cell_algebraic_budget(64,642)
        self.assertEqual(x['rank'],642)
        self.assertEqual(x['squared_cross_cap'],501711444)
        self.assertEqual(x['tail_upper'],F(891931456,2**64))
        self.assertLess(x['tail_upper'],F(1,10**9))

    def test_453_cell_depth_halves(self):
        for n in (0,1,8,32):
            self.assertEqual(H.finite_cell_algebraic_budget(n+1)['tail_upper']*2,
                             H.finite_cell_algebraic_budget(n)['tail_upper'])

    def test_rational_log2_453_642_alignment(self):
        lo,hi=H.log2_rational_interval(40)
        self.assertTrue(F(313)+F(199,200) < 453*lo <453*hi<F(314))
        self.assertLess(F(314)-453*lo,F(1,200))
        self.assertLess(642*hi-F(445),F(1,2000))
        self.assertGreater(642*lo,F(445))

    def test_true_fractional_cell_shift_sparse(self):
        v=(F(1),F(2),F(3),F(4),F(5))
        x=H.exact_prime_cell_shift(v,5,F(11,20))
        self.assertEqual(x['floor_lag'],2)
        self.assertEqual(x['fractional_part'],F(3,4))
        self.assertEqual(x['true_shift_correlation'],F(1,4)*(1*3+2*4+3*5)+F(3,4)*(1*4+2*5))
        self.assertGreaterEqual(x['correlation_error_cap'],abs(x['true_shift_correlation']-x['nearest_integer_clock_correlation']))

    def test_pure_integer_shift_zero_residual(self):
        x=H.exact_prime_cell_shift((1,2,3,4,5),5,F(2,5))
        self.assertEqual(x['lag_displacement_error'],0)
        self.assertEqual(x['true_shift_correlation'],x['nearest_integer_clock_correlation'])

    def test_prime_cell_invalid_fabricated_atom(self):
        with self.assertRaises(H.HiddenMemoryError):
            H.exact_prime_cell_shift((1,2),2,F(3,2))

    def test_zero_depth_and_zero_cross(self):
        z=H.rational_memory_telescope(((1,),),((0,),),((1,),),0,step=1,high_gap=1,coupling_sq_upper=0)
        self.assertEqual(z['finite_upper_S'],z['actual_finite_S'])
        self.assertEqual(z['Loewner_error_cap'],0)

    def test_bad_high_gap(self):
        with self.assertRaises(H.HiddenMemoryError):
            H.rational_memory_telescope(((2,),),((1,),),((1,),),1,high_gap=2)

    def test_bad_coupling_claim(self):
        with self.assertRaises(H.HiddenMemoryError):
            H.rational_memory_telescope(((2,),),((1,),),((1,),),1,coupling_sq_upper=F(1,2))

    def test_bad_input_type(self):
        for fn in (lambda:H.q(1.0),lambda:H.q(True),lambda:H.q('0')):
            with self.assertRaises(H.HiddenMemoryError):fn()

    def test_bad_shape(self):
        with self.assertRaises(H.HiddenMemoryError):
            H.rational_memory_telescope(((1,0),(0,1)),((1,),),((1,),),2)

    def test_bad_negative_depth(self):
        with self.assertRaises(H.HiddenMemoryError):
            H.rational_memory_telescope(((1,),),((1,),),((1,),),-1)

    def test_matrix_inertia_and_inverse(self):
        a=((2,1),(1,2))
        inv=H.matrix_inv(a)
        self.assertEqual(H.mult(a,inv),H.eye(2))
        self.assertTrue(H.is_psd(a))
        self.assertFalse(H.is_psd(((1,2),(2,1))))


class HiddenMemorySamplingTests(unittest.TestCase):
    def test_single_vs_delayed_measurement(self):
        x=H.two_read_hidden_gaussian(hidden_coupling=1,noise_variance=1)
        self.assertEqual(x['one_read_hidden_conditional_variance'],1)
        self.assertEqual(x['two_read_hidden_conditional_variance'],F(1,2))
        self.assertEqual(x['variance_gain'],F(1,2))
        self.assertFalse(x['thermodynamic_work_claimed'])

    def test_no_environmental_reaction(self):
        x=H.two_read_hidden_gaussian(hidden_coupling=0,noise_variance=1)
        self.assertEqual(x['variance_gain'],0)
        self.assertTrue(x['independent_environment_negative_control'])

    def test_nontrivial_delay_and_noise(self):
        x=H.two_read_hidden_gaussian(hidden_coupling=F(2),noise_variance=F(3))
        self.assertEqual(x['two_read_hidden_conditional_variance'],F(3,7))

    def test_no_negative_noise(self):
        with self.assertRaises(H.HiddenMemoryError):H.two_read_hidden_gaussian(noise_variance=0)

    def test_scalar_hankel_two_sources_same_two_readouts_opposite_sign(self):
        single=H.scalar_memory_hankel((1,),((1,),),4)
        b=(F(3,5),F(4,5))
        d=((F(37,13),F()),(F(),F(73,127)))
        double=H.scalar_memory_hankel(b,d,4)
        self.assertEqual(single[:2],double[:2])
        self.assertEqual(single[:2],(F(1),F(1,2)))
        self.assertNotEqual(single[2],double[2])
        rec1=H.reconstruct_two_hidden_lags(single)
        rec2=H.reconstruct_two_hidden_lags(double)
        self.assertEqual(rec1['zero_shift_inverse_response'],F(1))
        self.assertEqual(rec2['zero_shift_inverse_response'],F(3349,2701))
        A=F(9,8)
        self.assertGreater(A-rec1['zero_shift_inverse_response'],0)
        self.assertLess(A-rec2['zero_shift_inverse_response'],0)
        self.assertGreater(F(73,127),F(9,16))

    def test_exact_two_mode_recovery(self):
        b=(F(3,5),F(4,5));d=((F(37,13),F()),(F(),F(73,127)))
        z=H.reconstruct_two_hidden_lags(H.scalar_memory_hankel(b,d,4))
        self.assertEqual(z['modes'],(F(13,50),F(127,200)))
        self.assertEqual(z['weights'],(F(9,25),F(16,25)))

    def test_negative_hankel_mutant(self):
        with self.assertRaises(H.HiddenMemoryError):H.reconstruct_two_hidden_lags((1,1,0,0))

    def test_bad_truncated_four_moments(self):
        with self.assertRaises(H.HiddenMemoryError):H.reconstruct_two_hidden_lags((1,2,3))

    def test_memory_hankel_psd_and_rank(self):
        moments=H.scalar_memory_hankel((F(3,5),F(4,5)),
            ((F(37,13),F()),(F(),F(73,127))),5)
        pkt=H.finite_hankel_nonnegative(moments,3)
        self.assertTrue(pkt['nonnegative'])
        self.assertEqual(H.determinant(pkt['hankel_matrix']),0)
        self.assertGreater(H.determinant((pkt['hankel_matrix'][0][:2],pkt['hankel_matrix'][1][:2])),0)

    def test_negative_memory_hankel_detected(self):
        self.assertFalse(H.finite_hankel_nonnegative((1,2,1),2)['nonnegative'])

    def test_nonrational_reconstruction_fails_closed(self):
        with self.assertRaises(H.HiddenMemoryError):H.rational_sqrt(F(2))

    def test_one_mode_false_fourth_moment_fails(self):
        with self.assertRaises(H.HiddenMemoryError):H.reconstruct_two_hidden_lags((1,F(1,2),F(1,4),F(1,5)))


class AuthenticSourceInterface(unittest.TestCase):
    def test_actual_jump_source_memory_depth(self):
        try:
            from observational_succ.source_jump_spectral import authenticate_original_jump_rank_budget
        except ImportError:
            self.skipTest("isolated fixture lacks original SUCC source; hosted CI must execute")
        r=H.original_source_memory_budget(12)
        self.assertEqual(r['discrete_hidden_memory_tail_upper'],F(121,64*4096))
        self.assertEqual(r['source_low_rank_upper'],453)
        self.assertEqual(r['signed_high_gap_lower'],F(9,16))
        self.assertFalse(r['source_high_projector_built'])
        self.assertFalse(r['source_delayed_resolvent_probes_computed'])
        self.assertFalse(r['RH_proved'])

    def test_real_453_cell_observer_bound(self):
        try:
            from observational_succ.source_jump_spectral import authenticate_original_jump_rank_budget
        except ImportError:
            self.skipTest("standalone fixture; original SHA source required")
        packet=H.explicit_cell_source_memory_budget(64)
        self.assertEqual(packet['source_conditional_memory_tail_upper'],F(444268576,2**64))
        self.assertEqual(packet['explicit_equal_cell_observation_rank'],453)
        self.assertTrue(packet['source_positive_carrier_memory_may_be_nonzero'])
        self.assertFalse(packet['polar_cross_only'])
        self.assertFalse(packet['first_window_Weil_sign_proved'])

    def test_actual_prime_clock_source_alignment(self):
        try:
            from observational_succ.source_weil_hierarchy import log2_iv
        except ImportError:
            self.skipTest("isolated test missing frozen authentic prime tape")
        x=H.source_prime2_cell_alignment(453)
        y=H.source_prime2_cell_alignment(642)
        self.assertEqual(x['nearest_SUCC_integer_shift'],314)
        self.assertEqual(y['nearest_SUCC_integer_shift'],445)
        self.assertLess(y['phase_error_certified_upper'],F(1,2000))
        self.assertEqual(y['prime_quadratic_Succ_vs_Fucc_error_bound_per_unit_norm'],F(1,1000))

    def test_real_642_source_clock_observer_budget(self):
        try:
            from observational_succ.source_jump_spectral import authenticate_original_jump_rank_budget
        except ImportError:
            self.skipTest("original-Suzuki only; CI source must execute")
        packet=H.explicit_cell_source_memory_budget(64,642)
        self.assertEqual(packet['explicit_equal_cell_observation_rank'],642)
        self.assertEqual(packet['source_conditional_memory_tail_upper'],F(891931456,2**64))

    def test_original_source_budget_decay(self):
        try:
            from observational_succ.source_jump_spectral import authenticate_original_jump_rank_budget
        except ImportError:
            self.skipTest("isolation only; must run in full original SUCC checkout")
        a=H.original_source_memory_budget(5)
        b=H.original_source_memory_budget(6)
        self.assertEqual(b['discrete_hidden_memory_tail_upper']*2,a['discrete_hidden_memory_tail_upper'])


if __name__=='__main__':unittest.main()
