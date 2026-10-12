"""Independent exact rank, recurrence and delayed-source controls."""
import unittest
import random
from fractions import Fraction as F
from itertools import product
from observational_succ.carrier_hankel_bounds import (
    RealizationError, determinant, rank, hankel, hankel_dimension_receipt,
    verify_dimension_receipt, linear_recurrence_prefix,
    forecast_from_recurrence, delayed_impulse, impulse_realization_check,
)

class HankelProofTests(unittest.TestCase):
    def test_alternating_observation_forces_two_dimensional_lti_carrier(self):
        values=tuple(F(1+(-1)**i) for i in range(8))
        self.assertEqual(hankel(values,2,2),((2,0),(0,2)))
        proof=hankel_dimension_receipt(values,3,3)
        self.assertEqual(proof['linear_state_lower_bound'],2)
        self.assertTrue(verify_dimension_receipt(values,proof))
        reconstruction=linear_recurrence_prefix(values,2)
        self.assertTrue(reconstruction['all_supplied_samples_match'])
        self.assertEqual(reconstruction['coefficients'],(F(1),F(0)))
        self.assertEqual(forecast_from_recurrence(values[:2],(1,0),6),values)

    def test_fibonacci_hankel_realization(self):
        seq=[F(0),F(1)]
        for i in range(18):seq.append(seq[-1]+seq[-2])
        r=hankel_dimension_receipt(seq,8,8)
        self.assertEqual(r['linear_state_lower_bound'],2)
        self.assertTrue(verify_dimension_receipt(seq,r))
        fit=linear_recurrence_prefix(seq,2)
        self.assertEqual(fit['coefficients'],(1,1))
        self.assertTrue(fit['all_supplied_samples_match'])
        self.assertEqual(forecast_from_recurrence(seq[:2],(1,1),18),tuple(seq))

    def test_delayed_externality_mimic_arbitrarily_late(self):
        for h in range(1,14):
            seq=delayed_impulse(h)
            self.assertEqual(seq[:h],(F(0),)*h)
            cert=impulse_realization_check(h)
            self.assertEqual(cert['minimal_linear_state_dimension'],h+1)
            self.assertIn(cert['lower_bound_minor_determinant'],(F(1),F(-1)))
        self.assertEqual(impulse_realization_check(0)['minimal_linear_state_dimension'],1)

    def test_gauge_equivalent_internal_realizations_same_hankel(self):
        # Two distinct state-coordinate models: A=diag(2,3) vs
        # A'=S A S^-1, b'=S b, c'=c S^-1. Both realize y_n=2^n+3^n.
        seq=tuple(F(2**n+3**n) for n in range(16))
        proof=hankel_dimension_receipt(seq,6,6)
        self.assertEqual(proof['linear_state_lower_bound'],2)
        self.assertEqual(linear_recurrence_prefix(seq,2)['coefficients'],(-6,5))
        self.assertEqual(seq[5],2**5+3**5)
        self.assertTrue(verify_dimension_receipt(seq,proof))

    def test_even_tiny_sample_prefix_does_not_authorize_forecast(self):
        seq=tuple(F(1+(-1)**n) for n in range(4))
        rec=linear_recurrence_prefix(seq,2)
        self.assertEqual(rec['holdout_count'],0)
        self.assertFalse(rec['global_recurrence_certified'])
        # Two sequences share first four samples but diverge at index 4.
        a=seq+(F(2),)
        b=seq+(F(9),)
        self.assertEqual(linear_recurrence_prefix(a,2)['all_supplied_samples_match'],True)
        self.assertEqual(linear_recurrence_prefix(b,2)['all_supplied_samples_match'],False)

    def test_exhaustive_three_by_three_rational_minor(self):
        for values in product((-1,0,1),repeat=5):
            m=hankel(values,3,3)
            proof=hankel_dimension_receipt(values,3,3)
            self.assertEqual(proof['linear_state_lower_bound'],rank(m))
            self.assertTrue(verify_dimension_receipt(values,proof))
        self.assertEqual(determinant(((F(1),F(2)),(F(3),F(4)))),F(-2))

    def test_random_rank_oracle_against_all_minors(self):
        rng=random.Random(20261012)
        for _ in range(120):
            rows=rng.randint(1,4);cols=rng.randint(1,4)
            seq=tuple(F(rng.randint(-4,4)) for i in range(rows+cols-1))
            proof=hankel_dimension_receipt(seq,rows,cols)
            self.assertTrue(verify_dimension_receipt(seq,proof))
            self.assertEqual(proof['linear_state_lower_bound'],rank(hankel(seq,rows,cols)))

    def test_forged_hankel_minor_and_source_rejected(self):
        seq=(F(2),F(0),F(2),F(0),F(2))
        rec=hankel_dimension_receipt(seq,3,3)
        changed={**rec,'minor_determinant':rec['minor_determinant']+1}
        self.assertFalse(verify_dimension_receipt(seq,changed))
        with self.assertRaises(RealizationError):
            hankel((1,2),2,2)
        with self.assertRaises(RealizationError):
            hankel((0.5,1,2),2,2)
        with self.assertRaises(RealizationError):
            linear_recurrence_prefix((0,0,0,0),2)
        with self.assertRaises(RealizationError):
            impulse_realization_check(33)

    def test_universal_lower_bound_is_model_relative(self):
        seq=(F(2),F(0),F(2))
        cert=hankel_dimension_receipt(seq,2,2)
        self.assertEqual(cert['linear_state_lower_bound'],2)
        self.assertFalse(cert['global_upper_bound_proved'])
        # A nonlinear or nonstationary 1-D system may realize the same
        # samples. The test NEVER claims an unconditional physical bound.

if __name__=="__main__":unittest.main()
