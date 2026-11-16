"""Mathematics, calibration and adversarial controls for finite SUCC atlas."""
import unittest
from fractions import Fraction as Q
from itertools import product
from observational_succ.interferometer_atlas import (
    forcing, original_state,selected_hex_digits,source_shell_words,
    oily_grade,oily_harmonic,oily_tail,oily_mean_h,
    source_all_mode_transfer_budget,haar_next_digit_detail,
    haar_pair_oracle,haar_pair_response,haar_volume_energy,
    quarter_grid_weyl, quarter_grid_oily_energy,
    quarter_grid_oily_pair_oracle,quarter_grid_harmonic_energy,
    quarter_grid_gram_purity,quarter_grid_gram_pair_oracle,
    exact_digit_changes,exact_binary_changes,conductor_births,
    finite_witness_detect,propensity_corrected_mean)

class AtlasTests(unittest.TestCase):
    def test_forcing_immutable(self):
        for n in range(1,40):
            self.assertEqual(forcing(n),Q(120*n*n-89*n+16,(2*n-1)*(4*n-1)*(8*n-7)*(8*n-3)))
            self.assertGreater(forcing(n),0)

    def test_pointed_zero_and_successor(self):
        self.assertEqual(original_state(0),0)
        for n in range(0,22):
            self.assertEqual(original_state(n+1),16*original_state(n)+forcing(n+1))

    def test_oily_grade_normalization(self):
        self.assertEqual(oily_grade(0),Q(1,4))
        self.assertEqual(sum([oily_grade(j) for j in range(13)]),1-Q(15,2**14))

    def test_oily_nonzero_frequency_renormalization(self):
        for H in range(0,24):
            self.assertEqual(sum((oily_harmonic(h) for h in range(1,H+1)),Q(0))+oily_tail(H),1)
        self.assertEqual(oily_mean_h(),Q(8,3))

    def test_tail_monotone(self):
        for H in range(1,45):
            self.assertGreater(oily_tail(H-1),oily_tail(H))

    def test_rational_exact_source_digits(self):
        # pi/16 hexadecimal starts 0.3243f6a8885...
        digs=selected_hex_digits(9)
        self.assertEqual(''.join('0123456789abcdef'[d] for d in digs),'3243f6a88')

    def test_source_shell_words(self):
        for B in (1,2,4,8):
            w=source_shell_words(B,3)
            d=selected_hex_digits(2*B+3)
            self.assertEqual(len(w),B)
            self.assertEqual(w,tuple(d[n:n+3] for n in range(B,2*B)))

    def test_single_child_haar_all_identical(self):
        for k in range(6):
            self.assertEqual(haar_next_digit_detail(((3,)*7,)*4,k),1)

    def test_haar_invariant_of_full_symmetric_child_counts(self):
        words=tuple((a,) for a in range(16))
        self.assertEqual(haar_next_digit_detail(words,0),0)

    def test_haar_energy_positive_all_2digit_binary_controls(self):
        for digits in product(range(4),repeat=3):
            words=tuple((x, x^1) for x in digits)
            for k in range(2):
                self.assertEqual(haar_next_digit_detail(words,k),haar_pair_oracle(words,k))
                self.assertTrue(0<=haar_next_digit_detail(words,k)<=1)

    def test_haar_energy_source_prefix_sensitivity(self):
        for B in (2,3,5,9):
            words=source_shell_words(B,5)
            for k in range(5):
                self.assertEqual(haar_next_digit_detail(words,k),haar_pair_oracle(words,k))

    def test_haar_volume_tail_certification(self):
        w=source_shell_words(12,7)
        for K in range(1,8):
            v,tail=haar_volume_energy(w,K)
            self.assertEqual(tail,Q(1,2**K))
            self.assertTrue(0<=v<=1-tail)

    def test_quarter_grid_pair_equals_gram_harmonic(self):
        for n in range(1,5):
            for phases in product(range(4),repeat=n):
                for h in range(1,6):
                    r,i=quarter_grid_weyl(phases,h)
                    self.assertEqual(quarter_grid_harmonic_energy(phases,h),r*r+i*i)

    def test_oily_pair_matches_fourier_for_small_grids(self):
        for n in range(1,5):
            for phases in product(range(4),repeat=n):
                v,_=quarter_grid_oily_energy(phases,7)
                self.assertEqual(v,quarter_grid_oily_pair_oracle(phases,7))

    def test_fixed_point_false_r0_as_full_normality(self):
        for phase in range(4):
            p=(phase,)*5
            v,tail=quarter_grid_oily_energy(p,18)
            self.assertEqual(v,1-tail) # every Fourier mode locks

    def test_pi_transfer_uniform(self):
        for B in range(1,50):
            self.assertEqual(source_all_mode_transfer_budget(B),Q(7,12*B*B))
            self.assertLess(source_all_mode_transfer_budget(B+1),source_all_mode_transfer_budget(B))

    def test_gram_pair_matches_aggregate_energies(self):
        for n in range(1,5):
            for phases in product(range(4),repeat=n):
                for H in (2,3,4,5,7):
                    self.assertEqual(quarter_grid_gram_purity(phases,H),quarter_grid_gram_pair_oracle(phases,H))

    def test_gram_purity_fixed_source(self):
        for H in range(2,15):
            self.assertEqual(quarter_grid_gram_purity((0,)*6,H),H-1)

    def test_gram_purity_two_opposite_points(self):
        self.assertEqual(quarter_grid_gram_purity((0,2),2),0)
        self.assertEqual(quarter_grid_gram_purity((0,2),3),Q(2,3))

    def test_exact_hex_change_counts(self):
        d=selected_hex_digits(48)
        for B in (1,2,4,8,16):
            for k in (1,2,4):
                self.assertEqual(exact_digit_changes(d,B,k),Q(sum(d[n]!=d[n+k] for n in range(B,2*B)),B))

    def test_binary_change_count(self):
        d=selected_hex_digits(68)
        for B in (1,2,4,8,16):
            b=[(a>>i)&1 for a in d for i in (3,2,1,0)]
            self.assertEqual(exact_binary_changes(d,B),Q(sum(b[m]!=b[m+1] for m in range(4*B,8*B)),4*B))

    def test_conductor_primes_not_independent(self):
        flags=conductor_births(45)
        self.assertEqual(len(flags),45)
        self.assertEqual(flags[0],True)
        self.assertTrue(any(not q for q in flags))

    def test_one_sided_weil_sign_control(self):
        self.assertIsNone(finite_witness_detect((Q(1),Q(0),Q(2))))
        self.assertEqual(finite_witness_detect((Q(1),Q(-3,17),Q(0))),1)
        with self.assertRaises(ValueError):
            finite_witness_detect((0.0,))

    def test_adaptive_selection_requires_correct_weights(self):
        probs=(Q(1,2),Q(1,4),Q(1,8),Q(1,8))
        outputs=(Q(1),Q(0),Q(0),Q(0))
        self.assertEqual(sum((p*x for p,x in zip(probs,outputs)),Q(0)),Q(1,2))
        self.assertEqual(propensity_corrected_mean(probs,outputs),Q(1,4))
        with self.assertRaises(ValueError):
            propensity_corrected_mean((Q(1,2),Q(1,2),Q(0),Q(0)),outputs)

    def test_balanced_first_digit_can_hide_locked_future(self):
        # Even perfect uniformity among 16 first digits is NOT normality.
        words=tuple(tuple((i+j)%16 for j in range(4)) for i in range(16))
        self.assertEqual(haar_next_digit_detail(words,0),0)
        self.assertEqual(haar_next_digit_detail(words,1),Q(1,16))
        self.assertEqual(haar_next_digit_detail(words,2),Q(1,16))

    def test_zero_parity_does_not_imply_uniform_child_hierarchy(self):
        # Two source symbols with opposite parity, other 14 children absent.
        words=((0,),(1,))
        self.assertEqual(sum((-1)**x[0] for x in words),0)
        self.assertEqual(haar_next_digit_detail(words,0),Q(7,15))

    def test_invalid_inputs_fail_closed(self):
        for call in (lambda:forcing(0),lambda:oily_harmonic(0),
                     lambda:haar_next_digit_detail(((1,),),1),
                     lambda:source_shell_words(0,1),
                     lambda:quarter_grid_weyl((4,),1),
                     lambda:exact_binary_changes((1,),1)):
            with self.assertRaises(ValueError):call()

