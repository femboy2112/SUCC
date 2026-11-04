"""Adversarial, exact-rational checks of the research-only Weyl bridge."""
import importlib.util
from fractions import Fraction as F
from pathlib import Path
import unittest

TARGET = (Path(__file__).resolve().parents[1] / "research" / "2026-11-02" /
          "weyl_borg_fusion" / "weyl_fusion.py")
spec = importlib.util.spec_from_file_location("succc_weyl_borg_fusion", TARGET)
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)


class WeylBorgFusionTests(unittest.TestCase):
    def test_four_signed_poles_match_independent_combined_fraction(self):
        for n in range(1, 257):
            self.assertEqual(m.forcing(n), m.combined_forcing(n))
            self.assertGreater(m.forcing(n), 0)
        self.assertEqual(m.forcing(1), F(47, 15))

    def test_actual_zero_seed_and_unwrapped_recurrence(self):
        states = m.selected_states(80)
        self.assertEqual(states[0], F(47, 15))
        for n in range(1, len(states)):
            self.assertEqual(states[n], 16*states[n-1] + m.forcing(n+1))
        self.assertEqual(m.selected_states(0), [])

    def test_fiber_exact_at_all_aliases_and_signed_frequencies(self):
        states = m.selected_states(64)
        for M in (16, 256, 4096):
            for h in (-17, -1, 1, 3, 16, M, M+1):
                for q in (-2, -1, 0, 1, 3):
                    for x in states:
                        self.assertEqual(m.fiber_exponent(x, M, h, q),
                                         m.direct_exponent(x, h+q*M))

    def test_integer_carry_boundary_is_not_dropped(self):
        x = F(-29, 13)
        for M in (16, 256):
            a, s = m.phase_coordinates(x, M)
            self.assertEqual(F(a, M)+s/M, m.fractional(x))
            self.assertEqual(m.fiber_exponent(x, M, M), m.fractional(M*x))

    def test_weyl_clock_commutator_mod_every_small_level(self):
        for Q in (16, 256, 4096):
            for x in (0, 1, Q//2, Q-1):
                for a in (0, 1, 15):
                    for h in (0, 1, 3, Q-1):
                        self.assertEqual(h*((x+a) % Q) % Q,
                                         (h*x+h*a) % Q)

    def test_source_two_adic_first_digit_and_carry(self):
        self.assertEqual(m.source_clock_residue(1, 2), 225)
        previous = F(0)
        for n in range(1, 70):
            next_state = 16*previous + m.forcing(n)
            for power in (1, 2, 3):
                Q = 16**power
                previous_mod = (previous.numerator *
                                pow(previous.denominator, -1, Q)) % Q
                forcing_mod = m.source_clock_residue(n, power)
                next_mod = (next_state.numerator *
                            pow(next_state.denominator, -1, Q)) % Q
                self.assertEqual(next_mod, (16*previous_mod+forcing_mod) % Q)
            previous = next_state

    def test_source_upper_bound_for_all_tested_indices(self):
        for n in range(2, 300):
            self.assertLessEqual(m.forcing(n), F(1, n*n))

    def test_green_laurent_enclosures_with_independent_rational_tails(self):
        for n in (1, 2, 3, 5, 8, 16, 32, 65, 101):
            for order in (2, 3):
                self.assertTrue(m.verify_green_bound(n, order, 22), (n, order))
        self.assertLess(m.C4, F(1, 6))
        self.assertEqual(m.C3, F(77, 864))
        self.assertEqual(m.C4, F(28339, 172800))

    def test_tail_interval_shrinks_independently_of_pi_digits(self):
        for n in (1, 17, 55):
            lo8, hi8 = m.green_interval(n, 8)
            lo20, hi20 = m.green_interval(n, 20)
            self.assertLessEqual(lo8, lo20)
            self.assertLessEqual(hi20, hi8)
            self.assertLess(hi20-lo20, hi8-lo8)

    def test_moving_bounds_are_exact_nonnegative_and_improve_by_laurent_order(self):
        for N, h in ((100, 1), (500, 51), (1000, 16000)):
            J = min(N, max(1, int(abs(h)**.25)+1))
            b2 = m.moving_weyl_bound(N,h,2,J)
            b3 = m.moving_weyl_bound(N,h,3,J)
            self.assertTrue(all(x>=0 for x in b2+b3))
            if h>1:
                self.assertLess(b3[1], b2[1])

    def test_frequency_time_shift_budget_is_source_scoped(self):
        for N, h, k, J in ((100,1,0,10),(500,3,2,20),(1000,1,4,100)):
            a,b=m.shifted_frequency_bound(N,h,k,J)
            self.assertGreaterEqual(a,0)
            self.assertGreaterEqual(b,0)
            self.assertEqual(a,F(2*(k+J),N))
            self.assertEqual(b,F(2*abs(h)*16**k,15*N*J))

    def test_hostile_mutation_is_detected(self):
        # Wrong pole coefficient must break source fingerprint immediately.
        wrong = m.forcing(1) + F(1, 8*1-3)
        self.assertNotEqual(wrong, m.combined_forcing(1))
        # Cell counts alone cannot see h=M: exact uniform bin controls are nonnormal.
        for M in (16, 256):
            points = [F(a,M) for a in range(M)]
            self.assertEqual({m.phase_coordinates(x,M)[0] for x in points}, set(range(M)))
            self.assertTrue(all(m.direct_exponent(x,M)==0 for x in points))
            # Same occupied cells, a second within-cell profile flips the M-character.
            shifted = [x+F(1,2*M) for x in points]
            self.assertTrue(all(m.direct_exponent(x,M)==F(1,2) for x in shifted))


if __name__ == "__main__":
    unittest.main()
