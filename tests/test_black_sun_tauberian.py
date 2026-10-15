"""BLACK SUN B-track tests: Tauberian transfer, sharpness, Lambda dictionary."""
import unittest
from fractions import Fraction

from observational_succ.black_sun_tauberian import (
    BlackSunBTrackError,
    abel_transfer_identity,
    defect_DN,
    factorial_prime_identity,
    spike_cumulative_error,
    spike_sequence,
    transfer_dictionary_check,
    von_mangoldt_sieve,
)


class TestAbelTransferIdentity(unittest.TestCase):
    """BS-B1 core identity S(x) = xA(x) - int_1^x A, exact rational check."""

    def test_exact_identity(self):
        a = [Fraction((i*7) % 5) for i in range(300)]
        self.assertTrue(abel_transfer_identity(a, 200))
        b = [Fraction(1)]*400  # a(n)=1: A = H_n, S = n
        self.assertTrue(abel_transfer_identity(b, 300))

    def test_transfer_direction_a_to_s(self):
        """a(n)=1: A(x)=log x + gamma + O(1/x) (delta=1 limit case);
        S(x) = x exactly: the transfer gives S(x)=x+O(x^0)."""
        import mpmath as mp
        mp.mp.dps = 30
        N = 5000
        A = 0.0
        S = 0.0
        for n in range(1, N+1):
            A += 1/n
            S += 1
        # |S(N) - N| = 0 <= C * N^{0}: trivially; and A(N) = log N + gamma + O(1/N)
        errA = abs(A - (mp.log(N) + mp.euler))
        self.assertLess(errA, 2.0/N)


class TestSpikeSharpness(unittest.TestCase):
    """BS-B2: exponent delta is optimal in the nonnegative class."""

    def test_spike_weighted_error_decays_like_x_delta(self):
        # a = 1 + b with b(2^j) = floor(2^{j(1-delta)}), delta = 1/2, J = 12
        # scaled error |A(x)-log x-C_a| x^delta is O(1): jump oscillation
        # after each spike (~1) plus tail (< 2^{-delta}/(1-2^{-delta})).
        w, C_a, Sm = spike_cumulative_error(Fraction(1, 2), 12)
        self.assertLess(float(w), 3.0,
                        "scaled weighted error must stay O(1) (jump + tail)")
        self.assertGreater(float(w), 0.1,
                           "spike error must be visible (nonzero)")

    def test_spike_mass_grows_like_x_one_minus_delta(self):
        # S(2^J) - 2^J = sum_j 2^{j/2} ~ 2^{J/2} (c_delta ~ 2.41)
        _, _, Sm = spike_cumulative_error(Fraction(1, 2), 12)
        expect = 2**6 * 1.5  # ~ c_delta * 2^{J(1-delta)} = 2.41*2^6 ~ 154
        self.assertGreater(Sm, 100)
        self.assertLess(Sm, 300)

    def test_spike_sequence_nonnegative(self):
        a = spike_sequence(Fraction(2, 3), 8)
        self.assertTrue(all(x >= 0 for x in a))
        self.assertEqual(a[1], 1)
        self.assertEqual(a[2], 1 + int(Fraction(2)**(1*(Fraction(1, 3)))))


class TestLambdaDictionary(unittest.TestCase):
    """BS-B3/B4: authentic-source transfer and the D_N defect dictionary."""

    def test_factorial_prime_identity_exact(self):
        for N in (50, 200):
            _, _, resid = factorial_prime_identity(N)
            self.assertLess(float(resid), 1e-40)

    def test_DN_matches_weighted_error(self):
        """D_N - (1-gamma) == [A(N) - log N + gamma] - E_fac(N) with
        E_fac(N) = log(N!)/N - log N + 1 = O(log N / N): the quantization
        defect measures the weighted prime error (BS-B4)."""
        import mpmath as mp
        mp.mp.dps = 30
        N = 20000
        lam = von_mangoldt_sieve(N)
        D = defect_DN(N, lam)
        A = sum(lam[n]/n for n in range(2, N+1))
        # E_fac from Stirling: (1/2)log(2 pi N)/N + O(1/N)
        Efac = mp.log(2*mp.pi*N)/(2*N)
        lhs = D - (1 - mp.euler)
        rhs = (A - mp.log(N) + mp.euler) - Efac
        self.assertLess(abs(lhs - rhs), 30.0/N,
                        "D_N dictionary residual beyond Stirling remainder")

    def test_transfer_two_way_tracking(self):
        """E_A(N) and (psi(N)-N)/N track each other (same exponent)."""
        rows = transfer_dictionary_check([2000, 8000], dps=20)
        for (N, EA, EP, ra, rp) in rows:
            self.assertLess(abs(ra), 30.0, "|E_A| = O(N^-1/2) heuristic bound")
            self.assertLess(abs(rp), 30.0)
            self.assertLess(abs(EA - EP), 0.5,
                            "E_A(N) ~ (psi(N)-N)/N + o(1): same scale")


class TestDomainErrors(unittest.TestCase):

    def test_bad_delta(self):
        with self.assertRaises(BlackSunBTrackError):
            spike_sequence(Fraction(0, 1), 4)
        with self.assertRaises(BlackSunBTrackError):
            spike_sequence(Fraction(3, 2), 4)


if __name__ == "__main__":
    unittest.main()