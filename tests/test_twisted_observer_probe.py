"""Exact source/branch/gain controls for twisted observer agreement."""

from fractions import Fraction as Q
from math import gcd
import unittest

from observational_succ.bbp_cyclotomic_birth import source_window_split
from observational_succ.twisted_observer_probe import (
    authentic_odd_complement_window, bbp_odd_forcing, bbp_odd_states,
    circle_distance, doubling_inverse_certificate, gain23_certificate,
    gain_observability, odd_doubling_instability, signed_projection_certificate,
    twisted_pair_gaussian, two_branch_distance,
)


def direct_circle_distance(x):
    """Independent nearest-integer implementation, not residue/min."""
    floor = x.numerator // x.denominator
    return min(abs(x - floor), abs(x - floor - 1))


def direct_four_pole(n):
    return (Q(4, 8*n-7) - Q(2, 8*n-4)
            - Q(1, 8*n-3) - Q(1, 8*n-2))


def multiply(x, y):
    """Independent exact Gaussian arithmetic for test oracles."""
    return (x[0]*y[0]-x[1]*y[1], x[0]*y[1]+x[1]*y[0])


class AuthenticOddSource(unittest.TestCase):
    def test_regrouping_matches_literal_four_poles(self):
        for n in range(1, 301):
            expected = direct_four_pole(n)
            self.assertEqual(bbp_odd_forcing(n), expected)
            self.assertEqual(expected.denominator % 2, 1)
        self.assertEqual(bbp_odd_forcing(1), Q(47, 15))

    def test_states_match_unwrapped_source_sum(self):
        # Reconstruct independently from the explicit unwrapped finite sum.
        states = bbp_odd_states(28)
        self.assertEqual(states[0], 0)
        for n, state in enumerate(states):
            expected = sum((16**(n-j)*direct_four_pole(j)
                            for j in range(1, n+1)), Q()) % 1
            self.assertEqual(state, expected)
            self.assertEqual(state.denominator % 2, 1)

    def test_original_window_and_odd_form_are_independent_matches(self):
        for p in (17, 41, 73, 97, 113):
            actual = authentic_odd_complement_window(p)
            expected = tuple(w for _, w in source_window_split(p))
            self.assertEqual(actual, expected)
            self.assertTrue(all(w.denominator % 2 for w in actual))
            self.assertTrue(all(gcd(w.denominator, p) == 1 for w in actual))

    def test_authentic_small_difference_can_hide_near_half_turn(self):
        for p, t in ((41, 13), (73, 15)):
            w = authentic_odd_complement_window(p)[t]
            result = doubling_inverse_certificate(w)
            self.assertGreater(result["residual_distance"], Q(12, 25))
            self.assertLess(result["doubled_distance"], Q(1, 40))
            self.assertFalse(result["exact_agreement"])
            self.assertEqual(2*result["nearest_branch_distance"],
                             result["doubled_distance"])

    def test_zero_complement_cannot_persist_under_authentic_forcing(self):
        for n in range(3, 60):
            r = direct_four_pole(n)
            self.assertTrue(0 < r < Q(1, 4))
            # If w was zero, successor residual is precisely r modulo one.
            self.assertGreater(circle_distance(2*r), 0)


