"""Exact finite controls for the common beta source and BBP/Euler bridge."""
from fractions import Fraction as Q
from math import comb, factorial
import unittest

from observational_succ.bbp_natural_carrier import exact_forcing
from observational_succ.euler_mascheroni_succ import gamma_bounds, harmonic_prefix, rational_log_bounds
from observational_succ.exponential_gamma_bridge import (
    UPPER_BRIDGE_SHIFTED_COEFFICIENTS, bbp_euler_asymptotic_coefficients,
    bbp_euler_tail_bridge, euler_remainder_interval, finite_beta_fixed_point_interval,
    finite_beta_laplace_interval, finite_beta_log_mean_interval,
    finite_beta_mellin_successor, finite_beta_moment, finite_beta_survival,
    golden_gamma_offset_interval, golden_laplace_fixed_point_interval,
    upper_bridge_polynomial_certificate,
)


class ExponentialGammaBridgeTests(unittest.TestCase):
    def test_beta_moments_against_independent_polynomial_integrals(self):
        for m in range(1, 10):
            for k in range(9):
                # Expand (1-x/m)^(m-1), then integrate x^k on [0,m].
                direct = sum((Q((-1)**j*comb(m-1, j)*m**(k+1), k+j+1)
                              for j in range(m)), Q())
                self.assertEqual(finite_beta_moment(m, k), direct)
            self.assertEqual(finite_beta_moment(m, 0), 1)
            self.assertEqual(finite_beta_survival(m, 0), 1)
            self.assertEqual(finite_beta_survival(m, m), 0)

    def test_finite_mellin_successor_and_moment_error_bound(self):
        for m in (1, 2, 7, 31, 127):
            for k in range(1, 12):
                self.assertEqual(finite_beta_moment(m, k)/finite_beta_moment(m, k-1),
                                 finite_beta_mellin_successor(m, k-1))
                ratio = finite_beta_moment(m, k)/factorial(k)
                self.assertLess(ratio, 1)
                self.assertLessEqual(1-ratio, Q(k*(k+1), 2*m))
                self.assertLess(finite_beta_moment(m, k), finite_beta_moment(m+1, k))

    def test_survival_constructs_e_inverse_monotonically(self):
        last = Q(0)
        for m in (2, 3, 4, 8, 16, 32, 64):
            value = finite_beta_survival(m, 1)
            self.assertGreater(value, last)
            # Independent alternating-series enclosure of exp(-1).
            lo = sum((Q((-1)**j, factorial(j)) for j in range(14)), Q())
            hi = lo+Q(1, factorial(14))
            self.assertLess(value, lo)
            self.assertLess(hi-value, Q(1, m))
            last = value

    def test_log_mean_uses_no_gamma_input_and_converges_with_known_debt(self):
        g0, g1 = gamma_bounds(1024, 32)
        for m in (1, 2, 7, 31, 127):
            got = finite_beta_log_mean_interval(m, 32)
            l0, l1 = rational_log_bounds(m, 32)
            h = harmonic_prefix(m)
            self.assertEqual((got.lower, got.upper), (l0-h, l1-h))
            remainder = euler_remainder_interval(m)
            # log mean = -gamma - epsilon_m, a different limiting observable.
            self.assertLess(got.lower, -g0)
            self.assertGreater(got.upper, -g1-remainder.upper)
            self.assertLess(got.lower, -g0-remainder.lower)

    def test_laplace_brackets_against_independent_uniform_density(self):
        for s in (Q(1, 4), Q(3, 5), Q(1), Q(3)):
            # m=1 is uniform(0,1): L_1(s)=(1-exp(-s))/s.
            low_exp = sum(((-s)**j/Q(factorial(j)) for j in range(42)), Q())
            high_exp = low_exp+(-s)**42/Q(factorial(42))
            exact_lo, exact_hi = (1-high_exp)/s, (1-low_exp)/s
            got = finite_beta_laplace_interval(1, s, 64)
            self.assertLessEqual(exact_lo, got.lower)
            self.assertLessEqual(got.upper, exact_hi)
        self.assertEqual(finite_beta_laplace_interval(17, 0).lower, 1)

    def test_common_source_coupling_bounds_laplace_error(self):
        for m in (1, 2, 8, 37, 128):
            for s in (Q(1, 4), Q(3, 5), Q(1)):
                got = finite_beta_laplace_interval(m, s, 128)
                limit = 1/(1+s)
                self.assertGreater(got.lower, limit)
                self.assertLess(got.upper-limit, s/(m+1))

    def test_golden_fixed_point_and_finite_source_root(self):
        golden = golden_laplace_fixed_point_interval(64)
        self.assertLess(golden.lower**2+golden.lower, 1)
        self.assertGreater(golden.upper**2+golden.upper, 1)
        self.assertEqual(golden.width, Q(1, 2**64))
        last = Q(1)
        for m in (1, 2, 8, 32, 128):
            fixed = finite_beta_fixed_point_interval(m, bits=28)
            self.assertGreater(fixed.lower, golden.upper)
            self.assertLess(fixed.upper, last)
            self.assertLess(fixed.upper-golden.lower, golden.upper/(m+1))
            self.assertLess(finite_beta_laplace_interval(m, fixed.upper).upper, fixed.upper)
            self.assertGreater(finite_beta_laplace_interval(m, fixed.lower).lower, fixed.lower)
            last = fixed.lower

    def test_canonical_offset_enclosed_but_reference_cancels_from_error(self):
        offset = golden_gamma_offset_interval(256, 32)
        self.assertGreater(offset.lower, Q(4, 100))
        self.assertLess(offset.upper, Q(42, 1000))
        # No privileged constant occurs in the formal cancellation identity.
        for reference in (Q(0), Q(1, 2), Q(7, 11), Q(-3)):
            for gamma in (Q(1, 3), Q(5, 7)):
                approximant = gamma+Q(1, 99)
                self.assertEqual((reference-gamma)-(reference-approximant), Q(1, 99))

    def test_upper_bridge_identity_independent_four_pole_source_and_mutation(self):
        self.assertTrue(all(c > 0 for c in UPPER_BRIDGE_SHIFTED_COEFFICIENTS))
        for n in (1, 2, 3, 7, 31, 97, 257, 4099, 65521):
            proof = upper_bridge_polynomial_certificate(n)
            direct = Q(4, 8*n+1)-Q(2, 8*n+4)-Q(1, 8*n+5)-Q(1, 8*n+6)
            self.assertEqual(direct, exact_forcing(n+1))
            expected = euler_remainder_interval(n).lower**2/16-direct/15
            self.assertEqual(proof["positive_gap"], expected)
            self.assertGreater(expected, 0)
            # A dropped pole fails the exact source certificate.
            mutant = direct+Q(1, 8*n+6)
            self.assertNotEqual(euler_remainder_interval(n).lower**2/16-mutant/15,
                                proof["positive_gap"])

    def test_bbp_tail_against_independent_longer_green_prefix(self):
        for n in (1, 2, 7, 31, 97, 257, 4099):
            cert = bbp_euler_tail_bridge(n, 12)
            independent = sum((exact_forcing(n+j)/16**j for j in range(1, 31)), Q())
            remaining = exact_forcing(n+31)/Q(15*16**30)
            self.assertLess(cert.green_tail.lower, independent)
            self.assertLess(independent+remaining, cert.green_tail.upper)
            self.assertGreater(cert.normalized_ratio.lower, 0)
            self.assertLess(cert.normalized_ratio.upper, 1)
            self.assertGreater(cert.analytic_tail_lower, Q(1, 64*(n+1)**2))

    def test_asymptotic_coefficients_from_independent_source_moments(self):
        c = bbp_euler_asymptotic_coefficients()
        source = tuple(Q(4*7**k-2*4**k-3**k-2**k, 8**(k+1)) for k in (1, 2, 3))
        geom = (Q(1, 15), Q(16, 225), Q(272, 3375))
        tail = (source[0]*geom[0], source[1]*geom[0]-2*source[0]*geom[1],
                source[2]*geom[0]-3*source[1]*geom[1]+3*source[0]*geom[2])
        self.assertEqual(c["green_tail"], tail)
        self.assertEqual(c["euler_square_minus_tail_leading"], Q(-1, 192)-tail[1])
        self.assertEqual(c["normalized_ratio"][1], 64*tail[1]+Q(1, 3))
        self.assertEqual(c["normalized_ratio"][2], 64*tail[2]+64*tail[1]/3+Q(1, 12))

    def test_domain_and_precision_gates(self):
        for call in (
            lambda: finite_beta_moment(True, 2), lambda: finite_beta_moment(0, 2),
            lambda: finite_beta_moment(2, -1), lambda: finite_beta_survival(3, Q(4)),
            lambda: finite_beta_mellin_successor(3, -1),
            lambda: finite_beta_mellin_successor(3, 0.5),
            lambda: finite_beta_laplace_interval(3, -1),
            lambda: finite_beta_fixed_point_interval(8, bits=32, terms=0),
            lambda: golden_laplace_fixed_point_interval(0),
            lambda: bbp_euler_tail_bridge(0), lambda: bbp_euler_tail_bridge(3, -1),
        ):
            with self.assertRaises(ValueError):
                call()


if __name__ == "__main__":
    unittest.main()
