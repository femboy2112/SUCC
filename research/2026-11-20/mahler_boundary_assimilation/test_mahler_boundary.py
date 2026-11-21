"""Exact, scoped tests of Mahler auxiliary charts and independent W/C rivals."""
import importlib.util
import pathlib
import unittest
from fractions import Fraction as F

spec = importlib.util.spec_from_file_location("mahler_boundary", pathlib.Path(__file__).with_name("mahler_boundary.py"))
m = importlib.util.module_from_spec(spec)
import sys
sys.modules[spec.name] = m
spec.loader.exec_module(m)


class TestBoundary(unittest.TestCase):
    def test_guards_exact_edges(self):
        examples = [
            (2, F(0), True, "none"),
            (2, F(1, 3)-F(1, 100), True, "none"),
            (2, F(1, 3), False, "even_exit_at_one_third"),
            (1, F(0), False, "odd_branch_mismatch_at_one_third"),
            (1, F(1, 3), True, "none"),
            (1, F(1, 2)-F(1, 100), True, "none"),
            (1, F(1, 2), False, "outside_J"),
        ]
        for g, r, ok, name in examples:
            with self.subTest(g=g, r=r):
                report = m.boundary_step(g, r)
                self.assertEqual(report.chart_eligible, ok)
                self.assertEqual(report.boundary, name)

    def test_all_fraction_grid_guards_vs_independent_multiplier(self):
        count = 0
        for g in range(18):
            for numerator in range(40):
                r = F(numerator, 80)
                report = m.boundary_step(g, r)
                true_g, true_r = m.true_rational_step(g, r)
                self.assertEqual((report.actual_integer, report.actual_remainder), (true_g, true_r))
                self.assertEqual(report.chart_eligible,
                                 (report.chart_integer == true_g and report.chart_remainder == true_r and F(0) <= true_r < F(1, 2)))
                count += 1
        self.assertEqual(count, 720)

    def test_chart_failures_do_not_terminate_true_multiplier(self):
        even = m.boundary_step(2, F(1, 3))
        self.assertEqual((even.actual_integer, even.actual_remainder), (3, F(1, 2)))
        odd = m.boundary_step(1, F(1, 4))
        self.assertEqual((odd.actual_integer, odd.actual_remainder), (1, F(7, 8)))
        self.assertEqual(odd.chart_integer, 2)
        self.assertEqual(m.first_boundary(1, F(1, 4), 10)[0], 0)

    def test_survivor_intervals_small_horizons(self):
        self.assertEqual(m.survivor_interval(0, 0), (F(0), F(1, 2)))
        self.assertEqual(m.survivor_interval(0, 1), (F(0), F(1, 3)))
        self.assertEqual(m.survivor_interval(0, 2), (F(0), F(2, 9)))
        self.assertEqual(m.survivor_interval(1, 1), (F(1, 3), F(1, 2)))
        self.assertEqual(m.survivor_interval(1, 4), None)

    def test_survivor_intervals_against_direct_full_orbit_on_grid(self):
        for seed in range(13):
            for steps in range(7):
                interval = m.survivor_interval(seed, steps)
                for r0 in [F(j, 180) for j in range(90)]:
                    in_interval = interval is not None and interval[0] <= r0 < interval[1]
                    self.assertEqual(in_interval, m.first_boundary(seed, r0, steps) is None,
                                     msg=(seed, steps, r0, interval))

    def test_true_dynamics_matches_chart_in_admitted_survival(self):
        g0 = 13
        interval = m.survivor_interval(g0, 4)
        self.assertIsNotNone(interval)
        r = sum(interval, F(0)) / 2
        g = g0
        for _ in range(4):
            report = m.boundary_step(g, r)
            self.assertTrue(report.chart_eligible)
            self.assertEqual((report.chart_integer, report.chart_remainder),
                             (report.actual_integer, report.actual_remainder))
            g, r = report.actual_integer, report.actual_remainder


