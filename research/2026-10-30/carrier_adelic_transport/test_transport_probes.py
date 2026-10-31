"""Discover the three separately constructed exact research bearings."""
from adelic_jet_probe import ExactJetTests
from coboundary_probe import Audit
from spectral_source_probe import SpectralSourceTests
from prime_weight_transport_probe import PrimeWeightTests
from fractions import Fraction as F
from unittest import TestCase
from adelic_jet_probe import orbit, secant_bounds

class MovingPrimeFrameTests(TestCase):
    def test_explicit_diagonal_has_summable_rational_error_budget(self):
        budget = F(6853, 54000)
        total_upper = F(0)
        for n in range(1, 7):
            lo, hi = secant_bounds(n, 16 ** n * n ** 2, terms=32)
            u = orbit(n)[-1]
            self.assertGreater(u - hi, 0)
            self.assertLess(u - lo, budget / n ** 2)
            total_upper += u - lo
        self.assertLess(total_upper, 2 * budget)


__all__ = ["ExactJetTests", "Audit", "SpectralSourceTests", "MovingPrimeFrameTests", "PrimeWeightTests"]
