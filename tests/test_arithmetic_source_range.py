"""Fast exact controls; numerical checks are not analytic proof certificates."""
from fractions import Fraction as F
import unittest

from observational_succ import arithmetic_source_range as R


class ExactSourceRangeControls(unittest.TestCase):
    def test_source_pin_and_authority(self):
        s = R.source_snapshot()
        self.assertEqual(s["source_git_blob"], R.SOURCE_BLOB)
        self.assertEqual(s["origin_commit"], R.SOURCE_COMMIT)
        self.assertFalse(s["original_weil_sign_proved"])

    def test_primitive_endpoint_and_moment_transport(self):
        for n in (5, 6, 9, 12):
            with self.subTest(n=n):
                r = R.primitive_control(n)
                self.assertEqual(r["primitive_endpoints"], (0, 0))
                self.assertEqual(r["u_moments_through_4"], (0,)*5)
                self.assertEqual(r["primitive_moments_through_3"], (0,)*4)
                self.assertGreater(r["K_energy"], 0)

    def test_gamma_primitive_ibp_exact_in_exponential_basis(self):
        for n in (5, 6, 9):
            for j in (0, 1, 7):
                with self.subTest(n=n, j=j):
                    r = R.gamma_primitive_identity(n, j)
                    self.assertEqual(r["difference_affine"], (0, 0))

    def test_nonzero_boundary_terms_cannot_be_dropped(self):
        for j in (0, 1, 7):
            r = R.gamma_primitive_identity(rung=j, boundary_mutant=True)
            self.assertEqual(r["endpoints"], (1, 1))
            self.assertNotEqual(r["difference_affine"], (0, 0))

    def test_multiplier_even_and_zero_frequency(self):
        for xi in (F(0), F(1, 3), F(3), F(17)):
            p = R.gamma_multiplier_enclosure(xi)
            q = R.gamma_multiplier_enclosure(-xi)
            self.assertEqual(p["lower"], q["lower"])
            self.assertEqual(p["upper"], q["upper"])
        p = R.gamma_multiplier_enclosure(0)
        self.assertEqual((p["lower"], p["upper"]), (0, 0))

    def test_whole_tower_bound_contains_independent_finite_extension(self):
        for xi in (F(1, 8), F(2), F(37)):
            p = R.gamma_multiplier_enclosure(xi, 8)
            # Independent algebraic arrangement of each Fourier transform term.
            longer = sum((F(4, 4*j+1)-F(4*j+1)/
                          (F((4*j+1)**2, 4)+xi*xi) for j in range(256)), F())
            self.assertLessEqual(p["lower"], longer)
            self.assertLessEqual(longer, p["upper"])
            refined = R.gamma_multiplier_enclosure(xi, 64)
            self.assertLess(refined["tail_upper"], p["tail_upper"])

    def test_log_band_growing_lower_bound(self):
        previous = F()
        for n in (1, 4, 16, 64, 256):
            row = R.logarithmic_band_lower(n)
            actual = R.gamma_multiplier_enclosure(row["frequency"], n)
            self.assertGreater(row["lower"], previous)
            self.assertGreater(actual["lower"], row["lower"])
            previous = row["lower"]

    def test_invalid_exact_input_rejected(self):
        for x in (True, 1.0, "1"):
            with self.assertRaises(R.SourceRangeError):
                R.gamma_multiplier_enclosure(x)
        for n in (True, 0, 4097):
            with self.assertRaises(R.SourceRangeError):
                R.gamma_multiplier_enclosure(1, n)

    def test_no_fractional_or_sign_promotion(self):
        c = R.claim_boundaries()
        self.assertIn("OPEN", c["fractional_D_power_above_half"])
        self.assertIn("CONDITIONAL", c["dense_range"])
        self.assertFalse(c["strong_H01_annihilator_regularity_assumed"])
        self.assertFalse(c["RH_PROVED"])
        self.assertFalse(c["kernel_proof"])


class NumericalInstrumentControls(unittest.TestCase):
    def test_full_source_derivative_inside_existing_rational_boxes(self):
        from observational_succ.signed_gprime_enclosure import original_derivative_interval
        for r in (F(1, 16), F(1, 4), F(3, 5), F(4, 5), F(15, 16)):
            lo, hi = original_derivative_interval(r, r)
            # Float evaluation is checked against a genuine interval with a
            # declared floating tolerance; this does not widen the proof box.
            value = R.numerical_gprime(r)
            self.assertLessEqual(float(lo)-2e-14, value)
            self.assertLessEqual(value, float(hi)+2e-14)
            self.assertEqual(R.numerical_gprime(-r), -value)

    def test_gamma_geometric_sum_and_carleman_majorant(self):
        from math import exp
        for r in (.01, .1, .7, 2., 10.):
            exact_expression = R.numerical_gamma_offdiagonal(r)
            finite = sum(exp(-(4*j+1)*r/2) for j in range(4096))
            self.assertAlmostEqual(finite, exact_expression, delta=2e-12)
            self.assertLess(exact_expression, 1.5/r)

    def test_diagonal_and_domain_are_not_regularized_silently(self):
        for x in (0, 1.01, float("nan"), float("inf")):
            with self.assertRaises(R.SourceRangeError):
                R.numerical_gprime(x)

    def test_complex_weighted_adjoint_and_wrong_conjugation_mutant(self):
        try:
            import numpy as np
        except ImportError:
            self.skipTest("optional numpy unavailable")
        kernel = np.array([[1+2j, -2+3j], [4-1j, 2j]])
        weights = np.array([.25, .75])
        op = kernel*weights[None, :]
        adj = R.weighted_adjoint(kernel, weights)
        u, v = np.array([1+2j, 3-1j]), np.array([2-3j, -1+4j])
        inner = lambda a, b: np.sum(weights*a*b.conj())  # Linear first.
        self.assertAlmostEqual(inner(op@u, v), inner(u, adj@v))
        mutant = kernel.T*weights[None, :]
        self.assertGreater(abs(inner(op@u, v)-inner(u, mutant@v)), 1.)

    def test_actual_odd_kernel_has_negative_adjoint_and_reverses_parity(self):
        try:
            import numpy as np
        except ImportError:
            self.skipTest("optional numpy unavailable")
        x = np.array([-.43, -.19, .19, .43])
        w = np.array([.2, .3, .3, .2])
        # This isolated sampled control omits diagonal entries. It is not
        # a discretization of the singular integral or a range computation.
        kernel = np.array([[0. if a == b else R.numerical_gprime(a-b)
                            for b in x] for a in x])
        op = kernel*w[None, :]
        self.assertTrue(np.array_equal(R.weighted_adjoint(kernel, w), -op))
        reflection = np.eye(4)[::-1]
        self.assertLess(np.max(abs(op@reflection+reflection@op)), 1e-15)


if __name__ == "__main__":
    unittest.main()
