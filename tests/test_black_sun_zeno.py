"""BLACK SUN IV tests: Zeno schedules, the arrow floor, the budget fight."""
import unittest

from fractions import Fraction

from observational_succ.black_sun_zeno import (
    arrow_floor,
    arrow_floor_proof_check,
    arrow_measured_vs_floor,
    paradox_point_demo,
    rung_schedule,
    zeno_identity_check,
    zero_side_budget,
)


class TestZenoSchedule(unittest.TestCase):
    """BS-IV-1: explicit a-priori rung schedule."""

    def test_schedule_monotone_and_finite(self):
        prev_J = 0
        for eps in (1e-1, 1e-2, 1e-4, 1e-6):
            J, eps_J = rung_schedule(eps)
            self.assertGreaterEqual(J, prev_J)
            self.assertLessEqual(eps_J, eps)
            self.assertGreater(eps_J, eps/4)  # not absurdly conservative
            prev_J = J
        # the ~ eps^{-1/2} law
        J4, _ = rung_schedule(1e-4)
        J8, _ = rung_schedule(1e-8)
        self.assertAlmostEqual(J8/J4, 100, delta=30)  # sqrt(100)=10 -> x100

    def test_schedule_verification(self):
        import numpy as np
        rng = np.random.default_rng(11)
        vs = list(rng.standard_normal(7)*0.4)
        from observational_succ.black_sun_zeno import rung_schedule_verify
        for (eps, J, sched, measured) in rung_schedule_verify(vs, 0.5, (1e-2,)):
            self.assertLessEqual(measured, sched,
                                 "measured truncation error must respect "
                                 "the a-priori schedule")


class TestZenoIdentityAndParadoxPoint(unittest.TestCase):
    """BS-IV-2: the geometric identity; the divergence at t=0."""

    def test_identity(self):
        for t in ("0.3", "0.7", "2.0", "7.0"):
            closed, s, err = zeno_identity_check(t)
            self.assertLess(float(err), 1e-30)

    def test_paradox_point_diverges(self):
        rows = paradox_point_demo((10, 40, 160))
        for i in range(len(rows)-1):
            self.assertGreater(rows[i+1][1], rows[i][1])
        # logarithmic growth: sum_{j<J} 2/(4j+1) ~ (1/2) log J + c
        self.assertGreater(rows[-1][1], 3.5)


class TestArrowTheorem(unittest.TestCase):
    """BS-IV-3: d_k > 0 with the unconditional lcm floor."""

    def test_floor_proof(self):
        for k in (1, 3, 6, 8):
            sq = arrow_floor_proof_check(k)
            floor, L = arrow_floor(k)
            self.assertAlmostEqual(sq, floor**2, places=12)
            # every {L/l} = 0 for l in 2..k+1 (the one-line proof's content)
            for l in range(2, k+2):
                self.assertEqual(L % l, 0)

    def test_measured_above_floor(self):
        for (k, d, floor, L) in arrow_measured_vs_floor():
            self.assertGreaterEqual(d, floor,
                                    f"d_{k} must respect the floor")

    def test_floor_geometric(self):
        # log lcm(2..n) ~ psi(n) ~ n: the floor decays geometrically in k
        f4, L4 = arrow_floor(4)
        f8, L8 = arrow_floor(8)
        self.assertLess(f8/f4, 0.1)  # 4 extra steps shrink floor > 10x


class TestBudgetFight(unittest.TestCase):
    """BS-IV-4: the zero-side budget at the 1e-3 scale."""

    def test_budget_scale(self):
        import mpmath as mp
        budget, comp = zero_side_budget(0.5, T0=14)
        # the budget must be small but not absurd: the same scale as the
        # window margins (1e-4..1e-3)
        self.assertLess(float(budget), 5e-3)
        self.assertGreater(float(budget), 1e-4)

    def test_budget_is_test_dependent_not_monotone(self):
        # the budget depends on the TEST FUNCTION's high-frequency tail,
        # which oscillates with the window (cos(14a) factor): not monotone
        b_half, _ = zero_side_budget(0.5, T0=14)
        b_full, _ = zero_side_budget(1.0, T0=14)
        b_075, _ = zero_side_budget(0.75, T0=14)
        for b in (b_half, b_full, b_075):
            self.assertGreater(float(b), 1e-5)
            self.assertLess(float(b), 5e-3)


if __name__ == "__main__":
    unittest.main()