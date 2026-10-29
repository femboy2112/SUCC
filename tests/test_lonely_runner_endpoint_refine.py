from fractions import Fraction as F
import unittest

from observational_succ.lonely_runner_uniform import (
    AffineRunner, UniformRule, check_local_uniform, gap_counterexample, resonance_interval,
)
from scripts.lonely_runner_endpoint_refine import calibration


class EndpointRefinementControls(unittest.TestCase):
    def test_published_literal_rule_survives_candidate_menu(self):
        result = calibration()
        self.assertTrue(result["full_locality_pass"])
        self.assertTrue(result["literal_coefficients_in_menu"])
        self.assertEqual(result["gain"], 1)

    def test_covering_every_endpoint_can_miss_an_actual_responsible_time(self):
        rule = UniformRule((2,), (), (
            AffineRunner(1, F(0), F(3, 2)), AffineRunner(3, F(0), F(-5, 2)),
            AffineRunner(5, F(1, 2), F(7, 2)), AffineRunner(7, F(1, 2), F(-9, 2)),
        ))
        for k in (0, 1):
            intervals = [resonance_interval(2, k, v) for v in rule.added]
            for z in (-1, 1):
                self.assertTrue(any(interval is not None and interval[0] <= z <= interval[1]
                                    for interval in intervals))
        result = check_local_uniform(rule)
        self.assertFalse(result["local_uniform"])
        self.assertEqual(result["gap"], {"q": 2, "k": 0, "z": "0"})
        actual = gap_counterexample(rule, 2, 0, F(0))
        self.assertEqual(actual["time"], "0")
        self.assertTrue(all(F(x) > F(actual["delta"]) for x in actual["rescuer_distances"].values()))
        self.assertEqual(rule.gain, -3)  # no positive-gain countermodel is inferred


if __name__ == "__main__":
    unittest.main()
