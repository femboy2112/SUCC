"""BLACK SUN II tests: Goldbach Fourier dichotomy and binary mean dictionary."""
import unittest

from observational_succ.black_sun_goldbach import (
    fourier_dichotomy_check,
    hyperbola_identity,
    mean_G_track,
    prime_power_decomposition,
    R_Lambda,
    von_mangoldt_sieve,
)


class TestFourierDichotomy(unittest.TestCase):
    """BS-G1: sum diagonal vs difference diagonal."""

    def test_dichotomy(self):
        for N in (20, 30):
            c_sum, c_diff, r = fourier_dichotomy_check(N)
            self.assertAlmostEqual(c_sum.real, r, places=6,
                                   msg=f"F^2 coefficient must be R_Lambda({N})")
            self.assertAlmostEqual(c_sum.imag, 0.0, places=6)
            self.assertLess(abs(c_diff), 1e-10,
                            f"|F|^2 coefficient at N={N} must vanish")

    def test_R_Lambda_small_values(self):
        lam = von_mangoldt_sieve(30)
        # N=10: 3+7, 5+5, 7+3 (primes), plus prime powers: 2+8, 8+2, 4+6(no),
        # 5+5 = log5^2; 3+7 = log3 log7; 2+8 = log2 * log2; also 2^3=8:
        r = R_Lambda(10, lam)
        expect = 2*0.6931*0.6931 + 2*1.0986*1.9459 + 1.6094**2
        self.assertAlmostEqual(r, expect, places=3)


class TestHyperbolaIdentity(unittest.TestCase):
    """BS-G2: mean_G exact two ways."""

    def test_exact(self):
        for X in (150, 400):
            lhs, rhs = hyperbola_identity(X)
            self.assertLess(abs(lhs-rhs), 1e-9*max(1, abs(rhs)),
                            f"hyperbola identity must hold exactly at X={X}")


class TestMeanDictionary(unittest.TestCase):
    """BS-G3 corroboration: the X^{3/2} scale (TESTED MODEL)."""

    def test_track_scale(self):
        rows = mean_G_track([400, 800])
        for (X, err, scale) in rows:
            self.assertLess(abs(err)/scale, 0.5,
                            f"|mean_G - X^2/2| must be < X^1.5/2 at X={X}")


class TestPrimePowerBookkeeping(unittest.TestCase):
    """BS-G4: exact decomposition."""

    def test_N20(self):
        r_pp, r_mix, pairs = prime_power_decomposition(20)
        # hand check: pure pairs (3,17),(7,13),(13,7),(17,3):
        import math
        expect = 2*math.log(3)*math.log(17) + 2*math.log(7)*math.log(13)
        self.assertAlmostEqual(r_pp, expect, places=9)
        self.assertEqual(pairs, 2)
        self.assertGreater(r_mix, 0, "prime-power contamination is nonzero")
        # total consistency
        lam = von_mangoldt_sieve(20)
        self.assertAlmostEqual(r_pp + r_mix, R_Lambda(20, lam), places=9)


if __name__ == "__main__":
    unittest.main()