class DifferentialBranchControls(unittest.TestCase):
    def test_two_branch_identity_with_wrap_and_negative_inputs(self):
        for denominator in range(1, 36):
            for numerator in range(-denominator, 2*denominator+1):
                w = Q(numerator, denominator)
                expected = min(direct_circle_distance(w),
                               direct_circle_distance(w-Q(1, 2)))
                self.assertEqual(two_branch_distance(w), expected)
                self.assertEqual(2*expected, direct_circle_distance(2*w))

    def test_sharp_inverse_bound_on_all_small_odd_torsion(self):
        for q in range(1, 64, 2):
            worst = Q()
            for k in range(q):
                cert = doubling_inverse_certificate(Q(k, q), q)
                self.assertLessEqual(cert["residual_distance"],
                                     cert["residual_upper"])
                self.assertEqual(cert["exact_agreement"], cert["exact_zero"])
                if k:
                    worst = max(worst, cert["residual_distance"] /
                                cert["doubled_distance"])
            if q > 1:
                self.assertEqual(worst, Q(q-1, 2))

    def test_gain_two_has_no_denominator_uniform_inverse(self):
        # For every proposed bounded constant C, a finite exact witness defeats it.
        for constant in (1, 2, 10, 100, 1000):
            q = 2*constant+3
            witness = odd_doubling_instability(q)
            self.assertEqual(witness["doubled_distance"], Q(1, q))
            self.assertGreater(witness["residual_distance"],
                               constant*witness["doubled_distance"])
            self.assertEqual(witness["residual_upper"],
                             witness["residual_distance"])

    def test_half_turn_agrees_but_is_outside_odd_source_type(self):
        common = (Q(3, 5), Q(4, 5))
        cert = twisted_pair_gaussian(common, (-1, 0))
        self.assertEqual(cert["plus"], cert["minus"])
        self.assertEqual(cert["agreement_squared"], 0)
        self.assertEqual(cert["residual_squared"], 4)
        with self.assertRaises(ValueError):
            doubling_inverse_certificate(Q(1, 2))

    def test_explicit_odd_modulus_must_annihilate_phase(self):
        self.assertEqual(doubling_inverse_certificate(Q(2, 3), 9)["modulus"], 9)
        for q in (2, 5, 10):
            with self.assertRaises(ValueError):
                doubling_inverse_certificate(Q(2, 3), q)


class CoprimeGainCertificates(unittest.TestCase):
    def test_exact_injectivity_and_stability_are_different(self):
        expected = {
            (2,): (True, False),
            (4, 8): (True, False),
            (6, 12): (False, False),
            (2, 3): (True, True),
            (-5, 8, 0): (True, True),
            (9, 15): (False, False),
        }
        for gains, (injective, stable) in expected.items():
            cert = gain_observability(gains)
            self.assertEqual(cert["odd_torsion_injective"], injective)
            self.assertEqual(cert["uniformly_stable"], stable)
            self.assertEqual(sum(a*k for a, k in
                                 zip(cert["bezout_coefficients"], gains)),
                             cert["gcd"])
            self.assertEqual(cert["circle_injective"], stable)

    def test_general_bezout_certificate_against_exact_gaussian_powers(self):
        phase = (Q(3, 5), Q(4, 5))
        target = (phase[0]-1)**2 + phase[1]**2
        for gains in ((2, 3), (-5, 8), (6, 10, 15), (0, -7, 11)):
            cert = gain_observability(gains)
            energy = Q()
            for k in gains:
                factor = phase if k >= 0 else (phase[0], -phase[1])
                power = (Q(1), Q())
                for _ in range(abs(k)):
                    power = multiply(power, factor)
                energy += (power[0]-1)**2 + power[1]**2
            self.assertLessEqual(target, cert["bezout_norm_constant"]*energy)

    def test_sharp_gain23_certificate_and_mutated_constant(self):
        # cos(theta)=-3/4 is an exact algebraic unit, sin^2(theta)=7/16.
        sharp = gain23_certificate(Q(-3, 4))
        self.assertEqual(sharp["residual_squared"], Q(7, 2))
        self.assertEqual(sharp["gain2_squared"]+sharp["gain3_squared"], Q(21, 8))
        self.assertEqual(sharp["slack"], 0)
        for bad_constant in (Q(1), Q(5, 4), Q(133, 100)):
            self.assertGreater(sharp["residual_squared"], bad_constant *
                               (sharp["gain2_squared"]+sharp["gain3_squared"]))

    def test_gain23_polynomial_is_verified_on_full_rational_grid(self):
        for denominator in range(1, 46):
            for numerator in range(-denominator, denominator+1):
                c = Q(numerator, denominator)
                cert = gain23_certificate(c)
                self.assertEqual(cert["factor"], 3+6*c+4*c*c)
                self.assertGreaterEqual(cert["slack"], 0)
                self.assertGreaterEqual(cert["factor"], Q(3, 4))

    def test_exact_gaussian_pair_and_swap_orientation(self):
        u, v = (Q(3, 5), Q(4, 5)), (Q(5, 13), Q(12, 13))
        cert = twisted_pair_gaussian(u, v)
        swap = twisted_pair_gaussian(u, (v[0], -v[1]))
        self.assertEqual(cert["plus"], swap["minus"])
        self.assertEqual(cert["minus"], swap["plus"])
        self.assertEqual(cert["common_product"], multiply(u, u))
        self.assertEqual(cert["differential_product"], multiply(v, v))
        self.assertEqual(cert["agreement_squared"], swap["agreement_squared"])
        polynomial = gain23_certificate(v[0])
        self.assertEqual(cert["agreement_squared"], polynomial["gain2_squared"])


