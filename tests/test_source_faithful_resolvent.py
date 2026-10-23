"""Independent rational fiber and interval-frequency checks of memory bounds."""
from fractions import Fraction as Q
import unittest

from observational_succ.source_faithful_resolvent import (
    ResolventSourceError, radix_two_schur, uniform_band_budget,
)


def atan_bracket(x, terms=32):
    """Test-local alternating oracle; used only at rational 0<=x<=1/2."""
    assert 0 <= x <= Q(1, 2)
    s = sum(((-1)**j*x**(2*j+1)/(2*j+1) for j in range(terms)), Q(0))
    delta = (-1)**terms*x**(2*terms+1)/(2*terms+1)
    return min(s, s+delta), max(s, s+delta)


class ResolventMemoryTests(unittest.TestCase):
    def test_independent_two_by_two_inverse_in_original_residue_basis(self):
        for alpha in (Q(1, 2), Q(1), Q(3)):
            for h in (Q(1), Q(1, 2), Q(1, 8)):
                for c, sine in ((Q(1), Q(0)), (Q(0), Q(1)),
                                (Q(3, 5), Q(4, 5)), (Q(-3, 5), Q(4, 5)),
                                (Q(-1), Q(0))):
                    self.assertEqual(c*c+sine*sine, 1)
                    diagonal = alpha+2/h**2
                    offdiag_norm = ((1+c)**2+sine*sine)/h**4
                    determinant = diagonal**2-offdiag_norm
                    # u*(alpha+L)^-1 u from the residue-basis adjugate.
                    independent = (diagonal+(1+c)/h**2)/determinant
                    cert = radix_two_schur(alpha, h, c)
                    self.assertEqual(cert["visible_resolvent"], independent)

    def test_memory_is_positive_and_its_omission_is_detected(self):
        for c in (Q(-3, 5), Q(0), Q(3, 5)):
            cert = radix_two_schur(1, Q(1, 4), c)
            self.assertGreater(cert["memory_correction"], 0)
            self.assertGreater(cert["visible_resolvent"], cert["forgotten_memory_resolvent"])
        self.assertEqual(radix_two_schur(1, 1, 1)["memory_correction"], 0)
        self.assertEqual(radix_two_schur(1, 1, -1)["memory_correction"], 0)

    def test_zero_frequency_exact_resolvent(self):
        for alpha in (Q(1, 3), Q(2), Q(5)):
            for h in (Q(1, 2), Q(1, 17)):
                self.assertEqual(radix_two_schur(alpha, h, 1)["visible_resolvent"], 1/alpha)

    def test_quantitative_band_theorem_against_rational_phase_intervals(self):
        # z=(1+i*h)/(1-i*h), theta=2 atan(h), xi=atan(h)/h lies in (0,1).
        for h in (Q(1, 4), Q(1, 8), Q(1, 16)):
            c = (1-h*h)/(1+h*h)
            theta_lo, theta_hi = atan_bracket(h)
            xi2_lo, xi2_hi = (theta_lo/h)**2, (theta_hi/h)**2
            budget = uniform_band_budget(2, h, 1, Q(1, 2), 3)
            for alpha in (Q(1, 2), Q(1), Q(3)):
                cert = radix_two_schur(alpha, h, c)
                continuum_lo = 1/(alpha+xi2_hi)
                continuum_hi = 1/(alpha+xi2_lo)
                error = max(abs(cert["visible_resolvent"]-continuum_lo),
                            abs(cert["visible_resolvent"]-continuum_hi))
                self.assertLessEqual(error, budget["resolvent_error_upper"])
                memory_error = max(abs(cert["memory_correction"]-xi2_lo),
                                   abs(cert["memory_correction"]-xi2_hi))
                self.assertLessEqual(memory_error, budget["memory_error_upper"])

    def test_all_radix_budgets_scale_quadratically(self):
        for radix in (1, 2, 3, 5, 7, 11):
            first = uniform_band_budget(radix, Q(1, 10*radix), 2, Q(1, 2), 3)
            second = uniform_band_budget(radix, Q(1, 20*radix), 2, Q(1, 2), 3)
            for key in first:
                self.assertEqual(first[key], 4*second[key])

    def test_unbounded_alpha_counterexample_to_uniform_memory_limit(self):
        # alpha=h^-4 kills the correction even while physical xi approaches 1.
        for h in (Q(1, 4), Q(1, 8), Q(1, 16)):
            c = (1-h*h)/(1+h*h)
            cert = radix_two_schur(h**-4, h, c)
            self.assertLessEqual(cert["memory_correction"], 4*h*h)
            angle_lo, _ = atan_bracket(h)
            self.assertGreater((angle_lo/h)**2, Q(9, 10))

    def test_off_axis_and_unresolved_band_inputs_rejected(self):
        for bad in (1.0, True, "1"):
            with self.assertRaises(ResolventSourceError):
                radix_two_schur(bad, 1, 0)
        with self.assertRaises(ResolventSourceError):
            radix_two_schur(1, 1, 2)
        with self.assertRaises(ResolventSourceError):
            uniform_band_budget(3, 1, 10, 1, 2)
        with self.assertRaises(ResolventSourceError):
            uniform_band_budget(2, Q(1, 8), 1, 2, 1)


if __name__ == "__main__":
    unittest.main()
