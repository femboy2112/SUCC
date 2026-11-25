import unittest
from dataclasses import replace
from fractions import Fraction
from observational_succ.principia_cm_theta import construct_cm_theta_certificate
from observational_succ.principia_balance_frame import (
    cm_balance_frame, verify_balance_frame, source_error_bound,exact_inverse,
)
from observational_succ.principia_reorientation import ReorientationError

class QuantitativeBalanceTests(unittest.TestCase):
    def test_same_cm_source_integral_and_real_inverse(self):
        for p in (3,7):
            for n in (1,2,3):
                c=construct_cm_theta_certificate(p,n,Fraction(1,2))
                exact=cm_balance_frame(c,analytic=False)
                gaussian=cm_balance_frame(c,analytic=True)
                self.assertEqual(verify_balance_frame(exact),exact)
                self.assertEqual(verify_balance_frame(gaussian),gaussian)
                self.assertEqual(gaussian.source,c)
                self.assertTrue(gaussian.analytic)
                self.assertGreaterEqual(gaussian.inverse_infinity_norm,exact.inverse_infinity_norm)
    def test_weighted_inverse_is_expensive(self):
        c=construct_cm_theta_certificate(3,2,Fraction(1,2))
        real=cm_balance_frame(c,analytic=True)
        bare=cm_balance_frame(c,analytic=False)
        self.assertGreater(real.inverse_infinity_norm,100*bare.inverse_infinity_norm)
        self.assertGreater(source_error_bound(real,Fraction(1,1000)),
                           source_error_bound(bare,Fraction(1,1000)))
    def test_singular_duplicated_observations(self):
        with self.assertRaises(ReorientationError):exact_inverse(((1,1),(1,1)))
        with self.assertRaises(ReorientationError):exact_inverse(((1,1,1),(0,1,0)))
    def test_mutation_of_inverse_and_norm_rejected(self):
        c=construct_cm_theta_certificate(3,2)
        frame=cm_balance_frame(c,analytic=True)
        with self.assertRaises(ReorientationError):verify_balance_frame(replace(frame,inverse=frame.observation))
        with self.assertRaises(ReorientationError):verify_balance_frame(replace(frame,inverse_infinity_norm=Fraction(1)))
        with self.assertRaises(ReorientationError):verify_balance_frame(replace(frame,observation=frame.inverse))
        with self.assertRaises(ReorientationError):verify_balance_frame(replace(frame,source=replace(c,passport='fake')))
    def test_inverse_error_bound_is_actually_sharp_for_an_adversarial_noise(self):
        c=construct_cm_theta_certificate(3,2)
        frame=cm_balance_frame(c,analytic=True)
        i=max(range(len(frame.inverse)), key=lambda k:sum(abs(a) for a in frame.inverse[k]))
        noise=tuple(Fraction(1 if v>0 else -1 if v<0 else 0)
                    for v in frame.inverse[i])
        outcome=tuple(sum((row[j]*noise[j] for j in range(len(noise))),Fraction(0))
                      for row in frame.inverse)
        self.assertEqual(max(abs(x) for x in outcome),frame.inverse_infinity_norm)

    def test_measurement_noise_is_a_bound_not_a_truth_score(self):
        c=construct_cm_theta_certificate(3,2)
        frame=cm_balance_frame(c,analytic=True)
        self.assertEqual(source_error_bound(frame,Fraction(0)),0)
        self.assertEqual(source_error_bound(frame,Fraction(1,3)),frame.inverse_infinity_norm/3)
        with self.assertRaises(ReorientationError):source_error_bound(frame,Fraction(-1))

if __name__=='__main__':unittest.main()
