"""Exact Bayesian finite-phase controls for immutable original BBP chiral taps."""
import unittest
from fractions import Fraction as F
from observational_succ.chiral_virtual_phase_prior import (
    TAPS,ACTIVE,uniform_phase_prior,predicted_activity,
    posterior_phase,minimum_identifying_horizon,phase_hamming_distance,
    expected_log_odds_gain_per_period,authentic_chiral_tap, resolved_activity,guaranteed_silence_cycle,
)


class ChiralPhasePriorTests(unittest.TestCase):
    def test_literal_original_signed_taps(self):
        self.assertEqual(TAPS,(4,0,0,-2,-1,-1,0,0))
        self.assertEqual(ACTIVE,(1,0,0,1,1,1,0,0))

    def test_source_prior_precedes_receipts(self):
        self.assertEqual(posterior_phase(uniform_phase_prior(),()),uniform_phase_prior())

    def test_causal_receipt_five_ticks_completes_exact_phase(self):
        self.assertEqual(minimum_identifying_horizon(),5)
        for phase in range(8):
            actual=tuple((n,predicted_activity(phase,n)) for n in range(5))
            post=posterior_phase(uniform_phase_prior(),actual)
            self.assertEqual(post[phase],1)
            self.assertEqual(sum(post),1)
            self.assertTrue(all(q==0 for j,q in enumerate(post) if j!=phase))

    def test_four_receipts_not_sufficient_for_every_phase(self):
        words=[tuple(predicted_activity(k,n) for n in range(4)) for k in range(8)]
        self.assertEqual(len(set(words)),7)

    def test_sensor_noise_prevents_finite_exact_certainty(self):
        data=tuple((t,predicted_activity(0,t)) for t in range(8))
        post=posterior_phase(uniform_phase_prior(),data,F(1,4))
        self.assertTrue(F(1,8)<post[0]<1)
        self.assertTrue(all(p>0 for p in post))

    def test_fully_noisy_sensor_reveals_nothing(self):
        data=tuple((t,predicted_activity(0,t)) for t in range(5))
        self.assertEqual(posterior_phase(uniform_phase_prior(),data,F(1,2)),uniform_phase_prior())

    def test_exact_prior_not_unique(self):
        root=(F(1),)+(F(0),)*7
        data=((0,1),)
        self.assertEqual(posterior_phase(root,data,F(1,4)),root)
        self.assertNotEqual(posterior_phase(uniform_phase_prior(),data,F(1,4)),root)

    def test_source_period_distinguishability(self):
        self.assertEqual(phase_hamming_distance(0,0),0)
        self.assertTrue(all(phase_hamming_distance(0,p)>0 for p in range(1,8)))
        self.assertTrue(all(expected_log_odds_gain_per_period(0,p,F(1,4))>0 for p in range(1,8)))

    def test_actual_contracting_eight_shell(self):
        for n in range(8*6):
            self.assertEqual(authentic_chiral_tap(n),TAPS[n%8]/16**(n//8))

    def test_fixed_absolute_resolution_exhausts_activity(self):
        for floor in (F(1,1),F(1,100),F(1,10000)):
            k=guaranteed_silence_cycle(floor)
            for t in range(8*k,8*(k+2)):
                for p in range(8):
                    self.assertEqual(resolved_activity(p,t,floor),0)
        with self.assertRaises(ValueError):guaranteed_silence_cycle(0)

    def test_ideal_activity_requires_exact_detection(self):
        for t in range(100):
            for p in range(8):
                self.assertEqual(resolved_activity(p,t,0),predicted_activity(p,t))

    def test_invalid_evidence_and_prior(self):
        with self.assertRaises(ValueError):posterior_phase((F(1),)*8,())
        with self.assertRaises(ValueError):posterior_phase(uniform_phase_prior(),((0,3),))
        with self.assertRaises(ValueError):posterior_phase(uniform_phase_prior(),((-1,1),))
        with self.assertRaises(ValueError):posterior_phase(uniform_phase_prior(),((0,1),),F(3,4))
        with self.assertRaises(ValueError):expected_log_odds_gain_per_period(0,1,0)

if __name__=='__main__':unittest.main()
