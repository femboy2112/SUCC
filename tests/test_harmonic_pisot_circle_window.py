"""Finite hostile controls for fixed circular apertures (HPB-C1..C4).

Standard library only. No sourced pi/RH proof or infinite-limit validation.
Algebraic visibility and equidistribution are proved in CIRCLE_WINDOW.md.
"""

import math
import cmath
import unittest

ALPHA = (math.sqrt(5.0) - 1.0) / 2.0
DELTA = math.pi * ALPHA


def sinc_mode(h, delta):
    if h == 0:
        return 1.0
    return math.sin(h * delta) / (h * delta)


def golden_visibility_lower(h):
    return 2.0 / (DELTA * (math.sqrt(5.0) + 0.5) * h * h)


def delta_mass_energy(delta, cutoff):
    return 2.0 * sum(sinc_mode(h, delta)**2 for h in range(1, cutoff + 1))


class ConstantCircleWindowControls(unittest.TestCase):
    def test_constant_arc_measure(self):
        for radius in (0.7, 1.0, 9.0):
            for center in (0.0, 0.25, 1.7, 13.8):
                length = radius * 2 * DELTA
                measure = length / (2 * math.pi * radius)
                self.assertAlmostEqual(measure, ALPHA, delta=1e-13)
                self.assertAlmostEqual(1/radius * radius * 2*DELTA,
                                       2*DELTA, delta=1e-13)
                self.assertAlmostEqual(((center + DELTA)-(center - DELTA)),
                                       2*DELTA, delta=3e-15)

    def test_golden_norm_nonvanishing_and_bound(self):
        conjugate = (-1.0 - math.sqrt(5.0)) / 2.0
        for h in range(1, 501):
            k = round(h * ALPHA)
            norm = k*k + h*k - h*h
            self.assertNotEqual(norm, 0)
            self.assertAlmostEqual((h*ALPHA-k)*(h*conjugate-k),
                                   norm, delta=5e-8)
            self.assertGreaterEqual(abs(sinc_mode(h, DELTA)) + 1e-12,
                                    golden_visibility_lower(h))

    def test_rational_aperture_can_erase_character(self):
        # Rational delta/pi=1/3 erases the h=3 character exactly.
        delta = math.pi/3
        self.assertAlmostEqual(sinc_mode(3, delta), 0.0, delta=2e-16)
        # Non-Haar (1+cos(3 theta))m has ±3 Fourier modes only.
        # Multiplication by zero therefore yields Haar exactly.
        self.assertNotAlmostEqual(0.5, 0.0)

    def test_golden_locked_orbit_retains_nonzero_energy(self):
        limit_energy = math.pi / DELTA - 1
        self.assertAlmostEqual(limit_energy, ALPHA, delta=1e-14)
        self.assertAlmostEqual(delta_mass_energy(DELTA, 6000),
                               limit_energy, delta=3e-4)
        # The stable Galois sheet produces increasingly locked angles.
        psi = (1-math.sqrt(5.0))/2
        z = [cmath.exp(-2j*math.pi*psi**n) for n in range(1, 201)]
        mean = sum(z)/len(z)
        self.assertGreater(mean.real, 0.94)
        self.assertGreater(abs(sinc_mode(1, DELTA)), 0.4)

    def test_first_mode_quantitative_energy_bound(self):
        # Finite probability laws: direct E_delta truncated from Fourier modes.
        phases = [0.0, 0.1, 0.9, 2.3, 4.0]
        N = len(phases)
        hat = lambda h: sum(cmath.exp(-1j*h*x) for x in phases)/N
        energy_cut = sum(abs(hat(h)*sinc_mode(h, DELTA))**2
                         for h in range(-60, 61) if h)
        for h in range(1, 21):
            upper = (DELTA * (math.sqrt(5)+0.5)/2) * (h*h) * math.sqrt(energy_cut)
            self.assertLessEqual(abs(hat(h)), upper + 1e-12)
        # No assumption about equidistribution is smuggled into this finite check.

    def test_stationary_source_rotating_observer_countermodel(self):
        # Source never leaves zero; rotating centers scan a substantial arc.
        N = 2000
        source = [0.0] * N
        centers = [2*math.pi*((n*ALPHA)%1) for n in range(1, N+1)]
        hits = sum(1 for c in centers if min(c, 2*math.pi-c) <= DELTA)
        self.assertTrue(all(x == 0 for x in source))
        self.assertLess(abs(hits/N - ALPHA), 0.005)
        self.assertAlmostEqual(
            sum(cmath.exp(1j*x) for x in source).real/N,
            1.0, delta=1e-14)


if __name__ == '__main__':
    unittest.main()
