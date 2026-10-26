"""Exact Gamma primitive identities, independent enclosures and hostile gates."""
from fractions import Fraction as Q
import unittest

from observational_succ import bbp_gamma_boundary as g
from observational_succ.bbp_source_memory import forcing, pole_moment


class BBPGammaBoundaryTests(unittest.TestCase):
    def test_log_successor_derivative_recovers_original_source(self):
        for n in (1, 2, 3, 8, 17, 64, 131):
            self.assertEqual(g.gamma_ratio_log_derivative(n-1), 8*forcing(n))

    def test_rational_product_independent_pochhammer_implementation(self):
        for x in (Q(0), Q(2, 3), Q(9, 4)):
            for N in (0, 1, 2, 7, 16):
                factors = []
                for a in (Q(1, 8), Q(1, 2), Q(5, 8), Q(3, 4)):
                    value = Q(1)
                    for j in range(N):
                        value *= x+a+j
                    factors.append(value)
                direct = factors[0]**4/(factors[1]**2*factors[2]*factors[3])
                self.assertEqual(g.gamma_successor_product(x, N), direct)

    def test_successor_product_cocycle(self):
        for x in (Q(0), Q(1, 7), Q(5)):
            for N, M in ((0, 4), (1, 1), (3, 7), (11, 5)):
                self.assertEqual(g.gamma_successor_product(x, N+M),
                                 g.gamma_successor_product(x, N)*
                                 g.gamma_successor_product(x+N, M))

    def test_signed_moments_and_gamma_coefficient(self):
        self.assertEqual(g.source_gamma_moment(0), 0)
        self.assertEqual(g.source_gamma_moment(1), Q(15, 8))
        self.assertEqual(g.source_gamma_moment(2), Q(151, 64))
        for k in range(1, 35):
            self.assertEqual(g.source_gamma_moment(k), 8*pole_moment(k))
            self.assertGreater(g.source_gamma_moment(k), 0)
            self.assertLess(g.source_gamma_moment(k), 4*Q(7, 8)**k)

    def test_coefficient_balance_is_essential(self):
        # Mutating the last coefficient removes the cancellation of the
        # common -gamma term in the digamma readout.
        authentic = (4, -2, -1, -1)
        mutant = (4, -2, -1, 0)
        self.assertEqual(sum(authentic), 0)
        self.assertNotEqual(sum(mutant), 0)
        self.assertNotEqual(sum((Q(c)/(Q(1)+a) for c, a in
                                 zip(mutant, g.HURWITZ_SHIFTS)), Q()),
                            g.gamma_ratio_log_derivative(1))

    def test_ordinary_tail_enclosures_with_deeper_finite_source(self):
        for x in (Q(0), Q(1, 3), Q(6)):
            for N in (1, 4, 15):
                lo, hi = g.ordinary_source_tail_interval(x, N)
                M = 8*N+19
                prefix = sum((g.gamma_ratio_log_derivative(x+j)/8
                              for j in range(M)), Q())
                ml, mh = g.ordinary_source_tail_interval(x, M)
                self.assertLess(prefix, hi)
                self.assertLess(max(lo, ml), min(hi, mh))

    def test_two_log_gamma_enclosures_overlap_and_refine(self):
        previous_width = None
        for N in (8, 16, 32):
            a = g.log_gamma_boundary_series_interval(N, N)
            b = g.compensated_gamma_product_interval(N, N)
            self.assertLess(max(a[0], b[0]), min(a[1], b[1]))
            if previous_width is not None:
                self.assertLess(a[1]-a[0], previous_width)
            previous_width = a[1]-a[0]

    def test_missing_gamma_compensator_is_rejected(self):
        # The omitted (15/8)*gamma is order one, larger than the independent
        # certified widths. This is not a floating-point disagreement.
        a = g.log_gamma_boundary_series_interval(40, 32)
        b = g.compensated_gamma_product_interval(32, 32)
        gl, gh = g.gamma_bounds(32)
        mutant_upper = a[1]-Q(15, 8)*gl
        self.assertLess(mutant_upper, b[0])

    def test_wrong_source_scale_in_zeta_derivative_is_rejected(self):
        a = g.log_gamma_boundary_series_interval(40, 32)
        b = g.source_zeta_zero_derivative_interval(40, 32)
        # Omitting 8^-s in B(s) gives log G(0) rather than B'(0).
        self.assertLess(b[1], a[0])

    def test_ratio_does_not_fix_multiplicative_initial_normalization(self):
        for N in (1, 4, 12):
            p = g.gamma_successor_product(0, N)
            first, changed = p, 7*p
            self.assertNotEqual(first, changed)
            self.assertEqual(changed/first, 7)
            self.assertEqual((7*g.gamma_successor_product(0, N+1))/changed,
                             g.gamma_successor_ratio(N))

    def test_gamma_numeric_readout_is_inside_exact_intervals(self):
        # Independent special-function numerical calibration only; proof
        # authority comes from the paper bounds, not from mpmath.
        import mpmath as mp
        with mp.workdps(65):
            expected = sum((c*mp.loggamma(mp.mpf(a.numerator)/a.denominator)
                            for c, a in zip(g.COEFFICIENTS, g.HURWITZ_SHIFTS)), mp.mpf(0))
            for bounds in (g.log_gamma_boundary_series_interval(40, 32),
                           g.compensated_gamma_product_interval(32, 32)):
                lo, hi = (mp.mpf(v.numerator)/v.denominator for v in bounds)
                self.assertLess(lo, expected)
                self.assertLess(expected, hi)

    def test_exact_receipt_does_not_claim_normality(self):
        result = g.gamma_boundary_receipt(12, 8)
        self.assertEqual(result["M1"], Q(15, 8))
        self.assertEqual(result["log_ratio_derivative0"], 8*Q(47, 15))
        self.assertFalse(result["normality_proved"])
        self.assertFalse(result["new_lean_authority"])

    def test_domain_guards(self):
        for value in (-1, 0.5, True):
            with self.assertRaises(ValueError):
                g.gamma_successor_ratio(value)
        for value in (-1, 1.0, True):
            with self.assertRaises(ValueError):
                g.source_gamma_moment(value)
        for routine in (g.gamma_zeta_series_tail,
                        g.compensated_gamma_product_interval,
                        g.log_gamma_boundary_series_interval):
            with self.assertRaises(ValueError):
                routine(0)


if __name__ == "__main__":
    unittest.main()
