"""Main XXI integration receipt for #540 GA-09: the K=3 anti-clustering countermodel.

Each check evaluates the actual quantities; nothing compares a module against itself.
The finite rows use exact pair enumeration; the K formula 3 - 3/A and the analytic limit
sqrt(5)/9 - 1/6 are derived independently in the module docstring and recomputed here.
"""
import importlib.util
import pathlib
import unittest
from fractions import Fraction

import sympy as sp

_PATH = pathlib.Path(__file__).resolve().parents[1] / "research/2026-11-07/main_xxi_receipts/ga09_countermodel.py"
_spec = importlib.util.spec_from_file_location("ga09_countermodel", _PATH)
ga09 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ga09)


class GA09Countermodel(unittest.TestCase):
    def test_k_bound_holds_at_every_radius_and_matches_closed_form(self):
        for A in (1, 2, 3, 7, 50, 200):
            K = ga09.k_max(A)
            self.assertLessEqual(K, 3, A)
            if A >= 2:
                self.assertEqual(K, 3 - Fraction(3, A), A)

    def test_k_bound_checked_pointwise_on_a_dense_rational_grid(self):
        # independent of the jump-point argument: brute-force B_A(t) at many radii
        A = 40
        pts = [Fraction(j, A) * ga09.L for j in range(A)]
        for t in [Fraction(k, 997) for k in range(0, 499)]:
            B = sum(1 for x in pts for y in pts if min(abs(x - y), 1 - abs(x - y)) <= t)
            self.assertLessEqual(B, A + 3 * A * A * t, t)

    def test_limit_energy_two_routes_agree_and_is_positive(self):
        lim = ga09.limit_energy_by_integration()
        self.assertEqual(sp.simplify(lim - (sp.sqrt(5) / 9 - sp.Rational(1, 6))), 0)
        self.assertTrue(sp.simplify(lim).is_positive)
        self.assertGreater(float(sp.N(lim, 30)), 0.0817)

    def test_finite_energies_do_not_decay(self):
        lim = float(sp.N(ga09.E_LIMIT, 30))
        vals = [float(sp.N(ga09.golden_energy(A), 30)) for A in (50, 200)]
        for v in vals:
            self.assertGreater(v, 0.08)
        self.assertLess(abs(vals[1] - lim), abs(vals[0] - lim))

    def test_haar_like_control_is_small(self):
        # control: the full-circle grid j/A is asymptotically Haar, so its energy must be small,
        # which shows the energy functional is not trivially bounded below
        A = 200
        S = A * ga09.B_GOLD
        for d in range(1, A):
            dist = min(Fraction(d, A), 1 - Fraction(d, A))
            if (3 - 2 * dist) ** 2 > 5:
                S += A * (ga09.B_GOLD - sp.Rational(dist.numerator, dist.denominator))
        E = float(sp.N(S / (ga09.B_GOLD * A * A) - ga09.B_GOLD, 30))
        self.assertLess(E, 1e-3)

    def test_rejects_bad_input(self):
        for bad in (0, -1, True, 2.0):
            with self.assertRaises(ValueError):
                ga09.pair_distance_counts(bad)


if __name__ == "__main__":
    unittest.main()
