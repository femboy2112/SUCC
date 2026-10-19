"""Independent exact controls for source-authentic Gamma tail improvements."""
from fractions import Fraction as Q
import tempfile
from pathlib import Path
import unittest

from scripts import institute_schur_probe as G


class GammaMidpointCertificate(unittest.TestCase):
    def test_all_y_log_bound_has_exact_critical_point_certificate(self):
        data = G.logarithm_linear_certificate()
        self.assertGreater(data["positive_local_minimum_margin"], Q(1, 100))
        self.assertEqual(data["constant"], Q(13, 16))
        # Sharpening the coefficient to 4/5 is actually FALSE at y=2.
        lower, _ = G.log_interval(Q(5))
        self.assertGreater(lower, Q(8, 5))

    def test_independent_prefix_integral_oracle(self):
        for J in (1, 3, 9, 31):
            for x in (Q(1, 13), Q(3, 2), Q(17), Q(500)):
                lo, hi = G.independent_tail_interval(J, x, prefix=1024)
                a, b = G.logarithmic_envelope(J, x)
                self.assertGreaterEqual(lo, a)
                self.assertLessEqual(hi, b)
                coeff = G.gamma_coefficients(J)
                self.assertLessEqual(hi, coeff["new_H1"] * x)
                self.assertLessEqual(hi, coeff["selected_H2"] * x * x)

    def test_true_source_coefficients_improve_with_one_exception_preserved(self):
        for J in (1, 2, 8, 24, 10000):
            data = G.gamma_coefficients(J)
            self.assertLess(data["new_H1"], data["old_H1"])
            self.assertLessEqual(data["selected_H2"], data["old_H2"])
            if J > 1:
                self.assertLess(data["midpoint_H2"], data["old_H2"])
        self.assertGreater(G.gamma_coefficients(1)["midpoint_H2"],
                           G.gamma_coefficients(1)["old_H2"])

    def test_wrong_unshifted_upper_is_refuted(self):
        # Monotonicity makes the d-centered integral a LOWER, never an upper.
        true_lower, _ = G.independent_tail_interval(8, Q(7))
        _, mutant_upper = G.log_interval(1 + Q(196, 33 * 33))
        self.assertGreater(true_lower, mutant_upper / 2)
        # Even a shift of one, instead of the theorem's two, is too small.
        low, _ = G.independent_tail_interval(8, Q(1, 100))
        _, mutant = G.log_interval(1 + 4 * Q(1, 100)**2 / 32**2)
        self.assertGreater(low, mutant / 2)

    def test_coarse_oracle_upper_does_not_refute_a_tighter_true_upper(self):
        lo, hi = G.independent_tail_interval(31, Q(500), prefix=96)
        _, proved_upper = G.logarithmic_envelope(31, Q(500))
        self.assertLess(lo, proved_upper)
        self.assertGreater(hi, proved_upper)
        _, refined_hi = G.independent_tail_interval(31, Q(500), prefix=1024)
        self.assertLess(refined_hi, proved_upper)

    def test_original_source_and_wrong_gamma_mutation(self):
        self.assertEqual(G.source_identity()["git_blob"], G.SOURCE_BLOB)
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp) / G.SOURCE_PATH
            target.parent.mkdir(parents=True)
            target.write_text("d_j = 8*j + 1  # wrong real Gamma spacing\n")
            with self.assertRaisesRegex(ValueError, "blob mismatch"):
                G.source_identity(tmp)

    def test_reject_inexact_and_illegal_domains(self):
        for bad in (0, -1, True, 1.5, Q(2)):
            with self.assertRaises(ValueError):
                G.gamma_coefficients(bad)
        for bad in (True, 1.25, "3"):
            with self.assertRaises(ValueError):
                G.log_interval(bad)


if __name__ == "__main__":
    unittest.main()
