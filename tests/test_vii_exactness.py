"""Academic Main VII exact negative controls; finite checks are not formal proofs."""
from fractions import Fraction
from math import isqrt, prod
import unittest

import sympy as sp

from observational_succ import abc_decomposition as abc
from observational_succ import cloud_schur_certificates as cloud
from observational_succ import goldbach_circle as gold
from observational_succ import quantitative_rigidity as qr
from observational_succ import residue_box_counting as crt
from observational_succ.cloud_crt_ascent import triangle_count, triangle_enclosure


class ExactSpectrumControls(unittest.TestCase):
    def test_collapsed_float_ordering_is_not_authority(self):
        for height in (10**30, 10**100):
            for gap in (sp.Integer(1), sp.Rational(1, 10**80)):
                M = sp.Matrix([[height + 2*gap, gap], [gap, height + 2*gap]])
                least = qr.min_eigenvalue_exact(M)
                self.assertEqual(least, height + gap)
                self.assertTrue(qr.is_positive_semidefinite(M - least * sp.eye(2)))
                self.assertEqual((M - least * sp.eye(2)) * sp.Matrix([1, -1]), sp.zeros(2, 1))

    def test_irrational_roots_are_exactly_isolated(self):
        M = sp.Matrix([[1, 1], [1, 2]])
        least = qr.min_eigenvalue_exact(M)
        self.assertEqual(least, sp.CRootOf(sp.Symbol('x')**2 - 3*sp.Symbol('x') + 1, 0))
        self.assertGreater(least, sp.Rational(3, 8))
        self.assertLess(least, sp.Rational(2, 5))
        self.assertEqual(qr.min_eigenvalue_exact(sp.Matrix([[2, 3], [-1, 2]])), 1)

    def test_explicit_rational_square_domain(self):
        for M in (sp.zeros(0), sp.Matrix([[1, 2]]), sp.Matrix([[sp.sqrt(2)]]),
                  sp.Matrix([[sp.Symbol('x')]]), sp.Matrix([[sp.I]]), [[1.0]]):
            with self.subTest(M=M), self.assertRaises(qr.RigidityInputError):
                qr.min_eigenvalue_exact(M)

    def test_numerically_guided_margin_is_independently_checked(self):
        M = sp.Matrix([[5, 2], [2, 2]])
        margin = qr.certified_pd_margin(M)
        self.assertGreater(margin, 0)
        self.assertTrue(qr.is_positive_definite(M - margin * sp.eye(2)))


class PrimeCutoffControls(unittest.TestCase):
    def test_all_certified_paths_reject_noninteger_cutoffs_before_parity(self):
        functions = (gold.singular_series_truncated, gold.singular_series_enclosure,
                     gold.singular_series_via_transport, gold.singular_series_transport_enclosure)
        for fn in functions:
            for N in (1, 2, 3, 8):
                for cutoff in (True, False, 2.0, 3.0, Fraction(5, 2), Fraction(3), -1, 0, 1):
                    with self.subTest(fn=fn.__name__, N=N, cutoff=cutoff):
                        with self.assertRaises(gold.GoldbachCircleError):
                            fn(N, cutoff)
        for cutoff in (True, 3.0, Fraction(3), Fraction(7, 2), 2):
            with self.assertRaises(gold.GoldbachCircleError):
                gold.twin_prime_constant_enclosure(cutoff)
        with self.assertRaises(gold.GoldbachCircleError):
            gold._primes_upto(Fraction(5, 2))

    def test_two_is_a_valid_prime_cutoff_not_a_silent_three(self):
        for N in (2, 4, 8, 16):
            self.assertEqual(gold.singular_series_truncated(N, 2), 2)
            self.assertEqual(gold.singular_series_via_transport(N, 2), 2)
            self.assertEqual(gold.singular_series_enclosure(N, 2), (0, 2))
            self.assertEqual(gold.singular_series_transport_enclosure(N, 2), (0, 2))
            self.assertEqual(gold.odd_prime_transport_factor(N), 1)

    def test_finite_products_and_enclosures_agree(self):
        for N, cutoffs in ((2, (2, 3, 5, 11)), (30, (5, 7, 13)), (154, (11, 17))):
            for P in cutoffs:
                self.assertEqual(gold.singular_series_truncated(N, P), gold.singular_series_via_transport(N, P))
                self.assertEqual(gold.singular_series_enclosure(N, P), gold.singular_series_transport_enclosure(N, P))
        self.assertEqual(gold.singular_series_local_factor(5, 10) / gold.singular_series_local_factor(5, 2), Fraction(4, 3))


