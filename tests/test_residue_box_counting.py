"""Exact tests for residue-constrained integer-box counting (Proof Forge III, Part IV).

Covers: exact finite counting, the lattice-point formula validated against a
brute-force oracle, an independent floor-sum derivation, the explicit error
constant, boundary terms, mutation/invalid-input controls, the |R|/W^2 density,
and the growing-modulus failure boundary (X > 10 W)."""
import random
import unittest
from fractions import Fraction
from math import gcd

from observational_succ.residue_box_counting import (
    ResidueBoxError,
    coprime_pair_residues,
    coprime_sum_residues,
    error_bound,
    error_exact,
    growth_regime,
    local_density,
    main_term,
    residue_box_certificate,
    residue_box_count,
    residue_box_count_bruteforce,
    residue_box_count_floorsum,
    residues_from_predicate,
)


def _phi(W):
    return sum(1 for k in range(W) if gcd(k, W) == 1)


def _rand_R(W, rng):
    return frozenset((r, s) for r in range(W) for s in range(W)
                     if rng.random() < 0.5)


class TestThreeRoutesAgree(unittest.TestCase):
    def test_corpus_all_routes_agree(self):
        rng = random.Random(20261020)
        for _ in range(250):
            W = rng.randint(1, 6)
            X = rng.randint(1, 40)
            R = _rand_R(W, rng)
            c2d = residue_box_count(X, W, R)
            cfs = residue_box_count_floorsum(X, W, R)
            cbf = residue_box_count_bruteforce(X, W, R)
            self.assertEqual(c2d, cfs, f"2d!=floorsum at X={X},W={W},R={R}")
            self.assertEqual(c2d, cbf, f"2d!=brute at X={X},W={W},R={R}")

    def test_full_residue_set_is_triangular_number(self):
        # R = everything -> N = #{a,b>=1, a+b<=X} = sum_{a=1}^{X-1}(X-a) = (X-1)X/2
        for X in (2, 3, 10, 25):
            for W in (1, 3, 4):
                R = frozenset((r, s) for r in range(W) for s in range(W))
                self.assertEqual(residue_box_count(X, W, R),
                                 (X - 1) * X // 2)


class TestErrorBound(unittest.TestCase):
    def test_bound_holds_on_corpus(self):
        rng = random.Random(7)
        for _ in range(250):
            W = rng.randint(1, 7)
            X = rng.randint(1, 60)
            R = _rand_R(W, rng)
            cert = residue_box_certificate(X, W, R)
            self.assertTrue(cert.routes_agree)
            self.assertTrue(cert.bound_holds,
                            f"bound violated: {cert.as_record()}")

    def test_bound_holds_large_X_no_bruteforce(self):
        X, W = 10 ** 6, 210
        R = coprime_sum_residues(W)
        cert = residue_box_certificate(X, W, R, check_bruteforce=False)
        self.assertTrue(cert.bound_holds)
        # the relative error is tiny here (W << X): |error| << main term
        self.assertLess(abs(cert.error_exact) * 100, cert.main_term)

    def test_bound_is_exactly_five_R_times(self):
        X, W, R = 50, 4, frozenset({(1, 1), (2, 3)})
        self.assertEqual(error_bound(X, W, R),
                         Fraction(5 * 2 * (X + W), W))

    def test_worst_case_single_row_bound_holds(self):
        # lumpy R concentrated in one row: still within the proved bound.
        W = 5
        R = frozenset((2, s) for s in range(W))   # a == 2 mod 5, b anything
        for X in (10, 37, 100, 1000):
            cert = residue_box_certificate(X, W, R, check_bruteforce=(X <= 100))
            self.assertTrue(cert.bound_holds)


class TestDensityAndWDependence(unittest.TestCase):
    def test_local_density_is_R_over_W_squared(self):
        for W in (1, 2, 5, 6):
            R = coprime_pair_residues(W)
            self.assertEqual(local_density(W, R), Fraction(len(R), W * W))

    def test_coprime_pair_density(self):
        for W in (2, 3, 6, 12, 30):
            R = coprime_pair_residues(W)
            self.assertEqual(len(R), _phi(W) ** 2)
            self.assertEqual(local_density(W, R), Fraction(_phi(W), W) ** 2)

    def test_coprime_sum_density(self):
        for W in (2, 3, 5, 6, 12):
            R = coprime_sum_residues(W)
            self.assertEqual(len(R), W * _phi(W))       # phi(W) admissible s per r
            self.assertEqual(local_density(W, R), Fraction(_phi(W), W))

    def test_main_term_tracks_density(self):
        X, W = 1000, 30
        R = coprime_sum_residues(W)
        self.assertEqual(main_term(X, W, R),
                         Fraction(len(R), W * W) * Fraction(X * X, 2))


class TestBoundaryTerms(unittest.TestCase):
    def test_X_one_is_empty(self):
        self.assertEqual(residue_box_count(1, 1, {(0, 0)}), 0)

    def test_X_two_single_point(self):
        self.assertEqual(residue_box_count(2, 1, {(0, 0)}), 1)   # only (1,1)

    def test_X_below_min_class_sum_is_zero(self):
        # R = {(2,3)} mod 5 -> smallest a+b is 2+3=5; X=4 -> 0, X=5 -> 1
        self.assertEqual(residue_box_count(4, 5, {(2, 3)}), 0)
        self.assertEqual(residue_box_count(5, 5, {(2, 3)}), 1)

    def test_class_zero_representative(self):
        # residue 0 mod 4 has representative 4; smallest a=4,b=4 -> a+b=8
        self.assertEqual(residue_box_count(7, 4, {(0, 0)}), 0)
        self.assertEqual(residue_box_count(8, 4, {(0, 0)}), 1)


class TestMutationAndInvalidInputs(unittest.TestCase):
    def test_invalid_residue_class_rejected(self):
        with self.assertRaises(ResidueBoxError):
            residue_box_count(10, 4, {(4, 0)})     # 4 not in Z/4Z
        with self.assertRaises(ResidueBoxError):
            residue_box_count(10, 4, {(-1, 0)})

    def test_invalid_modulus_rejected(self):
        with self.assertRaises(ResidueBoxError):
            residue_box_count(10, 0, {(0, 0)})
        with self.assertRaises(ResidueBoxError):
            residue_box_count(10, -3, {(0, 0)})

    def test_non_integer_X_rejected(self):
        with self.assertRaises(ResidueBoxError):
            residue_box_count(10.5, 4, {(0, 0)})

    def test_additive_over_disjoint_R(self):
        rng = random.Random(99)
        W, X = 5, 30
        for _ in range(40):
            R1 = _rand_R(W, rng)
            R2 = frozenset((r, s) for r in range(W) for s in range(W)) - R1
            self.assertEqual(
                residue_box_count(X, W, R1 | R2),
                residue_box_count(X, W, R1) + residue_box_count(X, W, R2))

    def test_single_pair_mutation(self):
        # removing one allowed pair drops the count by exactly that class's count
        W, X = 4, 50
        R = frozenset((r, s) for r in range(W) for s in range(W))
        pair = (1, 2)
        Rminus = R - {pair}
        delta = residue_box_count(X, W, R) - residue_box_count(X, W, Rminus)
        self.assertEqual(delta, residue_box_count(X, W, {pair}))


class TestGrowingModulus(unittest.TestCase):
    def test_dominance_threshold_is_ten_W(self):
        W = 7
        R = coprime_sum_residues(W)
        below = growth_regime(5 * W, W, R)       # X = 35 < 10W = 70
        above = growth_regime(20 * W, W, R)      # X = 140 > 70
        self.assertFalse(below.main_dominates)
        self.assertTrue(above.main_dominates)
        self.assertEqual(above.dominance_threshold_X, 10 * W + 1)

    def test_degeneration_at_W_comparable_to_X(self):
        # W ~ X: error bound is at least the main term -> asymptotic is vacuous.
        X = 100
        W = 100
        R = coprime_sum_residues(W)
        reg = growth_regime(X, W, R)
        self.assertFalse(reg.main_dominates)
        self.assertGreaterEqual(reg.error_bound, reg.main_term)


class TestResiduePredicateBuilder(unittest.TestCase):
    def test_predicate_builds_expected_set(self):
        W = 6
        R = residues_from_predicate(W, lambda r, s: (r + s) % W == 0)
        # exactly one s per r makes r+s = 0 mod W
        self.assertEqual(len(R), W)
        self.assertEqual(R, coprime_sum_residues(W) & R | R)  # idempotent sanity


if __name__ == "__main__":
    unittest.main()
