from fractions import Fraction as F
import unittest

from observational_succ.lonely_runner_uniform import check_local_uniform, circle_distance
from scripts.lonely_runner_phase_schedule_probe import (
    divergent_residual_control, oscillatory_rule, receipt,
)


class ArbitraryPhaseControls(unittest.TestCase):
    def test_both_oscillating_components_are_universally_local(self):
        for d in (1, 3, 15, 45):
            even = oscillatory_rule(d, 2*d)
            odd = oscillatory_rule(d, 2*d+1)
            self.assertTrue(check_local_uniform(even)["local_uniform"])
            self.assertTrue(check_local_uniform(odd)["local_uniform"])
            self.assertEqual(even.affected, odd.affected)
            self.assertEqual(even.gain, odd.gain)
            self.assertEqual(even.added[0].alpha, F(3, 4))
            self.assertEqual(odd.added[0].alpha, F(1, 4))

    def test_two_phase_limits_remain_separated(self):
        for n in (2, 20, 2000):
            even, odd = oscillatory_rule(1, n), oscillatory_rule(1, n+1)
            theta_even = even.added[0].alpha + even.added[0].beta/F(n+1)
            theta_odd = odd.added[0].alpha + odd.added[0].beta/F(n+2)
            self.assertGreater(circle_distance(theta_even-theta_odd), F(2, 5))

    def test_divergent_normalized_lift_is_not_wraparound_rescue(self):
        for m in (3, 4, 7, 20, 1000, 10**20):
            control = divergent_residual_control(m)
            self.assertEqual(F(control["scaled_residual"]), m)
            self.assertEqual(F(control["epsilon"]), F(1, m))
            self.assertTrue(all(F(x) > F(control["delta"])
                                for x in control["distances"]))

    def test_source_receipt_and_invalid_domains(self):
        report = receipt()
        self.assertEqual(len(report["oscillatory_schedules"]), 12)
        self.assertFalse(report["input_schedule_identity_preserved"])
        for d, n in ((2, 8), (1, 1), (True, 2), (3, 5)):
            with self.assertRaises(ValueError):
                oscillatory_rule(d, n)


if __name__ == "__main__":
    unittest.main()
