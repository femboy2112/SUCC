"""Exact tests for the source-defect detectability-horizon theorem.

Every assertion is an exact-rational check against the summation identity
F(k) = sum_{m<=k} sum_{d|m} b(d); no floating-point certificate is used.
"""
import unittest
from fractions import Fraction as Q

from observational_succ.zero_centered_residue import mobius
from observational_succ.source_detectability import (
    SourceDetectabilityError, defective_source, detectability_horizon,
    detected_at, first_deviation, interpolant, nonidentifiable_pair,
    open_world_family,
)


class TestInterpolantIdentity(unittest.TestCase):
    def test_true_source_interpolates_one(self):
        mu = mobius(20)
        b = {n: Q(mu[n]) for n in range(1, 21)}
        for k in range(1, 21):
            self.assertEqual(interpolant(k, b), Q(1))

    def test_interpolant_matches_floor_form(self):
        # F(k) = sum_n b(n) floor(k/n) == sum_{m<=k} sum_{d|m} b(d)
        mu = mobius(20)
        b = {n: Q(mu[n]) for n in range(1, 21)}
        for k in range(1, 21):
            floor_form = sum((b[n] * Q(k // n) for n in b), Q())
            self.assertEqual(interpolant(k, b), floor_form)


class TestDetectabilityHorizon(unittest.TestCase):
    def test_iff_horizon_ge_d(self):
        for d in (2, 3, 4, 5, 6, 7, 9, 12):
            for K in range(1, d + 4):
                self.assertEqual(detected_at(d, Q(-2), K), K >= d,
                                 f"d={d} K={K}")

    def test_first_visible_cell_is_d_with_exact_value(self):
        for d in (2, 4, 6, 9):
            for delta in (Q(-2), Q(1), Q(3, 2)):
                b = defective_source(d, delta, d + 3)
                # hidden on every cell below d
                for k in range(1, d):
                    self.assertEqual(interpolant(k, b), Q(1))
                # exact value at d
                self.assertEqual(interpolant(d, b), Q(1) + delta)
                # nothing visible before d, d is first
                self.assertEqual(first_deviation(d, delta, d + 3), d)
                self.assertIsNone(first_deviation(d, delta, d - 1))

    def test_fake_composite_six_reproduces(self):
        # mu(6) = +1; b(6) = -1 means delta = -2; F_6(6) = 1 + (-2) = -1
        self.assertEqual(mobius(6)[6], 1)
        r = detectability_horizon(6, Q(-2))
        self.assertEqual(r["detectability_horizon"], 6)
        self.assertEqual(r["first_visible_cell"], 6)
        self.assertEqual(Q(r["verified_value"]), Q(-1))
        self.assertTrue(r["exact_match"])
        self.assertTrue(r["hidden_before_horizon"])
        self.assertEqual(value_at_6(), Q(-1))

    def test_report_self_consistency(self):
        for d in (3, 5, 6, 8):
            r = detectability_horizon(d, Q(-1))
            self.assertEqual(r["detectability_horizon"], d)
            self.assertEqual(r["first_visible_cell"], d)
            self.assertEqual(Q(r["predicted_value"]), Q(r["verified_value"]))
            self.assertFalse(r["RH_proved"])


def value_at_6():
    """Independent inline recomputation of the ZCR-08 fake composite at 6."""
    b = defective_source(6, Q(-2), 8)
    return interpolant(6, b)


class TestNonidentifiability(unittest.TestCase):
    def test_pair_agrees_on_prefix_differs_after(self):
        for K in (1, 2, 5, 10, 37):
            r = nonidentifiable_pair(K)
            self.assertTrue(r["agree_on_1_to_K"])
            self.assertTrue(r["finite_observations_identical"])
            self.assertEqual(r["first_difference_at"], K + 1)
            self.assertEqual(r["horizon"], K)
            # explicit: true vs alt maps differ at K+1 only
            st = r["source_true"]
            sa = r["source_alt"]
            for n in range(1, K + 1):
                self.assertEqual(st[str(n)], sa[str(n)])
            self.assertNotEqual(st[str(K + 1)], sa[str(K + 1)])
            self.assertTrue(r["open_world_unidentifiable"])

    def test_open_world_family_pairwise_distinct(self):
        K = 6
        fam = open_world_family(K, delta=Q(1), count=6)
        mu = mobius(K + 6)
        # each member agrees with mu on 1..K
        for src in fam:
            for n in range(1, K + 1):
                self.assertEqual(src[n], Q(mu[n]))
        # pairwise distinct
        for i in range(len(fam)):
            for j in range(i + 1, len(fam)):
                self.assertNotEqual(fam[i], fam[j])

    def test_identical_observations_across_family(self):
        K = 5
        fam = open_world_family(K, delta=Q(-2), count=5)
        base_obs = [interpolant(k, fam[0]) for k in range(1, K + 1)]
        for src in fam[1:]:
            obs = [interpolant(k, src) for k in range(1, K + 1)]
            self.assertEqual(obs, base_obs)


class TestInputRejection(unittest.TestCase):
    def test_rejects_float_delta(self):
        for fn in (lambda: detectability_horizon(6, 0.5),
                   lambda: defective_source(6, 0.5, 8),
                   lambda: detected_at(6, 0.5, 8)):
            with self.assertRaises(SourceDetectabilityError):
                fn()

    def test_rejects_zero_and_empty(self):
        with self.assertRaises(SourceDetectabilityError):
            detectability_horizon(6, Q(0))  # zero change is not a defect
        with self.assertRaises(SourceDetectabilityError):
            interpolant(5, {})  # empty source
        with self.assertRaises(SourceDetectabilityError):
            nonidentifiable_pair(0)  # horizon must be >= 1
        with self.assertRaises(SourceDetectabilityError):
            defective_source(1, Q(1), 3)  # defect position must be >= 2

    def test_rejects_float_source_coefficients(self):
        with self.assertRaises(SourceDetectabilityError):
            interpolant(5, {1: 0.5, 2: Q(1)})


if __name__ == "__main__":
    unittest.main()
