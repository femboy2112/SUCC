"""Hostile exact tests for history-memory learning, not pi normality."""
import unittest
from fractions import Fraction
from observational_succ.learning_pinbed import (
    RADIX, Learner, calibrated_phase, circle_at, four_pole, guard_margin,
    guarded_pin, learn_guarded_seed, learn_true_seed, oscillator_pin,
    seed, unwrapped_at, zero_source_history,
)


class LearningObserverTests(unittest.TestCase):
    def test_original_source_baseline_and_comoving_phase(self):
        a=zero_source_history(15)
        self.assertEqual(a[0],0)
        self.assertEqual(four_pole(1),Fraction(47,15))
        for n in range(1,len(a)):
            self.assertEqual(a[n]-16*a[n-1],four_pole(n))
        for N in (1,2,3):
            for k in (0,1,7,16**N-1):
                for n in range(N+2):
                    self.assertEqual(unwrapped_at(k,N,n),a[n]+16**n*seed(k,N))
                    self.assertEqual(calibrated_phase(k,N,n),(16**n*seed(k,N))%1)

    def test_present_circle_forgets_historical_seed_but_unwrapped_does_not(self):
        # Exact equality is restricted to circle projection, NOT the full carry.
        for N in (1,2,3,5):
            self.assertNotEqual(circle_at(0,N,0),circle_at(1,N,0))
            for t in range(N):
                self.assertNotEqual(circle_at(0,N,t),circle_at(1,N,t))
            for t in range(N,N+5):
                self.assertEqual(circle_at(0,N,t),circle_at(1,N,t))
                self.assertEqual(unwrapped_at(1,N,t)-unwrapped_at(0,N,t),16**(t-N))

    def test_each_local_pin_tells_exactly_one_seed_digit(self):
        for depth in (1,2,3):
            for index in range(min(16**depth,1000)):
                expected=tuple((index//(16**(depth-1-t)))%16 for t in range(depth))
                observed=tuple(oscillator_pin(index,depth,t,1) for t in range(depth))
                self.assertEqual(observed,expected)
                self.assertEqual(tuple(guarded_pin(index,depth,t) for t in range(depth)),expected)
                self.assertTrue(all(oscillator_pin(index,depth,t)==0
                                    for t in range(depth,depth+3)))

    def test_belief_shrinks_factor_16_and_then_becomes_certified(self):
        for depth,index in ((1,13),(2,0),(2,47),(3,0),(3,3145)):
            learner=Learner.full_grid(depth)
            self.assertEqual(len(learner.possible),16**depth)
            for t in range(depth):
                label=oscillator_pin(index,depth,t)
                learner=learner.observe(t,1,label)
                self.assertEqual(len(learner.possible),16**(depth-t-1))
                self.assertIn(index,learner.possible)
                self.assertEqual(learner.transcript[-1].bin_label,label)
            self.assertEqual(learner.possible,(index,))
            self.assertEqual(learner.truth_verdict(lambda k:k==index),"INVARIANT_TRUE")

    def test_active_mode_selects_informative_probe_and_fails_closed_at_tail(self):
        for depth,index in ((2,47),(3,3145)):
            learner=Learner.full_grid(depth)
            for t in range(depth):
                mode=learner.choose_mode(t)
                self.assertIsNotNone(mode)
                learner=learner.observe(t,mode,oscillator_pin(index,depth,t,mode))
            self.assertEqual(learner.possible,(index,))
            self.assertIsNone(Learner.full_grid(depth).choose_mode(depth))
            self.assertEqual(learn_true_seed(depth,index).possible,(index,))

    def test_claim_descends_after_learning_not_before(self):
        learner=Learner.full_grid(2)
        target=lambda i:i==0
        self.assertEqual(learner.truth_verdict(target),"AMBIGUOUS_TARGET_TRUE_COMPATIBLE")
        after1=learner.observe(0,1,0)
        self.assertEqual(len(after1.possible),16)
        self.assertEqual(after1.truth_verdict(target),"AMBIGUOUS_TARGET_TRUE_COMPATIBLE")
        self.assertEqual(after1.truth_verdict(lambda i:i<16),"INVARIANT_TRUE")
        after2=after1.observe(1,1,0)
        self.assertEqual(after2.possible,(0,))
        self.assertEqual(after2.truth_verdict(target),"INVARIANT_TRUE")
        self.assertEqual(after2.truth_verdict(lambda i:i==1),"INVARIANT_FALSE")

    def test_memory_cannot_be_function_of_present_circle(self):
        depth=2
        # For every seed, present state at time 2 agrees; retained transcripts
        # differ on all 256 cases (and preserve the original initial seed).
        states={circle_at(k,depth,depth) for k in range(16**depth)}
        self.assertEqual(len(states),1)
        transcripts={tuple(oscillator_pin(k,depth,t) for t in range(depth))
                     for k in range(16**depth)}
        self.assertEqual(len(transcripts),16**depth)
        # Any lossless memory code for all these histories needs >=8 bits.
        self.assertEqual((16**depth).bit_length()-1,8)

    def test_guarded_pin_has_exact_uniform_noise_margin(self):
        depth=2
        for t in range(depth):
            margin=guard_margin(depth,t)
            for k in range(16**depth):
                ideal=oscillator_pin(k,depth,t)
                self.assertEqual(guarded_pin(k,depth,t,margin/2),ideal)
                self.assertEqual(guarded_pin(k,depth,t,-margin/2),ideal)
        margin=guard_margin(depth,0)
        self.assertNotEqual(guarded_pin(0,depth,0,-2*margin),oscillator_pin(0,depth,0))
        self.assertEqual(learn_guarded_seed(2,47,(margin/3, -guard_margin(2,1)/3)).possible,(47,))

    def test_impossible_reports_and_untrusted_budget_rejected(self):
        learner=Learner.full_grid(2).observe(0,1,0)
        with self.assertRaises(ValueError):
            learner.observe(1,1,16)
        one=Learner.full_grid(1).observe(0,1,2)
        with self.assertRaises(ValueError):
            one.observe(0,1,3)
        with self.assertRaises(ValueError):
            learn_guarded_seed(2,47,(Fraction(0),guard_margin(2,1)))
        with self.assertRaises(ValueError):
            Learner.full_grid(4)
        with self.assertRaises(ValueError):
            learner.observe(-1,1,0)

    def test_every_source_corrected_closed_loop_is_seed_blind(self):
        for depth in (1,2,3):
            for idx in (0,1,16**depth-1):
                for n in range(0,7):
                    for d in range(1,5):
                        source_sum=Fraction()
                        for j in range(1,d+1):
                            source_sum=16*source_sum+four_pole(n+j)
                        self.assertEqual(unwrapped_at(idx,depth,n+d)-
                                         16**d*unwrapped_at(idx,depth,n),source_sum)


if __name__ == "__main__":
    unittest.main()
