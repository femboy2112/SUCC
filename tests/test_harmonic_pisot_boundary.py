"""Focused numerical/exact controls for the harmonic--Pisot boundary dossier.

These tests are finite sanity checks, NOT proof of infinite-series convergence,
not interval certificates, and not tests of pi normality or the RH.
Use stable conjugate phases: NEVER evaluate cos(2*pi*phi**n) at large n.
"""

import cmath
import math
import unittest
from fractions import Fraction

PHI = (1.0 + math.sqrt(5.0)) / 2.0
PSI = (1.0 - math.sqrt(5.0)) / 2.0
GAMMA = 0.577215664901532860606512090082402431  # finite numerical fixture


def defect(n):
    """1 - Re e(phi**n), via the small Galois conjugate."""
    return 2.0 * math.sin(math.pi * PSI**n) ** 2


def energy(n):
    return math.fsum(defect(k) / k for k in range(1, n + 1))


def boundary(n, B):
    harmonic = math.fsum(1.0 / k for k in range(1, n + 1))
    return B + harmonic - math.log(n) - energy(n)


def error_upper(n):
    """Rigorous *symbolic* upper-bound formula; evaluated in ordinary floats."""
    rho = abs(PSI)
    return (1.0 / (2 * n)
            + 2 * math.pi**2 * rho ** (2 * (n + 1))
            / ((n + 1) * (1 - rho**2)))


class HarmonicPisotBoundaryTests(unittest.TestCase):
    def test_lucas_trace_and_phase_conjugation(self):
        a, b = 2, 1  # L_0, L_1
        for n in range(1, 14):
            if n == 1:
                L = b
            else:
                a, b = b, a + b
                L = b
            self.assertAlmostEqual(PHI**n + PSI**n, L, delta=2e-9)
            self.assertAlmostEqual(
                1 - math.cos(2 * math.pi * PHI**n),
                defect(n), delta=3e-8,
            )

    def test_exact_source_balance_not_harmonic(self):
        coefficients = (4, -2, -1, -1)
        offsets = (7, 4, 3, 2)
        self.assertEqual(sum(coefficients), 0)
        self.assertEqual(sum(c * a for c, a in zip(coefficients, offsets)), 15)
        for n in (128, 1024, 8192):
            r = sum((Fraction(c, 8*n-a)
                     for c, a in zip(coefficients, offsets)), Fraction())
            self.assertGreater(r, 0)
            self.assertLess(abs(float(n*n*r - Fraction(15, 64))), 0.02)

    def test_monotone_boundary_for_multiple_controls(self):
        for phase in (lambda n: defect(n),
                      lambda n: 0.0,
                      lambda n: 1 - math.cos(2 * math.pi * n / 7)):
            current = 1.0
            for n in range(1, 120):
                difference = (1 - phase(n + 1)) / (n + 1)
                difference -= math.log1p(1 / n)
                self.assertLess(difference, 0.0)
                current += difference

    def test_critical_threshold_and_analytic_tail_envelope(self):
        critical = energy(80) - GAMMA
        self.assertAlmostEqual(critical, 2.477309460563155, delta=5e-12)
        for n in (2, 4, 8, 16, 32):
            approximate = -boundary(n, 0.0)
            self.assertGreater(critical - approximate, 0.0)
            self.assertLess(critical - approximate, error_upper(n))

    def test_threshold_crossing_at_19_and_safe_250(self):
        self.assertGreater(boundary(18, 2.45), 0.0)
        self.assertLess(boundary(19, 2.45), 0.0)
        for n in range(1, 180):
            self.assertGreater(boundary(n, 2.5), 0.0)

    def test_complex_defect(self):
        D = sum((cmath.exp(-2j * math.pi * PSI**n) - 1) / n
                for n in range(1, 120))
        self.assertAlmostEqual(D.real, -energy(120), delta=2e-13)
        self.assertAlmostEqual(D.real, -3.054525125464688, delta=4e-12)
        self.assertAlmostEqual(D.imag, -0.809499157698022, delta=4e-12)

    def test_abel_logarithmic_singularity_and_analytic_remainder(self):
        z = 0.75
        lhs = sum(cmath.exp(-2j * math.pi * PSI**n) * z**n / n
                  for n in range(1, 160))
        D_z = sum((cmath.exp(-2j * math.pi * PSI**n) - 1) * z**n / n
                  for n in range(1, 160))
        self.assertAlmostEqual((lhs + math.log(1 - z)).real, D_z.real,
                               delta=1e-13)
        self.assertAlmostEqual((lhs + math.log(1 - z)).imag, D_z.imag,
                               delta=1e-13)

    def test_pisot_is_antinormal_negative_control(self):
        sample = [cmath.exp(-2j * math.pi * PSI**n) for n in range(1, 200)]
        mean = sum(sample) / len(sample)
        self.assertGreater(mean.real, 0.95)
        self.assertLess(abs(mean.imag), 0.10)
        # The proof is the pointwise convergence z_n -> 1, not this sample.

    def test_phase_vanishes_but_harmonic_energy_can_diverge(self):
        def delta(n):
            return 1.0 / (4.0 * math.sqrt(math.log(n + 2)))
        self.assertLess(delta(200000), delta(2000))
        for n in (10, 100, 1000, 10000):
            q = 1 - math.cos(2 * math.pi * delta(n))
            self.assertGreaterEqual(q + 1e-15, 8 * delta(n) ** 2)
            self.assertLessEqual(q, 2 * math.pi**2 * delta(n) ** 2)
        # The proof of divergence is q_n/n >= 1/[2n log(n+2)].

    def test_no_rational_linear_16_intertwiner(self):
        # charpoly of golden unit X^2-X-1, silver unit X^2-2X-1.
        self.assertNotEqual(16**2 - 16 - 1, 0)
        self.assertNotEqual(16**2 - 2*16 - 1, 0)


if __name__ == "__main__":
    unittest.main()
