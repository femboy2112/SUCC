"""Finite, independent controls for RH–signed Basel research note (not a proof of RH or normality)."""
import cmath
import math
import unittest


def phase(h, n, numerator=1, denominator=37):
    """Exact modular rational phase followed by floating exponential."""
    return cmath.exp(2j * math.pi * ((h * numerator * pow(16, n - 1, denominator)) % denominator) / denominator)


def mel(s):
    x = 2 ** (1 - s)
    return (x - 1) / ((1 - s) * (1 + x))


class SpectralGateControls(unittest.TestCase):
    def test_radix_frequency_shift(self):
        for h in (-7, -1, 1, 5):
            for n in range(1, 41):
                self.assertAlmostEqual(abs(phase(16 * h, n) - phase(h, n + 1)), 0, places=13)

    def test_discrete_dirichlet_shift_with_endpoint(self):
        N, h, s = 111, 3, 1.37 + 0.41j
        lhs = sum(phase(16 * h, n) / (n ** s) for n in range(1, N + 1))
        lhs -= sum(phase(h, n) / (n ** s) for n in range(1, N + 1))
        rhs = -phase(h, 1) + sum(phase(h, n) * ((n - 1) ** (-s) - n ** (-s)) for n in range(2, N + 1))
        rhs += phase(h, N + 1) * N ** (-s)
        self.assertLess(abs(lhs - rhs), 2e-13)

    def test_log_block_counterexample_epoch(self):
        for k in range(1, 10):
            A = 2 ** k
            terms = [(-1) ** (n.bit_length() - 1) for n in range(A, 2 * A)]
            self.assertEqual(sum(terms), A * (-1) ** k)

    def test_mellin_block_formula(self):
        self.assertAlmostEqual(mel(2), 1 / 3, places=14)
        for s in (1.2, 1.8, 2.4):
            brute = sum((-1) ** k * (2 ** ((k + 1) * (1 - s)) - 2 ** (k * (1 - s))) / (1 - s)
                        for k in range(400))
            self.assertAlmostEqual(mel(s), brute, places=12)

    def test_mellin_regular_at_one(self):
        target = math.log(2) / 2
        for eps in (1e-3, 2e-4):
            self.assertLess(abs(mel(1 + eps) - target), eps ** 2)

    def test_mellin_nonreal_boundary_poles(self):
        # Denominator 1+2^(1-s) vanishes at 1 + (2k+1) pi i / log 2.
        for k in (-2, -1, 0, 1):
            s = 1 + 1j * (2 * k + 1) * math.pi / math.log(2)
            self.assertLess(abs(1 + 2 ** (1 - s)), 3e-14)
            self.assertGreater(abs(2 ** (1 - s) - 1), 1.99)

    def test_coherent_wrong_seed(self):
        for h in (-1, 1, 8):
            for A in (13, 127, 509):
                # Selected coherent wrong seed s=-pi/16 gives completed Y_n=0.
                numerator = sum(cmath.exp(2j * math.pi * h * 0) / n ** 2 for n in range(A, 2 * A))
                denominator = sum(1.0 / n ** 2 for n in range(A, 2 * A))
                self.assertAlmostEqual(abs(numerator / denominator - 1), 0, places=13)

    def test_rational_fixed_phase_counterexample(self):
        # 16=1 mod 3: a_n(1,1/3) is constant and cannot satisfy Weyl decay.
        vals = [phase(1, n, 1, 3) for n in range(1, 21)]
        self.assertLess(max(abs(v - vals[0]) for v in vals), 1e-13)
        self.assertAlmostEqual(abs(sum(vals) / len(vals)), 1.0, places=13)


if __name__ == "__main__":
    unittest.main()
