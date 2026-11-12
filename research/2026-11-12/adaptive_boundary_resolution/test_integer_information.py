"""Bounded adversarial tests; polynomial proofs live in INTEGER_INFORMATION.md."""
from fractions import Fraction as F
from itertools import combinations_with_replacement
from math import prod
import unittest

from integer_information import (
    IntegerTwins, ambiguity_mass_bounds, annihilator, channel_bounds,
    last_channel_noise_witness, noise_packet, prior_even_channels,
    responses, twins, unit_noise_witness, verify_twins,
    zero_count_from_adaptive_sample,
)


def direct(histogram, base, r):
    # Separate direct evaluation, including r=0 for the mass constraint.
    return sum((F(count, base ** (r * h))
                for h, count in enumerate(histogram)), F())


class IntegerInformationTests(unittest.TestCase):
    def test_frozen_one_channel_witness_attains_lower_bound(self):
        for base in (2, 3, 7):
            witness = twins(base, 1)
            self.assertEqual(witness.left, (1, 0, base))
            self.assertEqual(witness.right, (0, base + 1, 0))
            self.assertEqual(ambiguity_mass_bounds(base, 1), (base + 1, base + 1))
            self.assertTrue(verify_twins(witness))

    def test_frozen_two_channel_witness_and_nonminimality_control(self):
        basic = twins(2, 2)
        self.assertEqual(annihilator(2, 2), (1, -7, 14, -8))
        self.assertEqual(basic.mass, 15)
        self.assertEqual(responses(basic.left, 2, 2), (F(9, 2), F(15, 8)))
        improved = twins(2, 2, multiplier=(1, 1))
        self.assertEqual(improved.left, (1, 0, 7, 6, 0))
        self.assertEqual(improved.right, (0, 6, 0, 0, 8))
        self.assertEqual(improved.mass, 14)
        self.assertEqual(responses(improved.left, 2, 2), (F(7, 2), F(49, 32)))
        self.assertTrue(verify_twins(improved))

    def test_all_eighteen_product_witnesses_by_direct_sums(self):
        for base in (2, 3, 5):
            for d in range(1, 7):
                witness = twins(base, d)
                self.assertEqual(witness.zero_gap, 1)
                self.assertEqual(witness.mass, prod(base ** r + 1 for r in range(1, d + 1)))
                for r in range(d + 1):
                    self.assertEqual(direct(witness.left, base, r),
                                     direct(witness.right, base, r))
                self.assertNotEqual(direct(witness.left, base, d + 1),
                                    direct(witness.right, base, d + 1))

    def test_common_padding_preserves_packet_and_zero_gap(self):
        witness = twins(3, 3, total_mass=10000)
        self.assertEqual(sum(witness.left), 10000)
        self.assertEqual(sum(witness.right), 10000)
        self.assertEqual(witness.zero_gap, 1)
        self.assertTrue(verify_twins(witness))

    def test_equal_mass_factor_cannot_be_omitted(self):
        # (1-2z)(1-4z)=1-6z+8z^2 kills both damped samples,
        # but its positive and negative parts have masses 9 and 6.
        left, right = (1, 0, 8), (0, 6, 0)
        self.assertEqual(responses(left, 2, 2), responses(right, 2, 2))
        self.assertNotEqual(sum(left), sum(right))
        self.assertFalse(verify_twins(IntegerTwins(2, 2, left, right)))

    def test_missing_last_channel_is_a_real_discriminator(self):
        for base, d in ((2, 1), (2, 4), (3, 3)):
            packet = last_channel_noise_witness(base, d)
            a, b = packet["left_responses"], packet["right_responses"]
            self.assertEqual(a[:-1], b[:-1])
            kappa = prod((1 - F(1, base ** j) for j in range(1, d + 1)), start=F(1))
            self.assertEqual(abs(a[-1] - b[-1]), kappa / packet["mass"])
            self.assertEqual(packet["radius"], kappa / (2 * packet["mass"]))

    def test_normalized_noise_common_packet_is_authentic(self):
        packet = unit_noise_witness(2, 6, 1000)
        self.assertEqual(packet["radius"], F(63, 128000))
        for values in (packet["left_responses"], packet["right_responses"]):
            for truth, center in zip(values, packet["midpoint"]):
                self.assertLessEqual(abs(truth - center), packet["radius"])
        self.assertEqual(packet["left"][0] - packet["right"][0], 1)

    def test_rational_rescaling_destroys_any_positive_mass_threshold(self):
        witness = twins(2, 3)
        scale = F(1, 1000 * witness.mass)
        left = tuple(scale * x for x in witness.left)
        right = tuple(scale * x for x in witness.right)
        self.assertEqual(sum(left), F(1, 1000))
        self.assertNotEqual(left[0], right[0])
        for r in range(4):
            self.assertEqual(sum(x * F(1, 2 ** r) ** h for h, x in enumerate(left)),
                             sum(x * F(1, 2 ** r) ** h for h, x in enumerate(right)))
        with self.assertRaises(ValueError):
            responses(left, 2, 3)

    def test_channel_bounds_and_prior_rule_gap(self):
        self.assertEqual(channel_bounds(2, 0), (0, 0))
        self.assertEqual(channel_bounds(2, 1), (1, 1))
        self.assertEqual(channel_bounds(2, 3), (2, 2))
        self.assertEqual(channel_bounds(2, 9), (2, 3))
        self.assertEqual(channel_bounds(2, 1000), (4, 4))
        for base in (2, 3, 11):
            for mass in (1, 2, 3, 8, 15, 1000, 10 ** 6, 10 ** 12):
                lo, hi = channel_bounds(base, mass)
                self.assertIn(hi - lo, (0, 1))
                self.assertLessEqual(prior_even_channels(base, mass) - lo, 2)

    def test_independent_small_histogram_enumeration_has_no_collision(self):
        # This finite calibration does not replace the arbitrary-support proof.
        for mass in (1, 2):
            seen = {}
            for grades in combinations_with_replacement(range(8), mass):
                value = sum((F(1, 2 ** h) for h in grades), F())
                self.assertNotIn(value, seen)
                seen[value] = grades

    def test_mass_dependent_node_escapes_fixed_base_channel_bound(self):
        # These are indistinguishable with two fixed base-two channels.
        # Moving the sole node to 1/(M+1) separates their zero counts.
        witness = twins(2, 2, multiplier=(1, 1))
        self.assertTrue(verify_twins(witness))
        for histogram in (witness.left, witness.right, (2, 0, 0, 1000)):
            mass = sum(histogram)
            value = direct(histogram, mass + 1, 1)
            self.assertEqual(zero_count_from_adaptive_sample(mass, value), histogram[0])
        self.assertEqual(zero_count_from_adaptive_sample(0, 0), 0)

    def test_zero_channel_exception_and_mutated_witness(self):
        witness = twins(2, 0)
        self.assertEqual(ambiguity_mass_bounds(2, 0), (1, 1))
        self.assertTrue(verify_twins(witness))
        good = twins(2, 2)
        moved = list(good.right)
        moved[1] -= 1
        moved[2] += 1
        self.assertFalse(verify_twins(IntegerTwins(2, 2, good.left, tuple(moved))))

    def test_integer_model_rejects_invalid_domains(self):
        for args in ((True, 2), (1, 2), (2, True), (2, -1)):
            with self.assertRaises(ValueError):
                annihilator(*args)
        for values in ((1, F(1, 2)), (1, True), (1, -1), ()):
            with self.assertRaises(ValueError):
                responses(values, 2, 2)
        for multiplier in ((), (0, 1), (True, 1), (F(1, 2), 1)):
            with self.assertRaises(ValueError):
                twins(2, 2, multiplier=multiplier)
        with self.assertRaises(ValueError):
            twins(2, 2, total_mass=14)
        with self.assertRaises(ValueError):
            noise_packet((1,), (0,), 2, 2)


if __name__ == "__main__":
    unittest.main()
