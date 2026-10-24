"""Exact hostile controls; continuum theorems retain paper-proof authority."""
from fractions import Fraction as Q
from itertools import product
import unittest

from observational_succ.source_faithful_limits import (
    ClockLimitError, RationalBracket, action_horizon, compressed_laplacian_column,
    cycle_distance, cycle_heat_brackets, cyclic_multiplier_defect,
    exp_negative_bracket, gaussian_heat_bracket, heat_density_error_bound,
    hidden_heat_defect, laplacian_column, local_chart_certificate,
    nearest_integer, pi_bracket, rational_character_product_exponent,
    signed_representative, sqrt_bracket,
)


class ClockMetricTests(unittest.TestCase):
    def test_signed_representatives_cover_exact_source(self):
        for size in (2, 3, 5, 24, 120):
            reps = [signed_representative(n, size) for n in range(size)]
            self.assertEqual(len(set(reps)), size)
            for n, r in enumerate(reps):
                self.assertEqual((r - n) % size, 0)

    def test_local_chart_distances_and_radius_error(self):
        for size, e, radius in ((24, Q(1, 2), Q(2)),
                                (120, Q(1, 5), Q(7, 2)),
                                (720, Q(1, 24), Q(3))):
            cert = local_chart_certificate(size, e, radius)
            h = cert["radius_steps"]
            for a, b in product(range(-h, h + 1), repeat=2):
                self.assertEqual(e * cycle_distance(a, b, size), e * abs(a-b))
            self.assertLess(radius - h*e, cert["hausdorff_error_upper"])

    def test_wraparound_mutant_is_rejected_by_concrete_pair(self):
        # L>2R does NOT suffice for all pairwise distances in the radius-R ball.
        self.assertLess(2*4, 12)
        self.assertNotEqual(cycle_distance(-4, 4, 12), 8)
        with self.assertRaises(ClockLimitError):
            local_chart_certificate(12, 1, 4)

    def test_rounding_negative_times_and_ties(self):
        for denominator in range(1, 10):
            for numerator in range(-25, 26):
                x = Q(numerator, denominator)
                self.assertLessEqual(abs(nearest_integer(x) - x), Q(1, 2))

    def test_finite_action_error_and_no_wrap(self):
        word = (("translate", Q(3, 7)), ("multiply", 3),
                ("translate", Q(-2, 5)), ("multiply", 2))
        e, size = Q(1, 16), 720
        cert = action_horizon(size, e, 1, word)
        self.assertTrue(cert["no_wrap"])
        for n in range(-16, 17):
            discrete = n
            real = e*n
            for (op, value), stage in zip(word, cert["stages"]):
                if op == "translate":
                    discrete += stage["discrete_parameter"]
                    real += value
                else:
                    discrete *= value
                    real *= value
                self.assertEqual(signed_representative(discrete, size), discrete)
                self.assertLessEqual(abs(e*discrete-real), stage["error_upper"])
        self.assertFalse(action_horizon(24, e, 1, word)["no_wrap"])

    def test_multiplier_rank_is_not_an_arithmetic_isometry(self):
        for size, p in product((6, 24, 120), (2, 3, 5, 7)):
            cert = cyclic_multiplier_defect(size, p)
            image = {p*n % size for n in range(size)}
            self.assertEqual(len(image), cert["rank"])
            self.assertEqual(size-len(image), cert["kernel_dimension"])
            if p in (2, 3):
                self.assertFalse(cert["is_isometry"])
                self.assertEqual(p*(size//p) % size, 0)

    def test_wrong_physical_scaling_retains_circumference(self):
        # epsilon=1/N produces a unit circle, not a real line.
        for size in (24, 120, 720):
            e = Q(1, size)
            self.assertEqual(e*cycle_distance(0, size//2, size), Q(1, 2))
            with self.assertRaises(ClockLimitError):
                local_chart_certificate(size, e, 1)

    def test_fixed_conductor_parity_becomes_high_energy(self):
        # The same conductor-2 source character survives every even quotient.
        # Its scaled Laplacian energy is 4/epsilon^2, not a fixed real frequency.
        for size, e in ((24, Q(1, 4)), (120, Q(1, 8)), (720, Q(1, 16))):
            parity = [Q((-1)**n) for n in range(size)]
            image = [(2*parity[n]-parity[(n-1)%size]-parity[(n+1)%size])/e**2
                     for n in range(size)]
            self.assertEqual(image, [4*v/e**2 for v in parity])


class CompressionDefectTests(unittest.TestCase):
    def test_exact_uniform_block_compression(self):
        for radix, size, index in product((2, 3, 5, 7), (3, 5, 8), (0, 1, 2)):
            actual = compressed_laplacian_column(radix, size, index)
            expected = tuple(x/radix for x in laplacian_column(index, size))
            self.assertEqual(actual, expected)

    def test_false_laplacian_intertwining_mutation_fails(self):
        for radix in (2, 3, 5, 7):
            got = compressed_laplacian_column(radix, 5)
            desired = tuple(x/radix**2 for x in laplacian_column(0, 5))
            self.assertNotEqual(got, desired)
            self.assertEqual(got, tuple(radix*x for x in desired))

    def test_hidden_norm_from_independent_fine_vector(self):
        # Work with unnormalized block 1; divide every norm by radix at end.
        for radix in (2, 3, 5, 7, 11):
            size = 7*radix
            block = [Q(1) if 2*radix <= n < 3*radix else Q(0)
                     for n in range(size)]
            fine = [2*block[n]-block[(n-1)%size]-block[(n+1)%size]
                    for n in range(size)]
            means = [sum(fine[j*radix:(j+1)*radix], Q(0))/radix
                     for j in range(7)]
            hidden = [fine[n]-means[n//radix] for n in range(size)]
            norm = sum((x*x for x in hidden), Q(0))/radix
            self.assertEqual(norm, hidden_heat_defect(radix))
            self.assertGreater(norm, 0)
            self.assertEqual(hidden_heat_defect(radix, Q(1, 3)), 81*norm)

    def test_two_cycle_keeps_both_oriented_edges(self):
        self.assertEqual(laplacian_column(0, 2), (Q(2), Q(-2)))


class RationalHeatTests(unittest.TestCase):
    def test_exponential_enclosures_nest_and_recover_zero(self):
        self.assertEqual(exp_negative_bracket(0), RationalBracket(Q(1), Q(1)))
        for x in (Q(1, 10), Q(1, 2), Q(2), Q(8)):
            coarse = exp_negative_bracket(x, 8)
            fine = exp_negative_bracket(x, 16)
            self.assertLessEqual(coarse.lower, fine.lower)
            self.assertLessEqual(fine.upper, coarse.upper)
            self.assertGreater(fine.lower, 0)
            self.assertLess(fine.upper, 1)

    def test_machin_identity_has_independent_rational_tangent(self):
        # tan(2x)=2tan(x)/(1-tan(x)^2), applied twice at tan(x)=1/5.
        z = Q(1, 5)
        z = 2*z/(1-z*z)
        z = 2*z/(1-z*z)
        self.assertEqual((z-Q(1, 239))/(1+z*Q(1, 239)), 1)
        coarse, fine = pi_bracket(8), pi_bracket(16)
        self.assertTrue(3 < coarse.lower <= fine.lower <= fine.upper <= coarse.upper < Q(22, 7))

    def test_sqrt_interval_is_exactly_squared(self):
        for x in (Q(0), Q(1), Q(2), Q(7, 3), Q(999, 13)):
            out = sqrt_bracket(x)
            self.assertLessEqual(out.lower**2, x)
            self.assertGreaterEqual(out.upper**2, x)
            self.assertLessEqual(out.upper-out.lower, Q(1, 2**64))

    def test_heat_probability_mass_symmetry_and_positive_density(self):
        for size in (2, 4, 7, 12):
            out = cycle_heat_brackets(size, Q(1, 2), Q(1, 4), 32)
            self.assertLessEqual(sum(x.lower for x in out), 1)
            self.assertGreaterEqual(sum(x.upper for x in out), 1)
            for n in range(size):
                self.assertEqual(out[n], out[-n % size])
                self.assertGreater(out[n].lower, 0)
            self.assertLess(sum(x.upper-x.lower for x in out), Q(1, 10**15))

    def test_four_cycle_independent_closed_form(self):
        time = Q(3, 10)
        out = cycle_heat_brackets(4, 1, time, 32)
        e2, e4 = exp_negative_bracket(2*time), exp_negative_bracket(4*time)
        closed = RationalBracket(Q(1, 4)+e2.lower/2+e4.lower/4,
                                 Q(1, 4)+e2.upper/2+e4.upper/4)
        self.assertLessEqual(out[0].lower, closed.upper)
        self.assertLessEqual(closed.lower, out[0].upper)
        # A missing factor two in the Laplacian separates the enclosures.
        wrong = cycle_heat_brackets(4, 1, time/2, 32)[0]
        self.assertGreater(wrong.lower, out[0].upper)

    def test_probability_is_not_lebesgue_density(self):
        e = Q(1, 2)
        out = cycle_heat_brackets(12, e, Q(1, 4), 32)
        self.assertLessEqual(e*sum(x.lower/e for x in out), 1)
        self.assertGreaterEqual(e*sum(x.upper/e for x in out), 1)
        self.assertLess(e*sum(x.upper for x in out), Q(3, 4))

    def test_certified_heat_gaussian_comparison(self):
        size, e, t = 24, Q(1, 2), Q(1)
        heat = cycle_heat_brackets(size, e, t, 64)
        for n in range(-4, 5):
            gaussian = gaussian_heat_bracket(t, e*n)
            value = heat[n % size]
            upper_abs_error = max(abs(value.upper/e-gaussian.lower),
                                  abs(gaussian.upper-value.lower/e))
            bound = heat_density_error_bound(size, e, 1, abs(e*n))["total"]
            self.assertLessEqual(upper_abs_error, bound)

    def test_analytic_error_bound_decreases_in_line_regime(self):
        # N=m^2, epsilon=1/m; the full factorial theorem is a paper theorem.
        previous = None
        for m in (4, 8, 16, 32, 64):
            bound = heat_density_error_bound(m*m, Q(1, m), 1, 1)["total"]
            if previous is not None:
                self.assertLess(bound, previous)
            previous = bound

    def test_rational_character_product_and_sign_mutant(self):
        for denominator in (1, 2, 6, 12, 30, 49, 120):
            for numerator in range(-9, 10):
                cert = rational_character_product_exponent(numerator, denominator)
                self.assertEqual(cert["total_exponent"].denominator, 1)
        out = rational_character_product_exponent(1, 6)
        wrong_sign = out["real_exponent"] + sum(out["finite_fractional_parts"])
        self.assertNotEqual(wrong_sign.denominator, 1)

    def test_wrong_domains_are_rejected(self):
        for bad in (0.5, True, "1/2"):
            with self.assertRaises(ClockLimitError):
                local_chart_certificate(24, bad, 1)
        with self.assertRaises(ClockLimitError):
            heat_density_error_bound(7, 1, 1, 1)
        with self.assertRaises(ClockLimitError):
            cycle_heat_brackets(8, Q(1, 100), 1)
        with self.assertRaises(ClockLimitError):
            hidden_heat_defect(1)


if __name__ == "__main__":
    unittest.main()
