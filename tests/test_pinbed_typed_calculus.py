"""Exact tests for the typed higher-dimensional pinbed calculus (Front C).

Every assertion is finite and exact (integers only, no floating point).
The tests establish:
  - curry/uncurry round-trip identity,
  - d independent commuting, separately-addressable successors,
  - the fiber-product universal property,
  - CRT (3,4) full recovery vs (16,16) alias,
  - the hostile controls: single clock does NOT span N^2, and (16,16)
    diagonal scan loses Fourier characters,
  - affine square relation V_p S = S^p V_p and interchange coherence.
"""
import unittest
from itertools import product

from observational_succ.pinbed_typed_calculus import (
    AffineSquare,
    Pinbed,
    PinbedError,
    Successor,
    affine_interchange,
    affine_squares_commute_over_pair,
    crt_combine,
    crt_full_recovery,
    crt_is_isomorphism,
    curry,
    curry_uncurry_roundtrip,
    diagonal_scan_coverage,
    fiber_product_universal,
    fourier_characters_lost,
    pairwise_coprime,
    single_clock_spans,
    successors_commute,
    uncurry,
    FiberProduct,
)


class PinbedCurryTests(unittest.TestCase):
    def test_roundtrip_identity(self):
        axes = (3, 4, 5)
        p = Pinbed.from_function(axes, lambda idx: tuple(idx))
        for split in (1, 2):
            self.assertTrue(curry_uncurry_roundtrip(p, split))
            q = uncurry(curry(p, split))
            self.assertEqual(q.axes, p.axes)
            for idx in product(*(range(a) for a in axes)):
                self.assertEqual(q[idx], p[idx])

    def test_curry_shapes(self):
        p = Pinbed.from_function((2, 3, 4), lambda idx: 0)
        c = curry(p, 1)
        self.assertEqual(c.axes, (2,))
        self.assertEqual(c[(0,)].axes, (3, 4))
        c2 = curry(p, 2)
        self.assertEqual(c2.axes, (2, 3))
        self.assertEqual(c2[(0, 0)].axes, (4,))

    def test_rejects_wrong_arity(self):
        p = Pinbed.from_function((2, 2), lambda idx: 0)
        with self.assertRaises(PinbedError):
            _ = p[(0, 0, 0)]
        with self.assertRaises(PinbedError):
            _ = p[(2, 0)]  # out of range


class SuccessorTests(unittest.TestCase):
    def test_independent_commute(self):
        axes = (5, 7, 11)
        S = [Successor(axes, i) for i in range(3)]
        for i in range(3):
            for j in range(3):
                self.assertTrue(successors_commute(S[i], S[j], axes))

    def test_separately_addressable(self):
        axes = (4, 6)
        S0 = Successor(axes, 0)
        S1 = Successor(axes, 1)
        # S0 only changes coordinate 0
        self.assertEqual(S0((1, 2)), (2, 2))
        self.assertEqual(S1((1, 2)), (1, 3))
        # wraparound
        self.assertEqual(S0((3, 2)), (0, 2))
        self.assertEqual(S1((1, 5)), (1, 0))

    def test_successors_together_span(self):
        axes = (3, 4)
        S0 = Successor(axes, 0)
        S1 = Successor(axes, 1)
        reached = set()
        cur = (0, 0)
        for _ in range(3 * 4):
            reached.add(cur)
            cur = S1(S0(cur))
        self.assertEqual(len(reached), 12)
        self.assertEqual(len(reached), 3 * 4)


class FiberProductTests(unittest.TestCase):
    def test_universal_property(self):
        fp = FiberProduct(4)
        # a source object: agreed pairs over the middle coordinate
        source = [((x, y), (y, z)) for x in range(4) for y in range(4) for z in range(4)]
        self.assertTrue(fiber_product_universal(fp, source))

    def test_glue_mismatch_rejected(self):
        fp = FiberProduct(4)
        with self.assertRaises(PinbedError):
            fp.glue((0, 1), (2, 3))

    def test_three_coordinate_bijection(self):
        fp = FiberProduct(4)
        triples = set()
        for x in range(4):
            for y in range(4):
                for z in range(4):
                    triples.add(fp.glue((x, y), (y, z)))
        self.assertEqual(len(triples), 4 ** 3)


class CRTTests(unittest.TestCase):
    def test_crt_combine_inverse(self):
        # (3,4) coprime: reconstruct and check residues
        for r in product(range(3), range(4)):
            x = crt_combine(r, (3, 4))
            self.assertEqual(x % 3, r[0])
            self.assertEqual(x % 4, r[1])

    def test_crt_full_recovery_3_4(self):
        self.assertTrue(pairwise_coprime((3, 4)))
        self.assertTrue(crt_is_isomorphism((3, 4)))
        self.assertTrue(crt_full_recovery((3, 4)))

    def test_crt_not_full_16_16(self):
        self.assertFalse(pairwise_coprime((16, 16)))
        self.assertFalse(crt_is_isomorphism((16, 16)))
        self.assertFalse(crt_full_recovery((16, 16)))


class HostileControlTests(unittest.TestCase):
    def test_single_clock_does_not_span_n2(self):
        # CW-14 refutation: a single diagonal clock m -> (m+1, m+1) on 16x16
        def diagonal(idx):
            return ((idx[0] + 1) % 16, (idx[1] + 1) % 16)
        full, size = single_clock_spans(diagonal, (16, 16))
        self.assertFalse(full)
        self.assertEqual(size, 16)  # only the diagonal

    def test_diagonal_scan_misses_240_of_256(self):
        covered, total, missed = diagonal_scan_coverage(16, 2)
        self.assertEqual(total, 256)
        self.assertEqual(covered, 16)
        self.assertEqual(missed, 240)

    def test_fourier_characters_lost(self):
        # (16,16): 256 characters, only 16 resolvable along the diagonal
        self.assertEqual(fourier_characters_lost(16, 2), 240)


class AffineSquareTests(unittest.TestCase):
    def test_relation(self):
        for p, n in ((2, 7), (3, 11), (5, 13), (3, 16), (2, 16)):
            self.assertTrue(AffineSquare(p, n).check_relation())

    def test_prime_pair_cube_commutes(self):
        self.assertTrue(affine_squares_commute_over_pair(2, 3, 35))
        self.assertTrue(affine_squares_commute_over_pair(3, 5, 91))

    def test_interchange(self):
        self.assertTrue(affine_interchange(2, 3, 35))
        self.assertTrue(affine_interchange(3, 5, 91))


if __name__ == "__main__":
    unittest.main()
