import unittest
from fractions import Fraction as F

from observational_succ.duck_bbp_fourier import (
    BBP_POLES, PoleTerm, arc_discrepancy_transport_budget, bbp_force,
    bbp_force_positive_form, bbp_shadow_budget, bbp_shadow_sum_budget,
    bbp_tail_partial, circle_distance, forced_orbit, fourier_sum_transport_budget,
    fractional_part, leading_matched_impostor, prefix_impostor,
    rational_coboundary, solve_rational_coboundary, square_tail_majorant,
    weighted_pole_invariants,
)


class DuckBBPFourierTests(unittest.TestCase):
    def test_independent_bbp_forms_and_rational_bounds(self):
        for n in list(range(1, 100)) + [1000, 10**9]:
            expected = F(120*n*n-89*n+16, 512*n**4-1024*n**3+712*n*n-206*n+21)
            self.assertEqual(bbp_force(n), expected)
            self.assertEqual(bbp_force(n), bbp_force_positive_form(n))
            self.assertEqual(bbp_force(n), sum((t.coefficient/(n-t.pole)**t.order for t in BBP_POLES), F(0)))
            self.assertGreater(expected, 0)
            self.assertLessEqual(expected, F(8, n*n))
            self.assertGreater(bbp_force_positive_form(n), bbp_force_positive_form(n+1))
            self.assertLessEqual(bbp_shadow_budget(n), F(1, (8*n+1)**2))

    def test_tail_transport_index_with_exact_finite_bbp_source(self):
        depth = 48
        pi_partial = sum((bbp_force(m)/16**(m-1) for m in range(1, depth+1)), F(0))
        orbit = forced_orbit(bbp_force, 16, depth)
        for n in [1, 2, 3, 9, 17, 47]:
            tail, remaining = bbp_tail_partial(n, depth-n)
            self.assertEqual(fractional_part(16**(n-1)*pi_partial), fractional_part(orbit[n]+tail))
            self.assertLessEqual(tail, F(8, 15*(n+1)**2))
            self.assertLessEqual(tail, bbp_shadow_budget(n))
            # A wrong n versus n-1 digit index is genuinely detected.
            self.assertNotEqual(fractional_part(16**n*pi_partial), fractional_part(orbit[n]+tail))
            self.assertGreater(remaining, 0)

    def test_tail_remainder_against_longer_exact_holdout(self):
        for n in [1, 7, 64, 1000]:
            for k in [0, 1, 4, 12]:
                low, error = bbp_tail_partial(n, k)
                high, unused = bbp_tail_partial(n, k+20)
                self.assertGreaterEqual(high, low)
                self.assertLessEqual(high-low, error)

    def test_telescoping_square_majorant_and_uniform_character_budget(self):
        for start in [1, 2, 7, 1000]:
            for length in [0, 1, 9, 100]:
                actual = sum((F(1, (n+1)**2) for n in range(start, start+length)), F(0))
                self.assertLessEqual(actual, square_tail_majorant(start, length))
                for h in [-7, 0, 1, 11]:
                    self.assertLessEqual(fourier_sum_transport_budget(h, start, length), F(abs(h), 5))
                shadow = sum((bbp_shadow_budget(n) for n in range(start, start+length)), F(0))
                self.assertLessEqual(shadow, bbp_shadow_sum_budget(start, length))
        self.assertEqual(fourier_sum_transport_budget(0, 1, 100), 0)

    def test_discrepancy_budget_is_difference_not_cancellation(self):
        values = [arc_discrepancy_transport_budget(n)[0] for n in [1, 8, 64, 512]]
        self.assertTrue(all(a >= b for a, b in zip(values, values[1:])))
        self.assertGreater(values[0], values[-1])
        # Two identical constant orbits have zero transport but discrepancy one.
        self.assertEqual(circle_distance(F(0), F(0)), 0)
        self.assertGreater(values[-1], 0)

    def test_arc_transport_against_exact_empirical_discrepancy(self):
        def discrepancy(points):
            points = sorted(points)
            size = len(points)
            return (max(F(j, size)-point for j, point in enumerate(points, 1))
                    + max(point-F(j-1, size) for j, point in enumerate(points, 1)))
        depth = 48
        pi_partial = sum((bbp_force(m)/16**(m-1) for m in range(1, depth+1)), F(0))
        orbit = forced_orbit(bbp_force, 16, depth)
        for size in [3, 8, 16, 32]:
            digit_partial = [fractional_part(16**(n-1)*pi_partial) for n in range(1, size+1)]
            difference = abs(discrepancy(orbit[1:size+1])-discrepancy(digit_partial))
            self.assertLessEqual(difference, arc_discrepancy_transport_budget(size)[0])

    def test_weighted_residue_obstruction_for_actual_bbp(self):
        invariants = weighted_pole_invariants(BBP_POLES, 16)
        self.assertEqual(len(invariants), 4)
        self.assertTrue(all(invariants.values()))
        self.assertIsNone(solve_rational_coboundary(BBP_POLES, 16))

    def test_complete_coboundary_solver_with_mixed_shift_and_order_holdouts(self):
        cases = [(), (PoleTerm(F(-1), 2, F(1, 64)),),
                 (PoleTerm(F(-7, 3), 1, F(5, 11)), PoleTerm(F(2, 3), 1, F(-7, 5))),
                 (PoleTerm(F(-1, 2), 3, F(9)), PoleTerm(F(3, 2), 3, F(-9)),
                  PoleTerm(F(5, 7), 2, F(4, 3)))]
        for base in [2, 3, 16, 257]:
            for correction in cases:
                forcing = rational_coboundary(correction, base)
                self.assertTrue(all(value == 0 for value in weighted_pole_invariants(forcing, base).values()))
                solution = solve_rational_coboundary(forcing, base)
                self.assertIsNotNone(solution)
                self.assertEqual(rational_coboundary(solution, base), forcing)
        control = rational_coboundary((PoleTerm(F(0), 1, F(1)),), 16)
        self.assertNotEqual(sum(t.coefficient for t in control), 0)  # unweighted mutant fails
        mutant = control + (PoleTerm(F(1), 1, F(1, 10**30)),)
        self.assertIsNone(solve_rational_coboundary(mutant, 16))

    def test_positive_leading_matched_impostor_has_rational_shadow(self):
        orbit = forced_orbit(leading_matched_impostor, 16, 50)
        for n in range(1, 51):
            self.assertGreater(leading_matched_impostor(n), 0)
            self.assertLessEqual(leading_matched_impostor(n), F(1, 4*n*n))
            self.assertEqual(orbit[n], fractional_part(F(16**n, 64)-F(1, 64*(n+1)**2)))
            if n >= 2:
                self.assertEqual(circle_distance(orbit[n], 0), F(1, 64*(n+1)**2))

    def test_arbitrary_exact_prefix_can_be_forged_without_global_normality(self):
        for size in [0, 1, 2, 3, 5, 8, 12]:
            samples = [bbp_force(n) for n in range(1, size+1)]
            fake = prefix_impostor(samples)
            self.assertEqual(fake.denominator_power, size+2)
            self.assertLessEqual(len(fake.differences)-1, size)
            for n, value in enumerate(samples, 1):
                self.assertEqual(fake.force(n), value)
            self.assertEqual(forced_orbit(fake.force, 16, size), forced_orbit(bbp_force, 16, size))
            for n in [size+1, size+2, 2*size+9]:
                self.assertEqual(forced_orbit(fake.force, 16, n)[-1], fractional_part(-fake.correction(n)))

    def test_exact_domain_guards(self):
        for bad in [True, 1.0, F(1), -1]:
            with self.assertRaises(ValueError):
                bbp_force(bad)
        for bad in [True, 1e-200, float('nan')]:
            with self.assertRaises(ValueError):
                PoleTerm(bad, 1, F(1))
            with self.assertRaises(ValueError):
                prefix_impostor([bad])
        with self.assertRaises(ValueError):
            fourier_sum_transport_budget(1.0, 1, 1)
        with self.assertRaises(ValueError):
            arc_discrepancy_transport_budget(0)


if __name__ == '__main__':
    unittest.main()
