"""Exact hostile source authentication and sharpness tests; no pi-digit input."""
import unittest
from fractions import Fraction as Q
from math import gcd, isqrt

from observational_succ.bbp_cyclotomic_birth import p_primary_phase
from observational_succ.bbp_prime_window_signed_intervals import box_phase
from observational_succ.bbp_resonance_controls import (
    authentic_history_failures, exact_forced_history,
    homogeneous_denominator_lower, nearest_grid_point,
    one_impulse_control, pointwise_pfree_antiphase, same_forcing_odd_control,
    inverse_source_window_arcs, inverse_arc_membership,
)


def direct_four_poles(n):
    """Independent parameterization from the natural-index source passport."""
    return Q(4, 8*n-7) - Q(2, 8*n-4) - Q(1, 8*n-3) - Q(1, 8*n-2)


class SourceAuthenticationControls(unittest.TestCase):
    def test_original_history_passes_and_signed_coefficient_mutation_fails(self):
        original = exact_forced_history(25)
        self.assertEqual(authentic_history_failures(original), ())
        altered = [Q()]
        for n in range(1, 26):
            self.assertEqual(original[n] - 16*original[n-1], direct_four_poles(n))
            altered.append(16*altered[-1] + direct_four_poles(n) - Q(1, 8*n-4))
        self.assertEqual(authentic_history_failures(tuple(altered)),
                         tuple("forcing-step-%d" % n for n in range(1, 26)))

    def test_nearest_grid_bound_including_negative_ties(self):
        for numerator in range(-33, 34):
            for denominator in (1, 3, 7, 17):
                x = Q(numerator, 11)
                rounded = nearest_grid_point(x, denominator)
                self.assertLessEqual(abs(rounded-x), Q(1, 2*denominator))
                self.assertEqual((rounded*denominator).denominator, 1)
        self.assertEqual(nearest_grid_point(Q(-1, 2), 1), 0)

    def test_polynomial_denominator_pointwise_antiphase(self):
        for p in (17, 41, 73, 97):
            data = pointwise_pfree_antiphase(p, 2*p+1, h=2)
            self.assertGreater(data["real_mean_lower"], Q(9, 10))
            for phase, complement in zip(data["primary"], data["complement"]):
                self.assertEqual(gcd(complement.denominator, p), 1)
                self.assertEqual(complement.denominator % 2, 1)
                self.assertLessEqual(abs(phase+complement), Q(1, 2*(2*p+1)))
            self.assertTrue(any(data["homogeneous_recurrence_defects"]))
            self.assertEqual(data["complement"][:data["L"]],
                             data["complement"][data["L"]:2*data["L"]])
            self.assertFalse(data["authentic_source"])

    def test_same_forcing_odd_control_all_exact_passport_conditions(self):
        for p in (17, 41, 73, 97, 193):
            data = same_forcing_odd_control(p)
            m = (p-1)//8
            self.assertEqual(data["denominator"] % (2*p), 1)
            self.assertEqual(data["authentic_failures"], ("initial-state",))
            self.assertNotEqual(data["initial"], 0)
            for n in range(1, 4*m+1):
                history = data["history"]
                self.assertEqual(history[n]-16*history[n-1], direct_four_poles(n))
                self.assertEqual(history[n].denominator % 2, 1)
            for t, state in enumerate(data["states"]):
                self.assertLess(abs(state), Q(1, 32*m*m))
                self.assertEqual(p_primary_phase(state, p), 4*pow(16, t, p) % p)
            self.assertGreater(data["real_mean_lower"], 1-data["modulus_deficit_upper"])
            self.assertEqual(data["modulus_deficit_upper"], Q(121, 6272*m**4))

    def test_independent_terminal_backward_sum_identity(self):
        for p in (17, 41, 73):
            data = same_forcing_odd_control(p)
            N = data["horizon"]
            terminal_alpha = sum((direct_four_poles(k)/16**k for k in range(1, N+1)), Q())
            self.assertEqual(terminal_alpha, data["terminal_alpha"])
            epsilon = data["initial"] + terminal_alpha
            for t, state in enumerate(data["states"]):
                n = data["m"]+1+t
                future = sum((direct_four_poles(k)/16**(k-n)
                              for k in range(n+1, N+1)), Q())
                self.assertEqual(state, -future+16**n*epsilon)

    def test_squared_modulus_bound_calibrated_by_certified_phase_boxes(self):
        data = same_forcing_odd_control(17, h=1)
        boxes = [box_phase(state, terms=12, arctan_terms=20) for state in data["states"]]
        mean_real_lower = sum((box[0] for box in boxes), Q())/data["delta"]
        self.assertGreater(mean_real_lower, data["real_mean_lower"])
        self.assertGreater(mean_real_lower, 1-data["modulus_deficit_upper"])
        negative = same_forcing_odd_control(17, h=-3)
        self.assertEqual(negative["modulus_deficit_upper"], 9*data["modulus_deficit_upper"])
        self.assertEqual(same_forcing_odd_control(17, h=0)["real_mean_lower"], 1)

    def test_one_impulse_preserves_prefix_tail_and_exact_p_clock(self):
        for p, K in ((17, 0), (41, 2), (73, 7)):
            data = one_impulse_control(p, K)
            original = exact_forced_history(4*((p-1)//8))
            self.assertEqual(data["history"][:K+1], original[:K+1])
            self.assertEqual(data["authentic_failures"], ("forcing-step-%d" % (K+1),))
            self.assertEqual(gcd(data["impulse"].denominator, 2*p), 1)
            for n in range(K+2, len(original)):
                self.assertEqual(data["history"][n]-16*data["history"][n-1], direct_four_poles(n))
        with self.assertRaises(ValueError):
            one_impulse_control(17, 2)

    def test_homogeneous_denominator_cost_is_attained_on_a_small_rational(self):
        p, count = 17, 5
        q = 2*p*16**count+1
        x = Q(1, p*q)
        radius = 16**(count-1)*x
        self.assertLess(radius, Q(1, 17))
        self.assertEqual(homogeneous_denominator_lower(p, count, radius), q)
        self.assertTrue(all(16**t*x <= radius for t in range(count)))
        self.assertNotEqual(p_primary_phase(x, p), 0)

    def test_domain_and_source_confusion_rejected(self):
        for p in (3, 5, 9, 21, 25, 2, True, 17.0):
            with self.assertRaises(ValueError):
                same_forcing_odd_control(p)
        for q in (2, 17, 34, 0, True):
            with self.assertRaises(ValueError):
                pointwise_pfree_antiphase(17, q)
        for radius in (Q(), Q(1, 17), Q(1, 16), 0.01):
            with self.assertRaises(ValueError):
                homogeneous_denominator_lower(17, 5, radius)
        with self.assertRaises(ValueError):
            authentic_history_failures(())
        with self.assertRaises(ValueError):
            exact_forced_history(4, 0.0)

    def test_inverse_arcs_capture_provably_near_coherent_controls(self):
        for p in (41, 73, 97, 193):
            data = same_forcing_odd_control(p)
            a = Q(1, 8*data["m"]*isqrt(data["m"]))
            arcs = inverse_source_window_arcs(p, a)
            self.assertLess(data["modulus_deficit_upper"], arcs["deficit_threshold"])
            self.assertTrue(inverse_arc_membership(p, data["states"][0], a)["inside"])
            original_start = exact_forced_history(data["m"]+1)[-1]
            self.assertFalse(inverse_arc_membership(p, original_start, a)["inside"])
            self.assertFalse(arcs["coherence_hypothesis_established"])
            self.assertEqual(arcs["arc_count"], 15)

    def test_inverse_arcs_respect_all_fixed_point_and_frequency_lifts(self):
        p = 97
        for h in (-2, 3):
            data = same_forcing_odd_control(p, h)
            a = Q(abs(h), 8*data["m"]*isqrt(data["m"]))
            arcs = inverse_source_window_arcs(p, a, h)
            self.assertLess(data["modulus_deficit_upper"], arcs["deficit_threshold"])
            indices = set()
            for j in range(15*abs(h)):
                shifted_start = data["states"][0]+Q(j, 15*abs(h))
                membership = inverse_arc_membership(p, shifted_start, a, h)
                self.assertTrue(membership["inside"])
                indices.add(membership["cell_index"])
            self.assertEqual(len(indices), 15*abs(h))
            midpoint = -arcs["finite_source_sum"]+Q(1, 2*arcs["arc_count"])
            self.assertFalse(inverse_arc_membership(p, midpoint, a, h)["inside"])

    def test_inverse_arc_unwrapping_hypothesis_is_not_optional(self):
        for a in (Q(), Q(1, 34), Q(1, 10), 0.01):
            with self.assertRaises(ValueError):
                inverse_source_window_arcs(17, a)
        with self.assertRaises(ValueError):
            inverse_source_window_arcs(17, Q(1, 1000), h=0)
        with self.assertRaises(ValueError):
            inverse_source_window_arcs(17, Q(1, 1000), h=1000)


if __name__ == "__main__":
    unittest.main()