class LayerAndCRTControls(unittest.TestCase):
    def test_layer_tail_is_not_the_small_bblt_remainder(self):
        result = abc.truncate_exponent_layers(256, 4)
        self.assertEqual(result['n0'], 256)
        self.assertGreater(result['n0'], 4)
        self.assertEqual(abc.bblt_anatomy(256, 4), result)
        for n in (1, 360, 2**31 * 3**5 * 7, 2**97):
            for d in (1, 4, 32, 100):
                result = abc.truncate_exponent_layers(n, d)
                self.assertEqual(result['n0'] * prod(m**j for j, m in result['truncated_layers']), n)
                self.assertEqual(result['n0'] == 1, abc.max_exponent(n) <= d)

    def test_sharp_bound_and_floor_count_match_cloud(self):
        for W in range(1, 8):
            for R in (set(), {(0, 0)}, {(1 % W, 1 % W)}, crt.coprime_sum_residues(W)):
                for X in (0, 1, 2, W, 3*W, 4*W, 11*W):
                    radius = crt.error_bound(X, W, R)
                    self.assertEqual(radius, len(R) * (Fraction(3*X, 2*W) + 1))
                    self.assertLessEqual(radius, crt.legacy_error_bound(X, W, R))
                    count = crt.residue_box_count(X, W, R)
                    self.assertEqual(count, triangle_count(X, W, R))
                    self.assertEqual(count, crt.residue_box_count_floorsum(X, W, R))
                    self.assertTrue(triangle_enclosure(X, W, R).contains(count))
                    self.assertLessEqual(abs(count - crt.main_term(X, W, R)), radius)

    def test_sharp_dominance_threshold_is_exact(self):
        for W in range(1, 101):
            R = {(0, 0)}
            threshold = crt.growth_regime(W, W, R).dominance_threshold_X
            self.assertEqual(threshold, (3*W + isqrt(17*W*W)) // 2 + 1)
            self.assertTrue(crt.growth_regime(threshold, W, R).main_dominates)
            self.assertFalse(crt.growth_regime(threshold-1, W, R).main_dominates)
            self.assertFalse(crt.growth_regime(3*W, W, R).main_dominates)
            self.assertTrue(crt.growth_regime(4*W, W, R).main_dominates)

    def test_crt_domain_excludes_negative_and_coerced_inputs(self):
        for X in (-1, True, 1.0, Fraction(1)):
            with self.assertRaises(crt.ResidueBoxError):
                crt.error_bound(X, 1, {(0, 0)})
        for W in (0, True, 1.0, Fraction(1)):
            with self.assertRaises(crt.ResidueBoxError):
                crt.coprime_pair_residues(W)
        with self.assertRaises(crt.ResidueBoxError):
            crt.error_bound(1, 2, {(True, 0)})


class IndependentCertificateControls(unittest.TestCase):
    def test_extreme_rational_congruence_families(self):
        # Known inertia is a third control: invertible exact congruence preserves
        # the signs of these explicit diagonal forms. The two implementations
        # share classical elimination mathematics, not independent proof kernels.
        checked = 0
        for H, epsilon in ((10**30 + 7, sp.Rational(1, 10**80)), (101, sp.Rational(1, 10**12))):
            U = sp.Matrix([[1, H, sp.Rational(1, 7)], [0, 1, -H], [0, 0, 1]])
            self.assertEqual(U.det(), 1)
            for diagonal in ((epsilon, 1, H), (0, 0, 1), (1, 0, 0), (1, -epsilon, 0), (-epsilon, 1, H)):
                M = U.T * sp.diag(*diagonal) * U
                expected_psd = all(value >= 0 for value in diagonal)
                for order in ((0, 1, 2), (2, 0, 1)):
                    matrix = M.extract(order, order)
                    rational = tuple(tuple(Fraction(int(x.p), int(x.q)) for x in row) for row in matrix.tolist())
                    certificate = cloud.certify(rational)
                    self.assertTrue(cloud.verify_certificate(rational, certificate))
                    self.assertEqual(type(certificate) is cloud.RationalGram, expected_psd)
                    self.assertEqual(qr.is_positive_semidefinite(matrix), expected_psd)
                    witness = qr.negative_witness(matrix)
                    if expected_psd:
                        self.assertIsNone(witness)
                    else:
                        self.assertLess((witness.T * matrix * witness)[0], 0)
                        self.assertLess(cloud.quadratic_value(rational, certificate.vector), 0)
                    checked += 1
        # Zero diagonal/nonzero coupling is a separate non-PSD branch.
        rational = ((0, Fraction(1, 10**70)), (Fraction(1, 10**70), 10**80))
        self.assertIsInstance(cloud.certify(rational), cloud.NegativeWitness)
        M = sp.Matrix(rational)
        witness = qr.negative_witness(M)
        self.assertLess((witness.T * M * witness)[0], 0)
        self.assertEqual(checked, 20)


if __name__ == '__main__':
    unittest.main()
