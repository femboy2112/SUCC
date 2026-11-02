"""Focused root-discoverable tests for the additive Gamma-Haar research route."""
import importlib.util
from fractions import Fraction
from pathlib import Path
import unittest

BASE = Path(__file__).resolve().parents[1]/"research"/"2026-11-02"/"gamma_haar_window"


def load(name, file):
    spec = importlib.util.spec_from_file_location(name, BASE/file)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


g = load("succ_gamma_haar_exact", "gamma_haar.py")


class GammaHaarWindowTests(unittest.TestCase):
    def test_four_source_presentations(self):
        for n in range(1, 301):
            self.assertEqual(g.source(n), g.source_independent_polynomial(n))
            self.assertEqual(g.source(n), g.source_from_laplace(n))
            self.assertEqual(g.source(n), g.source_gamma_ratio_derivative(n))

    def test_positive_kernel_factorization(self):
        self.assertEqual(g.laplace_polynomial_coefficients(), (4, 0, 0, -2, -1, -1))
        self.assertEqual(g.source(1), Fraction(47, 15))

    def test_tail_bracket_against_exact_prefix_increments(self):
        for M in range(31):
            low, high = g.gamma_tail_bracket(M)
            finite = g.bbp_alpha_partial(M+30)-g.bbp_alpha_partial(M)
            self.assertGreater(finite, low)
            self.assertLess(finite, high)

    def test_actual_unwrapped_zero_seed(self):
        U = g.original_states(48)
        a = g.bbp_alpha_partial(48)
        for n in range(1, 49):
            self.assertEqual(16**n*a-U[n-1], g.exact_finite_future(n, 48))

    def test_weighted_gamma_lag(self):
        U = [Fraction()]+g.original_states(64)
        for n in (0, 1, 2, 9, 16, 31):
            for k in (0, 1, 2, 4, 8):
                self.assertEqual(U[n+k]-16**k*U[n], g.gamma_weighted_lag(n, k))

    def test_summable_total_window_precision(self):
        for M in (1, 2, 16, 64):
            for h in (1, 3, 7):
                fact = g.gamma_tail_l1_fourier_error_upper(h, M)
                self.assertLess(fact, Fraction(32*h,15*(8*M+1)*(8*M+2)))

    def test_haar_energy_and_coherent_control(self):
        for L in (1, 2, 4, 8, 16):
            child, difference, parent = g.dyadic_level_energy([1+0j]*32,L)
            self.assertEqual(difference,0)
            self.assertEqual(parent,2*child)
        self.assertLess(g.certified_dyadic_bound(256, 16, 0.25), 1)
        self.assertGreater(g.mean_prefix_bound(256,16,0.25),0)

    def test_rational_machin_interval(self):
        c = load("succ_gamma_haar_certificate", "finite_certificate.py")
        lo, hi = c.pi_interval()
        self.assertLess(Fraction(3),lo)
        self.assertLess(hi,Fraction(22,7))
        re, im, error = c.rational_trig_approx(Fraction(1,4))
        self.assertLessEqual(abs(re),error)
        self.assertLessEqual(abs(im-1),error)

    def test_original_finite_signed_certificate(self):
        c = load("succ_gamma_haar_certificate_again", "finite_certificate.py")
        result = c.check_gamma_haar(1,64)
        self.assertTrue(result["pass_all"])
        self.assertEqual([x["L"] for x in result["levels"]],[16,32])


if __name__ == "__main__":
    unittest.main()
