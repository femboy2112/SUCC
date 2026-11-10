"""Independent exact rational controls for Aphex conditional Haar descent."""
import unittest
from fractions import Fraction as F

from observational_succ.aphex_two_fiber_haar import (
    two_fiber_haar, original_bbp_two_fiber,
    perturbation_budget, real_parity_bound,
)
from observational_succ.bbp_parity_pressure import original_zero_parity_states


class TwoFiberHaarTests(unittest.TestCase):
    def test_exact_four_cell_original_source_count_oracle(self):
        # Matches already reported A=512 ORIGINAL-SOURCE joint counts
        # (254 plus-prime signs, 258 minus-prime signs); not a new holdout.
        a=[1]*254+[-1]*258
        b=[1]*133+[-1]*121+[1]*125+[-1]*133
        t=two_fiber_haar(a,b)
        self.assertEqual((t.n_plus,t.n_minus),(254,258))
        self.assertEqual(t.complement_given_plus,F(6,127))
        self.assertEqual(t.complement_given_minus,F(-4,129))
        self.assertEqual(t.haar_detail,F(641,16383))
        self.assertEqual(t.common_response,F(133,16383))
        self.assertEqual(t.a_mean,F(-1,128))
        self.assertEqual(t.b_mean,F(1,128))
        self.assertEqual(t.parity_mean,F(5,128))
        self.assertEqual(t.source_error,F(133,2097024))
        self.assertEqual(t.conditional_residual_energy,F(1046843,2097024))
        self.assertGreaterEqual(real_parity_bound(t,F(1,128)),abs(t.parity_mean))

    def test_actual_source_window_same_exact_values(self):
        original=list(original_zero_parity_states(1023))
        t=original_bbp_two_fiber(original[511:1023],1217)
        self.assertEqual(t.n,512)
        self.assertEqual(t.complement_given_plus,F(6,127))
        self.assertEqual(t.complement_given_minus,F(-4,129))
        self.assertEqual(t.haar_detail,F(641,16383))
        self.assertEqual(t.parity_mean,F(5,128))

    def test_zero_loss_nonnormal_source_p_integral_shadow(self):
        # This is the correct b=a countermodel from #572's coherent wrong seed.
        a=[1]*254+[-1]*258
        t=two_fiber_haar(a,a)
        self.assertEqual(t.complement_given_plus,1)
        self.assertEqual(t.complement_given_minus,-1)
        self.assertEqual(t.haar_detail,1)
        self.assertEqual(t.conditional_residual_energy,0)
        self.assertEqual(t.parity_mean,1)
        self.assertEqual(t.source_error,0)

    def test_false_optimistic_observer_gains(self):
        a=[1,-1]*8
        plus=two_fiber_haar(a,a)
        minus=two_fiber_haar(a,[-x for x in a])
        self.assertEqual(plus.a_mean,minus.a_mean)
        self.assertEqual(plus.haar_detail,1)
        self.assertEqual(minus.haar_detail,-1)
        self.assertEqual(plus.conditional_residual_energy,0)
        self.assertEqual(minus.conditional_residual_energy,0)
        # Their REAL parity signs are opposite, local prime tape identical.
        self.assertEqual(plus.parity_mean,1)
        self.assertEqual(minus.parity_mean,-1)

    def test_sharp_marginal_error_bound(self):
        a=[1]*10+[-1]*6
        for b_const in (1,-1):
            t=two_fiber_haar(a,[b_const]*16)
            self.assertEqual(t.haar_detail,0)
            self.assertEqual(t.parity_mean,t.a_mean*b_const)
            self.assertEqual(t.source_error,abs(t.a_mean))
            self.assertEqual(real_parity_bound(t,abs(t.a_mean)),abs(t.parity_mean))

    def test_sharp_probe_error_bound(self):
        a=[1]*10+[-1]*6
        b=[1]*16
        bh=[F(1) if x==1 else F(1,2) for x in a]
        diff,bound,eps=perturbation_budget(a,b,bh)
        self.assertEqual(eps,F(3,16))
        self.assertEqual(diff,F(1,4))
        self.assertEqual(diff,bound)

    def test_calibration_error_on_randomish_words(self):
        for N in (20,32,64):
            a=[1 if (i*7)%11<5 else -1 for i in range(N)]
            b=[1 if (i*i+3*i+2)%7<3 else -1 for i in range(N)]
            t=two_fiber_haar(a,b)
            self.assertLessEqual(t.source_error,abs(t.a_mean))
            self.assertLessEqual(abs(t.parity_mean),abs(t.haar_detail)+abs(t.a_mean))
            bh=[F(3,4)*x for x in b]
            diff,bound,eps=perturbation_budget(a,b,bh)
            self.assertLessEqual(diff,bound)

    def test_invalid_inputs_fail_closed(self):
        with self.assertRaises(ValueError): two_fiber_haar([1]*4,[1]*4)
        with self.assertRaises(ValueError): two_fiber_haar([1,-1],[1])
        with self.assertRaises(ValueError): two_fiber_haar([1,0],[1,1])
        t=two_fiber_haar([1]*5+[-1]*3,[1]*8)
        with self.assertRaises(ValueError): real_parity_bound(t,F(0))
        with self.assertRaises(ValueError): perturbation_budget([1,-1],[1,1],[1])
        with self.assertRaises(ValueError): original_bbp_two_fiber([],1217)

if __name__=="__main__": unittest.main()