if __name__=='__main__':unittest.main()

class CertifiedOilyTests(unittest.TestCase):
    def test_machin_interval_narrows_with_refinement(self):
        from observational_succ.interferometer_atlas import machin_pi_interval
        q0=machin_pi_interval(5);q1=machin_pi_interval(9)
        self.assertLess(q0[0],q1[0])
        self.assertLess(q1[1],q0[1])
        self.assertLess(q1[1]-q1[0],Q(1,10**10))

    def test_certified_unit_quarter_phases(self):
        from observational_succ.interferometer_atlas import machin_pi_interval,certified_unit_character
        pi_box=machin_pi_interval(10)
        for q in (Q(0),Q(1,4),Q(1,2),Q(3,4),Q(1,8),Q(-1,4)):
            c,s,e=certified_unit_character(q,pi_box,10)
            self.assertGreaterEqual(e,0)
            if q%1==0:
                self.assertLessEqual(abs(c-1),e)
                self.assertLessEqual(abs(s),e)
            elif q%1==Q(1,2):
                self.assertLessEqual(abs(c+1),e)
                self.assertLessEqual(abs(s),e)

    def test_original_pi_oily_energy_bounds(self):
        from observational_succ.interferometer_atlas import certified_original_oily_energy
        for B in (2,4,8):
            obj=certified_original_oily_energy(B,8,machin_terms=9,taylor_degree=10)
            self.assertLessEqual(obj['lower'],obj['upper'])
            self.assertTrue(0<=obj['lower']<=obj['upper']<=1)
            self.assertGreater(obj['unseen_harmonic_tail'],0)
            self.assertGreater(obj['original_source_transport_budget'],0)
            self.assertIn('OPEN',obj['claim'])
