"""Exact adversarial tests for finite distribution identities and source typing."""
import unittest
from fractions import Fraction as Q
from itertools import product

from observational_succ.logarithmic_sampling_succ import (
    source_r,canceled_source_r,states_through,pi_prefix,finite_green_tail,
    source_log_shift_ratio,log_shift_bounds_from_rational_epsilon,
    polynomial_at,polynomial_integral,polynomial_derivative,
    sawtooth_integral_exact,exact_weighted_sampling_identity,
    chiral_source,CHIRAL_PLUS,CHIRAL_MINUS,
    chiral_harmonic_counterterm,chiral_harmonic_remainder_constant_bound,
    chiral_harmonic_prefix,
    asymptotic_weight_equivalence,source_phase_tail_bound,
    source_log_shift_universal_upper,
    fixed_mellin_alias_upper,fixed_mellin_band_upper
)

class LogSamplingTest(unittest.TestCase):
    def test_original_source_four_signed_poles(self):
        for n in range(1,201):
            self.assertEqual(source_r(n),canceled_source_r(n))
            self.assertEqual(source_r(n).denominator%2,1)
            self.assertGreater(source_r(n),0)

    def test_native_original_source_if_present(self):
        try:
            from observational_succ.succ_internal_matrix_walk import authentic_r
        except ModuleNotFoundError:
            self.skipTest('native upstream SUCC source absent from isolated test environment')
        for n in range(1,101):
            self.assertEqual(source_r(n),authentic_r(n))

    def test_green_tail_exact_identity_and_bound(self):
        for L in (8,17,44):
            piL=pi_prefix(L)
            states=states_through(L)
            for n in range(1,L+1):
                tail=finite_green_tail(n,L)
                self.assertEqual(BASE_POW(n)*piL-states[n],tail)
                self.assertGreaterEqual(tail,0)
                self.assertLess(tail,Q(1,15*(n+1)**2))

    def test_rational_chart_shift_and_positive_log_bound(self):
        for L in (12,25,42):
            states=states_through(L)
            piL=pi_prefix(L)
            for time_index in range(L-1):
                epsilon=source_log_shift_ratio(time_index,L)
                n=time_index+1
                self.assertEqual(1-epsilon,states[n]/(piL*16**time_index))
                low,high=log_shift_bounds_from_rational_epsilon(epsilon)
                self.assertTrue(0<=low<=high)
                self.assertLess(high,Q(1,170))
                self.assertLess(high,source_log_shift_universal_upper(time_index)*2)

    def test_exact_polynomial_sawtooth_for_unshifted_clock(self):
        coeffs=((Q(3),),(Q(0),Q(1)),(Q(7),Q(-2),Q(5)),
                (Q(-1),Q(4),Q(3,7),Q(-2),Q(1,2)))
        for coeff,a,N in product(coeffs,(Q(1),Q(2,3),Q(11,4)),(1,2,4,9)):
            got=exact_weighted_sampling_identity(coeff,a,(Q(0),)*N)
            self.assertEqual(got['source_pulse'],0)
            self.assertEqual(got['defect_left'],got['defect_right'])

    def test_arithmetic_pulses_exact_for_arbitrary_polynomials(self):
        # A negative first source time and disjoint positive subsequent sites
        # are both allowed. The finite Dirac/sawtooth identity remains exact.
        shifts=(Q(1,180),Q(1,400),Q(1,1600),Q(1,5000))
        for coeff,a in product(((Q(1),),(Q(0),Q(1)),(Q(0),Q(0),Q(1)),
                                (Q(3),Q(-7),Q(0),Q(4),Q(1))),
                               (Q(1),Q(7,3))):
            got=exact_weighted_sampling_identity(coeff,a,shifts)
            self.assertEqual(got['defect_left'],got['defect_right'])
            expected=sum((polynomial_at(coeff,j*a-d) for j,d in enumerate(shifts)),Q())
            self.assertEqual(got['sample'],expected)

    def test_distributional_sign_mutation_is_rejected(self):
        coeff=(Q(0),Q(1))
        shifts=(Q(1,4),Q(1,8),Q(1,16))
        got=exact_weighted_sampling_identity(coeff,1,shifts)
        self.assertNotEqual(got['source_pulse'],0)
        self.assertNotEqual(got['defect_left'],got['boundary']+got['sawtooth']+got['source_pulse'])

    def test_exact_chiral_logarithmic_mass_cancellation(self):
        self.assertEqual(sum(CHIRAL_PLUS),Q(15,4))
        self.assertEqual(sum(CHIRAL_MINUS),Q(-15,4))
        self.assertEqual(sum(CHIRAL_PLUS)+sum(CHIRAL_MINUS),0)
        for n in range(1,201):
            self.assertEqual(chiral_source(n,'+')+chiral_source(n,'-'),source_r(n))

    def test_chiral_gamma_harmonic_counterterms_cancel_exactly(self):
        # Each isolated chiral lane has a +-15/32 harmonic divergence.
        # Joining them cancels the harmonic (and therefore gamma) exactly.
        for n in (2,7,40,120):
            plus=chiral_harmonic_prefix(n,'+')
            minus=chiral_harmonic_prefix(n,'-')
            self.assertEqual(plus['raw']+minus['raw'],
                             sum((source_r(j) for j in range(1,n+1)),Q()))
            self.assertEqual(plus['counterterm_sum']+minus['counterterm_sum'],
                             plus['raw']+minus['raw'])
            self.assertEqual(plus['harmonic'],minus['harmonic'])
        for sign in ('+','-'):
            C=chiral_harmonic_remainder_constant_bound(sign)
            self.assertGreater(C,0)
            # A fully rational tail bound follows from the exact 1/n^2 envelope.
            for n in (10,30,60):
                partial=sum((chiral_harmonic_counterterm(j,sign)
                             for j in range(n+1,181)),Q())
                self.assertLessEqual(abs(partial),C/Q(n))

    def test_gamma_and_oily_abstract_weights_are_asymptotically_scalar(self):
        # A toy packet model with exact grade error c/n.
        for N in (1,10,100):
            c=Q(4,9)
            weights=tuple(c+Q(1,n) for n in range(1,N+1))
            got=asymptotic_weight_equivalence(weights,c)
            harmonic=sum((Q(1,n) for n in range(1,N+1)),Q())
            self.assertEqual(got,harmonic/N)
            # Centered weights alone "cancel" even a coherent z_n=1 control.
            self.assertEqual(sum((w-c for w in weights),Q())/N,got)
            self.assertGreater(got,0)

    def test_nonvanishing_gamma_scalar_does_not_create_cancellation(self):
        weights=tuple(Q(4,9) for _ in range(20))
        self.assertEqual(asymptotic_weight_equivalence(weights,Q(4,9)),0)
        self.assertEqual(sum(weights,Q())/20,Q(4,9))
        # Ordinary rational alpha=1 has all base-16 radix phases exactly 1.
        for n in range(20):
            self.assertEqual(Q(16**n)%1,0)

    def test_source_tail_bound_is_monotone_and_nonvacuous(self):
        for h in (1,2,5):
            previous=None
            for start in range(1,60):
                bound=source_phase_tail_bound(start,h)
                self.assertGreater(bound,0)
                if previous is not None:self.assertLess(bound,previous)
                previous=bound
            self.assertLess(source_phase_tail_bound(1000,h),Q(1,100))

    def test_fixed_mellin_aliases_cannot_explain_rational_radix_coherence(self):
        # All fixed k integrals have an explicit T-uniform rational bound.
        # But for alpha=1 the actual discrete phase is constantly 1.
        for h in (1,-2,5):
            for alpha in (Q(1),Q(-2,3),Q(7,11)):
                for K in (0,1,3,8):
                    budget=sum((fixed_mellin_alias_upper(k,h,alpha)
                                for k in range(-K,K+1)),Q())
                    self.assertEqual(budget,fixed_mellin_band_upper(K,h,alpha))
                    self.assertGreater(budget,0)
        for n in range(100):
            self.assertEqual(16**n%1,0)
        with self.assertRaises(ValueError):fixed_mellin_alias_upper(0,0,Q(1))
        with self.assertRaises(ValueError):fixed_mellin_band_upper(1,1,Q(0))

    def test_invalid_input_controls(self):
        with self.assertRaises(ValueError): source_r(0)
        with self.assertRaises(ValueError): states_through(-1)
        with self.assertRaises(ValueError): log_shift_bounds_from_rational_epsilon(Q(1))
        with self.assertRaises(ValueError): exact_weighted_sampling_identity((1,),0,(Q(0),))
        with self.assertRaises(ValueError): exact_weighted_sampling_identity((1,),1,(Q(-1),))
        with self.assertRaises(ValueError): asymptotic_weight_equivalence((),Q(1))
        with self.assertRaises(ValueError): source_phase_tail_bound(5,1.0)


def BASE_POW(n):return Q(16**(n-1))

if __name__=='__main__':unittest.main()