class Test2AdicJournal(unittest.TestCase):
    def test_mahler_and_collatz_not_same_untransformed_orbit(self):
        self.assertEqual(m.parity_bits(2, 3, kind="mahler"), (0, 1, 1))
        self.assertEqual(m.parity_bits(2, 3, kind="collatz"), (0, 1, 0))

    def test_exhaustive_reverse_2adic_parity_construction(self):
        for kind in ("mahler", "collatz"):
            for size in range(1, 9):
                for word_int in range(1 << size):
                    bits = tuple((word_int >> j) & 1 for j in range(size))
                    seed = m.inverse_parity_residue(bits, kind=kind)
                    self.assertEqual(m.parity_bits(seed, size, kind=kind), bits)

    def test_prefix_common_series_padic_identity(self):
        for g in range(24):
            for n in range(1, 17):
                bits = m.parity_bits(g, n, kind="mahler")
                partial = m.weighted_parity_prefix(bits)
                self.assertEqual(m.rational_mod_2_power(partial + 3*g, n), 0)

    def test_real_prefix_remainder_identity(self):
        g0 = 13
        interval = m.survivor_interval(g0, 5)
        if interval is None:
            interval = m.survivor_interval(g0, 3)
            n = 3
        else:
            n = 5
        self.assertIsNotNone(interval)
        r0 = (interval[0] + interval[1])/2
        x = g0 + r0
        g, r = g0, r0
        bits = []
        for _ in range(n):
            report = m.boundary_step(g, r)
            self.assertTrue(report.chart_eligible)
            bits.append(g & 1)
            g, r = report.actual_integer, report.actual_remainder
        self.assertEqual(x * F(3, 2)**n, g + r)
        self.assertEqual(3*r0, m.weighted_parity_prefix(bits) + 3*F(2, 3)**n*r)

    def test_pi_finite_nibbles_and_mahler_boundary_no_go(self):
        bits = m.bits_from_hex_journal(m.PI_12_HEX_DIGITS)
        self.assertEqual(bits[:4], (1, 1, 0, 0))
        self.assertGreaterEqual(m.weighted_parity_prefix(bits[:2]), F(5, 3))
        self.assertGreaterEqual(m.weighted_parity_prefix(bits[:2])/3, F(5, 9))
        for kind in ("mahler", "collatz"):
            seed = m.inverse_parity_residue(bits, kind=kind)
            self.assertEqual(m.parity_bits(seed, len(bits), kind=kind), bits)
        self.assertEqual(m.inverse_parity_residue(bits, kind="collatz"), 0x138D4B466283)

    def test_one_bit_is_not_collision_free(self):
        bits = (1,)
        self.assertEqual(m.inverse_parity_residue(bits, kind="mahler"), 1)
        self.assertEqual(m.inverse_parity_residue(bits, kind="collatz"), 1)
        self.assertNotEqual(m.inverse_parity_residue((0, 1, 1), kind="mahler"),
                            m.inverse_parity_residue((0, 1, 1), kind="collatz"))

    def test_fibonacci_word_count(self):
        self.assertEqual([m.fibonacci_language_count(n) for n in range(8)],
                         [1, 2, 3, 5, 8, 13, 21, 34])
        for n in range(10):
            words = [[(mask >> j) & 1 for j in range(n)] for mask in range(1 << n)]
            count = sum(not any(bits[j] == bits[j+1] == 1 for j in range(n-1)) for bits in words)
            self.assertEqual(m.fibonacci_language_count(n), count)

    def test_radial_mahler_boundary_and_index(self):
        cases = [
            (F(1, 4), "inner", 4, F(0), 0),
            (F(1), "first_root_boundary", 4, F(0), None),
            (F(3, 2), "middle", 4, F(1, 2), 1),
            (F(2), "four_root_boundary", 4, F(1, 2), None),
            (F(9, 4), "outer", 1, F(5, 2), 5),
        ]
        for q, region, scale, exponent, winding in cases:
            with self.subTest(q=q):
                report = m.radial_spectral_certificate(q)
                self.assertEqual((report.region, report.log_constant, report.log_q_factor, report.winding),
                                 (region, scale, exponent, winding))
                self.assertEqual(report.toeplitz_index, -winding if winding is not None else None)
        with self.assertRaises(ValueError): m.radial_spectral_certificate(F(0))

    def test_source_polynomial_and_matched_jet_mutant(self):
        # Exact source identity, independent of float roots or selected digits.
        def times(a, b):
            out = [0]*(len(a)+len(b)-1)
            for j, x in enumerate(a):
                for k, y in enumerate(b): out[j+k] += x*y
            return out
        H = times([2, 0, 1], [2, 2, 1])
        self.assertEqual(H, [4, 4, 4, 2, 1])
        Q = times([1, -1], H)
        self.assertEqual(Q, [4, 0, 0, -2, -1, -1])
        self.assertEqual(times(H, [-4, 4, 0, -2, 1]),
                         [-16, 0, 0, 0, 0, 0, 0, 0, 1])
        for n in range(1, 80):
            direct = F(4,8*n-7)-F(2,8*n-4)-F(1,8*n-3)-F(1,8*n-2)
            reduced = F(120*n*n-89*n+16,
                        (2*n-1)*(4*n-1)*(8*n-7)*(8*n-3))
            self.assertEqual(direct, reduced)
        # H*=H+(1-t) preserves Q(1), Q'(1), not the four-root radius.
        Hstar = [5,3,4,2,1]
        self.assertNotEqual(Hstar[1]**2, Hstar[3]**2*Hstar[0])  # 3^2 != 2^2*5

    def test_boundary_frequency_does_not_prove_pi_R0(self):
        # Finite shadow of the rigorous sparse-zero F-word counterexample:
        # x = 1-15*sum_(k>=2)16^(-2^(2^k)), digits F except d_Nk=0.
        # Selected shell [32,64) lies far between zero positions 16 and 256.
        # Computation below is an *exact finite* diagnostic; the infinite
        # counterexample and all-shell density proof are paper arguments.
        x = F(1) - F(15,16**16) - F(15,16**256)
        for n in range(32,64):
            theta = (16**n * x) % 1
            self.assertEqual(theta, 1-F(15,16**(256-n)))
            self.assertTrue(F(15,16) <= theta < 1)  # next digit F
            self.assertLess(1-theta, F(1,16**190))
        self.assertEqual(m.bits_from_hex_journal("F")[:4], (1,1,1,1))

    def test_errors(self):
        with self.assertRaises(ValueError): m.survivor_interval(-1, 3)
        with self.assertRaises(ValueError): m.boundary_step(1, F(1, 1))
        with self.assertRaises(ValueError): m.inverse_parity_residue((0, 2), kind="mahler")
        with self.assertRaises(ValueError): m.rational_mod_2_power(F(1, 2), 3)
        with self.assertRaises(ValueError): m.bits_from_hex_journal("12Q")


if __name__ == "__main__":
    unittest.main()
