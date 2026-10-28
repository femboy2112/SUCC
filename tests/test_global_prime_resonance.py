"""Independent pole, cyclotomic, interval, and source-passport controls."""
from dataclasses import replace
from fractions import Fraction as Q
import unittest

from observational_succ.global_prime_resonance import (
    authentic_prime_source_passport, prime_resonance_budget,
    verify_prime_source_passport,
)
from observational_succ.finite_fourier_carrier import CyclotomicElement
from observational_succ.pi_source_genesis import character_interval, signed_sum_interval


def literal_force(n):
    return Q(4, 8*n-7)-Q(2, 8*n-4)-Q(1, 8*n-3)-Q(1, 8*n-2)


def squared_lower(box):
    def part(a, b):
        return Q() if a <= 0 <= b else min(a*a, b*b)
    return part(box.real_low, box.real_high)+part(box.imag_low, box.imag_high)


def independent_galois_polynomial(p, exponents):
    coefficients = [Q()]*p
    for a in range(1, p):
        for x in exponents:
            for y in exponents:
                coefficients[a*(x-y) % p] += 1
    return tuple(coefficients)


class GlobalPrimeResonanceTests(unittest.TestCase):
    def test_prescribed_window_integer_boundaries_and_nonaliasing(self):
        for p, K in ((257, 1), (40961, 1), (65537, 2),
                     (16777289, 3), (4294967377, 4)):
            result = prime_resonance_budget(p)
            self.assertEqual(result.window_length, K)
            self.assertLessEqual(256**K, p)
            self.assertGreater(256**(K+1), p)
            self.assertLessEqual(K, result.next_pole_gap)
            self.assertEqual(len({4*pow(16, t, p) % p for t in range(K)}), K)

    def test_unwrapped_source_replayed_from_all_four_literal_poles(self):
        for p in (257, 337, 577, 1153):
            passport = authentic_prime_source_passport(p)
            U = Q()
            exact = {}
            for n in range(1, passport.points[-1].source_index+1):
                U = 16*U+literal_force(n)
                exact[n] = U
            for point in passport.points:
                self.assertEqual(point.original_lift, exact[point.source_index])
                self.assertEqual(point.original_forcing, literal_force(point.source_index))
                self.assertEqual(point.original_lift, point.primary_phase+point.full_complement)
                self.assertNotEqual(point.full_complement.denominator % p, 0)
                self.assertEqual(point.common_conductor % point.original_lift.denominator, 0)
            self.assertTrue(verify_prime_source_passport(passport))

    def test_first_pole_and_next_pole_are_checked_independently(self):
        for p in (257, 337, 577):
            result = prime_resonance_budget(p)
            first, next_time = result.birth_index, result.birth_index+result.next_pole_gap
            hits = []
            for n in range(1, next_time+1):
                denominators = (8*n-7, 8*n-4, 8*n-3, 8*n-2)
                if any(d % p == 0 for d in denominators):
                    hits.append(n)
            self.assertEqual(hits, [first, next_time])
            self.assertEqual((literal_force(first)-Q(4, p)).denominator % p != 0, True)

    def test_primitive_galois_mean_in_native_cyclotomic_quotient(self):
        # Smaller independent carriers validate the general finite identity.
        for p, K in ((17, 2), (41, 3), (73, 2)):
            phases = tuple(4*pow(16, t, p) % p for t in range(K))
            self.assertEqual(len(set(phases)), K)
            formal = independent_galois_polynomial(p, phases)
            evaluated = CyclotomicElement(p, formal).scale(Q(1, p-1))
            self.assertEqual(evaluated, CyclotomicElement.scalar(p, Q(K*(p-K), p-1)))
            # Formal nonconstant coefficients remain; reduction is essential.
            self.assertTrue(any(formal[1:]))

    def test_actual_two_step_window_galois_polynomial(self):
        p = 65537
        result = prime_resonance_budget(p)
        coefficients = independent_galois_polynomial(p, (4, 64))
        self.assertEqual(coefficients[0], 2*(p-1))
        self.assertEqual(set(coefficients[1:]), {Q(2)})
        # Phi_p=1+X+...+X^(p-1): exact quotient is constant subtraction.
        quotient_constant = coefficients[0]-coefficients[1]
        self.assertEqual(quotient_constant/Q(p-1), result.galois_mean_sum_squared)

    def test_selected_sum_and_matrix_lower_bounds_by_outward_intervals(self):
        for p in (257, 65537, 16777289, 4294967377):
            for h in (1, -1, 3):
                result = prime_resonance_budget(p, h)
                box = signed_sum_interval(tuple((h*x, h*x) for x in result.primary_phases))
                self.assertGreaterEqual(squared_lower(box), result.selected_sum_modulus_lower**2)
                self.assertLess(result.selected_sum_deficit_upper, Q(2*h*h, p))
            result = prime_resonance_budget(p)
            selected_lower = Q()
            for h in range(1, result.width):
                box = signed_sum_interval(tuple((h*x, h*x) for x in result.primary_phases))
                selected_lower += 2*(1-Q(h, result.width))*squared_lower(box)/result.window_length**2
            self.assertGreaterEqual(selected_lower, result.selected_normalized_excess_lower)

    def test_exact_finite_matrix_separation_and_amplification(self):
        result = prime_resonance_budget(4294967377)
        self.assertEqual((result.window_length, result.width), (4, 3))
        self.assertLess(result.galois_mean_normalized_excess, Q(1, 2))
        self.assertGreater(result.selected_normalized_excess_lower, Q(199, 100))
        self.assertGreater(result.selected_amplification_lower, Q(399, 100))
        self.assertFalse(result.full_source_cancellation_proved)

    def test_full_complement_comparison_on_actual_source(self):
        for p in (257, 577):
            passport = authentic_prime_source_passport(p)
            for h in (1, -3):
                result = prime_resonance_budget(p, h)
                full = signed_sum_interval(tuple((h*x.original_lift, h*x.original_lift)
                                                  for x in passport.points))
                complement = signed_sum_interval(tuple((h*x.full_complement, h*x.full_complement)
                                                        for x in passport.points))
                self.assertLessEqual((full-complement).modulus_squared_upper(),
                                     result.full_complement_sum_error_upper**2)

    def test_aliased_period_and_resonant_frequency_refute_wrong_mean(self):
        p, K = 17, 3
        repeated = tuple(4*pow(16, t, p) % p for t in range(K))
        actual = CyclotomicElement(p, independent_galois_polynomial(p, repeated)).scale(Q(1,p-1))
        self.assertNotEqual(actual, CyclotomicElement.scalar(p, Q(K*(p-K), p-1)))
        resonant = CyclotomicElement(p, independent_galois_polynomial(p, (0, 0))).scale(Q(1,p-1))
        self.assertEqual(resonant, CyclotomicElement.scalar(p, 4))
        with self.assertRaises(ValueError):
            prime_resonance_budget(257, 257)

    def test_source_mutations_preserve_no_authentication(self):
        passport = authentic_prime_source_passport(257)
        point = passport.points[0]
        for mutant in (replace(passport, initial_state=Q(1, 3)),
                       replace(passport, source_id="unlabelled"),
                       replace(passport, points=(replace(point, original_lift=point.original_lift+1),)),
                       replace(passport, points=(replace(point, original_forcing=point.original_forcing+Q(1,257)),)),
                       replace(passport, points=(replace(point, primary_phase=Q(5,257)),))):
            self.assertFalse(verify_prime_source_passport(mutant))

    def test_domain_and_explicit_source_replay_budget(self):
        for call in (lambda: prime_resonance_budget(289),
                     lambda: prime_resonance_budget(263),
                     lambda: prime_resonance_budget(True),
                     lambda: prime_resonance_budget(257, 0),
                     lambda: prime_resonance_budget(257, 1, 258),
                     lambda: authentic_prime_source_passport(65537)):
            with self.assertRaises(ValueError):
                call()
        trivial = prime_resonance_budget(257, width=1)
        self.assertEqual(trivial.galois_mean_normalized_excess, 0)
        self.assertEqual(trivial.selected_normalized_excess_lower, 0)


if __name__ == "__main__":
    unittest.main()