class SignedProjectionControls(unittest.TestCase):
    def test_same_shared_mean_allows_maximal_hidden_correlation(self):
        # Both observer-visible means vanish, while hidden correlation is one.
        for phase, expected in (((1, 0), (Q(1), Q())),
                                ((-1, 0), (Q(-1), Q())),
                                ((0, 1), (Q(), Q(1)))):
            left = [(1, 0), (-1, 0)]
            right = [phase, (-phase[0], -phase[1])]
            cert = signed_projection_certificate(left, right, 1)
            self.assertEqual(cert["left_projected"], ((Q(), Q()),)*2)
            self.assertEqual(cert["right_projected"], ((Q(), Q()),)*2)
            self.assertEqual(cert["high"], expected)
            self.assertEqual(cert["high_squared"], 1)
            self.assertEqual(cert["high_squared_upper"], 1)

    def test_split_matches_independent_raw_bilinear_sum(self):
        a = [(Q(t-2, 3), Q(t*t-1, 7)) for t in range(12)]
        b = [(Q(3-t, 5), Q((-1)**t, 2)) for t in range(12)]
        raw = [multiply(x, y) for x, y in zip(a, b)]
        expected = (sum(z[0] for z in raw)/12, sum(z[1] for z in raw)/12)
        for period in (1, 2, 3, 4, 6, 12):
            cert = signed_projection_certificate(a, b, period)
            self.assertEqual(cert["total"], expected)
            self.assertEqual(cert["low_high"], (Q(), Q()))
            self.assertEqual(cert["high_low"], (Q(), Q()))
            self.assertEqual(tuple(x+y for x, y in zip(cert["low"], cert["high"])),
                             expected)

    def test_declared_bilinear_sign_is_not_hermitian(self):
        values = [(0, 1), (0, -1)]
        cert = signed_projection_certificate(values, values, 1)
        self.assertEqual(cert["high"], (-1, 0))
        self.assertEqual(cert["left_variance"], 1)


class StrictInputs(unittest.TestCase):
    def test_rational_functions_reject_float_bool_and_strings(self):
        for bad in (True, False, .5, "1/2", complex(1)):
            for function in (circle_distance, two_branch_distance,
                             doubling_inverse_certificate, gain23_certificate):
                with self.assertRaises(ValueError):
                    function(bad)

    def test_source_and_torsion_domain_guards(self):
        for bad in (True, 3.0, "3", -1):
            for function in (bbp_odd_forcing, bbp_odd_states,
                             odd_doubling_instability):
                with self.assertRaises(ValueError):
                    function(bad)
        with self.assertRaises(ValueError):
            bbp_odd_forcing(0)
        for bad in (2, 4, 21, 25, True, 17.0):
            with self.assertRaises(ValueError):
                authentic_odd_complement_window(bad)
        for bad in (0, 1, 2, 4):
            with self.assertRaises(ValueError):
                odd_doubling_instability(bad)

    def test_gain_and_gaussian_guards(self):
        for bad in ((), [], (0, 0), (True, 3), (2.0, 3), "23", {2, 3}):
            with self.assertRaises(ValueError):
                gain_observability(bad)
        for bad in ((1.0, 0), (True, 0), (1, 1), [1, 0], (1,), "1"):
            with self.assertRaises(ValueError):
                twisted_pair_gaussian((1, 0), bad)
        for bad in (Q(-2), Q(2)):
            with self.assertRaises(ValueError):
                gain23_certificate(bad)

    def test_projection_shape_and_period_guards(self):
        for a, b, d in (([], [], 1), ([(1, 0)], [], 1),
                        ([(1, 0)], [(1, 0)], True),
                        ([(1, 0)], [(1, 0)], 2),
                        ([(1.0, 0)], [(1, 0)], 1)):
            with self.assertRaises(ValueError):
                signed_projection_certificate(a, b, d)


if __name__ == "__main__":
    unittest.main()
