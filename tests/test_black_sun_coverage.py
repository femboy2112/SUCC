"""BLACK SUN II tests: coverage theory (phase transition, coverage law, no-go)."""
import unittest

import mpmath as mp

from observational_succ.black_sun_coverage import (
    coverage_table,
    lambda0_pair,
    measured_rescue_factor,
    nogo_budget_gap,
    omega,
    omega_2pi_bracket,
    omega_monotonicity_check,
    omega_zero_bracket,
    phase_rescue_factors,
)


class TestOmegaBand(unittest.TestCase):
    """BS-II-1/2: Omega monotone, negative band bracketed at 2pi."""

    def test_monotonicity_step(self):
        worst = omega_monotonicity_check(u_max=10.0, du=0.5)
        self.assertLess(float(worst), -0.1,
                        "Im psi'(1/4+iu/2) < 0 required for Omega'  > 0")

    def test_2pi_bracket_contains_direct(self):
        lo, hi = omega_2pi_bracket(J=40)
        direct = omega(2*mp.pi)
        self.assertLess(lo, direct)
        self.assertLess(direct, hi)
        self.assertLess(hi, mp.mpf('0'), "Omega(2pi) must be negative")
        self.assertGreater(lo, mp.mpf('-0.002'))

    def test_zero_bracket(self):
        lo, hi = omega_zero_bracket()
        self.assertAlmostEqual(float(lo), 6.283185307179586, places=9)
        self.assertEqual(hi, 6.4)


class TestPhaseTransition(unittest.TestCase):
    """BS-II-3: the archimedean phase transition bracket (0.370, 0.372)."""

    def test_bracket(self):
        lamA_lo, _, _ = lambda0_pair(0.370, M=1200)
        lamA_hi, _, _ = lambda0_pair(0.372, M=1200)
        self.assertGreater(lamA_lo, 3e-4,
                           "lambda_0(A)(0.370) must be clearly positive")
        self.assertLess(lamA_hi, -3e-4,
                        "lambda_0(A)(0.372) must be clearly negative")

    def test_prime_free_positivity_below_transition(self):
        for a in (0.30, 0.34, 0.36):
            lamA, _, _ = lambda0_pair(a, M=1000)
            self.assertGreater(lamA, 0,
                               f"a={a} below transition must be positive")


class TestCoverageLaw(unittest.TestCase):
    """BS-II-4: deficit/budget ratio bounded; lambda_0(Q) near zero."""

    def test_coverage_ratios(self):
        rows = coverage_table([0.42, 0.5, 0.5493, 0.7, 1.0], M=1000)
        for (a, deficit, budget, ratio, lamQ) in rows:
            self.assertGreater(budget, 0)
            self.assertLess(ratio, 0.5,
                            f"coverage ratio at a={a} must be < 0.5")
            self.assertLess(abs(lamQ), 1e-3)


class TestPhaseRescue(unittest.TestCase):
    """BS-II-5: the rescue phase structure."""

    def test_rescue_phases(self):
        phases = dict(phase_rescue_factors((2, 3, 5)))
        self.assertLess(float(phases[2]), 0,
                        "cos(2 pi log 2) < 0: prime-2 rescues the 2pi mode")
        self.assertGreater(float(phases[3]), 0,
                            "cos(2 pi log 3) > 0: prime-3 anti-rescues")

    def test_measured_rescue_factor(self):
        corr, factor, lamA, lamQ = measured_rescue_factor(0.5, M=1200)
        self.assertLess(corr, -0.1,
                        "deficit direction anti-correlates with log2 shift")
        # rescue factor (Q - A)/c2 on the A-minimizing direction must be
        # positive (the prime-2 term pushes the negative direction up)
        self.assertGreater(factor, 0.1)


class TestNoGoBudget(unittest.TestCase):
    """BS-II-6: crude band-mass accounting cannot close (gap > 0)."""

    def test_nogo_gap_positive(self):
        # a = 0.549 < log(sqrt 3): only the prime-2 atom is in the window
        deficit_crude, rescue_max, gap, beta = nogo_budget_gap(0.549)
        self.assertGreater(float(deficit_crude), 4.8,
                           "crude deficit must be ~C_G*beta with beta ~ 0.94")
        self.assertLess(float(beta), 1.0)
        self.assertGreater(float(gap), 1.5,
                           "the crude route must fail by a margin > 1.5")
        # and the TRUE deficit is far smaller (the profile weighting matters)
        lamA, _, _ = lambda0_pair(0.549, M=1000)
        self.assertLess(-lamA, float(deficit_crude)/8,
                        "true deficit << crude deficit bound")


if __name__ == "__main__":
    unittest.main()