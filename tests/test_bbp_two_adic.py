"""Independent rational controls for the source-specific 2-adic identities."""

from fractions import Fraction as Q
from collections import Counter
import unittest

from observational_succ import bbp_two_adic as two
from observational_succ.bbp_source_memory import forcing


def four_poles(index):
    """Independent unreduced formula, valid at every integral index."""
    return (Q(4, 8 * index - 7) - Q(2, 8 * index - 4)
            - Q(1, 8 * index - 3) - Q(1, 8 * index - 2))


def v2(integer):
    if integer == 0:
        return None
    return (abs(integer) & -abs(integer)).bit_length() - 1


class BBPTwoAdicTests(unittest.TestCase):
    def test_collapsed_residues_match_independent_four_poles(self):
        for index in range(-40, 81):
            value = four_poles(index)
            self.assertEqual(value.denominator % 2, 1)
            if index > 0:
                self.assertEqual(value, forcing(index))
            for bits in (1, 2, 4, 7, 16, 31):
                self.assertEqual(two.forcing_mod(index, bits),
                                 two.rational_mod(value, bits))

    def test_forcing_and_particular_are_finite_permutations(self):
        for bits in range(1, 10):
            modulus = 1 << bits
            for evaluator in (two.forcing_mod, two.particular_mod):
                values = [evaluator(n, bits) for n in range(modulus)]
                self.assertEqual(sorted(values), list(range(modulus)))
                self.assertEqual([evaluator(n + modulus, bits)
                                  for n in range(17)],
                                 [values[n % modulus] for n in range(17)])

    def test_isometry_and_compatible_reduction(self):
        for bits in (4, 8, 13):
            modulus = 1 << bits
            for evaluator in (two.forcing_mod, two.particular_mod):
                for left in (-91, -2, 0, 1, 10, 41, 257):
                    for right in (-36, 2, 7, 16, 97, 777):
                        difference = (left - right) % modulus
                        image_difference = (evaluator(left, bits)
                                            - evaluator(right, bits)) % modulus
                        self.assertEqual(v2(difference), v2(image_difference))
                    self.assertEqual(evaluator(left, bits + 7) % modulus,
                                     evaluator(left, bits))

    def test_particular_zero_and_recurrence_at_signed_indices(self):
        # The finite checks corroborate the separate analytic zero theorem.
        for bits in (1, 4, 8, 17, 32, 65, 129, 256):
            self.assertEqual(two.particular_mod(0, bits), 0)
            modulus = 1 << bits
            for n in (-19, -1, 0, 1, 4, 17, 10001):
                expected = (16 * two.particular_mod(n - 1, bits)
                            + two.forcing_mod(n, bits)) % modulus
                self.assertEqual(two.particular_mod(n, bits), expected)

    def test_particular_matches_zero_initial_unwrapped_source(self):
        unwrapped = Q()
        for n in range(1, 81):
            unwrapped = 16 * unwrapped + four_poles(n)
            self.assertEqual(v2(unwrapped.numerator), v2(n))
            for bits in (4, 13, 32, 100):
                self.assertEqual(two.particular_mod(n, bits),
                                 two.rational_mod(unwrapped, bits))

    def test_all_depth_truncation_denominator_and_preperiod(self):
        unwrapped = Q()
        for depth in range(1, 81):
            unwrapped = 16 * unwrapped + four_poles(depth)
            truncation = unwrapped / 16 ** (depth - 1)
            exponent = v2(truncation.denominator)
            self.assertEqual(two.truncation_dyadic_exponent(depth), exponent)
            preperiod = two.truncation_preperiod(depth)
            self.assertEqual((truncation * 16 ** preperiod).denominator % 2, 1)
            if preperiod:
                self.assertEqual((truncation * 16 ** (preperiod - 1))
                                 .denominator % 2, 0)
        self.assertEqual(two.truncation_preperiod(16), 14)
        self.assertEqual(two.truncation_preperiod(64), 62)
        # Reusing the formerly proved odd-depth rule at every depth fails.
        self.assertNotEqual(two.truncation_preperiod(16), 16 - 1)

    def test_bit_lift_inverse_and_larger_precision_holdouts(self):
        for bits in (1, 4, 7):
            for n in range(1 << bits):
                residue = two.particular_mod(n, bits)
                self.assertEqual(two.particular_inverse_mod(residue, bits), n)
        for bits, n in ((31, 123456789), (64, -(1 << 61) + 577),
                        (129, (1 << 120) + 1048601)):
            residue = two.particular_mod(n, bits)
            self.assertEqual(two.particular_inverse_mod(residue, bits),
                             n % (1 << bits))

    def test_odd_prime_transports_cohere_multiplicatively(self):
        for bits in (4, 7, 12):
            modulus = 1 << bits
            for q in (1, 3, 5, 7, 11, 13, -1, 17):
                for n in (-13, 0, 1, 4, 10, 53, 577):
                    moved = two.time_transport_mod(q, n, bits)
                    self.assertEqual(two.particular_mod(moved, bits),
                                     q * two.particular_mod(n, bits) % modulus)
                    self.assertEqual(two.time_transport_mod(q, n, bits + 3)
                                     % modulus, moved)
                    for r in (3, -5):
                        composed = two.time_transport_mod(
                            q, two.time_transport_mod(r, n, bits), bits)
                        self.assertEqual(composed,
                                         two.time_transport_mod(q * r, n, bits))

    def test_literal_carry_memory_retains_the_actual_state(self):
        state = Q()
        cumulative_carry = 0
        carries = []
        for n in range(1, 91):
            raw = 16 * state + four_poles(n)
            carry = raw.numerator // raw.denominator
            state = raw - carry
            carries.append(carry)
            cumulative_carry = 16 * cumulative_carry + carry
            for bits in (4, 17, 63):
                modulus = 1 << bits
                self.assertEqual(two.carry_memory_mod(carries, bits),
                                 cumulative_carry % modulus)
                self.assertEqual((two.particular_mod(n, bits)
                                  - two.rational_mod(state, bits)) % modulus,
                                 two.carry_memory_mod(carries, bits))
        # A literal carry of 16 must retain its effect at the next bit level.
        self.assertEqual(two.carry_memory_mod([16, 1], 12), 257)
        self.assertNotEqual(two.carry_memory_mod([16, 1], 12),
                            two.carry_memory_mod([0, 1], 12))

    def test_exact_dyadic_collisions_and_four_bit_loss(self):
        for length in (0, 1, 7, 16, 33, 97, 257):
            for bits in (0, 1, 3, 5, 8):
                expected = two.residue_collision_count(length, bits)
                for start in (-7, 0, 13, 1009):
                    values = (Counter(two.particular_mod(n, bits)
                                      for n in range(start, start + length))
                              if bits else {0: length})
                    actual = sum(count ** 2 for count in values.values())
                    self.assertEqual(actual, expected)
                for step in (1, 2, 4, 7):
                    radix = 1 << step
                    refined = two.residue_collision_count(length, bits + step)
                    self.assertLessEqual(radix * refined,
                                         expected + (radix - 1) * length)
        # Dropping the linear diagonal allowance creates a false theorem.
        self.assertGreater(two.residue_collision_count(1, 4),
                           Q(two.residue_collision_count(1, 0), 16))

    def test_two_adic_transport_does_not_transport_the_circle(self):
        unwrapped = [Q()]
        for n in range(1, 15):
            unwrapped.append(16 * unwrapped[-1] + four_poles(n))
        self.assertEqual(two.time_transport_mod(3, 10, 5), 14)
        defect = unwrapped[14] - 3 * unwrapped[10]
        self.assertEqual(two.rational_mod(defect, 5), 0)
        phase = defect % 1
        circle_distance = min(phase, 1 - phase)
        self.assertEqual(circle_distance,
                         Q(768205462011658030046123174167,
                           1551998839414697967442350160575))
        self.assertGreater(circle_distance, Q(49, 100))

    def test_every_fixed_finite_place_list_can_miss_a_half_turn(self):
        # All prime places below 16 are simultaneously small here.  The
        # growing denominator is the missing archimedean height information.
        for precision in (1, 3, 7):
            numerator = (2 * 3 * 5 * 7 * 11 * 13) ** precision
            value = Q(numerator, 2 * numerator + 1)
            for prime in (2, 3, 5, 7, 11, 13):
                self.assertEqual(value.numerator % prime ** precision, 0)
                self.assertNotEqual(value.denominator % prime, 0)
            self.assertGreater(value, Q(49, 100))
            self.assertLess(value, Q(1, 2))

    def test_universal_odd_source_clock_is_not_three_integral(self):
        # The dyadic chart cannot be silently reused at the next prime.
        self.assertEqual(four_poles(1), Q(47, 15))
        self.assertEqual(four_poles(1).denominator % 3, 0)

    def test_source_mutations_break_the_zero_and_isometry_claims(self):
        # Reversing the sign of the last BBP pole is an exact source change.
        def mutant(index):
            return (Q(4, 8 * index - 7) - Q(2, 8 * index - 4)
                    - Q(1, 8 * index - 3) + Q(1, 8 * index - 2))
        bits = 16
        bad_zero = sum((16 ** j * mutant(-j) for j in range(4)), Q())
        self.assertNotEqual(two.rational_mod(bad_zero, bits), 0)
        # A source doubled after evaluation is no longer an isometry.
        values = {2 * two.forcing_mod(n, 4) % 16 for n in range(16)}
        self.assertEqual(len(values), 8)

    def test_domain_guards(self):
        for bad in (0, -1, True, 2.5):
            with self.assertRaises(ValueError):
                two.particular_mod(0, bad)
        for bad in (True, 1.5, Q(1, 2)):
            with self.assertRaises(ValueError):
                two.forcing_mod(bad, 4)
        with self.assertRaises(ValueError):
            two.rational_mod(Q(1, 2), 8)
        with self.assertRaises(ValueError):
            two.time_transport_mod(2, 1, 8)
        with self.assertRaises(ValueError):
            two.truncation_dyadic_exponent(0)
        with self.assertRaises(ValueError):
            two.carry_memory_mod([1, 1.5], 8)


if __name__ == "__main__":
    unittest.main()
