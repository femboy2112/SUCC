"""Tests for the π-normality moonshot instrument.

These test the INSTRUMENT (precision discipline, the circularity identity, and
the shape of the Fejér energy). They do NOT test or claim π normality.
"""
import unittest

import mpmath as mp

from observational_succ.pi_normality_moonshot import (
    MoonShotError, _dps_for, chord_energy_identity_check, chord_mean,
    fejer_energy, phases, phases_for_pi, weyl_sum,
)


class TestPrecisionDiscipline(unittest.TestCase):
    """The bug this whole module exists to prevent."""

    def test_dps_scales_with_terms(self):
        self.assertGreater(_dps_for(16, 1000), 1200)
        self.assertLess(_dps_for(16, 10), 100)

    def test_phases_survive_large_j_for_pi(self):
        # frac(16^j pi) must stay in [0,1) and be non-degenerate at large j.
        ph = phases_for_pi(16, 40)
        self.assertTrue(all(0 <= float(p) < 1 for p in ph))
        tail = [float(p) for p in ph[30:]]
        # if precision were wrong these would all be 0.0 exactly
        self.assertGreater(sum(1 for t in tail if t != 0.0), 5)

    def test_phases_match_independent_computation(self):
        ph = phases_for_pi(16, 20)
        with mp.workdps(300):
            pi = +mp.pi
            for j in (5, 10, 15, 19):
                ref = mp.frac(mp.mpf(16) ** j * pi)
                self.assertLess(abs(ph[j] - ref), mp.mpf('1e-40'))

    def test_weyl_sum_rejects_zero_h(self):
        with self.assertRaises(MoonShotError):
            weyl_sum("pi", 16, 0, 32)


class TestChordHaarTracking(unittest.TestCase):
    """π's orbit chord mean tracks the Haar value 2 (as normality requires)."""

    def test_chord_mean_near_two(self):
        for n in (100, 500):
            m = chord_mean("pi", 16, n)
            self.assertLess(abs(m - 2), mp.mpf('0.25'),
                            f"N={n}: chord mean {m} too far from 2")

    def test_chord_mean_does_not_decay_like_one_over_n(self):
        # the precision bug produced values ~1/N; a correct computation must not
        m100 = chord_mean("pi", 16, 100)
        m500 = chord_mean("pi", 16, 500)
        self.assertGreater(float(m500), 0.5)   # would be ~0.004 under the bug


class TestCircularity(unittest.TestCase):
    """The chord-polynomial route returns exactly the Fourier energy."""

    def test_chord_energy_equals_fourier_energy(self):
        for m in (1, 2, 3):
            lhs, rhs, gap = chord_energy_identity_check(m, 12, base=2)
            self.assertLess(gap, mp.mpf('1e-40'),
                            f"m={m}: chord != Fourier (gap {gap})")


class TestFejerEnergyShape(unittest.TestCase):
    """E-1 is small compared with M, and comparable to M/N."""

    def test_energy_below_trivial_band_bound(self):
        for n in (512, 2048):
            for M in (4, 8):
                e = fejer_energy("pi", 16, M, n)
                self.assertGreaterEqual(e, 0.0)      # Fejer is nonnegative
                self.assertLess(e, M)                # far below the trivial bound

    def test_energy_nonnegative(self):
        # E >= 1 always (CC-05 floor); E-1 >= 0
        self.assertGreaterEqual(fejer_energy("pi", 16, 4, 256), 0.0)


if __name__ == "__main__":
    unittest.main()