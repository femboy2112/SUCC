import unittest
from fractions import Fraction as Q

from observational_succ.spectral_purity_certificates import (
    authentic_prefix, authentic_innovation_interval, innovation_interval,
    selected_trace_counterexample,
)


class SelectedInnovationCertificates(unittest.TestCase):
    def test_exact_cyclotomic_controls(self):
        # These exact values use independent root-of-unity evaluations.
        for phase, width, exact in ((Q(0), 3, Q(9)), (Q(1, 3), 3, Q(0)),
                                    (Q(1, 2), 3, Q(1)), (Q(1, 4), 2, Q(2))):
            low, high = innovation_interval((Q(0),), phase, width)
            self.assertLessEqual(low, exact)
            self.assertGreaterEqual(high, exact)
            self.assertLess(high-low, Q(1, 10**12))

    def test_actual_new_prime_power_does_not_bound_selected_embedding(self):
        result = selected_trace_counterexample()
        self.assertGreater(result["selected_q_interval"][0], 5)
        self.assertEqual(result["relative_galois_mean_q"], 3)

    def test_independent_holdout_arrival(self):
        # Chosen after the n=2 counterexample; same phenomenon at a new prime.
        low, high = authentic_innovation_interval(14, 4)
        self.assertGreater(low, Q(4*109, 108))
        self.assertLess(high-low, Q(1, 10**12))
        path = authentic_prefix(14)
        self.assertTrue(all(x.denominator % 109 for x in path[:-1]))
        self.assertEqual(path[-1].denominator % 109, 0)

    def test_signed_innovation_defects(self):
        # Identical and antipodal arrivals have opposite defects at H=2.
        self.assertGreater(innovation_interval((Q(),), Q(), 2)[0], 2)
        self.assertLess(innovation_interval((Q(),), Q(1, 2), 2)[1], 2)

    def test_mutated_source_cannot_reuse_authentic_certificate(self):
        path = authentic_prefix(2)
        mutated = 16*path[0] + (path[1]-16*path[0]) + Q(1, 2)
        low, high = innovation_interval(path[:1], mutated, 3)
        self.assertLess(high, 3)
        self.assertNotEqual((low, high), authentic_innovation_interval(2, 3))

    def test_invalid_inputs(self):
        for args in (((), Q(), 2), ((Q(),), 0.5, 2), ((Q(),), Q(), True)):
            with self.assertRaises(ValueError):
                innovation_interval(*args)


if __name__ == "__main__":
    unittest.main()
